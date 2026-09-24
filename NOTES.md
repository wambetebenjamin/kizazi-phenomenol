# Content notes & assumptions — PLEASE REVIEW

Everything below that is marked ⚠️ is a **drafting assumption** — edit it in
`tools/build_common.py` (data) or `tools/build.py` (layout/copy), then run
`python3 tools/build.py`.

## Confirmed from your brief / links

- Name: **KIZAZI Phenomenal** ("kizazi" = generation). Christian youth ministry /
  fellowship serving **Kenya, Uganda, Tanzania, Rwanda**.
- Registration form: `https://forms.gle/vzRJrigBHCNormVA9` — wired as the primary
  CTA everywhere (topbar, navbar, hero, programs, events, CTA bands, footer, contact).
- **Friday Online Catch-Up** — `https://meet.google.com/mcr-fupc-buw`, weekly,
  8:00 PM EAT — wired in topbar, hero, events, footer schedule, contact, 404.
- Socials — TikTok `@kizazi.phenomenal`, Instagram `kizazi_phenomenal`,
  Facebook `kizaziphenomenal` — wired in topbar, footer, team cards, contact, blog.
- **"Linktree coming soon"** — shown in the footer and on the contact page.
- Photos — the 42 file IDs of the **"KIZAZI 2026"** album, **vendored locally** as
  `img/gallery/01.jpg … 42.jpg` (registry in `PHOTOS`; refresh with
  `tools/fetch_gallery_photos.py` — see README). KIZAZI 2026 = **14–15 Aug 2026**, treated as the
  past flagship event and the gallery album.
- Verse used throughout: **1 Timothy 4:12**.
- No email, phone or physical address is invented anywhere — the contact page
  routes to the form, the Meet link and the socials.
- **Design (2026-09-24 v2, after "it looks bad" feedback):** first skin pass
  was too loud (heavy rounded display face, purple gradient pills). Re-tuned to
  Hilltop's actual stylesheet: steel blue `#0A3C63` structure, Poppins/Open
  Sans light weights, transparent white-uppercase nav over the photo that goes
  solid on scroll, thin outlined rectangular buttons, small radii, sage micro
  accents; purple kept only as a brand accent. Fonts/palette notes in README.
- **Design (2026-09-24, per your instruction):** the layout & theme now copy
  **hilltopcc.net's structure** (structure only — no photos or copy taken from
  that site): full-bleed crossfading photo hero with a centred "welcome to"
  block, photo page-banners with breadcrumbs, rounded photo cards, fixed photo
  bands, dark footer with a photo strip. The 42 event photos are organised by
  role (hero frames / banners / bands / cards / gallery / footer strip) so the
  backgrounds give the flat old layout its depth back. Softer frames were
  sharpened (unsharp scaled to a measured blur score) and upscaled so they hold
  up full-bleed. See `tools/process_photos.py` and the README "Photos".
- **Design (2026-09-20, per your instruction):** the site now uses the BabyCare
  zip's own structure and fonts (**Fredoka + Montserrat**). The palette was
  rebranded on 2026-09-21: the owner rejected the template pink, so it is now
  **royal purple `#6D28D9` / blue `#4D65F9`** (the earlier flame/gold skin was
  already gone). **No pink, no gold / flame-orange theme anywhere** (verified:
  zero such colour tokens in any shipped asset).

## ⚠️ Assumptions to confirm / replace

1. **Friday time** — copy says **8:00 PM EAT** (from your brief). The *date* shown
   on the site is **auto-calculated to the next Friday** (browser local time) and
   updates anywhere a `data-next-friday-*` attribute appears.
2. **Stats/counters** (about page) — "4 nations", "500+ young people reached",
   "8 ministries", "52 Fridays a year" are illustrative. Swap real numbers in
   `tools/build.py` (`build_about`, `stats` list).
3. **KIZAZI Conference 2027** — listed as "Aug 2027 · dates soon" (the next
   flagship placeholder). Replace with the real dates once announced.
4. **Programs** — *Rooted (12 weeks), Phenomenal Fridays, KIZAZI Creative Lab,
   Mentorship Circle, Campus Ambassadors, Serve East Africa* plus the rate badges
   and the 3-item meta bars are proposed structures — rename/replace to match what
   actually runs. The Rooted week-by-week phases are drafted too.
