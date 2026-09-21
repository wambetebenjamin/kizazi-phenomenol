# KIZAZI Phenomenal — Official Website

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fwambetebenjamin%2Fkizazi-phenomenol)

> **A generation on fire for God.** 🔥
> Christian youth ministry / fellowship serving **Kenya · Uganda · Tanzania · Rwanda**.
> *"Let no one despise you for your youth…"* — 1 Timothy 4:12

Built **on the BabyCare Bootstrap template (HTML Codex) exactly as shipped**: same
page structure, same components, same fonts and the template's own colour palette
(pink `#FF4880` + blue `#4D65F9`). No gold anywhere.

---

## Quick start (no build step needed to view)

The site is **plain static HTML/CSS/JS** at the repository root:

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

Any static host works out of the box (GitHub Pages, Netlify, Vercel, cPanel, S3…).
jQuery and Bootstrap JS are **vendored locally** (`js/vendor/`), so core behaviour
runs with no CDN. (Web fonts + icon fonts still load from their CDNs.)

## Pages

| File | Purpose |
|---|---|
| `index.html` | Home — template order: hero → about (play button) → ministries (service cards) → programs → events → **KIZAZI on film** → blog → team → testimonial carousel → 4-column footer |
| `about.html` | Story (video panel + checklist), stats, mission/vision/values, verse band, CTA |
| `ministries.html` | The 8 ministry doorways (template service cards) + "what to expect" accordion |
| `programs.html` | 6 programs (template program cards) + Rooted 12-week journey |
| `events.html` | Next Friday (auto-dated), Conference 2027, Worship & Word Night, Campus Tour + KIZAZI 2026 photo mosaic |
| `gallery.html` | All 42 KIZAZI 2026 photos — filterable + lightbox — plus the **Videos** room |
| `blog.html` | Devotionals, recaps & practicals (cards + full posts) |
| `team.html` | Serving teams/roles + how to serve |
| `testimonial.html` | Voices from the family (initials only) + share-your-story |
| `contact.html` | Four ways in (form / Meet / socials / Linktree note), weekly schedule, FAQ — no invented email/phone/address |
| `404.html` | Template not-found page |

## Design system (the template's, unchanged)

- **Fonts** — Fredoka 600/700 (display) + Montserrat 200/400/600 (body), loaded
  from Google Fonts exactly like the zip.
- **Palette** — primary pink `#FF4880`, secondary blue `#4D65F9`, light
  `#FFECF2`, dark `#393D72`, body grey `#70747F` — i.e. the zip's own
  `css/bootstrap.min.css`, used as shipped. **No gold / no orange theme.**
- **Layout & components** — topbar + navbar with Pages dropdown, full-screen
  search modal, `hero-header` / `page-header` heroes with breadcrumbs, service /
  program / events / blog / team cards, Owl testimonial carousel, 4-column footer
  with the circular photo grid, copyright bar (right slot:
  "A generation on fire for God. — 1 Timothy 4:12"),
  back-to-top button, WOW scroll animations, Lightbox, pulsing play button.
- **KIZAZI add-ons** — `css/kizazi.css` (~150 lines, no new palette): teaches the
  template about vendored gallery photos/backgrounds (placeholder SVG as
  CSS last-resort), video cards, initials
  avatars, the gallery filter and quick-search results.
- **Behaviour** — `js/main.js` (the template's script: spinner, WOW, back-to-top,
  carousel, video modal) + `js/kizazi.js` (next-Friday
  dates, gallery filter, quick search, newsletter note — plus a JS last-resort
  placeholder for a broken photo).

## Photos

All 42 "KIZAZI 2026" event photos are **vendored in the repo** at
`img/gallery/01.jpg … 42.jpg` (same order as the `PHOTOS` list in
`tools/build_common.py`) and served locally — no hotlinking, no Drive
dependency at runtime. Each tag is plain:

```html
<img src="img/gallery/07.jpg" class="img-fluid" alt="…" loading="lazy">
```

Section backgrounds (hero, page headers, the play-button panel, footer) use the
same files through the inline `--kz-photo` CSS variable.
`img/brand/photo-placeholder.svg` remains only as the CSS/JS last-resort if a
file is ever missing.

### Refreshing the photos

The Drive file IDs stay registered in `PHOTOS` (`tools/build_common.py`).
To re-download them (or after editing `PHOTOS`), run on a machine with
internet access to Google Drive:

```bash
python3 tools/fetch_gallery_photos.py   # writes img/gallery/01.jpg … 42.jpg
git add img/gallery && git commit -m "Refresh KIZAZI 2026 photos"
```

