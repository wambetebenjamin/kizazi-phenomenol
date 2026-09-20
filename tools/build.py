#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KIZAZI Phenomenal — page builder.

Composes the 11 static pages from the shared chrome in build_common.py and
the per-page bodies below, writing every file to the repository root.

Run from the repository root:

    python3 tools/build.py

After editing content in build_common.py / this file, re-run and refresh.
"""

import os

from build_common import (
    REG_URL, MEET_URL, TIKTOK_URL, INSTAGRAM_URL, FACEBOOK_URL, LINKTREE_NOTE,
    SITE, GALLERY_CATS, PHOTOS, durl, img, gallery_cat,
    MINISTRIES, PROGRAMS, EVENTS, BLOG, TEAMS, TESTIMONIALS,
    head, body_open, topbar, navbar, page_header, section_head,
    footer, back_to_top, scripts,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Badge lines (big, small) for the static events; index 0 (Fridays) is auto-dated.
EVENT_BADGES = [None, ("2027", "soon"), ("Monthly", "night"), ("Termly", "tour")]


# --------------------------------------------------------------- components ---
def btn(href, label, kind="sweep", icon="", target=True, extra=""):
    t = ' target="_blank" rel="noopener"' if target else ""
    ic = '<i class="fas %s me-2"></i>' % icon if icon else ""
    return '<a class="btn kz-btn kz-btn-%s %s" href="%s"%s>%s%s</a>' % (
        kind, extra, href, t, ic, label)



def alt_of(title):
    """Plain-text version of a display title (for alt attributes)."""
    return (title.replace("&mdash;", "\u2014").replace("&ndash;", "\u2013")
               .replace("&middot;", "\u00b7").replace("&ldquo;", "\u201c")
               .replace("&rdquo;", "\u201d").replace("&rsquo;", "\u2019")
               .replace("&lsquo;", "\u2018").replace("&amp;", "&"))

def marquee():
    items = [
        "PHENOMENAL FRIDAYS", "8:00 PM EAT", "A GENERATION ON FIRE",
        "KIZAZI 2026 · 14&ndash;15 AUG", "KENYA · UGANDA · TANZANIA · RWANDA",
        "1 TIMOTHY 4:12",
    ]
    block = "".join(
        '<span class="kz-marquee-item">%s</span><span class="kz-marquee-star">&#10022;</span>'
        % it for it in items)
    return """        <div class="kz-marquee" aria-hidden="true">
            <div class="kz-marquee-track">%(b)s%(b)s</div>
        </div>
""" % {"b": block}


def hero_header():
    return """        <!-- Hero Start -->
        <section class="kz-hero container-fluid position-relative overflow-hidden" id="top">
            <div class="kz-hero-dots"></div>
            <div class="kz-aurora kz-aurora-1"></div>
            <div class="kz-aurora kz-aurora-2"></div>
            <div class="kz-aurora kz-aurora-3"></div>
            <div class="container py-5">
                <div class="row align-items-center g-5">
                    <div class="col-lg-6 text-white">
                        <span class="kz-kicker kz-kicker-light"><i class="fas fa-fire"></i> %(tagline)s</span>
                        <h1 class="kz-hero-title">KIZAZI <span class="kz-grad-text">Phenomenal</span></h1>
                        <p class="kz-hero-verse kz-hand">&ldquo;%(verse)s&rdquo; <span class="kz-verse-ref">&mdash; %(ref)s</span></p>
                        <p class="kz-hero-sub">A bold, joyful Christian youth movement across %(countries)s &mdash; worship that moves, discipleship that sticks, and a family that carries you.</p>
                        <div class="d-flex flex-wrap gap-3 kz-hero-ctas">
                            <a class="btn kz-btn kz-btn-sweep btn-lg" href="%(reg)s" target="_blank" rel="noopener">Join the Movement <i class="fas fa-bolt ms-2"></i></a>
                            <a class="btn kz-btn kz-btn-ghost btn-lg text-white" href="%(meet)s" target="_blank" rel="noopener"><i class="fas fa-video me-2"></i>Friday Catch-Up &middot; 8 PM EAT</a>
                        </div>
                        <div class="kz-hero-stats">
                            <div class="kz-hero-stat"><strong><span class="kz-counter" data-count="4"></span></strong><span>nations served</span></div>
                            <div class="kz-hero-stat"><strong><span class="kz-counter" data-count="500" data-suffix="+"></span></strong><span>young people reached</span></div>
                            <div class="kz-hero-stat"><strong><span class="kz-counter" data-count="8"></span></strong><span>ministries</span></div>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <div class="kz-hero-photo position-relative">
                            %(photo)s
                            <div class="kz-hero-card kz-hero-card-date">
                                <span class="kz-card-label">Next Friday catch-up</span>
                                <strong data-next-friday-long>&hellip;</strong>
                                <span class="kz-card-time"><i class="fas fa-clock"></i> 8:00 PM EAT &middot; Google Meet</span>
                            </div>
                            <div class="kz-hero-card kz-hero-card-badge">
                                <i class="fas fa-fire-flame-curved"></i>
                                <span>KIZAZI 2026<small>14&ndash;15 Aug &mdash; two days on fire</small></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="kz-zigzag kz-zigzag-hero"></div>
        </section>
        <!-- Hero End -->
""" % {"tagline": SITE["tagline"], "verse": SITE["verse"], "ref": SITE["verse_ref"],
       "countries": SITE["countries"], "reg": REG_URL, "meet": MEET_URL,
       "photo": img(0, "KIZAZI 2026 — two days on fire", cls="img-fluid rounded-4 w-100", eager=True)}


def about_section():
    return """        <!-- About Start -->
        <section class="kz-about container-fluid py-5" id="about">
            <div class="container py-4">
                <div class="row align-items-center g-5">
                    <div class="col-lg-6 kz-reveal">
                        <div class="kz-about-collage position-relative">
                            <div class="kz-about-main position-relative">
                                %(main)s
                                <button type="button" class="kz-play" data-bs-toggle="modal" data-bs-target="#kz-media-modal"
                                        aria-label="Play KIZAZI 2026 highlights">
                                    <span class="kz-play-icon"></span>
                                </button>
                            </div>
                            <div class="kz-about-small">%(small)s</div>
                            <span class="kz-about-stamp kz-hand">every. single. friday.</span>
                        </div>
                    </div>
                    <div class="col-lg-6 kz-reveal">
                        <span class="kz-kicker">Our Story</span>
                        <h2 class="kz-section-title">Who is <span class="kz-grad-text">KIZAZI</span>?</h2>
                        <p>&ldquo;Kizazi&rdquo; means <em>generation</em>. We are KIZAZI Phenomenal &mdash; a Christian
                        youth movement serving %(countries)s, built on one verse: <strong>%(verse_ref)s</strong>.</p>
                        <p>We are students, first-years, fresh graduates and young professionals who decided
                        this generation will not be skipped &mdash; by the devil, by the world, or by the church.
                        We worship loudly, study the Word seriously, and carry one another for real.</p>
                        <ul class="kz-check-list">
                            <li><i class="fas fa-check"></i> Worship that gets you on your feet</li>
                            <li><i class="fas fa-check"></i> Discipleship that gets you rooted</li>
                            <li><i class="fas fa-check"></i> A family that carries you home</li>
                        </ul>
                        <div class="d-flex flex-wrap gap-3 mt-4">
                            <a class="btn kz-btn kz-btn-dark" href="about.html">Our Story</a>
                            <a class="btn kz-btn kz-btn-ghost-dark" href="ministries.html">Explore Ministries</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- About End -->

        <!-- Media Modal (play button) -->
        <div class="modal fade" id="kz-media-modal" tabindex="-1" aria-hidden="true">
            <div class="modal-dialog modal-lg modal-dialog-centered">
                <div class="modal-content kz-media-modal border-0">
                    <div class="modal-header border-0">
                        <h5 class="modal-title text-white">KIZAZI 2026 &mdash; highlights film <span class="kz-hand kz-hand-gold">(coming soon)</span></h5>
                        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body p-0">
                        <div class="position-relative">
                            %(modal_photo)s
                            <div class="kz-media-overlay">
                                <span class="kz-hand kz-media-hand">until the film drops &mdash;</span>
                                <strong>be there live, every Friday.</strong>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer border-0 bg-transparent">
                        <a href="%(meet)s" target="_blank" rel="noopener" class="btn kz-btn kz-btn-sweep text-white me-2">Join Friday Catch-Up</a>
                        <a href="gallery.html" class="btn kz-btn kz-btn-ghost text-white">Browse the gallery</a>
                    </div>
                </div>
            </div>
        </div>
        <!-- Media Modal End -->
