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
**paliers** : P1 est la moyenne de M1–M3, P2 celle de M4–M9. Mais un palier ne se vit
pas en moyenne, et c'est mois par mois que la trésorerie tombe. J'ai donc construit
une progression mensuelle sous contrainte : **les moyennes de M1 à M3 retombent
exactement sur P1, celles de M4 à M9 exactement sur P2.** Varient d'un mois sur
l'autre le volume de commandes, la part de réachat, le budget publicitaire et les
frais fixes ; restent constants à l'intérieur d'un palier le panier moyen et la
structure de coût variable, qui sont des paramètres de palier du modèle canonique
(§ 2 et § 2.1). Les budgets média sont posés en montants ronds, le dernier mois de
chaque palier absorbant l'arrondi pour que le MER moyen tombe sur 1,80 et 2,20 au
centième. Conséquence assumée : le panier de première commande passe de 45,50 € à
55,00 € en une marche au mois 4, là où une adoption réelle s'étalerait sur six à huit
semaines (*hypothèse déclarée*). Tout le reste est calculé.

---

## 1. La situation

NØRA lance en janvier. Soin capillaire premium, France, un seul produit : le **Sérum
Densité 50 ml à 39,00 € TTC** (canoniques § 1). Un fondateur à plein temps, une
personne à mi-temps, un logisticien au colis, Shopify et Meta. **90 000 € de fonds
propres** — 60 000 € du fondateur, 30 000 € de love money. Panier de première commande
**45,50 € TTC** : le sérum, plus le port facturé et une deuxième unité sur une
minorité de commandes (*hypothèse de composition ;* le montant est canonique, § 2).

### 1.1 L'économie d'une première commande au palier P1

Pourcentages de la structure de coût variable P1 (canoniques § 2.1), appliqués au CA
**HT**. Une commande de 45,50 € TTC vaut 45,50 ÷ 1,20 = **37,92 € HT**.

| Ligne | Taux (% CA HT) | Montant HT |
| --- | ---: | ---: |
| CA de la commande | — | 37,92 € |
| COGS | 20,0 % | −7,58 € |
| Logistique | 16,0 % | −6,07 € |
| Frais de paiement (PSP) | 1,80 % | −0,68 € |
| Retours et SAV | 2,0 % | −0,76 € |
| Remises et codes | 3,0 % | −1,14 € |
| **Marge brute (CM2)** | **57,2 %** | **21,69 €** |
| Coût d'acquisition (nCAC) | — | −26,62 € |
| **Marge sur la première commande** | — | **−4,93 €** |

Le nCAC est la dépense publicitaire du palier divisée par les nouveaux clients :
20 444 € ÷ 768 = 26,62 € (canoniques § 2.4).

**Chaque client acquis coûte 4,93 € de plus qu'il ne rapporte au moment où il
achète.** Ce n'est pas une anomalie de démarrage : c'est la structure de la marque, et
elle tient jusqu'à P5 (−7,26 €).

---

## 2. Le diagnostic

Ce que le fondateur croyait au mois 2 : « le produit marche, il faut juste plus de
budget ». Ce que les chiffres disent :

**Premier point — le CM3 est négatif, donc le volume aggrave.** Le CM3 est la marge
brute moins la publicité, avant frais fixes. Au palier P1 :

```
768 nouveaux clients × (−4,93 €)      = −3 788 €
 32 commandes de réachat × 27,65 €     =   +885 €
                                         ---------
CM3 mensuel                             = −2 903 €
```

C'est le CM3 canonique de P1. **À structure inchangée, doubler le volume double la
perte avant même de toucher aux frais fixes.**

**Deuxième point — le MER est sous ses deux seuils.** Le MER est le rapport CA TTC
sur dépense publicitaire. Seuils canoniques P1 (§ 2.3) : équilibre CM3 à 2,10,
équilibre EBITDA à 3,33. NØRA est à 1,80, soit 46,0 % sous sa ligne de flottaison.