5. **Ministries** — the 8 names and their copy are drafted from your list —
   adjust the blurbs/"what to expect" bullets as needed.
6. **Gallery categories** — the album has no labels, so the 6 filter categories
   (Worship / Word / Community / Service / Creative / Behind the Scenes) are
   assigned **round-robin** in `tools/build_common.py` (`GALLERY_CATS`). If you
   label the photos, update the mapping.
7. **Blog posts** — three drafted posts (1 Timothy 4:12 devotional, KIZAZI 2026
   recap, "5 habits" practical) with dates in Aug–Sep 2026. Titles, dates and
   bodies are placeholders until you write/confirm the real ones.
8. **Team page** — now has three layers: the **featured Patron panel**
   (Reverend Dr. Joslyn Isigi), the **admin team portrait cards**
   (`PEOPLE`) and the **serving teams/roles** with KIZAZI 2026 event photos
   (`TEAMS`). Add the real admin names/portraits in `tools/build_common.py`
   once you send them; the cards skip anyone without a JPEG in `img/team/`.
9. **Testimonies** — four quotes, **initials only** (K., A., M., T.), labelled
   "joined online, Kampala", "Campus Ambassador", "Rooted graduate",
   "first-year student" — all **illustrative**. Replace with real, consented
   testimonies before going public.
10. **Weekly schedule (footer/contact)** — only Friday is asserted (8:00 PM EAT);
    the weekday row says "cells, prayer & campus visits (schedule shared weekly)"
    without inventing fixed days. Add real recurring days when you have them.
11. **Worship & Word Night / Campus & School Tour cadence** — "monthly" and
    "termly" are drafted rhythms.
12. **Newsletter form (footer)** — decorative (shows a thank-you note); no emails
    are collected/stored. Wire it to a real service (or remove) before relying on it.
13. **Videos** — `VIDEOS` in `tools/build_common.py` is **empty until you paste
    Drive file IDs / share links** (see README → "Videos (Drive)"). Until then the
    play buttons link to TikTok and the film rooms show a "being cut" panel.
    Also set `DRIVE_ALBUM_URL` if you want the "Open the Drive album" button.
14. **Search modal** — the template's full-screen search is wired to a small
    client-side index of page titles, card titles and accordion headings. It is
    intentionally simple; replace with a real search service if the site grows.
15. **og:image** — uses the relative `img/brand/logo-mark.png`; after deploying,
    set an absolute URL (and a 1200×630 hero image) for better social previews.

## Photos & privacy

- **2026-09-24:** the vendored 42 were **re-curated from the event archive
  zips** committed at the repo root (`drive-download-*.zip`, 220 JPEGs / 217
  unique), because the sandbox has no route to Google Drive and the previous
  `img/gallery/` set was not in this checkout. Curation rules: unique frames,
  a balance of stage/worship, crowd, outdoor and portrait shots, one photo per
  role per page, and a sharpen pass scaled to each frame's measured blur score
  (Laplacian std-dev at 512 px). The mapping lives in `CURATED` in
  `tools/process_photos.py`; if you'd rather have a different 42 (e.g. the
  exact original Drive album), edit that table or run
  `tools/fetch_gallery_photos.py` somewhere with Drive access and re-run the
  build.
- **2026-09-21:** the 42 "KIZAZI 2026" photos are **vendored in the repo** at
  `img/gallery/01.jpg … 42.jpg` (downloaded at w1600, same order as `PHOTOS`),
  committed as binaries with `img/gallery/manifest.json` (Drive ID, SHA-256
  and byte size per photo, in `PHOTOS` order). Every page serves them
  locally; the Drive hotlink / JS fallback chain is gone, so the site never
  hotlinks Drive for photos.
- Refresh paths (details in README → "Photos"): `tools/fetch_gallery_photos.py`
  is manifest-aware (a re-run on an unchanged album re-downloads nothing and
  commits nothing; `--force` re-downloads all 42, `--changed-out FILE` lists
  the changed names for commit messages, `--manifest-only` rebuilds the
  manifest from local files, `--verify` checks 42 real JPEGs > 10 KB with
  hashes matching the manifest, completely offline). For sandboxes with no
  route to Google there is the browser-assisted
  `python3 tools/fetch_gallery_server.py 8123 --fetch-root`. The automated
  path is the GitHub Actions workflow
  `.github/workflows/fetch-gallery-photos.yml` (weekly, Mondays 06:30 UTC, and
  on demand): same script, verifies, commits `img/gallery/` only when
  something changed. No secrets; the job needs `contents: write` on the
  default `GITHUB_TOKEN`.
