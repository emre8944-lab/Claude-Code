# Cas C05 — Quand payer 2,4 fois le premier panier est rationnel

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des ordres de
> grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.
> **Ce que tu dois en tirer :** un CAC ne se juge jamais contre un panier — seulement
> contre une LTV en marge de contribution **et** contre une capacité de trésorerie datée.
> **Modules rattachés :** E01, E08, E10.

*Conventions. Prix client **TTC** (TVA 20 %, comme les [chiffres
canoniques](../donnees/chiffres-canoniques.md)), coûts et chiffre d'affaires **HT**. La
remise de bienvenue est portée en coût d'acquisition, donc la contribution mensuelle est
identique tous les mois. Affichage arrondi : une colonne peut s'écarter de 1 €.*

---

## 1. La situation

RITUEL vend une cure de compléments alimentaires en **abonnement mensuel à 42,00 € TTC**,
résiliable en un clic, premier mois à **39,90 € TTC** (bienvenue −5 %). Neuf mois après le
lancement, elle recrute **1 000 nouveaux abonnés par mois** à un **CAC entièrement chargé
de 96,00 €** — média, outils, affiliation, et les 1,71 € de contribution perdue sur la
remise de bienvenue.

**96,00 € pour un premier encaissement de 39,90 € TTC : ×2,41.** Le board veut couper
l'acquisition de moitié. Le fondateur veut la doubler.

| Paramètre | Valeur | Nature |
| --- | ---: | --- |
| Prix d'abonnement ; premier encaissement | 42,00 € TTC ; 39,90 € TTC | donnée |
| CA mensuel par abonné | 35,00 € HT | dérivé (÷ 1,20) |
| COGS (30 gélules, flacon, étui) | 5,60 € HT | *hypothèse* |
| Logistique (prépa. + envoi boîte aux lettres suivi) | 3,20 € HT | *hypothèse* |
| PSP (1,8 % du TTC + 0,25 € / prélèvement) | 1,01 € HT | *hypothèse* |
| SAV, casse, échecs de paiement récupérés | 0,79 € HT | *hypothèse* |
| Attrition mensuelle observée sur 9 mois | 8,0 % | donnée |
| CAC entièrement chargé ; nouveaux abonnés | 96,00 € ; 1 000 / mois | donnée |
| Base active ; frais fixes ; trésorerie | 6 085 ; 60 000 € / mois ; 234 615 € | donnée |
| Levée d'amorçage ; consommée à date | 750 000 € ; 515 385 € | donnée |

### 1.1 La marge de contribution mensuelle par abonné

```
35,00 € HT (CA mensuel par abonné)
−  5,60 €  COGS
−  3,20 €  logistique
−  1,01 €  PSP
−  0,79 €  SAV / casse / échecs de paiement
= 24,40 € HT par abonné et par mois, soit 24,40 ÷ 35,00 = 69,71 % du CA HT
```

### 1.2 Le compte de résultat mensuel au départ

| Ligne | Montant | % CA HT |
| --- | ---: | ---: |
| CA TTC (6 085 × 42,00 €) | 255 570 € TTC | — |
| **CA HT** (6 085 × 35,00 €) | **212 975 €** | **100,00 %** |
| Coûts variables (6 085 × 10,60 €) | −64 501 € | 30,29 % |
| **Marge de contribution** (6 085 × 24,40 €) | **148 474 €** | **69,71 %** |
| Acquisition (1 000 × 96,00 €) | −96 000 € | 45,08 % |
| **CM3 (marge après acquisition)** | **52 474 €** | **24,64 %** |
| Frais fixes | −60 000 € | 28,17 % |
| **EBITDA** | **−7 526 €** | **−3,53 %** |

58 978 € TTC par semaine, −7 526 € d'EBITDA par mois, 234 615 € en banque.

---

## 2. Le diagnostic

### 2.1 Ce que le board croit

