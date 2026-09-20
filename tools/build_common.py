#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KIZAZI Phenomenal — shared build data & site chrome.

Everything the site needs to stay consistent lives here:
  * external links (registration, Meet, socials)
  * the 42 "KIZAZI 2026" Google Drive photo IDs + <img data-drive=...> helpers
  * shared chrome: <head>, topbar, navbar, page-header, footer, copyright, scripts
  * content data: ministries, programs, events, blog, teams, testimonies

`tools/build.py` imports this module and composes the per-page bodies.
Edit the data below, then run:  python3 tools/build.py
"""

import html as _html

# ------------------------------------------------------------- external links
REG_URL = "https://forms.gle/vzRJrigBHCNormVA9"
MEET_URL = "https://meet.google.com/mcr-fupc-buw"
TIKTOK_URL = "https://www.tiktok.com/@kizazi.phenomenal"
INSTAGRAM_URL = "https://www.instagram.com/kizazi_phenomenal"
FACEBOOK_URL = "https://www.facebook.com/kizaziphenomenal"
LINKTREE_NOTE = "Linktree coming soon"

SITE = {
    "name": "KIZAZI Phenomenal",
    "tagline": "A generation on fire for God.",
    "verse_ref": "1 Timothy 4:12",
    "verse": ("Let no one despise you for your youth, but set the example "
              "for the believers in speech, in conduct, in love, in faith, in purity."),
    "countries": "Kenya &bull; Uganda &bull; Tanzania &bull; Rwanda",
}

# Nav order = page order. (file, label, active key)
PAGES = [
    ("index.html", "Home", "home"),
    ("about.html", "About", "about"),
    ("ministries.html", "Ministries", "ministries"),
    ("programs.html", "Programs", "programs"),
    ("events.html", "Events", "events"),
    ("gallery.html", "Gallery", "gallery"),
    ("blog.html", "Blog", "blog"),
    ("team.html", "Team", "team"),
    ("testimonial.html", "Testimonial", "testimonial"),
    ("contact.html", "Contact", "contact"),
]

# ------------------------------------------------- "KIZAZI 2026" Drive photos
# Public Google Drive file IDs (shared album). Resolved in the browser by
# js/kizazi.js:  drive thumbnail -> lh3 -> uc?export=view -> local placeholder.
PHOTOS = [
    "1w2oIGh9BBn2tXBDsNy8CvpZQywT6Qceh",   # 0
    "13BJwgGhr6XDHC9h13ByCXUag3ViLt4pK",   # 1
    "123Sg1hwdaWtmPDX9Qb6ePdTY8hzg04vV",   # 2
    "16r29HQUQrjocav3vAQa8T_Oun9K5lips",   # 3
    "138YqINm17FRZL1_guRj83Am0GF9QRV-n",   # 4
    "1N8Y4GFV3USaz65XVOQLyW-uUqNxxcyFC",   # 5
    "1lsHDY2-8zHeowao8Rs78H3ZgZaLh8672",   # 6
    "1A3iWtP0uMt94OvJVoQjdkR2I6kI9_41w",   # 7
    "1r53IGVmSRyDSz9Xx9Wysnz8V_wQ20OAF",   # 8
    "1k8-cGrV3hBe_bwbYc4_1MTg33q_pUsl0",   # 9
    "1zsNvbbpcajqQzaxU1f-9Ja-ZxCNxto7J",   # 10
    "1Pm8zA9AMZ5wNA_1XEdu9eOIPeKT0dhf5",   # 11
    "1J5BDRLvnpFOIA0JKbn5MviwyAEQhBaEn",   # 12
    "1NCK66Nzrr546lp8AJ8STAC5xSa-cIJpH",   # 13
    "1CTKDKQKLMM9d3GpFd2x6o_h4zNUTZmsD",   # 14
    "10dj_djGdcTMdxexY8rUn70k_hNgxZtVL",   # 15
    "1JuDHk07-EF-I6Kx11CJmPBtYuOl1eq9l",   # 16
    "1R9jm7BWDV-W22ASIHvRY_idhTjRFFIB3",   # 17
    "11q6L_hiO0Y9Ta_Fsfq4qp5mPjluvtAxd",   # 18
    "1o2flLyDHec9o19S6sC9sduj87e5YBr8a",   # 19
    "1dTi97bdexjjR-mlTQj50dEK2s39ZqT2U",   # 20
    "1KaN84BydKGM5gLShYPGwn_gg9lPyRmzh",   # 21
    "18VifyAxl_4l920PrnaGl07SSti9f8Q_e",   # 22
    "1YL9wWv2xYSE0fdrGLCFTA3CmlO9Q5E5D",   # 23
    "1xC3xzAePVgOzjyMOVLttJDPhrOEEoCUx",   # 24
    "1QbiJygQMAOB_4YWeMw_2s7mKgbc3xqR2",   # 25
    "1qFNX35z-KnZgpw0dmnXRRQcVK70uE-wt",   # 26
    "1lu1CakILnn5Ar6-JLSs3W8zjd6fALEme",   # 27
    "1TyHtNtLIsNm7hiN9xLLR6EzNoUZ8Lakh",   # 28
    "1MVKVbCyOOSxVvCEKzJeASc5SjxO-6fGp",   # 29
    "14tH-n17U4UtHupT7SGKQsyBq5yIIO-Wl",   # 30
    "1tOT1KZVRYt9IiCY-FTo1PdEs_PoKBc9C",   # 31
    "1XDDP7w7B9kKk6EuOuoZUevgqeRhbrUaR",   # 32
    "1URj0XMQeL1mSIMTPvoih6s1ZaocttXbf",   # 33
    "1wFCvoEH6UiTwp1gGOz92pzhrrUkKc2yA",   # 34
    "1t1GqRjKBRas5Qsi9oGqDSrkidRkGXlfN",   # 35
    "1kLm0a58babwyW_n4_9A6WZFVvvQywUEo",   # 36
    "1hr49FXlF6QJ0jw1mRAcELocFDytVL_ln",   # 37
    "1puPEA7OhRI_hJo7Czqfl-d4tSTQZRiLW",   # 38
    "1FMHYgnn1F8xw7B94PFZmtdudnCZMtomu",   # 39
    "1AJIZw6K86hDmgrbOs2ZOPmzLoF3TuWNa",   # 40
    "1m9-cKUNBm1c_DHfF3v9_RmdRP8X4Qq_B",   # 41
]

assert len(PHOTOS) == 42, "expected exactly 42 Drive photo IDs"

# Gallery filter categories — assigned round-robin (see NOTES.md, assumption #6).
GALLERY_CATS = [
    ("worship", "Worship"),
    ("word", "Word"),
    ("community", "Community"),
    ("service", "Service"),
    ("creative", "Creative"),
    ("bts", "Behind the Scenes"),
]

FOOTER_GRID = [28, 29, 30, 31, 32, 33, 34, 35]


def durl(i, w=1600):
    """Primary hotlinkable Drive URL (also used as the lightbox target)."""
    return "https://drive.google.com/thumbnail?id=%s&sz=w%d" % (PHOTOS[i], w)


def img(i, alt="", cls="", w=1600, eager=False, extra=""):
    """<img> that js/kizazi.js hydrates from data-drive with fallbacks."""
    loading = "" if eager else 'loading="lazy"'
    return ('<img data-drive="%s" data-drive-w="%d" class="%s" alt="%s" %s%s>'
            % (PHOTOS[i], w, cls, _html.escape(alt), loading,
               (" " + extra) if extra else ""))


def gallery_cat(i):
    key, label = GALLERY_CATS[i % len(GALLERY_CATS)]
    return key, label


# ------------------------------------------------------------------- chrome ---
def head(title, desc):
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>%(title)s</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta content="%(desc)s" name="description">
    <meta content="KIZAZI Phenomenal, Christian youth ministry, East Africa, youth fellowship, discipleship, worship, Kenya, Uganda, Tanzania, Rwanda" name="keywords">
    <meta content="#F4511E" name="theme-color">
    <meta property="og:site_name" content="KIZAZI Phenomenal">
    <meta property="og:title" content="%(title)s">
    <meta property="og:description" content="%(desc)s">
    <meta property="og:type" content="website">
    <meta property="og:image" content="img/brand/logo-mark.png">

    <link rel="icon" type="image/png" href="img/brand/logo-mark.png">
    <link rel="apple-touch-icon" href="img/brand/logo-mark.png">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
    <link href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" rel="stylesheet">

    <link href="lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">
    <link href="lib/lightbox/css/lightbox.min.css" rel="stylesheet">

    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
    <link href="css/kizazi.css" rel="stylesheet">
</head>
""" % {"title": _html.escape(title), "desc": _html.escape(desc)}


