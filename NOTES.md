# Content notes & assumptions — PLEASE REVIEW

"KIZAZI Phenomenal" is not indexed anywhere online yet, so the copy below was drafted
from (a) the links you provided, (b) the "KIZAZI 2026" Drive photo folder, and (c) your
confirmation that this is a **Christian youth ministry / fellowship serving East Africa**.
Everything marked ⚠️ is a drafting assumption — edit freely in `tools/build.py` and run
`python3 tools/build.py`.

## Confirmed from you / your links
- Name: **KIZAZI Phenomenal**. Type: Christian youth ministry/fellowship. Reach: East Africa.
- Registration form, Friday Google-Meet catch-up, TikTok / Instagram / Facebook handles.
- "Linktree will be up soon" → shown as a small topbar note.
- Drive folder = **KIZAZI 2026**, photos dated **14–15 Aug 2026** → used as the flagship
  past event ("KIZAZI 2026 — two days").

## ⚠️ Assumptions to confirm / replace
1. **Friday time** — copy says **8:00 PM EAT**. Change in `tools/build_common.py`/`build.py`
   if different. (The *date* shown on the site is auto-calculated to the next Friday.)
2. **Stats** — "500+ reached", "4 nations", "52 Fridays", "1 mission" are illustrative
   counters. Swap in real numbers.
3. **KIZAZI Conference 2027** — listed as "August 2027, dates soon" (placeholder for the
   next flagship). Replace with the real next event.
4. **Programme names** — *Rooted, Phenomenal Fridays, KIZAZI Creative Lab, Mentorship
   Circle, Campus Ambassadors, Serve East Africa* and the **8 ministry names** are
   proposed structures. Rename/add/remove to match what actually runs.
5. **Testimonies** — the four quotes are illustrative "voices from the fam" (initial-only,
   no real names used). Replace with real, consented testimonies.
6. **Blog posts** — titles/excerpts are drafted starters; bodies not yet written.
7. **Team page** — intentionally shows **serving teams/roles, not named individuals**, to
   avoid inventing or mis-attributing people (and to avoid putting random event photos on
   named leaders). Add real names/photos when ready.
8. **Contact email/phone** — deliberately **not invented**. Contact page routes to the
   registration form, the Meet link and socials. Add a real email/phone/physical address
   when available.
9. **Verse used**: 1 Timothy 4:12 (fits a youth movement).

## Photos & privacy
- All gallery photos are **hotlinked from the public Drive folder** (see README).
- They show identifiable people. Confirm you have consent to publish them publicly
  before going live. If any photo must come down, remove its ID from `PHOTOS` in
  `tools/build_common.py` and rebuild.

## Design decisions
- Palette: electric violet `#7C3AED` + phenomenal gold `#FFC53D`, magenta/coral gradient
  accents, deep-indigo ink `#16092F` (chosen as "the most amazing vibe" per your brief).
- Type: **Sora** (display) + **Plus Jakarta Sans** (body) + **Caveat** (handwritten accents).
- Logo: generated flame-"K" mark at `img/brand/logo-mark.png` (also the favicon).
- Template credit to HTML Codex is retained in the footer, per the template licence.
