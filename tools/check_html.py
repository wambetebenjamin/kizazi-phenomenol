#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KIZAZI Phenomenal — HTML sanity checker.

Verifies every page at the repo root:
  * starts with <!DOCTYPE html>
  * tags are balanced (void elements handled)
  * has exactly one <html> and one <body>

Usage:  python3 tools/check_html.py
Exit code 0 = all good, 1 = problems found.
"""

import glob
import html.parser
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Validator(html.parser.HTMLParser):
    VOID = {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "source", "track", "wbr",
    }

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.html_count = 0
        self.body_count = 0

    def handle_starttag(self, tag, attrs):
        if tag == "html":
            self.html_count += 1
        elif tag == "body":
            self.body_count += 1
        if tag not in self.VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if not self.stack:
            self.errors.append("stray </%s> at line %d" % (tag, self.getpos()[0]))
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
            return
        names = [t for t, _ in self.stack]
        if tag in names:
            while self.stack and self.stack[-1][0] != tag:
                t, p = self.stack.pop()
                self.errors.append(
                    "unclosed <%s> opened at line %d (closed by </%s> at line %d)"
                    % (t, p[0], tag, self.getpos()[0]))
            self.stack.pop()
        else:
            self.errors.append("unmatched </%s> at line %d" % (tag, self.getpos()[0]))


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "*.html")))
    if not files:
        print("no HTML files found at repo root")
        return 1
    ok = True
    for path in files:
        name = os.path.basename(path)
        src = open(path, encoding="utf-8").read()
        v = Validator()
        v.feed(src)
        v.close()
        for t, p in v.stack:
            v.errors.append("unclosed <%s> opened at line %d" % (t, p[0]))
        if not src.lstrip().lower().startswith("<!doctype html>"):
            v.errors.append("missing <!DOCTYPE html>")
        if v.html_count != 1:
            v.errors.append("expected exactly one <html>, found %d" % v.html_count)
        if v.body_count != 1:
            v.errors.append("expected exactly one <body>, found %d" % v.body_count)
        if v.errors:
            ok = False
            print("FAIL %s" % name)
            for e in v.errors[:10]:
                print("     " + e)
        else:
            print("ok   %s" % name)
    print()
    print("all %d pages valid" % len(files) if ok else "problems found — see above")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
