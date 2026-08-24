# Exercices — Module E14 : Le plan 1 M€/semaine

> **Avant de commencer :** rappel des règles — tout chiffre est marqué (obs) ou
> (est) ; tout montant est marqué TTC ou HT ; les seuils s'écrivent avant le test.
> **Ne lis pas le corrigé avant d'avoir rendu.**

Dernier module du cursus, exercices les plus longs. Conventions : TVA 20 %, un point
de marge d'EBITDA à P5 vaut **433 324 €** par an (1 % du CA HT annuel de 43 332 360 €),
et un chantier qui ne fait basculer aucune condition de passage n'est pas un chantier.

---

## Exercice 1 — Le pont P5 → P5+, refait au centime

Tu n'as le droit d'utiliser que ces données.

| Donnée | P5 | P5+ |
| --- | ---: | ---: |
| Commandes / mois | 60 200 | 56 130 |
| AOV mixte TTC | 71,98 € | 77,20 € |
| Marge brute (CM2) | 61,45 % | 66,00 % |
| MER | 2,90 | 3,40 |
| Part des commandes en réachat | 38,00 % | — |
| nCAC | 40,03 € | — |
| CA HT / mois | 3 610 997 € | — |
| Marge brute / mois | 2 218 957 € | — |
| Dépense publicitaire / mois | 1 494 206 € | — |
| Frais fixes / mois | 360 000 € | — |
| EBITDA / mois | 364 752 € | 733 799 € |

**(1)** Les cinq lignes manquantes de P5+, dans cet ordre.

| Ligne | CA TTC | CA HT | Marge brute | Publicité | **Frais fixes implicites** |
| --- | ---: | ---: | ---: | ---: | ---: |
| P5+ / mois | ______ € | ______ € | ______ € | ______ € | **______ €** |

*Contrôle :* la dépense publicitaire doit retomber sur les 1 274 481 € publiés au § 8
des canoniques. Sinon, arrête-toi.

**(2)** Le pont, en trois lignes.

| Bloc | Écart mensuel |
| --- | ---: |
| Marge brute | ______ € |
| Publicité | ______ € |
| Frais fixes | ______ € |
| **Total / mois** | **______ €** |
| **Total / an** | **______ €** |

*Contrôle :* écart avec les 4 428 560 € du § 8 ≤ 100 €.

**(3) L'attribution inverse.** L'identité du § 6.2 :

```
MER = AOV mixte ÷ (nCAC × part des commandes de première fois)
Contrôle P5 : 71,98 ÷ (40,03 × 0,6200) = 2,900
```

Au modèle, la part des commandes de première fois tombe de 62,00 % à 56,72 % et le
nCAC ne bouge pas. **Nouvelle hypothèse, imposée :** le nCAC baisse de **10 %**, et la
part de réachat ne progresse que de **la moitié du chemin**. Le MER cible reste 3,40 et
le CA TTC reste celui du (1).

| Ligne | Valeur |
| --- | ---: |
| nCAC de P5+ | ______ € |
| Part des commandes de première fois | ______ % |
| Facteur MER dû au nCAC | ×______ |
| Facteur MER dû au réachat | ×______ |
| **Facteur MER dû à l'AOV** (par différence) | **×______** |
| Contrôle : produit des trois | ×______ (cible ×1,17241) |
| **Nouvel AOV mixte** | **______ € TTC** |
| Commandes / mois qui en découlent | ______ |

**(4)** L'attribution du bloc publicité entre les **trois** facteurs. Le § 6.2 en
moyennait deux ordres ; avec trois facteurs il y a **six** ordres, et l'attribution
symétrique est leur moyenne. Montant à répartir : l'écart de publicité du (2).

| Facteur | Gain / mois | Gain / an |
| --- | ---: | ---: |
| AOV | ______ € | ______ € |
| Réachat | ______ € | ______ € |
| nCAC | ______ € | ______ € |
| **Total** | **______ €** | **______ €** |

