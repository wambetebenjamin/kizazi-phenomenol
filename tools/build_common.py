#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KIZAZI Phenomenal — static site builder.

Composes the shared chrome (head / topbar / navbar / footer / scripts) with
per-page bodies and writes every page to the repository root.

Usage:  python3 tools/build.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- links ----
REG_URL = "https://forms.gle/vzRJrigBHCNormVA9"
MEET_URL = "https://meet.google.com/mcr-fupc-buw"
TIKTOK = "https://www.tiktok.com/@kizazi.phenomenal"
INSTAGRAM = "https://www.instagram.com/kizazi_phenomenal"
FACEBOOK = "https://www.facebook.com/kizaziphenomenal"

# ------------------------------------------------- Drive photo registry ----
# Photos from the shared "KIZAZI 2026" Google Drive folder (public).
PHOTOS = [
    "1w2oIGh9BBn2tXBDsNy8CvpZQywT6Qceh", "13BJwgGhr6XDHC9h13ByCXUag3ViLt4pK",
    "123Sg1hwdaWtmPDX9Qb6ePdTY8hzg04vV", "16r29HQUQrjocav3vAQa8T_Oun9K5lips",
    "138YqINm17FRZL1_guRj83Am0GF9QRV-n", "1N8Y4GFV3USaz65XVOQLyW-uUqNxxcyFC",
    "1lsHDY2-8zHeowao8Rs78H3ZgZaLh8672", "1A3iWtP0uMt94OvJVoQjdkR2I6kI9_41w",
    "1r53IGVmSRyDSz9Xx9Wysnz8V_wQ20OAF", "1k8-cGrV3hBe_bwbYc4_1MTg33q_pUsl0",
    "1zsNvbbpcajqQzaxU1f-9Ja-ZxCNxto7J", "1Pm8zA9AMZ5wNA_1XEdu9eOIPeKT0dhf5",
    "1J5BDRLvnpFOIA0JKbn5MviwyAEQhBaEn", "1NCK66Nzrr546lp8AJ8STAC5xSa-cIJpH",
    "1CTKDKQKLMM9d3GpFd2x6o_h4zNUTZmsD", "10dj_djGdcTMdxexY8rUn70k_hNgxZtVL",
    "1JuDHk07-EF-I6Kx11CJmPBtYuOl1eq9l", "1R9jm7BWDV-W22ASIHvRY_idhTjRFFIB3",
    "11q6L_hiO0Y9Ta_Fsfq4qp5mPjluvtAxd", "1o2flLyDHec9o19S6sC9sduj87e5YBr8a",
    "1dTi97bdexjjR-mlTQj50dEK2s39ZqT2U", "1KaN84BydKGM5gLShYPGwn_gg9lPyRmzh",
    "18VifyAxl_4l920PrnaGl07SSti9f8Q_e", "1YL9wWv2xYSE0fdrGLCFTA3CmlO9Q5E5D",
    "1xC3xzAePVgOzjyMOVLttJDPhrOEEoCUx", "1QbiJygQMAOB_4YWeMw_2s7mKgbc3xqR2",
    "1qFNX35z-KnZgpw0dmnXRRQcVK70uE-wt", "1lu1CakILnn5Ar6-JLSs3W8zjd6fALEme",
    "1TyHtNtLIsNm7hiN9xLLR6EzNoUZ8Lakh", "1MVKVbCyOOSxVvCEKzJeASc5SjxO-6fGp",
    "14tH-n17U4UtHupT7SGKQsyBq5yIIO-Wl", "1tOT1KZVRYt9IiCY-FTo1PdEs_PoKBc9C",
    "1XDDP7w7B9kKk6EuOuoZUevgqeRhbrUaR", "1URj0XMQeL1mSIMTPvoih6s1ZaocttXbf",
    "1wFCvoEH6UiTwp1gGOz92pzhrrUkKc2yA", "1t1GqRjKBRas5Qsi9oGqDSrkidRkGXlfN",
    "1kLm0a58babwyW_n4_9A6WZFVvvQywUEo", "1hr49FXlF6QJ0jw1mRAcELocFDytVL_ln",
    "1puPEA7OhRI_hJo7Czqfl-d4tSTQZRiLW", "1FMHYgnn1F8xw7B94PFZmtdudnCZMtomu",
    "1AJIZw6K86hDmgrbOs2ZOPmzLoF3TuWNa", "1m9-cKUNBm1c_DHfF3v9_RmdRP8X4Qq_B",
]


def durl(idx, w=1600):
    """Direct hotlinkable URL for a Drive photo (used by lightbox / anchors)."""
    return "https://drive.google.com/thumbnail?id=%s&sz=w%d" % (PHOTOS[idx], w)