**Troisième point — le seul actif est la courbe de réachat, et elle n'existe pas
encore.** À 4 % de commandes en réachat, le modèle n'a aucun second étage. La LTV en
contribution se lit sur la courbe canonique (§ 3) : 0,72 réachat par client à six
mois, 1,24 à douze mois.

| Horizon | Réachats cumulés par client | LTV en contribution (P1) | LTV / nCAC |
| --- | ---: | ---: | ---: |
| 3 mois | 0,34 | 31,09 € | 1,17 |
| 6 mois | 0,72 | 41,59 € | 1,56 |
| 12 mois | 1,24 | 55,97 € | 2,10 |

Calcul déroulé à 12 mois : 21,69 € + 1,24 × 27,65 € (contribution d'un réachat à
58,00 € TTC de panier) ≈ **55,97 €**, soit 2,10 fois le nCAC. Conforme au § 3.1.

> **À retenir :** la marque n'est pas non rentable, elle est **différée**. Elle gagne
> 2,10 € par euro investi — dans douze mois. Le problème n'est pas la rentabilité,
> c'est le financement des douze mois.

---

## 3. Les options, à la fin du mois 3

Trésorerie au 31 du mois 3 : **29 210 €**, brûlage du mois 3 : 22 249 €. Il reste
1,3 mois. Quatre options, chiffrées à l'horizon du palier P2.

| Option | Ce qu'on fait | EBITDA mensuel | Sortie |
| --- | --- | ---: | --- |
| **A — Arrêter** | Liquider, solder le stock | 0 € ensuite | Perte définitive ≈ **39 771 €** |
| **B — Rester à l'échelle M3** | Ni levée, ni changement d'offre | **−10 678 €** | Mort en trésorerie à M6 |
| **C — Lever 250 k€ et pousser le volume** | 4 000 cmd/mois, offre inchangée | **−75 088 €** | Mort en trésorerie à M7 |
| **D — Lever 250 k€ et refaire l'économie** | Rituel + réachat + création | **−19 838 €** | Trésorerie tenable jusqu'à M9 |

**Option A.** Pertes cumulées M1–M3 = 28 209 €. Le BFR se récupère sauf le stock :
15 333 € × (55 500 ÷ 36 800) = 23 124 €, soldé à 50 %, soit 11 562 € perdus. Total
**39 771 €** — le seul montant certain de tout ce cas.

**Option B.** EBITDA du mois 3 = −10 678 €. À volume gelé le BFR cesse de croître, donc
le brûlage tombe à l'EBITDA seul : 29 210 ÷ 10 678 = **2,7 mois**. Mort au mois 6, sans
un apprentissage de plus.

**Option C — celle qui tue.** Même volume que D, mais panier à 45,50 €, réachat à
4 % et nCAC dégradé à 37,61 € (le CAC marginal monte quand on passe de 768 à 3 400
nouveaux clients par mois — module 13 § 2.2) :

```
CA TTC      = 3 400 × 45,50 € + 142 × 72,00 €  = 164 900 €  (HT : 137 417 €)
Marge brute = 137 417 € × 58,8 %               =  80 801 €
Publicité   = 3 400 × 37,61 €                  = 127 889 €  (MER = 1,29)
EBITDA      = 80 801 − 127 889 − 28 000        = −75 088 €
```

Trésorerie : 161 873 € à M4, 86 786 € à M5, 11 698 € à M6, négative à M7. **Financer
une économie unitaire non réparée, c'est acheter trois mois de sursis à 250 000 €.**

**Option D.** C'est ce qui a été fait. Trois décisions, prises ensemble.

---

## 4. La décision et l'exécution, mois par mois

### 4.1 Le tableau des neuf mois

Montants en euros. **CA TTC = prix client ; toutes les autres colonnes sont HT.**
Apports : +90 000 € au mois 1, +250 000 € au mois 4.

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

