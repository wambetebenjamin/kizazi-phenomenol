#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KIZAZI Phenomenal, shared build data & site chrome (BabyCare-template edition).

The site is a faithful BabyCare (HTML Codex) build: same markup structure, same
fonts (Fredoka + Montserrat), same palette shape, wearing the street
celebration skin (stamp red #E63946, leaf green #16A34A, sunshine yellow
#FACC15, paper #FAF7F0, ink black #0A0A0A, swapped in the template's own
css/bootstrap.min.css).  This module holds everything the pages
share:

  * external links (registration form, Friday Meet, socials)
  * the 42 "KIZAZI 2026" photos, vendored in img/gallery/01.jpg … 42.jpg
    (Drive file IDs kept in PHOTOS as the refresh registry: see
    tools/fetch_gallery_photos.py)
  * the Drive video list (easy to fill, see VIDEOS below)
  * shared chrome: head / spinner / topbar+navbar / search modal / page-header /
    footer / copyright / back-to-top / scripts
  * content data: ministries, programs, events, blog, teams, testimonies

`tools/build.py` imports this module and composes the per-page bodies.
Edit the data below, then run:  python3 tools/build.py
"""

import html as _html
import os as _os
import re as _re

_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))

# ------------------------------------------------------------- external links
REG_URL = "https://forms.gle/vzRJrigBHCNormVA9"
MEET_URL = "https://meet.google.com/mcr-fupc-buw"
TIKTOK_URL = "https://www.tiktok.com/@kizazi.phenomenal"
INSTAGRAM_URL = "https://www.instagram.com/kizazi_phenomenal"
FACEBOOK_URL = "https://www.facebook.com/kizaziphenomenal"
LINKTREE_NOTE = "Linktree coming soon"

# Paste the shared Drive folder link here (optional). When set, the site shows
# an "Open the Drive album" button next to the gallery / watch sections.
DRIVE_ALBUM_URL = ""   # e.g. "https://drive.google.com/drive/folders/XXXXXXXX"

SITE = {
    "name": "KIZAZI Phenomenal",
    "tagline": "A generation on fire for God.",
    "verse_ref": "1 Timothy 4:12",
    "verse": ("Let no one despise you for your youth, but set the example "
              "for the believers in speech, in conduct, in love, in faith, in purity."),
    "countries": "Kenya &bull; Uganda &bull; Tanzania &bull; Rwanda",
}

# ------------------------------------------------------------- ticker phrases
# The marquee strip that runs under the navbar on every page (chrome, see
# ticker()). KIZAZI voice: short lines, second person, verbs first, and no
# dashes (see NOTES.md). Edit freely; the strip loops seamlessly.
TICKER = [
    "Worship that moves",
    "Prayer that covers",
    "The Word, taught plainly",
    "Fellowship that carries you",
    "Join this Friday, 8:00 PM EAT",
    "Meet your cell near you",
    "Register free in two minutes",
    "Set the example",
    "A generation on fire for God",
]

# Nav: main items in this order; gallery/blog/team/testimonial live under "Pages".
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
DROPDOWN_KEYS = ("gallery", "blog", "team", "testimonial")

# ------------------------------------------- "KIZAZI 2026" photos (vendored)
# The photos are vendored in img/gallery/01.jpg … 42.jpg (01.jpg == PHOTOS[0]).
# The Google Drive file IDs below are the refresh registry: re-download with
#   python3 tools/fetch_gallery_photos.py
# after editing this list.
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

# Gallery filter categories, assigned round-robin (see NOTES.md).
GALLERY_CATS = [
    ("worship", "Worship"),
    ("word", "Word"),
    ("community", "Community"),
    ("service", "Service"),
    ("creative", "Creative"),
    ("bts", "Behind the Scenes"),
]

FOOTER_GRID = [28, 29, 30, 31, 32, 33]
HERO_PHOTO = 0            # index into PHOTOS (hero fallback; see HERO_SLIDES)
PAGE_HEADER_PHOTO = 1     # default inner-page header background
ABOUT_PHOTO = 2           # the "video" panel behind the play button
FOOTER_PHOTO = 3

# ------------------------------------------------------------ Drive videos ---
# Add your films here. Each entry is a tuple:
#   (drive_id_or_share_url, "Title", "One-line caption", poster_photo_index, tag)
# Both bare file IDs and pasted share links work, e.g.
#   ("1AbCdEf...", "KIZAZI 2026 highlight reel", "Two days, one family.", 10, "Highlights")
#   ("https://drive.google.com/file/d/1AbCdEf.../view", ... )
# Videos are embedded with Google Drive's player (file must be shared publicly).
VIDEOS = [
    # ("FILE_ID", "KIZAZI 2026: Highlight Film", "Two days that shook us.", 10, "Highlights"),
]

_DRIVE_ID_RE = _re.compile(r"[-\w]{20,}")


def drive_id(value):
    """Accept a bare Drive file ID or a pasted share/view link; return the ID."""
    value = (value or "").strip()
    if not value:
        return ""
    m = _re.search(r"/file/d/([-\w]+)", value) or _re.search(r"[?&]id=([-\w]+)", value)
    if m:
        return m.group(1)
    if _DRIVE_ID_RE.fullmatch(value):
        return value
    m = _DRIVE_ID_RE.search(value)
    return m.group(0) if m else value


def video_embed(vid):
    return "https://drive.google.com/file/d/%s/preview" % drive_id(vid)


def videos():
    """Normalised video list: dicts with id, embed, title, desc, poster, tag."""
    out = []
    for n, item in enumerate(VIDEOS):
        src, title, desc, poster, tag = item
        out.append(dict(id=drive_id(src), embed=video_embed(src), title=title,
                        desc=desc, poster=poster, tag=tag, n=n + 1))
    return out


def photo_file(i):
    """Vendored file for PHOTOS[i]: img/gallery/01.jpg up to 42.jpg (w1600 quality)."""
    return "img/gallery/%02d.jpg" % (i + 1)


def durl(i, w=1600):
    """Local full-quality photo (lightbox target). `w` kept for call compatibility."""
    return photo_file(i)


def img(i, alt="", cls="", w=1600, extra=""):
    """<img> pointing at the vendored file in img/gallery/ (alt + lazy kept)."""
    return ('<img src="%s" class="%s" alt="%s" loading="lazy"%s>'
            % (photo_file(i), cls, _html.escape(alt), (" " + extra) if extra else ""))


def bg(i, w=1600):
    """Inline style attr feeding a local photo to a CSS background via --kz-photo
    (consumed as `background-image: …, var(--kz-photo)` in css/kizazi.css)."""
    return "style=\"--kz-photo: url('%s');\"" % photo_file(i)


def bg_file(path):
    """Same as bg() but for a photo outside the PHOTOS registry (e.g. img/hero/)."""
    return "style=\"--kz-photo: url('%s');\"" % path


def gallery_cat(i):
    key, label = GALLERY_CATS[i % len(GALLERY_CATS)]
    return key, label


# ------------------------------------------------ home hero "transition" pics --
# The four photos uploaded on 2026-09-21 for "the top of the first page".
# index.html crossfades between them behind the hero copy; HERO_SLIDE_BG is the
# still frame used when animations are off (prefers-reduced-motion) and the
# fallback painted through --kz-photo.
HERO_SLIDES = [
    "img/hero/01.jpg",   # the family together, outdoors
    "img/hero/02.jpg",   # standing room, hands joined
    "img/hero/03.jpg",   # praying over one another
    "img/hero/04.jpg",   # the embrace
]
HERO_SLIDE_BG = HERO_SLIDES[0]

# ------------------------------------------------------ family description ---
# Exact copy supplied 2026-09-21. The asterisk in the brief marks emphasis, so
# "Ministers' Kids" is italic in FAMILY_DESC_HTML while FAMILY_DESC stays the
# plain-text form (what the bare text of a page reads).
FAMILY_DESC = ("We are on a mission to grow stronger, connect deeper, and shine "
               "brighter as Ministers' Kids")
FAMILY_DESC_HTML = ("We are on a mission to grow stronger, connect deeper, and shine "
                    "brighter as <em>Ministers' Kids</em>")
FAMILY_WHO = "We are Ministers' Kids."

# ---------------------------------------------------------- portraits/people ---
# Named people: the admin team and the Patron. Portraits are vendored in
# img/team/<slug>.jpg and consent to publish is logged in NOTES.md. Roles stay
# "Admin" or "Patron" only (no invented titles). `photo` wins over any gallery
# index so an entry can be added the moment its JPEG lands in img/team/.
PEOPLE = [
    # dict(name="Full Name", role="Admin", photo="img/team/full-name.jpg",
    #      line="One short line about what they carry.", team="Ministry name"),
]
PATRON = dict(
    name="Reverend Dr. Joslyn Isigi",
    role="Patron",
    photo="img/team/reverend-dr-joslyn-isigi.jpg",
    line="",
)


def people():
    """Portrait entries that actually exist on disk (safe to render)."""
    out = []
    for p in PEOPLE:
        if p.get("photo") and _os.path.exists(_os.path.join(_ROOT, p["photo"])):
            out.append(p)
    return out


def patron():
    """The Patron entry, or None while the portrait is not in img/team/."""
    if PATRON.get("photo") and _os.path.exists(_os.path.join(_ROOT, PATRON["photo"])):
        return PATRON
    return None


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
        <meta content="#0A0A0A" name="theme-color">
        <meta property="og:site_name" content="KIZAZI Phenomenal">
        <meta property="og:title" content="%(title)s">
        <meta property="og:description" content="%(desc)s">
        <meta property="og:type" content="website">
        <meta property="og:image" content="img/brand/logo-mark.png">

        <link rel="icon" type="image/png" href="img/brand/logo-mark.png">
        <link rel="apple-touch-icon" href="img/brand/logo-mark.png">

        <!-- Google Web Fonts -->
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@600;700&family=Montserrat:wght@200;400;600&display=swap" rel="stylesheet">

        <!-- Icon Font Stylesheet -->
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css"/>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css" rel="stylesheet">

        <!-- Libraries Stylesheet -->
        <link href="lib/animate/animate.min.css" rel="stylesheet">
        <link href="lib/lightbox/css/lightbox.min.css" rel="stylesheet">
        <link href="lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">

        <!-- Customized Bootstrap Stylesheet -->
        <link href="css/bootstrap.min.css" rel="stylesheet">

        <!-- Template Stylesheet -->
        <link href="css/style.css" rel="stylesheet">

        <!-- KIZAZI add-ons (gallery photos, video cards, filter & search) -->
        <link href="css/kizazi.css" rel="stylesheet">
    </head>
""" % {"title": _html.escape(title), "desc": _html.escape(desc)}


