# Cas C08 — Redressement : de −8 % à +14 % de marge nette en 90 jours

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des
> ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.
> **Ce que tu dois en tirer :** quand la marge est négative, la croissance multiplie la
> perte — on répare la structure d'abord, on accélère ensuite.
> **Modules rattachés :** E01, E03, E06, E10, E13.

---

## 0. Conventions et origine des chiffres

**LUMEN** est une marque fictive de soin du visage, DTC, France et Belgique, 14 ETP. Tous ses
chiffres sont **modélisés** : ce cas n'emprunte aux
[chiffres canoniques](../donnees/chiffres-canoniques.md) que leurs conventions.

- TVA **20 %**. Tout montant est **TTC** (prix client) ou **HT** (comptable).
- **La remise est un coût variable, pas une réduction de chiffre d'affaires** (§ 2.1 des
  canoniques) : le CA est la **valeur catalogue** des commandes expédiées, l'encaissement réel
  étant donné à part.
- **La logistique est modélisée en % du CA HT** ; le § 2 la redérive en euros par colis.
- `MER = CA TTC ÷ pub HT` · `CM1 = CA HT − COGS` ·
  `CM2 = CM1 − logistique − PSP − retours − remises` · `CM3 = CM2 − pub` ·
  `EBITDA = CM3 − fixes`.
- L'**upsell post-achat** ne supporte ni logistique additionnelle (même colis) ni remise.

---

## 1. La situation

Jour 0. Le fondateur t'appelle : « on stagne, il faut relancer la croissance ». Il a préparé
un plan média à +50 % de budget. Voici ce que dit son compte de résultat, reconstruit ligne à
ligne.

| Ligne | Montant | % du CA HT | Ce que la ligne dit |
| --- | ---: | ---: | --- |
| CA TTC | 780 000 € | — | 15 000 cmd, panier catalogue 52,00 € TTC |
| − TVA (20 %) | −130 000 € | — | |
| **CA HT** | **650 000 €** | **100,0 %** | 7,8 M€ HT par an |
| − COGS | −117 000 € | 18,0 % | coefficient effectif ×5,6 |
| **CM1 — marge marchandise** | **533 000 €** | **82,0 %** | la seule ligne saine |
| − Logistique | −91 000 € | 14,0 % | 6,07 € net par colis |
| − PSP | −12 350 € | 1,9 % | frais de paiement |
| − Retours / SAV | −39 000 € | 6,0 % | 1 commande sur 12 |
| − Remises | −78 000 € | 12,0 % | dont 55 800 € de bienvenue |
| **CM2 — marge brute** | **312 650 €** | **48,1 %** | |
| − Publicité | −267 150 € | 41,1 % | MER 2,92 |
| **CM3 — marge de contribution** | **45 500 €** | **7,0 %** | |
| − Frais fixes | −97 500 € | 15,0 % | 14 ETP, loyer, outils |
| **EBITDA** | **−52 000 €** | **−8,0 %** | |

**Les indicateurs sans lesquels la cascade ne se lit pas.**

