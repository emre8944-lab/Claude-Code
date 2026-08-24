# Corrigé — Module E03 : L'offre et le prix

> Ne lis ce fichier qu'après avoir rendu [`E03-rendu.md`](E03-rendu.md). Un corrigé
> lu avant l'effort donne le sentiment d'avoir compris, et rien d'autre.
>
> Convention : TVA 20 %, logistique en coût **par colis**, séparation systématique
> des coûts **fixes par commande** et **proportionnels au prix**. Les nombres de
> NØRA viennent de [`chiffres-canoniques.md`](../donnees/chiffres-canoniques.md).

---

## Exercice 1 — La table de sensibilité au prix du palier P3

### La réponse

**(1) et (2) — le CA HT par commande et les deux blocs.**

```
65,40 € TTC ÷ 1,20 = 54,50 € HT     Contrôle : × 18 000 = 981 000 €. Conforme.

Fixes par commande (ne suivent pas l'étiquette) :
  COGS       16,0 % × 54,50 =  8,72 €
  Logistique 12,0 % × 54,50 =  6,54 €              total = 15,26 €
Proportionnels au prix :
  PSP 1,65 % + retours/SAV 3,0 % + remises 7,0 %         = 11,65 %
```

Tout l'exercice est là. Le canonique donne 16 % et 12 % **du CA HT** : ce sont des
pourcentages de modélisation, pas des comportements. Un flacon coûte 3,60 € qu'il
soit vendu 29,00 € ou 23,20 € ; un colis coûte 6,54 € dans les deux cas. Les figer
en euros **avant** de toucher au prix, c'est la totalité de la difficulté.

**(3) Marge brute par commande.**

```
54,50 × (1 − 0,1165) − 15,26 = 48,15 − 15,26 = 32,89 €
Contrôle : × 18 000 = 592 033 € — canonique § 2.2. Conforme.
```

**(4) Tenir la marge brute de 592 033 €.**

| Scénario | CA HT / cmd | Marge brute / cmd | Commandes | Variation |
| --- | ---: | ---: | ---: | ---: |
| Référence | 54,50 € | 32,89 € | 18 000 | — |
| Prix **−10 %** | 49,05 € | **28,08 €** | **21 088** | **+17,2 %** |
| Prix **−20 %** | 43,60 € | **23,26 €** | **25 453** | **+41,4 %** |

```
−10 % : 49,05 × 0,8835 − 15,26 = 28,08 €   592 033 ÷ 28,08 = 21 088 (×1,1715)
−20 % : 43,60 × 0,8835 − 15,26 = 23,26 €   592 033 ÷ 23,26 = 25 453 (×1,4140)
```

La formule courte `volume = d ÷ (m − d)` avec m = 60,35 % donnerait **+19,9 %** :
elle sur-estime de 2,7 points parce qu'elle traite comme fixes 11,65 points de coûts
qui baissent avec le prix. Bonne pour un ordre de grandeur, jamais pour décider.

**(5) Tenir l'EBITDA.**

```
Publicité/commande : 436 000 ÷ 18 000 = 24,22 €
CM3/commande       : 32,89 − 24,22    =  8,67 €   × 18 000 = 156 033 €. Conforme.
EBITDA             : 156 033 − 105 000 = 51 033 €/mois. Conforme.
Cible : reconstituer 156 033 € de CM3, les fixes ne bougeant pas.
```

| Scénario | CM3 / cmd | Commandes | Variation |
| --- | ---: | ---: | ---: |
| Référence | 8,67 € | 18 000 | — |
| Prix **−10 %** | **3,85 €** | **40 492** | **+125,0 %** |
| Prix **−20 %** | **−0,96 €** | **impossible** | — |

À −20 %, la marge brute par commande (23,26 €) passe **sous** la publicité par
commande (24,22 €) : chaque commande supplémentaire détruit 0,96 €. Aucun volume ne
répare la décision, à aucune échelle. C'est la réponse attendue.

**(6) Prix +10 %, à EBITDA constant.**

```
59,95 × 0,8835 − 15,26 = 37,71 €     CM3/cmd = 37,71 − 24,22 = 13,48 €
156 033 ÷ 13,48 = 11 572 commandes   contre 18 000  →  −35,7 %
```

**« Au palier P3, je peux perdre 35,7 % de mes commandes après une hausse de 10 % et
gagner exactement autant qu'avant. »** Il faudrait une élasticité de −3,57 pour y
arriver : niveau d'une commodité indifférenciée.

