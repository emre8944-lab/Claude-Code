# Module E08 — La rétention, les cohortes et la LTV

> **Prérequis :** [E01](E01-arithmetique-de-la-marque.md), [E02](E02-marche-et-produit.md), [E03](E03-offre-et-prix.md), [E07](E07-funnel-et-conversion.md).
> **Objet :** savoir construire et lire un tableau de cohortes, calculer une LTV en marge qui tient devant un banquier, et piloter les six leviers qui font revenir un client.
> **Temps de travail :** ~5 h (lecture + exercices)

---

## 0. Pourquoi ce module existe

Ouvre les [chiffres canoniques](../donnees/chiffres-canoniques.md) au § 2.4 et lis la dernière colonne. Aux cinq paliers, sans exception, la marge de NØRA sur la **première** commande est négative : −4,93 € en P1, −3,83 € en P2, −3,01 € en P3, −6,06 € en P4, **−7,26 € en P5**.

Au palier P5, ce n'est pas une nuance comptable, c'est toute l'entreprise :

```
Contribution des commandes de réachat
  22 876 réachats/mois × 43,53 €        =    995 792 €/mois
Contribution des premières commandes, nette du CAC
  37 324 nouveaux clients × (−7,26 €)   =   −270 972 €/mois
Frais fixes (§ 2.5)                      =   −360 000 €/mois
                                            ─────────────────
EBITDA                                   =    364 820 €/mois
```

Le canonique donne 364 752 € (§ 2.2). L'écart de 68 € vient des arrondis sur les contributions unitaires. Autrement dit : **le compte de résultat de NØRA se reconstruit intégralement à partir de deux nombres, le réachat et le CAC.**

Maintenant coupe le réachat. Même produit, même publicité, mêmes 37 324 clients acquis par mois, mais aucun ne repasse commande :

```
EBITDA annuel sans réachat = (−270 972 − 360 000) × 12 = −7 571 667 €
EBITDA annuel avec réachat = +4 377 023 €  (§ 7)
Écart                      = 11 948 690 €  = la contribution de réachat
```

Une marque DTC qui achète son trafic et qui n'a pas de réachat n'est pas une marque à faible marge. C'est une marque qui n'existe pas : elle finance la croissance de sa plateforme publicitaire avec le capital de ses actionnaires. La rétention n'est pas le chapitre « fidélisation » qu'on ajoute quand l'acquisition tourne. **C'est le seul endroit du modèle où il y a de l'argent.**

> **À retenir :** en P5, 100 % de l'EBITDA et 7,57 M€ de plus sont produits par des commandes que personne n'a payées en publicité.

---

## 1. La cohorte, proprement définie

### 1.1 Définition

Une **cohorte** est un groupe de clients acquis pendant la même période — presque toujours le mois de leur **première** commande — et suivi ensuite dans le temps sans jamais changer de composition. Un client entre dans une cohorte et une seule, le jour de sa première commande, et il y reste. On ne le retire pas quand il arrête d'acheter : c'est précisément parce qu'on le garde au dénominateur que la mesure est honnête.

Deux mots à ne jamais confondre :

- **Âge de la cohorte** : le nombre de mois écoulés depuis l'acquisition. Noté M+0, M+1, M+3…
- **Mois calendaire** : janvier, février. C'est la période, pas l'âge.

Tout le pouvoir de la méthode vient de la séparation de ces deux axes.

### 1.2 Pourquoi la moyenne globale ment, avec les chiffres

Prends une marque en croissance. Trois cohortes seulement, et la courbe de réachat canonique de NØRA (§ 3) : 1,24 réachat par client à 12 mois, 0,72 à 6 mois, 0,06 à 1 mois.

| Cohorte | Âge | Clients | Réachats/client | Réachats |
| --- | ---: | ---: | ---: | ---: |
| A | 12 mois | 1 000 | 1,24 | 1 240 |
| B | 6 mois | 4 000 | 0,72 | 2 880 |
| C | 1 mois | 16 000 | 0,06 | 960 |
| **Total** | | **21 000** | | **5 080** |

```
Moyenne globale = 5 080 ÷ 21 000 = 0,242 réachat par client
LTV en contribution = 32,77 € + 0,242 × 43,53 € = 43,30 €
LTV / nCAC = 43,30 ÷ 40,03 = 1,08
```

Le pilote qui lit 1,08 applique la règle canonique du § 3 (« LTV/CAC 12 mois < 1,5 : on ne scale pas, on répare ») et coupe le budget. Il vient de tuer une marque dont la cohorte mature est à **1,24 réachat, LTV 86,75 €, ratio 2,17** — c'est-à-dire une marque qui marche.

