# Exercices — Module E12 : La marque comme actif

> **Avant de commencer :** rappel des règles — tout chiffre est marqué (obs) ou
> (est) ; tout montant est marqué TTC ou HT ; les seuils s'écrivent avant le test.
> **Ne lis pas le corrigé avant d'avoir rendu.**

Calculatrice obligatoire. Conventions valables partout dans ce fichier : TVA 20 %,
la **marge brute (CM2) de P5 vaut 61,45 %** du CA HT (valeur exacte des chiffres
canoniques § 2.1 — le module arrondit à 61,5 %, ce qui décale les EBITDA d'environ
900 € ; utilise 61,45 %), les frais fixes de P5 valent 360 000 € par mois et ne
bougent pas dans une coupure publicitaire. Arrondis les effectifs de clients et de
commandes à l'unité **avant** de multiplier par un prix.

---

## Exercice 1 — Le test de coupure de NØRA, avec d'autres hypothèses de survie

Toutes les données dont tu as besoin sont ici.

| Donnée — NØRA au palier P5 | Valeur |
| --- | ---: |
| CA TTC / mois | 4 333 196 € |
| Commandes / mois | 60 200 |
| Nouveaux clients / mois | 37 324 |
| Part du CA en réachat | 44,9 % |
| Marge brute (CM2) | 61,45 % du CA HT |
| Dépense publicitaire / mois | 1 494 206 € |
| Frais fixes / mois | 360 000 € |
| EBITDA / mois avant coupure | 364 752 € |
| Multiples de valorisation retenus (hypothèse) | bas 4,0× · central 5,5× · haut 7,0× |

**(1)** Redérive les deux paniers moyens de P5 — tu n'as le droit d'utiliser que
les quatre premières lignes du tableau.

| Ligne | Valeur |
| --- | ---: |
| CA de réachat / mois | ______ € TTC |
| CA de première commande / mois | ______ € TTC |
| Commandes de réachat / mois | ______ |
| **AOV de première commande** | **______ € TTC** |
| **AOV de réachat** | **______ € TTC** |

*Contrôle obligatoire :* `AOV 1ʳᵉ ÷ 1,2 × 61,45 %` doit retomber sur les 32,77 € de
contribution à la première commande des canoniques § 2.4, à quelques centimes près.
Si l'écart dépasse 0,10 €, ne va pas plus loin.

**(2)** Nouvelles hypothèses de coupure, imposées — plus optimistes que celles du
module. Part des nouveaux clients qui survit : **25 / 20 / 17 / 14 / 11 %** aux mois
1, 2, 3, 6 et 12. Facteur appliqué aux commandes de réachat : **0,92 / 0,88 / 0,84 /
0,72 / 0,55** aux mêmes mois. Aucune dépense publicitaire, aucun changement de prix,
aucune baisse des frais fixes.

| Mois de coupure | Nouveaux | Cmd. réachat | CA TTC | % du niveau P5 | CA HT | EBITDA |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Mois 0 (référence) | 37 324 | | 4 333 196 € | 100,0 % | 3 610 997 € | 364 752 € |
| Mois 1 | | | | | | |
| Mois 3 | | | | | | |
| Mois 6 | | | | | | |
| Mois 12 | | | | | | |

**(3)** Ta **demande autonome** (CA du mois 1 ÷ CA du mois 0) : ______ %

**(4)** Le mois où l'EBITDA repasse **sous** son niveau d'avant coupure, par
interpolation linéaire entre tes deux derniers points : mois ______

**(5)** Dans le module, ce mois de bascule vaut 6. Écris en une phrase pourquoi il
se déplace, et ce que ça t'apprend sur la lecture d'un compte de résultat.

______________________________________________________________________

**(6)** L'acquéreur du § 8. L'EBITDA annuel de P5 (4 377 023 €) **ne bouge pas**
d'une hypothèse de survie à l'autre — seul le multiple bouge.

| Ligne | Valeur |
| --- | ---: |
| Valorisation au multiple central 5,5× | ______ € |
| Valorisation au multiple haut 7,0× | ______ € |
| Écart entre les deux | ______ € |
| Points de demande autonome gagnés vs les 48,3 % du module | ______ pts |
| **Valeur d'un point de demande autonome** | **______ €** |

> **CORRECTION —** voir [E12-corrige.md](E12-corrige.md) § 1

---

## Exercice 2 — La bascule de budget au palier P3

Le module chiffre au § 6.2 une bascule de 5 % du budget publicitaire vers la marque
au palier P5. Refais-la à **P3**, avec une bascule de **8 %**.

