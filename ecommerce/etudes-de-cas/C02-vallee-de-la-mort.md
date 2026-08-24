# Cas C02 — NØRA, mois 1 à 9 : la vallée de la mort

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des
> ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.
> **Ce que tu dois en tirer :** une marque qui perd de l'argent sur la première
> commande ne se sauve pas par l'effort, elle se traverse avec du capital chiffré
> d'avance et une courbe de réachat qui arrive à l'heure.
> **Modules rattachés :** E01, E08, E10, E13.

---

## 0. Comment ce cas est construit

Les [chiffres canoniques](../donnees/chiffres-canoniques.md) figent NØRA par
**paliers**, pas par mois : P1 est la moyenne de M1–M3, P2 la moyenne de M4–M9.
Un palier ne se vit pas en moyenne, il se vit mois par mois — et c'est mois par
mois que la trésorerie tombe.

J'ai donc construit une progression mensuelle sous contrainte : **les moyennes de
M1 à M3 retombent exactement sur P1, celles de M4 à M9 exactement sur P2.** Ce qui
varie d'un mois à l'autre est le volume de commandes, la part de réachat, le budget
publicitaire et les frais fixes. Ce qui est tenu constant à l'intérieur d'un palier
est le panier moyen et la structure de coût variable, parce que ce sont des
paramètres de palier dans le modèle canonique (§ 2 et § 2.1). Les budgets média sont
posés en montants ronds ; le dernier mois de chaque palier absorbe l'arrondi pour que
le MER moyen tombe sur 1,80 et 2,20 au centième. Tout le reste est calculé, jamais
posé.

Une conséquence à assumer : le passage du panier de première commande de 45,50 € à
55,00 € apparaît comme une marche au mois 4, alors que dans la vraie vie l'adoption
d'une nouvelle offre s'étale sur six à huit semaines. *Hypothèse de modélisation
déclarée.* Elle ne change pas la leçon, elle la rend lisible.

---

## 1. La situation

NØRA lance en janvier. Soin capillaire premium, France uniquement, un seul produit :
le **Sérum Densité 50 ml à 39,00 € TTC** (chiffres canoniques § 1). Un fondateur à
plein temps, une personne à mi-temps, un prestataire logistique au colis, Shopify et
Meta. **90 000 € de fonds propres** au départ — 60 000 € du fondateur, 30 000 € de
love money.

Le panier moyen de première commande est de **45,50 € TTC** : le sérum à 39,00 €,
plus le port facturé et une deuxième unité sur une minorité de commandes.
*Hypothèse de composition ;* le montant, lui, est canonique (§ 2).

### 1.1 L'économie d'une première commande au palier P1

Tous les pourcentages sont ceux de la structure de coût variable P1 (canoniques
§ 2.1), appliqués au CA **HT**. Le CA HT d'une commande à 45,50 € TTC vaut
45,50 ÷ 1,20 = **37,92 € HT**.

| Ligne | Taux (% CA HT) | Montant HT |
| --- | ---: | ---: |
| CA de la commande | — | 37,92 € |
| COGS | 20,0 % | −7,58 € |
| Logistique | 16,0 % | −6,07 € |
| Frais de paiement (PSP) | 1,80 % | −0,68 € |
| Retours et SAV | 2,0 % | −0,76 € |
| Remises et codes | 3,0 % | −1,14 € |
| **Marge brute (CM2)** | **57,2 %** | **21,69 €** |
| Coût d'acquisition d'un nouveau client (nCAC) | — | −26,62 € |
| **Marge sur la première commande** | — | **−4,93 €** |

Le nCAC de 26,62 € est le rapport entre la dépense publicitaire du palier et le
nombre de nouveaux clients : 20 444 € ÷ 768 = 26,62 € (canoniques § 2.4).

**Chaque client acquis coûte 4,93 € de plus qu'il ne rapporte au moment où il
achète.** Ce n'est pas une anomalie de démarrage. C'est la structure de la marque,
et elle est la même à tous les paliers jusqu'à P5 (−7,26 € à P5).

---

## 2. Le diagnostic

Ce que le fondateur croyait au mois 2 : « le produit marche, il faut juste plus de
budget ». Ce que les chiffres disent :

**Premier point — le CM3 est négatif, donc le volume aggrave.** Le CM3 est la marge
brute moins la publicité, avant frais fixes. Vérification sur le palier P1 :

