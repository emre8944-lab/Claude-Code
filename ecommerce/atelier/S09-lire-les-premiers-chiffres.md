# Séance S09 — Lire les premiers chiffres et décider

> **Niveau requis :** L04 · **Durée :** 6 h · **Livrable :** un diagnostic complet sur dossier fourni, le goulot en une phrase, une décision unique de la semaine avec ses seuils écrits d'avance · **Modules :** [E09](../modules/E09-mesure-et-incrementalite.md), [E10](../modules/E10-cash-et-operations.md), [E01](../modules/E01-arithmetique-de-la-marque.md), [E05](../modules/E05-machine-creative.md)
> **Ce que tu ne peux pas faire sans avoir fait cette séance :** piloter. Tu sais produire des chiffres depuis [S08](S08-le-lancement.md) ; tu ne sais pas dans quel ordre les lire, et l'ordre décide de tout. Un dossier lu à l'envers produit une décision juste sur le mauvais sujet.

---

## 1. Où tu en es

Quatre-vingt-dix jours de données existent : des ventes, un compte publicitaire, une trésorerie qui bouge, un stock qui descend, et les premiers clients qui reviennent — ou pas.

**Décidé :** la catégorie ([S01](S01-choisir-le-terrain.md)), le coût rendu entrepôt ([S03](S03-produit-et-cogs.md)), la gamme et les prix ([S04](S04-offre-prix-et-panier.md)), les angles ([S05](S05-recherche-client-et-angles.md)), les créas ([S06](S06-premier-lot-de-creas.md)), la page ([S07](S07-le-site.md)), le plan des trente premiers jours ([S08](S08-le-lancement.md)). **Pas décidé :** ce que ces quatre-vingt-dix jours autorisent. La [Porte P1 → P2](../mentorat/jalons.md) demande sept conditions simultanées, dont une que presque personne ne remplit parce qu'elle exige d'attendre : le taux de première à deuxième commande à 90 jours, mesuré sur une cohorte réelle.

Cette séance ne te demande pas de produire de la donnée. Elle te demande de la **lire** — un geste ordonné, qui s'apprend, et que la quasi-totalité des opérateurs exécute à l'envers.

*Acronymes : **CPA** — coût par achat, en euros HT. **nCAC** — dépense publicitaire ÷ clients **nouveaux**, jamais ÷ commandes. **MER** — CA TTC ÷ dépense publicitaire HT, tous canaux. **CM2** — marge après coûts variables, avant publicité. **CM3** — CM2 moins publicité. **ROAS** — CA attribué à un canal ÷ sa dépense ; ce n'est pas le MER, et c'est là que commencent les ennuis. **BFR** — besoin en fonds de roulement.*

---

## 2. Ta mission

**Produire le diagnostic complet du dossier ORVANE fourni au § 3, puis une décision unique.**

1. **Le diagnostic**, au format du § 5 : cinq blocs, calculs déroulés, et **les quatre pièges du dossier identifiés nommément**. Ils sont volontaires, et ce sont exactement ceux que tu rencontreras.
2. **Le goulot, en une phrase chiffrée.** Pas trois : une. Une équipe qui poursuit trois goulots n'en résout aucun ([revue hebdomadaire](../mentorat/revue-hebdomadaire.md), bloc 3).
3. **Une décision unique pour la semaine**, avec le seuil daté qui dira si elle a marché, et celui qui la fera annuler.

Ni plan à 90 jours, ni liste de chantiers. **Une décision.** La contrainte est le cœur de l'exercice : une marque à ce stade n'a la bande passante que pour une chose, et le choix de cette chose est le métier.

---

## 3. Ce dont tu disposes

Le dossier complet est ci-dessous ; rien à chercher ailleurs. Les outils, un par bloc : [`simulateur_tresorerie.py`](../outils/simulateur_tresorerie.py) pour le point bas et la croissance autofinançable (bloc 1) · [`calculateur.py`](../outils/calculateur.py) pour la cascade, le MER seuil et le verdict (bloc 2) · [`test_significativite.py`](../outils/test_significativite.py) `--creatif` pour le plancher de jugement et l'écart détectable (bloc 3) · [`cohortes.py`](../outils/cohortes.py) pour le tableau de cohortes et l'alerte de dégradation (bloc 4). Les lectures : [E10](../modules/E10-cash-et-operations.md) § 2 et § 7.3 · [E09](../modules/E09-mesure-et-incrementalite.md) § 3 et § 7.6 · [E05](../modules/E05-machine-creative.md) § 7.1 et § 7.2 · [jalons](../mentorat/jalons.md), Porte P1 → P2.

### 3.1 Le dossier ORVANE — jour 90

> **Cas composite. Marque fictive.** ORVANE n'existe pas. Les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.

**ORVANE** — compléments alimentaires « sommeil et récupération », vente directe, France. Lancée il y a 90 jours. Apport initial 75 000 € en fonds propres. Une personne à temps plein, un prestataire logistique, aucune dette.

| Référence | PVC TTC | PVC HT | COGS rendu entrepôt | Coef. | Part des 1ʳᵉˢ cmd |
|---|---:|---:|---:|---:|---:|
| Flacon 30 jours (60 gélules) | 34,00 € | 28,33 € | 4,90 € | ×6,9 | 46 % |
| Duo Sommeil (flacon + spray oreiller) | 49,00 € | 40,83 € | 8,20 € | ×6,0 | 34 % |
| Cure 90 jours (3 flacons) | 84,00 € | 70,00 € | 14,70 € | ×5,7 | 20 % |

**Autres coûts variables relevés sur 90 jours :** logistique et emballage **4,60 € HT par commande** · frais de paiement **1,9 % du CA HT** · retours, casse et gestes SAV **1,6 % du CA HT** · remises et codes **6,4 % du CA HT** (code de lancement `DEBUT15` à −15 %, encore actif). **Frais fixes : 4 200 € HT par mois.**

**Les 90 jours de ventes, agrégées par semaine.**

