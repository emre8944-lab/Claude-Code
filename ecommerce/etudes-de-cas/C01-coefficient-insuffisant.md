# Cas C01 — Le produit à ×2,5 qui ne pouvait pas gagner

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des ordres de
> grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.
> **Ce que tu dois en tirer :** le coefficient produit est décidé avant ta première vente,
> et aucune performance publicitaire ne rattrape un coefficient trop bas.
> **Modules rattachés :** E01, E02, E03.

*Arrondi : calculs menés sur les euros exacts, pourcentages à deux décimales — la somme des
lignes peut s'écarter du total de 0,01 point.*

---

## 1. La situation

ATLAS vend un accessoire de bureau — support modulaire acier et bois, 1,4 kg emballé — à
**29,90 € TTC**, livraison offerte. Le fondateur est seul, a lancé il y a onze mois,
encaisse **34 000 € TTC par mois** et perd de l'argent depuis le premier. Son diagnostic :
« ma publicité est mauvaise, mes concurrents annoncent des ROAS de 4, moi je suis à 2,5 ».
Il cherche une agence. TVA 20 % partout, comme dans les [chiffres
canoniques](../donnees/chiffres-canoniques.md).

| Paramètre | Valeur | Nature |
| --- | ---: | --- |
| Prix catalogue ; **coefficient (PVC TTC ÷ COGS)** | 29,90 € TTC ; **×2,53** | donnée ; dérivé |
| Coût de revient rendu entrepôt (COGS) | 11,80 € HT | donnée |
| Remise moyenne encaissée (code −10 % pris par 30 % des cmd.) | 3,0 % | *hypothèse* |
| Transport aval (produit lourd, livraison offerte) + prépa. | 6,80 € + 1,20 € HT | donnée / *hyp.* |
| Taux de retour ; transport retour + reconditionnement ; reprise | 4,0 % ; 6,50 € HT ; 70 % | *hypothèse* |
| PSP (prestataire de paiement) | 1,80 % de l'encaissement TTC + 0,25 € / tr. | *hypothèse* |
| Commandes expédiées ; publicité | 1 172 / mois ; 13 600 € / mois | donnée |
| Frais fixes (il ne se paie pas) ; trésorerie ; stock | 4 200 € / mois ; 31 000 € ; 2 900 u. | donnée |

**Convention :** le CA de référence est le **CA encaissé** — après remise, avant
remboursement — parce que c'est ce que son back-office affiche, donc ce sur quoi se calcule
le MER. Les canoniques NØRA partent du CA catalogue, remise en ligne de coût. **Même euro
de marge, pourcentage différent :** dis toujours laquelle tu utilises.

### 1.1 Le compte, par 100 commandes expédiées et par mois

| Ligne | Par 100 cmd. | Par mois | % CA HT |
| --- | ---: | ---: | ---: |
| Encaissement TTC (29,90 € × 0,97 / cmd.) | 2 900,30 € TTC | 33 992 € TTC | — |
| **CA encaissé HT** (÷ 1,20) | **2 416,92 €** | **28 326 €** | **100,00 %** |
| Remboursements retours (4 % des commandes) | −96,68 € | −1 133 € | 4,00 % |
| COGS net de reprise (1 180,00 − 33,04 € récupérés) | −1 146,96 € | −13 442 € | 47,46 % |
| Logistique aller (100 × 8,00 €) + retour (4 × 6,50 €) | −826,00 € | −9 681 € | 34,18 % |
| PSP net (77,21 prélevés − 2,09 € restitués) | −75,12 € | −880 € | 3,11 % |
| **Marge brute (CM2)** | **272,16 €** | **3 190 €** | **11,26 %** |
| Publicité (MER 2,50) | — | −13 600 € | 48,01 % |
| **CM3 (marge après publicité)** | — | **−10 410 €** | −36,75 % |
| Frais fixes | — | −4 200 € | 14,83 % |
| **EBITDA** | — | **−14 610 €** | **−51,58 %** |

