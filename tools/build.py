#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds every KIZAZI Phenomenal page.  See tools/build_common.py."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_common import (REG_URL, MEET_URL, TIKTOK, INSTAGRAM, FACEBOOK,
                          PHOTOS, photo, page, write, marquee, durl)

# ------------------------------------------------------------------ utils ---
def eyebrow(text):
    return '<span class="kz-eyebrow"><span class="dot"></span>%s</span>' % text

def sec_title(kicker, title):
    return ('<div class="text-center mb-5"><%s>%s</div>' % (kicker, title))

def heading(ey, title, sub="", center=True):
    al = "text-center mx-auto" if center else ""
    mx = 'style="max-width:760px"' if center else ""
    sub_h = '<p class="text-muted mt-4 %s">%s</p>' % ("mx-auto", sub) if sub else ""
    return ('<div class="mb-5 %s" %s>%s<h2 class="display-5 mt-3 kz-section-title">%s</h2>%s</div>'
            % (al, mx, eyebrow(ey), title, sub_h))


# ================================================================ INDEX =====
def home():
    hero = """
        <section class="kz-hero py-5">
            <div class="container py-5 position-relative">
                <div class="row g-5 align-items-center">
                    <div class="col-lg-6">
                        %s
                        <h1 class="kz-hero-title mt-4">A generation<br><span class="grad">on fire</span> for God.</h1>
                        <p class="kz-hero-sub mt-4">KIZAZI Phenomenal is a family of young people across East
                        Africa discovering Jesus, discovering purpose, and refusing to live small.
                        Worship that hits. Word that sticks. People who show up for you.</p>
                        <div class="d-flex flex-wrap gap-3 mt-4">
                            <a href="%s" target="_blank" rel="noopener" class="btn-kz">Join The Movement <i class="fas fa-arrow-right"></i></a>
                            <a href="%s" target="_blank" rel="noopener" class="btn-kz btn-kz-ghost"><i class="fas fa-video"></i> Friday Catch-Up</a>
                        </div>
                        <div class="d-flex flex-wrap gap-4 mt-5" style="color:rgba(255,255,255,.75)">
                            <span><i class="fas fa-fire me-2" style="color:var(--kz-gold)"></i>KIZAZI 2026 &mdash; 2 days, one fire</span>
                            <span><i class="fas fa-globe-africa me-2" style="color:var(--kz-gold)"></i>KE &bull; UG &bull; TZ &bull; RW</span>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="kz-hero-collage">
                            <div class="row g-4">
                                <div class="col-7">
                                    <div class="kz-polaroid tilt-l" style="aspect-ratio:4/5">%s<span class="cap">KIZAZI 2026 &mdash; the gathering</span></div>
                                </div>
                                <div class="col-5 mt-5">
                                    <div class="kz-polaroid tilt-r" style="aspect-ratio:3/4">%s<span class="cap">worship night</span></div>
                                </div>
                                <div class="col-6 mt-2">
                                    <div class="kz-polaroid tilt-r" style="aspect-ratio:1/1">%s<span class="cap">the fam</span></div>
                                </div>
                                <div class="col-6 mt-n4">
                                    <div class="kz-polaroid tilt-l" style="aspect-ratio:1/1">%s<span class="cap">one family</span></div>
                                </div>
                            </div>
                            <span class="kz-float-chip" style="top:-14px;right:6%%"><i class="fas fa-bolt" style="color:var(--kz-magenta)"></i> Next Friday: <span class="kz-next-friday">&mdash;</span></span>
                            <span class="kz-float-chip" style="bottom:-18px;left:4%%;animation-delay:1.2s"><i class="fas fa-heart" style="color:var(--kz-coral)"></i> You belong here</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""" % (eyebrow("Karibu &mdash; welcome home"), REG_URL, MEET_URL,
       photo(0, "", "KIZAZI 2026 gathering", w=900), photo(1, "", "Worship night", w=700),
       photo(2, "", "The KIZAZI family", w=700), photo(3, "", "One family", w=700))

    about = """
        <section class="py-5 kz-tint">
            <div class="container py-5">
                <div class="row g-5 align-items-center">
                    <div class="col-lg-5">
                        <div class="position-relative">
                            <div class="kz-photo" style="aspect-ratio:4/5">%s<span class="kz-photo-tag">KIZAZI 2026</span></div>
                            <div class="kz-photo position-absolute d-none d-md-block" style="width:44%%;right:-24px;bottom:-30px;aspect-ratio:1/1;border:6px solid #fff">%s</div>
                            <span class="kz-sticker position-absolute" style="top:-16px;left:-10px">this is family &rarr;</span>
                        </div>
                    </div>
                    <div class="col-lg-7">
                        %s
                        <h2 class="display-5 mt-3">We're not a club.<br>We're a <span class="text-grad">generation.</span></h2>
                        <p class="text-muted mt-4">&ldquo;Kizazi&rdquo; is Swahili for <em>generation</em>. We believe this generation
                        isn't the &ldquo;church of tomorrow&rdquo; &mdash; we're the church of <strong>right now</strong>. KIZAZI Phenomenal exists to
                        help young people across East Africa meet Jesus, grow deep roots, find their purpose and
                        light up their schools, campuses, workplaces and cities.</p>
                        <div class="row g-3 mt-2">
                            <div class="col-md-6"><h6 class="mb-2"><i class="fas fa-check-circle me-2" style="color:var(--kz-violet)"></i>Bible-centred, Spirit-filled teaching</h6></div>
                            <div class="col-md-6"><h6 class="mb-2"><i class="fas fa-check-circle me-2" style="color:var(--kz-magenta)"></i>Worship you can actually feel</h6></div>
                            <div class="col-md-6"><h6 class="mb-2"><i class="fas fa-check-circle me-2" style="color:var(--kz-coral)"></i>Real community, zero pretence</h6></div>
                            <div class="col-md-6"><h6 class="mb-2"><i class="fas fa-check-circle me-2" style="color:var(--kz-gold)"></i>Purpose, career &amp; life mentorship</h6></div>
                            <div class="col-md-6"><h6 class="mb-2"><i class="fas fa-check-circle me-2" style="color:var(--kz-violet)"></i>Outreach across East Africa</h6></div>
                            <div class="col-md-6"><h6 class="mb-2"><i class="fas fa-check-circle me-2" style="color:var(--kz-magenta)"></i>Creative arts, music &amp; media</h6></div>
                        </div>
                        <div class="d-flex flex-wrap gap-3 mt-4">
                            <a href="about.html" class="btn-kz btn-kz-line">Our Story <i class="fas fa-arrow-right"></i></a>
                            <a href="%s" target="_blank" rel="noopener" class="btn-kz">Become Family</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""" % (photo(4, "", "KIZAZI 2026 moment", w=900), photo(5, "", "KIZAZI community", w=600),
       eyebrow("Who we are"), REG_URL)

    stats = """
        <section class="py-5" style="background:var(--kz-ink)">
            <div class="container py-4">
                <div class="row g-4 text-center">
                    <div class="col-6 col-lg-3 kz-stat"><div class="num kz-count" data-count="500" data-suffix="+">0</div><div class="lbl mt-2">Young people reached</div></div>
                    <div class="col-6 col-lg-3 kz-stat"><div class="num kz-count" data-count="4">0</div><div class="lbl mt-2">Nations &amp; counting</div></div>
                    <div class="col-6 col-lg-3 kz-stat"><div class="num kz-count" data-count="52">0</div><div class="lbl mt-2">Fridays a year, online</div></div>
                    <div class="col-6 col-lg-3 kz-stat"><div class="num kz-count" data-count="1">0</div><div class="lbl mt-2">Mission: make Jesus famous</div></div>
                </div>
            </div>
        </section>
"""

    ministries = """
        <section class="py-5">
            <div class="container py-5">
                %s
                <div class="row g-4">
                    %s
                </div>
            </div>
        </section>
""" % (heading("What we do", "Eight ways we move",
               "Every ministry is a doorway. Pick one, jump in, and watch God use you."),
       "".join(ministry_card(m) for m in MINISTRIES))

    programs = """
        <section class="py-5 kz-tint">
            <div class="container py-5">
                %s
                <div class="row g-4">
                    %s
                </div>
                <div class="text-center mt-5"><a href="programs.html" class="btn-kz btn-kz-line">See All Tracks <i class="fas fa-arrow-right"></i></a></div>
            </div>
        </section>
""" % (heading("Programs", "Tracks that build you",
               "Structured journeys &mdash; not random hangouts. Pick the one that fits your season."),
       "".join(program_card(p) for p in PROGRAMS[:3]))

    events = """
        <section class="py-5">
            <div class="container py-5">
                %s
                <div class="row g-4">
                    %s
                </div>
            </div>
        </section>
""" % (heading("Events", "Where we're meeting next",
               "Online every Friday. In person across East Africa throughout the year."),
       "".join(event_card(e) for e in EVENTS[:3]))

    gallery = """
        <section class="py-5" style="background:var(--kz-ink)">
            <div class="container py-5">
                <div class="text-center mb-5">
                    %s
                    <h2 class="display-5 mt-3" style="color:#fff">KIZAZI 2026 in frames</h2>
                    <p class="mt-4" style="color:rgba(255,255,255,.7)">Two days. Hundreds of young people. One fire. Relive it.</p>
                </div>
                <div class="row g-3">
                    %s
                </div>
                <div class="text-center mt-5"><a href="gallery.html" class="btn-kz btn-kz-gold">Open Full Gallery <i class="fas fa-images"></i></a></div>
            </div>
        </section>
""" % (eyebrow("Gallery"),
       "".join('<div class="col-6 col-md-4 col-lg-3"><a href="%s" data-lightbox="home-gal" class="kz-photo d-block" style="aspect-ratio:1/1">%s</a></div>'
               % (durl(i, 1200), photo(i, "", "KIZAZI 2026 moment", w=600)) for i in range(12, 20)))

    voices = """
        <section class="py-5 kz-tint">
            <div class="container py-5">
                %s
                <div class="owl-carousel testimonial-carousel">
                    %s
                </div>
            </div>
        </section>
""" % (heading("Testimonies", "Voices from the fam"),
       "".join(voice_card(v) for v in VOICES))

    cta = """
        <section class="py-5">
            <div class="container">
                <div class="kz-cta p-5 py-5 text-center position-relative">
                    <div class="position-relative" style="z-index:1">
                        <span class="kz-badge-live"><span class="dot"></span> Registration open</span>
                        <h2 class="display-5 mt-4 mb-3" style="color:#fff">Your seat in this generation is waiting.</h2>
                        <p class="mx-auto mb-4" style="max-width:640px;color:rgba(255,255,255,.85)">
                        Register today and we'll plug you into the Friday catch-up, a discipleship cell near you,
                        and a serving team that fits your gift.</p>
                        <div class="d-flex flex-wrap justify-content-center gap-3">
                            <a href="%s" target="_blank" rel="noopener" class="btn-kz btn-kz-gold">Register Now <i class="fas fa-arrow-right"></i></a>
                            <a href="%s" target="_blank" rel="noopener" class="btn-kz btn-kz-ghost"><i class="fas fa-video"></i> Join Friday Live</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""" % (REG_URL, MEET_URL)

    return page("KIZAZI Phenomenal — A Generation On Fire For God",
                "KIZAZI Phenomenal is a youth ministry movement across East Africa: worship, the Word, real community, purpose and outreach. Join us every Friday online.",
                "home",
                hero + marquee() + about + stats + ministries + programs + events + gallery + voices + cta)