« On paie 96 € un client qui nous rapporte 42 €. » Trois erreurs dans une phrase : du HT
contre du TTC, un coût d'acquisition contre un chiffre d'affaires au lieu d'une marge, une
dépense unique contre un revenu qui se répète.

| Ce à quoi on compare le CAC de 96,00 € | Rapport | Ce que ça vaut |
| --- | ---: | --- |
| Premier encaissement TTC (39,90 €) | ×2,41 | rien — du HT contre du TTC |
| CA HT mensuel de régime (35,00 €) | ×2,74 | rien — le CA n'est pas de la marge |
| Marge de contribution mensuelle (24,40 €) | **×3,93** | le payback, en mois |
| **LTV en contribution (305,00 €)** | **÷3,18** | **le seul ratio de décision** |

### 2.2 Ce que les chiffres disent

```
Durée de vie moyenne = 1 ÷ attrition mensuelle = 1 ÷ 0,08 = 12,5 mois
LTV en contribution  = 24,40 € × 12,5          = 305,00 € HT
LTV / CAC            = 305,00 ÷ 96,00          = 3,18
Payback nominal      = 96,00 ÷ 24,40           = 3,93 mois
```

Le payback nominal est faux dans le sens optimiste : il suppose que l'abonné survit ces
quatre mois. **Au niveau de la cohorte :**

```
24,40 × (1 − 0,92ⁿ) ÷ 0,08 = 96,00
        (1 − 0,92ⁿ)         = 0,31475
              0,92ⁿ         = 0,68525
                  n         = ln(0,68525) ÷ ln(0,92) = 4,53 mois
```

**Sept dixièmes de mois entre le payback affiché et celui qu'on vit.** À 1 000 abonnés par
mois, ils valent 17 000 € de trésorerie.

Second correctif (module 13 § 2.3) : une LTV à horizon infini n'est pas finançable.

| Horizon | Mois payés / abonné | LTV contribution | LTV / CAC |
| --- | ---: | ---: | ---: |
| 12 mois | 7,90 | 192,86 € | **2,01** |
| 24 mois | 10,81 | 263,77 € | 2,75 |
| 36 mois | 11,88 | 289,84 € | 3,02 |
| ∞ (non finançable) | 12,50 | 305,00 € | 3,18 |

**Le vrai chiffre de RITUEL n'est pas 3,18 : c'est 2,01 à 12 mois.** Le board a tort sur le
raisonnement et à peu près raison sur la marge de sécurité — il n'y en a pas.

---

## 3. Le tableau qui décide : attrition × CAC

`LTV / CAC = (24,40 ÷ attrition) ÷ CAC`. Contribution figée à 24,40 €, horizon infini.
Code : **A** = on accélère (≥ 3,00), **T** = on tient sans monter le volume (2,00 à 2,99),
**S** = on arrête l'acquisition payante et on répare la rétention (< 2,00).

| Attrition | Durée de vie | LTV | CAC 60 € | CAC 80 € | CAC 96 € | CAC 110 € | CAC 125 € | CAC 140 € |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 % | 20,0 mois | 488,00 € | 8,13 **A** | 6,10 **A** | 5,08 **A** | 4,44 **A** | 3,90 **A** | 3,49 **A** |
| 6 % | 16,7 mois | 406,67 € | 6,78 **A** | 5,08 **A** | 4,24 **A** | 3,70 **A** | 3,25 **A** | 2,90 **T** |
| **8 %** | 12,5 mois | 305,00 € | 5,08 **A** | 3,81 **A** | **3,18 A** | 2,77 **T** | 2,44 **T** | 2,18 **T** |
| 10 % | 10,0 mois | 244,00 € | 4,07 **A** | 3,05 **A** | 2,54 **T** | 2,22 **T** | 1,95 **S** | 1,74 **S** |
| 12 % | 8,3 mois | 203,33 € | 3,39 **A** | 2,54 **T** | 2,12 **T** | 1,85 **S** | 1,63 **S** | 1,45 **S** |
| 15 % | 6,7 mois | 162,67 € | 2,71 **T** | 2,03 **T** | 1,69 **S** | 1,48 **S** | 1,30 **S** | 1,16 **S** |
| 20 % | 5,0 mois | 122,00 € | 2,03 **T** | 1,52 **S** | 1,27 **S** | 1,11 **S** | 0,98 **S** | 0,87 **S** |