**2,72 € HT de marge brute par commande expédiée**, sur un ticket de 24,17 € HT. Il perd
**175 320 € par an**, et sa trésorerie de 31 000 € lui donne deux mois et six jours.

---

## 2. Le diagnostic

### 2.1 Le MER seuil

Le MER (*Media Efficiency Ratio*) rapporte le CA TTC à la dépense publicitaire :
33 992 ÷ 13 600 = **2,50**. Le fondateur compare ce 2,50 à des chiffres entendus ailleurs
et conclut qu'il manque de performance. Le MER **seuil**, celui au-delà duquel la marge
après publicité devient positive, tient en une ligne (module E01) :

```
MER seuil (CM3 = 0) = (1 + TVA) ÷ marge brute en % du CA HT
                    = 1,20 ÷ 0,1126 = 10,66
```

Contrôle : NØRA à P5 a 61,5 % de marge brute, et 1,20 ÷ 0,615 = 1,95 — exactement le MER
seuil du § 2.3 canonique. Appliquée à ATLAS, la formule exige **10,66**, là où la catégorie
« accessoire de bureau sous 40 € TTC » plafonne autour de 2,2 à 2,8. **Il est à −76,5 % du
seuil.** Pas un écart de pilotage : un écart de nature.

### 2.2 Le seuil EBITDA n'existe pas

```
MER seuil (EBITDA = 0) = (1 + TVA) ÷ (marge brute % − frais fixes en % du CA HT)
```

Contrôle sur NØRA P5 : 1,20 ÷ (0,615 − 360 000/3 610 997) = **2,33**, identique au
canonique. Pour ATLAS : 11,26 % − 14,83 % = **−3,57 %**, dénominateur négatif. **Aucun MER
ne rend ATLAS rentable à ce volume**, publicité gratuite comprise : 3 190 € de marge brute
ne couvrent pas 4 200 € de fixes. Il faudrait 1 544 commandes mensuelles de trafic gratuit
pour seulement payer les outils et le comptable.

### 2.3 La comparaison à NØRA

| Produit | PVC TTC | PVC HT | COGS | Marge marchandise | Taux | Coef. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| NØRA Masque Réparateur 200 ml | 29,00 € | 24,17 € | 3,60 € | 20,57 € | 85,1 % | ×8,1 |
| NØRA Rituel Complet (le plancher de la gamme) | 74,00 € | 61,67 € | 11,50 € | 50,17 € | 81,4 % | ×6,4 |
| **ATLAS** | **29,90 €** | **24,92 €** | **11,80 €** | **13,12 €** | **52,6 %** | **×2,53** |

Le Masque NØRA se vend **moins cher** qu'ATLAS (29,00 € contre 29,90 € TTC) et gagne
20,57 € de marge contre 13,12 € : le prix n'est pas le problème d'ATLAS. Structures de coût
variable en convention canonique § 2.1 — en % du **CA HT catalogue**, remise en coût :

| Ligne (% du CA HT catalogue) | NØRA P1 | NØRA P5 | **ATLAS** |
| --- | ---: | ---: | ---: |
| COGS | 20,00 % | 14,50 % | **46,03 %** |
| Logistique | 16,00 % | 11,00 % | **33,15 %** |
| PSP | 1,80 % | 1,55 % | **3,01 %** |
| Retours / SAV | 2,00 % | 3,50 % | **3,88 %** |
| Remises | 3,00 % | 8,00 % | **3,00 %** |
| **Marge brute (CM2)** | **57,20 %** | **61,50 %** | **10,92 %** |

