#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KIZAZI Phenomenal — page builder (BabyCare-template edition).

Composes the 11 pages from the BabyCare template's own markup structure
(hero-header / about+video / service / program / events / blog / team /
testimonial carousel / 4-column footer) with KIZAZI content and the hotlinked
"KIZAZI 2026" Drive photos.

Usage:  python3 tools/build.py
"""

import os

from build_common import (
    ABOUT_PHOTO, BLOG, DRIVE_ALBUM_URL, EVENTS, FOOTER_PHOTO, GALLERY_CATS,
    HERO_PHOTO, INSTAGRAM_URL, LINKTREE_NOTE, MEET_URL, MINISTRIES, PAGES,
    PHOTOS, PROGRAMS, REG_URL, SITE, TEAMS, TESTIMONIALS, TIKTOK_URL,
    FACEBOOK_URL, back_to_top, bg, body_open, durl, footer, head, img,
    page_header, scripts, section_head, social_buttons, spinner, topbar_navbar,
    video_embed, video_modal, videos,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WOW = ('class="wow fadeIn" data-wow-delay="%s"',)


def wow(delay="0.1s"):
    return 'class="wow fadeIn" data-wow-delay="%s"' % delay


def album_button(cls="btn btn-secondary px-4 py-2 text-white btn-border-radius"):
    if not DRIVE_ALBUM_URL:
        return ""
    return ('<a class="%s" href="%s" target="_blank" rel="noopener">'
            '<i class="fab fa-google-drive me-2"></i>Open the Drive album</a>'
            % (cls, DRIVE_ALBUM_URL))


# --------------------------------------------------------------- components ---
def service_card(m, delay, detail=False, anchor=True):
    slug, icon, name, blurb, long_, bullets = m
    text = long_ if detail else blurb
    anchor_attr = ' id="%s"' % slug if anchor else ''
    return """                    <div class="col-md-6 col-lg-6 col-xl-3 wow fadeIn" data-wow-delay="%(delay)s">
                        <div class="text-center border-primary border bg-white service-item"%(anchor)s>
                            <div class="service-content d-flex align-items-center justify-content-center p-4">
                                <div class="service-content-inner">
                                    <div class="p-4"><i class="fas %(icon)s fa-6x text-primary"></i></div>
                                    <a href="ministries.html#%(slug)s" class="h4">%(name)s</a>
                                    <p class="my-3">%(text)s</p>
                                    <a href="ministries.html#%(slug)s" class="btn btn-primary text-white px-4 py-2 my-2 btn-border-radius">Read More</a>
                                </div>
                            </div>
                        </div>
                    </div>
""" % dict(delay=delay, slug=slug, icon=icon, name=name, text=text, anchor=anchor_attr)


def program_card(p, delay):
    name, rate, photo_i, desc, leader, initials, when, where, meta = p
    slug = name.lower().replace(" ", "-").replace("&", "and")
    return """                    <div class="col-md-6 col-lg-6 col-xl-4 wow fadeIn" data-wow-delay="%(delay)s" id="%(slug)s">
                        <div class="program-item rounded">
                            <div class="program-img position-relative">
                                <div class="overflow-hidden img-border-radius">
                                    %(img)s
                                </div>
                                <div class="px-4 py-2 bg-primary text-white program-rate">%(rate)s</div>
                            </div>
                            <div class="program-text bg-white px-4 pb-3">
                                <div class="program-text-inner">
                                    <a href="programs.html#%(slug)s" class="h4">%(name)s</a>
                                    <p class="mt-3 mb-0">%(desc)s</p>
                                </div>
                            </div>
                            <div class="program-teacher d-flex align-items-center border-top border-primary bg-white px-4 py-3">
                                <div class="kz-initials rounded-circle border border-primary bg-white d-flex align-items-center justify-content-center" style="width: 70px; height: 70px;">%(initials)s</div>
                                <div class="ms-3">
                                    <h6 class="mb-0 text-primary">%(leader)s</h6>
                                    <small>%(when)s</small>
                                </div>
                            </div>
                            <div class="d-flex justify-content-between px-4 py-2 bg-primary rounded-bottom">
                                <small class="text-white"><i class="fas fa-users me-1"></i> %(m0)s</small>
                                <small class="text-white"><i class="fas fa-book me-1"></i> %(m1)s</small>
                                <small class="text-white"><i class="fas fa-clock me-1"></i> %(m2)s</small>
                            </div>
                        </div>
                    </div>
""" % dict(delay=delay, rate=rate, name=name, desc=desc, leader=leader,
           initials=initials, when=when, slug=name.lower().replace(" ", "-").replace("&", "and"),
           m0=meta[0], m1=meta[1], m2=meta[2],
           img=img(photo_i, name + " — KIZAZI 2026", cls="img-fluid w-100 kz-cover", w=900))


def event_card(ev, delay):
    if ev["when"] == "friday":
        badge = ('<div class="px-4 py-2 bg-secondary text-white text-center events-rate">'
                 '<span data-next-friday-day>&hellip;</span> <span data-next-friday-mon>&hellip;</span></div>')
        when_cell = ('<small class="text-white"><i class="fas fa-calendar me-1 text-primary"></i> '
                     '<span data-next-friday-long>&hellip;</span></small>')
    else:
        badge = ('<div class="px-4 py-2 bg-secondary text-white text-center events-rate">%s</div>'
                 % ev["when"])
        when_cell = ('<small class="text-white"><i class="fas fa-calendar me-1 text-primary"></i> %s</small>'
                     % ev["when"])
    return """                    <div class="col-md-6 col-lg-6 col-xl-3 wow fadeIn" data-wow-delay="%(delay)s">
                        <div class="events-item bg-primary rounded">
                            <div class="events-inner position-relative">
                                <div class="events-img overflow-hidden rounded-circle position-relative">
                                    %(img)s
                                    <div class="event-overlay">
                                        <a href="%(full)s" data-lightbox="events"><i class="fas fa-search-plus text-white fa-2x"></i></a>
                                    </div>
                                </div>
                                %(badge)s
                                <div class="d-flex justify-content-between px-4 py-2 bg-secondary">
                                    %(when_cell)s
                                    <small class="text-white"><i class="fas fa-map-marker-alt me-1 text-primary"></i> %(place)s</small>
                                </div>
                            </div>
                            <div class="events-text p-4 border border-primary bg-white border-top-0 rounded-bottom">
                                <span class="badge bg-secondary mb-2">%(tag)s</span>
                                <a href="events.html" class="h4 d-block">%(title)s</a>
                                <p class="mb-3 mt-2">%(desc)s</p>
                                <a class="btn btn-primary btn-sm text-white px-4 py-2 btn-border-radius" href="%(cta_url)s" target="_blank" rel="noopener"><i class="fas fa-bolt me-1"></i> %(cta_label)s</a>
                            </div>
                        </div>
                    </div>
