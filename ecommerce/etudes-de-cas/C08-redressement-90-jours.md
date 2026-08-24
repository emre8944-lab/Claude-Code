# Cas C08 — Redressement : de −8 % à +14 % de marge nette en 90 jours

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des
> ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.
> **Ce que tu dois en tirer :** quand la marge est négative, la croissance multiplie la
> perte — on répare la structure d'abord, on accélère ensuite.
> **Modules rattachés :** E01, E03, E06, E10, E13.

---

## 0. Conventions et origine des chiffres

**LUMEN** est une marque fictive de soin du visage, DTC, France et Belgique, quatre ans,
14 ETP. Tous ses chiffres sont **modélisés** : ce cas n'emprunte aux
[chiffres canoniques](../donnees/chiffres-canoniques.md) que leurs conventions.

- TVA **20 %**. Tout montant est **TTC** (prix client) ou **HT** (chiffre d'affaires
  comptable) : `CA HT = CA TTC ÷ 1,20`.
- **La remise est un coût variable, pas une réduction de chiffre d'affaires** (§ 2.1 des
  canoniques). Le CA est donc la **valeur catalogue** des commandes expédiées ; la remise
  est une ligne de coût visible. L'encaissement réel est donné à part.
- **La logistique est modélisée en % du CA HT** ; le § 2 la redérive en euros par colis.
- `MER = CA TTC ÷ dépense publicitaire HT` · `CM1 = CA HT − COGS` ·
  `CM2 = CM1 − logistique − PSP − retours − remises` · `CM3 = CM2 − publicité` ·
  `EBITDA = CM3 − frais fixes`.
- L'**upsell post-achat** ne supporte ni logistique additionnelle (même colis) ni remise.

---

## 1. La situation

Jour 0. Le fondateur t'appelle avec une phrase : « on stagne, il faut relancer la
croissance ». Il a préparé un plan média à +50 % de budget. Voici ce que son propre compte
de résultat dit, une fois reconstruit ligne à ligne.

**Cascade de marge — mois M0 (mensuel)**

| Ligne | Montant | % du CA HT | Ce que la ligne dit |
| --- | ---: | ---: | --- |
| CA TTC | 780 000 € | — | 15 000 commandes, panier catalogue 52,00 € TTC |
| − TVA (20 %) | −130 000 € | — | |
| **CA HT** | **650 000 €** | **100,0 %** | 7,8 M€ HT par an |
| − COGS | −117 000 € | 18,0 % | coefficient effectif ×5,6 sur le TTC |
| **CM1 — marge marchandise** | **533 000 €** | **82,0 %** | la seule ligne saine du tableau |
| − Logistique | −91 000 € | 14,0 % | 6,07 € net par colis |
| − PSP (frais de paiement) | −12 350 € | 1,9 % | carte + paiement fractionné |
| − Retours / SAV | −39 000 € | 6,0 % | 1 commande sur 12 revient |
| − Remises | −78 000 € | 12,0 % | dont 55 800 € de code de bienvenue |
| **CM2 — marge brute** | **312 650 €** | **48,1 %** | |
| − Publicité | −267 150 € | 41,1 % | MER 2,92 |
| **CM3 — marge de contribution** | **45 500 €** | **7,0 %** | |
| − Frais fixes | −97 500 € | 15,0 % | 14 ETP, loyer, outils, agence |
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
| CA HT annuel par ETP | 557 143 € | 7,8 M€ ÷ 14 |
| Trésorerie / consommation hebdo. | 132 000 € / 12 000 € | 52 000 × 12 ÷ 52 |
| **Autonomie** | **11 semaines** | 132 000 ÷ 12 000 |

Onze semaines. Ce n'est pas un problème de croissance, c'est un compte à rebours.

---

## 2. Le diagnostic

Une journée suffit : les quatre fuites sont toutes dans le tableau ci-dessus et aucune ne
demande de donnée nouvelle.

### 2.1 Le MER seuil de LUMEN — le chiffre qu'il n'avait jamais calculé

```
MER seuil (CM3 = 0)             = 1,20 ÷ 0,481                   = 2,49
Publicité maximale (EBITDA = 0) = CM2 − fixes = 312 650 − 97 500  = 215 150 € HT
MER seuil (EBITDA = 0)          = 780 000 ÷ 215 150              = 3,63
Écart au seuil                  = 215 150 ÷ 267 150 − 1          = −19,5 %
```