- The script probes the first ID and refuses to run if the album is not
  shared as "Anyone with the link → Viewer" — that sharing requirement now
  applies to **videos only** (they are still Drive embeds).
- All gallery photos show identifiable people. **Confirm you have consent to
  publish them publicly** before going live. To pull any photo, delete its
  file in `img/gallery/` and remove its ID from `PHOTOS` in
  `tools/build_common.py` (then re-run `python3 tools/fetch_gallery_photos.py
  --manifest-only` and `python3 tools/fetch_gallery_photos.py --verify`).

## Home hero: the transition photos (2026-09-21)

- The four photos uploaded for "the top of the first page" are vendored in
  `img/hero/01.jpg` to `img/hero/04.jpg` (the
  `front page transition pages .zip` upload was unpacked and removed; no other
  file in the repo changed). The originals are WhatsApp JPEGs, 1600 x 718.
- They are embedded as a **crossfading hero background** on `index.html` only:
  one `.kz-hero-slide` layer per file, staggered 8 s each (32 s cycle), under
  the template's existing blue wash so the hero copy keeps its contrast.
  `prefers-reduced-motion` and no-JS visitors see `img/hero/01.jpg` as a still,
  and `img/brand/photo-placeholder.svg` stays the CSS last-resort.
- The CSS lives in section 7 of `css/kizazi.css`; the list is `HERO_SLIDES` in
  `tools/build_common.py`. Swap a file (keep the name) or change the list and
  adjust the 32 s cycle + keyframe percentages to match.

## People, portraits & the Patron (2026-09-21)

- **Consent: confirmed by the site owner for every portrait published here**
  (the owner supplied the portrait files and asked for them to be published).
  Only replace or remove them if that consent changes, and keep this note in
  sync.
- Portraits are vendored in `img/team/` and driven by `PEOPLE` (admin team) and
  `PATRON` (Reverend Dr. Joslyn Isigi) in `tools/build_common.py`. Roles are
  written exactly as **"Admin"** and **"Patron"**; no other titles are invented.
- `team.html` shows the Patron as a featured panel plus the admin cards;
  `about.html` shows the compact Patron panel in the mission area. An entry
  whose JPEG is missing is skipped by the builder, so pages never show a broken
  portrait.
- To pull a person: delete their file in `img/team/` and their entry in
  `tools/build_common.py`, then re-run `python3 tools/build.py`.

## Energy layer (2026-09-21)

The site's young/energetic feel is one documented layer, kept and extended
from here on. It lives in **section 9 of `css/kizazi.css`** and in
`js/kizazi.js` (behaviours 6 and 7), additive on the BabyCare skin: nothing
template-visible was removed.

- **Palette and fonts are fixed** (royal purple rebrand, 2026-09-21): violet
  `#6D28D9` / blue `#4D65F9`, Fredoka + Montserrat. **No pink, no gold, no
  `#FFC53D`, no flame-orange anywhere.** New accents only through the one
  gradient token below.