| Sem. | Dépense pub HT | Sessions | Commandes | Taux conv. | AOV TTC | CA TTC | MER |
|---|---:|---:|---:|---:|---:|---:|---:|
| S01 | 2 050 € | 2 320 | 58 | 2,50 % | 47,10 € | 2 732 € | 1,33 |
| S02 | 2 480 € | 2 960 | 79 | 2,67 % | 48,30 € | 3 816 € | 1,54 |
| S03 | 2 760 € | 3 350 | 96 | 2,87 % | 49,60 € | 4 762 € | 1,73 |
| S04 | 2 900 € | 3 520 | 104 | 2,95 % | 50,10 € | 5 210 € | 1,80 |
| S05 | 3 180 € | 3 980 | 118 | 2,96 % | 49,40 € | 5 829 € | 1,83 |
| S06 | 3 320 € | 4 180 | 127 | 3,04 % | 49,90 € | 6 337 € | 1,91 |
| S07 | 3 510 € | 4 460 | 134 | 3,00 % | 48,80 € | 6 539 € | 1,86 |
| S08 | 3 640 € | 4 700 | 141 | 3,00 % | 49,30 € | 6 951 € | 1,91 |
| S09 | 3 810 € | 5 070 | 152 | 3,00 % | 49,00 € | 7 448 € | 1,95 |
| S10 | 3 860 € | 4 980 | **131** | **2,63 %** | 48,60 € | 6 367 € | **1,65** |
| S11 | 3 900 € | 5 090 | 149 | 2,93 % | 49,20 € | 7 331 € | 1,88 |
| S12 | 4 020 € | 5 260 | 158 | 3,00 % | 48,70 € | 7 695 € | 1,91 |
| S13 | 4 180 € | 5 620 | 166 | 2,95 % | 48,10 € | 7 985 € | 1,91 |
| **Total** | **43 610 €** | **55 490** | **1 613** | **2,91 %** | **48,98 €** | **79 001 €** | **1,81** |

Sur les 1 613 commandes, **76 sont des réachats** ; **1 537 clients distincts** ont été acquis.

**La machine créative — 14 concepts en test sur les 28 derniers jours (Meta prospection).** CPA cible fixé en [S08](S08-le-lancement.md) : **26,00 € HT**.

| Concept | Dépense HT | Achats | CPA | Fréquence | Statut affiché par l'équipe |
|---|---:|---:|---:|---:|---|
| C01 | 1 980 € | 71 | 27,89 € | **2,41** | gagnant, porte le compte |
| C02 | 1 640 € | 54 | 30,37 € | 2,08 | conservé |
| C03 | 1 420 € | 39 | 36,41 € | 1,74 | à surveiller |
| C04 | 1 180 € | 47 | **25,11 €** | 1,32 | conservé |
| C05 | 890 € | 24 | 37,08 € | 1,21 | à surveiller |
| C06 | 760 € | 19 | 40,00 € | 1,15 | à couper |
| **C07** | **142 €** | **5** | **28,40 €** | 1,04 | **« pépite, à monter ×8 »** |
| C08 | 610 € | 12 | 50,83 € | 1,18 | à couper |
| C09 | 480 € | 9 | 53,33 € | 1,09 | à couper |
| C10 | 350 € | 4 | 87,50 € | 1,06 | coupé |
| C11 | 280 € | 2 | 140,00 € | 1,03 | coupé |
| C12 | 88 € | 0 | — | 1,02 | coupé |
| C13 | 165 € | 1 | 165,00 € | 1,01 | coupé |
| C14 | 135 € | 0 | — | 1,00 | coupé |
| **Total** | **10 120 €** | **287** | **35,26 €** | — | |

**La répartition du budget — 28 derniers jours.**

| Canal | Dépense HT | Part | Achats **attribués** | CPA attribué | ROAS attribué |
|---|---:|---:|---:|---:|---:|
| Meta prospection | 10 120 € | 63,4 % | 287 | 35,26 € | 1,38 |
| Meta reciblage | 2 340 € | 14,7 % | 158 | 14,81 € | **3,29** |
| Google Search — requêtes de marque | 1 180 € | 7,4 % | 123 | 9,59 € | **5,08** |
| Google Search — requêtes génériques | 1 020 € | 6,4 % | 28 | 36,43 € | 1,34 |
| TikTok | 900 € | 5,6 % | 17 | 52,94 € | 0,92 |
| Influence (2 créateurs, forfait) | 400 € | 2,5 % | 9 | 44,44 € | 1,10 |
| **Total** | **15 960 €** | 100 % | **622** | 25,66 € | 1,90 |

Commandes réelles sur ces 28 jours : **604**, dont **55 réachats**, soit **549 nouveaux clients**.

**Le premier tableau de cohortes.** Le point « · » signale un âge non atteint par tous les membres de la cohorte — inconnu, et non pas nul.

| Cohorte | Nouveaux clients | J+30 | J+60 | J+90 |
|---|---:|---:|---:|---:|
| M1 (jours 1–30) | 337 | 3,9 % | 11,3 % | · |
| M2 (jours 31–60) | 651 | 3,7 % | · | · |
| M3 (jours 61–90) | 549 | · | · | · |

Panier moyen de réachat observé : **56,00 € TTC** (les réachats prennent majoritairement la Cure 90 jours).

**La trésorerie.** Solde du compte courant : **52 100 €** au jour 30, **46 800 €** au jour 60, **38 400 €** au jour 90.

Engagements pris et non décaissés au jour 90 : **solde fournisseur 20 580 € HT**, payable à l'expédition usine prévue au **jour 112** (commande n° 3 de 6 000 unités à 29 400 € HT, acompte de 30 % réglé au jour 74) · **TVA du trimestre : 8 270 € nets**, exigibles au **jour 110**, non provisionnés sur un compte séparé.

**Le stock, au jour 90.**

| Référence physique | Unités en stock | Consommation pour 100 commandes | Réassort attendu |
|---|---:|---:|---|
| Flacon 60 gélules | 1 940 | 140 | jour 124 |
| Spray oreiller | 240 | 34 | jour 124 |

*100 commandes consomment 46 flacons (flacon seul) + 34 (Duo) + 60 (Cure, 3 flacons) = 140 flacons, et 34 sprays.*

**Ce que dit l'équipe au jour 90.** « Le CPA monte, Meta se dégrade. La semaine S10 a décroché, le site doit avoir un problème. Google marque fait 5,08 de ROAS et le reciblage 3,29 : basculons du budget dessus. Et C07 est une pépite, il faut la monter tout de suite. »

---

## 4. La méthode, pas à pas

### 4.1 L'ordre de lecture, et pourquoi presque tout le monde le prend à l'envers

```
1. La trésorerie            → combien de temps me reste-t-il ?
2. La marge de contribution → chaque vente me rapproche-t-elle ou m'éloigne-t-elle ?
3. La machine créative      → aurai-je de quoi continuer dans huit semaines ?
4. La rétention             → ce que j'achète vaut-il quelque chose après le jour 1 ?
5. Les campagnes            → où mettre l'euro suivant ?
```