def body_open():
    return "    <body>\n"


def spinner():
    return """        <!-- Spinner Start -->
        <div id="spinner" class="show w-100 vh-100 bg-white position-fixed translate-middle top-50 start-50  d-flex align-items-center justify-content-center">
            <div class="spinner-grow text-primary" role="status"></div>
        </div>
        <!-- Spinner End -->
"""


def social_buttons(cls="btn btn-light btn-sm-square rounded-circle", icon_cls="text-secondary"):
    items = [
        (FACEBOOK_URL, "fab fa-facebook-f", "Facebook"),
        (TIKTOK_URL, "fab fa-tiktok", "TikTok"),
        (INSTAGRAM_URL, "fab fa-instagram", "Instagram"),
    ]
    out = []
    for url, icon, label in items:
        out.append('<a href="%s" target="_blank" rel="noopener" class="%s" aria-label="%s" title="%s"><i class="%s %s"></i></a>'
                   % (url, cls, label, label, icon, icon_cls))
    return "\n".join("                                " + o for o in out)


def ticker():
    """Marquee strip under the navbar.

    The phrase set (TICKER) is repeated exactly twice in the DOM so the CSS
    -50% translate loop (section 9 of css/kizazi.css) is seamless. The strip
    is decorative reinforcement of copy that lives on the pages, so it is
    aria-hidden.
    """
    def one_set():
        parts = []
        for phrase in TICKER:
            parts.append('<span class="kz-ticker-item">%s</span>' % _html.escape(phrase))
            parts.append('<span class="kz-ticker-star">&#10022;</span>')
        return "".join(parts)
    set_ = one_set()
    return """        <!-- Ticker Start -->
        <div class="kz-ticker" aria-hidden="true">
            <div class="kz-ticker-track">%s%s</div>
        </div>
        <!-- Ticker End -->
""" % (set_, set_)