Le fondateur regardait 2,92 et le trouvait « correct » — il l'avait lu quelque part. **2,92
n'est ni bon ni mauvais dans l'absolu : il l'est par rapport à 3,63.** LUMEN dépense
52 000 € HT de plus par mois que sa structure ne l'autorise (267 150 − 215 150). C'est,
à l'euro près, sa perte.

### 2.2 Les quatre fuites

**Fuite 1 — de la publicité sous le seuil.** Un test d'arrêt géographique de deux semaines
(protocole du cas [C06](C06-test-incrementalite.md)) isole trois groupes de campagnes
pesant **90 000 € HT par mois**, de **MER incrémental mesuré 1,40** contre un seuil de 2,49.

```
Destruction = 90 000 − (90 000 × 1,40 ÷ 1,20 × 48,1 %) = 90 000 − 50 505 = 39 495 €/mois
```

Le budget restant (177 150 € HT) porte les 654 000 € TTC restants, soit un MER de **3,69**,
au-dessus du seuil. **Les deux tiers du compte publicitaire sont déjà rentables ; c'est
l'autre tiers qui tue l'entreprise.**

**Fuite 2 — la remise permanente.** 78 000 € HT par mois, 12,0 % du CA HT.

| Poste de remise | M0 | Contrepartie obtenue |
| --- | ---: | --- |
| Code BIENVENUE20 (−20 %, permanent, 62 % des 1ʳᵉˢ cmd) | 55 800 € | aucune |
| Codes créateurs et affiliation (−15 %) | 7 200 € | une audience |
| Relance de panier abandonné (−10 %) | 6 000 € | une commande |
| Opérations ponctuelles (ventes privées, soldes) | 9 000 € | du volume |
| **Total** | **78 000 €** | **12,0 % du CA HT** |

Un code permanent affiché en page d'accueil n'est pas une promotion : c'est une baisse de
prix jamais décidée comme telle. Il coûte 55 800 € par mois et n'achète **rien** — ni une
adresse, ni un engagement, ni un délai (E03 § 5).

**Fuite 3 — le port offert sous le panier moyen.** Franco à **35,00 € TTC** pour un panier
catalogue de 52,00 € : **86,9 % des colis partent en port gratuit.**

```
15 000 colis × 6,60 € HT (transport 4,60 + préparation 3PL 2,00)      = 99 000 €
− participation client : 1 961 colis payants × 4,08 € HT (4,90 € TTC) =  8 001 €
Coût logistique net                                                   = 90 999 € ≈ 91 000 €
```

Un franco placé **sous** le panier moyen ne fait pas monter le panier : il offre le port
sur des commandes qui l'auraient payé.

**Fuite 4 — les retours.** 6,0 % du CA HT, 39 000 € par mois. Le SAV a classé les motifs :
**61 % sont des « pas la texture attendue » et des « mauvaise teinte »**. Ce ne sont pas des
retours produit, ce sont des retours de **fiche produit**.

**Et un cinquième poids, qui n'est pas une fuite.** Les frais fixes à 15,0 % du CA HT. Une
marque quatre fois plus petite tourne à 14,6 % (canoniques § 2.5, palier P2) et une marque
de la taille de LUMEN devrait viser 10,7 % (P3). On ne corrige pas ça en 90 jours ; on
l'empêche de grossir.

### 2.3 Ce que disent les chiffres, contre ce que croyait le dirigeant

| Les quatre fuites | Coût mensuel | En points de marge |
| --- | ---: | ---: |
| Publicité sous le seuil | 39 495 € | 6,08 pts |
| Remise permanente sans contrepartie | 42 250 € | 6,50 pts |
| Port offert (14,0 % contre 10,2 % atteignable) | 24 700 € | 3,80 pts |
| Retours (6,0 % contre 3,8 % atteignable) | 14 300 € | 2,20 pts |
| **Total** | **120 745 €** | **18,58 pts** |

**Les fuites valent 120 745 € par mois. La perte n'en vaut que 52 000 €.** LUMEN a
**68 745 € de bénéfice mensuel enfouis sous ses propres décisions commerciales**. Le
fondateur croyait devoir diluer ses frais fixes par du volume : il n'a pas un problème de
dilution, il a un problème de contribution unitaire. Sa première commande perd 4,51 €, donc
chaque client supplémentaire aggrave le compte.

> **À retenir :** avant de chercher du chiffre d'affaires, calcule ce que ta structure
> produirait si tu arrêtais simplement de saboter chaque commande. Chez LUMEN, la réponse
> est deux fois la perte.