Les deux lignes en gras sont les valeurs canoniques P1 et P2 (§ 2 et § 2.2). La part
de réachat moyenne est agrégée (réachats ÷ commandes) : 96 ÷ 2 400 = 4,00 % et
3 600 ÷ 24 000 = 15,00 %. Le MER moyen aussi : 1 381 200 ÷ 627 818 = 2,20.

### 4.2 Décision 1 — du produit unique au rituel en trois produits

Au mois 4, le Rituel Complet à 74,00 € TTC (sérum + shampooing + masque, § 1) devient
l'offre poussée en publicité ; le sérum seul reste disponible. Le panier de première
commande passe de **45,50 € à 55,00 € TTC** (§ 2), +20,9 %. Contrefactuel au palier
P2, panier maintenu à 45,50 € :

| | Sans le rituel | Avec le rituel | Écart |
| --- | ---: | ---: | ---: |
| CA TTC / mois | 197 900 € | 230 200 € | +32 300 € |
| Marge brute (58,8 % du HT) | 96 971 € | 112 798 € | +15 827 € |
| MER (publicité inchangée) | 1,89 | 2,20 | +0,31 |
| CM3 | −7 665 € | +8 162 € | +15 827 € |
| **EBITDA / mois** | **−35 665 €** | **−19 838 €** | **+15 827 €** |

**+94 962 € d'EBITDA sur les six mois de P2**, sans un euro de publicité en plus : on
achète le même client, on lui vend plus cher. Levier n° 1 du tableau canonique § 7.

### 4.3 Décision 2 — la relance de réachat calée sur la durée de consommation

Un flacon de sérum 50 ml dure environ **60 jours** à une pipette par jour
(*hypothèse produit*) : la séquence est calée sur J+45, J+58, J+70 — avant la rupture
d'usage, pas après. La part de commandes en réachat passe de **4 % à 15 %** (§ 2), en
montant de 7,0 % à 19,7 %. Contrefactuel : acquisition identique, réachat figé à 4 %,
soit 142 commandes au lieu de 600.

| | Réachat à 4 % | Réachat à 15 % | Écart |
| --- | ---: | ---: | ---: |
| Commandes / mois | 3 542 | 4 000 | +458 |
| CA TTC / mois | 197 200 € | 230 200 € | +33 000 € |
| MER | 1,88 | 2,20 | +0,32 |
| **EBITDA / mois** | **−36 008 €** | **−19 838 €** | **+16 170 €** |

**+97 020 € sur les six mois.** Ces 458 commandes n'ont coûté aucune publicité :
elles portent la marge brute entière, 35,28 € chacune (72,00 ÷ 1,20 × 58,8 %). Seule
ligne du cas où le CAC est nul.

### 4.4 Décision 3 — l'industrialisation créative

À P1, le fondateur produisait trois ou quatre publicités par semaine. À P2, le rythme
canonique est de **14 concepts testés par semaine pour 1,7 gagnant**, 9 gagnants en
rotation, 188 assets par mois (§ 6), financés par les 15 % du budget média réservés au
test — 3 622 € par semaine. Le MER passe de **1,80 à 2,20**. Contrefactuel : machine
restée artisanale, donc 3 400 nouveaux clients à **37,61 € pièce** au lieu de 30,78 €
(loi du CAC marginal croissant, module 13 § 2.2).

| | Sans industrialisation | Avec | Écart |
| --- | ---: | ---: | ---: |
| nCAC | 37,61 € | 30,78 € | −6,83 € |
| Publicité / mois | 127 889 € | 104 636 € | −23 253 € |
| MER | 1,80 | 2,20 | +0,40 |
| **EBITDA / mois** | **−43 091 €** | **−19 838 €** | **+23 253 €** |

**+139 515 € sur les six mois.** La plus grosse des trois.

### 4.5 Les trois ensemble