""" % dict(delay=delay, badge=badge, when_cell=when_cell, title=ev["title"],
           desc=ev["desc"], place=ev["place"], tag=ev["tag"],
           cta_url=ev["cta_url"], cta_label=ev["cta_label"], full=durl(ev["photo"]),
           img=img(ev["photo"], ev["title"], cls="img-fluid w-100 rounded-circle kz-cover", w=800))


def blog_card(post, delay, read_link):
    title, date, team, initials, photo_i, tag, paras = post
    slug = "post-%d" % (BLOG.index(post) + 1)
    excerpt = paras[0][:150].rsplit(" ", 1)[0] + "&hellip;"
    return """                    <div class="col-md-6 col-lg-6 col-xl-4 wow fadeIn" data-wow-delay="%(delay)s">
                        <div class="blog-item rounded-bottom">
                            <div class="blog-img overflow-hidden position-relative img-border-radius">
                                %(img)s
                            </div>
                            <div class="d-flex justify-content-between px-4 py-3 bg-light border-bottom border-primary blog-date-comments">
                                <small class="text-dark"><i class="fas fa-calendar me-1 text-dark"></i> %(date)s</small>
                                <small class="text-dark"><i class="fas fa-tag me-1 text-dark"></i> %(tag)s</small>
                            </div>
                            <div class="blog-content d-flex align-items-center px-4 py-3 bg-light">
                                <div class="kz-initials rounded-circle border border-primary bg-white d-flex align-items-center justify-content-center" style="width: 70px; height: 70px;">%(initials)s</div>
                                <div class="ms-3">
                                    <h6 class="text-primary">%(team)s</h6>
                                    <p class="text-muted mb-0">KIZAZI Phenomenal</p>
                                </div>
                            </div>
                            <div class="px-4 pb-4 bg-light rounded-bottom">
                                <div class="blog-text-inner">
                                    <a href="%(read)s" class="h4">%(title)s</a>
                                    <p class="mt-3 mb-4">%(excerpt)s</p>
                                </div>
                                <div class="text-center">
                                    <a href="%(read)s" class="btn btn-primary text-white px-4 py-2 mb-3 btn-border-radius">View Details</a>
                                </div>
                            </div>
                        </div>
                    </div>
""" % dict(delay=delay, date=date, tag=tag, team=team, initials=initials,
           title=title, excerpt=excerpt, read=read_link % slug,
           img=img(photo_i, title, cls="img-fluid w-100 kz-cover", w=900))


def team_card(t, delay):
    initials, name, desc, ministry, photo_i = t
    return """                    <div class="col-md-6 col-lg-4 col-xl-3 wow fadeIn" data-wow-delay="%(delay)s">
                        <div class="team-item border border-primary img-border-radius overflow-hidden">
                            %(img)s
                            <div class="team-icon d-flex align-items-center justify-content-center">
                                <a class="share btn btn-primary btn-md-square text-white rounded-circle me-3" href="%(reg)s" target="_blank" rel="noopener" aria-label="Join this team"><i class="fas fa-share-alt"></i></a>
                                <a class="share-link btn btn-primary btn-md-square text-white rounded-circle me-3" href="%(fb)s" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                                <a class="share-link btn btn-primary btn-md-square text-white rounded-circle me-3" href="%(tt)s" target="_blank" rel="noopener" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
                                <a class="share-link btn btn-primary btn-md-square text-white rounded-circle" href="%(ig)s" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                            </div>
                            <div class="team-content text-center py-3">
                                <h4 class="text-primary">%(name)s</h4>
                                <p class="text-muted mb-2">%(desc)s</p>
                            </div>
                        </div>
                    </div>
""" % dict(delay=delay, name=name, desc=desc, reg=REG_URL, fb=FACEBOOK_URL,
           tt=TIKTOK_URL, ig=INSTAGRAM_URL,
           img=img(photo_i, name + " serving at KIZAZI 2026", cls="img-fluid w-100 kz-cover", w=700))


def testimonial_item(t):
    initials, label, quote = t
    return """                    <div class="testimonial-item img-border-radius bg-light border border-primary p-4">
                        <div class="p-4 position-relative">
                            <i class="fa fa-quote-right fa-2x text-primary position-absolute" style="top: 15px; right: 15px;"></i>
                            <div class="d-flex align-items-center">
                                <div class="border border-primary bg-white rounded-circle">
                                    <div class="kz-initials kz-initials-lg rounded-circle p-2 d-flex align-items-center justify-content-center" style="width: 80px; height: 80px;">%(initials)s</div>
                                </div>
                                <div class="ms-4">
                                    <h4 class="text-dark">%(initials)s</h4>
                                    <p class="m-0 pb-3">%(label)s</p>
                                    <div class="d-flex pe-5">
                                        <i class="fas fa-star text-primary"></i>
                                        <i class="fas fa-star text-primary"></i>
                                        <i class="fas fa-star text-primary"></i>
                                        <i class="fas fa-star text-primary"></i>
                                        <i class="fas fa-star text-primary"></i>
                                    </div>
                                </div>
                            </div>
                            <div class="border-top border-primary mt-4 pt-3">
                                <p class="mb-0">%(quote)s</p>
                            </div>
                        </div>
                    </div>
""" % dict(initials=initials, label=label, quote=quote)


def play_button():
    """Template play button: opens the Drive video modal, or links to TikTok."""
    vids = videos()
    if vids:
        return ('<button type="button" class="btn btn-play" data-bs-toggle="modal" '
                'data-src="%s" data-bs-target="#videoModal" aria-label="Play the KIZAZI highlight film">'
                '<span></span></button>' % vids[0]["embed"])
    return ('<a class="btn btn-play" href="%s" target="_blank" rel="noopener" '
            'title="Highlight film coming soon — watch clips on TikTok" '
            'aria-label="Watch KIZAZI clips on TikTok"><span></span></a>' % TIKTOK_URL)


def watch_section(delay_head="0.1s"):
    vids = videos()
    head_html = section_head("KIZAZI On Film", "Watch The Movement",
                             "Films from the family &mdash; worship, word and the rooms in between. "
                             "Every clip is hosted on our Drive album.")
    if not vids:
        body = """                <div class="row g-5 justify-content-center">
                    <div class="col-lg-8 wow fadeIn" data-wow-delay="0.2s">
                        <div class="video border kz-video-thumb kz-video-empty mx-auto" %(bg)s>
                            %(play)s
                        </div>
                        <div class="text-center mt-4">
                            <h4 class="text-primary mb-2">The highlight film is being cut</h4>
                            <p class="text-body mb-4">Until the KIZAZI 2026 film drops, catch the moments on our socials &mdash; and the full photo album in the gallery.</p>
                            <div class="d-flex flex-wrap justify-content-center gap-3">
                                <a class="btn btn-primary px-4 py-2 text-white btn-border-radius" href="%(tt)s" target="_blank" rel="noopener"><i class="fab fa-tiktok me-2"></i>TikTok clips</a>
                                <a class="btn btn-primary px-4 py-2 text-white btn-border-radius" href="%(ig)s" target="_blank" rel="noopener"><i class="fab fa-instagram me-2"></i>Instagram</a>
                                <a class="btn btn-primary px-4 py-2 text-white btn-border-radius" href="gallery.html">Photo gallery</a>
                                %(album)s
                            </div>
                        </div>
                    </div>
                </div>
