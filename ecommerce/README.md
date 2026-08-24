# Cursus e-commerce — créer, développer et gérer une marque

> **Objectif de l'élève :** 1 000 000 € de chiffre d'affaires par semaine, avec une
> marge nette qui tient.
>
> **Objectif du cursus :** te donner l'arithmétique, les mécanismes et les rituels
> qui rendent ce nombre atteignable — et te dire honnêtement, à chaque étape, si tu
> es sur la trajectoire ou non.

---

## Avant tout : ce que 1 M€/semaine veut dire vraiment

C'est ~52 M€ TTC par an. Dans le modèle de référence de ce cursus, ce chiffre
d'affaires produit **10,1 % d'EBITDA**, soit 4,4 M€ par an. La même entreprise,
pilotée sur la marge au lieu du volume, en produit **20,3 %**, soit 8,8 M€ — pour
exactement le même chiffre d'affaires.

Ce n'est pas une nuance de comptable. C'est **4,4 millions d'euros par an d'écart**
qui ne dépendent d'aucune vente supplémentaire.

Donc, dès la première page : **le chiffre d'affaires n'est pas l'objectif, c'est une
conséquence.** Ta destination n'est pas P5. C'est P5+.

Physiquement, 1 M€/semaine, c'est :

| | |
|---|---:|
| Commandes par jour | ~1 984 |
| Dépense publicitaire par jour | ~49 151 € |
| Concepts publicitaires **nouveaux** à tester par semaine | ~57 |
| Personnes (ETP) | ~38 |
| Besoin en fonds de roulement | ~2 264 655 € |
| EBITDA mensuel | ~364 752 € |

Tous ces nombres viennent du même modèle, vérifiable et reproductible :
[`donnees/chiffres-canoniques.md`](donnees/chiffres-canoniques.md), généré par
[`outils/modele_nora.py`](outils/modele_nora.py).

---

## Le principe directeur

> Ta marge est le prix d'une asymétrie. Ton chiffre d'affaires est le prix de
> l'attention que tu loues. **La seule question qui compte est de savoir laquelle
> des deux tu construis.**

Le cursus racine de ce dépôt démontre d'où vient la marge (asymétries
d'information, distinctivité, unit economics). **Celui-ci est le cursus
d'exécution** : comment on fabrique, jour après jour, une marque qui capture cette
marge à l'échelle. Les deux se lisent ensemble — je renvoie constamment de l'un à
l'autre.

---

## Comment ce cursus est construit

Une marque fictive, **NØRA** (soin capillaire premium, vendu en direct en Europe),
traverse l'intégralité du programme. Ses chiffres sont figés dans un modèle unique
et cohérent, du premier euro de chiffre d'affaires jusqu'à 1 M€ par semaine.

Chaque module, chaque étude de cas, chaque exercice s'appuie sur les **mêmes**
nombres. Quand un module te dit qu'un point de taux de retour vaut 433 320 € par
an, ce n'est pas une formule : c'est calculé, et tu peux relancer le calcul.

> **NØRA est une marque fictive**, et le cursus le répète partout. Le modèle est
> calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes réels
> d'aucune entreprise. Aucun chiffre financier privé n'est attribué à une marque
> existante — quand une source est publique, elle est citée comme telle.

Les cinq paliers du parcours :

| Palier | Période | CA TTC/semaine | EBITDA | Ce qui s'y joue |
|---|---|---:|---:|---|
| **P1 — Validation** | M1–M3 | 8 492 € | −30,7 % | Le produit mérite-t-il d'exister |
| **P2 — Traction** | M4–M9 | 53 123 € | −10,3 % | **La vallée de la mort** |
| **P3 — Scale France** | M10–M18 | 271 662 € | +5,2 % | La machine créative tient-elle |
| **P4 — Multi-pays** | M19–M30 | 676 523 € | +8,1 % | L'organisation et le cash tiennent-ils |
| **P5 — 1 M€/sem.** | M31–M40 | 999 968 € | +10,1 % | Le volume est atteint |
| **P5+ — pilotage marge** | M41+ | 999 978 € | **+20,3 %** | **La vraie destination** |

---

## Par où commencer

**1. Fais le [diagnostic](mentorat/diagnostic.md)** — 30 minutes. Il te place, et
surtout il détermine ce qu'on va **ignorer**. Travailler le bon sujet au mauvais
moment est la façon la plus courante de perdre un an.

**2. Lis le [protocole de mentorat](mentorat/protocole.md)** — comment on travaille
ensemble, ce que je fais, ce que je ne ferai pas, et ce que tu m'envoies chaque
semaine.

**3. Lis le socle, dans cet ordre — pas dans l'ordre des numéros :**