```
768 nouveaux clients × (−4,93 €)      = −3 788 €
 32 commandes de réachat × 27,65 €     =   +885 €
                                         ---------
CM3 mensuel                             = −2 903 €
```

C'est exactement le CM3 canonique de P1. **Traduction : à structure inchangée,
doubler le volume double la perte avant même de toucher aux frais fixes.**

**Deuxième point — le MER est sous ses deux seuils.** Le MER est le rapport CA TTC
sur dépense publicitaire. Aux seuils canoniques du palier P1 (§ 2.3) : MER
d'équilibre CM3 = 2,10, MER d'équilibre EBITDA = 3,33. NØRA est à 1,80. Elle est à
46,0 % sous sa ligne de flottaison EBITDA.

**Troisième point — le seul actif est la courbe de réachat, et elle n'existe pas
encore.** Avec 4 % de commandes en réachat, le modèle n'a aucun second étage. La
LTV en contribution se lit sur la courbe canonique (§ 3) : 0,72 commande de réachat
par client acquis à six mois, 1,24 à douze mois.

| Horizon | Réachats cumulés par client | LTV en contribution (P1) | LTV / nCAC |
| --- | ---: | ---: | ---: |
| 1 mois | 0,06 | 23,35 € | 0,88 |
| 3 mois | 0,34 | 31,09 € | 1,17 |
| 6 mois | 0,72 | 41,59 € | 1,56 |
| 12 mois | 1,24 | 55,97 € | 2,10 |
| 24 mois | 1,98 | 76,43 € | 2,87 |