# =============================================================== SHARED =====
MINISTRIES = [
    ("fas fa-music", "", "Worship & The Word", "Loud, honest, Spirit-led worship and Bible teaching that answers real questions &mdash; not just religious slogans."),
    ("fas fa-seedling", "gold", "Discipleship Cells", "Small weekly groups in towns and on campuses where we do life together, study the Word and keep each other accountable."),
    ("fas fa-hands-praying", "mint", "Prayer & Intercession", "A house of prayer for a generation. We contend for our families, cities and nations &mdash; and we expect answers."),
    ("fas fa-video", "", "Friday Online Catch-Up", "Our weekly digital family night. Word, worship, chats and check-ins from wherever you are in East Africa."),
    ("fas fa-globe-africa", "gold", "Outreach & Missions", "Street evangelism, school visits, community care and cross-border missions. Faith with hands and feet."),
    ("fas fa-palette", "mint", "Creative & Media Lab", "Music, film, design, spoken word and content. We raise creators who tell God's story beautifully."),
    ("fas fa-briefcase", "", "Mentorship & Career", "Older-and-wiser believers walking with you through school, work, business and life decisions."),
    ("fas fa-hand-holding-heart", "gold", "Community & Care", "Nobody walks alone. Practical support, counselling referrals and a family that shows up."),
]

