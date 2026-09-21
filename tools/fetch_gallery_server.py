#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Browser-assisted photo fetcher for restricted-network environments.

Serves the repo root (like `python3 -m http.server`) plus two helpers:

  GET  /__fetch.html   a page that fetches the 42 "KIZAZI 2026" photos through
                       YOUR browser (which has internet access) and POSTs each
                       one to /__save/NN below
  POST /__save/NN      validates a real JPEG > 10 KB and writes img/gallery/NN.jpg

Use it when the machine running the build cannot reach Google Drive itself
(allowlisted sandboxes, locked-down CI):  python3 tools/fetch_gallery_server.py
then open http://localhost:8123/__fetch.html (or the proxied preview URL of
port 8123) in a normal browser and click "Fetch all photos".

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
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8123

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
  body { font-family: system-ui, sans-serif; background: #393D72; color: #fff;
         max-width: 780px; margin: 2rem auto; padding: 0 1rem; }
  h1 { color: #FF4880; font-weight: 700; }
  p, li { color: #dfe2f5; line-height: 1.5; }
  button { background: #FF4880; color: #fff; border: 0; border-radius: 24px;
           padding: .8rem 2rem; font-size: 1.05rem; cursor: pointer; }
  button:disabled { background: #4D65F9; cursor: wait; }
  #grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 8px; margin-top: 1rem; }
  #grid div { background: rgba(255,255,255,.08); border-radius: 8px; padding: 6px;
              font-size: .75rem; text-align: center; }
  #grid img { width: 100%%; aspect-ratio: 1/1; object-fit: cover; border-radius: 6px;
              display: block; margin-bottom: 4px; }
  .ok { color: #7CFFB2; } .bad { color: #FF4880; } .wait { color: #9aa0d4; }
  #summary { margin-top: 1rem; font-weight: 600; }
</style>
</head>
<body>
<h1>Fetch the 42 &ldquo;KIZAZI 2026&rdquo; photos</h1>
<p>This page downloads each photo <em>through your browser</em> (Drive &rarr; lh3
&rarr; uc fallbacks, then an image proxy) and saves it into
<code>img/gallery/01.jpg &hellip; 42.jpg</code> in the repository workspace.
Nothing leaves your machine except the photo bytes.</p>
<p><button id="go">Fetch all photos</button></p>
<div id="summary" class="wait">Idle &mdash; click the button to start.</div>
<div id="grid"></div>
<script>
var PHOTOS = %(ids)s;
var grid = document.getElementById('grid');
var summary = document.getElementById('summary');
var cells = [];
PHOTOS.forEach(function (id, i) {
  var n = i + 1;
  var d = document.createElement('div');
  d.innerHTML = '<span class="wait" id="s' + n + '">' + ('0' + n).slice(-2) + ' &hellip;</span>';
  grid.appendChild(d);
  cells.push(d);
});
function label(n, cls, text) {
  document.getElementById('s' + n).className = cls;
  document.getElementById('s' + n).textContent = ('0' + n).slice(-2) + ' ' + text;
}
function urlsFor(id) {
  return [
    'https://drive.google.com/thumbnail?id=' + id + '&sz=w1600',
    'https://lh3.googleusercontent.com/d/' + id + '=w1600',
    'https://drive.google.com/uc?export=view&id=' + id,
    'https://wsrv.nl/?url=' +
      encodeURIComponent('https://drive.google.com/thumbnail?id=' + id + '&sz=w1600') + '&n=-1',
    'https://api.codetabs.com/v1/proxy?quest=' +
      encodeURIComponent('https://lh3.googleusercontent.com/d/' + id + '=w1600')
  ];
}
async function grab(id) {
  var list = urlsFor(id), last = '';
  for (var k = 0; k < list.length; k++) {
    try {
      var r = await fetch(list[k], { mode: 'cors', credentials: 'omit', redirect: 'follow' });
      if (!r.ok) { last = 'HTTP ' + r.status; continue; }
      var b = await r.blob();
      if (b.size < %(min)d) { last = b.size + ' bytes (too small)'; continue; }
      return b;
    } catch (e) { last = 'blocked/failed'; }
  }
  throw new Error(last || 'no source worked');
}
async function save(n, blob) {
  var r = await fetch('/__save/' + ('0' + n).slice(-2), { method: 'POST', body: blob });
  if (!r.ok) { throw new Error('save HTTP ' + r.status); }
  return r.json();
}
document.getElementById('go').addEventListener('click', async function () {
  var btn = this;
  btn.disabled = true;
  var done = 0, failed = 0, queue = PHOTOS.map(function (id, i) { return [id, i + 1]; });
  async function worker() {
    while (queue.length) {
      var item = queue.shift(), id = item[0], n = item[1];
      try {
        label(n, 'wait', 'fetching');
        var blob = await grab(id);
        var res = await save(n, blob);
        done++;
        var img = document.createElement('img');
        img.src = URL.createObjectURL(blob);
        cells[n - 1].insertBefore(img, cells[n - 1].firstChild);
        label(n, 'ok', 'saved ' + Math.round(blob.size / 1024) + ' KB');
      } catch (e) {
        failed++;
        label(n, 'bad', 'FAILED (' + e.message + ')');
      }
      summary.textContent = done + ' saved / ' + failed + ' failed / ' + (42 - done - failed) + ' to go';
    }
  }
  await Promise.all([worker(), worker(), worker()]);
  summary.className = failed ? 'bad' : 'ok';
  summary.textContent = failed
    ? 'Finished with ' + failed + ' failure(s). Re-click to retry, or right-click the thumbnails above and use "Save image as" manually.'
    : 'All 42 photos are in img/gallery/ — tell the agent to verify and commit.';
  btn.disabled = false;
  btn.textContent = 'Retry failures';
});
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

    def do_GET(self):
        if self.path in ("/__fetch.html", "/__fetch"):
            body = (PAGE % {"ids": json.dumps(PHOTOS), "min": MIN_BYTES}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path == "/__status":
            have = [f for f in sorted(os.listdir(GALLERY))] if os.path.isdir(GALLERY) else []
            self._send_json(200, {"gallery": have})
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
    server.serve_forever()


if __name__ == "__main__":
    main()
