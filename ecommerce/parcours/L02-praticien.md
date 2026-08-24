# Niveau L02 — Praticien

> **Prérequis :** niveau [L01](L01-initié.md) validé — 75 / 100, sans question éliminatoire ratée.
> **Ce que tu sais faire à la sortie :**
> — tu chiffres un coût de revient complet **rendu entrepôt** depuis un devis, en retrouvant les six postes que le devis ne contient pas ;
> — tu construis la cascade jusqu'au MER seuil pour trois produits qui n'existent pas encore et tu désignes celui dont la structure autorise l'objectif, par le calcul et non par le goût ;
> — tu écris un protocole de demande dont les six seuils sont **dérivés** de ton objectif et **datés avant** le premier euro dépensé.
>
> **Temps de travail typique :** 30 à 45 h — 10 h de lecture, 14 à 24 h d'atelier et de sourcing, 3 h de simulateur, 3 h d'épreuve.

---

## 0. Les deux échelles — et le piège propre à ce niveau

| Échelle | Ce qu'elle mesure | Ce qui la fait monter |
|---|---|---|
| **Lxx** | Ta **compétence** | Une épreuve réussie sur un dossier inconnu |
| **Nx** | L'état de ton **business** | Ton chiffre d'affaires et tes indicateurs mesurés ([diagnostic](../mentorat/diagnostic.md)) |

C'est ici que la tentation de sauter est la plus forte : **on peut vendre depuis trois ans sans avoir jamais fait ce que ce niveau demande.** D'où la phrase du profil N2 ou N3 à compétence L01 : « je suis déjà lancé, L02 ne me concerne plus. » Il se trompe deux fois — la structure de coût qu'il subit a été décidée par ces gestes-là, et il les refera à sa prochaine référence, à son prochain fournisseur, à son prochain marché, trois à dix fois par an.

**On peut être L07 sans entreprise. On peut être N3 avec une compétence L04.** Le second cas est le plus dangereux du métier : le chiffre d'affaires masque l'incompétence tant que le marché est porteur, et le jour où il ne l'est plus, personne ne sait lire ce qui se passe. Garde ton L au-dessus de ton N. Un opérateur L02 dans une entreprise N0 est en avance et le sait ; un L01 dans une entreprise N3 est en retard et ne le sait pas.

---

## 1. Les compétences du niveau

1. **Je reconstitue un COGS rendu entrepôt à partir d'un devis** : je liste les postes que le fournisseur n'a pas cotés — fret, douane, contrôle qualité, provision casse, amortissement d'outillage, emballage secondaire — et je chiffre chacun.
2. **Je calcule un coefficient sur le coût complet, jamais sur le prix sortie usine** — je dis de combien l'écart flatte un dossier importé — et je passe du coefficient au taux de coût marchandise en % du CA HT par la division `1,20 ÷ coefficient`, dans les deux sens.
3. **Je convertis un taux de retour en ligne de coût variable**, via le coût net d'un retour : CA perdu, plus traitement, moins marchandise récupérée revendable. Et **je place une commande dans sa tranche tarifaire logistique**, en disant à quelle distance de la suivante elle est — avant qu'un bundle ne l'y fasse basculer.
4. **Je construis une cascade jusqu'au MER seuil pour un produit qui n'existe pas encore**, depuis un devis, un poids et un taux de retour de catégorie.
5. **Je note une catégorie sur la grille à 9 critères** et j'applique ses deux verrous — aucun critère sous 2, critère 1 jamais sous 3 — même quand le total est bon.
6. **Je dérive un seuil de test** au lieu de le recopier — celui de la recherche vient du nombre de commandes visées, ceux du smoke test et de la pré-commande du nCAC cible — et **je décide entre deux tests qui se contredisent**, en sachant lequel mesure un consentement à payer et lequel une curiosité gratuite.

---

## 2. Ce que tu lis

