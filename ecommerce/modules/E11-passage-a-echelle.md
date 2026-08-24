# Module E11 — Passer à l'échelle : international, équipe, organisation

> **Prérequis :** [E01](E01-arithmetique-de-la-marque.md), [E05](E05-machine-creative.md), [E06](E06-acquisition-payante.md), [E09](E09-mesure-et-incrementalite.md), [E10](E10-cash-et-operations.md).
> **Objet :** reconnaître le mur du marché national, chiffrer une ouverture de pays jusqu'au retour à l'équilibre, dimensionner l'organisation qui tient sept marchés, arbitrer entre acheter et internaliser.
> **Temps de travail :** ~7 h

---

## 0. Pourquoi ce module existe

Ouvre les [chiffres canoniques](../donnees/chiffres-canoniques.md) au § 2 et au § 2.5, et fais trois divisions.

```
CA TTC hebdomadaire : 999 968 € (P5) ÷ 271 662 € (P3) = 3,68  → ×3,7
Effectif            :      38 ETP ÷      12 ETP       = 3,17  → ×3,2
EBITDA mensuel      : 364 752 € ÷ 51 033 €            = 7,15    (§ 2.2)
```

Les deux premiers sont presque égaux, et c'est le problème : **une entreprise dont le chiffre d'affaires et l'effectif croissent au même rythme ne grandit pas, elle se duplique.** Les frais fixes passent de 10,7 % à 10,0 % du CA HT (§ 2.5) : sept dixièmes de point pour trois fois plus de monde.

Le troisième sauve l'histoire. L'EBITDA croît 7,15 ÷ 3,68 = **1,94 fois plus vite** que le chiffre d'affaires, et ce levier vient de la marge brute (60,3 % → 61,5 %, § 2.1) et de la baisse du poids publicitaire (44,4 % → 41,4 % du CA HT, § 2.2), pas de la structure. **Entre P3 et P5, l'organisation ne produit pas la performance, elle la protège.** Trois chantiers : sortir du marché national avant qu'il ne se referme, construire l'appareil qui tient sept marchés, écrire les systèmes sans lesquels 38 personnes produisent trois chiffres pour la même question.

---

## 1. Le mur du marché national

### 1.1 Un plafond de rentabilité, pas de volume

Un marché national ne cesse jamais de te vendre des clients : il te les vend de plus en plus cher. Le **CAC** (*customer acquisition cost*, coût d'acquisition d'un nouveau client) moyen ne voit pas venir la bascule ; le **CAC marginal** — le coût du prochain client — la voit des mois à l'avance.

```
CAC marginal P3 → P4 = (1 047 000 − 436 000) ÷ (27 720 − 13 140)
                     = 611 000 € ÷ 14 580 = 41,91 €    (§ 2.2 et § 2.4)
CAC marginal P4 → P5 = (1 494 206 − 1 047 000) ÷ (37 324 − 27 720)
                     = 447 206 € ÷ 9 604 = 46,56 €
```

Rapporté au nCAC moyen du § 2.4 — 33,18 € à P3, 37,77 € à P4, 40,03 € à P5 — le marginal dépasse le moyen de **11,0 % à P4 et de 16,3 % à P5**, et l'écart s'ouvre à chaque palier parce qu'on commence par l'audience la plus facile. Un tableau de bord qui n'affiche que le nCAC moyen te laisse croire que tu paies 40,03 € un client qui t'en coûte 46,56 €.

### 1.2 Le contrefactuel : P5 sans quitter la France

Mesure d'abord l'élasticité observée : si `clients = k × budget^α`, alors α = ln(2,110) ÷ ln(2,401) = **0,852** entre P3 et P4, 0,836 entre P4 et P5, 0,848 sur l'ensemble. Un budget doublé rendrait 2^0,85 = 1,80 fois plus de clients — excellent, **et trompeur** : cette trajectoire fait passer NØRA de 2 marchés (P3 : France + Belgique) à 7 (P5), § 2. Ce 0,85 est l'élasticité de la France **plus cinq audiences vierges**.

*Hypothèse déclarée :* à audience constante l'élasticité tombe à **α = 0,55**, l'ordre de grandeur observé quand le budget supplémentaire achète de la fréquence et non de la portée.

```
Objectif : 13 140 → 37 324 nouveaux clients/mois, soit ×2,840
Budget  = 2,840^(1 ÷ 0,55) = ×6,67 = 436 000 € × 6,67 = 2 909 625 €/mois
nCAC    = 2 909 625 ÷ 37 324 = 77,96 €
LTV/CAC = 86,75 € ÷ 77,96 € = 1,11          (LTV 12 mois, § 3.1)

Marge brute P5 (§ 2.2)      =  2 218 957 €
− publicité contrefactuelle = −2 909 625 €  →  CM3    =   −690 668 €
− frais fixes               =   −360 000 €  →  EBITDA = −1 050 668 €/mois
```

Le § 3 canonique est sans appel : sous 1,5 de LTV/CAC, on ne scale pas, on répare. Contre +364 752 € réels, **l'écart vaut 1 415 420 € d'EBITDA par mois** : au-delà d'un certain volume, l'international n'est pas une option de croissance, c'est la condition de la rentabilité.

### 1.3 Les trois signaux qui disent que tu y es