---

## 3. Les options

**Option A — ne rien faire.** EBITDA −52 000 €/mois, autonomie 11 semaines. Cessation des
paiements en semaine 11 ou 12.

**Option B — relancer la croissance : +50 % de budget.** Le plan du fondateur. Le budget
marginal irait aux campagnes qu'on peut encore élargir — exactement le bloc mesuré à 1,40.

```
Dépense supplémentaire      = 267 150 × 50 %          = 133 575 € HT
CA TTC supplémentaire       = 133 575 × 1,40          = 187 005 € TTC
Contribution supplémentaire = 187 005 ÷ 1,20 × 48,1 % =  74 958 €
Effet sur l'EBITDA          = 74 958 − 133 575        = −58 617 €
```

| | M0 | Option B |
| --- | ---: | ---: |
| CA TTC | 780 000 € | **967 005 € (+24,0 %)** |
| Dépense publicitaire HT | 267 150 € | 400 725 € |
| MER | 2,92 | **2,41** — sous le seuil CM3 |
| EBITDA (% CA HT) | −52 000 € (−8,0 %) | **−110 617 € (−13,7 %)** |
| Consommation hebdomadaire | 12 000 € | 25 527 € |
| **Autonomie** | **11 semaines** | **5,2 semaines** |

Le chiffre d'affaires monte de 24 %, la trésorerie passe de onze à cinq semaines. **À MER
2,41, la marge brute ne couvre même plus la publicité.** C'est la définition opérationnelle
de « la croissance multiplie la perte ».

**Option C — réparer la structure, sans un euro de croissance.** Huit leviers, détaillés
ci-dessous. EBITDA à M3 : **+78 397 €/mois**.

**Option D — lever 800 000 € pour financer 15 mois de perte.** À 11 semaines de trésorerie,
aucun prêteur ne signe en moins de 10 semaines, et le prix serait un taux ou une dilution
de détresse. Surtout : **une levée qui ne corrige aucune fuite finance les fuites** —
120 745 € × 15 mois = 1 811 175 €, soit plus que la levée. D n'est jamais un substitut à C,
au mieux son accompagnement une fois C engagée.

### 3.1 Les huit leviers de l'option C

Chiffrage **séquentiel** : chaque levier est évalué dans l'ordre où il est exécuté, sur
l'état laissé par le précédent. L'ordre change la répartition, pas le total. Les points sont
des points de taux d'EBITDA sur le CA HT de la période. L'effort est en jours-homme.

| Rang gain/effort | Levier | Gain €/mois | Points | Délai | Risque | Effort | € par j·h | Exéc. |
| ---: | --- | ---: | ---: | --- | --- | ---: | ---: | ---: |
| 1 | Arrêt des campagnes sous le MER seuil (2,49) | 39 495 € | 5,7 | 3 j | moyen — perte de signal | 2 j | 19 748 € | 1 |
| 2 | Gel des recrutements, 2 outils redondants, fin de 2 missions freelance | 10 900 € | 2,0 | 0–30 j | moyen — tension d'équipe | 4 j | 2 725 € | 2 |
| 3 | Fin du code de bienvenue permanent → code à usage unique contre inscription | 20 683 € | 4,0 | immédiat | **élevé — conversion** | 8 j | 2 585 € | 3 |
| 4 | Franco de port relevé de 35 € à 59 € TTC | 6 604 € | 1,4 | immédiat | moyen — abandon de panier | 3 j | 2 201 € | 4 |
| 5 | Réactivation de la base dormante par courriel | 21 968 € | 3,2 | 14 j | faible — délivrabilité | 10 j | 2 197 € | 8 |
| 6 | Upsell post-achat en un clic | 13 153 € | 2,3 | 21 j | faible | 15 j | 877 € | 6 |
| 7 | Renégociation du contrat 3PL et du transporteur | 6 072 € | 1,2 | 45–60 j | faible — migration | 12 j | 506 € | 5 |
| 8 | Baisse du taux de retour par la fiche produit et le guide de choix | 11 522 € | 2,2 | 60–90 j | faible | 35 j | 329 € | 7 |
| | **Total** | **130 397 €** | **22,0** | | | **89 j** | | |

**Vérification.** Points : 5,7 + 2,0 + 4,0 + 1,4 + 3,2 + 2,3 + 1,2 + 2,2 = **22,0**, donc
−8,0 % + 22,0 = **+14,0 %**. Euros : 39 495 + 10 900 + 20 683 + 6 604 + 21 968 + 13 153 +
6 072 + 11 522 = **130 397 €**, et −52 000 + 130 397 = **+78 397 €**.

