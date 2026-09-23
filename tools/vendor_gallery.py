#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vendor the curated KIZAZI 2026 gallery set into img/gallery/.

The 42 photos that run across the site come from the owner's upload of the
"KIZAZI 2026" album (14 to 15 August): the eight split parts
`drive-download-20260922T141329Z-1-001-part-00N.zip`, unzipped. That album
holds 220 JPEGs, of which 3 are exact duplicates, so 217 unique frames.

This tool:
  1. picks the curated 42 (CURATED below, in the exact order the pages use,
     so index 0..03 are the hero/header/about/footer slots and 28..33 are the
     footer photo grid),
  2. copies each pick to img/gallery/01.jpg .. 42.jpg at its original
     resolution (the uploads are 1000 px on the long edge, so nothing is
     upscaled),
  3. re-encodes each pick for the web (quality 82, progressive) and drops the
     camera metadata, which carries body and lens serial numbers, while
     keeping the ICC profile so the colours do not shift.  Without Pillow
     installed it falls back to a lossless copy with the same metadata strip,
     so the tool still runs on a bare Python;
  4. writes img/gallery/manifest.json in the schema
     tools/fetch_gallery_photos.py reads (name, drive_id, sha256, bytes), so
     `python3 tools/fetch_gallery_photos.py --verify` passes offline,
  5. writes img/gallery/SOURCES.json: which upload each slot came from, plus
     the photographer credit kept from the originals' EXIF.

Usage:
    python3 tools/vendor_gallery.py --from /path/to/unzipped-album
    python3 tools/vendor_gallery.py --from /path/to/unzipped-album --dry-run