**Ce que ça veut dire.** À P5 (§ 1.2 et § 1.3) : +76,4 % de volume à −10 %, −30,2 %
tolérables à +10 %. P3 est donc **plus fragile à la baisse** et **plus tolérant à la
hausse**, pour une seule raison : sa CM3 par commande vaut 8,67 € contre 12,04 € à
P5. Plus ta marge après publicité est mince, plus le prix est un levier violent —
dans les deux sens. La marque qui ne gagne pas encore d'argent est celle qui a le
moins le droit de baisser ses prix, et c'est exactement celle qui le fait.

### Le barème (sur 20)

**2** CA HT/cmd à 54,50 € avec son contrôle · **4** les deux blocs séparés, 15,26 €
et 11,65 %, avec la justification physique · **3** 32,89 € et le contrôle à
592 033 € écrit · **3** 21 088 et 25 453 commandes (±1 %) · **4** 40 492 commandes
et « impossible » à −20 % avec la CM3 négative montrée · **3** −35,7 % (±0,5 pt) et
la phrase en toutes lettres · **1** comparaison avec P5 et sa cause.

**Fautes éliminatoires.** Avoir appliqué 60,35 % de marge au nouveau prix — c'est
traiter le COGS et le colis comme proportionnels, la faute que tout l'exercice
existe pour tuer. Mélanger TTC et HT sur une ligne. Répondre « environ le double »
en (5) sans poser le calcul. Un montant sans mention TTC ou HT.

### L'erreur que presque tout le monde fait ici

**Appliquer le taux de marge au prix baissé.** On lit « marge brute 60,3 % », on
baisse de 10 %, on écrit « il me faut 10 ÷ (60,3 − 10) = +19,9 % de volume » et on
part en réunion. Deux erreurs empilées : le taux ne reste pas constant — il tombe à
57,2 % — et la question n'était pas la marge brute mais l'EBITDA, dont la vraie
réponse est **+125 %**. L'écart entre 19,9 % et 125 % est exactement l'espace dans
lequel une équipe se persuade qu'une promotion « s'autofinance ».

---

## Exercice 2 — Le seuil de franco de port optimal

### La réponse

**Le principe.** Ne calcule que les **écarts**. Une bande dont le statut ne change
pas entre deux seuils n'entre dans aucun calcul : les mono-format paient déjà le
port à 59,00 € et le paieront encore à 89,00 € et 109,00 €. Un seuil ne se juge que
sur les bandes qu'il capture.

**Seuil à 89,00 €.** Bande capturée : le Rituel, 74,00 €, 40 % des commandes.
Atteignable en un ajout, puisque 74,00 + 24,00 = 98,00 ≥ 89,00.

```
Commandes Rituel : 60 200 × 40 %                     = 24 080
  ajoutent   (25 %)  6 020 × 14,29 €                 = +  86 026 €
  paient     (72 %) 17 338 × 4,08 € HT               = +  70 739 €
  abandonnent (3 %)    722 × 35,52 € de contribution = −  25 645 €
Gain mensuel de marge brute                          =   131 120 €
Gain annuel d'EBITDA (les fixes ne bougent pas)      = 1 573 440 €   (+35,9 %)

Nouvel AOV :
  4 333 196 − 722×74,00 + 6 020×24,00 + 17 338×4,90  = 4 509 173 € TTC
  ÷ (60 200 − 722) = 59 478 commandes                =     75,81 €   (+3,83 €)
Part des commandes payant le port : (15 652 + 17 338) ÷ 59 478 = 55,5 %
```

**Seuil à 109,00 €.** Deux bandes changent de statut. La Cure (99,00 €, 27 %) passe
sous le seuil et l'atteint en un ajout (99 + 24 = 123 ≥ 109). Le Rituel reste sous
le seuil mais **ne l'atteint plus** : 74 + 24 = 98 < 109.

```
Bande Rituel — hors de portée (0 % / 94 % / 6 %) :
  paient      22 635 × 4,08 €   = + 92 351 €
  abandonnent  1 445 × 35,52 €  = − 51 326 €                   = + 41 025 €
Bande Cure — atteignable (25 % / 72 % / 3 %) :
  ajoutent     4 064 × 14,29 €  = + 58 075 €
  paient      11 703 × 4,08 €   = + 47 748 €
  abandonnent    488 × 50,73 €  = − 24 756 €                   = + 81 067 €
Gain mensuel 122 091 €  →  annuel 1 465 092 €  (+33,5 %)
Nouvel AOV : 4 443 746 ÷ 58 267 = 76,27 €      Port payé par 85,8 % des commandes
```