Lis-le horizontalement. **Divise l'attrition par deux et tu peux payer ton CAC deux fois
plus cher.** Elle est au dénominateur : elle commande tout.

### 3.1 Les trois seuils

**Seuil d'attrition, à CAC constant de 96,00 €.**

```
LTV = CAC (destruction stricte)  : c = 24,40 ÷ 96,00       = 25,42 %
EBITDA = 0 en régime établi (1 000 nouveaux/mois, 60 000 € de fixes) :
   base = 1 000 ÷ c ; 24 400 ÷ c = 156 000 → c             = 15,64 %
Décision (LTV/CAC ≥ 3)           : c = 24,40 ÷ (3 × 96,00) =  8,47 %
```

RITUEL est à **8,0 %** : il lui reste **0,47 point** avant de sortir de la zone où l'on a
le droit d'accélérer.

**Seuil de CAC, à attrition constante de 8,0 %.**

```
Théorique (LTV = CAC)                               : 305,00 €
EBITDA = 0 (base de régime 12 500, fixes 60 000 €) :
   (24,40 − 60 000 ÷ 12 500) ÷ 0,08 = 19,60 ÷ 0,08  = 245,00 €
Décision (LTV/CAC ≥ 3) : 305,00 ÷ 3                 = 101,67 €
```

**Retiens l'écart entre 305 € et 101,67 €.** Le premier est ce que dit la formule, le
second ce qu'autorise la gestion : les fixes coupent 20 %, la provision pour erreur
d'estimation coupe encore 59 % du reste.

> **À retenir :** le CAC de 96 € est valide parce que l'attrition est à 8,0 %, et pour
> aucune autre raison. À 10 %, le même CAC devient un **T** ; à 12,7 %, la LTV à 12 mois
> passe sous 2,0.

---

## 4. Le vrai piège : la trésorerie

Un abonné à payback de 4,53 mois est un trou de trésorerie qui se rembourse. Mille par
mois, c'est mille trous qui se recouvrent.

### 4.1 Le cash immobilisé pour recruter 1 000 abonnés par mois

Machine d'acquisition seule : hors frais fixes, hors stock, hors TVA.

| Mois | Base active | Contribution encaissée | Acquisition | Net du mois | **Cumul** |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 1 000 | 24 400 € | −96 000 € | −71 600 € | **−71 600 €** |
| 2 | 1 920 | 46 848 € | −96 000 € | −49 152 € | **−120 752 €** |
| **4** | 3 545 | 86 500 € | −96 000 € | −9 500 € | **−158 752 €** |
| 6 | 4 921 | 120 062 € | −96 000 € | +24 062 € | −126 710 € |
| **9** | 6 598 | 160 991 € | −96 000 € | +64 991 € | **+29 606 €** |

**158 752 € immobilisés au point bas du mois 4 ; cumul positif seulement au mois 9.**
Ajoute 60 000 € de frais fixes mensuels : point bas **−515 385 € au mois 8**, cumul positif
au **mois 19**. C'est la position exacte de RITUEL : 750 000 € levés, 515 385 € consommés,
234 615 € restants.

### 4.2 Comment on meurt avec un LTV/CAC de 5,08

Contribution de 24,40 €, attrition de **5,0 %** — excellente — CAC de 96,00 € : **LTV =
488,00 €, LTV/CAC = 5,08**. La marque recrute 5 000 abonnés par mois, porte 150 000 € de
fixes et dispose de **900 000 € de trésorerie**.