**Première raison : la réversibilité.** Une erreur de campagne se corrige en une semaine pour quelques centaines d'euros. Une erreur de créa, en six semaines. Une erreur de rétention, en un trimestre. Une erreur de marge, en un semestre — le temps de renégocier un fournisseur. **Une erreur de trésorerie ne se corrige pas : elle se subit.** On lit du moins réversible au plus réversible, parce que le moins réversible contraint tout le reste.

**Deuxième raison : chaque niveau plafonne le suivant.** Ta marge de contribution fixe le MER à tenir ; le MER fixe le CPA cible ; le CPA cible fixe le budget de test finançable ; le budget de test fixe le nombre de concepts jugeables. Lire les campagnes en premier, c'est optimiser un chiffre dont la cible n'a pas été calculée.

**Pourquoi l'ordre s'inverse en pratique.** Trois mécanismes, dont aucun n'est de la bêtise. *La disponibilité :* la régie s'ouvre en deux secondes, la trésorerie demande un tableur que personne n'a rempli. *La gratification :* une campagne se modifie ce soir, et la modification produit une sensation de contrôle ; une marge de contribution, non — le geste le plus utile de la semaine ne procure aucune sensation, et c'est pour ça qu'il est sauté. *La granularité trompeuse :* le compte offre des milliers de lignes, la trésorerie une seule, et l'on confond finesse et information. C'est l'inverse : ces milliers de lignes sont majoritairement du bruit ([E09](../modules/E09-mesure-et-incrementalite.md) § 7.6), la ligne unique est le seul chiffre du dossier qui ne puisse pas mentir.

> **À retenir :** l'ordre de lecture *est* la compétence. Deux opérateurs devant le même dossier produiront deux décisions opposées uniquement parce que l'un a commencé par la trésorerie et l'autre par le CPA — et le second aura travaillé plus longtemps.

### 4.2 Les cinq blocs, un à un

**Bloc 1 — la trésorerie.** `Trésorerie libre = solde − engagements fermes − TVA nette due − dépôts de garantie`. Le solde bancaire n'est pas de la trésorerie : la TVA collectée appartient à l'État, elle transite par ton compte, elle n'y est pas ([E10](../modules/E10-cash-et-operations.md) § 7.3). La consommation mensuelle n'est pas l'EBITDA prévu : c'est la variation **observée** du solde, sur deux périodes au moins, pour voir si elle s'accélère. Le temps restant = trésorerie libre ÷ consommation, plus le cash que la croissance immobilise ([E10](../modules/E10-cash-et-operations.md) § 2.1) — ligne toujours positive aux paliers P1 et P2, et toujours oubliée : **la croissance y consomme du cash au lieu d'en produire** ([canoniques § 4](../donnees/chiffres-canoniques.md)).

**Bloc 2 — la marge de contribution.**

```
PVC HT moyen (AOV TTC ÷ 1,20)
 − COGS moyen pondéré par le mix RÉEL, pas par le mix espéré
 − logistique et emballage, en € par commande
 − frais de paiement  − retours, casse, SAV  − remises et codes
 = contribution par commande, en € HT     ← le nombre central de ton entreprise
```

Descends-la **en euros**, jamais en pourcentage seul : un pourcentage cache l'ordre de grandeur, et c'est l'ordre de grandeur qui décide. Puis les trois dérivés : `MER seuil CM3 = 1,20 ÷ CM2` · `CPA d'équilibre = contribution par commande` · `marge à la 1ʳᵉ commande = contribution − nCAC`. **Le piège de mix :** un mix qui glisse vers la référence la moins chère fait baisser la contribution sans qu'aucune ligne de coût ne bouge, et le tableau de bord affiche « marge stable en pourcentage ».

**Bloc 3 — la machine créative.** Quatre questions, dont une seule est de performance. *Combien de concepts nouveaux par semaine ?* — un rythme, pas un résultat, et la seule condition de rythme du parcours ([Porte P2 → P3](../mentorat/jalons.md)). *Combien de gagnants **distincts** portent la dépense ?* — deux variations d'un même concept comptent pour un, et un concept portant plus de 25 % du budget est un point de rupture unique. *Quel âge, quelle fréquence ?* — la fréquence monte avant le CPA, c'est l'indicateur avancé de la fatigue ([E05](../modules/E05-machine-creative.md) § 7.6). *Chaque concept a-t-il eu sa chance ?* — plancher de jugement `3,689 × CPA cible` ; en dessous, une coupe est un tirage au sort ([E05](../modules/E05-machine-creative.md) § 7.2). Et la question inverse, que personne ne pose : **chaque concept conservé a-t-il assez de conversions pour que son CPA veuille dire quelque chose ?** L'écart détectable vaut `√(15,68 ÷ n)`, `n` étant le nombre d'achats ([E05](../modules/E05-machine-creative.md) § 7.1) ; à 5 achats il vaut 177 %, et le CPA affiché est alors compatible avec presque n'importe quelle vérité.

**Bloc 4 — la rétention.** Une règle unique : **on ne compare que des âges égaux**, et un âge non atteint n'est pas zéro, il est inconnu. À 90 jours de vie, le seul chiffre décidable est le **plus petit âge commun à plusieurs cohortes** — souvent J+30 : il ne prouve rien sur J+90, il est un indicateur avancé, et c'est tout ce que tu as. Le chiffre qui décide reste le passage **1ʳᵉ → 2ᵉ commande à 90 jours**, seuil de la [Porte P1 → P2](../mentorat/jalons.md) : **12 %**. [E08](../modules/E08-retention-et-ltv.md) § 4.1 démontre pourquoi celui-là et pas les suivants — il est une fois et demie plus difficile, parce que c'est le seul où le client n'a encore rien vérifié.

**Bloc 5 — les campagnes.** Additionne les achats attribués et compare aux commandes réelles : l'écart est la sur-attribution — 11 % à P5 avec six canaux ([canoniques § 5](../donnees/chiffres-canoniques.md)), et c'est un plancher, jamais un plafond. Classe ensuite les canaux **par nature avant de les classer par ROAS** : un canal de *récolte* capte une demande existante — recherche de marque, reciblage ; un canal de *création* la fabrique — prospection froide. Le premier affiche mécaniquement un ROAS élevé parce qu'il facture des ventes qui allaient avoir lieu ([E09](../modules/E09-mesure-et-incrementalite.md) § 3.1). **Un ROAS élevé n'est pas une performance, c'est une position dans le parcours d'achat.** Enfin, ne décide qu'au marginal : le CPA moyen dit si tu as bien fait d'y mettre ce que tu y as mis, il ne dit rien de l'euro suivant — le seul que tu puisses encore décider ([E06](../modules/E06-acquisition-payante.md) § 6.2).

### 4.3 Bruit ou signal, puis le goulot et la décision

Avant de chercher une cause, prouve qu'il y a quelque chose à expliquer ([E09](../modules/E09-mesure-et-incrementalite.md) § 7.6). **Un —** estime le bruit par le bas : sur un comptage, le plancher est celui de Poisson, `σ ≥ √n` ; un écart-type calculé sur huit ou neuf points est lui-même très imprécis, et s'il tombe sous ce plancher, garde le plancher. **Deux —** retire la tendance : une série qui croît a un écart-type gonflé par sa propre croissance. **Trois —** applique une règle écrite d'avance : un point au-delà de 2σ, ou trois semaines consécutives du même côté. Rien d'autre ne déclenche. **La discipline la plus dure du métier est de ne rien faire quand c'est du bruit** : chaque intervention sur un compte coûte une phase de réapprentissage, et corriger du bruit, c'est payer pour dégrader.

Le goulot s'écrit ensuite en **une phrase contenant un nombre et une échéance**. « Le CPA est trop élevé » est une plainte ; « la trésorerie libre est de X €, la consommation de Y € par mois, il reste Z semaines » est un goulot. La décision tient en quatre lignes : **ce qu'on fait** · **ce qu'on arrête pour le faire**, la bande passante étant finie · **le seuil de réussite, chiffré et daté** · **le seuil d'annulation, chiffré et daté**. Un seuil écrit après coup n'est pas un seuil, c'est une justification.

---

## 5. Ton livrable

```
=====================================================================
LIVRABLE S09 — DIAGNOSTIC ET DÉCISION
Dossier : ORVANE, jour 90     Date : __/__/__     Temps passé : ____ h