def body_open(active):
    return '<body class="kz-page kz-page-%s">\n' % active


def social_icons(cls="kz-social"):
    items = [
        (TIKTOK_URL, "fab fa-tiktok", "TikTok"),
        (INSTAGRAM_URL, "fab fa-instagram", "Instagram"),
        (FACEBOOK_URL, "fab fa-facebook-f", "Facebook"),
    ]
    out = []
    for url, icon, label in items:
        out.append('<a class="%s" href="%s" target="_blank" rel="noopener" aria-label="%s" title="%s"><i class="%s"></i></a>'
                   % (cls, url, label, label, icon))
    return "\n".join(out)


def topbar():
    return """        <div class="kz-topbar">
            <div class="container d-flex flex-wrap justify-content-between align-items-center gap-2">
                <div class="d-none d-lg-flex align-items-center gap-3">
                    <span class="kz-topbar-pill"><i class="fas fa-globe-africa"></i> Serving East Africa &mdash; %(countries)s</span>
                    <a class="kz-topbar-live" href="%(meet)s" target="_blank" rel="noopener"><span class="kz-live-dot"></span> This Friday &middot; Online Catch-Up &middot; 8:00 PM EAT</a>
                </div>
                <div class="d-flex align-items-center gap-3">
                    <span class="kz-topbar-note" title="A single link with everything"><i class="fas fa-link"></i> %(linktree)s</span>
                    <div class="d-flex align-items-center gap-2">
                        %(socials)s
                    </div>
                    <a class="kz-topbar-cta" href="%(reg)s" target="_blank" rel="noopener">Join Us</a>
                </div>
            </div>
        </div>
""" % {"countries": SITE["countries"], "meet": MEET_URL, "reg": REG_URL,
       "linktree": LINKTREE_NOTE,
       "socials": social_icons(cls="kz-topbar-social")}