| Mois | Base | Contribution | Acquisition | Fixes | Net | **Trésorerie** |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 5 000 | 122 000 € | −480 000 € | −150 000 € | −508 000 € | **+392 000 €** |
| 2 | 9 750 | 237 900 € | −480 000 € | −150 000 € | −392 100 € | **−100 €** |
| 3 | 14 263 | 348 005 € | −480 000 € | −150 000 € | −281 995 € | −282 095 € |
| 5 | 22 622 | 551 975 € | −480 000 € | −150 000 € | −78 025 € | −537 516 € |
| 6 | 26 491 | 646 376 € | −480 000 € | −150 000 € | +16 376 € | −521 140 € |

**Elle est morte à la fin du mois 2.** Le mois 6 lui donnait un EBITDA positif, le mois 12
lui rendait ses 900 000 €. Sa LTV de 488 € était juste ; son besoin au point bas était de
**1 437 516 €** au mois 5, soit 60 % de plus que ce qu'elle avait.

> **À retenir :** la LTV dit si tu as le droit de recruter, la trésorerie dit **combien**
> par mois. Deux décisions, et la seconde tue plus souvent —
> [E10](../modules/E10-cash-et-operations.md).

---

## 5. Les options

Le fondateur veut 1 800 nouveaux abonnés par mois : 172 800 € d'acquisition contre
148 474 € de contribution, impossible avec 234 615 € en banque. Quatre voies, chiffrées en
régime permanent à 1 000 nouveaux abonnés par mois et 60 000 € de fixes.

| Option | Description | CAC | LTV | LTV/CAC | Point bas trésorerie | Cumul > 0 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| **A** | Statu quo, mensuel seul | 96,00 € | 305,00 € | **3,18** | −515 385 € (M8) | M19 |
| **B** | Engagement 3 mois, payé mensuellement | 109,09 € | 305,00 € | **2,80** | −575 512 € (M8) | M20 |
| **C** | Prépaiement trimestriel obligatoire | 123,08 € | 388,33 € | **3,15** | −533 710 € (M9) | M18 |
| **D** | Les deux au choix, 35 % de trimestriels | 98,97 € | 334,17 € | **3,38** | −466 633 € (M8) | M18 |

**Option B — l'engagement de trois mois.** *Hypothèses :* −12 % de conversion
(CAC = 96,00 ÷ 0,88 = 109,09 €) ; trois mois pleins garantis, soit 3 × 24,40 = 73,20 € ;
76 % renouvellent au terme — moins que les 77,87 % survivants sans engagement (0,92³) : on
a retenu trois mois des gens qui voulaient partir. `LTV = 73,20 ÷ 0,24 = 305,00 €` :
**exactement la LTV du statu quo.** L'engagement n'a créé aucune valeur, il a déplacé du
cash et payé 13,6 % de CAC pour ce déplacement. **3,18 → 2,80. On jette.**

**Option C — le prépaiement trimestriel à 114,00 € TTC**, −9,5 % sur 3 × 42,00 €.

```
95,00 € HT (114,00 ÷ 1,20)
− 16,80 €  COGS (3 × 5,60)      −  2,30 €  PSP (114,00 × 1,8 % + 0,25)
−  4,40 €  logistique (1 colis)  −  1,60 €  SAV
= 69,90 € HT par trimestre, soit 23,30 € par mois
```

Contre 73,20 € pour trois mois de mensuel : **−3,30 €** — la remise coûte 10,00 € HT,
logistique (5,20 €), PSP (0,73 €) et SAV (0,77 €) en rendent 6,70. *Hypothèses :*
renouvellement trimestriel à 82 %, au-dessus des 77,87 % mécaniques parce que le
prépaiement supprime la décision mensuelle ; conversion −22 % (CAC = 96,00 ÷ 0,78 =
123,08 €). `LTV = 69,90 ÷ 0,18 = 388,33 €`, ratio 3,15 : **sous** le statu quo.

```
CAC d'indifférence = 388,33 ÷ 3,1771              = 122,23 €
Pénalité de conversion tolérable = 1 − (96,00 ÷ 122,23) = 21,5 %
```

