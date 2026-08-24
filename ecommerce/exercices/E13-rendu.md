# Exercices — Module E13 : Le risque de ruine

> **Avant de commencer :** rappel des règles — tout chiffre est marqué (obs) ou
> (est) ; tout montant est marqué TTC ou HT ; les seuils s'écrivent avant le test.
> **Ne lis pas le corrigé avant d'avoir rendu.**

Calculatrice obligatoire, et une qui fait les puissances. Convention valable partout :
une probabilité annuelle est **déclarée comme une estimation**, jamais présentée comme
une mesure — et elle s'écrit quand même. Un nombre faux se corrige ; une intuition non
écrite ne se corrige jamais.

---

## Exercice 1 — La survie de NØRA

Le modèle du § 0, rappelé en entier. Trois issues par an : la marque meurt avec une
probabilité `p` ; si elle survit, elle **triple** une année sur trois et croît de
**20 %** les deux autres années.

```
E[G] conditionnel à la survie = (1/3) × 3,0 + (2/3) × 1,2 = 1,80
Facteur annuel espéré, ruine comprise = (1 − p) × 1,80
```

**(1)** Complète le tableau. Les probabilités de survie sont `(1 − p)^t`.

| | **p = 5 %** | **p = 10 %** | **p = 20 %** |
| --- | ---: | ---: | ---: |
| Survie à 3 ans | | | |
| Survie à 5 ans | | | 32,8 % |
| Survie à 10 ans | | 34,9 % | |
| Survie à 20 ans | | | |
| Une chance sur deux d'être mort au bout de | ______ ans | ______ ans | ______ ans |
| Facteur annuel espéré | | | |
| **Valeur espérée à 5 ans (base 1)** | | **11,16 ×** | |
| Valeur espérée à 10 ans | | | |

*Contrôle :* la colonne p = 10 % doit reproduire exactement le tableau du § 0.

**(2)** Écris en une phrase ce que la ligne « une chance sur deux d'être mort » change
par rapport à la ligne « survie à 5 ans » pour quelqu'un qui a 32 ans et une seule
entreprise.

______________________________________________________________________

**(3) Le modèle modifié.** La marque triple désormais **une année sur cinq**, et croît
de **15 %** les quatre autres.

| Ligne | Valeur |
| --- | ---: |
| Nouveau `E[G]` conditionnel à la survie | |
| Valeur espérée à 5 ans si `p = 0` (plafond absolu du modèle lent) | |
| `p` qui égalerait l'ancien modèle à `p = 10 %` (11,16 ×) | |

**(4)** Renverse la question : à quel `p` **l'ancien** modèle — la croissance rapide —
retombe-t-il à la valeur du modèle lent parfait (`p = 0`) ?

`p` = ______ %

**(5)** La phrase d'arbitrage croissance / survie, en une ligne, avec son chiffre :

______________________________________________________________________

> **CORRECTION —** voir [E13-corrige.md](E13-corrige.md) § 1

---

## Exercice 2 — Le registre recalculé

Le registre de NØRA au palier P5 (§ 7.2), recopié en entier. EBITDA annuel de
référence : **4 377 023 €**. Réserve du palier : **1 243 595 €**.

| # | Risque | p/an | Impact | Espérance | Coût/an de la mesure | p rés. | Impact rés. | Espér. rés. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| R1 | Bannissement Meta, 11 j | 25 % | 414 464 € | 103 619 € | 36 000 € | 10 % | 414 464 € | 41 448 € |
| R2 | Coupure Meta ≥ 30 j | 6 % | 1 077 639 € | 64 658 € | — | 2,5 % | 1 077 639 € | 26 941 € |
| R3 | Sanction allégations | 8 % | 650 000 € | 52 000 € | 108 000 € | 2 % | 650 000 € | 13 000 € |
| R4 | Traceurs, perte de signal | 5 % | 1 583 244 € | 79 162 € | 60 000 € | 1,5 % | 1 583 244 € | 23 749 € |
| R5 | Rappel de lot | 2 % | 2 519 502 € | 50 390 € | 71 500 € | 1 % | 1 100 000 € | 11 000 € |
| R6 | Rupture fournisseur, 45 j | 6 % | 1 497 806 € | 89 868 € | 75 398 € | 1,5 % | 400 000 € | 6 000 € |
| R7 | Rétrofacturations > seuil PSP | 4 % | 1 200 000 € | 48 000 € | 69 267 € | 1 % | 1 200 000 € | 12 000 € |
| R8 | Perte des accès critiques | 8 % | 900 000 € | 72 000 € | 9 000 € | 1,5 % | 900 000 € | 13 500 € |
| | **Total** | | | **559 697 €** | **429 165 €** | | | **147 638 €** |