1. **Le CAC marginal monte plus vite que le CAC moyen, à exécution constante.** Alerte : > 1,25 × le CAC moyen sur deux paliers de budget consécutifs.
2. **La fréquence d'exposition monte à budget constant** : la plateforme n'a plus de portée neuve, elle re-sert les mêmes gens. Alerte : fréquence hebdomadaire > 3,5 en prospection large.
3. **Les nouveaux concepts créatifs ne débloquent plus de volume.** Décisif, parce qu'il élimine la seule autre explication : le § 6 fixe le débit attendu — 38 concepts testés par semaine à P3, 57 à P5 — et si tu le tiens et que le CAC marginal monte quand même, le problème n'est plus la créa ([E05](E05-machine-creative.md)). Aucun signal ne suffit seul ; les trois ensemble sont un verdict.

### 1.4 Les trois sorties

| Sortie | Coût | Contribution | Levier touché (§ 7) |
| --- | --- | --- | --- |
| **Nouveau pays** | 58 000 € non récurrent + 294 568 € de trésorerie au pic (§ 2.4) | 5 mois | Volume de nouveaux clients |
| **Nouveau segment** | 98 100 € d'apprentissage non récupérable | 2 à 4 mois | Volume, puis CAC |
| **Nouveau produit** | ≈ 100 000 €, dont 60 % en stock | 6 à 12 mois | **AOV — levier n° 1** |

*Hypothèses.* Segment : 15 % du budget pendant 3 mois, soit à P3 196 200 €, dont la moitié en apprentissage perdu — sortie la plus risquée, le segment pouvant ne pas exister. Produit : formulation et dossier réglementaire ≈ 40 000 € HT, premier lot de 15 000 unités à 4,00 € de COGS = 60 000 € immobilisés, risque industriel et non commercial. Le pays est le plus prévisible ; le produit est le plus lent et vaut pourtant le plus, puisque le § 7 classe **+10 % d'AOV en tête, à 3 139 401 € d'EBITDA annuel, soit 71,7 % de l'EBITDA de référence**. **Le pays finance le temps que demande le produit.**

> **À retenir :** tu ne sors pas de France parce que la France est trop petite, mais parce que le prochain client français coûte 46,56 € quand le premier client allemand en coûte 37,77 €. Le mur est une comparaison de prix, pas une géographie.

---

## 2. Ouvrir un pays : la méthode, chiffrée

### 2.1 Ce qui bloque quoi

Après l'étude de marché (5 jours), quatre branches partent en parallèle : la conformité — TVA/OSS, étiquetage, mentions — 30 jours ; le recrutement du service client natif, 35 jours ; la localisation du site et du catalogue, 20 jours ; l'appel d'offres transporteur, 15 jours, qui conditionne avec la conformité le stock avancé (10 jours). La créa locale, tournage et UGC, part de la localisation pour 25 jours.

Chemin critique = 5 + 35 = **40 jours**, et il passe par le recrutement. La traduction du site, que tout le monde met en tête de projet, tient sur une branche parallèle de 20 jours : **ce qui bloque une ouverture, c'est une personne à recruter et un dossier à instruire.** Lance ces deux-là le premier jour.

### 2.2 Les six chantiers

**Paiement** : le moyen dominant local est le seul point du parcours où une absence tue la vente sans laisser de trace analytique — iDEAL aux Pays-Bas, paiement sur facture (*Kauf auf Rechnung*) et PayPal en Allemagne, contre-remboursement résiduel en Italie et en Espagne. **Transport** : le **p90** du délai livré — celui que 90 % des colis respectent. **SAV natif** : chemin critique, voir § 2.1. **TVA** : depuis le 1ᵉʳ juillet 2021, le guichet unique **OSS** (*One-Stop-Shop*) impose la TVA du pays du client dès 10 000 € de ventes à distance intra-UE par an cumulés sur l'Union — déclaration unique, **taux différent à chaque frontière** ; hors UE, le Royaume-Uni exige un enregistrement propre et, pour les envois ≤ 135 £, la TVA collectée à la vente. **Étiquetage** : la notification cosmétique du règlement (CE) n° 1223/2009 vaut pour toute l'Union, mais **l'étiquette doit être dans la langue de chaque État membre où le produit est vendu**, plus LUCID en Allemagne et Triman en France. Paiement, TVA et étiquetage sont des faits publics ; les oublier bloque la vente.

**Traduire n'est pas localiser.** La traduction porte sur le texte, la localisation sur la promesse, la preuve et l'objection : fiches réécrites, nouveaux visages, nouvel angle, prix recalibré sur les paliers locaux, avis et créateurs du pays — 3 à 6 fois plus cher. Symptôme : **le taux de conversion du marché ouvert reste durablement sous celui du marché d'origine** (§ 3.1).

### 2.3 Le coût d'ouverture

*Hypothèses de ce module*, calibrées sur l'écart de frais fixes canonique entre P3 et P4 (105 000 € → 230 000 €/mois, § 2.5) ; aucune n'est canonique. Non récurrent : localisation du site, du catalogue, des courriels et des réponses types SAV 16 000 € ; conformité — étiquetage, mentions légales, CGV, TVA, emballage — 9 000 € ; création locale, tournage et première vague d'UGC natif, 21 000 € ; paiements locaux, appel d'offres et tests transporteur 5 000 € ; recrutement du SAV natif 7 000 €. **Total 58 000 € HT.**

Structure récurrente : 1 ETP SAV natif + 0,5 ETP média/CRM local + 0,3 ETP opérations = **1,8 ETP**, soit au coût de structure complet de P4 (230 000 € ÷ 25 ETP = **9 200 € par ETP et par mois**, § 2.5) **16 560 € par mois et par marché**.

### 2.4 Montée en charge et retour à l'équilibre

*Hypothèses.* Marché de la taille de l'Allemagne, 6 500 commandes/mois en régime, AOV TTC 69,80 €, marge brute 60,4 % du CA HT, soit 69,80 ÷ 1,2 × 0,604 = **35,13 € par commande** (§ 2 et § 2.1, P4). Le **MER** (*marketing efficiency ratio* = CA TTC ÷ dépense publicitaire) part sous sa cible et converge vers les 2,80 canoniques (§ 2.3).