**Au-delà de 21,5 % de perte de conversion, le prépaiement obligatoire détruit de la
valeur** — RITUEL est pile dessus. Et sa trésorerie est *pire* que le statu quo : l'avance
du trimestre (+45 500 € au mois 1 pour 1 000 abonnés) ne compense pas les 27 080 € de CAC
supplémentaire répétés chaque mois.

**Option D — l'offre au choix.** *Hypothèses :* deux options au tunnel coûtent 3 % de
conversion (CAC = 96,00 ÷ 0,97 = 98,97 €) ; 35 % prennent le trimestre.
`LTV = 0,65 × 305,00 + 0,35 × 388,33 = 334,17 €`, ratio **3,38**. L'encaissement du premier
mois passe à `0,65 × 24,40 + 0,35 × 69,90 = 40,33 €` : **le trou du jour un tombe de
71,60 € à 58,64 €, −18 %**, et le point bas à 466 633 € — **48 752 € libérés sans un euro
de capital.**

---

## 6. La décision et l'exécution

**Option D, accélération progressive à 1 800 nouveaux abonnés par mois, chantier
d'attrition.** Le CAC monte avec le volume (module 13 § 2.2) : 98,97 € à 1 000, 104,00 € à
1 800. Deux recrutements au mois 4 portent les fixes à 68 000 €. À partir du
mois 4, l'attrition passe de 8,0 % à 7,2 % — relance automatique sur échec de prélèvement,
et envoi de 60 jours dès le troisième mois, qui supprime un point de contact où l'on
résilie.

| Mois | Nouv. | % trim. | CAC | Base mens. | Base trim. | CA HT | Encaissé | Acquisition | **Cash net** | **Trésorerie** |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| M0 | 1 000 | 0 % | 96,00 € | 6 085 | 0 | 212 975 € | 148 474 € | −96 000 € | −7 526 € | **234 615 €** |
| M1 | 1 000 | 20 % | 98,97 € | 6 398 | 200 | 230 263 € | 170 091 € | −98 970 € | +11 121 € | **245 736 €** |
| M2 | 1 200 | 30 % | 99,80 € | 6 726 | 560 | 253 148 € | 189 282 € | −119 760 € | +9 522 € | **255 258 €** |
| M3 | 1 400 | 35 % | 101,20 € | 7 098 | 1 050 | 281 682 € | 207 443 € | −141 680 € | +5 763 € | **261 021 €** |
| M4 | 1 600 | 35 % | 102,60 € | 7 627 | 1 574 | 316 788 € | 236 706 € | −164 160 € | +4 546 € | **265 567 €** |
| M5 | 1 800 | 35 % | 104,00 € | 8 248 | 2 139 | 356 416 € | 265 919 € | −187 200 € | +10 719 € | **276 286 €** |
| M6 | 1 800 | 35 % | 104,00 € | 8 824 | 2 681 | 393 738 € | 287 428 € | −187 200 € | **+32 228 €** | **308 515 €** |

*Attrition : 8,0 % de M0 à M3, puis 7,2 %. Fixes : 60 000 € jusqu'à M3, 68 000 € ensuite.*

**La trésorerie ne descend jamais** : la base héritée de 6 085 abonnés produisait déjà
148 474 € de contribution mensuelle, donc elle finançait l'accélération. **La même décision
prise au mois 4 de la vie de la marque — base de 3 545 — creusait un point bas de 199 841 €
au mois 3, donc 200 000 € de capital extérieur.** Une décision d'acquisition n'est jamais
bonne dans l'absolu : elle est bonne **à une date**.

Attention à la colonne « CA HT » : l'abonné trimestriel encaisse 95,00 € HT d'un coup mais
n'en reconnaît que 31,67 € par mois. **Cash et compte de résultat divergent au mois 1 et se
recollent au mois 4.** Ne pilote jamais un abonnement prépayé sur le solde bancaire.