| Ordre | Module | Ce qu'il te donne |
|---|---|---|
| 1ᵉʳ | [**E00 — Le cadrage**](modules/E00-cadrage.md) | Ce métier vraiment, et les cinq façons d'y mourir |
| 2ᵉ | [**E01 — L'arithmétique**](modules/E01-arithmetique-de-la-marque.md) | Les six nombres qui décident. **Le module central.** |
| 3ᵉ | [**E02 — Marché et produit**](modules/E02-marche-et-produit.md) | Si ta catégorie autorise ton objectif |
| 4ᵉ | [**E14 — Le plan**](modules/E14-plan-1M-semaine.md) | La carte entière, pour savoir où tu es dessus |

**4. Puis suis le parcours de ton niveau**, décrit dans le
[protocole § 3](mentorat/protocole.md).

---

## Le programme

### Les modules

| Code | Module | Ce qu'il traite |
|---|---|---|
| **E00** | [Le cadrage](modules/E00-cadrage.md) | Les quatre façons de gagner, les cinq modes de mort, le capital réellement nécessaire |
| **E01** | [L'arithmétique de la marque](modules/E01-arithmetique-de-la-marque.md) | Cascade des marges, MER et son seuil, nCAC, LTV en contribution, payback, sensibilité |
| **E02** | [Marché et produit](modules/E02-marche-et-produit.md) | Structure de catégorie, grille de sélection, six tests de demande, sourcing |
| **E03** | [L'offre et le prix](modules/E03-offre-et-prix.md) | Élasticité, gamme, les six leviers de panier moyen, le coût réel d'une remise |
| **E04** | [Le client dans sa tête](modules/E04-psychologie-du-client.md) | Niveaux de conscience, chaîne de croyance, objections, hiérarchie des preuves, recherche client |
| **E05** | [La machine créative](modules/E05-machine-creative.md) | Le vrai goulot : anatomie, production, jugement, itération, fatigue |
| **E06** | [L'acquisition payante](modules/E06-acquisition-payante.md) | Mécanique de l'enchère, signal, structure de compte, CAC marginal, saturation |
| **E07** | [Le funnel et la conversion](modules/E07-funnel-et-conversion.md) | Chaîne de déperdition, continuité du message, page produit, paiement, vitesse |
| **E08** | [La rétention et la LTV](modules/E08-retention-et-ltv.md) | Cohortes, premier réachat, calendrier de consommation, CRM, abonnement |
| **E09** | [Mesurer](modules/E09-mesure-et-incrementalite.md) | Attribution, incrémentalité, test géographique, bruit, tableau de bord à trois niveaux |
| **E10** | [Le cash et les opérations](modules/E10-cash-et-operations.md) | BFR, financement, stock, logistique, retours, SAV, fournisseurs |
| **E11** | [Passer à l'échelle](modules/E11-passage-a-echelle.md) | Saturation nationale, ouverture de marché, organisation par palier, systèmes |
| **E12** | [La marque comme actif](modules/E12-marque-et-actif.md) | Performance contre marque, distinctivité, capital de marque, valorisation |
| **E13** | [Le risque de ruine](modules/E13-risque-de-ruine.md) | Bannissement, dépendance, conformité, fraude, registre des risques |
| **E14** | [Le plan 1 M€/semaine](modules/E14-plan-1M-semaine.md) | Le chemin chiffré, les conditions de passage, le passage de P5 à P5+ |

### Les études de cas

Chiffrées, avec questions et corrigés. **Fais les questions avant de lire le
corrigé** — sinon tu confondras la reconnaissance et la compréhension.

| Code | Cas | La leçon |
|---|---|---|
| **C01** | [Le produit à ×2,5](etudes-de-cas/C01-coefficient-insuffisant.md) | Le coefficient est décidé avant la première vente et plafonne tout |
| **C02** | [La vallée de la mort](etudes-de-cas/C02-vallee-de-la-mort.md) | Les neuf premiers mois de NØRA, trésorerie comprise |
| **C03** | [Anatomie d'un concept gagnant](etudes-de-cas/C03-anatomie-creative-gagnante.md) | La performance créative est une distribution à queue épaisse |
| **C04** | [41 M€ de CA, 5,8 M€ de perte](etudes-de-cas/C04-scale-qui-detruit-la-marge.md) | La croissance achetée par la remise détruit de la valeur |
| **C05** | [Le CAC à 2,4× le panier](etudes-de-cas/C05-abonnement-et-cac-negatif.md) | Un CAC ne se juge jamais contre un panier |
| **C06** | [Le test d'incrémentalité](etudes-de-cas/C06-test-incrementalite.md) | Un ROAS élevé signale une récolte, pas une création de demande |
| **C07** | [Ouvrir l'Allemagne](etudes-de-cas/C07-ouverture-allemagne.md) | Le produit se transfère, le message non |
| **C08** | [Redressement en 90 jours](etudes-de-cas/C08-redressement-90-jours.md) | Quand la marge est négative, la croissance multiplie la perte |
| **C09** | [Le piège du Black Friday](etudes-de-cas/C09-piege-du-black-friday.md) | Une promotion se juge sur la cohorte à 12 mois |
| **C10** | [Compte publicitaire banni](etudes-de-cas/C10-compte-publicitaire-banni.md) | La dépendance à un canal est un risque de ruine |

### Le mentorat

| Fichier | Usage |
|---|---|
| [protocole.md](mentorat/protocole.md) | Le contrat, les niveaux, le parcours de lecture, le rythme |
| [diagnostic.md](mentorat/diagnostic.md) | Le questionnaire d'entrée, chiffré, avec placement et prescription |
| [jalons.md](mentorat/jalons.md) | Les conditions binaires de passage de chaque palier |
| [tableau-de-bord.md](mentorat/tableau-de-bord.md) | Les définitions, les trois niveaux d'indicateurs, le formulaire hebdomadaire |
| [revue-hebdomadaire.md](mentorat/revue-hebdomadaire.md) | Le rituel de 45 minutes qui produit une décision par semaine |

### Les outils

Tous en Python 3, sans aucune dépendance externe. Chacun a un mode `--demo`.

| Outil | Ce qu'il calcule |
|---|---|
| [`modele_nora.py`](outils/modele_nora.py) | Le modèle canonique du cursus. Change une hypothèse, relance, tout reste cohérent |
| [`calculateur.py`](outils/calculateur.py) | Ta cascade de marges, ton MER seuil, ta LTV/CAC, ton verdict |
| [`simulateur_tresorerie.py`](outils/simulateur_tresorerie.py) | Ton point bas de trésorerie et ta croissance maximale autofinançable |
| [`test_significativite.py`](outils/test_significativite.py) | Combien de données il te faut avant d'avoir le droit de conclure |
| [`plan_objectif.py`](outils/plan_objectif.py) | Ton objectif de CA traduit en commandes, budget, créas, personnes, cash |
| [`cohortes.py`](outils/cohortes.py) | Ton tableau de cohortes depuis un export de commandes, et l'alerte de dégradation |

### Les modèles opérationnels

| Modèle | Usage |
|---|---|
| [brief-creatif.md](modeles/brief-creatif.md) | Obtenir une vidéo exploitable du premier coup |
| [protocole-test-creatif.md](modeles/protocole-test-creatif.md) | Décider avant de tester, pas après |
| [checklist-page-produit.md](modeles/checklist-page-produit.md) | Auditer une page produit, notée sur 100 |
| [sequences-crm.md](modeles/sequences-crm.md) | Les séquences courriel et SMS, rédigées |
| [protocole-test-geographique.md](modeles/protocole-test-geographique.md) | Mesurer l'incrémentalité réelle d'un canal |
| [plan-ouverture-pays.md](modeles/plan-ouverture-pays.md) | Ouvrir un marché sans le rater |
| [cahier-des-charges-fournisseur.md](modeles/cahier-des-charges-fournisseur.md) | Spécifier et négocier — dont le délai de paiement |
| [registre-des-risques.md](modeles/registre-des-risques.md) | Rendre survivable ce qui peut te ruiner |

---

## La méthode

Chaque module suit le même cycle :

1. **Le mécanisme** — la structure économique, avec ses conditions de validité.
2. **La démonstration** — le calcul déroulé, pas l'affirmation.
3. **Le transfert** — appliqué à NØRA, chiffres à l'appui.
4. **Les limites** — quand le modèle est faux, et quel module le contredit.
5. **L'exercice** — appliqué à **ton** activité. C'est la seule partie qui crée de
   la compétence.

**Règle du cursus : tu ne passes pas au module suivant sans avoir rendu
l'exercice.** Lire produit le *sentiment* d'apprendre, ce qui est pire que rien,
parce que ça arrête la recherche.

Les exercices se rendent dans [`exercices/`](exercices/). Les corrigés sont dans le
même dossier — ne les ouvre pas avant d'avoir rendu.

---

## Ce que ce cursus refuse de faire

- **Te promettre un délai.** « En 90 jours tu feras X » est une phrase de vendeur.
- **Enseigner des astuces de plateforme.** Elles meurent en 6 à 18 mois. Les
  mécanismes économiques, non. Quand j'enseigne quelque chose de daté, je le dis.
- **Te cacher la distribution des résultats.** L'immense majorité des marques ne
  dépasse jamais quelques dizaines de milliers d'euros par mois. Ce n'est
  généralement pas une question de motivation : c'est une question de structure,
  décidée très tôt et très difficile à changer ensuite. Le
  [diagnostic](mentorat/diagnostic.md) te dit franchement où tu te situes.
- **Inventer des chiffres pour impressionner.** Tout nombre de ce cursus est soit
  calculé et reproductible, soit déclaré comme hypothèse, soit sourcé.

---

## Structure des fichiers

```
ecommerce/
├── README.md                 ← tu es ici
├── CHARTE.md                 ← les règles de rédaction du cursus
├── modules/                  ← E00 à E14, les cours
├── etudes-de-cas/            ← C01 à C10, chiffrées, avec corrigés
├── exercices/                ← tes rendus et les corrigés
├── mentorat/                 ← protocole, diagnostic, jalons, tableau de bord, rituel
├── outils/                   ← les calculateurs Python
├── modeles/                  ← les documents opérationnels prêts à l'emploi
└── donnees/
    └── chiffres-canoniques.md  ← généré, la source de vérité chiffrée
```

Pour régénérer les chiffres après avoir modifié une hypothèse :

```bash
python3 ecommerce/outils/modele_nora.py --ecrire
```

---

*Commence par le [diagnostic](mentorat/diagnostic.md).*
