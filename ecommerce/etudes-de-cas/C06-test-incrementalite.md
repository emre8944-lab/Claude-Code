# Cas C06 — Le test qui a supprimé 22 % du budget sans perdre de chiffre d'affaires

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des
> ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.
> **Ce que tu dois en tirer :** un ROAS élevé mesure la facilité à s'attribuer une
> vente, pas la capacité à la créer.
> **Modules rattachés :** E01, E06, E09, E13.

---

## 0. Conventions et origine des chiffres

**La dépense publicitaire est HT, le chiffre d'affaires client est TTC**, à 20 % de TVA
([chiffres canoniques](../donnees/chiffres-canoniques.md)). Le **ROAS affiché** vaut ici
*CA TTC attribué par la plateforme ÷ dépense HT du canal* — convention par défaut d'une
boutique européenne ; change de convention et tous les ROAS bougent de 20 %. Le budget
média est **dérivé** du § 2.2 (CA TTC 2 931 600 €) et du § 2.3 (MER 2,80).

```
Dépense pub P4 = 2 931 600 € TTC ÷ 2,80 = 1 047 000 € HT / mois
Contrôle : 1 047 000 ÷ 2 443 000 € HT = 42,86 % ≈ 42,9 % (§ 2.2)
Par semaine 1 047 000 × 12 ÷ 52 = 241 615 € HT ; par jour × 12 ÷ 365 = 34 422 € HT
Contribution par commande = 69,80 ÷ 1,20 × 60,4 % (CM2, § 2.1) = 35,13 € HT
Panier de 1ʳᵉ commande P4 = 31,71 € (§ 2.4) ÷ 60,4 % × 1,20 = 63,00 € TTC
```

*Hypothèses locales :* ventilation du budget par canal (§ 1) ; la France pèse **46 % des
commandes** ; dépense de chaque canal répartie au prorata.

---

## 1. La situation

Mois 24. NØRA est en P4 : cinq marchés (FR, BE, DE, ES, IT), 42 000 commandes/mois,
2 931 600 € TTC, 198 572 € d'EBITDA (8,1 % du CA HT), 25 ETP, un plan média de
**1 047 000 € HT/mois**. Voici ce qu'affiche le tableau de bord.

| Canal | Part | Budget/mois HT | ROAS affiché | CA TTC attribué | Part du CA réel revendiquée |
| --- | ---: | ---: | ---: | ---: | ---: |
| Meta prospection (ASC + large) | 42 % | 439 740 € | 1,95 | 857 493 € | 29,3 % |
| TikTok prospection | 13 % | 136 110 € | 1,55 | 210 971 € | 7,2 % |
| **Meta retargeting** | **11 %** | **115 170 €** | **7,00** | **806 190 €** | **27,5 %** |
| **Google Search — marque** | **15 %** | **157 050 €** | **11,00** | **1 727 550 €** | **58,9 %** |
| Google Search générique + Shopping | 6 % | 62 820 € | 3,10 | 194 742 € | 6,6 % |
| PMax / Demand Gen / YouTube | 6 % | 62 820 € | 2,05 | 128 781 € | 4,4 % |
| Influence + affiliation | 5 % | 52 350 € | 2,40 | 125 640 € | 4,3 % |
| Pinterest, Snap, native | 2 % | 20 940 € | 1,30 | 27 222 € | 0,9 % |
| **Total** | **100 %** | **1 047 000 €** | **3,90** | **4 078 589 €** | **139,1 %** |

Le CAC attribué d'un canal vaut `69,80 € ÷ ROAS`. Le ROAS de la dernière ligne,
`4 078 589 ÷ 1 047 000 = 3,90`, sort d'un **MER réel de 2,80**.

**Le signal d'alerte n'est pas dans les bons chiffres, il est dans leur somme.** Les
canaux revendiquent **139,1 %** du CA réel, soit `4 078 589 − 2 931 600 = 1 146 989 € TTC
par mois` de ventes fantômes. Ce n'est pas de la fraude : chaque plateforme voit un
contact et une vente et relie les deux, sans savoir que trois autres ont vu la même. **La recherche sur le nom de la marque et le
retargeting pèsent 26 % du budget (272 220 €) et revendiquent 86,4 % du chiffre
d'affaires total de l'entreprise** — 2 533 740 € sur 2 931 600 €. Deux lignes qui ne
parlent qu'à des gens ayant déjà tapé le nom de la marque ou déjà visité le site
prétendent produire presque tout ce que l'entreprise vend. C'est arithmétiquement
impossible, et c'est le vrai signal.

