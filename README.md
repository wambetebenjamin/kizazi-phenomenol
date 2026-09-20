# KIZAZI Phenomenal — Official Website

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fwambetebenjamin%2Fkizazi-phenomenol)

> **A generation on fire for God.** 🔥
> Christian youth ministry / fellowship serving **Kenya · Uganda · Tanzania · Rwanda**.
> *"Let no one despise you for your youth…"* — 1 Timothy 4:12

Built on the **BabyCare** Bootstrap template (HTML Codex) — completely recoloured,
re-typeset and re-skinned for a bold, Gen-Z East-African audience.

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
| `index.html` | Home — hero → story (play button) → ministries → programs → events → blog → teams → testimonial carousel → 4-column footer |
| `about.html` | Story, verse band, stats, mission/vision/values, beliefs |
| `ministries.html` | The 8 ministry doorways (3D flip cards) |
| `programs.html` | 6 programs + Rooted 12-week timeline |
| `events.html` | Next Friday (auto-dated), KIZAZI Conference 2027, Worship & Word Night, Campus Tour, KIZAZI 2026 recap |
| `gallery.html` | All 42 KIZAZI 2026 photos — filterable + lightbox |
| `blog.html` | Devotionals, recaps & practicals |
| `team.html` | Serving teams/roles (initial tiles) + how to serve |
| `testimonial.html` | Voices from the family (initials only) |
| `contact.html` | Registration, Friday Meet, socials, FAQ — no invented email/phone/address |
| `404.html` | Friendly not-found |

## Design system

- **Palette** — flame orange-red `#F4511E` · phenomenal gold `#FFC53D` ·
  magenta `#FF2E6E` / coral `#FF7A45` sunset gradients · warm dark ink `#201108`.
  `css/bootstrap.min.css` is **recompiled from the template's `scss/` source**
  with these tokens (see “Rebuilding Bootstrap” below).
- **Type** — Sora (display) · Plus Jakarta Sans (body) · Caveat (handwritten accents).
- **Energetic layer** — `css/kizazi.css`: aurora orbs, drifting dot-grid,
  shine-sweep gradient buttons, 3D flip cards, rate badges + leader rows + dark
  meta bars on program cards, circular event photos with floating date badges,
  gradient photo rings on hover, sparkles/glows, marquee ticker, zigzag dividers,
  pulsing play button, scroll-reveal, animated counters, auto-calculated
  **next-Friday** dates. All motion respects `prefers-reduced-motion`.
- **Behaviour layer** — `js/kizazi.js` (photo resolution, dates, counters,
  reveal, carousel, lightbox, gallery filter, chrome).
- **Logo** — flame-“K” mark at `img/brand/logo-mark.png` (also the favicon).

## Photos

All 42 event photos live in the public **Google Drive “KIZAZI 2026” album** and are
hotlinked — nothing is downloaded into the repo. Each tag looks like:

```html
<img data-drive="FILE_ID" data-drive-w="1600" class="img-fluid" alt="…">
```

`js/kizazi.js` resolves each one through a fallback chain:

1. `https://drive.google.com/thumbnail?id=ID&sz=w1600`
2. `https://lh3.googleusercontent.com/d/ID=w1600`
3. `https://drive.google.com/uc?export=view&id=ID`
4. `img/brand/photo-placeholder.svg` (local placeholder, last resort)

The registry of all 42 IDs is in `tools/build_common.py` (`PHOTOS`).

> **⚠️ The album is currently NOT publicly shared** (as of 2026-09-20), so every
> photo silently falls back to the branded placeholder tile. To make the real
> photos appear: in Drive, open the “KIZAZI 2026” album folder → **Share** →
> “Anyone with the link” → **Viewer**, on the folder *and* each file. No code
> changes needed — the hotlinks start working on their own. (Drive also rate
> limits `thumbnail` URLs under heavy load; that's a known, harmless hiccup.)

## Rebuilding pages (content lives in Python)

Pages are generated from shared-chrome scripts so the nav/footer stay identical
on all 11 pages:

```bash
python3 tools/build.py        # regenerates all 11 pages at the repo root
```

- `tools/build_common.py` — links, the 42 photo IDs, ministries/programs/events/
  blog/teams/testimonies, and the shared head/topbar/navbar/footer/copyright.
- `tools/build.py` — the per-page bodies.

Edit the data in `build_common.py`, run the script, refresh. Every content
assumption is logged in [NOTES.md](NOTES.md) — please review it.

## Rebuilding Bootstrap (palette)

`css/bootstrap.min.css` is compiled from the template's SCSS source with the
KIZAZI tokens defined in `scss/kizazi-bootstrap.scss`:

```bash
cd tools
npm install
./node_modules/.bin/sass \
    ../scss/kizazi-bootstrap.scss ../css/bootstrap.min.css \
    --style=compressed --no-source-map --load-path=../scss --quiet
```

## Local checks

```bash
python3 -m http.server 8000   # then browse http://localhost:8000
```

HTML tag-balance validation for all pages:

```bash
python3 tools/check_html.py
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

- Structure: **BabyCare** daycare template by [HTML Codex](https://htmlcodex.com)
  (CC BY 4.0 — credit retained in the footer, per the template licence in
  `LICENSE.txt`).
- Photography: the public “KIZAZI 2026” Google Drive album (hotlinked).
- Copy: drafted for review — see [NOTES.md](NOTES.md).