| Mois | Cmd. | CA TTC | MER | Publicité | Marge brute | CM3 | − structure | **Cumul** |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| M0 | — | — | — | — | — | — | −58 000 € | **−58 000 €** |
| M1 | 800 | 55 840 € | 1,90 | 29 389 € | 28 104 € | −1 285 € | −17 845 € | **−75 845 €** |
| M2 | 2 000 | 139 600 € | 2,30 | 60 696 € | 70 260 € | 9 564 € | −6 996 € | **−82 841 €** |
| M3 | 3 400 | 237 320 € | 2,50 | 94 928 € | 119 442 € | 24 514 € | +7 954 € | **−74 887 €** |
| M4 | 5 000 | 349 000 € | 2,70 | 129 259 € | 175 650 € | 46 391 € | +29 831 € | **−45 056 €** |
| M5 | 6 500 | 453 700 € | 2,80 | 162 036 € | 228 345 € | 66 309 € | +49 749 € | **+4 693 €** |

**L'équilibre cumulé est au mois 5** — c'est lui qui décide si tu peux ouvrir le marché suivant. Le creux, mois 2 à −82 841 €, n'est pas le besoin de trésorerie : il faut y ajouter le BFR en régime, 14 jours de CA TTC au palier P4 (§ 4), soit 453 700 € × 14 ÷ 30 = 211 727 €. **Total : 294 568 €, dont 72 % en stock et encaissements en attente, pas en dépenses.** Le [C07](../etudes-de-cas/C07-ouverture-allemagne.md) déroule ce calendrier mois par mois ; [E10](E10-cash-et-operations.md) dit pourquoi cette ligne tue plus de marques que la publicité.

### 2.5 L'ordre de priorité des marchés européens

*Hypothèse :* notes sur 5 et pondérations sont un modèle de décision, pas une mesure. Pondérations : taille 30 %, proximité culturelle et créative 20 %, coût des enchères 20 % (5 = enchères peu chères), simplicité logistique 15 %, retours 15 % (5 = retours faibles).

| Marché | Taille | Proxim. | Enchères | Logist. | Retours | **Score** |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Espagne | 3 | 3 | 5 | 3 | 4 | **3,55** |
| Belgique | 1 | 5 | 4 | 5 | 4 | **3,45** |
| Allemagne | 5 | 2 | 2 | 4 | 2 | **3,20** |
| Italie | 3 | 3 | 4 | 3 | 3 | **3,20** |
| Pays-Bas | 3 | 2 | 3 | 4 | 3 | **2,95** |
| Royaume-Uni | 5 | 2 | 2 | 1 | 3 | **2,90** |

La Belgique francophone est une extension de zone, pas une ouverture ; l'Espagne a les enchères les moins chères d'Europe de l'Ouest ; l'Allemagne, plus gros marché continental, a les retours les plus lourds, gonflés par le paiement sur facture ; l'Italie est fragmentée du nord au sud, les Pays-Bas imposent iDEAL et un néerlandais natif, le Royaume-Uni ajoute douane, EORI et TVA propre. **Le classement dépend de ta contrainte** : trésorerie limitée, l'Espagne ; contrainte de volume — NØRA doit passer de 271 662 € à 676 523 € de CA hebdomadaire (§ 2) — l'Allemagne, **seul marché capable d'absorber 6 500 commandes par mois**. C'est pour cela que le canonique séquence DE, ES, IT à P4 puis NL et UK à P5.

---

## 3. Ce qui se transfère, ce qui ne se transfère pas

Se transfèrent : **le produit** — une formule qui répond à un besoin physiologique le fait partout ; **la structure de compte publicitaire** — séparer prospection et retargeting est de la mécanique d'enchère, pas de la culture ; **le protocole de test** — seuil, durée minimale et règle d'arrêt sont identiques partout ([E09](E09-mesure-et-incrementalite.md)). Ne se transfèrent pas : **l'angle publicitaire**, rarement, un angle étant une objection prioritaire et l'objection n° 1 changeant de pays en pays ; **le prix**, pas toujours ; **les créateurs**, jamais, une audience étant nationale.

L'hypothèse canonique est une TVA moyenne pondérée de 20 % ; la réalité est un taux par pays, et à **prix TTC identique** ton CA comptable change à chaque frontière : sur le Sérum Densité à 39,00 € TTC (§ 1), le PVC HT vaut 32,77 € en Allemagne (19 %) contre 31,97 € en Italie (22 %), soit à COGS de 4,80 € **1,9 % d'écart de marge marchandise sur la même vente**. **Le prix se pilote en HT et s'affiche en TTC.**

### 3.1 Le pouvoir d'achat et l'effet sur le CAC

*Hypothèse déclarée :* sur un marché au revenu médian sensiblement inférieur, un prix nominal identique fait perdre **18 % de taux de conversion** ; à coût du clic constant, le CAC est inversement proportionnel au taux de conversion.

```
nCAC local = 37,77 € ÷ (1 − 0,18) = 46,06 €             (nCAC P4, § 2.4)
Marge à la 1ʳᵉ commande = 31,71 € − 46,06 € = −14,35 €
au lieu de −6,06 € en France                            (§ 2.4)
Sur 6 500 commandes/mois dont 70 % de nouveaux clients (4 550) :
Surcoût = 4 550 × 8,29 € = 37 720 €/mois = 452 640 €/an
```