BLOC 1 — TRÉSORERIE             (rempli en premier, avant tout le reste)
Solde ____ €  − engagements ____ €  − TVA ____ € = LIBRE ______ €
Consommation j30→j60 ____ €  j60→j90 ____ €   accélère ? O / N
Runway ____ semaines  ·  cash immobilisé par la croissance ____ €
VERDICT : ___________________________________________________

BLOC 2 — MARGE DE CONTRIBUTION
AOV TTC ____ €  AOV HT ____ €  − COGS mix ____ €  − logistique ____ €
− PSP ____ €  − retours/SAV ____ €  − remises ____ €
= CONTRIBUTION PAR COMMANDE ______ € HT       CM2 ______ %
MER seuil = 1,20 ÷ CM2 ____   MER réel ____   écart ____ %
nCAC ____ € HT    marge à la 1ʳᵉ commande ____ € HT
CM3 90 j ____ €   EBITDA 90 j ____ €
VERDICT : ___________________________________________________

BLOC 3 — MACHINE CRÉATIVE
Concepts nouveaux / semaine ____ (≥ 10)  ·  gagnants distincts ____ (≥ 2)
Part du budget du 1ᵉʳ concept ____ %  ·  sa fréquence ____
Plancher = 3,689 × CPA cible ____ € HT  ·  coupés SOUS le plancher : ____
Conservés avec n < 30 achats : ____ ; écart détectable √(15,68÷n) = ____ %
VERDICT : ___________________________________________________

BLOC 4 — RÉTENTION
Plus petit âge commun à ≥ 2 cohortes ____ j  ·  taux : ____  bruit ? O / N
Taux 1ʳᵉ → 2ᵉ à 90 j ____ % (seuil 12 %)  ·  OBSERVABLE ? O / N
Si non, sur quoi décides-tu : _______________________________
Contribution d'un réachat ____ €  ·  taux nécessaire pour rembourser
la perte de la 1ʳᵉ commande ____ %  ·  pour couvrir aussi les fixes ____ %
VERDICT : ___________________________________________________

BLOC 5 — CAMPAGNES
Achats attribués ____  ·  nouveaux clients réels ____  ·  écart ____ %
nCAC réel ____ € HT
RÉCOLTE : __________ ____ %   ·   CRÉATION : __________ ____ %
VERDICT : ___________________________________________________

LES QUATRE PIÈGES  1 : ________  2 : ________  3 : ________  4 : ________

LE GOULOT — UNE PHRASE, AVEC UN NOMBRE ET UNE ÉCHÉANCE
_____________________________________________________________

