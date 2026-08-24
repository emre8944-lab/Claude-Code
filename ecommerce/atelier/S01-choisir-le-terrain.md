# Séance S01 — Choisir le terrain

> **Niveau requis :** L02 · **Durée :** 4 h · **Livrable :** une décision de catégorie argumentée, notée sur la grille à 9 critères et confrontée au MER seuil · **Modules :** [E01](../modules/E01-arithmetique-de-la-marque.md), [E02](../modules/E02-marche-et-produit.md)
>
> **Ce que tu ne peux pas faire sans cette séance :** rien de ce qui suit. S02 prouve une demande, S03 chiffre un coût de revient, S04 fixe un prix — les trois supposent une catégorie décidée, écrite et défendable devant quelqu'un qui te contredit.

---

## 1. Où tu en es

Tu n'as rien : ni produit, ni fournisseur, ni nom, ni client. C'est la meilleure position du parcours et tu ne la retrouveras jamais — **tout est réversible, rien ne t'a coûté.**

Déjà décidé, si tu as lu le socle : ton objectif est **P5+**, 20,3 % d'EBITDA et non 10,1 % ([canoniques § 8](../donnees/chiffres-canoniques.md)) ; le **MER seuil** vaut `(1 + TVA) ÷ taux de marge brute` ([E01](../modules/E01-arithmetique-de-la-marque.md) § 4.1) ; la porte 0 → P1 exige un coefficient ≥ ×5,0 rendu entrepôt ([jalons](../mentorat/jalons.md)). *MER : chiffre d'affaires TTC ÷ dépense publicitaire.* Tout le reste est ouvert.

Une phrase, désagréable. Deux fondateurs de talent égal, mêmes heures, même capital, même discipline, finissent à des ordres de grandeur différents parce que l'un a choisi une catégorie à coefficient ×7 et réachat trimestriel, l'autre ×3,5 et réachat annuel. Le § 8 le démontre sur 24 mois à dépense publicitaire identique au centime près : **491 875 € d'écart d'EBITDA cumulé, sans rapport avec le talent.**

---

## 2. Ta mission

**Produire une décision de catégorie, écrite, notée et chiffrée**, au format du § 5. Trois résultats :

1. **Huit à douze candidates**, générées par une méthode systématique — pas par introspection — chacune rattachée à sa source.
2. **Trois finalistes**, filtrées par les cinq variables structurelles d'[E02](../modules/E02-marche-et-produit.md) § 1, puis notées sur sa grille à 9 critères (§ 3, 45 points).
3. **Une décision**, adossée à la confrontation entre le MER seuil qu'implique chaque finaliste et le MER que la catégorie permet d'atteindre — avec la phrase chiffrée qui dit ce qui te ferait changer d'avis.

Ni nom, ni logo, ni fournisseur, ni analyse SWOT : rien de cela ne décide rien à ce stade. Répartition des 4 h : 1 h de génération, 1 h de filtrage, 1 h 30 de notation et calcul, 30 min de rédaction. Si tu y passes trois jours, tu ne décides pas, tu repousses.

---

## 3. Ce dont tu disposes

[`calculateur.py`](../outils/calculateur.py) pour ta cascade et ton MER seuil (étape 4) · [`simulateur_marque.py`](../outils/simulateur_marque.py) pour rejouer une stratégie dans deux catégories à graine identique (§ 9) · [`chiffres-canoniques.md`](../donnees/chiffres-canoniques.md) § 1 et § 2.1 comme calibration · [`E02`](../modules/E02-marche-et-produit.md) § 1 à § 3, dont cette séance est l'application · [`C01`](../etudes-de-cas/C01-coefficient-insuffisant.md) et [`jalons`](../mentorat/jalons.md), porte 0 → P1.

Fourni ici : le **tableau de référence des six catégories du simulateur** (étape 2). À aller chercher toi-même : le prix public médian de ta catégorie, un ordre de grandeur de coût de revient, la durée de consommation d'une unité, le poids expédié. Rien d'autre.

---

## 4. La méthode, pas à pas

### Étape 1 — Générer 8 à 12 candidates par les six sources

Une candidate s'écrit en une ligne : **[catégorie] pour [segment] avec [angle supposé]** — « soin visage pour adultes de 25–40 ans à acné hormonale, tolérance cutanée mesurée ». Pas « la beauté ».

**1. Les irritants documentés** — les avis 1 et 2 étoiles des trois leaders de cinq catégories consommables : le gisement le plus dense, un irritant récurrent étant une demande non servie écrite par le client lui-même. **2. Les segments mal servis** — où le produit existe mais où la formulation, la taille ou le prix ne s'adressent à personne. **3. Les migrations réglementaires** — ce qui vient d'être interdit : toute interdiction ouvre un marché de substitution. **4. Le retard d'adoption en direct** — catégories encore dominées par la distribution physique ; vérifie *pourquoi* la place est vide ([S02](S02-prouver-la-demande.md), test b). **5. Le geste professionnel qui descend** — ce qu'un professionnel fait en cabine et qui devient faisable seul. **6. Ce que tu consommes déjà** — le vocabulaire et l'accès aux communautés, **rien de plus**.

