#!/usr/bin/env python3
"""Génère les pages HTML statiques du site USTA dans public/.

Usage : python3 src/build.py   (ou npm run build:html)
Les coordonnées (ville, téléphone…) se changent dans la section CONFIG ci-dessous.
"""
import html
import json
import pathlib
import re

from content import PAGES, SERVICES
from services_content import SERVICE_PAGES

SRC = pathlib.Path(__file__).resolve().parent
OUT = SRC.parent / 'public'

# ------------------------------------------------------------------ CONFIG
SITE = 'https://www.votre-domaine.fr'
TEL = '06 00 00 00 00'
TEL_HREF = 'tel:+33600000000'
WHATSAPP = 'https://wa.me/33600000000'
EMAIL = 'contact@votre-domaine.fr'
FORM_ACTION = 'https://formspree.io/f/VOTRE_ID'
VILLE = '[Ville]'
RAYON = '[XX]'
HOURS = [('Lundi – Vendredi', '8h – 18h'), ('Samedi', '9h – 12h'), ('Dimanche', 'Fermé')]
HOURS_SHORT = 'Lun – Ven 8h – 18h · Sam 9h – 12h'
LASTMOD = '2026-09-24'

ICONS = {
    'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
    'check': '<polyline points="20 6 9 17 4 12"/>',
    'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>',
    'pin': '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    'drop': '<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>',
    'bolt': '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    'grid': '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/>',
    'layers': '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    'home': '<path d="M3 9.5 12 3l9 6.5V20a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 13 15 13 15 22"/>',
    'roller': '<rect x="3" y="3" width="15" height="6" rx="1.5"/><path d="M18 6h2.5v5.5H11V15"/><rect x="9" y="15" width="4" height="7" rx="1"/>',
    'arrow': '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>',
    'arrow-ur': '<line x1="7" y1="17" x2="17" y2="7"/><polyline points="8 7 17 7 17 16"/>',
    'chev': '<polyline points="6 9 12 15 18 9"/>',
    'file': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
    'chat': '<path d="M21 11.5a8.4 8.4 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.4 8.4 0 0 1-3.8-.9L3 21l1.9-5.7a8.4 8.4 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.4 8.4 0 0 1 3.8-.9h.5a8.5 8.5 0 0 1 8 8z"/>',
    'bulb': '<path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.2 1 2V17h6v-.3c0-.8.4-1.5 1-2A7 7 0 0 0 12 2z"/>',
    'alert': '<path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    'lock': '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    'clock': '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
}

LOGO_MARK = (
    '<svg class="brand__mark" viewBox="0 0 40 40" aria-hidden="true">'
    '<rect width="40" height="40" rx="11" fill="#FF5A1F"/>'
    '<path d="M8 18.5 20 9l12 9.5" fill="none" stroke="#0E0E0C" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>'
    '<path d="M13.5 19v6.5a6.5 6.5 0 0 0 13 0V19" fill="none" stroke="#0E0E0C" stroke-width="3.4" stroke-linecap="round"/>'
    '</svg>'
)

# Dessin affiché avant le chargement de la 3D (ou si le navigateur ne la supporte pas)
SCENE_FALLBACK = (
    '<svg class="scene3d__fallback" viewBox="0 0 400 360" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true">'
    '<path d="M200 320 360 240 200 160 40 240Z"/><path d="M40 240V130l160-80v110"/><path d="M200 50l160 80v110"/>'
    '<path d="M80 250 200 190l120 60M120 270l120-60M160 290l120-60M120 230l120 60M160 210l120 60"/>'
    '<path d="M70 95 200 25l130 70" stroke="#FF5A1F" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    '</svg>'
)


def sprite():
    symbols = ''.join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items())
    return ('<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" '
            'style="position:absolute;width:0;height:0;overflow:hidden">' + symbols + '</svg>')


def icon(name, extra=''):
    cls = {'fill': 'icon icon--fill', 'arrow': 'icon icon--arrow', 'chev': 'icon icon--chev'}.get(extra, 'icon')
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'