| | 59,00 € | 89,00 € | 109,00 € |
| --- | ---: | ---: | ---: |
| Commandes payant le port | 26 % | **55,5 %** | **85,8 %** |
| Port encaissé, € HT/mois | ≈ 63 900 € | 70 739 € | **140 099 €** |
| Ajouts déclenchés / mois | 0 | **6 020** | 4 064 |
| Abandons / mois | 0 | **722** | **1 933** |
| Nouvel AOV TTC | 71,98 € | 75,81 € | **76,27 €** |
| **Gain d'EBITDA annuel** | 0 € | **1 573 440 €** | 1 465 092 € |

**(5) Pourquoi 109,00 € est moins bon.** Le seuil viole la contrainte
d'atteignabilité sur la bande la plus lourde de la gamme : le Rituel, 40 % des
commandes, ne franchit plus le seuil en un seul ajout. Le seuil cesse d'être un
levier et devient une taxe — il encaisse deux fois plus de port (140 099 € contre
70 739 €) mais **n'achète rien avec** : zéro ajout sur cette bande, et l'abandon qui
double. Résultat : 108 348 € d'EBITDA annuel de moins qu'à 89,00 €.

**Le piège de la question (3).** L'AOV est **plus élevé** à 109,00 € (76,27 €) qu'à
89,00 € (75,81 €) alors que l'EBITDA y est plus bas. Un euro de port encaissé n'a ni
COGS ni colis ; un Rituel perdu emporte 35,52 € de contribution. **Optimiser l'AOV,
c'est optimiser une moyenne dont les euros n'ont pas la même structure.** Le juge de
paix est la marge brute par commande.

### Le barème (sur 20)

**3** n'avoir calculé que les écarts de bandes, et l'avoir dit · **4** 131 120 €/mois
et 1 573 440 €/an à 89,00 € (±1 %) · **3** AOV 75,81 € avec le CA TTC déroulé ·
**4** avoir vu que le Rituel devient hors de portée à 109,00 € · **3** ≈ 1 465 000 €
/an à 109,00 € (±2 %) · **2** contrainte d'atteignabilité nommée · **1** avoir relevé
que l'AOV monte pendant que l'EBITDA baisse.

**Fautes éliminatoires.** Le port encaissé compté en TTC dans une ligne de marge
(4,90 € au lieu de 4,08 €). Un abandon valorisé au prix de vente au lieu de sa
contribution. « 109 est mieux » parce que l'AOV y est plus haut. Avoir fait réagir
les bandes mono-format, dont le statut ne change dans aucun scénario.

### L'erreur que presque tout le monde fait ici

**Croire qu'un seuil de franco se règle « au-dessus du panier moyen », point.** La
règle a deux contraintes : le seuil doit **mordre** (S > AOV, sinon il est franchi
tout seul et ne fait rien) **et** rester **atteignable en un ajout**. On retient la
première, on en déduit que plus haut est toujours mieux, et on place le seuil
au-delà de ce que la gamme permet de franchir. Le symptôme est trompeur : le port
encaissé explose, l'AOV monte, le tableau de bord verdit — et la marge brute par
commande baisse.

---

## Exercice 3 — Ta gamme, référence par référence

### La réponse — grille de lecture

Lis d'abord le **coefficient** (PVC TTC ÷ COGS), qui dit si la catégorie finance une
acquisition payante.

| Coefficient | Diagnostic | Action |
| --- | --- | --- |
| **< ×3** | Non finançable par de la publicité payante : à ×2 le MER d'équilibre est de 7,52, hors de portée. | Pas un euro de média. Change de sourcing, de positionnement ou de canal. |
| **×3 à ×5** | Mort lente : tu peux acquérir, pas financer les signaux qui rendent ton prix crédible. | Monte le prix ou baisse le COGS **avant** tout scale. |
| **×5 à ×6** | Minimum vital. Aucune marge d'erreur sur le CAC. | Scale prudent, MER seuil recalculé chaque mois. |
| **> ×6** | Zone NØRA (×6,4 à ×8,1) : le budget du signal existe. | Le sujet devient la contribution en euros. |

