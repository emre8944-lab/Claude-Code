# Site USTA Conseils & Travaux — version 1 (exemple de travail)

Site vitrine de l'entreprise familiale USTA Conseils & Travaux (plomberie, électricité,
carrelage, placo, rénovation intérieure). Pensé pour **transformer les visiteurs en demandes
de devis** et **ressortir sur Google pour les recherches locales** (« plombier + ville »,
« carreleur + ville »…).

HTML, CSS et JavaScript simples : aucun framework, aucune dépendance, aucun cookie.

## Voir le site

Double-cliquer sur `index.html`. Pour un rendu identique à la mise en ligne :

```bash
cd site-usta
python3 -m http.server 8000   # puis ouvrir http://localhost:8000
```

## Pages

| Fichier | Rôle | Recherche Google visée |
|---|---|---|
| `index.html` | Accueil : proposition de valeur, formulaire de rappel, métiers, méthode, réalisations, avis, zone, FAQ | « artisan rénovation [ville] » |
| `plomberie.html` | Page métier | « plombier [ville] » |
| `electricite.html` | Page métier | « électricien [ville] » |
| `carrelage.html` | Page métier | « carreleur [ville] » |
| `placo-platrerie.html` | Page métier | « plaquiste [ville] » |
| `renovation-interieure.html` | Rénovation clé en main | « rénovation salle de bain [ville] » |
| `contact.html` | Formulaire de devis complet | — |
| `merci.html` | Confirmation après envoi (sert aussi à mesurer les conversions) | non indexée |
| `mentions-legales.html` | Mentions légales, RGPD, assurance, médiateur | non indexée |
| `404.html` | Page introuvable | non indexée |

Autres fichiers : `assets/css/style.css`, `assets/js/main.js`, `assets/img/` (logo, favicon,
image de partage réseaux sociaux), `sitemap.xml`, `robots.txt`.

## À remplacer avant la mise en ligne

Dans le navigateur, **tout ce qui est surligné en jaune** (texte entre crochets) et
**tous les encadrés « À faire »** sont à compléter ou à supprimer.

Dans le code, rechercher (dans tous les fichiers) :

| Rechercher | Remplacer par |
|---|---|
| `[Ville]` | la ville principale (dans les titres, textes et données structurées) |
| `[XX]`, `[année]`, `[Commune…]`, `[Adresse]`, `[Code postal]`, `[SIRET…]`, `[Assureur]`… | les vraies informations |
| `06 00 00 00 00`, `+33600000000`, `33600000000` | le vrai numéro (affiché, lien d'appel, lien WhatsApp) |
| `contact@votre-domaine.fr` | la vraie adresse e-mail |
| `https://www.votre-domaine.fr` | le nom de domaine (y compris dans `sitemap.xml` et `robots.txt`) |
| `VOTRE_ID` | l'identifiant du formulaire Formspree (voir ci-dessous) |
| `Lun – Ven 8h – 18h`, `8h – 18h`… et `openingHoursSpecification` | les vrais horaires |
| `class="dev-note"` | supprimer ces encadrés une fois le contenu en place |
| `class="ph"` | une fois le texte remplacé, retirer le `<span class="ph">` autour |

Le bouton « Voir tous nos avis Google » (accueil) doit pointer vers votre fiche Google.

**Important :** ne jamais inventer d'avis clients, de chiffres (« 500 chantiers ») ou de
labels (RGE, Qualibat) que l'entreprise n'a pas : c'est interdit et sanctionné.

## Le formulaire de devis

Le site étant statique, les formulaires passent par un service d'envoi d'e-mails.
Réglage par défaut : [Formspree](https://formspree.io) (gratuit jusqu'à 50 envois/mois).

1. Créer un compte Formspree et un formulaire → récupérer l'identifiant (ex. `xyzabcd`).
2. Remplacer `VOTRE_ID` par cet identifiant dans `index.html` et `contact.html`.
3. Faire un envoi de test.

Tant que `VOTRE_ID` est présent, le formulaire reste en **mode démonstration** (il affiche un
message au lieu d'envoyer). Si l'envoi échoue, le visiteur voit le numéro de téléphone.
Formspree est hébergé aux États-Unis ; un équivalent européen peut le remplacer sans toucher
au reste (il suffit de changer l'adresse `action` du formulaire).

## Ce qui est en place pour la conversion

- Téléphone cliquable partout, **barre « Appeler / Devis gratuit » fixe sur mobile**.
- Formulaire de rappel court (4 champs) dès le haut de l'accueil, formulaire complet sur `contact.html`.
- Chaque page métier pré-coche le bon type de travaux dans le formulaire (`contact.html?service=plomberie`).
- Réassurance : décennale, devis gratuit sous 48 h, entreprise familiale, méthode en 4 étapes.
- Argument différenciant : **un seul interlocuteur pour tous les corps de métier** (comparatif).
- Réponses aux objections (FAQ), encadré « urgence » sur plomberie et électricité.
- Clics sur les boutons marqués (`data-track`) : prêts pour Google Tag Manager le jour où il sera ajouté.

## Ce qui est en place pour le SEO

- Une page par métier avec un contenu **unique** (pas de copier-coller entre les pages).
- Titres, méta-descriptions, un seul `h1` par page, fil d'Ariane, maillage interne entre métiers.
- Données structurées schema.org : entreprise locale (adresse, horaires, zone, services),
  pages service, fil d'Ariane, FAQ.
- `sitemap.xml`, `robots.txt`, URL canoniques, balises de partage (Open Graph).
- Site très léger (pas d'images lourdes, pas de police externe, pas de framework) → rapide sur mobile.
- Pas de cookie → pas de bandeau de consentement nécessaire.

## Prochaines étapes (par ordre d'impact)

1. **Fiche Google Business Profile** : c'est le levier n°1 pour un artisan local (carte Google).
   Même nom, adresse et téléphone que sur le site.
2. **Vraies photos de chantiers** (avant/après) dans la section Réalisations.
3. **Avis clients** : demander systématiquement un avis Google en fin de chantier, puis en reprendre quelques-uns sur le site.
4. Nom de domaine + hébergement (Netlify, OVH, o2switch…), puis **Google Search Console** avec envoi du `sitemap.xml`.
5. Si RGE / Qualibat / autre label : l'ajouter dans la barre de confiance (fort impact sur la confiance).
6. Page « Réalisations » dédiée avec un cas détaillé par chantier (budget, durée, photos).
7. Pages par commune **uniquement avec du contenu réellement local** (chantiers réalisés sur place),
   sinon Google les considère comme des pages satellites.
8. Mesure d'audience sans cookie (Plausible, Matomo configuré en mode exempté) pour suivre les appels et les devis.

Note technique : l'en-tête et le pied de page sont répétés dans chaque fichier HTML. Si le site
grossit (blog, pages par commune), passer à un générateur de site statique (ex. Eleventy)
évitera de les modifier page par page.