def tokens(text, plain=False):
    """Remplace les jetons de contenu. plain=True pour les données structurées (texte brut)."""
    ph = (lambda s: s) if plain else (lambda s: f'<span class="ph">{s}</span>')
    text = text.replace('%VILLE%', ph(VILLE))
    text = text.replace('%RAYON%', ph(RAYON))
    text = text.replace('%TEL_HREF%', TEL_HREF)
    text = text.replace('%TEL%', TEL if plain else TEL.replace(' ', ' '))
    text = text.replace('%WHATSAPP%', WHATSAPP)
    text = text.replace('%EMAIL%', EMAIL)
    text = text.replace('%HOURS%', HOURS_SHORT)
    text = text.replace('%FORM_ACTION%', FORM_ACTION)
    text = re.sub(r'%PH:([^%]+)%', lambda m: ph('[' + m.group(1) + ']'), text)
    text = re.sub(r'%I:([a-z-]+)(?::([a-z]+))?%', lambda m: icon(m.group(1), m.group(2) or ''), text)
    return text


NBSP = ' '


def french_typo(doc):
    """Espaces insécables de la typographie française, hors balises et hors <script>/<style>."""
    parts = re.split(r'(<script[\s\S]*?</script>|<style[\s\S]*?</style>|<[^>]+>)', doc)
    for i, part in enumerate(parts):
        if not part or part.startswith('<'):
            continue
        part = re.sub(r' ([?!:;»])', NBSP + r'\1', part)
        part = part.replace('« ', '«' + NBSP).replace('n° ', 'n°' + NBSP)
        part = re.sub(r'(\d) (h|%|km|€|m²|ans|litres|cm)(?=[\s<.,;)]|$)', r'\1' + NBSP + r'\2', part)
        parts[i] = part
    return ''.join(parts)


