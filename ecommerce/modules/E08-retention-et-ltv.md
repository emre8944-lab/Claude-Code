# Module E08 — La rétention, les cohortes et la LTV

> **Prérequis :** [E01](E01-arithmetique-de-la-marque.md), [E02](E02-marche-et-produit.md), [E03](E03-offre-et-prix.md), [E07](E07-funnel-et-conversion.md).
> **Objet :** construire et lire un tableau de cohortes, calculer une LTV en marge qui tient devant un banquier, et piloter les leviers qui font revenir un client.
> **Temps de travail :** ~5 h (lecture + exercices)

---

## 0. Pourquoi ce module existe

Ouvre les [chiffres canoniques](../donnees/chiffres-canoniques.md) au § 2.4, dernière colonne. Aux cinq paliers, sans exception, la marge de NØRA sur la **première** commande est négative : −4,93 € en P1, −3,83 € en P2, −3,01 € en P3, −6,06 € en P4, **−7,26 € en P5**.

En P5, ce n'est pas une nuance comptable, c'est toute l'entreprise :

```
Contribution des réachats       22 876 × 43,53 €   =   995 792 €/mois
1ʳᵉ commande nette du CAC       37 324 × (−7,26 €) =  −270 972 €/mois
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

Une marque DTC qui achète son trafic sans réachat n'est pas une marque à faible marge : c'est une marque qui n'existe pas, qui finance la croissance de sa régie publicitaire avec le capital de ses actionnaires. **La rétention est le seul endroit du modèle où il y a de l'argent.**

---

## 1. La cohorte, proprement définie

### 1.1 Définition

Une **cohorte** est un groupe de clients acquis pendant la même période — le mois de leur **première** commande — et suivi ensuite sans jamais changer de composition. Un client entre dans une cohorte et une seule, et il y reste même quand il cesse d'acheter. C'est parce qu'on le garde au dénominateur que la mesure est honnête.

Deux axes à ne jamais confondre : l'**âge** de la cohorte (mois depuis l'acquisition, noté M+1, M+3…) et le **mois calendaire**. Tout le pouvoir de la méthode vient de leur séparation.

### 1.2 Pourquoi la moyenne globale ment

Marque en croissance, trois cohortes, courbe canonique (§ 3) : 1,24 réachat par client à 12 mois, 0,72 à 6 mois, 0,06 à 1 mois.

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

Le pilote qui lit 1,08 applique la règle du § 3 (« LTV/CAC 12 mois < 1,5 : on ne scale pas, on répare ») et coupe le budget d'une marque dont la cohorte mature est à 1,24 réachat, 86,75 € de LTV, ratio **2,17**.

Inverse les effectifs — 16 000 en A, 4 000 en B, 1 000 en C — sans rien changer d'autre : moyenne globale 1,085 réachat, LTV 80,00 €, ratio **2,00**.

**Le même business affiche 1,08 quand il croît et 2,00 quand il décroît.** La moyenne globale ne mesure pas la rétention, elle mesure la forme de ta courbe d'acquisition : elle te félicite quand tu meurs et te punit quand tu gagnes. Dans une cohorte, tous les clients ont le même âge ; ce biais disparaît.

### 1.3 Construire le tableau

**Maille :** le mois par défaut ; la semaine si ton cycle de consommation est sous 30 jours ; le trimestre seulement sous 300 clients/mois, en dessous le bruit dépasse le signal.

**Valeur dans la cellule :** quatre candidates, deux bonnes.

| Valeur | Verdict |
| --- | --- |
| CA cumulé TTC par client | À proscrire — § 8, erreur 7 |
| Commandes cumulées par client | Diluée par le « 1 » de départ. Acceptable pour un rapport |
| **Réachats cumulés par client** | **Celle-là** : exactement ce que tu pilotes |
| Contribution cumulée par client | La seconde à tenir : c'est elle qui décide d'un investissement |

La première commande vaut 1 pour tout le monde, par construction, et écrase les variations. Une cohorte passée de 1,34 à 1,30 commande cumulée à M+3 a l'air d'avoir perdu 3 % ; en réachats, elle est passée de 0,34 à 0,30, soit **−11,8 %**. Même fait, quatre fois plus lisible.

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

**Le long d'une ligne — la maturation.** M31 accumule 0,72 réachat en six mois sur les 1,24 de sa première année : **58 % des réachats de l'année arrivent dans les six premiers mois** (0,72 ÷ 1,24). Tu peux donc juger une cohorte avant sa maturité, et le pilotage devient possible. Ce qui n'est pas gagné à M+6 ne se rattrape presque plus : 0,087 réachat par mois entre M+7 et M+12, contre 0,14 entre M+1 et M+3.

**Le long d'une colonne — la qualité des cohortes successives.** Colonne M+3 : 0,34 → 0,33 → 0,32 → 0,30. Quatre cohortes consécutives sous la précédente au même âge. Ce n'est plus du bruit, c'est une pente. C'est la lecture qui décide.

**La diagonale — les effets de période.** Les cellules atteintes le même mois calendaire forment une diagonale : en M36 tu observes M31 à M+5, M32 à M+4, M33 à M+3, M34 à M+2, M35 à M+1. Un événement qui frappe **le mois** — rupture de stock sur le héros, bug de paiement, gueule de bois post-soldes — fait décrocher toute la diagonale d'un coup, et les colonnes se rétablissent le mois suivant. **Diagonale = période, colonne = cohorte.** Ce tri coûte cinq minutes et se fait en premier.

---

## 2. Le signal d'alarme numéro un

### 2.1 Ce qu'il coûte

Colonne M+3 : 0,34 pour M31, 0,30 pour M34, soit −11,8 %. Propagation constante jusqu'à 12 mois — l'hypothèse la plus prudente, elle n'invente aucune aggravation :

```
Réachats 12 mois : 1,24 × (1 − 0,118)        = 1,094
LTV contribution : 32,77 € + 1,094 × 43,53 € = 80,38 €
LTV / nCAC : 80,38 ÷ 40,03                   = 2,01
```

Tu passes de 2,17 à 2,01 : au-dessus du seuil canonique de 2,0, mais de 0,01, et la cohorte M35 n'a pas fini d'arriver. En euros, via le levier du § 7 (+10 % de commandes de réachat = 1 194 871 € d'EBITDA annuel) :

```
1 194 871 € × 1,18 = 1 409 948 €/an, soit 32,2 % de l'EBITDA de référence
```

**Quatre cohortes mensuelles viennent d'effacer un tiers de l'EBITDA annuel, et le compte de résultat du mois ne montre rien.** Il ne montrera rien pendant six à douze mois, parce que les réachats manquants sont des réachats futurs. C'est pour ça que le tableau de cohortes existe : c'est le seul instrument du tableau de bord qui soit en avance sur le résultat.

### 2.2 Les trois causes, et comment les distinguer

| | Saturation de l'audience | Dérive du produit | Dérive de la promesse |
| --- | --- | --- | --- |
| **Mécanisme** | Les acheteurs faciles sont épuisés ; l'algorithme va chercher des profils de plus en plus éloignés du cœur | Formule, fournisseur, lot ou emballage ont changé, ou la qualité a glissé sans que personne l'écrive | La créa promet plus que le produit ne tient, pour tenir le CPA |
| **Forme** | Lente, régulière, corrélée à la hausse du budget | Brutale et **datée** : toutes les cohortes après une date précise, tous canaux confondus | Progressive, limitée aux cohortes issues des nouveaux concepts |
| **nCAC** | **Monte** | Stable | **Baisse** — la sur-promesse convertit mieux |
| **Retours, SAV** | Stables | **Montent** dans la même fenêtre | Montent au premier usage, pas à la livraison |
| **Test** | Cohorter par canal : si Google Search marque tient et que la prospection large s'effondre, c'est la saturation | Croiser la date de bascule avec les numéros de lot et les changements de fournisseur | Cohorter par **concept créatif** ; verbatims SAV : « ce n'est pas ce qui était montré » |
| **Réponse** | Élargir l'offre, monter l'AOV, ouvrir un marché — [E11](E11-passage-a-echelle.md) | Arrêter, corriger, rappeler les lots | Réécrire la promesse, tuer les concepts — [E05](E05-machine-creative.md) |

La ligne décisive est la troisième. **Un nCAC qui baisse pendant que la rétention baisse est une signature unique** : la saturation fait monter le CAC, la dérive produit le laisse tranquille. Si ton coût d'acquisition s'améliore pendant que tes cohortes se dégradent, tu n'as pas trouvé un bon angle — tu as trouvé un mensonge rentable à court terme, et tu le paieras sur douze mois de réachat, au prix du § 2.1.

Un quatrième suspect s'écarte avant les trois autres : le **mix promotionnel**. Une cohorte acquise pendant une semaine à −30 % contient une proportion anormale de chasseurs de remise, qui ne rachètent qu'en promotion. Ce n'est pas une dérive, c'est une composition. Test : cohorter selon la présence d'un code promo sur la première commande — [C09](../etudes-de-cas/C09-piege-du-black-friday.md).

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
100,30 = 1,18 × AOV réachat  →  AOV réachat = 85,00 € TTC
AOV 1ʳᵉ commande = 69,10 − 0,06 × 85,00 = 64,00 € TTC
```