Un ROAS de 11 sur son propre nom ne dit pas « ce canal est excellent ». Il dit : **ce
canal se place à l'endroit du parcours où la vente est déjà décidée.** Le clic sur son
propre nom est bon marché — personne d'autre n'enchérit dessus sérieusement — et il
convertit énormément, l'intention étant maximale : le ROAS est élevé **par construction
du placement**, pas par mérite. Même mécanique pour le retargeting, qui parle à des gens
ayant mis un produit au panier il y a trois jours.

> **À retenir :** plus un canal intervient tard dans le parcours, plus son ROAS affiché
> est élevé et plus son incrémentalité est faible. La corrélation entre les deux est
> négative. Un canal qui affiche 11 est **suspect**, pas performant.

Le dirigeant lisait le tableau à l'envers : « la marque et le retargeting tiennent le
compte, c'est la prospection qui coûte cher. » Il voulait **y déplacer du budget**.

---

## 2. Le diagnostic

1. **Personne ne sait ce que ces deux canaux produisent.** Le ROAS mesure une
   corrélation temporelle, pas une causalité : aucun chiffre du § 1 ne répond à
   « combien de ventes en moins si je coupe ? ».
2. **La direction du biais est connue d'avance.** La sur-attribution s'accumule sur le
   dernier point de contact — presque toujours la recherche marque.
3. **L'enjeu est chiffré avant de tester.** À 100 % d'incrémentalité, rien à faire ; à
   20 %, ce sont 272 220 €/mois — **3 266 640 € HT par an** — mal employés, pour un
   EBITDA annuel de 2 382 864 €. La question vaut plus que l'entreprise ne gagne.
4. **Le seul instrument non contaminé est l'expérience géographique.** Ni l'attribution,
   ni le « lift study » vendu par la plateforme, juge et partie. On coupe dans une zone,
   on garde dans une autre, on compare les ventes **totales** — Hopkins, 1923, ch. 16.

---

## 3. Les options

Évaluées au troisième mois après bascule, frais fixes constants. Calculs aux § 4 et § 5.

| Option | Budget pub/mois HT | Commandes/mois | CA TTC/mois | MER | **EBITDA/mois** | % CA HT | Δ EBITDA/an |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **A — statu quo** | 1 047 000 € | 42 000 | 2 931 600 € | 2,80 | **198 572 €** | 8,1 % | — |
| **B — couper 22 %, encaisser** | 816 660 € | 36 484 | 2 546 583 € | 3,12 | **235 120 €** | 11,1 % | +438 576 € |
| **C — couper 22 %, réallouer** | 1 047 000 € | 43 499 | 3 036 230 € | 2,90 | **251 236 €** | 9,9 % | **+631 968 €** |
| **D — couper 26 %, réallouer** | 1 047 000 € | 40 044 | 2 795 071 € | 2,67 | **129 852 €** | 5,6 % | −824 640 € |

**B est le piège de la marge en pourcentage** : meilleur taux du tableau, 13,1 % de CA
en moins. Reculer de 385 017 € de CA mensuel pour 36 548 € d'EBITDA est un mauvais
échange : le taux monte parce que le dénominateur descend.

**D coupe les deux canaux à zéro** et détruit 824 640 € d'EBITDA par an : le premier
euro de recherche marque est bien plus incrémental que le dernier — il défend le nom —
et la tranche réallouée devient trop grosse pour le CAC marginal de la prospection
(*hypothèse : 47,50 € au lieu de 44,00 €*).

**On retient C** — non parce qu'elle gagne dans un tableau, mais parce que le § 4 a
mesuré les deux nombres, 20,4 % et 35,8 %, sans lesquels ce tableau serait une opinion.

---

## 4. La décision et l'exécution

### 4.1 Le terrain : trois cellules, pas deux