Deux réponses : un prix local recalibré, au risque d'un arbitrage transfrontalier visible sur ton propre site ; ou une offre d'entrée différente — format réduit, mêmes marges — qui préserve le prix de référence, actif de marque ([E12](E12-marque-et-actif.md)).

### 3.2 Retours et paiement : le poste qui déclasse un marché

**Le paiement différé fabrique du retour** : là où le paiement sur facture domine, le client reçoit avant de payer et le coût psychologique du renvoi s'effondre — dans l'habillement, les taux de retour allemands dépassent régulièrement 40 % (constat sectoriel public). La cosmétique retourne beaucoup moins, mais **l'écart relatif entre pays demeure** : le mécanisme tient au moyen de paiement, pas au produit.

Le § 7 donne le prix d'un point de retour — **−1 point = 433 320 € d'EBITDA annuel, soit 9,9 %** — et 1 % du CA HT P5 de 3 610 997 € fait bien 36 110 €/mois. *Hypothèse :* l'Allemagne pèse 22 % du CA HT à P5 et retourne 3 points de plus que la France, soit 0,03 × 0,22 × 3 610 997 € = **23 833 €/mois, 285 996 €/an, 6,5 % de l'EBITDA annuel** (4 377 023 €, § 7).

Un marché, un écart de comportement de paiement, 6,5 % de l'EBITDA du groupe. **Une marge de contribution consolidée cache le marché qui perd de l'argent derrière ceux qui en gagnent** : ouvre un marché avec un compte de résultat par marché, ou n'ouvre pas ([C07](../etudes-de-cas/C07-ouverture-allemagne.md)).

---

## 4. L'organisation par palier

### 4.1 Les organigrammes

Les effectifs sont canoniques (§ 2.5) ; **la répartition par fonction est une hypothèse de ce module**, construite pour totaliser exactement les ETP canoniques et rester cohérente avec le débit créatif du § 6 et le volume de commandes du § 2.

| Fonction | **P2** — 4 | **P3** — 12 | **P4** — 25 | **P5** — 38 |
| --- | ---: | ---: | ---: | ---: |
| Direction, finance, contrôle de gestion | 1 (fondateur, dont média) | 1 | 2 | 3 |
| Acquisition payante | — | 2 | 4 | 5 |
| Création | 1 | 4 | 8 | 12 |
| Data et mesure | — | — | 1 | 2 |
| CRM, rétention, abonnement | — | 1 | 2 | 3 |
| Site, CRO, développement front | — | 1 | 1 | 2 |
| Service client | dans opérations | 2 | 4 | 5 |
| Supply chain, opérations, qualité | 1 | 1 | 2 | 4 |
| Produit, achats, R&D, réglementaire | 1 | 1 | 1 | 2 |
| **Coût de structure par ETP** (frais fixes ÷ ETP) | **7 000 €** | **8 750 €** | **9 200 €** | **9 474 €** |

La création pèse 33 % de l'effectif à P3, 32 % à P4, 31,6 % à P5 : **un tiers de l'entreprise produit des publicités**, et toute organisation DTC nettement en dessous a un goulot créatif qu'elle ne voit pas encore. Restent achetés dehors la comptabilité partout, le développement, le studio et l'entrepôt (3PL) jusqu'à P3, la production vidéo lourde et les pics de SAV à P5.

Chaque poste se dimensionne par une formule, pas par un ressenti. Le SAV : à un contact pour 8 commandes, 6 minutes par contact et 151,67 heures productives par ETP et par mois (35 h × 52 ÷ 12), les 60 200 commandes de P5 (§ 2) donnent 7 525 contacts, 753 heures, **4,96 ETP** — les 5 du tableau ; la formule donne 1,48 à P3 et 3,46 à P4, soit les 2 et 4 retenus une fois le multilingue compté. **Un poste que tu ne sais pas dimensionner par un calcul est un poste que tu ne sauras pas supprimer.**

### 4.2 Le premier recrutement, et pourquoi ce n'est pas celui qu'on croit

La réponse spontanée, « un acheteur média », est fausse deux fois.

**De principe :** tu ne recrutes pas une compétence que tu n'as pas, tu recrutes quelqu'un pour exécuter un processus que **tu as déjà écrit en le faisant toi-même** — sinon tu prends quelqu'un dont tu ne peux évaluer ni le travail ni l'échec. Le premier recrutement est celui de la tâche que tu maîtrises le mieux et qui te prend le plus d'heures, pas celle qui te fait peur.

**Arithmétique :** palier P2, budget publicitaire constant (104 636 €/mois, § 2.2), MER 2,20 (§ 2.3). *Hypothèses :* un monteur à 3 800 €/mois chargé fait passer le débit de 14 à 20 concepts testés par semaine, soit de 1,7 à 2,43 gagnants au taux de réussite du § 6 (1,7 ÷ 14 = 12,1 %), donc **+43 % de gagnants en rotation** ; un acheteur média à 4 200 €/mois améliore l'efficacité d'enchère de 5 % ; +10 % de gagnants = +2 % de MER.

```
A — MONTEUR   MER = 2,20 × (1 + 0,43 × 0,20) = 2,39
  CA TTC = 104 636 × 2,39 = 250 080 € contre 230 199 €  →  Δ CA HT = +16 568 €
  Δ marge brute = 16 568 × 58,8 % (§ 2.1) = +9 742 €  →  net +5 942 €/mois
B — ACHETEUR  MER = 2,20 × 1,05 = 2,31  →  CA TTC = 241 709 €
  Δ CA HT = +9 592 €  →  Δ marge brute = +5 640 €    →  net +1 440 €/mois
```