| Ordre | Lecture | Ce que ça apporte **à ce niveau précisément** |
|---|---|---|
| 1 | [**E02 — Choisir le terrain**](../modules/E02-marche-et-produit.md), en entier | Le cœur du niveau. § 1 les cinq variables structurelles, dont la conversion taux de retour → ligne de coût (§ 1.3) et les tranches logistiques (§ 1.4) ; § 3 la grille à 9 critères et ses verrous ; § 4 les six tests et leurs seuils dérivés ; § 6 le COGS complet et l'arbitrage MOQ. |
| 2 | [**E03 — L'offre et le prix**](../modules/E03-offre-et-prix.md) | Ce que E02 ne traite pas : comment un panier se construit, ce que coûte une remise de lot en points de coefficient, et pourquoi le panier est le levier le plus rentable du modèle de référence — 71,7 % de l'EBITDA annuel pour 10 % d'amélioration. |
| 3 | [**C01 — Le produit à ×2,5**](../etudes-de-cas/C01-coefficient-insuffisant.md), **relu** | Lu à L01 pour l'arithmétique ; relis-le pour la décision : les quatre options de sortie, leur chiffrage comparé, et le fait qu'« arrêter » en soit une, chiffrée et respectable. |

Garde ouverts les [chiffres canoniques](../donnees/chiffres-canoniques.md) **§ 1** : les cinq références de NØRA, de ×6,4 à ×8,1, sont ton étalon. Un dossier se juge par comparaison à cette colonne, pas dans l'absolu.

---

## 3. Ce que tu fais

| Travail | Livrable attendu |
|---|---|
| **[Atelier S03 — Le produit et le coût réel](../atelier/S03-produit-et-cogs.md)** | Le cahier des charges rédigé contre les défauts des avis 1 et 2 étoiles, deux devis qualifiés, le COGS rendu entrepôt ligne à ligne, le coefficient, l'arbitrage MOQ en mois de stock et en euros immobilisés. |
| **[Atelier S04 — L'offre, le prix, le panier](../atelier/S04-offre-prix-et-panier.md)** | La gamme, la grille de prix, et le **tableau de construction d'AOV** : quelle proportion de clients prend quoi, quel panier en résulte. Avec, pour chaque remise de lot, le coefficient **du panier** — pas celui de l'unité. |
| **Simulateur `--comparer`, sur deux catégories opposées** | `--comparer --categorie mode_accessoire --graine 7`, puis la même chose sur `soin_cheveux`. **Livrable : deux pages d'analyse** — quelle stratégie survit dans chaque catégorie, à quel mois les trajectoires divergent, par quelle ligne de la cascade la mort arrive. À graine fixée le simulateur est déterministe : l'écart n'est imputable qu'à la catégorie. |
| **[E02 exercices 1 à 6](../modules/E02-marche-et-produit.md) et ceux de E03** | Réponses déroulées pour NØRA ; grille de lecture remplie pour ta catégorie ; pour l'exercice de décision, la réponse **et** la condition sous laquelle l'autre option serait la bonne. Ajoute le contrôle croisé : recalcule le COGS du sérum NØRA (E02 § 6.2) et sa variante asiatique jusqu'à retrouver ×8,1 et ×10,2. |

---

## 4. L'épreuve

> **Dossiers fictifs.** BAUME NUIT, LUMEN et GRANOLA TERRA sont inventés pour cette épreuve. Les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.

**Temps imparti : 3 h.** Calculatrice et tableur autorisés. Aucun document, aucune grille, aucune formule sous les yeux. **Sur 100.**

### 4.1 Hypothèses communes aux trois dossiers

Marché : France. TVA : 20 %. PSP : **1,70 %** du CA HT. Remises, codes promo et paniers abandonnés : **5,00 %** du CA HT. Au palier de lancement : frais fixes **6 500 € / mois**, objectif **800 commandes / mois**.

| Traitement d'un retour | A et C : transport 3,90 € + reconditionnement 1,10 € — B : transport 8,50 € + test et reconditionnement 4,00 € |
|---|---|
| **Marchandise non revendable après retour** | A : 10 % — B : 20 % — C : 100 % (alimentaire) |

**Grille logistique négociée** — transport + préparation et emballage par commande, selon le poids expédié :

| 0 – 1 kg | 1 – 2 kg | 2 – 5 kg | 5 – 10 kg |
|---:|---:|---:|---:|
| 6,60 € | 7,90 € | 9,80 € | 13,50 € |

### 4.2 Les trois devis, poste par poste

| Poste | **A — BAUME NUIT** baume corporel 200 ml, façonnier UE | **B — LUMEN** lampe de luminothérapie, Asie | **C — GRANOLA TERRA** granola bio 400 g, façonnier FR |
|---|---:|---:|---:|
| Matière, formule ou produit fini départ usine | 1,74 € | **27,50 €** FOB, produit complet | 1,08 € |
| Contenant primaire | 1,28 € (pot airless + capot) | — | 0,22 € (doypack + opercule) |
| Étui, notice, étiquetage | 0,53 € | — | 0,05 € |
| Façonnage, remplissage, ensachage | 0,55 € | — | 0,54 € |
| **Sous-total sortie usine** | **à calculer** | **27,50 €** | **à calculer** |
| Fret | 0,18 € routier intra-UE | 3,10 € maritime | 0,09 € routier |
| Droits de douane | 0,00 € (intra-UE) | **4,7 %** de (sortie usine + fret) | 0,00 € |
| Contrôle qualité, analyses, inspection | 0,12 € | 0,85 € | 0,06 € |
| Provision casse et non-conformité | **2 %** de (usine + fret + contrôle) | **3 %** de (usine + fret + douane) | **3 %** de (usine + fret + contrôle) |
| Amortissement outillage | moule 9 000 € ÷ 60 000 u | moules 18 000 € ÷ 25 000 u | 7 500 € ÷ 150 000 sachets |

> Le fournisseur de LUMEN écrit dans son offre : « avec un prix de vente à 149 €, vous êtes à un coefficient de **×5,4**. »

### 4.3 Les trois dossiers commerciaux

| Donnée | **A — BAUME NUIT** | **B — LUMEN** | **C — GRANOLA TERRA** |
|---|---|---|---|
| Prix de vente unitaire | 32,00 € TTC | 149,00 € TTC | 12,90 € TTC |
| Panier moyen attendu | 1,8 unité, **sans remise de lot** | 1 unité — non bundlable | lot de 3 sachets vendu **34,00 € TTC** |
| Poids expédié du panier moyen | 1,8 × 0,22 kg + 0,15 kg d'emballage | 1,9 kg, calage compris | 3 × 0,42 kg + 0,30 kg d'emballage |
| Fréquence de réachat naturelle | 3,5 mois | 30 mois | 5 semaines |
| Taux de retour de la catégorie | 3,0 % | 14,0 % | 2,0 % |
| Recherches mensuelles France | 41 000 | 22 000 | 55 000 |
| Annonceurs installés > 6 mois | 9, dont 3 à > 20 créatifs actifs | 6, dont 1 à > 20 créatifs | 12, dont 5 à > 20 créatifs |
| Différenciation | actif encapsulé, exclusivité de formule chez le façonnier, 24 mois | design du boîtier ; LED et driver de catalogue | recette et sourcing |
| Barrière réglementaire | dossier cosmétique UE 10 000 €/référence, personne responsable 1 800 €/an | marquage CE, basse tension, compatibilité électromagnétique | agrément sanitaire, traçabilité, DLUO |
| Démonstrabilité de l'effet | texture visible, avant/après photographiable à 14 jours | effet invisible en vidéo, allégations santé restreintes | le goût ne se filme pas |
| MOQ et délai | 6 000 unités — 8 semaines | 1 000 unités — 16 semaines | 12 000 sachets — 5 semaines |

### 4.4 Les questions

**Q1 — Les coûts de revient (15 points).** *(Éliminatoire.)* Calcule le COGS rendu entrepôt unitaire des trois produits, poste par poste, puis leur coefficient. Pour B, donne aussi celui du fournisseur et l'écart en pourcentage. Pour C, celui de l'unité **et** celui du panier.

**Q2 — Les cascades et les seuils (24 points).** *(Éliminatoire.)* Pour chaque dossier : la structure de coût variable en % du CA HT — COGS, logistique, PSP, retours, remises — puis le taux de marge brute et le MER seuil de contribution. La ligne « retours » doit être **dérivée** du taux de retour. Ajoute, pour le seul dossier retenu au Q4, le MER seuil de résultat nul au palier de lancement.

**Q3 — La grille de sélection (18 points).** Note les trois dossiers sur la grille à 9 critères de E02 § 3. Applique les deux verrous et dis, pour chacun, s'ils se déclenchent.

**Q4 — La décision (12 points).** Lequel lances-tu ? Justifie **par le calcul**, en dix lignes, et dis pour chacun des deux autres la variable unique qui l'a tué et si elle est modifiable.

**Q5 — Le protocole de validation de la demande (21 points).** *(Éliminatoire.)* Pour le dossier retenu, écris les six tests dans l'ordre, avec budget, durée, **seuil de décision et dérivation**. Les seuils de (a), (e) et (f) se calculent depuis l'objectif de 800 commandes par mois et le nCAC cible, ils ne se recopient pas. Termine par le budget total du protocole et sa part du capital qu'il protège.

**Q6 — La décision de test (10 points).** Tu as lancé le protocole sur le dossier retenu.

| Test | Résultat |
|---|---|
| (e) Smoke test | 1 000 € de média, 857 clics sur la page, **322 inscriptions** |
| (f) Pré-commande | 1 750 € de média, **28 pré-commandes** en 14 jours, panier moyen des pré-commandes **36,80 € TTC** |

(e) passe tes seuils, (f) les échoue. Que fais-tu ? Justifie, chiffre le coût de chaque option, et dis ce que tu ne fais surtout pas.

---

## 5. Le corrigé

### Q1 — Les coûts de revient (15 points)

| Poste | **A** | **B** | **C** |
|---|---:|---:|---:|
| Sortie usine | **4,10 €** | **27,50 €** | **1,89 €** |
| Fret | 0,18 € | 3,10 € | 0,09 € |
| Douane | 0,00 € | `4,7 % × 30,60` = **1,44 €** | 0,00 € |
| Contrôle et inspection | 0,12 € | 0,85 € | 0,06 € |
| Provision casse | `2 % × 4,40` = **0,09 €** | `3 % × 32,04` = **0,96 €** | `3 % × 2,04` = **0,06 €** |
| Outillage | `9 000 ÷ 60 000` = **0,15 €** | `18 000 ÷ 25 000` = **0,72 €** | `7 500 ÷ 150 000` = **0,05 €** |
| **COGS rendu entrepôt** | **4,64 €** | **34,57 €** | **2,15 €** |
| **Coefficient** | **×6,90** | **×4,31** | **×6,00** (unité) |

**Dossier B.** Le fournisseur annonce `149,00 ÷ 27,50 = ×5,42` ; écart `1 − 4,3101 ÷ 5,4182 = 20,5 %`. Il ne ment pas : il cote ce qu'il vend, départ usine. **Les 7,07 € qu'il ne cote pas — fret, douane, inspection, casse, outillage — valent un cinquième du coefficient**, et c'est l'acheteur qui les découvre. En intra-UE l'oubli est bénin ; sur un sourcing lointain il est décisif.

**Dossier C.** Deux coefficients, et le second est le seul qui compte :
```
Coefficient DU PANIER   = 34,00 ÷ (3 × 2,15 = 6,45)   = ×5,27
Remise de lot implicite = (3 × 12,90 − 34,00) ÷ 38,70 = 12,1 %
```
La remise de lot coûte **0,73 point de coefficient avant la première vente**. Qui n'annonce que ×6,00 n'a pas lu ce que le panier fait à la structure.

*Barème.* 4 points par COGS complet ; 1 point par coefficient (celui du panier de C compris) ; **−2** par poste oublié. **Éliminatoire** si un coefficient est calculé sur le prix sortie usine, ou si la douane, l'outillage ou la casse manquent.

### Q2 — Les cascades et les seuils (24 points)

Méthode, identique pour les trois : `ligne retours = taux de retour × coût net d'un retour ÷ AOV HT`, avec `coût net = AOV HT + traitement − marchandise récupérée revendable`.

```
A  récupéré 0,90 × 8,35 = 7,52 €   coût net 48,00 + 5,00 − 7,52  =  45,48 €
   ligne = 0,030 × 45,48 ÷ 48,00                                 =   2,84 %
B  récupéré 0,80 × 34,57 = 27,66 € coût net 124,17 + 12,50 − 27,66 = 109,01 €
   ligne = 0,140 × 109,01 ÷ 124,17                               =  12,29 %
C  récupéré 0 (alimentaire)        coût net 28,33 + 5,00         =  33,33 €
   ligne = 0,020 × 33,33 ÷ 28,33                                 =   2,35 %
```

| Ligne, en % du CA HT | **A** | **B** | **C** |
|---|---:|---:|---:|
| Panier moyen TTC → HT | 57,60 € → **48,00 €** | 149,00 € → **124,17 €** | 34,00 € → **28,33 €** |
| Poids expédié → tranche | 0,546 kg → 6,60 € | 1,9 kg → 7,90 € | 1,56 kg → 7,90 € |
| COGS (contrôle B : `1,20 ÷ 4,3101` ✓) | 17,40 % | 27,84 % | 22,76 % |
| Logistique | 13,75 % | 6,36 % | **27,88 %** |
| PSP | 1,70 % | 1,70 % | 1,70 % |
| Retours (dérivée ci-dessus) | 2,84 % | **12,29 %** | 2,35 % |
| Remises | 5,00 % | 5,00 % | 5,00 % |
| **Total coûts variables** | **40,69 %** | **53,19 %** | **59,69 %** |
| **MARGE BRUTE (CM2)** | **59,31 %** | **46,81 %** | **40,31 %** |
| **MER seuil (CM3 = 0)** | **2,02** | **2,56** | **2,98** |

**Seuil de résultat nul du dossier A, au palier de lancement**
```
CA TTC visé = 800 × 57,60 = 46 080 €   →   CA HT = 38 400 €
Frais fixes en % du CA HT = 6 500 ÷ 38 400              = 16,93 %
MER seuil (EBITDA = 0) = 1,20 ÷ (0,5931 − 0,1693)       =   2,83
```

**Lecture d'ensemble.** **A à 2,02** est au niveau du modèle de référence (1,95 à 2,10 selon le palier) : jouable en acquisition payante froide. **B à 2,56** devrait être tenu **en prospection quasi pure** — à 30 mois de fréquence, un client livre à peine plus d'une commande sur 12 mois (*hypothèse : n ≈ 1,05*), donc aucun réachat ne soutient le MER, quand le meilleur MER du modèle de référence vaut 2,90. **C à 2,98** est hors de portée, et l'origine n'est pas le coefficient : c'est la logistique à 27,88 %, parce qu'un panier de 34,00 € porte 7,90 € de transport.

*Barème.* 6 points par cascade (1 par ligne, 1 le total et la marge brute) ; 1,5 par MER seuil de contribution ; 1,5 le seuil de résultat. **Éliminatoire** si le taux de retour est reporté tel quel comme ligne de coût — 3,0 %, 14,0 %, 2,0 % — au lieu d'être converti : c'est l'erreur qui fait passer B pour viable et C pour excellent.

### Q3 — La grille de sélection (18 points)

| # | Critère (ancrages : 0 / 3 / 5) | **A** | **B** | **C** |
|---:|---|---:|---:|---:|
| 1 | Coefficient rendu entrepôt `<×3 / ×5-6 / >×7,5` | **4** ×6,90 | **2** ×4,31 | **3** ×5,27 au panier |
| 2 | Fréquence de réachat `>12 mois / 4-6 mois / <8 sem.` | **4** 3,5 mois | **0** 30 mois | **5** 5 semaines |
| 3 | Taux de retour `>25 % / 8-12 % / <4 %` | **5** 3,0 % | **2** 14,0 % | **5** 2,0 % |
| 4 | Densité de valeur `<12 / 25-45 / >70 €/kg` | **5** 105 €/kg | **5** 78 €/kg | **2** 22 €/kg |
| 5 | AOV atteignable et bundlable `<25 / 40-55 / >70 €` | **4** 57,60 € | **5** 149 €, non bundlable | **2** 34,00 € |
| 6 | Mécanisme différenciant | **4** exclusivité de formule | **1** design, LED catalogue | **1** recette |
| 7 | Demande exprimée | **5** 41 000, 9 annonceurs | **4** 22 000, 6 annonceurs | **5** 55 000, 12 annonceurs |
| 8 | Barrière d'entrée | **4** dossier UE 10 000 € | **3** CE, basse tension | **3** agrément sanitaire |
| 9 | Charge de preuve créative | **4** avant/après à 14 j | **2** effet invisible | **2** le goût ne se filme pas |
| | **TOTAL / 45** | **39** | **24** | **28** |

Densités : A `57,60 ÷ 0,546 = 105 €/kg` ; B `149,00 ÷ 1,9 = 78 €/kg` ; C `34,00 ÷ 1,56 = 22 €/kg`.

| Verrou | **A** | **B** | **C** |
|---|---|---|---|
| Total ≥ 32 | 39 ✓ | 24 ✗ | 28 ✗ |
| Aucun critère < 2 | min. 4 ✓ | critères 2 = 0 et 6 = 1 ✗ | critère 6 = 1 ✗ |
| Critère 1 ≥ 3 | 4 ✓ | 2 ✗ | 3 ✓ |
| **Verdict** | **Recevable** | **Refus — trois verrous** | **Refus — deux motifs** |

*Barème.* 6 points par dossier : 4 la notation, 2 les verrous. **Tolérance de ±1 par critère** si la justification est écrite, le total restant à ±3 du corrigé. Un total juste sans verrou appliqué plafonne à 3 sur 6 : la grille sert à empêcher qu'un bon total masque une porte fermée.

### Q4 — La décision (12 points)

**On lance A — BAUME NUIT.** Seul des trois à passer les trois filtres : marge brute de 59,31 % contre 46,81 % et 40,31 % ; MER seuil de 2,02, dans la plage du modèle de référence ; 39 sur 45 sans verrou. Le seuil de résultat de 2,83 reste exigeant, mais il s'effondrera avec le volume — il est porté par des frais fixes qui passeront de 16,93 % à moins de 11 % du CA HT.

**B est tué par son coefficient réel — ×4,31 et non ×5,42 — combiné à 30 mois de fréquence de réachat.** Modifiable ? Le coefficient, marginalement : un FOB renégocié de 27,50 € à 22,00 € porterait le COGS à 28,64 €, le coefficient à ×5,20, la marge brute à 51,05 % et le seuil à 2,35 — encore trop haut sans réachat. La fréquence, elle, **n'est pas modifiable** : un objet qu'on achète une fois tous les trente mois se vend en récolte de demande, jamais en création de demande.

**C est tué par sa densité de valeur — 22 €/kg — qui produit une logistique à 27,88 %.** Modifiable, et c'est ce qui rend le dossier intéressant : un lot de 5 à 55,00 € TTC porte le poids à `5 × 0,42 + 0,30 = 2,40 kg`, donc en tranche 2 – 5 kg à 9,80 €, pour un AOV HT de 45,83 € — la logistique tomberait à 21,38 %. Mieux, pas suffisant : la sortie réelle passe par l'abonnement, qui amortit le transport sur une fréquence, et par un prix unitaire plus élevé. **Le granola n'est pas un mauvais produit, c'est un mauvais produit expédié à l'unité.**

*Barème.* 4 points le choix de A appuyé sur deux des trois filtres chiffrés ; 4 la variable tueuse de B et son caractère non modifiable ; 4 celle de C et sa correction chiffrée. Choisir B ou C plafonne le Q4 à 0 ; choisir A sans calcul, à 4.

### Q5 — Le protocole de validation de la demande (21 points)

**La règle qui commande tout :** chaque seuil est écrit, daté et signé **avant** le lancement du test. Un seuil écrit après coup n'est pas un seuil, c'est une justification.

```
LES TROIS DÉRIVATIONS

nCAC cible — AOV 1ʳᵉ commande visé 1,6 unité = 51,20 € TTC → 42,67 € HT
   contribution = 42,67 × 59,31 % = 25,31 € ; perte acceptée 5,00 €
   nCAC cible = 25,31 + 5,00 = 30,31                          →  30,00 €

(a) 15 % des 800 commandes = 120 ; conversion 2,5 % → 4 800 visites ;
    demande captée 20 % → 24 000        seuil retenu : ≥ 20 000 rech./mois

(e) Hypothèse : 12 % d'une liste d'attente chaude achète sous 60 jours,
    donc une inscription vaut 0,12 client → 30,00 × 0,12       =  3,60 €
    CPM 14,00 €, clic sortant 1,20 % → CPC 1,17 € → 857 clics ;
    1 000 ÷ 3,60 = 278 inscriptions = 32,4 %      → seuil posé à 25 %

(f) Coût maximal = 30,00 × 1,5                                 = 45,00 €
    (1,5 = provision déclarée : ni pixel, ni preuve sociale, ni
     retargeting au lancement)
    Volume : à 40 conversions, erreur-type relative 1 ÷ √40     = 15,8 %
    → sous 40, on ne lit pas un signal, on lit du bruit
```
*La perte de 5,00 € est une hypothèse assumée, du même ordre que celle du modèle de référence (−4,93 € à −7,26 €), et finançable seulement si le réachat la rembourse — ce qu'aucun de ces six tests ne mesure.*

| # | Test | Budget | Durée | Seuil de décision, écrit et daté d'avance |
|---|---|---:|---|---|
| **(a)** | Recherche et tendance | 0 – 99 € | 1 j | **≥ 20 000 recherches/mois** sur le champ du problème, tendance à 24 mois ne décroissant pas de plus de 15 %. Observé : 41 000 → favorable |
| **(b)** | Concurrents payants | 0 € | 2 j | **≥ 5 annonceurs distincts** diffusant depuis ≥ 6 mois, dont **≥ 2 à ≥ 20 créatifs actifs** — un annonceur qui tient dix-huit mois prouve, par son comportement, que la catégorie supporte un MER au-dessus de son seuil |
| **(c)** | Marketplaces et avis 1 – 2 étoiles | 200 – 400 € | 1 sem. | **≥ 3 produits à ≥ 500 avis**, et **les 3 défauts dominants couvrant ≥ 45 %** des 200 critiques lues — sous 30 %, aucune modification produit ne capte l'insatisfaction |
| **(d)** | Communautés et vocabulaire | 0 € | 1 sem. | **≥ 3 communautés actives** et **≥ 30 verbatims**, dont **≥ 10 revenant ≥ 5 fois** — le stock d'angles dont sortiront les concepts |
| **(e)** | Smoke test | 1 000 € | 5 – 7 j | **≤ 3,60 € par inscription** ET **≥ 25 % d'inscriptions** sur les visiteurs de la page |
| **(f)** | Pré-commande réelle | 2 200 € | 10 – 14 j | **≤ 45,00 € par pré-commande**, **≥ 40 en 14 jours**, ET **panier ≥ 51,20 € TTC** — contrôle croisé de l'hypothèse d'AOV |

```
Budget total du protocole                              ≈  3 500 €
Capital engagé si l'on lance sans lui :
   MOQ 6 000 × 4,64 = 27 840 €  +  outillage 9 000 €
   +  dossier réglementaire 10 000 €                   = 46 840 €
Part du protocole = 3 500 ÷ 46 840                     =    7,5 %
Stock immobilisé par le MOQ = 6 000 ÷ (800 × 1,8)      =    4,2 mois
```
Sauter ces cinq semaines n'économise pas 3 500 € : c'est refuser de payer 7,5 % pour savoir si les 92,5 % restants ont une chance.

*Barème.* 2 points par test ordonné avec budget, durée et seuil (12) ; 3 points par dérivation chiffrée pour (a), (e) et (f) (9). **Éliminatoire** si un seuil est recopié sans dérivation, ou écrit après les résultats.

### Q6 — La décision de test (10 points)

```
(e) Taux d'inscription = 322 ÷ 857     = 37,6 %   ≥ 25 %    ✓
    Coût par inscription = 1 000 ÷ 322 =  3,11 €  ≤ 3,60 €  ✓        → PASSE
(f) Coût par pré-commande = 1 750 ÷ 28 = 62,50 €  > 45,00 € ✗
    Volume                             =     28   < 40      ✗
    Panier moyen                       = 36,80 €  < 51,20 € ✗        → ÉCHOUE
```

**1. La pré-commande prime, sans discussion.** Une inscription est gratuite pour qui la donne : elle mesure une curiosité. Une pré-commande débite une carte : elle mesure un consentement à payer. Quand les deux se contredisent, l'écart **est** l'information — entre 37,6 % de curiosité et 28 achats, il y a la distance exacte entre l'intérêt et la valeur perçue.

**2. Mais lis le panier avant d'arrêter.** 36,80 € contre 51,20 € attendus, soit `36,80 ÷ 32,00 = 1,15` unité par commande : **presque personne n'a pris le duo.** Le signal ne désigne pas la catégorie — la demande est là : 41 000 recherches, 9 annonceurs, 37,6 % d'inscriptions. Il désigne **l'offre et le prix**, et toute la construction du protocole reposait sur 1,6 unité à la première commande.

**3. Un seul re-test, sur l'offre, jamais sur la catégorie.** Même catégorie, même angle, échelle de prix modifiée — prix unitaire, construction du lot, seuil de franco — seuils réécrits et **datés avant**, **arrêt définitif si le volume reste sous 40**. Un seul : au deuxième, tu ne testes plus, tu cherches un résultat.
```
Re-test                                           = 2 200 €  → 4,7 % du capital protégé
Total engagé si le re-test échoue et qu'on arrête = 5 700 €, contre 46 840 €
   engagés avant la première vente si l'on lance sans re-tester
Échec en cours : 1 030,40 € de remboursements + 22,97 € de PSP non restitués
   + 1 750 € de média déjà dépensé                          ≈  1 773 €
```
Les 1 773 € ne sont pas le sujet : vingt-huit personnes ont donné leur argent pour un produit qui n'existera peut-être pas. La contre-mesure n'est pas de renoncer au test, c'est de l'avoir rendu honnête d'avance — date d'expédition annoncée, condition de réalisation sur la page de paiement, remboursement automatique.

**4. Ce que tu ne fais surtout pas.** Relancer le même test avec plus de budget : le coût par pré-commande ne baisse pas quand le budget monte, il monte — c'est la définition du CAC marginal. Décider que « 28, c'est presque 40 » : 28 conversions donnent `1 ÷ √28 = 18,9 %` d'erreur relative, et « presque » est le mot par lequel un seuil cesse d'exister. Et surtout pas engager le MOQ « puisque la demande est prouvée » : 27 840 € de stock sur un produit dont personne n'a voulu le duo.

*Barème.* 3 points la primauté de la pré-commande justifiée par la nature des deux tests ; 3 la lecture du panier et l'imputation à l'offre ; 2 le re-test unique borné et chiffré ; 2 au moins deux des pièges. Répondre « on lance quand même » plafonne le Q6 à 0.

---

## 6. Le critère de passage

| | |
|---|---|
| **Note minimale** | **72 / 100** |
| **Questions éliminatoires** | **Q1** — un coefficient calculé sur le prix sortie usine, ou l'oubli de la douane, de l'outillage, de la casse. **Q2** — un taux de retour reporté tel quel comme ligne de coût. **Q5** — un seuil recopié au lieu d'être dérivé, ou écrit après les résultats. |
| **Temps** | 3 h. Au-delà de 3 h 30, épreuve échouée. |

Soixante-douze est le seuil le plus bas des trois premiers niveaux, et c'est délibéré : l'épreuve comporte des jugements — la note du critère 6, la correction de C — où deux copies compétentes divergent d'un point. On ne pénalise pas le désaccord argumenté, on pénalise l'absence de calcul. Les trois éliminatoires, elles, portent sur des automatismes dont l'absence produit toujours la mauvaise décision : un coefficient surestimé de 20 %, une catégorie à retours qui passe pour saine, un seuil qui s'adapte au résultat.

**En cas d'échec :** refais le COGS du sérum NØRA et sa variante asiatique jusqu'à retomber sur ×8,1 et ×10,2, la conversion taux de retour → ligne de coût sur trois catégories opposées, puis repasse une **variante** : trois autres dossiers, mêmes mécanismes.

---

## 7. Les pièges de ce niveau

**1. « Mon produit est à ×8. »** Sur quel dénominateur ? Le prix sortie usine flatte de 12 % en Europe et de 20 à 25 % en Asie. Un coefficient sans la mention « rendu entrepôt » est un chiffre de vendeur — et le vendeur, ici, c'est ton fournisseur. Corollaire : un MOQ est un problème de trésorerie déguisé en problème d'achat, et le sourcing lointain, qui économise 0,98 € par unité sur le sérum NØRA, se décide à P3, pas à P1.

**2. Croire que le coefficient est le verdict.** Il est le premier verrou, pas le seul : le t-shirt en coton biologique de E02 § 3.3 passe le mur du coefficient à ×5,0 et meurt sur ses retours, MER seuil 4,20. À l'épreuve, LUMEN est refusé par la variable la plus visible, GRANOLA TERRA par la moins regardée. **Un débutant élimine la lampe tout seul ; il lance le granola.**

**3. Croire qu'un panier élevé compense une mauvaise marge brute, ou qu'une remise de lot est gratuite.** Le MER seuil vaut `1,20 ÷ m` : le panier n'apparaît pas dans la formule, et LUMEN a le meilleur AOV des trois pour le deuxième plus mauvais seuil. La remise de lot, elle, fait monter l'AOV et descendre le coefficient — sur GRANOLA TERRA, ×6,00 devient ×5,27, soit 0,73 point consommé avant que le premier client n'existe. Un panier se juge toujours avec le coefficient **du panier**.

**4. Croire qu'une catégorie sans concurrence payante est une opportunité.** C'est la reformulation optimiste de « personne n'a trouvé comment gagner de l'argent ici ». Trois explications à une absence d'annonceurs, toutes mauvaises : la marge brute ne finance pas de trafic payant, l'achat exige une délibération que la publicité ne déclenche pas, ou la catégorie est interdite de publicité. La question utile n'est pas « pourquoi personne n'y est » mais **« quelle contrainte a arrêté les autres, et que sais-je qu'ils ne savaient pas ? »**

**5. Croire qu'un smoke test prouve la demande, et écrire le seuil après le test.** Le premier mesure une curiosité gratuite : 37,6 % d'inscriptions et vingt-huit pré-commandes coexistent parfaitement. Le second ne se voit jamais dans un document — le seuil est là, chiffré, il a l'air rigoureux. La seule protection est la date : **un seuil non daté n'est pas un seuil.**

> **À retenir :** à L02, tu ne cherches plus à savoir si un produit est bon, mais **quelle variable le tuera** et si elle est modifiable. Un dossier qui ne dit pas où sera la douleur n'a pas été analysé, il a été apprécié.

---

*Fin du niveau L02. Suite : [L03 — Opérateur](L03-opérateur.md), où tu quittes la structure pour le message : un corpus client brut à transformer en angle, en script et en page.*