Sans aucune des trois décisions, l'EBITDA du palier P2 vaut **−75 088 € par mois**
(c'est l'option C du § 3), soit **−331 497 € sur les six mois**. Les trois effets sont
ici **exactement additifs** : 15 827 + 16 170 + 23 253 = 55 250 €, soit l'écart entre
l'EBITDA réel (−19 838 €) et ce contrefactuel total. Chacun agit sur un terme
différent — le panier, les commandes sans CAC, le coût d'acquisition — et la marge
brute est linéaire en chiffre d'affaires. **Ce n'est pas une loi générale :** dès
qu'un levier touche au taux de marge ou à la conversion, les effets se composent au
lieu de s'additionner.

---

## 5. Les résultats

### 5.1 Avant / après

| | M1 | M9 | Écart |
| --- | ---: | ---: | --- |
| Commandes | 420 | 6 300 | ×15,0 |
| Part de commandes en réachat | 0,0 % | 19,7 % | +19,7 pts |
| CA TTC / semaine | 4 410 € | 84 834 € | ×19,2 |
| Marge brute (CM2) | 9 109 € | 180 131 € | 57,2 % → 58,8 % |
| MER (pub : 12 300 € → 149 318 €) | 1,55 | 2,46 | +0,91 |
| CM3 en % du CA HT | −20,0 % | +10,1 % | **+30,1 pts** |
| EBITDA | −8 191 € | −10 187 € | −1 996 € |
| **EBITDA en % du CA HT** | **−51,4 %** | **−3,3 %** | **+48,1 pts** |

La ligne EBITDA en euros est **pire** à M9 qu'à M1 ; celle du dessous est meilleure de
48 points. Les deux sont vraies — c'est ce que produit une marque qui répare son
économie unitaire en accélérant. **Piloter la perte en euros pendant cette phase est
la meilleure façon de tuer une marque qui allait s'en sortir.**

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

BFR = ratio canonique du palier appliqué au CA TTC du mois : 21 603 ÷ 36 800 =
0,587038 pour P1, 104 462 ÷ 230 200 = 0,453788 pour P2 (§ 4). Contrôle :
0,453788 × 100 000 = 45 379 €, soit le « cash immobilisé par +100 k€ de CA mensuel »
du tableau canonique § 4.

**Le point bas de trésorerie est au mois 9 : 25 942 €.** Pas au mois 4, où la perte
est la plus lourde — au mois 9, où l'EBITDA est le meilleur de tout P2. À partir du
mois 6, l'EBITDA se répare de 25 471 € à 10 187 €, mais le BFR grossit de 21 309 € à
24 754 € par mois : **le financement de la croissance dépasse la réparation du compte
de résultat.** Au rythme du mois 9, il reste 25 942 ÷ 34 941 = **0,74 mois**.

### 5.3 Le chiffre à retenir

```
Pertes cumulées M1 → M9                   147 239 €
Besoin en fonds de roulement immobilisé   166 819 €
                                        -----------
CAPITAL CONSOMMÉ EN NEUF MOIS             314 058 €
```

Contrôle : la somme des neuf brûlages mensuels vaut aussi 314 058 €.

**314 058 € pour amener une marque de 0 à 84 834 € de CA TTC par semaine, toujours en
perte** — soit 8,5 % de l'objectif de 999 968 € par semaine du palier P5. Le BFR pèse
53 % du capital consommé : **plus de la moitié de l'argent brûlé n'est pas une perte,
c'est du stock et des encaissements en attente.** Récupérable, mais pas tant que tu
croîs.

---

## 6. Ce qui aurait pu mal tourner

**La levée du mois 4 ne se signe pas.** Sans les 250 000 €, la trésorerie du mois 4
vaut 90 000 − 51 896 − 48 447 = **−10 343 €** : défaut de paiement fournisseur. Tout
le cas repose sur un virement reçu à temps.

