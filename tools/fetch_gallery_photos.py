#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download the 42 "KIZAZI 2026" photos from Google Drive into img/gallery/.

Legacy path: the site's photos are now the curated, vendored set produced by
tools/vendor_gallery.py (img/gallery/SOURCES.json records the source of every
slot).  This script keeps working for --verify and --manifest-only, and its
Drive download refuses to run while SOURCES.json is present unless
--replace-curated is passed.

Files are written as 01.jpg … 42.jpg, in exactly the order of `PHOTOS` in
tools/build_common.py (01.jpg == PHOTOS[0]).  Each file is fetched at w1600
(gallery / lightbox quality) and must be a real JPEG larger than 10 KB.

The manifest (img/gallery/manifest.json)
----------------------------------------
Every run maintains `img/gallery/manifest.json`: for each photo the Drive
file ID, the SHA-256 hash of the committed bytes and the byte size, in
`PHOTOS` order.  Commit the JPEGs and the manifest together.

  * A plain re-run is manifest-aware: photos whose bytes already match the
    manifest are skipped, so an unchanged album produces a zero-diff run
    (nothing re-downloaded, nothing to commit).
  * `--force` re-downloads all 42 and compares against the manifest (used by
    the GitHub Actions workflow, where the checkout is already in sync and a
    normal run would detect no album changes).
  * `--changed-out FILE` writes the names of the photos whose bytes changed
    during the run (one per line, empty when nothing changed) for commit
    messages.
  * `--manifest-only` builds the manifest from the files already on disk
    (no network) for the browser-assisted route (tools/fetch_gallery_server.py).
  * `--verify` checks everything completely offline: 42 files named 01.jpg to
    42.jpg, each a real JPEG > 10 KB, hashes matching the manifest, and the
    manifest order matching `PHOTOS`.

Fallback chain per photo (see README):
  1. https://drive.google.com/thumbnail?id=ID&sz=w1600
  2. https://lh3.googleusercontent.com/d/ID=w1600
  3. https://drive.google.com/uc?export=view&id=ID

Prerequisite: the Drive album is shared "Anyone with the link → Viewer".
The script probes PHOTOS[0] first and refuses to continue on HTTP 403/404;
share the folder (and each file) instead of guessing.

Usage:
  python3 tools/fetch_gallery_photos.py                # refresh (manifest-aware)
  python3 tools/fetch_gallery_photos.py --force        # re-download all 42
  python3 tools/fetch_gallery_photos.py --changed-out changed.txt
  python3 tools/fetch_gallery_photos.py --manifest-only
  python3 tools/fetch_gallery_photos.py --verify

Runs on stock Python 3 (stdlib only).  `.github/workflows/fetch-gallery-photos.yml`
runs this same script on a weekly schedule and on demand, verifies, and
commits img/gallery/ only when something changed.
"""

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_common import PHOTOS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "img", "gallery")
# The vendored, curated set (see tools/vendor_gallery.py) records where each
# slot came from.  While that file is present, this Drive fetch refuses to
# overwrite the gallery unless --replace-curated says so on purpose.
SOURCES = os.path.join(OUT_DIR, "SOURCES.json")
MANIFEST = os.path.join(OUT_DIR, "manifest.json")

ALBUM = "KIZAZI 2026"
WIDTH = 1600
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
    return data is not None and len(data) > MIN_BYTES and data.startswith(JPEG_MAGIC)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def read_file(path):
    try:
        with open(path, "rb") as fh:
            return fh.read()
    except OSError:
        return None


def load_manifest():
    """Return the manifest's photo list (in PHOTOS order) or None."""
    raw = read_file(MANIFEST)
    if raw is None:
        return None
    try:
        doc = json.loads(raw.decode("utf-8"))
        photos = doc.get("photos")
    except (ValueError, UnicodeDecodeError, AttributeError):
        return None
    return photos if isinstance(photos, list) else None


def manifest_width():
    """The width recorded in the existing manifest, when it has one.

    The curated, vendored set (tools/vendor_gallery.py) tops out at the upload
    resolution (1000 px), so its manifest says 1000; keep that value when
    rebuilding the manifest from local files instead of stamping the Drive
    download width over it.
    """
    raw = read_file(MANIFEST)
    if raw is None:
        return None
    try:
        return json.loads(raw.decode("utf-8")).get("width")
    except (ValueError, UnicodeDecodeError):
        return None


