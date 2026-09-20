/* =========================================================================
   KIZAZI Phenomenal — behaviour layer
   Drives: photo resolution from Google Drive, next-Friday dates, counters,
   scroll reveal, carousel, lightbox, gallery filter, chrome niceties.
   Core behaviour has NO CDN dependency (jQuery + Bootstrap are vendored).
   ========================================================================= */
(function () {
    'use strict';

    var doc = document;
    var reducedMotion = window.matchMedia &&
        window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    /* ------------------------------------------------------------ helpers -- */
    function $(sel, ctx) { return (ctx || doc).querySelector(sel); }
    function $all(sel, ctx) { return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel)); }

    /* ------------------------------------------- 1. Drive photo resolution --
       <img data-drive="FILE_ID" data-drive-w="1600">
       Fallback chain:
         1. https://drive.google.com/thumbnail?id=ID&sz=w1600
         2. https://lh3.googleusercontent.com/d/ID=w1600
         3. https://drive.google.com/uc?export=view&id=ID
         4. img/brand/photo-placeholder.svg                                       */
    var PLACEHOLDER = 'img/brand/photo-placeholder.svg';

    function driveUrls(id, w) {
        return [
            'https://drive.google.com/thumbnail?id=' + encodeURIComponent(id) + '&sz=w' + w,
            'https://lh3.googleusercontent.com/d/' + encodeURIComponent(id) + '=w' + w,
            'https://drive.google.com/uc?export=view&id=' + encodeURIComponent(id),
            PLACEHOLDER
        ];
    }

    function loadChain(imgEl, urls, pos) {
        var probe = new Image();
        probe.onload = function () {
            if (!imgEl.isConnected) { return; }
            imgEl.src = urls[pos];
            imgEl.classList.add('kz-photo-loaded');
            imgEl.dataset.driveDone = '1';
            imgEl.dispatchEvent(new Event('kz:photo'));
        };
        probe.onerror = function () {
            if (pos + 1 < urls.length) { loadChain(imgEl, urls, pos + 1); }
            else { imgEl.src = PLACEHOLDER; imgEl.dataset.driveDone = '1'; }
        };
        probe.src = urls[pos];
    }

    function resolveDrivePhotos() {
        $all('img[data-drive]').forEach(function (el) {
            if (el.dataset.driveState === '1') { return; }
            el.dataset.driveState = '1';
            var id = el.getAttribute('data-drive');
            var w = parseInt(el.getAttribute('data-drive-w') || '1600', 10);
            if (!el.hasAttribute('loading') || el.closest('.kz-hero, .kz-page-header, .kz-featured-photo, .kz-media-photo')) {
                loadChain(el, driveUrls(id, w), 0);
            } else {
                // data-drive imgs have no src until we set one — resolve on
                // visibility for performance
                if ('IntersectionObserver' in window) {
                    var io = new IntersectionObserver(function (entries, obs) {
                        entries.forEach(function (entry) {
                            if (entry.isIntersecting) {
                                obs.unobserve(el);
                                loadChain(el, driveUrls(id, w), 0);
                            }
                        });
                    }, { rootMargin: '400px 0px' });
                    io.observe(el);
                } else {
                    loadChain(el, driveUrls(id, w), 0);
                }
            }
        });
    }

    /* ------------------------------------------------- 2. Next Friday dates --
       Elements:
         [data-next-friday-long]   "Fri, 26 Sep 2026"
         [data-next-friday-day]    "26"            (auto date badges)
         [data-next-friday-mon]    "SEP"
         [data-next-friday-rel]    "in 3 days" / "today" / "tomorrow"        */
    function nextFriday(from) {
        var d = new Date(from.getFullYear(), from.getMonth(), from.getDate());
        var diff = (5 - d.getDay() + 7) % 7; // 0 when today IS Friday
        d.setDate(d.getDate() + diff);
        return d;
    }

    function fmtLong(d) {
        return d.toLocaleDateString('en-GB', {
            weekday: 'short', day: 'numeric', month: 'short', year: 'numeric'
        });
    }

    function relLabel(d) {
        var now = new Date();
        var today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
        var days = Math.round((d - today) / 86400000);
        if (days <= 0) { return 'tonight!'; }
        if (days === 1) { return 'tomorrow'; }
        return 'in ' + days + ' days';
    }

    function updateFridays() {
        var fr = nextFriday(new Date());
        var long = fmtLong(fr);
        var day = String(fr.getDate());
        var mon = fr.toLocaleDateString('en-GB', { month: 'short' }).toUpperCase();
        var rel = relLabel(fr);

        $all('[data-next-friday-long]').forEach(function (el) { el.textContent = long; });
        $all('[data-next-friday-day]').forEach(function (el) { el.textContent = day; });
        $all('[data-next-friday-mon]').forEach(function (el) { el.textContent = mon; });
        $all('[data-next-friday-rel]').forEach(function (el) {
            el.textContent = el.closest('[data-rel-parens]') ? '(' + rel + ')' : rel;
        });
    }

    /* ------------------------------------------------------- 3. Counters -- */
    function animateCounter(el) {
        var target = parseInt(el.getAttribute('data-count') || '0', 10);
        var suffix = el.getAttribute('data-suffix') || '';
        if (reducedMotion) { el.textContent = target + suffix; return; }
        var dur = 1500;
        var t0 = null;
        function step(ts) {
            if (t0 === null) { t0 = ts; }
            var p = Math.min((ts - t0) / dur, 1);
            var eased = 1 - Math.pow(1 - p, 3); // easeOutCubic
            el.textContent = Math.round(target * eased) + (p === 1 ? suffix : '');
            if (p < 1) { requestAnimationFrame(step); }
        }
        requestAnimationFrame(step);
    }

    function initCounters() {
        var counters = $all('.kz-counter');
        if (!counters.length) { return; }
        if (!('IntersectionObserver' in window)) {
            counters.forEach(animateCounter);
            return;
        }
        var io = new IntersectionObserver(function (entries, obs) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    obs.unobserve(entry.target);
                    animateCounter(entry.target);
                }
            });
        }, { threshold: 0.4 });
        counters.forEach(function (c) { io.observe(c); });
    }

    /* ----------------------------------------------------- 4. Scroll reveal -- */
    function initReveal() {
        var els = $all('.kz-reveal');
        if (!els.length) { return; }
        if (reducedMotion || !('IntersectionObserver' in window)) {
            els.forEach(function (el) { el.classList.add('kz-in'); });
            return;
        }
        // light stagger inside rows
        $all('.row').forEach(function (row) {
            var kids = $all(':scope > .kz-reveal', row);
            kids.forEach(function (el, i) {
                el.style.transitionDelay = (i * 90) + 'ms';
            });
        });
        var io = new IntersectionObserver(function (entries, obs) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('kz-in');
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
        els.forEach(function (el) { io.observe(el); });
    }

    /* ------------------------------------------------------- 5. Navbar -- */
    function initNavbar() {
        var wrap = $('.kz-navbar-wrap');
        if (!wrap) { return; }
        var onScroll = function () {
            wrap.classList.toggle('kz-nav-scrolled', window.scrollY > 24);
        };
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();

        // close the mobile menu after choosing a page
        var collapse = $('#navbarCollapse');
        if (collapse && window.bootstrap) {
            $all('.nav-link', collapse).forEach(function (a) {
                a.addEventListener('click', function () {
                    if (collapse.classList.contains('show') &&
                        window.bootstrap.Collapse.getInstance(collapse)) {
                        window.bootstrap.Collapse.getInstance(collapse).hide();
                    }
                });
            });
        }
    }

    /* ---------------------------------------------------- 6. Back to top -- */
    function initBackToTop() {
        var btn = $('.kz-back-to-top');
        if (!btn) { return; }
        var onScroll = function () {
            btn.classList.toggle('kz-show', window.scrollY > 560);
        };
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: reducedMotion ? 'auto' : 'smooth' });
        });
    }

    /* ------------------------------------------------- 7. Carousel + LB -- */
    function initCarousel() {
        var el = $('.kz-testimonial-carousel');
        if (el && window.jQuery && jQuery.fn.owlCarousel) {
            jQuery(el).owlCarousel({
                loop: true,
                margin: 24,
                dots: true,
                nav: false,
                smartSpeed: 700,
                autoplay: !reducedMotion,
                autoplayTimeout: 5200,
                autoplayHoverPause: true,
                responsive: {
                    0: { items: 1 },
                    992: { items: 2 }
                }
            });
        }
        if (window.lightbox && lightbox.option) {
            lightbox.option({
                resizeDuration: 220,
                fadeDuration: 220,
                imageFadeDuration: 220,
                wrapAround: true,
                albumLabel: 'Photo %1 of %2'
            });
        }
    }

    /* --------------------------------------------------- 8. Gallery filter -- */
    function initGalleryFilter() {
        var chips = $all('.kz-filter-chip');
        if (!chips.length) { return; }
        chips.forEach(function (chip) {
            chip.addEventListener('click', function () {
                chips.forEach(function (c) { c.classList.remove('active'); });
                chip.classList.add('active');
                var f = chip.getAttribute('data-filter');
                $all('.kz-gallery-item').forEach(function (item) {
                    var show = (f === 'all') || (item.getAttribute('data-cat') === f);
                    item.classList.toggle('kz-hidden', !show);
                });
            });
        });
    }

    /* --------------------------------------------------- 9. Newsletter -- */
    function initNewsletter() {
        var form = $('.kz-newsletter');
        if (!form) { return; }
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            var done = doc.createElement('div');
            done.className = 'kz-newsletter-done';
            done.innerHTML = '🔥 You&rsquo;re on the list! (Announcements hit our socials first.)';
            form.replaceWith(done);
        });
    }

    /* --------------------------------------- 10. Flip cards (touch/tap) -- */
    function initFlipCards() {
        $all('.kz-flip').forEach(function (card) {
            card.addEventListener('click', function (e) {
                if (e.target.closest('a')) { return; } // let links do their thing
                card.classList.toggle('kz-flipped');
            });
            card.setAttribute('tabindex', '0');
        });
    }

    /* --------------------------------------------------------- 11. Year -- */
    function initYear() {
        var y = String(new Date().getFullYear());
        $all('[data-year]').forEach(function (el) { el.textContent = y; });
    }

    /* ------------------------------------------------------------- boot -- */
    function boot() {
        resolveDrivePhotos();
        updateFridays();
        initCounters();
        initReveal();
        initNavbar();
        initBackToTop();
        initCarousel();
        initGalleryFilter();
        initNewsletter();
        initFlipCards();
        initYear();

        // re-check Fridays at midnight boundary (cheap insurance)
        setInterval(function () {
            var now = new Date();
            var fr = nextFriday(now);
            if (String(now.getDate()) !== doc.body.getAttribute('data-friday-check')) {
                doc.body.setAttribute('data-friday-check', String(now.getDate()));
                updateFridays();
            }
        }, 3600000);
    }

    if (doc.readyState === 'loading') {
        doc.addEventListener('DOMContentLoaded', boot);
    } else {
        boot();
    }
})();