| Donnée — NØRA au palier P3 | Valeur |
| --- | ---: |
| Dépense publicitaire P2 / P3 | 104 636 € / 436 000 € par mois |
| Nouveaux clients P2 / P3 | 3 400 / 13 140 par mois |
| Commandes / mois à P3 | 18 000 |
| nCAC moyen à P3 | 33,18 € |
| Contribution 1ʳᵉ commande à P3 | 30,17 € |
| LTV 12 mois en contribution à P3 | 80,06 € |
| Réachats à 12 mois par client (canonique § 3) | 1,24 |
| CA HT / mois à P3 | 981 000 € |
| EBITDA / mois à P3 | 51 033 € |
| Structure de coût variable à P3 | COGS 16,0 % · logistique 12,0 % · PSP 1,65 % · retours 3,0 % · remises 7,0 % |

**(1)** CAC marginal P2 → P3 : `(______ − ______) ÷ (______ − ______)` = ______ €

**(2)**

| Ligne | Valeur |
| --- | ---: |
| Montant basculé (8 % du budget P3) | ______ € / mois |
| Clients perdus | ______ / mois |
| Clients perdus | ______ / an |
| **Contribution annuelle perdue** (LTV 12 mois, régime établi) | **______ €** |
| EBITDA annuel de P3 | ______ € |
| **Part de l'EBITDA annuel concernée** | **______ %** |

**(3)** Les trois formulations du seuil de neutralité, à P3.

| Levier | Seuil |
| --- | ---: |
| Baisse du nCAC | ______ %, soit 33,18 € → ______ € |
| Commandes de réachat supplémentaires | + ______ / mois, soit + ______ % |
| Hausse de l'AOV | + ______ % |