Deux candidates par source, douze au total, dont tu en jetteras neuf.

#### Pourquoi « ce qui te passionne » n'est pas une source

C'est le conseil le plus répandu, et il produit une part écrasante des échecs de la porte 0 → P1. **Un.** La passion est une information sur toi, pas sur le marché : aucune des cinq variables structurelles ne bouge selon ton enthousiasme. **Deux.** Elle fausse ton estimation de la demande, toujours dans le même sens — passionné d'une catégorie, tu es dans le percentile supérieur des acheteurs et tu prends ton comportement pour la moyenne alors que tu es l'exception statistique. C'est ce mécanisme, pas la malchance, qui produit les lancements où « tout le monde à qui j'en parlais trouvait ça génial » — c'est-à-dire des gens qui te ressemblent. **Trois.** Elle rend la sortie impossible : le jour où tes cohortes diront d'arrêter, tu chercheras une explication, parce que la passion transforme une décision en identité et qu'une identité ne se corrige pas avec un tableau de cohortes.

Ce qu'elle apporte : pas la qualité du choix, la **durée**. **Ce n'est donc pas un critère de sélection mais de départage** — tu l'utilises **en dernier**, entre deux finalistes ayant déjà passé le filtre structurel et la confrontation au MER seuil. L'ordre des opérations *est* la méthode.

### Étape 2 — Filtrer par les cinq variables structurelles

Les cinq variables d'[E02](../modules/E02-marche-et-produit.md) § 1. Structurelles au sens propre : **elles ne bougent pas par l'effort.** Tu peux améliorer ta créa et ton site ; tu ne peux pas rendre un canapé léger ni faire qu'on rachète une lampe tous les trois mois.

**1. Coefficient rendu entrepôt** — PVC TTC ÷ coût de revient complet. Éliminatoire **< ×5,0** (porte 0 → P1). **2. Fréquence de réachat naturelle** — éliminatoire **> 8 mois** au titre de la porte, mais [E02](../modules/E02-marche-et-produit.md) § 1.2 démontre que le seuil économique réel est **5,7 mois** : au-delà, la LTV à 12 mois ne finance plus un nCAC de 40 €, quel que soit le coefficient. **3. Taux de retour structurel** — éliminatoire **> 25 %**. **4. Poids et densité de valeur** — en euros de PVC par kilogramme expédié ; sous 12 €/kg la logistique mange la marge (§ 1.4). **5. Barrière d'entrée** — euros et mois avant la première vente légale **et** avant la première publicité légale ; à double lecture, une barrière forte te protégeant autant qu'elle te retarde.

Une candidate qui touche un seuil est éliminée : pas discutée, pas « en réserve ». Tu écris pourquoi, et tu le reliras en S12.

**La conversion qui te servira toute ta vie.** `COGS en % du CA HT = (1 + TVA) ÷ coefficient = 1,20 ÷ coefficient`. Contrôle sur le Sérum Densité de NØRA (canoniques § 1), 39,00 € TTC pour 4,80 € de COGS, soit ×8,1 : 1,20 ÷ 8,1 = 14,8 %, et directement 4,80 ÷ 32,50 = 14,8 % ✓. De tête : ×5 → **24,0 %** · ×7 → **17,1 %** · ×8 → 15,0 % · ×3,5 → **34,3 %** · ×3 → 40,0 %.

#### Le tableau de référence des six catégories du simulateur

*Les quatre premières colonnes sont les paramètres déclarés dans [`simulateur_marque.py`](../outils/simulateur_marque.py) — exactement ce qu'il applique quand tu lui passes `--categorie`. Les suivantes en dérivent par quatre règles déclarées : coefficient obtenu au lancement = 84 % du maximum de la catégorie, faute de volume au premier lot ; logistique au palier P2 = tarif plancher + 3 points ; ligne retours-SAV = 0,5 × taux de retour + 0,75 point de SAV ; remises 5,0 % (7,0 % là où la catégorie solde). Contrôle : la ligne soin capillaire reproduit la cascade canonique de NØRA à P2 — CM2 58,9 % contre 58,8 %, nCAC 30,80 € contre 30,78 €, MER 2,20 (canoniques § 2 et § 2.1).*