def save_manifest(entries, width=None):
    """Write manifest.json atomically.  Return True when the file changed."""
    doc = {"album": ALBUM, "width": width or manifest_width() or WIDTH,
           "photos": entries}
    text = json.dumps(doc, indent=2) + "\n"
    old = read_file(MANIFEST)
    if old is not None and old.decode("utf-8") == text:
        return False
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = MANIFEST + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.replace(tmp, MANIFEST)
    return True


def fetch_photo(file_id, n):
    """Download one photo across the fallback chain; return bytes or raise RuntimeError."""
    last = ""
    for url in url_candidates(file_id):
        for attempt in range(1, RETRIES_PER_URL + 1):
            try:
                code, data = http_status(url)
            except Exception as e:  # noqa: BLE001 (network flake; try next)
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


def probe_album():
    """Gate: probe one ID first.  Returns 0 ok, 3 not shared, 1 other problem."""
    probe_id = PHOTOS[0]
    probe_url = url_candidates(probe_id)[0]
    print("probing %s" % probe_url)
    try:
        code, data = http_status(probe_url)
    except Exception as e:  # noqa: BLE001
        print("probe failed with a network error (%s); cannot tell whether the album is shared." % e)
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
    print("probe ok (%d bytes); album is reachable.\n" % len(data))
    return 0


def run_fetch(force, changed_out):
    if len(PHOTOS) != 42:
        print("expected 42 photo IDs in PHOTOS, found %d" % len(PHOTOS))
        return 1
    if probe_album() != 0:
        return 3

    existing = load_manifest()
    entries, changed = [], []
    downloaded = skipped = failures = 0
    total = 0
    for n, file_id in enumerate(PHOTOS, 1):
        name = "%02d.jpg" % n
        path = os.path.join(OUT_DIR, name)
        old = None
        if existing is not None and len(existing) == len(PHOTOS):
            old = existing[n - 1] if isinstance(existing[n - 1], dict) else None

        # Manifest-aware skip: bytes on disk already match the manifest entry.
        if old is not None and old.get("drive_id") == file_id:
            data = read_file(path)
            if is_real_jpeg(data) and sha256(data) == old.get("sha256"):
                entries.append(dict(name=name, drive_id=file_id,
                                    sha256=old["sha256"], bytes=len(data)))
                skipped += 1
                total += len(data)
                print("[skip] %s (matches manifest)" % name)
                continue

        try:
            data = fetch_photo(file_id, n)
        except RuntimeError as e:
            print("  FAIL: %s" % e)
            failures += 1
            continue
        with open(path, "wb") as fh:
            fh.write(data)
        entries.append(dict(name=name, drive_id=file_id,
                            sha256=sha256(data), bytes=len(data)))
        if old is None or old.get("sha256") != entries[-1]["sha256"]:
            changed.append(name)
        downloaded += 1
        total += len(data)

    print("\ndone: %d/42 photos (%d downloaded, %d skipped, %d failed), "
          "%.1f MB total in %s" % (42 - failures, downloaded, skipped, failures,
                                   total / 1e6, OUT_DIR))
    if failures:
        print("FAILURES: %d photo(s) missing; manifest not updated. Fix and re-run." % failures)
        return 1
    if save_manifest(entries):
        print("manifest updated: %s" % os.path.relpath(MANIFEST, ROOT))
    else:
        print("manifest unchanged")

    if changed_out:
        with open(changed_out, "w", encoding="utf-8") as fh:
            for name in changed:
                fh.write(name + "\n")
        print("changed photos (%d): %s"
              % (len(changed), ", ".join(changed) if changed else "none"))
    return 0