**La courbe de réachat plafonne à 8 % au lieu de 15 %** — scénario le plus probable :
le sérum plaît, mais la relance arrive après la rupture d'usage.

| | Réachat 8 % | Réachat 15 % |
| --- | ---: | ---: |
| CA TTC / mois (P2) | 208 287 € | 230 200 € |
| MER | 1,99 | 2,20 |
| CM3 | −2 576 € | +8 162 € |
| EBITDA / mois | −30 576 € | −19 838 € |

Écart : 10 738 €/mois, **64 424 € sur P2**. Le capital consommé passerait à
378 482 €, au-delà du plafond de 350 000 € posé au mois 1 (§ 6.1). **La règle d'arrêt
se déclencherait, et elle aurait raison.**

**Le MER de 2,20 est une illusion d'attribution.** Le MER se lit sur les ventes
totales, donc il est robuste — la *répartition* entre canaux, non (sur-attribution
canonique de 11 % au palier P5, § 5). Si le passage de 1,80 à 2,20 venait d'un
retargeting qui récolte des ventes déjà acquises, couper 20 % du budget ne coûterait
rien. Un test à faire, pas une hypothèse à croire — C06.

**La rupture de stock au mois 8.** Le stock est le premier poste du BFR. Une commande
fournisseur sous-dimensionnée au mois 6, sur un réapprovisionnement à huit ou dix
semaines, coupe la croissance là où la trésorerie ne supporte plus une reprise
ratée.

**Le rituel cannibalise au lieu d'ajouter.** Le panier monte de 20,9 %, mais si le
taux de conversion baisse de plus de 17,3 %, le CA net baisse :
1,209 × (1 − 0,173) = 1,000. Le seuil est étroit, et il se mesure.

### 6.1 À quel moment un fondateur rationnel aurait-il dû arrêter ?

La question honnête n'est pas « quand arrêter » mais « qu'avais-tu écrit avant de
commencer ». Le contrat qu'il fallait poser au mois 1, en quatre lignes :

```
CRITÈRE D'ARRÊT — écrit le premier jour, non renégociable

1. Capital total engagé plafonné à 350 000 €. Au-delà, on arrête.
2. Contrôle à M6, cohorte M1 devenue observable à 6 mois :
   LTV 6 mois en contribution ÷ nCAC >= 1,50. Sinon, arrêt.
3. Contrôle à M6 : MER du mois >= MER d'équilibre CM3 (2,04).
   Sinon, arrêt.
4. En permanence : trésorerie >= 2 mois de brûlage projeté. Sous
   2 mois sans tour signé à 30 jours, arrêt de l'acquisition
   payante le jour même — pas le mois suivant.
```

Confrontation aux faits :

| Ligne | Seuil | Réalisé | Verdict |
| --- | ---: | ---: | --- |
| 1. Capital engagé | ≤ 350 000 € | 340 000 € | Passe |
| 2. LTV 6 mois / nCAC (cohorte M1) | ≥ 1,50 | 41,59 ÷ 26,62 = **1,56** | Passe de 0,06 |
| 3. MER à M6 vs seuil CM3 | ≥ 2,04 | **2,05** | Passe de 0,01 |
| 4. Trésorerie en mois de brûlage | ≥ 2,0 | **0,74 à M9** | **Déclenche** |

**Réponse : il ne fallait pas arrêter, et il fallait quand même cesser de dépenser au
mois 9.** Les deux tests d'économie unitaire passent, d'un cheveu ; le test de
financement saute. Ce n'est pas la marque qui a échoué, c'est le plan de financement :
la levée du mois 4 était calibrée sur les pertes et pas sur le BFR, qui pèse 53 % du
besoin. **Il fallait lever 500 000 € au mois 4, pas 250 000 €.** Et retiens que le
point 2 est passé à 0,06 près, le point 3 à 0,01 près : ce cas se lit après coup comme
une réussite, il s'est joué à deux centièmes.

