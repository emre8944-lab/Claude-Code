# Module E10 — Le cash, le stock et les opérations

> **Prérequis :** [E01](E01-arithmetique-de-la-marque.md), [E03](E03-offre-et-prix.md), [E06](E06-acquisition-payante.md), [E08](E08-retention-et-ltv.md).
> **Objet :** calculer ce que ta croissance consomme en trésorerie, quel capital il faut pour aller de zéro à 1 M€ de CA par semaine, et comment le stock, la logistique, le SAV et les fournisseurs déplacent ce chiffre.
> **Temps de travail :** ~6 h (lecture + exercices)

---

## 0. Pourquoi ce module existe

Ouvre les [chiffres canoniques](../donnees/chiffres-canoniques.md) au § 4. Le besoin en fonds de roulement de NØRA passe de **21 603 €** au palier P1 à **2 264 655 €** au palier P5. L'EBITDA, lui, passe de −9 403 € à +364 752 € par mois (§ 2.2). Ces deux trajectoires ne racontent pas la même histoire, et c'est la première qui décide de ta survie.

Une marque rentable meurt quand l'argent qu'elle doit avancer croît plus vite que celui qu'elle dégage. À P4, NØRA gagne 198 572 € par mois ; si elle croît de 20 % par mois, son BFR de 1 392 510 € augmente de 278 502 € dans le même mois.

```
Trésorerie générée     = +198 572 €
Trésorerie immobilisée = −278 502 €  (20 % × 1 392 510 €)
                         ───────────
Flux réel              =  −79 930 € par mois
```

L'entreprise affiche 8,1 % d'EBITDA (§ 2.2), elle est saine sur tous les tableaux, et perd 79 930 € par mois — 129 573 € avec l'impôt. **L'EBITDA n'est pas du cash. Le tableau du § 4 est le tableau qui tue.**

Ce module donne trois nombres : ce que ta croissance coûte en cash, celle que tu peux financer toi-même, et le capital nécessaire pour atteindre P5. Le troisième vaut ≈ 2,36 M€, et le moment le plus dangereux n'est pas le départ.

---

## 1. Le cycle de conversion du cash

### 1.1 Les quatre délais