Puis la **contribution en euros**, comparée à ton nCAC.

| Contribution vs nCAC | Diagnostic | Action |
| --- | --- | --- |
| **> nCAC** | S'autofinance dès la première commande. | Ta référence de scale : vérifie qu'elle porte bien du média. |
| **70 à 100 %** | Déficit léger, comblé au premier réachat. | Acceptable si le payback est **mesuré** et < 4 mois. |
| **40 à 70 %** | Cas de NØRA : héros à 16,86 € pour 40,03 € de nCAC. Pari explicite sur le réachat. | Pilotage par la LTV et les cohortes. Franco et upsell prioritaires. |
| **< 40 %** | Tu achètes des clients que seule une rétention exceptionnelle rembourse. | Ne scale pas. Répare le panier avant le budget. |

**Les verdicts de structure.** *Aucune référence ne rembourse son nCAC à la première
commande* — cas de NØRA, où seule la Cure est positive de 10,70 € : ton modèle est
un **pari sur le réachat**, donc LTV/CAC 12 mois ≥ 2,0 et payback ≤ 4 mois avant
toute accélération. *Plus d'une référence porte du budget média* : tu paies le
facteur 5 du § 3.2 — réparti sur cinq références, le budget de test met 22 semaines
à reconstituer la rotation d'**une** d'entre elles, contre 4,4 semaines concentré
sur un héros. Un concept gagnant vit quelques semaines : une rotation qui met
22 semaines à se reconstituer est morte avant d'exister. *Une référence sans rôle*
en a un cinquième, non écrit : occuper du stock et une ligne de catalogue.
Retire-la huit semaines et regarde le CA **total** — pas le sien.

**Contre-intuition.** Le Rituel a le **pire** coefficient de la gamme (×6,4) et la
**deuxième meilleure** contribution absolue (35,52 €). Un taux de marge ne paie pas
les salaires ; des euros, oui.

### Le barème (sur 20)

**5** contribution en convention colis, pas en pourcentage du panier · **3**
coefficient et contribution pour toutes les références vendues · **3** écart au nCAC
référence par référence · **3** un seul rôle par référence, et un seul héros · **2**
un responsable nommé par référence · **2** chaque chiffre marqué (obs) ou (est) ·
**2** verdict de structure écrit.

**Fautes éliminatoires.** La logistique répartie au prorata du prix — ça avantage
mécaniquement les références chères et fausse le classement. Les références « qui ne
comptent pas » omises. Deux rôles pour une référence, ou deux héros. Une case
« responsable » vide.

### L'erreur que presque tout le monde fait ici

**Classer la gamme par taux de marge.** Le tableur trie par pourcentage, l'œil suit,
et la référence à 85 % de taux et 7,69 € de contribution passe devant celle à 81 %
et 50,17 €. On met le budget média sur la première — le produit d'appel — et on se
demande pourquoi le CAC ne rentre jamais. **Trie par euros de contribution.** Le
pourcentage sert à choisir une catégorie une fois pour toutes ; les euros servent à
décider tous les jours.

---

## Exercice 4 — Ta hausse de prix de 10 %

### La réponse — grille de lecture

| Perte tolérable | Diagnostic | Action |
| --- | --- | --- |
| **> 30 %** | Marge après publicité confortable : il faudrait une élasticité pire que −3. | Monte le prix. La seule raison de s'abstenir serait une élasticité **mesurée**. |
| **20 à 30 %** | Zone normale d'une marque DTC premium qui achète son trafic. | Monte par palier, sur une zone d'abord. Surveille le taux de retour de la cohorte suivante. |
| **10 à 20 %** | CM3 par commande mince : levier violent dans les deux sens. | Hausse possible, test obligatoire, jamais toute la gamme d'un coup. |
| **< 10 %** | Ta publicité par commande mange presque toute ta marge brute. | Le problème n'est pas le prix, c'est le CAC ou le panier. |
| **Négative** | Marge brute par commande déjà sous la publicité par commande. | Chaque commande marginale détruit de la valeur. Coupe le budget avant de parler prix. |

**Le diagnostic de date.** Dernière hausse à plus de dix-huit mois : tu as consenti
une baisse de prix réelle sans jamais la décider. Une revue annuelle au calendrier,
test géographique à l'appui.