""" % dict(bg=bg(10), play=play_button(), tt=TIKTOK_URL, ig=INSTAGRAM_URL, album=album_button())
    else:
        cards = []
        for n, v in enumerate(vids):
            cards.append("""                    <div class="col-md-6 col-lg-4 wow fadeIn" data-wow-delay="%(delay)s">
                        <div class="border border-primary bg-white rounded overflow-hidden h-100">
                            <div class="video kz-video-thumb" %(bg)s>
                                <button type="button" class="btn btn-play" data-bs-toggle="modal" data-src="%(embed)s" data-bs-target="#videoModal" aria-label="Play %(title)s"><span></span></button>
                            </div>
                            <div class="p-4">
                                <span class="badge bg-secondary mb-2">%(tag)s</span>
                                <h4 class="text-primary">%(title)s</h4>
                                <p class="text-body mb-0">%(desc)s</p>
                            </div>
                        </div>
                    </div>
""" % dict(delay=("0.%ds" % (1 + n * 2)), bg=bg(v["poster"]), embed=v["embed"],
           title=v["title"], desc=v["desc"], tag=v["tag"]))
        body = ('                <div class="row g-5 justify-content-center">\n%s\n                </div>\n'
                % "".join(cards))
        if album_button():
            body += ('                <div class="text-center mt-4">%s</div>\n' % album_button())
    return """        <!-- Watch Start -->
        <div class="container-fluid py-5 bg-light">
            <div class="container py-5">
%s%s            </div>
        </div>
        <!-- Watch End -->
""" % (head_html, body)


def testimonials_carousel():
    return """        <!-- Testimonial Start -->
        <div class="container-fluid testimonial py-5">
            <div class="container py-5">
%s                <div class="owl-carousel testimonial-carousel wow fadeIn" data-wow-delay="0.3s">
%s                </div>
            </div>
        </div>
        <!-- Testimonial End -->
""" % (section_head("Our Testimonials", "Voices From The Family"),
       "".join(testimonial_item(t) for t in TESTIMONIALS))


def page(title, desc, active, body, with_video_modal=True):
    parts = [head(title, desc), body_open(), spinner(), topbar_navbar(active)]
    if with_video_modal:
        parts.append(video_modal())
    parts.append(body)
    parts.append(footer())
    parts.append(back_to_top())
    parts.append(scripts())
    return "".join(parts)


# ------------------------------------------------------------------- pages ---
def build_index():
    body = """
        <!-- Hero Start -->
        <div class="container-fluid py-5 hero-header wow fadeIn" data-wow-delay="0.1s" %(bg)s>
            <div class="container py-5">
                <div class="row g-5">
                    <div class="col-lg-7 col-md-12">
                        <h1 class="mb-3 text-primary">A Generation On Fire For God</h1>
                        <h1 class="mb-4 display-1 text-white">KIZAZI Phenomenal</h1>
                        <p class="text-white mb-5" style="max-width: 560px;">Christian youth movement across %(countries)s &mdash;
                        worship that moves, discipleship that sticks, a family that carries you.
                        <strong class="text-white">This Friday:</strong> Online Catch-Up, 8:00 PM EAT
                        (<span data-next-friday-long>&hellip;</span>).</p>
                        <a href="%(reg)s" target="_blank" rel="noopener" class="btn btn-primary px-4 py-3 px-md-5 me-4 btn-border-radius">Register Free</a>
                        <a href="about.html" class="btn btn-secondary px-4 py-3 px-md-5 btn-border-radius">Our Story</a>
                    </div>
                </div>
            </div>
        </div>
        <!-- Hero End -->


        <!-- About Start -->
        <div class="container-fluid py-5 about bg-light">
            <div class="container py-5">
                <div class="row g-5 align-items-center">
                    <div class="col-lg-5 wow fadeIn" data-wow-delay="0.1s">
                        <div class="video border" %(about_bg)s>
                            %(play)s
                        </div>
                    </div>
                    <div class="col-lg-7 wow fadeIn" data-wow-delay="0.3s">
                        <h4 class="text-primary mb-4 border-bottom border-primary border-2 d-inline-block p-2 title-border-radius">About Us</h4>
                        <h1 class="text-dark mb-4 display-5">We Are The Generation That Sets The Example</h1>
                        <p class="text-dark mb-4">&ldquo;%(verse)s&rdquo; &mdash; %(verse_ref)s. KIZAZI Phenomenal is a family of students
                        and young workers across Kenya, Uganda, Tanzania and Rwanda, gathered every Friday
                        online and in cells through the week.</p>
                        <div class="row mb-4">
                            <div class="col-lg-6">
                                <h6 class="mb-3"><i class="fas fa-check-circle me-2"></i>Weekly Friday catch-up</h6>
                                <h6 class="mb-3"><i class="fas fa-check-circle me-2 text-primary"></i>Discipleship cells</h6>
                                <h6 class="mb-3"><i class="fas fa-check-circle me-2 text-secondary"></i>Campus &amp; school tours</h6>
                            </div>
                            <div class="col-lg-6">
                                <h6 class="mb-3"><i class="fas fa-check-circle me-2"></i>Creative &amp; media lab</h6>
                                <h6 class="mb-3"><i class="fas fa-check-circle me-2 text-primary"></i>Mentorship &amp; career</h6>
                                <h6><i class="fas fa-check-circle me-2 text-secondary"></i>Serve East Africa trips</h6>
                            </div>
                        </div>
                        <a href="about.html" class="btn btn-primary px-5 py-3 btn-border-radius">More Details</a>
                    </div>
                </div>
            </div>
        </div>
        <!-- About End -->


        <!-- Ministries / Service Start -->
        <div class="container-fluid service py-5">
            <div class="container py-5">
%(service_head)s                <div class="row g-5">
%(service_cards)s                </div>
            </div>
        </div>
        <!-- Ministries / Service End -->


        <!-- Programs Start -->
        <div class="container-fluid program py-5">
            <div class="container py-5">
