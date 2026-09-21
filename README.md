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
| `team.html` | Featured Patron panel, admin team portraits, serving teams/roles + how to serve |
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
- **KIZAZI add-ons** — `css/kizazi.css` (no new palette): teaches the
  template about vendored gallery photos/backgrounds (placeholder SVG as
  CSS last-resort), video cards, initials avatars, the gallery filter,
  quick-search results, the home hero crossfade and the energy layer below.
- **Energy layer** (section 9 of `css/kizazi.css` + behaviours 6-7 of
  `js/kizazi.js`) — one gradient token, `--kz-grad` (pink → light pink → blue,
  the template's own colours, **no gold / no orange**), worn by the buttons,
  the sticker kicker pills, the about-page stat numerals, the marquee rules,
  the copyright rule and the scroll progress bar. Plus the marquee ticker
  under the navbar (phrases in `TICKER`, `tools/build_common.py`),
  lifting/tilting cards, counting stats (`data-kz-count`) and the pulsing
  play-button ring. Motion stays honest: transform/opacity only, no layout
  shift, and every animation is off under `prefers-reduced-motion` (the block
  at the end of `css/kizazi.css`).
- **Behaviour** — `js/main.js` (the template's script: spinner, WOW, back-to-top,
  carousel, video modal) + `js/kizazi.js` (next-Friday dates, gallery filter,
  quick search, newsletter note, scroll progress bar, counting stats — plus
  a JS last-resort placeholder for a broken photo).

## Photos

All 42 "KIZAZI 2026" event photos are **vendored in the repo** at
`img/gallery/01.jpg … 42.jpg` (same order as the `PHOTOS` list in
`tools/build_common.py`) and served locally — no hotlinking, no Drive
dependency at runtime. Each tag is plain:

```html
<img src="img/gallery/07.jpg" class="img-fluid" alt="…" loading="lazy">
```

Section backgrounds (page headers, the play-button panel, footer) use the same
files through the inline `--kz-photo` CSS variable.
`img/brand/photo-placeholder.svg` remains only as the CSS/JS last-resort if a
file is ever missing.

### Home hero (the transition photos)

The top of `index.html` crossfades through the four photos vendored in
`img/hero/` (`01.jpg` to `04.jpg`) behind the hero copy: one `.kz-hero-slide`
layer per file, staggered 8 s each so the four-photo cycle is 32 s (section 7 of
`css/kizazi.css`). The first file is also the still `--kz-photo` base layer, so
no-JS and `prefers-reduced-motion` visitors still get a real photo. To swap a
photo, replace the file keeping its name and re-run the build. To change the
number of photos, edit `HERO_SLIDES` in `tools/build_common.py` and update the
cycle + keyframe percentages in `css/kizazi.css` to match.

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

The Drive file IDs stay registered in `PHOTOS` (`tools/build_common.py`) and
the committed bytes in `img/gallery/manifest.json` (Drive ID, SHA-256 and
byte size per photo, in `PHOTOS` order). Commit the JPEGs **and** the
manifest together.

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
