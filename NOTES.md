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
- **Design (2026-09-20, per your instruction):** the site now uses the BabyCare
  zip's own structure, fonts (**Fredoka + Montserrat**) and palette
  (**pink `#FF4880` / blue `#4D65F9`**) — the previous flame/gold skin is gone.
  **No gold / flame-orange theme anywhere** (verified: zero gold or orange
  colour tokens in any shipped asset).

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

- **2026-09-21:** the 42 "KIZAZI 2026" photos are now **vendored in the repo** at
  `img/gallery/01.jpg … 42.jpg` (downloaded at w1600, same order as `PHOTOS`).
  Every page serves them locally; the Drive hotlink / JS fallback chain is gone.
  To refresh them (or after editing `PHOTOS`), run
  `python3 tools/fetch_gallery_photos.py` on a machine with internet access to
  Google Drive and commit the JPEGs. The script refuses to run if the album is
  not shared as "Anyone with the link → Viewer" — that sharing requirement now
  applies to **videos only** (they are still Drive embeds).
- All gallery photos show identifiable people. **Confirm you have consent to
  publish them publicly** before going live. To pull any photo, delete its file
  in `img/gallery/` and remove its ID from `PHOTOS` in `tools/build_common.py`.

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
  font/palette rules are unchanged: Fredoka + Montserrat, pink `#FF4880` /
  blue `#4D65F9`, and no gold or flame-orange anywhere.

## Design decisions (not copy, but easy to change)

- **Structure/fonts/palette = the zip's.** Pages are generated from the template's
  own components (topbar+navbar+dropdown, search modal, hero/page-header, service,
  program, events, blog, team cards, Owl testimonial carousel, 4-column footer,
  copyright, back-to-top). Fredoka + Montserrat; pink `#FF4880` / blue `#4D65F9`.
- `css/bootstrap.min.css` and `css/style.css` are the **untouched files from
  BabyCare-1.0.0.zip**; `scss/bootstrap.scss` + `scss/bootstrap/` are the zip's
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
- Logo: AI-generated flame-"K" badge in the template palette (pink→blue, no gold)
  at `img/brand/logo-mark.png` (favicon + og:image). The navbar/footer brand is
  the template's two-tone text wordmark. Regenerate/replace freely.
- **HTML Codex credit-removal note (2026-09-21):** the template credit line
  ("Designed By HTML Codex / Distributed By ThemeWagon", plus its "keep the
  credit" comment) is **deliberately removed from the copyright bar**. The
  right-hand slot now reads **"A generation on fire for God. 1 Timothy 4:12"**.
  Do **not** re-add any template credit line. `LICENSE.txt` stays in the repo.