%(program_head)s                <div class="row g-5 justify-content-center">
%(program_cards)s                    <div class="d-inline-block text-center wow fadeIn" data-wow-delay="0.1s">
                        <a href="programs.html" class="btn btn-primary px-5 py-3 text-white btn-border-radius">View All Programs</a>
                    </div>
                </div>
            </div>
        </div>
        <!-- Program End -->


        <!-- Events Start -->
        <div class="container-fluid events py-5 bg-light">
            <div class="container py-5">
%(events_head)s                <div class="row g-5 justify-content-center">
%(event_cards)s                </div>
            </div>
        </div>
        <!-- Events End-->


%(watch)s

        <!-- Blog Start-->
        <div class="container-fluid blog py-5">
            <div class="container py-5">
%(blog_head)s                <div class="row g-5 justify-content-center">
%(blog_cards)s                </div>
            </div>
        </div>
        <!-- Blog End-->


        <!-- Team Start-->
        <div class="container-fluid team py-5 bg-light">
            <div class="container py-5">
%(team_head)s                <div class="row g-5 justify-content-center">
%(team_cards)s                    <div class="d-inline-block text-center wow fadeIn" data-wow-delay="0.1s">
                        <a href="team.html" class="btn btn-primary px-5 py-3 text-white btn-border-radius">Meet The Whole Family</a>
                    </div>
                </div>
            </div>
        </div>
        <!-- Team End-->


%(testimonials)s
""" % dict(
        bg=bg(HERO_PHOTO), about_bg=bg(ABOUT_PHOTO), play=play_button(),
        countries=SITE["countries"], verse=SITE["verse"], verse_ref=SITE["verse_ref"],
        reg=REG_URL,
        service_head=section_head("What We Do", "Eight Doorways Into The Family"),
        service_cards="".join(service_card(m, "0.%ds" % (1 + (n % 4) * 2)) for n, m in enumerate(MINISTRIES)),
        program_head=section_head("Our Programs", "Programs That Build A Generation"),
        program_cards="".join(program_card(p, "0.%ds" % (1 + (n % 3) * 2)) for n, p in enumerate(PROGRAMS[:3])),
        events_head=section_head("Our Events", "Where We Meet Next"),
        event_cards="".join(event_card(e, "0.%ds" % (1 + (n % 4) * 2)) for n, e in enumerate(EVENTS)),
        watch=watch_section(),
        blog_head=section_head("Word &amp; Stories", "Read Our Latest"),
        blog_cards="".join(blog_card(b, "0.%ds" % (1 + n * 2), "blog.html#%s") for n, b in enumerate(BLOG)),
        team_head=section_head("Serving Teams", "The Crew Behind The Fire"),
        team_cards="".join(team_card(t, "0.%ds" % (1 + n * 2)) for n, t in enumerate(TEAMS[:4])),
        testimonials=testimonials_carousel(),
    )
    return page("KIZAZI Phenomenal — A Generation on Fire for God",
                "KIZAZI Phenomenal is a Christian youth ministry serving Kenya, Uganda, "
                "Tanzania and Rwanda. Phenomenal Fridays, 8:00 PM EAT. Register free.",
                "home", body)


def build_about():
    stats = [("4", "Nations served"), ("500+", "Young people reached"),
             ("8", "Ministries"), ("52", "Fridays a year")]
    stat_html = "".join(
        """                    <div class="col-6 col-lg-3 wow fadeIn" data-wow-delay="0.%ds">
                        <div class="text-center border border-primary bg-white p-4 rounded h-100">
                            <h1 class="display-4 text-primary mb-0">%s</h1>
                            <p class="text-body mb-0">%s</p>
                        </div>
                    </div>
""" % (1 + n * 2, v, l_) for n, (v, l_) in enumerate(stats))
    values = [
        ("fa-fire", "On fire", "Worship and prayer first &mdash; everything else is overflow."),
        ("fa-book-open", "In the Word", "Scripture taught plainly, questioned honestly, lived loudly."),
        ("fa-hands-holding-child", "In family", "Nobody walks exams, home or grief alone."),
        ("fa-globe-africa", "On mission", "Campuses, schools and borders &mdash; the gospel goes."),
    ]
    value_html = "".join(
        """                    <div class="col-md-6 col-xl-3 wow fadeIn" data-wow-delay="0.%ds">
                        <div class="text-center border-primary border bg-white service-item h-100">
                            <div class="service-content d-flex align-items-center justify-content-center p-4">
                                <div class="service-content-inner">
                                    <div class="p-4"><i class="fas %s fa-6x text-primary"></i></div>
                                    <a href="#" class="h4">%s</a>
                                    <p class="my-3">%s</p>
                                </div>
                            </div>
                        </div>
                    </div>
""" % (1 + n * 2, icon, name, desc) for n, (icon, name, desc) in enumerate(values))
    body = """
%(header)s

        <!-- About Start -->
        <div class="container-fluid py-5 about bg-light">
            <div class="container py-5">
                <div class="row g-5 align-items-center">
                    <div class="col-lg-5 wow fadeIn" data-wow-delay="0.1s">
                        <div class="video border" %(about_bg)s>
                            %(play)s
                        </div>
                    </div>
                    <div class="col-lg-7 wow fadeIn" data-wow-delay="0.3s">
                        <h4 class="text-primary mb-4 border-bottom border-primary border-2 d-inline-block p-2 title-border-radius">About Us</h4>
                        <h1 class="text-dark mb-4 display-5">KIZAZI Means &ldquo;Generation&rdquo; &mdash; And That Is Exactly Who We Are</h1>
                        <p class="text-dark mb-4">KIZAZI Phenomenal began the way most moves of God do: a few students who refused
                        to wait for &ldquo;after graduation&rdquo; to live for God. Today the family gathers every Friday at 8:00 PM EAT
                        on Google Meet &mdash; Kenya, Uganda, Tanzania and Rwanda in one room &mdash; and in discipleship cells,
                        campus fellowships and Serve East Africa trips through the week.</p>
                        <p class="text-dark mb-4">We are not a building and we are not a brand. We are a generation learning to set
                        the example &mdash; in speech, in conduct, in love, in faith, in purity.</p>
                        <div class="row mb-4">
                            <div class="col-lg-6">
                                <h6 class="mb-3"><i class="fas fa-check-circle me-2 text-primary"></i>Online every Friday</h6>
                                <h6 class="mb-3"><i class="fas fa-check-circle me-2 text-secondary"></i>Cells in person weekly</h6>
                                <h6 class="mb-3"><i class="fas fa-check-circle me-2"></i>Free to join, always</h6>
                            </div>
                            <div class="col-lg-6">
                                <h6 class="mb-3"><i class="fas fa-check-circle me-2"></i>Student-led, mentor-backed</h6>
                                <h6 class="mb-3"><i class="fas fa-check-circle me-2 text-primary"></i>Creative-first culture</h6>
                                <h6><i class="fas fa-check-circle me-2 text-secondary"></i>Four nations, one family</h6>
                            </div>
                        </div>
                        <a href="%(reg)s" target="_blank" rel="noopener" class="btn btn-primary px-5 py-3 btn-border-radius">Join The Family</a>
                    </div>
                </div>
            </div>
        </div>
        <!-- About End -->


        <!-- Stats Start -->
        <div class="container-fluid py-5">
            <div class="container py-5">
                <div class="row g-4">