def ministry_card(m):
    icon, tone, title, body = m
    return ('<div class="col-md-6 col-xl-3"><div class="kz-card h-100 p-4">'
            '<div class="kz-icon %s mb-3"><i class="%s"></i></div>'
            '<h4 class="h5">%s</h4><p class="text-muted mb-0 small">%s</p></div></div>'
            % (tone, icon, title, body))

PROGRAMS = [
    (6, "12-week track", "Rooted — Discipleship Track", "From new believer to deep roots: identity, scripture, prayer, spiritual gifts and purpose.",
     [("fas fa-users", "Cohorts of 12"), ("fas fa-book", "12 sessions"), ("fas fa-clock", "Weekly")]),
    (7, "Weekly", "Phenomenal Fridays", "The weekly online family night &mdash; worship, word, wins and real talk. Your anchor for the week.",
     [("fas fa-video", "Google Meet"), ("fas fa-clock", "Fri 8PM EAT"), ("fas fa-globe-africa", "All of EA")]),
    (8, "Creative", "KIZAZI Creative Lab", "Incubator for musicians, producers, filmmakers, designers and writers who want their craft on God's altar.",
     [("fas fa-music", "Music & media"), ("fas fa-users", "Mentored"), ("fas fa-fire", "Showcases")]),
    (9, "6-month circle", "Mentorship Circle", "Matched 1-on-1 with a mentor for career, studies, business, relationships and faith-in-the-real-world.",
     [("fas fa-user-tie", "1-on-1"), ("fas fa-calendar", "6 months"), ("fas fa-briefcase", "Career")]),
    (10, "On campus", "Campus Ambassadors", "Student-led squads planting KIZAZI cells in schools and universities across the region.",
     [("fas fa-school", "Schools"), ("fas fa-university", "Campuses"), ("fas fa-flag", "Lead a cell")]),
    (11, "Seasonal", "Serve East Africa", "Mission and outreach expeditions &mdash; evangelism, community projects and cross-border teams.",
     [("fas fa-globe-africa", "Regional"), ("fas fa-hand-holding-heart", "Serve"), ("fas fa-route", "Expeditions")]),
]

