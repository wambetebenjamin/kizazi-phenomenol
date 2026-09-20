#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recolour a CSS file from the old violet palette to the flame-sunset palette.

Every colour whose hue sits in the violet/indigo range (240-320 deg) is
rotated into the orange range (14-34 deg); deep inks get a lightness nudge so
warmth survives. Hex (#xxx/#xxxx/#xxxxxx/#xxxxxxxx), URL-encoded %23xxxxxx,
and rgb()/rgba() values are all handled.

Usage:  python3 tools/recolor.py FILE [FILE...] [--dry]
"""
import re
import sys
import colorsys

def rotate(rgb):
    r, g, b = [v / 255.0 for v in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    hp, sp = h * 360.0, s * 100.0
    if not (240 <= hp <= 320 and sp > 5):
        return None
    nh = 14 + (hp - 240) * (20.0 / 80.0)
    nl = l * 100.0
    if nl < 20:
        nl = min(nl * 1.3 + 2, 30)
    r2, g2, b2 = colorsys.hls_to_rgb(nh / 360.0, nl / 100.0, sp / 100.0)
    return (round(r2 * 255), round(g2 * 255), round(b2 * 255))

REPORT = {}

def note(old, new):
    REPORT.setdefault(old, set()).add(new)

def hex_sub(m):
    raw = m.group(0)
    d = re.sub(r'[^0-9a-fA-F]', '', raw)
    if len(d) == 3:
        d = ''.join(c * 2 for c in d)
    if len(d) == 4:
        d = ''.join(c * 2 for c in d[:3]) + 'ff'
    if len(d) not in (6, 8):
        return raw
    rgb = (int(d[0:2], 16), int(d[2:4], 16), int(d[4:6], 16))
    new = rotate(rgb)
    if not new:
        return raw
    note(raw.upper(), new)
    out = '#%02x%02x%02x' % new
    return out + ('%02x' % int(d[6:8], 16) if len(d) == 8 else '')

def rgb_sub(m):
    raw = m.group(0)
    nums = re.findall(r'\d+(?:\.\d+)?', raw)
    rgb = (float(nums[0]), float(nums[1]), float(nums[2]))
    new = rotate(rgb)
    if not new:
        return raw
    note(raw, new)
    it = iter(str(v) for v in new)
    return re.sub(r'\d+(?:\.\d+)?', lambda _: next(it), raw, count=3)

HEX_RE = re.compile(r'%23[0-9a-fA-F]{6}|#[0-9a-fA-F]{8}\b|#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3,4}\b')
RGB_RE = re.compile(r'rgba?\(\s*\d+(?:\.\d+)?\s*,\s*\d+(?:\.\d+)?\s*,\s*\d+(?:\.\d+)?')

def recolor(text):
    text = RGB_RE.sub(rgb_sub, text)
    text = HEX_RE.sub(hex_sub, text)
    return text

def main():
    args = [a for a in sys.argv[1:]]
    dry = '--dry' in args
    args = [a for a in args if a != '--dry']
    for path in args:
        REPORT.clear()
        s = open(path).read()
        s2 = recolor(s)
        if not dry:
            open(path, 'w').write(s2)
        print('== %s (%s) ==' % (path, 'dry-run' if dry else 'written'))
        for old, news in sorted(REPORT.items(), key=lambda kv: str(kv[0])):
            shown = ', '.join(
                ('%s' % v) if isinstance(v, tuple) and len(v) == 3 and all(isinstance(x, float) for x in v)
                else ('#%02x%02x%02x' % v) for v in news)
            print('  %-28s -> %s' % (old, shown))

if __name__ == '__main__':
    main()
