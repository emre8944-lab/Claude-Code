# Corrigé — Module E14 : Le plan 1 M€/semaine

> Ne lis ce fichier qu'après avoir rendu [`E14-rendu.md`](E14-rendu.md). C'est le
> dernier corrigé du cursus : si tu le lis avant, tu auras terminé quatorze modules
> sans avoir jamais eu à trancher seul une seule fois.
>
> Conventions : TVA 20 %, un point de marge d'EBITDA à P5 vaut **433 324 €** par an.

---

## Exercice 1 — Le pont P5 → P5+, refait au centime

### La réponse

**(1) Les cinq lignes de P5+.**

```
CA TTC   = 56 130 × 77,20 €                          = 4 333 236 €
CA HT    = 4 333 236 ÷ 1,2                           = 3 611 030 €
Marge brute = 3 611 030 × 66,00 %                    = 2 383 280 €
Publicité   = 4 333 236 ÷ 3,40                       = 1 274 481 €   ✓ canonique § 8
Frais fixes = 2 383 280 − 1 274 481 − 733 799        =   375 000 €
```

**Les frais fixes de P5+ ne sont pas 360 000 € mais 375 000 €.** Les canoniques ne les
publient pas ; ils se déduisent sans reste, et le nombre tombe rond — ce qui est le
signe qu'il était bien dans le modèle. **Piloter sur la marge coûte 15 000 € de
structure par mois** : la donnée, le CRM, la qualité, le contrôle de gestion.

**(2) Le pont.**

| Bloc | Écart mensuel |
| --- | ---: |
| Marge brute — 2 383 280 − 2 218 957 | **+164 323 €** |
| Publicité — 1 494 206 − 1 274 481 | **+219 725 €** |
| Frais fixes — 360 000 − 375 000 | **−15 000 €** |
| **Total / mois** | **+369 048 €** |
| **Total / an** | **+4 428 576 €** |

Canonique § 8 : 4 428 560 €. Écart **16 €**, soit 0,0004 %. Le pont boucle.

**(3) L'attribution inverse.**

```
nCAC de P5+ = 40,03 × 0,90                                     =  36,03 €
Part de réachat, à mi-chemin : 38,00 + (43,28 − 38,00) ÷ 2     =  40,64 %
   → part des commandes de première fois                       =  59,36 %

Facteur nCAC     = 40,03 ÷ 36,03                               = ×1,11111
Facteur réachat  = 0,6200 ÷ 0,5936                             = ×1,04447
Facteur AOV      = 1,17241 ÷ (1,11111 × 1,04447)               = ×1,01024
Contrôle : 1,01024 × 1,04447 × 1,11111 = 1,17241 = 3,40 ÷ 2,90       ✓

Nouvel AOV mixte = 71,98 × 1,01024                             =  72,72 € TTC
Commandes/mois   = 4 333 236 ÷ 72,72                           =  59 590
```

**Le panier ne monte presque plus : +1,0 % au lieu de +7,3 %.** C'est la conséquence
mécanique de l'identité — le MER cible est le même, donc si deux facteurs poussent
plus fort, le troisième pousse moins.

**(4) L'attribution symétrique sur trois facteurs.** Six ordres au lieu de deux ;
l'attribution est leur moyenne. Montant à répartir : 219 738 € par mois.

| Facteur | Gain / mois | Gain / an |
| --- | ---: | ---: |
| AOV | **14 091 €** | **169 090 €** |
| Réachat | **60 143 €** | **721 711 €** |
| nCAC | **145 505 €** | **1 746 057 €** |
| **Total** | **219 738 €** | **2 636 858 €** |

*(Le § 6.2 répartit 219 740 € entre deux facteurs seulement ; l'écart de 2 € vient du
CA TTC retenu — 4 333 236 € ici, 4 333 196 € là.)*

**(5) Les six chantiers refaits.**

| # | Chantier | Gain / an | Part | Points | Rang module | **Nouveau rang** |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| D | **nCAC — marque et créa** | **1 746 057 €** | 39,4 % | **+4,03** | 5 | **1** |
| C | Discipline de remise | 1 083 309 € | 24,5 % | +2,50 | 3 | **2** |
| E | COGS et logistique | 888 313 € | 20,1 % | +2,05 | 4 | **3** |
| B | Part de réachat | **721 711 €** | 16,3 % | **+1,67** | 1 | **4** |
| A | **Panier moyen** | **169 090 €** | 3,8 % | **+0,39** | 2 | **5** |
| F | Structure | −180 000 € | −4,1 % | −0,42 | 6 | **6** |
| | **Total** | **4 428 480 €** | **100,0 %** | **+10,22** | | |

*(Contrôle : 4 428 480 € contre 4 428 560 € au § 8 — écart 80 €, 0,002 %. Les points se
contrôlent en divisant chaque gain par 433 324 €.)*