| Catégorie (`--categorie`) | Coef. max | Fréq. | Retour | Coef. retenu | **CM2** | **MER seuil** | AOV TTC | nCAC | **MER atteign.** | **Écart** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `soin_cheveux` | ×8,0 | 3,0 m | 3,5 % | ×6,7 | **58,9 %** | **2,04** | 57,55 € | 30,80 € | **2,20** | **+7,8 %** |
| `complement` | ×7,5 | 1,5 m | 2,0 % | ×6,3 | **60,5 %** | **1,98** | 66,60 € | 35,20 € | **2,28** | **+15,2 %** |
| `soin_visage` | ×8,5 | 2,5 m | 4,0 % | ×7,1 | **60,7 %** | **1,98** | 72,52 € | 39,60 € | **2,17** | **+9,7 %** |
| `animalerie` | ×6,0 | 2,0 m | 5,0 % | ×5,0 | **48,1 %** | **2,50** | 51,80 € | 26,40 € | **2,35** | **−6,1 %** |
| `maison_deco` | ×4,5 | 14,0 m | 12,0 % | ×3,8 | **28,0 %** | **4,29** | 96,20 € | 24,20 € | **4,32** | **+0,6 %** |
| `mode_accessoire` | ×3,5 | 10,0 m | 28,0 % | ×2,9 | **15,2 %** | **7,91** | 81,40 € | 28,60 € | **3,15** | **−60,2 %** |

**Trois lectures, et il faut faire les trois.**

**Un.** La porte de fréquence d'[E02](../modules/E02-marche-et-produit.md) § 1.2 — 5,7 mois — élimine d'entrée `maison_deco` (14,0 mois, 146 % au-dessus) et `mode_accessoire` (10,0 mois). Des quatre restantes, `animalerie` échoue la porte du MER à −6,1 %. **Trois catégories sur six passent** : soin capillaire, complément, soin visage.

**Deux. `maison_deco` affiche un MER atteignable de 4,32 pour un seuil de 4,29 : elle est au-dessus de son seuil et elle est morte quand même.** Son panier de 96,20 € et son coût pour mille très bas la font passer *au mois* ; c'est sa fréquence de 14 mois qui la tue, un client qui revient tous les quatorze mois ne remboursant jamais son coût d'acquisition dans une fenêtre finançable. **Le MER décrit un mois ; la fréquence décrit une vie de client.** C'est pour cette raison que le filtre structurel passe **avant** la grille et avant le MER.

**Trois. `mode_accessoire` n'est pas difficile, elle est arithmétiquement hors d'atteinte** : ×3,5 plafond et 28 % de retours donnent 15,2 % de marge brute et un MER seuil de **7,91**, quand le meilleur MER de NØRA, à sept marchés et dix ans, vaut 2,90 (canoniques § 2.3). Aucune exécution ne comble un facteur 2,7 ([E02](../modules/E02-marche-et-produit.md) § 2.2). Note enfin que le soin capillaire n'a que +7,8 % de marge au seuil : **une catégorie viable n'est pas une catégorie confortable.**

### Étape 3 — Noter les trois finalistes sur la grille à 9 critères

La grille d'[E02](../modules/E02-marche-et-produit.md) § 3 : neuf critères notés **0 à 5**, **45 points**, seuil **32/45**, deux verrous — **aucun critère sous 2**, **critère 1 jamais sous 3**.

| # | Critère | 0 | 3 | 5 |
|---:|---|---|---|---|
| 1 | **Coefficient rendu entrepôt** | < ×3 | ×5 à ×6 | > ×7,5 |
| 2 | **Fréquence de réachat naturelle** | > 12 mois | 4 à 6 mois | < 8 semaines |
| 3 | **Taux de retour structurel** | > 25 % | 8 à 12 % | < 4 % |
| 4 | **Densité de valeur** | < 12 €/kg | 25 à 45 €/kg | > 70 €/kg |
| 5 | **AOV atteignable et bundlable** | < 25 € | 40 à 55 € | > 70 € |
| 6 | **Mécanisme différenciant défendable** | Aucun | Format ou procédé | Formule ou exclusivité |
| 7 | **Demande existante et exprimée** | Aucune recherche | Recherche, peu d'annonceurs | Recherche forte + annonceurs installés |
| 8 | **Barrière d'entrée** | Nulle | Moyenne (dossier, agrément) | Forte et récurrente |
| 9 | **Charge de preuve créative** | Effet invisible et différé | Preuve possible mais lente | Démontrable en 10 secondes |

**Les verrous sont la partie utile.** Un total masque une porte fermée : un produit à 38 points dont le coefficient vaut ×3,5 est un produit mort avec un beau bulletin. Une candidate à 34/45 avec un critère à 1 est éliminée ; une candidate à 32/45 sans critère sous 2 passe.

**Le critère 7** récompense la présence d'annonceurs installés : la concurrence publicitaire est un signal **positif**, son absence est le piège le plus coûteux du métier ([S02](S02-prouver-la-demande.md), test b). **Le critère 9** décide de ta machine créative : si l'effet de ton produit ne se voit pas en dix secondes, ton taux de concepts gagnants s'effondre — le goulot de tout le parcours (canoniques § 6).

### Étape 4 — Calculer le MER seuil et le confronter à ce que la catégorie permet

Celle que personne ne fait, et qui décide. **Premier nombre : ce que ta cascade de coûts exige.**