""" % {"main": img(1, "KIZAZI 2026 — worship night", cls="img-fluid rounded-4 w-100", eager=True),
       "small": img(2, "KIZAZI 2026 — the fam", cls="img-fluid rounded-4 w-100"),
       "modal_photo": img(3, "KIZAZI 2026 highlights", cls="img-fluid w-100 kz-media-photo", eager=True),
       "countries": SITE["countries"], "verse_ref": SITE["verse_ref"], "meet": MEET_URL}


def services_section():
    cards = []
    for slug, icon, name, blurb, _detail, _expect in MINISTRIES:
        cards.append("""<div class="col-md-6 col-xl-3 kz-reveal">
                        <a class="kz-service-card" href="ministries.html#w-%(slug)s">
                            <div class="kz-service-icon"><i class="fas %(icon)s"></i></div>
                            <h4 class="kz-service-name">%(name)s</h4>
                            <p class="kz-service-blurb">%(blurb)s</p>
                            <span class="kz-service-more">Step in <i class="fas fa-arrow-right"></i></span>
                        </a>
                    </div>""" % {"slug": slug, "icon": icon, "name": name, "blurb": blurb})
    return """        <!-- Ministries / Services Start -->
        <section class="kz-services container-fluid py-5" id="ministries">
            <div class="container py-4">
                %(head)s
                <div class="row g-4">
%(cards)s
                </div>
                <div class="text-center mt-5 kz-reveal">
                    <a class="btn kz-btn kz-btn-dark" href="ministries.html">All 8 Ministries <i class="fas fa-arrow-right ms-2"></i></a>
                </div>
            </div>
        </section>
        <!-- Ministries / Services End -->
""" % {"head": section_head("The Ministry Family", "Eight doorways, <span class='kz-grad-text'>one fire</span>",
                            "Every ministry is a doorway into the same thing: a generation being shaped by Jesus."),
       "cards": "\n".join(cards)}


def programs_section():
    cards = [program_card(p) for p in PROGRAMS]
    return """        <!-- Programs Start -->
        <section class="kz-programs container-fluid py-5 kz-section-tint" id="programs">
            <div class="container py-4">
                %(head)s
                <div class="row g-4">
%(cards)s
                </div>
                <div class="text-center mt-5 kz-reveal">
                    <a class="btn kz-btn kz-btn-dark" href="programs.html">All Programs <i class="fas fa-arrow-right ms-2"></i></a>
                </div>
            </div>
        </section>
        <!-- Programs End -->
""" % {"head": section_head("Programs", "Pick a track, <span class='kz-grad-text'>get in</span>",
                            "Structured ways to go deeper &mdash; every program is free unless it says otherwise."),
       "cards": "\n".join(cards)}


def program_card(p):
    name, badge, photo, desc, leader, initials, when, where = p
    return """<div class="col-md-6 col-xl-4 kz-reveal">
                    <article class="kz-program-card">
                        <div class="kz-program-img">
                            %(photo)s
                            <span class="kz-rate-badge">%(badge)s</span>
                        </div>
                        <div class="kz-program-body">
                            <h4 class="kz-program-name">%(name)s</h4>
                            <p class="kz-program-desc">%(desc)s</p>
                        </div>
                        <div class="kz-program-leader">
                            <span class="kz-leader-avatar" aria-hidden="true">%(initials)s</span>
                            <span class="kz-leader-text"><strong>%(leader)s</strong><small>leads this track</small></span>
                        </div>
                        <div class="kz-program-meta">
                            <span><i class="fas fa-calendar-check"></i> %(when)s</span>
                            <span><i class="fas fa-map-marker-alt"></i> %(where)s</span>
                        </div>
                    </article>
                </div>""" % {"photo": img(photo, "%s — program" % name, cls="img-fluid"),
                             "badge": badge, "name": name, "desc": desc, "leader": leader,
                             "initials": initials, "when": when, "where": where}


def events_section():
    cards = [event_card(e, b) for e, b in zip(EVENTS, EVENT_BADGES)]
    return """        <!-- Events Start -->
        <section class="kz-events container-fluid py-5" id="events">
            <div class="container py-4">
                %(head)s
                <div class="row g-4">
%(cards)s
                </div>
                <div class="text-center mt-5 kz-reveal">
                    <a class="btn kz-btn kz-btn-dark" href="events.html">All Events <i class="fas fa-arrow-right ms-2"></i></a>
                </div>
            </div>
        </section>
        <!-- Events End -->