---

## 7. Le mécanisme généralisable

> **À retenir :** la vallée de la mort n'est pas un accident, c'est la structure
> normale d'une marque qui perd de l'argent sur la première commande. Elle se
> traverse avec du capital et une courbe de réachat, pas avec de la volonté.

Trois règles, dans cet ordre.

**1. Si ta marge de première commande est négative, ta perte est proportionnelle à ta
croissance.** Marge première commande = marge brute unitaire − nCAC ; chez NØRA,
21,69 − 26,62 = −4,93 €. Tant que ce nombre est négatif, chaque client creuse le trou,
et le seul indicateur qui décide est le CM3 — pas le chiffre d'affaires.

**2. Le capital nécessaire n'est pas la somme des pertes**, mais
`pertes cumulées + BFR de fin de période` : 147 239 + 166 819 = 314 058 €. Un plan qui
ne budgète que les pertes sous-estime le besoin de **113 %** (166 819 ÷ 147 239) —
mode de mort le plus fréquent des marques qui marchent.

**3. Le point bas de trésorerie arrive après le point bas du compte de résultat** —
trois mois après, ici. Tant que la croissance mensuelle du CA multipliée par le ratio
de BFR dépasse la réparation de l'EBITDA, le cash baisse pendant que tous les
indicateurs s'améliorent. **Le tableau de bord dit « on s'en sort » pendant que la
banque dit « il reste trois semaines ». Les deux ont raison.**

Corollaire : on ne sort pas de la vallée en coupant les coûts, mais par trois leviers
— le panier de première commande, les commandes sans CAC, le coût d'acquisition :
+15 827 €, +16 170 €, +23 253 € par mois. Les frais fixes, eux, ont été **multipliés
par 8,2** (5 000 € → 41 000 €), et c'était juste : ils ont financé la machine
créative, qui a rapporté le plus.

---

## 8. Questions

1. Calcule le capital total consommé sur M1–M9 et décompose-le en deux postes. Lequel
   est récupérable, et sous quelle condition ?
2. À la fin du mois 9, combien de mois de trésorerie reste-t-il au rythme de brûlage
   de ce mois-là ? Déroule.
3. Le MER d'équilibre CM3 de P2 vaut 2,04. À quel mois NØRA le franchit-elle, et que
   vaut alors le CM3 ?
4. Sans la relance de réachat (part figée à 4 %, acquisition inchangée), quel serait
   l'EBITDA mensuel du palier P2 ? Déroule.
5. À P2, combien de commandes de réachat par mois faudrait-il pour que l'EBITDA soit
   nul, à acquisition et frais fixes inchangés ? Exprime-le en part de commandes en
   réachat, et dis à quel palier canonique cela correspond.
6. Au mois 10, le fondateur veut ajouter 100 000 € de CA TTC mensuel. Quelle
   trésorerie faut-il mobiliser ? L'EBITDA du mois 9 le finance-t-il ?
7. Écris le critère d'arrêt qu'il fallait poser au mois 1. Laquelle de ses lignes
   saute, et à quel mois ?

---

## 9. Corrigé des questions

**1.** Pertes cumulées M1–M9 = **147 239 €** (colonne EBITDA du § 4.1). BFR au 31 du
mois 9 = **166 819 €**. Capital consommé = 147 239 + 166 819 = **314 058 €** ; la
somme des neuf brûlages du § 5.2 donne le même montant. Le BFR (53,1 % du total) est
**récupérable, à la seule condition de cesser de croître.** C'est pourquoi une marque
en difficulté paraît soudain riche le trimestre où elle s'arrête. C'est un mirage.

**2.** Brûlage du mois 9 = EBITDA − ΔBFR = −10 187 − 24 754 = **−34 941 €**, donc
25 942 ÷ 34 941 = **0,74 mois**, soit 23 jours. En divisant par le seul EBITDA
(2,5 mois), on se croirait trois fois plus riche. **Le brûlage n'est pas la perte.**