```
MER seuil (CM3 = 0)    = 1,20 ÷ CM2
   Contrôle NØRA P5 : 1,20 ÷ 0,6145 = 1,95            ✓ canoniques § 2.3
MER seuil (EBITDA = 0) = 1,20 ÷ (CM2 − frais fixes en % du CA HT)
   Palier P1, fixes à 21,2 % du CA HT (canoniques § 2.5), CM2 60,4 % :
   1,20 ÷ (0,604 − 0,212) = 3,06 — inatteignable en année 1, et c'est prévu :
   la porte 0 → P1 exige que le capital couvre P1 et P2.
```

**Second nombre : ce que ta catégorie permet réellement.** Il se dérive.

```
                        AOV TTC ÷ nCAC
MER atteignable  =  ─────────────────────────────────
                    1 − part des commandes en réachat

   car CA TTC = commandes × AOV, dépense = nouveaux × nCAC,
   et nouveaux = commandes × (1 − part de réachat)

Contrôle NØRA au palier P2 (canoniques § 2 et § 2.4) :
   4 000 commandes/mois, 3 400 nouveaux → réachat 15,0 %
   (57,55 ÷ 30,78) ÷ 0,850 = 1,8697 ÷ 0,850 = 2,20      ✓ MER canonique P2
Contrôle au palier P5 : 60 200 commandes, 37 324 nouveaux → réachat 38,0 %
   (71,98 ÷ 40,03) ÷ 0,620 = 2,90                       ✓ MER canonique P5
```

Deux contrôles exacts sur deux paliers écartés de trente mois : ce n'est pas une approximation, c'est l'identité comptable du MER. **Ton MER se fabrique avec trois leviers et trois seulement** — panier, coût d'acquisition, part de réachat. Optimiser tes campagnes agit sur le nCAC seul.

**La part de réachat se dérive de la fréquence**, par le modèle du cursus calibré sur la courbe canonique § 3 :

```
   C(t, F) = 1 + 1,896 × ln( 1 + t ÷ (4,333 × F) )   commandes cumulées
   par client après t mois, à fréquence F mois

   Calibration NØRA (F = 3) : t=12 → 2,24 (canon. 2,24) · t=24 → 2,98 (2,98) ✓
   réachat en commandes, régime P2 = 0,24 × (1 − 1 ÷ C(18, F))
   Contrôle NØRA : 0,24 × (1 − 1/2,65) = 14,9 % ≈ 15,0 % canonique          ✓
```

*Le facteur 0,24 est un coefficient de régime : une marque qui triple de taille en six mois a une base installée jeune, donc une part de réachat très inférieure à ce que ses cohortes produiraient à volume stable. Calibré sur P2.*

Écris les deux nombres côte à côte. **Une finaliste dont le MER atteignable est sous son seuil est éliminée**, quelle que soit sa note — et ça arrive à 34/45.

### Étape 5 — Décider

Dans cet ordre. **Un :** élimine ce qui touche un seuil du filtre structurel. **Deux :** élimine ce qui déclenche un verrou de la grille, quel que soit le total. **Trois :** élimine ce dont le MER atteignable est sous le seuil sans chemin de rattrapage chiffré. **Quatre :** classe le reste sur 45, et départage les écarts de moins de 3 points par le chemin de rattrapage le plus court, puis ton accès au sujet, puis — en dernier — ton intérêt à long terme. **Cinq :** écris la condition de renversement, le fait chiffré et observable en S02 qui te ferait changer d'avis. Sans elle, ce n'est pas une décision, c'est une croyance.

---

## 5. Ton livrable

Copie et remplis.

```
LIVRABLE S01 — DÉCISION DE CATÉGORIE                     Date : __/__/____

A. CANDIDATES ET FILTRE STRUCTUREL (E02 § 1)              (8 à 12 lignes)
 #  Src  Catégorie / segment / angle  Coef. Fréq. Ret.% €/kg Barrière  Verdict + motif
 1  ___  _________________________    ____  ____  ____  ____ ________  ____________
 …                                            (une ligne par candidate)
 Sources : 1☐ 2☐ 3☐ 4☐ 5☐ 6☐ (≥ 4)  Éliminées : __/__
 Finalistes : F1 ________  F2 ________  F3 ________

B. GRILLE À 9 CRITÈRES (E02 § 3, 0 à 5)          F1      F2      F3
 1 Coefficient · 2 Fréquence · 3 Retours · 4 Densité de valeur
 5 AOV · 6 Mécanisme · 7 Demande · 8 Barrière · 9 Preuve créative
 Une note de 0 à 5 par critère              __/5    __/5    __/5
 TOTAL (seuil 32)                          __/45   __/45   __/45
 VERROUS  critère < 2 ? ☐n°__ ☐n°__ ☐n°__   critère 1 < 3 ? ☐ ☐ ☐

C. CASCADE ET MER                              F1        F2        F3
 PVC cible TTC / COGS rendu entrepôt   __€/__€  __€/__€  __€/__€
 Coefficient / COGS % du CA HT         __/__%   __/__%   __/__%
 Logist. / PSP / Ret.-SAV / Remises    _/_/_/_  _/_/_/_  _/_/_/_
 = MARGE BRUTE CM2                     _____%   _____%   _____%
 MER seuil CM3=0 / EBITDA=0            ___/___  ___/___  ___/___
 AOV cible TTC / nCAC estimé           __€/__€  __€/__€  __€/__€
 Fréquence F / C(18, F) / réachat      _/_/__%  _/_/__%  _/_/__%
 MER ATTEIGNABLE / ÉCART AU SEUIL      __/___%  __/___%  __/___%

D. DÉCISION
 Catégorie retenue : ______________ Segment : ______________
 Angle supposé : _______________________________________
 Pourquoi elle — trois phrases, deux nombres au moins : _________
 Pourquoi PAS la deuxième (une phrase, un nombre) : _____________
 Chemin de rattrapage si l'écart est négatif ou < 5 % : _________
 CONDITION DE RENVERSEMENT : « Si ______________ est ______
   (chiffré), j'abandonne cette catégorie et je reprends F__. »
 Ce que je m'interdis d'invoquer pour ne pas l'appliquer : _______
```

