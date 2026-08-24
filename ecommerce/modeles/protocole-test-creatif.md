# Protocole de test créatif

> **À quoi ça sert :** fixer **avant** une vague comment on jugera — budget, durée, seuils, décisions. Un seuil écrit après coup n'est pas un seuil, c'est une justification.
> **Quand l'utiliser :** une fois à la mise en place, puis un en-tête rempli avant chaque vague. Les concepts viennent du [brief créatif](brief-creatif.md).
> **Module rattaché :** E05 — la machine créative. Compléments : [E09](../modules/E09-mesure-et-incrementalite.md) (attribution) et l'outil [`test_significativite.py`](../outils/test_significativite.py).

---

## 1. Concept nouveau, variation, déclinaison

Trois objets, trois budgets. Les confondre fausse le taux de réussite, donc le plan média.

| Ce qui change | Statut | Budget |
|---|---|---|
| L'angle | **concept nouveau** | tranche 1 complète |
| Le mécanisme, du problème ou de la solution | **concept nouveau** | tranche 1 complète |
| Le format ou le dispositif (UGC, statique, démo…) | **concept nouveau** | tranche 1 complète |
| L'accroche, l'ordre des preuves, le casting, le décor, la durée, la fin — à angle et mécanisme inchangés | **variation** | pas de tranche 1 : entre en rotation |
| Le ratio, les sous-titres, la langue | **déclinaison** | jamais jugée séparément |

Définition du [tableau de bord](../mentorat/tableau-de-bord.md) § 1 : *angle **ou** mécanisme **ou** format différent*. Compter une variation comme un concept nouveau gonfle le dénominateur et fait croire à une machine deux fois plus productive.

---

## 2. La structure de la campagne de test

Une campagne dédiée, séparée de la rotation, en trois tranches.

| Tranche | Où | Budget cumulé / concept | Décision |
|---|---|---|---|
| **T1 — sélection** | campagne de test (enveloppe 15 %) | 12 × CPA cible | couper ou promouvoir |
| **T2 — confirmation** | campagne principale (enveloppe 85 %) | 30 × CPA cible | conserver, scaler ou couper |
| **T3 — échelle** | campagne principale | libre | variations, rotation |

Quatre règles non négociables :

1. **Un concept = un groupe d'annonces = un budget forcé, identique pour tous.** Si l'algorithme répartit, il tranche avant toi sur 40 € HT, et tu ne mesures plus que sa décision.
2. **Même audience large, même placement, même page de destination.** Seul le concept varie.
3. **Aucun remarketing dans la campagne de test.** Servi à une audience chaude, un concept affiche un CPA sans rapport avec sa capacité de recrutement.
4. **Tous les concepts démarrent le même jour, à la même heure.** Le jour de la semaine vaut plusieurs points de CPA.

---

## 3. Le budget par concept selon le palier

Dérivé des [chiffres canoniques](../donnees/chiffres-canoniques.md) § 6 : `budget de test hebdo ÷ concepts testés`.

| Palier | Budget de test / sem. | Concepts / sem. | **T1 par concept** | CPA cible (nCAC) | Multiple de la cible | Plancher de jugement |
|---|---:|---:|---:|---:|---:|---:|
| P2 | 3 622 € HT | 14 | **258,71 € HT** | 30,78 € HT | ×8,4 | 113,55 € HT |
| P3 | 15 092 € HT | 38 | **397,16 € HT** | 33,18 € HT | ×12,0 | 122,40 € HT |
| P5 | 51 722 € HT | 57 | **907,40 € HT** | 40,03 € HT | ×22,7 | 147,67 € HT |

Le **plancher de jugement** vaut **3,69 × CPA cible** : la dépense sous laquelle un zéro achat ne veut rien dire, puisqu'un concept tenant exactement la cible a encore 2,5 % de chances de ne rien montrer. C'est la règle des trois CPA.

La qualité de décision **s'achète avec l'échelle** : le budget de test vaut 8,4 fois la cible à P2, 22,7 fois à P5. **P1 n'est pas au tableau**, et pour cause : `20 444 × 12 ÷ 52 × 15 % = 707,70 € HT` par semaine, soit deux concepts à 12 × 26,62 € HT. À P1 une vague dure quinze jours et compte six concepts ; en annoncer quinze, c'est tirer au sort.

> **À retenir :** l'enveloppe de test achète des clients **plus cher** que la rotation, et c'est normal. À P3, la vague du § 11 les paie 50,00 € HT, soit `15 092 ÷ 50,00 = 302` clients par semaine sur les `13 140 × 12 ÷ 52 = 3 032` de la marque (canoniques § 2.4) ; la rotation absorbe le reste à `(100 615 − 15 092) ÷ 2 730 = 31,33 € HT`, et le mélange redonne `100 615 ÷ 3 032 = 33,18 € HT` — le nCAC canonique. **Une vague qui affiche le CPA cible est une vague qui n'a rien testé.**