def navbar(active):
    links = []
    for file_, label, key in PAGES:
        cls = "nav-link kz-nav-link active" if key == active else "nav-link kz-nav-link"
        links.append('<li class="nav-item"><a class="%s" href="%s">%s</a></li>' % (cls, file_, label))
    return """        <div class="container-fluid kz-navbar-wrap">
            <div class="container">
                <nav class="navbar navbar-expand-xl navbar-light kz-navbar py-0" id="mainNav">
                    <a class="navbar-brand kz-brand d-flex align-items-center" href="index.html">
                        <img src="img/brand/logo-mark.png" alt="KIZAZI Phenomenal flame-K logo" class="kz-brand-logo" width="46" height="46">
                        <span class="kz-brand-text">KIZAZI <span class="kz-brand-phen">Phenomenal</span></span>
                    </a>
                    <button class="navbar-toggler kz-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
                            aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="kz-toggler-bar"></span>
                        <span class="kz-toggler-bar"></span>
                        <span class="kz-toggler-bar"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarCollapse">
                        <ul class="navbar-nav m-auto ms-4 mb-3 mb-xl-0">
%s
                        </ul>
                        <a class="btn kz-btn kz-btn-sweep kz-nav-cta text-white" href="%(reg)s" target="_blank" rel="noopener"><i class="fas fa-bolt me-2"></i>Register Free</a>
                    </div>
                </nav>
            </div>
        </div>
""" % {"links": "\n".join(links), "reg": REG_URL}


def page_header(title, sub, photo_i, kicker=""):
    return """        <!-- Page Header Start -->
        <header class="kz-page-header">
            <div class="kz-page-header-dots"></div>
            <div class="container py-5">
                <div class="row align-items-center g-4">
                    <div class="col-lg-8">
                        <nav aria-label="breadcrumb">
                            <ol class="breadcrumb kz-breadcrumb mb-3">
                                <li class="breadcrumb-item"><a href="index.html"><i class="fas fa-home me-1"></i>Home</a></li>
                                <li class="breadcrumb-item active" aria-current="page">%(title)s</li>
                            </ol>
                        </nav>
                        <span class="kz-kicker kz-kicker-light">%(kicker)s</span>
                        <h1 class="kz-page-title">%(title)s</h1>
                        <p class="kz-page-sub">%(sub)s</p>
                    </div>
                    <div class="col-lg-4 d-none d-lg-block text-center">
                        <div class="kz-page-photo">%(photo)s</div>
                    </div>
                </div>
            </div>
        </header>
        <!-- Page Header End -->
""" % {"title": _html.escape(title), "sub": sub, "kicker": kicker,
       "photo": img(photo_i, "KIZAZI Phenomenal — %s" % title, cls="img-fluid")}


