#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Curate, sharpen and vendor the 42 "KIZAZI 2026" photos.

The raw event archive lives in the repo-root ``drive-download-*.zip`` parts
(220 JPEGs, 217 unique).  The site always served exactly 42 curated photos
(img/gallery/01.jpg .. 42.jpg).  This tool rebuilds that set from the zips:

  * picks the 42 curated files (CURATED below, index N -> NN.jpg),
  * upscales them (Lanczos) so full-bleed backgrounds do not look soft,
  * applies an unsharp pass scaled to each photo's measured blur score,
  * writes img/gallery/01.jpg .. 42.jpg and the 4 hero frames
    img/hero/01.jpg .. 04.jpg (1600x900 centre crops),
  * refreshes img/gallery/manifest.json (source zip + sha256 + size).

Needs ImageMagick (``convert``) on PATH.  Stdlib Python otherwise.

Usage:  python3 tools/process_photos.py [--force]
A run without --force skips photos whose manifest entry already matches.
"""

import hashlib
import json
import os
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "img", "gallery")
HERO_OUT = os.path.join(ROOT, "img", "hero")
MANIFEST = os.path.join(OUT, "manifest.json")

# index (0-based) -> (zip entry name, measured sharpness score 0..255).
# Lower score = softer image = stronger unsharp pass below.
CURATED = [
    (0,  "20260815-IMG_2134.jpg", 137),
    (1,  "20260815-IMG_2168.jpg", 164),
    (2,  "20260815-IMG_2223.jpg", 177),
    (3,  "20260815-IMG_2293.jpg", 140),
    (4,  "20260814-IMG_2008.jpg", 151),
    (5,  "20260815-IMG_2292.jpg", 130),
    (6,  "20260814-IMG_1990.jpg", 131),
    (7,  "20260815-IMG_2138.jpg", 128),
    (8,  "20260815-IMG_2153.jpg", 142),
    (9,  "20260815-IMG_2145.jpg", 159),
    (10, "20260815-IMG_2238.jpg", 118),
    (11, "20260815-IMG_2126.jpg", 171),
    (12, "20260814-IMG_1850.jpg", 121),
    (13, "20260815-IMG_2154.jpg", 162),
    (14, "20260815-IMG_2148.jpg", 161),
    (15, "20260815-IMG_2130.jpg", 159),
    (16, "20260815-IMG_2136.jpg", 148),
    (17, "20260815-IMG_2294.jpg", 138),
    (18, "20260814-IMG_1862.jpg", 136),
    (19, "20260815-IMG_2147.jpg", 155),
    (20, "20260815-IMG_2119.jpg", 152),
    (21, "20260814-IMG_1864.jpg", 126),
    (22, "20260815-IMG_2157.jpg", 163),
    (23, "20260815-IMG_2217.jpg", 129),
    (24, "20260815-IMG_2211.jpg", 129),
    (25, "20260815-IMG_2164.jpg", 165),
    (26, "20260815-IMG_2212.jpg", 146),
    (27, "20260815-IMG_2139.jpg", 134),
    (28, "20260815-IMG_2193.jpg", 205),
    (29, "20260815-IMG_2200.jpg", 198),
    (30, "20260815-IMG_2185.jpg", 195),
    (31, "20260814-IMG_2036.jpg", 194),
    (32, "20260814-IMG_2017.jpg", 189),
    (33, "20260815-IMG_2125.jpg", 184),
    (34, "20260815-IMG_2291.jpg", 161),
    (35, "20260815-IMG_2251.jpg", 158),
    (36, "20260814-IMG_2014.jpg", 158),
    (37, "20260815-IMG_2176.jpg", 156),
    (38, "20260815-IMG_2216.jpg", 155),
    (39, "20260814-IMG_1844.jpg", 124),
    (40, "20260815-IMG_2158.jpg", 147),
    (41, "20260815-IMG_2214.jpg", 162),
]

# The four home-hero frames: (hero NN.jpg, gallery index whose source is used)
HERO = [(1, 0), (2, 6), (3, 1), (4, 11)]

ZIPS = [f for f in sorted(os.listdir(ROOT))
        if f.startswith("drive-download-") and f.endswith(".zip")]


def find_entry(name):
    for z in ZIPS:
        zf = zipfile.ZipFile(os.path.join(ROOT, z))
        if name in zf.namelist():
            data = zf.read(name)
            zf.close()
            return z, data
        zf.close()
    raise SystemExit("photo %s not found in any zip" % name)


def unsharp_for(score):
    if score >= 150:
        return "0x0.6+0.5+0"
    if score >= 120:
        return "0x0.9+0.8+0"
    return "0x1.2+1.0+0"


def gallery_bytes(src, score):
    """Upscale long side to 1400 + tone + unsharp scaled to blur score."""
    return subprocess.run(
        ["convert", src, "-auto-orient", "-filter", "Lanczos",
         "-resize", "1400x1400", "-brightness-contrast", "1x5",
         "-unsharp", unsharp_for(score), "-quality", "88", "jpg:-"],
        check=True, stdout=subprocess.PIPE).stdout


def hero_bytes(src, score):
    return subprocess.run(
        ["convert", src, "-auto-orient", "-filter", "Lanczos",
         "-resize", "1600x", "-gravity", "center", "-crop", "1600x900+0+0",
         "+repage", "-brightness-contrast", "1x6",
         "-unsharp", "0x1.0+0.9+0", "-quality", "88", "jpg:-"],
        check=True, stdout=subprocess.PIPE).stdout


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def main():
    force = "--force" in sys.argv
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(HERO_OUT, exist_ok=True)
    old = {}
    if os.path.exists(MANIFEST):
        old = {e["file"]: e for e in json.load(open(MANIFEST))["photos"]}

    manifest = []
    for idx, name, score in CURATED:
        zfile, data = find_entry(name)
        out_name = "%02d.jpg" % (idx + 1)
        out_path = os.path.join(OUT, out_name)
        entry = dict(file=out_name, source_zip=zfile, source_name=name,
                     sharpness=score)
        done = (not force and out_name in old and os.path.exists(out_path)
                and old[out_name].get("source_name") == name)
        if done:
            manifest.append(dict(old[out_name]))
            print("keep  %s" % out_name)
            continue
        tmp = os.path.join(OUT, ".src.jpg")
        with open(tmp, "wb") as fh:
            fh.write(data)
        out = gallery_bytes(tmp, score)
        with open(out_path, "wb") as fh:
            fh.write(out)
        os.remove(tmp)
        entry.update(sha256=sha256(out), size=len(out))
        manifest.append(entry)
        print("write %s  (%s, score %d)" % (out_name, zfile, score))

    for n, idx in HERO:
        name = dict((i, (nm, sc)) for i, nm, sc in CURATED)[idx]
        zfile, data = find_entry(name[0])
        tmp = os.path.join(HERO_OUT, ".src.jpg")
        with open(tmp, "wb") as fh:
            fh.write(data)
        out = hero_bytes(tmp, name[1])
        with open(os.path.join(HERO_OUT, "%02d.jpg" % n), "wb") as fh:
            fh.write(out)
        os.remove(tmp)
        print("hero  %02d.jpg <- %s" % (n, name[0]))

    json.dump(dict(album="KIZAZI 2026", photos=manifest),
              open(MANIFEST, "w"), indent=2)
    print("done: %d gallery photos, %d hero frames" % (len(manifest), len(HERO)))


if __name__ == "__main__":
    main()
