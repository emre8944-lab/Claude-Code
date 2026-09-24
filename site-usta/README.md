# Site USTA Conseils & Travaux — v2

Site vitrine de l'entreprise familiale USTA Conseils & Travaux (plomberie, électricité, carrelage,
placo, rénovation intérieure). Objectifs : **une image de marque forte**, **des demandes de devis**
et **une bonne visibilité sur Google pour les recherches locales** (« plombier + ville »…).

## Voir le site

- Ouvrir `public/index.html` dans un navigateur (double-clic), ou
- `npm run serve` puis ouvrir http://localhost:8000 (rendu identique à la mise en ligne).

**Mettre en ligne = envoyer le contenu du dossier `public/`** chez l'hébergeur (Netlify, OVH, o2switch…).
Le dossier `src/` sert uniquement à générer les pages.

## Organisation

```
site-usta/
├── public/                  ← le site à mettre en ligne (HTML généré + ressources)
│   ├── *.html
│   └── assets/
│       ├── css/style.css    ← toute l'identité visuelle
│       ├── js/main.js       ← menus, animations, formulaires
│       ├── js/scene3d.js    ← maquette 3D (fichier généré, ne pas modifier à la main)
│       ├── fonts/           ← polices hébergées sur le site (pas de Google Fonts → RGPD)
│       └── img/             ← logo, favicon, image de partage réseaux sociaux
└── src/                     ← sources
    ├── build.py             ← CONFIG (ville, téléphone…) + en-tête, menu, pied de page
    ├── content.py           ← titres Google, descriptions, FAQ de chaque page
    ├── services_content.py  ← textes des 5 pages métiers
    ├── pages/               ← contenu de l'accueil, contact, mentions légales, 404, merci
    │   └── _service.html    ← gabarit commun des pages métiers
    └── js/scene3d.js        ← source de la maquette 3D (Three.js)
```

### Modifier le site

```bash
npm install          # une seule fois (Three.js + esbuild pour la 3D)
npm run build        # régénère public/ (3D + pages HTML)
npm run build:html   # seulement les pages (Python 3, sans dépendance)
```

Ne pas modifier les fichiers HTML de `public/` à la main : ils sont écrasés à chaque génération.

## À compléter avant la mise en ligne

1. **Dans `src/build.py`, section CONFIG** (répercuté partout, y compris dans les données Google) :
   `VILLE`, `RAYON`, `TEL`, `TEL_HREF`, `WHATSAPP`, `EMAIL`, `SITE` (nom de domaine), `HOURS`, `FORM_ACTION`.
2. **Textes entre crochets** encore présents dans les sources (`[Adresse]`, `[Code postal]`, `[SIRET…]`,
   `[Assureur]`, `[XXXX]`, `[30]`…) : rechercher `%PH:` dans `src/` et `[` dans `src/pages/mentions-legales.html`.
   Adresse et code postal sont aussi dans `BUSINESS` (`src/build.py`).
3. **Mentions légales** : forme juridique, SIRET, TVA, hébergeur, assureur décennale, médiateur de la consommation.
4. **Formulaire** : créer un formulaire gratuit sur [Formspree](https://formspree.io) et remplacer `VOTRE_ID`
   dans `FORM_ACTION`. Tant que ce n'est pas fait, le formulaire affiche un message « mode démonstration ».
   (Formspree est hébergé aux États-Unis ; un service européen peut le remplacer en changeant juste l'adresse.)

**Ne jamais inventer** d'avis clients, de chiffres (« 500 chantiers ») ni de labels (RGE, Qualibat) :
c'est interdit et sanctionné. Les chiffres affichés (48 h, 24 h, 10 ans, 1 contact) sont des
engagements de service : à ajuster s'ils ne correspondent pas à votre fonctionnement.

## Identité visuelle

- **Concept** : « le plan, puis le chantier ». Fond encre, papier, orange signal, annotations
  façon plan d'architecte (police à chasse fixe, repères, numérotation).
- **Couleurs** : encre `#0E0E0C`, papier `#F2F0EB`, orange signal `#FF5A1F`.
- **Code couleur des métiers** (repris dans la 3D, le menu et les formulaires) :
  plomberie bleu `#3D7BFF`, électricité jaune `#FFC53D`, carrelage vert d'eau `#2BB5A0`, placo plâtre `#C9C4B8`.
- **Typographie** : Archivo (largeur variable, version élargie pour les titres) + JetBrains Mono pour les annotations.
- **Logo** : le toit et le « U » de USTA, en noir sur carré orange.

## La maquette 3D

Sur l'accueil, une pièce en coupe se construit couche par couche : carrelage, réseau de plomberie,
circuits électriques, cloisons en placo, et le toit orange du logo qui flotte au-dessus.
Les métiers s'allument à tour de rôle ; survoler un métier sous le titre le met en avant ;
en faisant défiler, la maison « s'éclate » en couches. Sur chaque page métier, la même maquette
met en avant le métier concerné.

Performances : la 3D se charge **après** la page (elle ne retarde pas l'affichage), s'arrête quand elle
n'est plus visible, se simplifie sur mobile, et un dessin fixe la remplace si le navigateur ne gère
pas la 3D ou si le visiteur a demandé à réduire les animations.

## Conversion et SEO

- Téléphone toujours visible, barre « Appeler / Devis gratuit » fixe sur mobile, formulaire de rappel
  en fin de chaque page, pré-rempli selon le métier.
- Une page par métier au contenu unique, titres et descriptions optimisés, fil d'Ariane, FAQ,
  données structurées schema.org (entreprise locale, services, FAQ), `sitemap.xml`, `robots.txt`.
- Site léger, polices et 3D hébergées sur le site, aucun cookie (pas de bandeau nécessaire).
- Clics sur les boutons marqués `data-track`, prêts pour Google Tag Manager.

## Prochaines étapes (par ordre d'impact)

1. **Fiche Google Business Profile** (levier n°1 pour un artisan local), avec les mêmes nom, adresse, téléphone.
2. **Photos réelles de chantiers** (avant/après) : une page ou une section « Réalisations ».
3. **Avis Google** demandés à chaque fin de chantier, puis une section avis sur le site.
4. Nom de domaine, hébergement, puis **Google Search Console** avec envoi du sitemap.
5. Labels éventuels (RGE, Qualibat…) dans le hero et le pied de page.
6. Pages par commune **seulement avec du contenu réellement local** (chantiers réalisés sur place).
7. Mesure d'audience sans cookie (Plausible, ou Matomo en mode exempté).