def photo(idx, cls="", alt="", w=1600, extra=""):
    return ('<img data-drive="%s" data-drive-w="%d" class="%s" alt="%s" loading="lazy" %s>'
            % (PHOTOS[idx], w, cls, alt, extra))


# ------------------------------------------------------------ shared bits ----
def head(title, desc):
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>%(title)s</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta content="KIZAZI Phenomenal, youth ministry, East Africa, Christian youth, Jesus, worship, discipleship, Kenya, Uganda, Tanzania, Rwanda" name="keywords">
    <meta content="%(desc)s" name="description">
    <meta property="og:title" content="%(title)s">
    <meta property="og:description" content="%(desc)s">
    <meta property="og:type" content="website">
    <meta property="og:image" content="img/brand/logo-mark.png">
    <link rel="icon" type="image/png" href="img/brand/logo-mark.png">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Caveat:wght@600;700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css"/>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css" rel="stylesheet">

    <link href="lib/animate/animate.min.css" rel="stylesheet">
    <link href="lib/lightbox/css/lightbox.min.css" rel="stylesheet">
    <link href="lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">

    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
    <link href="css/kizazi.css" rel="stylesheet">
</head>
""" % {"title": title, "desc": desc}


def topbar():
    return """        <div class="kz-topbar py-2">
            <div class="container d-none d-lg-flex justify-content-between align-items-center">
                <div class="d-flex align-items-center gap-4">
                    <span><i class="fas fa-globe-africa me-2" style="color:var(--kz-gold)"></i> Serving East Africa &mdash; Kenya &bull; Uganda &bull; Tanzania &bull; Rwanda</span>
                    <a href="%s" target="_blank" rel="noopener" class="kz-live"><span class="dot"></span> Fridays 8:00 PM EAT &mdash; Online Catch-Up</a>
                </div>
                <div class="d-flex align-items-center gap-3">
                    <a href="%s" target="_blank" rel="noopener" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
                    <a href="%s" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                    <a href="%s" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                    <span class="ms-2" style="opacity:.6">Linktree coming soon</span>
                </div>
            </div>
        </div>
""" % (MEET_URL, TIKTOK, INSTAGRAM, FACEBOOK)


NAV = [
    ("index.html", "Home", "home"),
    ("about.html", "About", "about"),
    ("ministries.html", "Ministries", "ministries"),
    ("programs.html", "Programs", "programs"),
    ("events.html", "Events", "events"),
    ("contact.html", "Contact", "contact"),
]
DROPDOWN = [
    ("gallery.html", "Gallery", "gallery"),
    ("blog.html", "Word &amp; Stories", "blog"),
    ("team.html", "Team &amp; Serving", "team"),
    ("testimonial.html", "Testimonies", "testimonial"),
]


def navbar(active):
    links = []
    for href, label, key in NAV:
        cls = " active" if key == active else ""
        links.append('<a href="%s" class="nav-item nav-link%s">%s</a>' % (href, cls, label))
    dd = []
    for href, label, key in DROPDOWN:
        cls = " active" if key == active else ""
        dd.append('<a href="%s" class="dropdown-item%s">%s</a>' % (href, cls, label))
    dd_html = "".join(dd)
    dd_active = " active" if active in [k for _, _, k in DROPDOWN] else ""
    return """        <nav class="navbar navbar-expand-xl kz-navbar sticky-top py-2">
            <div class="container">
                <a href="index.html" class="navbar-brand kz-brand">
                    <img src="img/brand/logo-mark.png" alt="KIZAZI Phenomenal logo">
                    <span class="kz-brand-name">KIZAZI<span>phenomenal</span></span>
                </a>
                <button class="navbar-toggler py-2 px-3" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-label="Toggle navigation">
                    <span class="fa fa-bars" style="color:var(--kz-violet)"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarCollapse">
                    <div class="navbar-nav mx-auto">
                        %(links)s
                        <div class="nav-item dropdown">
                            <a href="#" class="nav-link dropdown-toggle%(dd_active)s" data-bs-toggle="dropdown">More</a>
                            <div class="dropdown-menu m-0 rounded-3 border-0 shadow p-2">%(dd)s</div>
                        </div>
                    </div>
                    <div class="d-flex align-items-center gap-2 mt-3 mt-xl-0">
                        <a href="%(meet)s" target="_blank" rel="noopener" class="btn-kz btn-kz-line btn-sm px-3 py-2"><i class="fas fa-video"></i> Friday Live</a>
                        <a href="%(reg)s" target="_blank" rel="noopener" class="btn-kz btn-sm px-4 py-2">Join Us <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </nav>
""" % {"links": "".join(links), "dd": dd_html, "dd_active": dd_active, "meet": MEET_URL, "reg": REG_URL}


def marquee():
    words = ["Worship", "The Word", "Real Community", "Purpose", "Prayer", "KIZAZI 2026",
             "Creative Arts", "Mentorship", "Outreach", "Friday Catch-Up", "East Africa", "On Fire"]
    spans = "".join("<span>%s <i class='fas fa-fire'></i></span>" % w for w in words)
    return """        <div class="kz-marquee"><div class="kz-marquee-track">%s</div></div>
