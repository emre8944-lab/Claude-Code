# Corrigé — Module E12 : La marque comme actif

> Ne lis ce fichier qu'après avoir rendu [`E12-rendu.md`](E12-rendu.md). Un corrigé
> lu avant l'effort donne le sentiment d'avoir compris, et rien d'autre.
>
> Conventions : TVA 20 %, marge brute de P5 à **61,45 %** (valeur exacte des
> [chiffres canoniques](../donnees/chiffres-canoniques.md) § 2.1 ; le module arrondit
> à 61,5 % et affiche donc des EBITDA supérieurs d'environ 900 €). Effectifs arrondis
> à l'unité avant multiplication par un prix.

---

## Exercice 1 — Le test de coupure de NØRA, avec d'autres hypothèses de survie

### La réponse

**(1) Les deux paniers moyens, redérivés.**

```
CA de réachat      = 4 333 196 × 44,9 %        = 1 945 605 € TTC
CA de 1ʳᵉ commande = 4 333 196 − 1 945 605     = 2 387 591 € TTC
Cmd. de réachat    = 60 200 − 37 324           =      22 876
AOV 1ʳᵉ commande   = 2 387 591 ÷ 37 324        =      63,97 € TTC
AOV réachat        = 1 945 605 ÷ 22 876        =      85,05 € TTC

Contrôle : 63,97 ÷ 1,2 × 61,45 % = 32,76 €  contre 32,77 € au § 2.4   ✓
           85,05 ÷ 1,2 × 61,45 % = 43,55 €  contre 43,53 € au § 3     ✓
```

Les canoniques publient 64,00 € et 85,00 € au § 2 : la redérivation tombe à 3 et
5 centimes. **Ce contrôle n'est pas décoratif** — si tes AOV ne se contrôlent pas
contre le § 2.4, tu as mélangé du TTC et du HT, et tout le reste sera faux avec l'air
d'être juste.

**(2) Le tableau de coupure.**

| Mois | Nouveaux | Cmd. réachat | CA TTC | % de P5 | CA HT | EBITDA |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Mois 0 | 37 324 | 22 876 | 4 333 196 € | 100,0 % | 3 610 997 € | 364 752 € |
| Mois 1 | **9 331** | **21 046** | **2 386 866 €** | **55,1 %** | 1 989 055 € | **862 274 €** |
| Mois 3 | **6 345** | **19 216** | **2 040 210 €** | **47,1 %** | 1 700 175 € | **684 758 €** |
| Mois 6 | **5 225** | **16 471** | **1 735 102 €** | **40,0 %** | 1 445 918 € | **528 517 €** |
| Mois 12 | **4 106** | **12 582** | **1 332 760 €** | **30,8 %** | 1 110 633 € | **322 484 €** |

Le détail du mois 1, à reproduire pour les trois autres :

```
Nouveaux   = 37 324 × 25 %  =  9 331 cmd × 63,97 € =   596 904 € TTC
Réachat    = 22 876 × 0,92  = 21 046 cmd × 85,05 € = 1 789 962 € TTC
CA TTC                                             = 2 386 866 €
CA HT      = 2 386 866 ÷ 1,2                       = 1 989 055 €
Marge brute= 1 989 055 × 61,45 %                   = 1 222 274 €
EBITDA     = 1 222 274 − 0 € de pub − 360 000 €    =   862 274 €
```

**(3) Demande autonome = 2 386 866 ÷ 4 333 196 = 55,1 %**, contre 48,3 % au module.

**(4) Le mois de bascule.**

```
Entre M6 et M12, l'EBITDA perd 528 517 − 322 484 = 206 033 € en 6 mois
                                                 =  34 339 € / mois
Il doit encore perdre 528 517 − 364 752 = 163 765 €
163 765 ÷ 34 339 = 4,77 mois  →  6 + 4,77 = mois 10,8
```

**L'EBITDA repasse sous son niveau d'avant coupure au mois 10,8** — appelle-le
**mois 11**.

**(5) Pourquoi il se déplace.** Le module, à 16 % de survivants, plaçait la bascule au
mois 6 ; à 25 %, elle passe au mois 11. **Une marque deux fois plus forte s'offre cinq
mois de mensonge comptable supplémentaires**, pas cinq mois de sursis : au mois 10,8 le
CA est à environ 32 % du niveau de départ et l'EBITDA est identique à celui d'avant.
Plus la demande autonome est élevée, plus le compte de résultat met de temps à trahir
la destruction — donc **plus la marque est forte, moins le compte de résultat sert à la
surveiller.** C'est l'inverse de l'intuition, et la raison d'être du § 1.3.

**(6) L'acquéreur.**

```
Central 5,5 × 4 377 023 €                        = 24 073 627 €
Haut    7,0 × 4 377 023 €                        = 30 639 161 €
Écart                                            =  6 565 535 €
Points de demande autonome gagnés : 55,1 − 48,3  =        6,8 pts
Valeur du point = 6 565 535 ÷ 6,8                =    965 520 €
```

**Un point de demande autonome vaut 965 520 € de valeur d'entreprise**, sans un euro
de CA ni un centime d'EBITDA supplémentaire : l'EBITDA annuel est **le même des deux
côtés**, tout l'écart est dans le multiple, et le multiple est le prix mis sur la
probabilité que le flux se reproduise sans ta publicité — exactement ce que mesure le
test de coupure.

*Réserve à écrire à côté du chiffre :* les multiples 5,5× et 7,0× sont une hypothèse
déclarée au § 8.2, pas une donnée de marché ; les 965 520 € sont donc une dérivée
d'hypothèse. Ce qui n'en est pas une, c'est la direction — le multiple monte avec la
demande autonome, et plus vite que l'EBITDA.

### Le barème (sur 20)

**3** les deux AOV à 63,97 € et 85,05 € **avec** le contrôle contre le § 2.4 écrit ·
**5** le tableau de coupure complet, ±1 % sur chaque CA TTC · **2** les quatre EBITDA
à ±1 000 € · **2** demande autonome 55,1 % · **3** mois 10,8 avec l'interpolation
posée · **2** l'explication du (5) : le délai s'allonge, la destruction est identique ·
**3** les 965 520 € avec l'EBITDA explicitement déclaré inchangé.

**Fautes éliminatoires.** Avoir appliqué 61,45 % à du CA **TTC** — 20 % d'erreur
d'un coup. Avoir soustrait une dépense publicitaire dans un mois de coupure : il n'y
en a plus, c'est tout le sujet. Avoir écrit que l'EBITDA baisse au mois 1 : il
**double presque**, et ne pas le voir, c'est ne pas avoir compris l'exercice. Avoir
fait bouger l'EBITDA annuel de 4 377 023 € en (6). Un montant sans mention TTC ou HT.

### L'erreur que presque tout le monde fait ici

**Conclure du mois 1 que la publicité ne sert à rien.** L'EBITDA passe de 364 752 € à
862 274 €, soit **+136 %**, et le raisonnement s'écrit tout seul : « on dépense
1 494 206 € par mois pour gagner 364 752 € ». Le calcul est juste, la conclusion est
fausse : elle lit un **niveau** là où il faut lire une **pente**. Au mois 12, l'EBITDA
est retombé à 322 484 € avec 30,8 % du chiffre d'affaires — même résultat, un tiers de
l'entreprise. Le seul garde-fou est de refuser de commenter la ligne d'EBITDA sans la
ligne de CA à côté.

---

## Exercice 2 — La bascule de budget au palier P3

### La réponse

**(1) CAC marginal P2 → P3.**

```
(436 000 − 104 636) ÷ (13 140 − 3 400) = 331 364 ÷ 9 740 = 34,02 €
```

Le nCAC moyen à P3 vaut 33,18 € : **le prochain client coûte 2,5 % de plus que le
client moyen.** C'est le bon chiffre pour une décision de budget.

**(2) La bascule de 8 %.**

```
Montant basculé   = 8 % × 436 000 €               =   34 880 € / mois
Clients perdus    = 34 880 ÷ 34,02                =    1 025 / mois
                                                  =   12 300 / an
Contribution perdue en régime établi
                  = 12 300 × 80,06 € (LTV 12 m)   =  984 738 € / an
EBITDA annuel P3  = 51 033 × 12                   =  612 396 €
Part concernée    = 984 738 ÷ 612 396             =    160,8 %
```

**Huit pour cent du budget publicitaire de P3 valent 160,8 % de l'EBITDA annuel du
palier.** Pas 160,8 % de la marge, pas 160,8 % du budget : de l'année entière de
résultat. Une bascule de 5 % y coûte encore 100,6 % — l'année exacte.

**(3) Les trois formulations du seuil de neutralité.**

La condition de neutralité est celle du § 6.2, et elle est exacte : basculer une
fraction `x` du budget est neutre si et seulement si le nCAC baisse de `x` sur le
budget restant.

```
1 — nCAC : −8,0 %, soit 33,18 € → 33,18 × 0,92 = 30,53 €

2 — Réachats. Contribution par réachat à P3, dérivée du § 3.1 et du § 2.4 :
    (80,06 − 30,17) ÷ 1,24 réachat à 12 mois          = 40,23 €
    984 738 ÷ 40,23 = 24 475 réachats/an = 2 040 / mois
    Réachats actuels = 18 000 − 13 140 = 4 860 / mois  →  + 42,0 %

3 — AOV. Convention des canoniques § 7 : COGS proportionnel au prix,
    logistique fixe par commande.
    Contrôle à P5 : proportionnels = 14,5 + 1,55 + 3,5 + 8,0 = 27,55 %
      3 610 997 × 10 % × 72,45 % × 12 = 3 139 401 €   ✓ ligne exacte du § 7
    À P3 : proportionnels = 16,0 + 1,65 + 3,0 + 7,0   = 27,65 %
      +10 % d'AOV = 981 000 × 10 % × 72,35 % × 12     =   851 704 € / an
      Seuil = 984 738 ÷ 851 704 × 10 %                =    +11,6 %
```

Le contrôle à P5 n'est pas facultatif : il **prouve** la convention. En traitant le
COGS comme fixe par commande tu aurais trouvé 3 767 712 € au lieu de 3 139 401 €, et su
en une ligne que ton hypothèse était fausse.

**(4) et (5) — la comparaison avec P5, et sa cause.**

| | P3, bascule 8 % | P5, bascule 8 % | P5, bascule 5 % |
| --- | ---: | ---: | ---: |
| Montant basculé / mois | 34 880 € | 119 536 € | 74 710 € |
| CAC marginal | 34,02 € | 46,56 € | 46,56 € |
| Clients perdus / mois | 1 025 | 2 567 | 1 605 |
| LTV 12 mois | 80,06 € | 86,75 € | 86,75 € |
| Contribution perdue / an | 984 738 € | 2 672 247 € | 1 670 805 € |
| **Part de l'EBITDA annuel** | **160,8 %** | **61,0 %** | **38,2 %** |

À bascule identique, **P3 paie 2,63 fois plus cher que P5**. Deux facteurs, dont le
produit reproduit exactement le rapport :

```
Facteur 1 — le poids du budget publicitaire dans le résultat
   P3 : 436 000 × 12 ÷ 612 396     = 8,543
   P5 : 1 494 206 × 12 ÷ 4 377 023 = 4,096        rapport = ×2,086

Facteur 2 — le rendement du client marginal
   P3 : 80,06 ÷ 34,02 = 2,353
   P5 : 86,75 ÷ 46,56 = 1,863                     rapport = ×1,263

Produit = 2,086 × 1,263 = 2,634
Rapport constaté = 160,8 ÷ 61,0 = 2,634                            ✓
```

**Le sens de ces deux facteurs est opposé, et la leçon est là.** Le premier dit que P3
est pauvre : son budget publicitaire pèse deux fois plus lourd dans son résultat. Le
second dit que P3 est **meilleur** : son client marginal rapporte 2,35 fois son coût,
contre 1,86 à P5. Le palier qui a le plus à gagner par euro d'acquisition est celui qui
a le moins les moyens d'en détourner un seul — et les deux effets ne se compensent pas,
ils s'additionnent contre la bascule, parce que le second renchérit le client perdu.
C'est l'erreur n° 3 du § 9, chiffrée : **le budget de marque à P2 et P3 n'achète pas de
la mémoire, il achète une faillite.**

### Le barème (sur 20)

**2** CAC marginal 34,02 € avec la formule posée · **4** les 984 738 € et les 160,8 % ·
**2** −8,0 % de nCAC et 30,53 € · **3** +2 040 réachats et +42,0 %, avec la
contribution par réachat de 40,23 € dérivée et non devinée · **4** +11,6 % d'AOV
**avec** le contrôle à P5 sur les 3 139 401 € · **2** la colonne P5 à 8 % (61,0 %) ·
**3** les deux facteurs 2,086 et 1,263 et leur produit contrôlé.

**Fautes éliminatoires.** Avoir utilisé le nCAC moyen (33,18 €) au lieu du CAC
marginal (34,02 €) pour chiffrer les clients perdus : on ne perd pas le client moyen,
on perd le dernier. Avoir comparé les 160,8 % de P3 aux 38,2 % de P5 sans recalculer
P5 à 8 % — comparer deux fractions différentes de deux budgets différents et appeler
ça un écart. Avoir appliqué 60,35 % de marge brute au surcroît d'AOV. Un montant sans
mention TTC ou HT.

### L'erreur que presque tout le monde fait ici

**Prendre la LTV 12 mois pour la perte de l'année 1.** On écrit « 12 300 clients ×
80,06 € = 984 738 € perdus cette année » et on passe à la suite. La cohorte du mois 12
n'aura livré qu'un mois de sa LTV à la clôture, celle du mois 1 en aura livré douze :
984 738 € est la perte **en régime établi**, à partir de la deuxième année, et la
première année civile en coûte environ la moitié. Écrire « en régime établi » à côté du
nombre est la différence entre un calcul et une prévision de trésorerie — exactement
l'écart qui tue des marques dont le modèle était juste.

---

## Exercice 3 — Ton test de coupure

### La réponse : la grille de lecture

| Demande autonome | Diagnostic | L'action, ce trimestre |
| ---: | --- | --- |
| **< 10 %** | Tu n'as pas une marque, tu as un compte publicitaire — le profil de Store A (§ 1.2) | Aucun budget de marque. Le chantier est le produit et le réachat |
| **10 à 20 %** | Normal à P1 et P2, alarmant dès P4 | Constance visuelle et verbale à coût zéro (§ 6.1), rien d'autre tant que l'EBITDA est négatif |
| **20 à 35 %** | Un actif existe, minoritaire. La bascule du § 2.3 commence à se discuter | 1 à 3 points de budget non directement mesurable, sous politique écrite à 24 mois (§ 6.3) |
| **35 à 50 %** | Actif réel. NØRA à P5 est à 48,3 % | 5 à 8 points. La mesure n° 4 du § 3.1 devient ton indicateur principal, parce qu'elle est mensuelle |
| **50 à 65 %** | Marque installée — ou test incomplet, vérifie d'abord | Tu es en position de monter tes prix avant de monter ton budget |
| **> 65 %** | Presque toujours un test mal fait | Relis ce que tu as laissé tourner |

**Les quatre décisions de périmètre, et la seule réponse défendable pour chacune.**

| | Règle | Pourquoi |
| --- | --- | --- |
| E-mail et SMS | **Garder** | Ils s'adressent à une base **déjà acquise** : c'est l'actif mesuré, pas la location testée. Les couper mesure ton CRM |
| Recherche sur ton nom | **Garder**, sans la compter en acquisition | Disponibilité physique (§ 5.2), rendement incrémental 0,32. La couper laisse un concurrent se placer sur ton nom |
| Reciblage | **Couper** | Il ne parle qu'à des gens que ta publicité vient d'amener : un résidu de la variable qu'on éteint |
| Affiliation et influence | **Couper**, et le dire | Du média payé (§ 5 : 8 % du budget). Le garder gonfle la demande autonome de plusieurs points |

Au-dessus de 65 %, tu as presque certainement gardé le reciblage ou l'affiliation.

**« Je ne peux pas me le permettre. »** Le calcul, et ce qu'il te dit :

```
Coût attendu = CA hebdomadaire de la zone témoin × (1 − demande autonome estimée)
               × marge brute × nombre de semaines − budget pub économisé sur la zone
```

| Coût ÷ trésorerie | Ce que tu fais |
| ---: | --- |
| **< 3 %** | Tu peux le faire, tu ne l'as jamais fait. Programme-le ce trimestre |
| **3 à 10 %** | Réduis le périmètre — jamais les seuils d'arrêt |
| **10 à 25 %** | Version géographique, plus petit marché, 14 jours |
| **> 25 %** | **Le test n'est pas le problème.** Une entreprise qui ne peut pas éteindre sa publicité deux semaines sur un marché secondaire sans risquer un quart de sa trésorerie a déjà sa réponse : tu es à P1 ou P2, et la question du budget de marque ne se pose pas avant 720 000 € de CA TTC hebdomadaire (§ 2.2) |

**Le refus de faire le test est lui-même un résultat**, et le plus rapide à obtenir.

### Le barème (sur 20)

**4** marché témoin **avec** trois indicateurs de comparabilité sur 6 mois · **4** les
quatre décisions de périmètre, chacune justifiée par un mécanisme et non une
préférence · **4** coût attendu chiffré **avant** exécution, marqué TTC ou HT · **4**
deux seuils d'arrêt écrits avant, chiffrés · **4** la demande autonome obtenue, ou le
calcul qui prouve que le test est hors de portée.

**Fautes éliminatoires.** Un seuil d'arrêt écrit après le début. Avoir gardé le
reciblage et appelé le résultat « demande autonome ». Avoir coupé l'e-mail : tu as
mesuré autre chose. « Je le ferai plus tard » sans le calcul — le calcul *est*
l'exercice.

### L'erreur que presque tout le monde fait ici

**Couper une semaine.** La durée que tout le monde choisit, parce qu'elle fait peur et
pas mal. Elle ne mesure rien : le stock de mémoire met trois à six semaines à
s'épuiser, et les commandes différées de la semaine coupée retombent la semaine
suivante. Un test de sept jours mesure ton délai de conversion, pas ton actif.
**Trente jours est le plancher, et la version géographique existe exactement pour
rendre ces trente jours payables.**

---

## Exercice 4 — L'inventaire de tes actifs distinctifs

### La réponse : la grille de lecture

**Reconnaissance** — l'actif montré seul, sans ton nom, à dix personnes de ta catégorie :

| Reconnu par | Diagnostic et action |
| ---: | --- |
| **0 à 2 / 10** | Pas un actif : une dépense de design. Deux issues — le porter sur 100 % de tes assets pendant 12 mois, ou l'abandonner. **Pas de troisième** : le pire est de le porter à moitié |
| **3 à 5 / 10** | Actif en formation, la capitalisation a commencé. Ne le touche plus, monte sa présence vers 100 %, reteste à 12 mois |
| **6 à 8 / 10** | Actif réel : il fait baisser ton coût d'exposition. Il devient une contrainte de brief opposable — aucune créa ne sort sans lui |
| **9 à 10 / 10** | Actif mature. Écris-le dans une charte, avec la date, et nomme qui a le droit de dire non |

**Présence dans tes assets des 90 derniers jours :** sous **40 %**, l'actif n'accumule
pas — tu paies l'exposition sans capitaliser. Entre **40 et 75 %**, zone morte : assez
présent pour contraindre, pas assez pour être reconnu. Au-dessus de **90 %**, régime de
capitalisation — le seul qui produit la bande 6-10 ci-dessus.

**Âge, et le cliquet du tableau de bord n° 6 :**

| Dernière modification | Lecture et action |
| --- | --- |
| **< 12 mois** | Aucune reconnaissance mesurable n'a pu se former. Interdiction de toucher, quelle que soit la lassitude interne |
| **12 à 24 mois** | La zone de danger du § 4.2 : le marché commence à reconnaître **exactement** quand l'équipe n'en peut plus. Toute refonte proposée ici est un artefact du facteur 115 000 — refuse-la par écrit |
| **> 24 mois** | Régime normal. On étend, on ne change pas |

**Le chiffrage d'une refonte** (§ 4.1) : `CA HT mensuel × 8 % × marge brute × 9 mois`.
Pour NØRA à P5 : `3 610 997 × 8 % × 61,45 % × 9 = 1 597 649 €`, soit **36,5 % d'une
année d'EBITDA**, dont pas un euro n'apparaît en comptabilité.

| Coût de refonte ÷ ton EBITDA annuel | Verdict |
| ---: | --- |
| **< 10 %** | Tu es trop jeune pour avoir un actif à détruire. Refais l'inventaire dans un an |
| **10 à 30 %** | Le coût est réel : il exige une raison écrite qui ne soit pas esthétique |
| **> 30 %** | Une décision de plusieurs centaines de milliers d'euros prise en réunion de création. Elle remonte au comité qui approuve les investissements de ce montant, ou elle n'a pas lieu |

**Combien d'actifs faut-il ?** Quatre à sept reconnus à 6/10 ou plus. Sous trois, une
seule modification te rend méconnaissable ; au-dessus de huit, aucun n'est porté sur
assez d'assets pour capitaliser.

### Le barème (sur 20)

**6** le test des dix personnes **réellement exécuté**, avec le compte par actif — un
inventaire sans test vaut 0 sur ces 6 points · **4** la part des assets, mesurée sur
les fichiers et non estimée · **3** les dates de dernière modification · **3** le
classement et l'actif nommé intouchable, avec une date d'engagement · **4** le
chiffrage de la refonte sur tes chiffres, rapporté à ton EBITDA.

**Fautes éliminatoires.** Avoir montré l'actif **avec** le nom de la marque : tu as
testé la lecture, pas la reconnaissance. Avoir interrogé ton équipe ou tes clients
fidèles au lieu de gens de ta catégorie. Avoir classé le logo en premier sans le
tester. Ne nommer aucun actif intouchable — l'exercice demande un engagement, pas un
inventaire.

### L'erreur que presque tout le monde fait ici

**Confondre « je l'aime » et « on le reconnaît ».** Le test des dix personnes existe
pour rendre cette distinction impossible à éviter, et c'est pour ça qu'il n'est presque
jamais fait. Un actif distinctif n'a pas à être beau — il doit être **unique dans ta
catégorie** et **constant dans le temps** : deux critères vérifiables, dont aucun ne
parle de goût. Conséquence pratique : le meilleur actif de ton inventaire sera souvent
celui que ton directeur artistique veut changer en priorité, précisément parce qu'il
l'a vu 1 600 heures cette année quand ton client l'a vu 50 secondes.

---

## Exercice 5 — Tes cinq mesures du § 3.1

### La réponse : la grille de lecture

| # | Mesure | Bandes et diagnostic |
| --- | --- | --- |
| **1** | **Indice de mémoire** — impressions sur requêtes de marque ÷ dépense pub du mois. **La pente, jamais le niveau** : celui-ci dépend de ton nom et n'est comparable qu'à lui-même | En hausse à dépense constante : tu **accumules**. Stable : tu tiens. En baisse deux mois de suite à dépense constante : tu **loues** — seuil d'alerte du tableau de bord n° 2 |
| **2** | **Trafic direct + organique de marque** ÷ sessions totales. Retire l'e-mail et le SMS du non payant, sinon tu mesures ton CRM (NØRA : 21,3 % après retrait de 45 %) | **< 10 %** location pure · **10 à 18 %** marque naissante · **18 à 30 %** actif réel, zone de NØRA à P5 · **> 30 %** vérifie que ton « direct » n'est pas du non-attribué |
| **3** | **Conversion à froid**, prospection pure hors reciblage. C'est l'indicateur qui **bouge le plus tôt** — avant la demande autonome, avant le trafic direct, avant le réachat | Rapporté à ta conversion globale : **< 40 %** il te faut sept touches pour vendre · **40 à 70 %** normal · **> 70 %** tu es connu avant le clic. En baisse trois mois de suite : ta marque se dégrade, quoi que disent tes autres indicateurs |
| **4** | **Prix acceptable** — variation de volume ÷ variation de prix, sur zone comparable. Une **élasticité**, donc négative. Se mesure en retirant une remise, pas en montant l'étiquette | **0 à −1** préférence forte, monte tes prix · **−1 à −2** normal · **−2 à −3,5** connu mais non préféré · **au-delà de −3,5** la remise **est** ton produit (E03 § 5) |
| **5** | **Réachat sans relance** ÷ total des réachats. Le **seul indicateur de préférence pure** : ni pub, ni e-mail, ni remise. Exige zéro contact CRM dans les 7 jours précédents | **< 20 %** ta base est louée à ton outil d'e-mailing · **20 à 30 %** fragile, seuil d'alerte du tableau de bord n° 4 · **30 à 45 %** sain, NØRA à P5 : 38 % · **> 45 %** actif rare, protège-le |

**Ce qui rendrait chaque mesure fausse**, et qu'on te demande d'écrire. **1 :** un
changement de nom de campagne, une saisonnalité de recherche, un concurrent qui
enchérit sur ton nom. **2 :** le « direct » qui absorbe tout le non-attribué —
applications, navigateurs restrictifs, liens sans paramètres. **3 :** un reciblage mal
exclu, et la définition de « froid » qui varie d'une plateforme à l'autre. **4 :** une
saison, une rupture de stock, un concurrent en promotion la même semaine. **5 :** une
notification d'application ou un courrier papier que ton outil ne compte pas comme
contact CRM, alors que c'en est un.

**Ta dette de mesure**, en comptant les lignes sans source exacte :

| Lignes sans source | Diagnostic |
| ---: | --- |
| **0 à 1** | Tu peux décider d'un budget de marque |
| **2 à 3** | Tu décideras au ressenti pendant encore un trimestre. Installe la 5 en premier : mensuelle, la moins chère, et la seule qui mesure la préférence |
| **4 à 5** | La question du budget de marque ne se pose pas encore. Ton chantier du trimestre est la mesure, et il passe avant toute action commerciale |

**Ordre d'installation**, du moins cher au plus cher : la 5 (une requête sur ta base),
la 2 (une segmentation d'analytique), la 1 (un export de régie mensuel), la 3 (une
discipline d'exclusion d'audience), la 4 (un test réel, donc un coût).

### Le barème (sur 20)

**10** deux points par mesure avec sa **valeur** et sa **source exacte** — « mon
analytics » vaut 0 ; « segment Direct + Organic hors requêtes de marque payées, export
mensuel » vaut 2 · **5** un point par mesure pour « ce qui la rendrait fausse »,
spécifique et non générique · **3** la dette de mesure nommée et comptée · **2** la
première mesure à installer, avec un délai en semaines.

**Fautes éliminatoires.** Avoir laissé l'e-mail et le SMS dans le trafic direct de la
mesure 2 : tu surestimes ta marque de dix points. Avoir mesuré la 4 en montant
l'étiquette au lieu de retirer une remise — tu as testé ton prix, pas ta préférence.
Une élasticité écrite en positif. Une mesure marquée (obs) qui est une estimation.

### L'erreur que presque tout le monde fait ici

**Commander un sondage de notoriété.** Premier réflexe, tué par une ligne
d'arithmétique au § 3.1 : détecter trois points d'écart à 80 % de puissance demande
`7,84 × 0,50 ÷ 0,03² = 4 356` répondants par vague, quand une vague à 300 porte un
intervalle de ±5,7 points — deux fois l'effet cherché. Tu paieras un institut pour
recevoir du bruit avec deux décimales. Les cinq mesures ci-dessus utilisent des données
que tu possèdes déjà, coûtent une journée d'installation, et sont mensuelles au lieu de
semestrielles.

---

## Exercice 6 — Décision : le canal sous le seuil

### La réponse

**(1) Le report sur Meta.**

```
Ratio de budget = (821 813 + 62 000) ÷ 821 813              = ×1,07544
Facteur volume  = 1,07544^0,84                              = ×1,06300
Clients Meta    = 21 346 × 1,06300                          =  22 691 / mois
Clients gagnés  = 22 691 − 21 346                           =   1 345 / mois
CAC marginal du report = 62 000 ÷ 1 345                     =   46,10 €
```

Le CAC marginal du report vaut **46,10 €, pas 38,50 €.** Tout l'exercice est là : ton
directeur compare 59,05 € à 38,50 € et voit un gouffre ; l'écart réel est de 12,95 €.

**(2) Les deux options sur 24 mois.**

| | A — garder le canal | B — couper et reporter |
| --- | ---: | ---: |
| Clients acquis sur 24 mois | 25 200 | 32 280 |
| LTV 12 mois en contribution | 88,00 € | 86,75 € |
| Contribution générée | 2 217 600 € | 2 800 290 € |
| Budget engagé | 1 488 000 € | 1 488 000 € |
| **Solde** | **729 600 €** | **1 312 290 €** |
| Contribution nette par euro dépensé | 0,49 € | 0,88 € |

**B gagne de 582 690 € sur 24 mois.** La décision arithmétique est de couper, et ton
directeur a raison sur ce qu'il a calculé — CAC marginal corrigé compris.

**Le ratio de 1,49 n'était pas l'argument.** Un ratio LTV/CAC sous le seuil ne dit pas
qu'un canal détruit de la valeur, il dit qu'il en crée moins qu'une alternative. Le
canal crée bien 729 600 € : la question n'est pas s'il gagne, c'est s'il gagne assez.

**(3) Ce que le calcul ne voit pas.**

```
Meta en clients réels après report = 19 261 + 1 345 × 0,9023 = 20 475
Total réels                        = 37 324 − 1 050 + 1 214  = 37 488
Part de Meta                       = 20 475 ÷ 37 488         =  54,6 %
```

**Meta passe de 51,6 % à 54,6 % des nouveaux clients réels** — trois points obtenus en
une réunion. Deux conséquences que le tableau des 24 mois ignore : le seuil d'alerte de
concentration de [E13](../modules/E13-risque-de-ruine.md) § 2.1 est à 55 %, tu arrives
à 0,4 point ; et le § 8.3 pose que la dépendance à Meta doit **repasser sous 50 %** pour
éviter une décote d'audit. La décision t'en éloigne.

**(4) Les trois conditions exactes qui renversent la décision.**

```
a — Élasticité de Meta
    Pour que le report rende autant que le canal (1,49 € par euro) :
      clients requis = 1,4903 × 62 000 ÷ 86,75              = 1 065 / mois
      α tel que 1,07544^α = (21 346 + 1 065) ÷ 21 346 = 1,04989
      α = ln(1,04989) ÷ ln(1,07544)                         =  0,669
    → sous α = 0,669, garder le canal devient la bonne décision.

b — Décote de multiple pour concentration
      582 690 ÷ 4 377 023 € d'EBITDA annuel                 = 0,133 ×
    → si l'acquéreur retire plus de 0,133 × de multiple pour les trois points
      de concentration supplémentaires, garder le canal est la bonne décision.

c — Demande autonome détruite par la coupure
      Un point vaut 965 520 € (exercice 1)
      582 690 ÷ 965 520                                     = 0,60 point
    → si couper le canal fait perdre plus de 0,60 point de demande autonome,
      garder le canal est la bonne décision.
```

**Les trois seuils sont tous atteignables.** Une élasticité de 0,669 est banale sur un
compte déjà à 822 000 € par mois : le 0,84 est mesuré entre P4 et P5, donc sur une
croissance accompagnée de créa neuve, pas sur un ajout de budget sec. Une décote de
0,133× vaut le quart d'un cran de multiple. Et 0,60 point de demande autonome, c'est ce
que rend un canal qui produit de la citation par des tiers plutôt que du clic.

**Décision du cursus : couper si et seulement si les trois seuils sont vérifiés comme
non atteints, et les trois nombres écrits avant de trancher.** Sans cette vérification,
garder : les 582 690 € sont un flux sur 24 mois, les trois seuils portent sur un actif,
et un flux perdu se rattrape quand un actif détruit ne se rachète pas.

**(5) La phrase.** « Je coupe ce canal si, et seulement si, l'élasticité mesurée de
Meta dépasse 0,669, faute de quoi les 582 690 € de gain sur 24 mois sont une erreur
de mesure, pas un gain. »

### Le barème (sur 20)

**4** le facteur ×1,063 et les 1 345 clients gagnés, avec l'exposant posé · **2** le
CAC marginal du report à 46,10 € et le refus explicite d'utiliser 38,50 € · **4** les
deux soldes, 729 600 € et 1 312 290 €, et l'écart de 582 690 € · **2** la décision
arithmétique énoncée en faveur de B **avant** les objections · **3** les 54,6 % de
concentration, calculés en clients réels · **4** les trois seuils : 0,669 · 0,133× ·
0,60 point, chacun avec sa dérivation · **1** la phrase de décision, avec son chiffre.

**Fautes éliminatoires.** Avoir reporté le budget au CAC moyen de Meta (38,50 €) : tu
obtiens 1 610 clients au lieu de 1 345 et tu as supprimé la moitié du sujet. Avoir
répondu « on garde, la diversification c'est important » sans chiffrer B : une intuition
juste sans calcul ne vaut pas mieux qu'un calcul juste sans intuition, et ce module
refuse les deux. Avoir calculé la concentration en clients attribués. Avoir donné les
trois conditions en mots plutôt qu'en nombres.

### L'erreur que presque tout le monde fait ici

**Reporter un budget au coût moyen du canal d'accueil.** L'erreur la plus fréquente du
métier, et la plus invisible : le tableau qui justifie le report est arithmétiquement
correct, ses données viennent de l'interface publicitaire, et il se trompe de 20 % sur
la seule ligne qui décide. Meta à 38,50 € est le prix des 21 346 clients que tu achètes
**déjà** ; les 1 345 suivants coûtent 46,10 €, parce que la courbe
`clients = k × budget^0,84` a un rendement décroissant que la régie n'affiche nulle
part. **Un budget qu'on déplace se chiffre au CAC marginal du canal d'accueil, jamais à
son CAC moyen** — et si tu n'as pas mesuré ton α, tu ne connais pas le prix de ton
propre report.

---

*Fin du corrigé E12. Suite : [E13-rendu.md](E13-rendu.md), où la demande autonome
proche de zéro rencontre un compte publicitaire qui ferme.*