Stdlib only, like the other tools/ scripts.
"""

import argparse
import hashlib
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
sys.path.insert(0, _HERE)

import build_common as B  # noqa: E402  (PHOTOS, GALLERY_CATS, gallery_cat)

OUT_DIR = os.path.join(_ROOT, "img", "gallery")
MANIFEST = os.path.join(OUT_DIR, "manifest.json")
SOURCES = os.path.join(OUT_DIR, "SOURCES.json")

# Same manifest schema tools/fetch_gallery_photos.py reads and writes
# ({"album", "width", "photos": [...]}), so --verify and --manifest-only keep
# working.  The width is the real cap of these uploads: no upscaling.
ALBUM = "KIZAZI 2026"
WIDTH = 1000

# The credit carried in the originals' EXIF (Artist / Copyright), kept here so
# it survives the metadata strip.
CREDIT = "Photography: SPLENDOR WEMA (@BELLA TEHILLAH)"

# The curated 42, in site order (slot 0 = img/gallery/01.jpg).  The order is
# load-bearing: `tools/build.py` and `tools/build_common.py` point fixed slots
# at fixed jobs, so every pick below answers the slot it sits in:
#
#   slot 0        home hero fallback (landscape)
#   slot 1        default page header (landscape)
#   slot 2        about page video panel (landscape)
#   slot 3        footer photo (landscape)
#   slots 4 to 9  the six program cards, in PROGRAMS order
#   slots 10 to 13 the four event cards, in EVENTS order (10 also backgrounds
#                 the events page header and the film sections)
#   slots 14 to 16 the three blog cards, in BLOG order (14 also heads the
#                 blog page)
#   slots 17 to 24 the eight serving-team cards, in TEAMS order (17 also heads
#                 the team page)
#   slot 21       also heads the gallery page
#   slots 25 to 27 the about, ministries and programs page headers
#   slots 28 to 33 the six footer photo-grid circles
#   slot 30       also heads the testimonial page, 31 the contact page
#                 (with 32 as its photo) and 33 the 404 page
#   slots 34 to 41 the rest of the gallery wall
#
# The category after each filename is the curated label that
# GALLERY_ITEM_CATS (tools/build_common.py) assigns to that slot.
CURATED = [
    # --- page-level slots -------------------------------------------------
    ("20260814-IMG_1862.jpg", "worship"),     # 0  hero fallback, voices up
    ("20260814-IMG_1903.jpg", "bts"),         # 1  default header, stage prep
    ("20260815-IMG_2130.jpg", "community"),   # 2  about video panel, the circle
    ("20260815-IMG_2265.jpg", "service"),     # 3  footer photo, the handover
    # --- program cards (PROGRAMS order) -----------------------------------
    ("20260814-IMG_2006.jpg", "community"),   # 4  Rooted
    ("20260815-IMG_2077.jpg", "bts"),         # 5  Phenomenal Fridays
    ("20260815-IMG_2086.jpg", "creative"),    # 6  KIZAZI Creative Lab
    ("20260815-IMG_2187.jpg", "community"),   # 7  Mentorship Circle
    ("20260815-IMG_2168.jpg", "community"),   # 8  Campus Ambassadors
    ("20260814-IMG_1950.jpg", "service"),     # 9  Serve East Africa
    # --- event cards (EVENTS order) ---------------------------------------
    ("20260814-IMG_1846.jpg", "bts"),         # 10 Phenomenal Friday + bg
    ("20260815-IMG_2293.jpg", "worship"),     # 11 Conference 2027
    ("20260815-IMG_2258.jpg", "worship"),     # 12 Worship & Word Night
    ("20260815-IMG_2153.jpg", "community"),   # 13 Campus & School Tour
    # --- blog cards (BLOG order) ------------------------------------------
    ("20260815-IMG_2138.jpg", "community"),   # 14 devotional + blog header
    ("20260815-IMG_2294.jpg", "community"),   # 15 KIZAZI 2026 recap
    ("20260814-IMG_1884.jpg", "community"),   # 16 5 habits
    # --- serving-team cards (TEAMS order) ---------------------------------
    ("20260814-IMG_1988.jpg", "creative"),    # 17 Worship & Sound + header
    ("20260814-IMG_1927.jpg", "word"),        # 18 Word & Teaching Team
    ("20260815-IMG_2260.jpg", "service"),     # 19 Prayer Watch
    ("20260814-IMG_1886.jpg", "community"),   # 20 Discipleship Mentors
    ("20260815-IMG_2117.jpg", "bts"),         # 21 Media & Creative + gallery header
    ("20260815-IMG_2220.jpg", "community"),   # 22 Outreach & Missions
    ("20260814-IMG_1948.jpg", "service"),     # 23 Service & Hospitality
    ("20260815-IMG_2185.jpg", "community"),   # 24 Mentorship & Career
    # --- inner-page headers ----------------------------------------------
    ("20260815-IMG_2104.jpg", "creative"),    # 25 about header
    ("20260815-IMG_2136.jpg", "community"),   # 26 ministries header
    ("20260815-IMG_2264.jpg", "service"),     # 27 programs header
    # --- footer photo grid (FOOTER_GRID order) ---------------------------
    ("20260814-IMG_1851.jpg", "worship"),     # 28
    ("20260815-IMG_2215.jpg", "community"),   # 29
    ("20260814-IMG_1864.jpg", "worship"),     # 30 + testimonial header
    ("20260815-IMG_2063.jpg", "word"),        # 31 + contact header
    ("20260815-IMG_2221.jpg", "community"),   # 32 + contact photo
    ("20260815-IMG_2245.jpg", "service"),     # 33 + 404 header
    # --- the rest of the gallery wall -------------------------------------
    ("20260814-IMG_1859.jpg", "worship"),     # 34 praise
    ("20260815-IMG_2113.jpg", "bts"),         # 35 quiet portrait
    ("20260815-IMG_2276.jpg", "worship"),     # 36 singing it out
    ("20260815-IMG_2274.jpg", "word"),        # 37 the message
    ("20260814-IMG_1946.jpg", "community"),   # 38 lunch and laughter
    ("20260815-IMG_2266.jpg", "service"),     # 39 bags and blessings
    ("20260815-IMG_2285.jpg", "creative"),    # 40 last song of the night
    ("20260815-IMG_2115.jpg", "bts"),         # 41 between sessions
]

# JPEG marker segments that carry camera/software metadata.  APP0 (JFIF) and
# APP2 (ICC profile) are kept: dropping APP1/APP13 strips EXIF, XMP and IPTC.
_DROP_MARKERS = {0xE1, 0xED}


def is_jpeg(data):
    return data[:2] == b"\xff\xd8" and data[-2:] == b"\xff\xd9"


def strip_metadata(data):
    """Return the same JPEG without its EXIF/XMP/IPTC segments (lossless)."""
    if not is_jpeg(data):
        raise ValueError("not a complete JPEG (SOI/EOI magic missing)")
    out = bytearray(data[:2])
    i = 2
    n = len(data)
    while i < n - 1:
        if data[i] != 0xFF:
            raise ValueError("malformed JPEG at offset %d" % i)
        marker = data[i + 1]
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:   # standalone
            out += data[i:i + 2]
            i += 2
            continue
        if marker == 0xDA:                                     # start of scan
            out += data[i:]
            return bytes(out)
        if i + 4 > n:
            raise ValueError("truncated JPEG segment header")
        seglen = (data[i + 2] << 8) | data[i + 3]
        seg = data[i:i + 2 + seglen]
        if marker not in _DROP_MARKERS:
            out += seg
        i += 2 + seglen
    raise ValueError("no scan data found")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def encode_web(path, quality):
    """Re-encode for the web; returns None when Pillow is not installed."""
    try:
        from PIL import Image
    except ImportError:
        return None
    import io
    with Image.open(path) as im:
        im = im.convert("RGB")
        icc = im.info.get("icc_profile")
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=quality, optimize=True, progressive=True,
                icc_profile=icc)
        return buf.getvalue()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--from", dest="src", required=True,
                    help="folder holding the unzipped album JPEGs")
    ap.add_argument("--quality", type=int, default=82,
                    help="web JPEG quality (needs Pillow; default 82)")
    ap.add_argument("--lossless", action="store_true",
                    help="copy the bytes as they are, only stripping metadata")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would be written, write nothing")
    args = ap.parse_args(argv)

    if len(CURATED) != 42:
        print("CURATED must list exactly 42 photos, found %d" % len(CURATED))
        return 1
    photos = B.PHOTOS
    if len(photos) != 42:
        print("expected 42 photo IDs in PHOTOS, found %d" % len(photos))
        return 1
    if len({name for name, _ in CURATED}) != 42:
        print("CURATED lists a source file twice")
        return 1

    missing = [name for name, _ in CURATED
               if not os.path.isfile(os.path.join(args.src, name))]
    if missing:
        print("missing %d source photo(s) in %s:" % (len(missing), args.src))
        for m in missing:
            print("   " + m)
        return 1

    if not args.dry_run:
        os.makedirs(OUT_DIR, exist_ok=True)

    entries, sources, total = [], [], 0
    for i, (name, cat) in enumerate(CURATED, 1):
        out_name = "%02d.jpg" % i
        src_path = os.path.join(args.src, name)
        raw = open(src_path, "rb").read()
        clean = None if args.lossless else encode_web(src_path, args.quality)
        if clean is None:
            clean = strip_metadata(raw)
            mode = "lossless"
        else:
            mode = "q%d" % args.quality
        expect_cat = B.gallery_cat(i - 1)[0]
        flag = "" if expect_cat == cat else "  (category mismatch!)"
        entries.append(dict(name=out_name, drive_id=photos[i - 1],
                            sha256=sha256(clean), bytes=len(clean)))
        sources.append(dict(name=out_name, source=name, category=expect_cat,
                            source_bytes=len(raw), source_sha256=sha256(raw),
                            stripped_bytes=len(raw) - len(clean)))
        total += len(clean)
        if not args.dry_run:
            with open(os.path.join(OUT_DIR, out_name), "wb") as fh:
                fh.write(clean)
        print("%-8s <- %-28s %-9s %6.0f KB from %5.0f KB  (%s)%s"
              % (out_name, name, mode, len(clean) / 1024.0,
                 len(raw) / 1024.0, expect_cat, flag))

    doc = dict(
        album="KIZAZI 2026, 14 to 15 August 2026",
        source="owner upload: drive-download-20260922T141329Z-1-001-part-001..008.zip",
        curated="42 of 217 unique frames, chosen for people, spread and light",
        credit=CREDIT,
        resolution="original upload resolution, up to 1000 px on the long edge "
                   "(no upscaling)",
        encoding="re-encoded at JPEG quality 82, progressive, optimize on; "
                 "camera EXIF/XMP/IPTC stripped (body and lens serial numbers "
                 "removed); ICC profile kept",
        order="slot order matters, see tools/vendor_gallery.py",
        photos=sources,
    )
    if args.dry_run:
        print("\ndry run: %d photos, %.1f MB total, nothing written"
              % (len(entries), total / 1e6))
        return 0

    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(dict(album=ALBUM, width=WIDTH, photos=entries), fh, indent=2)
        fh.write("\n")
    with open(SOURCES, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2)
        fh.write("\n")
    print("\nwrote %s and %s (%d photos, %.1f MB)"
          % (os.path.relpath(MANIFEST, _ROOT), os.path.relpath(SOURCES, _ROOT),
             len(entries), total / 1e6))
    return 0


if __name__ == "__main__":
    sys.exit(main())