LA DÉCISION DE LA SEMAINE — UNE SEULE
On fait : ___________________________________________________
On arrête pour le faire : ___________________________________
Seuil de réussite ____________ le __/__/__
Seuil d'annulation ___________ le __/__/__
Ce que je NE fais pas, bien que ce soit tentant : ____________
=====================================================================
```

---

## 6. La grille d'évaluation

Barème sur 100, **seuil de validation 75** — le plus haut de l'atelier, et c'est volontaire : une lecture de dossier à moitié juste produit une décision entièrement fausse.

| # | Critère | Pts | Ce qui vaut les points | Ce qui les fait perdre |
|---|---|---:|---|---|
| 1 | **Ordre de lecture respecté** | 10 | Blocs remplis 1 → 5, chaque verdict écrit avant le bloc suivant | Commencer par les campagnes : **−10, et la décision finale est presque toujours fausse** |
| 2 | **Trésorerie** | 18 | Trésorerie **libre**, TVA retirée, consommation sur deux périodes, runway en semaines | Prendre le solde bancaire pour la trésorerie : **éliminatoire** ; oublier la TVA : −8 |
| 3 | **Marge de contribution** | 15 | Cascade en € par commande, mix réel, MER seuil, marge à la 1ʳᵉ commande | Raisonner en pourcentage seul : −6 ; utiliser le mix espéré : −5 |
| 4 | **Machine créative** | 12 | Rythme, gagnants distincts, concentration, fréquence, plancher, écart détectable | Ne pas calculer l'écart détectable sur les petits effectifs : −6 |
| 5 | **Rétention** | 12 | Ne compare que des âges égaux, dit ce qui n'est pas observable | Comparer deux âges différents : **éliminatoire** ; lire un « · » comme un zéro : −6 |
| 6 | **Campagnes et attribution** | 10 | Sur-attribution chiffrée, canaux classés récolte/création avant ROAS | Recommander de basculer sur le ROAS le plus élevé : **−10** |
| 7 | **Les quatre pièges** | 12 | 3 points par piège nommé **et démontré par le calcul** | Un piège « senti » sans calcul : 1 point sur 3 |
| 8 | **Le goulot en une phrase** | 6 | Une phrase, un nombre, une échéance | Trois goulots : −6 ; un goulot sans nombre : −4 |
| 9 | **La décision et ses seuils** | 5 | Une décision, ce qu'on arrête, deux seuils datés | Décision sans seuil d'annulation : −5 |

**Cinq fautes éliminatoires.** Confondre le solde bancaire et la trésorerie disponible. Comparer deux cohortes d'âges différents. Décider de scaler un concept sur moins de 15 achats. Recommander une réallocation vers un canal de récolte au motif de son ROAS. **Rendre plus d'une décision** — trois décisions valent zéro décision.

---

## 7. Le corrigé exemplaire

> **Cas composite. Marque fictive.** Tous les chiffres ci-dessous sont dérivés du dossier du § 3.1 par les calculs déroulés.

### 7.1 Bloc 1 — La trésorerie

```
Solde au jour 90                                           38 400 €
− solde fournisseur, exigible jour 112                   − 20 580 €
− TVA nette du trimestre, exigible jour 110               − 8 270 €
= TRÉSORERIE LIBRE                                          9 550 €
```

**Consommation.** Jour 30 → 60 : `46 800 − 52 100 = −5 300 €`. Jour 60 → 90 : `38 400 − 46 800 = −8 400 €`. **Elle s'accélère de 58,5 %** pendant que le chiffre d'affaires progresse : signature d'une marque dont chaque vente supplémentaire coûte de l'argent — ce que le bloc 2 confirmera.

```
Runway = 9 550 € ÷ 8 400 € par mois = 1,14 mois ≈ 5 semaines
```

**Et la croissance en rajoute** : la publicité se paie avant le client, et à l'intensité en cash du palier P1 ([E10](../modules/E10-cash-et-operations.md) § 2.1, ~58 700 € par tranche de 100 000 € de CA mensuel), les +6 300 € de CA TTC mensuel visés immobilisent encore `58 700 × 0,063 = 3 698 €`.

> **Verdict : ORVANE dispose de cinq semaines, pas de quatre mois. Le solde de 38 400 € affiché en haut du tableau de bord est faux de 75 %.** Personne ne l'a calculé, et rien dans les phrases du jour 90 n'y fait allusion.

### 7.2 Bloc 2 — La marge de contribution

```
AOV TTC  = 0,46 × 34,00 + 0,34 × 49,00 + 0,20 × 84,00
         = 15,64 + 16,66 + 16,80                          =  49,10 €
AOV HT   = 49,10 ÷ 1,20                                   =  40,92 €
COGS mix = 0,46 × 4,90 + 0,34 × 8,20 + 0,20 × 14,70
         = 2,25 + 2,79 + 2,94                             =   7,98 €
```

| Ligne | € HT / commande | % du CA HT |
|---|---:|---:|
| Prix de vente HT | 40,92 € | 100,0 % |
| − COGS | 7,98 € | 19,5 % |
| − logistique et emballage | 4,60 € | 11,2 % |
| − frais de paiement | 0,78 € | 1,9 % |
| − retours, casse, SAV | 0,65 € | 1,6 % |
| − remises et codes | 2,62 € | 6,4 % |
| **= contribution par commande** | **24,28 €** | **59,4 %** |

```
MER seuil CM3 = 1,20 ÷ 0,594                              =    2,02
MER réel sur 90 jours                                      =    1,81   (−10,4 %)
nCAC = 43 610 € ÷ 1 537 nouveaux clients                   =   28,37 € HT
Marge à la 1ʳᵉ commande = 24,28 − 28,37                    =   −4,09 € HT
CM3 90 j = 79 001 ÷ 1,20 × 0,594 − 43 610                  =  −4 538 €
EBITDA   = −4 538 − 3 × 4 200                              = −17 138 €  (−26,0 % du CA HT)
```

**Comparaison au modèle de référence** ([canoniques § 2](../donnees/chiffres-canoniques.md), palier P1) : MER 1,80 contre 1,81 · EBITDA −30,7 % contre −26,0 % · nCAC 26,62 € contre 28,37 € · marge à la 1ʳᵉ commande −4,93 € contre −4,09 €. **ORVANE est très exactement une marque de palier P1 normale.** Elle perd de l'argent parce que c'est ce que fait une marque de palier P1 — constat que tout diagnostic doit produire d'abord, et qui manque le plus souvent : sans lui, on répare ce qui fonctionne.

**Un seul chiffre sort de la norme :** les remises à **6,4 % du CA HT** contre 3,0 % au canonique P1. `DEBUT15` tourne depuis 90 jours sur tout le trafic, y compris sur ceux qui auraient acheté au prix fort. Surcoût : `2,62 − 1,23 = 1,39 € HT` par commande, soit `1,39 × 1 613 = 2 242 €` sur le trimestre — 13,1 % de la perte.

> **Verdict : structure de coût saine, coefficient bon, contribution de 24,28 € HT par commande. La seule anomalie est un code de lancement qu'on a oublié d'éteindre.**

### 7.3 Bloc 3 — La machine créative

**Rythme :** 14 concepts sur 28 jours = **3,5 par semaine**, quand la [Porte P2 → P3](../mentorat/jalons.md) en demande 10 et que le canonique en teste 14 dès P2 ([canoniques § 6](../donnees/chiffres-canoniques.md)). Un quart de la cible du palier suivant : pas un problème aujourd'hui, un problème dans huit semaines.

**Concentration et fatigue :** C01 porte `1 980 ÷ 10 120 = 19,6 %` du budget de prospection et sa **fréquence est de 2,41**, quand aucun autre ne dépasse 2,08. À ce niveau de dépense sur une audience française, 2,41 en 28 jours signale une audience travaillée jusqu'à la corde. Le CPA de C01 va monter — **après** la fréquence, jamais avant.

**Le plancher de jugement :** `3,689 × 26,00 € = 95,91 € HT`. C14 (135 € HT, 0 achat) est au-dessus : coupe légitime. **C12 (88 € HT, 0 achat) est en dessous :** un concept tenant exactement la cible aurait `e^(−88 ÷ 26) = 3,4 %` de chances de n'avoir aucun achat — on ne peut rien conclure, et la coupe est un tirage au sort. C'est la faute qui détruit 10,7 % de l'EBITDA annuel dans la démonstration d'[E05](../modules/E05-machine-creative.md) § 7.3.

**Et l'erreur inverse**, `écart détectable = √(15,68 ÷ n)` :

| Concept | Achats | CPA affiché | Écart détectable | Ce que le CPA autorise à dire |
|---|---:|---:|---:|---|
| C01 | 71 | 27,89 € | 47 % | « entre 15 € et 41 € » |
| C02 | 54 | 30,37 € | 54 % | « entre 14 € et 47 € » |
| C04 | 47 | 25,11 € | 58 % | « entre 11 € et 40 € » |
| **C07** | **5** | **28,40 €** | **177 %** | **rien du tout** |

> **Verdict : rythme à un quart de la cible, un concept porte 19,6 % du budget et sa fréquence annonce sa mort, un concept a été coupé sous le plancher, et celui que l'équipe veut multiplier par huit repose sur cinq achats.**

### 7.4 Bloc 4 — La rétention

Le plus petit âge commun à deux cohortes est **J+30** : M1 (337 clients, 3,9 %) et M2 (651 clients, 3,7 %). M3 n'est observable à aucun âge, et le J+60 de M1 (11,3 %) n'a **aucun point de comparaison** : chiffre isolé, pas tendance. L'écart 3,9 % → 3,7 % est-il un signal ?

```
n = 651, p = 0,039  →  σ = √(0,039 × 0,961 ÷ 651) = 0,76 point
Écart observé = 0,2 point  →  z = 0,26      →  du bruit. Rien à expliquer.
```

**Le chiffre qui décide n'existe pas encore.** Le taux à 90 jours de M1 sera observable au jour 120. Ce qu'on a : 11,3 % à J+60 sur la première cohorte, quand la [Porte P1 → P2](../mentorat/jalons.md) exige 12 % à J+90. Trajectoire plausible, non démontrée.

```
Contribution d'un réachat = (56,00 ÷ 1,20) × 59,4 %        =  27,72 € HT
Taux de réachat pour rembourser la perte : 4,09 ÷ 27,72    =  14,8 %
Taux pour couvrir aussi les fixes :
   fixes par commande = 4 200 ÷ 656 cmd/mois               =   6,40 €
   (4,09 + 6,40) ÷ 27,72                                    =  37,8 %
