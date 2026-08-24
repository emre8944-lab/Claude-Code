# Module E08 — La rétention, les cohortes et la LTV

> **Prérequis :** [E01](E01-arithmetique-de-la-marque.md), [E02](E02-marche-et-produit.md), [E03](E03-offre-et-prix.md), [E07](E07-funnel-et-conversion.md).
> **Objet :** construire et lire un tableau de cohortes, calculer une LTV en marge qui tient devant un banquier, et piloter les leviers qui font revenir un client.
> **Temps de travail :** ~5 h (lecture + exercices)

---

## 0. Pourquoi ce module existe

Ouvre les [chiffres canoniques](../donnees/chiffres-canoniques.md) au § 2.4, dernière colonne. Aux cinq paliers, sans exception, la marge de NØRA sur la **première** commande est négative : −4,93 € en P1, −3,83 € en P2, −3,01 € en P3, −6,06 € en P4, **−7,26 € en P5**.

En P5, ce n'est pas une nuance comptable, c'est toute l'entreprise :

```
Contribution des réachats     22 876 × 43,53 €     =   995 792 €/mois
Première commande nette du CAC  37 324 × (−7,26 €) =  −270 972 €/mois
Frais fixes (§ 2.5)                                =  −360 000 €/mois
                                                      ───────────────
EBITDA                                             =   364 820 €/mois
```

Le canonique donne 364 752 € (§ 2.2) ; l'écart de 68 € vient des arrondis unitaires. **Le compte de résultat de NØRA se reconstruit intégralement à partir de deux nombres : le réachat et le CAC.**

Coupe le réachat. Même produit, même publicité, mêmes 37 324 clients acquis par mois, mais aucun ne repasse commande :

```
EBITDA annuel sans réachat = (−270 972 − 360 000) × 12 = −7 571 667 €
EBITDA annuel réel (§ 7)                               = +4 377 023 €
Écart = 11 948 690 € = exactement la contribution de réachat
```

Une marque DTC qui achète son trafic sans réachat n'est pas une marque à faible marge : c'est une marque qui n'existe pas, qui finance la croissance de sa régie publicitaire avec le capital de ses actionnaires. La rétention n'est pas le chapitre qu'on ajoute quand l'acquisition tourne. **C'est le seul endroit du modèle où il y a de l'argent.**

---

## 1. La cohorte, proprement définie

### 1.1 Définition

Une **cohorte** est un groupe de clients acquis pendant la même période — le mois de leur **première** commande — et suivi ensuite sans jamais changer de composition. Un client entre dans une cohorte et une seule, le jour de sa première commande, et il y reste même quand il cesse d'acheter. C'est parce qu'on le garde au dénominateur que la mesure est honnête.

Deux axes à ne jamais confondre : l'**âge** de la cohorte (mois depuis l'acquisition, noté M+1, M+3…) et le **mois calendaire** (janvier, février). Tout le pouvoir de la méthode vient de leur séparation.

### 1.2 Pourquoi la moyenne globale ment

Marque en croissance, trois cohortes, courbe de réachat canonique (§ 3) : 1,24 réachat par client à 12 mois, 0,72 à 6 mois, 0,06 à 1 mois.

| Cohorte | Âge | Clients | Réachats/client | Réachats |
| --- | ---: | ---: | ---: | ---: |
| A | 12 mois | 1 000 | 1,24 | 1 240 |
| B | 6 mois | 4 000 | 0,72 | 2 880 |
| C | 1 mois | 16 000 | 0,06 | 960 |
| **Total** | | **21 000** | | **5 080** |

```
Moyenne globale = 5 080 ÷ 21 000 = 0,242 réachat par client
LTV contribution = 32,77 € + 0,242 × 43,53 € = 43,30 €
LTV / nCAC = 43,30 ÷ 40,03 = 1,08
```

Le pilote qui lit 1,08 applique la règle canonique du § 3 (« LTV/CAC 12 mois < 1,5 : on ne scale pas, on répare ») et coupe le budget. Il vient de tuer une marque dont la cohorte mature est à 1,24 réachat, 86,75 € de LTV, ratio **2,17**.

Inverse les effectifs — 16 000 en A, 4 000 en B, 1 000 en C — sans rien changer d'autre : moyenne globale 1,085 réachat, LTV 80,00 €, ratio **2,00**.

**Le même business affiche 1,08 quand il croît et 2,00 quand il décroît.** La moyenne globale ne mesure pas la rétention, elle mesure la forme de ta courbe d'acquisition. Elle te félicite quand tu meurs et te punit quand tu gagnes. Dans une cohorte, tous les clients ont le même âge : ce biais-là disparaît.

### 1.3 Construire le tableau

**Maille :** le mois par défaut ; la semaine si ton cycle de consommation est sous 30 jours ; le trimestre seulement sous 300 clients/mois, en dessous le bruit dépasse le signal.

**Valeur dans la cellule :** quatre candidates, deux bonnes.

| Valeur | Ce qu'elle mesure | Verdict |
| --- | --- | --- |
| CA cumulé TTC par client | Rien d'exploitable | À proscrire — § 8, erreur 7 |
| Commandes cumulées par client | La fréquence, diluée par le « 1 » de départ | Acceptable pour un rapport |
| **Réachats cumulés par client** | Exactement ce que tu pilotes | **Celle-là** |
| Contribution cumulée par client | La décision d'investissement | La seconde à tenir |

La première commande vaut 1 pour tout le monde, par construction : elle écrase les variations. Une cohorte passée de 1,34 à 1,30 commande cumulée à M+3 a l'air d'avoir perdu 3 % ; en réachats, elle est passée de 0,34 à 0,30, soit **−11,8 %**. Même fait, quatre fois plus lisible.

**Dénominateur :** le nombre de clients **acquis**, figé pour toujours. Pas les clients « encore actifs » — ce dénominateur-là fabrique de la rétention à partir de rien.

### 1.4 Lire dans les trois directions

Réachats cumulés par client, cohortes M31 à M36 (début de P5). Les jalons 1, 3 et 6 mois viennent du § 3 ; les mois intermédiaires sont interpolés linéairement, ce qui donne la trajectoire de référence **0,06 / 0,20 / 0,34 / 0,47 / 0,59 / 0,72**.

| Cohorte | M+1 | M+2 | M+3 | M+4 | M+5 | M+6 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| M31 | 0,06 | 0,20 | 0,34 | 0,47 | 0,59 | 0,72 |
| M32 | 0,06 | 0,19 | 0,33 | 0,45 | 0,57 | — |
| M33 | 0,05 | 0,18 | 0,32 | 0,44 | — | — |
| M34 | 0,05 | 0,17 | 0,30 | — | — | — |
| M35 | 0,04 | 0,15 | — | — | — | — |
| M36 | 0,04 | — | — | — | — | — |