Deux lignes tuent ATLAS, pas une. Le COGS pèse 46 % contre 20 % chez NØRA au même stade de
vie. Et la **logistique pèse 33 %** parce que le produit fait 1,4 kg, que la livraison est
offerte et que le panier est mono-produit : 8,00 € sur un ticket de 24,17 € HT, quand un
flacon de 50 ml voyage pour une fraction de ce prix dans un panier de 1,6 article. **Le
poids du produit est une variable financière.** Troisième signal, le PSP à 3,01 % au lieu
de 1,80 % : les 0,25 € fixes par transaction pèsent trois fois plus sur un panier de 29 €
que sur un panier de 74 €.

### 2.4 Ce que grandir fait à la perte

Le fondateur voulait lever pour passer à l'échelle. Volume ×10, avec des gains d'échelle
généreux (COGS −8 %, transport −10 %, PSP renégocié) et un MER maintenu à 2,50 — optimiste,
il se dégrade normalement avec le volume. Remises portées à 6 % et retours à 5,5 %, comme
chez NØRA § 2.1.

| Ligne | Aujourd'hui | ×10 avec gains d'échelle |
| --- | ---: | ---: |
| Commandes / mois | 1 172 | 11 720 |
| CA encaissé TTC ; HT | 33 992 € TTC ; 28 326 € | 329 402 € TTC ; 274 502 € |
| Marge brute (€ ; %) | 3 190 € ; 11,26 % | 41 158 € ; **14,99 %** |
| MER seuil (CM3 = 0) | 10,66 | **8,00** |
| Publicité (MER 2,50) | 13 600 € | 131 761 € |
| CM3 ; frais fixes | −10 410 € ; 4 200 € | −90 603 € ; 26 000 € |
| **EBITDA / mois ; % CA HT** | **−14 610 € ; −51,58 %** | **−116 603 € ; −42,48 %** |
| **EBITDA / an** | **−175 320 €** | **−1 399 236 €** |

Sans aucun gain d'échelle, la colonne de droite donnerait **−130 069 €** par mois (marge
brute 31 897 €, publicité 135 966 €). Avec les gains, le **taux** de perte s'améliore de
9,1 points, de −51,58 % à −42,48 %, pendant que le **montant** est multiplié par **7,98**.
Le MER seuil descend de 10,66 à 8,00 et reste à 3,2 fois le MER atteignable. Le seuil
EBITDA, lui, existe enfin, la marge brute (14,99 %) dépassant les fixes (9,47 % du CA HT) :

```
MER seuil (EBITDA = 0) = 1,20 ÷ (0,1499 − 0,0947) = 21,73
```

NØRA, à son palier le plus exigeant, a besoin de 2,33.

> **À retenir :** quand la marge après publicité est négative, chaque euro de CA
> supplémentaire creuse la perte. Les gains d'échelle améliorent le ratio et aggravent le
> montant : un tableau de bord en pourcentages te montre une courbe qui monte pendant que
> ton compte en banque se vide.

---

## 3. Les options

Décomposition par 100 commandes expédiées. *(a)* prix 49,00 € TTC, retours à 6 % — un
client qui paie 49 € examine ce qu'il reçoit. *(b)* COGS à 9,44 €. *(c)* recharges
14,90 € TTC, COGS 2,10 €, 190 g, panier de 2 packs, retours 1 %.

| Ligne (par 100 commandes) | Statu quo | (a) 49 € | (b) COGS −20 % | (c) recharges |
| --- | ---: | ---: | ---: | ---: |
| CA encaissé HT | 2 416,92 € | 3 960,83 € | 2 416,92 € | 2 483,33 € |
| Remboursements retours | −96,68 € | −237,65 € | −96,68 € | −24,83 € |
| COGS net | −1 146,96 € | −1 130,44 € | −917,57 € | −420,00 € |
| Logistique | −826,00 € | −839,00 € | −826,00 € | −333,00 € |
| PSP net | −75,12 € | −105,42 € | −75,12 € | −78,10 € |
| **Marge brute (€ ; %)** | **272,16 € ; 11,26 %** | **1 648,32 € ; 41,62 %** | **501,55 € ; 20,75 %** | **1 627,40 € ; 65,53 %** |
| **MER seuil ; coefficient** | **10,66 ; ×2,53** | **2,88 ; ×4,15** | **5,78 ; ×3,17** | **1,83 ; ×7,10** |