**Le chantier qui change de rang : D, du cinquième au premier — quatre places.** Il
valait **zéro euro** au module et vaut **1 746 057 €** ici, soit 39,4 % du total. Le
symétrique est A, qui tombe du deuxième au cinquième.

**Ce que ça démontre, et c'est le point de l'exercice.** Le tableau du § 6.2 n'est pas
une mesure : c'est une **conséquence de l'hypothèse déclarée** *« le nCAC reste à
40,03 € »*. Change cette hypothèse de 10 % et le classement des six chantiers
s'inverse presque entièrement. La destination — 8 805 583 € d'EBITDA annuel — ne
bouge pas d'un euro ; seule la répartition du mérite bouge. **Un tableau d'attribution
ne dit jamais d'où vient l'argent, il dit ce qu'on a supposé.** C'est vrai de celui-ci,
et c'est vrai de celui de ta plateforme publicitaire.

**(6) La ligne du § 8.1 qui devient fausse.** La **logistique**.

```
Le § 8.1 pose 11,00 % → 10,23 %, soit −0,50 pt de marge brute, parce que le
coût logistique est surtout par commande et que P5+ fait −7 % de commandes.
Ici P5+ fait 59 590 commandes contre 60 200, soit −1,0 % seulement.
Logistique = 11,00 % × 59 590 ÷ 60 200                            = 10,89 %
Écart contre les 10,23 % du modèle                                =  0,66 pt
En euros : 0,66 % × 43 332 360 € de CA HT annuel                  = 286 004 €/an
```

**La marge brute de P5+ tomberait à 65,34 % au lieu de 66,00 %**, et le total du pont
perdrait 286 004 €. Un panier qui monte peu, c'est un nombre de commandes qui baisse
peu, donc une logistique qui ne se dilue pas. **Les six chantiers ne sont pas
indépendants**, et l'exercice le prouve : déplacer l'hypothèse sur le nCAC déplace la
logistique, à trois étapes de distance.

### Le barème (sur 20)

**3** les cinq lignes du (1), dont les 375 000 € de frais fixes déduits · **3** le pont
et son contrôle à 16 € · **4** les trois facteurs du (3) et le contrôle du produit à
1,17241 · **4** l'attribution sur six ordres, ±2 000 € par facteur · **3** le tableau
des six chantiers et le total à 100 € près · **2** D nommé comme chantier qui change de
rang, et l'interprétation : le § 6.2 est une conséquence d'hypothèse · **1** la ligne
logistique du (6) et ses 0,66 pt.

**Fautes éliminatoires.** Avoir attribué sur deux ordres au lieu de six quand il y a
trois facteurs — l'attribution n'est plus symétrique, et le facteur placé en premier
rafle la mise. Avoir fait bouger le total de 4 428 560 € : l'hypothèse change la
répartition, pas la destination. Avoir appliqué 66,00 % de marge brute à du CA TTC. Un
montant sans mention TTC ou HT.

### L'erreur que presque tout le monde fait ici

**Croire qu'une attribution mesure une cause.** Le § 6.2 dit que le panier vaut 26,2 %
du chemin et le nCAC 0 % ; cet exercice, avec une hypothèse différente et le même
modèle, dit 3,8 % et 39,4 %. Aucun des deux ne ment : ils répondent à des questions
différentes, posées avec des hypothèses différentes, et **la moitié des réunions de
pilotage d'une marque DTC consiste à comparer deux attributions qui ne partagent pas
leurs hypothèses.** La discipline qui protège de ça tient en une ligne : on ne présente
jamais un tableau d'attribution sans écrire, au-dessus, la phrase *« ce tableau suppose
que… »*. Le module le fait au § 6.2, en encadré, et c'est pour ça qu'on a pu le
contredire proprement.

---

## Exercice 2 — L'effondrement de la rotation créative

### La réponse

**(1) et (2) — le budget d'exposition et le contrôle du modèle.**

```
Bₑ = (budget hebdomadaire ÷ rotation) × durée de vie
   P2 : (24 147 ÷ 9)  × 5,29                                =  14 193 €
   P3 : (100 615 ÷ 21) × 5,00                               =  23 956 €
   P5 : (344 817 ÷ 23) × 4,42                               =  66 265 €
Facteur P5 ÷ P2 = 4,669       Facteur P5 ÷ P3 = 2,766

Contrôle : c* = budget hebdomadaire ÷ (taux de réussite × Bₑ)
   P2 :  24 147 ÷ (12,14 % × 14 193) = 14,01     canonique 14   ✓
   P3 : 100 615 ÷ (11,05 % × 23 956) = 38,01     canonique 38   ✓
   P5 : 344 817 ÷ ( 9,12 % × 66 265) = 57,06     canonique 57   ✓
```

Les trois paliers tombent juste avec leur propre taux de réussite et leur propre
budget d'exposition. **Le modèle du § 3.2 n'est pas une illustration : c'est une
identité qui se vérifie trois fois.**

**(3) La rotation et la pression à P5.**

