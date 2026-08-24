# Le simulateur de marque — mode d'emploi

> Tu crées une marque, tu la pilotes mois par mois, et tu vois ce que chaque
> décision coûte. Une erreur simulée coûte dix minutes. La même erreur réelle
> coûte deux ans.
>
> Fichier : [`simulateur_marque.py`](simulateur_marque.py). Python 3.9+,
> bibliothèque standard uniquement. Aucune dépendance à installer.

---

## 0. Ce que c'est, et ce que ce n'est pas

C'est un **modèle économique jouable**, calibré sur les
[chiffres canoniques](../donnees/chiffres-canoniques.md) du cursus. Les six
mécanismes qui décident du sort d'une marque DTC y sont représentés
explicitement : la machine créative, le rendement décroissant de l'acquisition,
le panier, le réachat par cohortes, la cascade de marge, et la trésorerie.

Ce n'est **pas** un oracle. Il ne te dira pas combien tu feras l'an prochain. Il
te fera sentir, en quarante minutes, des enchaînements de causes à effets qui
mettent normalement deux ans à se manifester — et dont la cause est justement
invisible quand l'effet arrive.

Le simulateur est **entièrement déterministe à graine fixée** : mêmes décisions,
même graine, mêmes chiffres au centime. C'est ce qui rend les exercices
corrigeables, et ce qui te permet de rejouer une partie en ne changeant qu'une
seule décision pour isoler son effet.

---

## 1. Démarrer en une commande

```bash
# le mode le plus pédagogique : cinq stratégies, une seule graine, un tableau
python3 ecommerce/outils/simulateur_marque.py --comparer

# joue toi-même, tour par tour
python3 ecommerce/outils/simulateur_marque.py --interactif

# rejoue un scénario écrit d'avance
python3 ecommerce/outils/simulateur_marque.py \
    --scenario ecommerce/outils/scenarios/S00-la-trajectoire-de-reference.json

# écris le déroulé complet en markdown
python3 ecommerce/outils/simulateur_marque.py --auto equilibree --rapport partie.md

# vérifie que le modèle se comporte comme annoncé
python3 ecommerce/outils/simulateur_marque.py --verifier
```

Options communes : `--graine N`, `--categorie CODE`, `--prix 39`, `--coef 8`,
`--capital 250000`, `--mois 60`, `--mois-depart 1` (mois calendaire du
lancement — il change la saisonnalité des CPM), `--muet` (masque le mois par
mois).

---

## 2. Tour 0 — la création

Tu choisis une **catégorie**, un **prix TTC**, un **coefficient visé** et un
**capital**. Ces quatre décisions sont prises avant la première vente et
plafonnent tout le reste.

| Code | Coef. max | Réachat | Retours | Logistique | Marché FR | CPM |
|---|---:|---:|---:|---:|---:|---:|
| `soin_cheveux` | ×8,0 | 3,0 mois | 3,5 % | 11 % | 45 000 000 € | 14 € |
| `complement` | ×7,5 | 1,5 mois | 2,0 % | 9 % | 38 000 000 € | 16 € |
| `soin_visage` | ×8,5 | 2,5 mois | 4,0 % | 10 % | 62 000 000 € | 18 € |
| `animalerie` | ×6,0 | 2,0 mois | 5,0 % | 15 % | 28 000 000 € | 12 € |
| `maison_deco` | ×4,5 | 14,0 mois | 12,0 % | 22 % | 70 000 000 € | 11 € |
| `mode_accessoire` | ×3,5 | 10,0 mois | 28,0 % | 17 % | 120 000 000 € | 13 € |

> **Le coefficient visé est plafonné par la catégorie.** Tu ne décides pas
> d'acheter à ×8 ce que le marché fournisseur vend à ×4,5. Le coefficient
> détermine ton COGS de départ : `COGS unitaire = prix TTC ÷ coefficient`.

**Joue `maison_deco` et `mode_accessoire` une fois.** Sur sept graines, la
stratégie « équilibrée » y fait faillite **sept fois sur sept**, avec une marge
brute de 25 % au lieu de 61 %. Ce n'est pas un défaut du simulateur : c'est le
cas [C01](../etudes-de-cas/C01-coefficient-insuffisant.md), et c'est la raison
pour laquelle le [diagnostic](../mentorat/diagnostic.md) commence par le bloc A.

