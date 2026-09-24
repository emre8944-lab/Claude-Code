/* USTA Conseils & Travaux — interactions du site (aucune dépendance) */
(function () {
  'use strict';

  window.__usta = true;
  var root = document.documentElement;
  root.classList.add('js');
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var TEL = '06 00 00 00 00';

  /* ---------- Menu : méga-menu, listes déroulantes, menu mobile ---------- */
  var header = document.querySelector('.site-header');
  var burger = document.querySelector('.burger');
  var items = Array.prototype.slice.call(document.querySelectorAll('.nav__item.has-mega, .nav__item.has-drop'));
  var desktop = window.matchMedia('(min-width: 1160px)');
  var closeTimer;

  function closeAll(except) {
    items.forEach(function (item) {
      if (item === except) return;
      item.classList.remove('is-open');
      var b = item.querySelector('.nav__link');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  }
  function open(item) {
    closeAll(item);
    item.classList.add('is-open');
    item.querySelector('.nav__link').setAttribute('aria-expanded', 'true');
  }

  items.forEach(function (item) {
    var button = item.querySelector('.nav__link');
    button.addEventListener('click', function () {
      if (item.classList.contains('is-open')) closeAll(); else open(item);
    });
    item.addEventListener('mouseenter', function () {
      if (!desktop.matches) return;
      clearTimeout(closeTimer);
      open(item);
    });
    item.addEventListener('mouseleave', function () {
      if (!desktop.matches) return;
      closeTimer = setTimeout(function () { closeAll(); }, 180);
    });
    item.addEventListener('focusout', function (e) {
      if (desktop.matches && !item.contains(e.relatedTarget)) item.classList.remove('is-open');
    });
  });

  function setMobileMenu(isOpen) {
    if (!burger) return;
    burger.setAttribute('aria-expanded', String(isOpen));
    burger.setAttribute('aria-label', isOpen ? 'Fermer le menu' : 'Ouvrir le menu');
    document.body.classList.toggle('nav-open', isOpen);
    if (!isOpen) closeAll();
  }
  if (burger) {
    burger.addEventListener('click', function () {
      setMobileMenu(burger.getAttribute('aria-expanded') !== 'true');
    });
  }
  document.addEventListener('click', function (e) {
    if (e.target.closest('.site-nav a')) setMobileMenu(false);
    if (desktop.matches && !e.target.closest('.nav__item')) closeAll();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    var openItem = items.filter(function (i) { return i.classList.contains('is-open'); })[0];
    if (openItem) { closeAll(); openItem.querySelector('.nav__link').focus(); }
    else if (document.body.classList.contains('nav-open')) { setMobileMenu(false); burger.focus(); }
  });
  desktop.addEventListener('change', function () { setMobileMenu(false); });

  /* ---------- En-tête au défilement + progression de la méthode ---------- */
  var rail = document.querySelector('.steps');
  function onScroll() {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 20);
    if (rail) {
      var r = rail.getBoundingClientRect();
      var p = (window.innerHeight * 0.75 - r.top) / (r.height + window.innerHeight * 0.2);
      rail.style.setProperty('--p', Math.max(0, Math.min(1, p)).toFixed(3));
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Apparitions et compteurs ---------- */
  function count(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    if (reduced) { el.textContent = target; return; }
    var start = null;
    function step(t) {
      if (!start) start = t;
      var k = Math.min(1, (t - start) / 1400);
      el.textContent = Math.round(target * (1 - Math.pow(1 - k, 3)));
      if (k < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        if (entry.target.hasAttribute('data-count')) count(entry.target);
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    document.querySelectorAll('[data-reveal], [data-count]').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('[data-reveal]').forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------- Cartes inclinables en 3D (souris uniquement) ---------- */
  if (finePointer && !reduced) {
    document.querySelectorAll('[data-tilt]').forEach(function (card) {
      var max = parseFloat(card.getAttribute('data-tilt')) || 6;
      card.addEventListener('pointermove', function (e) {
        var r = card.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var y = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform = 'perspective(900px) rotateX(' + (-y * max).toFixed(2) + 'deg) rotateY(' + (x * max).toFixed(2) + 'deg) translateY(-4px)';
      });
      card.addEventListener('pointerleave', function () { card.style.transform = ''; });
    });
  }

  /* ---------- Scène 3D : chargée après la page, pour ne pas la ralentir ---------- */
  if (document.querySelector('[data-scene3d]')) {
    var loadScene = function () {
      var s = document.createElement('script');
      s.src = 'assets/js/scene3d.js';
      s.async = true;
      document.body.appendChild(s);
    };
    var idle = window.requestIdleCallback || function (fn) { return setTimeout(fn, 200); };
    if (document.readyState === 'complete') idle(loadScene, { timeout: 1500 });
    else window.addEventListener('load', function () { idle(loadScene, { timeout: 1500 }); });
  }

  /* ---------- Année du copyright ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Pré-sélection du type de travaux (contact.html?service=plomberie) ---------- */
  var service = new URLSearchParams(window.location.search).get('service');
  if (service) {
    document.querySelectorAll('input[name="travaux"]').forEach(function (input) {
      if (input.value === service) input.checked = true;
    });
    document.querySelectorAll('select[name="travaux"]').forEach(function (select) {
      if (select.querySelector('option[value="' + service + '"]')) select.value = service;
    });
  }

  /* ---------- Suivi des clics (prêt pour Google Tag Manager) ---------- */
  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-track]');
    if (el && Array.isArray(window.dataLayer)) window.dataLayer.push({ event: 'cta_click', cta: el.getAttribute('data-track') });
  });

  /* ---------- Formulaires de devis ----------
     Envoi vers le service indiqué dans action (Formspree par défaut).
     Tant que VOTRE_ID n'est pas remplacé, le formulaire reste en mode démo. */
  function showStatus(form, type, html) {
    var box = form.querySelector('.form-status');
    if (box) box.innerHTML = '<p class="notice notice--' + type + '">' + html + '</p>';
  }

  document.querySelectorAll('form[data-lead-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var trap = form.querySelector('[name="_gotcha"]');
      if (trap && trap.value) return;

      if (form.getAttribute('action').indexOf('VOTRE_ID') !== -1) {
        showStatus(form, 'demo', 'Mode démonstration : le formulaire n\'est pas encore relié à une boîte mail (voir README). En production, le visiteur arrive sur la page de remerciement.');
        return;
      }

      var raw = new FormData(form);
      var data = new FormData();
      Array.from(new Set(Array.from(raw.keys()))).forEach(function (key) {
        data.append(key, raw.getAll(key).join(', '));
      });

      var button = form.querySelector('[type="submit"]');
      var label = button.innerHTML;
      button.disabled = true;
      button.textContent = 'Envoi en cours…';

      fetch(form.action, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then(function (res) {
          if (!res.ok) throw new Error('HTTP ' + res.status);
          window.location.href = form.getAttribute('data-success') || 'merci.html';
        })
        .catch(function () {
          showStatus(form, 'error', 'L\'envoi n\'a pas abouti. Appelez-nous directement au <a href="tel:+33600000000">' + TEL + '</a>.');
          button.disabled = false;
          button.innerHTML = label;
        });
    });
  });
})();