- **One gradient token** — `--kz-grad:
  linear-gradient(120deg, #6D28D9, #F3E8FF 50%, #4D65F9)` (violet → light
  violet → blue, all from the template's own CSS variables). It is the only
  new accent, and it paints: the buttons (`.btn-primary` / `.btn-secondary`,
  with the template's blue/violet hover inversion kept on top), the sticker
  kicker pills, the about-page stat numerals (`.kz-stat-num`), the marquee
  rules, the copyright rule and the scroll progress bar.
- **Marquee ticker** under the navbar on every page: the phrases live in
  `TICKER` (`tools/build_common.py`), repeated exactly twice in the DOM so
  the CSS -50% translate loop is seamless; it pauses on hover and is
  `aria-hidden` (decorative reinforcement of copy that lives on the pages).
- **Sticker kickers**: the template's `h4.title-border-radius` section
  kickers are now white, slightly tilted (rotate -1.5deg) pills carrying a
  gradient rule underneath (the template's old 2px primary-colour underline is
  neutralised).
- **Lifting/tilting cards**: `.service-item`, `.program-item`,
  `.events-item`, `.blog-item`, `.team-item`, the gallery tiles and the hero
  moments lift and tilt on hover. Transform + shadow only; the template's
  own inner hover effects (icon inversion, image zoom, event overlay) keep
  working.
- **Counting stats**: the about-page stat numerals carry `data-kz-count`
  (and `data-kz-suffix` for the "+") and count up (ease-out cubic, 1.2s)
  when they scroll into view. The final value stays in the markup, so no-JS
  visitors read the real number and reduced-motion visitors skip the count.
  (The numbers themselves are still the illustrative ones, see
  Assumptions #2.)
- **Scroll progress bar**: fixed 4px gradient rule at the very top of the
  viewport, driven by `transform: scaleX()` only (rAF-throttled, passive
  listeners). No layout shift.
- **Pulsing play button**: the template's pulse ring (its own
  `pulse-border` animation) is re-inked in the gradient token.
- **Honest motion**: every animation here is transform/opacity only (no
  layout shift), and the `prefers-reduced-motion: reduce` block at the end
  of `css/kizazi.css` switches the marquee, the card motion and the play
  pulse off (and `js/kizazi.js` checks the same media query to skip the
  count-up). The progress bar is the one element kept, because it mirrors
  the user's own scrolling instead of running on its own.
- **New copy** (the ticker phrases) follows the house rules: short lines,
  second person, verbs first, no dashes.

## Dash policy (2026-09-21)

- **No em-dashes (`&mdash;`, `—`) and no en-dashes (`&ndash;`, `–`) anywhere in visible
  copy.** They were rewritten with plain punctuation (comma, colon, full stop,
  or just a space) and date ranges now read "14 to 15 August". Word hyphens stay
  (`catch-up`, `follow-up`).
- The copyright bar's right-hand slot reads exactly
  **"A generation on fire for God. 1 Timothy 4:12"** (the removed template credit
  is documented below).
- Proof: `grep -n "&mdash;\|&ndash;\|—\|–" tools/*.py` prints nothing and every generated
  `*.html` page is clean. The only dashes left in the repo are inside the
  untouched third-party template files (`css/bootstrap.min.css`,
  `css/style.css`, `js/vendor/*`, `lib/*`), which are not site copy. The
  font rules are unchanged: Fredoka + Montserrat. The palette is the royal
  purple rebrand (2026-09-21): violet `#6D28D9` / blue `#4D65F9`, and no pink,
  gold or flame-orange anywhere.

## Design decisions (not copy, but easy to change)

- **Structure/fonts/palette = the zip's.** Pages are generated from the template's
  own components (topbar+navbar+dropdown, search modal, hero/page-header, service,
  program, events, blog, team cards, Owl testimonial carousel, 4-column footer,
  copyright, back-to-top). Fredoka + Montserrat; violet `#6D28D9` / blue `#4D65F9`.
- `css/bootstrap.min.css` and `css/style.css` come from **BabyCare-1.0.0.zip**,
  with the pink hexes swapped in place for the royal purple rebrand
  (2026-09-21); `scss/bootstrap.scss` + `scss/bootstrap/` are the zip's
  sources if you ever recompile.
- `css/kizazi.css` is a small add-on layer (photo backgrounds via `--kz-photo`
  with the placeholder SVG as CSS last-resort, video
  cards, initials avatars, gallery filter, search results) that only uses the
  template's CSS variables — no new palette.
- `js/main.js` is the template's script (with one tweak: Drive embeds are used
  as-is instead of getting YouTube autoplay params). `js/kizazi.js` adds
  next-Friday dates, gallery filter, quick search
  and the newsletter note (plus a JS last-resort placeholder for a broken
  photo) — the old Drive photo/background resolution chain was deleted when the
  photos were vendored.
- Logo: AI-generated flame-"K" badge in the royal purple palette (violet→blue, no gold)
  at `img/brand/logo-mark.png` (favicon + og:image). The navbar/footer brand is
  the template's two-tone text wordmark. Regenerate/replace freely.
- **HTML Codex credit-removal note (2026-09-21):** the template credit line
  ("Designed By HTML Codex / Distributed By ThemeWagon", plus its "keep the
  credit" comment) is **deliberately removed from the copyright bar**. The
  right-hand slot now reads **"A generation on fire for God. 1 Timothy 4:12"**.
  Do **not** re-add any template credit line. `LICENSE.txt` stays in the repo.
