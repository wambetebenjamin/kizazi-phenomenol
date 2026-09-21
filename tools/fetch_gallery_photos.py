#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download the 42 "KIZAZI 2026" photos from Google Drive into img/gallery/.

Files are written as 01.jpg … 42.jpg, in exactly the order of `PHOTOS` in
tools/build_common.py (01.jpg == PHOTOS[0]).  Each file is fetched at w1600
(gallery / lightbox quality) and must be a real JPEG larger than 10 KB.

Fallback chain per photo (see README):
  1. https://drive.google.com/thumbnail?id=ID&sz=w1600
  2. https://lh3.googleusercontent.com/d/ID=w1600
  3. https://drive.google.com/uc?export=view&id=ID

Prerequisite: the Drive album is shared "Anyone with the link → Viewer".
The script probes PHOTOS[0] first and refuses to continue on HTTP 403/404 —
share the folder (and each file) instead of guessing.

Usage:
  python3 tools/fetch_gallery_photos.py           # refresh all 42 photos

Runs on stock Python 3 (stdlib only).  `.github/workflows/fetch-gallery-photos.yml`
runs this same script and commits img/gallery/ — handy where outbound internet
is restricted but GitHub Actions is available.
"""

import os
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_common import PHOTOS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "img", "gallery")

MIN_BYTES = 10 * 1024          # every photo must be a real JPEG > 10 KB
JPEG_MAGIC = b"\xff\xd8\xff"   # SOI marker
UA = {"User-Agent": "Mozilla/5.0 (compatible; kizazi-photo-fetch/1.0)"}
RETRIES_PER_URL = 2
PAUSE = 2.0                    # seconds between attempts


def url_candidates(file_id):
    return [
        "https://drive.google.com/thumbnail?id=%s&sz=w1600" % file_id,
        "https://lh3.googleusercontent.com/d/%s=w1600" % file_id,
        "https://drive.google.com/uc?export=view&id=%s" % file_id,
    ]


def http_status(url):
    """GET the URL; return (status_code, body_bytes).  Raises URLError on network failure."""
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, b""


def is_real_jpeg(data):
    return len(data) > MIN_BYTES and data.startswith(JPEG_MAGIC)


def fetch_photo(file_id, n):
    """Download one photo across the fallback chain; return bytes or raise RuntimeError."""
    last = ""
    for url in url_candidates(file_id):
        for attempt in range(1, RETRIES_PER_URL + 1):
            try:
                code, data = http_status(url)
            except Exception as e:  # noqa: BLE001 — network flake; try next
                last = "%s -> %s" % (url, e)
                print("    try %d %s -> error %s" % (attempt, url, e))
                time.sleep(PAUSE)
                continue
            if code == 200 and is_real_jpeg(data):
                print("    try %d %s -> ok (%d bytes)" % (attempt, url, len(data)))
                return data
            last = "%s -> HTTP %s (%d bytes)" % (url, code, len(data))
            print("    try %d %s -> HTTP %s (%d bytes)%s"
                  % (attempt, url, code, len(data),
                     "" if code not in (403, 404) else "  [not shared?]"))
            time.sleep(PAUSE)
    raise RuntimeError("photo %d (%s) failed on all URLs; last: %s" % (n, file_id, last))


def main():
    if len(PHOTOS) != 42:
        print("expected 42 photo IDs in PHOTOS, found %d" % len(PHOTOS))
        return 1

    # ---- Gate: probe one ID first. 403/404 => album not shared; STOP. --------
    probe_id = PHOTOS[0]
    probe_url = url_candidates(probe_id)[0]
    print("probing %s" % probe_url)
    try:
        code, data = http_status(probe_url)
    except Exception as e:  # noqa: BLE001
        print("probe failed with a network error (%s) — cannot tell whether the album is shared." % e)
        return 1
    if code in (403, 404):
        print("STOP: HTTP %d for %s" % (code, probe_url))
        print('The Drive album is NOT shared as "Anyone with the link \u2192 Viewer".')
        print("Share the 'KIZAZI 2026' folder (folder AND each file) in Google Drive,")
        print("then re-run this script. Nothing was written.")
        return 3
    if code == 200 and not is_real_jpeg(data):
        print("STOP: probe returned HTTP 200 but not a real JPEG > %d KB (got %d bytes)." % (MIN_BYTES // 1024, len(data)))
        print("The album is probably shared but the thumbnail endpoint is unhappy; try again later.")
        return 1
    if code != 200:
        print("STOP: probe returned HTTP %d (not 403/404, but not usable either)." % code)
        return 1
    print("probe ok (%d bytes) — album is reachable.\n" % len(data))

    # ---- Fetch all 42, in PHOTOS order -> 01.jpg … 42.jpg --------------------
    os.makedirs(OUT_DIR, exist_ok=True)
    total = 0
    failures = 0
    for n, file_id in enumerate(PHOTOS, 1):
        name = "%02d.jpg" % n
        path = os.path.join(OUT_DIR, name)
        print("[%s] %s" % (name, file_id))
        try:
            data = fetch_photo(file_id, n)
        except RuntimeError as e:
            print("  FAIL: %s" % e)
            failures += 1
            continue
        with open(path, "wb") as fh:
            fh.write(data)
        total += len(data)

    print("\ndone: %d/42 photos, %.1f MB total in %s" % (42 - failures, total / 1e6, OUT_DIR))
    if failures:
        print("FAILURES: %d photo(s) missing — fix and re-run." % failures)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
