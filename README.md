# KIZAZI Phenomenal — Official Website

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fwambetebenjamin%2Fkizazi-phenomenol)

> **A generation on fire for God.** 🔥
> Christian youth ministry / fellowship serving **Kenya · Uganda · Tanzania · Rwanda**.
> *"Let no one despise you for your youth…"* — 1 Timothy 4:12

Built **on the BabyCare Bootstrap template (HTML Codex) exactly as shipped**: same
page structure, same components, same fonts and the template's palette shape,
rebranded to royal purple (`#6D28D9` + blue `#4D65F9`). No gold anywhere.

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
| `team.html` | Featured Patron panel, admin team portraits, serving teams/roles + how to serve |
| `testimonial.html` | Voices from the family (initials only) + share-your-story |
| `contact.html` | Four ways in (form / Meet / socials / Linktree note), weekly schedule, FAQ — no invented email/phone/address |
| `404.html` | Template not-found page |

## Design system (Hilltop skin, 2026-09-24)

The layout & theme now follow **hilltopcc.net's structure** (structure only —
every photo is KIZAZI's own): full-bleed crossfading photo hero with a centred
"welcome to" block, transparent white-uppercase nav over the photo (solid
steel blue once scrolled), blue-gradient photo page banners with breadcrumbs,
rectangular photo cards with hover lift/zoom, fixed-attachment photo bands
(verse / follow / join-the-team), and a steel-blue footer with a photo strip.
All of it lives in `css/kizazi.css`; `css/style.css` and
`css/bootstrap.min.css` remain as the base layer.

- **Fonts** — Poppins 300/400/500/600 (display, uppercase, light weights) +
  Open Sans 300/400/600 (body): the same pairing hilltopcc.net loads.
- **Palette (v2, after owner feedback)** — Hilltop's steel blue `#0A3C63` is
  the structural colour (header, banners, footer, chips) with light-blue
  `#B1D5E6` accents on dark and a touch of sage `#75A799`; KIZAZI's royal
  purple `#6D28D9` survives only as the brand accent (logo word, kickers,
  primary CTA, links). Buttons are thin rectangles (3px radius), solid or
  1-2px outlined — no gradient pills.
- **Palette (royal purple rebrand, 2026-09-21)** — primary violet `#6D28D9`
  (hover `#5B21B6`), secondary blue `#4D65F9`, light `#F3E8FF`, dark `#393D72`,
  body grey `#70747F`. The owner rejected the template pink, so the swap was
  applied in place to the zip's own `css/bootstrap.min.css` / `css/style.css`
  (and `scss/bootstrap.scss`). **No pink, no gold / no orange theme.**
- **Layout & components** — dark utility strip + sticky white header with
  Pages dropdown, full-screen search modal, crossfading `ht-hero` on the home
  page, `ht-banner` photo page headers with breadcrumbs, "join us friday"
  split card, what's-happening event cards, "get connected" photo tiles,
  fixed photo bands, program/ministry/blog/team cards, Owl testimonial
  carousel, 4-column dark footer with the `ht-fstrip` photo grid, copyright
  bar, back-to-top button, WOW scroll animations, Lightbox gallery.
- **KIZAZI add-ons** — `css/kizazi.css` is the whole skin (no new palette):
  it organises the vendored photos by role (hero frames, banners, bands,
  cards, gallery, footer strip) through the inline `--kz-photo` variable,
  with `img/brand/photo-placeholder.svg` kept only as the JS last-resort if a
  file is ever missing.
- **Motion** — one gradient token, `--kz-grad` (violet → blue, **no gold / no
  orange**), worn by buttons, kicker pills, card tags and the scroll progress
  bar. Cards lift on hover, stats count up (`data-kz-count`), the hero
  crossfades its four frames. Motion stays honest: transform/opacity only, no
  layout shift, and every autonomous animation is off under
  `prefers-reduced-motion` (hero crossfade and scroll hint in `css/kizazi.css`).
- **Behaviour** — `js/main.js` (the template's script: spinner, WOW, back-to-top,
  carousel, video modal) + `js/kizazi.js` (next-Friday dates, gallery filter,
  quick search, newsletter note, scroll progress bar, counting stats — plus
  a JS last-resort placeholder for a broken photo).

## Photos

All 42 "KIZAZI 2026" event photos are **vendored in the repo** at
`img/gallery/01.jpg … 42.jpg` and served locally — no hotlinking, no Drive
dependency at runtime. Since 2026-09-24 the 42 are **curated from the event
archive zips** (`drive-download-*.zip`, 220 shots) by
`tools/process_photos.py`: each chosen frame is upscaled (Lanczos, 1400 px
long side), brightened slightly and **unsharp-masked in proportion to its
measured blur score**, so full-bleed backgrounds read sharp instead of soft.
The curation (zip entry → gallery index, plus sharpness score) is the
`CURATED` table in that script; re-run `python3 tools/process_photos.py
--force` after editing it. Each tag is plain:

```html
<img src="img/gallery/07.jpg" class="img-fluid" alt="…" loading="lazy">
```

Section backgrounds (page headers, the play-button panel, footer) use the same
files through the inline `--kz-photo` CSS variable.
`img/brand/photo-placeholder.svg` remains only as the CSS/JS last-resort if a
file is ever missing.

### Home hero (the transition photos)

The top of `index.html` crossfades through the four frames vendored in
`img/hero/` (`01.jpg` to `04.jpg`) behind the hero copy: one `.ht-slide` layer
per file, staggered 7 s each so the four-photo cycle is 28 s (`.ht-hero` block
of `css/kizazi.css`). The frames are sharpened 1600×900 centre crops derived
from gallery photos 01, 07, 02 and 12 (`HERO` table in
`tools/process_photos.py`). Under `prefers-reduced-motion` the first frame is
shown as a still. To swap a frame, edit the `HERO` table and re-run
`process_photos.py --force`; to change the number of slides, edit
`HERO_SLIDES` in `tools/build_common.py` and the stagger/`htFade` keyframes in
`css/kizazi.css` to match.