**Attention à la colonne des euros :** 22,0 % de 650 000 € HT font 143 000 €, pas 130 397 €.
L'écart de 12 603 € n'est pas une erreur — c'est la question 4.

**Deux natures de gain dans le levier 2.** L'arrêt de deux outils redondants (3 900 € nets,
après souscription d'un outil de cycle de vie à 1 500 €) et la fin de deux missions
freelance (7 000 €) sont des **économies constatées** : elles font les 10 900 €. Le gel des
deux CDI qu'elles préfiguraient — **10 500 € par mois chargés** — est un **coût évité** : il
n'améliore pas l'EBITDA constaté, il empêche sa dégradation programmée. Ne les additionne
jamais dans un compte de résultat.

---

## 4. La décision et l'exécution

Option C, dans l'ordre du cash : d'abord ce qui rend de la trésorerie en trois jours.

| Semaine | Ce qui est fait | Chiffre de contrôle |
| ---: | --- | --- |
| 1 | Diagnostic en une journée, gel de toute nouvelle dépense, test d'arrêt géographique sur 3 groupes de campagnes. | MER seuil publié : 2,49 / 3,63 |
| 2 | Verdict du test : 1,40. **Coupe de 90 000 €/mois.** Suppression de BIENVENUE20, remplacé par un −15 % à usage unique après inscription. Arrêt de 2 outils. | Budget pub : 267 150 → 177 150 € |
| 3 | Franco relevé à 59,00 € TTC. Première séquence de réactivation (6 courriels) sur 58 000 clients inactifs depuis plus de 6 mois. | Point bas de trésorerie : ≈ 126 000 € |
| 4 | Upsell post-achat en ligne (mini-format 20,00 € TTC). Appel d'offres 3PL et transporteur auprès de 4 prestataires. | Taux de prise upsell : 6,1 % |
| 5 | Fin des 2 missions freelance, gel des 2 CDI budgétés. La cascade du § 1 est montrée à toute l'équipe, sans filtre. | Frais fixes : 97 500 → 86 600 € |
| 6 | Refonte des 12 fiches qui concentrent 71 % des retours : macro de texture, nuancier sur trois carnations, quantité par application. | 12 fiches sur 40 |
| 7 | Guide de choix en 4 questions, placé avant l'ajout au panier. Réponses du 3PL reçues. | Taux de retour hebdo. : 5,4 % |
| 8 | Contrat 3PL signé : préparation 2,00 → 1,80 €, transport 4,60 → 4,15 € par colis. | −0,45 € par colis |
| 9 | Deuxième vague de réactivation, segmentée par ancienneté et produit. Séquence post-inscription réécrite. | 550 commandes réactivées / mois |
| 10 | Migration 3PL sur un week-end, cellule de crise 72 h. | 3 jours de retard, 0 perte |
| 11 | Fin de la refonte des 40 fiches. Guide de choix en test A/B sur 50 % du trafic. | Taux de retour : 4,3 % |
| 12 | Upsell étendu (seconde offre si la première est refusée). Nettoyage de la base courriel. | Taux de prise upsell : 8,8 % |
| 13 | Clôture, recalcul de la cascade, publication du nouveau MER seuil à toute l'équipe. | MER seuil EBITDA = 0 : 2,63 |

**Le tableau de suivi mensuel.** Tous les montants sont **HT** sauf la ligne CA TTC.

| | **M0** | **M1** | **M2** | **M3** |
| --- | ---: | ---: | ---: | ---: |
| Commandes | 15 000 | 12 625 | 11 950 | 12 150 |
| CA TTC | 780 000 € | 673 900 € | 655 100 € | 672 000 € |
| CA HT | 650 000 € | 561 583 € | 545 917 € | 560 000 € |
| Marge brute (CM2) | 312 650 € | 305 274 € | 323 758 € | 342 147 € |
| *en % du CA HT* | *48,1 %* | *54,4 %* | *59,3 %* | *61,1 %* |
| Dépense publicitaire | 267 150 € | 199 650 € | 177 150 € | 177 150 € |
| **MER** | **2,92** | **3,38** | **3,70** | **3,79** |
| *MER seuil EBITDA = 0* | *3,63* | *3,18* | *2,76* | *2,63* |
| CM3 | 45 500 € | 105 624 € | 146 608 € | 164 997 € |
| Frais fixes | 97 500 € | 93 600 € | 86 600 € | 86 600 € |
| **EBITDA** | **−52 000 €** | **+12 024 €** | **+60 008 €** | **+78 397 €** |
| *en % du CA HT* | *−8,0 %* | *+2,1 %* | *+11,0 %* | *+14,0 %* |
| Trésorerie fin de mois | 132 000 € | 154 024 € | 224 032 € | 308 429 € |