---

## 6. La grille d'évaluation

Sur 100. Elle note **ton travail**, pas ta catégorie.

| # | Critère | Pts | Ce qui vaut les points | Ce qui les fait perdre |
|---|---|---:|---|---|
| 1 | Génération systématique | 12 | 8 à 12 candidates, ≥ 4 sources, chacune rattachée | < 8 : −6. Une seule source : −8. Non déclarées : 0 |
| 2 | Précision des candidates | 8 | Catégorie **et** segment **et** angle par ligne | « La beauté », « le fitness » : −2 par ligne |
| 3 | Filtre structurel appliqué | 14 | Les 5 variables d'E02 § 1 pour **toutes** les candidates | Finalistes seules : −8. Motif absent : −1/ligne. Densité absente : −4 |
| 4 | Notation sur 45 et verrous | 14 | Trois finalistes notées critère par critère | Note globale sans détail : −10. Verrou non signalé : −7 |
| 5 | Cascade de marge complète | 14 | Six lignes de coût variable, CM2, tout montant marqué TTC ou HT | Montant sans TTC/HT : **−5 chacun**. Sans PSP ni remise : −6 |
| 6 | **Les deux MER, confrontés** | 20 | MER seuil **et** MER atteignable, écart en % | MER seuil seul : −12. Aucun MER : 0 |
| 7 | Décision et justification | 10 | Trois phrases, deux nombres, le « pourquoi pas la deuxième » | Aucun nombre : −7 |
| 8 | Condition de renversement | 8 | Chiffrée, sur un fait observable en S02 | « Si ça ne marche pas » : 0. Non chiffrée : −5 |

**Seuil de validation : 70/100. Fautes éliminatoires, séance à refaire quelle que soit la note :** un coefficient retenu sous ×5,0 ([C01](../etudes-de-cas/C01-coefficient-insuffisant.md)) ; une finaliste retenue malgré un verrou de la grille ; un MER atteignable sous le seuil sans chemin de rattrapage chiffré — avoir fait le calcul et décidé contre lui est pire que de ne pas l'avoir fait ; une fréquence supérieure à 8 mois ; un coefficient calculé sur le prix d'achat usine au lieu du coût rendu entrepôt, ce qui transforme couramment un ×5,2 en ×3,4 ; une justification qui commence par « parce que ça me passionne ».

---

## 7. Le corrigé exemplaire

> **Cas composite. Marque fictive.** CLARÈNE n'existe pas. Les chiffres sont un modèle calibré sur les ordres de grandeur du cursus : ce ne sont les comptes d'aucune entreprise réelle, et aucun chiffre privé n'est attribué ici à une entreprise existante.

**LIVRABLE S01 — projet CLARÈNE — 4 h 10 de travail**

### A. Les douze candidates et le filtre structurel

