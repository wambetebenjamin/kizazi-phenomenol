# KIZAZI Phenomenal — Official Website

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fwambetebenjamin%2Fkizazi-phenomenol)


> A generation on fire for God. 🔥
> Youth-ministry movement serving **Kenya · Uganda · Tanzania · Rwanda**.

Built on the **BabyCare** Bootstrap template (HTML Codex) — completely recoloured,
re-typeset and re-imagined for a Gen-Z East-African audience.

---

## Quick start (no build step needed)

The site is **plain static HTML/CSS/JS**. Open `index.html` in a browser, or serve it:

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

Any static host works out of the box: GitHub Pages, Netlify, Vercel, cPanel, S3, etc.
jQuery and Bootstrap JS are **vendored locally** (`js/vendor/`), so there is no CDN
dependency for core behaviour.

## Pages

| File | Purpose |
|---|---|
| `index.html` | Home — hero, story, stats, ministries, programs, events, gallery, testimonies, CTA |
| `about.html` | Story, mission, vision, values, what we believe |
| `ministries.html` | The 8 ministry doorways |
| `programs.html` | Discipleship / mentorship / creative / campus tracks |
| `events.html` | Friday catch-up (live date auto-calculated), conference, tours |
| `gallery.html` | Filterable photo gallery with lightbox |
| `blog.html` | Devotionals, recaps & stories |
| `team.html` | Serving teams & how to join one |
| `testimonial.html` | Voices from the family |
| `contact.html` | Registration, socials, message form |
| `404.html` | Friendly not-found |

## Photos

Event photos live in the shared **Google Drive "KIZAZI 2026" folder** and are
hotlinked via Google's thumbnail CDN. Each image tag looks like:

```html
<img data-drive="FILE_ID" data-drive-w="1600" ...>
```

`js/kizazi.js` resolves `data-drive` → `drive.google.com/thumbnail`, then falls back to
`lh3.googleusercontent.com/d/…`, then `drive.google.com/uc`, then
`img/brand/photo-placeholder.svg`. **A broken link never shows a dead image.**

To use local copies instead (recommended for production/performance):
1. Download the photos into `img/photos/`.
2. Replace `data-drive="…"` with `src="img/photos/NAME.jpg"` (or re-map the `PHOTOS`
   list in `tools/build_common.py` to local paths and rebuild).

## Rebuilding pages

All pages share one chrome (topbar / navbar / footer). Edit content in
`tools/build.py`, then:

```bash
python3 tools/build.py
```

### Recompiling the theme (Bootstrap)

The palette lives in `scss/bootstrap.scss` (violet `#7C3AED`, gold `#FFC53D`,
ink `#16092F`). After editing:

```bash
cd tools && npm install        # once
npx sass --style=compressed --no-source-map --load-path=scss \
     scss/bootstrap.scss css/bootstrap.min.css
```

Custom youth styles that sit on top: `css/kizazi.css`. Behaviour layer: `js/kizazi.js`.

## Key links wired in

* **Registration** → https://forms.gle/vzRJrigBHCNormVA9
* **Friday Online Catch-Up** → https://meet.google.com/mcr-fupc-buw
* **TikTok** → @kizazi.phenomenal · **Instagram** → @kizazi_phenomenal · **Facebook** → kizaziphenomenal

See `NOTES.md` for content assumptions that the team should confirm.

## Deploy to Vercel (one click)

1. Click the **Deploy with Vercel** button above (or open
   `https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fwambetebenjamin%2Fkizazi-phenomenol`).
2. Sign in / connect your GitHub account when Vercel asks.
3. Vercel reads `vercel.json` (static site, no build step) — just press **Deploy**.
4. Production = `main` branch. Every future push to `main` redeploys automatically;
   every other branch/PR gets its own preview URL.