Le **cycle de conversion du cash** est le nombre de jours entre le moment où tu paies et celui où tu es payé. Trois délais classiques — le **DIO** (*days inventory outstanding*), jours en stock avant la vente, en jours de COGS (coût d'achat des marchandises vendues) ; le **DSO** (*days sales outstanding*), délai de reversement de ton prestataire de paiement (PSP) ; le **DPO** (*days payables outstanding*), crédit fournisseur. Plus un quatrième que le commerce en ligne a inventé : **l'avance publicitaire**, dépense média engagée dont le CA n'est pas encaissé, absente des manuels, et qui pèse **1 045 944 €** à P5 (§ 4).

### 1.2 Ce que le § 4 dit vraiment

Le tableau canonique donne des euros ; convertis-les en jours et le mécanisme apparaît. Convention : mois de 30 jours.

```
DIO = Stock ÷ (COGS ÷ 30)          DPO = Dettes fourn. ÷ (COGS ÷ 30)
DSO = Encaissements ÷ (CA TTC ÷ 30) Pub = Avance pub ÷ (dép. pub ÷ 30)
COGS mensuel P5 = 14,5 % × 3 610 997 € = 523 595 €  (§ 2.1 et § 2.2)
DIO P5 = 1 832 581 ÷ (523 595 ÷ 30)    = 105,0 jours
```

| Palier | DIO (j de COGS) | DSO (j de CA) | Avance pub (j de dép.) | DPO (j de COGS) |
| --- | ---: | ---: | ---: | ---: |
| P1 | 75 | 4 | 2 | 0 |
| P2 | 70 | 4 | 3 | 15 |
| P3 | 80 | 3 | 7 | 30 |
| P4 | 95 | 3 | 14 | 45 |
| **P5** | **105** | **3** | **21** | **60** |

Le modèle est régulier : le DPO gagne 15 jours par palier, le DSO passe de 4 à 3 quand tu négocies ton PSP, et le DIO se dégrade parce que sept marchés (§ 2) exigent du stock avancé dans plusieurs entrepôts.
 Sur la ligne du temps : réception et facture fournisseur à J−105, paiement à J−45, dépense publicitaire à J−21, commande client à J 0, versement du PSP à J+3. Ton argent est sorti 48 jours pour la marchandise et 24 pour la publicité ; le BFR est la somme des deux avances.

### 1.3 Pourquoi le BFR vaut entre 12 et 18 jours de CA

Ramène chaque poste en jours de **CA TTC**, base de la dernière colonne du § 4 (CA TTC quotidien P5 : 4 333 196 ÷ 30 = 144 440 €).

| Palier | Stock | + Encaissements | + Avance pub | − Dettes fourn. | **BFR en j de CA** |
| --- | ---: | ---: | ---: | ---: | ---: |
| P1 | 12,50 | 4,00 | 1,11 | 0,00 | **17,61 → 18 j** |
| P2 | 10,50 | 4,00 | 1,36 | 2,25 | **13,61 → 14 j** |
| P3 | 10,67 | 3,00 | 2,59 | 4,00 | **12,26 → 12 j** |
| P4 | 11,88 | 3,00 | 5,00 | 5,63 | **14,25 → 14 j** |
| P5 | 12,69 | 3,00 | 7,24 | 7,25 | **15,68 → 16 j** |

Vérification P5 : 15,68 × 144 440 = 2 264 800 € contre 2 264 655 € au canonique, l'écart venant des arrondis. La courbe descend de P1 à P3 — tu passes de 0 à 30 jours de crédit fournisseur — puis remonte, et la remontée est le vrai enseignement. Décompose P3 → P5, en jours de CA TTC : stock +2,02 ; encaissements 0,00 ; publicité +4,65 ; dettes fournisseurs −3,25 (un gain) — total +3,42, et 12,26 j deviennent 15,68 j.

**Ce qui dégrade ton cycle à l'échelle, ce n'est pas le stock. C'est la publicité.** Tu as arraché 3,25 jours à tes fournisseurs et reperdu 4,65 chez tes régies — 671 556 € de plus qu'au rythme de P3. La cause est mécanique : à P1 le client achète en 48 heures ; à P5, avec 55 % du budget en prospection large et 8 % en influence (§ 5), la fenêtre passe à 21 jours. **Plus tu fais de marque, plus ton cycle de cash s'allonge** — le prix rarement chiffré de [E12](E12-marque-et-actif.md).

C'est négociable : une ligne de crédit régie à 30 jours transformerait à P5 un emploi de 1 045 944 € en ressource de 1 494 206 € — au prix d'un créancier qui peut couper ton trafic ([C10](../etudes-de-cas/C10-compte-publicitaire-banni.md)).

> **À retenir :** ton BFR n'est pas une fatalité comptable, c'est la somme de quatre délais. Trois se négocient avec des humains — fournisseur, PSP, régie ; le quatrième, le stock, avec ta propre discipline de commande.

---

## 2. Le calcul central : ce que coûte un euro de croissance

### 2.1 Le cash immobilisé par tranche de 100 000 €

L'intensité en cash vaut `BFR ÷ CA TTC mensuel × 100 000 €` : 2 264 655 ÷ 4 333 196 × 100 000 = **52 263 €** à P5 ; 481 053 ÷ 1 177 200 × 100 000 = **40 864 €** à P3.

| Palier | Cash par +100 k€ de CA/mois | EBITDA mensuel | Croissance autofinançable |
| --- | ---: | ---: | ---: |
| P1 | 58 704 € | −9 403 € | négative |
| P2 | 45 379 € | −19 838 € | négative |
| P3 | 40 864 € | 51 033 € | 124 886 € de CA |
| P4 | 47 500 € | 198 572 € | 418 046 € de CA |
| P5 | 52 263 € | 364 752 € | 697 917 € de CA |

L'intensité descend jusqu'à P3 puis remonte, pour la raison du § 1.3. **Ta croissance devient plus chère en cash à mesure que tu grandis** — l'inverse de l'intuition d'économie d'échelle.

### 2.2 La formule à retenir par cœur

```
Croissance autofinançable = EBITDA mensuel ÷ intensité × 100 000 €
P5 : 364 752 ÷ 52 263 × 100 000 = 697 917 € de CA TTC mensuel
Taux : 697 917 ÷ 4 333 196 = 16,11 % par mois

Ce qui se simplifie en  g = EBITDA mensuel ÷ BFR
  P3 :  51 033 ÷   481 053 = 10,61 %
  P4 : 198 572 ÷ 1 392 510 = 14,26 %
  P5 : 364 752 ÷ 2 264 655 = 16,11 %
```

**Ta croissance mensuelle autofinançable est ton EBITDA mensuel divisé par ton BFR. Deux nombres, une division.** À P5, 1,1611¹² = **×6,0 par an** — si la publicité absorbe la dépense au même CAC, ce qu'elle ne fait pas ([E01](E01-arithmetique-de-la-marque.md) § 5).

L'EBITDA canonique est **avant impôt et avant investissement** : à 25 % d'impôt sur les sociétés (règle publique), l'EBITDA P5 disponible tombe à 273 564 € et le taux à **12,08 %** par mois, soit ×4,0 par an.

### 2.3 Le point le plus important du module

Aux paliers P1 et P2, l'EBITDA est **négatif** : aucun euro interne à réinvestir, chaque euro de BFR vient de l'extérieur, **et** il faut financer la perte courante.

```
P2, +100 000 € de CA TTC mensuel :
  cash immobilisé, une fois       = 45 379 €
  CA HT supplémentaire            = 100 000 ÷ 1,2      = 83 333 €
  CM3 marginale = 8 162 ÷ 191 833 = 4,25 % du CA HT
  contribution gagnée             = 83 333 × 4,25 %    =  3 542 €/mois
  récupération du BFR             = 45 379 ÷ 3 542     = 12,8 mois
P1, même tranche : CM3 = −2 903 ÷ 30 667 = −9,47 % du CA HT
  → 58 704 € immobilisés ET −7 892 € de CM3 par mois
```

**Aux paliers P1 et P2, la croissance est intégralement financée par l'extérieur.** Ce n'est pas une anomalie : NØRA est volontairement sous son MER d'équilibre EBITDA (§ 2.3, écart de −46,0 % et −19,0 %) pour constituer une base qui rembourse en réachat ([E08](E08-retention-et-ltv.md), [C02](../etudes-de-cas/C02-vallee-de-la-mort.md)) — un pari financé, mais il faut avoir l'argent.

Et **toute croissance au-dessus de EBITDA ÷ BFR est un appel de fonds mensuel** : viser +25 %/mois à P4 demande 348 128 € de BFR contre 198 572 € d'EBITDA, soit 149 556 € de trou dès le premier mois ([C04](../etudes-de-cas/C04-scale-qui-detruit-la-marge.md)).

---

## 3. Le capital pour aller de zéro à P5

*Hypothèses : chaque palier tourne à son régime canonique toute sa durée (§ 2), le BFR est constitué au premier mois du palier.*

### 3.1 Les trois briques

**Pertes cumulées de P1 et P2** (§ 2.2) : 3 × 9 403 = 28 209 € sur M1-M3, 6 × 19 838 = 119 028 € sur M4-M9, soit **147 237 €**.

**Constitution du BFR** (§ 4) : 21 603 € en P1, +82 859 € (P2), +376 591 € (P3), +911 457 € (P4), +872 145 € (P5) — cumul **2 264 655 €**.

**Réserve.** *Hypothèse déclarée : 2 mois de frais fixes du palier + 1 mois de COGS* — deux mois pour réagir à un choc, un mois de COGS pour passer la commande fournisseur suivante même si les ventes s'arrêtent. Soit **19 133 €** en P1 (13 000 + 6 133), **90 530 €** en P2, **366 960 €** en P3, **826 450 €** en P4, **1 243 595 €** en P5.

### 3.2 La trajectoire de trésorerie

```
M1  entrée P1  − BFR 21 603     X −    21 603
M1→M3          − 3 × 9 403      X −    49 812
M4  entrée P2  − BFR 82 859     X −   132 671
M4→M9          − 6 × 19 838     X −   251 699
M10 entrée P3  − BFR 376 591    X −   628 290
M10→M18        + 9 × 51 033     X −   168 993
M19 entrée P4  − BFR 911 457    X − 1 080 450  ← plus bas
M19→M30        + 12 × 198 572   X + 1 302 414
M31 entrée P5  − BFR 872 145    X +   430 269
M31→M40        + 10 × 364 752   X + 4 077 789
```

Le point le plus bas n'est pas au démarrage : il est au **mois 19**, à l'ouverture des quatre marchés. Il faut y couvrir le creux **et** la réserve du palier — 1 080 450 + 826 450 = **1 906 900 €**. Les autres points exigent moins : 995 250 € à M10, 342 229 € à M9, 813 326 € à M31.

### 3.3 Le total et l'échéancier

Ajoute ce que le § 4 ne modélise pas. Les 147 237 € de pertes P1-P2 forment un déficit reportable qui absorbe les 2,9 premiers mois de bénéfice P3 ; le solde est imposé à 25 %, soit ≈ 78 000 € avant M19. *Hypothèse : 380 000 € d'investissement cumulé sur M1-M40 (site, ERP et WMS, moules, marque, aménagement), dont 250 000 € avant M19.*

| Tranche | À réunir avant | Besoin cumulé | Tranche | Ce qu'elle finance |
| --- | --- | ---: | ---: | --- |
| 1 | M1 | 128 945 € | **128 945 €** | BFR P1, 3 mois de perte, réserve P1, site, premier lot |
| 2 | M4 | 442 229 € | **313 284 €** | saut de BFR P2, 6 mois de perte, réserve P2 |
| 3 | M10 | 1 245 250 € | **803 021 €** | saut de BFR P3, réserve P3, ERP |
| 4 | M19 | 2 364 900 € | **1 119 650 €** | saut de BFR P4, réserve P4, impôt |
| — | M31 | — | **0 €** | P5 autofinancé par l'EBITDA de P4 |

**Aller de zéro à 1 M€ de CA par semaine demande environ 2,36 M€, dont 47 % appelés au mois 19.** Presque tout le monde budgète la tranche 1 et découvre la tranche 4 six semaines avant.

### 3.4 La forme de la courbe vaut un million

Refais le § 3.2 en constituant le BFR marché par marché : le creux tombe à −251 699 € au M9, la contrainte reste M19 — la réserve exigée passe à celle de P4 quand la trésorerie est à −46 372 € — et le capital minimum vaut **872 822 €** contre 1 906 900 €. Même destination, même compte de résultat, même BFR d'arrivée, même durée : **1 034 078 € d'écart, produits par la seule forme de la courbe.** C'est la raison financière d'ouvrir les marchés en séquence ([E11](E11-passage-a-echelle.md)).

---

## 4. Les sources de financement, comparées honnêtement

### 4.1 Pourquoi « 8 % sur 6 mois » n'est pas 8 % par an

L'arnaque de présentation la plus répandue du secteur. On te propose 100 000 €, commission 8 %, remboursés en 6 mensualités de 18 000 €.

```
Capital restant dû, début de mois : 100 000 / 83 333 / 66 667 /
  50 000 / 33 333 / 16 667           → moyenne 58 333 €
Taux simple = 8 000 ÷ (58 333 × 0,5) = 27,43 % par an
Actuariel : r tel que 100 000 = 18 000 × [1 − (1+r)⁻⁶] ÷ r
  annuité = 100 000 ÷ 18 000 = 5,5556 → r = 2,244 %/mois
  taux effectif = 1,02244¹² − 1       = 30,5 % par an
```

**8 % sur 6 mois, c'est 30,5 % par an.** Formule à connaître : un forfait de *p* % remboursé linéairement sur *n* mois coûte environ `p × 24 ÷ (n + 1)` en taux annuel simple — ici 27,4 %.

### 4.2 Les sept sources

Coût annuel pour porter les 911 650 € de la tranche 4 sur douze mois. *Taux de marché : hypothèses d'ordre de grandeur, à revérifier avant d'emprunter.*

| Source | Coût annuel | Sur 911 650 € | Dilution | Contrainte imposée | Palier utile |
| --- | ---: | ---: | ---: | --- | --- |
| Autofinancement | 0 % | 0 € | 0 % | Croissance plafonnée à EBITDA ÷ BFR | P3+ |
| Prêt bancaire | ~6 % | 54 699 € | 0 % | Caution perso., 2 bilans, covenants | P3+ |
| Financement de stock | ~11 % | 100 282 € | 0 % | Gage sur marchandise, audit | P2–P4 |
| Affacturage | ~1,5 % des factures | sans objet en DTC | 0 % | Exige des créances B2B | P4+ si B2B |
| Avance sur revenus | **30,5 %** (§ 4.1) | 278 053 € | 0 % | Prélèvement quotidien sur encaissements | P2–P4 |
| Obligataire / venture debt | ~12 % + BSA | 109 398 € + 5 à 15 % de BSA | indirecte | Covenants ; rupture = exigibilité | P4–P5 |
| Capital-risque | 0 € de cash | 0 € | 15 à 25 % | Gouvernance, sortie imposée | P3–P4 |

**L'affacturage est un faux ami en DTC** : ton DSO est de 3 jours (§ 1.2), il n'y a rien à affacturer — racheter les 433 320 € d'encaissements à 1,5 % des factures coûterait 65 000 € par mois. Il gagne sa place le jour où tu ouvres un canal grossiste à 60 jours : 20 % du CA de P5 en B2B produirait 1 733 278 € de créances.

Compare toujours au capital. *Hypothèse : cette taille de marque se valorise vers 6 × l'EBITDA.* L'EBITDA annuel de P5+ vaut 8 805 583 € (§ 8), soit 52 833 498 € : céder 20 % coûte **10 566 700 €**, contre 1 744 814 € pour porter les 1 906 900 € du § 3.2 en avance sur revenus à 30,5 % pendant trois ans. **Le capital-risque coûte six fois plus cher que la dette la plus chère** — mais il ne se rembourse pas et n'exige rien quand l'année est mauvaise. Tu paies cette assurance six fois son prix : rationnel si ta probabilité de ruine est élevée ([E13](E13-risque-de-ruine.md)), massacre sinon.

---

## 5. Le stock

### 5.1 Le point de recommande

```
Point de recommande = consommation quotidienne × délai + sécurité
Stock de sécurité   = Z × σ(demande sur le délai)
```

*Hypothèses NØRA à P5 : le Sérum Densité fait 45 % du COGS et du CA ; délai de 75 jours (7 j de passation, 35 j de fabrication, 28 j de transport et dédouanement, 5 j de réception) ; service 97,5 %, soit Z = 1,96.*

```
COGS mensuel du héros = 45 % × 523 595 € = 235 618 €
Unités par mois       = 235 618 ÷ 4,80 € = 49 087  (COGS unit., § 1)
Consommation par jour = 49 087 ÷ 30      = 1 636 unités
Demande sur le délai  = 1 636 × 75       = 122 700 unités
Manuel, σ quotidien 18 % : 0,18 × 1 636 = 294
  → 1,96 × 294 × √75 = 4 999 u = 3,1 j de sécurité
```

Trois jours de sécurité pour un délai de 75 jours. L'absurdité vient de l'hypothèse cachée : la racine carrée suppose les écarts quotidiens **indépendants**. En DTC ils ne le sont pas — une publicité qui gagne, une rupture concurrente, le Black Friday sont des décalages de niveau qui durent des semaines. **Mesure ton σ sur la fenêtre du délai, jamais sur la journée.**

```
Hyp. : σ sur fenêtres glissantes de 75 j = 25 % de la demande moyenne
  σ = 0,25 × 122 700 = 30 675 → 1,96 × 30 675 = 60 123 u = 36,8 j
  Point de recommande = 122 700 + 60 123 = 182 823 u = 877 550 € de COGS
```

Douze fois le manuel. Cohérence avec le canonique : le stock du héros vaut 45 % × 1 832 581 = 824 661 €, soit 171 804 unités, soit 105,0 jours — le DIO du § 1.2, décomposé en 28,0 j de transit, 36,8 j de sécurité, 40,2 j de stock de travail : une commande tous les **80,4 jours**.

### 5.2 Rupture contre surstock, chiffré

**Une rupture de 10 jours sur le héros.** CA TTC quotidien : 45 % × 144 440 = 64 998 €, soit 54 165 € HT ; marge brute à 61,5 % (§ 2.1) = 33 311 €/jour ; pub attribuable 22 413 €/jour.

```
A — pub maintenue (dépensée dans les deux cas)
  marge brute non réalisée : 10 × 33 311    = 333 110 €
B — pub coupée
  CM3 non réalisée : 10 × (33 311 − 22 413) = 108 980 €
  réapprentissage, hyp. +25 % de CAC sur 14 j : 22 413 × 14
  = 313 782 € ÷ 40,03 € = 7 839 clients, −20 % = 1 568 perdus
  × 86,75 € (LTV 12 mois, § 3)              = 136 024 €
                                              = 245 004 €
```

**Une rupture de dix jours sur ton héros coûte entre 245 004 € et 333 110 €**, et couper la publicité est le moins mauvais choix, de 88 106 €. Le stock de sécurité qui l'aurait évitée immobilise 288 590 €, financés à 11 % pour 31 745 € par an : il se rembourse dès que la probabilité annuelle d'une telle rupture dépasse **13 %**.

**Un surstock de 60 jours sur le héros** — 98 160 unités, 471 168 € immobilisés :

```
Portage à 11 %                                   =  51 828 €/an
Obsolescence, hyp. 8 % démarqués à −40 % :
  7 853 u × 32,50 € HT × 40 %                    = 102 089 €
Croissance non financée : 471 168 ÷ 52 263 × 100 000 = 901 532 € de
  CA TTC/mois × 20,07 % de CM3 marginale         = 150 781 €/mois
```

Les deux premières lignes sont fermes ; la troisième est un plafond, atteint seulement quand le capital est ta contrainte active — de P2 à P4 ([E01](E01-arithmetique-de-la-marque.md) § 5).

### 5.3 Ta prévision est fausse, et ça n'a pas d'importance

Aucune marque en croissance ne prévoit correctement sa demande par référence à 155 jours (75 de délai + 80 de cycle). *Hypothèse : l'erreur absolue moyenne par SKU à cet horizon vaut 25 à 35 %.* Aucun modèle ne réglera ça ; tu le rends inoffensif en **réduisant l'horizon sur lequel tu t'engages**.

```
Cycle 80,4 j : 28,0 + 36,8 + 40,2 = 105,0 j de stock
Cycle 30 j   : 28,0 + 36,8 + 15,0 =  79,8 j
Cash libéré, héros : 25,2 j × 1 636 u × 4,80 € = 197 890 €
Gamme entière      : 197 890 ÷ 0,45            = 439 756 €
  → finance 439 756 ÷ 52 263 × 100 000 = 841 435 € de CA/mois
Coût : hyp. 2 400 €/expédition × 7,5 de plus   =  18 000 €/an
```

Ce n'est même pas un arbitrage. Trois leviers, dans cet ordre :

1. **Commander plus souvent.** Le seul frein est le MOQ (quantité minimale de commande) : un cycle de 30 jours exige un MOQ ≤ 49 087 unités sur le héros. **Le MOQ que tu négocies vaut 439 756 € de trésorerie** — arrive avec ce chiffre.
2. **Un fournisseur plus réactif.** Passer de 75 à 50 jours ramène la demande sur le délai à 81 800 unités et la sécurité à 49 080 : 249 326 € de cash sur le seul héros.
3. **Réserver de la capacité sans engager le mix.** Bloque des créneaux et des matières, décide les références au dernier moment.

---

## 6. La logistique, les retours et le SAV

### 6.1 Retrouver les 11,0 % du canonique

```
Coût logistique mensuel = 11,0 % × 3 610 997 € HT = 397 210 €  (§ 2.1)
Coût par commande       = 397 210 ÷ 60 200        = 6,60 € HT  (§ 2)
```

*Décomposition, hypothèse déclarée cohérente avec ce total :* réception 0,25 € ; stockage 0,35 € ; préparation 0,90 € ; emballage 0,95 € ; transport sur sept pays 3,60 € ; retours amortis sur toutes les commandes 0,55 €. **Total 6,60 €**, dont 54,5 % de transport.

Le même calcul aux cinq paliers donne le résultat le plus contre-intuitif du module.

```
Taux × AOV HT = coût par commande
  P1 16,0 % × 38,33 € = 6,13 €   P4 11,5 % × 58,17 € = 6,69 €
  P2 14,0 % × 47,96 € = 6,71 €   P5 11,0 % × 59,98 € = 6,60 €
  P3 12,0 % × 54,50 € = 6,54 €
Le coût unitaire ne baisse pas quand le volume est multiplié par 75.
À coût unitaire de P1 sur l'AOV de P5 : 6,13 ÷ 59,98 = 10,22 % du CA HT
contre 11,0 % au canonique → panier moyen −5,78 pts, inflation +0,78 pt
```

**Les cinq points gagnés sur ta ligne logistique ne viennent pas de ta négociation avec le 3PL. Ils viennent du panier moyen**, qui passe de 38,33 € à 59,98 € HT (+56,5 %). La négociation a rendu −0,78 point : un colis international plus lourd coûte plus cher qu'un colis français léger. Travaille l'offre ([E03](E03-offre-et-prix.md)), pas l'appel d'offres.

### 6.2 Internaliser ou rester en 3PL

*Hypothèses : 3PL à 6,60 €/commande sans coût fixe. En interne — entrepôt 8 000 €/mois, WMS et matériel amortis 2 500 €, un responsable 4 200 € ; un opérateur à 4 000 €/mois chargé prépare 420 commandes/jour sur 21 jours ouvrés ; emballage et transport identiques au 3PL, 4,55 €/commande.*

```
Main-d'œuvre/commande = 4 000 ÷ (420 × 21)      = 0,45 €
Coût interne = 14 700 € + N × 5,00 €   3PL = N × 6,60 €
Seuil : 14 700 = N × 1,60 → N = 9 188 cmd/mois ≈ 306/jour
```

NØRA franchit ce seuil entre P2 (4 000 commandes/mois) et P3 (18 000). **Et à P3 il ne faut pas internaliser** : le 3PL absorbe un pic de Black Friday à ×3,5 au coût marginal, ton entrepôt non ; sept marchés exigent plusieurs points de départ ; et ton goulot à P3 est la production de 654 créations par mois (§ 6). Règle utilisable : **internalise quand le gain dépasse deux fois les frais fixes engagés**, soit N > 18 375 commandes/mois.

### 6.3 Le délai de livraison est une ligne de compte de résultat

*Hypothèse : chaque jour de délai annoncé en plus coûte ~1,5 % relatif de conversion.* Un transporteur moins cher, un jour de plus, 0,45 € de moins par colis : l'économie vaut 0,45 × 60 200 = **325 080 €/an** ; la perte vaut 1,5 % × 3 610 997 € HT × 61,5 % de marge brute = **399 732 €/an**, intégralement en CM3 puisque la publicité ne bouge pas. **Solde : −74 652 € par an.** Et *hypothèse, chaque jour de retard ajoute 0,4 point au taux de tickets « où est ma commande »* : 241 tickets de plus par mois.

### 6.4 Les retours

Le poste canonique « Retours/SAV » vaut 3,5 % du CA HT à P4 et P5 (§ 2.1). **Ce n'est pas un taux de retour, c'est une ligne de coût.** *Hypothèse : le taux de retour de NØRA est de 3,5 % des commandes.* Il est bas parce que la catégorie l'est : un consommable à 39 € ne se retourne pas comme un vêtement, où acheter trois tailles pour en garder une est normal.

Coût complet d'une commande retournée à P5 : COGS détruit (cosmétique ouvert) 14,5 % × 59,98 = **8,70 €** ; logistique aller **6,60 €** ; transport retour **4,50 €** ; réception, contrôle, destruction **1,80 €** ; frais PSP non restitués 1,55 % × 71,98 € TTC = **1,12 €** ; ticket SAV **2,20 €**. **Total 24,92 €.**

```
Retours = 3,5 % × 60 200 = 2 107 × 24,92 € = 52 507 €/mois, 1,45 % du CA HT
Reste pour le SAV pur : 126 385 − 52 507   = 73 878 €/mois, 2,05 % du CA HT

Passer de 14 à 60 j de rétractation, retour gratuit — hyp. +1,2 % relatif
de conversion, +0,9 pt de retour :
  gain  1,2 % × 3 610 997 € HT × 61,5 %    = 26 649 €/mois
  coût  0,9 % × 60 200 = 542 × 24,92 €     = 13 507 €/mois
  solde                        +13 142 €/mois, soit +157 704 €/an
  bascule à +1,78 pt de retour (26 649 ÷ 24,92 ÷ 60 200)
```

**La politique de retour est un arbitrage chiffrable :** avec 3 points de retour en plus, le solde devient −18 291 € par mois. **Mesure le point de bascule avant de généraliser.**

Les retours frauduleux — colis vide, produit substitué, article usé — coûtent le prix plein plus le remboursement (*hyp. 0,4 % des commandes*). Traitement : pesée à l'expédition et au retour, photo horodatée, score par client déclenchant un contrôle manuel au-delà de trois retours par an. **Ne bloque jamais sur un seul incident** : un client vaut 138,11 € à 36 mois (§ 3), et un faux positif détruit dix fois la fraude évitée.

### 6.5 Dimensionner le SAV

*Hypothèses : 0,22 ticket par commande tous canaux confondus ; 6,5 minutes de traitement moyen ; 7 heures utiles par jour, 21 jours, 78 % d'occupation.*

```
Tickets/mois       = 60 200 × 0,22     = 13 244
Charge             = 13 244 × 6,5 min  = 1 434,8 h
Capacité par agent = 7 h × 21 j × 78 % = 114,7 h
ETP nécessaires    = 1 434,8 ÷ 114,7   = 12,5 ETP
Contrôle contre le budget du § 6.4 (73 878 €/mois) : 12,5 agents
× 3 400 € + 2 responsables × 4 800 € + 2 800 € d'outillage
+ 0,25 €/commande de gestes = 69 950 €
```

Piège de lecture : le § 2.5 donne **38 ETP** à P5 pour 360 000 € de frais fixes, soit 9 474 € par ETP et par mois — un coût de siège, pas d'agent. Les 12,5 ETP de SAV **n'y sont pas** : ils sont dans la ligne variable « Retours/SAV » du § 2.1. Comptés deux fois, la productivité de 1 140 315 € par ETP tombe à 858 000 € et tu crois ta structure trop lourde.

*Hypothèse : 45 % des tickets sont des « où est ma commande » (WISMO), dont 60 % disparaissent avec une page de suivi et des notifications proactives.* Soit 13 244 × 45 % × 60 % = **3 576 tickets évités par mois**, 387,4 heures, 3,38 ETP, **137 904 € par an**.

Le SAV est aussi la seule information produit gratuite, datée et non biaisée que tu possèdes : impose une **taxonomie de motifs à deux niveaux** à la clôture de chaque ticket, et une revue mensuelle. Un motif qui monte de 1,5 % à 4 % en deux mois annonce un défaut de lot, une promesse publicitaire mal calibrée ([E05](E05-machine-creative.md)) ou une page produit qui ment ([E07](E07-funnel-et-conversion.md)) — six semaines avant les retours.

---

## 7. Les fournisseurs et la TVA

### 7.1 Trente jours de délai valent plus que 2 % de remise

```
Soit C le COGS mensuel et k ton coût du capital annuel.
30 jours de délai libèrent      C  de trésorerie, en permanence.
2 % de remise rapportent 0,02 × C  par mois, soit 0,24 × C par an.
Égalité quand C × k = 0,24 × C,  soit  k = 24 %
Généralisation, n jours contre p % :  k seuil = 360 × p ÷ n
  60 j / 3 % → 18 %   45 j / 2 % → 16 %   30 j / 1 % → 12 %
```

Le seuil de 24 % ne dépend ni du volume, ni du palier, ni du produit. Applique-le à P5, COGS mensuel 523 595 € :

| Ton financement marginal | Coût k | 30 j de délai valent | 2 % de remise valent | Choix |
| --- | ---: | ---: | ---: | --- |
| Avance sur revenus (§ 4.1) | 30,5 % | 159 696 €/an | 125 663 €/an | **le délai** |
| Financement de stock | 11,0 % | 57 595 €/an | 125 663 €/an | **la remise** |
| Prêt bancaire | 6,0 % | 31 416 €/an | 125 663 €/an | **la remise** |
| Capital rationné (P2–P4) | > 100 % | croissance non finançable | 125 663 €/an | **le délai** |

**Il n'y a pas de bonne réponse universelle : il y a ton coût du capital.** De P2 à P4, où la contrainte est la trésorerie, prends les jours ; à P5+, avec une banque et un EBITDA prévisible, prends le prix. NØRA gagne 15 jours de DPO par palier (§ 4) : le passage de P4 à P5 libère **261 798 €**.

### 7.2 Prix, double source, qualité, dépendance

La remise volume ne se demande pas, elle se construit : engage-toi sur un volume **annuel** avec des appels trimestriels, jamais sur une grosse commande — tu obtiens le prix du palier supérieur sans en payer le stock.

```
Double source — hyp. : un second fournisseur qualifié prend 30 % du volume
à +6 % de COGS.
  Prime annuelle   = 30 % × 523 595 € × 6 % × 12  =   113 097 €/an
  Sinistre couvert = 60 j de rupture = 2 × CM3    = 1 449 504 €
  Probabilité d'équilibre = 113 097 ÷ 1 449 504   = 7,8 % par an
```

**Si tu estimes à plus de 7,8 % par an la probabilité qu'un fournisseur unique te laisse deux mois en rupture, double-source.** Sur un site unique, dans un seul pays, produit réglementé, ligne de production unique, elle est très au-dessus.

Deux garde-fous. **L'audit qualité** : contrôle par lot, contre-échantillon conservé, droit d'auditer sur site — un lot défectueux à P5, c'est 60 200 commandes exposées. **La dépendance croisée** : au-delà de 40 % du CA de ton fournisseur il ne survit pas à ton départ, au-delà de 60 % de ton COGS chez un seul tu ne survis pas au sien.

### 7.3 La TVA n'est jamais de la trésorerie

**Les règles publiques.** Depuis le 1ᵉʳ juillet 2021, un seuil unique de **10 000 € par an**, cumulé sur toutes les ventes à distance intracommunautaires, remplace les seuils par pays : en dessous, la TVA de ton pays d'établissement ; au-dessus, celle du **pays de destination**, déclarée via le **guichet unique (OSS)** — une déclaration trimestrielle unique dans un seul État membre. Le Royaume-Uni en est hors et exige une immatriculation propre ; la TVA à l'importation est autoliquidée en France depuis le 1ᵉʳ janvier 2022. Franchir 10 000 € arrive au palier P1 : **ce n'est pas un sujet de grande entreprise.**

```
TVA collectée à P5 = 4 333 196 − 3 610 997     = 722 199 €/mois
TVA déductible réellement décaissée :
  logistique  397 210 × 20 %                   =  79 442 €
  frais fixes 360 000 × 70 % × 20 % (hyp.)     =  50 400 €
  marchandise (autoliquidée à l'import) et publicité
  (autoliquidation intra-UE)                   →       0 €
TVA nette à reverser = 722 199 − 129 842       = 592 357 €/mois
```

Presque toute la TVA déductible que tu imagines n'existe pas en trésorerie : publicité et marchandise sont autoliquidées, donc neutres. **Tu encaisses 722 199 € par mois et n'en récupères que 129 842 €.** D'où un flottant considérable.

```
Hyp. : 40 % du CA en France (déclaration mensuelle), 60 % via l'OSS
       (déclaration trimestrielle).
  France : 236 943 € × 1,5 mois =   355 415 €
  OSS    : 355 414 € × 2,5 mois =   888 535 €
  Flottant moyen                  1 243 950 €
  Un trimestre de TVA nette       1 777 071 €
```

Le flottant moyen vaut **55 % du BFR de P5**, et un trimestre de TVA nette **75 % du capital nécessaire pour construire toute l'entreprise** (§ 3.3). Il n'apparaît nulle part au § 4 : prêt à taux zéro consenti par l'État, exigible à date fixe, sans négociation ni étalement.

**Conséquence non négociable :** un compte séparé, alimenté chaque semaine de la TVA nette de la semaine, sur lequel tu ne prélèves jamais ; son solde ne figure pas dans ta trésorerie disponible. Une marque qui finance un lot de stock avec un trimestre de TVA gagne quatre-vingt-dix jours et meurt le quatre-vingt-onzième.

> **À retenir :** trois lignes de ton compte en banque ne t'appartiennent pas — la TVA collectée, les dettes fournisseurs échues, les commandes encaissées non expédiées. Ta trésorerie disponible, c'est le solde moins ces trois lignes.

---

## 8. Les erreurs qui coûtent cher

**1. Confondre EBITDA et trésorerie.** À P4 avec 20 % de croissance mensuelle : EBITDA +198 572 €, BFR −278 502 €, impôt −49 643 €, soit **−129 573 € par mois** dans une entreprise à 8,1 % de rentabilité. Le seul tableau qui décide est celui des flux.

**2. Financer du stock permanent avec de la dette courte.** Les 1 832 581 € de stock de P5 tournent mais ne descendent jamais à zéro. Financés par un découvert révocable : la ligne est coupée, tu liquides 105 jours de stock en 30, décote de 40 %, **733 032 € détruits**, et tu ne réapprovisionnes plus — la rupture à 1 449 504 € du § 7.2. **Actif permanent, financement permanent.**

**3. Traiter la TVA collectée comme du cash.** Un trimestre de TVA nette à P5 vaut **1 777 071 €** (§ 7.3) : trois quarts du capital total de l'entreprise, sur ton compte, qui ne t'appartient pas. L'erreur arrive entre P2 et P3, quand le flottant devient assez gros pour financer le lot que tu ne peux pas payer.

**4. Commander gros pour obtenir un meilleur prix unitaire.** Le fournisseur propose −4 % si tu passes d'un cycle de 2 mois à 6 mois sur le héros.

```
Gain : 4 % × (49 087 × 12 × 4,80 €)              = 113 096 €/an
Portage : 60 j de stock, 471 168 € à 11 %        =  51 828 €/an
Prévision à 6 mois — hyp. 12 % mal réparti, démarqué à −40 % :
  0,12 × 294 522 = 35 343 u × 32,50 € × 40 % = 459 459 €/commande,
  × 2 commandes/an                               = 918 918 €/an
Solde                                            = −857 650 €/an
```

**La remise vaut huit fois moins que l'erreur de prévision qu'elle t'oblige à accepter.**

**5. Sous-dimensionner le SAV avant un pic.** *Hypothèse Black Friday : ×3,5 sur les commandes pendant 5 jours, taux de tickets doublé par les retards.*

```
Commandes du pic = 2 007 × 3,5 × 5 = 35 123
Tickets/jour = 0,44 × 7 025 = 3 091 contre 441 (×7,0) → arriéré 13 250
Hyp. 4 % des commandes du pic annulées ou contestées :
  1 405 × (59,98 + 6,60) + 1 405 × 15 € de frais  = 114 620 €
Prévention : 10 renforts pendant 3 semaines       =  25 500 €
```

Voir [C09](../etudes-de-cas/C09-piege-du-black-friday.md).

**6. Ne pas provisionner les retours.** Les retours de la cohorte Black Friday arrivent en janvier, quand la trésorerie est au plus bas. *Hypothèse : taux de retour doublé à 7 % sur cette cohorte.*

```
Retours = 7 % × 35 123 = 2 459 commandes
  remboursements 2 459 × 71,98 € TTC = 176 999 €
  traitement     2 459 × 24,92 €     =  61 278 €  → 238 277 €
```

238 277 € de sortie en janvier, sur un chiffre d'affaires reconnu en décembre. **Provisionne le taux de retour de chaque cohorte au mois de la vente.**

---

## 9. Ce que ce module ne dit pas

**Il n'enseigne ni la comptabilité ni la fiscalité.** Le § 7.3 énonce des règles publiques et un ordre de grandeur ; il ne remplace ni un expert-comptable ni un avocat fiscaliste. Seuils, taux et régimes changent, les obligations dépendent de ta forme juridique et de tes pays d'établissement, et une erreur de TVA transfrontalière se règle en redressement. Fais valider ton montage avant d'ouvrir le deuxième pays.

**Il ne s'applique pas aux modèles sans stock.** Dropshipping, impression à la demande, produit numérique, expédition par la place de marché : le DIO tombe à zéro, le DPO peut dépasser le DSO, le BFR devient nul ou **négatif** — le client finance l'exploitation, et la section 3 s'effondre : le capital n'est plus 2,36 M€ mais le cumul des pertes, 147 237 €. Prix de cette liberté : coefficient plus faible, différenciation nulle, délais subis, aucun actif à revendre ([E02](E02-marche-et-produit.md)).

**Il laisse quatre sujets à d'autres modules.** Le change n'est pas traité : acheter en dollars expose le COGS annuel de P5 (6 283 135 €) à 628 313 € d'EBITDA pour 10 % de parité — la ligne « −10 % de COGS » du § 7 des canoniques. La levée de fonds et la valorisation relèvent de [E12](E12-marque-et-actif.md) et [E14](E14-plan-1M-semaine.md), l'organisation de [E11](E11-passage-a-echelle.md), la ruine de [E13](E13-risque-de-ruine.md), qui reprend le § 3.2 avec des distributions.

---

## 10. Le tableau de bord du module

| # | Indicateur | Maille | Fréquence | Seuil d'alerte |
| --- | --- | --- | --- | --- |
| 1 | Trésorerie **nette** de TVA collectée, dettes échues et commandes encaissées non expédiées | Global | Hebdo. | < réserve du palier (§ 3.1) |
| 2 | BFR en jours de CA TTC, décomposé en 4 postes (§ 1.3) | Global | Mensuel | +3 j sur 2 mois de suite, ou > 20 j |
| 3 | EBITDA mensuel ÷ BFR, contre croissance réalisée | Global | Mensuel | Croissance > ce ratio sans financement identifié |
| 4 | Couverture de stock en jours | SKU × marché | Hebdo. | < délai + sécurité (§ 5.1), ou > 150 j |
| 5 | Arriéré SAV et délai de première réponse | Global | Quotidien | Arriéré > 1,5 × capacité quotidienne |
| 6 | DPO réel constaté, contre DPO contractuel | Fournisseur | Mensuel | Écart > 5 jours dans un sens ou dans l'autre |

L'indicateur 3 compare une ambition à une capacité ; l'indicateur 1 est le seul qui ne ment jamais.

> **À retenir :** une marque en croissance meurt de trésorerie, jamais de rentabilité. Si tu ne gardes qu'une de ces six lignes, garde la première.

---

## 11. Exercices

À rendre dans [`ecommerce/exercices/E10-rendu.md`](../exercices/E10-rendu.md), corrigés dans `E10-corrige.md`.

**1 — Le cycle de cash de P4 (réponse numérique unique).** À partir du seul § 4 et du § 2.2, retrouve le DIO, le DSO, l'avance publicitaire et le DPO de P4 dans leur unité native, convertis-les en jours de CA TTC, vérifie que la somme redonne les 14 jours du canonique, et dis quel poste explique la dégradation entre P3 et P4.

**2 — Le capital d'un scénario intermédiaire (réponse numérique unique).** Refais le § 3.2 avec un BFR constitué à 50 % au premier mois du palier, à 50 % sur les mois suivants. Donne le creux, le mois où il se produit, le capital minimum avec la réserve du § 3.1, et l'écart avec les deux scénarios du § 3.4.

**3 — Ton BFR.** Calcule tes quatre postes sur ton dernier mois clos : stock au coût d'achat, encaissements en attente chez ton PSP, dépense publicitaire des N derniers jours dont le CA n'est pas rentré (mesure N, ne le devine pas), dettes fournisseurs. Exprime-le en euros **et** en jours de CA TTC, puis compare au § 4 : quel poste est le plus éloigné du modèle, et pourquoi ?

**4 — Ta croissance mensuelle autofinançable.** Applique `g = EBITDA mensuel ÷ BFR` et compare g à ta croissance réelle des six derniers mois. Si elle dépasse g, chiffre le trou mensuel et nomme la source qui le comble aujourd'hui. Si tu ne peux pas la nommer, tu la découvriras quand elle s'arrêtera.

**5 — Ton point de recommande et ta réserve.** Pour ta référence la plus vendue : consommation quotidienne en unités, délai en quatre étapes, σ mesuré sur des fenêtres glissantes de la longueur de ton délai (pas sur la journée), sécurité à Z = 1,96, point de recommande en unités et en euros. Calcule ta réserve (§ 3.1) et compare-la à la trésorerie nette de l'indicateur 1.

**6 — Décision : la remise ou les jours.** Ton fournisseur propose **3 % de remise** ou **45 jours de délai en plus**. COGS mensuel : 180 000 €. Ton seul financement marginal est une avance sur revenus à 6 % sur 5 mois, en 5 mensualités égales. Calcule son taux annuel effectif, applique `k seuil = 360 × p ÷ n`, tranche, et écris la condition sous laquelle l'autre option deviendrait la bonne.

---

*Fin du module E10. Suite : [E11](E11-passage-a-echelle.md), qui construit l'organisation capable d'exécuter ces opérations sur sept marchés ; puis [E13](E13-risque-de-ruine.md), qui reprend le § 3.2 avec des distributions, et [E14](E14-plan-1M-semaine.md), qui assemble le plan.*