| Concepts / sem. | Régime | Rotation | Pression par concept et par semaine |
| ---: | --- | ---: | ---: |
| 35 | bas | **6,4** | **53 878 €** |
| 45 | bas | **8,2** | **42 051 €** |
| 55 | bas | **10,0** | **34 482 €** |
| **57,1 (`c*`)** | équilibre | **23** | **14 992 €** |
| 60 | haut | **43,8** | **7 873 €** |
| 70 | haut | **51,1** | **6 748 €** |

```
Sous c* : N = 2 × 9,12 % × c        Au-dessus : N = 8 × 9,12 % × c
Pression = 344 817 ÷ N
```

**Entre 55 et 60 concepts par semaine — 9 % d'écart — la rotation passe de 10 à 43,8 et
la pression par concept est divisée par 4,4.** Le modèle nu a un point critique. La
réalité l'adoucit, mais la direction et l'ordre de grandeur tiennent, et ils expliquent
pourquoi une marque qui « lève le pied deux semaines » met six mois à retrouver son
MER : elle est tombée du régime haut au régime bas, et remonter demande de repasser
au-dessus de `c*`, pas de revenir au débit d'avant.

**(4) et (5) — le même `c*` avec trois calibrages.**

| `Bₑ` utilisé | celui de P2 | celui de P3 | celui de P5 |
| --- | ---: | ---: | ---: |
| `c*` à P5 | **266,4** | **157,8** | **57,1** |

Le rapport 266,4 ÷ 57,1 = 4,67 est exactement le rapport des budgets d'exposition.
**Pourquoi les trois diffèrent :** `Bₑ` est le budget qu'un concept absorbe avant de
mourir, et un concept meurt de **fréquence**, pas de temps. À P2, une audience d'un
seul pays sature après 14 193 € ; à P5, sept marchés et 60 millions de personnes
absorbent 66 265 € avant que la même lassitude apparaisse. **Le budget d'exposition
n'est pas une constante de la marque, c'est une propriété de l'audience adressée** — et
c'est pour ça que le débit créatif ne croît pas proportionnellement au budget : le
budget est ×14,3 de P2 à P5, le débit seulement ×4,07.

**(6) Le sixième marché.**

```
Budget hebdomadaire du marché = 344 817 ÷ 7                    =  49 260 €
Concepts nécessaires pour ce marché, à Bₑ de P3 :
   49 260 ÷ (9,12 % × 23 956)                                  =    22,6 / sem.
Ce que suggère un raisonnement en moyenne d'entreprise :
   49 260 ÷ (9,12 % × 66 265)                                  =     8,2 / sem.
Facteur                                                        =    ×2,77
```

**Ouvrir un marché ne demande pas une fraction proportionnelle du débit créatif : il en
demande 2,77 fois plus.** Un marché neuf est une audience étroite sans stock de mémoire,
donc un budget d'exposition faible, donc des concepts qui meurent vite. C'est le
« mini-P1 » du § 7 chiffré, et c'est la raison créative — et non seulement financière —
d'ouvrir les pays **en séquence** : quatre marchés d'un coup demandent
`4 × 22,6 = 90` concepts par semaine en plus des 57, soit un débit total de 147, alors
que l'organisation en produit 57.

### Le barème (sur 20)

**4** les trois `Bₑ` à 50 € près et les deux facteurs · **4** le contrôle des trois
`c*` contre les canoniques — un seul palier vérifié ne suffit pas · **4** les cinq
rotations et les cinq pressions, avec le régime nommé pour chacune · **3** les trois
`c*` du (4) · **2** l'explication du (5), qui doit parler d'audience et de fréquence,
pas de budget · **3** les 22,6 concepts du (6), le facteur 2,77 et la conséquence sur
l'ouverture en séquence.

**Fautes éliminatoires.** Avoir utilisé le régime haut sous `c*` ou l'inverse : la
frontière est à 57,1 et elle décide de tout. Avoir cru que `Bₑ` était une constante du
cursus. Avoir calculé le débit du sixième marché en divisant 57 par 7. Avoir répondu
que 60 concepts donnent une rotation « un peu supérieure » à 55 : elle est **4,4 fois**
supérieure, et c'est la réponse.

### L'erreur que presque tout le monde fait ici

**Traiter le débit créatif comme un objectif de production.** « 57 concepts par
semaine » se lit comme une ambition, un chiffre qu'on se fixe et qu'on approche. Ce
n'est pas ça : c'est le **débit d'équilibre d'un système de remplacement**, et un
système de remplacement n'a pas de zone intermédiaire. À 55 tu tiens 10 gagnants, à 60
tu en tiens 44 ; il n'existe aucun réglage qui en tienne 23 de façon stable, sauf
exactement à `c*`. La conséquence est qu'**à taux de réussite constant, franchir `c*`
compte plus que tout ce qu'on peut faire en deçà** — passer de 50 à 60 vaut plus que
tout ce qu'on gagne entre 35 et 55.