def run_manifest_only(changed_out):
    """No network: rebuild manifest.json from the files already in img/gallery/."""
    if len(PHOTOS) != 42:
        print("expected 42 photo IDs in PHOTOS, found %d" % len(PHOTOS))
        return 1
    existing = load_manifest()
    entries, changed, problems = [], [], []
    total = 0
    for n, file_id in enumerate(PHOTOS, 1):
        name = "%02d.jpg" % n
        data = read_file(os.path.join(OUT_DIR, name))
        if data is None:
            problems.append("%s: file missing" % name)
            continue
        if not data.startswith(JPEG_MAGIC):
            problems.append("%s: not a real JPEG (missing SOI magic)" % name)
            continue
        if len(data) <= MIN_BYTES:
            problems.append("%s: only %d bytes, need > %d KB" % (name, len(data), MIN_BYTES // 1024))
            continue
        old = None
        if existing is not None and len(existing) == len(PHOTOS):
            old = existing[n - 1] if isinstance(existing[n - 1], dict) else None
        entries.append(dict(name=name, drive_id=file_id,
                            sha256=sha256(data), bytes=len(data)))
        if old is None or old.get("sha256") != entries[-1]["sha256"]:
            changed.append(name)
        total += len(data)
    if problems:
        print("cannot build the manifest, fix first:")
        for p in problems:
            print("  " + p)
        return 1
    if save_manifest(entries):
        print("manifest written: %s (%d photos, %.1f MB)"
              % (os.path.relpath(MANIFEST, ROOT), len(entries), total / 1e6))
    else:
        print("manifest unchanged (%d photos, %.1f MB)" % (len(entries), total / 1e6))
    if changed_out:
        with open(changed_out, "w", encoding="utf-8") as fh:
            for name in changed:
                fh.write(name + "\n")
        print("changed photos (%d): %s"
              % (len(changed), ", ".join(changed) if changed else "none"))
    return 0


def run_verify():
    """Offline check: 42 real JPEGs > 10 KB, hashes matching the manifest."""
    problems = []
    if len(PHOTOS) != 42:
        problems.append("expected 42 photo IDs in PHOTOS, found %d" % len(PHOTOS))
    existing = load_manifest()
    if existing is None:
        problems.append("manifest missing or unreadable: img/gallery/manifest.json")
        existing = [None] * len(PHOTOS)
    elif len(existing) != len(PHOTOS):
        problems.append("manifest has %d entries, expected %d"
                        % (len(existing), len(PHOTOS)))
        existing = list(existing) + [None] * (len(PHOTOS) - len(existing))
    total = 0
    for n, file_id in enumerate(PHOTOS, 1):
        name = "%02d.jpg" % n
        old = existing[n - 1] if isinstance(existing[n - 1], dict) else {}
        if old.get("drive_id") != file_id:
            problems.append("%s: manifest drive ID does not match PHOTOS[%d]" % (name, n - 1))
        data = read_file(os.path.join(OUT_DIR, name))
        if data is None:
            problems.append("%s: file missing" % name)
            continue
        if not data.startswith(JPEG_MAGIC):
            problems.append("%s: not a real JPEG (missing SOI magic)" % name)
        if len(data) <= MIN_BYTES:
            problems.append("%s: only %d bytes, need > %d KB" % (name, len(data), MIN_BYTES // 1024))
        if old.get("sha256") != sha256(data):
            problems.append("%s: hash does not match manifest" % name)
        total += len(data)
    if problems:
        print("verify FAILED, %d problem(s):" % len(problems))
        for p in problems:
            print("  " + p)
        return 1
    raw = read_file(MANIFEST) or b"{}"
    try:
        width = json.loads(raw.decode("utf-8")).get("width") or WIDTH
    except (ValueError, UnicodeDecodeError):
        width = WIDTH
    print("verify ok: 42 photos, real JPEGs, hashes match img/gallery/manifest.json "
          "(album: %s, w%s, %.1f MB total)" % (ALBUM, width, total / 1e6))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Fetch/refresh the 42 KIZAZI 2026 photos into img/gallery/.")
    parser.add_argument("--force", action="store_true",
                        help="re-download all 42 photos, ignoring the manifest")
    parser.add_argument("--changed-out", metavar="FILE",
                        help="write the names of the photos whose bytes changed to FILE")
    parser.add_argument("--manifest-only", action="store_true",
                        help="no network: rebuild manifest.json from the files already on disk")
    parser.add_argument("--verify", action="store_true",
                        help="offline check: 42 real JPEGs > 10 KB, hashes match the manifest")
    parser.add_argument("--replace-curated", action="store_true",
                        help="allow a Drive download to overwrite the curated, "
                             "vendored gallery (img/gallery/SOURCES.json)")
    args = parser.parse_args(argv)
    if args.verify:
        return run_verify()
    if args.manifest_only:
        return run_manifest_only(args.changed_out)
    if os.path.exists(SOURCES) and not args.replace_curated:
        print("img/gallery/ holds the curated, vendored set "
              "(img/gallery/SOURCES.json).")
        print("Refusing to overwrite it from Drive.")
        print("  * to check the files:      python3 tools/fetch_gallery_photos.py --verify")
        print("  * to re-vendor by hand:    python3 tools/vendor_gallery.py --from <album>")
        print("  * to really re-download:   add --replace-curated")
        return 1
    return run_fetch(args.force, args.changed_out)


if __name__ == "__main__":
    sys.exit(main())