def program_card(p):
    img, tag, title, body, meta = p
    meta_html = "".join('<small class="text-muted"><i class="%s me-1" style="color:var(--kz-violet)"></i>%s</small>' % (i, t) for i, t in meta)
    return ('<div class="col-md-6 col-xl-4"><div class="kz-card h-100">'
            '<div class="kz-photo" style="aspect-ratio:16/10;border-radius:0">%s<span class="kz-photo-tag">%s</span></div>'
            '<div class="p-4"><h4 class="h5">%s</h4><p class="text-muted small mb-3">%s</p>'
            '<div class="d-flex flex-wrap gap-3">%s</div>'
            '<a href="%s" target="_blank" rel="noopener" class="btn-kz btn-kz-line btn-sm px-3 py-2 mt-3">Join this track</a>'
            '</div></div></div>' % (photo(img, "", title, w=800), tag, title, body, meta_html, REG_URL))

EVENTS = [
    (21, "Weekly", "Phenomenal Friday Catch-Up", "Our whole family on one call &mdash; worship, a short word, updates and prayer. Bring a friend.",
     "Every Friday", "8:00 PM EAT", "Google Meet", MEET_URL, "Join live"),
    (22, "Annual", "KIZAZI Conference 2027", "The flagship gathering. Two days of worship, teaching, nights of fire and friendships that outlive the weekend.",
     "August 2027", "Dates soon", "East Africa", REG_URL, "Register"),
    (23, "Monthly", "Worship & Word Night", "An evening set apart for loud worship and unhurried teaching &mdash; hosted in rotation across our cities.",
     "Monthly", "Time TBA", "Rotating city", REG_URL, "Get details"),
    (24, "Termly", "Campus & School Tour", "We hit campuses and schools with music, message and madness &mdash; and leave a cell behind.",
     "Each term", "TBA", "Schools & campuses", REG_URL, "Host us"),
]

def event_card(e):
    img, tag, title, body, d1, d2, loc, url, cta = e
    return ('<div class="col-md-6 col-xl-4"><div class="kz-card h-100">'
            '<div class="kz-photo" style="aspect-ratio:16/10;border-radius:0">%s<span class="kz-photo-tag">%s</span></div>'
            '<div class="p-4"><h4 class="h5">%s</h4><p class="text-muted small mb-3">%s</p>'
            '<div class="d-flex flex-column gap-2 small mb-3">'
            '<span><i class="fas fa-calendar-day me-2" style="color:var(--kz-violet)"></i>%s &bull; %s</span>'
            '<span><i class="fas fa-map-marker-alt me-2" style="color:var(--kz-magenta)"></i>%s</span></div>'
            '<a href="%s" target="_blank" rel="noopener" class="btn-kz btn-sm px-4 py-2">%s <i class="fas fa-arrow-right"></i></a>'
            '</div></div></div>' % (photo(img, "", title, w=800), tag, title, body, d1, d2, loc, url, cta))

VOICES = [
    ("A", "Nairobi, KE", "I came for the music and stayed for Jesus. KIZAZI is the first place that felt like home without me having to perform."),
    ("K", "Kampala, UG", "The Friday catch-up got me through my hardest semester. Real people, real prayer, real God."),
    ("M", "Dar es Salaam, TZ", "Rooted changed how I read my Bible. I'm not just attending church anymore &mdash; I'm growing."),
    ("J", "Kigali, RW", "I found my purpose in the Creative Lab. Now my camera is my ministry."),
]

def voice_card(v):
    init, loc, quote = v
    return ('<div class="kz-card p-4 m-2"><div class="p-3">'
            '<i class="fa fa-quote-right fa-2x position-absolute" style="top:18px;right:20px;color:rgba(124,58,237,.2)"></i>'
            '<div class="d-flex align-items-center mb-3">'
            '<span class="d-grid place-items-center rounded-circle text-white fw-bold" style="width:56px;height:56px;background:var(--kz-grad);font-family:Sora,sans-serif">%s</span>'
            '<div class="ms-3"><h5 class="h6 mb-0">A voice from the fam</h5><small class="text-muted">%s</small></div></div>'
            '<p class="mb-0 text-muted">%s</p></div></div>' % (init, loc, quote))