**(5)** Les six chantiers, refaits. Le bloc marge brute est inchangé : remise 2,50 pts
soit 1 083 309 € par an, COGS et logistique 2,05 pts soit 888 313 €, structure
−180 000 €.

| # | Chantier | Gain / an | Part | Points | Rang au module | **Nouveau rang** |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| A | Panier moyen | ______ € | ___ % | ______ | 2 | |
| B | Part de réachat | ______ € | ___ % | ______ | 1 | |
| C | Discipline de remise | 1 083 309 € | ___ % | +2,50 | 3 | |
| D | nCAC — marque et créa | ______ € | ___ % | ______ | 5 | |
| E | COGS et logistique | 888 313 € | ___ % | +2,05 | 4 | |
| F | Structure | −180 000 € | ___ % | −0,42 | 6 | |
| | **Total** | **______ €** | **100 %** | **______** | | |

**Le chantier qui change de rang, et de combien de places :** ______________________

**(6)** Une ligne du § 8.1 des canoniques devient fausse sous cette hypothèse. Laquelle,
et de combien de points ?

Ligne : ______________  ·  Valeur au modèle : ______  ·  Valeur ici : ______
Écart : ______ pt, soit ______ € par an

> **CORRECTION —** voir [E14-corrige.md](E14-corrige.md) § 1

---

## Exercice 2 — L'effondrement de la rotation créative

Le modèle du § 3.2, rappelé en entier. Un concept meurt après avoir absorbé un
**budget d'exposition fixe** `Bₑ`. Sa durée de vie dépend donc de la pression qu'il
subit, et cette pression dépend du nombre de gagnants en rotation.

```
Durée de vie (N gagnants) = Bₑ ÷ (budget hebdomadaire ÷ N)
Équilibre : N produits par semaine × durée de vie = N en rotation
   ⇔ c × taux de réussite × Bₑ ÷ budget hebdomadaire = 1
   ⇔ c* = budget hebdomadaire ÷ (taux de réussite × Bₑ)
Durée de vie bornée entre 2 et 8 semaines.
   Sous c* : N = 2 × taux de réussite × c      Au-dessus : N = 8 × taux × c
```

| Palier | Budget pub / sem. | Rotation | Durée de vie | Taux de réussite | Concepts / sem. |
| --- | ---: | ---: | ---: | ---: | ---: |
| P2 | 24 147 € | 9 | 5,29 sem. | 12,14 % | 14 |
| P3 | 100 615 € | 21 | 5,00 sem. | 11,05 % | 38 |
| P5 | 344 817 € | 23 | 4,42 sem. | 9,12 % | 57 |