**Le long d'une ligne — la maturation.** M31 accumule 0,72 réachat en six mois sur les 1,24 de sa première année : **58 % des réachats de l'année arrivent dans les six premiers mois** (0,72 ÷ 1,24). Donc tu peux juger une cohorte bien avant sa maturité — le pilotage devient possible. Et ce qui n'est pas gagné à M+6 ne se rattrape presque plus : 0,087 réachat par mois entre M+7 et M+12, contre 0,14 entre M+1 et M+3.

**Le long d'une colonne — la qualité des cohortes successives.** Colonne M+3 : 0,34 → 0,33 → 0,32 → 0,30. Quatre cohortes consécutives sous la précédente au même âge. Ce n'est plus du bruit, c'est une pente. C'est la lecture qui décide.

**La diagonale — les effets de période.** Les cellules atteintes le même mois calendaire forment une diagonale : en M36 tu observes M31 à M+5, M32 à M+4, M33 à M+3, M34 à M+2, M35 à M+1. Un événement qui frappe **le mois** — rupture de stock sur le produit héros, bug de paiement, gueule de bois post-soldes — fait décrocher toute la diagonale d'un coup, et les colonnes se rétablissent le mois suivant. **Diagonale = période, colonne = cohorte.** C'est le premier tri à faire et il coûte cinq minutes.

---

## 2. Le signal d'alarme numéro un

### 2.1 Ce qu'il coûte

Colonne M+3 : 0,34 pour M31, 0,30 pour M34, soit −11,8 %. Propagation constante jusqu'à 12 mois — hypothèse la plus prudente, elle n'invente aucune aggravation :

```
Réachats 12 mois : 1,24 × (1 − 0,118)          = 1,094
LTV contribution : 32,77 € + 1,094 × 43,53 €   = 80,38 €
LTV / nCAC : 80,38 ÷ 40,03                     = 2,01
```

