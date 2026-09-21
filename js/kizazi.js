/* =========================================================================
   KIZAZI Phenomenal, behaviour layer (template edition)
   Teaches the BabyCare template about:
     1. auto-calculated next-Friday dates
     2. gallery category filter
     3. the template's full-screen quick search
     4. the decorative newsletter form
     5. last-resort placeholder for a broken gallery photo
   Photos are vendored in img/gallery/ (plain <img src> + inline --kz-photo
   backgrounds). There is no Drive resolution chain any more.
   Core behaviour has NO CDN dependency (jQuery + Bootstrap are vendored).
   ========================================================================= */
(function () {
    'use strict';

    var doc = document;
    var PLACEHOLDER = 'img/brand/photo-placeholder.svg';

    function $all(sel, ctx) {
        return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel));
    }

    /* --------------------------------- 1. last-resort photo placeholder ---
       If a vendored photo is ever missing/corrupt, swap in the branded
       placeholder instead of a broken-image icon (CSS covers backgrounds). */
    doc.addEventListener('error', function (ev) {
        var el = ev.target;
        if (el && el.tagName === 'IMG' && el.src.indexOf(PLACEHOLDER) === -1) {
            el.src = PLACEHOLDER;
        }
    }, true);

    /* ------------------------------------------------- 2. Next Friday dates --\n       [data-next-friday-long]  \"Fri, 26 Sep 2026\"
       [data-next-friday-day]   \"26\"
       [data-next-friday-mon]   \"SEP\"                                             */
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

    /* ------------------------------------------------- 3. Gallery filter --- */
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

    /* -------------------------------------------------- 4. Quick search --- */
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
                    q.replace(/[<>&]/g, '') + '&rdquo;. Try &ldquo;friday&rdquo; or &ldquo;rooted&rdquo;.</p>';
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

    /* ------------------------------------------------- 5. Newsletter form -- */
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
                if (note) { note.textContent = 'Decorative for now. Nothing was stored.'; }
            });
        });
    }

    /* ---------------------------------------------------------------- boot -- */
    doc.addEventListener('DOMContentLoaded', function () {
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