# =============================================================== ABOUT ======
def about_page():
    body = """
        <section class="py-5 kz-tint">
            <div class="container py-5">
                <div class="row g-5 align-items-center">
                    <div class="col-lg-6">
                        %s
                        <h1 class="display-4 mt-3">Our story is still<br>being <span class="text-grad">written.</span></h1>
                        <p class="text-muted mt-4">KIZAZI Phenomenal began with a simple conviction: this generation
                        is not a problem to manage &mdash; it's a powerhouse to release. What started as young people
                        gathering to seek God has grown into a family stretching across Kenya, Uganda, Tanzania and
                        Rwanda, meeting in person and every Friday online.</p>
                        <p class="text-muted">We're not tied to one building. We're a movement &mdash; in cells, on campuses,
                        in group chats, on calls and at conferences &mdash; carried by one heartbeat:
                        <strong>to see a phenomenal generation raised for Jesus in East Africa.</strong></p>
                    </div>
                    <div class="col-lg-6">
                        <div class="row g-3">
                            <div class="col-7"><div class="kz-photo" style="aspect-ratio:4/5">%s</div></div>
                            <div class="col-5"><div class="kz-photo mt-4" style="aspect-ratio:3/4">%s</div></div>
                            <div class="col-5"><div class="kz-photo" style="aspect-ratio:1/1">%s</div></div>
                            <div class="col-7"><div class="kz-photo mt-n5" style="aspect-ratio:16/10">%s</div></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        %s
        <section class="py-5">
            <div class="container py-5">
                <div class="row g-4">
                    <div class="col-md-4"><div class="kz-card p-4 h-100"><div class="kz-icon mb-3"><i class="fas fa-bullseye"></i></div>
                        <h4 class="h5">Mission</h4><p class="text-muted small mb-0">To raise a phenomenal generation of young people
                        who know Jesus, love the Word, and transform East Africa through their gifts.</p></div></div>
                    <div class="col-md-4"><div class="kz-card p-4 h-100"><div class="kz-icon gold mb-3"><i class="fas fa-eye"></i></div>
                        <h4 class="h5">Vision</h4><p class="text-muted small mb-0">An East Africa where every young person has a
                        family, a faith and a purpose &mdash; and where the youth lead the revival, not just attend it.</p></div></div>
                    <div class="col-md-4"><div class="kz-card p-4 h-100"><div class="kz-icon mint mb-3"><i class="fas fa-heart"></i></div>
                        <h4 class="h5">Values</h4><p class="text-muted small mb-0">Jesus first. The Word above all. Real relationship.
                        Radical service. Joyful worship. Excellence in everything.</p></div></div>
                </div>
                <div class="kz-verse p-4 mt-5">
                    <p class="mb-0 fs-5">&ldquo;Let no one despise your youth, but be an example to the believers in word,
                    in conduct, in love, in spirit, in faith, in purity.&rdquo;<br>
                    <strong class="text-grad">1 Timothy 4:12</strong></p>
                </div>
            </div>
        </section>
        <section class="py-5" style="background:var(--kz-ink)">
            <div class="container py-5 text-center">
                %s
                <div class="row g-4 mt-2 justify-content-center">
                    %s
                </div>
            </div>
        </section>
""" % (eyebrow("About KIZAZI"), photo(25, "", "KIZAZI gathering", w=900), photo(26, "", "Worship", w=600),
       photo(27, "", "Community", w=600), photo(28, "", "Prayer", w=600),
       marquee(),
       eyebrow("What we believe"),
       "".join(belief_card(b) for b in BELIEFS))
    return page("About — KIZAZI Phenomenal",
                "The story, mission, vision and beliefs of KIZAZI Phenomenal, a youth ministry movement across East Africa.",
                "about", body)

BELIEFS = [
    ("fas fa-cross", "Jesus is Lord", "Salvation is by grace through faith in Jesus Christ alone."),
    ("fas fa-book-bible", "The Word", "The Bible is God's living Word &mdash; our final authority for life and faith."),
    ("fas fa-dove", "The Holy Spirit", "The Spirit empowers, gifts and leads every believer today."),
    ("fas fa-church", "The Church", "We are the church &mdash; a family, not a building."),
    ("fas fa-globe-africa", "The Mission", "Every member is a missionary to their generation."),
    ("fas fa-sun", "The Hope", "Jesus is coming back for a radiant, phenomenal generation."),
]

def belief_card(b):
    icon, t, d = b
    return ('<div class="col-md-6 col-lg-4"><div class="p-4 h-100" style="border:1px solid rgba(255,255,255,.12);border-radius:22px">'
            '<i class="%s fa-2x mb-3" style="color:var(--kz-gold)"></i>'
            '<h5 style="color:#fff">%s</h5><p class="mb-0 small" style="color:rgba(255,255,255,.65)">%s</p></div></div>' % (icon, t, d))


# ========================================================== MINISTRIES =====
def ministries_page():
    body = """
        <section class="py-5 kz-tint">
            <div class="container py-5">
                %s
                <div class="row g-4">%s</div>
                <div class="kz-cta p-5 mt-5 text-center position-relative">
                    <div class="position-relative" style="z-index:1">
                        <h3 class="h2 mb-3" style="color:#fff">Not sure where to plug in?</h3>
                        <p class="mb-4" style="color:rgba(255,255,255,.85)">Register and tell us your gift &mdash; we'll match you to a team.</p>
                        <a href="%s" target="_blank" rel="noopener" class="btn-kz btn-kz-gold">Find My Place <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </section>
""" % (heading("Ministries", "Every gift has a home here",
               "Eight ministries, one mission. Wherever you're wired, there's a place for you to serve and grow."),
       "".join(ministry_card(m) for m in MINISTRIES), REG_URL)
    return page("Ministries — KIZAZI Phenomenal",
                "Worship, discipleship, prayer, outreach, creative arts, mentorship and care: the ministries of KIZAZI Phenomenal.",
                "ministries", body)


