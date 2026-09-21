/* =========================================================================
   KIZAZI Phenomenal — behaviour layer (template edition)
   Teaches the BabyCare template about:
     1. hotlinked Google-Drive photos  (<img data-drive="ID">)
     2. hotlinked Drive backgrounds    ([data-drive-bg="ID"])
     3. auto-calculated next-Friday dates
     4. gallery category filter
     5. the template's full-screen quick search
     6. the decorative newsletter form
   Core behaviour has NO CDN dependency (jQuery + Bootstrap are vendored).
   ========================================================================= */
(function () {
    'use strict';

    var doc = document;
    var PLACEHOLDER = 'img/brand/photo-placeholder.svg';

    function $all(sel, ctx) {
        return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel));
    }

    /* ------------------------------------------- 1. Drive photo resolution --
       <img data-drive="FILE_ID" data-drive-w="1600">
       Fallback chain:
         1. https://drive.google.com/thumbnail?id=ID&sz=w1600
         2. https://lh3.googleusercontent.com/d/ID=w1600
         3. https://drive.google.com/uc?export=view&id=ID
         4. img/brand/photo-placeholder.svg                                       */
    function driveUrls(id, w) {
        return [
            'https://drive.google.com/thumbnail?id=' + encodeURIComponent(id) + '&sz=w' + w,
            'https://lh3.googleusercontent.com/d/' + encodeURIComponent(id) + '=w' + w,
            'https://drive.google.com/uc?export=view&id=' + encodeURIComponent(id),
            PLACEHOLDER
        ];
    }

    function loadChain(onOk, onFail, urls, pos) {
        var probe = new Image();
        probe.onload = function () { onOk(urls[pos]); };
        probe.onerror = function () {
            if (pos + 1 < urls.length) { loadChain(onOk, onFail, urls, pos + 1); }
            else { onFail(); }
        };
        probe.src = urls[pos];
    }

    function resolveDrivePhotos() {
        $all('img[data-drive]').forEach(function (el) {
            if (el.dataset.driveState === '1') { return; }
            el.dataset.driveState = '1';
            var id = el.getAttribute('data-drive');
            var w = parseInt(el.getAttribute('data-drive-w') || '1600', 10);

            function apply(url) { el.src = url; }
            function fail() { el.src = PLACEHOLDER; }

            if ('IntersectionObserver' in window) {
                var io = new IntersectionObserver(function (entries, obs) {
                    entries.forEach(function (entry) {
                        if (entry.isIntersecting) {
                            obs.unobserve(el);
                            loadChain(apply, fail, driveUrls(id, w), 0);
                        }
                    });
                }, { rootMargin: '500px 0px' });
                io.observe(el);
            } else {
                loadChain(apply, fail, driveUrls(id, w), 0);
            }
        });
    }

    /* ------------------------------------------ 2. Drive CSS backgrounds --
       [data-drive-bg="ID"] elements carry an inline --kz-photo custom property;
       we walk the same fallback chain and swap the property when a URL dies. */
    function resolveDriveBackgrounds() {
        $all('[data-drive-bg]').forEach(function (el) {
            if (el.dataset.driveBgState === '1') { return; }
            el.dataset.driveBgState = '1';
            var id = el.getAttribute('data-drive-bg');
            var w = parseInt(el.getAttribute('data-drive-bg-w') || '1600', 10);
            loadChain(
                function (url) { el.style.setProperty('--kz-photo', 'url("' + url + '")'); },
                function () { el.style.setProperty('--kz-photo', 'url("' + PLACEHOLDER + '")'); },
                driveUrls(id, w), 0);
        });
    }

    /* ------------------------------------------------- 3. Next Friday dates --
       [data-next-friday-long]  "Fri, 26 Sep 2026"
       [data-next-friday-day]   "26"
       [data-next-friday-mon]   "SEP"                                             */
    function nextFriday(from) {
        var d = new Date(from.getFullYear(), from.getMonth(), from.getDate());
        d.setDate(d.getDate() + ((5 - d.getDay() + 7) % 7));
        return d;
    }

    function updateFridays() {
        var fr = nextFriday(new Date());
        var long = fr.toLocaleDateString('en-GB', {
            weekday: 'short', day: 'numeric', month: 'short', year: 'numeric'
        });
        var day = String(fr.getDate());
        var mon = fr.toLocaleDateString('en-GB', { month: 'short' }).toUpperCase();
        $all('[data-next-friday-long]').forEach(function (el) { el.textContent = long; });
        $all('[data-next-friday-day]').forEach(function (el) { el.textContent = day; });
        $all('[data-next-friday-mon]').forEach(function (el) { el.textContent = mon; });
    }

    /* ------------------------------------------------- 4. Gallery filter --- */
    function initGalleryFilter() {
        var buttons = $all('.kz-filter-btn');
        var items = $all('.kz-gallery-item');
        if (!buttons.length || !items.length) { return; }
        buttons.forEach(function (btn) {
            btn.addEventListener('click', function () {
                buttons.forEach(function (b) { b.classList.remove('active'); });
                btn.classList.add('active');
                var cat = btn.getAttribute('data-filter');
                items.forEach(function (item) {
                    var show = (cat === 'all') || (item.getAttribute('data-cat') === cat);
                    item.classList.toggle('kz-hidden', !show);
                });
                if (window.lightbox && typeof window.lightbox.option === 'function') {
                    window.lightbox.option({ albumLabel: 'Photo %1 of %2' });
                }
            });
        });
    }

    /* -------------------------------------------------- 5. Quick search --- */
    function buildSearchIndex() {
        var seen = {};
        var index = [];
        function add(title, href) {
            title = (title || '').replace(/\s+/g, ' ').trim();
            if (!title || !href || href === '#' || seen[title + href]) { return; }
            seen[title + href] = 1;
            index.push({ title: title, href: href });
        }
        $all('.navbar-nav a, .footer-item a[href$=".html"]').forEach(function (a) {
            add(a.textContent, a.getAttribute('href'));
        });
        $all('a.h4').forEach(function (a) { add(a.textContent, a.getAttribute('href')); });
        $all('.accordion-button').forEach(function (b) {
            var item = b.closest('.accordion-item');
            add(b.textContent, (item && item.id) ? '#' + item.id : '#');
        });
        $all('h1, h4.text-primary').forEach(function (h) {
            add(h.textContent, location.pathname.split('/').pop() || 'index.html');
        });
        return index;
    }

    function initSearch() {
        var input = doc.getElementById('kz-search-input');
        var results = doc.getElementById('kz-search-results');
        if (!input || !results) { return; }
        var index = buildSearchIndex();

        function render(q) {
            results.innerHTML = '';
            if (q.length < 2) { return; }
            var needle = q.toLowerCase();
            var hits = index.filter(function (e) {
                return e.title.toLowerCase().indexOf(needle) !== -1;
            }).slice(0, 8);
            if (!hits.length) {
                results.innerHTML = '<p class="kz-search-empty mb-0">Nothing found for &ldquo;' +
                    q.replace(/[<>&]/g, '') + '&rdquo; &mdash; try &ldquo;friday&rdquo; or &ldquo;rooted&rdquo;.</p>';
                return;
            }
            hits.forEach(function (h) {
                var a = doc.createElement('a');
                a.href = h.href;
                a.innerHTML = '<i class="fas fa-angle-right me-2 text-primary"></i>' + h.title;
                results.appendChild(a);
            });
        }

        input.addEventListener('input', function () { render(input.value); });
        input.addEventListener('keydown', function (ev) {
            if (ev.key === 'Enter') {
                var first = results.querySelector('a');
                if (first) { location.href = first.getAttribute('href'); }
            }
        });
    }

    /* ------------------------------------------------- 6. Newsletter form -- */
    function initNewsletter() {
        $all('form.kz-newsletter').forEach(function (form) {
            form.addEventListener('submit', function (ev) {
                ev.preventDefault();
                var input = form.querySelector('input');
                if (!input || !input.value || input.value.indexOf('@') === -1) {
                    if (input) { input.focus(); }
                    return;
                }
                var note = form.parentElement.querySelector('.kz-newsletter-note');
                form.innerHTML = '<p class="mb-0 text-primary fw-semibold py-2 px-3">' +
                    '<i class="fas fa-check-circle me-2"></i>Asante! You&rsquo;re on the list.</p>';
                if (note) { note.textContent = 'Decorative for now — nothing was stored.'; }
            });
        });
    }

    /* ---------------------------------------------------------------- boot -- */
    doc.addEventListener('DOMContentLoaded', function () {
        resolveDrivePhotos();
        resolveDriveBackgrounds();
        updateFridays();
        initGalleryFilter();
        initSearch();
        initNewsletter();
        if (window.lightbox && typeof window.lightbox.option === 'function') {
            window.lightbox.option({
                resizeDuration: 200,
                fadeDuration: 200,
                imageFadeDuration: 200,
                wrapAround: true,
                albumLabel: 'Photo %1 of %2'
            });
        }
    });
})();