**(1)** Le budget d'exposition de chaque palier, `Bₑ = (budget hebdo ÷ rotation) × durée
de vie` :

| Palier | P2 | P3 | P5 |
| --- | ---: | ---: | ---: |
| `Bₑ` | ______ € | ______ € | ______ € |

Facteur P5 ÷ P2 : ×______   ·   Facteur P5 ÷ P3 : ×______

**(2)** Contrôle du modèle : `c* = budget hebdo ÷ (taux de réussite × Bₑ)` doit
reproduire la dernière colonne du tableau à chaque palier.

| Palier | P2 | P3 | P5 |
| --- | ---: | ---: | ---: |
| `c*` calculé | | | |
| Canonique | 14 | 38 | 57 |

**(3)** À P5, avec le `Bₑ` de P5, la rotation d'équilibre et la pression hebdomadaire
par concept :

| Concepts testés / sem. | Régime (bas / haut) | Rotation | Pression par concept et par semaine |
| ---: | --- | ---: | ---: |
| 35 | | | ______ € |
| 45 | | | ______ € |
| 55 | | | ______ € |
| **57,1 (`c*`)** | équilibre | **23** | **14 992 €** |
| 60 | | | ______ € |
| 70 | | | ______ € |

**(4)** Le même calcul de `c*` à P5, mais en calibrant `Bₑ` sur P2 puis sur P3 (taux de
réussite de P5 conservé) :

| `Bₑ` utilisé | celui de P2 | celui de P3 | celui de P5 |
| --- | ---: | ---: | ---: |
| `c*` à P5 | ______ | ______ | ______ |

**(5)** Pourquoi les trois `Bₑ` diffèrent d'un facteur 4,67, en deux phrases :

______________________________________________________________________

**(6) Le sixième marché.** Une marque à P5 ouvre un septième pays et lui affecte
**1/7 du budget publicitaire hebdomadaire**. *Hypothèse imposée :* le budget
d'exposition d'un concept sur ce marché neuf est celui de **P3**, parce que l'audience
est celle d'un pays et non de sept, et que la marque n'y a aucun stock de mémoire. Le
taux de réussite reste celui de P5.

| Ligne | Valeur |
| --- | ---: |
| Budget hebdomadaire du nouveau marché | ______ € |
| Concepts / semaine nécessaires pour ce seul marché | ______ |
| Ce que suggérerait un raisonnement en moyenne d'entreprise | ______ |
| **Facteur** | **×______** |

**Ce que ça implique, en une phrase :** ______________________________________

> **CORRECTION —** voir [E14-corrige.md](E14-corrige.md) § 2

---

## Exercice 3 — Ton placement sur le tableau de marche

**Ton palier est le dernier dont tu remplis TOUTES les conditions de la porte
d'entrée.** Pas « entre P2 et P3 ».

| | **P1** | **P2** | **P3** | **P4** | **P5** |
| --- | ---: | ---: | ---: | ---: | ---: |
| CA TTC / semaine | 8 492 € | 53 123 € | 271 662 € | 676 523 € | 999 968 € |
| Commandes / jour | 26 | 132 | 593 | 1 385 | 1 984 |
| EBITDA en % du CA HT | −30,7 % | −10,3 % | +5,2 % | +8,1 % | +10,1 % |
| Marge brute (CM2) | 57,20 % | 58,80 % | 60,35 % | 60,40 % | 61,45 % |
| MER réel / seuil EBITDA | 1,80 / 3,33 | 2,20 / 2,71 | 2,70 / 2,42 | 2,80 / 2,35 | 2,90 / 2,33 |
| BFR | 21 603 € | 104 462 € | 481 053 € | 1 392 510 € | 2 264 655 € |

**Mon palier déclaré :** ______   **Le palier que je pensais occuper :** ______

| Indicateur | Ma valeur | (obs)/(est) | Valeur canonique de mon palier | **Écart %** |
| --- | ---: | --- | ---: | ---: |
| CA TTC / semaine | | | | |
| Commandes / jour | | | | |
| EBITDA en % du CA HT | | | | |
| Mois de trésorerie *(cash ÷ (BFR du palier visé + fixes mensuels))* | | | | |

**Mon plus grand écart, et donc le nom de mon problème :** ______________________

> **CORRECTION —** voir [E14-corrige.md](E14-corrige.md) § 3

---

## Exercice 4 — Tes propres conditions de passage

La porte que je vise : ______ → ______ . Chaque ligne se réécrit avec **mes** chiffres.
Trois réponses possibles et pas une de plus : **oui / non / non mesuré**.

| Condition | Seuil recalculé sur mes chiffres | Ma valeur | oui / non / **non mesuré** |
| --- | --- | ---: | --- |
| Coefficient **rendu entrepôt** du héros — port, droits, emballage, casse inclus | | | |
| Marge brute CM2 mesurée | | | |
| **MER seuil (CM3 = 0)** = 1,20 ÷ marge brute | ______ | | |
| **MER seuil (EBITDA = 0)** = 1,20 ÷ (marge brute − fixes en % du CA HT) | ______ | | |
| MER blended sur 4 / 8 / 12 semaines | | | |
| **Débit créatif d'équilibre** = budget hebdo ÷ (taux de réussite × `Bₑ`) | ______ | | |
| Gagnants en rotation · âge moyen de ceux qui portent la dépense | · ≤ 8 sem. | | |
| **AOV mixte minimum** (§ 3.3, avec mon nCAC) | ______ € TTC | | |
| **r90** sur cohorte réelle · LTV/CAC 12 mois · payback | · ≥ 2,00 · ≤ 4 mois | | |
| Part du canal publicitaire principal | | | |
| Trésorerie = BFR visé + 3 à 4 mois de fixes | ______ € | | |
| Responsable dédié aux fonctions exigées par la porte | | | |

**Le calcul de mon AOV minimum**, à poser en entier (§ 3.3) :

```
LTV 12 mois = (AOV 1ʳᵉ ÷ 1,2) × ma marge brute × (1 + mes réachats × ratio d'AOV)
Condition : LTV 12 mois ≥ 2,0 × mon nCAC
AOV 1ʳᵉ minimum = ______ € TTC   →   AOV mixte minimum = ______ € TTC
Ma marge sur le panier = ______ %
```

| Compte | Nombre |
| --- | ---: |
| Conditions à **oui** | |
| Conditions à **non** | |
| Conditions **non mesurées** | |

**Une porte à cinq conditions sur six est une porte fermée.** Ma porte est :
☐ ouverte  ☐ fermée

**La date de mon prochain rituel de porte :** ______________
**Qui le tient :** ______________

> **CORRECTION —** voir [E14-corrige.md](E14-corrige.md) § 4

---

## Exercice 5 — Ton plan à 90 jours

**Trois chantiers. Pas quatre.** Contrainte : chacun doit faire passer au moins une
ligne de l'exercice 4 de « non » ou « non mesuré » à « oui ».

| | Chantier 1 | Chantier 2 | Chantier 3 |
| --- | --- | --- | --- |
| Intitulé | | | |
| **L'indicateur unique qui le mesure** | | | |
| Sa valeur aujourd'hui → sa cible à J+90 | → | → | → |
| **Le critère d'échec, écrit d'avance** | | | |
| Ce qu'on fait si ce critère est atteint | | | |
| **La ligne de l'exercice 4 qui bascule** | | | |
| Le responsable nommé | | | |

**Le test du § 4 :** *si je doublais ce chantier demain, quelle condition de passage
passerait de « non » à « oui » ?* Aucune → je le supprime.

| Chantier | 1 | 2 | 3 |
| --- | --- | --- | --- |
| La condition qui bascule | | | |
| Aucune, je supprime | ☐ | ☐ | ☐ |

**Le chantier de mise en mesure passe avant le chantier commercial.** Respecté ?
☐ oui ☐ non — si non, pourquoi : ______________________________________

> **CORRECTION —** voir [E14-corrige.md](E14-corrige.md) § 5

---

## Exercice 6 — Décision : accélérer ou réparer

**La situation.** Tout est ici.

| Donnée | Valeur |
| --- | ---: |
| CA TTC / semaine | 62 000 € |
| MER blended, 9 semaines | 2,35 |
| Marge brute mesurée (CM2) | 56,5 % |
| Frais fixes / mois | 31 000 € |
| Trésorerie | 340 000 € |
| r90 sur trois cohortes | 14,5 % |
| Gagnants distincts en rotation | 6 |
| Concepts nouveaux testés / semaine | 11 |
| AOV mixte TTC · AOV réachat TTC | 58,00 € · 72,00 € |
| Part des commandes en réachat | 15 % |

**Hypothèses imposées.** Élasticité du CA au budget publicitaire : `CA ∝ budget^0,84`.
Frais fixes constants quel que soit le volume — hypothèse généreuse, note-le. BFR
mobilisé au ratio de P3 : **40 864 € par tranche de 100 000 € de CA TTC mensuel
supplémentaire**. Conversion r90 → 12 mois : `premier réachat = r90 ÷ 0,2742`, puis
`réachats à 12 mois = premier réachat × 2,8182` (§ 2.3). Le gain de r90 monte
linéairement sur 12 mois — compte-le à 50 % en moyenne sur la première année.

**(1)** L'état actuel.

| Ligne | Valeur |
| --- | ---: |
| CA TTC / mois · CA HT / mois | ______ € · ______ € |
| Marge brute · dépense publicitaire | ______ € · ______ € |
| CM3 · **EBITDA / mois** | ______ € · **______ €** |
| Commandes / mois · réachats · nouveaux clients · nCAC | ___ · ___ · ___ · ___ € |
| **MER seuil (CM3 = 0)** · **MER seuil (EBITDA = 0)** | ______ · ______ |
| Écart entre mon MER réel et mon seuil EBITDA | ______ % |

**(2)** Où suis-je sur les portes du § 2.2 ? Porte visée : **P2 → P3**.

| Condition | Seuil | Ma valeur | oui / non |
| --- | ---: | ---: | --- |
| Marge brute CM2 | ≥ 55 % | | |
| MER blended | ≥ 2,20 | | |
| Concepts nouveaux / semaine | ≥ 10 | | |
| Gagnants distincts en rotation | ≥ 5 | | |
| **r90** | ≥ 18 % | | |
| **Trésorerie** | ≥ 796 053 € | | |

**Porte :** ☐ ouverte ☐ fermée — conditions manquantes : ______________

**(3) Option A — tripler le budget publicitaire.**

| Ligne | Valeur |
| --- | ---: |
| Dépense publicitaire / mois | ______ € |
| Facteur appliqué au CA (`3^0,84`) | ×______ |
| CA TTC / mois · **nouveau MER** | ______ € · **______** |
| Marge brute · CM3 · **EBITDA / mois** | ______ € · ______ € · **______ €** |
| EBITDA cumulé sur 12 mois | ______ € |
| BFR supplémentaire mobilisé | ______ € |
| **Besoin de cash total sur 12 mois** | **______ €** |
| Trésorerie disponible | 340 000 € |
| **Manque** | **______ €** |
| **Mois où la trésorerie est épuisée** | **mois ______** |

**(4) Option B — réparer le r90, budget inchangé.**

| Ligne | Valeur |
| --- | ---: |
| Réachats par client à 12 mois : à r90 = 14,5 % · à 18,0 % · **gain** | ___ · ___ · **___** |
| Réachats supplémentaires / mois en régime établi · contribution par réachat | ___ · ___ € |
| **Gain / mois en régime établi** · EBITDA / mois en régime établi | **___ €** · ___ € |
| EBITDA cumulé sur 12 mois (gain à 50 %) · **trésorerie à 12 mois** | ___ € · **___ €** |

**(5)** L'écart entre les deux options sur 12 mois : ______ €

**Ma décision :** ☐ A — accélérer  ☐ B — réparer

**(6)** Les conditions exactes qui renverseraient la décision, et le délai pour savoir.

| Levier | La décision s'inverse si… | En combien de semaines je le sais |
| --- | --- | ---: |
| Élasticité `α` | elle dépasse ______ | ______ |
| r90 | il atteint ______ % | ______ |
| Trésorerie | j'ai ______ € de plus — **et est-ce suffisant ? ☐ oui ☐ non** | ______ |
| Débit créatif | il atteint ______ concepts / semaine | ______ |

**Le levier qui se vérifie le plus vite, donc celui par lequel je commence :**
______________________

**(7)** La phrase de décision, en une ligne, avec son chiffre :

______________________________________________________________________

> **CORRECTION —** voir [E14-corrige.md](E14-corrige.md) § 6

---

## Ma synthèse

**1 — Ce que j'ai appris, en une phrase :**
______________________________________________________________________

**2 — Le chiffre qui m'a le plus surpris, et pourquoi :**
______________________________________________________________________

**3 — La condition de passage que je croyais remplie et qui ne l'est pas :**
______________________________________________________________________

**4 — La décision que ça change chez moi cette semaine :**
______________________________________________________________________

**5 — La date de ma prochaine revue de porte, et qui la tient :**
______________________________________________________________________