| Indicateur | M0 | Calcul |
| --- | ---: | --- |
| Commandes premières / réachat | 11 250 / 3 750 | 25 % des commandes en réachat |
| Panier catalogue 1ʳᵉ cmd / réachat | 48,00 € / 64,00 € TTC | l'écart est le symptôme |
| Panier réellement encaissé | 45,76 € TTC | (780 000 − 93 600) ÷ 15 000 |
| nCAC (coût d'un nouveau client) | 23,75 € | 267 150 ÷ 11 250 |
| Contribution de la 1ʳᵉ commande | 19,24 € HT | 40,00 € HT × 48,1 % |
| **Marge à la 1ʳᵉ commande** | **−4,51 €** | 19,24 − 23,75 |
| **Trésorerie / autonomie** | **132 000 € / 11 sem.** | burn 12 000 €/sem. = 52 000 × 12 ÷ 52 |

Onze semaines. Ce n'est pas un problème de croissance, c'est un compte à rebours.

---

## 2. Le diagnostic

Une journée suffit : les quatre fuites sont dans le tableau ci-dessus, aucune ne demande de
donnée nouvelle.

### 2.1 Le MER seuil de LUMEN — le chiffre qu'il n'avait jamais calculé

```
MER seuil (CM3 = 0)             = 1,20 ÷ 0,481                  = 2,49
Publicité maximale (EBITDA = 0) = 312 650 − 97 500              = 215 150 € HT
MER seuil (EBITDA = 0)          = 780 000 ÷ 215 150             = 3,63
Écart au seuil                  = 215 150 ÷ 267 150 − 1         = −19,5 %
```

Le fondateur regardait 2,92 et le trouvait « correct ». **2,92 n'est ni bon ni mauvais dans
l'absolu : il l'est par rapport à 3,63.** LUMEN dépense 52 000 € HT de plus par mois que sa
structure ne l'autorise (267 150 − 215 150) : à l'euro près, sa perte.

### 2.2 Les quatre fuites

**Fuite 1 — de la publicité sous le seuil.** Un test d'arrêt géographique de deux semaines
([C06](C06-test-incrementalite.md)) isole trois groupes de campagnes pesant **90 000 € HT par
mois**, de **MER incrémental mesuré 1,40** contre un seuil de 2,49.

```
Destruction = 90 000 − (90 000 × 1,40 ÷ 1,20 × 48,1 %) = 90 000 − 50 505 = 39 495 €/mois
```

Le budget restant (177 150 € HT) porte les 654 000 € TTC restants : MER **3,69**, au-dessus du
seuil. **Les deux tiers du compte sont déjà rentables ; c'est l'autre tiers qui tue
l'entreprise.**

**Fuite 2 — la remise permanente.** 78 000 € HT par mois, 12,0 % du CA HT : **55 800 € de code
BIENVENUE20** (−20 %, permanent, sur 62 % des premières commandes, soit 11 250 × 62 % ×
40,00 € HT × 20 %), 7 200 € de codes créateurs, 6 000 € de relance de panier, 9 000 €
d'opérations ponctuelles. Un code permanent affiché en page d'accueil n'est pas une promotion,
c'est une baisse de prix jamais décidée comme telle : 55 800 € par mois pour **rien** — ni
adresse, ni engagement, ni délai (E03 § 5).

**Fuite 3 — le port offert sous le panier moyen.** Franco à **35,00 € TTC** pour un panier
catalogue de 52,00 € : **86,9 % des colis partent en port gratuit.**

```
15 000 colis × 6,60 € HT (transport 4,60 + préparation 3PL 2,00)      = 99 000 €
− participation : 1 961 colis payants × 4,08 € HT (4,90 € TTC)        =  8 001 €
Coût logistique net                                                   = 90 999 € ≈ 91 000 €
```

Un franco placé **sous** le panier moyen n'élève pas le panier : il offre le port sur des
commandes qui l'auraient payé.

**Fuite 4 — les retours.** 6,0 % du CA HT, 39 000 € par mois, dont **61 % de motifs « pas la
texture attendue » et « mauvaise teinte »**. Ce ne sont pas des retours produit, ce sont des
retours de **fiche produit**.

**Et un cinquième poids, qui n'est pas une fuite :** les frais fixes à 15,0 % du CA HT, quand
une marque quatre fois plus petite tourne à 14,6 % (canoniques § 2.5, P2) et qu'une marque de
cette taille devrait viser 10,7 % (P3). On ne corrige pas ça en 90 jours ; on l'empêche de
grossir.

### 2.3 Ce que disent les chiffres, contre ce que croyait le dirigeant

| Les quatre fuites | Coût mensuel | En points de marge |
| --- | ---: | ---: |
| Publicité sous le seuil | 39 495 € | 6,08 pts |
| Remise permanente sans contrepartie | 42 250 € | 6,50 pts |
| Port offert (14,0 % contre 10,2 % atteignable) | 24 700 € | 3,80 pts |
| Retours (6,0 % contre 3,8 % atteignable) | 14 300 € | 2,20 pts |
| **Total** | **120 745 €** | **18,58 pts** |

**Les fuites valent 120 745 € par mois. La perte n'en vaut que 52 000 €.** LUMEN a **68 745 €
de bénéfice mensuel enfouis sous ses propres décisions commerciales**. Le fondateur croyait
devoir diluer ses frais fixes par du volume : son problème n'est pas la dilution mais la
contribution unitaire — la première commande perd 4,51 €, donc chaque client de plus aggrave
le compte.

> **À retenir :** avant de chercher du chiffre d'affaires, calcule ce que ta structure
> produirait si tu arrêtais de saboter chaque commande. Chez LUMEN, deux fois la perte.

---

## 3. Les options

**Option A — ne rien faire.** Cessation des paiements en semaine 11 ou 12.

**Option B — relancer la croissance : +50 % de budget.** Le plan du fondateur. Le budget
marginal irait aux campagnes encore élargissables — exactement le bloc mesuré à 1,40.

```
Dépense supplémentaire = 133 575 € HT  →  CA TTC = 133 575 × 1,40      = 187 005 €
Contribution           = 187 005 ÷ 1,20 × 48,1 % = 74 958 €  →  EBITDA = −58 617 €
```

CA TTC **967 005 € (+24,0 %)**, budget 400 725 € HT, MER **2,41**, EBITDA **−110 617 €
(−13,7 % du CA HT)**, consommation 25 527 €/semaine, **autonomie 5,2 semaines**. Le chiffre
d'affaires monte de 24 %, la trésorerie passe de onze à cinq semaines, et **à MER 2,41 la
marge brute ne couvre même plus la publicité** — la définition opérationnelle de « la
croissance multiplie la perte ».

**Option C — réparer la structure, sans un euro de croissance.** Huit leviers, ci-dessous.
EBITDA à M3 : **+78 397 €/mois**.

**Option D — lever 800 000 € pour financer 15 mois de perte.** Aucun prêteur ne signe en moins
de 10 semaines, et **une levée qui ne corrige aucune fuite finance les fuites** : 120 745 € ×
15 mois = 1 811 175 €, plus que la levée. D n'est jamais un substitut à C.

### 3.1 Les huit leviers de l'option C

Chiffrage **séquentiel** : chaque levier est évalué dans l'ordre d'exécution du § 4, sur
l'état laissé par le précédent. L'ordre change la répartition, pas le total. Les points sont
des points de taux d'EBITDA sur le CA HT de la période ; l'effort est en jours-homme.

| Rang gain/effort | Levier | Gain €/mois | Points | Délai | Risque | Effort | € par j·h |
| ---: | --- | ---: | ---: | --- | --- | ---: | ---: |
| 1 | Arrêt des campagnes sous le MER seuil (2,49) | 39 495 € | 5,7 | 3 j | moyen — perte de signal | 2 j | 19 748 € |
| 2 | Gel des recrutements, 2 outils, 2 missions freelance | 10 900 € | 2,0 | 0–30 j | moyen — tension d'équipe | 4 j | 2 725 € |
| 3 | Fin du code de bienvenue permanent → code à usage unique contre inscription | 20 683 € | 4,0 | immédiat | **élevé — conversion** | 8 j | 2 585 € |
| 4 | Franco relevé de 35 € à 59 € TTC | 6 604 € | 1,4 | immédiat | moyen — abandon de panier | 3 j | 2 201 € |
| 5 | Réactivation de la base dormante par courriel | 21 968 € | 3,2 | 14 j | faible — délivrabilité | 10 j | 2 197 € |
| 6 | Upsell post-achat en un clic | 13 153 € | 2,3 | 21 j | faible | 15 j | 877 € |
| 7 | Renégociation du 3PL et du transporteur | 6 072 € | 1,2 | 45–60 j | faible — migration | 12 j | 506 € |
| 8 | Baisse du taux de retour (fiche produit, guide de choix) | 11 522 € | 2,2 | 60–90 j | faible | 35 j | 329 € |
| | **Total** | **130 397 €** | **22,0** | | | **89 j** | |

**Vérification.** Points : 5,7 + 2,0 + 4,0 + 1,4 + 3,2 + 2,3 + 1,2 + 2,2 = **22,0**, donc
−8,0 % + 22,0 = **+14,0 %**. Euros : 39 495 + 10 900 + 20 683 + 6 604 + 21 968 + 13 153 +
6 072 + 11 522 = **130 397 €**, et −52 000 + 130 397 = **+78 397 €**. Attention : 22,0 % de
650 000 € HT font 143 000 €, pas 130 397 € — l'écart est la question 4.

**Deux natures de gain dans le levier 2.** L'arrêt de deux outils redondants (3 900 € nets
d'un outil de cycle de vie à 1 500 €) et la fin de deux missions freelance (7 000 €) sont des
**économies constatées** : elles font les 10 900 €. Le gel des deux CDI qu'elles préfiguraient
— **10 500 € par mois chargés** — est un **coût évité** : il n'améliore pas l'EBITDA constaté,
il empêche sa dégradation programmée. Ne les additionne jamais.

---

## 4. La décision et l'exécution

Option C, dans l'ordre du cash.

| Semaine | Ce qui est fait | Chiffre de contrôle |
| ---: | --- | --- |
| 1 | Diagnostic en une journée, gel des dépenses, test d'arrêt sur 3 groupes de campagnes. | MER seuil publié : 2,49 / 3,63 |
| 2 | Verdict : 1,40. **Coupe de 90 000 €/mois.** BIENVENUE20 remplacé par un −15 % à usage unique après inscription. Arrêt de 2 outils. | Pub : 267 150 → 177 150 € |
| 3 | Franco à 59,00 € TTC. Réactivation (6 courriels) sur 58 000 inactifs de plus de 6 mois. | Point bas de trésorerie : ≈ 126 000 € |
| 4 | Upsell post-achat en ligne (20,00 € TTC). Appel d'offres 3PL et transporteur. | Prise d'upsell : 6,1 % |
| 5 | Fin des 2 missions freelance, gel des 2 CDI. La cascade du § 1 est montrée à toute l'équipe. | Fixes : 97 500 → 86 600 € |
| 6 | Refonte des 12 fiches qui concentrent 71 % des retours : macro de texture, nuancier sur trois carnations, dosage réel. | 12 fiches sur 40 |
| 7 | Guide de choix en 4 questions, avant l'ajout au panier. Réponses du 3PL. | Retours hebdo. : 5,4 % |
| 8 | Contrat 3PL signé : préparation 2,00 → 1,80 €, transport 4,60 → 4,15 €. | −0,45 € par colis |
| 9 | Deuxième vague de réactivation, segmentée par ancienneté et produit. | 550 commandes réactivées/mois |
| 10 | Migration 3PL sur un week-end, cellule de crise 72 h. | 3 jours de retard, 0 perte |
| 11 | Fin de la refonte des 40 fiches. Guide de choix en A/B sur 50 % du trafic. | Retours : 4,3 % |
| 12 | Upsell étendu (seconde offre si refus). Nettoyage de la base courriel. | Prise d'upsell : 8,8 % |
| 13 | Clôture, recalcul de la cascade, publication du nouveau MER seuil. | MER seuil EBITDA = 0 : 2,63 |

**Le tableau de suivi mensuel.** Tous les montants sont **HT** sauf la ligne CA TTC.

| | **M0** | **M1** | **M2** | **M3** |
| --- | ---: | ---: | ---: | ---: |
| CA TTC | 780 000 € | 673 900 € | 655 100 € | 672 000 € |
| CA HT | 650 000 € | 561 583 € | 545 917 € | 560 000 € |
| Marge brute (CM2) | 312 650 € | 305 274 € | 323 758 € | 342 147 € |
| *en % du CA HT* | *48,1 %* | *54,4 %* | *59,3 %* | *61,1 %* |
| Dépense publicitaire | 267 150 € | 199 650 € | 177 150 € | 177 150 € |
| **MER** | **2,92** | **3,38** | **3,70** | **3,79** |
| CM3 | 45 500 € | 105 624 € | 146 608 € | 164 997 € |
| Frais fixes | 97 500 € | 93 600 € | 86 600 € | 86 600 € |
| **EBITDA** | **−52 000 €** | **+12 024 €** | **+60 008 €** | **+78 397 €** |
| *en % du CA HT* | *−8,0 %* | *+2,1 %* | *+11,0 %* | *+14,0 %* |
| Trésorerie fin de mois | 132 000 € | 154 024 € | 224 032 € | 308 429 € |

**La trésorerie ne monte pas seulement grâce à l'EBITDA :** les +176 429 € du trimestre sont
150 429 € d'EBITDA cumulé, **+42 000 € de stock libéré** (22 000 / 14 000 / 6 000) et
**−16 000 € de coûts ponctuels** du plan (12 000 / 4 000 / 0). Les 42 000 € sont un
**encaissement de bilan, pas un résultat** (E10).

---

## 5. Les résultats

| | M0 | M3 | Écart € | Écart en points |
| --- | ---: | ---: | ---: | ---: |
| CA TTC | 780 000 € | 672 000 € | −108 000 € | **−13,8 %** |
| Logistique | 14,0 % | 9,9 % | −35 691 € | **+4,1 pts** |
| Retours / SAV | 6,0 % | 3,8 % | −17 720 € | **+2,2 pts** |
| Remises | 12,0 % | 5,3 % | −48 176 € | **+6,7 pts** |
| **Marge brute (CM2)** | **48,1 %** | **61,1 %** | +29 497 € | **+13,0 pts** |
| Dépense publicitaire | 267 150 € | 177 150 € | −90 000 € | −33,7 % |
| MER / MER seuil EBITDA | 2,92 / 3,63 | 3,79 / 2,63 | | **de −19,5 % à +44,3 % du seuil** |
| **EBITDA mensuel** | **−52 000 €** | **+78 397 €** | **+130 397 €** | **+22,0 pts** |
| **EBITDA % CA HT** | **−8,0 %** | **+14,0 %** | | |
| nCAC | 23,75 € | 23,16 € | −0,59 € | −2,5 % |
| **Marge à la 1ʳᵉ commande** | **−4,51 €** | **+1,08 €** | **+5,59 €** | |

*COGS (18,0 %) et PSP (1,9 %) sont inchangés : aucun levier ne les touche.*

**La ligne à lire deux fois est le nCAC : il n'a quasiment pas bougé.** Ce qui a changé, c'est
ce que rapporte la première commande, 19,24 € devenus 24,24 €. **LUMEN n'a pas mieux acheté
ses clients, elle a arrêté de les revendre à perte.** Sur 90 jours, l'EBITDA cumulé est de
**+150 429 €** contre **−156 000 €** en cas d'inaction : **306 429 € d'écart**.

---

## 6. Ce qui aurait pu mal tourner

**Le chiffre d'affaires baisse d'abord, et il fallait l'accepter.** Point bas en M2 à −16,0 %,
M3 à −13,8 %. Le pont, en TTC :

```
780 000 − 126 000 (campagnes coupées) − 32 400 (fin du code) − 14 400 (franco relevé)
        + 21 300 (upsell)            + 43 500 (réactivation)  = 672 000 € TTC
```

Trois quarts de la baisse sont **du chiffre d'affaires qu'on ne voulait plus** : il coûtait
plus cher à produire qu'il ne rapportait. Un dirigeant qui juge ce plan sur la courbe de CA
l'arrête en semaine 6.

**Le MER incrémental mesuré pouvait être faux.** Le gain du levier 1 vaut
`90 000 − 90 000 × m ÷ 1,20 × 48,1 %`, soit selon le *m* réel : **1,00 → 53 925 € ·
1,40 → 39 495 € · 1,80 → 25 065 € · 2,10 → 14 243 € · 2,49 → 0 € · 2,80 → −11 010 €.** Le point
d'annulation tombe exactement sur le seuil de 2,49 — c'est la définition du seuil. **La
décision reste bonne avec 78 % d'erreur sur la mesure**, et c'est ce qui autorise à couper
vite.

**La fin de la remise pouvait coûter plus cher.** Le modèle retient −6 % de conversion des
nouveaux visiteurs ; à −12 %, le levier 3 tombe de 20 683 € à **5 941 €** — positif encore,
mais il faut le savoir avant.

**Les clients « remise » ont réagi :** 143 réclamations en trois semaines, dont 38 publiques.
Le code étant réservé à la première commande, les plus virulents étaient ceux qui ouvraient un
compte neuf à chaque achat pour le réutiliser — **ce segment achetait un prix, pas un
produit.** Le réachat de la base réelle n'a pas bougé : 3 750 commandes de M0 à M3.

**L'équipe a résisté, avec des arguments.** Le responsable acquisition a défendu son budget
avec un ROAS plateforme de 2,4 sur les campagnes coupées — déclaratif, contre un MER mesuré
par arrêt (E09). Deux personnes sont parties en semaine 6. Ce qui a débloqué la situation :
montrer la cascade et les onze semaines à tout le monde. **Un redressement qui ne publie pas
ses chiffres passe pour une punition.**

**Le scénario dégradé, chiffré avant de commencer** — MER réel 1,80, conversion −12 %,
retours à 4,8 % seulement :

| Scénario à M3 | CA TTC | EBITDA | % CA HT |
| --- | ---: | ---: | ---: |
| Nominal | 672 000 € | +78 397 € | **+14,0 %** |
| Dégradé | 601 200 € | +37 319 € | **+7,5 %** |
| Dégradé aggravé (migration 3PL ratée, base courriel brûlée) | 592 500 € | +21 048 € | **+4,3 %** |

**Le pire scénario reste 73 000 € par mois au-dessus de l'inaction.** Décider sous incertitude,
c'est comparer les planchers, pas les espérances.

**Ce qui reste ouvert :** les 42 000 € de stock libérés ne se reproduiront pas ; les frais
fixes pèsent 15,5 % du CA HT à M3, plus qu'à M0, le CA ayant baissé plus vite qu'eux ; et un
MER de 3,79 est un sous-investissement délibéré, tenu trois mois pour acheter de la sécurité.

---

## 7. Le mécanisme généralisable

> **La règle.** Quand la marge de contribution unitaire est négative, la croissance est un
> multiplicateur de perte : chaque euro d'acquisition agrandit le trou proportionnellement au
> volume. **On répare la structure d'abord, on accélère ensuite. L'ordre n'est pas une
> préférence de style, c'est une contrainte arithmétique.**

Le test, dans cet ordre. **1.** Ma marge à la première commande est-elle positive ? Sinon,
aucune dépense d'acquisition supplémentaire n'est défendable, quelle que soit la LTV projetée.
**2.** Mon MER réel est-il au-dessus de mon MER seuil EBITDA ? Sinon, je ne pilote pas une
entreprise, je pilote une vitesse de disparition. **3.** Alors seulement : où est mon CAC
marginal ? Le fondateur attaquait la troisième question avec des réponses fausses aux deux
premières — pas de l'incompétence, un ordre inversé, la forme la plus répandue de l'échec en
DTC.

**Pourquoi la croissance redevient une bonne idée à M3.** Le MER réel (3,79) est **44,3 %
au-dessus** du seuil EBITDA (2,63) : LUMEN peut redépenser jusqu'à 255 547 € HT par mois avant
de repasser sous l'équilibre. Réaccélération sur M4–M6 en remettant 32 850 € sur les campagnes
qui mesurent **2,60 de MER incrémental** — pas celles à 1,40 :

| | M0 | M3 | M6 simulé |
| --- | ---: | ---: | ---: |
| CA TTC | 780 000 € | 672 000 € | **757 410 €** |
| Dépense publicitaire HT | 267 150 € | 177 150 € | 210 000 € |
| MER | 2,92 | 3,79 | 3,61 |
| EBITDA (% CA HT) | −52 000 € (−8,0 %) | +78 397 € (+14,0 %) | **+88 679 € (+14,1 %)** |

Le chiffre d'affaires revient à 2,9 % de son niveau de départ **et la marge nette monte
encore**. La même dépense faite en M0, sur les campagnes marginales à 1,40, aurait coûté
14 416 € de perte mensuelle supplémentaire.

**C'est le vrai sujet du cas.** Pas « croissance ou marge » : un ordre d'opérations. La
croissance sur une structure réparée est un investissement ; sur une structure percée, une
fuite plus rapide. Voir [E01](../modules/E01-arithmetique-de-la-marque.md) pour la
contribution unitaire et [E10](../modules/E10-cash-et-operations.md) pour le cash — c'est lui
qui te donne ou non le droit de te tromper.

---

## 8. Questions

1. Recalcule les deux MER seuils de M0 à partir de la seule cascade du § 1, et dis de combien
   la marque est sous son seuil EBITDA.
2. Un groupe de campagnes pèse 42 000 € HT par mois, MER incrémental mesuré **2,10**.
   Faut-il le couper à M0 ? Et à M3 ? Justifie par le calcul.
3. Le fondateur veut réserver le code aux inscrits mais le remonter à **−20 %** au lieu de
   −15 %. Chiffre l'effet sur la remise mensuelle et la marge nette de M3 (taux de prise
   inchangé, 38 % des 7 650 premières commandes).