**Convention imposée :** quand on multiplie les probabilités par `k`, on multiplie
**les deux** — nominale et résiduelle. Une mesure ne devient ni meilleure ni pire
parce que le monde est plus dangereux.

**(1)** Les trois jeux de probabilités. Le scénario **c** ne touche que la probabilité
nominale de R1, qui passe de 25 % à 40 % ; sa probabilité résiduelle reste à 10 %.

| | Espérance totale | Espérance résiduelle | Gain en espérance | Coût | **Solde** |
| --- | ---: | ---: | ---: | ---: | ---: |
| Référence | 559 697 € | 147 638 € | 412 059 € | 429 165 € | **−17 106 €** |
| **a** — probabilités ÷ 2 | | | | 429 165 € | |
| **b** — probabilités × 2 | | | | 429 165 € | |
| **c** — R1 à 40 % | | | | 429 165 € | |

**(2)** Le multiplicateur `k` à partir duquel le programme devient rentable **en
espérance seule** :

`k` = ______

**(3)** Pour chaque ligne du § 7.3, le multiplicateur `k*` au-delà duquel **cette
mesure-là** devient positive. Une mesure est positive quand `k × gain ≥ coût`.

| Ligne | R1+R2 | R8 | R6 | R4 | R5 | R7 | R3 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Gain en espérance | 99 888 € | 58 500 € | 83 868 € | 55 413 € | 39 390 € | 36 000 € | 39 000 € |
| Coût annuel | 36 000 € | 9 000 € | 75 398 € | 60 000 € | 71 500 € | 69 267 € | 108 000 € |
| **`k*`** | | | | | | | |
| Positive à ÷2 ? | | | | | | | |
| Positive à ×2 ? | | | | | | | |

**(4)** Rapport **impact ÷ réserve** (1 243 595 €) : les lignes au-dessus de 1,00 sont
celles que l'indicateur n° 6 du tableau de bord compte, et dont le seuil est zéro.

| Ligne | R5 | R4 | R6 | R7 | R2 | R8 | R3 | R1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Impact ÷ réserve | | | | | | | | |
| > 1,00 ? | | | | | | | | |

**(5)** Croise (3) et (4) : combien de lignes sont **à la fois** au-dessus de la
réserve et couvertes par une mesure d'espérance négative à la référence ? ______
Ce que ça implique sur la façon de trier un registre :

______________________________________________________________________

**(6)** La lecture en survie (§ 7.4), refaite. Valorisation à 6 × EBITDA.

| Valorisation de P5 | Points de survie gagnés (90,4 − 59,0) | Valeur de survie créée | Coût sur 5 ans | **Rapport** |
| ---: | ---: | ---: | ---: | ---: |
| ______ € | ______ pts | ______ € | ______ € | **______ pour 1** |

> **CORRECTION —** voir [E13-corrige.md](E13-corrige.md) § 2

---

## Exercice 3 — Ton registre des risques

Dix lignes minimum. Chaque impact est **calculé** et sa ligne de calcul figure dans le
tableau ; chaque probabilité est un nombre écrit ; chaque mesure a un coût annuel, y
compris en marge ou en conversion.

**Ta réserve actuelle :** ______ €    **Ton EBITDA annuel :** ______ €

| # | Risque, formulé comme un événement daté | p/an (est) | Impact (calcul) | Impact € | Espérance | Mesure | Coût/an | p rés. | Espér. rés. |
| --- | --- | ---: | --- | ---: | ---: | --- | ---: | ---: | ---: |
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |
| 5 | | | | | | | | | |
| 6 | | | | | | | | | |
| 7 | | | | | | | | | |
| 8 | | | | | | | | | |
| 9 | | | | | | | | | |
| 10 | | | | | | | | | |
| | **Total** | | | | | | | | |

