/* USTA Conseils & Travaux — scripts du site (aucune dépendance) */
(function () {
  'use strict';

  var TEL = '06 00 00 00 00';

  /* ---------- Menu mobile ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');

  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
    document.body.classList.toggle('nav-open', open);
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      setMenu(toggle.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setMenu(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && document.body.classList.contains('nav-open')) {
        setMenu(false);
        toggle.focus();
      }
    });
  }

  /* ---------- Ombre de l'en-tête au défilement ---------- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Année du copyright ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

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

  /* ---------- Suivi des clics sur les appels à l'action ----------
     Prêt pour Google Tag Manager : ne fait rien tant que dataLayer n'existe pas. */
  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-track]');
    if (el && Array.isArray(window.dataLayer)) {
      window.dataLayer.push({ event: 'cta_click', cta: el.getAttribute('data-track') });
    }
  });

  /* ---------- Formulaires de demande de devis ----------
     Envoi en arrière-plan vers le service défini dans l'attribut action (Formspree par défaut).
     Tant que l'identifiant n'est pas configuré (VOTRE_ID), le formulaire reste en mode démo. */
  function showStatus(form, type, html) {
    var box = form.querySelector('.form-status');
    if (box) box.innerHTML = '<p class="notice notice--' + type + '">' + html + '</p>';
  }

  document.querySelectorAll('form[data-lead-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }

      var trap = form.querySelector('[name="_gotcha"]');
      if (trap && trap.value) return; // robot détecté

      if (form.getAttribute('action').indexOf('VOTRE_ID') !== -1) {
        showStatus(form, 'demo',
          'Mode démonstration : le formulaire n\'est pas encore relié à une boîte mail (voir README). ' +
          'En production, le visiteur sera redirigé vers la page de remerciement.');
        return;
      }

      // Regroupe les cases cochées d'un même champ (ex. « plomberie, carrelage »)
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
          showStatus(form, 'error',
            'L\'envoi n\'a pas abouti. Appelez-nous directement au <a href="tel:+33600000000">' + TEL + '</a>.');
          button.disabled = false;
          button.innerHTML = label;
        });
    });
  });
})();