def scroll_progress():
    """Fixed gradient progress rule at the very top of the viewport.

    js/kizazi.js drives it with transform: scaleX() only (no layout shift).
    """
    return """        <!-- Scroll progress Start -->
        <div class="kz-progress" aria-hidden="true"><span class="kz-progress-bar"></span></div>
        <!-- Scroll progress End -->
"""


def topbar_navbar(active):
    links = []
    for file_, label, key in PAGES:
        if key in DROPDOWN_KEYS or key == "contact":
            continue
        cls = " active" if key == active else ""
        links.append('                            <a href="%s" class="nav-item nav-link%s">%s</a>'
                     % (file_, cls, label))
    if active in DROPDOWN_KEYS:
        links.append('                            <div class="nav-item dropdown">\n'
                     '                                <a href="#" class="nav-link dropdown-toggle active" data-bs-toggle="dropdown">Pages</a>')
    else:
        links.append('                            <div class="nav-item dropdown">\n'
                     '                                <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">Pages</a>')
    links.append('                                <div class="dropdown-menu m-0 bg-secondary rounded-0">')
    for file_, label, key in PAGES:
        if key not in DROPDOWN_KEYS:
            continue
        links.append('                                    <a href="%s" class="dropdown-item">%s</a>' % (file_, label))
    links.append('                                </div>\n                            </div>')
    for file_, label, key in PAGES:
        if key != "contact":
            continue
        cls = " active" if key == active else ""
        links.append('                            <a href="%s" class="nav-item nav-link%s">%s</a>'
                     % (file_, cls, label))

    return """        <!-- Navbar start -->
        <div class="container-fluid border-bottom bg-light wow fadeIn" data-wow-delay="0.1s">
            <div class="container topbar bg-primary d-none d-lg-block py-2" style="border-radius: 0 40px">
                <div class="d-flex justify-content-between">
                    <div class="top-info ps-2">
                        <small class="me-3"><i class="fas fa-globe-africa me-2 text-secondary"></i> <a href="about.html" class="text-white">Serving East Africa: %(countries)s</a></small>
                        <small class="me-3"><i class="fas fa-video me-2 text-secondary"></i><a href="%(meet)s" target="_blank" rel="noopener" class="text-white">This Friday &middot; Online Catch-Up &middot; 8:00 PM EAT</a></small>
                    </div>
                    <div class="top-link pe-2">
%(socials)s
                    </div>
                </div>
            </div>
            <div class="container px-0">
                <nav class="navbar navbar-light navbar-expand-xl py-3">
                    <a href="index.html" class="navbar-brand"><h1 class="text-primary display-6">KIZAZI <span class="text-secondary">Phenomenal</span></h1></a>
                    <button class="navbar-toggler py-2 px-3" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
                        <span class="fa fa-bars text-primary"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarCollapse">
                        <div class="navbar-nav mx-auto">
%(links)s
                        </div>
                        <div class="d-flex me-4 align-items-center">
                            <div class="d-flex flex-column pe-3 border-end border-primary">
                                <span class="text-primary">New here?</span>
                                <a href="%(reg)s" target="_blank" rel="noopener"><span class="text-secondary">Register free</span></a>
                            </div>
                        </div>
                        <button class="btn-search btn btn-primary btn-md-square rounded-circle" data-bs-toggle="modal" data-bs-target="#searchModal" aria-label="Search the site"><i class="fas fa-search text-white"></i></button>
                    </div>
                </nav>
            </div>
        </div>
        <!-- Navbar End -->

%(ticker)s
        <!-- Modal Search Start -->
        <div class="modal fade" id="searchModal" tabindex="-1" aria-labelledby="searchModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-fullscreen">
                <div class="modal-content rounded-0">
                    <div class="modal-header">
                        <h5 class="modal-title" id="searchModalLabel">Search by keyword</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body d-flex align-items-center">
                        <div class="w-75 mx-auto">
                            <div class="input-group d-flex">
                                <input type="search" id="kz-search-input" class="form-control p-3" placeholder="Try &ldquo;friday&rdquo;, &ldquo;rooted&rdquo;, &ldquo;gallery&rdquo;&hellip;" aria-describedby="search-icon-1">
                                <span id="search-icon-1" class="input-group-text p-3"><i class="fa fa-search"></i></span>
                            </div>
                            <div id="kz-search-results" class="kz-search-results mt-4"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Modal Search End -->
""" % {"countries": SITE["countries"], "meet": MEET_URL, "reg": REG_URL,
       "socials": social_buttons(), "links": "\n".join(links), "ticker": ticker()}