def strip_tags(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()


# ------------------------------------------------------------------ blocs communs

def trade_style(s):
    return f'style="--trade: var(--c-{s["slug"]})"'


def header(page):
    current = page['file']
    section = page.get('section')

    def cur(href):
        return ' aria-current="page"' if href == current else ''

    trades = [s for s in SERVICES if s['slug'] != 'renovation']
    cards = [
        f'<a class="mega__card" href="{s["file"]}" {trade_style(s)}{cur(s["file"])}>'
        f'<span class="mega__icon">%I:{s["icon"]}%</span>'
        f'<strong>{s["name"]} <span class="mega__num">{s["num"]}</span></strong>'
        f'<span class="mega__desc">{s["short"]}</span></a>'
        for s in trades
    ]
    sec = lambda name: ' is-section' if section == name else ''
    return f'''<a class="skip-link" href="#contenu">Aller au contenu</a>
<header class="site-header">
  <div class="header__bar">
    <a class="brand" href="index.html" aria-label="USTA Conseils &amp; Travaux — accueil">
      {LOGO_MARK}
      <span class="brand__name">USTA</span>
      <span class="brand__sub">Conseils<br>&amp; Travaux</span>
    </a>
    <nav id="site-nav" class="site-nav" aria-label="Navigation principale">
      <ul class="nav__list">
        <li class="nav__item has-mega{sec('metiers')}">
          <button class="nav__link" type="button" aria-expanded="false" aria-controls="menu-metiers">Métiers %I:chev:chev%</button>
          <div class="mega" id="menu-metiers">
            <div class="mega__col">{cards[0]}{cards[1]}</div>
            <div class="mega__col">{cards[2]}{cards[3]}</div>
            <a class="mega__feature" href="renovation-interieure.html"{cur('renovation-interieure.html')}>
              <span class="mono">Clé en main</span>
              <strong>Rénovation intérieure</strong>
              <span>Tous les métiers, une seule équipe, un seul devis. %I:arrow%</span>
            </a>
          </div>
        </li>
        <li class="nav__item has-drop{sec('renovation')}">
          <button class="nav__link" type="button" aria-expanded="false" aria-controls="menu-renovation">Rénovation %I:chev:chev%</button>
          <div class="drop" id="menu-renovation">
            <a href="renovation-interieure.html#salle-de-bain">Salle de bain clé en main %I:arrow%</a>
            <a href="renovation-interieure.html#cuisine">Rénovation de cuisine %I:arrow%</a>
            <a href="renovation-interieure.html#logement">Appartement &amp; maison %I:arrow%</a>
            <a href="renovation-interieure.html#location">Avant location ou vente %I:arrow%</a>
          </div>
        </li>
        <li class="nav__item"><a class="nav__link" href="index.html#projets">Projets</a></li>
        <li class="nav__item has-drop{sec('entreprise')}">
          <button class="nav__link" type="button" aria-expanded="false" aria-controls="menu-entreprise">L'entreprise %I:chev:chev%</button>
          <div class="drop" id="menu-entreprise">
            <a href="index.html#pourquoi">Pourquoi USTA %I:arrow%</a>
            <a href="index.html#methode">Notre méthode %I:arrow%</a>
            <a href="index.html#zone">Zone d'intervention %I:arrow%</a>
            <a href="index.html#faq">Questions fréquentes %I:arrow%</a>
          </div>
        </li>
        <li class="nav__item nav__item--mobile"><a class="nav__link" href="contact.html"{cur('contact.html')}>Contact</a></li>
      </ul>
      <div class="nav__foot">
        <a class="btn btn--signal btn--lg" href="contact.html" data-track="devis-menu">Demander un devis gratuit %I:arrow:arrow%</a>
        <a class="btn btn--ghost btn--lg" href="%TEL_HREF%" data-track="appel-menu">%I:phone% %TEL%</a>
      </div>
    </nav>
    <div class="header__actions">
      <a class="header__phone" href="%TEL_HREF%" data-track="appel-header"><span class="pulse" aria-hidden="true"></span>%TEL%</a>
      <a class="btn btn--signal btn--sm" href="contact.html" data-track="devis-header">Devis gratuit %I:arrow:arrow%</a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Ouvrir le menu"><span></span><span></span></button>
    </div>
  </div>
</header>'''


def footer(devis_href):
    links = ''.join(f'<li><a href="{s["file"]}">{s["name"]}</a></li>' for s in SERVICES)
    hours = ''.join(f'<li><span>{d}</span><span>{h}</span></li>' for d, h in HOURS)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__about">
        <a class="brand" href="index.html" aria-label="USTA Conseils &amp; Travaux — accueil">
          {LOGO_MARK}
          <span class="brand__name">USTA</span>
          <span class="brand__sub">Conseils<br>&amp; Travaux</span>
        </a>
        <p>Entreprise familiale de rénovation tous corps d'état à %VILLE%. Plomberie, électricité, carrelage, placo : du conseil à la finition, un seul interlocuteur.</p>
        <p class="footer__insurance">%I:shield% <span>Garantie décennale : %PH:Assureur%, contrat n° %PH:XXXX%</span></p>
      </div>
      <div>
        <p class="footer__title">Métiers</p>
        <ul class="footer__links">{links}</ul>
      </div>
      <div>
        <p class="footer__title">Contact</p>
        <address>
          USTA Conseils &amp; Travaux<br>
          %PH:Adresse%<br>
          %PH:Code postal% %VILLE%<br>
          <a href="%TEL_HREF%" data-track="appel-footer">%TEL%</a><br>
          <a href="mailto:%EMAIL%">%EMAIL%</a>
        </address>
      </div>
      <div>
        <p class="footer__title">Horaires</p>
        <ul class="footer__hours">{hours}</ul>
      </div>
    </div>
    <div class="footer__bottom">
      <p>© <span data-year>2026</span> USTA Conseils &amp; Travaux · SIRET %PH:XXX XXX XXX XXXXX%</p>
      <p><a href="mentions-legales.html">Mentions légales</a> · <a href="mentions-legales.html#donnees-personnelles">Données personnelles</a></p>
    </div>
    <p class="footer__word" aria-hidden="true">USTA</p>
  </div>
</footer>
<nav class="mobile-cta" aria-label="Contact rapide">
  <a class="btn btn--ghost" href="%TEL_HREF%" data-track="appel-mobile">%I:phone% Appeler</a>
  <a class="btn btn--signal" href="{devis_href}" data-track="devis-mobile">Devis gratuit %I:arrow:arrow%</a>
</nav>'''


def breadcrumb(page):
    return (f'<nav class="breadcrumb" aria-label="Fil d\'Ariane"><ol><li><a href="index.html">Accueil</a></li>'
            f'<li aria-current="page">{page["crumb"]}</li></ol></nav>')


def faq_html(faqs):
    items = ''.join(f'<details><summary>{q}</summary><div>{a}</div></details>' for q, a in faqs)
    return f'<div class="faq">{items}</div>'


def scene(focus=None, offset='0.7', extra_class=''):
    labels = ''.join(
        f'<span class="scene3d__label" data-layer="{s["slug"]}" {trade_style(s)}><span><b>{s["num"]}</b>{s["label"]}</span></span>'
        for s in SERVICES if s['slug'] != 'renovation'
    )
    focus_attr = f' data-focus="{focus}"' if focus else ''
    return (f'<div class="scene3d {extra_class}" data-scene3d data-offset="{offset}"{focus_attr}>'
            f'<div class="scene3d__stage"></div>{SCENE_FALLBACK}{labels}</div>')


def legend():
    chips = ''.join(
        f'<a class="chip-link" href="{s["file"]}" data-scene-chip data-layer="{s["slug"]}" {trade_style(s)}>'
        f'<i></i>{s["label"]} <span class="mono">{s["num"]}</span></a>'
        for s in SERVICES if s['slug'] != 'renovation'
    )
    return f'''<div class="container hero__legend fade-in" style="--d:1.1s">
      <p class="mono">Survolez un métier pour l'explorer</p>
      <div class="chips">{chips}</div>
    </div>'''


def other_services(current_slug):
    tiles = ''.join(
        f'<a class="tile" href="{s["file"]}" {trade_style(s)} data-tilt="5" data-reveal style="--d:{i}">'
        f'<span class="tile__top"><span class="tile__icon">%I:{s["icon"]}%</span><span class="tile__num">{s["num"]}</span></span>'
        f'<h3>{s["name"]}</h3><p>{s["short"]}</p>'
        f'<span class="tile__more">Découvrir %I:arrow-ur%</span></a>'
        for i, s in enumerate(x for x in SERVICES if x['slug'] != current_slug)
    )
    return f'''<section class="section section--paper-2">
    <div class="container">
      <div class="section-head section-head--split">
        <div>
          <p class="index">Tous corps d'état</p>
          <h2 class="display" data-reveal>Nos autres <em>métiers.</em></h2>
        </div>
        <p class="section-head__text" data-reveal style="--d:1">Un chantier réussi se joue rarement sur un seul métier : nous réalisons aussi le reste, avec la même équipe.</p>
      </div>
      <div class="trades-row">{tiles}</div>
    </div>
  </section>'''


def cta_final(page):
    title, text = page['cta']
    slug = page.get('service', {}).get('slug')
    options = [('plomberie', 'Plomberie'), ('electricite', 'Électricité'), ('carrelage', 'Carrelage'),
               ('placo', 'Placo / plâtrerie'), ('renovation', 'Rénovation complète'), ('autre', 'Autre')]
    opts = ''.join(f'<option value="{v}"{" selected" if v == slug else ""}>{l}</option>' for v, l in options)
    placeholder = '' if slug else '<option value="" disabled selected>Choisir…</option>'
    track = page.get('track', 'page')
    return f'''<section class="cta-final grain" id="devis">
    <div class="container cta-final__grid">
      <div>
        <p class="index">Devis gratuit · Réponse sous 24 h</p>
        <h2 data-reveal>{title}</h2>
        <p class="cta-final__text" data-reveal style="--d:1">{text}</p>
        <a class="bigphone" href="%TEL_HREF%" data-track="appel-{track}-cta"><span class="bigphone__icon">%I:phone%</span>%TEL%</a>
        <p class="hours mono">%HOURS%</p>
      </div>
      <div class="form-card" data-reveal style="--d:2">
        <h3>Être rappelé gratuitement</h3>
        <p>Laissez vos coordonnées : on vous rappelle sous 24 h ouvrées pour parler de votre projet.</p>
        <form class="form" action="%FORM_ACTION%" method="POST" data-lead-form>
          <input type="hidden" name="_subject" value="Demande de rappel — site USTA">
          <input type="hidden" name="source" value="{page['file']} — formulaire de rappel">
          <div class="field">
            <label for="cf-travaux">Type de travaux</label>
            <select class="input" id="cf-travaux" name="travaux" required>{placeholder}{opts}</select>
          </div>
          <div class="form__row">
            <div class="field">
              <label for="cf-nom">Nom</label>
              <input class="input" id="cf-nom" name="nom" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="cf-cp">Code postal</label>
              <input class="input" id="cf-cp" name="code_postal" inputmode="numeric" autocomplete="postal-code" pattern="[0-9]{{5}}" maxlength="5" required>
            </div>
          </div>
          <div class="field">
            <label for="cf-tel">Téléphone</label>
            <input class="input" id="cf-tel" name="telephone" type="tel" autocomplete="tel" minlength="10" placeholder="06 12 34 56 78" required>
          </div>
          <div class="hp" aria-hidden="true"><label>Ne pas remplir <input name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
          <button class="btn btn--signal btn--lg btn--block" type="submit" data-track="form-rappel-{track}">Être rappelé gratuitement %I:arrow:arrow%</button>
          <div class="form-status" role="status" aria-live="polite"></div>
          <p class="form__micro">%I:lock% Gratuit, sans engagement, données confidentielles</p>
        </form>
      </div>
    </div>
  </section>'''


# ------------------------------------------------------------------ données structurées

BIZ_ID = SITE + '/#entreprise'

BUSINESS = {
    '@type': ['GeneralContractor', 'Plumber', 'Electrician'],
    '@id': BIZ_ID,
    'name': 'USTA Conseils & Travaux',
    'description': "Entreprise familiale de rénovation tous corps d'état : plomberie, électricité, carrelage, placo et rénovation intérieure.",
    'url': SITE + '/',
    'logo': SITE + '/assets/img/apple-touch-icon.png',
    'image': SITE + '/assets/img/og-image.png',
    'telephone': '+33600000000',
    'email': EMAIL,
    'priceRange': '€€',
    'address': {'@type': 'PostalAddress', 'streetAddress': '[Adresse]', 'postalCode': '[Code postal]',
                'addressLocality': VILLE, 'addressCountry': 'FR'},
    'areaServed': [{'@type': 'City', 'name': VILLE}],
    'openingHoursSpecification': [
        {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
         'opens': '08:00', 'closes': '18:00'},
        {'@type': 'OpeningHoursSpecification', 'dayOfWeek': 'Saturday', 'opens': '09:00', 'closes': '12:00'},
    ],
    'hasOfferCatalog': {
        '@type': 'OfferCatalog', 'name': 'Travaux de rénovation',
        'itemListElement': [{'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': s['name'], 'url': f'{SITE}/{s["file"]}'}}
                            for s in SERVICES],
    },
}

WEBSITE = {'@type': 'WebSite', '@id': SITE + '/#site', 'url': SITE + '/', 'name': 'USTA Conseils & Travaux',
           'inLanguage': 'fr-FR', 'publisher': {'@id': BIZ_ID}}


def jsonld(page, url):
    graph = [BUSINESS, WEBSITE, {
        '@type': page.get('schema_type', 'WebPage'), '@id': url + '#page', 'url': url,
        'name': strip_tags(page['title']), 'description': page['description'], 'inLanguage': 'fr-FR',
        'isPartOf': {'@id': SITE + '/#site'}, 'about': {'@id': BIZ_ID},
    }]
    if page.get('crumb'):
        graph.append({'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Accueil', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': strip_tags(page['crumb']), 'item': url}]})
    if page.get('service'):
        graph.append({'@type': 'Service', '@id': url + '#service', 'name': page['service']['name'],
                      'serviceType': page['service']['name'], 'description': page['description'], 'url': url,
                      'provider': {'@id': BIZ_ID}, 'areaServed': {'@type': 'City', 'name': VILLE}})
    if page.get('faqs'):
        graph.append({'@type': 'FAQPage', 'mainEntity': [
            {'@type': 'Question', 'name': strip_tags(tokens(q, plain=True)),
             'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(tokens(a, plain=True))}}
            for q, a in page['faqs']]})
    data = {'@context': 'https://schema.org', '@graph': graph}
    return json.dumps(data, ensure_ascii=False, indent=2).replace('</', '<\\/')


# ------------------------------------------------------------------ page

def service_body(svc):
    """Remplit le gabarit des pages métiers avec les textes de services_content.py."""
    d = SERVICE_PAGES[svc['slug']]
    body = (SRC / 'pages' / '_service.html').read_text(encoding='utf-8')
    slug = svc['slug']
    title, text = d['urgent']
    if slug in ('plomberie', 'electricite'):
        urgent = (f'<a class="urgent" href="%TEL_HREF%" data-track="urgence-{slug}"><span class="urgent__icon">%I:alert%</span>'
                  f'<span><strong>{title}</strong> {text}</span></a>')
    else:
        urgent = (f'<a class="urgent" href="contact.html?service={slug}" data-track="visite-{slug}"><span class="urgent__icon">%I:bulb%</span>'
                  f'<span><strong>{title}</strong> {text}</span></a>')
    items = []
    for i, item in enumerate(d['prestations'], 1):
        anchor = f' id="{item[2]}"' if len(item) > 2 else ''
        items.append(f'<article class="service-item"{anchor} data-reveal style="--d:{(i - 1) % 2}">'
                     f'<span class="mono">{i:02d}</span><h3>{item[0]}</h3><p>{item[1]}</p></article>')
    adv = f'<p class="lead" data-reveal style="--d:1">{d["adv_text"]}</p>'
    if d.get('adv_timeline'):
        adv += '<ol class="timeline" data-reveal style="--d:2">' + ''.join(
            f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in d['adv_timeline']) + '</ol>'
    else:
        adv += '<ul class="checks" data-reveal style="--d:2">' + ''.join(
            f'<li>%I:check% <span>{c}</span></li>' for c in d['adv_checks']) + '</ul>'
    fields = {
        '{{SLUG}}': slug, '{{H1}}': d['h1'], '{{H1_SMALL}}': d['h1_small'], '{{LEAD}}': d['lead'],
        '{{CTA_LABEL}}': d['cta_label'], '{{URGENT}}': urgent, '{{PRESTA_TITLE}}': d['presta_title'],
        '{{PRESTA_INTRO}}': d['presta_intro'], '{{PRESTATIONS}}': ''.join(items), '{{ADV_TITLE}}': d['adv_title'],
        '{{ADV_BODY}}': adv, '{{TIP}}': d['tip'], '{{FAQ_TITLE}}': d['faq_title'],
    }
    for k, v in fields.items():
        body = body.replace(k, v)
    return body


def render(page):
    file = page['file']
    url = SITE + '/' + ('' if file == 'index.html' else file)
    devis_href = page.get('devis_href', 'contact.html')
    svc = page.get('service', {})
    body = service_body(svc) if svc else (SRC / 'pages' / file).read_text(encoding='utf-8')
    replacements = {
        '{{BREADCRUMB}}': breadcrumb(page) if 'crumb' in page else '',
        '{{FAQ}}': faq_html(page.get('faqs', [])),
        '{{SCENE_HOME}}': scene(extra_class='scene3d--hero'),
        '{{SCENE_FOCUS}}': scene(focus=svc.get('slug'), offset='0.72') if svc else '',
        '{{LEGEND}}': legend(),
        '{{OTHER_SERVICES}}': other_services(svc.get('slug')) if svc else '',
        '{{CTA_FINAL}}': cta_final(page) if page.get('cta') else '',
        '{{TRADE_STYLE}}': trade_style(svc) if svc else '',
        '{{TRADE_TAG}}': (f'<p class="trade-tag" {trade_style(svc)}><i></i>{svc["num"]} — {svc["label"]}</p>' if svc else ''),
    }
    for k, v in replacements.items():
        body = body.replace(k, v)

    robots = '<meta name="robots" content="noindex, follow">\n' if page.get('noindex') else ''
    base = f'<base href="{page["base"]}">\n' if page.get('base') else ''
    title = html.escape(page['title'], quote=False)
    desc = html.escape(page['description'])

    doc = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{base}<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
{robots}<meta name="theme-color" content="#0E0E0C">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="USTA Conseils &amp; Travaux">
<meta property="og:title" content="{html.escape(page.get('og_title', page['title']))}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/archivo-variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
<script>document.documentElement.classList.add('js');setTimeout(function(){{if(!window.__usta)document.documentElement.classList.remove('js')}},3000)</script>
<script src="assets/js/main.js" defer></script>
<script type="application/ld+json">
{jsonld(page, url)}
</script>
</head>
<body>
{sprite()}
{header(page)}

{body.strip()}

{footer(devis_href)}
</body>
</html>
'''
    doc = french_typo(tokens(doc))
    leftovers = re.findall(r'%[A-Z_:]+%|\{\{[A-Z_]+\}\}', doc)
    assert not leftovers, f'{file}: jetons non remplacés {leftovers}'
    (OUT / file).write_text(doc, encoding='utf-8')
    return file


def sitemap(pages):
    urls = []
    for p in pages:
        if p.get('noindex'):
            continue
        loc = SITE + '/' + ('' if p['file'] == 'index.html' else p['file'])
        prio = '1.0' if p['file'] == 'index.html' else ('0.9' if p.get('service') else '0.6')
        urls.append(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{LASTMOD}</lastmod>\n    <priority>{prio}</priority>\n  </url>')
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + '\n'.join(urls) + '\n</urlset>\n')
    (OUT / 'sitemap.xml').write_text(xml, encoding='utf-8')


if __name__ == '__main__':
    for p in PAGES:
        print('ok', render(p))
    sitemap(PAGES)
    (OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n', encoding='utf-8')
    print('ok sitemap.xml robots.txt')
