# Niveau L05 — Constructeur

> **Prérequis :** niveau L04 validé.
>
> **Ce que tu sais faire à la sortie :**
> 1. Tu juges un lot de concepts avec un intervalle de confiance et non avec une impression, et tu dis pour chacun combien d'euros il faudrait encore dépenser pour trancher.
> 2. Tu tiens une cadence de production créative chiffrée pour ton palier, et tu démontres ce que sa suppression coûte, avec le délai auquel la facture arrive.
> 3. Tu lis un tableau de cohortes dans ses trois directions, tu chiffres une dégradation en euros de contribution annuelle, et tu nommes le test qui distingue ses causes.
>
> **Temps de travail typique :** 25 à 35 heures — le niveau le plus long avant L09, parce que ses deux compétences (juger un concept, lire une cohorte) sont des automatismes et non des connaissances.

> **Lxx mesure ta compétence. Nx mesure l'état de ton business.** Les deux sont indépendantes. Un directeur créatif peut être L05 sans posséder de marque. Et une marque **N3** peut être pilotée par une compétence L04 : elle alloue correctement un budget, elle ne sait pas fabriquer ce qui le rend rentable. Ce cas ne se voit pas tout de suite — le stock de concepts gagnants met quatre à six mois à s'éteindre, et pendant ce temps les chiffres sont bons alors que la décision qui tue la marque a déjà été prise. Garde ton L au-dessus de ton N ([diagnostic](../mentorat/diagnostic.md)).

---

## 1. Les compétences du niveau

1. **Je calcule l'intervalle de confiance du CPA d'un concept** à partir de sa dépense et de ses achats, et je ne juge jamais sur le CPA observé seul.
2. **Je connais la règle des trois CPA** : sous ~3,7 fois le CPA cible de dépense, zéro achat ne démontre rien, et couper là-dessus élimine au hasard des concepts qui allaient gagner.
3. **Je distingue « à couper », « à conserver », « à scaler » et « trop tôt »** avec quatre critères écrits, et j'emploie le quatrième autant que les trois autres.
4. **Je chiffre le budget qui manque à un concept pour être jugeable**, et je décide de ne pas le dépenser quand le concept colle à la cible.
5. **Je dimensionne une cadence de production** en concepts nouveaux par semaine à partir du budget média de mon palier.
6. **Je construis un tableau de cohortes** avec le bon dénominateur et la bonne valeur de cellule, et je le lis dans ses trois directions — ligne, colonne, diagonale — en faisant le tri période/cohorte en premier.
8. **Je propage une dégradation jusqu'à l'euro de contribution annuelle**, par deux méthodes indépendantes qui doivent converger.
9. **Je nomme la cause d'une dégradation de rétention par la signature du nCAC**, et j'écris le test qui distingue les trois causes.

---

## 2. Ce que tu lis