Tu passes de 2,17 à 2,01 : encore au-dessus du seuil canonique de 2,0, mais de 0,01, et la cohorte M35 n'a pas fini d'arriver. En euros, via le levier canonique du § 7 (+10 % de commandes de réachat = 1 194 871 € d'EBITDA annuel) :

```
1 194 871 € × 1,18 = 1 409 948 € d'EBITDA annuel
soit 32,2 % de l'EBITDA de référence (4 377 023 €)
```

**Quatre cohortes mensuelles viennent d'effacer un tiers de l'EBITDA annuel, et le compte de résultat du mois ne montre rien.** Il ne montrera rien pendant six à douze mois, parce que les réachats manquants sont des réachats futurs. C'est pour ça que le tableau de cohortes existe : c'est le seul instrument du tableau de bord qui soit en avance sur le résultat.

### 2.2 Les trois causes, et comment les distinguer

| | Saturation de l'audience | Dérive du produit | Dérive de la promesse |
| --- | --- | --- | --- |
| **Mécanisme** | Les acheteurs faciles sont épuisés ; l'algorithme va chercher des profils de plus en plus éloignés du cœur | Formule, fournisseur, lot ou emballage ont changé, ou la qualité a glissé sans que personne l'écrive | La créa promet plus que le produit ne tient, pour tenir le CPA |
| **Forme de la chute** | Lente, régulière, corrélée à la hausse du budget | Brutale et **datée** : toutes les cohortes après une date précise, tous canaux confondus | Progressive, limitée aux cohortes issues des nouveaux concepts |
| **nCAC** | **Monte** | Stable | **Baisse** — la sur-promesse convertit mieux |
| **Retours et SAV** | Stables | **Montent** dans la même fenêtre | Montent au premier usage, pas à la livraison |
| **Test qui tranche** | Cohorter par canal : si Google Search marque tient et que la prospection large s'effondre, c'est la saturation | Croiser la date de bascule avec les numéros de lot et les changements de fournisseur | Cohorter par **concept créatif** ; verbatims SAV : « ce n'est pas ce qui était montré » |
| **Réponse** | Élargir l'offre, monter l'AOV, ouvrir un marché — [E11](E11-passage-a-echelle.md) | Arrêter, corriger, rappeler les lots | Réécrire la promesse, tuer les concepts — [E05](E05-machine-creative.md) |

La ligne décisive est la troisième. **Un nCAC qui baisse pendant que la rétention baisse est une signature unique** : la saturation fait monter le CAC, la dérive produit le laisse tranquille. Si ton coût d'acquisition s'améliore pendant que tes cohortes se dégradent, tu n'as pas trouvé un bon angle — tu as trouvé un mensonge rentable à court terme, et tu le paieras sur douze mois de réachat, au prix calculé en § 2.1.

Un quatrième suspect à écarter avant les trois autres : le **mix promotionnel**. Une cohorte acquise pendant une semaine à −30 % contient une proportion anormale de chasseurs de remise, qui ne rachètent qu'en promotion. Ce n'est pas une dérive, c'est une composition. Test : cohorter selon la présence d'un code promo sur la première commande. Voir [C09](../etudes-de-cas/C09-piege-du-black-friday.md).

---

## 3. La courbe de réachat canonique, chiffre par chiffre

### 3.1 Ce que dit le § 3

Base : nCAC **40,03 €**, contribution de la première commande **32,77 €**, contribution d'un réachat **43,53 €**.

| Horizon | Réachats/client | LTV contribution | LTV / nCAC |
| --- | ---: | ---: | ---: |
| 1 mois | 0,06 | 35,38 € | 0,88 |
| 3 mois | 0,34 | 47,57 € | 1,19 |
| 6 mois | 0,72 | 64,11 € | 1,60 |
| 12 mois | 1,24 | 86,75 € | 2,17 |
| 24 mois | 1,98 | 118,96 € | 2,97 |
| 36 mois | 2,42 | 138,11 € | 3,45 |

Sache reconstruire chaque ligne, sinon tu ne pourras jamais la contester : `32,77 + 1,24 × 43,53 = 86,75 €`, puis `86,75 ÷ 40,03 = 2,17`.

### 3.2 Deux chiffres non publiés, que tu peux dériver

Le § 3 donne le CA cumulé TTC : 69,10 € à 1 mois, 169,40 € à 12 mois. Deux équations, deux inconnues.

```
169,40 − 69,10 = (1,24 − 0,06) × AOV réachat
100,30 = 1,18 × AOV réachat        →  AOV réachat  = 85,00 € TTC
AOV 1ʳᵉ commande = 69,10 − 0,06 × 85,00 = 64,00 € TTC
```

Contrôle sur le § 2 : 37 324 × 64,00 € + 22 876 × 85,00 € = 2 388 736 € + 1 944 460 € = **4 333 196 €**, exactement le CA TTC mensuel de P5. Second contrôle : (85,00 ÷ 1,2) × 61,45 % = 43,53 €, la contribution de réachat canonique — 61,45 % étant la somme exacte des lignes du § 2.1, que le tableau arrondit à 61,5 %.

**Le panier de réachat dépasse de 33 % le panier d'acquisition** (85,00 € contre 64,00 €). C'est la raison pour laquelle un réachat rapporte 43,53 € de contribution quand une première commande n'en rapporte que 32,77 € : un client qui revient achète le rituel entier, pas le produit d'appel.

### 3.3 Ce que le payback autorise

```
Contribution cumulée à M+1 : 35,38 €  (sous le CAC de 40,03 €)
Contribution cumulée à M+3 : 47,57 €  (au-dessus)
1 + (40,03 − 35,38) ÷ (47,57 − 35,38) × 2 = 1,76 mois → ≈ 1,8 mois
```

Il ne faut pas 1,24 réachat pour rembourser l'acquisition. Il en faut :

```
7,26 € de déficit ÷ 43,53 € = 0,167 réachat par client acquis
```

**Un client sur six qui repasse une seule commande, et l'acquisition est remboursée.** Tout le reste de la courbe est du profit net d'acquisition. C'est ce qui rend le modèle si sensible au **premier** réachat et si peu sensible aux suivants — section 4.

| Nombre | P5 | Ce qu'il autorise |
| --- | ---: | --- |
| Payback | 1,8 mois | Financer l'acquisition avec ~2 mois de trésorerie roulante. Avec 45 à 60 jours de crédit fournisseur, la croissance est presque autofinancée en marge — pas en stock, voir [E10](E10-cash-et-operations.md) |
| LTV/CAC 12 mois | 2,17 | Au-dessus de 2,0 : on accélère. Marge de sécurité de 8 % seulement |
| LTV/CAC 24 mois | 2,97 | Ce qu'on montre à un prêteur, si les 24 mois sont observés et non extrapolés |
| Réachats 12 → 24 mois | 1,24 → 1,98 | +0,74 réachat, soit +32,21 € par client. C'est le prix d'attendre : l'argent est immobilisé |

Le ratio de 3,45 à 36 mois est vrai et inutile pour décider : une décision d'achat média se prend sur l'argent qui revient avant que tu doives le redépenser. **Pilote sur 12 mois, publie sur 24, ne décide jamais sur 36.**

---

## 4. Le premier réachat est le seul qui compte vraiment

### 4.1 La démonstration

Le canonique donne un total (1,24 réachat à 12 mois) mais pas sa décomposition. *Hypothèse déclarée :* je pose le taux de passage de la commande 1 à la commande 2 à **44 %** et je choisis les taux conditionnels suivants de sorte que la somme des probabilités cumulées reproduise **exactement** le 1,24 canonique. Le total est contraint par le § 3 ; seule la répartition est un choix de modélisation.

| Passage | Probabilité cumulée d'atteindre ce rang | Taux conditionnel |
| --- | ---: | ---: |
| Commande 1 → 2 | 0,44 | **44,0 %** |
| Commande 2 → 3 | 0,29 | 65,9 % |
| Commande 3 → 4 | 0,20 | 69,0 % |
| Commande 4 → 5 | 0,14 | 70,0 % |
| Commande 5 → 6 | 0,10 | 71,4 % |
| Commande 6 → 7 | 0,07 | 70,0 % |
| **Somme** | **1,24** | |

Le premier passage est à 44 %, tous les suivants entre 66 % et 71 %. **Le premier réachat est une fois et demie plus difficile que tous les autres**, et l'écart n'est pas un accident de calibrage : un client qui a commandé deux fois a vérifié que le produit marche, que le colis arrive et que le SAV répond. Il n'a plus rien à découvrir. Un client qui a commandé une fois n'a encore rien vérifié.

### 4.2 Ce que vaut un point

À taux conditionnels constants, le total est proportionnel au premier passage :

```
K = 1,24 ÷ 0,44 = 2,8182
44 % → 45 % : 0,45 × 2,8182 = 1,268 réachat
Gain : +0,028 réachat par client acquis, soit +2,27 %
Levier canonique § 7 : 1 194 871 € × (2,27 ÷ 10) = 271 562 €
```

> **À retenir :** **un point de taux de premier réachat vaut 271 562 € d'EBITDA par an au palier P5**, soit 6,2 % de l'EBITDA. Trois points valent 814 663 €, soit 18,6 %. Ces points ne coûtent aucun euro de publicité.

Le levier « +10 % de réachat » du § 7, qui pèse 27,3 % de l'EBITDA, ne demande donc pas un miracle : il demande **4,4 points de premier réachat** (44 % → 48,4 %). C'est un chantier de trimestre.

### 4.3 Les leviers, par ordre d'efficacité

L'ordre compte plus que la liste : les quatre premiers ne coûtent presque rien en marketing, et c'est sur le cinquième que tout le monde se jette.

| Rang | Levier | Pourquoi là |
| ---: | --- | --- |
| 1 | **L'expérience produit** | Elle plafonne tous les autres : si ton produit satisfait 55 % de tes acheteurs, ton premier réachat ne dépassera pas durablement 55 %. Mesure-le — enquête à J+30, une question, une note sur 10 — et traite ce chiffre comme le plafond sous lequel toute la section 5 travaille |
| 2 | **La livraison** | Première promesse tenue ou trahie, avant même l'essai. L'écart entre délai promis et délai réel compte plus que le délai : annoncer 5 jours et livrer en 4 satisfait davantage qu'annoncer 2 et livrer en 3 — [E10](E10-cash-et-operations.md) |
| 3 | **Le contenu d'accompagnement** | Un soin mal dosé ne donne pas de résultat. Le flux post-achat ne vend pas, il **fait réussir l'usage** : dose, fréquence, trois erreurs courantes, et le résultat attendu à la semaine 6 pour que le client ne conclue pas trop tôt. Meilleur rapport effort/rendement du module, et le plus négligé — il ne produit aucune vente attribuée le jour de l'envoi |
| 4 | **Le moment de la relance** | Calé sur la durée de consommation réelle (§ 4.4). Levier de timing, pas de message : le même e-mail au bon et au mauvais moment n'a pas le même rendement, à un facteur qui se compte en multiples |
| 5 | **L'offre de réapprovisionnement** | Réassort en un clic du produit exact. Efficace, et volontairement dernier : une remise à qui n'a pas eu de résultat ne produit rien, et une remise à qui allait racheter au prix fort te coûte la remise — § 7.2 |

### 4.4 Le calendrier de consommation

**On ne relance pas après un délai, on relance avant une date d'épuisement.** Un délai est un chiffre recopié d'un article de blog ; une date d'épuisement se calcule. Dérivation sur la gamme canonique (§ 1) — les dosages sont des *hypothèses*, contrôlées par le fait que le canonique vend une « Cure 3 mois » composée de 3 sérums, ce qui fixe la durée d'un sérum à un mois.

| Produit | Contenance | Dosage (hypothèse) | Épuisement |
| --- | ---: | --- | ---: |
| Sérum Densité | 50 ml | 1,6 ml/jour | **31 jours** |
| Shampooing Fortifiant | 250 ml | 10 ml × 3 lavages/semaine | **58 jours** |
| Masque Réparateur | 200 ml | 15 ml × 1 application/semaine | **93 jours** |
| Rituel Complet | les 3 | premier vide : le sérum | **31 jours** |
| Cure 3 mois | 3 sérums | 3 × 31 jours | **93 jours** |

Contrôle : 50 ÷ 1,6 = 31,3 jours, cohérent avec les 3 mois annoncés pour 3 sérums.

Le mix des premières commandes doit reproduire l'AOV d'acquisition de 64,00 € TTC (§ 3.2). *Hypothèse contrainte :*

```
0,25 × 39,00 € (Sérum seul)      =  9,75 €
0,42 × 74,00 € (Rituel Complet)  = 31,08 €
0,20 × 99,00 € (Cure 3 mois)     = 19,80 €
0,08 × 24,00 € (Shampooing seul) =  1,92 €
0,05 × 29,00 € (Masque seul)     =  1,45 €
                                   ───────
                                    64,00 €
```

La date d'épuisement moyenne pondérée du premier article vide vaut alors :

```
0,25×31 + 0,42×31 + 0,20×93 + 0,08×58 + 0,05×93 = 48,7 jours
```

**Ne relance jamais à J+49.** Ce délai « moyen » arrive 18 jours trop tard pour 67 % de la base (sérum et rituel, vides à J31) et 44 jours trop tôt pour 25 % (cure et masque, vides à J93). Il ne tombe juste pour personne : c'est le défaut structurel de toute relance calée sur la moyenne d'une distribution bimodale.

Le calendrier correct est **par référence achetée**, déclencheur à 78 % du cycle — assez tôt pour que le colis arrive avant le dernier usage, assez tard pour que le besoin soit réel.

| Panier de la 1ʳᵉ commande | Relance 1 | Relance 2 | Relance 3 |
| --- | ---: | ---: | ---: |
| Sérum seul | J+24 | J+31 | J+38 |
| Rituel Complet | J+24 (sérum) | J+45 (shampooing) | J+72 (masque) |
| Shampooing seul | J+45 | J+58 | J+70 |
| Masque seul, Cure 3 mois | J+72 | J+93 | J+110 |

Le Rituel n'a pas une date d'épuisement mais trois, et la relance de J+24 ne propose **que** le sérum : proposer le rituel entier à quelqu'un qui a encore 90 % de son masque, c'est lui demander de payer pour du stock qu'il possède déjà.

---

## 5. E-mail et SMS

### 5.1 L'ordre de grandeur, et le piège

*Ordre de grandeur déclaré :* pour une marque DTC consommable en bonne santé, l'e-mail et le SMS se voient attribuer, en dernier clic, **22 à 30 % du chiffre d'affaires**. Fourchette d'observation sectorielle, pas chiffre canonique. Prends 25 % pour NØRA en P5 :

```
CA attribué dernier clic : 0,25 × 4 333 196 € = 1 083 299 € TTC/mois
```

Un e-mail de réapprovisionnement envoyé à quelqu'un dont le flacon est vide s'attribue une vente qui allait avoir lieu. Le dernier clic ne l'invente pas, il la **récolte**. *Hypothèse :* 45 % de ce CA est incrémental — protocoles dans [E09](E09-mesure-et-incrementalite.md), le seul honnête étant la retenue aléatoire.

```
CA incrémental     : 1 083 299 × 0,45 = 487 485 € TTC/mois
CA non incrémental : 1 083 299 × 0,55 = 595 814 € TTC/mois
Contribution incrémentale : (487 485 ÷ 1,2) × 61,45 % = 249 633 €/mois
```

Contrôle : 249 633 € font 25,1 % des 995 792 € de contribution de réachat mensuelle (§ 0). Cohérent — **l'e-mail n'est pas une source de CA supplémentaire, c'est le canal d'exécution du réachat.** Il ne s'additionne pas à la rétention, il la réalise.

Les 595 814 € restants sont le danger : ils apparaissent au tableau de bord comme du CA « e-mail », servent à justifier un budget, et surtout servent à justifier une coupe ailleurs — « l'e-mail nous fait 25 % du CA à coût quasi nul, réduisons Meta ». Réduis Meta et tu réduis, six mois plus tard, la base à qui l'e-mail parle. **Un canal de récolte ne peut pas financer sa propre semence.**

### 5.2 Les flux automatisés

| Flux | Déclencheur | Msg | Délais | Contenu |
| --- | --- | ---: | --- | --- |
| **Bienvenue** | E-mail capté, aucune commande | 4 | +15 min, J+1, J+3, J+6 | Preuve (avant/après, composition), objection prix, « est-ce que ça marche sur mes cheveux », offre d'entrée au dernier message seulement |
| **Panier abandonné** | Ajout au panier, rien sous 1 h | 3 + 1 SMS | +1 h, +20 h, +48 h ; SMS +4 h | Produit exact, levée de risque (retour, garantie), avis client. Remise **au troisième message uniquement**, et pas systématiquement |
| **Navigation abandonnée** | ≥ 2 vues d'une fiche, pas d'ajout | 2 | +4 h, +36 h | Le produit vu, sa preuve, la question qu'il se pose à ce stade |
| **Post-achat / onboarding** | Commande expédiée | 4 | J+0, jour de livraison, +3, J+21 | Suivi, dose et fréquence exactes, 3 erreurs d'usage, résultat attendu à S6, demande d'avis |
| **Réapprovisionnement** | Date d'épuisement par référence (§ 4.4) | 3 | 78 %, 100 %, 118 % du cycle | Le produit déjà acheté, réassort en un clic, montée en cure |
| **Réactivation** | Rien depuis 2 cycles | 3 | J+0, J+6, J+14 | Nouveauté, preuve renouvelée, offre de retour au dernier message |
| **Anniversaire** | Anniversaire ou date de 1ʳᵉ commande | 1 | J+0 | Geste non monétaire de préférence : accès anticipé, format exclusif |

**Deux classements, pas un.** Par euro et par destinataire : panier abandonné > navigation abandonnée > réapprovisionnement > bienvenue > post-achat > réactivation > anniversaire. Par euro **total** : bienvenue > réapprovisionnement > panier abandonné > post-achat > navigation abandonnée > réactivation > anniversaire. La différence tient au volume d'entrées. **C'est le second classement qui paie tes salaires** — l'erreur courante est d'optimiser trois semaines le panier abandonné, qui affiche les plus beaux taux du compte, pendant que le flux de réapprovisionnement n'existe pas.

Chiffrons ce dernier, directement branché sur la section 4 :

```
Entrées : 60 200 commandes livrées/mois (§ 2)
Hypothèses : 6,5 % de réachats produits sur les entrées, dont 40 % incrémentaux
60 200 × 0,065 × 0,40 = 1 565 commandes incrémentales/mois
1 565 × 43,53 € = 68 134 €/mois → 817 608 €/an, soit 18,7 % de l'EBITDA de P5
```

Un flux, sept messages, écrits une fois.

### 5.3 Campagnes, pression et coût d'une désinscription

Les flux sont déclenchés par un comportement ; les campagnes sont envoyées parce que c'est jeudi. Elles n'ont ni la même économie ni le même coût caché.

*Hypothèses :* 400 000 abonnés actifs (une ouverture sur 180 jours) ; une campagne de pression supplémentaire produit 0,08 € TTC par envoi, sous la moyenne du programme puisqu'elle est marginale ; elle porte la désinscription de l'envoi à 0,25 %.

```
Valeur d'un abonné : 249 633 € ÷ 400 000 = 0,624 €/mois → 7,49 €/an

La campagne rapporte
  400 000 × 0,08 € = 32 000 € TTC
  contribution : (32 000 ÷ 1,2) × 61,45 % = 16 387 €
  incrémentale à 45 %                     =  7 374 €  une fois

La campagne coûte
  désinscriptions : 400 000 × 0,25 % = 1 000 abonnés
  valeur perdue : 1 000 × 7,49 €     =  7 490 €  par an, chaque année
```

**7 374 € encaissés une fois contre 7 490 € détruits chaque année**, sans compter l'effet délivrabilité. C'est la réponse arithmétique à la tentation universelle — le mois est mauvais, on ajoute deux envois : tu déplaces du chiffre d'affaires du futur vers le présent et tu détruis une part du futur au passage.

Le SMS a en plus un coût direct. *Hypothèse :* 0,045 € par SMS en Europe.

```
Envoi à toute la base : 400 000 × 0,045 € = 18 000 €
CA TTC nécessaire pour le couvrir : (18 000 ÷ 61,45 %) × 1,2 = 35 151 €
soit 0,088 € TTC par SMS en incrémental
soit 0,195 € TTC par SMS en dernier clic (à 45 % d'incrémentalité)
```

Barre que peu de campagnes franchissent. **Le SMS n'est pas un canal de masse, c'est un canal de déclencheur** : réapprovisionnement, panier abandonné, retour en stock, et les segments à forte valeur du § 7.1. Jamais la base entière.

### 5.4 La délivrabilité est un actif, et elle se détruit vite

Depuis février 2024, Google et Yahoo imposent aux expéditeurs de masse — plus de 5 000 messages par jour vers leurs domaines — l'authentification SPF, DKIM et DMARC, la désinscription en un clic et un taux de plainte spam sous 0,3 %, avec 0,1 % en cible recommandée (exigences publiées par Google et Yahoo, 2024). Faits publics, pas bonnes pratiques.

Le mécanisme : les filtres notent ton domaine sur **l'engagement de tes destinataires**. Envoyer à des adresses mortes abaisse l'engagement global, donc la note, donc le placement en boîte de réception de **tous** tes messages, flux rentables compris. *Hypothèse :* tu envoies à 700 000 adresses au lieu de 400 000 actives et ton placement passe de 92 % à 78 %.

```
Perte de placement : 14 ÷ 92 = 15,2 % des messages délivrés
0,152 × 249 633 € = 37 944 €/mois → 455 330 €/an de contribution
```

**455 330 € par an détruits pour écrire à 300 000 personnes qui ne t'ouvrent plus.** L'envoi lui-même était gratuit ; c'est ce qui rend l'erreur si fréquente.

La règle : quatre paliers d'engagement (0–30 jours, 31–90, 91–180, plus de 180) ; campagnes sur les deux premiers, réactivation sur le troisième, **suppression** du quatrième. Un domaine d'envoi séparé pour le promotionnel et le transactionnel, pour qu'une campagne ratée n'emporte pas les confirmations de commande. Et un plafond écrit d'avance : au-delà de 0,10 % de plainte sur un envoi, on arrête le programme du jour.

---

## 6. L'abonnement

### 6.1 Le calcul complet

*Hypothèse d'offre :* Sérum Densité en abonnement mensuel à −15 %, soit 33,15 € TTC au lieu de 39,00 € (§ 1). D'abord un coût qu'il faut sortir des pourcentages : la logistique n'est pas proportionnelle au panier, elle l'est au **colis**.

```
Logistique P5 : 11,0 % du CA HT (§ 2.1) × 3 610 997 € = 397 210 €/mois
÷ 60 200 commandes = 6,60 € par colis
```

C'est ce chiffre qui décide du sort de tout abonnement à petit panier.

| | Sérum plein tarif | Abonnement −15 % | Cure 3 mois prépayée |
| --- | ---: | ---: | ---: |
| Prix TTC / CA HT | 39,00 € / 32,50 € | 33,15 € / 27,63 € | 99,00 € / 82,50 € |
| − COGS (§ 1) | 4,80 € | 4,80 € | 14,40 € |
| − Logistique (1 colis) | 6,60 € | 6,60 € | 6,60 € |
| − PSP 1,55 % | 0,50 € | 0,43 € | 1,28 € |
| − Retours/SAV 3,5 % | 1,14 € | 0,97 € | 2,89 € |
| − Remises 8 % | 2,60 € | 0 € | 6,60 € |
| **Contribution** | **16,86 €** | **14,83 €** | **50,73 €** |

Premier résultat, contre-intuitif : **trois expéditions d'abonnement rapportent 44,49 € quand la cure prépayée équivalente en rapporte 50,73 €.** La cure gagne 6,24 €, soit +14,0 %, parce qu'elle ne paie qu'un colis au lieu de trois.

### 6.2 Attrition, durée de vie, seuil de destruction de valeur

```
Durée de vie moyenne (mois) = 1 ÷ attrition mensuelle
LTV abonnement = 14,83 € × (1 ÷ attrition)
```

| Attrition mensuelle | Durée de vie | LTV abonnement | vs LTV naturelle 24 mois (118,96 €) |
| ---: | ---: | ---: | --- |
| 5 % | 20,0 mois | 296,60 € | +149 % |
| 8 % | 12,5 mois | 185,38 € | +56 % |
| **12,5 %** | **8,0 mois** | **118,64 €** | **équivalence** |
| 15 % | 6,7 mois | 98,87 € | −17 % |
| 20 % | 5,0 mois | 74,15 € | −38 % |

```
Seuil : 14,83 € ÷ 118,96 € = 12,47 % d'attrition mensuelle
```

Au-delà, l'abonnement rapporte moins que le parcours naturel du même client, à qui tu as pourtant consenti 15 % de remise à vie. **Tu paies pour perdre de l'argent.** Le seuil dépend de l'horizon : 17,1 % contre la LTV 12 mois (86,75 €), 10,7 % contre 36 mois (138,11 €). Utilise 24 mois, borne raisonnable d'un pilotage.

Note l'asymétrie du dénominateur : passer de 10 % à 8 % d'attrition n'améliore pas la LTV de 2 % mais de 25 %. Un point d'attrition est le levier le plus rentable d'un modèle d'abonnement, et il ne s'achète pas en publicité.

### 6.3 Pourquoi pas avant d'avoir un réachat naturel

Un abonnement ne crée pas la fidélité, il la **facture d'avance**. Son attrition est plancherée par la satisfaction réelle du produit, et l'engagement récurrent ajoute même une raison de partir. Marque dont le premier réachat naturel est à 20 % au lieu de 44 % ; *hypothèse :* l'abonnement y tourne à 25 % d'attrition, soit 4,0 mois.

```
LTV : 14,83 € × 4,0 = 59,32 €   pour un nCAC de 40,03 €   →   1,48
```

Sous 1,5 : la règle canonique du § 3 dit « on ne scale pas, on répare ». L'abonnement n'a rien réparé — il a converti un problème de rétention en problème d'attrition, remise de 15 % offerte au passage. **L'abonnement est un amplificateur, pas un correcteur.** Le test d'entrée se lit sur le tableau du § 1.4 : lance-le quand ton premier réachat naturel dépasse 40 % et que ta courbe est stable sur six cohortes consécutives. Pas avant.

### 6.4 L'effet sur le cash

L'abonnement mensuel prélevé au fil de l'eau n'apporte aucune avance : tu encaisses quand tu expédies. C'est la **cure prépayée** qui travaille sur le cash.

```
Hypothèse : 20 % des 37 324 nouveaux clients/mois prennent une Cure 3 mois,
soit 7 465 clients portant en moyenne une demi-cure non consommée (49,50 € TTC)
7 465 × 49,50 € = 369 518 € de produit payé et non livré
soit 16,3 % du BFR de P5 (2 264 655 €, § 4)
```

Un sixième de ton besoin en fonds de roulement financé par tes clients. C'est le seul financement du cursus qui ne se négocie ni avec une banque ni avec un fonds. Voir [E10](E10-cash-et-operations.md) et [C05](../etudes-de-cas/C05-abonnement-et-cac-negatif.md).

---

## 7. Piloter la base installée : RFM, fidélité, SAV

### 7.1 La segmentation RFM et la valeur d'un segment

Trois variables notées de 1 à 5 par quintile de **ta** base, jamais par des seuils absolus copiés ailleurs. **R — Récence** : jours depuis la dernière commande, la plus prédictive de loin. **F — Fréquence** : commandes sur 24 mois. **M — Montant** : contribution cumulée, pas chiffre d'affaires cumulé.

Taille de la base au mois 40, dérivée du § 2.4 et des durées de palier du § 2 :

```
P1 :    768 × 3 = 2 304   P2 : 3 400 × 6  =  20 400   P3 : 13 140 × 9  = 118 260
P4 : 27 720 × 12 = 332 640   P5 : 37 324 × 10 = 373 240
Total clients acquis = 846 844
Valeur d'un segment = effectif × commandes attendues sur 12 mois × 43,53 €
```

*Hypothèses :* les parts de base et les contributions attendues ci-dessous, dérivées par segment de la courbe canonique du § 3.

| Segment | R / F | Part | Effectif | Contribution attendue / client | **Valeur du segment** |
| --- | --- | ---: | ---: | ---: | ---: |
| Champions | R 4-5, F 4-5 | 4 % | 33 874 | 118,00 € | 3 997 132 € |
| Fidèles | R 3-5, F 3-4 | 9 % | 76 216 | 62,00 € | 4 725 392 € |
| Récents à 1 commande | R 5, F 1 | 22 % | 186 306 | 38,00 € | 7 079 628 € |
| Prometteurs | R 4, F 2 | 8 % | 67 748 | 44,00 € | 2 980 912 € |
| À risque | R 2, F 3-5 | 7 % | 59 279 | 26,00 € | 1 541 254 € |
| Endormis | R 1-2, F 1-2 | 34 % | 287 927 | 3,00 € | 863 781 € |
| Perdus | R 1, F 1, > 24 mois | 16 % | 135 495 | 0,60 € | 81 297 € |
| **Total** | | **100 %** | **846 845** | | **21 269 396 €** |

```
Champions + Fidèles : 13 % de la base,  41,0 % de la valeur
Endormis + Perdus   : 50 % de la base,   4,4 % de la valeur
```

**La moitié de ta liste porte 4,4 % de sa valeur.** C'est le chiffre qui justifie la suppression du § 5.4 : tu ne détruis rien en cessant d'écrire à 423 000 personnes, tu protèges les 41 %.

### 7.2 Qui relancer, qui laisser tranquille, qui récompenser

**Relancer : les « À risque ».** Fréquence prouvée (F 3-5), récence dégradée — les seuls dont le comportement passé démontre qu'ils savent racheter. Récupérer 10 % du segment vaut 154 125 € de contribution sur 12 mois. Le message ne doit pas être une remise : il doit demander ce qui s'est passé.

**Laisser tranquille : les Champions.** Ils achètent déjà au prix fort. Leur envoyer 10 % de remise coûte :

```
33 874 × (118,00 € ÷ 43,53 €) = 91 825 commandes/an
91 825 × 71,98 € × 10 % ÷ 1,2 = 550 796 € de contribution
soit 12,6 % de l'EBITDA annuel, pour zéro commande incrémentale
```

Une remise à un client qui allait acheter est une contribution offerte à 100 %. C'est la façon la plus discrète de perdre un demi-million par an.

**Récompenser : Prometteurs et Récents à 1 commande** — les seuls dont le comportement n'est pas encore fixé, donc les seuls qu'une incitation peut déplacer. Le segment « Récents à 1 commande » porte à lui seul 33,3 % de la valeur de la base : c'est exactement la section 4. **Supprimer : les Perdus** — 16 % de la base, 0,4 % de la valeur.

### 7.3 Le programme de fidélité : le test

Un programme crée de la valeur s'il modifie un comportement ; il en détruit s'il subventionne un comportement qui existait déjà. Ce n'est pas une opinion, c'est une soustraction :

```
Valeur nette = (commandes incrémentales × 43,53 €)
             − (récompenses consommées par TOUS les membres) − plateforme
```

*Hypothèses :* 5 % de cashback en points, 60 % des commandes de P5 passées par des membres, 70 % des points consommés, plateforme à 8 000 €/mois.

```
Commandes membres : 0,60 × 60 200 = 36 120/mois → CA 2 599 918 € TTC
Points consommés : 2 599 918 × 5 % × 70 % = 90 997 € TTC/mois
Coût en contribution : ÷ 1,2 = 75 831 €/mois → 909 971 €/an
Seuil : (909 971 + 96 000) ÷ 43,53 € = 23 110 commandes/an
      = 1 926/mois, soit +5,3 % des commandes membres
```

**Le programme doit produire 5,3 % de commandes en plus chez ses membres pour ne rien coûter.** C'est beaucoup, et c'est la question que personne ne pose.

Le test, et il n'y en a qu'un : **la retenue aléatoire.** Inscris 90 % des éligibles, retiens-en 10 % tirés au sort qui ne voient jamais le programme, compare la contribution moyenne par client sur au moins deux cycles de consommation — six mois pour NØRA (§ 4.4). Sous 5,3 % d'écart, le programme est un transfert de ta marge vers tes meilleurs clients. Protocole dans [E09](E09-mesure-et-incrementalite.md).

Une variante échappe souvent au piège : la récompense **non monétaire** (accès anticipé, format exclusif, expertise). Son coût n'est pas proportionnel au chiffre d'affaires, donc elle ne subventionne pas mécaniquement ceux qui achetaient déjà.

### 7.4 Le SAV comme moteur de rétention

```
Coût SAV et retours par commande : 3,5 % × 3 610 997 € ÷ 60 200 = 2,10 €
Hypothèses : 9 % des commandes créent un ticket (5 418/mois) ; 7 minutes
à 28 €/h chargés = 3,27 € de main-d'œuvre par ticket, 17 717 €/mois
```

Le reste des 126 385 € mensuels est du produit repris, du transport retour et des gestes commerciaux. **L'arbitrage**, sur un client mécontent au panier moyen de 71,98 € TTC :

```
Contribution conservée si tu ne fais rien         : +36,86 €
Contribution si tu rembourses sans retour         : −23,12 €
  (tu rends le CA HT, tu as déjà payé COGS, colis, PSP, SAV)
Écart d'un remboursement total                    :  59,98 €
Coût d'un renvoi produit (COGS 4,80 + colis 6,60) :  11,40 €
```

| Client | Valeur résiduelle 12 mois | Remboursement total (59,98 €) | Renvoi produit (11,40 €) |
| --- | ---: | --- | --- |
| Récent à 1 commande | 38,00 € | **Jamais rentable** : même récupéré à 100 %, tu perds 21,98 € | Rentable dès +30 pts de rétention |
| Champion | 118,00 € | Rentable au-delà de +50,8 pts de rétention | Rentable dès +10 pts |

**Le même geste est rentable sur un champion et destructeur sur un client à une commande.** Le geste ne s'indexe pas sur la gravité du ticket mais sur la valeur résiduelle du client. Et pour la grande majorité de ta base, **le renvoi du produit bat le remboursement** — 11,40 € contre 59,98 €, soit 5,3 fois moins, parce qu'il coûte le COGS et non le chiffre d'affaires.

Le terme que ce calcul ignore volontairement : l'avis public. Un ticket mal traité qui devient un avis à une étoile a un coût de conversion réel que ce module ne sait pas chiffrer honnêtement. C'est une raison de pencher vers le geste, jamais un chiffre à mettre dans un tableau. Deux leviers gratuits pèsent sur la colonne M+1 du tableau de cohortes : le délai de première réponse (sous 4 heures ouvrées) et le fait de répondre à la question posée plutôt qu'à la procédure.

---

## 8. Les erreurs qui coûtent cher

**1. Mesurer la rétention en moyenne globale.** Une marque en croissance lit 0,242 réachat par client là où sa cohorte mature en fait 1,24 (§ 1.2) : ratio affiché 1,08, ratio réel 2,17. Le pilote coupe le budget d'une machine qui gagne. Coût : la marque.

**2. Attribuer à l'e-mail des ventes non incrémentales.** 595 814 € TTC/mois de CA qui aurait eu lieu de toute façon (§ 5.1), inscrits au crédit d'un canal de récolte et servant à justifier une coupe sur le canal de semence. Coût : la base d'acquisition, avec six mois de décalage.

**3. Lancer un abonnement trop tôt.** Sur un premier réachat naturel de 20 %, l'abonnement à 25 % d'attrition donne 59,32 € de LTV pour 40,03 € de nCAC, soit 1,48 — sous le seuil canonique de 1,5 (§ 6.3). Tu as ajouté 15 % de remise permanente à un problème non résolu.

**4. Monter la pression e-mail pour compenser un mauvais mois.** 7 374 € de contribution incrémentale encaissés une fois contre 7 490 € par an détruits en désinscriptions (§ 5.3), délivrabilité non comptée. Perdant dès la première année, puis chaque année.

**5. Ne pas segmenter.** Écrire à toute la base plutôt qu'aux seuls actifs coûte 455 330 € par an de contribution en placement perdu (§ 5.4). Et une remise indifférenciée qui touche les Champions coûte 550 796 € par an pour zéro commande incrémentale (§ 7.2).

**6. Caler la relance sur un délai moyen.** J+49 est la moyenne pondérée de la gamme (§ 4.4) : 18 jours trop tard pour 67 % de la base, 44 jours trop tôt pour 25 %. Elle ne tombe juste pour personne.

**7. Calculer une LTV en chiffre d'affaires.** Le CA cumulé TTC à 12 mois est 169,40 € (§ 3) ; rapporté au nCAC de 40,03 €, il donne 4,23. La LTV en contribution donne 2,17. **L'écart est de 95 %, dans le sens qui incite à dépenser.** L'erreur la plus coûteuse du cursus, parce que tous les chiffres sont exacts et que seule la ligne choisie est fausse. Voir [E01](E01-arithmetique-de-la-marque.md).

---

## 9. Ce que ce module ne dit pas

Il suppose une catégorie à **fréquence structurelle élevée**. NØRA vend un consommable qui s'épuise en 31 à 93 jours ; cohortes, relance, abonnement et RFM reposent là-dessus.

Dans une catégorie à faible fréquence — matelas, canapé, lunettes de vue, valise, gros électroménager — le client n'a pas besoin du produit avant plusieurs années, et aucun e-mail n'y changera rien. Avec les unit economics de NØRA et 0,15 réachat sur 24 mois :

```
LTV 24 mois = 32,77 € + 0,15 × 43,53 € = 39,30 €
39,30 ÷ 40,03 = 0,98  →  la marque ne rembourse jamais son acquisition
```

Aucun travail de rétention ne corrige ça : il n'y a rien à retenir. La première commande doit être rentable seule. Pour tenir un ratio de 2,0 :

```
Contribution nécessaire sur la 1ʳᵉ commande : 80,06 − 6,53 = 73,53 €
CA HT à 61,45 % de marge : 119,66 €  →  panier d'entrée 143,59 € TTC
```

Soit 2,24 fois le panier de NØRA, ou un CAC divisé d'autant. C'est pourquoi les marques de matelas vendent cher et dépensent en marque plutôt qu'en réachat : catégorie dans [E02](E02-marche-et-produit.md), panier d'entrée dans [E03](E03-offre-et-prix.md), valeur sans fréquence dans [E12](E12-marque-et-actif.md).

Trois autres limites. Ce module suppose que **tu possèdes ta liste** : sur une place de marché, tu ne possèdes ni l'e-mail ni le droit de relancer. Il suppose tes cohortes **mesurables** : sans identification fiable du client entre deux commandes (commandes invité, e-mails multiples, doublons), ton tableau est du bruit — [E09](E09-mesure-et-incrementalite.md). Et il ne dit rien du cas où la rétention est bonne et le cash absent : une LTV excellente à 24 mois avec un payback à 8 mois te met en faillite avant le gain — [E10](E10-cash-et-operations.md), [E13](E13-risque-de-ruine.md).

---

## 10. Le tableau de bord du module

Six lignes, dont aucune n'est un taux moyen global.

| # | Indicateur | Maille | Fréquence | Seuil d'alerte |
| --- | --- | --- | --- | --- |
| 1 | Passage commande 1 → 2 à 60 jours | Cohorte mensuelle d'acquisition | Mensuel | −2 pts sous la médiane des 6 cohortes précédentes |
| 2 | Réachats cumulés par client à M+3 | Cohorte mensuelle | Mensuel | 3 cohortes consécutives sous la précédente |
| 3 | LTV 12 mois en contribution ÷ nCAC | Global et par canal d'acquisition | Mensuel | < 2,0 : on arrête d'accélérer ; < 1,5 : on répare (§ 3) |
| 4 | Payback en mois | Cohorte | Mensuel | > 4 mois, ou > ce que la trésorerie peut financer |
| 5 | Part du CA en réachat | Global | Mensuel | Baisse 2 mois de suite à croissance d'acquisition constante |
| 6 | Plainte et désinscription par envoi | Envoi | À chaque envoi | Plainte > 0,10 % ; désinscription > 0,25 % |

Les indicateurs 1 et 2 sont en **avance** de six à douze mois sur le compte de résultat ; les autres le suivent. Si tu ne dois en tenir que deux, tiens ceux-là.

> **À retenir :** un tableau de bord de rétention sans axe « mois d'acquisition » ne mesure pas la rétention. Il mesure ta croissance, à l'envers.

---

## 11. Exercices

À rendre dans [`ecommerce/exercices/E08-rendu.md`](../exercices/E08-rendu.md) ; corrigés dans `E08-corrige.md`.

**Exercice 1 — Le tableau de cohortes de NØRA (réponse numérique unique).** À partir de la courbe canonique du § 3 (0,06 / 0,34 / 0,72 / 1,24 aux mois 1, 3, 6 et 12), construis le tableau des réachats cumulés par client pour six cohortes mensuelles, âges M+1 à M+6, en interpolant linéairement les mois intermédiaires. Puis : quelle part des réachats de la première année est acquise à M+6 ? à M+3 ?

**Exercice 2 — Un point de premier réachat sur l'EBITDA de P5 (réponse numérique unique).** Le passage 1 → 2 monte de 44 % à 46 %, taux conditionnels inchangés. Déroule : (a) le nouveau nombre de réachats à 12 mois, (b) la variation relative, (c) la nouvelle LTV 12 mois et le nouveau ratio LTV/CAC, (d) le gain d'EBITDA annuel via le levier du § 7. Vérifie que (d) vaut bien le double de la valeur d'un point calculée au § 4.2.

**Exercice 3 — Ton tableau de cohortes.** Exporte 18 mois de commandes avec un identifiant client stable. Construis le tableau en réachats cumulés par client, dénominateur figé aux clients acquis. Réponds : ta colonne M+3 monte-t-elle ou descend-elle sur les six dernières cohortes ? ta diagonale montre-t-elle un mois calendaire anormal ? quel écart entre ta moyenne globale et ta cohorte à 12 mois ?

**Exercice 4 — Ton calendrier de consommation.** Pour tes trois références les plus vendues : contenance, rythme d'usage réel (demande à dix clients, ne devine pas), date d'épuisement, date de relance à 78 % du cycle. Compare à ce que ton flux envoie aujourd'hui, écart en jours par référence.

**Exercice 5 — Le coût de ta campagne supplémentaire.** Reprends le § 5.3 avec tes chiffres : base active, contribution incrémentale mensuelle, valeur annuelle d'un abonné, revenu par envoi et désinscription des trois dernières campagnes. La campagne marginale du mois dernier était-elle rentable sur douze mois ?

**Exercice 6 — Décision : lancer l'abonnement ou non.** Ta marque vend un consommable à 42,00 € TTC, COGS 6,00 €, marge brute 58 %, nCAC 31,00 €, premier réachat à 12 mois de 37 %. **Option A** : abonnement à −20 %, attrition mensuelle attendue 14 %. **Option B** : ne rien lancer, et investir le même trimestre d'équipe dans le flux post-achat et le calendrier de réapprovisionnement, pour +4 points de premier réachat. Chiffre les deux, tranche, et écris explicitement la condition sous laquelle l'autre option deviendrait la bonne.

---

*Fin du module E08. Suite : [E09 — Mesurer : attribution, incrémentalité, pilotage](E09-mesure-et-incrementalite.md), qui donne les protocoles permettant de savoir si les 45 % d'incrémentalité supposés au § 5.1 sont réels. Puis [E10](E10-cash-et-operations.md) pour ce que la rétention fait au cash, et [E14](E14-plan-1M-semaine.md) pour l'assemblage.*
