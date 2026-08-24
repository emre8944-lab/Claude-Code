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

Le cursus se parcourt sur **deux échelles indépendantes** — ne les confonds jamais :

| Échelle | Ce qu'elle mesure | Où |
|---|---|---|
| **Lxx — de L00 à L10** | Ta **compétence**, validée par des épreuves notées | [`parcours/`](parcours/README.md) |
| **Nx — de N0 à N4** | L'état de ton **business** | [`mentorat/diagnostic.md`](mentorat/diagnostic.md) |

On peut être L07 sans entreprise. On peut être N3 avec une compétence L04 — une
marque à 500 000 € par mois pilotée par quelqu'un qui n'a jamais calculé un CAC
marginal. **Ce second cas est le plus dangereux du métier, et le plus fréquent.**
Garde ton niveau L au-dessus de ton niveau N.

Dans l'ordre :

**1. Le [diagnostic](mentorat/diagnostic.md)** — 30 minutes. Il place ton business
et détermine ce qu'on va **ignorer**. Travailler le bon sujet au mauvais moment est
la façon la plus courante de perdre un an.

**2. Le [parcours](parcours/README.md), à partir de [L00](parcours/L00-novice.md)** —
même si tu penses le dépasser. L'épreuve L00 se passe en 25 minutes et révèle presque
toujours deux automatismes manquants.

**3. L'[atelier](atelier/README.md), à partir de [S01](atelier/S01-choisir-le-terrain.md)** —
tu construis réellement une marque, séance par séance, sur ton projet ou sur un
projet fictif.

**4. Le [simulateur](outils/simulateur_marque.py)** — tu joues la création d'une
marque mois par mois et tu vois les conséquences chiffrées de chaque décision.

```bash
python3 ecommerce/outils/simulateur_marque.py --comparer
```

> **Pourquoi les trois, et pas seulement les cours.** Un module peut t'expliquer que
> couper le budget de test créatif tue une marque en six mois. L'atelier te fait
> construire la machine créative de tes mains. Le simulateur te fait **vivre**
> l'extinction : tu joues la stratégie sans test, tu regardes ton compte s'éteindre
> mois après mois, et tu n'oublies plus. Une erreur simulée coûte dix minutes. La
> même erreur réelle coûte deux ans.

**5. Le socle théorique, dans cet ordre — pas dans l'ordre des numéros :**

| Ordre | Module | Ce qu'il te donne |
|---|---|---|
| 1ᵉʳ | [**E00 — Le cadrage**](modules/E00-cadrage.md) | Ce métier vraiment, et les cinq façons d'y mourir |
| 2ᵉ | [**E01 — L'arithmétique**](modules/E01-arithmetique-de-la-marque.md) | Les six nombres qui décident. **Le module central.** |
| 3ᵉ | [**E02 — Marché et produit**](modules/E02-marche-et-produit.md) | Si ta catégorie autorise ton objectif |
| 4ᵉ | [**E14 — Le plan**](modules/E14-plan-1M-semaine.md) | La carte entière, pour savoir où tu es dessus |

---

## Les trois activités

Aucune ne suffit seule. Le parcours les combine à chaque niveau.

| Activité | Où | Ce que ça produit |
|---|---|---|
| **Tu lis** | [`modules/`](modules/) et [`etudes-de-cas/`](etudes-de-cas/) | Les mécanismes |
| **Tu construis** | [`atelier/`](atelier/README.md) — 12 séances | Les livrables réels d'une marque |
| **Tu joues** | [`outils/simulateur_marque.py`](outils/simulateur_marque.py) | Les conséquences, en accéléré |

### Les onze niveaux

| Niveau | Nom | Épreuve de passage |
|---|---|---|
| [L00](parcours/L00-novice.md) | Novice | 25 questions, dont 10 calculs |
| [L01](parcours/L01-initie.md) | Initié | Dossier chiffré, 3 erreurs à trouver |
| [L02](parcours/L02-praticien.md) | Praticien | 3 dossiers produits, tu choisis et tu prouves |
| [L03](parcours/L03-operateur.md) | Opérateur | Corpus client brut → angle, script, page |
| [L04](parcours/L04-acquereur.md) | Acquéreur | 8 semaines de données → allocation budgétaire |
| [L05](parcours/L05-constructeur.md) | Constructeur | 12 concepts à juger + cohortes à diagnostiquer |
| [L06](parcours/L06-gestionnaire.md) | Gestionnaire | Plan de redressement à 90 jours |
| [L07](parcours/L07-stratege.md) | Stratège | Test géographique biaisé à corriger |
| [L08](parcours/L08-batisseur.md) | Bâtisseur | Plan d'ouverture de marché + organigramme |
| [L09](parcours/L09-architecte.md) | Architecte | 9,4 % → 18 % d'EBITDA sans croissance du CA |
| [L10](parcours/L10-expert-mondial.md) | Expert mondial | Diagnostic chronométré, arbitrage, enseignement |

### Les douze séances de l'atelier

| # | Séance | Livrable |
|---|---|---|
| [S01](atelier/S01-choisir-le-terrain.md) | Choisir le terrain | Décision de catégorie, notée et chiffrée |
| [S02](atelier/S02-prouver-la-demande.md) | Prouver la demande | Six tests avec seuils écrits d'avance |
| [S03](atelier/S03-produit-et-cogs.md) | Le produit et le coût réel | Spécification + COGS rendu entrepôt |
| [S04](atelier/S04-offre-prix-et-panier.md) | L'offre, le prix, le panier | Gamme, prix, construction d'AOV |
| [S05](atelier/S05-recherche-client-et-angles.md) | Recherche client et angles | Trois fiches d'angle sur verbatim réel |
| [S06](atelier/S06-premier-lot-de-creas.md) | Le premier lot de créas | Douze concepts, accroches et scripts rédigés |
| [S07](atelier/S07-le-site.md) | Le site qui convertit | Page produit rédigée + mesure vérifiée |
| [S08](atelier/S08-le-lancement.md) | Les 30 premiers jours | Plan de lancement + tableau de seuils |
| [S09](atelier/S09-lire-les-premiers-chiffres.md) | Lire les chiffres et décider | Diagnostic sur dossier piégé |
| [S10](atelier/S10-installer-la-retention.md) | Installer la rétention | Sept flux rédigés + cohortes |
| [S11](atelier/S11-passer-a-l-echelle.md) | Passer à l'échelle | Plan 30 k€ → 300 k€ sur 12 mois |
| [S12](atelier/S12-la-crise.md) | La crise et la revue générale | Plan de crise + auto-évaluation finale |

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
| [`simulateur_marque.py`](outils/simulateur_marque.py) | **Le simulateur.** Tu crées une marque et tu la pilotes mois par mois, avec les conséquences |
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
├── parcours/                 ← L00 à L10, les niveaux et leurs épreuves notées
├── atelier/                  ← S01 à S12, la construction réelle d'une marque
├── modules/                  ← E00 à E14, les cours
├── etudes-de-cas/            ← C01 à C10, chiffrées, avec corrigés
├── exercices/                ← tes rendus et les corrigés
├── mentorat/                 ← protocole, diagnostic, jalons, tableau de bord, rituel
├── outils/                   ← les calculateurs et le simulateur de marque
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