%(stats)s                </div>
            </div>
        </div>
        <!-- Stats End -->


        <!-- Values Start -->
        <div class="container-fluid service py-5">
            <div class="container py-5">
%(values_head)s                <div class="row g-5">
%(values)s                </div>
            </div>
        </div>
        <!-- Values End -->


        <!-- Verse Start -->
        <div class="container-fluid py-5 bg-light">
            <div class="container py-5">
                <div class="row justify-content-center">
                    <div class="col-lg-9 text-center wow fadeIn" data-wow-delay="0.2s">
                        <i class="fas fa-cross fa-2x text-secondary mb-4"></i>
                        <h1 class="display-5 text-dark fst-italic">&ldquo;%(verse)s&rdquo;</h1>
                        <h4 class="text-primary mt-4 mb-0">&mdash; %(verse_ref)s</h4>
                    </div>
                </div>
            </div>
        </div>
        <!-- Verse End -->


        <!-- CTA Start -->
        <div class="container-fluid py-5">
            <div class="container py-5">
                <div class="p-5 bg-light rounded text-center wow fadeIn" data-wow-delay="0.2s">
                    <h1 class="display-4 mb-4">Come As You Are</h1>
                    <p class="text-body mb-4">Register free, get the Friday link, and let a cell near you adopt you this term.</p>
                    <a href="%(reg)s" target="_blank" rel="noopener" class="btn btn-primary px-5 py-3 me-3 text-white btn-border-radius">Register Free</a>
                    <a href="%(meet)s" target="_blank" rel="noopener" class="btn btn-secondary px-5 py-3 text-white btn-border-radius">Join This Friday</a>
                </div>
            </div>
        </div>
        <!-- CTA End -->
""" % dict(header=page_header("About Us", "One generation, four nations, on fire for God.", 25),
           about_bg=bg(ABOUT_PHOTO), play=play_button(), reg=REG_URL, meet=MEET_URL,
           stats=stat_html,
           values_head=section_head("Mission &middot; Vision &middot; Values", "What We Hold Onto"),
           values=value_html, verse=SITE["verse"], verse_ref=SITE["verse_ref"])
    return page("About Us — KIZAZI Phenomenal",
                "The story, mission and values of KIZAZI Phenomenal, a Christian youth "
                "movement across Kenya, Uganda, Tanzania and Rwanda.",
                "about", body)


def build_ministries():
    cards = "".join(service_card(m, "0.%ds" % (1 + (n % 4) * 2), detail=True, anchor=False)
                    for n, m in enumerate(MINISTRIES))
    acc = []
    for slug, icon, name, blurb, long_, bullets in MINISTRIES:
        acc.append("""                            <div class="accordion-item" id="%(slug)s">
                                <h2 class="accordion-header">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#acc-%(slug)s" aria-expanded="false" aria-controls="acc-%(slug)s">
                                        <i class="fas %(icon)s me-3 text-primary"></i>%(name)s &mdash; what to expect
                                    </button>
                                </h2>
                                <div id="acc-%(slug)s" class="accordion-collapse collapse" data-bs-parent="#ministryAccordion">
                                    <div class="accordion-body">
                                        <p class="mb-3">%(long)s</p>
                                        <ul class="mb-0">
%(bullets)s
                                        </ul>
                                    </div>
                                </div>
                            </div>
""" % dict(slug=slug, icon=icon, name=name, long=long_,
           bullets="\n".join("                                            <li>%s</li>" % b for b in bullets)))
    body = """
%(header)s

        <!-- Ministries Start -->
        <div class="container-fluid service py-5">
            <div class="container py-5">
%(head)s                <div class="row g-5">
%(cards)s                </div>
            </div>
        </div>
        <!-- Ministries End -->


        <!-- Expect Start -->
        <div class="container-fluid py-5 bg-light">
            <div class="container py-5">
%(expect_head)s                <div class="row justify-content-center">
                    <div class="col-lg-9 wow fadeIn" data-wow-delay="0.2s">
                        <div class="accordion" id="ministryAccordion">
%(accordion)s                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Expect End -->
""" % dict(header=page_header("Ministries", "Eight doorways into the family &mdash; pick the one that fits your gift.", 26),
           head=section_head("What We Do", "The Eight Ministries"),
           cards=cards,
           expect_head=section_head("Get Involved", "What To Expect In Each Ministry"),
           accordion="".join(acc))
    return page("Ministries — KIZAZI Phenomenal",
                "The eight ministries of KIZAZI Phenomenal: worship & the Word, discipleship "
                "cells, prayer, Friday catch-up, outreach, creative lab, mentorship and care.",
                "ministries", body)


def build_programs():
    cards = "".join(program_card(p, "0.%ds" % (1 + (n % 3) * 2)) for n, p in enumerate(PROGRAMS))
    phases = [
        ("Weeks 1&ndash;3", "Foundations", ["Who God is &mdash; and who you are in Him", "How to read Scripture without panic", "Your first honest prayer rhythm"]),
        ("Weeks 4&ndash;6", "Hearing God", ["Spirit, word and wisdom", "Journaling &amp; quiet mornings", "Testing what you hear"]),
        ("Weeks 7&ndash;9", "Living On Purpose", ["Gifts, calling and campus", "Friendships that carry you", "Saying no without guilt"]),
        ("Weeks 10&ndash;12", "Sent", ["Building your cell&rsquo;s outreach project", "Leading something small", "Commissioning night"]),
    ]
    phase_html = "".join(
        """                    <div class="col-md-6 col-xl-3 wow fadeIn" data-wow-delay="%(delay)s">
                        <div class="border border-primary bg-white p-4 rounded h-100">
                            <div class="px-3 py-2 bg-primary text-white d-inline-block mb-3 program-rate-static">%(weeks)s</div>
                            <h4 class="text-primary">%(name)s</h4>
                            <ul class="mb-0">
%(items)s
                            </ul>
                        </div>
                    </div>
""" % dict(delay="0.%ds" % (1 + n * 2), weeks=w, name=nme,
           items="\n".join("                                <li>%s</li>" % i for i in its))
        for n, (w, nme, its) in enumerate(phases))
    body = """
%(header)s

        <!-- Programs Start -->
        <div class="container-fluid program py-5">
            <div class="container py-5">