---

## 7. Les résultats

| Indicateur | M0 (avant) | M6 (après) | Écart |
| --- | ---: | ---: | ---: |
| Abonnés actifs | 6 085 | 11 505 | +89 % |
| CA TTC / semaine | 58 978 € TTC | 109 035 € TTC | +85 % |
| Marge de contribution (comptable) | 148 474 € | 277 773 € | +87 % |
| **EBITDA / mois** | **−7 526 €** | **+22 573 €** | **+30 099 €** |
| **EBITDA en % du CA HT** | **−3,53 %** | **+5,73 %** | **+9,26 pts** |
| CAC entièrement chargé | 96,00 € | 104,00 € | +8,3 % |
| Attrition mensuelle (plan mensuel) | 8,0 % | 7,2 % | −0,8 pt |
| LTV en contribution (mixte) | 305,00 € | 356,19 € | +16,8 % |
| **LTV / CAC** | **3,18** | **3,43** | **+0,25** |
| Payback nominal | 3,93 mois | 4,33 mois | +0,40 mois |
| **Trésorerie** | **234 615 €** | **308 515 €** | **+73 900 €** |

**Le CAC a monté de 8,3 % et c'est la bonne nouvelle :** un CAC plat quand le volume
augmente de 80 % signifierait que tu n'avais pas exploité ton canal. Le CAC marginal entre
M0 et M6 vaut `(187 200 − 96 000) ÷ (1 800 − 1 000) = 114,00 €` — encore sous les 122,23 €
d'indifférence, mais plus pour longtemps.

**Le payback s'est allongé de 0,40 mois pendant que la trésorerie gagnait 73 900 €.** La
contribution mixte tombe à `0,65 × 24,40 + 0,35 × 23,30 = 24,02 €` et le CAC monte, mais
l'abonné trimestriel paie trois mois d'avance. **Payback en mois et calendrier
d'encaissement sont deux objets différents :** le premier compare des modèles, le second
évite de mourir. Sans l'option trimestrielle, le mois 6 finissait à **262 084 €**, avec un
mois 3 en cash net négatif.

---

## 8. Ce qui aurait pu mal tourner

**L'attrition monte au lieu de baisser.** L'envoi de 60 jours est une modification produit.
S'il avait porté l'attrition à 9,5 % au lieu de 7,2 %, la LTV tombait à 256,84 € et le
ratio à **2,47** — un **T**, en pleine accélération à 1 800 par mois. On ne teste jamais
une modification de rétention et une hausse de volume le même mois. RITUEL l'a fait :
c'est le vrai reproche à lui adresser.

**Le mix trimestriel ne monte pas à 35 %.** À 15 % de prise, la LTV mixte tombe à 317,50 €
et le gain de cash du mois 1 est divisé par plus de deux : l'accélération aurait dû
s'arrêter à 1 400.

**Le CAC marginal casse.** À 114,00 €, il reste 8,23 € avant le seuil de 122,23 € : un
concurrent sur les mêmes audiences consomme cette marge en un trimestre.

**Le stock n'est pas dans le modèle.** Une rupture ne coûte pas une vente : elle coûte
l'abonné et sa LTV résiduelle. Deux mois de couverture sur 11 505 abonnés, c'est
`11 505 × 5,60 × 2 = 128 856 €` — 42 % de la trésorerie du mois 6, hors modèle.

**Les prélèvements échouent.** 2 à 4 % des cartes par mois ; la ligne SAV de 0,79 € les
provisionne au taux observé. Une hausse du taux de refus ajoute de l'attrition involontaire
— la moins chère à réparer, et celle qu'on ne regarde jamais.

---

## 9. Le mécanisme généralisable

> **Un CAC ne se juge jamais contre un panier. Il se juge contre deux choses, toujours les
> deux : une LTV en marge de contribution plafonnée à un horizon finançable, et une
> capacité de trésorerie chiffrée en euros et en mois.**