Il existe une seconde sortie, plus élégante et presque jamais empruntée : `c*` est
inversement proportionnel au taux de réussite. Passer de 9,12 % à 11,00 % fait tomber
`c*` de 57,1 à `344 817 ÷ (11,00 % × 66 265) = 47,3`, et **55 concepts par semaine
suffisent alors à tenir 48 gagnants au lieu de 10**. Améliorer la qualité ne remplace
pas le débit : elle déplace le seuil. Encore faut-il mesurer son taux de réussite avant
de se féliciter de l'avoir amélioré.

---

## Exercice 3 — Ton placement sur le tableau de marche

### La réponse : la grille de lecture

**La règle de placement, d'abord, parce que c'est là que 90 % des réponses sont
fausses.** Ton palier est le dernier dont tu remplis **toutes** les conditions de la
porte d'entrée. Pas celui dont tu approches le chiffre d'affaires. Une marque à
280 000 € de CA TTC hebdomadaire avec un r90 de 11 % et 8 concepts par semaine n'est
pas à P3 : elle est à **P2, avec le chiffre d'affaires de P3**, ce qui est la situation
la plus dangereuse du cursus — le budget d'un palier, la machine du précédent.

**Le diagnostic par écart.** Compare chacun de tes quatre indicateurs à la valeur
canonique de **ton palier déclaré**, pas de celui que tu vises.

| Écart | Indicateur | Ce que ça dit |
| ---: | --- | --- |
| **CA TTC hebdomadaire au-dessus de +30 %** | | Tu vends plus que ta machine ne le supporte. Le goulot est en amont — créa, cash, ou opérations. C'est le profil de mort de [C04](../etudes-de-cas/C04-scale-qui-detruit-la-marge.md) |
| **EBITDA en % du CA HT sous −5 points** | | Regarde d'abord la marge brute, pas le MER : à ce palier, deux points de CM2 pèsent plus que 0,2 de MER |
| **Marge brute sous le canonique** | | Le coefficient, la remise ou les retours. Un seul des trois, jamais les trois — identifie lequel avant d'agir |
| **Mois de trésorerie sous 4** | | Aucune autre ligne ne compte ce trimestre. Le cash est la seule contrainte qui ne se rattrape pas en travaillant plus |
| **Tous les écarts sous 15 %** | | Tu es sur la courbe. Ton chantier est la **porte suivante**, pas ton palier courant |

**Le plus grand écart nomme ton problème** — et il le nomme mieux que ton intuition,
parce qu'il est comparé à un modèle qui, lui, boucle. Les quatre indicateurs sont
choisis pour couvrir les quatre familles de mort : le volume, la marge, la structure de
coût, et le cash. Un cinquième n'ajouterait rien.

**Le cas fréquent, et la bonne conduite.** Presque tout le monde se déclare un palier
au-dessus de son palier réel, parce qu'on se place par le chiffre d'affaires. Si ton
palier déclaré est inférieur à celui que tu pensais occuper, **c'est le résultat de
l'exercice, pas son échec** : tu viens d'apprendre que tes trois prochains chantiers ne
sont pas ceux que tu avais prévus.

### Le barème (sur 20)

**6** le palier déclaré par la **règle des portes** et non par le chiffre d'affaires,
avec la liste des conditions vérifiées · **6** les quatre indicateurs, chacun marqué
(obs) ou (est) · **4** les quatre écarts en pourcentage, calculés contre le palier
déclaré · **2** le plus grand écart identifié et nommé comme problème · **2** l'écart
entre le palier déclaré et le palier que tu croyais occuper, énoncé sans le maquiller.

**Fautes éliminatoires.** S'être placé par le seul chiffre d'affaires. Avoir écrit
« entre P2 et P3 » : il n'y a pas d'entre-deux, il y a une porte. Avoir comparé ses
écarts au palier visé au lieu du palier occupé. Un EBITDA calculé en % du CA TTC.

### L'erreur que presque tout le monde fait ici

**Se placer par la ligne dont on est le plus fier.** Le tableau du § 2.1 a douze lignes
et l'œil va d'abord au chiffre d'affaires, parce que c'est la seule que l'on cite en
réunion et la seule qui monte toute seule quand on dépense plus. Or c'est aussi la
seule des douze qu'on peut acheter : trois mois de budget publicitaire à perte
déplacent la ligne de CA d'un palier entier sans déplacer aucune des onze autres.
**Le chiffre d'affaires est la conséquence des onze autres lignes, jamais leur
résumé** — et une marque qui se place par lui se croira à P4 pendant les six mois où
elle finit de mourir de son r90.

---

## Exercice 4 — Tes propres conditions de passage

### La réponse : la grille de lecture

**Les cinq seuils qui se recalculent, et qu'on recopie presque toujours au lieu de les
recalculer.**

