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
- Photos — the 42 public Drive file IDs of the **"KIZAZI 2026"** album, hotlinked
  with fallbacks (see README). KIZAZI 2026 = **14–15 Aug 2026**, treated as the
  past flagship event and the gallery album.
- Verse used throughout: **1 Timothy 4:12**.
- No email, phone or physical address is invented anywhere — the contact page
  routes to the form, the Meet link and the socials.
- **Design (2026-09-20, per your instruction):** the site now uses the BabyCare
  zip's own structure, fonts (**Fredoka + Montserrat**) and palette
  (**pink `#FF4880` / blue `#4D65F9`**) — the previous flame/gold skin is gone.
  **No gold theme anywhere** (verified: zero `#FFC53D` / flame-orange tokens in
  any shipped asset).

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
8. **Team page** — shows **serving teams/roles**, now with KIZAZI 2026 *event*
   photos on the cards (roles, not portraits — the photo caption/alt says
   "…serving at KIZAZI 2026"). Swap in consented portraits whenever you want them
   (`TEAMS` in `tools/build_common.py`).
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

- **2026-09-20:** the Drive album turned out to be **not publicly shared**, so
  every photo was falling back to the branded placeholder tile. **Fix: share the
  "KIZAZI 2026" folder in Drive as "Anyone with the link → Viewer" (folder + each
  file, and each video file).** Nothing to rebuild; the existing `data-drive`
  hotlinks pick the photos up automatically.
- All gallery photos are **hotlinked from the public Drive folder** — they show
  identifiable people. **Confirm you have consent to publish them publicly**
  before going live. To pull any photo, remove its ID from `PHOTOS` in
  `tools/build_common.py` and rebuild (or block its URL at the host level).

## Design decisions (not copy, but easy to change)

- **Structure/fonts/palette = the zip's.** Pages are generated from the template's
  own components (topbar+navbar+dropdown, search modal, hero/page-header, service,
  program, events, blog, team cards, Owl testimonial carousel, 4-column footer,
  copyright, back-to-top). Fredoka + Montserrat; pink `#FF4880` / blue `#4D65F9`.
- `css/bootstrap.min.css` and `css/style.css` are the **untouched files from
  BabyCare-1.0.0.zip**; `scss/bootstrap.scss` + `scss/bootstrap/` are the zip's
  sources if you ever recompile.
- `css/kizazi.css` is a small add-on layer (Drive photos & backgrounds, video
  cards, initials avatars, gallery filter, search results) that only uses the
  template's CSS variables — no new palette.
- `js/main.js` is the template's script (with one tweak: Drive embeds are used
  as-is instead of getting YouTube autoplay params). `js/kizazi.js` adds Drive
  photo/background resolution, next-Friday dates, gallery filter, quick search
  and the newsletter note.
- Logo: AI-generated flame-"K" badge in the template palette (pink→blue, no gold)
  at `img/brand/logo-mark.png` (favicon + og:image). The navbar/footer brand is
  the template's two-tone text wordmark. Regenerate/replace freely.
- Template credit to **HTML Codex** is retained in the footer, per the BabyCare
  template licence (`LICENSE.txt`).