---

## 4. La durée minimale, et pourquoi

**La décision se déclenche sur la dépense atteinte, pas sur le calendrier**, qui ne pose qu'un plancher et un plafond.

**Plancher : 72 heures.** Deux raisons. L'apprentissage : un groupe neuf est servi à un coût instable tant que l'algorithme manque de signaux. La conversion différée : *hypothèse — environ 20 % des achats surviennent plus de 24 h après le clic*. Juger à 24 h, c'est juger sur 80 % des achats en croyant en compter 100 %.

**Plafond : 7 jours.** Un concept qui n'a pas dépensé sa tranche en sept jours n'est pas un perdant : il n'a pas été servi. CPM élevé, clic faible, enchère perdue — cela se note **« non servi »**, jamais « couper ».

---

## 5. L'indicateur de décision, et ceux qui ne décident pas

**Principal : le CPA du concept, en € HT, comparé à la cible par son intervalle de confiance à 95 %.** Pas le ROAS — il dépend du panier, très bruité à faible volume, et de la fenêtre d'attribution. Ni le clic ni le CPM.

Ce CPA est **attribué** : il compare des concepts entre eux dans une vague, il ne mesure aucune incrémentalité ([E09](../modules/E09-mesure-et-incrementalite.md)) — le seul chiffre honnête au niveau de la marque reste le nCAC global. Les secondaires diagnostiquent, ils ne décident pas :

| Indicateur | Cible | Alerte | Ce qu'il désigne |
|---|---:|---:|---|
| Rétention à 3 s | ≥ 25 % | < 20 % | l'accroche |
| Clic parmi les retenus | ≥ 5,00 % | < 4,00 % | le corps, pas l'accroche |
| Taux de clic sortant | ≥ 1,25 % | < 1,00 % | l'ensemble |
| Ajout au panier depuis la publicité | ≥ 6,8 % | < 5,5 % | la rupture publicité → page |

*Cibles reprises de [E04](../modules/E04-psychologie-du-client.md) § 10 — hypothèses du module, pas des canoniques.* Ils se lisent **par paires** : rétention haute et clic bas, l'accroche attire le mauvais public ; rétention basse et clic haut parmi les retenus, l'angle est juste et l'ouverture ratée.

**Une exception écrite d'avance :** un défaut de production (son inaudible, mention obligatoire manquante, mauvais fichier) coupe le concept sur-le-champ. Il retourne au [brief](brief-creatif.md), n'entre pas au registre des morts, ne compte pas au dénominateur.

---

## 6. Les seuils, écrits d'avance

Calculés par `test_significativite.py --creatif`, qui applique la loi de Poisson : couper si la borne basse de l'intervalle dépasse la cible, scaler si la borne haute passe sous 0,80 × cible, conserver si elle passe sous.

| Palier | Tr. | Dépense | Couper si ach. ≤ | Conserver si ach. ≥ | Scaler si ach. ≥ |
|---|---|---:|---:|---:|---:|
| P2 | T1 | 258,71 € HT | 2 | 16 | 18 |
| P3 | T1 | 397,16 € HT | 5 | 20 | 24 |
| P3 | T2 | 1 000,00 € HT | 19 | 42 | 55 |
| P5 | T1 | 907,40 € HT | 13 | 33 | 40 |

Entre les deux : **promu en tranche 2**. Une vague de T1 ne fabrique pas de gagnants, elle élimine des perdants ; lui en demander plus est l'erreur la plus chère du métier.

**Combien de conversions pour que la décision ne soit pas du bruit ?** Pas une réponse, une courbe : plus le concept est proche de la cible, plus il en faut.

| CPA observé ÷ cible | Conversions minimales pour « conserver » |
|---:|---:|
| 0,50 | 12 |
| 0,60 | 19 |
| 0,70 | 36 |
| 0,80 | 87 |
| 0,90 | 365 |

**Conséquence :** un concept qui colle à la cible ne se démontrera jamais. Encore indécis à 30 × CPA cible, on tranche sur l'observé — sous la cible il entre en rotation basse, au-dessus il est coupé. Un créneau occupé par un concept à la cible est un créneau que ne prend pas un concept à 0,70 × la cible.

---

## 7. Produire des variations à partir d'un gagnant

Un gagnant ne se rejoue pas à l'identique : il se décline. **Quatre à six variations**, une seule couche modifiée à la fois.

**Ce qu'on fait varier**, par rendement décroissant : l'accroche (nouvelle formulation, même promesse), l'ordre des preuves, le casting et le décor, la durée et le montage, la fin et l'appel à l'action.