```

**14,8 % pour cesser de perdre de l'argent sur l'acquisition ; 37,8 % pour être à l'équilibre.** Le second est un niveau de fin de parcours — le modèle de référence est à 44 % au palier P5 ([E08](../modules/E08-retention-et-ltv.md) § 4.1) — et l'exiger à 90 jours de vie serait une erreur de diagnostic. Le premier, en revanche, est à 3,5 points du J+60 déjà observé.

> **Verdict : le seul chiffre qui décide n'est pas encore observable. Aucune décision de scale ne peut s'appuyer sur la rétention avant le jour 120.**

### 7.5 Bloc 5 — Les campagnes

```
Achats attribués 622  ·  nouveaux clients réels 549
Sur-attribution = 622 ÷ 549 − 1                                = 13,3 %
nCAC réel = 15 960 € ÷ 549                                     = 29,07 € HT
```

13,3 % contre 11 % au canonique ([canoniques § 5](../donnees/chiffres-canoniques.md)) : normal, et c'est un plancher.

| Canal | Nature | Dépense | ROAS | Ce que le ROAS mesure vraiment |
|---|---|---:|---:|---|
| Google Search — marque | **récolte pure** | 1 180 € | 5,08 | Des gens qui tapent « ORVANE » : ils te connaissent déjà |
| Meta reciblage | **récolte** | 2 340 € | 3,29 | Des gens déjà venus sur le site |
| Meta prospection | **création** | 10 120 € | 1,38 | Des gens qui ne te connaissaient pas |
| Google générique · TikTok · influence | mixte et création | 2 320 € | 0,92 à 1,34 | Demande de catégorie, tests, effet différé |

Les deux canaux au meilleur ROAS pèsent **22,1 % du budget et n'ont créé aucune demande.** Quelqu'un a cherché « ORVANE » sur Google parce qu'il avait vu une publicité Meta trois jours plus tôt : ce ROAS de 5,08 est le reçu d'une vente fabriquée ailleurs.

*Hypothèse d'incrémentalité, cohérente avec [E09](../modules/E09-mesure-et-incrementalite.md) § 6.2 : 30 % sur la recherche de marque, 40 % sur le reciblage, 85 % sur la prospection froide.*

```
Déplacer 3 000 € de la prospection vers marque + reciblage :
  perdu : 3 000 ÷ 35,26 × 85 %              = 72,3 clients réels
  gagné : 3 000 ÷ 12,00 × 35 % d'incrément. = 30,6 clients réels
  Solde RÉEL : −41,7 clients par mois
  Solde AFFICHÉ : nCAC attribué de 35,26 € à ~24,00 €, soit « −32 % de CAC ».
```

> **Verdict : sur-attribution 13,3 %, nCAC réel 29,07 € HT, et la réallocation proposée ferait perdre 41,7 clients par mois en affichant une amélioration de 32 % du coût d'acquisition.**

### 7.6 Les quatre pièges, nommés

**Piège 1 — C07 : le bon CPA sur trop peu de conversions.** 5 achats, écart détectable `√(15,68 ÷ 5) = 177 %` : le vrai CPA est compatible avec 10 € comme avec 79 €. Multiplier la dépense par huit, c'est engager 1 136 € sur une hypothèse dont l'intervalle couvre presque toute la distribution des CPA du compte. **Geste correct : monter C07 à 400 € HT, soit ~15 achats attendus, ce qui ramène l'écart détectable à 102 %** — encore mauvais, mais décidable deux semaines plus tard. Un concept ne se juge sur son CPA qu'à partir d'une trentaine d'achats, et rigoureusement qu'à 392 ([E05](../modules/E05-machine-creative.md) § 7.1).

**Piège 2 — la semaine S10 : du bruit pris pour un signal.**

```
Tendance ajustée sur S05–S13 : commandes = 96,03 + 5,08 × n° de semaine
Prévu en S10 : 96,03 + 5,08 × 10 = 146,9   ·   Observé 131   ·   Résidu −15,9