**Le diagnostic de nature.** « Supposée » cochée sans protocole écrit en dessous : ta
réponse est un nombre juste au service d'une décision impossible à prendre.
L'élasticité n'est pas observable passivement — tes ventes passées mélangent prix,
saison, budget média et créations. Deux marchés comparables, prix différents, quatre
semaines, **ventes totales** comparées — pas le taux de conversion, pas le ROAS — et
les deux seuils écrits **avant**.

### Le barème (sur 20)

**5** les deux blocs de coûts séparés poste par poste · **3** marge brute par
commande avant et après, calcul déroulé · **2** publicité par commande isolée et
maintenue constante · **2** CM3 par commande dans les deux cas · **3** volume
d'équilibre et perte tolérable · **1** la phrase en toutes lettres · **2** élasticité
déclarée mesurée ou supposée honnêtement · **2** si supposée, protocole complet avec
seuils écrits d'avance.

**Fautes éliminatoires.** La logistique classée en coût proportionnel au prix. Le
taux de marge laissé constant après la hausse. La publicité par commande qui varie
sans qu'on le dise. « Mesurée » cochée sans pouvoir citer le protocole, les dates et
les deux zones.

### L'erreur que presque tout le monde fait ici

**Répondre à « de combien vais-je perdre » alors qu'on a calculé « de combien je peux
me permettre de perdre ».** Deux nombres différents, un seul calculable au bureau. Ce
module produit un **seuil de tolérance**, jamais une prévision de volume. Celui qui
confond annonce « on va perdre 30 % de volume », se fait refuser la hausse, et laisse
sur la table les 3 767 712 € annuels du § 1.3. La bonne phrase : « je peux perdre
jusqu'à X % sans rien perdre — voici le test à quatre semaines qui nous dira ce que
nous perdons réellement. »

---

## Exercice 5 — Ta facture de remise et ton audit d'accoutumance

### La réponse — grille de lecture

| Remises en % du CA HT | Diagnostic | Action |
| --- | --- | --- |
| **< 3 %** | Discipline tenue. Niveau NØRA à P1. | Protège-le : c'est un actif, et il se perd en un trimestre. |
| **3 à 6 %** | Normal en croissance. Niveau P2–P3. | Plafond mensuel écrit, propriétaire nommé par mécanique. |
| **6 à 9 %** | Niveau P5 (8,0 %) : chaque point vaut 433 320 €/an d'EBITDA net. | Chantier de réduction — le poste le moins cher à améliorer, il ne demande ni fournisseur ni investissement. |
| **> 9 %** | Ton prix affiché est une fiction, ton positionnement aussi. | Arrête les mécaniques empilables, puis reconstruis la référence par paliers sur douze mois. |

Cadrage : à P5, 8,0 % de remise font 3 466 557 € par an, soit **9,6 mois de la
totalité des frais fixes**. C'est le seul poste de coût variable qui **se dégrade
quand tout le reste s'améliore** : 3,0 % à P1, 8,0 % à P5. Le passage à P5+ en
récupère 2,5 points — 1 083 300 €/an, **24,5 %** de l'écart d'EBITDA entre paliers.

**La répartition (question 3).** Un total sans propriétaire ne se réduit jamais. Le
geste commercial SAV est presque toujours sous-déclaré parce qu'il ne passe pas par
un code promo : va le chercher dans les avoirs, pas dans l'outil marketing.

**La concentration (question 4).** Sous 5 % du CA sur les cinq jours les plus
promotionnels, c'est sain ; de 5 à 10 %, surveille ; de 10 à 15 %, la dépendance est
installée et ton année a un point de rupture unique ; au-delà de 15 %, ton modèle
n'est plus une marque mais une opération annuelle avec onze mois d'attente. La
mesure honnête est le **creux d'avant-opération** : si le CA hebdomadaire des huit
semaines précédentes est sous la moyenne, la « performance » de l'opération contient
du CA que tu avais déjà.

**L'accoutumance (question 5) — la grille qui compte.**

| Part de la base n'achetant qu'en promotion | Diagnostic | Action |
| --- | --- | --- |
| **< 10 %** | Segment sensible au prix, normal et gérable. | Isole-le et cible-le ; ne le laisse pas contaminer les campagnes générales. |
| **10 à 20 %** | Alerte. La pente compte plus que le niveau. | Fin de la remise d'accueil systématique : exige une contrepartie (inscription, avis, parrainage). |
| **20 à 30 %** | La population plein tarif se vide dans l'autre — jamais l'inverse. | Plan de sortie sur douze mois, une mécanique à la fois. |
| **> 30 %** | La remise n'est plus un levier : c'est ton prix. | Reprix complet au prix réellement pratiqué, et reconstruction de la référence à partir de là. |