Inverse maintenant les effectifs : 16 000 clients dans la cohorte A, 4 000 dans B, 1 000 dans C. Même produit, même courbe, même client.

```
Moyenne globale = 22 780 ÷ 21 000 = 1,085 réachat par client
LTV = 32,77 € + 1,085 × 43,53 € = 80,00 €  →  ratio 2,00
```

**Le même business affiche 1,08 quand il croît et 2,00 quand il décroît.** La moyenne globale ne mesure pas la rétention : elle mesure la forme de ta courbe d'acquisition. C'est un indicateur qui te félicite quand tu meurs et qui te punit quand tu gagnes.

La cohorte, elle, ne peut pas mentir sur ce point : à l'intérieur d'une cohorte, tous les clients ont le même âge.

### 1.3 Construire le tableau

Trois décisions à prendre avant la première ligne.

**La maille temporelle.** Le mois, par défaut. La semaine si ton cycle de consommation est court (moins de 30 jours) ou si tu as besoin de lire une cohorte avant qu'elle ait un trimestre. Le trimestre seulement si tu as moins de 300 clients par mois — en dessous, le bruit d'échantillonnage dépasse le signal.

**La valeur dans la cellule.** Trois choix, et un seul est bon.

| Valeur | Ce qu'elle mesure | Verdict |
| --- | --- | --- |
| CA cumulé TTC par client | Rien d'exploitable | À proscrire. Voir § 8, erreur 6 |
| Commandes cumulées par client | La fréquence, mais diluée par le « 1 » de départ | Acceptable pour un rapport |
| **Réachats cumulés par client** | Exactement ce que tu pilotes | **C'est celle-là** |
| Marge de contribution cumulée par client | La décision d'investissement | La seconde à tenir |

Pourquoi les réachats plutôt que les commandes cumulées : la première commande vaut 1 pour tout le monde, par construction. Elle occupe donc une part écrasante du nombre affiché et écrase les variations. Une cohorte qui passe de 1,34 à 1,30 commande cumulée à M+3 a l'air d'avoir perdu 3 % ; en réachats, elle est passée de 0,34 à 0,30, soit **−11,8 %**. Le même fait, quatre fois plus lisible.

**L'unité de dénominateur.** Le nombre de clients **acquis** dans la cohorte, figé pour toujours. Pas le nombre de clients encore actifs — ce dénominateur-là fabrique de la rétention à partir de rien.

### 1.4 Lire dans les trois directions

Voici le tableau des réachats cumulés par client de NØRA, cohortes M31 à M36 (début du palier P5). La courbe canonique du § 3 donne les jalons 1, 3, 6 mois ; les mois intermédiaires sont interpolés linéairement, ce qui donne la trajectoire de référence **0,06 / 0,20 / 0,34 / 0,47 / 0,59 / 0,72**.

| Cohorte | M+1 | M+2 | M+3 | M+4 | M+5 | M+6 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| M31 | 0,06 | 0,20 | 0,34 | 0,47 | 0,59 | 0,72 |
| M32 | 0,06 | 0,19 | 0,33 | 0,45 | 0,57 | — |
| M33 | 0,05 | 0,18 | 0,32 | 0,44 | — | — |
| M34 | 0,05 | 0,17 | 0,30 | — | — | — |
| M35 | 0,04 | 0,15 | — | — | — | — |
| M36 | 0,04 | — | — | — | — | — |

**Le long d'une ligne — la maturation.** La cohorte M31 accumule 0,72 réachat en six mois, sur les 1,24 qu'elle atteindra à douze mois : **58 % des réachats de la première année arrivent dans les six premiers mois** (0,72 ÷ 1,24). Deux conséquences opérationnelles. Un : tu peux juger une cohorte bien avant sa maturité, ce qui rend le pilotage possible. Deux : ce qui n'est pas gagné à M+6 ne se rattrape presque plus — les mois 7 à 12 n'apportent que 0,52 réachat, soit 0,087 par mois, contre 0,14 par mois entre M+1 et M+3.

**Le long d'une colonne — la qualité des cohortes successives.** C'est la lecture qui décide. Colonne M+3 : 0,34 → 0,33 → 0,32 → 0,30. Quatre cohortes consécutives, chacune sous la précédente au même âge. Ce n'est plus du bruit, c'est une pente.

**La diagonale — les effets de période.** Les cellules atteintes pendant le même mois calendaire forment une diagonale : en M36, tu observes M31 à M+5, M32 à M+4, M33 à M+3, M34 à M+2, M35 à M+1. Si un événement a frappé **le mois** — rupture de stock sur le produit héros, bug de paiement, gueule de bois post-soldes, canicule sur une catégorie saisonnière — toute la diagonale décroche d'un coup et les colonnes se rétablissent le mois suivant. Si le décrochage se lit sur les **colonnes** et pas sur la diagonale, il est dans la cohorte, donc dans ce que tu as acheté comme clients. **Diagonale = période, colonne = cohorte.** C'est le premier tri à faire, et il coûte cinq minutes.