*Aide pour la troisième :* la convention des canoniques § 7 traite le COGS comme
**proportionnel au prix** (plus de panier = plus d'unités) et la logistique comme
**fixe par commande**. Vérifie-la d'abord à P5 : elle doit reproduire les
3 139 401 € de la ligne « +10 % de panier moyen » au millier près.

**(4)** Comparaison avec P5.

| | P3, bascule 8 % | P5, bascule 8 % | P5, bascule 5 % (module § 6.2) |
| --- | ---: | ---: | ---: |
| Part de l'EBITDA annuel | ______ % | ______ % | 38,2 % |

**(5)** Explique l'écart en **deux facteurs chiffrés**, dont le produit doit
reproduire le rapport entre la colonne P3 et la colonne P5 à 8 %.

Facteur 1 — ______________________________________ = ×______
Facteur 2 — ______________________________________ = ×______
Produit = ×______   ·   Rapport constaté = ×______

> **CORRECTION —** voir [E12-corrige.md](E12-corrige.md) § 2

---

## Exercice 3 — Ton test de coupure

Conçois-le **avant** de l'exécuter. Un test dont les seuils sont écrits après coup
n'est pas un test, c'est une justification.

| Élément | Ta réponse |
| --- | --- |
| Marché ou zone témoin | |
| Preuve de comparabilité (3 indicateurs sur 6 mois) | |
| Durée de la coupure | |
| Ce que je coupe | |
| Ce que je laisse tourner — et pourquoi, ligne par ligne | |
| — e-mail et SMS : coupé / gardé, motif | |
| — recherche sur mon nom : coupé / gardé, motif | |
| — reciblage : coupé / gardé, motif | |
| — affiliation et influence : coupé / gardé, motif | |
| **Coût attendu, calculé d'avance** | ______ € (marqué TTC ou HT) |
| Seuil d'arrêt anticipé n° 1, écrit avant | |
| Seuil d'arrêt anticipé n° 2, écrit avant | |

**Après exécution :**

| Ligne | Valeur | (obs) ou (est) ? |
| --- | ---: | --- |
| CA du mois précédent, zone témoin | ______ € TTC | |
| CA du mois de coupure, zone témoin | ______ € TTC | |
| **Demande autonome** | **______ %** | |
| Part de ce CA venant du réachat | ______ % | |
| Part venant de nouveaux clients | ______ % | |

**Si je ne peux pas me le permettre**, voici le calcul qui le prouve — coût attendu
de la coupure rapporté à ma trésorerie disponible :

______________________________________________________________________

> **CORRECTION —** voir [E12-corrige.md](E12-corrige.md) § 3

---

## Exercice 4 — L'inventaire de tes actifs distinctifs

Le test qui compte : montre l'actif **seul, sans ton nom**, à dix personnes de ta
catégorie et demande de quelle marque il s'agit.

| Candidat | Dernière modification | Part de mes assets des 90 derniers jours qui le portent | Reconnu par ___ / 10 | Actif ou dépense de design ? |
| --- | --- | ---: | ---: | --- |
| Nom | | % | | |
| Couleur dominante | | % | | |
| Forme du flacon / du packaging | | % | | |
| Typographie | | % | | |
| Visage récurrent | | % | | |
| Signature sonore | | % | | |
| Format éditorial répété | | % | | |
| Autre : | | % | | |

**Nombre d'actifs reconnus par au moins 3 personnes sur 10 :** ______

**Celui que je ne changerai plus, et la date à laquelle je m'y engage :**

______________________________________________________________________

**Une refonte est-elle à l'ordre du jour chez moi ?** ☐ oui ☐ non
Si oui, son coût chiffré par la méthode du § 4.1, sur **mes** chiffres :
`CA HT mensuel ______ € × 8 % × marge brute ______ % × 9 mois =` ______ €

> **CORRECTION —** voir [E12-corrige.md](E12-corrige.md) § 4

---

## Exercice 5 — Tes cinq mesures du § 3.1

Pour chacune : la valeur, la source **exacte** (pas « mon analytics »), et ce qui la
rendrait fausse. Les lignes dont tu ne sais pas nommer la source forment ta **dette
de mesure**.

| # | Mesure | Valeur | (obs)/(est) | Source exacte | Ce qui la rendrait fausse |
| --- | --- | ---: | --- | --- | --- |
| 1 | Indice de mémoire (impressions sur requêtes de marque ÷ dépense pub du mois) | | | | |
| 1b | Sa variation sur 3 mois, à dépense constante | ___ % | | | |
| 2 | Part du trafic direct + organique de marque | ___ % | | | |
| 3 | Taux de conversion à froid (prospection pure, hors reciblage) | ___ % | | | |
| 4 | Prix acceptable : variation de volume ÷ variation de prix | | | | |
| 5 | Réachat sans relance (aucun contact CRM sous 7 jours) | ___ % | | | |

**Ma dette de mesure — les lignes sans source nommable :** ______________________

**La première que j'installe, et sous combien de semaines :** ____________________

> **CORRECTION —** voir [E12-corrige.md](E12-corrige.md) § 5

---

## Exercice 6 — Décision : le canal sous le seuil

**La situation.** Tu pilotes NØRA à P5. Un canal secondaire coûte **62 000 € par
mois** et apporte **1 050 nouveaux clients** — CAC 59,05 €, LTV 12 mois en
contribution **88,00 €**, ratio 1,49. Ton seuil interne est 2,0 ; ton ratio global
est 2,20. Ton directeur de l'acquisition veut couper ce canal et verser ses 62 000 €
sur Meta.

| Donnée | Valeur |
| --- | ---: |
| Budget Meta actuel | 821 813 € / mois |
| Clients attribués à Meta | 21 346 / mois |
| CAC moyen Meta | 38,50 € |
| LTV 12 mois en contribution, base NØRA | 86,75 € |
| Élasticité du volume au budget (§ 7.1) | α = 0,84 |
| Nouveaux clients réels / mois, tous canaux | 37 324 |
| dont Meta, en clients réels | 19 261, soit 51,6 % |
| Facteur de conversion attribué → réel (§ 5) | 0,9023 |
| EBITDA annuel de P5 | 4 377 023 € |

**Convention imposée pour la comparaison :** 24 mois d'acquisition, chaque cohorte
mensuelle évaluée à sa LTV 12 mois en contribution. Les deux options sont comptées
en clients **attribués** — le facteur 0,9023 s'applique des deux côtés et ne change
donc pas le classement ; tu ne l'utilises que pour la question de concentration.

**(1)** Le report sur Meta, avec `clients = k × budget^0,84` :

| Ligne | Valeur |
| --- | ---: |
| Ratio de budget après report | ×______ |
| Facteur appliqué au volume de clients | ×______ |
| Clients Meta après report | ______ / mois |
| **Clients gagnés** | **______ / mois** |
| **CAC marginal du report** | **______ €** |

**(2)** Les deux options sur 24 mois :

| | Option A — garder le canal | Option B — couper et reporter |
| --- | ---: | ---: |
| Clients acquis sur 24 mois | | |
| Contribution générée | ______ € | ______ € |
| Budget engagé | ______ € | ______ € |
| **Solde** | **______ €** | **______ €** |
| Contribution nette par euro dépensé | ______ € | ______ € |

**Ma décision :** ☐ A — garder  ☐ B — couper

**(3)** Ce que le calcul ne voit pas. Part de Meta dans tes nouveaux clients
**réels** après le report : ______ % (contre 51,6 % avant).

**(4)** Les trois conditions exactes qui renverseraient la décision. Chacune est un
nombre, pas une opinion.

| Levier | La décision s'inverse si… |
| --- | --- |
| Élasticité de Meta | α tombe sous ______ |
| Décote de multiple à la revente pour concentration | elle dépasse ______ × d'EBITDA |
| Demande autonome détruite par la coupure du canal | elle dépasse ______ point(s) |

**(5)** Écris la phrase de décision, en une ligne, avec son chiffre :

______________________________________________________________________

> **CORRECTION —** voir [E12-corrige.md](E12-corrige.md) § 6

---

## Ma synthèse

**1 — Ce que j'ai appris, en une phrase :**
______________________________________________________________________

**2 — Le chiffre qui m'a le plus surpris, et pourquoi :**
______________________________________________________________________

**3 — Ce que je croyais avant, et qui est faux :**
______________________________________________________________________

**4 — La décision que ça change chez moi cette semaine :**
______________________________________________________________________

**5 — Ce que je mesurerai dans 90 jours pour savoir si j'avais raison :**
______________________________________________________________________