Capital par défaut : **250 000 €**, soit les pertes cumulées modélisées de P1 et
P2 plus le BFR de P2 ([canoniques § 2.2 et § 4](../donnees/chiffres-canoniques.md)).
Ce n'est pas un chiffre rond choisi au hasard : c'est la porte 0 → P1 des
[jalons](../mentorat/jalons.md).

---

## 3. Les dix décisions de chaque mois, et ce qu'elles influencent

| Décision | Ce qu'elle change directement | Ce qu'elle change six mois plus tard |
|---|---|---|
| `budget_pub` | nouveaux clients — **à rendement décroissant** (`clients ∝ budget^0,72`) | le CAC marginal, donc le MER, donc l'EBITDA |
| `part_test_crea` | nombre de concepts testés ce mois-ci | **la qualité créative, donc le CAC de tout le compte** |
| `remise` | +conversion immédiate, −AOV, −marge brute | **le réachat des cohortes acquises en promotion** |
| `invest_retention` | rien ce mois-ci | la courbe de réachat de toutes les cohortes |
| `invest_offre` | le multiplicateur de panier, **de façon permanente** | l'AOV, donc le premier levier d'EBITDA |
| `commande_stock` | l'acompte payé maintenant | le stock disponible dans **2 mois** — et la rupture |
| `recrutement` | les frais fixes, immédiatement | le plafond de qualité créative (sous-effectif = créa bridée) |
| `ouvrir_marche` | 30 000 € de mise en place | le marché adressable, donc la saturation, donc le CAC |
| `prix_ttc` | l'AOV, le COGS, et le nombre de clients à budget égal | la marge brute, via le coût de colis qui, lui, ne bouge pas |
| `part_canal_principal` | rien | **la probabilité de bannissement du compte publicitaire** |

### Les quatre mécanismes qu'il faut avoir compris pour bien jouer

**1. Le rendement décroissant.** `clients = A × budget^0,72`. Conséquence
arithmétique : le **CAC marginal vaut le CAC moyen ÷ 0,72**, soit 39 % de plus.
Le tableau de bord affiche les deux, côte à côte, exprès. Quand tu décides
d'ajouter 20 % de budget, c'est le CAC marginal qui s'applique, jamais le moyen.

**2. Le coût d'un test créatif monte avec la taille du compte.** 259 € par
concept à 104 636 € de budget mensuel, 900 € à 1 494 206 € — les deux valeurs
sortent des [canoniques § 6](../donnees/chiffres-canoniques.md). Un gros compte
doit donc dépenser *proportionnellement* autant en test qu'un petit pour tenir
le même stock de gagnants.

**3. Le stock a un délai de 2 mois.** Le niveau de recomplètement doit couvrir
le délai fournisseur **plus** la période de révision, soit au moins 3 mois de
demande future. En dessous, la rupture est arithmétique quelle que soit ta
trésorerie. Une rupture ne coûte pas seulement les ventes du mois : elle inflige
une **pénalité durable de 15 % sur la qualité créative**, parce que l'algorithme
a désappris.

**4. La trésorerie n'est pas l'EBITDA.** Tu paies l'acompte du stock deux mois
avant de le vendre, le solde à la livraison, la publicité le mois même, et tu
encaisses 78 % du chiffre d'affaires dans le mois, 22 % le mois suivant. Une
marque qui croît de 30 % par mois avec ce cycle est en faillite technique bien
avant d'être non rentable.

---

## 4. Lire le tableau de bord

```
Mois │   CA TTC │  Cmd │   AOV │ %Réa │      Pub │  MER │  CACm │  CACx │ Qcré │ Gag │  MB % │      CM3 │   EBITDA │    Trésorerie │ JSt
```

| Colonne | Définition | Ce qui doit t'alerter |
|---|---|---|
| **CA TTC** | encaissé, net de remise | — |
| **AOV** | panier moyen TTC | stagnation : ton offre ne travaille pas |
| **%Réa** | part des commandes en réachat | sous 15 % après 12 mois : tu loues de l'attention |
| **MER** | CA TTC ÷ dépense pub | sous ton MER seuil CM3, chaque euro de CA détruit de la marge |
| **CACm / CACx** | CAC moyen / **marginal** | l'écart est structurel : CACx = CACm ÷ 0,72 |
| **Qcré** | qualité créative, bornée [0,55 ; 1,45] | à 0,55 tu paies tes clients 82 % plus cher qu'à 1,00 |
| **Gag** | concepts gagnants vivants | une décrue de trois mois de suite est une alerte rouge |
| **MB %** | marge brute (CM2) en % du CA HT facturé | sous 55 % : retourne au bloc A du diagnostic |
| **CM3** | marge brute − publicité | négatif = tu finances la croissance avec ton capital |
| **JSt** | jours de stock | sous 25 jours, la rupture est mécanique |