def section_head(kicker, title, sub=""):
    sub_html = "<p class=\"kz-section-sub\">%s</p>" % sub if sub else ""
    return """                <div class="text-center mx-auto kz-section-head kz-reveal" style="max-width: 640px;">
                    <span class="kz-kicker">%s</span>
                    <h2 class="kz-section-title">%s</h2>
                    %s
                </div>
""" % (kicker, title, sub_html)


def footer():
    grid = []
    for i in FOOTER_GRID:
        grid.append("""<div class="col-3">
                                <a class="kz-footer-photo" href="gallery.html" title="View in gallery">
                                    %s
                                </a>
                            </div>""" % img(i, "KIZAZI 2026 photo", cls="img-fluid rounded-circle"))
    links = "\n".join(
        '                                <li><a href="%s"><i class="fas fa-arrow-right kz-footer-arrow"></i>%s</a></li>'
        % (file_, label)
        for file_, label, _ in PAGES
    )
    return """        <footer class="kz-footer">
            <div class="kz-footer-aurora"></div>
            <div class="container py-5">
                <div class="row g-4 g-lg-5">
                    <div class="col-md-6 col-xl-3">
                        <div class="kz-footer-item">
                            <a class="kz-footer-brand d-flex align-items-center" href="index.html">
                                <img src="img/brand/logo-mark.png" alt="KIZAZI Phenomenal" class="kz-brand-logo kz-brand-logo-lg">
                                <span class="kz-brand-text text-white">KIZAZI <span class="kz-brand-phen">Phenomenal</span></span>
                            </a>
                            <p class="kz-footer-blurb">%(tagline)s A Christian youth movement across %(countries)s &mdash; worship that moves, discipleship that sticks, a family that carries you.</p>
                            <p class="kz-footer-verse kz-hand">&ldquo;%(verse_short)s&rdquo; &mdash; %(verse_ref)s</p>
                            <div class="kz-footer-newsletter">
                                <h5 class="mb-3">Newsletter</h5>
                                <form class="kz-newsletter" novalidate>
                                    <input type="email" class="form-control kz-newsletter-input" placeholder="Your email" aria-label="Your email" required>
                                    <button type="submit" class="kz-newsletter-btn kz-btn kz-btn-sweep text-white">Sign Up</button>
                                </form>
                                <p class="kz-newsletter-note">Announcements only &mdash; no spam, ever.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-xl-3">
                        <div class="kz-footer-item">
                            <h4 class="kz-footer-title">This Week at KIZAZI</h4>
                            <div class="kz-schedule">
                                <div class="kz-schedule-row kz-schedule-live">
                                    <span class="kz-schedule-day">Friday</span>
                                    <span class="kz-schedule-what">Phenomenal Friday &mdash; Online Catch-Up, <strong>8:00 PM EAT</strong></span>
                                    <a class="kz-schedule-link" href="%(meet)s" target="_blank" rel="noopener">Join <i class="fas fa-external-link-alt"></i></a>
                                </div>
                                <div class="kz-schedule-row">
                                    <span class="kz-schedule-day">Weekdays</span>
                                    <span class="kz-schedule-what">Cells, prayer &amp; campus visits (schedule shared weekly)</span>
                                </div>
                                <div class="kz-schedule-row">
                                    <span class="kz-schedule-day">Next Friday</span>
                                    <span class="kz-schedule-what"><span data-next-friday-long>&hellip;</span></span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-xl-3">
                        <div class="kz-footer-item">
                            <h4 class="kz-footer-title">Quick Links</h4>
                            <ul class="kz-footer-links">
%(links)s
                            </ul>
                            <div class="d-flex align-items-center gap-2 mt-4">
                                %(socials)s
                            </div>
                            <p class="kz-footer-note mt-3"><i class="fas fa-link me-1"></i> %(linktree)s &mdash; one link for everything.</p>
                        </div>
                    </div>
                    <div class="col-md-6 col-xl-3">
                        <div class="kz-footer-item">
                            <h4 class="kz-footer-title">KIZAZI 2026 &mdash; in pics</h4>
                            <div class="row g-2">
%(grid)s
                            </div>
                            <a class="kz-footer-more" href="gallery.html">Full gallery <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="kz-copyright">
                <div class="container d-flex flex-wrap justify-content-between align-items-center gap-2">
                    <span class="kz-copyright-text">&copy; <span data-year>2026</span> KIZAZI Phenomenal. All rights reserved.</span>
                    <span class="kz-copyright-credit">Template <a href="https://htmlcodex.com" target="_blank" rel="noopener">BabyCare</a> by <a href="https://htmlcodex.com" target="_blank" rel="noopener">HTML Codex</a> &middot; customised for KIZAZI</span>
                </div>
            </div>
        </footer>
""" % {"tagline": SITE["tagline"], "countries": SITE["countries"],
       "verse_short": SITE["verse"][:60] + "&hellip;", "verse_ref": SITE["verse_ref"],
       "meet": MEET_URL, "linktree": LINKTREE_NOTE,
       "socials": social_icons(cls="kz-footer-social"),
       "links": links, "grid": "\n".join(grid)}