""" % {"head": section_head("Events", "Never miss <span class='kz-grad-text'>the fire</span>",
                            "Fridays are set in stone. Everything else drops on our socials first."),
       "cards": "\n".join(cards)}


def event_card(e, badge):
    if e["when"] == "friday":
        badge_html = ('<div class="kz-event-date kz-event-date-auto">'
                      '<span data-next-friday-day>&ndash;</span><small data-next-friday-mon>&ndash;</small></div>')
    else:
        big, small = badge
        badge_html = '<div class="kz-event-date"><span>%s</span><small>%s</small></div>' % (big, small)
    when_html = ('<span data-next-friday-long>&hellip;</span>' if e["when"] == "friday" else e["when"])
    return """<div class="col-md-6 col-xl-3 kz-reveal">
                    <article class="kz-event-card">
                        <div class="kz-event-photo-wrap position-relative">
                            <div class="kz-event-photo">%(photo)s</div>
                            %(badge)s
                        </div>
                        <div class="kz-event-body">
                            <span class="kz-event-tag">%(tag)s</span>
                            <h4 class="kz-event-title">%(title)s</h4>
                            <p class="kz-event-desc">%(desc)s</p>
                            <ul class="kz-event-list">
                                <li><i class="fas fa-calendar"></i> %(when)s</li>
                                <li><i class="fas fa-clock"></i> %(time)s</li>
                                <li><i class="fas fa-map-marker-alt"></i> %(place)s</li>
                            </ul>
                            <a class="btn kz-btn kz-btn-sweep text-white w-100" href="%(url)s" target="_blank" rel="noopener"><i class="fas %(icon)s me-2"></i>%(cta)s</a>
                        </div>
                    </article>
                </div>""" % {"photo": img(e["photo"], alt_of(e["title"]), cls="img-fluid"),
                             "badge": badge_html, "tag": e["tag"], "title": e["title"], "desc": e["desc"],
                             "when": when_html, "time": e["time"], "place": e["place"],
                             "url": e["cta_url"], "icon": e["cta_icon"], "cta": e["cta_label"]}


def blog_section():
    cards = [blog_card(b, full=False) for b in BLOG]
    return """        <!-- Blog Start -->
        <section class="kz-blog container-fluid py-5 kz-section-tint" id="blog">
            <div class="container py-4">
                %(head)s
                <div class="row g-4 justify-content-center">
%(cards)s
                </div>
                <div class="text-center mt-5 kz-reveal">
                    <a class="btn kz-btn kz-btn-dark" href="blog.html">Read the Blog <i class="fas fa-arrow-right ms-2"></i></a>
                </div>
            </div>
        </section>
        <!-- Blog End -->
""" % {"head": section_head("Blog", "Word to the <span class='kz-grad-text'>generation</span>",
                            "Devotionals, recaps and honest conversations from the KIZAZI fam."),
       "cards": "\n".join(cards)}


def blog_card(b, full=False):
    title, date, team, initials, photo, tag, body = b
    if full:
        inner = "".join("<p>%s</p>" % p for p in body)
        return """<article class="kz-blog-post kz-reveal">
                        <div class="kz-blog-post-img">%(photo)s</div>
                        <div class="kz-blog-post-body">
                            <div class="kz-blog-post-meta">
                                <span class="kz-event-tag">%(tag)s</span>
                                <span><i class="fas fa-calendar"></i> %(date)s</span>
                                <span class="d-flex align-items-center gap-2"><span class="kz-initials-avatar kz-initials-sm" aria-hidden="true">%(initials)s</span> %(team)s</span>
                            </div>
                            <h3 class="kz-blog-post-title">%(title)s</h3>
                            %(inner)s
                        </div>
                    </article>""" % {"photo": img(photo, alt_of(title), cls="img-fluid"),
                                    "tag": tag, "date": date, "initials": initials, "team": team,
                                    "title": title, "inner": inner}
    return """<div class="col-md-6 col-xl-4 kz-reveal">
                    <article class="kz-blog-card">
                        <div class="kz-blog-card-img">%(photo)s</div>
                        <div class="kz-blog-card-meta">
                            <span class="kz-event-tag">%(tag)s</span>
                            <span><i class="fas fa-calendar"></i> %(date)s</span>
                        </div>
                        <div class="kz-blog-card-body">
                            <h4 class="kz-blog-card-title">%(title)s</h4>
                            <p class="kz-blog-card-excerpt">%(excerpt)s</p>
                            <div class="kz-blog-card-author d-flex align-items-center gap-2">
                                <span class="kz-initials-avatar kz-initials-sm" aria-hidden="true">%(initials)s</span>
                                <span>%(team)s</span>
                            </div>
                            <a class="kz-blog-read" href="blog.html">Read more <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </article>
                </div>""" % {"photo": img(photo, alt_of(title), cls="img-fluid"), "tag": tag, "date": date,
                             "initials": initials, "team": team, "title": title, "excerpt": body[0]}


def team_section(limit=4):
    cards = [team_card(t) for t in TEAMS[:limit]]
    more = ""
    if limit < len(TEAMS):
        more = """<div class="text-center mt-5 kz-reveal">
                    <a class="btn kz-btn kz-btn-dark" href="team.html">All Serving Teams <i class="fas fa-arrow-right ms-2"></i></a>
                </div>"""
    return """        <!-- Team Start -->
        <section class="kz-team container-fluid py-5" id="team">
            <div class="container py-4">
                %(head)s
                <div class="row g-4 justify-content-center">
%(cards)s
                </div>
%(more)s
            </div>
        </section>
        <!-- Team End -->
""" % {"head": section_head("The Team", "Servants, not <span class='kz-grad-text'>headshots</span>",
                            "We serve as teams &mdash; the same way the body of Christ actually works. Faces come when the team says so."),
       "cards": "\n".join(cards), "more": more}


def team_card(t):
    initials, name, desc, ministry = t
    return """<div class="col-md-6 col-xl-3 kz-reveal">
                    <div class="kz-team-card">
                        <span class="kz-team-tile" aria-hidden="true">%(initials)s</span>
                        <h4 class="kz-team-name">%(name)s</h4>
                        <p class="kz-team-desc">%(desc)s</p>
                        <span class="kz-team-serving"><i class="fas fa-arrow-right"></i> Serves under %(ministry)s</span>
                    </div>
                </div>""" % {"initials": initials, "name": name, "desc": desc, "ministry": ministry}


def testimonial_section():
    items = [testimonial_item(t) for t in TESTIMONIALS]
    return """        <!-- Testimonial Start -->
        <section class="kz-testimonial container-fluid py-5 kz-section-tint" id="testimonial">
            <div class="container py-4">
                %(head)s
                <div class="owl-carousel kz-testimonial-carousel kz-reveal">
%(items)s
                </div>
                <div class="text-center mt-5 kz-reveal">
                    <a class="btn kz-btn kz-btn-dark" href="testimonial.html">More Testimonies <i class="fas fa-arrow-right ms-2"></i></a>
                </div>
            </div>
        </section>
        <!-- Testimonial End -->