# ============================================================ PROGRAMS =====
def programs_page():
    body = """
        <section class="py-5 kz-tint">
            <div class="container py-5">
                %s
                <div class="row g-4">%s</div>
            </div>
        </section>
""" % (heading("Programs", "Pick your track",
               "Structured journeys designed to take you from curious to committed, and from gifted to deployed."),
       "".join(program_card(p) for p in PROGRAMS))
    return page("Programs — KIZAZI Phenomenal",
                "Discipleship tracks, mentorship circles, creative labs and campus squads at KIZAZI Phenomenal.",
                "programs", body)


# ============================================================== EVENTS =====
def events_page():
    body = """
        <section class="py-5">
            <div class="container py-5">
                %s
                <div class="kz-card p-4 p-md-5 mb-5 d-flex flex-column flex-lg-row align-items-center gap-4 justify-content-between">
                    <div class="d-flex align-items-center gap-4">
                        <div class="text-center rounded-4 px-3 py-2 text-white" style="background:var(--kz-grad)">
                            <div class="kz-next-friday-day" style="font-family:Sora,sans-serif;font-weight:800;font-size:2rem;line-height:1">&mdash;</div>
                            <div class="kz-next-friday-month small fw-bold">&mdash;</div>
                        </div>
                        <div>
                            <span class="kz-badge-live"><span class="dot"></span> Happening weekly</span>
                            <h3 class="h4 mt-2 mb-1">Phenomenal Friday Catch-Up</h3>
                            <p class="text-muted mb-0">Next one: <strong class="kz-next-friday">&mdash;</strong> &bull; 8:00 PM EAT &bull; Google Meet</p>
                        </div>
                    </div>
                    <a href="%s" target="_blank" rel="noopener" class="btn-kz">Join The Call <i class="fas fa-video"></i></a>
                </div>
                <div class="row g-4">%s</div>
            </div>
        </section>
""" % (heading("Events", "Mark your calendar",
               "From weekly online nights to the annual conference &mdash; there's always something to show up for."),
       MEET_URL, "".join(event_card(e) for e in EVENTS))
    return page("Events — KIZAZI Phenomenal",
                "Friday online catch-up, KIZAZI Conference, worship nights and campus tours across East Africa.",
                "events", body)


# ============================================================= GALLERY =====
def gallery_page():
    cats = [("all", "All Moments"), ("worship", "Worship"), ("family", "Family"), ("word", "Word & Prayer"), ("outdoor", "Out & About")]
    buttons = "".join('<button class="kz-filter-btn%s" data-filter="%s">%s</button>' % (" active" if c[0] == "all" else "", c[0], c[1]) for c in cats)
    cycle = ["worship", "family", "word", "outdoor"]
    items = []
    for n, i in enumerate(range(12, 42)):
        cat = cycle[n % 4]
        items.append('<div class="col-6 col-md-4 col-lg-3 kz-gallery-item" data-cat="%s">'
                     '<a href="%s" data-lightbox="kz-gal" class="kz-photo d-block" style="aspect-ratio:1/1">%s</a></div>'
                     % (cat, durl(i, 1400), photo(i, "", "KIZAZI moment", w=700)))
    body = """
        <section class="py-5">
            <div class="container py-5">
                %s
                <div class="d-flex flex-wrap justify-content-center gap-2 mb-5">%s</div>
                <div class="row g-3">%s</div>
                <p class="text-center text-muted mt-5 mb-0">Want your moments featured? Tag us
                <a href="%s" target="_blank" rel="noopener" style="color:var(--kz-violet);font-weight:700">@kizazi_phenomenal</a>.</p>
            </div>
        </section>
""" % (heading("Gallery", "The fam, in pictures",
               "Every photo here is a memory from KIZAZI 2026 and beyond. Tap any frame to open it full size."),
       buttons, "".join(items), INSTAGRAM)
    return page("Gallery — KIZAZI Phenomenal",
                "Photos from KIZAZI 2026 and KIZAZI Phenomenal gatherings across East Africa.",
                "gallery", body)


# ================================================================ BLOG =====
POSTS = [
    (30, "Story", "KIZAZI 2026: Two Days That Changed Us",
     "We arrived as strangers from four nations and left as family. Here's what God did in 48 hours &mdash; and why we're still talking about it."),
    (31, "Devotional", "Why We Meet Every Single Friday",
     "It's not just a call. It's a rhythm of grace that keeps a scattered generation connected, accountable and on fire."),
    (32, "Devotional", "3 Ways To Stay On Fire Between Gatherings",
     "Conferences fade. Cells, scripture and service keep the flame alive on an ordinary Tuesday."),
    (33, "Story", "From Audience To Family",
     "What happens after the altar call? The unglamorous, glorious work of becoming a family that stays."),
    (34, "Devotional", "Your Campus Is Your Mission Field",
     "You don't need a title to be a missionary. You need a lecture hall and a burden."),
    (35, "Story", "The Creative Lab Is Raising Storytellers",
     "Behind every KIZAZI recap is a young creator learning that their craft is an altar."),
]

def post_card(p):
    img, tag, title, ex = p
    return ('<div class="col-md-6 col-xl-4"><div class="kz-card h-100">'
            '<div class="kz-photo" style="aspect-ratio:16/10;border-radius:0">%s<span class="kz-photo-tag">%s</span></div>'
            '<div class="p-4"><h4 class="h5">%s</h4><p class="text-muted small mb-3">%s</p>'
            '<a href="blog.html" class="fw-bold small" style="color:var(--kz-violet)">Read more <i class="fas fa-arrow-right"></i></a>'
            '</div></div></div>' % (photo(img, "", title, w=800), tag, title, ex))