def back_to_top():
    return """        <a href="#" class="kz-back-to-top" aria-label="Back to top"><i class="fas fa-arrow-up"></i></a>
"""


def scripts():
    return """    <script src="js/vendor/jquery.min.js"></script>
    <script src="js/vendor/bootstrap.bundle.min.js"></script>
    <script src="lib/owlcarousel/owl.carousel.min.js"></script>
    <script src="lib/lightbox/js/lightbox.min.js"></script>
    <script src="js/kizazi.js"></script>
</body>
</html>
"""


# -------------------------------------------------------------- content data ---
# 8 ministries — (slug, icon, name, blurb, detail, [what to expect])
MINISTRIES = [
    ("worship-word", "fa-music", "Worship &amp; The Word",
     "Songs that move and messages that stick.",
     "Worship that gets you on your feet, and the Word taught without fluff. "
     "This is the heartbeat of KIZAZI &mdash; everything else flows from time with God.",
     ["Friday catch-ups with live worship &amp; teaching", "Worship &amp; Word Nights through the term", "Worshipper and teacher tracks if you want to lead"]),
    ("cells", "fa-users", "Discipleship Cells",
     "Small groups where nobody fakes it.",
     "Real discipleship happens in small rooms. Our cells meet around the Word, "
     "ask hard questions and carry each other through exams, home and everything between.",
     ["Weekly cell meetings (online + in person)", "The 12-week Rooted journey", "Accountability that actually shows up"]),
    ("prayer", "fa-hands-praying", "Prayer &amp; Intercession",
     "The room where heaven gets serious.",
     "We believe prayer changes the atmosphere of a generation. A constant watch "
     "intercedes for East Africa, for our campuses and for the family &mdash; before and between every gathering.",
     ["Prayer before every event &mdash; join in", "Rotating intercession teams", "National &amp; campus prayer lists shared weekly"]),
    ("friday", "fa-video", "Friday Online Catch-Up",
     "Every Friday, 8:00 PM EAT. Same time, different fire.",
     "Our weekly online gathering: worship, a Word bite, prayers and connection "
     "across Kenya, Uganda, Tanzania and Rwanda. One link, whole family.",
     ["Live on Google Meet, 8:00 PM EAT", "Worship, teaching and prayer every week", "Open to everyone &mdash; no registration needed to join in"]),
    ("outreach", "fa-globe-africa", "Outreach &amp; Missions",
     "A generation that can&rsquo;t stay home.",
     "Campus visits, school tours and Serve East Africa trips &mdash; we take the "
     "gospel and the gospel&rsquo;s hands-on love to campuses, communities and borders.",
     ["Campus &amp; school tours each term", "Serve East Africa cross-border trips", "Outreach teams that plan and fundraise together"]),
    ("creative", "fa-pen-nib", "Creative &amp; Media Lab",
     "Where the KIZAZI story gets made.",
     "Design, video, socials, set and stage &mdash; our lab turns worship into something "
     "the generation can&rsquo;t see, feel and share. Every album shot you see was made here.",
     ["Monthly creative workshops", "Media crew for every event", "Publishing across TikTok, Instagram &amp; Facebook"]),
    ("mentorship", "fa-graduation-cap", "Mentorship &amp; Career",
     "Someone older, on your side.",
     "Students matched with mentors for school, work, vocation and purpose. "
     "Career clinics, CV nights, application sprints and honest conversations about the future.",
     ["1-on-1 and small-group mentoring", "Career clinics &amp; CV nights in term", "Scholarship and application support"]),
    ("care", "fa-heart", "Community &amp; Care",
     "Family means nobody carries it alone.",
     "Birthdays, hospital visits, grief, homesickness &mdash; care is a ministry. "
     "Hospitality at every event, check-ins through the week, and a family that notices.",
     ["Hospitality &amp; reception at events", "Weekly check-ins in the cells", "Care funds for families in crisis"]),
]