""" % {"head": section_head("Testimonials", "The fam, <span class='kz-grad-text'>in their words</span>"),
       "items": "\n".join(items)}


def testimonial_item(t):
    initials, label, quote = t
    stars = "".join('<i class="fas fa-star"></i>' for _ in range(5))
    return """<div class="testimonial-item">
                        <div class="kz-testimonial-card">
                            <i class="fas fa-quote-right kz-testimonial-quote"></i>
                            <p class="kz-testimonial-text">&ldquo;%(quote)s&rdquo;</p>
                            <div class="kz-testimonial-person">
                                <span class="kz-initials-avatar" aria-hidden="true">%(initials)s</span>
                                <span class="kz-testimonial-meta"><strong>%(initials)s</strong><small>%(label)s</small></span>
                                <span class="kz-testimonial-stars" aria-label="5 out of 5 stars">%(stars)s</span>
                            </div>
                        </div>
                    </div>""" % {"initials": initials, "label": label, "quote": quote, "stars": stars}


def cta_band():
    return """        <!-- CTA Start -->
        <section class="kz-cta-band position-relative">
            <div class="kz-zigzag kz-zigzag-cta"></div>
            <div class="container py-5 py-lg-6 text-center text-white">
                <span class="kz-hand kz-cta-hand">no small steps in this house &hellip;</span>
                <h2 class="kz-cta-title">Ready to be <span class="kz-grad-text kz-grad-text-light">phenomenal</span>?</h2>
                <p class="kz-cta-sub">&ldquo;%(verse)s&rdquo; &mdash; <em>%(ref)s</em></p>
                <div class="d-flex justify-content-center flex-wrap gap-3">
                    <a class="btn kz-btn kz-btn-sweep btn-lg text-white" href="%(reg)s" target="_blank" rel="noopener">Register &mdash; it&rsquo;s free</a>
                    <a class="btn kz-btn kz-btn-ghost btn-lg text-white" href="%(meet)s" target="_blank" rel="noopener">This Friday &middot; 8:00 PM EAT</a>
                </div>
            </div>
        </section>
        <!-- CTA End -->
""" % {"verse": SITE["verse"], "ref": SITE["verse_ref"], "reg": REG_URL, "meet": MEET_URL}


def verse_band():
    return """        <!-- Verse Band -->
        <section class="kz-verse-band position-relative">
            <div class="kz-zigzag kz-zigzag-verse"></div>
            <div class="container py-5 text-center text-white">
                <i class="fas fa-cross kz-verse-cross"></i>
                <blockquote class="kz-verse-text">&ldquo;%(verse)s&rdquo;</blockquote>
                <cite class="kz-verse-cite kz-hand">&mdash; %(ref)s</cite>
            </div>
        </section>
        <!-- Verse Band End -->
""" % {"verse": SITE["verse"], "ref": SITE["verse_ref"]}


# ------------------------------------------------------------------- pages ---
def page_index():
    return (hero_header() + marquee() + about_section() + services_section() +
            programs_section() + events_section() + blog_section() +
            team_section(limit=4) + testimonial_section() + cta_band())


def page_about():
    story = """        <!-- Story Start -->
        <section class="container-fluid kz-about-2 py-5">
            <div class="container py-4">
                <div class="row align-items-center g-5">
                    <div class="col-lg-6 kz-reveal">
                        <span class="kz-kicker">Our Story</span>
                        <h2 class="kz-section-title">A generation that <span class="kz-grad-text">refused to be skipped</span></h2>
                        <p>It started with a question on a Friday night: <em>what if our generation is the one?</em>
                        A handful of students, a Google Meet link, one verse on the screen &mdash; %(verse_ref)s.</p>
                        <p>From that night, KIZAZI Phenomenal grew into a cross-border youth family across
                        %(countries)s: worship nights, discipleship cells, prayer watches, campus tours and
                        creative labs. No headquarters worship, no VIP seating &mdash; just a generation that
                        decided faith was not a phase, and fire was not a gimmick.</p>
                        <p>Two days in August 2026 &mdash; <strong>KIZAZI 2026</strong> &mdash; proved what we had
                        been claiming all along: this generation shows up. The photos are in the
                        <a href="gallery.html">gallery</a>; the next conference is already being built.</p>
                        <div class="d-flex flex-wrap gap-3 mt-2">
                            <a class="btn kz-btn kz-btn-sweep text-white" href="%(reg)s" target="_blank" rel="noopener">Join the Movement <i class="fas fa-bolt ms-2"></i></a>
                        </div>
                    </div>
                    <div class="col-lg-6 kz-reveal">
                        <div class="kz-about-strip">
                            %(p1)s
                            %(p2)s
                            %(p3)s
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Story End -->
""" % {"verse_ref": SITE["verse_ref"], "countries": SITE["countries"], "reg": REG_URL,
       "p1": img(36, "KIZAZI 2026 — day one", cls="img-fluid rounded-4"),
       "p2": img(37, "KIZAZI 2026 — worship", cls="img-fluid rounded-4"),
       "p3": img(38, "KIZAZI 2026 — the fam", cls="img-fluid rounded-4")}

    stats = """        <!-- Stats -->
        <section class="kz-stats container-fluid">
            <div class="container py-4">
                <div class="row g-4 text-center">
                    <div class="col-6 col-lg-3 kz-reveal"><div class="kz-stat"><strong><span class="kz-counter" data-count="4"></span></strong><span>nations</span></div></div>
                    <div class="col-6 col-lg-3 kz-reveal"><div class="kz-stat"><strong><span class="kz-counter" data-count="500" data-suffix="+"></span></strong><span>young people reached</span></div></div>
                    <div class="col-6 col-lg-3 kz-reveal"><div class="kz-stat"><strong><span class="kz-counter" data-count="8"></span></strong><span>ministries</span></div></div>
                    <div class="col-6 col-lg-3 kz-reveal"><div class="kz-stat"><strong><span class="kz-counter" data-count="52"></span></strong><span>Fridays a year</span></div></div>
                </div>
            </div>
        </section>
        <!-- Stats End -->
"""

    mvv = """        <!-- Mission / Vision / Values -->
        <section class="container-fluid kz-mvv py-5">
            <div class="container py-4">
                %(head)s
                <div class="row g-4">
                    <div class="col-lg-4 kz-reveal">
                        <div class="kz-mvv-card">
                            <div class="kz-mvv-icon"><i class="fas fa-crosshairs"></i></div>
                            <h4>Mission</h4>
                            <p>Make East Africa&rsquo;s next generation fearless for Jesus &mdash; rooted in the Word,
                            bold in the culture, faithful in the details.</p>
                        </div>
                    </div>
                    <div class="col-lg-4 kz-reveal">
                        <div class="kz-mvv-card">
                            <div class="kz-mvv-icon"><i class="fas fa-eye"></i></div>
                            <h4>Vision</h4>
                            <p>A generation that leads the church, the campus and the culture with the gospel
                            &mdash; and sends the next one after it.</p>
                        </div>
                    </div>
                    <div class="col-lg-4 kz-reveal">
                        <div class="kz-mvv-card">
                            <div class="kz-mvv-icon"><i class="fas fa-heart"></i></div>
                            <h4>Values</h4>
                            <p>Radical faith. Holy friendship. Bold creativity. Servant hearts.
                            Excellence &mdash; God is not impressed by almost.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Mission / Vision / Values End -->