| Seuil | La formule | Ce qui change tout |
| --- | --- | --- |
| **MER seuil (CM3 = 0)** | `1,20 ÷ ta marge brute` | Il ne dépend **ni de ta taille ni de ton budget**. À 56,5 % de CM2 il vaut 2,124 ; à 61,45 % il vaut 1,953. Cinq points de marge brute valent 0,17 de MER |
| **MER seuil (EBITDA = 0)** | `1,20 ÷ (marge brute − fixes en % du CA HT)` | Celui-ci dépend de ta taille, et il **monte quand ton CA baisse** : en perte de panier, le seuil monte pendant que le MER baisse (§ 3.3) |
| **Débit créatif d'équilibre** | `budget hebdo ÷ (taux de réussite × Bₑ)` | Exige que tu aies **mesuré** ton taux de réussite et ta durée de vie. Personne ne les a mesurés, tout le monde les estime, et l'estimation est toujours optimiste sur la durée de vie |
| **AOV mixte minimum** | `AOV 1ʳᵉ min × (1 + réachats × ratio d'AOV)` avec `LTV 12 m ≥ 2,0 × nCAC` | NØRA à P5 n'a que **8,3 %** de marge sur son panier. Si tu en as plus de 25 %, vérifie ton nCAC : il est probablement sous-estimé |
| **Trésorerie** | `BFR visé + 3 à 4 mois de fixes` | Le BFR **visé**, pas le BFR courant. La porte se franchit avec le cash du palier suivant, pas de celui qu'on quitte |

**Le décompte, et la seule lecture qui vaille.**

| Composition | Verdict |
| --- | --- |
| **Toutes à oui** | Porte ouverte. Franchis-la ce trimestre : une porte ouverte qu'on ne franchit pas se referme, parce que les seuils du palier suivant montent avec le temps |
| **Une ou deux à non**, aucune non mesurée | Porte fermée, et tu sais exactement pourquoi. Ce sont tes chantiers de l'exercice 5 |
| **Une seule non mesurée** | Porte fermée. Une condition non mesurée compte comme un **non**, jamais comme un « probablement oui » |
| **Trois non mesurées ou plus** | Tu ne pilotes pas, tu constates. Le plan des 90 prochains jours est intégralement un plan de mesure, et il n'y a rien à discuter |