4. Un élève multiplie 22,0 % par 650 000 € HT et trouve 143 000 €, quand le pont des huit
   leviers donne 130 397 €. Qui a raison ? D'où viennent les 12 603 € d'écart ?
5. À M3, à partir de quel MER incrémental un euro de publicité **détruit-il** de l'EBITDA ?
   Et à partir de quel MER fait-il **monter le taux** de marge nette ?
6. La trésorerie a gagné 176 429 € en 90 jours pour 150 429 € d'EBITDA cumulé. Explique
   l'écart, et ce qui arrive au trimestre suivant si le chiffre d'affaires remonte.
7. Option B : à partir de quel MER incrémental le +50 % de budget aurait-il été **neutre** sur
   l'EBITDA de M0 ? Que remarques-tu ?

---

## 9. Corrigé des questions

**1.** Marge brute 312 650 € sur 650 000 € HT, soit 48,1 %.

```
MER seuil CM3 = 0        : 1,20 ÷ 0,481 = 2,4948 → 2,49
Publicité max (EBITDA=0) : 312 650 − 97 500 = 215 150 € HT
MER seuil EBITDA = 0     : 780 000 ÷ 215 150 = 3,6254 → 3,63
Écart au seuil           : 215 150 ÷ 267 150 − 1 = −19,5 %
```