def video_modal():
    return """        <!-- Modal Video -->
        <div class="modal fade" id="videoModal" tabindex="-1" aria-labelledby="videoModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content rounded-0">
                    <div class="modal-header">
                        <h5 class="modal-title" id="videoModalLabel">KIZAZI on film</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <!-- 16:9 aspect ratio -->
                        <div class="ratio ratio-16x9">
                            <iframe class="embed-responsive-item" src="" id="video" allowfullscreen allowscriptaccess="always"
                                allow="autoplay"></iframe>
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""


def page_header(title, sub, photo_i=None):
    i = PAGE_HEADER_PHOTO if photo_i is None else photo_i
    return """        <!-- Page Header Start -->
        <div class="container-fluid page-header py-5 wow fadeIn" data-wow-delay="0.1s" %(bg)s>
            <div class="container text-center py-5">
                <h1 class="display-2 text-white mb-4">%(title)s</h1>
                <p class="text-white-50 mx-auto mb-4" style="max-width: 640px;">%(sub)s</p>
                <nav aria-label="breadcrumb">
                    <ol class="breadcrumb justify-content-center mb-0">
                        <li class="breadcrumb-item"><a href="index.html">Home</a></li>
                        <li class="breadcrumb-item text-white" aria-current="page">%(title)s</li>
                    </ol>
                </nav>
            </div>
        </div>
        <!-- Page Header End -->