### 3.1 Option (a) — le prix à 49,00 €

Le MER seuil devient atteignable ; reste la conversion. Le site convertit à 2,30 %
(1 172 commandes pour 50 957 sessions). À budget publicitaire donc à sessions constantes :

| Scénario | Conversion | Cmd. | CA encaissé TTC | MER | CM3 | EBITDA |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Conversion −20 % | 1,840 % | 938 | 44 583 € TTC | 3,28 | +1 861 € | **−2 339 €** |
| Conversion −35 % | 1,495 % | 762 | 36 218 € TTC | 2,66 | −1 040 € | **−5 240 €** |
| Conversion −50 % | 1,150 % | 586 | 27 853 € TTC | 2,05 | −3 941 € | **−8 141 €** |

Aucun ne rend l'affaire rentable. Pour un EBITDA nul il faut 1 080 commandes, soit 2,12 %
de conversion : **une baisse de conversion sous 7,8 % pour une hausse de prix de 63,9 %**,
soit une élasticité de −0,12, là où un accessoire sans marque est plutôt à −1,0 ou −2,0.

### 3.2 Option (b) — le COGS

Mensuellement : marge brute 5 878 €, CM3 −7 722 €, **EBITDA −11 922 €**. Gain de 2 688 €
par mois ; il perd toujours 143 000 € par an. Prix de ce gain : le fournisseur exige 6 000
unités fermes, **56 640 € HT dont la moitié à la commande**. Il immobiliserait 28 320 € —
sur 31 000 € de trésorerie — dans cinq mois de stock d'un produit déficitaire à l'unité.

### 3.3 Option (c) — le consommable

**16,27 € HT de marge brute par commande de recharge, contre 2,72 € sur le produit
principal.** *Hypothèse de comportement :* 22 % des acheteurs commandent des recharges sur
12 mois, 1,9 commande chacun, soit 0,418 commande par client acquis.

```
Contribution de réachat / client acquis = 0,418 × 16,27 €          = 6,80 € HT
nCAC                                    = 13 600 € ÷ 1 125 clients = 12,09 €
LTV 12 mois en contribution             = 2,72 € + 6,80 €          =  9,52 €
LTV / CAC                               = 9,52 ÷ 12,09             =    0,79
```

**0,79.** Sous 1 : on arrête l'acquisition. Pour atteindre 2,0 il faudrait **1,32 commande
de recharge par client acquis** au lieu de 0,418, soit 3,2 fois le comportement modélisé.
Un support de bureau n'est pas une cure capillaire : le réachat n'a pas de raison
biologique d'exister. En régime après douze mois : marge brute mixte **27,10 %**, MER seuil
**4,43**, **EBITDA −7 857 €** — jamais positif.

### 3.4 Option (d) — arrêter

| Ligne | Montant |
| --- | ---: |
| Stock résiduel (2 400 u., COGS engagé) | 28 320 € HT |
| Cession à un grossiste, 7,50 € HT l'unité, enlèvement à sa charge | +18 000 € HT |
| Perte comptable sur stock ; coûts de sortie | −10 320 € ; −3 500 € |
| Pertes d'exploitation évitées sur 12 mois | +175 320 € |
| **Écart net à 12 mois contre le statu quo** | **+189 820 €** |

### 3.5 Le tableau qui décide