Contrôle sur le § 2 : 37 324 × 64,00 € + 22 876 × 85,00 € = 4 333 196 €, exactement le CA TTC mensuel de P5. Second contrôle : (85,00 ÷ 1,2) × 61,45 % = 43,53 €, la contribution de réachat canonique — 61,45 % étant la somme exacte des lignes du § 2.1, que le tableau arrondit à 61,5 %.

**Le panier de réachat dépasse de 33 % le panier d'acquisition** (85,00 € contre 64,00 €). C'est pourquoi un réachat rapporte 43,53 € de contribution quand une première commande n'en rapporte que 32,77 € : un client qui revient achète le rituel entier, pas le produit d'appel.

### 3.3 Ce que le payback autorise

```
Contribution cumulée à M+1 : 35,38 €  (sous le CAC de 40,03 €)
Contribution cumulée à M+3 : 47,57 €  (au-dessus)
1 + (40,03 − 35,38) ÷ (47,57 − 35,38) × 2 = 1,76 → ≈ 1,8 mois
```

Il ne faut pas 1,24 réachat pour rembourser l'acquisition, il en faut `7,26 € ÷ 43,53 € = 0,167`. **Un client sur six qui repasse une seule commande, et l'acquisition est remboursée.** Tout le reste de la courbe est du profit net d'acquisition : c'est ce qui rend le modèle si sensible au **premier** réachat et si peu aux suivants.