**Le monteur rapporte 4,1 fois plus, et coûte moins cher.** Le § 6 nomme le goulot : *« ce n'est ni le produit, ni le budget, ni l'algorithme : c'est la capacité à produire et juger 57 concepts publicitaires nouveaux par semaine »*. L'acheteur optimise la distribution d'un actif rare ; le monteur le fabrique.

D'où l'ordre : **1.** création ; **2.** opérations et SAV, dont le processus est déjà écrit ; **3.** acquisition payante, au seuil du § 5.1 ; **4.** CRM, au-delà de 25 % de réachat ([E08](E08-retention-et-ltv.md)) ; **5.** data, dès que deux canaux s'attribuent les mêmes clients ([E09](E09-mesure-et-incrementalite.md)) ; **6.** finance, quand le BFR dépasse 6 mois d'EBITDA ([E10](E10-cash-et-operations.md)).

### 4.3 Le chiffre d'affaires par ETP

| Palier | CA HT annuel par ETP (§ 2.5) | Variation | Frais fixes en % du CA HT |
| --- | ---: | ---: | ---: |
| P1 | 245 333 € | — | 21,2 % |
| P2 | 575 500 € | ×2,35 | 14,6 % |
| P3 | 981 000 € | ×1,70 | 10,7 % |
| P4 | **1 172 640 €** | ×1,20 | **9,4 %** |
| P5 | 1 140 315 € | **×0,97** | 10,0 % |

**La productivité par tête culmine à P4 et recule à P5** — seule série non monotone du canonique, et ce n'est pas un défaut du modèle : c'est sa thèse.

```
ETP nécessaires à P5 à la productivité de P4 :
  3 610 997 € × 12 ÷ 1 172 640 € = 36,95 ETP
Écart = 38 − 36,95 = 1,05 ETP → 1,05 × 9 474 € = 9 948 €/mois = 119 376 €/an

Concepts testés par semaine et par ETP  (§ 6 et § 2.5) :
  P2 : 14 ÷ 4 = 3,50  |  P3 : 38 ÷ 12 = 3,17  |  P5 : 57 ÷ 38 = 1,50   (−57 %)
```

Le montant est modeste, la direction ne l'est pas : un palier de plus au même régime et le levier d'exploitation disparaît ([C04](../etudes-de-cas/C04-scale-qui-detruit-la-marge.md), 41 M€ de CA, 5,8 M€ de perte).

**Lire ton écart.** Très au-dessus de la courbe : dette opérationnelle — rien n'est écrit, une fonction meurt avec la personne qui la porte. Conforme mais coût par ETP au-dessus du palier : tu paies cher les mauvaises fonctions, ou tu as internalisé ce qui devait être acheté (§ 5). Très en dessous : recrutement avant chiffre d'affaires, ou mix produit non digéré — compare la date d'embauche à celle du CA correspondant. En baisse deux trimestres de suite : coût de coordination non traité, le signal le plus grave.

---

## 5. Acheter ou internaliser : quatre seuils de bascule

On compare le **coût interne complet** — salaire chargé, outils, encadrement, inoccupation, part de structure consommée — au **coût externe** pour le même volume. Le coût complet par ETP se dérive du § 2.5 : 7 000 € à P2, 8 750 € à P3, 9 200 € à P4, 9 474 € à P5.

**5.1 L'achat média.** *Hypothèse :* une agence facture 10 % de la dépense, et l'équipe interne minimale viable est de 2 ETP, un ETP unique n'étant pas remplaçable en cas d'absence. Le seuil est donc `0,10 × dépense = 2 × 8 750 €`, soit **175 000 € de dépense mensuelle** — à MER 2,70, 472 500 € de CA TTC par mois, ou 109 038 € par semaine. Ce seuil tombe entre P2 (53 123 €/semaine) et P3 (271 662 €/semaine) : **l'achat média s'internalise pendant le palier P3**, ce que reflète l'organigramme du § 4.1.

**5.2 La création.** *Hypothèse :* 180 € par asset monté à partir de rushes fournis. Seuil : `180 € × N = 8 750 €` → **N = 48,6 assets/mois**, alors que le § 6 en donne 188 dès P2. Le seuil est franchi avant le premier recrutement, ce qui corrobore le § 4.2 par un chemin indépendant. **La création est la première fonction à internaliser, et de loin la plus rentable.**

**5.3 Le développement.** Seuil inversé, le besoin étant intermittent : 113 688 € par an en interne (9 474 × 12) contre 550 € par jour de freelance, soit **206,7 jours par an**, 85 % d'un temps plein, pour justifier un poste.

**5.4 Le service client.** *Hypothèse :* un centre de contact externe facture 2,20 € par contact traité. À P3, 2 250 contacts coûtent 4 950 € dehors contre 17 500 € pour 2 ETP ; à P5, 7 525 contacts coûtent 16 555 € dehors contre 47 370 € pour 5 ETP, soit **30 815 € de surcoût mensuel**. Sur le coût pur l'externe gagne partout : **il faut donc que l'interne se paie ailleurs**, et il ne se paie qu'en points de retour évités — un SAV interne détecte un défaut de lot ou un délai intenable avant que les retours n'arrivent. Le prix d'un point de retour à P5 étant de 36 110 €/mois (§ 7), il faut en récupérer **30 815 ÷ 36 110 = 0,85**. Si tu ne l'atteins pas en deux trimestres, externalise le volume et garde 2 ETP pour le pilotage, l'escalade et les verbatims : ainsi une décision d'organisation devient un engagement mesurable au lieu d'une préférence.

