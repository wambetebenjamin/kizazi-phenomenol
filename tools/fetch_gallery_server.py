#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Browser-assisted photo fetcher for restricted-network environments.

Serves the repo root (like `python3 -m http.server`) plus two helpers:

  GET  /__fetch.html   a page that fetches the 42 "KIZAZI 2026" photos through
                       YOUR browser (which has internet access) and POSTs each
                       one to /__save/NN below
  POST /__save/NN      validates a real JPEG > 10 KB and writes img/gallery/NN.jpg
  GET  /__status       JSON list of the files already in img/gallery/

Use it when the machine running the build cannot reach Google Drive itself
(allowlisted sandboxes, locked-down CI):  python3 tools/fetch_gallery_server.py
then open the served /__fetch.html (e.g. http://localhost:8123/__fetch.html, or
the proxied preview URL of port 8123) in a normal browser and click
"Fetch all 42 photos".  With `--fetch-root` the same page is served at "/",
so a bare preview link works too:

    python3 tools/fetch_gallery_server.py 8123 --fetch-root

How the browser part works (no CORS needed):
  * every source URL is requested with `fetch(url, {mode: 'no-cors'})`, which
    returns an opaque response whose BYTES are still forwarded untouched when
    the page POSTs that blob back to this server.  The server, not the browser,
    is what decides whether the bytes are a real JPEG, so Google's missing CORS
    headers no longer matter.
  * two passes: `credentials: 'omit'` first (album shared "Anyone with the
    link -> Viewer"), then `credentials: 'include'` (your own Drive session).
  * proxy fallbacks (wsrv.nl, codetabs, allorigins) are tried afterwards.
  * if everything fails, the page falls back to thumbnails + drag & drop: save
    the images by hand, drop them onto the page, and it POSTs them in order.

The ordinary refresh path remains `python3 tools/fetch_gallery_photos.py`.
"""

import json
import os
import re
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_common import PHOTOS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GALLERY = os.path.join(ROOT, "img", "gallery")
# usage: python3 tools/fetch_gallery_server.py [port] [--fetch-root]
#   --fetch-root also serves the fetch page at "/" (handy when the port is
#   opened through a preview proxy, where the root is the only easy entry).
PORT = next((int(a) for a in sys.argv[1:] if a.isdigit()), 8123)
FETCH_AT_ROOT = "--fetch-root" in sys.argv[1:]

MIN_BYTES = 10 * 1024
MAX_BYTES = 30 * 1024 * 1024
JPEG_MAGIC = b"\xff\xd8\xff"
SAVE_RE = re.compile(r"^/__save/(\d{2})$")

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KIZAZI gallery photo fetcher</title>
<style>
  body { font-family: system-ui, sans-serif; background: #0A0A0A; color: #fff;
         max-width: 900px; margin: 2rem auto; padding: 0 1rem; }
  h1 { color: #E63946; font-weight: 700; }
  h2 { font-size: 1.05rem; margin-top: 2rem; }
  p, li { color: #dfe2f5; line-height: 1.5; }
  code { color: #FAF7F0; }
  button { background: #E63946; color: #fff; border: 0; border-radius: 24px;
           padding: .8rem 2rem; font-size: 1.05rem; cursor: pointer; }
  button:disabled { background: #16A34A; cursor: wait; }
  button.ghost { background: transparent; border: 1px solid #E63946;
                 padding: .5rem 1.2rem; font-size: .9rem; }
  #grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 8px; margin-top: 1rem; }
  #grid div { background: rgba(255,255,255,.08); border-radius: 8px; padding: 6px;
              font-size: .75rem; text-align: center; }
  #grid img { width: 100%%; aspect-ratio: 1/1; object-fit: cover; border-radius: 6px;
              display: block; margin-bottom: 4px; }
  .ok { color: #FACC15; } .bad { color: #E63946; } .wait { color: #FAF7F0; }
  #summary { margin-top: 1rem; font-weight: 600; }
  #drop { margin-top: 1rem; border: 2px dashed #E63946; border-radius: 12px;
          padding: 1.5rem; text-align: center; color: #dfe2f5; }
  #drop.hot { background: rgba(109,40,217,.18); }
  input[type=number] { width: 4.5rem; padding: .3rem; border-radius: 6px; border: 0; }
</style>
</head>
<body>
<h1>Fetch the 42 &ldquo;KIZAZI 2026&rdquo; photos</h1>
<p>This page downloads each photo <em>through your browser</em> and saves it into
<code>img/gallery/01.jpg &hellip; 42.jpg</code> in the repository workspace.
Leave the tab open until it finishes. Nothing leaves your machine except the
photo bytes, which are POSTed to the tiny local server that served this page.</p>
<p><button id="go">Fetch all 42 photos</button></p>
<div id="summary" class="wait">Idle. Click the button to start.</div>
<div id="grid"></div>

<h2>Photos (only the ones that failed are listed here)</h2>
<p>If the automatic fetch cannot read a file (wrong sharing setting, or a
network filter), right-click its thumbnail below and choose
<em>Save image as&hellip;</em>, or download the album from Google Drive, then drop
the JPEGs anywhere on this box. They are saved in the order they arrive, or by
filename when the names end in numbers.</p>
<div id="drop">
  Drop the JPEG files here <br>
  <small>start at number <input type="number" id="start" min="1" max="%(count)d" value="1"></small>
  <div><input type="file" id="picker" multiple accept="image/jpeg,image/*" style="margin-top:.6rem"></div>
</div>
<div id="manual" class="wait"></div>
<script>
var PHOTOS = %(ids)s;
var TOTAL = PHOTOS.length;
var grid = document.getElementById('grid');
var summary = document.getElementById('summary');
var drop = document.getElementById('drop');
var manual = document.getElementById('manual');
var cells = [];
var saved = {};
for (var i = 0; i < TOTAL; i++) {
  var n = i + 1;
  var d = document.createElement('div');
  d.innerHTML = '<span class="wait" id="s' + n + '">' + pad(n) + ' &hellip;</span>';
  grid.appendChild(d);
  cells.push(d);
}
function pad(n) { return ('0' + n).slice(-2); }
function label(n, cls, text) {
  var el = document.getElementById('s' + n);
  el.className = cls;
  el.textContent = pad(n) + ' ' + text;
}
function thumb(n, url) {
  if (cells[n - 1].querySelector('img')) { return; }
  var img = document.createElement('img');
  img.src = url;
  img.alt = 'photo ' + pad(n) + ' (right-click to save)';
  img.loading = 'lazy';
  cells[n - 1].insertBefore(img, cells[n - 1].firstChild);
}
/* Every Google/proxy URL for one photo, in the order we try them.  All of
   them are requested as opaque (no-cors) responses, so the browser does not
   need the server to send CORS headers; the blob travels back to our own
   server untouched and THAT decides whether it is a real JPEG. */
function sourcesFor(id) {
  var direct = encodeURIComponent('https://drive.google.com/thumbnail?id=' + id + '&sz=w1600');
  var lh3 = encodeURIComponent('https://lh3.googleusercontent.com/d/' + id + '=w1600');
  return [
    'https://drive.google.com/thumbnail?id=' + id + '&sz=w1600',
    'https://lh3.googleusercontent.com/d/' + id + '=w1600',
    'https://drive.google.com/uc?export=view&id=' + id,
    'https://wsrv.nl/?url=' + direct + '&n=-1&output=jpg',
    'https://api.codetabs.com/v1/proxy?quest=' + lh3,
    'https://api.allorigins.win/raw?url=' + direct
  ];
}
async function relay(url, n, withCreds) {
  var opts = { mode: 'no-cors', redirect: 'follow',
               credentials: withCreds ? 'include' : 'omit' };
  var r = await fetch(url, opts);
  var blob = await r.blob();
  if (!blob || !blob.size) { throw new Error('empty response'); }
  var res = await fetch('/__save/' + pad(n), { method: 'POST', body: blob });
  if (!res.ok) { throw new Error('HTTP ' + res.status); }
  return blob.size;
}
async function grab(id, n) {
  var list = sourcesFor(id), last = 'no source worked';
  for (var pass = 0; pass < 2; pass++) {
    for (var k = 0; k < list.length; k++) {
      try {
        return await relay(list[k], n, pass === 1);
      } catch (e) {
        last = (pass ? 'session: ' : 'public: ') + e.message;
      }
    }
  }
  throw new Error(last);
}
async function run(btn) {
  btn.disabled = true;
  document.getElementById('go').disabled = true;
  var todo = [];
  for (var i = 0; i < TOTAL; i++) { if (!saved[i + 1]) { todo.push([PHOTOS[i], i + 1]); } }
  var done = 0, failed = 0, queue = todo.slice();
  async function worker() {
    while (queue.length) {
      var item = queue.shift(), id = item[0], n = item[1];
      label(n, 'wait', 'fetching');
      try {
        var size = await grab(id, n);
        saved[n] = true;
        done++;
        label(n, 'ok', 'saved ' + Math.round(size / 1024) + ' KB');
      } catch (e) {
        failed++;
        label(n, 'bad', 'FAILED (' + e.message + ')');
        thumb(n, 'https://drive.google.com/thumbnail?id=' + id + '&sz=w1600');
      }
      summary.textContent = done + ' saved / ' + failed + ' failed / ' +
        (todo.length - done - failed) + ' to go';
    }
  }
  await Promise.all([worker(), worker(), worker()]);
  var missing = TOTAL - Object.keys(saved).length;
  summary.className = missing ? 'bad' : 'ok';
  summary.textContent = missing
    ? 'Finished with ' + missing + ' photo(s) missing. Re-click to retry, or use the thumbnails and the drop box below.'
    : 'All ' + TOTAL + ' photos are in img/gallery/. Tell the agent to verify and commit.';
  btn.disabled = false;
  btn.textContent = 'Retry the missing ones';
}
document.getElementById('go').addEventListener('click', function () { run(this); });

document.getElementById('picker').addEventListener('change', function () {
  saveFiles(this.files);
});
['dragenter', 'dragover'].forEach(function (ev) {
  drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('hot'); });
});
['dragleave', 'drop'].forEach(function (ev) {
  drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('hot'); });
});
drop.addEventListener('drop', function (e) {
  if (e.dataTransfer && e.dataTransfer.files) { saveFiles(e.dataTransfer.files); }
});
function naturalNumber(name) {
  var m = /(\d+)(?!.*\d)/.exec(name || '');
  return m ? parseInt(m[1], 10) : null;
}
async function saveFiles(fileList) {
  var files = Array.prototype.slice.call(fileList).filter(function (f) {
    return /jpe?g$/i.test(f.type) || /\.jpe?g$/i.test(f.name);
  });
  if (!files.length) { manual.textContent = 'No JPEG files in that drop.'; return; }
  files.sort(function (a, b) {
    var na = naturalNumber(a.name), nb = naturalNumber(b.name);
    if (na !== null && nb !== null && na !== nb) { return na - nb; }
    return a.name.localeCompare(b.name);
  });
  var numbered = files.every(function (f) { var n = naturalNumber(f.name); return n !== null && n >= 1 && n <= TOTAL; });
  var start = numbered ? 0 : Math.max(1, parseInt(document.getElementById('start').value, 10) || 1);
  var ok = 0, bad = 0;
  for (var i = 0; i < files.length; i++) {
    var n = numbered ? naturalNumber(files[i].name) : start + i;
    if (n > TOTAL) { break; }
    try {
      var res = await fetch('/__save/' + pad(n), { method: 'POST', body: files[i] });
      if (!res.ok) { throw new Error('HTTP ' + res.status); }
      saved[n] = true;
      ok++;
      thumb(n, URL.createObjectURL(files[i]));
      label(n, 'ok', 'saved ' + Math.round(files[i].size / 1024) + ' KB');
    } catch (e) {
      bad++;
      label(n, 'bad', 'FAILED (' + e.message + ')');
    }
  }
  manual.textContent = 'Dropped: ' + ok + ' saved, ' + bad + ' rejected. ' +
    (TOTAL - Object.keys(saved).length) + ' still missing.';
  summary.textContent = (TOTAL - Object.keys(saved).length) + ' photo(s) still missing.';
}
</script>
</body>
</html>
"""


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def _send_json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _wants_fetch_page(self):
        path = (self.path or "").split("?")[0]
        if path in ("/__fetch.html", "/__fetch"):
            return True
        return FETCH_AT_ROOT and path in ("/", "/index.html")

    def do_GET(self):
        if self._wants_fetch_page():
            body = (PAGE % {"ids": json.dumps(PHOTOS), "min": MIN_BYTES,
                            "count": len(PHOTOS)}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path == "/__status":
            have = [f for f in sorted(os.listdir(GALLERY))] if os.path.isdir(GALLERY) else []
            self._send_json(200, {"gallery": have, "expected": len(PHOTOS)})
            return
        super().do_GET()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()

    def do_POST(self):
        m = SAVE_RE.match(self.path or "")
        if not m:
            self._send_json(404, {"error": "use /__save/NN"})
            return
        n = int(m.group(1))
        if not (1 <= n <= len(PHOTOS)):
            self._send_json(400, {"error": "NN out of range"})
            return
        length = int(self.headers.get("Content-Length") or 0)
        if length <= 0 or length > MAX_BYTES:
            self._send_json(411, {"error": "bad length"})
            return
        data = self.rfile.read(length)
        if not data.startswith(JPEG_MAGIC) or len(data) <= MIN_BYTES:
            self._send_json(422, {"error": "not a real JPEG > %d KB" % (MIN_BYTES // 1024)})
            return
        os.makedirs(GALLERY, exist_ok=True)
        path = os.path.join(GALLERY, "%02d.jpg" % n)
        with open(path, "wb") as fh:
            fh.write(data)
        self._send_json(200, {"saved": "%02d.jpg" % n, "bytes": len(data)})


def main():
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print("serving %s on port %d  (fetch page: /__fetch.html)" % (ROOT, PORT))
    if FETCH_AT_ROOT:
        print("the fetch page is also served at / (--fetch-root)")
    server.serve_forever()


if __name__ == "__main__":
    main()