| # | Catégorie / segment / angle | Coef. | Fréq. | €/kg | Verdict et motif |
|---|---|---:|---:|---:|---|
| 1 | Soin visage, adultes 25–40 ans à acné hormonale, tolérance mesurée | ×7,4 | 2,5 m | 113 | **Retenue — F1** (retour 3 %) |
| 2 | Café de spécialité, buveurs quotidiens | ×2,8 | 1,0 m | 58 | Éliminée — coefficient < ×5,0 |
| 3 | Complément sommeil sans mélatonine, 30–50 ans | ×8,1 | 1,0 m | 240 | Éliminée — aucune allégation sommeil autorisée |
| 4 | Solaire visage sans fini blanc, peaux mates | ×5,6 | 9,0 m | 96 | Éliminée — fréquence 9 m ; 71 % du CA sur 4 mois |
| 5 | Lessive sans microcapsules de parfum | ×3,2 | 3,0 m | **6** | Éliminée — coefficient **et** densité de valeur |
| 6 | Entretien ménager rechargeable | ×4,0 | 4,0 m | 31 | Éliminée — coefficient < ×5,0 |
| 7 | Soin capillaire cheveux texturés, femmes 25–45 ans | ×6,3 | 2,5 m | 47 | **Retenue — F2** (retour 2,5 %) |
| 8 | Complément périménopause, femmes 42–55 ans | ×8,4 | 1,0 m | 260 | **Retenue — F3** (retour 1,5 %) |
| 9 | Litière végétale agglomérante | ×3,0 | 1,5 m | **2** | Éliminée — coefficient **et** 9,2 kg par commande |
| 10 | Petit électroménager de cuisine | ×3,9 | 60 m | 44 | Éliminée — les trois premières variables |
| 11 | Peeling à l'acide mandélique dosé | ×7,8 | 2,5 m | 130 | Éliminée — recouvre F1 à 80 % |
| 12 | Coloration capillaire assistée à domicile | ×6,9 | 2,0 m | 89 | Éliminée — SAV structurel : résultat subjectif |

Les six sources utilisées. Éliminées : **9 / 12**. Finalistes : **F1** soin visage adulte · **F2** capillaire texturé · **F3** complément périménopause.

### B. La grille à 9 critères

| # | Critère | F1 soin visage | F2 capillaire texturé | F3 périménopause |
|---:|---|---:|---:|---:|
| 1 | Coefficient | 4 — ×7,39 | 3 — ×6,30 | **5** — ×8,39 |
| 2 | Fréquence | 4 — 10 semaines | 4 — 10 semaines | **5** — 4 semaines |
| 3 | Taux de retour | **5** — 3 % | **5** — 2,5 % | **5** — 1,5 % |
| 4 | Densité de valeur | **5** — 113 €/kg | 3 — 47 €/kg | **5** — 260 €/kg |
| 5 | AOV | 3 — 52,00 € | 3 — 47,00 € | 3 — 42,00 € |
| 6 | Mécanisme différenciant | 4 — formule + dose calibrée | 3 — format | 4 — formule |
| 7 | Demande exprimée | **5** — 48 100 rech., 11 annonceurs | 4 — 7 annonceurs | **1** — 3 annonceurs, aucun installé |
| 8 | Barrière | 3 — CPNP + DIP | 3 — idem | **5** — allégations |
| 9 | Preuve créative | 3 — visible à 8 semaines | **5** — boucle visible immédiatement | **1** — effet invisible et différé |
| | **TOTAL** | **36 / 45** | **33 / 45** | **34 / 45** |

**Le moment le plus important du corrigé.** F3 obtient 34/45, au-dessus du seuil, et le maximum sur les quatre variables structurelles — coefficient, fréquence, retours, densité. Elle est deuxième au classement. **Et elle est refusée**, parce que **deux verrous se déclenchent** : critères 7 et 9 à 1. La grille ne classe pas, elle ferme des portes, et une porte fermée ne se rachète avec aucun total.

Les deux verrous ne sont pas indépendants : le critère 9 à 1 **cause** le critère 7 à 1. Personne ne diffuse longtemps sur ce sujet parce que la réglementation des allégations interdit à peu près tout ce qu'on voudrait dire et qu'aucune créa ne peut montrer le résultat. **La barrière n'est pas de vendre, elle est de dire.**

### C. La cascade et le MER

|  | **F1** soin visage | **F2** capillaire texturé | **F3** périménopause |
|---|---:|---:|---:|
| PVC cible TTC / COGS rendu entrepôt | 34,00 € / 4,60 € | 26,00 € / 4,13 € | 39,00 € / 4,65 € |
| **Coefficient** (mixte de gamme) | **×7,39** (×7,00) | **×6,30** (×6,30) | **×8,39** (×8,40) |
| COGS % du CA HT (1,20 ÷ coef) | 17,14 % | 19,05 % | 14,29 % |
| Logist. / PSP / Ret.-SAV / Remises | 13,50 / 1,70 / 2,25 / 5,00 % | 15,00 / 1,70 / 2,00 / 6,00 % | 11,00 / 1,70 / 1,50 / 7,00 % |
| **MARGE BRUTE CM2** | **60,41 %** | **56,25 %** | **64,51 %** |
| **MER seuil CM3 = 0** | **1,99** | **2,13** | **1,86** |
| AOV cible TTC / nCAC estimé | 52,00 € / 27,00 € | 47,00 € / 30,00 € | 42,00 € / 34,00 € |
| Fréquence F / C(18, F) | 2,5 mois / 2,86 | 2,5 mois / 2,86 | 1,0 mois / 4,11 |
| Part de réachat en commandes | 15,6 % | 15,6 % | 18,2 % |
| **MER ATTEIGNABLE** | **2,28** | **1,86** | **1,51** |
| **ÉCART AU SEUIL** | **+14,9 %** | **−13,0 %** | **−18,9 %** |