σ résiduel calculé sur 9 points                            =  7,7
Plancher de Poisson à 147 commandes : √146,9               = 12,1
On garde le plus grand des deux : σ = 12,1
z = −15,9 ÷ 12,1                                           = −1,31
```

**−1,31 écart-type. Sous bruit pur, on attend une semaine au moins aussi basse une fois tous les cinq mois.** S11 et S12 reviennent sur la tendance (résidus −2,9 et +1,0), ce qui exclut la règle des trois semaines du même côté. Aucun signal. Refondre le site cette semaine, c'est payer une phase de réapprentissage pour corriger une fluctuation.

**Piège 3 — Google marque et le reciblage : un ROAS flatteur et non incrémental.** Démontré au § 7.5. Mécanisme à retenir : **le ROAS classe les canaux par leur position dans le parcours d'achat, pas par leur contribution.** Le seul test qui tranche est la retenue — couper la recherche de marque sur une région pendant deux semaines et comparer le chiffre d'affaires **total**, pas le chiffre d'affaires attribué ([E09](../modules/E09-mesure-et-incrementalite.md) § 5).

**Piège 4 — le stock du spray, et la trésorerie derrière.** En agrégat, 2 180 unités sur 243 par semaine donnent 9 semaines de couverture : confortable. Par référence, à 171 commandes par semaine :

| | Stock jour 90 | Consommation/semaine | Couverture | Rupture |
|---|---:|---:|---:|---|
| Flacon | 1 940 | 239 | 8,1 semaines | jour 147 |
| **Spray oreiller** | **240** | **58** | **4,1 semaines** | **jour 119** |

Le réassort arrive au **jour 124** : **cinq jours de rupture sur le spray**, donc sur le Duo Sommeil, donc sur **34 % des premières commandes** et sur la référence à 49,00 € TTC qui tient l'AOV. Coût direct si la demande Duo bascule intégralement sur le flacon seul : la contribution passe de 23,99 € à 16,03 € par commande concernée, soit `5 j × 24,4 cmd/j × 34 % × 7,96 € = 331 € HT` — davantage si une part renonce à commander. Et le piège dans le piège : **avancer le réassort coûte du cash au moment exact où il n'y en a plus** — le solde fournisseur tombe au jour 112, la TVA au jour 110. La rupture du spray n'est pas un problème logistique : c'est le symptôme visible du problème de trésorerie du bloc 1.

### 7.7 Le goulot, en une phrase

> **La trésorerie libre d'ORVANE est de 9 550 €, la consommation de 8 400 € par mois et en accélération : il reste cinq semaines, et aucun des leviers dont l'équipe parle n'agit sur ce nombre avant le jour 120.**

Ce n'est pas le CPA, normal pour un palier P1. Ce n'est pas S10, qui est du bruit. Ce n'est pas la répartition des canaux, dont la correction ferait perdre des clients. **C'est le cash — et le cash se desserre par la contribution par commande, pas par le volume.**

### 7.8 La décision de la semaine

```
ON FAIT
  Éteindre DEBUT15 et le remplacer par une construction de panier : la Cure
  90 jours en choix par défaut sur la page produit et dans le tunnel, avec le
  prix par jour affiché (84,00 ÷ 90 = 0,93 € TTC/jour contre 34,00 ÷ 30 = 1,13 €).
  Cible : AOV de 49,10 € à 53,00 € TTC en 4 semaines, part de la Cure de 20 % à 30 %.

ON ARRÊTE POUR LE FAIRE
  Toute modification du compte publicitaire cette semaine — bascule vers Google
  marque et montée de C07 comprises. Budget gelé à l'identique.

POURQUOI CELUI-LÀ
  +3,90 € d'AOV TTC = +3,25 € HT, dont 59,4 % de contribution  = +1,93 €
  Extinction du code                                            = +1,39 €
  Total +3,32 € HT × 660 commandes/mois                         = +2 191 €/mois
  La consommation tombe de 8 400 € à 6 209 €/mois, le runway passe de 5 à
  6,7 semaines — et la Cure allonge le cycle de consommation de 30 à 90 jours,
  ce qui recule le besoin de réassort et donc le prochain appel de cash.

