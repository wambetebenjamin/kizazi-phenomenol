# Content notes & assumptions — PLEASE REVIEW

Everything below that is marked ⚠️ is a **drafting assumption** — edit it in
`tools/build_common.py` (data) or `tools/build.py` (layout/copy), then run
`python3 tools/build.py`.

## Confirmed from your brief / links

- Name: **KIZAZI Phenomenal** (“kizazi” = generation). Christian youth ministry /
  fellowship serving **Kenya, Uganda, Tanzania, Rwanda**.
- Registration form: `https://forms.gle/vzRJrigBHCNormVA9` — wired as the primary
  CTA everywhere (topbar, nav, hero, programs, events, CTA bands, footer, contact).
- **Friday Online Catch-Up** — `https://meet.google.com/mcr-fupc-buw`, weekly,
  8:00 PM EAT — wired in topbar, hero, events, footer schedule, contact.
- Socials — TikTok `@kizazi.phenomenal`, Instagram `kizazi_phenomenal`,
  Facebook `kizaziphenomenal` — wired in topbar, footer, contact, blog.
- **“Linktree coming soon”** — shown as a small topbar note, a footer note and a
  contact card.
- Photos — the 42 public Drive file IDs of the **“KIZAZI 2026”** album, hotlinked
  with fallbacks (see README). KIZAZI 2026 = **14–15 Aug 2026**, treated as the
  past flagship event and the gallery album.
- Verse used throughout: **1 Timothy 4:12**.
- No email, phone or physical address is invented anywhere — the contact page
  routes to the form, the Meet link and the socials.

## ⚠️ Assumptions to confirm / replace

1. **Friday time** — copy says **8:00 PM EAT** (from your brief). The *date* shown
   on the site is **auto-calculated to the next Friday** (browser local time) and
   updates anywhere a `data-next-friday-*` attribute appears.
2. **Stats/counters** — “4 nations”, “500+ young people reached”, “8 ministries”,
   “52 Fridays a year” are illustrative. Swap real numbers in `tools/build.py`
   (`data-count` attributes).
3. **KIZAZI Conference 2027** — listed as “August 2027 · dates soon” (the next
   flagship placeholder). Replace with the real dates once announced.
4. **Programs** — *Rooted (12 weeks), Phenomenal Fridays, KIZAZI Creative Lab,
   Mentorship Circle, Campus Ambassadors, Serve East Africa* plus the rate badges
   (“Free · 12 weeks”, “Weekly”, “Term intake”, “Applications open”, “Recruiting
   now”, “Next trip TBA”) are proposed structures — rename/replace to match what
   actually runs.
5. **Ministries** — the 8 names (Worship & The Word, Discipleship Cells, Prayer &
   Intercession, Friday Online Catch-Up, Outreach & Missions, Creative & Media
   Lab, Mentorship & Career, Community & Care) and their copy are drafted from
   your list — adjust the blurbs/“what to expect” bullets as needed.
6. **Gallery categories** — the album has no labels, so the 6 filter categories
   (Worship / Word / Community / Service / Creative / Behind the Scenes) are
   assigned **round-robin** in `tools/build_common.py` (`GALLERY_CATS`). If you
   label the photos, update the mapping (a 42-line list or a smarter rule).
7. **Blog posts** — three drafted posts (1 Timothy 4:12 devotional, KIZAZI 2026
   recap, “5 habits” practical) with dates in Aug–Sep 2026. Titles, dates and
   bodies are placeholders until you write/confirm the real ones.
8. **Team page** — deliberately shows **serving teams/roles with initial tiles
   (WS, WW, PW, DM, CM, OM, SH, MC)**, not named individuals — to avoid inventing
   people or putting random event photos on leaders. Add real names + consented
   photos when you want them.
9. **Testimonies** — four quotes, **initials only** (K., A., M., T.), labelled
   “joined online, Kampala”, “Campus Ambassador”, “Rooted graduate”,
   “first-year student” — all **illustrative**. Replace with real, consented
   testimonies before going public.
10. **Weekly schedule (footer)** — only Friday is asserted (8:00 PM EAT); the
    weekday row says “cells, prayer & campus visits (schedule shared weekly)”
    without inventing fixed days. Add real recurring days when you have them.
11. **Worship & Word Night / Campus & School Tour cadence** — “monthly” and
    “termly, announced weekly” are drafted rhythms.
12. **Newsletter form (footer)** — decorative for now (shows a thank-you note);
    no emails are collected/stored. Wire it to a real service (or remove) before
    relying on it.
13. **Highlight film** — the hero play button opens a modal with a KIZAZI 2026
    photo and “film coming soon”. Replace with a real video embed when one exists.
14. **og:image** — uses the relative `img/brand/logo-mark.png`; after deploying,
    set an absolute URL (and a 1200×630 hero image) for better social previews.

## Photos & privacy

- **2026-09-20:** the Drive album turned out to be **not publicly shared**, so
  every photo was 404-ing into the (now flame-coloured) placeholder tile — the
  site looked empty/weird. **Fix: share the “KIZAZI 2026” folder in Drive as
  “Anyone with the link → Viewer” (folder + each file).** Nothing to rebuild;
  the existing `data-drive` hotlinks pick the photos up automatically.
- All gallery photos are **hotlinked from the public Drive folder** — they show
  identifiable people. **Confirm you have consent to publish them publicly**
  before going live. To pull any photo, remove its ID from `PHOTOS` in
  `tools/build_common.py` and rebuild (or block its URL at the host level).

## Design decisions (not copy, but easy to change)

- Palette: flame orange-red `#F4511E` + phenomenal gold `#FFC53D`, magenta/coral
  sunset gradient accents, warm dark ink `#201108` — tokens live in
  `scss/kizazi-bootstrap.scss` (Bootstrap) and `css/kizazi.css` (skin).
  (Switched from the original electric-violet palette on 2026-09-20 —
  `tools/recolor.py` documents how the skin was re-rotated; Bootstrap was
  recompiled from SCSS, so just edit the SCSS and re-run the documented
  `sass` command for future palette tweaks.)
- Type: Sora / Plus Jakarta Sans / Caveat via Google Fonts.
- Logo: AI-generated flame-“K” at `img/brand/logo-mark.png` (also favicon +
  placeholder-free brand mark). Regenerate/replace freely.
- Template credit to **HTML Codex** is retained in the footer, per the BabyCare
  template licence (`LICENSE.txt`).