**La trésorerie ne monte pas seulement grâce à l'EBITDA.**

| | M1 | M2 | M3 | Cumul |
| --- | ---: | ---: | ---: | ---: |
| EBITDA | 12 024 € | 60 008 € | 78 397 € | 150 429 € |
| Libération de stock (baisse du volume) | +22 000 € | +14 000 € | +6 000 € | +42 000 € |
| Coûts ponctuels du plan (refonte, dev, migration) | −12 000 € | −4 000 € | 0 € | −16 000 € |
| **Variation de trésorerie** | **+22 024 €** | **+70 008 €** | **+84 397 €** | **+176 429 €** |

Les 42 000 € de stock sont un **encaissement de bilan, pas un résultat** : dès que le volume
remontera, le stock reconsommera du cash (E10).

---

## 5. Les résultats

| | M0 | M3 | Écart € | Écart en points |
| --- | ---: | ---: | ---: | ---: |
| CA TTC | 780 000 € | 672 000 € | −108 000 € | **−13,8 %** |
| Commandes | 15 000 | 12 150 | −2 850 | −19,0 % |
| Panier catalogue TTC | 52,00 € | 55,31 € | +3,31 € | +6,4 % |
| Panier encaissé TTC | 45,76 € | 52,36 € | +6,60 € | +14,4 % |
| Logistique | 14,0 % | 9,9 % | −35 691 € | **+4,1 pts** |
| Retours / SAV | 6,0 % | 3,8 % | −17 720 € | **+2,2 pts** |
| Remises | 12,0 % | 5,3 % | −48 176 € | **+6,7 pts** |
| **Marge brute (CM2)** | **48,1 %** | **61,1 %** | +29 497 € | **+13,0 pts** |
| Dépense publicitaire | 267 150 € | 177 150 € | −90 000 € | −33,7 % |
| MER / MER seuil EBITDA | 2,92 / 3,63 | 3,79 / 2,63 | | **de −19,5 % à +44,3 % du seuil** |
| Frais fixes | 97 500 € | 86 600 € | −10 900 € | |
| **EBITDA mensuel** | **−52 000 €** | **+78 397 €** | **+130 397 €** | **+22,0 pts** |
| **EBITDA % CA HT** | **−8,0 %** | **+14,0 %** | | |
| nCAC | 23,75 € | 23,16 € | −0,59 € | −2,5 % |
| **Marge à la 1ʳᵉ commande** | **−4,51 €** | **+1,08 €** | **+5,59 €** | |
| Trésorerie | 132 000 € | 308 429 € | +176 429 € | |

*COGS (18,0 %) et PSP (1,9 %) sont inchangés : aucun des huit leviers ne les touche.*

**La ligne à lire deux fois est le nCAC : il n'a quasiment pas bougé.** Aucun levier de ce
cas n'a rendu l'acquisition moins chère. Ce qui a changé, c'est ce que la première commande
rapporte : 19,24 € de contribution devenus 24,24 €. **LUMEN n'a pas mieux acheté ses
clients. Elle a arrêté de les revendre à perte.**

Sur 90 jours, l'EBITDA cumulé est de **+150 429 €** contre **−156 000 €** en cas d'inaction :
**306 429 € d'écart** en un trimestre, sans un euro de chiffre d'affaires supplémentaire.

---

## 6. Ce qui aurait pu mal tourner

**Le MER incrémental mesuré pouvait être faux.** Tout le levier 1 repose sur un test de deux
semaines. Le gain net vaut `90 000 − 90 000 × m ÷ 1,20 × 48,1 %` :

| MER incrémental réel *m* | 1,00 | 1,40 | 1,80 | 2,10 | **2,49** | 2,80 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Gain net mensuel | 53 925 € | **39 495 €** | 25 065 € | 14 243 € | **0 €** | −11 010 € |