**5.5 Les deux coûts cachés.** *L'agence perd le savoir accumulé* — elle apprend sur ton compte quels angles fatiguent après combien de dépense, et ce savoir reste chez elle. *Hypothèse :* une équipe interne avec deux ans d'historique atteint un MER supérieur de 0,15 ; à P3, 436 000 € × 0,15 = 65 400 € de CA TTC/mois = 54 500 € HT × 60,3 % = **32 864 € par mois, 392 000 € par an, invisibles sur toute facture**. *L'internalisation achète de la rigidité* : une agence se résilie en un mois, une équipe créative de 8 personnes ne se réduit pas quand le CA baisse de 30 %. À P5, une telle chute — publicité réduite dans la même proportion, frais fixes intacts — fait tomber l'EBITDA de 364 752 € à 147 326 € par mois. **L'EBITDA chute de 60 % pour une baisse de 30 % du CA** : le levier joue à l'envers ([E13](E13-risque-de-ruine.md)).

> **À retenir :** internalise ce qui accumule du savoir propriétaire et tourne en continu — la création d'abord, l'achat média ensuite. Achète ce qui est intermittent ou purement volumétrique. Et écris, pour chaque internalisation, le chiffre qui la justifie.

---

## 6. Les systèmes qui rendent l'échelle possible

### 6.1 Pourquoi 38 personnes produisent trois chiffres pour une question

*« Combien de nouveaux clients le mois dernier ? »* Meta répond **21 346**, ce qu'il s'attribue (§ 5) ; la somme des six canaux, **41 364**, chacun s'attribuant le même client ; le back-office dédoublonné, **37 324** (§ 2.4), le seul chiffre réel.

```
Sur-attribution = 41 364 − 37 324 = 4 040 clients, soit 10,8 %
nCAC apparent = 1 494 206 ÷ 41 364 = 36,12 €   contre 40,03 € réel (§ 2.4)
Écart = 3,91 € × 37 324 = 145 937 €/mois = 1 751 244 €/an
     →  40,0 % de l'EBITDA annuel (4 377 023 €, § 7)
```

Trois personnes de bonne foi, trois outils corrects, trois réponses : **40 % de l'EBITDA annuel tient dans une définition non écrite.**

### 6.2 Le dictionnaire des indicateurs, et les trois autres systèmes

Un indicateur sans définition écrite est une opinion partagée. Chaque ligne porte sa définition exacte, sa source de vérité unique, son propriétaire nommé et sa date de dernière modification. Ce que « exact » veut dire : **nouveau client** = première commande payée et non annulée, dédoublonnée par adresse électronique **et** par empreinte d'adresse de livraison, datée à l'encaissement et non à la commande ; **chiffre d'affaires** = HT, hors frais de port, net des annulations, **brut des retours**, comptabilisé à l'expédition — ces cinq choix changent le résultat, ce qui compte est qu'ils soient écrits. Test de recette : deux personnes qui ne se parlent pas partent des définitions et trouvent le même nombre.

**Les processus** s'écrivent **par celui qui les fait**, la troisième fois qu'il les fait : déclencheur, étapes, critère de fin, personne à qui l'on escalade. **La bibliothèque créative** ([E05](E05-machine-creative.md)) : 1 245 assets par mois à P5 (§ 6) et, sans indexation par angle, format et preuve, l'entreprise repaie chaque trimestre des concepts déjà testés — à 180 € l'asset (§ 5.2), en retester 10 % par oubli coûte **22 410 € par mois**. **Le protocole de test** ([E09](E09-mesure-et-incrementalite.md)) : hypothèse, seuil, durée minimale et règle d'arrêt écrits d'avance, seul rempart contre 38 interprétations du même résultat ([C06](../etudes-de-cas/C06-test-incrementalite.md)).

---

## 7. Le rythme, et ce qui casse en chemin

### 7.1 Ce qui se décide à quelle fréquence