```
F1  CM2 = 100 − (17,14 + 13,50 + 1,70 + 2,25 + 5,00)         = 60,41 %
    MER seuil = 1,20 ÷ 0,6041 → 1,99
    C(18 ; 2,5) = 1 + 1,896 × ln(1 + 18 ÷ 10,833) = 2,858
    réachat = 0,24 × (1 − 1 ÷ 2,858) = 15,6 %
    MER atteignable = (52,00 ÷ 27,00) ÷ 0,844 → 2,28 · écart = +14,9 %
F3  CM2 64,51 % · seuil 1,86 · (42,00 ÷ 34,00) ÷ 0,818 → 1,51 · −18,9 %
```

**Le verdict que la note ne donnait pas.** F3 a la meilleure marge brute du dossier — 64,51 %, trois points au-dessus du palier P5 de NØRA — et échoue le plus lourdement, pour une raison sans rapport avec sa marge : **panier bas, coût d'acquisition élevé**, 42,00 ÷ 34,00 = 1,24. F2 échoue plus simplement : ×6,30 et 15,0 % de logistique — les 400 ml pèsent, d'où son 3 au critère 4 — donnent 56,25 % de CM2 et un MER atteignable 13,0 % sous le sien.

### D. La décision

**Catégorie retenue : soin visage.** Segment : adultes de 25 à 40 ans à imperfections persistantes ou hormonales, ayant déjà essayé deux routines. Angle : efficacité mesurée sans agression cutanée — la catégorie fait l'inverse et le paie dans ses avis.

1. **C'est la seule sans verrou et dont le MER atteignable dépasse son seuil** : 2,28 contre 1,99, soit +14,9 % de marge de manœuvre. Les deux autres, à −13,0 % et −18,9 %, détruisent de la contribution à chaque euro dépensé au palier P2.
2. **Sa demande est exprimée et ses concurrents paient pour elle** : 48 100 recherches mensuelles, 11 annonceurs actifs dont 3 diffusant une créa de plus de 180 jours. Personne ne paie 180 jours pour une publicité qui perd de l'argent.
3. **Sa densité de valeur est de 113 €/kg** contre 47 pour F2 : la logistique restera sous 14 % du CA HT même en multipliant les références, soit trois points de marge brute préservés.

Pourquoi pas F3, deuxième au classement : **parce que 64,51 % de marge brute ne servent à rien si l'on n'achète du trafic qu'à un MER de 1,51 pour un seuil de 1,86, et si deux verrous sont tombés.** Deux points de grille contre 19 points de MER relatif : le calcul l'emporte sur la note, toujours.

**Condition de renversement.** « Si le dépouillement des avis en S02 ne fait pas apparaître trois défauts couvrant au moins 45 % des critiques, ou si le smoke test rend un coût par inscription supérieur à 5,00 € TTC, j'abandonne le soin visage et je reprends F2 en corrigeant d'abord son format vers 250 ml. » Ce que je m'interdis d'invoquer pour ne pas l'appliquer : « le test était mal ciblé », « la créa n'était pas bonne », « il aurait fallu plus de budget ». Un doute sur le dispositif se corrige **avant** d'en lire les résultats.

---

## 8. Les conséquences chiffrées de ton choix

Deux fondateurs. Même capital, même temps, même compétence, même budget publicitaire **au centime près**. L'un en catégorie A, calibrée sur `soin_cheveux` — ×7,0, réachat tous les 3 mois ; l'autre en B, calibrée sur `mode_accessoire` — ×3,5, tous les 10 mois.

### 8.1 Ce qui est tenu identique

Publicité **16 000 € HT/mois**, 384 000 € HT sur 24 mois · nCAC **32,00 €** · **500 nouveaux clients/mois** · panier **62,00 € TTC** · fixes **8 000 €/mois** · TVA 20 %. *Panier et nCAC sont figés pour isoler les deux variables qui changent. La cascade de B est volontairement **généreuse** : le simulateur lui applique 20,0 % de logistique et 14,75 % de retours-SAV, donc un résultat bien pire.*

| % du CA HT | COGS | Logist. | PSP | Ret.-SAV | Remises | **CM2** | **MER seuil** |
|---|---:|---:|---:|---:|---:|---:|---:|
| **A** | 17,14 % | 13,00 % | 1,70 % | 2,50 % | 5,00 % | **60,66 %** | **1,98** |
| **B** | 34,29 % | 14,00 % | 1,70 % | 6,00 % | 7,00 % | **37,01 %** | **3,24** |

### 8.2 Les deux trajectoires