| Nombre | P5 | Ce qu'il autorise |
| --- | ---: | --- |
| Payback | 1,8 mois | Financer l'acquisition avec ~2 mois de trésorerie roulante. Avec 45 à 60 jours de crédit fournisseur, la croissance est presque autofinancée en marge — pas en stock, [E10](E10-cash-et-operations.md) |
| LTV/CAC 12 mois | 2,17 | Au-dessus de 2,0 : on accélère. Marge de sécurité de 8 % seulement |
| LTV/CAC 24 mois | 2,97 | Ce qu'on montre à un prêteur, si les 24 mois sont observés et non extrapolés |
| Réachats 12 → 24 mois | 1,24 → 1,98 | +0,74 réachat, soit +32,21 € par client : le prix d'attendre, l'argent restant immobilisé |

Le ratio de 3,45 à 36 mois est vrai et inutile pour décider : une décision média se prend sur l'argent qui revient avant que tu doives le redépenser. **Pilote sur 12 mois, publie sur 24, ne décide jamais sur 36.**

---

## 4. Le premier réachat est le seul qui compte vraiment

### 4.1 La démonstration

Le canonique donne un total (1,24 à 12 mois) mais pas sa décomposition. *Hypothèse déclarée :* je pose le passage de la commande 1 à la commande 2 à **44 %** et je choisis les taux conditionnels suivants de sorte que la somme des probabilités cumulées reproduise **exactement** le 1,24 canonique. Le total est contraint par le § 3 ; seule la répartition est un choix de modélisation.