**Les deux tris.**

| Rang | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Par **gain net** | | | | | |
| Par **impact ÷ réserve** | | | | | |

**Les lignes qui changent de rang de plus de trois places :** ______________________

**Grille imposée :** *si les deux classements donnent le même ordre, tu as sous-estimé
au moins un impact.* Est-ce ton cas ? ☐ oui ☐ non — si oui, laquelle et pourquoi :

______________________________________________________________________

> **CORRECTION —** voir [E13-corrige.md](E13-corrige.md) § 3

---

## Exercice 4 — Ta trésorerie de survie

```
Semaines de survie = (Trésorerie nette disponible
                      − engagements non annulables à moins de 90 jours)
                     ÷ Frais fixes hebdomadaires
```

Les définitions comptent plus que la formule. **Fais toutes les soustractions.**

| Ligne | Montant |
| --- | ---: |
| Solde bancaire | ______ € |
| + Encaissements PSP à recevoir sous 7 jours | + ______ € |
| **− TVA collectée non reversée** | − ______ € |
| **− Dettes fournisseurs échues ou à 30 jours** | − ______ € |
| **− Commandes encaissées non expédiées** | − ______ € |
| **− Charges sociales et fiscales dues** | − ______ € |
| **− Crédit remboursable à vue** | − ______ € |
| **= Trésorerie nette disponible** | **______ €** |

**Engagements non annulables à moins de 90 jours**, avec leur date d'exigibilité :

| Engagement | Date | Montant |
| --- | --- | ---: |
| Commandes fournisseurs signées | | ______ € |
| Loyers et contrats à préavis long | | ______ € |
| Recrutements signés · engagements média forfaitaires | | ______ € |
| Autre : | | ______ € |
| **Total** | | **______ €** |

| Ligne | Valeur |
| --- | ---: |
| Frais fixes mensuels | ______ € |
| Frais fixes hebdomadaires (÷ 4,3333) | ______ € |
| **Mes semaines de survie** | **______** |
| Mon délai fournisseur réel, mesuré sur mes 3 dernières commandes | ______ jours |
| Ce délai + 4 semaines, en semaines | ______ |
| **Écart** | **______ semaines** |

**Si l'écart est négatif :** montant à réunir ______ €, date à laquelle il doit être
en banque ______________, et par quel moyen : ______________________

> **CORRECTION —** voir [E13-corrige.md](E13-corrige.md) § 4

---

## Exercice 5 — Tes six dépendances

Mesure sur **douze mois**, dans l'unité indiquée — pas dans celle qui t'arrange.

| Dépendance | Unité de mesure imposée | Ma valeur | Vigilance | Alerte | Critique | Mon niveau |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Premier canal d'acquisition | part des **nouveaux clients réels** | ___ % | > 40 % | > 55 % | > 70 % | |
| Premier produit | part du CA HT | ___ % | > 40 % | > 55 % | > 70 % | |
| Premier fournisseur | part du **COGS annuel** | ___ % | > 50 % | > 70 % | mono-source | |
| Premier marché | part de la **marge brute** | ___ % | > 40 % | > 55 % | > 70 % | |
| Premier prestataire logistique | part des colis expédiés | ___ % | > 60 % | > 80 % | site unique | |
| Premier prestataire de paiement | part des encaissements | ___ % | > 70 % | > 90 % | PSP unique | |

**Le délai de substitution**, et le produit qui classe vraiment tes dépendances :

| Dépendance | Délai de substitution (sem.) | Perte hebdomadaire si elle disparaît demain | **Produit** | ÷ réserve |
| --- | ---: | ---: | ---: | ---: |
| Premier canal | | ______ € | ______ € | |
| Premier produit | | ______ € | ______ € | |
| Premier fournisseur | | ______ € | ______ € | |
| Premier marché | | ______ € | ______ € | |
| Premier logisticien | | ______ € | ______ € | |
| Premier PSP | | ______ € | ______ € | |

**Classement par ce produit, du plus grave au moins grave :** 1. ______________
2. ______________  3. ______________