La première dit **si** tu as le droit de recruter, la seconde **combien** par mois. Un
LTV/CAC de 5,08 avec un point bas de 1 437 516 € et 900 000 € en banque est une faillite au
mois 2 ; un LTV/CAC de 3,18 avec un point bas de 466 633 € et une base qui finance déjà
l'effort est une accélération.

1. **L'attrition est au dénominateur de tout.** La diviser par deux double le CAC que tu
   peux payer : rendement proportionnel, pas additif —
   [E08](../modules/E08-retention-et-ltv.md).
2. **Un engagement contractuel ne crée pas de valeur : il déplace du cash et coûte de la
   conversion.** Chiffre son point d'indifférence avant de l'imposer — ici 21,5 %.
3. **Offrir le choix bat imposer.** L'option D prend l'avance de cash des 35 % qui
   l'acceptent sans payer la pénalité des 65 % qui la refusent.

**Et pour l'objectif à 1 M€ par semaine.** À 42,00 € TTC par mois, 4 333 333 € TTC mensuels
demandent **103 175 abonnés actifs**. À 8 % d'attrition, il faut en recruter **8 254 par
mois uniquement pour ne pas reculer** — **792 384 € HT d'acquisition avant le premier euro
de croissance** — et la machine d'acquisition immobilise en permanence
`8,254 × 158 752 = 1 310 339 €`. À 7,2 % d'attrition il n'en faut plus que 7 429, soit
713 184 € : ces **825 abonnés de moins à racheter chaque mois valent `825 × 96 × 12 =
950 400 €` par an**. C'est le mécanisme du passage de P5 à P5+ des [chiffres
canoniques](../donnees/chiffres-canoniques.md) § 8 —
[E01](../modules/E01-arithmetique-de-la-marque.md).

---

## 10. Questions

1. Le COGS passe de 5,60 € à 7,00 € HT et la logistique de 3,20 € à 3,90 € HT. Recalcule la
   contribution, la LTV à 8 % d'attrition, le LTV/CAC à 96,00 € et le seuil d'attrition
   pour tenir 3,00.
2. Un concurrent affiche un CAC de 62,00 € et une attrition de 14 %, à contribution
   identique. Qui a le meilleur modèle ? À horizon infini, puis à 24 mois, puis en payback.
3. Le fondateur veut passer directement à 3 000 nouveaux abonnés par mois, à 96,00 € de CAC
   et 8 % d'attrition. Cash immobilisé maximal de la machine d'acquisition seule, à quel
   mois, et quand le cumul redevient-il positif ?
4. À CAC constant de 96,00 €, à quelle attrition le ratio tombe-t-il à 2,00 ? Et à 10 %
   d'attrition, quel CAC maximal pour tenir 3,00 ?
5. Démontre le seuil de 21,5 % de pénalité de conversion du prépaiement trimestriel.
6. Une marque à 5 % d'attrition, 24,40 € de contribution et 96,00 € de CAC recrute 5 000
   abonnés par mois avec 900 000 € de trésorerie et 150 000 € de fixes. Son LTV/CAC ?
   Survit-elle ? Que changer, et de combien ?
7. **Décision.** Ton abonnement : 9,5 % d'attrition, 108,00 € de CAC, 24,40 € de
   contribution, 800 nouveaux abonnés par mois, 180 000 € de trésorerie. Tu accélères, tu
   tiens, ou tu arrêtes ? Justifie par deux calculs distincts.

---

## 11. Corrigé

**1.** `7,00 + 3,90 + 1,01 + 0,79 = 12,70 €`, donc `m = 35,00 − 12,70 = 22,30 € HT`
(63,71 % du CA HT contre 69,71 %). `LTV = 22,30 ÷ 0,08 = 278,75 €`, ratio
`278,75 ÷ 96,00 = 2,90` — code **T**. Seuil pour tenir 3,00 : `22,30 ÷ 288,00 = 7,74 %` ;
RITUEL est à 8,0 %, donc **2,10 € de coût variable en plus le font basculer du mauvais
côté.** Payback : `96,00 ÷ 22,30 = 4,31 mois`.