# 6 programs — (name, rate badge, photo_i, desc, leader, leader initials, when, where)
PROGRAMS = [
    ("Rooted", "Free &middot; 12 weeks", 4,
     "A 12-week discipleship journey through the basics that don&rsquo;t get skipped &mdash; "
     "who God is, how to hear from Him, how to pray, how to live on purpose.",
     "Discipleship Cells team", "DC", "12 weeks &middot; new intake each term", "Online + in person"),
    ("Phenomenal Fridays", "Weekly", 5,
     "The heartbeat: worship, a Word bite, prayer and connection &mdash; live every "
     "Friday at 8:00 PM EAT on Google Meet, across East Africa.",
     "Worship &amp; The Word team", "WW", "Fridays &middot; 8:00 PM EAT", "Google Meet"),
    ("KIZAZI Creative Lab", "Term intake", 6,
     "Worship, design, video and media workshops for the makers &mdash; learn to build "
     "what the movement puts in front of the generation.",
     "Creative &amp; Media Lab", "CM", "Monthly sessions", "Studio + online"),
    ("Mentorship Circle", "Applications open", 7,
     "Get matched with a mentor for school, career and purpose. Small circles, "
     "regular check-ins, real accountability.",
     "Mentorship &amp; Career", "MC", "Ongoing", "1-on-1 + small group"),
    ("Campus Ambassadors", "Recruiting now", 8,
     "Plant and lead KIZAZI on your campus &mdash; toolkits, training and a network of "
     "ambassadors across East African universities.",
     "Outreach &amp; Missions", "OM", "During term", "Your campus"),
    ("Serve East Africa", "Next trip TBA", 9,
     "Annual cross-border outreach trips across Kenya, Uganda, Tanzania and Rwanda. "
     "Train, raise, go, report.",
     "Community &amp; Care", "CC", "Annual trips", "Kenya &middot; Uganda &middot; Tanzania &middot; Rwanda"),
]

# 4 events — dict(title, tag, photo_i, desc, when, time, place, cta_label, cta_url, date_mode)
# date_mode: "friday" (auto next Friday) | "static" (when text is final)
EVENTS = [
    dict(title="Phenomenal Friday &mdash; Online Catch-Up", tag="Weekly", photo=10,
         desc="Worship, a Word bite, prayer and connection &mdash; live from across East Africa.",
         when="friday", time="8:00 PM EAT", place="Google Meet",
         cta_label="Join Live", cta_url=MEET_URL, cta_icon="fa-video"),
    dict(title="KIZAZI Conference 2027", tag="2027 Flagship", photo=11,
         desc="The next flagship. Two days of worship, word and fire &mdash; details as they drop.",
         when="August 2027 &middot; dates soon", time="Full-day", place="East Africa",
         cta_label="Get Notified", cta_url=REG_URL, cta_icon="fa-bell"),
    dict(title="Worship &amp; Word Night", tag="Monthly", photo=12,
         desc="One night a month we gather in person &mdash; deeper worship, uncut Word.",
         when="Monthly &middot; announced on socials", time="Evening", place="In person + live stream",
         cta_label="Follow for the Date", cta_url=INSTAGRAM_URL, cta_icon="fa-calendar-alt"),
    dict(title="Campus &amp; School Tour", tag="Termly", photo=13,
         desc="We bring the catch-up to campuses and schools across the region. Invite us to yours.",
         when="Every term &middot; visits announced weekly", time="Flexible", place="Your campus",
         cta_label="Host Us", cta_url=REG_URL, cta_icon="fa-school"),
]