| # | Lecture | Ce qu'elle apporte **à ce niveau** |
|---|---|---|
| 1 | [**E05 — La machine créative**](../modules/E05-machine-creative.md) § 1 à § 3 | L'anatomie d'un concept, et la démonstration que la performance créative est une distribution à queue épaisse : la moyenne n'y décrit aucun concept réel. |
| 2 | [**E05**](../modules/E05-machine-creative.md) § 4 et § 5 | Le jugement : seuils de décision, coût d'une coupe prématurée, coût d'un scale prématuré. **Le cœur de la partie (a).** |
| 3 | [**E05**](../modules/E05-machine-creative.md) § 6 et § 7 | L'industrialisation et la fatigue créative. [Canoniques § 6](../donnees/chiffres-canoniques.md) : 14 concepts nouveaux/semaine à P2, 38 à P3, 57 à P5. |
| 4 | [**C03 — Anatomie d'un concept gagnant**](../etudes-de-cas/C03-anatomie-creative-gagnante.md) | Un gagnant décomposé : ce qui le sépare d'un concept correct n'est pas 20 % mais un facteur. |
| 5 | [**E08 — La rétention et la LTV**](../modules/E08-retention-et-ltv.md) § 1 à § 4 | La cohorte définie, les trois directions de lecture, le signal d'alarme n° 1 et ses trois causes ; puis la courbe de réachat canonique, le payback, et pourquoi le premier réachat porte presque toute la valeur. **Le cœur de la partie (b).** |

---

## 3. Ce que tu fais

| Travail | Livrable | Comment on sait que c'est fait |
|---|---|---|
| [**S10 — Installer la rétention**](../atelier/S10-installer-la-retention.md) | Sept flux rédigés et ton **premier tableau de cohortes** | Dénominateur = clients **acquis**, figé. Cellules = réachats cumulés par client, pas du CA |
| [**S11**](../atelier/S11-passer-a-l-echelle.md), première moitié | Le volet créatif du plan 30 k€ → 300 k€ : cadence, coût par concept, effectif | Le nombre de concepts par semaine est dérivé du budget, pas choisi |
| **`test_significativite.py`** et **`cohortes.py`** | Tes douze derniers concepts passés à l'outil avec ton verdict écrit **avant** ; ton tableau de cohortes et son alerte | L'écart entre tes verdicts et ceux de l'outil est ton programme de travail |
| **Simulateur : `sans_test_crea` contre `equilibree`** | Les deux parties, même graine, un seul paramètre d'écart | Tu nommes le mois où la courbe se retourne et tu comptes les mois depuis la décision qui l'a causée |

> **Pourquoi cette comparaison est le travail le plus important du niveau.** `sans_test_crea` est identique à `equilibree` sauf sur `part_test_crea = 0`, et termine à **−92,5 %** de CA cumulé sur la graine 7. Ce qu'il faut voir n'est pas le total : c'est que **rien ne se passe pendant quatre à six mois**. Le délai entre la cause et l'effet est exactement celui qui rend la cause invisible quand l'effet arrive.

---

## 4. L'épreuve

**Durée : 3 h 30**, deux parties indépendantes. Calculatrice autorisée, table de Poisson fournie. **Barème sur 100 — partie (a) sur 55, partie (b) sur 45. Passage à 72.**

### Le dossier — VÉLINE

> *Marque fictive, chiffres modélisés sur des ordres de grandeur sectoriels : ce ne sont les comptes d'aucune entreprise réelle.*

VÉLINE vend du soin du visage en direct, en France et en Belgique, au palier **P3** ([canoniques § 2](../donnees/chiffres-canoniques.md)).

| L'économie de la marque | |
|---|---:|
| Panier moyen d'une **première** commande | 60,00 € TTC — 50,00 € HT |
| Panier moyen d'un **réachat** | 80,00 € TTC — 66,67 € HT |
| Taux de marge brute CM2 | 60,3 % *(valeur canonique de P3)* |
| Contribution de la première commande | 50,00 × 60,3 % = **30,15 € HT** |
| Contribution d'un réachat | 66,67 × 60,3 % = **40,20 € HT** |
| Réachats cumulés à 12 mois, cohorte de référence | **1,24** *(courbe canonique § 3)* |
| **LTV 12 mois en contribution** | 30,15 + 1,24 × 40,20 = **80,00 € HT** |
| Frais fixes mensuels | 52 000 € HT, soit 15,0 % du CA HT — au-dessus du profil canonique de P3 (10,7 %) : VÉLINE a recruté en avance |

---

## Partie (a) — Juger douze concepts (55 points)

**Le contexte.** Le lot 14 : douze concepts nouveaux, lancés le même jour dans une campagne de test à budget partagé et relevés à quatorze jours. Il a consommé **14 400 € HT** sur les ~30 000 € HT de test de la quinzaine ([canoniques § 6](../donnees/chiffres-canoniques.md) : 15 092 € HT par semaine à P3). Les dépenses sont très inégales **parce que le budget est partagé** : l'algorithme réalloue vers ce qui convertit tôt. C'est ce comportement normal qui fabrique le piège — un concept qui a démarré lentement n'a jamais reçu assez de budget pour être jugeable, et son silence n'est pas une information.

**Le CPA cible : 33,18 € HT**, le nCAC canonique de P3 — un concept qui ne l'atteint pas dégrade le CAC du compte au lieu de l'améliorer.

### Le lot 14

| Concept | Dépense HT | Achats | CPA observé HT |
|---|---:|---:|---:|
| **K01** Miroir de la salle de bain | 1 240 € | 62 | 20,00 € |
| **K02** La minute de 6 h 40 | 740 € | 40 | 18,50 € |
| **K03** Témoignage esthéticienne | 1 850 € | 78 | 23,72 € |
| **K04** Démonstration du test d'eau | 980 € | 42 | 23,33 € |
| **K05** Avant / après 14 jours | 5 100 € | 170 | 30,00 € |
| **K06** Comparatif tube de pharmacie | 1 180 € | 22 | 53,64 € |
| **K07** Voix off spécialiste | 2 450 € | 40 | 61,25 € |
| **K08** Animation 3D du mécanisme | 150 € | 0 | — |
| **K09** Gros plan texture | 68 € | 4 | 17,00 € |
| **K10** Déballage du coffret | 132 € | 6 | 22,00 € |
| **K11** Statique fond blanc | 90 € | 0 | — |
| **K12** Interview cliente longue | 420 € | 12 | 35,00 € |
| **Total** | **14 400 €** | **476** | **30,25 €** |

### La table de Poisson (intervalle à 95 %, sur le nombre d'achats)

| Achats observés | Borne basse de λ | Borne haute de λ |
|---:|---:|---:|
| 0 | 0,00 | 3,69 |
| 4 | 1,09 | 10,24 |
| 6 | 2,20 | 13,06 |
| 12 | 6,20 | 20,96 |
| 22 | 13,79 | 33,31 |
| 40 | 28,58 | 54,47 |
| 42 | 30,27 | 56,77 |
| 62 | 47,54 | 79,48 |
| 78 | 61,66 | 97,35 |
| 170 | 145,41 | 197,56 |

```
Le CPA est dépense ÷ achats. La dépense est connue exactement ; c'est le nombre
d'achats qui est incertain. Plus d'achats donne un CPA plus bas, donc :

    borne BASSE du CPA  = dépense ÷ borne HAUTE de λ
    borne HAUTE du CPA  = dépense ÷ borne BASSE de λ
```

### Les quatre règles de décision, écrites avant le test

```
1. À COUPER     si borne BASSE du CPA  >  CPA cible
                (même l'hypothèse la plus favorable reste au-dessus)
2. À SCALER     si borne HAUTE du CPA  <  0,80 × CPA cible = 26,54 € HT
                (démontré NETTEMENT sous la cible, pas frôlant par le haut)
3. À CONSERVER  si borne HAUTE du CPA  <  CPA cible
4. Si l'intervalle enjambe la cible mais que sa largeur rapportée à la cible
   est ≤ 30 %, dépenser plus ne changera plus la décision : on tranche sur le
   CPA observé — À CONSERVER s'il est sous la cible, À COUPER sinon.
5. Sinon : TROP TÔT POUR JUGER.
```

### Les questions de la partie (a)

**A1 — Le classement. (36 points, 3 par concept)** Pour chacun des douze : bornes basse et haute du CPA, puis verdict. Un verdict sans les bornes vaut 1 sur 3.

**A2 — Les deux pièges. (8 points)** Deux concepts affichent un CPA que n'importe quelle régie ferait scaler et qui ne démontre rien. Nomme-les, et dis en deux lignes ce qui les rend piégeux.

**A3 — Le zéro achat qu'on ne coupe pas. (5 points)** Deux concepts n'ont produit aucun achat ; l'un se coupe, l'autre non. Dis lequel, et à partir de quelle dépense totale tu aurais le droit de le couper.

**A4 — Lundi matin. (6 points)** Trois décisions chiffrées sur le budget de test de la semaine suivante, dont au moins une qui **arrête** un concept classé « trop tôt », justifiée en euros.

---

## Partie (b) — Diagnostiquer neuf mois de cohortes (45 points)

**Réachats cumulés par client**, cohortes M01 à M09, relevées à la fin du mois M09. Une cellule vide signifie que le mois n'est pas encore écoulé pour cette cohorte.

| Cohorte | Clients acquis | nCAC HT | Part acquise en promotion | M+1 | M+2 | M+3 | M+4 | M+5 | M+6 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| M01 | 2 400 | 33,90 € | 11 % | 0,06 | 0,20 | 0,34 | 0,47 | 0,59 | 0,72 |
| M02 | 2 610 | 34,20 € | 11 % | 0,06 | 0,20 | 0,34 | 0,46 | 0,58 | 0,71 |
| M03 | 2 880 | 34,50 € | 11 % | 0,06 | 0,19 | 0,33 | 0,46 | 0,58 | 0,70 |
| M04 | 3 150 | 34,80 € | 11 % | 0,06 | 0,19 | 0,33 | 0,45 | 0,57 | — |
| M05 | 3 420 | 33,60 € | 12 % | 0,05 | 0,17 | 0,29 | 0,40 | — | — |
| M06 | 3 900 | 32,40 € | 12 % | 0,04 | 0,15 | 0,26 | — | — | — |
| M07 | 4 260 | 31,20 € | 12 % | 0,04 | 0,14 | — | — | — | — |
| M08 | 4 620 | 30,50 € | 12 % | 0,04 | — | — | — | — | — |
| M09 | 4 980 | 30,10 € | 12 % | — | — | — | — | — | — |

*M01 et M02 ont aussi M+7 et M+8 ; le tableau s'arrête à M+6 pour que les colonnes restent comparables.*

**Le compte de résultat du mois M09**

```
Nouveaux clients                                4 980
Dépense publicitaire      4 980 × 30,10 €  =  149 898 € HT
CA TTC des premières cmd  4 980 × 60,00 €  =  298 800 € TTC
Part du CA en réachat                          28,0 %
CA TTC total              298 800 ÷ 0,72   =  415 000 € TTC
CA HT                     415 000 ÷ 1,20   =  345 833 € HT
Marge brute CM2           345 833 × 60,3 % =  208 538 € HT
CM3                       208 538 − 149 898 =  58 640 € HT
EBITDA                    58 640 − 52 000  =    6 640 € HT   →  1,92 % du CA HT
```

*Hypothèse déclarée, utile à B5 :* une cohorte acquise en promotion réachète jusqu'à **42 %** moins souvent qu'une cohorte au prix plein ([simulateur](../outils/README-simulateur.md) § 8).

### Les questions de la partie (b)

**B1 — La direction de lecture. (8 points)** Dans quelle direction lis-tu ce tableau ? Nomme la colonne retenue et dis pourquoi tu écartes les deux autres directions et les deux premières colonnes.

**B2 — L'ampleur, en points de rétention. (12 points)** (a) Sur la colonne retenue. (b) Propagée aux réachats à 12 mois et à la LTV. (c) Le LTV/CAC de la cohorte la plus récente et de celle de référence.

**B3 — L'ampleur, en euros. (8 points)** (a) Sur les cohortes déjà acquises. (b) En régime annuel si rien ne change, face à l'EBITDA annualisé de M09.

**B4 — Les trois causes et leurs tests. (12 points)** Pour chacune : sa signature sur le nCAC, le test qui la distingue des deux autres, et ce qu'il doit montrer.

**B5 — Le quatrième suspect. (5 points)** Nomme-le, écarte-le par un calcul.

---

## 5. Le corrigé

### Question A1 — Le classement

| Concept (€ HT) | Dépense | Achats | CPA obs. | bas | haut | Largeur ÷ cible | **Verdict** |
|---|---:|---:|---:|---:|---:|---:|---|
| K01 | 1 240 € | 62 | 20,00 € | 15,60 € | 26,08 € | 0,32 | **à scaler** |
| K02 | 740 € | 40 | 18,50 € | 13,59 € | 25,89 € | 0,37 | **à scaler** |
| K03 | 1 850 € | 78 | 23,72 € | 19,00 € | 30,00 € | 0,33 | **à conserver** |
| K04 | 980 € | 42 | 23,33 € | 17,26 € | 32,38 € | 0,46 | **à conserver** |
| K05 | 5 100 € | 170 | 30,00 € | 25,81 € | 35,07 € | 0,28 | **à conserver** *(règle 4)* |
| K06 | 1 180 € | 22 | 53,64 € | 35,42 € | 85,57 € | 1,51 | **à couper** |
| K07 | 2 450 € | 40 | 61,25 € | 44,98 € | 85,72 € | 1,23 | **à couper** |
| K08 | 150 € | 0 | — | 40,65 € | ∞ | ∞ | **à couper** |
| K09 | 68 € | 4 | 17,00 € | 6,64 € | 62,39 € | 1,68 | **trop tôt** |
| K10 | 132 € | 6 | 22,00 € | 10,11 € | 60,00 € | 1,50 | **trop tôt** |
| K11 | 90 € | 0 | — | 24,39 € | ∞ | ∞ | **trop tôt** |
| K12 | 420 € | 12 | 35,00 € | 20,04 € | 67,74 € | 1,44 | **trop tôt** |

```
K01 : bas = 1 240 ÷ 79,48 = 15,60 €   haut = 1 240 ÷ 47,54 = 26,08 €
      26,08 < 26,54 (= 0,80 × 33,18)                →  À SCALER
K04 : bas =   980 ÷ 56,77 = 17,26 €   haut =   980 ÷ 30,27 = 32,38 €
      32,38 < 33,18 mais > 26,54                    →  À CONSERVER, pas à scaler
K05 : haut = 5 100 ÷ 145,41 = 35,07 €, au-dessus de la cible ; mais la largeur
      (35,07 − 25,81) ÷ 33,18 = 0,28 ≤ 0,30 et le CPA observé est sous la cible
                                                     →  À CONSERVER, règle 4
K08 : 0 achat, bas = 150 ÷ 3,69 = 40,65 € > 33,18    →  À COUPER
K11 : 0 achat, bas =  90 ÷ 3,69 = 24,39 € < 33,18    →  TROP TÔT
```

**Les trois lectures qui séparent un L05 d'un L04.** **K04 a le troisième meilleur CPA du lot et ne se scale pas** : 23,33 € contre 33,18 €, mais sa borne haute de 32,38 € ne franchit pas la marge de 26,54 €. **K05 est le mieux mesuré et le moins spectaculaire** : 170 achats, intervalle large de 9,26 €, borne haute au-dessus de la cible, conservé quand même parce que dépenser plus ne changera plus la décision. **K07 a le même nombre d'achats que K02 et le verdict opposé** : 40 achats des deux côtés, 740 € d'un côté, 2 450 € de l'autre — les achats donnent la **précision**, la dépense le **niveau**.

**Barème.** 3 par ligne : 1 par borne, 1 pour le verdict. Verdict correct sans bornes : 1 sur 3. Un intervalle à l'envers — division par la mauvaise extrémité de λ — coûte les 3 points de la ligne.

---

### Question A2 — Les deux pièges : K09 et K10

**K09** affiche **17,00 €** de CPA, le meilleur du lot entier, sur **4 achats** et 68 € de dépense. **K10** affiche **22,00 €**, le troisième meilleur, sur **6 achats** et 132 €.

Ce qui les rend piégeux : leur intervalle va de 6,64 € à 62,39 € pour K09, de 10,11 € à 60,00 € pour K10 — chacun compatible avec « le meilleur concept jamais produit » **et** avec « à couper ». Le CPA affiché n'est pas une mesure, c'est un artefact de division par un très petit nombre.

Et la cause est structurelle : le budget étant partagé, ces deux concepts n'ont jamais reçu d'argent **parce que** l'algorithme réalloue tôt — pendant que le tableau de bord de la régie les classe premiers du lot.

```
K09 : il faut porter la dépense à 204 € HT pour que le verdict devienne net, soit 136 € de plus.
K10 : il faut la porter à 616 € HT, soit 484 € de plus.
```

**Barème.** 2 par concept nommé. 4 pour l'explication, qui doit contenir la **largeur de l'intervalle** et non « il n'y a pas assez de données ». Nommer K11 ou K12 à la place : 0 sur le concept concerné.

---

### Question A3 — Le zéro achat qu'on ne coupe pas : K11

Un concept qui tient **exactement** la cible produit en moyenne `dépense ÷ 33,18` achats. Tant que ce nombre reste petit, ne rien observer reste compatible avec un bon concept.

```
Nombre d'achats attendu de K11 à la cible = 90 ÷ 33,18 = 2,71
Probabilité d'observer 0 achat sous cette espérance = e^(−2,71) = 6,6 %

Un concept parfaitement à la cible a donc 6,6 % de chances de montrer
zéro achat à ce stade. Couper là-dessus élimine au hasard 6,6 % des
concepts qui allaient tenir la cible.
```

Le seuil au-delà duquel zéro achat devient une information est celui où la borne basse du CPA dépasse la cible :

```
Dépense minimale de jugement = 3,69 × 33,18 € = 122,43 € HT
```

C'est la **règle des trois CPA** : sous ~3,7 fois le CPA cible de dépense, l'absence d'achat n'est pas exploitable. K11 est à 90 €, il lui manque **32,43 € HT** ; K08, à 150 €, a franchi le seuil. D'où le verdict opposé pour deux concepts qui affichent la même chose.

**Barème.** 2 pour K11 ; 3 pour le calcul (1 la formule `3,69 × cible`, 1 les 122,43 €, 1 l'écart de 32,43 €). La probabilité de 6,6 % donnée en plus vaut les 3 points même si le seuil est arrondi.

---

### Question A4 — Lundi matin

| Décision | Concepts | Montant (€ HT) | Justification |
|---|---|---:|---|
| **Arrêter** | K06, K07, K08 | 0 € | Démontrés au-dessus de la cible. Les 2 450 € de K07 sont le coût normal d'un verdict propre |
| **Sortir en campagne principale** | K01, K02 | +30 % au maximum | Démontrés sous 26,54 €. La borne protège l'apprentissage ([E06](../modules/E06-acquisition-payante.md) § 6) |
| **Maintenir en test** | K03, K04, K05 | inchangé | K04 a besoin de volume pour franchir 26,54 € ; K05 n'a plus rien à apprendre mais tient la cible |
| **Financer le verdict** | K09, K10, K11 | 136 + 484 + 33 = **653 € HT** | Trois verdicts nets pour 4,5 % du budget du lot |
| **Arrêter malgré « trop tôt »** | **K12** | **économie de 6 580 € HT** | Son CPA de 35,00 € colle à la cible : trancher demanderait 7 000 € HT au total, soit **23 % du budget de test de la quinzaine**, pour un concept qui au mieux égalera le compte |

**La cinquième ligne est celle que la question mesure.** « Trop tôt pour juger » n'est pas un ordre de continuer à payer : un concept dont l'intervalle enjambe la cible en son milieu ne tranchera qu'à un coût sans rapport avec ce qu'il rapporte. Les 6 580 € vont à onze concepts neufs.

**Barème.** 2 par décision chiffrée et justifiée, plafonné à 6. La décision sur K12 est obligatoire : sans elle, 3 au maximum.

---

### Question B1 — La direction de lecture

**On lit en colonne** : une colonne compare des cohortes **au même âge**, la seule comparaison qui isole la qualité des clients acquis de la forme de la courbe d'acquisition.

**On écarte la ligne** : elle décrit la maturation d'une cohorte et ne compare rien — toutes les lignes montent, y compris celles des cohortes qui s'effondrent.

**On écarte la diagonale, après l'avoir regardée.** Les cellules atteintes le même mois calendaire en forment une : un incident de période — rupture de stock, bug de paiement — fait décrocher une diagonale entière d'un coup, et les colonnes se rétablissent le mois suivant. Ce tri se fait **en premier**. Ici, les deux dernières diagonales portent le même profil : ce n'est pas un effet de période.

**La colonne retenue : M+3.** On écarte M+1 et M+2 par résolution : les cellules sont arrondies au centième, et à M+1 l'écart de 0,06 à 0,04 vaut −33,3 % dont **un centième relève de l'arrondi**. À M+3, l'écart de 0,34 à 0,26 se lit sur huit centièmes — et c'est la première colonne assez remplie pour montrer une pente.

**Barème.** 3 pour « en colonne », 2 pour l'écartement de la ligne, 2 pour la diagonale à condition de dire qu'on la regarde **d'abord** et ce qu'elle aurait montré, 1 pour M+3 justifié par la résolution.

---

### Question B2 — L'ampleur en points de rétention

**(a) Sur la colonne M+3**

| Cohorte | M01 | M02 | M03 | M04 | M05 | M06 |
|---|---:|---:|---:|---:|---:|---:|
| Réachats/client à M+3 | 0,34 | 0,34 | 0,33 | 0,33 | 0,29 | 0,26 |

```
M06 contre M01 : 0,26 ÷ 0,34 − 1 = −23,5 %
M06 contre M04 : 0,26 ÷ 0,33 − 1 = −21,2 %
```

Ce n'est pas du bruit : six cohortes consécutives, aucune au-dessus de la précédente, et la rupture est **datée** entre M04 (0,33) et M05 (0,29). Contrôle sur M+2 : 0,20 → 0,14 de M01 à M07, soit −30,0 %.

**(b) Propagée à 12 mois.** Hypothèse la plus prudente : la dégradation reste constante et ne s'aggrave pas au-delà de M+3.

```
Réachats à 12 mois     = 1,24 × (1 − 0,235)          = 0,9486
LTV en contribution    = 30,15 € + 0,9486 × 40,20 €  = 68,28 € HT
Perte de LTV           = 80,00 − 68,28               = 11,72 € par client, −14,7 %
```

**(c) Le ratio LTV/CAC — le piège de la question**

```
Cohorte de référence M01 : 80,00 ÷ 33,90 = 2,36
Cohorte dégradée M09     : 68,28 ÷ 30,10 = 2,27
```

**Le ratio n'a perdu que 3,8 % pendant que la rétention en perdait 23,5 %**, et il reste **au-dessus de 2,0** — la zone où la règle canonique dit « accélère » ([canoniques § 3](../donnees/chiffres-canoniques.md)). La raison : le nCAC a baissé de 33,90 € à 30,10 €, soit −11,2 %, et compense presque exactement la perte de LTV.

> **À retenir :** un ratio LTV/CAC stable ne prouve pas que rien ne bouge — il peut couvrir une dégradation de rétention par une amélioration de coût d'acquisition. Et [E08](../modules/E08-retention-et-ltv.md) § 2.2 démontre que ces deux mouvements simultanés ne sont pas une coïncidence mais **une signature**.

**Barème.** (a) 2 pour le −23,5 %, 2 pour la datation entre M04 et M05. (b) 4, calcul déroulé. (c) 2 pour les deux ratios, 2 pour l'explication de leur quasi-stabilité. Répondre « le ratio reste bon, tout va bien » : 0 sur la question entière.

---

### Question B3 — L'ampleur en euros

**(a) Sur les cohortes déjà acquises**

```
M05     (−14,7 % à M+3, 3 420 clients)  3 420 × 1,24 × 0,147 × 40,20 € =  25 061 €
M06–M09 (−23,5 %,     17 760 clients) 17 760 × 1,24 × 0,235 × 40,20 € = 208 046 €
                                                                 Total = 233 107 €
```

**(b) En régime annuel**, l'acquisition se maintenant autour de 5 000 clients par mois :

```
Clients sur douze mois = 60 000 ; réachats perdus 60 000 × 1,24 × 0,235 = 17 484
Contribution perdue    = 17 484 × 40,20 €                     = 702 857 € / an
```

**La comparaison qui décide.**
```
EBITDA du mois M09           =   6 640 € HT     annualisé  =  79 674 € HT
Contribution annuelle perdue = 702 857 € HT     →  8,8 fois l'EBITDA annuel
```

Et le compte de résultat de M09 **ne montre rien** : la marque est bénéficiaire, son MER vaut `415 000 ÷ 149 898 = 2,77`, au-dessus de son seuil EBITDA de `1,20 ÷ (0,603 − 0,150) = 2,65`. Les réachats manquants sont **futurs** : ils n'apparaîtront que dans six à douze mois, quand la cause aura disparu du champ de vision.

> **C'est la raison d'être du tableau de cohortes :** le seul instrument du tableau de bord qui soit en avance sur le compte de résultat.

**Barème.** (a) 3, avec le traitement séparé de M05. (b) 3. (c) 2 pour la comparaison à l'EBITDA annualisé — 0 si le candidat compare 702 857 € à un EBITDA mensuel.

---

### Question B4 — Les trois causes et leurs tests

| | **Saturation de l'audience** | **Dérive du produit** | **Dérive de la promesse** |
|---|---|---|---|
| **Mécanisme et forme** | Les acheteurs faciles sont épuisés ; l'algorithme s'éloigne du cœur. Chute lente, régulière, corrélée au budget | Formule, fournisseur ou lot ont changé. Chute brutale et **datée** : toutes cohortes après une date, tous canaux | La créa promet plus que le produit ne tient, pour tenir le CPA. Chute progressive, limitée aux cohortes des nouveaux concepts |
| **Signature nCAC** | **Il monte** | Stable | **Il baisse** — la sur-promesse convertit mieux |
| **Le test** | Cohorter par **canal** | Croiser la date de bascule avec les **lots** et les fournisseurs ; retours et SAV sur la même fenêtre | Cohorter par **concept créatif** ; verbatims SAV : « ce n'est pas ce qui était montré » |
| **Ce qu'il doit montrer** | Un écart de rétention entre canaux, le plus large étant le plus dégradé | Une bascule à moins de deux semaines d'un changement de lot, **et** une hausse des retours | Une rétention qui décroche seulement sur les cohortes des concepts postérieurs à M04 |

**Ce que le dossier dit déjà.** Le nCAC passe de 34,80 € (M04) à 30,10 € (M09), soit **−13,5 %**, dans la fenêtre exacte où la rétention décroche. **Un nCAC qui baisse pendant que la rétention baisse est une signature unique** : la saturation ferait monter le CAC, la dérive produit le laisserait tranquille. Suspect n° 1, la **dérive de la promesse** — la plus coûteuse, parce qu'elle se déguise en performance.

**Barème.** 4 par cause : 1 la nommer, 1 la signature nCAC, 1 le test, 1 ce qu'il doit montrer. Aucun point pour désigner le suspect n° 1, mais **−4** si le candidat désigne la saturation alors que le nCAC baisse : c'est la faute que la question existe pour attraper.

---

### Question B5 — Le quatrième suspect : le mix promotionnel

Une cohorte acquise en promotion est pleine de chasseurs de remise. La part promotionnelle passe de 11 % à 12 % entre M04 et M05, au moment exact de la rupture : il faut donc l'écarter, par un calcul et non par une opinion.

```
Hausse du mix promotionnel                              = +1 point
Sous-réachat d'une cohorte promotionnelle (hypothèse)   = −42 %
Effet sur le réachat moyen de la cohorte  1 % × 42 %    = −0,42 %

À expliquer : −23,5 %.   Le mix promotionnel en explique 1,8 %.
```

Un point de mix promotionnel ne peut pas produire 23,5 % de dégradation : il faudrait que la part promotionnelle ait bondi d'environ **56 points**. Le suspect est écarté.

**Barème.** 2 pour le nommer, 3 pour le calcul (1 le +1 point de mix, 1 le produit par 42 %, 1 la comparaison au −23,5 %). Écarter le suspect sans calcul : 2 sur 5.

---

## 6. Le critère de passage

**Note minimale : 72 / 100**, dont **au moins 30 / 55 en partie (a) et 24 / 45 en partie (b)** : les deux parties ne se compensent pas, et une marque pilotée par quelqu'un qui n'en maîtrise qu'une meurt de l'autre.

**Quatre fautes éliminatoires :**

1. **Scaler K09 ou K10** — prendre une division par 4 pour une mesure. Toute la partie (a) existe pour éliminer cette faute.
2. **Couper K11.** L'erreur symétrique, et la plus grave : appliquée à chaque lot, elle élimine au hasard une part fixe des bons concepts et plafonne la qualité créative du compte pour toujours, sans laisser de trace.
3. **Une LTV exprimée en chiffre d'affaires.** Celle de VÉLINE vaut 80,00 € HT en contribution ; en CA cumulé elle vaudrait plus du double, et tout ratio bâti dessus est faux dans le sens qui rassure.
4. **Lire le tableau en ligne** pour conclure que « la rétention progresse » : toutes les lignes montent, y compris celles des cohortes qui s'effondrent.

**Deux fautes lourdes :** désigner la saturation alors que le nCAC baisse (−4, question B4) ; comparer la perte annuelle à un EBITDA mensuel (−4, question B3).

**En cas d'échec**, tu repasses sur un autre lot et une autre matrice — avec, cette fois, une dégradation qui peut aussi bien être un effet de période. Le tri diagonale/colonne devient la question qui décide.

---

## 7. Les pièges de ce niveau

**1. Croire qu'on juge un concept sur son CPA.** On le juge sur son **intervalle** : quand le dénominateur vaut 4, une division n'est pas une mesure. Le test honnête — reprends les douze derniers concepts que tu as coupés et compte combien avaient moins de 122 € de dépense. La réponse explique pourquoi ton compte n'a jamais eu plus de deux gagnants à la fois.

**2. Croire que « trop tôt pour juger » veut dire « continue ».** C'est un état, pas une instruction : on finance le verdict quand il coûte quelques centaines d'euros, on arrête quand il en coûte des milliers.

**3. Croire qu'un bon ratio LTV/CAC signifie que la rétention va bien, et qu'un CAC qui baisse est une bonne nouvelle.** La question B2 (c) est construite là-dessus : 23,5 % de rétention en moins, un ratio qui n'en perd que 3,8 %, parce que le CAC a baissé en même temps. **Regarde toujours le numérateur et le dénominateur avant le quotient.** Un CAC qui baisse pendant que la rétention baisse a une explication ordinaire : une promesse qui a grossi. Tu n'as pas trouvé un meilleur angle, tu as trouvé un mensonge rentable à court terme, payable sur douze mois de réachat.

**4. Le mauvais dénominateur.** Rapporter les réachats aux clients « encore actifs » fabrique de la rétention à partir de rien : plus tes clients partent, meilleure ta courbe paraît.

**5. Croire que L05 mesure ta marque.** C'est ici que l'écart entre les deux échelles est le plus retors, parce que la dégradation qu'on apprend à lire **améliore les indicateurs de court terme**. Une marque **N3** dont le CAC s'améliore, dont le MER monte et dont le LTV/CAC reste au-dessus de 2 est félicitée par tout le monde — pendant qu'elle détruit huit fois son EBITDA annuel en contribution future. Personne n'y verra une erreur : on y verra un bon trimestre.

---

*Fin du niveau L05. Suite : [L06 — Gestionnaire](L06-gestionnaire.md) — une marque ne meurt presque jamais de ne pas être rentable, mais de manquer de cash le mois où elle allait le devenir.*
