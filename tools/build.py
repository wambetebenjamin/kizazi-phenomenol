#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KIZAZI Phenomenal, page composer (Hilltop-skin edition, 2026-09-24).

Layout & theme structure follows hilltopcc.net (structure only; all photos are
KIZAZI's own, vendored in img/gallery/ + img/hero/):

  home        full-bleed crossfading photo hero -> "join us friday" split card
              -> what's happening (event cards) -> get connected (photo tiles)
              -> fixed verse band -> groups & programs -> follow band
              -> join-the-team band -> dark footer with photo strip
  inner pages photo banner header with breadcrumb, then card grids / lists

Edit data in tools/build_common.py, then run:  python3 tools/build.py
Photos are curated & sharpened by:             python3 tools/process_photos.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_common as C  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def wow(delay="0.1s"):
    return ' class="wow fadeIn" data-wow-delay="%s"' % delay


# ------------------------------------------------------------- small pieces --
def chip(icon, text):
    return '<span class="ht-chip"><i class="fas %s"></i>%s</span>' % (icon, text)


def card_start(photo_i, tag, alt, delay):
    return """                <div%s>
                    <div class="ht-card">
                        <div class="ht-card-img">
                            %s
                            <span class="ht-card-tag">%s</span>
                        </div>
                        <div class="ht-card-body">
""" % (wow(delay), C.img(photo_i, alt, cls="img-fluid"), tag)


def card_end():
    return """                        </div>
                    </div>
                </div>
"""


# ---------------------------------------------------------------- page shell --
def page(title, desc, active, body, with_video_modal=True):
    return (C.head(title, desc)
            + C.body_open()
            + C.scroll_progress()
            + C.spinner()
            + C.header(active)
            + body
            + C.footer()
            + C.back_to_top()
            + (C.video_modal() if with_video_modal else "")
            + C.scripts())


# --------------------------------------------------------------------- home --
def hero():
    slides = "\n".join(
        '            <div class="ht-slide" %s role="img" aria-label="KIZAZI 2026 photo"></div>'
        % C.bg_file(p) for p in C.HERO_SLIDES)
    return """        <!-- Hero Start -->
        <section class="ht-hero" id="home">
%(slides)s
            <div class="ht-hero-shade"></div>
            <div class="container ht-hero-in">
                <p class="ht-hero-eyebrow">welcome to</p>
                <h1>KIZAZI <span>Phenomenal</span></h1>
                <p class="ht-hero-tag">%(tagline)s Worship, the Word and a family that carries you &mdash; across %(countries)s.</p>
                <div class="ht-hero-cta">
                    <a class="btn-kz" href="%(reg)s" target="_blank" rel="noopener">Register free</a>
                    <a class="btn-kz-line" href="%(meet)s" target="_blank" rel="noopener"><i class="fas fa-video me-2"></i>Join this Friday</a>
                </div>
                <p class="ht-hero-verse">&ldquo;%(verse)s&rdquo; &middot; %(verse_ref)s</p>
            </div>
            <a class="ht-hero-scroll" href="#friday" aria-label="Scroll to this Friday"><i class="fa fa-chevron-down"></i></a>
        </section>
        <!-- Hero End -->
""" % {"slides": slides, "tagline": C.SITE["tagline"],
       "countries": C.SITE["countries"], "reg": C.REG_URL, "meet": C.MEET_URL,
       "verse": C.SITE["verse"], "verse_ref": C.SITE["verse_ref"]}


def friday_join():
    return """        <!-- Join Us Start -->
        <section class="ht-section" id="friday">
            <div class="container">
                <div class="ht-join wow fadeIn" data-wow-delay="0.1s">
                    <div class="row g-0">
                        <div class="col-lg-6">
                            <div class="ht-join-photo h-100" %(bg)s role="img" aria-label="The family seated together"></div>
                        </div>
                        <div class="col-lg-6">
                            <div class="ht-join-body">
                                <span class="ht-kicker">join us</span>
                                <h3>For worship &amp; the Word, every Friday</h3>
                                <p class="text-muted">One link, whole family. We gather online every Friday at
                                8:00 PM EAT for worship, a Word bite, prayer and real connection &mdash;
                                Kenya, Uganda, Tanzania and Rwanda in one room.</p>
                                <div class="mb-3">
                                    %(chips)s
                                </div>
                                <p class="mb-4"><strong>Next gathering:</strong> <span data-next-friday-long>&hellip;</span> &middot; 8:00 PM EAT</p>
                                <div class="d-flex flex-wrap gap-2">
                                    <a class="btn-kz" href="%(meet)s" target="_blank" rel="noopener"><i class="fas fa-video me-2"></i>Open Google Meet</a>
                                    <a class="btn-kz-soft" href="%(reg)s" target="_blank" rel="noopener">Register free</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Join Us End -->
""" % {"bg": C.bg(26),
       "chips": chip("fa-video", "Live on Google Meet") +
                chip("fa-clock", "8:00 PM EAT") +
                chip("fa-globe-africa", "East Africa") +
                chip("fa-hand-holding-heart", "Free to join"),
       "meet": C.MEET_URL, "reg": C.REG_URL}


def whats_happening():
    cards = []
    for n, ev in enumerate(C.EVENTS[:3]):
        cards.append(card_start(ev["photo"], ev["tag"], ev["title"], "0.%ds" % (n + 1)))
        cards.append("""                            <h3><a href="events.html">%s</a></h3>
                            <p>%s</p>
                            <div class="ht-card-meta">
                                <span><i class="far fa-calendar-alt me-1"></i>%s</span>
                                <span><i class="far fa-clock me-1"></i>%s</span>
                                <span><i class="fas fa-map-marker-alt me-1"></i>%s</span>
                            </div>
                            <a class="ht-card-link" href="%s" target="_blank" rel="noopener">%s <i class="fa fa-arrow-right ms-1"></i></a>
""" % (ev["title"], ev["desc"], ev["when"], ev["time"], ev["place"], ev["cta_url"], ev["cta_label"]))
        cards.append(card_end())
    return """        <!-- What's Happening Start -->
        <section class="ht-section ht-section-mist">
            <div class="container">
%(head)s
                <div class="row g-4 mt-2">
%(cards)s
                </div>
                <div class="text-center mt-5">
                    <a class="btn-kz" href="events.html">View full calendar</a>
                </div>
            </div>
        </section>
        <!-- What's Happening End -->
""" % {"head": C.section_head("what&rsquo;s happening", "Events &amp; <span>Catch-Ups</span>",
                              "See what&rsquo;s on. Click a card for times, places and how to join in."),
       "cards": "".join(cards)}


def get_connected():
    tiles = []
    picks = [(0, 25), (1, 20), (2, 19)]
    for n, (mi, photo) in enumerate(picks):
        slug, icon, name, tag, desc, _bul = C.MINISTRIES[mi]
        tiles.append("""                <div%s>
                    <a class="ht-tile d-block" href="ministries.html#%s" %s>
                        <span class="ht-tile-bg" aria-hidden="true"></span>
                        <span class="ht-tile-in d-block">
                            <h3>%s</h3>
                            <p>%s</p>
                        </span>
                    </a>
                </div>
""" % (wow("0.%ds" % (n + 1)), slug, C.bg(photo), name, tag))
    return """        <!-- Get Connected Start -->
        <section class="ht-section">
            <div class="container">
%(head)s
                <div class="row g-4 mt-2">
%(tiles)s
                </div>
                <div class="text-center mt-5">
                    <a class="btn-kz" href="ministries.html">All eight ministries</a>
                </div>
            </div>
        </section>
        <!-- Get Connected End -->
""" % {"head": C.section_head("ministries for everyone", "Get <span>Connected</span>",
                              "A place to belong for every generation of this generation. Worship, cells, prayer and more &mdash; jump in where you fit."),
       "tiles": "".join(tiles)}


def verse_band():
    return """        <!-- Verse Band Start -->
        <section class="ht-band" %(bg)s>
            <div class="container">
                <span class="ht-kicker">our commission</span>
                <p class="ht-verse">&ldquo;%(verse)s&rdquo;</p>
                <p class="ht-verse-ref">%(verse_ref)s</p>
                <div class="mt-4">
                    <a class="btn-kz-line" href="about.html">Who we are</a>
                </div>
            </div>
        </section>
        <!-- Verse Band End -->
""" % {"bg": C.bg(39), "verse": C.SITE["verse"], "verse_ref": C.SITE["verse_ref"]}


def program_card(p, delay):
    name, rate, photo, desc, leader, initials, when, where, meta = p
    out = [card_start(photo, rate, name, delay)]
    out.append("""                            <h3><a href="programs.html#%s">%s</a></h3>
                            <p>%s</p>
                            <div class="ht-card-meta">
                                <span><i class="far fa-calendar-alt me-1"></i>%s</span>
                                <span><i class="fas fa-map-marker-alt me-1"></i>%s</span>
""" % (name.lower().replace(" ", "-"), name, desc, when, where))
    for m in meta:
        out.append("                                <span>%s</span>\n" % m)
    out.append("""                            </div>
                            <a class="ht-card-link" href="programs.html#%s">How it runs <i class="fa fa-arrow-right ms-1"></i></a>
""" % name.lower().replace(" ", "-"))
    out.append(card_end())
    return "".join(out)


def programs_section(on_home=True):
    cards = "".join(program_card(p, "0.%ds" % (n % 3 + 1))
                    for n, p in enumerate(C.PROGRAMS))
    cta = """                <div class="text-center mt-5">
                    <a class="btn-kz" href="programs.html">Program details</a>
                </div>
""" if on_home else ""
    return """                <div class="row g-4 mt-2">
%(cards)s
                </div>
%(cta)s""" % {"cards": cards, "cta": cta}


def programs_home():
    return """        <!-- Groups & Programs Start -->
        <section class="ht-section ht-section-mist">
            <div class="container">
%(head)s
%(body)s
            </div>
        </section>
        <!-- Groups & Programs End -->
""" % {"head": C.section_head("grow in your faith", "Groups &amp; <span>Programs</span>",
                              "Classes, circles and journeys designed to help you grow, connect and find community. Click a card to see how each one runs."),
       "body": programs_section(True)}


def follow_band():
    vids = C.videos()
    if vids:
        inner = "".join(
            '<a class="btn-kz-line me-2 btn-play" href="#" data-bs-toggle="modal" data-bs-target="#videoModal" data-src="%s"><i class="fas fa-play me-2"></i>%s</a>'
            % (v["embed"], v["title"]) for v in vids)
    else:
        inner = ('<a class="btn-kz-line me-2" href="%s" target="_blank" rel="noopener"><i class="fas fa-play me-2"></i>Watch on TikTok</a>'
                 % C.TIKTOK_URL)
    socials = "".join(
        '<a class="btn-kz-line me-2" href="%s" target="_blank" rel="noopener"><i class="%s me-2"></i>%s</a>'
        % (u, i, l) for u, i, l in
        [(C.INSTAGRAM_URL, "fab fa-instagram", "Instagram"),
         (C.FACEBOOK_URL, "fab fa-facebook-f", "Facebook")])
    return """        <!-- Follow Band Start -->
        <section class="ht-band" %(bg)s>
            <div class="container">
                <span class="ht-kicker">kizazi on film</span>
                <h2 class="ht-h2">Follow the <span>fire</span></h2>
                <p class="ht-lead">The KIZAZI 2026 highlight film is being cut by the Media &amp; Creative Crew.
                Until it drops, the moments live on our socials &mdash; worship, word and everything between.</p>
                <div class="d-flex justify-content-center flex-wrap">%(inner)s%(socials)s</div>
            </div>
        </section>
        <!-- Follow Band End -->
""" % {"bg": C.bg(34), "inner": inner, "socials": socials}


def team_band():
    return """        <!-- Join The Team Start -->
        <section class="ht-band" %(bg)s>
            <div class="container">
                <span class="ht-kicker">ministries for everyone</span>
                <h2 class="ht-h2">Join the <span>team</span></h2>
                <p class="ht-lead">Get involved and make a difference. Worship &amp; sound, prayer watch, media crew,
                hospitality &mdash; we&rsquo;d love for you to join the team, use your gifts and help carry the mission.</p>
                <div class="d-flex justify-content-center flex-wrap gap-2">
                    <a class="btn-kz" href="team.html">Meet the serving teams</a>
                    <a class="btn-kz-line" href="testimonial.html">Read testimonies</a>
                </div>
            </div>
        </section>
        <!-- Join The Team End -->
""" % {"bg": C.bg(17)}


def build_index():
    body = (hero() + friday_join() + whats_happening() + get_connected()
            + verse_band() + programs_home() + follow_band() + team_band())
    return page("KIZAZI Phenomenal: A Generation on Fire for God",
                "KIZAZI Phenomenal is a Christian youth ministry serving Kenya, Uganda, Tanzania and Rwanda. Phenomenal Fridays, 8:00 PM EAT. Register free.",
                "home", body)


# -------------------------------------------------------------------- about --
def build_about():
    stat_html = "\n".join(
        """                    <div class="col-6 col-md-3">
                        <div class="ht-stat">
                            <b><span data-kz-count="%s" data-kz-suffix="%s">%s%s</span></b>
                            <span>%s</span>
                        </div>
                    </div>""" % (num.rstrip("+") if num.isdigit() else num, suf, num, suf, label)
        for num, suf, label in
        [("4", "", "nations, one family"), ("500", "+", "young people reached"),
         ("8", "", "ministries"), ("52", "", "Fridays a year")])
    delve = [
        ("ministries.html", 3, "Our Ministries",
         "Worship, cells, prayer, outreach and more &mdash; opportunities to grow and serve together."),
        ("programs.html", 13, "Groups &amp; Programs",
         "Rooted, Mentorship Circles, the Creative Lab: journeys that help you grow in faith."),
        ("team.html", 12, "Meet the Team",
         "The serving crews and the patron who carry this movement week to week."),
    ]
    delve_html = ""
    for n, (href, photo, name, blurb) in enumerate(delve):
        delve_html += """                <div%s>
                    <a class="ht-tile d-block" style="min-height: 280px;" href="%s" %s>
                        <span class="ht-tile-bg" aria-hidden="true"></span>
                        <span class="ht-tile-in d-block">
                            <h3>%s</h3>
                            <p>%s</p>
                        </span>
                    </a>
                </div>
""" % (wow("0.%ds" % (n + 1)), href, C.bg(photo), name, blurb)
    body = C.page_header(
        "About", "One generation, four nations, on fire for God.", 2)
    body += """        <!-- Story Start -->
        <section class="ht-section">
            <div class="container">
                <div class="row g-5 align-items-center">
                    <div class="col-lg-6 wow fadeIn" data-wow-delay="0.1s">
                        <div class="row g-3">
                            <div class="col-7"><div class="ht-card-img" style="aspect-ratio: 3/4; border-radius: 18px;">%(img35)s</div></div>
                            <div class="col-5">
                                <div class="ht-card-img" style="aspect-ratio: 3/4; border-radius: 18px;">%(img36)s</div>
                                <div class="ht-card-img mt-3" style="aspect-ratio: 1; border-radius: 18px;">%(img33)s</div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 wow fadeIn" data-wow-delay="0.2s">
                        <span class="ht-kicker">who we are</span>
                        <h2 class="ht-h2">We are <span>Ministers&rsquo; Kids</span></h2>
                        <p class="ht-lead mb-4">KIZAZI (&ldquo;generation&rdquo;) Phenomenal is a Christian youth
                        fellowship serving %(countries)s. %(family_html)s</p>
                        <p class="text-muted">We gather online every Friday, meet in cells through the week,
                        and cross borders for conferences, campus tours and serve trips. Worship that moves,
                        the Word taught plainly, and a family that carries you &mdash; that&rsquo;s the rhythm.</p>
                        <p class="text-muted">It all stands on one commission: <em>&ldquo;Let no one despise you
                        for your youth, but set the example for the believers.&rdquo;</em> &middot; %(verse_ref)s</p>
                        <div class="d-flex flex-wrap gap-2 mt-2">
                            <a class="btn-kz" href="%(reg)s" target="_blank" rel="noopener">Register free</a>
                            <a class="btn-kz-soft" href="ministries.html">Explore ministries</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Story End -->
        <!-- Stats Start -->
        <section class="ht-section ht-section-mist py-5">
            <div class="container">
                <div class="row">
%(stats)s
                </div>
            </div>
        </section>
        <!-- Stats End -->
        <!-- Delve Deeper Start -->
        <section class="ht-section">
            <div class="container">
%(head)s
                <div class="row g-4 mt-2">
%(delve)s
                </div>
            </div>
        </section>
        <!-- Delve Deeper End -->
""" % {"img35": C.img(35, "KIZAZI 2026: on stage", cls="img-fluid", extra='style="width:100%;height:100%;object-fit:cover;border-radius:18px"'),
       "img36": C.img(36, "KIZAZI 2026: two friends", cls="img-fluid", extra='style="width:100%;height:100%;object-fit:cover;border-radius:18px"'),
       "img33": C.img(33, "KIZAZI 2026: praise", cls="img-fluid", extra='style="width:100%;height:100%;object-fit:cover;border-radius:18px"'),
       "countries": C.SITE["countries"], "family_html": C.FAMILY_DESC_HTML,
       "verse_ref": C.SITE["verse_ref"], "reg": C.REG_URL,
       "stats": stat_html,
       "head": C.section_head("delve deeper", "More of <span>KIZAZI</span>",
                              "Explore our mission, meet the people who serve, and see the ways we live out faith together."),
       "delve": delve_html}
    body += verse_band()
    return page("About: KIZAZI Phenomenal",
                "Who we are: a Christian youth movement of Ministers' Kids across Kenya, Uganda, Tanzania and Rwanda.",
                "about", body)


# --------------------------------------------------------------- ministries --
MINISTRY_PHOTO = {
    "worship-word": 17, "cells": 20, "prayer": 19, "friday": 5,
    "outreach": 22, "creative": 21, "mentorship": 24, "care": 23,
}


def build_ministries():
    cards = []
    for n, (slug, icon, name, tag, desc, bullets) in enumerate(C.MINISTRIES):
        cards.append(card_start(MINISTRY_PHOTO[slug], tag, name, "0.%ds" % (n % 3 + 1)))
        cards.append("""                            <h3 id="%s"><i class="fas %s me-2" style="color: var(--kz-purple);"></i>%s</h3>
                            <p>%s</p>
                            <ul class="mb-0 ps-3" style="color: var(--kz-muted); font-size: .9rem;">
%s
                            </ul>
""" % (slug, icon, name, desc,
       "\n".join("                                <li>%s</li>" % b for b in bullets)))
        cards.append(card_end())
    body = C.page_header(
        "Ministries", "Every ministry offers a way to get involved, grow and serve.", 3)
    body += """        <!-- Ministries Start -->
        <section class="ht-section">
            <div class="container">
%(head)s
                <div class="row g-4 mt-2">
%(cards)s
                </div>
            </div>
        </section>
        <!-- Ministries End -->
""" % {"head": C.section_head("ministries for everyone", "Eight ways <span>in</span>",
                              "Click into what fits you. Every crew welcomes first-timers &mdash; come as you are."),
       "cards": "".join(cards)}
    body += team_band()
    return page("Ministries: KIZAZI Phenomenal",
                "Worship & The Word, Discipleship Cells, Prayer & Intercession, Friday Catch-Up, Outreach & Missions, Creative & Media Lab, Mentorship & Career, Community & Care.",
                "ministries", body)


# ----------------------------------------------------------------- programs --
ROOTED_PHASES = [
    ("Weeks 1&ndash;3", "Foundations", "Who God is, who you are in Him, and how to hear His voice &mdash; the basics that don&rsquo;t get skipped."),
    ("Weeks 4&ndash;7", "Rhythms", "Prayer, the Word and fellowship as daily habits, not emergency tools."),
    ("Weeks 8&ndash;10", "Purpose", "Gifts, calling and campus life: setting the example where you actually live."),
    ("Weeks 11&ndash;12", "Sent", "Commissioning: every graduate joins a cell, a crew or a campus team."),
]


def build_programs():
    acc = ""
    for n, (when_, name, desc) in enumerate(ROOTED_PHASES):
        acc += """                        <div class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button%s" type="button" data-bs-toggle="collapse" data-bs-target="#rooted%d">%s &mdash; %s</button>
                            </h2>
                            <div id="rooted%d" class="accordion-collapse collapse%s" data-bs-parent="#rootedAcc">
                                <div class="accordion-body text-muted">%s</div>
                            </div>
                        </div>
""" % (" collapsed" if n else "", n, when_, name, n, " show" if not n else "", desc)
    body = C.page_header(
        "Programs", "Journeys, circles and labs that help you grow, connect and go.", 13)
    body += """        <!-- Programs Start -->
        <section class="ht-section">
            <div class="container">
%(head)s
%(grid)s
            </div>
        </section>
        <!-- Programs End -->
        <!-- Rooted phases Start -->
        <section class="ht-section ht-section-mist">
            <div class="container">
                <div class="row g-5 align-items-start">
                    <div class="col-lg-5 wow fadeIn" data-wow-delay="0.1s">
                        <span class="ht-kicker">rooted &middot; 12 weeks</span>
                        <h2 class="ht-h2">How <span>Rooted</span> runs</h2>
                        <p class="ht-lead">A 12-week discipleship journey in four phases. New intake each term,
                        30 seats, three sessions a week &mdash; online and in person. Open the phases to see the shape.</p>
                        <a class="btn-kz" href="%(reg)s" target="_blank" rel="noopener">Apply for the next intake</a>
                    </div>
                    <div class="col-lg-7 ht-acc wow fadeIn" data-wow-delay="0.2s">
                        <div class="accordion" id="rootedAcc">
%(acc)s
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Rooted phases End -->
""" % {"head": C.section_head("grow in your faith", "Pick your <span>journey</span>",
                              "Every program is free or pay-what-you-can &mdash; nobody is turned away for money."),
       "grid": programs_section(False), "reg": C.REG_URL, "acc": acc}
    return page("Programs: KIZAZI Phenomenal",
                "Rooted discipleship, Phenomenal Fridays, the Creative Lab, Mentorship Circles, Campus Ambassadors and Serve East Africa.",
                "programs", body)


# ------------------------------------------------------------------- events --
def build_events():
    rows = []
    for n, ev in enumerate(C.EVENTS):
        rows.append("""                <div%s>
                    <div class="ht-event">
                        <div class="row g-0">
                            <div class="col-md-5">
                                <div class="ht-event-img h-100" %s role="img" aria-label="%s photo">
                                    <div class="ht-event-date"><span>%s</span></div>
                                </div>
                            </div>
                            <div class="col-md-7">
                                <div class="ht-event-body">
                                    <span class="ht-chip"><i class="fas fa-tag"></i>%s</span>
                                    <h3>%s</h3>
                                    <p>%s</p>
                                    <div class="ht-card-meta">
                                        <span><i class="far fa-calendar-alt me-1"></i>%s</span>
                                        <span><i class="far fa-clock me-1"></i>%s</span>
                                        <span><i class="fas fa-map-marker-alt me-1"></i>%s</span>
                                    </div>
                                    <a class="btn-kz mt-3" href="%s" target="_blank" rel="noopener">%s</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
""" % (wow("0.%ds" % (n + 1)), C.bg(ev["photo"]), ev["title"],
       ev["when"][:3].upper() if ev.get("when") != "friday" else "THIS",
       ev["tag"], ev["title"], ev["desc"], ev["when"], ev["time"], ev["place"],
       ev["cta_url"], ev["cta_label"]))
    body = C.page_header(
        "Events", "What&rsquo;s happening: catch-ups, conferences, nights and tours.", 15)
    body += """        <!-- Events Start -->
        <section class="ht-section">
            <div class="container">
                <div class="row g-4">
%(rows)s
                </div>
            </div>
        </section>
        <!-- Events End -->
""" % {"rows": "".join(rows)}
    body += follow_band()
    return page("Events: KIZAZI Phenomenal",
                "Phenomenal Fridays, KIZAZI Conference 2027, Worship & Word Nights and the Campus & School Tour.",
                "events", body)


# ------------------------------------------------------------------ gallery --
def build_gallery():
    filters = ['<button class="kz-filter-btn active" data-filter="all">All</button>']
    for key, label in C.GALLERY_CATS:
        filters.append('<button class="kz-filter-btn" data-filter="%s">%s</button>' % (key, label))
    items = []
    for i in range(42):
        key, label = C.gallery_cat(i)
        items.append("""                    <div class="col-6 col-md-4 col-lg-3 kz-gallery-item" data-cat="%s">
                        <a href="%s" data-lightbox="kizazi2026" data-title="KIZAZI 2026 &middot; %s">%s</a>
                    </div>
""" % (key, C.durl(i), label, C.img(i, "KIZAZI 2026 photo &middot; %s" % label, cls="img-fluid")))
    album_btn = ""
    if C.DRIVE_ALBUM_URL:
        album_btn = '<a class="btn-kz-soft ms-2" href="%s" target="_blank" rel="noopener">Open the Drive album</a>' % C.DRIVE_ALBUM_URL
    body = C.page_header(
        "Gallery", "KIZAZI 2026 &middot; 14&ndash;15 August &middot; two days, one family.", 1)
    body += """        <!-- Gallery Start -->
        <section class="ht-section">
            <div class="container">
                <div class="ht-center mb-4">
                    <div class="d-flex justify-content-center flex-wrap">%(filters)s</div>
                    %(album)s
                </div>
                <div class="row g-3">
%(items)s
                </div>
            </div>
        </section>
        <!-- Gallery End -->
""" % {"filters": "".join(filters), "album": album_btn, "items": "".join(items)}
    return page("Gallery: KIZAZI 2026 | KIZAZI Phenomenal",
                "Photos from KIZAZI 2026, 14-15 August: worship, word, community, service, creative and behind the scenes.",
                "gallery", body, with_video_modal=False)


# --------------------------------------------------------------------- blog --
def build_blog():
    cards = []
    for n, (title, date, team, initials, photo, tag, paras) in enumerate(C.BLOG):
        cards.append(card_start(photo, tag, title, "0.%ds" % (n + 1)))
        cards.append("""                            <div class="ht-card-meta" style="padding-top:0; margin-top:0; margin-bottom:.6rem;">
                                <span><i class="far fa-calendar-alt me-1"></i>%s</span>
                                <span><i class="far fa-user me-1"></i>%s</span>
                            </div>
                            <h3>%s</h3>
                            <p>%s&hellip;</p>
                            <a class="ht-card-link" href="blog.html#post%d">Read the note <i class="fa fa-arrow-right ms-1"></i></a>
""" % (date, team, title, paras[0][:220], n + 1))
        cards.append(card_end())
    full = []
    for n, (title, date, team, initials, photo, tag, paras) in enumerate(C.BLOG):
        full.append("""                <div class="ht-section %s" id="post%d" style="padding: 3.5rem 0;">
                    <div class="row g-5 align-items-start">
                        <div class="col-lg-5">
                            <div class="ht-card-img" style="aspect-ratio: 4/3; border-radius: 18px;">%s</div>
                        </div>
                        <div class="col-lg-7">
                            <span class="ht-kicker">%s &middot; %s</span>
                            <h2 class="ht-h2" style="font-size: 1.7rem;">%s</h2>
%s
                            <p class="small text-muted mb-0"><i class="far fa-user me-2"></i>%s</p>
                        </div>
                    </div>
                </div>
""" % ("ht-section-mist" if n % 2 else "", n + 1,
       C.img(photo, title, cls="img-fluid", extra='style="width:100%;height:100%;object-fit:cover;border-radius:18px"'),
       tag, date, title,
       "\n".join('                            <p class="text-muted">%s</p>' % p for p in paras),
       team))
    body = C.page_header(
        "Blog", "Notes from the movement: devotionals, recaps and practical habits.", 16)
    body += """        <!-- Blog cards Start -->
        <section class="ht-section">
            <div class="container">
                <div class="row g-4">
%(cards)s
                </div>
            </div>
        </section>
        <!-- Blog cards End -->
        <!-- Blog full Start -->
%(full)s
        <!-- Blog full End -->
""" % {"cards": "".join(cards), "full": "".join(full)}
    return page("Blog: KIZAZI Phenomenal",
                "Devotionals, conference recaps and practical discipleship notes from the KIZAZI teams.",
                "blog", body)


# --------------------------------------------------------------------- team --
def build_team():
    patron = C.patron()
    patron_html = ""
    if patron:
        patron_html = """        <!-- Patron Start -->
        <section class="ht-section pt-5 pb-0">
            <div class="container">
                <div class="ht-join wow fadeIn" data-wow-delay="0.1s">
                    <div class="row g-0 align-items-center">
                        <div class="col-md-4"><img src="%s" class="img-fluid w-100" style="object-fit: cover; min-height: 280px; max-height: 340px;" alt="%s"></div>
                        <div class="col-md-8">
                            <div class="ht-join-body">
                                <span class="ht-kicker">%s</span>
                                <h3>%s</h3>
                                <p class="text-muted mb-0">%s</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Patron End -->
""" % (patron["photo"], patron["name"], patron["role"], patron["line"] or "Carries this movement in prayer.")
    people_html = ""
    folks = C.people()
    if folks:
        cards = []
        for n, p in enumerate(folks):
            cards.append("""                <div%s>
                    <div class="ht-card">
                        <div class="ht-card-img ht-team-img"><img src="%s" class="img-fluid" alt="%s"></div>
                        <div class="ht-card-body">
                            <h3>%s</h3>
                            <p class="ht-kicker mb-2" style="letter-spacing:.2em;">%s</p>
                            <p>%s</p>
                        </div>
                    </div>
                </div>
""" % (wow("0.%ds" % (n + 1)), p["photo"], p["name"], p["name"], p["role"], p.get("line", "")))
        people_html = """        <section class="ht-section pt-4">
            <div class="container">
                <div class="row g-4">%s</div>
            </div>
        </section>
""" % "".join(cards)
    team_cards = []
    for n, (initials, name, desc, ministry, photo) in enumerate(C.TEAMS):
        team_cards.append(card_start(photo, ministry, name, "0.%ds" % (n % 3 + 1)))
        team_cards.append("""                            <div class="d-flex align-items-center gap-3 mb-3">
                                <span class="ht-initials">%s</span>
                                <h3 class="mb-0">%s</h3>
                            </div>
                            <p>%s</p>
                            <a class="ht-card-link" href="%s" target="_blank" rel="noopener">Join this crew <i class="fa fa-arrow-right ms-1"></i></a>
""" % (initials, name, desc, C.REG_URL))
        team_cards.append(card_end())
    body = C.page_header(
        "Team", "The serving crews &mdash; and the patron &mdash; who carry this movement.", 12)
    body += patron_html + people_html + """        <!-- Serving teams Start -->
        <section class="ht-section%(pad)s">
            <div class="container">
%(head)s
                <div class="row g-4 mt-2">
%(cards)s
                </div>
            </div>
        </section>
        <!-- Serving teams End -->
""" % {"pad": " pt-4" if (patron_html or people_html) else "",
       "head": C.section_head("join the team", "Serving <span>crews</span>",
                              "Roles, not titles. Every crew trains together and welcomes new hands each term."),
       "cards": "".join(team_cards)}
    body += team_band()
    return page("Team: KIZAZI Phenomenal",
                "Meet the serving teams of KIZAZI Phenomenal: worship & sound, word & teaching, prayer watch, mentors, media crew, outreach, hospitality and career crew.",
                "team", body)


# -------------------------------------------------------------- testimonial --
def build_testimonial():
    items = []
    for initials, label, quote in C.TESTIMONIALS:
        items.append("""                    <div class="item">
                        <div class="ht-quote">
                            <i class="fas fa-quote-left d-block"></i>
                            <p>%s</p>
                            <div class="d-flex align-items-center gap-3 mt-4">
                                <span class="ht-initials">%s</span>
                                <div><b class="d-block">%s</b><span class="small text-muted">Testimony &middot; illustrative until confirmed</span></div>
                            </div>
                        </div>
                    </div>
""" % (quote, initials, label))
    body = C.page_header(
        "Testimonial", "What the generation says when the mic is off.", 20)
    body += """        <!-- Testimonials Start -->
        <section class="ht-section">
            <div class="container">
                <div class="row g-4 align-items-center">
                    <div class="col-lg-5 wow fadeIn" data-wow-delay="0.1s">
                        <div class="ht-card-img" style="aspect-ratio: 4/5; border-radius: 18px;">%(photo)s</div>
                    </div>
                    <div class="col-lg-7">
                        <div class="testimonial-carousel owl-carousel">
%(items)s
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Testimonials End -->
""" % {"photo": C.img(37, "Listening in, KIZAZI 2026", cls="img-fluid",
                      extra='style="width:100%;height:100%;object-fit:cover;border-radius:18px"'),
       "items": "".join(items)}
    body += verse_band()
    return page("Testimonial: KIZAZI Phenomenal",
                "Testimonies from the KIZAZI family: joined online, campus ambassadors, Rooted graduates and first-year students.",
                "testimonial", body)


# ------------------------------------------------------------------ contact --
def build_contact():
    cards = [
        (C.REG_URL, "fa-pen-to-square", "Register free",
         "Two minutes, no fee. The form is the front door to cells, Fridays and every program.",
         "Open the form"),
        (C.MEET_URL, "fa-video", "Friday Catch-Up",
         "Join live every Friday at 8:00 PM EAT on Google Meet &mdash; next one: <span data-next-friday-long>&hellip;</span>",
         "Open Google Meet"),
        (C.INSTAGRAM_URL, "fa-paper-plane", "Slide into the DMs",
         "Questions, prayer requests, campus invites: Instagram, TikTok or Facebook &mdash; a human replies.",
         "Message us"),
    ]
    out = []
    for n, (url, icon, name, desc, cta) in enumerate(cards):
        out.append("""                <div%s>
                    <div class="ht-card">
                        <div class="ht-card-body text-center">
                            <span class="ht-initials mx-auto mb-3" style="width: 64px; height: 64px;"><i class="fas %s"></i></span>
                            <h3>%s</h3>
                            <p>%s</p>
                            <a class="btn-kz" href="%s" target="_blank" rel="noopener">%s</a>
                        </div>
                    </div>
                </div>
""" % (wow("0.%ds" % (n + 1)), icon, name, desc, url, cta))
    body = C.page_header(
        "Contact", "No call centres &mdash; just a family that answers.", 9)
    body += """        <!-- Contact Start -->
        <section class="ht-section">
            <div class="container">
                <div class="row g-4">
%(cards)s
                </div>
                <div class="ht-join mt-5 wow fadeIn" data-wow-delay="0.2s">
                    <div class="row g-0 align-items-center">
                        <div class="col-md-5"><div class="ht-join-photo h-100" %(bg)s role="img" aria-label="KIZAZI 2026 welcome desk"></div></div>
                        <div class="col-md-7">
                            <div class="ht-join-body">
                                <span class="ht-kicker">everywhere we are</span>
                                <h3>One link for everything</h3>
                                <p class="text-muted">%(linktree)s &mdash; socials, form, Meet and the gallery in a single tap.
                                Follow %(social_names)s as <strong>@kizazi</strong> and you&rsquo;ll never miss a Friday.</p>
                                <div class="ht-fsocial" style="margin-top: .5rem;">
                                    <a href="%(fb)s" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                                    <a href="%(tt)s" target="_blank" rel="noopener" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
                                    <a href="%(ig)s" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Contact End -->
""" % {"cards": "".join(out), "bg": C.bg(8), "linktree": C.LINKTREE_NOTE,
       "social_names": "TikTok, Instagram and Facebook",
       "fb": C.FACEBOOK_URL, "tt": C.TIKTOK_URL, "ig": C.INSTAGRAM_URL}
    return page("Contact: KIZAZI Phenomenal",
                "Reach KIZAZI Phenomenal: register free, join the Friday Google Meet, or message us on TikTok, Instagram and Facebook.",
                "contact", body)


# ---------------------------------------------------------------------- 404 --
def build_404():
    body = C.page_header("Page not found", "Even the best generation hits a dead link sometimes.", 27)
    body += """        <!-- 404 Start -->
        <section class="ht-section ht-center">
            <div class="container ht-404">
                <b>404</b>
                <h2 class="ht-h2">This page went to <span>prayer</span></h2>
                <p class="ht-lead mx-auto">The link may have moved, or the page was never here.
                Head home, or catch us live this Friday at 8:00 PM EAT.</p>
                <div class="d-flex justify-content-center gap-2 mt-4">
                    <a class="btn-kz" href="index.html">Back home</a>
                    <a class="btn-kz-soft" href="%(meet)s" target="_blank" rel="noopener">Join this Friday</a>
                </div>
            </div>
        </section>
        <!-- 404 End -->
""" % {"meet": C.MEET_URL}
    return page("404: KIZAZI Phenomenal", "Page not found. Head back home or join us this Friday.",
                "", body, with_video_modal=False)


PAGES_OUT = [
    ("index.html", build_index),
    ("about.html", build_about),
    ("ministries.html", build_ministries),
    ("programs.html", build_programs),
    ("events.html", build_events),
    ("gallery.html", build_gallery),
    ("blog.html", build_blog),
    ("team.html", build_team),
    ("testimonial.html", build_testimonial),
    ("contact.html", build_contact),
    ("404.html", build_404),
]


def main():
    for name, builder in PAGES_OUT:
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
            fh.write(builder())
        print("wrote %s" % name)


if __name__ == "__main__":
    main()