| Option (fixes 4 200 €, sauf (c) 5 100 € et (d) 0 €) | Marge brute / mois | CM3 | **EBITDA** | Δ vs statu quo |
| --- | ---: | ---: | ---: | ---: |
| Statu quo | 3 190 € | −10 410 € | **−14 610 €** | — |
| (a) 49 €, conv. −20 % à −50 % | 15 461 à 9 659 € | +1 861 à −3 941 € | **−2 339 à −8 141 €** | +12 271 à +6 469 € |
| (b) COGS −20 % | 5 878 € | −7 722 € | **−11 922 €** | +2 688 € |
| (c) recharges, en régime | 10 843 € | −2 757 € | **−7 857 €** | +6 753 € |
| (a)+(b), conv. −20 % | 17 582 € | +3 982 € | **−218 €** | +14 392 € |
| (d) arrêt | 0 € | 0 € | **0 €** | +14 610 € |

Seul (a)+(b) approche l'équilibre, et il exige de réussir **simultanément** deux paris
indépendants : que le marché absorbe +64 % de prix en ne perdant que 20 % de conversion, et
que le fournisseur concède −20 % contre 56 640 € de commande ferme. Probabilité jointe
faible, mise 28 320 € sur 31 000 € de trésorerie, gain : un EBITDA de −218 €. **On ne joue
pas sa trésorerie pour atteindre zéro.**

---

## 4. La décision et l'exécution

Décision en semaine 1 : **arrêt d'ATLAS v1, cession du stock, repositionnement sur un
produit dont le coefficient est décidé avant le sourcing.** Cahier des charges chiffré,
écrit **avant** de chercher un fournisseur : coefficient ≥ ×6,0, poids emballé ≤ 400 g,
transport aval ≤ 3,50 € HT, prix cible 55 à 65 € TTC. Résultat : **ATLAS Studio**,
organiseur modulaire léger, 59,00 € TTC, COGS 8,90 € HT, 380 g, transport 3,20 € HT,
coefficient **×6,63**.

| Mois | Ce qui se passe | Marge brute | EBITDA | Trésorerie fin de mois |
| --- | --- | ---: | ---: | ---: |
| M0 | Décision | — | — | 31 000 € |
| M1 | Publicité coupée à 3 000 €. 380 commandes plein tarif. | 1 034 € | −6 166 € | 24 834 € |
| M2 | Cession de 2 400 u. au grossiste (+18 000 €). Publicité 1 500 €. 120 cmd. | 327 € | −5 373 € | 37 461 € |
| M3 | Publicité à zéro. Sourcing, 4 échantillons (−4 200 €). Fixes à 3 400 €. | 0 € | −3 400 € | 29 861 € |
| M4 | Commande 1 200 × 8,90 € comptant. 2 500 € de créa. Aucune vente. | 0 € | −3 400 € | 13 281 € |
| M5 | Lancement. 210 commandes. Publicité 6 000 €, MER 1,98 — apprentissage. | 6 391 € | −3 009 € | 10 272 € |
| M6 | 620 cmd. Publicité 13 500 €, MER 2,60. Réappro 17 800 €, 50 / 50 à 30 j. | 18 868 € | **+968 €** | **2 340 €** |

Le contrefactuel, s'il avait continué : 16 390 € au M1, 1 780 € au M2, **−12 830 € au M3**,
−27 440 € au M4. **Il était en cessation de paiements au mois 3**, réappros non comptés.

Note le mois 6 : celui où l'EBITDA redevient positif **et** celui où la trésorerie touche
son point bas, parce que la croissance exige d'acheter du stock avant d'encaisser — le
mécanisme du § 4 des canoniques. Sans les 50 % à 30 jours, il passait sous zéro le mois où
il devenait rentable.

---

## 5. Les résultats