**Ce qu'on ne touche jamais :** l'**angle** et le **mécanisme**. Les modifier ne produit pas une variation mais un concept nouveau, qui repasse par la tranche 1 sans hériter du budget du gagnant. C'est la règle qui empêche la dérive silencieuse : six « variations » plus tard, la marque diffuse un angle qu'elle n'a jamais testé.

**Les variations ne se testent pas contre le gagnant.** Elles entrent en rotation, jugées au même seuil absolu. Démontrer qu'une variation bat un gagnant de 10 % sur un taux de conversion de 2 % demande **161 364 visiteurs et 112 435 € HT** (`--taille --taux 2 --ecart 10`), soit **7,4 semaines** de l'enveloppe de test de P3. Ce test n'aura pas lieu : il sera arrêté trop tôt et interprété quand même.

---

## 8. La convention de nommage

```
NORA _ A07  _ M03       _ UGC    _ 9x16 _ 20s   _ v01     _ FR     _ ST      .mp4
marque angle  mécanisme   format   ratio  durée   version   langue   variante
```

`format` : UGC · STAT · DEMO · COMP · VOIX · RECIT — `version` : v01 = original, v02+ = variation — `variante` : ST = sous-titres incrustés, SANSTXT = master propre.

Campagnes : `TEST_S27_T1`, `TEST_S27_T2`, `SCALE_FR_ROTATION` ; un groupe d'annonces par concept, `S27_A07-M03-UGC`.

Trois règles. Les codes d'angle et de mécanisme viennent d'un **registre**, jamais inventés à la volée : sinon deux personnes nomment le même angle différemment et le registre des morts ne sert à rien. **Le numéro de vague est dans la campagne, pas dans le fichier** : un fichier peut être rejoué ailleurs. **Un nom de fichier ne change jamais après mise en ligne** : un réexport est une version.

---

## 9. Le registre des concepts morts

Une ligne par concept coupé, le jour même.

| Date | Code | Angle | Méca. | Format | Dépense € HT | Achats | CPA | Verdict | Cause probable | Condition de réouverture |
|---|---|---|---|---|---|---|---|---|---|---|

Cause probable, liste fermée : *accroche · mécanisme · preuve · offre · exécution · non servi*. Pourquoi le tenir :

**La machine oublie.** À P5, 57 concepts par semaine font **2 964 par an** ; sans registre, le même angle est retesté chaque trimestre par la personne arrivée depuis. *Hypothèse : 10 % de doublons.* À P3, `38 × 52 × 10 % = 197,6` concepts redoublés par an à 714,76 € HT le concept complet ([brief créatif](brief-creatif.md) § 2.11) = **141 236 € HT par an** pour réapprendre ce qu'on savait.

**Un angle mort et une exécution ratée ne se traitent pas pareil.** Un angle enterré à cause d'une accroche inaudible n'est pas mort : il est non testé. Sans la colonne « cause », les deux cas sont indiscernables six mois plus tard.

**Un mort peut ressusciter, sur condition écrite** — nouveau marché, nouvelle preuve, changement de prix, saison. Elle s'écrit le jour de la coupe, quand on sait encore pourquoi. Rouvrir sans condition écrite est un oubli, pas une reprise.

---

## 10. Le suivi de vague — modèle vierge

```
VAGUE [Sxx] — palier [Pn] — écrit le [date], AVANT le lancement
CPA cible : [xx,xx € HT]        Concepts : [n]        Lancement : [date, heure]
Tranche 1 : [xxx € HT] par concept (12 × cible)     Enveloppe T1 : [x xxx € HT]
Tranche 2 : cumul [x xxx € HT] (30 × cible)         Enveloppe T2 : [x xxx € HT]
Durée : plancher 72 h · plafond 7 j
SEUILS T1 : couper si achats ≤ [n]  ·  conserver si ≥ [n]  ·  scaler si ≥ [n]
SEUILS T2 : couper si achats ≤ [n]  ·  conserver si ≥ [n]  ·  scaler si ≥ [n]
Signature : [qui a écrit ces seuils, et quand]
```

| # | Code concept | Ach. T1 | CPA T1 € HT | Verdict T1 | Ach. T2 | CPA T2 € HT | Verdict final | Cause / suite |
|---|---|---:|---:|---|---:|---:|---|---|
| 1 |  |  |  |  |  |  |  |  |
| … |  |  |  |  |  |  |  |  |

---

## 11. Une vague réelle — S27, palier P3, 12 concepts

> Cas composite, marque fictive. Budgets et CPA cible : [chiffres canoniques](../donnees/chiffres-canoniques.md) § 6 et § 2.4. Verdicts calculés par `test_significativite.py --creatif`.