%(head)s                <div class="row g-5 justify-content-center">
%(cards)s                </div>
            </div>
        </div>
        <!-- Program End -->


        <!-- Rooted timeline Start -->
        <div class="container-fluid py-5 bg-light">
            <div class="container py-5">
%(rooted_head)s                <div class="row g-4">
%(phases)s                </div>
                <div class="text-center mt-5 wow fadeIn" data-wow-delay="0.2s">
                    <a href="%(reg)s" target="_blank" rel="noopener" class="btn btn-primary px-5 py-3 text-white btn-border-radius">Apply For The Next Rooted Intake</a>
                </div>
            </div>
        </div>
        <!-- Rooted timeline End -->
""" % dict(header=page_header("Programs", "Six programs, one goal: a generation that knows what it believes.", 27),
           head=section_head("Our Programs", "Pick Your Track"),
           cards=cards,
           rooted_head=section_head("Rooted &middot; 12 Weeks", "The Rooted Journey, Week By Week"),
           phases=phase_html, reg=REG_URL)
    return page("Programs — KIZAZI Phenomenal",
                "KIZAZI Phenomenal programs: Rooted (12 weeks), Phenomenal Fridays, Creative Lab, "
                "Mentorship Circle, Campus Ambassadors and Serve East Africa.",
                "programs", body)


def build_events():
    cards = "".join(event_card(e, "0.%ds" % (1 + (n % 4) * 2)) for n, e in enumerate(EVENTS))
    mosaic = []
    for i in range(16, 28):
        mosaic.append("""                        <div class="col-6 col-md-4 col-lg-2 wow fadeIn" data-wow-delay="0.1s">
                            <a href="%s" data-lightbox="kizazi-2026" class="d-block border border-primary rounded-circle overflow-hidden kz-square">
                                %s
                            </a>
                        </div>
""" % (durl(i), img(i, "KIZAZI 2026 photo", cls="img-fluid w-100 kz-cover", w=600)))
    body = """
%(header)s

        <!-- Events Start -->
        <div class="container-fluid events py-5 bg-light">
            <div class="container py-5">
%(head)s                <div class="row g-5 justify-content-center">
%(cards)s                </div>
                <div class="text-center mt-5 wow fadeIn" data-wow-delay="0.2s">
                    <p class="text-body mb-3">Every Friday is free and open &mdash; no registration needed to join the Meet.</p>
                    <a href="%(meet)s" target="_blank" rel="noopener" class="btn btn-primary px-5 py-3 me-3 text-white btn-border-radius"><i class="fas fa-video me-2"></i>Join This Friday</a>
                    <a href="%(reg)s" target="_blank" rel="noopener" class="btn btn-secondary px-5 py-3 text-white btn-border-radius">Get Event Updates</a>
                </div>
            </div>
        </div>
        <!-- Events End-->


        <!-- Recap Start -->
        <div class="container-fluid py-5">
            <div class="container py-5">
%(recap_head)s                <div class="row g-3 justify-content-center">
%(mosaic)s                </div>
                <div class="text-center mt-4">
                    <a class="btn btn-primary px-5 py-3 text-white btn-border-radius" href="gallery.html">See All 42 Photos</a>
                    %(album)s
                </div>
            </div>
        </div>
        <!-- Recap End -->
""" % dict(header=page_header("Events", "Fridays online, nights in person, conferences and tours.", 10),
           head=section_head("Our Events", "What&rsquo;s Coming Up"),
           cards=cards, meet=MEET_URL, reg=REG_URL,
           recap_head=section_head("KIZAZI 2026 &middot; 14&ndash;15 August", "The Flagship, In Pictures"),
           mosaic="".join(mosaic), album=album_button())
    return page("Events — KIZAZI Phenomenal",
                "Upcoming KIZAZI Phenomenal events: Phenomenal Fridays online catch-up, KIZAZI "
                "Conference 2027, Worship & Word Nights and the Campus & School Tour.",
                "events", body)


def build_gallery():
    filters = ['<button type="button" class="btn btn-primary kz-filter-btn active btn-border-radius px-4 py-2 text-white" data-filter="all">All</button>']
    for key, label in GALLERY_CATS:
        filters.append('<button type="button" class="btn btn-primary kz-filter-btn btn-border-radius px-4 py-2 text-white" data-filter="%s">%s</button>' % (key, label))
    items = []
    for i in range(len(PHOTOS)):
        key, label = GALLERY_CATS[i % len(GALLERY_CATS)]
        items.append("""                        <div class="col-6 col-md-4 col-lg-3 kz-gallery-item" data-cat="%s">
                            <a href="%s" data-lightbox="kizazi-gallery" data-title="KIZAZI 2026 &middot; %s" class="d-block border border-primary rounded overflow-hidden kz-square">
                                %s
                            </a>
                        </div>
""" % (key, durl(i), label, img(i, "KIZAZI 2026 photo — %s" % label, cls="img-fluid w-100 kz-cover", w=800)))
    vids = videos()
    if vids:
        vcards = "".join(
            """                    <div class="col-md-6 col-lg-4 wow fadeIn" data-wow-delay="0.%ds">
                        <div class="border border-primary bg-white rounded overflow-hidden h-100">
                            <div class="video kz-video-thumb" %s>
                                <button type="button" class="btn btn-play" data-bs-toggle="modal" data-src="%s" data-bs-target="#videoModal" aria-label="Play %s"><span></span></button>
                            </div>
                            <div class="p-4">
                                <span class="badge bg-secondary mb-2">%s</span>
                                <h4 class="text-primary">%s</h4>
                                <p class="text-body mb-0">%s</p>
                            </div>
                        </div>
                    </div>
""" % (1 + n * 2, bg(v["poster"]), v["embed"], v["title"], v["tag"], v["title"], v["desc"])
            for n, v in enumerate(vids))
        video_block = """        <!-- Videos Start -->
        <div class="container-fluid py-5 bg-light">
            <div class="container py-5">
%s                <div class="row g-5 justify-content-center">
%s                </div>
            </div>
        </div>
        <!-- Videos End -->
""" % (section_head("Films", "Watch The Movement"), vcards)
    else:
        video_block = """        <!-- Videos Start -->
        <div class="container-fluid py-5 bg-light">
            <div class="container py-5">
%(head)s                <div class="row justify-content-center">
                    <div class="col-lg-8 text-center wow fadeIn" data-wow-delay="0.2s">
                        <div class="video border kz-video-thumb kz-video-empty mx-auto mb-4" %(bg)s>
                            %(play)s
                        </div>
                        <p class="text-body mb-4">The film room is being loaded from our Drive album &mdash; clips drop here first.
                        Meanwhile the photos above and our socials carry the story.</p>
                        %(album)s
                    </div>
                </div>
            </div>
        </div>
        <!-- Videos End -->
""" % dict(head=section_head("Films", "Videos Coming Soon"), bg=bg(10), play=play_button(), album=album_button())
    body = """