| Indicateur | ATLAS v1 — 29,90 € | ATLAS Studio — 59,00 € | Écart |
| --- | ---: | ---: | ---: |
| Coefficient ; ticket encaissé | ×2,53 ; 29,00 € TTC | **×6,63** ; 56,64 € TTC | +4,10 ; +95 % |
| COGS ; logistique / commande | 11,80 € ; 8,00 € HT | 8,90 € ; 4,40 € HT | −24,6 % ; −45,0 % |
| Commandes / mois ; CA encaissé HT | 1 172 ; 28 326 € | 620 ; 29 264 € | −47 % ; +3,3 % |
| **Marge brute (% ; €)** | **11,26 % ; 3 190 €** | **64,48 % ; 18 868 €** | **+53,2 pts ; ×5,9** |
| **MER seuil (CM3 = 0)** | **10,66** | **1,86** | |
| MER réel ; écart au seuil | 2,50 ; **−76,5 %** | 2,60 ; **+39,8 %** | |
| Publicité ; frais fixes | 13 600 € ; 4 200 € | 13 500 € ; 4 400 € | |
| CM3 | −10 410 € | +5 368 € | +15 778 € |
| **EBITDA / mois** | **−14 610 €** | **+968 €** | **+15 578 €** |
| **EBITDA en % du CA HT** | **−51,58 %** | **+3,31 %** | **+54,9 pts** |

**+3,3 % de chiffre d'affaires avec 47 % de commandes en moins**, et un passage de −51,58 %
à +3,31 % d'EBITDA : il n'a pas amélioré son exécution, il a changé son arithmétique. Les
quatre mois sacrifiés valaient 135 968 € TTC de CA — un CA qui portait −14 610 € d'EBITDA
par mois, donc y renoncer a **rapporté 58 440 €**. Avec 29 264 € de CA HT il reste sous le
palier P1 de NØRA (30 667 € HT), mais **avec un EBITDA positif**, là où NØRA est à −30,7 %
à ce stade parce qu'elle achète volontairement des clients qui reviendront. ATLAS Studio
n'a pas de réachat biologique : il n'a pas le droit de faire ce pari.

---

## 6. Ce qui aurait pu mal tourner

**Le déstockage pouvait détruire le repositionnement.** L'option initiale était de liquider
les 2 400 unités à 19,90 € TTC sur son propre site : 39 800 € HT encaissés, moins 19 200 €
de logistique, 1 460 € de PSP et 2 000 € de publicité = **17 140 € nets**, soit 860 € de
**moins** que la cession au grossiste — et en prime une liste d'acheteurs à 19,90 € à qui
vendre 59,00 € six mois plus tard. **La voie qui paraissait la plus rentable était dominée
sur le cash et destructrice sur la marque.**

**Le nouveau produit pouvait ne pas convertir.** Au 1er du mois 5 il avait 13 281 €, soit
3,9 mois au rythme de brûlage de M3–M4 : si le premier concept rentable était arrivé au mois
8 et non au mois 6, il mourait. La faute n'est pas au mois 1, elle est onze mois plus tôt —
quand il n'a pas fait ce calcul avant son premier conteneur.

**Le sourcing léger pouvait dégrader la qualité.** Le taux de retour modélisé passe de 4 %
à 5 %. S'il avait triplé à 12 % : marge brute 2 735,64 € par 100 commandes soit **57,96 %**,
MER seuil 1,20 ÷ 0,5796 = **2,07** — toujours sous le MER réel de 2,60. **Un coefficient de
×6,63 absorbe un triplement du taux de retour ; ×2,53 n'absorbe rien.** Voilà ce qu'achète
un bon coefficient : de la tolérance à l'erreur.

---

## 7. Le mécanisme généralisable

> **La règle :** le coefficient est fixé le jour où tu choisis un produit et un prix, avant
> ta première vente, et il plafonne définitivement tout ce que la créa, l'algorithme, le
> funnel et la négociation pourront faire ensuite.

Il se calcule avant le sourcing, où « autres coûts var. » = logistique + PSP + retours :

```
Coefficient minimum = (1 + TVA)
                    ÷ [ (1 − remise) × (1 − (1 + TVA)/MER_atteignable − autres coûts var. en % du CA HT) ]
```