Les pourcentages de la cascade sont calculés sur le **CA HT facturé avant
remise**, exactement comme les [canoniques § 2.1](../donnees/chiffres-canoniques.md),
pour que les deux tableaux soient comparables ligne à ligne. Le « CA TTC »
affiché est, lui, ce que tu encaisses réellement.

---

## 5. Les événements

Tirés à graine fixe, probabilités mensuelles déclarées en constantes en tête du
fichier, chacun annoncé en clair avec son effet chiffré.

| Événement | Probabilité | Effet |
|---|---:|---|
| Bannissement du compte publicitaire | 2,0 %/mois, **majorée** par la concentration sur un canal et par la remise | 62 % du budget du mois rendu inefficace |
| Retard fournisseur | 9,0 %/mois | livraisons décalées d'un mois |
| Entrée d'un concurrent | 5,5 %/mois | −11 % de clients à budget égal, **durable et cumulatif** |
| Contenu viral | 4,5 %/mois | +38 % de clients pendant 2 mois |
| Litige qualité | 2,5 %/mois | +2 points de retours pendant 3 mois, 12 000 € immédiats |
| Pic de CPM | novembre et décembre | indice ×1,32 et ×1,45 |

> La probabilité de bannissement se calcule ainsi :
> `2,0 % × (1 + 1,8 × excès de concentration au-delà de 60 %) × (1 + 2,2 × remise)`.
> Un compte mono-canal à 95 % qui pratique 14 % de remise court **2,1 fois** le
> risque d'un compte diversifié sans promotion : `(1 + 1,8 × 0,35) × (1 + 2,2 ×
> 0,14) = 1,63 × 1,31 = 2,13`. C'est le cas
> [C10](../etudes-de-cas/C10-compte-publicitaire-banni.md), rendu jouable.

---

## 6. Les cinq stratégies automatiques

`--auto NOM`, ou toutes ensemble avec `--comparer`.

| Stratégie | Ce qui la définit |
|---|---|
| `prudente` | MER visé 3,00, croissance ≤ +20 %/mois, jamais de remise, 15 % de test créatif |
| `agressive` | MER visé 1,40, croissance ≤ +85 %/mois, 92 % de la trésorerie engagée, un seul canal à 95 %, stock au plus juste |
| `equilibree` | MER visé 2,45, croissance ≤ +35 %/mois, 15 % de test, 3 % de remise, 4,5 % du CA HT en rétention, bascule sur le pilotage de la marge à 70 % de l'objectif |
| `sans_test_crea` | **identique à `equilibree`, sauf `part_test_crea = 0`** |
| `remise_permanente` | **identique à `equilibree`, sauf `remise = 18 %`** |

Les deux dernières ne diffèrent de la troisième que par **un seul paramètre**.
C'est délibéré : tout écart de résultat est imputable à cette décision-là et à
aucune autre.

Sortie de `--comparer` sur la graine 7, `soin_cheveux`, prix 39 € TTC,
coefficient ×8, capital 250 000 €, horizon 60 mois :

| Stratégie | Mois | Issue | CA TTC/sem. (moy. 6 derniers mois) | Meilleure semaine | EBITDA % CA HT | Trésorerie min. | EBITDA cumulé | Qualité créa |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| prudente | 60 | horizon atteint | 697 101 € | 721 744 € | 19,1 % | 176 678 € | 13 221 120 € | 1,45 |
| agressive | **9** | **faillite (cash)** | 17 820 € | 30 745 € | −15,8 % | **−15 736 €** | −143 561 € | 0,60 |
| equilibree | 60 | horizon atteint | **897 437 €** | **942 236 €** | 8,9 % | 82 817 € | 10 408 301 € | 1,45 |
| sans_test_crea | 60 | horizon atteint | 38 928 € | 42 507 € | 3,9 % | 58 284 € | 396 925 € | **0,55** |
| remise_permanente | 60 | horizon atteint | 136 188 € | 176 233 € | −1,1 % | 45 891 € | 1 573 891 € | 1,45 |

> **Lis les deux dernières lignes contre la troisième.** `sans_test_crea` et
> `remise_permanente` ont eu exactement le même budget, le même capital, les
> mêmes marchés, les mêmes événements et la même graine que `equilibree`. Un
> paramètre a changé dans chacune. Le premier divise le chiffre d'affaires
> cumulé par 13, le second par 6.
>
> **Et regarde `prudente`.** Elle finit avec moins de chiffre d'affaires que
> `equilibree` mais **27 % d'EBITDA cumulé en plus**. Ce n'est pas un bug de
> calibrage : c'est le rendement décroissant. Passé un certain MER, chaque euro
> de budget supplémentaire achète un client plus cher que ce qu'il rapporte.
> C'est exactement le débat P5 contre P5+.

---

## 7. Les scénarios rejouables

Dans [`scenarios/`](scenarios/). Format JSON, une liste de décisions indexée par
mois ; les mois non décrits reconduisent la décision précédente, sauf les actes
ponctuels (ouverture de marché, changement de prix, investissement d'offre,
recrutement). `reappro_auto` et `recrutement_auto` évitent d'écrire à la main le
réapprovisionnement et l'effectif.

| Scénario | Ce qu'il change | Résultat à 36 mois (graine 7) |
|---|---|---|
| `S00-la-trajectoire-de-reference` | rien — c'est le témoin | survit, 480 776 € TTC/sem., EBITDA cumulé 3 596 536 € |
| `S01-la-discipline-creative` | `part_test_crea → 0` au mois 13 | **faillite**, qualité créative 0,55, **0 gagnant vivant** |
| `S02-le-piege-de-la-remise` | `remise → 25 %` au mois 9 | **faillite**, marge brute 40,8 %, réachat 40,3 % au lieu de 66,2 % |
| `S03-le-coefficient-insuffisant` | mêmes décisions, catégorie `maison_deco` | **faillite**, marge brute 25,9 %, EBITDA cumulé **−161 683 €** |

**La bonne façon de les utiliser :** joue S00, note les chiffres. Joue S01. Ne
lis pas le total — regarde le mois où la courbe se retourne, et compte combien
de mois se sont écoulés depuis la décision qui l'a causée.

---

## 8. Les cinq leçons que ce simulateur est fait pour te faire découvrir

### Leçon 1 — le vrai goulot n'est ni le budget ni l'algorithme, c'est la créa

Coupe `part_test_crea` à 0 en gardant **tout le reste identique**. Le stock de
concepts gagnants met quatre à six mois à s'éteindre : pendant ce temps, rien ne
se voit. Puis la qualité créative tombe à son plancher, le CAC double, et le
compte s'éteint. Sur graine 7, `sans_test_crea` termine à **−92,5 % de CA TTC
cumulé** face à `equilibree`, pour une seule décision d'écart.

**Ce que ça t'apprend :** le délai entre la cause et l'effet est de six mois,
exactement le délai qui rend la cause invisible quand l'effet arrive. Module
[E05](../modules/E05-machine-creative.md).

### Leçon 2 — la remise achète du chiffre d'affaires et vend ta marge deux fois

La remise fonctionne : elle augmente vraiment la conversion (+0,9 point de
clients par point de remise). C'est précisément ce qui la rend tentante. Elle te
coûte ensuite **deux fois** : une fois sur la marge brute du mois, une seconde
fois sur la courbe de réachat des clients acquis en promotion, qui reviennent
jusqu'à 42 % moins souvent. Sur 60 mois, `remise_permanente` produit du chiffre
d'affaires — mais **8,9 centimes d'EBITDA par euro de CA contre 10,3** pour
`equilibree`, avec une marge brute de 46,5 % contre 61,5 %.

**Ce que ça t'apprend :** une promotion ne se juge jamais sur le mois où elle est
lancée, mais sur la cohorte à douze mois. Modules
[E03](../modules/E03-offre-et-prix.md) et [E08](../modules/E08-retention-et-ltv.md),
cas [C09](../etudes-de-cas/C09-piege-du-black-friday.md).

### Leçon 3 — la trésorerie tue avant la rentabilité

`agressive` fait faillite **8 fois sur 10** sur 40 graines, alors que sa marge
brute est correcte et que son chiffre d'affaires monte plus vite que celui de
toutes les autres. Elle ne meurt pas de perdre de l'argent : elle meurt de payer
son stock deux mois avant de l'encaisser, sur une base qui double tous les deux
mois.

**Ce que ça t'apprend :** la croissance consomme du cash tant que le BFR est
positif. Ta croissance maximale n'est pas fixée par ta rentabilité mais par ton
cycle de conversion. Module [E10](../modules/E10-cash-et-operations.md), cas
[C02](../etudes-de-cas/C02-vallee-de-la-mort.md).

### Leçon 4 — la structure est décidée avant la première vente

Joue exactement les mêmes décisions en `soin_cheveux` puis en `maison_deco`
(c'est S00 contre S03). Même budget, même discipline créative, même rétention,
même graine. La première survit avec 61 % de marge brute ; la seconde meurt avec
26 %. Aucune quantité d'exécution ne compense un coefficient à ×4,5 assorti de
12 % de retours et de 22 % de logistique.

**Ce que ça t'apprend :** le travail que tu fournis ne s'ajoute pas à ta
structure, il se multiplie par elle. Modules
[E01](../modules/E01-arithmetique-de-la-marque.md) et
[E02](../modules/E02-marche-et-produit.md), cas
[C01](../etudes-de-cas/C01-coefficient-insuffisant.md).

### Leçon 5 — ton objectif n'est pas 1 M€/semaine, c'est P5+

La condition de victoire demande **les deux à la fois** : 1 000 000 € de CA TTC
par semaine **et** 15 % d'EBITDA, tenus trois mois consécutifs. Tu découvriras
vite qu'il est facile d'avoir l'un **ou** l'autre. Acheter du volume au MER 2,0
te donne le chiffre d'affaires et pas la marge ; piloter au MER 3,0 te donne la
marge et pas le volume. Les stratégies non agressives basculent volontairement
sur le pilotage de la marge à 70 % de l'objectif : c'est le passage P5 → P5+ des
[canoniques § 8](../donnees/chiffres-canoniques.md), qui double l'EBITDA sans un
euro de chiffre d'affaires supplémentaire.

**Ce que ça t'apprend :** le chiffre d'affaires est une conséquence, pas un
objectif. Modules [E14](../modules/E14-plan-1M-semaine.md) et
[E12](../modules/E12-marque-et-actif.md).

---

## 9. Vérifier le modèle toi-même

```bash
python3 ecommerce/outils/simulateur_marque.py --verifier --graines 40
```

Quatre comportements sont contrôlés à chaque exécution : que `sans_test_crea`
finisse nettement plus mal que `equilibree`, que `agressive` ait une probabilité
élevée de rupture de trésorerie, que `remise_permanente` produise du chiffre
d'affaires et peu d'EBITDA, et que les ordres de grandeur d'une partie
`equilibree` en `soin_cheveux` restent cohérents avec les chiffres canoniques.

---

## 10. Ce que ce simulateur ne dit pas

- **Le produit n'existe pas.** Le modèle ne connaît ni la qualité perçue, ni le
  positionnement, ni la marque. Deux joueurs avec les mêmes paramètres obtiennent
  les mêmes chiffres : dans la vraie vie, non.
- **Un seul produit, un seul prix.** Pas de gamme, pas de mix. Le
  multiplicateur d'offre représente les bundles et l'upsell de façon agrégée, et
  plafonne à ×1,45.
- **L'organisation est réduite à un nombre d'ETP.** Ni compétence, ni
  recrutement raté, ni départ d'une personne clé.
- **Les canaux publicitaires sont agrégés.** Une seule courbe d'acquisition, un
  seul CPM. `part_canal_principal` ne sert qu'à moduler le risque de
  bannissement. Le module [E06](../modules/E06-acquisition-payante.md) et le cas
  [C06](../etudes-de-cas/C06-test-incrementalite.md) traitent ce que le
  simulateur agrège.
- **L'attribution est parfaite.** Le simulateur connaît le vrai nombre de
  nouveaux clients. Ton tableau de bord réel, jamais — c'est tout l'objet du
  module [E09](../modules/E09-mesure-et-incrementalite.md).
- **L'élasticité au prix est une hypothèse**, pas une mesure : le nombre de
  clients varie en `(prix de référence ÷ ton prix)^0,85`. Le gain d'un
  positionnement premium vient dans ce modèle du coût de colis, qui est
  physique et ne monte pas avec ton prix.
- **La saturation est modélisée par pays**, sans concurrence explicite sur les
  mêmes segments. L'entrée d'un concurrent est un événement, pas un acteur.

*Fin du mode d'emploi. Le fichier de référence reste
[`simulateur_marque.py`](simulateur_marque.py) : toutes les constantes du modèle
sont déclarées en tête, avec leur justification.*
