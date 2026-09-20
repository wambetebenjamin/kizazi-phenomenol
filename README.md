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
  with the circular photo grid, copyright bar with the HTML Codex credit,
  back-to-top button, WOW scroll animations, Lightbox, pulsing play button.
- **KIZAZI add-ons** — `css/kizazi.css` (~150 lines, no new palette): teaches the
  template about hotlinked Drive photos/backgrounds, video cards, initials
  avatars, the gallery filter and quick-search results.
- **Behaviour** — `js/main.js` (the template's script: spinner, WOW, back-to-top,
  carousel, video modal) + `js/kizazi.js` (Drive photo resolution, next-Friday
  dates, gallery filter, quick search, newsletter note).

## Photos

All 42 event photos live in the public **Google Drive "KIZAZI 2026" album** and are
hotlinked — nothing is downloaded into the repo. Each tag looks like:

```html
<img data-drive="FILE_ID" data-drive-w="1600" class="img-fluid" alt="…">
```

`js/kizazi.js` resolves each one through a fallback chain:

1. `https://drive.google.com/thumbnail?id=ID&sz=w1600`
2. `https://lh3.googleusercontent.com/d/ID=w1600`
3. `https://drive.google.com/uc?export=view&id=ID`
4. `img/brand/photo-placeholder.svg` (local placeholder, last resort)

Section backgrounds (hero, page headers, the play-button panel, footer) use the
same chain via `data-drive-bg` + a `--kz-photo` CSS variable.

> **⚠️ The album must be shared as "Anyone with the link → Viewer"** (folder *and*
> each file) or every photo silently falls back to the branded placeholder.
> The registry of all 42 IDs is in `tools/build_common.py` (`PHOTOS`).

## Videos (Drive)

Videos are embedded with Google Drive's own player (`/file/d/ID/preview`) in the
template's video modal, the **"KIZAZI On Film"** section on the home page and the
**Videos** room in the gallery. To publish films:

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

- `tools/build_common.py` — links, the 42 photo IDs, `VIDEOS`, ministries/programs/
  events/blog/teams/testimonies, and the shared chrome.
- `tools/build.py` — the per-page bodies, composed from the template's components.

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
  [HTML Codex](https://htmlcodex.com) (CC BY 4.0 — credit retained in the footer,
  per the template licence in `LICENSE.txt`).
- Photography & films: the public "KIZAZI 2026" Google Drive album (hotlinked).
- Copy: drafted for review — see [NOTES.md](NOTES.md).