---

## 2. Le signal d'alarme numéro un

### 2.1 Ce qu'il coûte

Reprends la colonne M+3 du tableau ci-dessus : 0,34 pour M31, 0,30 pour M34. Écart : −11,8 %.

Si cette dégradation se propage proportionnellement jusqu'à 12 mois — hypothèse de propagation constante, la plus prudente puisqu'elle n'invente pas d'aggravation :

```
Réachats à 12 mois : 1,24 × (1 − 0,118)      = 1,094
LTV en contribution : 32,77 € + 1,094 × 43,53 € = 80,38 €
LTV / nCAC : 80,38 ÷ 40,03                    = 2,01
```

Tu passes de 2,17 à 2,01. Tu es encore au-dessus du seuil canonique de 2,0, mais tu es dessus **de 0,01**, et la cohorte M35 n'a pas fini d'arriver.

Traduction en euros, avec le levier canonique du § 7 (« +10 % de commandes de réachat = 1 194 871 € d'EBITDA annuel ») :

```
−11,8 % de réachats → 1 194 871 € × 1,18 = 1 409 948 € d'EBITDA annuel
soit 32,2 % de l'EBITDA annuel de référence (4 377 023 €)
```

**Quatre cohortes mensuelles viennent d'effacer un tiers de l'EBITDA annuel, et le compte de résultat du mois ne montre encore rien.** Il ne montrera rien pendant six à douze mois, parce que les réachats manquants sont des réachats qui n'auront pas lieu dans le futur. C'est exactement pour ça que le tableau de cohortes existe : c'est le seul instrument du tableau de bord qui soit en avance sur le résultat.

### 2.2 Les trois causes, et comment les distinguer

Une colonne qui baisse a trois causes possibles, et une seule bonne réponse par cause. Les confondre coûte un trimestre.

| | Saturation de l'audience | Dérive du produit | Dérive de la promesse publicitaire |
| --- | --- | --- | --- |
| **Mécanisme** | Tu as épuisé les acheteurs faciles ; l'algorithme va chercher des profils de plus en plus éloignés du cœur | La formule, le fournisseur, le lot ou l'emballage ont changé, ou la qualité a glissé sans que personne l'écrive | La créa promet plus que le produit ne tient, pour tenir le CPA |
| **Forme de la chute** | Lente, régulière, corrélée à la hausse du budget | Brutale et **datée** : toutes les cohortes après une date précise, quel que soit le canal | Progressive, limitée aux cohortes issues des nouveaux concepts |
| **nCAC pendant ce temps** | **Monte** | Stable | **Baisse** — la sur-promesse convertit mieux |
| **Taux de retour / tickets SAV** | Stable | **Monte** dans la même fenêtre | Monte au premier usage, pas à la livraison |
| **Test qui tranche** | Cohorter par canal et par audience : si Google Search marque tient et que la prospection large s'effondre, c'est la saturation | Croiser la date de bascule avec les numéros de lot et les changements de fournisseur ; commander son propre produit et le comparer à un exemplaire de six mois | Cohorter par **concept créatif** ; lire les verbatims SAV : « ce n'est pas ce qui était montré » |
| **Réponse** | Élargir l'offre, monter l'AOV, ouvrir un marché — [E11](E11-passage-a-echelle.md) | Arrêter, corriger, rappeler les lots. Rien d'autre ne marche | Réécrire la promesse, tuer les concepts concernés — [E05](E05-machine-creative.md) |

La signature la plus utile est la troisième ligne. **Un nCAC qui baisse pendant que la rétention baisse est une signature unique.** Aucune autre cause ne produit ce couple : la saturation fait monter le CAC, la dérive produit le laisse tranquille. Si ton coût d'acquisition s'améliore et que tes cohortes se dégradent, tu n'as pas trouvé un bon angle publicitaire — tu as trouvé un mensonge rentable à court terme, et tu le paieras sur douze mois de réachat. Le calcul du § 2.1 te donne le prix.

Un quatrième suspect existe et il faut l'écarter avant les trois autres : **le mix promotionnel**. Une cohorte acquise pendant une semaine de −30 % contient une proportion anormale de chasseurs de remise, qui réachètent moins et seulement en promotion. Ce n'est pas une dérive, c'est une composition. Le test : cohorter par présence ou absence d'un code promo sur la première commande. Voir [C09](../etudes-de-cas/C09-piege-du-black-friday.md).

---

## 3. La courbe de réachat canonique, chiffre par chiffre

### 3.1 Ce que dit le § 3

| Horizon | Réachats/client | LTV en contribution | LTV / nCAC |
| --- | ---: | ---: | ---: |
| 1 mois | 0,06 | 35,38 € | 0,88 |
| 3 mois | 0,34 | 47,57 € | 1,19 |
| 6 mois | 0,72 | 64,11 € | 1,60 |
| 12 mois | 1,24 | 86,75 € | 2,17 |
| 18 mois | 1,66 | 105,03 € | 2,62 |
| 24 mois | 1,98 | 118,96 € | 2,97 |
| 36 mois | 2,42 | 138,11 € | 3,45 |

Base : nCAC **40,03 €**, contribution de la première commande **32,77 €**, contribution d'un réachat **43,53 €** (§ 3).

Vérifie que tu sais reconstruire chaque ligne, sinon tu ne pourras pas la contester :

```
LTV(12 mois) = 32,77 € + 1,24 × 43,53 €
             = 32,77 € + 53,98 €
             = 86,75 €
LTV/CAC      = 86,75 ÷ 40,03 = 2,17
```

### 3.2 Deux chiffres que le canonique ne publie pas et que tu peux dériver

Le § 3 donne le CA cumulé TTC : 69,10 € à 1 mois, 169,40 € à 12 mois. Deux équations, deux inconnues.

```
169,40 − 69,10 = (1,24 − 0,06) × AOV réachat
100,30         = 1,18 × AOV réachat
AOV réachat    = 85,00 € TTC

AOV 1ʳᵉ commande = 69,10 − 0,06 × 85,00 = 64,00 € TTC
```

Contrôle sur le § 2 : 37 324 premières commandes × 64,00 € + 22 876 réachats × 85,00 € = 2 388 736 € + 1 944 460 € = **4 333 196 €**, soit exactement le CA TTC mensuel de P5. Deuxième contrôle : (85,00 ÷ 1,2) × 61,45 % = 43,53 €, la contribution de réachat canonique. Le taux de 61,45 % est la somme exacte des lignes du § 2.1 ; le tableau l'arrondit à 61,5 %.

**Le panier de réachat est 33 % plus élevé que le panier d'acquisition** (85,00 € contre 64,00 €). Ce n'est pas un détail : c'est la raison pour laquelle un réachat rapporte 43,53 € de contribution quand une première commande n'en rapporte que 32,77 €. Un client qui revient achète le rituel entier, pas le produit d'appel.

### 3.3 Ce que le payback autorise

```
Contribution cumulée à M+1 : 35,38 €   (sous le CAC de 40,03 €)
Contribution cumulée à M+3 : 47,57 €   (au-dessus)
Interpolation : 1 + (40,03 − 35,38) ÷ (47,57 − 35,38) × 2 = 1,76 mois
```

Soit le **≈ 1,8 mois** du canonique. Ce chiffre commande directement ta vitesse de croissance, parce qu'il fixe combien de mois d'acquisition tu dois financer avant que le premier euro revienne.

Il ne suffit pas de 1,24 réachat pour rembourser le CAC. Il en suffit de :

```
Déficit à la 1ʳᵉ commande : 7,26 €
Réachats nécessaires : 7,26 ÷ 43,53 = 0,167 réachat par client acquis
```

**Un client sur six qui repasse une seule commande, et l'acquisition est remboursée.** Le reste de la courbe — les 1,07 réachats restants à 12 mois, les 1,81 à 24 mois — est du profit net d'acquisition. C'est ce qui rend le modèle si sensible au **premier** réachat, et si peu sensible au reste : section 4.

Ce que chaque nombre t'autorise :

| Nombre | Valeur P5 | Ce qu'il autorise |
| --- | ---: | --- |
| Payback | 1,8 mois | Financer l'acquisition avec ~2 mois de trésorerie roulante. Combiné à un crédit fournisseur de 45 à 60 jours, la croissance est presque autofinancée en marge — mais pas en stock, voir [E10](E10-cash-et-operations.md) |
| LTV/CAC 12 mois | 2,17 | Au-dessus de 2,0 : on accélère. À 2,17, la marge de sécurité est de 8 % — une dégradation de 8 % de la courbe te ramène à la ligne |
| LTV/CAC 24 mois | 2,97 | Ce que tu peux montrer à un prêteur, à condition d'avoir 24 mois de données observées et pas extrapolées |
| Réachats 12 → 24 mois | 1,24 → 1,98 | +0,74 réachat, soit +32,21 € de contribution par client. C'est le prix d'attendre, et c'est pour ça qu'on ne pilote pas sur 24 mois : l'argent est immobilisé |

Attention au ratio de 3,45 à 36 mois. Il est vrai et il ne sert à rien pour décider : une décision d'achat média se prend sur l'argent qui revient avant que tu aies besoin de le redépenser. **Pilote sur 12 mois, publie sur 24, ne décide jamais sur 36.**

---

## 4. Le premier réachat est le seul qui compte vraiment

### 4.1 La démonstration

Le canonique donne un total (1,24 réachat à 12 mois) mais pas sa décomposition. Décompose-la, sous contrainte.

*Hypothèse déclarée :* je pose le taux de passage de la commande 1 à la commande 2, à 12 mois, à **44 %**, et je choisis les taux conditionnels suivants de sorte que la somme des probabilités cumulées reproduise **exactement** le 1,24 canonique. Ce n'est pas une invention : le total est contraint par le § 3, seule la répartition est un choix de modélisation, et il est calé sur la forme universelle de ces courbes.

| Passage | Probabilité cumulée d'atteindre ce rang | Taux conditionnel |
| --- | ---: | ---: |
| Commande 1 → 2 | 0,44 | **44,0 %** |
| Commande 2 → 3 | 0,29 | 65,9 % |
| Commande 3 → 4 | 0,20 | 69,0 % |
| Commande 4 → 5 | 0,14 | 70,0 % |
| Commande 5 → 6 | 0,10 | 71,4 % |
| Commande 6 → 7 | 0,07 | 70,0 % |
| **Somme** | **1,24** | |

Regarde la colonne de droite. Le premier passage est à 44 %, tous les suivants entre 66 % et 71 %. **Le premier réachat est 1,5 fois plus difficile que tous les autres**, et cet écart n'est pas un accident de calibrage : il se retrouve dans toutes les catégories consommables. Un client qui a commandé deux fois a vérifié que le produit marche, que le colis arrive, que le SAV répond. Il n'a plus rien à découvrir. Un client qui a commandé une fois n'a encore rien vérifié du tout.

### 4.2 Ce que vaut un point

Si les taux conditionnels sont tenus constants, le total est proportionnel au premier passage :

```
K = 1,24 ÷ 0,44 = 2,8182  (multiplicateur de la chaîne)
44 % → 45 % :  0,45 × 2,8182 = 1,268 réachat
Gain : +0,028 réachat par client acquis, soit +2,27 %
```

Applique le levier canonique du § 7 (+10 % de commandes de réachat = 1 194 871 € d'EBITDA annuel) :

```
1 194 871 € × (2,27 ÷ 10) = 271 562 € d'EBITDA annuel
soit 6,2 % de l'EBITDA annuel de P5
```

> **À retenir :** **un point de taux de premier réachat vaut 271 562 € d'EBITDA par an au palier P5.** Trois points valent 814 663 €, soit 18,6 % de l'EBITDA. Ces trois points ne coûtent aucun euro de publicité.

Compare avec le § 7 : le levier « +10 % de réachat » pèse 27,3 % de l'EBITDA. Il ne demande pas de multiplier le réachat par 1,1 partout ; il demande **4,4 points de premier réachat** (44 % → 48,4 %). C'est un chantier de trimestre, pas un miracle.

### 4.3 Les leviers du premier réachat, par ordre d'efficacité

L'ordre compte plus que la liste, parce que les quatre premiers coûtent presque zéro en marketing et que le dernier est celui sur lequel tout le monde se jette.

**1. L'expérience produit elle-même.** Un client qui ne voit pas le résultat qu'on lui a promis ne revient pas, quelle que soit la qualité de ta relance. C'est le seul levier qui plafonne tous les autres : si ton produit satisfait 55 % de tes acheteurs, ton taux de premier réachat ne dépassera pas durablement 55 %. Mesure-le directement — enquête à J+30, une question, une note sur 10 — et traite ce chiffre comme le plafond de ta rétention. Toute la section 6 travaille **sous** ce plafond.

**2. La livraison.** Elle est la première promesse tenue ou trahie, et elle arrive avant que le produit soit essayé. Trois variables : le délai promis, l'écart entre le délai promis et le délai réel, et l'état du colis. L'écart compte plus que le délai : un client à qui on annonce 5 jours et qui reçoit en 4 est plus satisfait qu'un client à qui on annonce 2 jours et qui reçoit en 3. Voir [E10](E10-cash-et-operations.md).

**3. Le contenu d'accompagnement.** Un soin capillaire mal dosé ne donne pas de résultat. Le rôle du flux post-achat n'est pas de vendre, c'est de **faire réussir l'usage** : la dose exacte, la fréquence, les trois erreurs courantes, et surtout à quoi ressemble le résultat à la semaine 6 pour que le client ne conclue pas trop tôt que ça ne marche pas. C'est le levier au meilleur rapport effort/rendement du module, et c'est aussi le plus négligé, parce qu'il ne produit aucune vente attribuée le jour de l'envoi.

**4. Le moment de la relance, calé sur la durée de consommation réelle.** Section 4.4. C'est un levier de timing, pas de message : le même e-mail envoyé au bon moment et au mauvais moment n'a pas le même rendement, à un facteur qui se compte en multiples.

**5. L'offre de réapprovisionnement.** Le réassort en un clic du produit exact déjà acheté, avec la bonne référence et la bonne taille. Simple, mécanique, efficace — et volontairement en cinquième position : offrir une remise de réassort à quelqu'un qui n'a pas eu de résultat ne produit rien, et offrir une remise à quelqu'un qui allait racheter au prix fort te coûte la remise. Voir § 7.4.

### 4.4 Le calendrier de consommation

La règle : **on ne relance pas après un délai, on relance avant une date d'épuisement.** Un délai est un chiffre arbitraire recopié d'un article de blog. Une date d'épuisement se calcule.

Dérivation pour la gamme canonique (§ 1). Les dosages sont des *hypothèses* déclarées ; le contrôle est que le canonique vend une « Cure 3 mois » composée de 3 sérums, ce qui fixe la durée d'un sérum à un mois.

| Produit | Contenance | Dosage (hypothèse) | Épuisement |
| --- | ---: | --- | ---: |
| Sérum Densité | 50 ml | 1,6 ml/jour | **31 jours** |
| Shampooing Fortifiant | 250 ml | 10 ml × 3 lavages/semaine | **58 jours** |
| Masque Réparateur | 200 ml | 15 ml × 1 application/semaine | **93 jours** |
| Rituel Complet | les 3 | premier vide : le sérum | **31 jours** |
| Cure 3 mois | 3 sérums | 3 × 31 jours | **93 jours** |

Contrôle : 50 ÷ 1,6 = 31,3 jours, cohérent avec les 3 mois annoncés pour 3 sérums.

Maintenant, le mix des premières commandes. On sait que l'AOV d'acquisition vaut 64,00 € TTC (§ 3.2). Un mix qui le reproduit exactement :

```
0,25 × 39,00 €  (Sérum seul)      =  9,75 €
0,42 × 74,00 €  (Rituel Complet)  = 31,08 €
0,20 × 99,00 €  (Cure 3 mois)     = 19,80 €
0,08 × 24,00 €  (Shampooing seul) =  1,92 €
0,05 × 29,00 €  (Masque seul)     =  1,45 €
                                    ───────
                                     64,00 €
```

*Hypothèse :* ce mix est une reconstruction, contrainte par l'AOV canonique. La date d'épuisement moyenne pondérée du premier article vide vaut alors :

```
0,25 × 31 + 0,42 × 31 + 0,20 × 93 + 0,08 × 58 + 0,05 × 93 = 48,7 jours
```

**Ne relance jamais à J+49.** Ce délai « moyen » arrive 18 jours trop tard pour 67 % de ta base (les acheteurs de sérum et de rituel, vides à J31) et 44 jours trop tôt pour 25 % (cure et masque, vides à J93). Il ne tombe juste pour personne. C'est le défaut structurel de toute relance calée sur une moyenne : la moyenne d'une distribution bimodale ne décrit aucun individu.

Le calendrier correct est **par référence achetée**, avec le déclencheur posé à 78 % du cycle — assez tôt pour que le colis arrive avant le dernier usage, assez tard pour que le besoin soit réel :

| Panier de la 1ʳᵉ commande | Relance 1 | Relance 2 | Relance 3 |
| --- | ---: | ---: | ---: |
| Sérum seul | J+24 | J+31 | J+38 |
| Rituel Complet | J+24 (sérum) | J+45 (shampooing) | J+72 (masque) |
| Shampooing seul | J+45 | J+58 | J+70 |
| Masque seul | J+72 | J+93 | J+110 |
| Cure 3 mois | J+72 | J+93 | J+110 |

Deux remarques. Le Rituel Complet n'a pas une date d'épuisement mais trois, et la bonne relance à J+24 ne propose que le sérum — proposer le rituel entier à quelqu'un qui a encore 90 % de son masque, c'est lui demander de payer pour du stock qu'il possède déjà. Et les acheteurs de Cure 3 mois sont, mécaniquement, ceux qu'on relance le moins souvent et le plus tard : c'est le prix d'un panier d'entrée élevé, à mettre en face du gain de trésorerie (§ 6.4).

---

## 5. E-mail et SMS

### 5.1 L'ordre de grandeur, et le piège

*Ordre de grandeur déclaré :* pour une marque DTC consommable en bonne santé, l'e-mail et le SMS se voient attribuer, en dernier clic, **22 à 30 % du chiffre d'affaires**. Ce n'est pas un chiffre canonique ; c'est une fourchette d'observation sectorielle, et tu dois la traiter comme telle.

Prends 25 % pour NØRA au palier P5 :

```
CA attribué en dernier clic : 0,25 × 4 333 196 € = 1 083 299 € TTC/mois
```

Maintenant le piège. Un e-mail de réapprovisionnement envoyé à quelqu'un dont le flacon est vide s'attribue une vente qui allait avoir lieu. Le dernier clic n'invente pas cette vente, il la **récolte**.

*Hypothèse :* 45 % de ce chiffre d'affaires est incrémental — la vente n'aurait pas eu lieu, ou pas maintenant, sans le message. Les protocoles de mesure sont dans [E09](E09-mesure-et-incrementalite.md) ; le seul honnête est le groupe de contrôle par retenue aléatoire.

```
CA incrémental      : 1 083 299 × 0,45 =   487 485 € TTC/mois
CA non incrémental  : 1 083 299 × 0,55 =   595 814 € TTC/mois
Contribution incrémentale : (487 485 ÷ 1,2) × 61,45 % = 249 633 €/mois
```

Contrôle de cohérence : 249 633 € représentent 25,1 % des 995 792 € de contribution de réachat mensuelle (§ 0). C'est cohérent — **l'e-mail n'est pas une source de chiffre d'affaires supplémentaire, c'est le canal d'exécution du réachat.** Il ne s'additionne pas à la rétention, il la réalise.

Les 595 814 € restants sont le vrai danger. Ils apparaissent dans le tableau de bord comme du CA « e-mail », ils servent à justifier un budget, et surtout ils servent à justifier une coupe ailleurs — « l'e-mail nous fait 25 % du CA à coût quasi nul, réduisons Meta ». Réduis Meta et tu réduis, six mois plus tard, la base à qui l'e-mail parle. **Un canal de récolte ne peut pas financer sa propre semence.**

### 5.2 Les flux automatisés

| Flux | Déclencheur | Messages | Délais | Contenu |
| --- | --- | ---: | --- | --- |
| **Bienvenue** | E-mail capté, aucune commande | 4 | +15 min, J+1, J+3, J+6 | Preuve (avant/après, composition), levée de l'objection prix, réponse à « est-ce que ça marche sur mes cheveux », rappel de l'offre d'entrée au dernier message seulement |
| **Panier abandonné** | Ajout au panier, pas de commande sous 1 h | 3 + 1 SMS | +1 h, +20 h, +48 h ; SMS à +4 h | Rappel visuel du produit exact, levée de risque (retour, garantie), avis client. Remise **au troisième message uniquement**, et pas systématiquement |
| **Navigation abandonnée** | ≥ 2 vues d'une même fiche, pas d'ajout | 2 | +4 h, +36 h | Le produit vu, sa preuve, la question qu'il se pose à ce stade |
| **Post-achat / onboarding** | Commande expédiée | 4 | J+0, jour de livraison, livraison +3, J+21 | Suivi, dose et fréquence exactes, les 3 erreurs d'usage, à quoi ressemble le résultat à S6, demande d'avis |
| **Réapprovisionnement** | Date d'épuisement calculée par référence (§ 4.4) | 3 | 78 %, 100 %, 118 % du cycle | Le produit exact déjà acheté, réassort en un clic, montée en cure |
| **Réactivation** | Aucune commande depuis 2 cycles | 3 | J+0, J+6, J+14 | Nouveauté, preuve renouvelée, offre de retour au dernier message |
| **Anniversaire** | Anniversaire, ou date de 1ʳᵉ commande | 1 | J+0 | Geste non monétaire de préférence : accès anticipé, format exclusif, contenu |

**Deux classements, pas un.** Par euro et par destinataire, l'ordre est : panier abandonné > navigation abandonnée > réapprovisionnement > bienvenue > post-achat > réactivation > anniversaire. Par euro **total**, l'ordre est : bienvenue > réapprovisionnement > panier abandonné > post-achat > navigation abandonnée > réactivation > anniversaire. La différence tient au volume d'entrées : un panier abandonné rapporte beaucoup par personne mais concerne peu de monde ; le flux de bienvenue concerne tous les captés.

**C'est le second classement qui paie tes salaires.** L'erreur courante est de passer trois semaines à optimiser le panier abandonné, qui affiche les plus beaux taux de conversion du compte, pendant que le flux de réapprovisionnement n'existe pas.

Chiffrons le réapprovisionnement, qui est le flux directement branché sur la section 4 :

```
Entrées : 60 200 commandes livrées/mois (§ 2)
Hypothèse : le flux produit 6,5 % de réachats sur les entrées
Hypothèse : 40 % de ces réachats sont incrémentaux
Commandes incrémentales : 60 200 × 0,065 × 0,40 = 1 565 /mois
Contribution : 1 565 × 43,53 € = 68 134 €/mois
Annuel : 817 608 €, soit 18,7 % de l'EBITDA de P5
```

Un flux, sept messages au total, écrit une fois. C'est la meilleure heure de travail du module.

### 5.3 Les campagnes, la pression et le coût d'une désinscription

Les flux sont déclenchés par un comportement. Les campagnes sont envoyées parce que c'est jeudi. Elles n'ont pas la même économie, et surtout pas le même coût caché.

*Hypothèses :* base de 400 000 abonnés actifs (ouverture au moins une fois sur 180 jours) ; une campagne de pression supplémentaire produit 0,08 € TTC par envoi, sous la moyenne du programme puisqu'elle est marginale ; elle porte le taux de désinscription de l'envoi à 0,25 %.

```
Valeur d'un abonné : 249 633 € ÷ 400 000 = 0,624 €/mois → 7,49 €/an de contribution

La campagne rapporte
  400 000 × 0,08 €              =  32 000 € TTC
  contribution : (32 000 ÷ 1,2) × 61,45 % = 16 387 €
  incrémentale à 45 %           =   7 374 €  une fois

La campagne coûte
  désinscriptions : 400 000 × 0,25 % = 1 000 abonnés
  valeur perdue : 1 000 × 7,49 €     =   7 490 €  par an, chaque année
```

**7 374 € encaissés une fois contre 7 490 € détruits chaque année.** La campagne supplémentaire est perdante dès la première année, et perdante de 7 490 € par an ensuite. Et ce calcul ne compte pas encore l'effet sur la délivrabilité de toute la base.

C'est la réponse arithmétique à la tentation universelle : le mois est mauvais, on ajoute deux envois. Tu déplaces du chiffre d'affaires du futur vers le présent, et tu détruis une part du futur au passage. Voir § 8, erreur 4.

Le SMS a en plus un coût direct que l'e-mail n'a pas. *Hypothèse :* 0,045 € par SMS en Europe.

```
Coût d'un envoi à toute la base : 400 000 × 0,045 € = 18 000 €
CA TTC nécessaire pour le couvrir : (18 000 ÷ 61,45 %) × 1,2 = 35 151 €
soit 0,088 € TTC par SMS, en incrémental
soit 0,195 € TTC par SMS en dernier clic (à 45 % d'incrémentalité)
```

Une barre que peu de campagnes franchissent. Conclusion opérationnelle : **le SMS n'est pas un canal de masse, c'est un canal de déclencheur.** Réapprovisionnement, panier abandonné, rupture de stock résolue, et les segments à forte valeur du § 7. Jamais la base entière.

### 5.4 La délivrabilité est un actif, et elle se détruit vite

Depuis février 2024, Google et Yahoo imposent aux expéditeurs de masse — plus de 5 000 messages par jour vers leurs domaines — l'authentification SPF, DKIM et DMARC, la désinscription en un clic, et un taux de plainte pour spam maintenu sous 0,3 %, avec 0,1 % comme cible recommandée (exigences publiées par Google et Yahoo, 2024). Ce sont des faits publics, pas des bonnes pratiques.

Le mécanisme qu'il faut comprendre : les filtres modernes notent ton domaine expéditeur sur **l'engagement de tes destinataires**. Envoyer à des adresses mortes ne coûte pas seulement l'envoi ; ça abaisse le taux d'engagement global, donc la note du domaine, donc le placement en boîte de réception de **tous** les autres messages, y compris tes flux rentables.

Chiffre-le. *Hypothèse :* tu envoies à 700 000 adresses au lieu de 400 000 actives, et ton placement en boîte de réception passe de 92 % à 78 %.

```
Perte de placement : 14 ÷ 92 = 15,2 % des messages délivrés
Contribution incrémentale perdue : 0,152 × 249 633 € = 37 944 €/mois
Annuel : 455 330 €
```

**Tu as détruit 455 330 € par an de contribution pour envoyer à 300 000 personnes qui ne t'ouvrent plus.** L'envoi lui-même était gratuit ; c'est ce qui rend l'erreur si fréquente.

La règle : segmentation par engagement en quatre paliers (0–30 jours, 31–90, 91–180, plus de 180), campagnes sur les deux premiers, réactivation sur le troisième, **suppression** du quatrième. Un domaine d'envoi séparé pour les campagnes promotionnelles et pour les flux transactionnels, pour qu'une campagne ratée n'emporte pas les confirmations de commande. Et un plafond de plainte écrit d'avance : au-delà de 0,10 % sur un envoi, on arrête le programme du jour et on cherche pourquoi.