Couper les deux canaux dans la même zone aurait produit **une** mesure pour **deux**
inconnues. D'où trois cellules de 21 départements en France métropolitaine : **A**
(recherche marque coupée à 100 %), **B** (retargeting coupé à 100 %), **C** (témoin,
rien n'est touché). Exclus : l'Île-de-France (18 % du volume France, sans zone
comparable), les départements frontaliers (débordement d'audience) et ceux sous
200 commandes/mois.

`42 000 × 46 % = 19 320 cmd/mois` en France, moins 18 % d'Île-de-France = 15 842, en
trois cellules : `15 842 ÷ 3 × 12 ÷ 365 =` **173,6 commandes/jour par cellule**.

### 4.2 La période de référence et l'appariement

Huit semaines (S−8 à S−1) servent à apparier les cellules, figer leur rapport de base et
mesurer la sur-dispersion.

| Critère (moyenne quotidienne, 8 semaines) | Cellule A | Cellule B | Cellule C (témoin) |
| --- | ---: | ---: | ---: |
| Commandes / jour | 172,4 | 175,1 | 173,4 |
| CA TTC / jour (AOV 69,80 € dans les trois) | 12 034 € | 12 222 € | 12 103 € |
| Part du CA en réachat / du trafic direct + SEO | 41,2 % / 27,8 % | 41,6 % / 28,1 % | 41,4 % / 27,9 % |
| Taux de retour / délai de livraison | 3,4 % / 2,4 j | 3,6 % / 2,3 j | 3,5 % / 2,4 j |
| Corrélation de la série quotidienne avec C | 0,94 | 0,93 | — |
| **Rapport de base à C (commandes)** | **0,9942** | **1,0098** | **1,0000** |

Le rapport de base est le seul chiffre qui compte : on ne compare jamais A à C
directement, on compare **l'évolution de A/C**. C'est la stabilité qui fait le témoin,
pas l'égalité.


### 4.3 La puissance statistique — la partie que tout le monde saute

Objectif : détecter une baisse de **10 %** des commandes. Modèle de comptage :

```
Var(ln(N_test / N_témoin)) ≈ 1/N_test + 1/N_témoin ; effet |ln 0,90| = 0,10536
```

Deux comparaisons (A contre C, B contre C) : Bonferroni, donc α bilatéral de 2,5 % par
test → z = 2,2414 ; puissance 90 % → z = 1,2816. Somme 3,5230, carré 12,4115.

```
n (Poisson) = 2 × 12,4115 ÷ 0,10536² = 24,823 ÷ 0,011101 = 2 236 par cellule
```

**C'est là que 90 % des tests géographiques mentent.** Les commandes quotidiennes ne
suivent pas une loi de Poisson : paie, météo, week-ends, envois CRM, tout corrèle. On
mesure la sur-dispersion sur les 8 semaines de référence :

```
Écart-type observé du log-ratio quotidien A/C         = 0,1863
Écart-type attendu sous Poisson √(1/172,4 + 1/173,4)  = 0,1076
Sur-dispersion (design effect) = (0,1863 ÷ 0,1076)² = 3,00
n réel = 2 236 × 3,00 = 6 708 par cellule → 6 708 ÷ 173,6 = 38,6 j → 42 jours
```

**Six semaines. Pourquoi 10 jours n'auraient rien prouvé.** À 10 jours, chaque cellule
n'accumule que 1 736 commandes et l'effet minimum détectable devient :

```
MDE = 1 − exp( −3,5230 × √(3 × 2 ÷ 1 736) ) = 1 − exp(−0,2071) = 18,7 %
```

Un test de 10 jours qui conclut « pas d'effet » est donc **compatible avec une perte
réelle de 18,7 % des commandes** — `42 000 × 18,7 % × 69,80 € = 548 172 € TTC par mois`,
6,58 M€ par an que le test ne voit pas. Tu n'aurais pas prouvé que le canal
n'est pas incrémental, mais que tu manques de données : ce n'est pas la même phrase, et
elle coûte beaucoup plus cher. À 42 jours, 7 291 commandes par cellule, le MDE tombe à
**9,6 %** — le test peut enfin exclure une perte de 10 %.

### 4.4 Ce qu'on coupe et ce qu'on ne touche pas

**Coupé, de J à J+41 :** en A, toutes les campagnes sur le nom de la marque et ses
variantes — exact, expression, large — budget à zéro sur les 21 départements. En B,
exclusion de ces départements de toutes les audiences de retargeting (visiteurs 30 j,
panier 14 j, vues vidéo 75 %, fichier client 180 j). **Non touché, et c'est aussi
important :** prospection, enchères, créations, prix, promotions, CRM, SMS, SEO, presse,
influence, et aucun lancement produit.

**La précaution qui sauve le test :** les campagnes de prospection sont dupliquées en
trois jeux géographiques à budget figé. Sinon l'algorithme déplace sa diffusion vers la
cellule où l'enchère se libère, et le témoin est contaminé par la mesure.

**Calendrier.** S−8 à S−1 référence · S1 à S6 test · S7–S8 observation des conversions
décalées, sans réactivation, avant lecture finale.

### 4.5 Le coût du test

Sur 42 jours : dépense évitée `27 075 + 20 166 = 47 241 € HT` ; commandes perdues
`868,6 + 723,8 = 1 592,4`, soit `× 35,13 = 55 941 €` de contribution. **Coût net :
8 700 €** pour une question qui pèse 3 266 640 € HT par an. Un test se juge à son coût
net, pas au budget qu'il met en jeu.

---

## 5. Les résultats

### 5.1 Zone test contre zone témoin, avant et pendant

| Mesure (moyenne quotidienne) | A — marque coupée | B — retargeting coupé | C — témoin |
| --- | ---: | ---: | ---: |
| Commandes, référence (56 j) / test (42 j) | 172,4 → 155,2 | 175,1 → 161,4 | 173,4 → **176,9** |
| Variation brute | −10,0 % | −7,8 % | **+2,0 %** |
| CA TTC/j, référence → test | 12 034 → 10 833 € | 12 222 → 11 266 € | 12 103 → 12 348 € |
| **Contrefactuel (C × rapport de base)** | **175,88** | **178,63** | — |
| **Lift = (test/réf.) ÷ (C test / C réf.) − 1** | **−11,76 %** | **−9,65 %** | — |
| Écart-type du log-ratio / z | 0,0294 / **4,26** | 0,0291 / **3,49** | — |
| Décision (seuil Bonferroni z > 2,2414) | significatif | significatif | — |

Lis la variation brute du témoin : **+2,0 %**. Sans lui, A se lisait « −10,0 % » au lieu
de −11,76 % et B « −7,8 % » au lieu de −9,65 % — le témoin valait 1,8 point de mesure.

### 5.2 Incrémentalité et CAC réel

Commandes revendiquées par les canaux coupés dans leur cellule sur 42 jours : 4 267 en A
(101,59/jour), 2 022 en B (48,15/jour).

```
Marque      : perdues = (175,88 − 155,2) × 42 = 869 → 869 ÷ 4 267 = 20,4 %
Retargeting : perdues = (178,63 − 161,4) × 42 = 724 → 724 ÷ 2 022 = 35,8 %
```

| Canal | CAC attribué | Incrémentalité | **CAC incrémental** | ROAS affiché | **ROAS incrémental** |
| --- | ---: | ---: | ---: | ---: | ---: |
| Google Search — marque | 6,35 € | **20,4 %** | **31,17 €** (×4,9) | 11,00 | **2,24** |
| Meta retargeting | 9,97 € | **35,8 %** | **27,86 €** (×2,8) | 7,00 | **2,51** |
| *Rappel : MER seuil EBITDA P4 (§ 2.3)* | | | | | *2,35* |

Contrôle au niveau du groupe : `157 050 ÷ (24 750 × 20,4 %) = 31,17 €` et
`115 170 ÷ (11 550 × 35,8 %) = 27,86 €`.

La recherche marque coûte réellement 31,17 € par commande, pas 6,35 € : cinq fois plus
cher qu'affiché, et son ROAS incrémental de 2,24 passe **sous le MER seuil EBITDA de
2,35**. Le retargeting, à 2,51, franchit le seuil de justesse ; son intervalle de
confiance à 95 %, **[12,9 % ; 55,8 %]**, interdit de le supprimer.

L'arbitrage se fait dans une seule unité : la contribution obtenue par euro dépensé.

| Emploi du prochain euro | Sans queue de LTV | En créditant la queue de LTV |
| --- | ---: | ---: |
| Recherche marque (marginal) | 35,13 ÷ 31,17 = **1,13** | 44,45 ÷ 31,17 = **1,43** |
| Retargeting (marginal) | 35,13 ÷ 27,86 = **1,26** | 44,45 ÷ 27,86 = **1,60** |
| **Prospection, contribution 12 mois (§ 3.1)** | — | 83,51 ÷ 44,00 = **1,90** |

La colonne de droite est l'objection honnête : 18 % des commandes incrémentales de
récolte viennent de nouveaux clients, dont la queue de LTV vaut
`83,51 − 31,71 = 51,80 €` — créditée, `35,13 + 0,18 × 51,80 = 44,45 €`. **La prospection
gagne quand même.**

### 5.3 Avant / après, sur 90 jours

Recherche marque `157 050 € → 20 940 €`, retargeting `115 170 € → 20 940 €` : `230 340 €`
libérés, **22,0 % du budget**, réalloués en prospection Meta et TikTok
(`575 850 € → 806 190 €`, +40,0 %). CAC marginal mesuré sur la tranche ajoutée :
**44,00 €** → 5 235 nouveaux clients/mois.

| Mois | Commandes gagnées | Commandes perdues | **Net** | Δ CA TTC | **Δ EBITDA** |
| --- | ---: | ---: | ---: | ---: | ---: |
| M+1 | 5 549 | 5 252 | **+297** | +20 731 € | **+10 434 €** |
| M+2 | 6 282 | 5 384 | **+898** | +62 680 € | **+31 547 €** |
| M+3 | 7 015 | 5 516 | **+1 499** | +104 630 € | **+52 660 €** |
| **Cumul 90 j** | 18 846 | 16 152 | **+2 694** | **+188 041 €** | **+94 641 €** |

Les gains montent parce que les cohortes reviennent (1,06 commande le premier mois,
+0,14 ensuite, § 3) ; les pertes aussi, plus lentement, car 18 % des commandes perdues
étaient des premières commandes.

| Indicateur | Avant (M0) | Après (M+3) | Écart |
| --- | ---: | ---: | ---: |
| Commandes / mois | 42 000 | 43 499 | +3,6 % |
| CA TTC / mois | 2 931 600 € | 3 036 230 € | **+3,6 %** |
| Dépense pub / mois HT | 1 047 000 € | 1 047 000 € | **0 €** |
| — dont marque + retargeting | 272 220 € (26,0 %) | 41 880 € (4,0 %) | **−22,0 pts** |
| — dont prospection | 575 850 € (55,0 %) | 806 190 € (77,0 %) | +22,0 pts |
| MER blended (seuil EBITDA 2,35) | 2,80 | **2,90** | +19,0 % → +23,4 % au-dessus du seuil |
| Marge brute CM2 (60,4 % du CA HT) | 1 475 572 € | 1 528 236 € | +52 664 € |
| CM3 (après pub), frais fixes 230 000 € | 428 572 € | 481 236 € | +52 664 € |
| **EBITDA / mois** | **198 572 €** | **251 236 €** | **+52 664 €** |
| **EBITDA en % du CA HT** | **8,1 %** | **9,9 %** | **+1,8 pt** |
| **EBITDA annualisé** | 2 382 864 € | 3 014 832 € | **+631 968 €** |

**Le CA n'a pas baissé : il a monté de 3,6 %**, à budget publicitaire identique. Gain
annualisé d'EBITDA **631 968 €**, +26,5 %, pour un test à 8 700 € — **73 pour 1**.

---

## 6. Ce qui aurait pu mal tourner

1. **Le concurrent qui enchérit pendant le test.** En A, la part d'impression sur les
   requêtes de marque est tombée de 94 % à 61 % sans qu'aucun concurrent n'escalade. Si
   l'un l'avait fait, les 20,4 % auraient été surestimés : on coupe un canal défensif en
   croyant couper une récolte.
2. **La contamination algorithmique.** Sans budgets géographiques figés, Meta redéploie
   sa diffusion vers la cellule où le retargeting disparaît : le témoin perd du budget et
   le lift devient artificiellement bon.
3. **Le CAC marginal de la prospection.** Toute l'option C repose sur 44,00 € ; à 56 €
   l'opération devient neutre. D'où une réallocation **par tranches de 25 %, avec
   relecture du CAC marginal toutes les deux semaines.**
4. **Le décalage de trésorerie.** La récolte rendait sa contribution immédiatement, la
   prospection la rend sur 12 mois. Payback P4 1,6 mois (§ 3.1), BFR 1 392 510 € (§ 4) :
   finançable. À payback 5 mois, la même décision tuait la marque (E10, E13).
5. **La borne basse de l'intervalle.** À 10,0 % d'incrémentalité (question 7), la coupe
   aurait dû aller plus loin ; à 30,1 %, moins loin. **On décide sur le point estimé, en
   gardant un plancher.**

---

## 7. Le mécanisme généralisable

> **La règle.** Un ROAS élevé est plus souvent le symptôme d'une **récolte** que d'une
> **création de demande**. Classe tes canaux par position dans le parcours, pas par
> ROAS : plus un canal intervient tard, plus il s'attribue de ventes qu'il n'a pas
> causées. **Ce qui se pilote n'est jamais le ROAS affiché mais le produit
> `ROAS affiché × incrémentalité mesurée`** — et l'incrémentalité se mesure, elle ne se
> déduit d'aucun tableau.

Trois corollaires opérationnels :

- **Le budget se juge à l'arbitrage, pas au seuil.** Un canal peut couvrir ses coûts
  variables (2,24 > 1,99, MER seuil CM3) et rester le pire emploi du prochain euro.
- **On ne coupe jamais à zéro un canal défensif.** Le plancher de 4 % du budget sépare
  C (+631 968 €) de D (−824 640 €).
- **Un test se dimensionne avant d'être lancé.** Sans le § 4.3 : 10 jours, « pas
  d'effet », et 272 220 € coupés par mois sur une mesure incapable de distinguer 0 % de
  18,7 % de perte.

Les autres protocoles (holdout d'audience, PSA test, MMM géographique) sont dans
[E09](../modules/E09-mesure-et-incrementalite.md), le CAC marginal dans
[E01](../modules/E01-arithmetique-de-la-marque.md).

**Ce que ce test ne dit pas, et qu'il faut écrire noir sur blanc.**

- **Il ne voit que six semaines.** L'effet de long terme de la recherche marque —
  protection du nom, clients revenus au-delà de la fenêtre — lui échappe : on rejoue à
  12 mois.
- **Il ne mesure pas la défense concurrentielle**, puisque personne n'a attaqué pendant
  la fenêtre : un test mesure ce qui s'est passé, pas ce qui aurait pu se passer. D'où le
  plancher de 20 940 € sur les requêtes « marque » exactes et « marque + concurrent », et
  une alerte si la part d'impression passe sous 85 % ou si un annonceur tiers apparaît
  sur plus de 5 % des requêtes de marque. **On ne coupe jamais son propre nom sans
  surveiller qui enchérit dessus le lendemain.**
- **Il ne dit rien de la saisonnalité, ni des autres marchés.** Six semaines de mai-juin
  ne prédisent pas novembre : à remesurer avant le Black Friday (C09). Et DE, ES et IT
  ont une notoriété plus faible, donc une incrémentalité de marque sans doute plus
  élevée : la coupe y a été appliquée à moitié, en attente d'un test local.

---

## 8. Questions

1. Retrouve la dépense publicitaire mensuelle de NØRA en P4 à partir des seuls § 2.2 et
   § 2.3 des canoniques, puis exprime-la par semaine et par jour.
2. Chiffre les ventes fantômes mensuelles du § 1, et dis pourquoi elles augmenteraient
   avec une fenêtre d'attribution de 28 jours après clic.
3. On n'exige plus de détecter qu'une baisse de 15 % au lieu de 10 %, tout le reste
   identique. Combien de conversions par cellule, et combien de jours ?
4. Calcule le CAC incrémental et le ROAS incrémental de la recherche marque à partir des
   seules données brutes de la cellule A, sans réutiliser le § 5.2.
5. À partir de quel taux d'incrémentalité la recherche marque couvre-t-elle sa
   contribution à budget plein ? Compare à 20,4 %, et dis pourquoi ça ne suffit pas à
   décider.
6. Le CAC marginal de la prospection s'établit à 62,00 € au lieu de 44,00 €. Refais le
   calcul du mois M+3 et tranche.
7. Si l'incrémentalité de la recherche marque était à la borne basse de son intervalle
   (10,0 %), quel serait son CAC incrémental et qu'aurait-il fallu décider ?

---

## 9. Corrigé des questions

**1.** `2 931 600 ÷ 2,80 = 1 047 000 € HT/mois`, contrôlé par
`1 047 000 ÷ 2 443 000 = 42,9 %` (§ 2.2) ; puis `× 12 ÷ 52 = 241 615 €` par semaine et
`× 12 ÷ 365 = 34 422 €` par jour, toujours HT. Ne divise jamais un mensuel par 4 pour
obtenir une semaine : l'écart vaut `261 750 − 241 615 = 20 135 €`, soit 8,3 %.

**2.** `4 078 589 − 2 931 600 = 1 146 989 € TTC par mois`, soit +39,1 %. En passant la
fenêtre de 7 à 28 jours après clic, chaque plateforme s'attribue des conversions plus
lointaines : le recouvrement entre canaux augmente, la somme des CA attribués monte, le
CA réel ne bouge pas. **Allonger la fenêtre améliore tous les ROAS sans créer un euro.**

**3.** Effet à détecter `|ln 0,85| = 0,162519`.

```
n (Poisson) = 24,823 ÷ 0,026412 = 940 → n réel = 940 × 3,00 = 2 820 par cellule
Durée = 2 820 ÷ 173,6 = 16,2 jours → 21 jours
```

Deux fois plus court, et incapable de distinguer une perte de 12 % d'une perte nulle. Un
MDE lâche est une zone de risque acceptée : `42 000 × 12 % × 69,80 € = 351 792 € TTC/mois`.
Écris ce montant avant de choisir la durée.

**4.** Cellule A : 172,4 puis 155,2 cmd/j ; témoin 173,4 puis 176,9 ; dépense évitée
27 075 € HT sur 42 jours ; 101,59 commandes/jour revendiquées.

```
Rapport de base A/C = 172,4 ÷ 173,4 = 0,9942
Contrefactuel A     = 176,9 × 0,9942 = 175,88 cmd/j
Commandes perdues   = (175,88 − 155,2) × 42 = 868,6
CAC incrémental  = 27 075 ÷ 868,6 = 31,17 € HT   ROAS incr. = 69,80 ÷ 31,17 = 2,24
Incrémentalité   = 868,6 ÷ (101,59 × 42) = 20,4 %
```

Contrôle croisé : `6,35 ÷ 20,4 % = 31,13 €`, le même nombre à l'arrondi près. Le CAC
incrémental vaut toujours `CAC attribué ÷ incrémentalité`.

**5.** Le canal couvre sa contribution si son CAC incrémental passe sous 35,13 €, donc
`157 050 ÷ (24 750 × 35,13) = 157 050 ÷ 869 468 = **18,1 %** d'incrémentalité`.

À 20,4 % elle est **au-dessus** de son seuil : chaque euro y rapporte 1,13 €. Insuffisant
pour décider, car un seuil compare un canal à zéro alors qu'un budget le compare **aux
autres emplois du même euro** — 1,90 € en prospection (§ 5.2). On ne coupe pas parce que
c'est mauvais, on coupe parce que c'est le moins bon.

**6.**

```
Nouveaux clients = 230 340 ÷ 62,00 = 3 715 /mois
Gagnées M+3 = 3 715 × (1,06 + 0,14 + 0,14) = 4 978 ; perdues 5 516 ; net −538
Δ EBITDA = −538 × 35,13 = −18 900 €/mois = −226 800 €/an
```

**On ne réalloue pas.** Seuil d'indifférence : `230 340 ÷ (5 516 ÷ 1,34) = 55,96 €`.
Au-delà, la bonne décision n'est plus C mais B — couper et encaisser (+438 576 €/an) en
acceptant le recul de CA. **Un test d'incrémentalité dit où ne pas mettre l'argent, jamais
où le mettre : cette seconde réponse demande le CAC marginal du canal d'accueil.**

**7.** `24 750 × 10,0 % = 2 475` commandes incrémentales/mois, donc
`157 050 ÷ 2 475 = 63,45 € HT` de CAC incrémental et `69,80 ÷ 63,45 = 1,10` de ROAS
incrémental.

1,10 est très inférieur au MER seuil CM3 de 1,99 (§ 2.3) : le canal ne couvrirait pas ses
coûts variables. Il aurait fallu descendre au plancher purement défensif — requêtes de
marque exactes et « marque + concurrent », environ 8 000 €/mois au lieu de 20 940 €. Mais
on décide sur le point estimé, puis **on resserre l'intervalle en rejouant le test** : un
intervalle large est une commande de mesure, pas une excuse.

---

*Fin du cas C06. Suite : [C07](C07-ouverture-allemagne.md) — ouvrir l'Allemagne.*