**Ma dépendance la plus grave est-elle celle dont le pourcentage est le plus élevé ?**
☐ oui ☐ non — si non, explique pourquoi en une phrase :

______________________________________________________________________

> **CORRECTION —** voir [E13-corrige.md](E13-corrige.md) § 5

---

## Exercice 6 — Décision : diversifier ou tenir

**La situation.** Toutes les données sont ici.

| Donnée | Valeur |
| --- | ---: |
| Nouveaux clients réels / mois, tous canaux | 12 000 |
| Part du premier canal | 62 % |
| CAC du premier canal | 34,00 € |
| CAC moyen des autres canaux | 48,00 € |
| LTV 12 mois en contribution | 86,75 € |
| Part du CA en réachat | 40 % |
| Réserve de trésorerie | 480 000 € |
| Frais fixes / mois | 145 000 € |
| Probabilité annuelle estimée d'une coupure ≥ 45 jours du premier canal | 2,5 % |

**Hypothèses imposées.** La diversification se fait **à budget publicitaire constant**
— on déplace, on n'ajoute pas. Une coupure de 45 jours détruit `clients du canal ×
(LTV 12 mois − CAC du canal) × 1,5 mois`, plus un coût d'apprentissage : 7 jours de
reprise à **+30 % de CPA** sur le budget quotidien du canal (mois de 30,4 jours).

**(1)** L'état actuel et le coût de la diversification à 45 %.

| Ligne | Valeur |
| --- | ---: |
| Clients du premier canal / mois · budget du canal | ______ · ______ € |
| Budget des autres canaux · **budget total / mois** | ______ € · **______ €** |
| CAC moyen pondéré à la cible 45 / 55 | ______ € |
| Clients totaux après diversification, à budget constant | ______ / mois |
| **Clients perdus** | **______ / mois** |
| **Contribution perdue** | **______ € / mois — ______ € / an** |
| Clients du premier canal après diversification | ______ / mois |

**(2)** L'impact d'une coupure de 45 jours, avant et après.

| Ligne | Avant (62 %) | Après (45 %) |
| --- | ---: | ---: |
| Contribution détruite (1,5 mois) | ______ € | ______ € |
| Coût d'apprentissage | ______ € | ______ € |
| **Impact total** | **______ €** | **______ €** |
| **Impact ÷ réserve** | **×______** | **×______** |
| Au-dessus de la réserve ? | ☐ oui ☐ non | ☐ oui ☐ non |

**(3)** La lecture en espérance, sur 24 mois.

| Réduction d'impact | Espérance évitée / an | sur 24 mois | Coût sur 24 mois | **Rapport** |
| ---: | ---: | ---: | ---: | ---: |
| ______ € | ______ € | ______ € | ______ € | **______ pour 1** |

**Ma décision :** ☐ diversifier  ☐ tenir

**(4)** Les trois conditions exactes qui renverseraient la décision.

| Levier | La décision s'inverse si… |
| --- | --- |
| Probabilité annuelle de coupure | elle dépasse ______ % |
| Trésorerie | ma réserve dépasse ______ €, soit ______ € à réunir — à comparer aux ______ € par an de la diversification, rapport ×______ |
| Part réelle du canal dans le CA à 12 mois | elle tombe sous ______ % |

*Aide pour la troisième :* le § 2.2. La part du canal dans le CA du mois est
`62 % × la part des premières commandes` ; la part réelle, à douze mois, est autre
chose. Donne les deux nombres et l'écart en points.

**(5)** La phrase de décision, en une ligne, avec son chiffre :

______________________________________________________________________

> **CORRECTION —** voir [E13-corrige.md](E13-corrige.md) § 6

---

## Ma synthèse

**1 — Ce que j'ai appris, en une phrase :**
______________________________________________________________________

**2 — Le chiffre qui m'a le plus surpris, et pourquoi :**
______________________________________________________________________

**3 — Le risque que je n'avais jamais écrit nulle part :**
______________________________________________________________________

**4 — La décision que ça change chez moi cette semaine :**
______________________________________________________________________

**5 — La date de ma prochaine revue de registre, et qui la tient :**
______________________________________________________________________
