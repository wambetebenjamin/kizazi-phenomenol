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
- **Design:** the site uses the BabyCare zip's own structure and fonts
  (**Fredoka + Montserrat**). The skin was rebranded three times, always in
  place: template pink, then royal purple (2026-09-21), and now the
  owner-approved **street celebration** (2026-09-23, see the section below):
  stamp red `#E63946` / leaf green `#16A34A` / sunshine yellow `#FACC15` /
  paper `#FAF7F0` / ink black `#0A0A0A`, body grey `#70747F`.
  **No gradients, no pink, no purple, no `#FFC53D`, no gold anywhere**
  (verified: zero banned tokens in any shipped asset).

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

- **2026-09-23:** this branch ships `img/gallery/` **empty**: the 42 JPEGs
  are not committed here yet (the sandbox has no route to Google Drive). The
  pages are already wired to `img/gallery/01.jpg … 42.jpg`, so they light up
  as soon as the files land; until then every photo falls back to
  `img/brand/photo-placeholder.svg` (CSS and JS last resort), so no page ever
  shows a broken image. The owner is uploading the Drive files to GitHub; the
  CI job (`.github/workflows/fetch-gallery-photos.yml`, whose byte-identical
  copy sits in the working tree because pushing it needs a token with
  `workflows` write) can also vendor them after it lands, and the
  browser-assisted `tools/fetch_gallery_server.py 8123
  --fetch-root` remains the manual route. The PR that carried this skin states
  the photo count and the `du -sk img/gallery` size as they stand.
- **2026-09-21:** the 42 "KIZAZI 2026" photos were vendored in the repo at
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
- Portraits live in `img/team/` and are driven by `PEOPLE` (admin team) and
  `PATRON` (Reverend Dr. Joslyn Isigi) in `tools/build_common.py`. In this
  branch `img/team/` is still empty, so the builder skips those entries
  (team.html shows the serving-team role cards only) until the portraits are
  committed. Roles are
  written exactly as **"Admin"** and **"Patron"**; no other titles are invented.
- `team.html` shows the Patron as a featured panel plus the admin cards;
  `about.html` shows the compact Patron panel in the mission area. An entry
  whose JPEG is missing is skipped by the builder, so pages never show a broken
  portrait.
- To pull a person: delete their file in `img/team/` and their entry in
  `tools/build_common.py`, then re-run `python3 tools/build.py`.

## Energy layer (2026-09-21, re-skinned 2026-09-23)

The site's young/energetic feel is one documented layer, kept and extended
from here on. It lives in **section 9 of `css/kizazi.css`** and in
`js/kizazi.js` (behaviours 6 and 7), additive on the BabyCare skin: nothing
template-visible was removed and no behaviour changed on 2026-09-23, only the
paint.

- **Palette and fonts are fixed** (street celebration, 2026-09-23): stamp red
  `#E63946` (hover `#C1121F`), leaf green `#16A34A`, sunshine yellow `#FACC15`,
  paper `#FAF7F0`, ink black `#0A0A0A`; Fredoka + Montserrat. **No gradients,
  no pink, no purple, no `#FFC53D`, no gold anywhere.**
- **One energy fill** — `--kz-yellow: #FACC15`, flat. The old gradient token
  (`--kz-grad`) is **retired**; the only gradient shapes left in the sheet are
  the hard-stop black/yellow hazard stripes (flat by construction) and the
  photo washes that keep hero/page-header/footer copy readable over a photo
  (single-hue overlay, no decorative fill). The yellow paints: the ticker
  band, the sticker kicker pills, the stat ticket chips (`.kz-stat-num`), the
  play ring, the scroll progress bar and the hazard rules.
  The primary red and secondary green paint the stamp buttons, links and the
  card frames.
- **Marquee ticker** under the navbar on every page: the phrases live in
  `TICKER` (`tools/build_common.py`), repeated exactly twice in the DOM so
  the CSS -50% translate loop is seamless; it pauses on hover and is
  `aria-hidden` (decorative reinforcement of copy that lives on the pages).