""" % {"head": section_head("Why We Exist", "Mission, vision &amp; <span class='kz-grad-text'>values</span>")}

    believe = """        <!-- What we believe -->
        <section class="container-fluid kz-believe py-5 kz-section-tint">
            <div class="container py-4">
                <div class="row align-items-center g-5">
                    <div class="col-lg-6 kz-reveal">
                        <div class="kz-believe-photo">%(photo)s</div>
                    </div>
                    <div class="col-lg-6 kz-reveal">
                        <span class="kz-kicker">The Basics</span>
                        <h2 class="kz-section-title">What we <span class="kz-grad-text">believe</span></h2>
                        <ul class="kz-check-list kz-check-list-lg">
                            <li><i class="fas fa-check"></i> <span><strong>Jesus first.</strong> He is the whole gospel &mdash; not one verse of it.</span></li>
                            <li><i class="fas fa-check"></i> <span><strong>The Bible is true.</strong> We read it to be changed, not just quoted.</span></li>
                            <li><i class="fas fa-check"></i> <span><strong>Prayer is real.</strong> Heaven listens, especially when we stop whispering.</span></li>
                            <li><i class="fas fa-check"></i> <span><strong>Community is essential.</strong> Nobody gets to grow up alone.</span></li>
                            <li><i class="fas fa-check"></i> <span><strong>The world matters.</strong> Campus, career, culture &mdash; all of it is ministry ground.</span></li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        <!-- What we believe End -->
""" % {"photo": img(39, "KIZAZI Phenomenal — community", cls="img-fluid rounded-4")}

    return (page_header("About Us", "Who we are, where we came from, and the verse that runs everything.", 17, "Our Story") +
            story + verse_band() + stats + mvv + believe + cta_band())


def page_ministries():
    cards = []
    for slug, icon, name, blurb, detail, expect in MINISTRIES:
        expect_html = "".join("<li>%s</li>" % e for e in expect)
        cards.append("""<div class="col-lg-6 kz-reveal">
                    <div class="kz-flip" id="w-%(slug)s">
                        <div class="kz-flip-inner">
                            <div class="kz-flip-front">
                                <div class="kz-flip-icon"><i class="fas %(icon)s"></i></div>
                                <h3 class="kz-flip-name">%(name)s</h3>
                                <p class="kz-flip-blurb">%(blurb)s</p>
                                <span class="kz-flip-hint">flip for the real talk <i class="fas fa-rotate"></i></span>
                            </div>
                            <div class="kz-flip-back">
                                <h4>%(name)s</h4>
                                <p>%(detail)s</p>
                                <ul class="kz-flip-expect">%(expect)s</ul>
                                <a class="btn kz-btn kz-btn-sweep text-white" href="%(reg)s" target="_blank" rel="noopener"><i class="fas fa-bolt me-2"></i>Sign me up</a>
                            </div>
                        </div>
                    </div>
                </div>""" % {"slug": slug, "icon": icon, "name": name, "blurb": blurb,
                             "detail": detail, "expect": expect_html, "reg": REG_URL})
    return (page_header("Ministries", "Eight doorways into the same fire — find the one God opened for you.", 18, "8 Doorways") +
            """        <section class="container-fluid kz-ministries py-5">
            <div class="container py-4">
                %(head)s
                <div class="row g-4">
%(cards)s
                </div>
            </div>
        </section>
""" % {"head": section_head("Ministries", "Every ministry is a <span class='kz-grad-text'>doorway</span>",
                          "None of them are optional, and all of them are open. Hover (or tap) a card for the real talk."),
       "cards": "\n".join(cards)} +
            cta_band())


def page_programs():
    cards = [program_card(p) for p in PROGRAMS]
    rooted = """        <!-- Rooted timeline -->
        <section class="container-fluid kz-rooted py-5 kz-section-tint">
            <div class="container py-4">
                %(head)s
                <div class="row g-4">
                    <div class="col-lg-4 kz-reveal">
                        <div class="kz-phase-card">
                            <span class="kz-phase-num">01</span>
                            <h4>Weeks 1&ndash;4 &middot; Foundation</h4>
                            <p>Who God is. What the gospel actually says. How to read your Bible without crying by chapter two (okay, maybe a little crying).</p>
                        </div>
                    </div>
                    <div class="col-lg-4 kz-reveal">
                        <div class="kz-phase-card">
                            <span class="kz-phase-num">02</span>
                            <h4>Weeks 5&ndash;8 &middot; Deep Roots</h4>
                            <p>Prayer, obedience, sin and freedom &mdash; the stuff that separates a religion from a relationship.</p>
                        </div>
                    </div>
                    <div class="col-lg-4 kz-reveal">
                        <div class="kz-phase-card">
                            <span class="kz-phase-num">03</span>
                            <h4>Weeks 9&ndash;12 &middot; Go Forth</h4>
                            <p>Sending you out: a serving role, a cell of your own, a campus, a mission. You graduate by being sent.</p>
                        </div>
                    </div>
                </div>
                <p class="kz-rooted-note kz-hand">graduates of Rooted join the mentorship &amp; serving teams &mdash; the fire keeps moving.</p>
            </div>
        </section>
""" % {"head": section_head("Inside Rooted", "The 12 weeks, <span class='kz-grad-text'>phase by phase</span>",
                            "Our flagships discipleship track. One cohort at a time, in a small group, with a mentor who actually checks in.")}
    return (page_header("Programs", "Structured tracks to go deeper — every program has a door and a way in.", 19, "Go Deeper") +
            """        <section class="container-fluid kz-programs-2 py-5">
            <div class="container py-4">
                <div class="row g-4">
%(cards)s
                </div>
            </div>
        </section>
""" % {"cards": "\n".join(cards)} + rooted + cta_band())


def page_events():
    cards = [event_card(e, b) for e, b in zip(EVENTS, EVENT_BADGES)]
    featured = """        <!-- Featured: next Friday -->
        <section class="kz-events-featured container-fluid py-5">
            <div class="container">
                <div class="kz-featured-card kz-reveal">
                    <div class="kz-featured-info">
                        <span class="kz-event-tag kz-event-tag-light">Happens weekly &middot; never skip</span>
                        <h2 class="kz-featured-title">Phenomenal Friday &mdash; Online Catch-Up</h2>
                        <p>Worship, a Word bite, prayer and connection &mdash; live on Google Meet across
                        Kenya, Uganda, Tanzania and Rwanda. First-timers welcome, earphones optional (not recommended).</p>
                        <ul class="kz-event-list kz-event-list-light">
                            <li><i class="fas fa-calendar"></i> Next up: <strong data-next-friday-long>&hellip;</strong> <span class="kz-friday-rel" data-next-friday-rel></span></li>
                            <li><i class="fas fa-clock"></i> 8:00 PM EAT (5:00 PM UTC)</li>
                            <li><i class="fas fa-video"></i> Google Meet &mdash; link below</li>
                        </ul>
                        <div class="d-flex flex-wrap gap-3">
                            <a class="btn kz-btn kz-btn-sweep text-white btn-lg" href="%(meet)s" target="_blank" rel="noopener"><i class="fas fa-video me-2"></i>Join Live</a>
                            <a class="btn kz-btn kz-btn-ghost text-white btn-lg" href="%(reg)s" target="_blank" rel="noopener">Register with us</a>
                        </div>
                    </div>
                    <div class="kz-featured-photo">%(photo)s
                        <div class="kz-event-date kz-event-date-big kz-event-date-auto">
                            <span data-next-friday-day>&ndash;</span><small data-next-friday-mon>&ndash;</small>
                        </div>
                    </div>
                </div>
            </div>
        </section>