Le point d'annulation tombe exactement sur le seuil de 2,49 — c'est la définition du seuil.
**La décision reste bonne avec 78 % d'erreur sur la mesure.** C'est ce qui autorise à couper
vite ; un levier qui s'annulerait à 1,50 aurait exigé quatre semaines de test que LUMEN
n'avait pas.

**La fin de la remise pouvait coûter plus cher.** Le modèle retient une baisse de 6 % de la
conversion des nouveaux visiteurs. À 12 %, le levier 3 tombe de 20 683 € à **5 941 €**. Il
reste positif — mais il faut le savoir avant, pas après.

**Les clients « remise » ont réagi.** 143 réclamations en trois semaines, dont 38 publiques.
Le code était réservé à la première commande : les plus virulents étaient donc ceux qui
ouvraient un compte neuf à chaque achat pour le réutiliser. **Ce segment achetait un prix,
pas un produit.** Le réachat de la base réelle n'a pas bougé de M0 à M3 : 3 750 commandes.

**L'équipe a résisté, et elle avait des arguments.** Le responsable acquisition a défendu son
budget avec un ROAS plateforme de 2,4 sur les campagnes coupées — un ROAS déclaratif contre
un MER mesuré par arrêt (E09). Deux personnes sont parties en semaine 6, le gel des CDI a
été vécu comme un renoncement. Ce qui a débloqué la situation en semaine 5 : montrer la
cascade et les onze semaines à tout le monde. **Un plan de redressement qui ne publie pas
ses chiffres passe pour une punition.**

**Le scénario dégradé, chiffré avant de commencer** — MER réel à 1,80, conversion en baisse
de 12 %, retours qui ne descendent qu'à 4,8 % :

| Scénario à M3 | CA TTC | CM2 | EBITDA | % CA HT |
| --- | ---: | ---: | ---: | ---: |
| Nominal | 672 000 € | 61,1 % | +78 397 € | **+14,0 %** |
| Dégradé | 601 200 € | 60,1 % | +37 319 € | **+7,5 %** |
| Dégradé aggravé (migration 3PL ratée, base courriel brûlée) | 592 500 € | 57,7 % | +21 048 € | **+4,3 %** |

**Le pire scénario reste 73 000 € par mois au-dessus de l'inaction.** Décider sous
incertitude, c'est comparer les planchers, pas les espérances.

**Ce qui reste ouvert.** Les 42 000 € de stock libérés sont non renouvelables. Les frais
fixes pèsent 15,5 % du CA HT à M3, plus qu'à M0, parce que le CA a baissé plus vite qu'eux.
Et un MER de 3,79 n'est pas une performance : c'est un sous-investissement délibéré, tenu
trois mois pour acheter de la sécurité.

---

## 7. Le mécanisme généralisable

> **La règle.** Quand la marge de contribution unitaire est négative, la croissance est un
> multiplicateur de perte. Tant que la première commande ne rapporte pas, chaque euro
> d'acquisition supplémentaire agrandit le trou proportionnellement au volume. **On répare
> la structure d'abord, on accélère ensuite. L'ordre n'est pas une préférence de style :
> c'est une contrainte arithmétique.**

Le test, dans cet ordre :

1. **Ma marge à la première commande est-elle positive ?** Sinon, aucune dépense
   d'acquisition supplémentaire n'est défendable, quelle que soit la LTV projetée.
2. **Mon MER réel est-il au-dessus de mon MER seuil EBITDA ?** Sinon, je ne pilote pas une
   entreprise, je pilote une vitesse de disparition.
3. **Alors seulement : où est mon CAC marginal ?**

Le fondateur attaquait la question 3 avec des réponses fausses aux questions 1 et 2. Ce
n'est pas de l'incompétence, c'est un ordre inversé — et c'est la forme la plus répandue de
l'échec en DTC.

**Pourquoi la croissance redevient une bonne idée à M3.** Le MER réel (3,79) est **44,3 %
au-dessus** du seuil EBITDA (2,63) : LUMEN peut redépenser jusqu'à 255 547 € HT par mois
avant de repasser sous l'équilibre. Réaccélération prudente sur M4–M6, en remettant
32 850 € sur les campagnes qui mesurent **2,60 de MER incrémental** — pas celles à 1,40 :

| | M0 | M3 | M6 simulé |
| --- | ---: | ---: | ---: |
| CA TTC | 780 000 € | 672 000 € | **757 410 €** |
| Dépense publicitaire HT | 267 150 € | 177 150 € | 210 000 € |
| MER | 2,92 | 3,79 | 3,61 |
| EBITDA (% CA HT) | −52 000 € (−8,0 %) | +78 397 € (+14,0 %) | **+88 679 € (+14,1 %)** |