Cette part est presque toujours croissante, par un mécanisme qui ne figure sur
aucune ligne comptable : le client qui achète en promotion mémorise ce prix comme
référence, à la suivante il attend, à la troisième il n'achète plus qu'en promotion.
Série stable ou décroissante ? Vérifie ta définition de « client actif » avant de te
réjouir.

### Le barème (sur 20)

**3** total en € HT et en % du CA HT · **2** valeur d'un point sur le CA HT annuel ·
**3** répartition complète par mécanique, total à 100 % · **3** un propriétaire nommé
et un plafond écrit par mécanique · **2** geste SAV retrouvé dans les avoirs · **3**
concentration sur 5 jours et creux des 8 semaines précédentes · **4** série
d'accoutumance sur 3 ans, définition de « client actif » écrite.

**Fautes éliminatoires.** Les remises comptées en TTC. La remise traitée en réduction
de chiffre d'affaires plutôt qu'en coût variable — ligne visible, avec un
responsable, sinon elle disparaît dans le prix moyen et personne ne la défend
jamais. Une mécanique sans propriétaire. « Je n'ai pas la donnée » en (5) sans le
chantier de mesure écrit en dessous.

### L'erreur que presque tout le monde fait ici

**Juger une promotion sur son chiffre d'affaires.** « L'opération a fait 320 000 €,
c'est un record. » La bonne question n'est jamais « a-t-elle bien vendu » mais
**« combien de commandes en plus fallait-il pour qu'elle ne détruise rien »**. À
−25 %, il faut **+54,7 % de commandes** rien que pour tenir la marge brute — et le
double si la moitié seraient venues de toute façon. Presque personne ne calcule ce
nombre avant de lancer, et personne ne peut le calculer après.

---

## Exercice 6 — Décision : le prix ou le seuil

### La réponse

```
Option A — prix +6 %, volume −4 %
  CA HT/cmd          71,98 ÷ 1,20 × 1,06              =    63,58 €
  Marge brute/cmd    63,58 × 0,8695 − 15,30           =    39,98 €
  Publicité/cmd      1 494 206 ÷ 60 200               =    24,82 €
  CM3/cmd            39,98 − 24,82                    =    15,16 €
  Commandes          60 200 × 0,96                    =    57 792
  EBITDA/mois        15,16 × 57 792 − 360 000         =   516 366 €
  Gain annuel        (516 366 − 364 752) × 12         = 1 819 369 €
  Nouvel AOV         71,98 × 1,06                     =    76,30 €  (+4,32 €)
```

*Contrôle par les totaux canoniques : 1 822 320 €/an, écart de 0,2 % dû à l'arrondi
de l'AOV au centime. C'est la précision réelle de ce type de modèle.*

Option B, résultats de l'exercice 2 : **1 573 440 €/an**, AOV **75,81 €** (+3,83 €).

| | A — prix +6 % | B — franco 89,00 € |
| --- | ---: | ---: |
| Gain d'EBITDA annuel | **1 819 369 €** | 1 573 440 € |
| Nouvel AOV TTC | 76,30 € | 75,81 € |
| Coût d'exécution | 7 marchés à repricer, tous les visuels portant un prix, les flux catalogue, le CRM, la conformité d'affichage | **un nombre dans un champ de configuration**, une barre de progression, une bannière |
| Réversibilité | faible — un prix qu'on redescend enseigne à la base d'attendre | totale, en une journée |
| Délai avant de savoir | jamais, sans test géographique | 4 semaines, dans ton propre tunnel |

**La décision : option B.** Elle capture **86,5 %** du gain de A pour une fraction du
coût d'exécution ; son résultat est **observable dans ton propre tunnel en quatre
semaines** — taux de port payé, taux d'attache, taux d'abandon sont des mesures, pas
des estimations ; elle est **réversible en une journée** ; son plancher est positif,
puisque même sans aucun ajout déclenché et avec un abandon doublé à 6 % elle rapporte
encore 41 025 €/mois, soit 492 300 €/an ; et elle **laisse le levier prix intact**
pour le trimestre suivant, alors que A consomme le seul chantier du trimestre sur un
pari qu'on ne saura pas relire.