""" % spans


def footer():
    g = "".join(
        '<div class="col-4"><a href="%s" data-lightbox="footer-gal" class="d-block kz-photo" style="border-radius:14px">%s</a></div>'
        % (durl(i, 1200), photo(i, "", "KIZAZI moment", w=400))
        for i in range(18, 24))
    return """        <footer class="kz-footer pt-5 mt-5">
            <div class="container py-5">
                <div class="row g-5">
                    <div class="col-md-6 col-lg-4">
                        <a href="index.html" class="kz-brand mb-3 d-inline-flex">
                            <img src="img/brand/logo-mark.png" alt="KIZAZI Phenomenal logo" style="width:52px;height:52px">
                            <span class="kz-brand-name" style="color:#fff">KIZAZI<span>phenomenal</span></span>
                        </a>
                        <p class="mb-4">A movement of young people across East Africa who have met Jesus and refuse to be ordinary. We gather, we worship, we grow, we serve &mdash; together.</p>
                        <div class="kz-social d-flex gap-2">
                            <a href="%s" target="_blank" rel="noopener" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
                            <a href="%s" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                            <a href="%s" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                            <a href="%s" target="_blank" rel="noopener" aria-label="Friday online catch-up"><i class="fas fa-video"></i></a>
                            <a href="%s" target="_blank" rel="noopener" aria-label="Register"><i class="fas fa-user-plus"></i></a>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-2">
                        <h4 class="mb-4 h5">Explore</h4>
                        <div class="d-flex flex-column gap-2">
                            <a href="about.html">About Us</a>
                            <a href="ministries.html">Ministries</a>
                            <a href="programs.html">Programs</a>
                            <a href="events.html">Events</a>
                            <a href="gallery.html">Gallery</a>
                            <a href="blog.html">Word &amp; Stories</a>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-3">
                        <h4 class="mb-4 h5">Gather With Us</h4>
                        <div class="d-flex flex-column gap-3">
                            <div><i class="fas fa-video me-2" style="color:var(--kz-gold)"></i> <strong style="color:#fff">Phenomenal Fridays</strong><br><small>Every Friday, 8:00 PM EAT &mdash; online</small></div>
                            <div><i class="fas fa-church me-2" style="color:var(--kz-gold)"></i> <strong style="color:#fff">KIZAZI Conference</strong><br><small>Annual &mdash; East Africa</small></div>
                            <div><i class="fas fa-users me-2" style="color:var(--kz-gold)"></i> <strong style="color:#fff">Discipleship Cells</strong><br><small>Weekly &mdash; in your town / campus</small></div>
                            <a href="%s" target="_blank" rel="noopener" class="btn-kz btn-kz-gold btn-sm px-4 py-2 mt-1" style="align-self:flex-start">Register <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </div>
                    <div class="col-md-6 col-lg-3">
                        <h4 class="mb-4 h5">From The Fam</h4>
                        <div class="row g-2">%s</div>
                    </div>
                </div>
            </div>
            <div class="border-top" style="border-color:rgba(255,255,255,.1)!important">
                <div class="container py-4 d-flex flex-column flex-md-row justify-content-between align-items-center gap-2">
                    <small>&copy; <span class="kz-year">2026</span> KIZAZI Phenomenal. A generation on fire for God.</small>
                    <small style="opacity:.55">Built on the BabyCare template by HTML Codex &mdash; recoloured &amp; reimagined for the fam.</small>
                </div>
            </div>
        </footer>
        <a href="#" class="btn btn-primary border-0 rounded-circle back-to-top" style="background:var(--kz-grad)"><i class="fa fa-arrow-up"></i></a>
""" % (TIKTOK, INSTAGRAM, FACEBOOK, MEET_URL, REG_URL, REG_URL, g)


SCRIPTS = """    <script src="js/vendor/jquery.min.js"></script>
    <script src="js/vendor/bootstrap.bundle.min.js"></script>
    <script src="lib/wow/wow.min.js"></script>
    <script src="lib/easing/easing.min.js"></script>
    <script src="lib/waypoints/waypoints.min.js"></script>
    <script src="lib/lightbox/js/lightbox.min.js"></script>
    <script src="lib/owlcarousel/owl.carousel.min.js"></script>
    <script src="js/main.js"></script>
    <script src="js/kizazi.js"></script>
</body>
</html>
"""


def page(title, desc, active, body):
    return head(title, desc) + "<body>\n" + topbar() + navbar(active) + body + footer() + SCRIPTS


def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
        fh.write(html)
    print("  wrote", name)