%(header)s

        <!-- Gallery Start -->
        <div class="container-fluid py-5">
            <div class="container py-5">
%(head)s                <div class="d-flex flex-wrap justify-content-center gap-2 mb-5 wow fadeIn" data-wow-delay="0.2s">
%(filters)s                </div>
                <div class="row g-3" id="kz-gallery-grid">
%(items)s                </div>
            </div>
        </div>
        <!-- Gallery End -->


%(videos)s
""" % dict(header=page_header("Gallery", "All 42 photos from KIZAZI 2026 &mdash; 14&ndash;15 August, two days of fire.", 21),
           head=section_head("KIZAZI 2026", "The Album", "Tap any photo to open the lightbox. Filters are our best guess at categories &mdash; the album came unlabelled."),
           filters="\n".join("                    " + f for f in filters),
           items="".join(items), videos=video_block)
    return page("Gallery — KIZAZI Phenomenal",
                "The full KIZAZI 2026 photo album: worship, word, community, service, creative "
                "and behind-the-scenes, plus films from the Drive album.",
                "gallery", body)


def build_blog():
    cards = "".join(blog_card(b, "0.%ds" % (1 + n * 2), "#%s") for n, b in enumerate(BLOG))
    posts = []
    for n, (title, date, team, initials, photo_i, tag, paras) in enumerate(BLOG):
        posts.append("""                <div class="row g-5 align-items-start mb-5 pb-5 border-bottom border-primary wow fadeIn" data-wow-delay="0.1s" id="post-%(n)d">
                    <div class="col-lg-5">
                        <div class="overflow-hidden img-border-radius border border-primary">
                            %(img)s
                        </div>
                    </div>
                    <div class="col-lg-7">
                        <div class="d-flex flex-wrap gap-3 mb-3">
                            <span class="badge bg-primary">%(tag)s</span>
                            <small class="text-body my-auto"><i class="fas fa-calendar me-1"></i>%(date)s</small>
                            <small class="text-body my-auto"><i class="fas fa-user-pen me-1"></i>%(team)s</small>
                        </div>
                        <h1 class="display-5 text-dark mb-4">%(title)s</h1>
%(paras)s
                    </div>
                </div>
""" % dict(n=n + 1, tag=tag, date=date, team=team, title=title,
           img=img(photo_i, title, cls="img-fluid w-100 kz-cover", w=1000),
           paras="\n".join("                        <p class=\"text-body mb-3\">%s</p>" % p for p in paras)))
    body = """
%(header)s

        <!-- Blog Start-->
        <div class="container-fluid blog py-5">
            <div class="container py-5">
%(head)s                <div class="row g-5 justify-content-center">
%(cards)s                </div>
            </div>
        </div>
        <!-- Blog End-->


        <!-- Posts Start -->
        <div class="container-fluid py-5 bg-light">
            <div class="container py-5">
%(posts_head)s%(posts)s                <div class="text-center">
                    <a href="blog.html" class="btn btn-primary px-5 py-3 text-white btn-border-radius">Back To Top Of The Blog</a>
                </div>
            </div>
        </div>
        <!-- Posts End -->
""" % dict(header=page_header("Word &amp; Stories", "Devotionals, recaps and practicals from the family.", 14),
           head=section_head("Latest News &amp; Blog", "Read Our Latest"),
           cards=cards,
           posts_head=section_head("Full Posts", "This Term&rsquo;s Writing"),
           posts="".join(posts))
    return page("Blog — KIZAZI Phenomenal",
                "Devotionals, conference recaps and practical discipleship writing from the "
                "KIZAZI Phenomenal teams.",
                "blog", body)


def build_team():
    cards = "".join(team_card(t, "0.%ds" % (1 + (n % 4) * 2)) for n, t in enumerate(TEAMS))
    steps = [
        ("fa-user-plus", "1 &middot; Register", "Fill the free form &mdash; it takes two minutes."),
        ("fa-comments", "2 &middot; Get placed", "A cell and a serving team near you adopt you."),
        ("fa-hands-helping", "3 &middot; Serve", "Show up for one thing this term. That&rsquo;s how it starts."),
    ]
    step_html = "".join(
        """                    <div class="col-md-4 wow fadeIn" data-wow-delay="0.%ds">
                        <div class="text-center border border-primary bg-white p-4 rounded h-100">
                            <i class="fas %s fa-4x text-primary mb-3"></i>
                            <h4 class="text-primary">%s</h4>
                            <p class="text-body mb-0">%s</p>
                        </div>
                    </div>
""" % (1 + n * 2, icon, name, desc) for n, (icon, name, desc) in enumerate(steps))
    body = """
%(header)s

        <!-- Team Start-->
        <div class="container-fluid team py-5">
            <div class="container py-5">
%(head)s                <div class="row g-5 justify-content-center">
%(cards)s                </div>
            </div>
        </div>
        <!-- Team End-->


        <!-- Serve Start -->
        <div class="container-fluid py-5 bg-light">
            <div class="container py-5">
%(serve_head)s                <div class="row g-4">
%(steps)s                </div>
                <div class="text-center mt-5 wow fadeIn" data-wow-delay="0.2s">
                    <a href="%(reg)s" target="_blank" rel="noopener" class="btn btn-primary px-5 py-3 text-white btn-border-radius">Register &amp; Pick A Team</a>
                </div>
            </div>
        </div>
        <!-- Serve End -->
""" % dict(header=page_header("Team", "Serving teams, not celebrities &mdash; every role is a doorway.", 17),
           head=section_head("Serving Teams", "Meet The Crew", "Photos are from KIZAZI 2026; roles are open &mdash; yours could be next."),
           cards=cards,
           serve_head=section_head("How To Serve", "Three Steps In"),
           steps=step_html, reg=REG_URL)
    return page("Team — KIZAZI Phenomenal",
                "The serving teams of KIZAZI Phenomenal: worship & sound, word & teaching, "
                "prayer watch, discipleship mentors, media crew, outreach, hospitality and mentorship.",
                "team", body)


def build_testimonial():
    body = """
%(header)s

%(carousel)s

        <!-- Share Start -->
        <div class="container-fluid py-5 bg-light">
            <div class="container py-5">
                <div class="p-5 bg-white border border-primary rounded text-center wow fadeIn" data-wow-delay="0.2s">
                    <h1 class="display-5 mb-4">Your Story Belongs Here</h1>
                    <p class="text-body mb-4">What has God done in you since you joined? Tell us &mdash; initials only if you prefer,
                    exactly like the voices above.</p>
                    <a href="%(reg)s" target="_blank" rel="noopener" class="btn btn-primary px-5 py-3 me-3 text-white btn-border-radius">Share Your Testimony</a>
                    <a href="%(ig)s" target="_blank" rel="noopener" class="btn btn-secondary px-5 py-3 text-white btn-border-radius">Or DM Us On Instagram</a>
                </div>
            </div>
        </div>
        <!-- Share End -->