# Blog — (title, date, team, team initials, photo_i, tag, body paragraphs)
BLOG = [
    ("What it means to be a &ldquo;phenomenal&rdquo; generation",
     "12 Aug 2026", "Media &amp; Creative Crew", "CM", 14, "Devotional",
     ["&ldquo;Let no one despise you for your youth&rdquo; &mdash; that&rsquo;s not a permission slip, "
      "it&rsquo;s a commission. Paul isn&rsquo;t telling Timothy he&rsquo;s too young; he&rsquo;s telling him the world "
      "will be looking for a reason to dismiss him, and the best answer is a life.",
      "A phenomenal generation isn&rsquo;t louder or flashier than the one before it. It&rsquo;s a "
      "generation that sets the example &mdash; in speech, in conduct, in love, in faith, in purity. "
      "The example, not the argument, is what gets people asking questions.",
      "So this week, don&rsquo;t defend your faith &mdash; display it. Let your cell, your campus and your "
      "timeline make the claim. The generation on fire is the generation that shows up first."]),
    ("KIZAZI 2026: two days that shook us",
     "18 Aug 2026", "Conference Crew", "CC", 15, "Recap",
     ["14&ndash;15 August. Two days. One generation refusing to sit down. "
      "We don&rsquo;t have a highlight film ready yet, but we have the photos &mdash; and if you "
      "weren&rsquo;t there, the gallery is the closest thing to the feeling.",
      "There was worship that went past sound-check, prayers that went past the hour, "
      "and a Word that landed harder than any sermon should. Students crossed borders "
      "to be in the room, and the room was still not big enough.",
      "If you missed it: the next flagship is already being built. Keep your eyes on "
      "our socials &mdash; Conference 2027 dates are coming, and this time, be in it."]),
    ("Staying rooted between the Fridays: 5 habits",
     "5 Sep 2026", "Discipleship Cells", "DC", 16, "Practical",
     ["Fridays are the heartbeat, but faith lives in the four days between. Here are the "
      "five habits we keep preaching in the cells &mdash; because consistency is the culture.",
      "1) Five verses before five minutes of scrolling. 2) One prayer you can actually "
      "finish saying out loud. 3) One person in your cell you check on before the weekend. "
      "4) One honest question you&rsquo;re not afraid to bring next Friday. 5) One act of care "
      "no one asked for &mdash; sent, done, unposted.",
      "None of these are big. That&rsquo;s the point. Rooted doesn&rsquo;t grow by leaps &mdash; "
      "it grows by never missing."]),
]

# Serving teams (ROLES, not named people) — (initials, name, desc, ministry)
TEAMS = [
    ("WS", "Worship &amp; Sound", "Leads the band, the keys and the sound board.", "Worship &amp; The Word"),
    ("WW", "Word &amp; Teaching Team", "Preps and delivers Word nights and Friday messages.", "Worship &amp; The Word"),
    ("PW", "Prayer Watch", "Intercedes before every gathering and for the nation.", "Prayer &amp; Intercession"),
    ("DM", "Discipleship Mentors", "Walks with small groups through the Rooted journey.", "Discipleship Cells"),
    ("CM", "Media &amp; Creative Crew", "Captures, designs and publishes the KIZAZI story.", "Creative &amp; Media Lab"),
    ("OM", "Outreach &amp; Missions Team", "Runs campus visits, school tours and Serve East Africa trips.", "Outreach &amp; Missions"),
    ("SH", "Service &amp; Hospitality", "Reception, refreshments, welcome &mdash; the family&rsquo;s front door.", "Community &amp; Care"),
    ("MC", "Mentorship &amp; Career Crew", "Matches students with mentors for school, work and purpose.", "Mentorship &amp; Career"),
]

# Testimonies — initial-only, illustrative (see NOTES.md). (initials, label, quote)
TESTIMONIALS = [
    ("K.", "Joined online, Kampala",
     "I opened the Friday link as a joke &mdash; I was half an hour from anywhere. "
     "A year later I&rsquo;ve stopped joking. That cell is the first reason I passed my first year."),
    ("A.", "Campus Ambassador",
     "My campus didn&rsquo;t have a Christian club, let alone a fire. Now I get to say: "
     "you&rsquo;re not crazy, there&rsquo;s a generation, and it meets on Fridays."),
    ("M.", "Rooted graduate",
     "Twelve weeks of &lsquo;what do you actually believe?&rsquo; &mdash; and I finally stopped faking "
     "my faith and started learning it. Nobody in my family has prayed with me like my cell has."),
    ("T.", "First-year student",
     "I moved 2,000 km for university and was done for. Someone from Community &amp; Care "
     "showed up with food and prayers in my second week. I still can&rsquo;t explain that. But I believe it."),
]