The script probes the first ID and **refuses to run on HTTP 403/404** — share
the "KIZAZI 2026" folder as *"Anyone with the link → Viewer"* first. It falls
back across Drive hosts (`drive.google.com/thumbnail` →
`lh3.googleusercontent.com` → `drive.google.com/uc`) and verifies every file
is a real JPEG > 10 KB before writing it.

> No direct Google access (restricted sandbox / CI)? Two helpers:
> run `python3 tools/fetch_gallery_server.py` and open the served
> `/__fetch.html` page in a normal browser — it fetches the photos through
> the browser and writes them into `img/gallery/`. Or copy
> `tools/fetch-gallery-photos.workflow.yml` to `.github/workflows/` (needs a
> token with `workflows` write) and let GitHub Actions download and commit them.

## Videos (Drive)

Videos are embedded with Google Drive's own player (`/file/d/ID/preview`) in the
template's video modal, the **"KIZAZI On Film"** section on the home page and the
**Videos** room in the gallery. To publish films:

> **⚠️ Videos are still hotlinked from Google Drive — each video file must be
> shared as "Anyone with the link → Viewer"** or the embed will not load.
> (The vendored photos in `img/gallery/` do **not** need any sharing.)

1. Share each video file in Drive as *Anyone with the link → Viewer*.
2. Add one line per film to `VIDEOS` in `tools/build_common.py`:

   ```python
   VIDEOS = [
       ("1AbCdEfGhIjKlMnOpQrStUvWxYz", "KIZAZI 2026 — Highlight Film",
        "Two days that shook us.", 10, "Highlights"),
       # pasted share links work too:
       # ("https://drive.google.com/file/d/1AbC.../view", "Title", "Caption", 11, "Recap"),
   ]
   ```

   (ID or link, title, one-line caption, poster photo index, tag.)
3. Optionally set `DRIVE_ALBUM_URL` to the shared folder link — an
   "Open the Drive album" button then appears next to the gallery/watch sections.
4. Re-run `python3 tools/build.py`.

Until `VIDEOS` has entries, the play buttons link to TikTok and the film rooms
show an honest "film is being cut" panel — never a broken embed.

## Rebuilding pages (content lives in Python)

Pages are generated from shared-chrome scripts so the topbar/nav/footer stay
identical on all 11 pages:

```bash
python3 tools/build.py        # regenerates all 11 pages at the repo root
```

- `tools/build_common.py` — links, the 42 photo IDs (refresh registry), `VIDEOS`, ministries/programs/
  events/blog/teams/testimonies, and the shared chrome.
- `tools/build.py` — the per-page bodies, composed from the template's components.
- `tools/fetch_gallery_photos.py` — re-downloads `img/gallery/` from Drive.
- `tools/fetch_gallery_server.py` — browser-assisted fetcher (writes `img/gallery/`
  via `/__fetch.html`) for machines without direct Google access;
  `tools/fetch-gallery-photos.workflow.yml` is the CI variant.

Every content assumption is logged in [NOTES.md](NOTES.md) — please review it.

## Changing colours (optional)

The shipped `css/bootstrap.min.css` **is** the zip's. If you ever want a different
palette, edit `scss/bootstrap.scss` (the template's own variable file) and compile:

```bash
npx sass scss/bootstrap.scss css/bootstrap.min.css \
    --style=compressed --no-source-map --load-path=scss --quiet
```

(`scss/bootstrap/` holds the untouched Bootstrap 5 source the zip ships with.)

## Local checks

```bash
python3 -m http.server 8000   # then browse http://localhost:8000
python3 tools/check_html.py   # tag-balance validation for all 11 pages
```

## Deploy (Vercel)

- **One-click:** [Deploy with Vercel](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fwambetebenjamin%2Fkizazi-phenomenol)
- **Manual:** Vercel → *Add New Project* → import `wambetebenjamin/kizazi-phenomenol`
  → Framework **None** (static) → Build Command *(leave empty)* →
  Output Directory *(leave empty / repo root)* → Deploy.
- `vercel.json` configures `cleanUrls` and long cache headers for `/img`, `/css`, `/js`, `/lib`.
- After the first deploy, update the socials bio / Linktree with the live URL.

---

### Credits & licence

- Structure, fonts & palette: **BabyCare** daycare template by
  [HTML Codex](https://htmlcodex.com) (CC BY 4.0 — `LICENSE.txt` stays in the
  repo). The template credit line is **not** shown in the site footer — see the
  credit-removal note in [NOTES.md](NOTES.md).
- Photography & films: the "KIZAZI 2026" album — photos vendored in
  `img/gallery/`, films embedded from Drive.
- Copy: drafted for review — see [NOTES.md](NOTES.md).