- **Sticker kickers**: the template's `h4.title-border-radius` section
  kickers are sunshine-yellow stickers, slightly tilted (rotate -1.5deg), with
  black text, a 3px ink border, a hard offset shadow and the stamp-red rule
  underneath (the template's old 2px primary-colour underline is neutralised).
- **Lifting/tilting cards**: `.service-item`, `.program-item`,
  `.events-item`, `.blog-item`, `.team-item`, the gallery tiles and the hero
  moments all move on hover with transform + shadow only, exactly as before.
  The street treatment turns that motion into a **stamp press**
  (translate 2px + smaller hard shadow, tilt kept) per the 2026-09-23 design;
  flip `.service-item:hover` back to `translateY(-8px)` in section 9.4 if you
  would rather have the lift back. The template's own inner hover effects
  (icon inversion, image zoom, event overlay) keep working.
- **Counting stats**: the about-page stat numerals carry `data-kz-count`
  (and `data-kz-suffix` for the "+") and count up (ease-out cubic, 1.2s)
  when they scroll into view; each numeral is a tilted sunshine-yellow ticket
  chip with a 3px ink border and a hard offset shadow. The final value stays in the markup, so no-JS
  visitors read the real number and reduced-motion visitors skip the count.
  (The numbers themselves are still the illustrative ones, see
  Assumptions #2.)
- **Scroll progress bar**: fixed 5px sunshine-yellow rule, inked on its lower
  edge, at the very top of the viewport; driven by `transform: scaleX()` only
  (rAF-throttled, passive listeners). No layout shift.
- **Pulsing play button**: the template's pulse ring (its own
  `pulse-border` animation) is re-inked in the one energy fill, yellow, with a
  black edge ring; the play disc behind it is stamp red.
- **Honest motion**: every animation here is transform/opacity only (no
  layout shift), and the `prefers-reduced-motion: reduce` block at the end
  of `css/kizazi.css` switches the marquee, the card motion, the button and
  kicker presses (transform and shadow both stay put) and the play pulse off (and `js/kizazi.js` checks the same media query to skip the
  count-up). The progress bar is the one element kept, because it mirrors
  the user's own scrolling instead of running on its own.
- **New copy** (the ticker phrases) follows the house rules: short lines,
  second person, verbs first, no dashes.

## Street celebration skin (2026-09-23)

- **Owner-approved look** after the mockup review: a fusion of a
  Spotify-Wrapped celebration and a Nairobi matatu collage. Stamp red
  `#E63946` (hover `#C1121F`) is the primary, leaf green `#16A34A` the
  secondary, sunshine yellow `#FACC15` the one energy fill (`--kz-yellow`),
  paper `#FAF7F0` the light wash, ink black `#0A0A0A` the topbar/footer/border
  and hard-shadow ink, body grey `#70747F` unchanged.
- **No gradient fills.** The old `--kz-grad` token is gone from
  `css/kizazi.css`; the only gradient shapes left are the hard-stop hazard
  stripes (`repeating-linear-gradient(45deg, black, black, yellow, yellow)`,
  flat by construction) and the single-hue photo washes that keep copy
  readable over the hero/page-header/footer photos. The template's two
  decorative section washes (`.service`, `.program`) became flat paper.
- **Street treatment applied in `css/kizazi.css` section 9.1 to 9.9**: 3px
  ink borders and hard offset shadows (4 to 6px, solid black) on the stamp
  buttons, the kicker pills, the cards and the stat chips; hover presses the
  stamp (translate 2px, smaller shadow); the ticker is a yellow band with
  black text framed by black/yellow hazard stripes; the kicker pills are
  yellow with black text and the stamp-red rule; the stat numerals sit on
  tilted yellow ticket chips; the play ring is yellow with a black edge; the
  progress bar is yellow; the copyright bar is capped by a hazard stripe; the
  topbar is black with yellow icons; the footer is ink black with paper copy,
  yellow rules and a paper newsletter sticker.
- **The swatch is complete in `css/bootstrap.min.css` too.** The zip's own
  compile was re-derived in place: each of the palette's bases, its tints,
  its shades, its table variants, its focus rings and the SVG data-URI fills
  were recomputed from the new bases, so the previous pink/blue/violet
  leftovers (for example `.form-control:focus` border, `.btn-primary:hover`,
  `.table-*`, `.accordion-button::after`) cannot show up anywhere. Nothing
  structural changed: same selectors, same sizes, same rules.
- **Bootstrap's own hue variables** (`--bs-pink: #d63384`, `--bs-purple:
  #6f42c1`, `--bs-info`, `--bs-warning` and friends) are the framework's
  defaults and were left untouched; no KIZAZI markup uses them.
- Regenerate the skin check with (scoped to the shipped assets, this file is
  not scanned):
  `grep -ril "ff4880\|cc3a66\|ffecf2\|6d28d9\|4d65f9\|393d72" css/ *.html img/brand/ scss/bootstrap.scss`
  It prints nothing.

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
  font rules are unchanged: Fredoka + Montserrat. The palette is the street
  celebration (2026-09-23): stamp red `#E63946`, leaf green `#16A34A`,
  sunshine yellow `#FACC15`, paper `#FAF7F0`, ink black `#0A0A0A`, and no
  gradients, pink, purple, `#FFC53D`, gold or flame-orange anywhere.

## Design decisions (not copy, but easy to change)

- **Structure/fonts = the zip's.** Pages are generated from the template's
  own components (topbar+navbar+dropdown, search modal, hero/page-header, service,
  program, events, blog, team cards, Owl testimonial carousel, 4-column footer,
  copyright, back-to-top). Fredoka + Montserrat; street celebration palette
  (stamp red / leaf green / sunshine yellow / paper / ink black).
- `css/bootstrap.min.css` and `css/style.css` come from **BabyCare-1.0.0.zip**,
  with the palette swapped in place for the street celebration (2026-09-23):
  every base colour **and its derived tints and shades** were re-derived from
  the same bases, so no pink or violet shade survives in focus rings, table
  variants, disabled states or the SVG data-URIs. Only colours changed: the
  selector structure, sizes and every other declaration are still the zip's.
  `scss/bootstrap.scss` + `scss/bootstrap/` are the zip's sources if you ever
  recompile (a fresh dart-sass build drops the zip's autoprefixer prefixes).
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
- Logo: AI-generated **street sticker** badge at `img/brand/logo-mark.png`
  (favicon + og:image): white circular sticker with a black outline, a black
  "K" whose stem is a flame (yellow outer, red inner) and a red crown, flat
  colours only. `img/brand/photo-placeholder.svg` wears the same skin. The navbar/footer brand is
  the template's two-tone text wordmark. Regenerate/replace freely.
- **HTML Codex credit-removal note (2026-09-21):** the template credit line
  ("Designed By HTML Codex / Distributed By ThemeWagon", plus its "keep the
  credit" comment) is **deliberately removed from the copyright bar**. The
  right-hand slot now reads **"A generation on fire for God. 1 Timothy 4:12"**.
  Do **not** re-add any template credit line. `LICENSE.txt` stays in the repo.