SEUIL DE RÉUSSITE, mesuré le jour 118
  AOV ≥ 52,00 € TTC sur 14 jours  ET  part de la Cure ≥ 27 %
  ET  taux de conversion ≥ 2,80 % (pas d'effondrement du haut de tunnel)

SEUIL D'ANNULATION, mesuré le jour 104
  Taux de conversion < 2,55 % sur 7 jours consécutifs
  OU commandes hebdomadaires < 140 deux semaines de suite
  → page remise en l'état sous 24 h.

CE QUE JE NE FAIS PAS, BIEN QUE CE SOIT TENTANT
  Monter C07. Basculer sur Google marque. Toucher au site à cause de S10.
  Couper C06 et C08 : au-dessus du plancher, mais leur coupe ne libère que
  1 370 € — ce n'est pas le sujet de la semaine.
```

**Trois gestes d'exécution, qui ne consomment pas de bande passante d'arbitrage** et se font dans la foulée : provisionner la TVA sur un compte séparé dès le jour 91 · demander au fournisseur le report du solde du jour 112 au jour 140 — trente jours de délai valent plus que 2 % de remise ([E10](../modules/E10-cash-et-operations.md) § 7.1) · commander des sprays seuls pour éviter les cinq jours de rupture.

---

## 8. Les conséquences chiffrées de ton choix

Deux trajectoires à six mois depuis le même jour 90. La différence n'est pas le sérieux de l'équipe — dans les deux cas elle travaille beaucoup. **La différence est par quoi elle a commencé sa lecture.**

*Hypothèses communes : frais fixes en légère hausse, aucune levée de fonds, aucune dette. Ce sont des modèles, pas des prévisions.*

### 8.1 Trajectoire A — traiter le symptôme le plus visible

L'équipe lit le compte publicitaire en premier. Elle voit un CPA qui monte, une semaine qui décroche, deux canaux à ROAS élevé et une pépite. Elle bascule 3 000 € vers Google marque et le reciblage, monte C07 par huit, refond la page à cause de S10, et réduit le budget de test de 15 % à 4 % pour financer le tout.

| Mois | Cmd | AOV TTC | CA TTC | CM2 | Pub | CM3 | Fixes | EBITDA | Cumul |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| M4 | 740 | 48,50 € | 35 890 € | 59,0 % | 17 200 € | 446 € | 4 200 € | −3 754 € | −3 754 € |
| M5 | 780 | 48,00 € | 37 440 € | 58,5 % | 18 500 € | −248 € | 4 500 € | −4 748 € | −8 502 € |
| M6 | 760 | 47,50 € | 36 100 € | 58,0 % | 19 800 € | −2 352 € | 4 500 € | −6 852 € | **−15 354 €** |
| M7 | 690 | 47,00 € | 32 430 € | 57,8 % | 20 500 € | −4 880 € | 4 700 € | −9 580 € | −24 933 € |
| M8 | 640 | 46,50 € | 29 760 € | 57,5 % | 20 000 € | −5 740 € | 4 700 € | −10 440 € | −35 373 € |
| M9 | 600 | 46,00 € | 27 600 € | 57,5 % | 19 000 € | −5 775 € | 4 700 € | −10 475 € | **−45 848 €** |

**Les mécanismes.** Le budget de test tombé à 4 % ne produit plus assez de concepts nouveaux : quand C01 meurt au mois 6 — sa fréquence de 2,41 l'annonçait dès le jour 90 —, il n'y a pas de remplaçant, et le CPA de tout le compte monte pour compenser. La bascule vers la récolte a fait baisser le CPA **affiché** deux mois, puis la récolte s'est épuisée faute de semence : **un canal de récolte ne finance pas sa semence.** L'AOV baisse parce que les remises montent pour tenir le volume. MER moyen : **1,73** contre 2,02 de seuil — chaque euro supplémentaire détruit de la marge.

**Le cash.** Trésorerie libre au jour 90 : 9 550 €. Pertes cumulées −3 754 €, −8 502 €, −15 354 €. **ORVANE est en cessation de paiements au cours du mois 6** — sans compter les 20 580 € du fournisseur et les 8 270 € de TVA, qui tombent tous deux au mois 4.

### 8.2 Trajectoire B — traiter le goulot

L'équipe lit la trésorerie en premier. Elle voit cinq semaines. Elle prend la décision du § 7.8, puis une décision par semaine, toujours sur la contribution par commande : Cure par défaut, code éteint, remise ramenée à 4,0 %, abonnement introduit au mois 6, **budget de test maintenu à 15 %**.

| Mois | Cmd | AOV TTC | CA TTC | CM2 | Pub | CM3 | Fixes | EBITDA | Cumul |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| M4 | 700 | 50,80 € | 35 560 € | 59,8 % | 15 800 € | 1 921 € | 4 200 € | −2 279 € | −2 279 € |
| M5 | 730 | 52,60 € | 38 398 € | 60,6 % | 16 400 € | 2 991 € | 4 400 € | −1 409 € | −3 688 € |
| M6 | 780 | 54,10 € | 42 198 € | 61,3 % | 17 600 € | 3 956 € | 4 400 € | −444 € | −4 132 € |
| M7 | 840 | 55,20 € | 46 368 € | 62,0 % | 19 000 € | 4 957 € | 4 600 € | **+357 €** | −3 775 € |
| M8 | 910 | 56,10 € | 51 051 € | 62,6 % | 20 600 € | 6 053 € | 4 600 € | +1 453 € | −2 322 € |
| M9 | 980 | 56,60 € | 55 468 € | 63,0 % | 22 300 € | 6 821 € | 4 800 € | +2 021 € | **−302 €** |

Le chiffre d'affaires du mois 9 est de **55 468 € TTC, soit 12 801 € par semaine**. ORVANE n'est pas au palier P2 canonique (53 123 € par semaine), mais elle est vivante, à l'équilibre, et son MER moyen de **2,41** est au-dessus du seuil de 2,02 : chaque euro supplémentaire crée maintenant de la marge.

### 8.3 L'écart, et ce qu'il enseigne

| | Trajectoire A | Trajectoire B | Écart |
|---|---:|---:|---:|
| CA TTC cumulé sur 6 mois | 199 220 € | 269 043 € | +35,1 % |
| Dépense publicitaire cumulée | 115 000 € | 111 700 € | **−2,9 %** |
| MER moyen | 1,73 | 2,41 | +39,3 % |
| CM2 au mois 9 | 57,5 % | 63,0 % | +5,5 pts |
| **EBITDA cumulé sur 6 mois** | **−45 848 €** | **−302 €** | **45 546 €** |
| Trésorerie libre au mois 9 | −36 298 € | +9 248 € | |
| État de l'entreprise | morte au mois 6 | vivante, à l'équilibre | |

**Regarde la deuxième ligne.** B a dépensé **3 300 € de moins** en publicité et produit 69 823 € de chiffre d'affaires en plus. Aucun des 45 546 € d'écart ne vient d'un meilleur ciblage, d'un meilleur créatif ou d'une meilleure négociation média : tous viennent de trois gestes de bloc 2 — un code éteint, un mix déplacé vers la référence à forte contribution, une remise ramenée à la norme.

**Ce que le budget de test réduit a réellement acheté.** 11 points de test sur 115 000 € = 12 650 € « économisés », contre la mort de la machine créative, donc le décrochage du CPA à partir du mois 6, donc environ 30 000 € d'EBITDA perdu sur les trois derniers mois. **Rapport de 1 à 2,4 — et le délai de quatre mois entre la cause et l'effet est exactement ce qui rend la cause invisible quand l'effet arrive.**

> **À retenir :** la trajectoire A n'a pas commis d'erreur de calcul. Elle a commis une erreur d'**ordre**. Elle a lu le compte publicitaire en premier, et à partir de là toutes ses décisions étaient cohérentes — avec la mauvaise question.

**Honnêteté du modèle.** B tient de justesse : au mois 7 il faut passer un nouveau tour de stock, de l'ordre de 34 000 € HT, que 9 248 € de trésorerie libre ne financent pas. B a besoin d'un apport ou d'un crédit fournisseur allongé — et l'avoir vu au jour 90 plutôt qu'au jour 200 est précisément ce qui rend ce financement possible : on prête à une marque qui présente une trajectoire à l'équilibre, pas à une marque qui présente une urgence.

---

## 9. Avant la séance suivante

1. **Refais les blocs 1 et 2 sur tes chiffres**, avec `simulateur_tresorerie.py` puis `calculateur.py`. Deux nombres à écrire en haut de ton tableau de bord et à tenir chaque lundi : ta **trésorerie libre** et ta **contribution par commande en euros HT**. Si tu n'as pas encore vendu, fais-le sur les hypothèses de [S08](S08-le-lancement.md) — le geste compte plus que la donnée.
2. **Exporte tes commandes et lance `cohortes.py`.** Même avec trois cohortes et deux âges observables, tu verras ce qui est mesurable et ce qui ne l'est pas. Ce fichier est l'entrée de [S10](S10-installer-la-retention.md).
3. **Ouvre un compte bancaire séparé et vire-y la TVA collectée**, cette semaine. Meilleur rapport temps/risque de tout l'atelier : dix minutes, un mode de mort supprimé.

*Fin de la séance S09. Suite : [S10 — Installer la rétention](S10-installer-la-retention.md).*