def blog_page():
    body = """
        <section class="py-5 kz-tint">
            <div class="container py-5">
                %s
                <div class="row g-4">%s</div>
            </div>
        </section>
""" % (heading("Word & Stories", "Devotionals, recaps & real talk",
               "Short, sharp words to keep you anchored between gatherings."),
       "".join(post_card(p) for p in POSTS))
    return page("Word & Stories — KIZAZI Phenomenal",
                "Devotionals, conference recaps and stories from the KIZAZI Phenomenal family.",
                "blog", body)


# ================================================================ TEAM =====
TEAMS = [
    ("fas fa-hands-praying", "Lead & Pastoral Care", "Shepherding the family, teaching the Word and holding the vision."),
    ("fas fa-music", "Worship Team", "Singers, musicians and technicians leading the family into God's presence."),
    ("fas fa-clapperboard", "Media & Creative", "Cameras, design, sound and content &mdash; telling our story beautifully."),
    ("fas fa-hands", "Prayer Team", "The engine room. Interceding for the family, the events and the nations."),
    ("fas fa-school", "Campus & School Leads", "Student leaders planting and shepherding cells on their campuses."),
    ("fas fa-mug-hot", "Hospitality & Care", "Welcome desks, follow-ups, counselling referrals and making sure nobody eats alone."),
]

def team_page():
    cards = "".join(
        '<div class="col-md-6 col-xl-4"><div class="kz-card h-100 p-4 text-center">'
        '<div class="kz-icon %s mx-auto mb-3"><i class="%s"></i></div>'
        '<h4 class="h5">%s</h4><p class="text-muted small mb-3">%s</p>'
        '<a href="%s" target="_blank" rel="noopener" class="btn-kz btn-kz-line btn-sm px-3 py-2">Join this team</a></div></div>'
        % (tone, icon, t, d, REG_URL)
        for (icon, t, d), tone in zip(TEAMS, ["", "gold", "mint", "", "gold", "mint"]))
    body = """
        <section class="py-5">
            <div class="container py-5">
                %s
                <div class="row g-4">%s</div>
                <div class="kz-verse p-4 mt-5">
                    <p class="mb-0">KIZAZI is served by volunteers &mdash; students, workers, creators and parents' worst
                    nightmares-turned-best-testimonies. Names and faces of our serving team are updated after every
                    commissioning. <strong>Want your name on this page one day? Start by joining a team.</strong></p>
                </div>
            </div>
        </section>
""" % (heading("Team & Serving", "The hands behind the move",
               "No celebrities here &mdash; just servants. Find the team where your gift fits."), cards)
    return page("Team & Serving — KIZAZI Phenomenal",
                "Serving teams at KIZAZI Phenomenal: worship, media, prayer, campus leads, hospitality and pastoral care.",
                "team", body)


# ========================================================= TESTIMONIAL =====
def testimonial_page():
    body = """
        <section class="py-5 kz-tint">
            <div class="container py-5">
                %s
                <div class="row g-4">%s</div>
                <div class="text-center mt-5">
                    <p class="text-muted mb-3">Got a testimony? We want to hear it &mdash; and celebrate you.</p>
                    <a href="%s" target="_blank" rel="noopener" class="btn-kz">Share Your Story <i class="fas fa-pen"></i></a>
                </div>
            </div>
        </section>
""" % (heading("Testimonies", "What God is doing in us"),
       "".join('<div class="col-md-6">%s</div>' % voice_card(v) for v in VOICES), REG_URL)
    return page("Testimonies — KIZAZI Phenomenal",
                "Real voices from the KIZAZI Phenomenal family across East Africa.",
                "testimonial", body)