| Marque | MER atteignable | Remise | Autres coûts var. | **Coef. minimum** | Coef. réel | Marge de sécurité |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| ATLAS v1 | 2,50 | 3,0 % | 41,29 % | **×11,55** | ×2,53 | **0,22** |
| ATLAS Studio | 2,60 | 4,0 % | 17,33 % | **×3,42** | ×6,63 | **1,94** |
| NØRA Rituel (P5) | 2,90 | 8,0 % | 16,05 % | **×3,06** | ×6,4 | **2,09** |

**Un.** ATLAS v1 avait besoin de ×11,55 et avait ×2,53 : il lui manquait un facteur 4,6.
Aucune agence, aucun angle créatif, aucune optimisation de tunnel ne produit un facteur 4,6.
La décision fatale avait été prise onze mois plus tôt, en trente secondes, sur un tableur.

**Deux.** Le coefficient minimum n'est pas le coefficient cible : vise **au moins le
double**. C'est le sens du ×5 plancher des chiffres canoniques § 1, et ce que fait NØRA
avec 2,09 de sécurité. Cette marge paie les retours et les remises qui montent, le MER qui
se dégrade quand tu passes d'un pays à cinq, et les erreurs à venir.

**Trois.** Le coefficient ne dépend pas que du COGS : les autres coûts variables pèsent
41,29 % chez ATLAS v1 contre 17,33 % chez ATLAS Studio, parce que l'un fait 1,4 kg et
l'autre 380 g. **Le poids et la valeur du panier sont des variables financières.**

> **À retenir :** avant de commander ton premier conteneur, écris trois lignes — le MER que
> ta catégorie permet, tes coûts variables hors COGS en % du CA HT, le coefficient minimum
> qui en découle. Si ton coefficient réel n'est pas au moins le double, tu ne cherches pas
> une agence : tu cherches un autre produit.

---

## 8. Questions

1. Calcule le coefficient d'ATLAS v1, compare-le au Rituel Complet de NØRA, et dis à quel
   prix TTC ATLAS devrait se vendre, à COGS constant, pour atteindre le plancher ×6,4.
2. Déroule le calcul de la marge brute d'ATLAS v1 par commande expédiée, en euros HT et
   en pourcentage du CA HT encaissé.
3. Calcule le MER seuil CM3 = 0, démontre que le MER seuil EBITDA = 0 n'existe pas, puis
   réponds : à MER 4,00, puis avec une publicité gratuite, ATLAS v1 serait-il rentable ?
4. Volume ×10 avec gains d'échelle : EBITDA mensuel, rapport à la perte actuelle, et en
   deux phrases pourquoi le taux s'améliore pendant que le montant explose.
5. Option (b) seule : quel COGS faudrait-il pour un MER seuil de 2,50 ? Exprime-le en
   baisse en pourcentage et en coefficient. Conclus.
6. Option (a) : à 49,00 € TTC, quel taux de conversion minimum pour un EBITDA nul, et
   quelle baisse maximale cela autorise-t-il par rapport aux 2,30 % actuels ?
7. Le fondateur veut tester (b) puis (c) pendant six mois avant d'envisager l'arrêt.
   Chiffre ce que coûte cette décision par rapport à un arrêt immédiat.

---

## 9. Corrigé des questions

**1.** Coefficient = 29,90 ÷ 11,80 = **×2,53**. Le Rituel Complet NØRA est à
74,00 ÷ 11,50 = ×6,4 pour un COGS quasi identique (11,50 € contre 11,80 €) : même coût
marchandise, prix 2,5 fois plus élevé. Pour atteindre ×6,4 à COGS constant : 11,80 × 6,4 =
**75,52 € TTC**. Réponse chiffrée à « et si j'augmentais un peu mes prix ? ».