**« Non mesuré » est la seule réponse honnête, et la plus fréquente.** Elle n'est pas
une faute : la faute est de l'écrire « oui » parce qu'on a un ordre de grandeur en
tête. Les trois lignes qui recueillent le plus de faux « oui », dans l'ordre : le
**coefficient rendu** (calculé sur le tarif fournisseur au lieu du prix rendu entrepôt
— 3,8 points d'écart chez NØRA, un ×7,4 sortie usine qui est un ×6,0 rendu), le **r90**
(estimé sur l'ensemble des clients au lieu d'une cohorte réelle), et l'**âge moyen des
gagnants** (que personne ne mesure parce qu'aucune interface ne l'affiche).

**Le rituel de porte.** Une date, un tenant, et une règle : on ne discute pas une ligne
pendant le rituel, on la lit. Les conditions se remplissent avant, ou elles ne se
remplissent pas. Un rituel trimestriel où l'on argumente qu'une condition est
« presque » remplie n'est pas un rituel de porte, c'est une réunion de justification.

### Le barème (sur 20)

**5** les deux MER seuils **recalculés** sur ta marge brute et tes fixes, pas recopiés ·
**4** le débit créatif d'équilibre, avec ton taux de réussite et ton `Bₑ` mesurés · **4**
l'AOV minimum, avec le calcul posé en entier et ta marge sur le panier · **3** la
trésorerie exigée, calculée sur le **BFR visé** · **2** le décompte oui / non / non
mesuré, sans troisième catégorie inventée · **2** la date du rituel et son tenant.

**Fautes éliminatoires.** Avoir recopié un seuil canonique au lieu de le recalculer —
c'est l'exercice entier. Avoir écrit « presque » ou « en cours » dans la colonne de
droite. Avoir compté une condition non mesurée comme un oui. Avoir calculé la
trésorerie exigée sur le BFR du palier qu'on quitte. Un coefficient calculé sur le
tarif fournisseur sans le port ni les droits.

### L'erreur que presque tout le monde fait ici

**Traiter les conditions comme une moyenne.** « J'en ai cinq sur six, je suis à 83 % »
est arithmétiquement vrai et opérationnellement faux : les cinq conditions du § 0 ne se
compensent pas, et les portes non plus. Un coefficient à ×4 rend l'AOV minimum
inatteignable quel que soit le panier ; un cash absent au mois 19 arrête une marque
dont les quatre autres conditions sont vraies. **Quatre sur cinq ne donnent pas 80 % du
résultat, elles donnent zéro** — et la seule façon de s'en souvenir est de refuser la
colonne « partiellement ». Trois réponses, jamais quatre.

---

## Exercice 5 — Ton plan à 90 jours

### La réponse : la grille de lecture

**Le test unique.** Un chantier qui ne fait basculer aucune ligne de l'exercice 4 de
« non » ou « non mesuré » à « oui » n'est pas un chantier : il est **hors saison**. Le
§ 4 le démontre à P2 — travailler l'offre y rapporte 11 279 € par mois quand franchir
la porte en rapporte 70 871 €, soit **6,3 fois plus**, et le premier ne débloque rien :
à −8 559 € par mois, la marque reste en P2 avec un an de trésorerie en moins. Le levier
de l'offre n'est pas mauvais, il est prématuré ; il redeviendra le premier levier du
cursus à P5.

**Trois, pas quatre.** La contrainte n'est pas cosmétique. Un chantier de 90 jours
consomme une personne responsable, un indicateur suivi chaque semaine, et une capacité
d'arbitrage. Au-delà de trois, aucun n'a de responsable réel et tous glissent d'un
trimestre.

**La grille par palier**, pour savoir si tes trois chantiers sont les bons :

| Ton palier | Le goulot du § 4 | Si tes trois chantiers n'en traitent aucun |
| --- | --- | --- |
| **P1** | **L'offre** — MER réel 1,80 contre seuil CM3 2,10, un écart de structure qu'aucune optimisation média ne comble | Tu optimises une machine qui ne peut pas gagner. Change de produit ou de source |
| **P2** | **La créa** — de 3 à 14 concepts par semaine, puis 38 : ×12,7 de débit pendant que l'effectif passe de 1,5 à 12 ETP | Tu retardes le seul chantier dont l'effet met six mois à arriver |
| **P3** | **Le cash et la créa** — la durée de P3 est exactement la vitesse de l'autofinancement, `ln(2,490) ÷ ln(1,106) = 9,06 mois` | Tu vas franchir P4 avec la machine de P3 |
| **P4** | **L'organisation et les marchés** — le cash autoriserait P4 en 2,93 mois, le modèle en donne 12 : **les 9,07 mois d'écart sont de l'organisation pure** | Tu paies neuf mois pour rien |
| **P5** | **La marge** — le volume est atteint, toute la valeur restante est dans la façon de fabriquer le même chiffre d'affaires | Tu laisses 4 428 560 € par an sur la table |

**Le critère d'échec écrit d'avance.** C'est la ligne que tout le monde laisse vide, et
c'est celle qui distingue un plan d'une intention. Un critère valide a trois
propriétés : il est **chiffré**, il est **daté**, et il dit **ce qu'on fait** quand il
est atteint. « Si le r90 n'améliore pas » n'est pas un critère. « Si le r90 des
cohortes de janvier, février et mars reste sous 15 %, on arrête la montée en budget et
le chantier 2 devient le chantier 1 » en est un.

| Défaut du critère d'échec | Ce qu'il produit |
| --- | --- |
| Pas de chiffre | On décidera au ressenti, donc en faveur de la continuation |
| Pas de date | Le chantier ne finit jamais, il s'estompe |
| Pas d'action associée | Le critère est atteint, constaté, et rien ne change |
| Écrit après le lancement | Ce n'est plus un critère, c'est une justification |

**La règle transversale.** Le chantier de mise en mesure passe avant le chantier
commercial. Une condition « non mesurée » te fera décider au ressenti pendant encore un
trimestre, ce qui coûte plus cher que le trimestre passé à installer la mesure. Si tes
trois chantiers sont tous commerciaux alors que trois lignes de l'exercice 4 sont non
mesurées, tu as construit un plan qui ne pourra pas être évalué.

### Le barème (sur 20)

**3** trois chantiers, pas quatre · **5** un **indicateur unique** par chantier, avec sa
valeur d'aujourd'hui — un chantier à deux indicateurs vaut 0 pour sa ligne · **3** les
trois cibles à J+90, chiffrées · **6** les trois critères d'échec, chacun chiffré, daté,
et assorti de l'action déclenchée · **2** la ligne de l'exercice 4 que chaque chantier
fait basculer, nommée · **1** un responsable nommé par chantier.

**Fautes éliminatoires.** Un quatrième chantier. Un chantier qui ne fait basculer aucune
ligne. Un critère d'échec sans nombre. Un chantier sans responsable nommé — « l'équipe »
n'est pas un responsable. Trois chantiers commerciaux quand trois lignes de l'exercice 4
sont non mesurées.

### L'erreur que presque tout le monde fait ici

**Choisir le chantier du palier suivant plutôt que celui du palier courant.** C'est
l'erreur la plus sympathique du cursus : une marque à P2 veut travailler son panier
moyen et sa marge, parce que ce sont les leviers dont parlent tous les modules et qu'on
lit le § 7 des canoniques comme un classement universel. Il ne l'est pas — il est
calculé **au palier P5**. À P2, le même levier vaut 11 279 € par mois contre 70 871 €
pour le franchissement de la porte. **Le classement des leviers dépend du palier, et un
levier hors saison ne coûte pas seulement son manque à gagner : il coûte le trimestre
qu'il occupe.** Le test qui protège tient en une phrase, et il est mécanique : *si je
doublais ce chantier demain, quelle condition de passage passerait de « non » à
« oui » ?* Aucune ? Ce n'est pas ton chantier.

---

## Exercice 6 — Décision : accélérer ou réparer

### La réponse

**(1) L'état actuel.**

```
CA TTC/mois = 62 000 × 4,3333                        =  268 666 €
CA HT       = 268 666 ÷ 1,2                          =  223 889 €
Marge brute = 223 889 × 56,5 %                       =  126 497 €
Publicité   = 268 666 ÷ 2,35                         =  114 326 €
CM3         = 126 497 − 114 326                      =   12 171 €
EBITDA      = 12 171 − 31 000                        =  −18 829 € / mois

Commandes   = 268 666 ÷ 58,00 €                      =    4 632
   dont réachats 15 %                                =      695
   dont nouveaux clients                             =    3 937
nCAC        = 114 326 ÷ 3 937                        =    29,04 €

MER seuil (CM3 = 0)    = 1,20 ÷ 0,565                =    2,124
Fixes en % du CA HT    = 31 000 ÷ 223 889            =   13,85 %
MER seuil (EBITDA = 0) = 1,20 ÷ (0,565 − 0,1385)     =    2,813
Écart : 2,35 ÷ 2,813 − 1                             =   −16,5 %
```

L'entreprise est **16,5 % sous son MER d'équilibre EBITDA**, au-dessus de son seuil de
contribution (2,124). C'est exactement la position de P2 dans le canonique § 2.3 : elle
achète des clients à perte en pariant sur le réachat, et le pari n'est pas encore payé.

**(2) La porte P2 → P3.**

| Condition | Seuil | Sa valeur | |
| --- | ---: | ---: | --- |
| Marge brute CM2 | ≥ 55 % | 56,5 % | **oui** |
| MER blended | ≥ 2,20 | 2,35 sur 9 sem. | **oui** |
| Concepts nouveaux / semaine | ≥ 10 | 11 | **oui** |
| Gagnants distincts en rotation | ≥ 5 | 6 | **oui** |
| **r90** | ≥ 18 % | **14,5 %** | **NON** |
| **Trésorerie** | ≥ 796 053 € | **340 000 €** | **NON** |

**Quatre sur six. La porte est fermée**, et elle l'est sur les deux conditions que
tripler un budget ne peut ni l'une ni l'autre améliorer.

**(3) Option A — tripler le budget.**

```
Publicité   = 114 326 × 3                            =  342 978 € / mois
Facteur CA  = 3^0,84                                 =   ×2,5164
CA TTC      = 268 666 × 2,5164                       =  676 076 €
Nouveau MER = 676 076 ÷ 342 978                      =    1,971
Marge brute = 676 076 ÷ 1,2 × 56,5 %                 =  318 319 €
CM3         = 318 319 − 342 978                      =  −24 659 €
EBITDA      = −24 659 − 31 000                       =  −55 659 € / mois
Sur 12 mois                                          = −667 914 €
BFR = (676 076 − 268 666) × 40,864 %                 =  166 484 €
Besoin de cash total                                 =  834 398 €
Trésorerie disponible                                =  340 000 €
Manque                                               =  494 398 €
Rupture : (340 000 − 166 484) ÷ 55 659               =  mois 3,1
```

**Le MER tombe à 1,971, sous le seuil de contribution de 2,124.** Ce n'est plus une
question de rentabilité : **chaque euro de chiffre d'affaires supplémentaire détruit de
la marge**, et aucun volume ne répare la décision à aucune échelle. La trésorerie est
épuisée au **mois 3**, et les frais fixes ont été supposés constants, ce qui est
généreux : à 676 000 € de CA TTC mensuel, ils ne le resteront pas.

**(4) Option B — réparer le r90, budget inchangé.**

```
Réachats par client à 12 mois = (r90 ÷ 0,2742) × 2,8182
   à 14,5 % : (52,88 %) × 2,8182                     =   1,4903
   à 18,0 % : (65,65 %) × 2,8182                     =   1,8500
   gain                                              =   0,3597
Réachats supplémentaires = 3 937 × 0,3597            =    1 416 / mois
Contribution par réachat = 72,00 ÷ 1,2 × 56,5 %      =    33,90 €
Gain en régime établi = 1 416 × 33,90 €              =   48 015 € / mois
EBITDA en régime établi = −18 829 + 48 015           =  +29 186 € / mois
Sur 12 mois, gain compté à 50 % : −225 948 + 288 090 =  +62 142 €
Trésorerie à 12 mois = 340 000 + 62 142              =  402 142 €
```

**(5) L'écart entre les deux options sur 12 mois : `402 142 − (340 000 − 834 398) =
896 540 €.`** L'option A détruit 834 398 € de trésorerie et laisse l'entreprise morte
au mois 3 ; l'option B en crée 62 142 € et ouvre une des deux conditions manquantes.

**La décision : réparer.** Et pas parce que c'est prudent — parce que le MER après
triplement passe **sous le seuil de contribution**. C'est l'erreur n° 1 du § 8 :
franchir une porte avec un r90 insuffisant ne fait pas découvrir un problème, il le
**multiplie par trois** et avance la date à laquelle il coûtera dix fois plus cher.

**(6) Les conditions qui renversent la décision, et le délai pour savoir.**

| Levier | Seuil exact | Délai |
| --- | --- | ---: |
| **Élasticité `α`** | `2,35 × 3^(α−1) ≥ 2,124` → **α ≥ 0,908** | 6 à 8 sem. par un test de budget par paliers |
| **r90** | **18,0 %**, il manque 3,5 points | **21 semaines** : 13 par cohorte, plus 8 pour en aligner trois consécutives |
| **Trésorerie** | +494 398 € — et **ce n'est pas suffisant** | immédiat |
| **Débit créatif** | `79 149 ÷ (11,05 % × 23 956)` = **29,9 concepts / sem.**, il en fait 11 | **8 semaines**, c'est la définition de la porte |

**La ligne « trésorerie » est la plus importante des quatre, et sa réponse est non.**
Réunir les 494 398 € rend l'option A survivable, pas bonne : à MER 1,971 sous un seuil
de contribution de 2,124, l'argent ne fait que financer plus longtemps une destruction
de marge. **Aucun montant de trésorerie ne rend rentable un MER sous le seuil de
contribution.** C'est le seul cas du cursus où du cash ne répare rien.

**Le levier qui se vérifie le plus vite est le débit créatif : 8 semaines.** C'est donc
par lui qu'on commence — et il est aussi le seul des quatre qui soit un **rythme** et
non un résultat : les trois autres se dégraderont s'il ne tient pas, avec six mois de
retard.

**(7) La phrase.** « Je ne triple pas : à budget ×3, mon MER tombe à 1,971 sous mon
seuil de contribution de 2,124, ma trésorerie est épuisée au mois 3, et il me manque
494 398 € qui ne répareraient rien. Je passe de 11 à 30 concepts par semaine — je le
saurai en 8 semaines — et je remonte mon r90 de 14,5 % à 18 %, ce qui vaut 48 015 € par
mois et me rend rentable sans un euro de budget en plus. »

### Le barème (sur 20)

**3** l'état actuel, dont l'EBITDA à −18 829 € · **3** les deux MER seuils, 2,124 et
2,813, recalculés sur sa marge brute et ses fixes · **2** la porte fermée sur r90 **et**
trésorerie · **4** l'option A : MER 1,971, EBITDA −55 659 €, besoin 834 398 €, rupture
au mois 3 · **4** l'option B : 1 416 réachats, 48 015 € par mois, trésorerie à
402 142 € · **3** les quatre conditions du (6), chacune chiffrée, dont le **non** à la
ligne trésorerie · **1** la phrase de décision, avec son chiffre.

**Fautes éliminatoires.** Avoir triplé le CA en même temps que le budget : c'est
l'hypothèse `α = 1`, et elle est fausse de 25 points de chiffre d'affaires. Avoir oublié
le BFR. Avoir répondu « on triple, on a 340 000 € de trésorerie » sans calculer le mois
de rupture. Avoir conclu que réunir 494 398 € règle le problème. Avoir comparé le MER
de 1,971 au seuil EBITDA de 2,813 au lieu du seuil de contribution de 2,124 — les deux
disent non, mais ils ne disent pas la même chose.

### L'erreur que presque tout le monde fait ici

**Croire qu'un problème de croissance se règle avec du budget.** L'associé n'a pas tort
de vouloir accélérer : le MER blended de 2,35 sur neuf semaines est au-dessus du seuil
de contribution, la marge brute passe la porte, la créa passe la porte, la rotation
passe la porte. Quatre signaux sur six disent « vas-y ». Les deux qui disent non — le
r90 et la trésorerie — sont précisément les deux que **le budget ne touche pas**, et
c'est ce qui les rend invisibles : on les cherche dans le tableau de bord de la semaine
et ils n'y sont pas, parce que l'un se mesure en trimestres et l'autre sur un relevé
bancaire. **Les conditions qu'un budget publicitaire ne peut pas améliorer sont
exactement celles qu'il faut vérifier avant de l'augmenter** — et c'est toute la raison
d'être des portes du § 2.2.

---

*Fin du corrigé E14, et fin du cursus. Il ne te manque plus que la seule chose qu'aucun
corrigé ne peut te donner : la discipline de ne pas franchir une porte avant de l'avoir
remplie. Reprends le [diagnostic](../mentorat/diagnostic.md), puis reviens à l'exercice
4 tous les trimestres.*