**3.** Au **mois 6**, MER de 2,05 contre un seuil de 2,04. Le CM3 vaut alors
95 029 − 94 500 = **+529 €**, premier mois positif de l'histoire de la marque : six
mois et 102 848 € de pertes cumulées pour que la publicité cesse de coûter plus que
la marge qu'elle rapporte — et il reste 26 000 € de frais fixes à couvrir.

**4.** Acquisition inchangée (3 400 nouveaux clients, 104 636 € de publicité), donc
réachats = 3 400 × 0,04 ÷ 0,96 = **142 commandes** au lieu de 600.

```
CA TTC      = 3 400 × 55,00 € + 142 × 72,00 €  = 197 200 €
CA HT       = 197 200 ÷ 1,20                   = 164 333 €
Marge brute = 164 333 € × 58,8 %               =  96 628 €
CM3         = 96 628 € − 104 636 €             =  −8 008 €
EBITDA      = −8 008 € − 28 000 €              = −36 008 €
```

Contre −19 838 € réels : **16 170 € par mois, 97 020 € sur le palier.** Le MER
retombe à 197 200 ÷ 104 636 = 1,88, sous le seuil CM3 de 2,04.

**5.** EBITDA nul ⇒ CM3 = frais fixes = 28 000 €, donc marge brute nécessaire =
28 000 + 104 636 = **132 636 €**.

```
CA HT requis  = 132 636 ÷ 0,588            = 225 572 €
CA TTC requis = 225 572 × 1,20             = 270 686 €
CA TTC manquant                            =  40 486 €
Réachats supplémentaires = 40 486 ÷ 72,00  =     562
Réachats totaux = 600 + 562                =   1 162
Part de réachat = 1 162 ÷ (3 400 + 1 162)  =   25,5 %
```

Il faudrait **25,5 % de commandes en réachat** contre 15 % à P2. Le palier qui porte
ce niveau est **P3 (27 %)** — précisément celui où l'EBITDA canonique devient positif
(+5,2 %). **NØRA ne sort pas de la vallée par le volume, elle en sort par la
rétention.**

**6.** Ratio de BFR du palier P2 : 0,453788 du CA TTC. Pour +100 000 € de CA TTC
mensuel, 0,453788 × 100 000 = **45 379 €** immobilisés (tableau canonique § 4).
L'EBITDA du mois 9 vaut **−10 187 €** : il ne finance rien, il aggrave. Besoin total
45 379 + 10 187 = **55 566 €**, pour une croissance de 100 000 ÷ 367 614 = **27,2 %**,
contre 25 942 € disponibles. **La croissance que le compte de résultat rend désirable
est financièrement impossible** — la faillite technique d'une marque en bonne santé.

**7.** Voir l'encadré du § 6.1 : plafond de capital à 350 000 € ; LTV 6 mois ÷ nCAC
≥ 1,50 à M6 ; MER ≥ MER d'équilibre CM3 à M6 ; trésorerie ≥ 2 mois de brûlage en
permanence. **C'est la ligne 4 qui saute, au mois 9**, à 0,74 mois — les lignes 2 et 3
passant de 0,06 et de 0,01, la ligne 1 à 10 000 € près. Conclusion : non pas « il
fallait arrêter » mais **« il fallait lever deux fois plus au mois 4 »**. La levée de
250 000 € était calibrée sur les pertes et ignorait le BFR, soit 53 % du capital
réellement consommé.

---

*Fin du cas C02. Suite : [E10](../modules/E10-cash-et-operations.md) pour le pilotage
du BFR, [E08](../modules/E08-retention-et-ltv.md) pour la courbe de réachat, et
[C04](C04-scale-qui-detruit-la-marge.md) pour le même mécanisme à 41 M€ de CA.*