### People (portraits)

`img/team/` holds the consented portraits of the named people: the admin team
and the Patron, **Reverend Dr. Joslyn Isigi**. They are driven by the `PEOPLE`
and `PATRON` entries in `tools/build_common.py`:

- `team.html` shows the Patron as a featured panel right under the page header,
  then the admins as template `team-item` cards (role reads simply "Admin"; no
  invented titles), then the serving-team role cards.
- `about.html` shows the compact Patron panel in the mission area.

To add or replace a person: drop `img/team/<slug>.jpg` (portrait crop, roughly
4:5, at least 700 px wide), add or point the entry in `PEOPLE` / `PATRON`, then
re-run `python3 tools/build.py`. Entries whose JPEG is missing are skipped
entirely, so the build never emits a broken portrait. Consent to publish is
logged in [NOTES.md](NOTES.md).

### Refreshing the photos

The current 42 are the curated + sharpened set produced by
`tools/process_photos.py`; `img/gallery/manifest.json` now records, per
photo, the source zip, source file name, sharpness score, SHA-256 and byte
size. Commit the JPEGs **and** the manifest together.

The Drive file IDs remain registered in `PHOTOS` (`tools/build_common.py`)
as the historical album registry. `tools/fetch_gallery_photos.py` still
downloads that original album (in `PHOTOS` order) if you ever want it back —
note that doing so replaces the curation and its role mapping, so re-check
the hero/banner picks in `tools/build.py` afterwards.

```bash
python3 tools/fetch_gallery_photos.py            # manifest-aware refresh:
                                                 # skips photos whose bytes
                                                 # already match the manifest
python3 tools/fetch_gallery_photos.py --force \
    --changed-out /tmp/changed.txt               # re-download all 42 and
                                                 # list the ones that changed
python3 tools/fetch_gallery_photos.py --verify   # offline: 42 real JPEGs
                                                 # > 10 KB, hashes match the
                                                 # manifest, order matches PHOTOS
python3 tools/fetch_gallery_photos.py --manifest-only   # rebuild the manifest
                                                 # from files already on disk
                                                 # (browser-assisted route)
```

A re-run on an unchanged album is a no-op: zero re-downloads, zero diff,
nothing to commit. The script probes the first ID and **refuses to run on
HTTP 403/404** — share the "KIZAZI 2026" folder as *"Anyone with the link
→ Viewer"* first. It falls back across Drive hosts
(`drive.google.com/thumbnail` → `lh3.googleusercontent.com` →
`drive.google.com/uc`) and verifies every file is a real JPEG > 10 KB before
writing it.

**Automated:** `.github/workflows/fetch-gallery-photos.yml` (source template
`tools/fetch-gallery-photos.workflow.yml`) runs the same script on a weekly
schedule (Mondays 06:30 UTC) and on demand (`workflow_dispatch`), verifies,
and commits `img/gallery/` **only when something changed** (the commit
message lists the changed photo names from `--changed-out`). No secrets are
needed: the album is public via link sharing and the job declares
`contents: write` on the default `GITHUB_TOKEN`.

> No direct Google access (restricted sandbox / CI)? Run
> `python3 tools/fetch_gallery_server.py 8123 --fetch-root` and open the
> served page (the preview of port 8123) in a normal browser, then click
> "Fetch all 42 photos": your browser downloads each photo and POSTs it
> back, writing `img/gallery/01.jpg … 42.jpg`. When it is done, run
> `python3 tools/fetch_gallery_photos.py --manifest-only` and then
> `python3 tools/fetch_gallery_photos.py --verify`.

## Copy conventions

- **No em-dashes or en-dashes in visible copy.** They are rewritten with plain
  punctuation (comma, colon, full stop) and date ranges read "14 to 15 August".
  Word hyphens stay (`catch-up`, `follow-up`).
  Proof: `grep -n "&mdash;\|&ndash;\|—\|–" tools/*.py` prints nothing, and the
  generated `*.html` pages are clean too. (The untouched third-party template
  files under `css/`, `js/vendor/` and `lib/` are not part of the copy.)
- **Family description** (exact copy; the last two words are italic):
  *We are on a mission to grow stronger, connect deeper, and shine brighter as
  Ministers' Kids*. It lives in `FAMILY_DESC` / `FAMILY_DESC_HTML`
  (`tools/build_common.py`) and appears in the home hero, the home about block,
  the about page story and mission area, the Patron panel and the footer.
- Verse stays **1 Timothy 4:12**: in full on the about page, short in the footer
  and in the copyright bar ("A generation on fire for God. 1 Timothy 4:12").

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

- `tools/build_common.py` — links, the 42 photo IDs (refresh registry), `VIDEOS`, the hero
  `HERO_SLIDES`, the `FAMILY_DESC` copy, the `PEOPLE`/`PATRON` portraits,
  ministries/programs/events/blog/teams/testimonies, and the shared chrome.
- `tools/build.py` — the per-page bodies, composed from the template's components.
- `tools/fetch_gallery_photos.py` — refreshes `img/gallery/` + the manifest
  from Drive (manifest-aware, `--force`, `--changed-out`, `--manifest-only`,
  `--verify`).
- `tools/fetch_gallery_server.py` — browser-assisted fetcher (serves the
  fetch page at `/` with `--fetch-root`) for machines without a route to
  Google; `tools/fetch-gallery-photos.workflow.yml` is the CI variant, live
  at `.github/workflows/fetch-gallery-photos.yml` (weekly + on demand).

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