# ============================================================= CONTACT =====
def contact_page():
    body = """
        <section class="py-5 kz-tint">
            <div class="container py-5">
                %s
                <div class="row g-4">
                    <div class="col-lg-5">
                        <div class="kz-card p-4 p-md-5 h-100">
                            <h3 class="h4 mb-4">Fastest ways to reach us</h3>
                            <div class="d-flex flex-column gap-4">
                                <div class="d-flex gap-3"><div class="kz-icon" style="width:48px;height:48px;font-size:1.1rem"><i class="fas fa-user-plus"></i></div>
                                    <div><h5 class="h6 mb-1">Register / Join</h5><p class="small text-muted mb-0">The registration form is our front door.</p>
                                    <a href="%s" target="_blank" rel="noopener" class="small fw-bold" style="color:var(--kz-violet)">Open form <i class="fas fa-external-link-alt"></i></a></div></div>
                                <div class="d-flex gap-3"><div class="kz-icon gold" style="width:48px;height:48px;font-size:1.1rem"><i class="fas fa-video"></i></div>
                                    <div><h5 class="h6 mb-1">Friday Catch-Up</h5><p class="small text-muted mb-0">Show up live, say hi in the chat.</p>
                                    <a href="%s" target="_blank" rel="noopener" class="small fw-bold" style="color:var(--kz-violet)">meet.google.com <i class="fas fa-external-link-alt"></i></a></div></div>
                                <div class="d-flex gap-3"><div class="kz-icon mint" style="width:48px;height:48px;font-size:1.1rem"><i class="fas fa-hashtag"></i></div>
                                    <div><h5 class="h6 mb-1">Socials</h5>
                                    <div class="d-flex gap-2 mt-2">
                                        <a href="%s" target="_blank" rel="noopener" class="btn-kz btn-kz-line btn-sm px-3 py-1"><i class="fab fa-tiktok"></i></a>
                                        <a href="%s" target="_blank" rel="noopener" class="btn-kz btn-kz-line btn-sm px-3 py-1"><i class="fab fa-instagram"></i></a>
                                        <a href="%s" target="_blank" rel="noopener" class="btn-kz btn-kz-line btn-sm px-3 py-1"><i class="fab fa-facebook-f"></i></a>
                                    </div></div></div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-7">
                        <div class="kz-card p-4 p-md-5 h-100">
                            <h3 class="h4 mb-2">Send us a word</h3>
                            <p class="text-muted small mb-4">Questions, prayer requests, partnership or press &mdash; drop it here and a servant will get back to you.</p>
                            <form id="kz-contact-form">
                                <div class="row g-3">
                                    <div class="col-md-6"><input class="form-control kz-input" placeholder="Your name" required></div>
                                    <div class="col-md-6"><input class="form-control kz-input" type="email" placeholder="Email or phone" required></div>
                                    <div class="col-12"><select class="form-select kz-input">
                                        <option>I want to join KIZAZI</option><option>Prayer request</option>
                                        <option>I want to serve / join a team</option><option>Partner with us</option><option>Something else</option>
                                    </select></div>
                                    <div class="col-12"><textarea class="form-control kz-input" rows="5" placeholder="Your message" required></textarea></div>
                                    <div class="col-12 d-flex flex-wrap gap-3 align-items-center">
                                        <button type="submit" class="btn-kz">Send It <i class="fas fa-paper-plane"></i></button>
                                        <small class="text-muted">Prefer forms? <a href="%s" target="_blank" rel="noopener" style="color:var(--kz-violet);font-weight:700">Use registration</a></small>
                                    </div>
                                </div>
                            </form>
                            <div id="kz-form-note" class="alert mt-4 d-none" style="background:rgba(20,224,192,.12);color:#0b7a68;border:1px solid rgba(20,224,192,.4)"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""" % (heading("Contact", "Slide into our DMs (or forms)",
               "However you reach us, a human from the fam will respond."),
       REG_URL, MEET_URL, TIKTOK, INSTAGRAM, FACEBOOK, REG_URL)
    extra = """    <script>
    jQuery(function($){
      $("#kz-contact-form").on("submit", function(e){
        e.preventDefault();
        $("#kz-form-note").removeClass("d-none").html(
          "Asante! We've got your note. While our inbox is being set up, the fastest reply is via our socials or the registration form &mdash; " +
          "<a href='__REG__' target='_blank' rel='noopener' style='font-weight:700'>register here</a>.");
        this.reset();
      });
    });
    </script>
""".replace("__REG__", REG_URL)
    html = page("Contact — KIZAZI Phenomenal",
                "Reach KIZAZI Phenomenal: registration, Friday online catch-up, TikTok, Instagram and Facebook.",
                "contact", body)
    return html.replace("</body>", extra + "</body>")


# ================================================================ 404 ======
def notfound_page():
    body = """
        <section class="py-5 kz-tint" style="min-height:70vh;display:flex;align-items:center">
            <div class="container py-5 text-center">
                <div class="display-1 text-grad" style="font-size:clamp(5rem,16vw,11rem);line-height:1">404</div>
                <h2 class="display-6 mt-2">Whoops &mdash; wrong turn, fam.</h2>
                <p class="text-muted mx-auto mt-3" style="max-width:520px">This page skipped the catch-up.
                Let's get you back to where the fire is.</p>
                <div class="d-flex flex-wrap justify-content-center gap-3 mt-4">
                    <a href="index.html" class="btn-kz">Back Home <i class="fas fa-home"></i></a>
                    <a href="%s" target="_blank" rel="noopener" class="btn-kz btn-kz-line">Join Friday Live</a>
                </div>
            </div>
        </section>
""" % MEET_URL
    return page("404 — KIZAZI Phenomenal", "Page not found.", "404", body)


# ================================================================ MAIN =====
def main():
    print("Building KIZAZI Phenomenal ...")
    write("index.html", home())
    write("about.html", about_page())
    write("ministries.html", ministries_page())
    write("programs.html", programs_page())
    write("events.html", events_page())
    write("gallery.html", gallery_page())
    write("blog.html", blog_page())
    write("team.html", team_page())
    write("testimonial.html", testimonial_page())
    write("contact.html", contact_page())
    write("404.html", notfound_page())
    print("Done.")


if __name__ == "__main__":
    main()