| Mois | A : CA TTC | A : MER | **A : EBITDA cum.** | B : CA TTC | B : MER | **B : EBITDA cum.** |
|---|---:|---:|---:|---:|---:|---:|
| M1 | 35 356 € | 2,21 | **−6 128 €** | 32 341 € | 2,02 | **−14 024 €** |
| M6 | 53 305 € | 3,33 | **−8 446 €** | 38 622 € | 2,41 | **−78 251 €** |
| M12 | 69 435 € | 4,34 | **+38 844 €** | 45 368 € | 2,84 | **−143 374 €** |
| M18 | 82 079 € | 5,13 | **+128 468 €** | 51 419 € | 3,21 | **−196 785 €** |
| M24 | 92 478 € | 5,78 | **+252 251 €** | 56 905 € | 3,56 | **−239 624 €** |

*Le MER de A grimpe à 5,78 parce que le budget est figé 24 mois : la base vieillit et la part de réachat monte. Non comparable au 2,70 canonique de P3.*

|  | A | B | Écart |
|---|---:|---:|---:|
| Publicité / nouveaux clients | 384 000 € HT / 12 000 | 384 000 € HT / 12 000 | **0** |
| Commandes / par client | 26 428 / 2,20 | 17 589 / 1,47 | −33,4 % |
| CA TTC | 1 638 556 € | 1 090 529 € | −33,4 % |
| Marge brute | 828 251 € | 336 376 € | **−59,4 %** |
| CM3 (après publicité) | +444 251 € | **−47 624 €** | — |
| **EBITDA cumulé** | **+252 251 €** | **−239 624 €** | **491 875 €** |
| 1ᵉʳ EBITDA mensuel positif | **M5** | **jamais** | — |
| Point bas d'exploitation | −12 729 € au M4 | −239 624 € au M24, en baisse | — |

**Lis la dernière ligne deux fois.** A touche son point bas au quatrième mois, sous 13 000 €, et remonte ; B n'a pas de point bas — au vingt-quatrième mois il creuse encore. Les deux travaillent autant : l'un pilote une entreprise, l'autre finance un passe-temps.

### 8.3 D'où vient l'écart, et ce qu'il faudrait à B

En changeant une variable à la fois depuis A : dégrader le coefficient à ×3,5 coûte **234 079 €** (EBITDA cumulé +18 172 €) ; dégrader ensuite la fréquence à 10 mois coûte **198 725 €** (−180 553 €) ; les coûts propres à un bien durable coûtent les **59 071 €** restants. Dans l'ordre inverse la fréquence pèse 277 014 € et le coefficient 155 790 € : la répartition dépend de l'ordre, c'est le propre d'un effet multiplicatif. Ce qui n'en dépend pas : **chacune pèse entre 155 000 € et 277 000 € sur 24 mois.**

**Quel coefficient faudrait-il à B, à fréquence de 10 mois ?** Cas extrême, COGS = 0 : CM2 = 100 − (0 + 14,00 + 1,70 + 6,00 + 7,00) = 71,30 % ; marge brute 908 774 × 0,7130 = 647 956 € ; EBITDA = 647 956 − 384 000 − 192 000 = **71 956 €**, soit **180 295 €** de moins que A. **Aucun coefficient ne suffit** : même produit gratuit, 12 000 clients qui commandent 1,47 fois ne produisent pas ce que 12 000 clients qui commandent 2,20 fois produisent. **Et quelle fréquence, à ×3,5 ?** **F = 0,84 mois**, un réachat tous les 25 jours. Un bien durable racheté tous les 25 jours n'est pas un bien durable : la question n'a pas de réponse dans sa catégorie, elle en a une dans une autre.

> **À retenir :** coefficient et fréquence ne se compensent ni l'un par l'autre, ni par l'exécution. À dépense publicitaire identique ils produisent 491 875 € d'écart d'EBITDA en 24 mois, et le rattrapage exigerait soit un produit gratuit, soit un réachat mensuel. **C'est pourquoi cette séance est la première.**

---

## 9. Avant la séance suivante

**1. Rejoue ta décision dans le simulateur (exercice L02).** Une stratégie, deux catégories, **la même graine** :

```bash
python3 ecommerce/outils/simulateur_marque.py --auto equilibree --categorie soin_visage --graine 4211
python3 ecommerce/outils/simulateur_marque.py --auto equilibree --categorie maison_deco --graine 4211
```

La graine identique fige la chance créative, les incidents et la saisonnalité : tout ce qui diffère vient de la structure de la catégorie. Rejoue ensuite ta catégorie retenue contre celle classée deuxième, même graine, et écris en trois lignes ce que tu observes aux mois 12 et 24.

**2. Prépare le dépouillement des avis.** Repère les cinq produits les mieux notés de ta catégorie sur la marketplace dominante, vérifie qu'au moins trois dépassent 500 avis, collecte 200 avis 1 et 2 étoiles de moins de 18 mois. C'est le seul travail de S02 qu'on ne peut pas accélérer.

**3. Écris ton budget de validation et tes six seuils avant d'avoir rien vu**, dans un fichier daté. Un seuil écrit après le test est une justification — [protocole](../mentorat/protocole.md) § 6, faute n° 4.

---

*Fin de la séance S01. Suite : [S02 — Prouver la demande avant de produire](S02-prouver-la-demande.md).*