Contrôle : la perte (52 000 €) **est** la dépense excédentaire (267 150 − 215 150), à l'euro
près.

**2.** Le critère de coupe est le seuil **CM3 = 0**, pas le seuil EBITDA : une campagne
au-dessus du premier contribue aux frais fixes même si l'entreprise perd de l'argent.

```
À M0 — seuil 1,20 ÷ 0,481 = 2,49. MER 2,10 < 2,49 → couper.
  Gain = 42 000 − (42 000 × 2,10 ÷ 1,20 × 48,1 %) = 42 000 − 35 354 = +6 647 €/mois
À M3 — contribution 60,6 %, seuil 1,20 ÷ 0,606 = 1,98. MER 2,10 > 1,98 → garder.
  Couper coûterait 42 000 − (42 000 × 2,10 ÷ 1,20 × 60,6 %) = −2 541 €/mois
```

**La même campagne, au même MER, se coupe à M0 et se garde à M3 :** le seuil est une propriété
de ta structure de coûts, pas de la campagne.

**3.**

```
−15 % : 7 650 × 38 % × 40,00 € HT × 15 % = 2 907 × 6,00 € = 17 442 €
−20 % : 7 650 × 38 % × 40,00 € HT × 20 % = 2 907 × 8,00 € = 23 256 €
Surcoût 5 814 €  →  EBITDA 78 397 − 5 814 = 72 583 €  →  ÷ 560 000 = 12,96 % → 13,0 %
```