Calcul déroulé pour l'horizon 12 mois : contribution de la première commande
21,69 € + 1,24 × 27,65 € (contribution d'un réachat à 58,00 € TTC de panier) =
**55,97 €**, soit 2,10 fois le nCAC. Conforme au canonique § 3.1.

> **À retenir :** la marque n'est pas non rentable, elle est **différée**. Elle
> gagne 2,10 € par euro investi — dans douze mois. Le problème n'est pas la
> rentabilité, c'est le financement des douze mois.

---

## 3. Les options, à la fin du mois 3

Trésorerie au 31 du mois 3 : **29 210 €**. Brûlage du mois 3 : 22 249 €. Il reste
1,3 mois. Quatre options, chacune chiffrée à l'horizon du palier P2.

| Option | Ce qu'on fait | EBITDA mensuel | Sortie |
| --- | --- | ---: | --- |
| **A — Arrêter** | Liquider, solder le stock | 0 € ensuite | Perte définitive ≈ **39 771 €** |
| **B — Rester à l'échelle M3** | Ni levée, ni changement d'offre | **−10 678 €** | Mort en trésorerie à M6 |
| **C — Lever 250 k€ et pousser le volume** | 4 000 cmd/mois, offre inchangée | **−75 088 €** | Mort en trésorerie à M7 |
| **D — Lever 250 k€ et refaire l'économie** | Rituel + réachat + création | **−19 838 €** | Trésorerie tenable jusqu'à M9 |

**Option A.** Pertes cumulées M1–M3 = 28 209 €. Le BFR se récupère sauf le stock :
stock estimé à M3 = 15 333 € × (55 500 ÷ 36 800) = 23 124 €, soldé à 50 % de sa
valeur, soit 11 562 € perdus. Total : 28 209 + 11 562 = **39 771 €**. C'est le prix
d'une sortie propre au mois 3, et c'est le seul montant de ce cas qui soit certain.

**Option B.** L'EBITDA du mois 3 est de −10 678 €. À volume gelé, le BFR cesse de
croître, donc le brûlage tombe à l'EBITDA seul. 29 210 ÷ 10 678 = **2,7 mois**.
La marque meurt au mois 6, avec zéro apprentissage supplémentaire.

**Option C — celle qui tue.** Même volume que l'option D, mais panier de première
commande à 45,50 €, réachat à 4 % et nCAC dégradé à 37,61 € (le CAC marginal monte
quand on passe de 768 à 3 400 nouveaux clients par mois — module 13 § 2.2) :

```
CA TTC        = 3 400 × 45,50 € + 142 × 72,00 €   = 164 900 €
CA HT         = 164 900 ÷ 1,20                    = 137 417 €
Marge brute   = 137 417 € × 58,8 %                =  80 801 €
Publicité     = 3 400 × 37,61 €                   = 127 889 €  (MER = 1,29)
CM3                                               = −47 088 €
EBITDA        = −47 088 € − 28 000 €              = −75 088 €
```

Trésorerie : 161 873 € à M4, 86 786 € à M5, 11 698 € à M6, négative à M7. **Lever
de l'argent pour faire tourner une économie unitaire non réparée revient à acheter
trois mois de sursis à 250 000 €.**

**Option D.** C'est ce qui a été fait. Trois décisions, prises ensemble.

---

## 4. La décision et l'exécution, mois par mois

### 4.1 Le tableau des neuf mois

Montants en euros. **CA TTC = prix client ; toutes les autres colonnes sont HT.**
Apports en capital : +90 000 € au mois 1, +250 000 € au mois 4.

| Mois | Cmd. | Réachat | CA TTC | CA HT | Marge brute | Pub | MER | CM3 | Fixes | EBITDA | Trésorerie fin de mois |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| M1 | 420 | 0,0 % | 19 110 | 15 925 | 9 109 | 12 300 | 1,55 | −3 191 | 5 000 | −8 191 | 70 591 |
| M2 | 780 | 3,1 % | 35 790 | 29 825 | 17 060 | 19 900 | 1,80 | −2 840 | 6 500 | −9 340 | 51 459 |
| M3 | 1 200 | 6,0 % | 55 500 | 46 250 | 26 455 | 29 133 | 1,91 | −2 678 | 8 000 | −10 678 | 29 210 |
| **Moy. M1–M3** | **800** | **4,0 %** | **36 800** | **30 667** | **17 541** | **20 444** | **1,80** | **−2 903** | **6 500** | **−9 403** | — |
| M4 | 1 900 | 7,0 % | 106 761 | 88 968 | 52 313 | 60 000 | 1,78 | −7 687 | 16 000 | −23 687 | 239 657 |
| M5 | 2 600 | 9,0 % | 146 978 | 122 482 | 72 019 | 76 500 | 1,92 | −4 481 | 21 000 | −25 481 | 195 926 |
| M6 | 3 400 | 12,0 % | 193 936 | 161 613 | 95 029 | 94 500 | 2,05 | +529 | 26 000 | −25 471 | 149 146 |
| M7 | 4 400 | 14,5 % | 252 846 | 210 705 | 123 895 | 114 000 | 2,22 | +9 895 | 30 000 | −20 105 | 102 308 |
| M8 | 5 400 | 17,5 % | 313 065 | 260 888 | 153 402 | 133 500 | 2,35 | +19 902 | 34 000 | −14 098 | 60 883 |
| M9 | 6 300 | 19,7 % | 367 614 | 306 345 | 180 131 | 149 318 | 2,46 | +30 813 | 41 000 | −10 187 | **25 942** |
| **Moy. M4–M9** | **4 000** | **15,0 %** | **230 200** | **191 833** | **112 798** | **104 636** | **2,20** | **+8 162** | **28 000** | **−19 838** | — |

Les deux lignes en gras sont les valeurs canoniques P1 et P2 (§ 2 et § 2.2), pas des
moyennes recalculées à la main. La part de réachat moyenne est agrégée
(réachats totaux ÷ commandes totales) : 96 ÷ 2 400 = 4,00 % et 3 600 ÷ 24 000 =
15,00 %. Le MER moyen est agrégé lui aussi : 1 381 200 ÷ 627 818 = 2,20.

### 4.2 Décision 1 — du produit unique au rituel en trois produits

Lancée au mois 4 : le Rituel Complet à 74,00 € TTC (sérum + shampooing + masque,
canoniques § 1) devient l'offre poussée en publicité, le sérum seul reste
disponible. Effet : le panier moyen de première commande passe de **45,50 € à
55,00 € TTC** (§ 2), soit +20,9 %.

Contrefactuel au palier P2, panier de première commande maintenu à 45,50 € :

| | Sans le rituel | Avec le rituel | Écart |
| --- | ---: | ---: | ---: |
| CA TTC / mois | 197 900 € | 230 200 € | +32 300 € |
| CA HT / mois | 164 917 € | 191 833 € | +26 917 € |
| Marge brute (58,8 %) | 96 971 € | 112 798 € | +15 827 € |
| Publicité (inchangée) | 104 636 € | 104 636 € | 0 € |
| MER | 1,89 | 2,20 | +0,31 |
| CM3 | −7 665 € | +8 162 € | +15 827 € |
| **EBITDA / mois** | **−35 665 €** | **−19 838 €** | **+15 827 €** |

**+94 962 € d'EBITDA sur les six mois de P2.** La publicité ne bouge pas : on
achète le même client, on lui vend plus cher. C'est le levier le plus rentable du
tableau canonique § 7, et c'est aussi celui qui ne demande aucun euro de plus.

### 4.3 Décision 2 — la relance de réachat calée sur la durée de consommation

Un flacon de sérum 50 ml dure environ **60 jours** à raison d'une pipette par jour.
*Hypothèse produit.* La séquence de relance est donc calée sur J+45, J+58, J+70 —
avant la rupture, pas après. Effet : la part de commandes en réachat passe de
**4 % à 15 %** (§ 2), en montant mois par mois de 7,0 % à 19,7 %.

Contrefactuel : acquisition identique (3 400 nouveaux clients, même budget média),
réachat maintenu à 4 % des commandes, soit 142 commandes au lieu de 600.

| | Réachat à 4 % | Réachat à 15 % | Écart |
| --- | ---: | ---: | ---: |
| Commandes / mois | 3 542 | 4 000 | +458 |
| CA TTC / mois | 197 200 € | 230 200 € | +33 000 € |
| Marge brute | 96 628 € | 112 798 € | +16 170 € |
| MER | 1,88 | 2,20 | +0,32 |
| **EBITDA / mois** | **−36 008 €** | **−19 838 €** | **+16 170 €** |

**+97 020 € sur les six mois.** Ces 458 commandes n'ont coûté aucune publicité :
elles portent la marge brute entière, 35,28 € de contribution chacune
(72,00 ÷ 1,20 × 58,8 %). C'est la seule ligne de ce cas où le CAC est nul.

### 4.4 Décision 3 — l'industrialisation créative

À P1, NØRA testait trois ou quatre nouvelles publicités par semaine, produites par
le fondateur. À P2, le rythme canonique est de **14 concepts testés par semaine
pour 1,7 gagnant**, avec 9 gagnants en rotation permanente et 188 assets produits
par mois (§ 6), financés par 15 % du budget média réservé au test — 3 622 € par
semaine. Effet : le MER passe de **1,80 à 2,20**.

Contrefactuel : mêmes volumes, machine créative restée artisanale. Acquérir 3 400
nouveaux clients par mois au lieu de 768 coûte alors **37,61 € pièce** au lieu de
30,78 € — c'est la loi du CAC marginal croissant (module 13 § 2.2).

| | Sans industrialisation | Avec | Écart |
| --- | ---: | ---: | ---: |
| nCAC | 37,61 € | 30,78 € | −6,83 € |
| Publicité / mois | 127 889 € | 104 636 € | −23 253 € |
| MER | 1,80 | 2,20 | +0,40 |
| CM3 | −15 091 € | +8 162 € | +23 253 € |
| **EBITDA / mois** | **−43 091 €** | **−19 838 €** | **+23 253 €** |

**+139 515 € sur les six mois.** C'est la plus grosse des trois.

### 4.5 Les trois ensemble

| Décision | Effet EBITDA / mois | Sur les 6 mois de P2 |
| --- | ---: | ---: |
| 1. Rituel en trois produits | +15 827 € | +94 962 € |
| 2. Relance de réachat | +16 170 € | +97 020 € |
| 3. Industrialisation créative | +23 253 € | +139 515 € |
| **Aucune des trois** | **EBITDA = −75 088 €/mois** | **−331 497 €** |

Les trois effets sont ici **exactement additifs** : 15 827 + 16 170 + 23 253 =
55 250 €, et l'écart entre l'EBITDA réel (−19 838 €) et le contrefactuel total
(−75 088 €) vaut 55 250 €. La raison est mécanique — chacune agit sur un terme
différent (le panier, le nombre de commandes sans CAC, le coût d'acquisition) et
la marge brute est linéaire en chiffre d'affaires. **Ce n'est pas une loi
générale :** dès qu'un levier modifie le taux de marge ou la conversion, les
effets se composent au lieu de s'additionner.

---

## 5. Les résultats

### 5.1 Avant / après

| | M1 | M9 | Écart |
| --- | ---: | ---: | --- |
| Commandes | 420 | 6 300 | ×15,0 |
| Part de commandes en réachat | 0,0 % | 19,7 % | +19,7 pts |
| CA TTC / mois | 19 110 € | 367 614 € | ×19,2 |
| CA TTC / semaine | 4 410 € | 84 834 € | ×19,2 |
| Marge brute (CM2) | 9 109 € | 180 131 € | 57,2 % → 58,8 % |
| Dépense publicitaire | 12 300 € | 149 318 € | ×12,1 |
| MER | 1,55 | 2,46 | +0,91 |
| CM3 en % du CA HT | −20,0 % | +10,1 % | **+30,1 pts** |
| EBITDA | −8 191 € | −10 187 € | −1 996 € |
| **EBITDA en % du CA HT** | **−51,4 %** | **−3,3 %** | **+48,1 pts** |

Regarde la ligne EBITDA en euros : elle est **pire** à M9 qu'à M1. Regarde la
ligne au-dessous : elle est meilleure de 48 points. Les deux sont vraies. C'est
exactement ce que produit une marque qui répare son économie unitaire tout en
accélérant : la perte absolue reste stable ou grossit, le taux s'effondre vers
zéro. **Piloter la perte en euros pendant cette phase est la meilleure façon de
tuer une marque qui allait s'en sortir.**

### 5.2 La trésorerie — le vrai tableau

| Mois | EBITDA | BFR fin de mois | Δ BFR | Brûlage de cash | Apport | Trésorerie |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| M1 | −8 191 € | 11 218 € | +11 218 € | −19 409 € | +90 000 € | 70 591 € |
| M2 | −9 340 € | 21 010 € | +9 792 € | −19 132 € | — | 51 459 € |
| M3 | −10 678 € | 32 581 € | +11 571 € | −22 249 € | — | 29 210 € |
| M4 | −23 687 € | 48 447 € | +15 866 € | −39 553 € | +250 000 € | 239 657 € |
| M5 | −25 481 € | 66 697 € | +18 250 € | −43 731 € | — | 195 926 € |
| M6 | −25 471 € | 88 006 € | +21 309 € | −46 780 € | — | 149 146 € |
| M7 | −20 105 € | 114 738 € | +26 732 € | −46 838 € | — | 102 308 € |
| M8 | −14 098 € | 142 065 € | +27 327 € | −41 425 € | — | 60 883 € |
| M9 | −10 187 € | 166 819 € | +24 754 € | −34 941 € | — | **25 942 €** |
| **Total** | **−147 239 €** | — | **+166 819 €** | **−314 058 €** | **+340 000 €** | — |

Le BFR est calculé au ratio canonique du palier appliqué au CA TTC du mois :
21 603 ÷ 36 800 = 0,587038 pour P1, 104 462 ÷ 230 200 = 0,453788 pour P2 (§ 4).
Contrôle : 0,453788 × 100 000 = 45 379 €, exactement le « cash immobilisé par
+100 k€ de CA mensuel » du tableau canonique § 4.

**Le point bas de trésorerie est au mois 9 : 25 942 €.** Pas au mois 4, où la perte
mensuelle est la plus lourde. Au mois 9, où l'EBITDA est le meilleur de tout le
palier P2. Raison : à partir du mois 6, l'EBITDA se répare de 25 471 € à 10 187 €,
mais le BFR grossit de 21 309 € à 24 754 € par mois. **Le besoin de financement de
la croissance dépasse la réparation du compte de résultat.**

Au rythme du mois 9, il reste 25 942 ÷ 34 941 = **0,74 mois de trésorerie**. Trois
semaines.

### 5.3 Le chiffre à retenir

```
Pertes cumulées M1 → M9                   147 239 €
Besoin en fonds de roulement immobilisé   166 819 €
                                        -----------
CAPITAL CONSOMMÉ EN NEUF MOIS             314 058 €
```

Contrôle : la somme des neuf brûlages mensuels vaut 314 058 €. Les deux méthodes
convergent.

**314 058 € pour amener une marque de 0 à 84 834 € de CA TTC par semaine, toujours
en perte.** Et 84 834 €, c'est 8,5 % de l'objectif de 999 968 € par semaine du
palier P5. Le BFR pèse 53 % du capital consommé : **plus de la moitié de l'argent
brûlé n'est pas une perte, c'est du stock et des encaissements en attente.** Il est
récupérable — mais pas tant que tu croîs.

---

## 6. Ce qui aurait pu mal tourner

**La levée du mois 4 ne se signe pas.** Sans les 250 000 €, la trésorerie du mois 4
vaut 90 000 − 51 896 − 48 447 = **−10 343 €**. Défaut de paiement fournisseur au
mois 4. Le cas entier repose sur un virement reçu à temps.

**La courbe de réachat plafonne à 8 % au lieu de 15 %.** Le scénario le plus
probable : le sérum plaît, mais la relance arrive après la rupture d'usage.

| | Réachat 8 % | Réachat 15 % |
| --- | ---: | ---: |
| CA TTC / mois (P2) | 208 287 € | 230 200 € |
| MER | 1,99 | 2,20 |
| CM3 | −2 576 € | +8 162 € |
| EBITDA / mois | −30 576 € | −19 838 € |

Écart : 10 738 €/mois, **64 424 € sur P2**. Le capital consommé passerait de
314 058 € à 378 482 € — au-delà du plafond de 350 000 € posé au mois 1 (§ 6.1).
**La règle d'arrêt se déclencherait, et elle aurait raison.**

**Le MER de 2,20 est une illusion d'attribution.** Le MER se lit sur les ventes
totales et non sur l'attribution plateforme, donc il est robuste — mais la
*répartition* entre canaux ne l'est pas. Au palier P5, la sur-attribution
canonique est de 11 % (§ 5). Si l'amélioration de 1,80 à 2,20 venait d'un
retargeting qui récolte des ventes déjà acquises, couper 20 % du budget ne coûterait
rien. C'est un test à faire, pas une hypothèse à croire — voir C06.

**La rupture de stock au mois 8.** Le stock est le premier poste du BFR. Une commande
fournisseur sous-dimensionnée au mois 6, sur un délai de réapprovisionnement de
huit à dix semaines, coupe la croissance au mois 8 — au moment exact où la
trésorerie ne supporte plus une reprise ratée.

**Le rituel cannibalise au lieu d'ajouter.** Le panier monte de 20,9 %, mais si le
taux de conversion baisse de plus de 17,3 % le CA net baisse. Vérification :
1,209 × (1 − 0,173) = 1,000. Le seuil est étroit et il se mesure, il ne se suppose
pas.

### 6.1 À quel moment un fondateur rationnel aurait-il dû arrêter ?

La question honnête n'est pas « quand arrêter » mais « qu'avais-tu écrit avant de
commencer ». Voici le contrat qu'il fallait poser au mois 1, en quatre lignes non
révisables :

```
CRITÈRE D'ARRÊT — écrit le premier jour, non renégociable

1. Capital total engagé plafonné à 350 000 €. Au-delà, on arrête,
   quel que soit l'espoir du moment.
2. Contrôle à M6 sur la cohorte M1, devenue observable à 6 mois :
   LTV 6 mois en contribution ÷ nCAC ≥ 1,50. Sinon, arrêt.
3. Contrôle à M6 : MER du mois ≥ MER d'équilibre CM3 du palier (2,04).
   Sinon, arrêt.
4. En permanence : trésorerie ≥ 2 mois de brûlage projeté. Sous 2 mois
   sans tour signé à 30 jours, arrêt de l'acquisition payante le jour
   même — pas le mois suivant.
```

Confrontation aux faits :

| Ligne | Seuil | Réalisé | Verdict |
| --- | ---: | ---: | --- |
| 1. Capital engagé | ≤ 350 000 € | 340 000 € | Passe |
| 2. LTV 6 mois / nCAC (cohorte M1) | ≥ 1,50 | 41,59 ÷ 26,62 = **1,56** | Passe de 0,06 |
| 3. MER à M6 vs seuil CM3 | ≥ 2,04 | **2,05** | Passe de 0,01 |
| 4. Trésorerie en mois de brûlage | ≥ 2,0 | **0,74 à M9** | **Déclenche** |

**Réponse : il ne fallait pas arrêter, et il fallait quand même s'arrêter de
dépenser au mois 9.** Les deux tests d'économie unitaire passent — d'un cheveu. Le
test de financement, lui, saute. Ce n'est pas la marque qui a échoué, c'est le plan
de financement : la levée du mois 4 était calibrée sur les pertes et pas sur le BFR,
qui pèse 53 % du besoin. **Il fallait lever 500 000 € au mois 4, pas 250 000 €.**

Et si tu retiens une seule ligne : **le point 2 est passé à 0,06 près et le point 3
à 0,01 près.** Ce cas se lit après coup comme une réussite. Il s'est joué à deux
centièmes.

---

## 7. Le mécanisme généralisable

> **À retenir :** la vallée de la mort n'est pas un accident, c'est la structure
> normale d'une marque qui perd de l'argent sur la première commande. Elle se
> traverse avec du capital et une courbe de réachat, pas avec de la volonté.

Énoncé comme une règle, en trois temps :

**1. Si ta marge de première commande est négative, ta perte est proportionnelle à
ta croissance.** Marge première commande = marge brute unitaire − nCAC. NØRA :
21,69 − 26,62 = −4,93 €. Tant que ce nombre est négatif, chaque client acquis
creuse le trou. Le pilotage par le chiffre d'affaires est alors une erreur de
lecture ; le seul indicateur qui compte est le CM3.

**2. Le capital nécessaire n'est pas la somme des pertes.** Il vaut
`pertes cumulées + BFR de fin de période`. Chez NØRA : 147 239 + 166 819 = 314 058 €.
Un plan de financement qui ne budgète que les pertes sous-estime le besoin de **113 %**
(166 819 ÷ 147 239). C'est le mode de mort le plus fréquent des marques qui marchent.

**3. Le point bas de trésorerie arrive après le point bas du compte de résultat.**
Chez NØRA, trois mois après. Tant que la croissance mensuelle du CA multipliée par
le ratio de BFR dépasse la réparation mensuelle de l'EBITDA, le cash continue de
baisser alors que tous les indicateurs de gestion s'améliorent. **Le tableau de bord
dit « on s'en sort » pendant que la banque dit « il reste trois semaines ». Les deux
ont raison.**

Corollaire opérationnel : la sortie de la vallée ne vient pas d'une réduction des
coûts. Elle vient de trois leviers, dans cet ordre de rendement — le panier de
première commande, le nombre de commandes sans CAC, le coût d'acquisition. Chez
NØRA : +15 827 €, +16 170 €, +23 253 € par mois. Les frais fixes, eux, ont été
**multipliés par 8,2** sur la période (5 000 € → 41 000 €) sans que ce soit une
erreur : ils ont financé la machine créative qui a rapporté le plus.

---

## 8. Questions

1. Calcule le capital total consommé par NØRA sur M1–M9 et décompose-le en deux
   postes. Quel poste est récupérable, et sous quelle condition ?
2. À la fin du mois 9, combien de mois de trésorerie reste-t-il au rythme de
   brûlage du mois 9 ? Déroule le calcul.
3. Le MER d'équilibre CM3 du palier P2 est de 2,04. À quel mois NØRA le franchit-elle,
   et que vaut alors le CM3 ?
4. Sans la relance de réachat (part maintenue à 4 % des commandes, acquisition
   inchangée), quel serait l'EBITDA mensuel du palier P2 ? Déroule.
5. Au palier P2, combien de commandes de réachat par mois faudrait-il pour que
   l'EBITDA soit nul, à acquisition et à frais fixes inchangés ? Exprime le résultat
   en part de commandes en réachat, et dis à quel palier canonique cela correspond.
6. Au mois 10, le fondateur veut ajouter 100 000 € de CA TTC mensuel. Quel montant
   de trésorerie faut-il mobiliser ? L'EBITDA du mois 9 le finance-t-il ?
7. Écris le critère d'arrêt qu'il fallait poser au mois 1. Laquelle de ses lignes
   saute, et à quel mois ?

---

## 9. Corrigé des questions

**1.** Pertes cumulées M1–M9 = **147 239 €** (somme de la colonne EBITDA du § 4.1).
BFR au 31 du mois 9 = **166 819 €**. Capital consommé = 147 239 + 166 819 =
**314 058 €**. Contrôle : la somme des brûlages mensuels du § 5.2 vaut aussi
314 058 €. Le BFR (53,1 % du total) est **récupérable — à la seule condition de
cesser de croître.** Une marque qui décélère libère son BFR ; c'est pourquoi une
marque en difficulté paraît soudain riche en trésorerie le trimestre où elle
s'arrête, et c'est un mirage.

**2.** Brûlage du mois 9 = EBITDA − ΔBFR = −10 187 − 24 754 = **−34 941 €**.
Trésorerie = 25 942 €. 25 942 ÷ 34 941 = **0,74 mois**, soit 23 jours. Note bien
que si l'on avait divisé par le seul EBITDA (25 942 ÷ 10 187 = 2,5 mois), on se
serait cru trois fois plus riche. **Le brûlage n'est pas la perte.**

**3.** Au **mois 6**, avec un MER de 2,05 contre un seuil de 2,04. Le CM3 vaut
alors 95 029 − 94 500 = **+529 €**, premier mois positif de l'histoire de la
marque. Il aura fallu six mois et 102 848 € de pertes cumulées pour que la
publicité cesse de coûter plus que la marge qu'elle rapporte — et il restera encore
26 000 € de frais fixes à couvrir ce mois-là.

**4.** Acquisition inchangée : 3 400 nouveaux clients, 104 636 € de publicité. Si le
réachat vaut 4 % du total, alors réachats = 3 400 × 0,04 ÷ 0,96 = **142 commandes**
(au lieu de 600).

```
CA TTC      = 3 400 × 55,00 € + 142 × 72,00 €  = 197 200 €
CA HT       = 197 200 ÷ 1,20                   = 164 333 €
Marge brute = 164 333 € × 58,8 %               =  96 628 €
CM3         = 96 628 € − 104 636 €             =  −8 008 €
EBITDA      = −8 008 € − 28 000 €              = −36 008 €
```

Contre −19 838 € réels : **écart de 16 170 € par mois, 97 020 € sur le palier.**
Le MER retombe à 197 200 ÷ 104 636 = 1,88, sous le seuil CM3 de 2,04.

**5.** EBITDA nul ⇒ CM3 = frais fixes = 28 000 €. Donc marge brute nécessaire =
28 000 + 104 636 = **132 636 €**.

```
CA HT requis  = 132 636 ÷ 0,588            = 225 572 €
CA TTC requis = 225 572 × 1,20             = 270 686 €
CA TTC manquant                            =  40 486 €
Réachats supplémentaires = 40 486 ÷ 72,00  =     562
Réachats totaux = 600 + 562                =   1 162
Part de réachat = 1 162 ÷ (3 400 + 1 162)  =   25,5 %
```

Il faudrait **25,5 % de commandes en réachat**, soit presque le double des 15 % de
P2. Le palier canonique qui porte ce niveau est **P3 (27 %)** — et c'est
précisément le palier où l'EBITDA canonique devient positif (+5,2 %). Le modèle est
cohérent avec lui-même : **NØRA ne sort pas de la vallée par le volume, elle en sort
par la rétention.**

**6.** Le ratio de BFR du palier P2 est de 0,453788 du CA TTC. Pour +100 000 € de CA
TTC mensuel : 0,453788 × 100 000 = **45 379 €** de trésorerie immobilisée — le
chiffre du tableau canonique § 4. L'EBITDA du mois 9 vaut **−10 187 €** : il ne
finance rien, il aggrave. Besoin total du mois : 45 379 + 10 187 = **55 566 €**,
pour une croissance de 100 000 ÷ 367 614 = **27,2 %**. Or la trésorerie disponible
est de 25 942 €. **La croissance de 27 % que le compte de résultat rend désirable
est financièrement impossible.** C'est la définition exacte de la faillite technique
d'une marque en bonne santé.

**7.** Voir l'encadré du § 6.1. Les quatre lignes : plafond de capital à 350 000 € ;
LTV 6 mois ÷ nCAC ≥ 1,50 à M6 ; MER ≥ MER d'équilibre CM3 à M6 ; trésorerie ≥ 2 mois
de brûlage en permanence. **C'est la ligne 4 qui saute, au mois 9** — à 0,74 mois de
trésorerie. Les lignes 2 et 3 passent respectivement de 0,06 et de 0,01. La ligne 1
passe à 10 000 € près. La conclusion n'est pas « il fallait arrêter » mais **« il
fallait lever deux fois plus au mois 4 »** : la levée de 250 000 € avait été
calibrée sur les pertes prévisionnelles et ignorait le BFR, qui représente 53 % du
capital réellement consommé.

---

*Fin du cas C02. Suite logique : [E10](../modules/E10-cash-et-operations.md) pour le
pilotage du BFR, [E08](../modules/E08-retention-et-ltv.md) pour la courbe de réachat
qui décide de tout, et [C04](C04-scale-qui-detruit-la-marge.md) pour voir le même
mécanisme à 41 M€ de chiffre d'affaires.*