Le chiffre d'affaires revient à 2,9 % de son niveau de départ **et la marge nette monte
encore**. La même dépense faite en M0, sur les mêmes campagnes marginales à 1,40, aurait
coûté 14 416 € par mois de perte supplémentaire.

**C'est le vrai sujet du cas.** Ce n'est pas « croissance ou marge », c'est un ordre
d'opérations : la croissance sur une structure réparée est un investissement, la même
croissance sur une structure percée est une fuite plus rapide. Voir
[E01](../modules/E01-arithmetique-de-la-marque.md) pour la contribution unitaire et
[E10](../modules/E10-cash-et-operations.md) pour le cash — c'est le cash qui te donne ou non
le droit de te tromper.

---

## 8. Questions

1. Recalcule les deux MER seuils de LUMEN à M0 à partir de la seule cascade du § 1, et dis
   de combien la marque est sous son seuil EBITDA.
2. Un groupe de campagnes pèse 42 000 € HT de budget mensuel, avec un MER incrémental
   mesuré de **2,10**. Faut-il le couper à M0 ? Et à M3 ? Justifie par le calcul.
3. Le fondateur veut réserver le code aux inscrits mais le remonter à **−20 %** au lieu de
   −15 %. Chiffre l'effet sur la remise mensuelle et sur la marge nette de M3 (taux de prise
   inchangé, 38 % des 7 650 premières commandes).
4. Un élève multiplie 22,0 % par 650 000 € HT et trouve 143 000 €, alors que le pont des
   huit leviers donne 130 397 €. Qui a raison ? D'où viennent les 12 603 € d'écart ?
5. À M3, à partir de quel MER incrémental un euro de publicité supplémentaire **détruit-il**
   de l'EBITDA ? Et à partir de quel MER fait-il **monter le taux** de marge nette ?
6. La trésorerie a gagné 176 429 € en 90 jours pour 150 429 € d'EBITDA cumulé. Explique
   l'écart et dis ce qui se passe au trimestre suivant si le chiffre d'affaires remonte.
7. Reprends l'option B. À partir de quel MER incrémental le +50 % de budget aurait-il été
   **neutre** sur l'EBITDA de M0 ? Que remarques-tu ?

---

## 9. Corrigé des questions

**1.** La marge brute vaut 312 650 € sur 650 000 € HT, soit 48,1 %.

```
MER seuil CM3 = 0        : 1,20 ÷ 0,481 = 2,4948 → 2,49
Publicité max (EBITDA=0) : 312 650 − 97 500 = 215 150 € HT
MER seuil EBITDA = 0     : 780 000 ÷ 215 150 = 3,6254 → 3,63
Écart au seuil           : 215 150 ÷ 267 150 − 1 = −19,5 %
```

Contrôle : 52 000 € de perte pour 52 000 € de dépense excédentaire (267 150 − 215 150). **La
perte est l'excès publicitaire, à l'euro près.**

**2.** Le critère de coupe d'une campagne est le seuil **CM3 = 0**, pas le seuil EBITDA :
une campagne au-dessus du premier contribue aux frais fixes, même si l'entreprise perd de
l'argent globalement.

```
À M0 — seuil = 1,20 ÷ 0,481 = 2,49. MER 2,10 < 2,49 → couper.
  Gain = 42 000 − (42 000 × 2,10 ÷ 1,20 × 48,1 %) = 42 000 − 35 354 = +6 647 €/mois
À M3 — contribution 60,6 %, seuil = 1,20 ÷ 0,606 = 1,98. MER 2,10 > 1,98 → garder.
  Couper coûterait : 42 000 − (42 000 × 2,10 ÷ 1,20 × 60,6 %) = 42 000 − 44 541 = −2 541 €/mois
```

**La même campagne, au même MER, se coupe à M0 et se garde à M3.** Le seuil n'est pas une
propriété de la campagne, c'est une propriété de ta structure de coûts : réparer 13 points
de marge brute a fait descendre le seuil de coupe de 2,49 à 1,98, et a rendu rentables des
campagnes qui ne l'étaient pas. C'est la deuxième raison, moins visible, de réparer avant
d'accélérer.

**3.**