Cinq points de remise de plus coûtent **1,0 point de marge nette**. Une remise n'est jamais
« juste 5 % ».

**4.** Les deux ont raison : 22,0 points est un **écart entre deux taux calculés sur des
dénominateurs différents** — −8,0 % sur 650 000 € HT, +14,0 % sur 560 000 € HT.

```
CA HT maintenu à 650 000 € : 650 000 × 14,0 % = 91 000 €
EBITDA réel de M3          :                    78 397 €
Écart 12 603 €  =  14,0 % × (650 000 − 560 000)  =  14,0 % × 90 000
```

C'est **la marge nette que LUMEN ne fait pas sur le chiffre d'affaires qu'elle a
volontairement abandonné** : les 143 000 € sont une projection à volume constant qui n'a jamais
eu lieu. **Quand tu annonces un redressement en points, dis sur quel chiffre d'affaires.**

**5.** Contribution marginale à M3 : 60,6 % du CA HT. Pour un euro de plus, à MER
incrémental *m* :

```
Effet sur l'EBITDA     = m ÷ 1,20 × 60,6 % − 1 = 0,505 m − 1
Destruction d'EBITDA   : 0,505 m − 1 < 0  →  m < 1,20 ÷ 0,606 = 1,98
Taux marginal ≥ 14,0 % : (0,505 m − 1) ÷ (m ÷ 1,20) ≥ 14,0 %  →  m ≥ 2,58
```