""" % {"title": _html.escape(title), "sub": sub, "bg": bg(i)}


def section_head(kicker, title, sub=""):
    sub_html = ("<p class=\"text-body mt-3 mb-0\">%s</p>" % sub) if sub else ""
    return """                <div class="mx-auto text-center wow fadeIn" data-wow-delay="0.1s" style="max-width: 700px;">
                    <h4 class="text-primary mb-4 border-bottom border-primary border-2 d-inline-block p-2 title-border-radius">%s</h4>
                    <h1 class="mb-5 display-3">%s</h1>%s
                </div>
""" % (kicker, title, sub_html)


def footer():
    grid = []
    for i in FOOTER_GRID:
        grid.append("""                                <div class="col-4">
                                    <div class="footer-galary-img rounded-circle border border-primary">
                                        <a href="gallery.html" title="Open the gallery">%s</a>
                                    </div>
                                </div>""" % img(i, "KIZAZI 2026 photo", cls="img-fluid rounded-circle p-2", w=400))
    return """        <!-- Footer Start -->
        <div class="container-fluid footer py-5 wow fadeIn" data-wow-delay="0.1s" %(bg)s>
            <div class="container py-5">
                <div class="row g-5">
                    <div class="col-md-6 col-lg-4 col-xl-3">
                        <div class="footer-item">
                            <h2 class="fw-bold mb-3"><span class="text-primary mb-0">KIZAZI</span> <span class="text-secondary">Phenomenal</span></h2>
                            <p class="mb-4">%(tagline)s A Christian youth movement across %(countries)s: worship that moves, discipleship that sticks, a family that carries you. We are on a mission to grow stronger, connect deeper, and shine brighter as <em>Ministers' Kids</em>.</p>
                            <p class="text-dark fst-italic mb-4">&ldquo;%(verse_short)s&hellip;&rdquo; &middot; %(verse_ref)s</p>
                            <div class="border border-primary p-3 rounded bg-light">
                                <h5 class="mb-3">Newsletter</h5>
                                <form class="kz-newsletter position-relative mx-auto border border-primary rounded" style="max-width: 400px;" novalidate>
                                    <input class="form-control border-0 w-100 py-3 ps-4 pe-5" type="email" placeholder="Your email" aria-label="Your email" required>
                                    <button type="submit" class="btn btn-primary py-2 position-absolute top-0 end-0 mt-2 me-2 text-white">SignUp</button>
                                </form>
                                <p class="kz-newsletter-note mb-0 mt-2 small text-muted">Announcements only. Nothing is stored or shared.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4 col-xl-3">
                        <div class="footer-item">
                            <div class="d-flex flex-column p-4 ps-5 text-dark border border-primary"
                            style="border-radius: 50%% 20%% / 10%% 40%%;">
                                <p><strong>Friday:</strong> Online Catch-Up, 8:00 PM EAT</p>
                                <p><strong>Next Friday:</strong> <span data-next-friday-long>&hellip;</span></p>
                                <p><strong>Weekdays:</strong> cells, prayer &amp; campus visits</p>
                                <p><strong>Join live:</strong> <a href="%(meet)s" target="_blank" rel="noopener">Google Meet</a></p>
                                <p class="mb-0"><strong>Register:</strong> <a href="%(reg)s" target="_blank" rel="noopener">free form</a></p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4 col-xl-3">
                        <div class="footer-item">
                            <h4 class="text-primary mb-4 border-bottom border-primary border-2 d-inline-block p-2 title-border-radius">EXPLORE</h4>
                            <div class="d-flex flex-column align-items-start">
%(links)s
                                <div class="footer-icon d-flex mt-2">
%(socials)s
                                </div>
                                <p class="small text-muted mt-3 mb-0"><i class="fas fa-link me-1"></i> %(linktree)s: one link for everything.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-4 col-xl-3">
                        <div class="footer-item">
                            <h4 class="text-primary mb-4 border-bottom border-primary border-2 d-inline-block p-2 title-border-radius">KIZAZI 2026 IN PICS</h4>
                            <div class="row g-3">