""" % dict(header=page_header("Testimonial", "Voices from the family &mdash; initials only, stories real.", 30),
           carousel=testimonials_carousel(), reg=REG_URL, ig=INSTAGRAM_URL)
    return page("Testimonial — KIZAZI Phenomenal",
                "Testimonies from KIZAZI Phenomenal: students and young workers across East Africa "
                "on what the family has meant to them.",
                "testimonial", body)


def build_contact():
    routes = [
        ("fa-user-plus", "Register", "The free form is the front door &mdash; placement, cells and updates start here.", REG_URL, "Open the form"),
        ("fa-video", "Friday Meet", "Every Friday, 8:00 PM EAT (<span data-next-friday-long>&hellip;</span>). No registration needed to join.", MEET_URL, "Join the Meet"),
        ("fa-hashtag", "Socials", "Clips, announcements and DMs &mdash; TikTok, Instagram and Facebook.", INSTAGRAM_URL, "Follow us"),
        ("fa-link", LINKTREE_NOTE, "One link with everything lands here soon; until then the form and socials cover it.", REG_URL, "Use the form"),
    ]
    route_html = "".join(
        """                        <div class="col-lg-6 wow fadeIn" data-wow-delay="0.%ds">
                            <div class="d-flex w-100 border border-primary p-4 rounded bg-white h-100">
                                <i class="fas %s fa-2x text-primary me-4"></i>
                                <div>
                                    <h4>%s</h4>
                                    <p class="mb-2">%s</p>
                                    <a class="btn btn-primary btn-sm px-4 py-2 text-white btn-border-radius" href="%s" target="_blank" rel="noopener">%s</a>
                                </div>
                            </div>
                        </div>
""" % (1 + n * 2, icon, name, desc, url, cta) for n, (icon, name, desc, url, cta) in enumerate(routes))
    faqs = [
        ("Do I need to register to join a Friday?", "No &mdash; the Meet link is open. Registration only helps us place you in a cell and keep you posted."),
        ("Is KIZAZI a denomination?", "No. We are a youth fellowship; students from every church and campus fellowship are welcome."),
        ("Which countries do you serve?", "Kenya, Uganda, Tanzania and Rwanda &mdash; online every Friday, in person through cells and tours."),
        ("What does it cost?", "Nothing. Programs, cells and Friday catch-ups are free; Serve East Africa trips fundraise together."),
        ("Can I serve behind the scenes?", "Yes &mdash; pick a team on the Team page and register; a leader will reach out on socials."),
    ]
    faq_html = "".join(
        """                            <div class="accordion-item">
                                <h2 class="accordion-header">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq-%d" aria-expanded="false" aria-controls="faq-%d">%s</button>
                                </h2>
                                <div id="faq-%d" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
                                    <div class="accordion-body">%s</div>
                                </div>
                            </div>
""" % (n, n, q, n, a) for n, (q, a) in enumerate(faqs))
    body = """
%(header)s

        <!-- Contact Start -->
        <div class="container-fluid py-5">
            <div class="container py-5">
                <div class="p-5 bg-light rounded">
%(head)s                    <div class="row g-4 mb-5">
%(routes)s                    </div>
                    <div class="row g-5">
                        <div class="col-lg-6 wow fadeIn" data-wow-delay="0.3s">
                            <div class="border border-primary h-100 rounded overflow-hidden kz-square-lg">
                                %(photo)s
                            </div>
                        </div>
                        <div class="col-lg-6 wow fadeIn" data-wow-delay="0.5s">
                            <div class="d-flex flex-column p-4 ps-5 text-dark border border-primary bg-white h-100" style="border-radius: 50%% 20%% / 10%% 40%%;">
                                <h4 class="text-primary mb-3">This week at KIZAZI</h4>
                                <p><strong>Friday:</strong> Online Catch-Up, 8:00 PM EAT</p>
                                <p><strong>Next Friday:</strong> <span data-next-friday-long>&hellip;</span></p>
                                <p><strong>Weekdays:</strong> cells, prayer &amp; campus visits (schedule shared weekly)</p>
                                <p><strong>Where:</strong> Google Meet + cells in KE &middot; UG &middot; TZ &middot; RW</p>
                                <p class="mb-0"><strong>Fastest reply:</strong> DM us on Instagram or TikTok</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Contact End -->


        <!-- FAQ Start -->
        <div class="container-fluid py-5 bg-light">
            <div class="container py-5">
%(faq_head)s                <div class="row justify-content-center">
                    <div class="col-lg-9 wow fadeIn" data-wow-delay="0.2s">
                        <div class="accordion" id="faqAccordion">
%(faqs)s                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- FAQ End -->
""" % dict(header=page_header("Contact", "No office, no inbox &mdash; just doors that actually open.", 31),
           head=section_head("Contact Us", "Four Ways In"),
           routes=route_html, photo=img(32, "KIZAZI 2026 gathering", cls="img-fluid w-100 h-100 kz-cover", w=1200),
           faq_head=section_head("Quick Answers", "Asked Every Term"),
           faqs=faq_html)
    return page("Contact — KIZAZI Phenomenal",
                "Reach KIZAZI Phenomenal: the free registration form, the Friday Google Meet, "
                "our socials and answers to common questions.",
                "contact", body)


def build_404():
    body = """
%(header)s

        <!-- 404 Start -->
        <div class="container-fluid py-5 wow fadeInUp" data-wow-delay="0.3s">
            <div class="container text-center py-5">
                <div class="row justify-content-center">
                    <div class="col-lg-6">
                        <i class="bi bi-exclamation-triangle display-1 text-primary"></i>
                        <h1 class="display-1">404</h1>
                        <h1 class="mb-4">Page Not Found</h1>
                        <p class="mb-4">We&rsquo;re sorry &mdash; that page isn&rsquo;t here. Maybe head home, or catch us live this Friday at 8:00 PM EAT?</p>
                        <a class="btn btn-primary rounded-pill py-3 px-5 me-2" href="index.html">Go Home</a>
                        <a class="btn btn-secondary rounded-pill py-3 px-5" href="%(meet)s" target="_blank" rel="noopener">Join Friday</a>
                    </div>
                </div>
            </div>
        </div>
        <!-- 404 End -->
""" % dict(header=page_header("404 Error", "Lost? The family is one click away.", 33), meet=MEET_URL)
    return page("404 — KIZAZI Phenomenal", "Page not found — KIZAZI Phenomenal.", "home", body,
                with_video_modal=False)


BUILDERS = [
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
    for name, fn in BUILDERS:
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
            fh.write(fn())
        print("wrote %s" % name)


if __name__ == "__main__":
    main()