**2.** Par 100 commandes expédiées :
```
CA encaissé HT = 100 × 29,90 × 0,97 ÷ 1,20      = 2 416,92 €
Remboursements = 4 × 29,003 ÷ 1,20              =    96,68 €
COGS net       = 100 × 11,80 − 4 × 0,70 × 11,80 = 1 146,96 €
Logistique     = 100 × 8,00 + 4 × 6,50          =   826,00 €
PSP net        = 2 900,30 × 1,8 % + 25,00 − 4 × 29,003 × 1,8 % = 75,12 €
Marge brute    = 2 416,92 − 2 144,76            =   272,16 €
```
Soit **2,72 € HT par commande**, et 272,16 ÷ 2 416,92 = **11,26 %**.

**3.** MER seuil CM3 = 0 : 1,20 ÷ 0,1126 = **10,66**. Pour le seuil EBITDA, le dénominateur
vaut 11,26 % − 4 200/28 326 = **−3,57 %** : négatif, donc aucun MER n'annule l'EBITDA. À
MER 4,00 : publicité = 33 992 ÷ 4 = 8 498 €, EBITDA = 3 190 − 8 498 − 4 200 = **−9 508 €**.
Publicité gratuite : 3 190 − 4 200 = **−1 010 €**. **Ce n'est pas un problème de publicité.**

**4.** EBITDA à ×10 avec gains d'échelle : **−116 603 € par mois**, −1 399 236 € par an ;
rapport 116 603 ÷ 14 610 = **×7,98**. Le taux s'améliore parce que les frais fixes et les
gains sur COGS et transport se diluent sur dix fois plus de volume — marge brute de 11,26 %
à 14,99 %, frais fixes de 14,83 % à 9,47 % du CA HT. Le montant explose parce que la marge
après publicité reste négative, à −33,0 % du CA HT : chaque commande détruit de la valeur,
et il y en a dix fois plus.

**5.** Il faut m = 1,20 ÷ 2,50 = **48,00 %**, soit 1 160,12 € de marge par 100 commandes.
Les coûts hors COGS valent 96,68 + 826,00 + 75,12 = 997,80 €, donc le COGS net maximum est
2 416,92 − 997,80 − 1 160,12 = **259,00 €**. Comme COGS net = 97,2 × C, on a
C = 259,00 ÷ 97,2 = **2,66 € HT**, soit **−77,4 %** et un coefficient de 29,90 ÷ 2,66 ≈
**×11,2**. Ce n'est pas une négociation, c'est un autre produit : un fournisseur concède
10 à 25 % contre un engagement de volume, pas 77 %. « Puis-je négocier mon COGS ? » est une
question à poser **avant** de choisir le produit.

**6.** Marge brute par commande à 49,00 € = **16,4832 € HT**. Pour un EBITDA nul il faut
couvrir 13 600 € de publicité + 4 200 € de fixes = 17 800 €, donc 17 800 ÷ 16,4832 =
**1 080 commandes**. À sessions constantes (1 172 ÷ 0,0230 = 50 957), cela fait un taux de
conversion de 1 080 ÷ 50 957 = **2,12 %**, soit une baisse maximale de **7,8 %** — alors
que le prix monte de **+63,9 %**. Élasticité-prix de −0,12 : invraisemblable sur un produit
indifférencié.

**7.** Sur six mois :
```
Pertes d'exploitation, option (b) : 6 × 11 922 €  =  71 532 €
Avance sur commande ferme MOQ (50 % de 56 640 €)  =  28 320 €
Stock et développement du consommable, option (c) =  15 000 €
Décaissement total                                = 114 852 €
```
Face à un arrêt immédiat (+18 000 € de cession − 3 500 € de sortie = **+14 500 €**),
**l'écart est de 114 852 + 14 500 = 129 352 €.** Or sa trésorerie est de 31 000 € : le seul
M1 (11 922 € de perte + 28 320 € de MOQ = 40 242 €) dépasse déjà ce qu'il a en banque. **Le
choix n'existe pas** — et c'est le point le plus dur du cas : quand tu as attendu onze mois
pour faire l'arithmétique, tu n'as plus que l'option que ta trésorerie t'autorise encore.

---

*Fin du cas C01. Suite : C02 — la vallée de la mort.*