| Passage | Probabilité cumulée d'atteindre ce rang | Taux conditionnel |
| --- | ---: | ---: |
| Commande 1 → 2 | 0,44 | **44,0 %** |
| Commande 2 → 3 | 0,29 | 65,9 % |
| Commande 3 → 4 | 0,20 | 69,0 % |
| Commande 4 → 5 | 0,14 | 70,0 % |
| Commande 5 → 6 | 0,10 | 71,4 % |
| Commande 6 → 7 | 0,07 | 70,0 % |
| **Somme** | **1,24** | |

Le premier passage est à 44 %, tous les suivants entre 66 % et 71 %. **Le premier réachat est une fois et demie plus difficile que tous les autres.** Ce n'est pas un accident de calibrage : un client qui a commandé deux fois a vérifié que le produit marche, que le colis arrive et que le SAV répond. Il n'a plus rien à découvrir. Un client qui a commandé une fois n'a encore rien vérifié.

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

Les quatre premiers ne coûtent presque rien en marketing ; c'est sur le cinquième que tout le monde se jette.

| Rang | Levier | Pourquoi là |
| ---: | --- | --- |
| 1 | **L'expérience produit** | Elle plafonne tous les autres : si ton produit satisfait 55 % de tes acheteurs, ton premier réachat ne dépassera pas durablement 55 %. Mesure-le — enquête à J+30, une question, une note sur 10 — et traite ce chiffre comme le plafond sous lequel toute la section 5 travaille |
| 2 | **La livraison** | Première promesse tenue ou trahie, avant même l'essai. L'écart promis/réel compte plus que le délai : annoncer 5 jours et livrer en 4 satisfait davantage qu'annoncer 2 et livrer en 3 — [E10](E10-cash-et-operations.md) |
| 3 | **Le contenu d'accompagnement** | Un soin mal dosé ne donne pas de résultat. Le flux post-achat ne vend pas, il **fait réussir l'usage** : dose, fréquence, trois erreurs courantes, résultat attendu à la semaine 6 pour que le client ne conclue pas trop tôt. Meilleur rapport effort/rendement du module, et le plus négligé — il ne produit aucune vente attribuée le jour de l'envoi |
| 4 | **Le moment de la relance** | Calé sur la durée de consommation réelle (§ 4.4). Levier de timing, pas de message : le même e-mail au bon et au mauvais moment n'a pas le même rendement, à un facteur qui se compte en multiples |
| 5 | **L'offre de réapprovisionnement** | Réassort en un clic du produit exact. Efficace, et volontairement dernier : une remise à qui n'a pas eu de résultat ne produit rien, et une remise à qui allait racheter au prix fort te coûte la remise — § 7.2 |

### 4.4 Le calendrier de consommation

**On ne relance pas après un délai, on relance avant une date d'épuisement.** Un délai est un chiffre recopié d'un article de blog ; une date d'épuisement se calcule. Les dosages ci-dessous sont des *hypothèses*, contrôlées par le fait que le canonique vend une « Cure 3 mois » composée de 3 sérums, ce qui fixe la durée d'un sérum à un mois.

| Produit (§ 1) | Contenance | Dosage (hypothèse) | Épuisement |
| --- | ---: | --- | ---: |
| Sérum Densité | 50 ml | 1,6 ml/jour | **31 jours** |
| Shampooing Fortifiant | 250 ml | 10 ml × 3 lavages/semaine | **58 jours** |
| Masque Réparateur | 200 ml | 15 ml × 1 application/semaine | **93 jours** |
| Rituel Complet | les 3 | premier vide : le sérum | **31 jours** |
| Cure 3 mois | 3 sérums | 3 × 31 jours | **93 jours** |

Contrôle : 50 ÷ 1,6 = 31,3 jours, cohérent avec les 3 mois annoncés pour 3 sérums. Le mix des premières commandes doit reproduire l'AOV d'acquisition de 64,00 € TTC (§ 3.2) — *hypothèse contrainte* :

```
0,25 × 39,00 € (Sérum seul)  9,75 €    0,42 × 74,00 € (Rituel)      31,08 €
0,20 × 99,00 € (Cure)       19,80 €    0,08 × 24,00 € (Shampooing)   1,92 €
0,05 × 29,00 € (Masque)      1,45 €                        Total    64,00 €

Épuisement moyen pondéré du premier article vide :
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