```
VAGUE S27 — palier P3 — écrit le 30/06, AVANT le lancement
CPA cible : 33,18 € HT          Concepts : 12          Lancement : 01/07, 09 h 00
Tranche 1 : 400 € HT par concept (≈ 12 × cible)     Enveloppe T1 : 4 800 € HT
Tranche 2 : cumul 1 000 € HT (≈ 30 × cible)         Enveloppe T2 : 4 200 € HT
Durée : plancher 72 h · plafond 7 j
SEUILS T1 : couper si achats ≤ 5   ·  conserver si ≥ 20  ·  scaler si ≥ 24
SEUILS T2 : couper si achats ≤ 19  ·  conserver si ≥ 42  ·  scaler si ≥ 55
Signature : Léa, 30/06
```

| # | Code concept | Ach. T1 | CPA T1 € HT | Verdict T1 | Ach. T2 | CPA T2 € HT | Verdict final | Cause / suite |
|---|---|---:|---:|---|---:|---:|---|---|
| 1 | A07-M03-UGC | 21 | 19,05 € | conserver | 56 | 17,86 € | **scaler** | 4 variations en S28 |
| 2 | A07-M03-STAT | 9 | 44,44 € | promu | 14 | 71,43 € | couper | format |
| 3 | A07-M06-COMP | 3 | 133,33 € | **couper** | — | — | couper | mécanisme |
| 4 | A09-M03-UGC | 14 | 28,57 € | promu | 31 | 32,26 € | non tranché | → T2 bis |
| 5 | A09-M07-STAT | 1 | 400,00 € | **couper** | — | — | couper | mécanisme |
| 6 | A11-M03-VOIX | 7 | 57,14 € | promu | 12 | 83,33 € | couper | accroche |
| 7 | A11-M08-UGC | 0 | indéfini | **couper** | — | — | couper | accroche |
| 8 | A12-M03-DEMO | 17 | 23,53 € | promu | 43 | 23,26 € | **conserver** | rotation S28 |
| 9 | A12-M09-UGC | 5 | 80,00 € | **couper** | — | — | couper | preuve |
| 10 | A14-M03-RECIT | 11 | 36,36 € | promu | 18 | 55,56 € | couper | exécution |
| 11 | A14-M10-STAT | 2 | 200,00 € | **couper** | — | — | couper | offre |
| 12 | A15-M11-UGC | 6 | 66,67 € | promu | 16 | 62,50 € | couper | accroche |

**Tranche 2 bis (§ 6).** Le concept 4 est le seul indécis dont le CPA observé passe sous la cible (32,26 € contre 33,18 € HT). Il repart pour 1 000 € HT, une fois : 68 achats cumulés à 2 000 € HT, soit **29,41 € HT**, intervalle 23,20 € – 37,88 € HT. Toujours indécis — on tranche sur l'observé : **conservé en rotation basse**, premier sorti dès qu'un meilleur arrive.

**Le bilan.**

```
Dépense totale   = 4 800 + 4 200 + 1 000      = 10 000 € HT
Achats totaux    =                                   238
CPA de la vague  = 10 000 ÷ 238               =  42,02 € HT
Gagnants : 2 sur 12                           =  16,7 %
Taux attendu à P3 (canoniques § 6)            =  11,1 %
```

Deux gagnants au lieu des 1,3 attendus : **cette vague a eu de la chance, et il faut le dire.** Sur douze concepts, l'écart entre 1 et 2 gagnants n'est pas un signal de qualité créative, c'est du tirage. Le taux de réussite se lit sur un trimestre — 494 concepts à P3 —, pas sur une vague.

Deux lignes de registre valent le détour : l'angle **A14** est coupé deux fois, pour « exécution » (n° 10) et pour « offre » (n° 11). Aucune des deux causes ne condamne l'angle lui-même — sans la colonne « cause », il serait enterré par erreur.

---

## 12. Les erreurs qu'on voit tout le temps

**Couper à 40 € HT de dépense.** À 33,18 € HT de cible, 40 € HT c'est 1,21 achat attendu : un concept qui tient la cible a **29,9 %** de chances de n'en montrer aucun. Couper là élimine au hasard trois bons concepts sur dix. Le plancher de 122,40 € HT n'est pas négociable : ce n'est pas une opinion, c'est la loi de Poisson.

**Écrire les seuils après avoir vu les résultats.** La faute qui annule tout le reste : un seuil décidé devant le tableau de bord épouse la forme du résultat espéré. La signature datée est la seule preuve qu'il est antérieur.

**Confondre « non servi » et « perdant ».** Un concept qui n'a pas dépensé sa tranche n'a pas été testé : le coder « couper » laisse l'enchère décider de ta grille créative (§ 4).

**Ne pas tenir le registre des morts.** 141 236 € HT par an à P3 pour réapprendre ce qu'on savait (§ 9) — et, plus grave, l'impossibilité de distinguer un angle mort d'une exécution ratée, qui enterre des angles encore exploitables.

*Modèle rattaché à E05. Amont : [brief créatif](brief-creatif.md).*