""" % {"meet": MEET_URL, "reg": REG_URL, "photo": img(34, "Phenomenal Friday — online catch-up", cls="img-fluid rounded-4 w-100")}

    past = """        <!-- Past flagship: KIZAZI 2026 -->
        <section class="kz-events-past container-fluid py-5">
            <div class="container py-4">
                <div class="kz-past-card kz-reveal">
                    <div class="kz-past-info">
                        <span class="kz-event-tag">Past flagship</span>
                        <h3 class="kz-past-title">KIZAZI 2026 <span class="kz-hand kz-hand-gold">&mdash; thank you, fam.</span></h3>
                        <p><strong>14&ndash;15 August 2026.</strong> Two days, one generation, zero chill. The highlight
                        film is in the works &mdash; until then, the 42 photos from the event live in the gallery.</p>
                        <a class="btn kz-btn kz-btn-sweep text-white" href="gallery.html"><i class="fas fa-images me-2"></i>Relive It in the Gallery</a>
                    </div>
                    <div class="kz-past-photos">
                        %(p1)s
                        %(p2)s
                        %(p3)s
                    </div>
                </div>
            </div>
        </section>
""" % {"p1": img(35, "KIZAZI 2026 — day one", cls="img-fluid rounded-4"),
       "p2": img(40, "KIZAZI 2026 — worship", cls="img-fluid rounded-4"),
       "p3": img(41, "KIZAZI 2026 — night two", cls="img-fluid rounded-4")}

    prepare = """        <!-- Prepare for Friday -->
        <section class="container-fluid kz-prepare py-5 kz-section-tint">
            <div class="container py-4">
                %(head)s
                <div class="row g-4">
                    <div class="col-lg-4 kz-reveal">
                        <div class="kz-prepare-card"><span class="kz-prepare-num">1</span><h4>Pray on your day</h4><p>Before you ever click Join, pray for the night, the speakers and your city. Five minutes counts.</p></div>
                    </div>
                    <div class="col-lg-4 kz-reveal">
                        <div class="kz-prepare-card"><span class="kz-prepare-num">2</span><h4>Set up your corner</h4><p>Quiet place, charged phone, earphones if you can. Camera on if you&rsquo;re up for it &mdash; faces make a family.</p></div>
                    </div>
                    <div class="col-lg-4 kz-reveal">
                        <div class="kz-prepare-card"><span class="kz-prepare-num">3</span><h4>Arrive 5 early</h4><p>Doors at 7:55, fire at 8:00. Grab a prayer topic from someone in the chat before you go.</p></div>
                    </div>
                </div>
            </div>
        </section>
""" % {"head": section_head("Before Friday", "Three habits that <span class='kz-grad-text'>level you up</span>")}

    return (page_header("Events", "Fridays are set in stone. Everything else drops on socials first.", 20, "What's On") +
            featured + past +
            """        <section class="container-fluid kz-events-2 py-5">
            <div class="container py-4">
                %(head)s
                <div class="row g-4">
%(cards)s
                </div>
            </div>
        </section>
""" % {"head": section_head("The Calendar", "Everything KIZAZI, <span class='kz-grad-text'>in one place</span>"),
       "cards": "\n".join(cards)} + prepare + cta_band())


def page_gallery():
    chips = ['<button type="button" class="kz-filter-chip active" data-filter="all">All <span class="kz-chip-count">%d</span></button>' % len(PHOTOS)]
    for key, label in GALLERY_CATS:
        count = sum(1 for i in range(len(PHOTOS)) if gallery_cat(i)[0] == key)
        chips.append('<button type="button" class="kz-filter-chip" data-filter="%s">%s <span class="kz-chip-count">%d</span></button>' % (key, label, count))

    items = []
    for i in range(len(PHOTOS)):
        key, label = gallery_cat(i)
        items.append("""<a class="kz-gallery-item" data-cat="%(key)s" href="%(href)s" data-lightbox="kizazi-2026" data-title="KIZAZI 2026 · %(label)s · photo %(num)d">
                    %(img)s
                    <span class="kz-gallery-cat">%(label)s</span>
                </a>""" % {"key": key, "href": durl(i, 1600), "label": label, "num": i + 1,
                            "img": img(i, "KIZAZI 2026 photo %d" % (i + 1), cls="img-fluid")})
    return (page_header("Gallery", "The entire KIZAZI 2026 album — 42 photos from two days that shook us. (Lightbox inside.)", 21, "KIZAZI 2026") +
            """        <section class="container-fluid kz-gallery-sec py-5">
            <div class="container py-4">
                <div class="kz-filter-bar kz-reveal">
%(chips)s
                </div>
                <p class="kz-gallery-note kz-hand">tap any photo to open it full-size &rarr;</p>
                <div class="kz-gallery-grid">
%(items)s
                </div>
            </div>
        </section>
""" % {"chips": "\n".join(chips), "items": "\n".join(items)} + cta_band())


def page_blog():
    posts = [blog_card(b, full=True) for b in BLOG]
    return (page_header("Blog", "Devotionals, recaps and honest conversations from the KIZAZI fam.", 22, "Word to You") +
            """        <section class="container-fluid kz-blog-sec py-5">
            <div class="container py-4">
                <div class="kz-blog-stack">
%(posts)s
                </div>
                <div class="kz-blog-coming kz-reveal text-center mt-5">
                    <p class="kz-hand kz-hand-dark mb-2">more is loading&hellip;</p>
                    <p class="mb-3">New devotionals drop on our socials before they land here.</p>
                    <div class="d-flex justify-content-center gap-3">
                        <a class="btn kz-btn kz-btn-dark" href="%(tiktok)s" target="_blank" rel="noopener"><i class="fab fa-tiktok me-2"></i>TikTok</a>
                        <a class="btn kz-btn kz-btn-dark" href="%(ig)s" target="_blank" rel="noopener"><i class="fab fa-instagram me-2"></i>Instagram</a>
                    </div>
                </div>
            </div>
        </section>
""" % {"posts": "\n".join(posts), "tiktok": TIKTOK_URL, "ig": INSTAGRAM_URL} + cta_band())


def page_team():
    cards = [team_card(t) for t in TEAMS]
    steps = """        <!-- How to serve -->
        <section class="container-fluid kz-serve py-5 kz-section-tint">
            <div class="container py-4">
                %(head)s
                <div class="row g-4">
                    <div class="col-lg-4 kz-reveal">
                        <div class="kz-serve-card"><span class="kz-prepare-num">1</span><h4>Register</h4><p>Fill the registration form &mdash; it tells the team where you are and what you&rsquo;re into.</p></div>
                    </div>
                    <div class="col-lg-4 kz-reveal">
                        <div class="kz-serve-card"><span class="kz-prepare-num">2</span><h4>Tell us your gift</h4><p>Singing? Design? Prayer? Driving the van? Every gift gets a door.</p></div>
                    </div>
                    <div class="col-lg-4 kz-reveal">
                        <div class="kz-serve-card"><span class="kz-prepare-num">3</span><h4>Join a team this term</h4><p>Teams meet, train and ship together. You&rsquo;ll know your team by your second Friday.</p></div>
                    </div>
                </div>
                <div class="text-center mt-5 kz-reveal">
                    <a class="btn kz-btn kz-btn-sweep text-white btn-lg" href="%(reg)s" target="_blank" rel="noopener"><i class="fas fa-hand-holding-heart me-2"></i>I Want to Serve</a>
                </div>
            </div>
        </section>