Le **quotidien** (15 min) décide la réallocation entre campagnes, la pause d'un concept, les incidents de stock et de transport — jamais un prix, une embauche ou un marché. L'**hebdomadaire** (moins d'une heure) décide la rotation créative, l'arbitrage de budget entre marchés, les écarts au seuil et les décisions ouvertes — jamais une remise ni une refonte de site. Le **mensuel** (2 h) traite le compte de résultat par marché, les cohortes, le plan créatif et l'approvisionnement — jamais une réorganisation. Le **trimestriel** (une journée) décide une ouverture de marché, un lancement, les recrutements, le calendrier promotionnel et les prix. Règle : **une décision se prend au niveau de rythme le plus lent compatible avec son échéance.**

### 7.2 Une revue hebdomadaire de moins d'une heure

Trois règles préalables : le tableau de bord est publié **la veille à 18 h** et qui ne l'a pas lu ne parle pas ; **aucun chiffre n'est présenté oralement**, seuls les écarts au seuil le sont ; tout sujet dépassant trois minutes en sort et devient une décision datée avec un responsable.

| Minutes | Séquence | Sortie |
| --- | --- | --- |
| 0 – 5 | Lecture silencieuse du tableau de bord | Chacun a vu les mêmes chiffres |
| 5 – 12 | Écarts au seuil, dans l'ordre du tableau. 90 s par ligne rouge | Une cause probable par ligne |
| 12 – 25 | Créa : concepts testés, gagnants, sorties de rotation, entrées de la semaine | Le plan de production |
| 25 – 35 | Acquisition : MER par marché contre MER seuil (§ 2.3), **un seul** arbitrage | Un mouvement de budget chiffré |
| 35 – 42 | Opérations : p90 du délai livré par marché, retours, ruptures à 30 jours | Les commandes fournisseurs |
| 42 – 50 | Décisions : quoi, qui, pour quand, quel chiffre la juge, date de revue | Le registre à jour |
| 50 – 55 | Une question ouverte, annoncée d'avance | Rien — le seul moment de réflexion |

### 7.3 Ce qui casse, et le signal qui l'annonce

| Ce qui casse | Signal précoce | Alerte |
| --- | --- | --- |
| **Qualité produit** à volume | Écart-type inter-lots sur 2 ou 3 critères mesurés (viscosité, pH, remplissage), **pas la moyenne** ; réclamations produit par lot | +0,2 point sur un lot |
| **SAV** | Première réponse au **p90** ; taux de re-contact | Re-contact > 15 % |
| **Délai de livraison** | **p90 par marché**, jamais la moyenne | p90 > promesse affichée deux semaines de suite |
| **Culture** | Délai entre la décision et sa première trace écrite | > 24 h |
| **Qualité du recrutement** | Recrues présentes à 12 mois ; délai avant première contribution mesurable | Contribution > 90 jours |
| **Vitesse de décision** | Âge médian des décisions ouvertes (§ 7.2) | > 14 jours |

Chiffre le cinquième, le plus sous-estimé. *Hypothèse :* 25 % de rotation annuelle à P5, soit 9,5 départs sur 38 ETP, un remplacement coûtant 3 mois à 50 % de productivité plus 7 000 € de recrutement — **21 211 € par départ, 201 505 € par an** ; à 12 % de rotation, 104 783 € économisés, soit 2,4 % de l'EBITDA annuel (§ 7).

---

## 8. Les erreurs qui coûtent cher

**1. Recruter avant d'avoir un processus écrit.** *Hypothèse :* sans processus, une recrue met 6 mois au lieu de 3 à contribuer, soit 3 × 9 200 € = 27 600 € ; sur les 13 recrutements du passage P3 → P4 (§ 2.5), **358 800 €**, ou 1,81 mois d'EBITDA du palier P4.

**2. Ouvrir trois pays en même temps.** Trois ouvertures simultanées demandent 3 × 294 568 € = **883 704 €** au même moment, soit 17,3 mois d'EBITDA du palier P3 ; séquencées, un seul creux à la fois, le premier marché dégageant dès le mois 5 les 49 749 €/mois qui financent le deuxième. **Le même projet coûte trois fois plus cher en trésorerie s'il est simultané, et il monte moins vite** : l'attention créative se divise, et c'est elle le goulot (§ 6).

**3. Traduire au lieu de localiser.** −18 % de taux de conversion, nCAC de 37,77 € à 46,06 €, perte à la première commande de −6,06 € à −14,35 € (§ 3.1) : **452 640 € par an sur un seul marché**, quand la localisation complète coûte 21 000 € une fois.

**4. Dupliquer l'organisation française à l'étranger.** Un marché ouvert pèse 1,8 ETP (§ 2.3). *Hypothèse :* dupliquer coûte 6 ETP, soit sur les trois marchés non francophones de P4 : 3 × 4,2 = 12,6 ETP en trop × 9 200 € = **115 920 €/mois, 1 391 040 €/an** — 58 % de l'EBITDA annuel du palier P4 (2 382 864 €). Créa, média, data et finance restent centrales ; seuls SAV, CRM local et une part d'opérations se localisent.

**5. Recruter un directeur avant d'avoir su faire le travail soi-même.** Le coût n'est pas le salaire, c'est le **délai de détection** : qui ne sait pas juger met 12 mois au lieu de 3 à détecter un mauvais recrutement. *Hypothèse :* 11 000 €/mois chargés et un écart de MER de 0,2 ; à P3, 9 × 11 000 = 99 000 € de salaire, plus 436 000 × 0,2 × 9 = 784 800 € de CA TTC perdu, soit 654 000 € HT × 60,3 % = 394 362 € de marge brute. **493 362 € au total, 81 % de l'EBITDA annuel de P3.**

**6. Croire qu'un outil remplace une décision.** Le § 6.1 le chiffre : 4 040 clients de sur-attribution, 3,91 € d'écart de nCAC, **1 751 244 € par an, 40 % de l'EBITDA annuel**. Aucun outil ne tranche entre 21 346, 41 364 et 37 324 : c'est une décision de définition, elle se prend une fois, elle s'écrit, elle a un propriétaire nommé.

---

## 9. Ce que ce module ne dit pas

**Les acquisitions.** Racheter une marque pour entrer sur un marché est une alternative réelle au § 2 : on achète un chiffre d'affaires, une base clients et une équipe locale contre du capital immédiat, et on hérite d'un passif. Valorisation, intégration, risque de destruction de la base rachetée : métier distinct.

**Le retail physique.** La marge marchandise du § 1 se partage avec le distributeur, l'AOV disparaît comme notion, le retour devient reprise d'invendus et l'incrémentalité de [E09](E09-mesure-et-incrementalite.md) devient bien plus difficile : ce n'est pas un canal de plus, c'est un autre modèle économique.

**Les places de marché comme canal.** Louer la relation client : commission, perte du contrôle du prix, pas de donnée client exploitable, donc pas de LTV pilotable — ce qui contredit frontalement [E08](E08-retention-et-ltv.md).

Absents aussi : le droit du travail par pays, les prix de transfert, l'Amérique du Nord. Et ce module est contredit sur un point — il traite l'organisation comme un coût à minimiser, quand [E12](E12-marque-et-actif.md) montre qu'à P5+ des fonctions improductives à court terme permettent le passage de 10,1 % à 20,3 % d'EBITDA (§ 8). Le § 4.3 dirait de les supprimer ; il aurait tort.

---

## 10. Le tableau de bord du module

| # | Indicateur | Calcul | Seuil d'alerte |
| --- | --- | --- | --- |
| 1 | **CA HT annuel par ETP** | CA HT du mois × 12 ÷ ETP | Baisse deux trimestres de suite, ou écart > 20 % au § 2.5 |
| 2 | **CAC marginal ÷ CAC moyen** | À chaque hausse de budget, jamais en fin de mois | > 1,25 sur deux paliers consécutifs → tu es au mur (§ 1.3) |
| 3 | **Marge de contribution par marché** | Après retours, transport, SAV et TVA **réels** du pays | Un marché sous 50 % de la CM2 du palier (§ 2.1) |
| 4 | **Concepts testés par semaine et par ETP** | Concepts testés ÷ effectif total | < 1,3 à P5 (référence : 1,50, § 4.3) |
| 5 | **Indicateurs à définition écrite, datée, avec propriétaire** | Dictionnaire du § 6.2 | < 100 %. Le seul seuil absolu du cursus |
| 6 | **Âge médian des décisions ouvertes** | Registre du § 7.2 | > 14 jours |

Les indicateurs 1 et 4 mesurent la même chose par deux chemins indépendants ; quand ils divergent, le 4 a raison le premier. Le 5 ne se négocie pas : les cinq autres n'existent pas sans lui.

> **À retenir :** à P3 tu pilotes des campagnes, à P4 des marchés, à P5 des définitions. Le jour où deux personnes donnent deux chiffres différents pour la même question et que personne ne s'en étonne, l'organisation a cessé de croître, quel que soit le chiffre d'affaires.

---

## 11. Exercices

À rendre dans [`ecommerce/exercices/E11-rendu.md`](../exercices/E11-rendu.md) ; corrigés dans `E11-corrige.md`.

**1 — Le mur et le contrefactuel (réponse numérique unique).** À partir des seuls § 2.2 et § 2.4 canoniques, recalcule le CAC marginal P3 → P4 et P4 → P5, puis α sur chaque intervalle. Refais ensuite le contrefactuel du § 1.2 avec α = 0,45 : budget mensuel, nCAC moyen, LTV/CAC à 12 mois, EBITDA mensuel. Une phrase sur ce que la valeur de α change à la décision.

**2 — Le plan allemand, variante lente (réponse numérique unique).** Reprends le § 2.4 avec 500 / 1 200 / 2 200 / 3 500 / 5 000 / 6 500 commandes et des MER de 1,80 / 2,10 / 2,35 / 2,55 / 2,70 / 2,80. Donne le mois du creux et son montant, le mois d'équilibre cumulé, la trésorerie à réunir BFR de régime inclus, et de combien ce retard alourdit le besoin, en euros et en pourcentage.

**3 — Ton plan d'ouverture de pays, chiffré.** Choisis un marché : (a) le tableau de priorité du § 2.5 refait avec tes CPM observés et tes pondérations, justifiées ; (b) le coût non récurrent poste par poste ; (c) la structure récurrente en ETP et en euros ; (d) la montée en charge sur six mois — commandes, MER, publicité, marge brute, CM3, cumul ; (e) mois d'équilibre cumulé, creux, BFR de régime en jours de CA TTC ; (f) le graphe de dépendances du § 2.1 avec tes délais réels et ton chemin critique. Deux pages : s'il en fait dix, tu n'as pas décidé.

**4 — Ton prochain recrutement prioritaire.** Trois postes envisagés et, pour chacun : coût mensuel chargé, effet chiffré sur **un seul** indicateur, conversion en marge brute mensuelle par le chemin du § 4.2, gain net. Classe-les, puis applique le double filtre : le processus du poste est-il écrit, et sais-tu faire le travail toi-même ? Si le premier échoue, il passe en deuxième et tu écris pourquoi. Donne enfin le seuil de CA hebdomadaire à partir duquel le deuxième devient le premier.

**5 — Ton organigramme contre la courbe.** Établis ton effectif réel en ETP, fonction par fonction, ton temps et tes freelances comptés au prorata. Calcule ton CA HT annuel par ETP et ton coût de structure par ETP, place-toi sur la courbe du § 4.3, puis écris pour chaque poste sa formule de dimensionnement (§ 4.1) : dénominateur, hypothèse, ETP calculés. Les postes dont tu ne sais pas écrire la formule forment ta dette d'organisation.

**6 — Décision : l'agence ou l'équipe.** Tu dépenses 210 000 € de publicité par mois, MER 2,60, marge brute 60,0 % du CA HT, frais fixes 9 000 € par ETP et par mois. Ton agence facture 9 % de la dépense et détient trois ans d'apprentissage sur ton compte ; une équipe interne de 2 ETP repart de zéro (*hypothèse* : −0,20 de MER pendant six mois, puis +0,10 au-delà de dix-huit mois). Calcule le coût des deux options sur 24 mois en marge brute nette de tous les coûts, tranche, puis écris la condition précise — en dépense mensuelle, en durée de dégradation du MER, ou en probabilité de départ de ton interlocuteur chez l'agence — sous laquelle l'autre option devient la bonne réponse.

---

*Fin du module E11. Suite : [E12](E12-marque-et-actif.md), qui montre pourquoi une partie de la structure que ce module minimise est l'actif du passage de 10,1 % à 20,3 % d'EBITDA ; [E13](E13-risque-de-ruine.md), qui reprend le levier du § 5.5 dans le sens de la descente ; [E14](E14-plan-1M-semaine.md), qui séquence ouvertures et recrutements. Cas : [C07](../etudes-de-cas/C07-ouverture-allemagne.md), [C04](../etudes-de-cas/C04-scale-qui-detruit-la-marge.md).*