%(grid)s
                            </div>
                            <a class="btn btn-primary btn-sm px-4 py-2 mt-3 text-white btn-border-radius" href="gallery.html">Full gallery</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Footer End -->


        <!-- Copyright Start -->
        <div class="container-fluid copyright bg-dark py-4">
            <div class="container">
                <div class="row">
                    <div class="col-md-6 text-center text-md-start mb-3 mb-md-0">
                        <span class="text-light"><a href="index.html" class="text-light"><i class="fas fa-copyright text-light me-2"></i>KIZAZI Phenomenal</a>, All right reserved.</span>
                    </div>
                    <div class="col-md-6 my-auto text-center text-md-end text-white">
                        %(tagline)s %(verse_ref)s
                    </div>
                </div>
            </div>
        </div>
        <!-- Copyright End -->
""" % {"bg": bg(FOOTER_PHOTO, 1200), "tagline": SITE["tagline"],
       "countries": SITE["countries"], "verse_short": SITE["verse"][:70],
       "verse_ref": SITE["verse_ref"], "meet": MEET_URL, "reg": REG_URL,
       "linktree": LINKTREE_NOTE,
       "links": "\n".join(
           '                                <a href="%s" class="text-body mb-3"><i class="fa fa-angle-double-right text-primary me-2"></i>%s</a>'
           % (f_, l_) for f_, l_, _ in PAGES),
       "socials": social_buttons(cls="btn btn-primary btn-sm-square me-3 rounded-circle text-white", icon_cls=""),
       "grid": "\n".join(grid)}


def back_to_top():
    return """        <!-- Back to Top -->
        <a href="#" class="btn btn-primary border-3 border-primary rounded-circle back-to-top" aria-label="Back to top"><i class="fa fa-arrow-up"></i></a>
"""


def scripts():
    return """    <!-- JavaScript Libraries -->
    <script src="js/vendor/jquery.min.js"></script>
    <script src="js/vendor/bootstrap.bundle.min.js"></script>
    <script src="lib/wow/wow.min.js"></script>
    <script src="lib/easing/easing.min.js"></script>
    <script src="lib/waypoints/waypoints.min.js"></script>
    <script src="lib/lightbox/js/lightbox.min.js"></script>
    <script src="lib/owlcarousel/owl.carousel.min.js"></script>

    <!-- Template Javascript -->
    <script src="js/main.js"></script>

    <!-- KIZAZI: next-Friday dates, gallery filter, search, newsletter note -->
    <script src="js/kizazi.js"></script>
    </body>