""" % {"head": section_head("How to Serve", "Three steps, <span class='kz-grad-text'>zero gatekeeping</span>"), "reg": REG_URL}
    intro_note = """        <section class="container-fluid kz-team-note py-5">
            <div class="container">
                <div class="kz-note-card kz-reveal text-center">
                    <i class="fas fa-users kz-note-icon"></i>
                    <p>We&rsquo;re a movement first, so this page shows <strong>serving teams and roles</strong> rather than
                    named individuals &mdash; no invented names, no borrowed faces. Real names and photos land here
                    as the team consents to be public. (And no, we will not put random event photos on leaders.)</p>
                </div>
            </div>
        </section>
"""
    return (page_header("Team", "The people behind the fire — and how to join one of the teams.", 23, "The Fam") +
            intro_note +
            """        <section class="container-fluid kz-team-sec py-5">
            <div class="container py-4">
                %(head)s
                <div class="row g-4 justify-content-center">
%(cards)s
                </div>
            </div>
        </section>
""" % {"head": section_head("Serving Teams", "Eight teams, <span class='kz-grad-text'>one body</span>"),
       "cards": "\n".join(cards)} + steps + cta_band())


def page_testimonial():
    cards = []
    for t in TESTIMONIALS:
        initials, label, quote = t
        stars = "".join('<i class="fas fa-star"></i>' for _ in range(5))
        cards.append("""<div class="col-lg-6 kz-reveal">
                    <div class="kz-testimonial-card kz-testimonial-card-lg">
                        <i class="fas fa-quote-right kz-testimonial-quote"></i>
                        <p class="kz-testimonial-text">&ldquo;%(quote)s&rdquo;</p>
                        <div class="kz-testimonial-person">
                            <span class="kz-initials-avatar" aria-hidden="true">%(initials)s</span>
                            <span class="kz-testimonial-meta"><strong>%(initials)s</strong><small>%(label)s</small></span>
                            <span class="kz-testimonial-stars" aria-label="5 out of 5 stars">%(stars)s</span>
                        </div>
                    </div>
                </div>""" % {"initials": initials, "label": label, "quote": quote, "stars": stars})
    return (page_header("Testimonial", "Voices from the family — real stories, initials only, consent first.", 24, "In Their Words") +
            """        <section class="container-fluid kz-testimonial-sec py-5">
            <div class="container py-4">
                %(head)s
                <div class="row g-4">
%(cards)s
                </div>
            </div>
        </section>
""" % {"head": section_head("Voices", "The fam, <span class='kz-grad-text'>in their words</span>",
                          "Illustrative quotes from where the family is today. Share yours and it can be here, with your consent."),
       "cards": "\n".join(cards)} + verse_band() +
            """        <section class="container-fluid kz-share py-5">
            <div class="container">
                <div class="kz-share-card kz-reveal text-center text-white">
                    <span class="kz-hand kz-cta-hand">your story could be next&hellip;</span>
                    <h2 class="kz-share-title">Share your story</h2>
                    <p>DM us on Instagram or fill the form &mdash; we&rsquo;ll find a way to feature you (with your name, or without, your call).</p>
                    <div class="d-flex justify-content-center flex-wrap gap-3">
                        <a class="btn kz-btn kz-btn-sweep btn-lg text-white" href="%(reg)s" target="_blank" rel="noopener">Send Your Story</a>
                        <a class="btn kz-btn kz-btn-ghost btn-lg text-white" href="%(ig)s" target="_blank" rel="noopener"><i class="fab fa-instagram me-2"></i>DM on Instagram</a>
                    </div>
                </div>
            </div>
        </section>
""" % {"reg": REG_URL, "ig": INSTAGRAM_URL})


def page_contact():
    friday = """        <section class="container-fluid kz-contact py-5">
            <div class="container py-4">
                %(head)s
                <div class="row g-4">
                    <div class="col-md-6 col-xl-3 kz-reveal">
                        <div class="kz-contact-card">
                            <div class="kz-contact-icon"><i class="fas fa-pen"></i></div>
                            <h4>Register with us</h4>
                            <p>The fastest way to say hi &mdash; join the family, pick a program, get on the map.</p>
                            <a class="kz-contact-link" href="%(reg)s" target="_blank" rel="noopener">Open the form <i class="fas fa-external-link-alt"></i></a>
                        </div>
                    </div>
                    <div class="col-md-6 col-xl-3 kz-reveal">
                        <div class="kz-contact-card">
                            <div class="kz-contact-icon"><i class="fas fa-video"></i></div>
                            <h4>Friday Catch-Up</h4>
                            <p>Next up: <strong data-next-friday-long>&hellip;</strong> at 8:00 PM EAT on Google Meet.</p>
                            <a class="kz-contact-link" href="%(meet)s" target="_blank" rel="noopener">Join the Meet <i class="fas fa-external-link-alt"></i></a>
                        </div>
                    </div>
                    <div class="col-md-6 col-xl-3 kz-reveal">
                        <div class="kz-contact-card">
                            <div class="kz-contact-icon"><i class="fab fa-instagram"></i></div>
                            <h4>Find us on socials</h4>
                            <p>TikTok, Instagram &amp; Facebook &mdash; the fastest replies are usually on DMs.</p>
                            <div class="d-flex gap-2">
                                <a class="kz-social kz-social-lg" href="%(tiktok)s" target="_blank" rel="noopener" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
                                <a class="kz-social kz-social-lg" href="%(ig)s" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                                <a class="kz-social kz-social-lg" href="%(fb)s" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-xl-3 kz-reveal">
                        <div class="kz-contact-card">
                            <div class="kz-contact-icon"><i class="fas fa-link"></i></div>
                            <h4>One link, everything</h4>
                            <p>%(linktree)s &mdash; soon you&rsquo;ll find every link in one place.</p>
                            <span class="kz-contact-soon">Coming soon</span>
                        </div>
                    </div>
                </div>
                <div class="kz-contact-honesty kz-reveal">
                    <p><i class="fas fa-info-circle me-2"></i> We deliberately haven&rsquo;t published an email, phone or
                    physical address yet &mdash; the moment they&rsquo;re confirmed they&rsquo;ll appear here and on our socials.</p>
                </div>
            </div>
        </section>