```
Remise à −15 % : 7 650 × 38 % × 40,00 € HT × 15 % = 2 907 × 6,00 € = 17 442 €
Remise à −20 % : 7 650 × 38 % × 40,00 € HT × 20 % = 2 907 × 8,00 € = 23 256 €
Surcoût : 23 256 − 17 442 = 5 814 €
EBITDA M3 : 78 397 − 5 814 = 72 583 €  →  72 583 ÷ 560 000 = 12,96 % → 13,0 %
```

Cinq points de remise supplémentaires coûtent **1,0 point de marge nette**. Le rapport vaut
d'être mémorisé : sur cette structure, 1 point de remise consenti sur les commandes
concernées vaut environ 0,2 point de marge nette. Une remise n'est jamais « juste 5 % ».

**4.** Les deux ont raison, mais ne répondent pas à la même question. 22,0 points est un
**écart entre deux taux calculés sur deux dénominateurs différents** : −8,0 % porte sur
650 000 € HT, +14,0 % porte sur 560 000 € HT.

```
Si le CA HT était resté à 650 000 € : 650 000 × 14,0 % = 91 000 €
EBITDA réel de M3                   :                    78 397 €
Écart                               :                    12 603 €
Contrôle : 14,0 % × (650 000 − 560 000) = 14,0 % × 90 000 = 12 600 €
```

Les 12 603 € sont **la marge nette que LUMEN ne fait pas sur le chiffre d'affaires qu'elle a
volontairement abandonné**. Le pont en euros (130 397 €) est le chiffre à porter au compte
de résultat ; les 143 000 € sont une projection à volume constant qui n'a jamais eu lieu.
**Quand tu annonces un redressement en points, dis toujours sur quel chiffre d'affaires.**

**5.** Contribution marginale à M3 : 60,6 % du CA HT. Pour un euro de publicité
supplémentaire à MER incrémental *m* :

```
CA HT généré       = m ÷ 1,20
Contribution       = m ÷ 1,20 × 60,6 % = 0,505 m
Effet sur l'EBITDA = 0,505 m − 1

Destruction d'EBITDA   : 0,505 m − 1 < 0  →  m < 1,20 ÷ 0,606 = 1,98
Taux marginal ≥ 14,0 % : (0,505 m − 1) ÷ (m ÷ 1,20) ≥ 14,0 %  →  m ≥ 2,58
```

Trois zones : **sous 1,98**, la dépense détruit de l'EBITDA ; **entre 1,98 et 2,58**, elle
ajoute des euros mais **dilue le taux** ; **au-dessus de 2,58**, elle fait les deux. La
réaccélération du § 7 se fait à 2,60, juste au-dessus de la borne haute. C'est délibéré : on
ne rachète pas de la croissance qui abîme le taux qu'on vient de reconstruire.

**6.**

```
Variation de trésorerie 90 jours : +176 429 €
  dont EBITDA cumulé             : +150 429 €
  dont libération de stock (BFR) :  +42 000 €
  dont coûts ponctuels du plan   :  −16 000 €
Contrôle : 150 429 + 42 000 − 16 000 = 176 429 €
```

Les 42 000 € viennent du **bilan**, pas de l'exploitation : le volume ayant baissé de 19 %,
LUMEN a cessé de réapprovisionner au rythme ancien et a vidé du stock déjà payé. **C'est un
encaissement unique.** Au trimestre suivant, si le chiffre d'affaires remonte de 13 %, le
stock doit être reconstitué et le même mécanisme **consomme** de la trésorerie. Une marque
qui confond ce cash-là avec du résultat croit avoir 176 429 € de bénéfice trimestriel alors
qu'elle en a 150 429 €, et budgète sa réaccélération sur un chiffre faux (E10).

**7.**

```
Effet sur l'EBITDA = 133 575 × (m ÷ 1,20 × 48,1 % − 1) = 0
→ m ÷ 1,20 × 0,481 = 1  →  m = 1,20 ÷ 0,481 = 2,4948 → 2,49
```

C'est **exactement le MER seuil CM3 = 0** calculé à la question 1 — et ce n'est pas un
hasard : ce seuil *est*, par construction, le MER auquel un euro de publicité rend
exactement un euro de contribution. Le plan du fondateur supposait donc, sans l'avoir jamais
écrit, que ses campagnes marginales tourneraient à 2,49 alors que la mesure donnait 1,40.
**Tout plan de croissance contient une hypothèse de MER incrémental. Si tu ne l'écris pas,
tu l'as quand même faite.**

---

*Fin du cas C08. Suite : [C09 — Le piège du Black Friday, modélisé](C09-piege-du-black-friday.md).*