**L'estimation la plus fragile est celle de l'option A**, non parce que son chiffre
serait plus audacieux, mais parce que c'est **la seule des deux que tu ne pourras
jamais vérifier après coup** : les ventes qui suivront la hausse mélangeront prix,
saison, budget média et créations, et personne n'isolera les 4 %. Chaque hypothèse
de B produit au contraire une métrique que ton back-office affiche dès la deuxième
semaine.

### La condition exacte sous laquelle l'option A devient la bonne

```
Commandes nécessaires pour égaler le gain de B :
  (364 752 + 131 120 + 360 000) ÷ 15,16                      = 56 440
Perte de volume tolérable : 1 − 56 440 ÷ 60 200              =  6,2 %
Élasticité correspondante : 6,2 ÷ 6                          = −1,04
Perte au-delà de laquelle A détruit de la valeur : 20,6 %  (élasticité −3,43)
```

**Condition de niveau :** au-delà de 6,2 % de perte de volume réelle, B rapporte plus
que A en euros bruts. En dessous, A gagne. Le risque de A n'est donc pas de perdre de
l'argent — il faudrait −20,6 % pour cela — mais de dépenser un trimestre entier pour
gagner moins que l'option d'une journée.

**Condition de connaissance :** le 4 % doit cesser d'être une estimation interne. Le
jour où un test géographique le **mesure** sous 6,2 %, A devient la bonne décision —
et elle ne se prend plus contre B mais **après** B, au trimestre suivant, avec le
seuil de franco recalculé à 89 × 1,06 ≈ 94,00 €. Le ratio franco ÷ AOV se recalcule
à chaque révision de prix ou de gamme : c'est le seul indicateur du tableau de bord
qui se dégrade tout seul.

**Le test à quatre semaines.** Prix +6 % sur une zone, deux marchés comparables en
taille, saisonnalité et maturité — Espagne contre Italie, ou Belgique contre
Pays-Bas, jamais la France contre un petit marché. Budget média strictement identique
dans les deux zones. Métrique de décision : **ventes totales en euros HT et marge
brute totale de la zone**, jamais le taux de conversion ni le ROAS. Seuil de
généralisation écrit avant : perte mesurée < 6,2 %. Seuil d'abandon écrit avant :
perte > 10 %, ou marge brute de la zone test inférieure à celle de la zone témoin.
Quatre semaines de test, plus quatre semaines d'observation après retour au prix
initial.

### Le barème (sur 20)

**4** option A à ≈ 1 819 000 €/an (±2 %) et AOV 76,30 € · **3** option B à
1 573 440 €/an et AOV 75,81 € · **3** coût d'exécution des deux options comparé ·
**2** décision tranchée, sans « ça dépend » · **3** phrase sur l'estimation la plus
fragile, avec le motif de **vérifiabilité** · **3** seuil de bascule à 6,2 % (±0,5 pt)
avec le calcul déroulé · **2** protocole de test complet, seuils écrits avant.

**Fautes éliminatoires.** Avoir tranché sur le seul gain brut, sans le coût
d'exécution ni la réversibilité. N'avoir pas tranché. Avoir laissé la publicité
totale inchangée alors que le volume baisse de 4 %. Un test dont les seuils sont
écrits après le lancement, ou dont la métrique de décision est un taux de conversion.

### L'erreur que presque tout le monde fait ici

**Comparer deux options sur leur gain brut seul.** A rapporte 15,6 % de plus que B,
donc on prend A — et on découvre au bout du trimestre que le chantier est à moitié
fait, que la conformité de l'affichage des prix a pris six semaines, et que personne
ne sait dire si les 4 % étaient les bons. Trois colonnes manquent toujours dans ce
tableau et valent plus que la première : **le coût d'exécution, la réversibilité, le
délai avant de savoir.** Un gain de 1,57 M€ encaissé en quatre semaines et vérifiable
vaut mieux qu'un gain de 1,82 M€ espéré en un trimestre et invérifiable. Ce n'est pas
de la prudence : c'est la seule des deux options qui laisse l'autre disponible.

---

*Fin du corrigé E03. Reporte les deux ou trois nombres que tu n'avais pas dans ton
tableau de bord, donne-leur un propriétaire, puis passe à
[E04](../modules/E04-psychologie-du-client.md).*