**2.** Concurrent : `24,40 ÷ 0,14 = 174,29 €`, ratio `174,29 ÷ 62,00 = 2,81` contre 3,18 :
**RITUEL gagne à horizon infini.** À 24 mois : concurrent
`24,40 × (1 − 0,86²⁴) ÷ 0,14 = 169,62 €` → **2,74** ; RITUEL
`24,40 × (1 − 0,92²⁴) ÷ 0,08 = 263,77 €` → **2,75**. **Égalité.** En payback :
`62,00 ÷ 24,40 = 2,54 mois` contre 3,93. Par tranche de 1 000 abonnés recrutés chaque mois,
son point bas est de 54 216 € contre 158 752 € : **à trésorerie égale il recrute 2,9 fois
plus.** À horizon finançable les deux modèles se valent ; le payback le plus court gagne.

**3.** Trajectoire linéaire en volume : `3 × 158 752 = 476 256 € au mois 4`, cumul positif
au **mois 9** — le calendrier ne dépend pas du volume, seule l'amplitude change. Avec les
fixes, le point bas dépasse **1,5 M€**. RITUEL a 234 615 € : **non finançable.**

**4.** Ratio 2,00 : `c = 24,40 ÷ (2 × 96,00) = 12,71 %`. À 10 % : `LTV = 244,00 €` et
`CAC max = 244,00 ÷ 3 = 81,33 €`, **15 % sous le CAC actuel.**

**5.** Le prépaiement doit produire au moins le ratio du statu quo :
`388,33 ÷ CAC = 3,1771` → `CAC d'indifférence = 122,23 €` ; `p` vérifie
`96,00 ÷ (1 − p) = 122,23` → `1 − p = 0,7854` → `p = 21,5 %`.

**6.** `LTV = 24,40 ÷ 0,05 = 488,00 €`, ratio `488,00 ÷ 96,00 = 5,08`.
Mois 1 : `5 000 × 24,40 − 5 000 × 96,00 − 150 000 = −508 000 €` → trésorerie 392 000 €.
Mois 2 : base `5 000 × 0,95 + 5 000 = 9 750`, net `237 900 − 480 000 − 150 000 = −392 100 €`
→ trésorerie **−100 €**. **Elle meurt fin du mois 2**, alors que son EBITDA devient positif
au mois 6 et son cumul au mois 12. Point bas : **1 437 516 € au mois 5.** Deux correctifs :
lever 540 000 € de plus, ou ramener le recrutement à
`900 000 ÷ 1 437 516 × 5 000 ≈ 3 130 par mois` — le second ne coûte rien et donne la même
entreprise six mois plus tard.

**7.** *Calcul 1 — la valeur.* `LTV = 24,40 ÷ 0,095 = 256,84 €`, ratio
`256,84 ÷ 108,00 = 2,38` → code **T** ; plafonnée à 12 mois,
`24,40 × (1 − 0,905¹²) ÷ 0,095 = 179,32 €` → **1,66**, sous le seuil de 2,0.
*Calcul 2 — le cash.* Machine d'acquisition seule à 800 abonnés par mois : point bas
**−173 744 € au mois 5** contre 180 000 € de trésorerie. Il reste **6 256 €**, avant le
premier euro de frais fixes.
**Verdict : tu tiens, tu n'accélères pas, tu attaques l'attrition.** Ramener 9,5 % à 7,5 %
porte la LTV à 325,33 € et le ratio à 3,01 : la même accélération devient légitime sans un
euro de capital. **La condition pour qu'« accélérer » soit la bonne réponse :** un CAC
ramené à 85,00 € *et* une trésorerie supérieure à 260 000 €. Les deux, pas l'un des deux.

---

*Fin du cas C05. Suite : [C06 — le test d'incrémentalité](C06-test-incrementalite.md).*