**Sous 1,98**, la dépense détruit de l'EBITDA ; **entre 1,98 et 2,58**, elle ajoute des euros
mais **dilue le taux** ; **au-dessus de 2,58**, elle fait les deux. La réaccélération du § 7 se
fait à 2,60 : on ne rachète pas de la croissance qui abîme le taux qu'on vient de reconstruire.

**6.** `+176 429 € = 150 429 € d'EBITDA + 42 000 € de stock libéré − 16 000 € de coûts
ponctuels.` Les 42 000 € viennent du **bilan** : le volume ayant baissé de 19 %, LUMEN a vidé
du stock déjà payé au lieu de le réapprovisionner. **Encaissement unique.** Au trimestre
suivant, si le chiffre d'affaires remonte de 13 %, le stock se reconstitue et le même mécanisme
**consomme** de la trésorerie. Confondre ce cash avec du résultat, c'est budgéter sa
réaccélération sur 176 429 € au lieu de 150 429 € (E10).

**7.** `133 575 × (m ÷ 1,20 × 48,1 % − 1) = 0  →  m = 1,20 ÷ 0,481 = 2,49.`

C'est **exactement le MER seuil CM3 = 0** de la question 1 : ce seuil *est*, par construction,
le MER auquel un euro de publicité rend un euro de contribution. Le plan du fondateur supposait
donc, sans l'écrire, que ses campagnes marginales tourneraient à 2,49 quand la mesure donnait
1,40. **Tout plan de croissance contient une hypothèse de MER incrémental. Si tu ne l'écris
pas, tu l'as quand même faite.**

---

*Fin du cas C08. Suite : [C09 — Le piège du Black Friday, modélisé](C09-piege-du-black-friday.md).*