</html>
"""


# -------------------------------------------------------------- content data ---
# 8 ministries: (slug, icon, name, blurb, detail, [what to expect])
MINISTRIES = [
    ("worship-word", "fa-music", "Worship &amp; The Word",
     "Songs that move and messages that stick.",
     "Worship that gets you on your feet, and the Word taught without fluff. "
     "This is the heartbeat of KIZAZI: everything else flows from time with God.",
     ["Friday catch-ups with live worship &amp; teaching", "Worship &amp; Word Nights through the term", "Worshipper and teacher tracks if you want to lead"]),
    ("cells", "fa-users", "Discipleship Cells",
     "Small groups where nobody fakes it.",
     "Real discipleship happens in small rooms. Our cells meet around the Word, "
     "ask hard questions and carry each other through exams, home and everything between.",
     ["Weekly cell meetings (online + in person)", "The 12-week Rooted journey", "Accountability that actually shows up"]),
    ("prayer", "fa-hands-praying", "Prayer &amp; Intercession",
     "The room where heaven gets serious.",
     "We believe prayer changes the atmosphere of a generation. A constant watch "
     "intercedes for East Africa, for our campuses and for the family, before and between every gathering.",
     ["Prayer before every event, join in", "Rotating intercession teams", "National &amp; campus prayer lists shared weekly"]),
    ("friday", "fa-video", "Friday Online Catch-Up",
     "Every Friday, 8:00 PM EAT. Same time, different fire.",
     "Our weekly online gathering: worship, a Word bite, prayers and connection "
     "across Kenya, Uganda, Tanzania and Rwanda. One link, whole family.",
     ["Live on Google Meet, 8:00 PM EAT", "Worship, teaching and prayer every week", "Open to everyone, no registration needed to join in"]),
    ("outreach", "fa-globe-africa", "Outreach &amp; Missions",
     "A generation that can&rsquo;t stay home.",
     "Campus visits, school tours and Serve East Africa trips: we take the "
     "gospel and the gospel&rsquo;s hands-on love to campuses, communities and borders.",
     ["Campus &amp; school tours each term", "Serve East Africa cross-border trips", "Outreach teams that plan and fundraise together"]),
    ("creative", "fa-pen-nib", "Creative &amp; Media Lab",
     "Where the KIZAZI story gets made.",
     "Design, video, socials, set and stage: our lab turns worship into something "
     "the generation can see, feel and share. Every album shot you see was made here.",
     ["Monthly creative workshops", "Media crew for every event", "Publishing across TikTok, Instagram &amp; Facebook"]),
    ("mentorship", "fa-graduation-cap", "Mentorship &amp; Career",
     "Someone older, on your side.",
     "Students matched with mentors for school, work, vocation and purpose. "
     "Career clinics, CV nights, application sprints and honest conversations about the future.",
     ["1-on-1 and small-group mentoring", "Career clinics &amp; CV nights in term", "Scholarship and application support"]),
    ("care", "fa-heart", "Community &amp; Care",
     "Family means nobody carries it alone.",
     "Birthdays, hospital visits, grief, homesickness: care is a ministry. "
     "Hospitality at every event, check-ins through the week, and a family that notices.",
     ["Hospitality &amp; reception at events", "Weekly check-ins in the cells", "Care funds for families in crisis"]),
]

# 6 programs: (name, rate badge, photo_i, desc, leader, leader initials, when, where, sits/lessons/hours-style meta)
PROGRAMS = [
    ("Rooted", "Free &middot; 12 weeks", 4,
     "A 12-week discipleship journey through the basics that don&rsquo;t get skipped: "
     "who God is, how to hear from Him, how to pray, how to live on purpose.",
     "Discipleship Cells", "DC", "New intake each term", "Online + in person",
     ("30 seats", "12 weeks", "3 sessions / wk")),
    ("Phenomenal Fridays", "Weekly", 5,
     "The heartbeat: worship, a Word bite, prayer and connection, live every "
     "Friday at 8:00 PM EAT on Google Meet, across East Africa.",
     "Worship &amp; The Word", "WW", "Every Friday", "Google Meet",
     ("Open to all", "8:00 PM EAT", "60 minutes")),
    ("KIZAZI Creative Lab", "Term intake", 6,
     "Worship, design, video and media workshops for the makers: learn to build "
     "what the movement puts in front of the generation.",
     "Creative &amp; Media Lab", "CM", "Monthly sessions", "Studio + online",
     ("20 seats", "6 modules", "1 project / mo")),
    ("Mentorship Circle", "Applications open", 7,
     "Get matched with a mentor for school, career and purpose. Small circles, "
     "regular check-ins, real accountability.",
     "Mentorship &amp; Career", "MC", "Ongoing", "1-on-1 + small group",
     ("1-on-1", "Bi-weekly", "All year")),
    ("Campus Ambassadors", "Recruiting now", 8,
     "Plant and lead KIZAZI on your campus: toolkits, training and a network of "
     "ambassadors across East African universities.",
     "Outreach &amp; Missions", "OM", "During term", "Your campus",
     ("4 nations", "1 toolkit", "Termly meet")),
    ("Serve East Africa", "Next trip TBA", 9,
     "Annual cross-border outreach trips across Kenya, Uganda, Tanzania and Rwanda. "
     "Train, raise, go, report.",
     "Community &amp; Care", "CC", "Annual trips", "KE &middot; UG &middot; TZ &middot; RW",
     ("1 team", "1 border", "1 mission")),
]

# 4 events: dict(title, tag, photo_i, desc, when, time, place, cta_label, cta_url, date_mode)
EVENTS = [
    dict(title="Phenomenal Friday: Online Catch-Up", tag="Weekly", photo=10,
         desc="Worship, a Word bite, prayer and connection, live from across East Africa.",
         when="friday", time="8:00 PM EAT", place="Google Meet",
         cta_label="Join Live", cta_url=MEET_URL),
    dict(title="KIZAZI Conference 2027", tag="2027 Flagship", photo=11,
         desc="The next flagship. Two days of worship, word and fire. Details as they drop.",
         when="Aug 2027", time="Full-day", place="East Africa",
         cta_label="Get Notified", cta_url=REG_URL),
    dict(title="Worship &amp; Word Night", tag="Monthly", photo=12,
         desc="One night a month we gather in person: deeper worship, uncut Word.",
         when="Monthly", time="Evening", place="In person + stream",
         cta_label="Follow for the Date", cta_url=INSTAGRAM_URL),
    dict(title="Campus &amp; School Tour", tag="Termly", photo=13,
         desc="We bring the catch-up to campuses and schools across the region. Invite us to yours.",
         when="Each term", time="Flexible", place="Your campus",
         cta_label="Host Us", cta_url=REG_URL),
]

# Blog: (title, date, team, team initials, photo_i, tag, body paragraphs)
BLOG = [
    ("What it means to be a &ldquo;phenomenal&rdquo; generation",
     "12 Aug 2026", "Media &amp; Creative Crew", "CM", 14, "Devotional",
     ["&ldquo;Let no one despise you for your youth&rdquo;. That&rsquo;s not a permission slip, "
      "it&rsquo;s a commission. Paul isn&rsquo;t telling Timothy he&rsquo;s too young; he&rsquo;s telling him the world "
      "will be looking for a reason to dismiss him, and the best answer is a life.",
      "A phenomenal generation isn&rsquo;t louder or flashier than the one before it. It&rsquo;s a "
      "generation that sets the example: in speech, in conduct, in love, in faith, in purity. "
      "The example, not the argument, is what gets people asking questions.",
      "So this week, don&rsquo;t defend your faith, display it. Let your cell, your campus and your "
      "timeline make the claim. The generation on fire is the generation that shows up first."]),
    ("KIZAZI 2026: two days that shook us",
     "18 Aug 2026", "Conference Crew", "CC", 15, "Recap",
     ["14 to 15 August. Two days. One generation refusing to sit down. "
      "We don&rsquo;t have a highlight film ready yet, but we have the photos. If you "
      "weren&rsquo;t there, the gallery is the closest thing to the feeling.",
      "There was worship that went past sound-check, prayers that went past the hour, "
      "and a Word that landed harder than any sermon should. Students crossed borders "
      "to be in the room, and the room was still not big enough.",
      "If you missed it: the next flagship is already being built. Keep your eyes on "
      "our socials. Conference 2027 dates are coming, and this time, be in it."]),
    ("Staying rooted between the Fridays: 5 habits",
     "5 Sep 2026", "Discipleship Cells", "DC", 16, "Practical",
     ["Fridays are the heartbeat, but faith lives in the four days between. Here are the "
      "five habits we keep preaching in the cells, because consistency is the culture.",
      "1) Five verses before five minutes of scrolling. 2) One prayer you can actually "
      "finish saying out loud. 3) One person in your cell you check on before the weekend. "
      "4) One honest question you&rsquo;re not afraid to bring next Friday. 5) One act of care "
      "no one asked for: sent, done, unposted.",
      "None of these are big. That&rsquo;s the point. Rooted doesn&rsquo;t grow by leaps; "
      "it grows by never missing."]),
]

# Serving teams (ROLES, not named people): (initials, name, desc, ministry, photo_i)
TEAMS = [
    ("WS", "Worship &amp; Sound", "Leads the band, the keys and the sound board.", "Worship &amp; The Word", 17),
    ("WW", "Word &amp; Teaching Team", "Preps and delivers Word nights and Friday messages.", "Worship &amp; The Word", 18),
    ("PW", "Prayer Watch", "Intercedes before every gathering and for the nation.", "Prayer &amp; Intercession", 19),
    ("DM", "Discipleship Mentors", "Walks with small groups through the Rooted journey.", "Discipleship Cells", 20),
    ("CM", "Media &amp; Creative Crew", "Captures, designs and publishes the KIZAZI story.", "Creative &amp; Media Lab", 21),
    ("OM", "Outreach &amp; Missions Team", "Runs campus visits, school tours and Serve East Africa trips.", "Outreach &amp; Missions", 22),
    ("SH", "Service &amp; Hospitality", "Reception, refreshments, welcome: the family&rsquo;s front door.", "Community &amp; Care", 23),
    ("MC", "Mentorship &amp; Career Crew", "Matches students with mentors for school, work and purpose.", "Mentorship &amp; Career", 24),
]

# Testimonies: initial-only, illustrative (see NOTES.md). (initials, label, quote)
TESTIMONIALS = [
    ("K.", "Joined online, Kampala",
     "I opened the Friday link as a joke. I was half an hour from anywhere. "
     "A year later I&rsquo;ve stopped joking. That cell is the first reason I passed my first year."),
    ("A.", "Campus Ambassador",
     "My campus didn&rsquo;t have a Christian club, let alone a fire. Now I get to say: "
     "you&rsquo;re not crazy, there&rsquo;s a generation, and it meets on Fridays."),
    ("M.", "Rooted graduate",
     "Twelve weeks of &lsquo;what do you actually believe?&rsquo;, and I finally stopped faking "
     "my faith and started learning it. Nobody in my family has prayed with me like my cell has."),
    ("T.", "First-year student",
     "I moved 2,000 km for university and was done for. Someone from Community &amp; Care "
     "showed up with food and prayers in my second week. I still can&rsquo;t explain that. But I believe it."),
]