""" % {"head": section_head("Contact", "Say hi, <span class='kz-grad-text'>find the fire</span>",
                          "No inboxes invented, no addresses made up &mdash; these are the real doors."),
       "reg": REG_URL, "meet": MEET_URL, "tiktok": TIKTOK_URL, "ig": INSTAGRAM_URL,
       "fb": FACEBOOK_URL, "linktree": LINKTREE_NOTE}

    faq_items = [
        ("What exactly is KIZAZI Phenomenal?",
         "A Christian youth ministry and fellowship serving East Africa &mdash; "
         + SITE["countries"] + " &ldquo;Kizazi&rdquo; means <em>generation</em>. We exist so this "
         "generation knows Jesus deeply, worships boldly, and gets sent out into campuses, "
         "careers and culture."),
        ("Who can join? Do I have to be from East Africa?",
         "Students, fresh graduates, young professionals &mdash; anyone who&rsquo;s in it. If you&rsquo;re in East "
         "Africa you can join cells, events and trips; if you&rsquo;re anywhere else, Fridays are online, "
         "so the whole world can catch up with us."),
        ("What happens on Fridays?",
         "Worship, a Word bite, prayer and connection &mdash; live on Google Meet at 8:00 PM EAT. "
         "No registration needed to sit in; the link is right on the homepage."),
        ("How do I serve or reach the team?",
         "Fill the registration form and tell us your gift &mdash; the teams take it from there. "
         "Until our official email is published, the fastest way to reach a human is a DM on "
         "Instagram or TikTok."),
    ]
    items = []
    for i, (q, a) in enumerate(faq_items):
        items.append("""<div class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button kz-accordion-btn collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#kzFaq%(i)d"
                                        aria-expanded="%(expanded)s" aria-controls="kzFaq%(i)d">%(q)s</button>
                            </h2>
                            <div id="kzFaq%(i)d" class="accordion-collapse collapse" data-bs-parent="#kzFaq">
                                <div class="accordion-body">%(a)s</div>
                            </div>
                        </div>""" % {"q": q, "a": a, "i": i, "expanded": "true" if i == 0 else "false"})
    faq = """        <section class="container-fluid kz-faq py-5 kz-section-tint">
            <div class="container py-4">
                %(head)s
                <div class="row justify-content-center">
                    <div class="col-lg-8">
                        <div class="accordion kz-accordion" id="kzFaq">
%(items)s
                        </div>
                    </div>
                </div>
            </div>
        </section>
""" % {"head": section_head("FAQ", "Before you <span class='kz-grad-text'>ask&hellip;</span>"),
       "items": "\n".join(items), "countries": SITE["countries"]}
    return (page_header("Contact", "The real doors in — register, join the Friday, or DM the fam.", 25, "Talk to Us") +
            friday + faq + cta_band())


def page_404():
    body = """        <!-- 404 Start -->
        <section class="kz-404 container-fluid position-relative overflow-hidden">
            <div class="kz-hero-dots"></div>
            <div class="kz-aurora kz-aurora-1"></div>
            <div class="kz-aurora kz-aurora-2"></div>
            <div class="container py-5 py-lg-0 text-center text-white">
                <div style="min-height: 70vh;" class="d-flex flex-column align-items-center justify-content-center">
                    <span class="kz-hand kz-404-hand">oh no &mdash; this page burned away</span>
                    <h1 class="kz-404-code">4<span class="kz-grad-text">0</span>4</h1>
                    <p class="kz-404-sub">The page you&rsquo;re looking for isn&rsquo;t here &mdash; but the fire is.</p>
                    <div class="d-flex flex-wrap justify-content-center gap-3 mt-2">
                        <a class="btn kz-btn kz-btn-sweep btn-lg text-white" href="index.html"><i class="fas fa-home me-2"></i>Back Home</a>
                        <a class="btn kz-btn kz-btn-ghost btn-lg text-white" href="contact.html">Contact Us</a>
                        <a class="btn kz-btn kz-btn-ghost btn-lg text-white" href="gallery.html">See the Fire</a>
                    </div>
                    <p class="kz-verse-ref-404 kz-hand mt-4">&ldquo;%(verse_short)s&rdquo; &mdash; %(ref)s</p>
                </div>
            </div>
        </section>
        <!-- 404 End -->
""" % {"verse_short": SITE["verse"][:60] + "&hellip;", "ref": SITE["verse_ref"]}
    return body


# ---------------------------------------------------------------- assembly ---
PAGES_META = {
    "index.html": ("KIZAZI Phenomenal — A Generation on Fire for God",
                   "KIZAZI Phenomenal is a Christian youth ministry serving Kenya, Uganda, Tanzania and Rwanda. "
                   "Phenomenal Fridays, 8:00 PM EAT. Register free.",
                   "home", page_index),
    "about.html": ("About Us — KIZAZI Phenomenal",
                   "The story, mission, vision and values of KIZAZI Phenomenal — a youth movement built on 1 Timothy 4:12.",
                   "about", page_about),
    "ministries.html": ("Ministries — KIZAZI Phenomenal",
                   "Eight ministries: Worship & The Word, Discipleship Cells, Prayer & Intercession, Friday Online Catch-Up, "
                   "Outreach & Missions, Creative & Media Lab, Mentorship & Career, Community & Care.",
                   "ministries", page_ministries),
    "programs.html": ("Programs — KIZAZI Phenomenal",
                   "Rooted 12-week discipleship, Phenomenal Fridays, Creative Lab, Mentorship Circle, Campus Ambassadors and Serve East Africa.",
                   "programs", page_programs),
    "events.html": ("Events — KIZAZI Phenomenal",
                   "Phenomenal Friday Online Catch-Up (8:00 PM EAT), KIZAZI Conference 2027, Worship & Word Night and Campus & School Tour.",
                   "events", page_events),
    "gallery.html": ("Gallery — KIZAZI 2026 Photos — KIZAZI Phenomenal",
                   "The full KIZAZI 2026 album: 42 photos from two days on fire, in a filterable lightbox gallery.",
                   "gallery", page_gallery),
    "blog.html": ("Blog — KIZAZI Phenomenal",
                   "Devotionals, recaps and honest conversations from the KIZAZI Phenomenal family.",
                   "blog", page_blog),
    "team.html": ("Team — KIZAZI Phenomenal",
                   "The serving teams of KIZAZI Phenomenal and how to join one of them.",
                   "team", page_team),
    "testimonial.html": ("Testimonial — KIZAZI Phenomenal",
                   "Voices from the KIZAZI Phenomenal family — real stories, initials only, consent first.",
                   "testimonial", page_testimonial),
    "contact.html": ("Contact — KIZAZI Phenomenal",
                   "Register, join the Friday Catch-Up, find us on TikTok, Instagram and Facebook. Linktree coming soon.",
                   "contact", page_contact),
    "404.html": ("Page Not Found — KIZAZI Phenomenal",
                   "This page burned away — but the fire is. Head back to KIZAZI Phenomenal.",
                   "404", page_404),
}


def main():
    for file_, (title, desc, active, builder) in PAGES_META.items():
        html = head(title, desc) + body_open(active) + topbar() + navbar(active)
        html += builder()
        html += footer() + back_to_top() + scripts()
        path = os.path.join(ROOT, file_)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote %-18s %6d bytes" % (file_, len(html)))
    print("done — %d pages" % len(PAGES_META))


if __name__ == "__main__":
    main()
