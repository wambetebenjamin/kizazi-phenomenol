/* ==========================================================================
   KIZAZI PHENOMENAL — behaviour layer
   --------------------------------------------------------------------------
   Photos live in a shared Google Drive folder. Because the site is static,
   every <img data-drive="ID"> is pointed at Google's thumbnail CDN, with a
   graceful fallback chain so a broken link never shows a dead image.
   ========================================================================== */
(function ($) {
    "use strict";

    /* ---------- Drive image resolver ---------- */
    var SOURCES = [
        function (id, w) { return "https://drive.google.com/thumbnail?id=" + id + "&sz=w" + w; },
        function (id, w) { return "https://lh3.googleusercontent.com/d/" + id + "=w" + w; },
        function (id, w) { return "https://drive.google.com/uc?export=view&id=" + id; }
    ];
    var PLACEHOLDER = "img/brand/photo-placeholder.svg";

    function wireDriveImages(scope) {
        $("img[data-drive]", scope || document).each(function () {
            var $img = $(this);
            if ($img.data("driveWired")) { return; }
            $img.data("driveWired", true);
            var id = $img.data("drive");
            var w = $img.data("drive-w") || 1600;
            var step = 0;
            $img.attr("src", SOURCES[0](id, w));
            $img.on("error", function () {
                step += 1;
                if (step < SOURCES.length) {
                    $img.attr("src", SOURCES[step](id, w));
                } else {
                    $img.attr("src", PLACEHOLDER);
                    $img.addClass("kz-photo-missing");
                }
            });
        });
    }

    /* ---------- Navbar stick ---------- */
    function stickyNav() {
        var $nav = $(".kz-navbar");
        $(window).on("scroll", function () {
            $nav.toggleClass("kz-stuck", $(window).scrollTop() > 40);
        });
    }

    /* ---------- Reveal on scroll ---------- */
    function reveal() {
        var io = ("IntersectionObserver" in window) ? new IntersectionObserver(function (entries) {
            entries.forEach(function (e) {
                if (e.isIntersecting) {
                    e.target.classList.add("in");
                    io.unobserve(e.target);
                }
            });
        }, { threshold: 0.12 }) : null;
        $(".kz-reveal").each(function () {
            if (io) { io.observe(this); } else { this.classList.add("in"); }
        });
    }

    /* ---------- Animated counters ---------- */
    function counters() {
        var run = function (el) {
            var $el = $(el);
            var target = parseInt($el.data("count"), 10) || 0;
            var suffix = $el.data("suffix") || "";
            var start = null;
            var dur = 1600;
            function frame(ts) {
                if (!start) { start = ts; }
                var p = Math.min((ts - start) / dur, 1);
                var eased = 1 - Math.pow(1 - p, 3);
                $el.text(Math.round(target * eased) + suffix);
                if (p < 1) { window.requestAnimationFrame(frame); }
            }
            window.requestAnimationFrame(frame);
        };
        var io = ("IntersectionObserver" in window) ? new IntersectionObserver(function (entries) {
            entries.forEach(function (e) {
                if (e.isIntersecting) { run(e.target); io.unobserve(e.target); }
            });
        }, { threshold: 0.4 }) : null;
        $(".kz-count").each(function () {
            if (io) { io.observe(this); } else { run(this); }
        });
    }

    /* ---------- Marquee: duplicate content so the loop is seamless ---------- */
    function marquee() {
        $(".kz-marquee-track").each(function () {
            var $t = $(this);
            $t.append($t.html());
        });
    }

    /* ---------- "Next Friday" catch-up date ---------- */
    function nextFriday() {
        var now = new Date();
        var day = now.getDay();            // 5 = Friday
        var diff = (5 - day + 7) % 7;
        var next = new Date(now.getTime() + diff * 86400000);
        if (diff === 0 && now.getHours() >= 22) { next = new Date(now.getTime() + 7 * 86400000); }
        var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
        var label = months[next.getMonth()] + " " + next.getDate();
        $(".kz-next-friday").text(label);
        $(".kz-next-friday-day").text(next.getDate());
        $(".kz-next-friday-month").text(months[next.getMonth()].toUpperCase());
    }

    /* ---------- Gallery filter ---------- */
    function galleryFilter() {
        $(".kz-filter-btn").on("click", function () {
            var f = $(this).data("filter");
            $(".kz-filter-btn").removeClass("active");
            $(this).addClass("active");
            $(".kz-gallery-item").each(function () {
                var cats = String($(this).data("cat") || "");
                var show = (f === "all") || (cats.indexOf(f) > -1);
                $(this).toggleClass("hide", !show);
            });
        });
    }

    /* ---------- Copyright year ---------- */
    function year() { $(".kz-year").text(new Date().getFullYear()); }

    /* ---------- Tilt on polaroids (desktop only) ---------- */
    function tilt() {
        if (!window.matchMedia("(pointer:fine)").matches) { return; }
        $(".kz-polaroid").on("mousemove", function (e) {
            var r = this.getBoundingClientRect();
            var x = (e.clientX - r.left) / r.width - 0.5;
            var y = (e.clientY - r.top) / r.height - 0.5;
            this.style.transform = "perspective(700px) rotateY(" + (x * 8) + "deg) rotateX(" + (-y * 8) + "deg)";
        }).on("mouseleave", function () {
            this.style.transform = "";
        });
    }

    $(function () {
        wireDriveImages();
        stickyNav();
        reveal();
        counters();
        marquee();
        nextFriday();
        galleryFilter();
        year();
        tilt();

        // Lightbox defaults
        if (window.lightbox) {
            lightbox.option({ resizeDuration: 260, fadeDuration: 260, wrapAround: true, albumLabel: "Moment %1 of %2" });
        }
    });

    // expose for lazy-loaded content
    window.KizaziPhotos = { wire: wireDriveImages };
})(jQuery);
