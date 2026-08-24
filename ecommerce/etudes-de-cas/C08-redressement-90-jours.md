# Cas C08 — Redressement : de −8 % à +14 % de marge nette en 90 jours

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des
> ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.
> **Ce que tu dois en tirer :** quand la marge est négative, la croissance multiplie la
> perte — on répare la structure d'abord, on accélère ensuite.
> **Modules rattachés :** E01, E03, E06, E10, E13.

---

## 0. Conventions et origine des chiffres

**LUMEN** est une marque fictive de soin du visage, DTC, France et Belgique, quatre ans
d'existence, 14 ETP. Tous ses chiffres sont **modélisés** : ce cas ne cite aucun chiffre
canonique de NØRA, il en emprunte seulement les conventions.

- TVA **20 %**. Tout montant est explicitement **TTC** (prix client) ou **HT** (chiffre
  d'affaires comptable). `CA HT = CA TTC ÷ 1,20`.
- **La remise est un coût variable, pas une réduction de chiffre d'affaires**
  ([chiffres canoniques § 2.1](../donnees/chiffres-canoniques.md)). Le CA est donc la
  **valeur catalogue** des commandes expédiées, et la remise est une ligne de coût visible,
  avec un responsable. L'encaissement réel est donné séparément.
- **La logistique est modélisée en % du CA HT.** Le § 2 la redérive en euros par colis.
- `MER = CA TTC ÷ dépense publicitaire HT`. `CM1 = CA HT − COGS`.
  `CM2 = CM1 − logistique − PSP − retours − remises`. `CM3 = CM2 − publicité`.
  `EBITDA = CM3 − frais fixes`.
- L'**upsell post-achat** ne supporte ni logistique additionnelle (même colis) ni remise.
  C'est pour ça que son taux de contribution dépasse celui du reste de l'activité.

---

## 1. La situation

Jour 0. Le fondateur de LUMEN t'appelle avec une phrase : « on stagne, il faut relancer la
croissance ». Il a préparé un plan média à +50 % de budget. Voici ce que son propre
compte de résultat dit, une fois reconstruit ligne à ligne.

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

**Les indicateurs d'appoint, sans lesquels le tableau ci-dessus ne se lit pas.**

| Indicateur | M0 | Lecture |
| --- | ---: | --- |
| Commandes premières / réachat | 11 250 / 3 750 | 25 % des commandes en réachat |
| Panier catalogue 1ʳᵉ commande / réachat | 48,00 € / 64,00 € TTC | l'écart est le symptôme |
| Panier réellement encaissé | 45,76 € TTC | 780 000 − 93 600 € TTC de remise, ÷ 15 000 |
| nCAC (coût d'acquisition d'un nouveau client) | 23,75 € | 267 150 € ÷ 11 250 |
| Contribution de la 1ʳᵉ commande | 19,24 € HT | 40,00 € HT × 48,1 % |
| **Marge à la 1ʳᵉ commande** | **−4,51 €** | chaque nouveau client démarre en dette |
| CA HT annuel par ETP | 557 143 € | 7,8 M€ ÷ 14 |
| Trésorerie | 132 000 € | |
| Consommation hebdomadaire | 12 000 € | 52 000 € × 12 ÷ 52 |
| **Autonomie** | **11 semaines** | 132 000 ÷ 12 000 |

Onze semaines. Ce n'est pas un problème de croissance, c'est un compte à rebours.

---

## 2. Le diagnostic

Il tient en une journée. Pas une semaine, pas un audit : une journée, parce que les quatre
fuites sont toutes dans le tableau du § 1 et qu'aucune ne demande de donnée nouvelle.

### 2.1 Le MER seuil de LUMEN — le chiffre qu'il n'avait jamais calculé

```
MER seuil (CM3 = 0)     = 1,20 ÷ CM2 %        = 1,20 ÷ 0,481 = 2,49
Publicité maximale (EBITDA = 0) = CM2 − fixes = 312 650 − 97 500 = 215 150 € HT
MER seuil (EBITDA = 0)  = 780 000 ÷ 215 150   = 3,63
```

| Seuil | Valeur | Ce qu'il signifie |
| --- | ---: | --- |
| MER réel | **2,92** | ce que fait la marque |
| MER seuil CM3 = 0 | **2,49** | en dessous, la marge brute ne paie même plus la publicité |
| MER seuil EBITDA = 0 | **3,63** | en dessous, l'entreprise perd de l'argent |
| Écart au seuil EBITDA | **−19,5 %** | 215 150 ÷ 267 150 − 1 |

Le fondateur regardait 2,92 et le trouvait « correct » — il l'avait lu quelque part. **2,92
n'est ni bon ni mauvais dans l'absolu : il est bon ou mauvais par rapport à 3,63.** LUMEN
dépense 52 000 € HT de plus par mois que ce que sa structure de coûts autorise. C'est,
au centime près, sa perte.

### 2.2 Les quatre fuites

**Fuite 1 — de la publicité sous le seuil.** Un test d'arrêt géographique de deux semaines
(protocole du cas [C06](C06-test-incrementalite.md)) isole trois groupes de campagnes
pesant **90 000 € HT par mois**, dont le **MER incrémental mesuré est de 1,40** — contre
un seuil de 2,49. Ce bloc produit 126 000 € TTC de chiffre d'affaires, soit 105 000 € HT
et 50 505 € de contribution, pour 90 000 € dépensés.

```
Destruction mensuelle = 90 000 − (90 000 × 1,40 ÷ 1,20 × 48,1 %) = 90 000 − 50 505 = 39 495 €
```

Le budget restant (177 150 € HT) porte les 654 000 € TTC restants, soit un MER de **3,69** :
au-dessus du seuil de 3,63. **La moitié utile du compte publicitaire est déjà rentable ;
c'est l'autre tiers qui tue l'entreprise.**

**Fuite 2 — la remise permanente.** 78 000 € HT par mois, 12,0 % du CA HT.

| Poste de remise | M0 | Nature |
| --- | ---: | --- |
| Code BIENVENUE20 (−20 %, permanent, 62 % des 1ʳᵉˢ commandes) | 55 800 € | sans contrepartie |
| Codes créateurs et affiliation (−15 %) | 7 200 € | contre une audience |
| Relance de panier abandonné (−10 %) | 6 000 € | contre une commande |
| Opérations ponctuelles (ventes privées, soldes) | 9 000 € | contre du volume |
| **Total** | **78 000 €** | **12,0 % du CA HT** |

Un code permanent affiché sur la page d'accueil n'est pas une promotion : c'est une baisse
de prix qui n'a jamais été décidée comme telle. Il coûte 55 800 € par mois et n'achète
**rien** — ni une adresse, ni un engagement, ni un délai. C'est le poste le plus cher du
tableau après la publicité, et le seul qui ne demande ni fournisseur ni investissement pour
être corrigé (voir E03 § 5).

**Fuite 3 — le port offert sous le panier moyen.** Franco de port à **35,00 € TTC** pour un
panier catalogue de 52,00 € TTC : **86,9 % des colis partent en port gratuit.**

```
15 000 colis × 6,60 € HT (transport 4,60 + préparation 3PL 2,00)      = 99 000 €
− participation client : 1 961 colis payants × 4,08 € HT (4,90 € TTC) =  8 001 €
Coût logistique net                                                   = 90 999 € ≈ 91 000 €
```

Un seuil de franco placé **sous** le panier moyen ne fait pas monter le panier : il offre
le port sur des commandes qui l'auraient payé.

**Fuite 4 — les retours.** 6,0 % du CA HT, 39 000 € par mois. Le SAV a classé les motifs :
**61 % sont des « pas la texture attendue » et des « mauvaise teinte »**. Ce ne sont pas des
retours produit, ce sont des retours de **fiche produit** : elle promet une chose, le flacon
en livre une autre.

**Et un cinquième poids, qui n'est pas une fuite.** Les frais fixes à 15,0 % du CA HT. Une
marque quatre fois plus petite tourne à 14,6 % ([chiffres canoniques § 2.5](../donnees/chiffres-canoniques.md), palier P2)
et une marque de la taille de LUMEN devrait viser 10,7 % (palier P3). Ce n'est pas une
fuite, c'est une structure trop lourde pour son chiffre d'affaires. On ne la corrige pas en
90 jours ; on l'empêche de grossir.

### 2.3 Ce que disent les chiffres, contre ce que croyait le dirigeant

| Les quatre fuites | Coût mensuel | En points de marge |
| --- | ---: | ---: |
| Publicité sous le seuil | 39 495 € | 6,08 pts |
| Remise permanente sans contrepartie | 42 250 € | 6,50 pts |
| Port offert (14,0 % contre 10,2 % atteignable) | 24 700 € | 3,80 pts |
| Retours (6,0 % contre 3,8 % atteignable) | 14 300 € | 2,20 pts |
| **Total** | **120 745 €** | **18,58 pts** |

**Les fuites valent 120 745 € par mois. La perte n'en vaut que 52 000 €.** LUMEN n'a pas un
problème de chiffre d'affaires : elle a **68 745 € de bénéfice mensuel enfouis sous ses
propres décisions commerciales**. Le fondateur croyait devoir diluer ses frais fixes par
plus de volume. Il n'a pas de problème de dilution : il a un problème de contribution
unitaire — sa première commande perd 4,51 €, donc chaque nouveau client aggrave le compte.

> **À retenir :** avant de chercher du chiffre d'affaires, calcule ce que ta structure
> actuelle produirait si tu arrêtais simplement de saboter chaque commande. Chez LUMEN,
> la réponse est deux fois la perte.

---

## 3. Les options

Quatre. Chacune chiffrée sur l'EBITDA mensuel, à structure de coûts M0 sauf mention.

**Option A — ne rien faire et attendre que le marché se retourne.** EBITDA −52 000 €/mois,
autonomie 11 semaines. Cessation des paiements en semaine 11 ou 12. Rien à ajouter.

**Option B — relancer la croissance : +50 % de budget publicitaire.** C'est le plan du
fondateur. Le budget marginal irait aux campagnes qu'on peut encore élargir, c'est-à-dire
exactement le bloc mesuré à **MER incrémental 1,40**.

```
Dépense supplémentaire         = 267 150 × 50 %                = 133 575 € HT
CA TTC supplémentaire          = 133 575 × 1,40                = 187 005 € TTC
Contribution supplémentaire    = 187 005 ÷ 1,20 × 48,1 %       =  74 958 €
Effet sur l'EBITDA             = 74 958 − 133 575              = −58 617 €
```

| | M0 | Option B |
| --- | ---: | ---: |
| CA TTC | 780 000 € | **967 005 € (+24,0 %)** |
| Dépense publicitaire HT | 267 150 € | 400 725 € |
| MER | 2,92 | **2,41** — sous le seuil CM3 |
| EBITDA | −52 000 € | **−110 617 €** |
| EBITDA % CA HT | −8,0 % | −13,7 % |
| Consommation hebdomadaire | 12 000 € | 25 527 € |
| **Autonomie** | **11 semaines** | **5,2 semaines** |

Le chiffre d'affaires monte de 24 %, la trésorerie passe de onze à cinq semaines. **À MER
2,41, LUMEN tombe sous son seuil de CM3 : la marge brute ne couvre plus la publicité,
avant même qu'on parle de salaires.** C'est la définition opérationnelle de « la croissance
multiplie la perte ».

**Option C — réparer la structure, sans un euro de croissance.** Huit leviers, aucun ne
demande de chiffre d'affaires supplémentaire. Détaillée ci-dessous.

**Option D — lever 800 000 € pour financer 15 mois de perte.** Le coût d'une levée à 11
semaines de trésorerie est un taux ou une dilution de détresse, et aucun prêteur ne signe
en moins de 10 semaines. Surtout : **une levée qui ne corrige aucune fuite finance les
fuites.** 120 745 € × 15 mois = 1 811 175 €. L'argent levé serait consommé par les quatre
fuites avant d'avoir servi à quoi que ce soit. L'option D n'est jamais un substitut à
l'option C — au mieux son accompagnement, une fois C engagée.

### 3.1 Les huit leviers de l'option C

Chiffrage **séquentiel** : chaque levier est évalué dans l'ordre où il est exécuté, sur
l'état de l'entreprise laissé par le précédent. L'ordre change la répartition entre
leviers ; il ne change pas le total. Les points sont des **points de taux d'EBITDA sur le
CA HT de la période**. L'effort est en jours-homme.

| Rang gain/effort | Levier | Gain €/mois | Points | Délai | Risque | Effort | € par j·h | Ordre d'exécution |
| ---: | --- | ---: | ---: | --- | --- | ---: | ---: | ---: |
| 1 | Arrêt des campagnes sous le MER seuil (2,49) | 39 495 € | 5,7 | 3 j | moyen — perte de signal, réapprentissage | 2 j | 19 748 € | 1 |
| 2 | Gel des recrutements, 2 outils redondants, fin de 2 missions freelance | 10 900 € | 2,0 | 0–30 j | moyen — tension d'équipe | 4 j | 2 725 € | 2 |
| 3 | Fin du code de bienvenue permanent, remplacé par un code à usage unique contre inscription | 20 683 € | 4,0 | immédiat | **élevé — conversion** | 8 j | 2 585 € | 3 |
| 4 | Franco de port relevé de 35 € à 59 € TTC | 6 604 € | 1,4 | immédiat | moyen — abandon de panier | 3 j | 2 201 € | 4 |
| 5 | Réactivation de la base dormante par courriel | 21 968 € | 3,2 | 14 j | faible — fatigue de base, délivrabilité | 10 j | 2 197 € | 8 |
| 6 | Upsell post-achat en un clic | 13 153 € | 2,3 | 21 j | faible | 15 j | 877 € | 6 |
| 7 | Renégociation du contrat 3PL et du transporteur | 6 072 € | 1,2 | 45–60 j | faible — risque de migration | 12 j | 506 € | 5 |
| 8 | Baisse du taux de retour par la fiche produit et le guide de choix | 11 522 € | 2,2 | 60–90 j | faible | 35 j | 329 € | 7 |
| | **Total** | **130 397 €** | **22,0** | | | **89 j** | | |

**Vérification de l'addition.** Points : 5,7 + 2,0 + 4,0 + 1,4 + 3,2 + 2,3 + 1,2 + 2,2 =
**22,0**. Marge nette : −8,0 % + 22,0 = **+14,0 %**. Euros :
39 495 + 10 900 + 20 683 + 6 604 + 21 968 + 13 153 + 6 072 + 11 522 = **130 397 €**, et
−52 000 + 130 397 = **+78 397 €** d'EBITDA mensuel.

**Attention à la colonne des euros.** 22,0 % de 650 000 € HT font 143 000 €, pas 130 397 €.
L'écart de 12 603 € n'est pas une erreur : le chiffre d'affaires a reculé, donc le
dénominateur du taux final n'est plus celui du taux de départ. C'est la question 4.

**Deux natures de gain à ne pas confondre dans le levier 2.** L'arrêt de deux outils
redondants (3 900 € nets par mois, après souscription d'un outil de cycle de vie à 1 500 €)
et la fin de deux missions freelance (7 000 €) sont des **économies constatées** : elles
entrent dans les 10 900 €. Le gel des deux CDI qu'elles préfiguraient — **10 500 € par mois
chargés** — est un **coût évité** : il n'améliore pas l'EBITDA constaté, il empêche sa
dégradation programmée. Ne l'additionne jamais aux deux autres dans un compte de résultat.

---

## 4. La décision et l'exécution

Option C, exécutée dans l'ordre du cash : d'abord ce qui rend de la trésorerie en trois
jours, ensuite ce qui en rend en trois mois.

### 4.1 Treize semaines

| Semaine | Ce qui est fait | Chiffre de contrôle |
| ---: | --- | --- |
| 1 | Diagnostic en une journée. Gel de toute nouvelle dépense. Lancement du test d'arrêt géographique sur les 3 groupes de campagnes suspects. | MER seuil publié : 2,49 / 3,63 |
| 2 | Le test rend son verdict : MER incrémental 1,40. **Coupe de 90 000 €/mois de budget.** Suppression du code BIENVENUE20, remplacé par un code −15 % à usage unique envoyé après inscription. Arrêt de 2 outils. | Budget publicitaire : 267 150 → 177 150 € |
| 3 | Franco relevé à 59,00 € TTC. Première séquence de réactivation (6 courriels) sur 58 000 clients sans commande depuis plus de 6 mois. | Trésorerie au point bas : ≈ 126 000 € |
| 4 | Upsell post-achat en ligne (mini-format 20,00 € TTC en un clic). Appel d'offres 3PL et transporteur lancé auprès de 4 prestataires. | Taux de prise upsell : 6,1 % |
| 5 | Fin des 2 missions freelance. Les 2 CDI budgétés sont gelés. Réunion d'équipe : les chiffres du § 1 sont montrés à tout le monde, sans filtre. | Frais fixes : 97 500 → 86 600 € |
| 6 | Refonte des 12 fiches produit qui concentrent 71 % des retours : macro de texture, nuancier photographié sur trois carnations, quantité réelle par application. | 12 fiches sur 40 |
| 7 | Guide de choix interactif en 4 questions, placé avant l'ajout au panier. Réponses du 3PL reçues. | Taux de retour hebdomadaire : 5,4 % |
| 8 | Contrat 3PL signé : préparation 2,00 → 1,80 €, transport 4,60 → 4,15 € par colis. Migration planifiée. | −0,45 € par colis |
| 9 | Deuxième vague de réactivation, segmentée par ancienneté et produit acheté. Séquence de bienvenue post-inscription réécrite. | 550 commandes réactivées / mois |
| 10 | Migration 3PL exécutée sur un week-end. Cellule de crise pendant 72 h. | 3 jours de retard d'expédition, 0 perte |
| 11 | Fin de la refonte des 40 fiches. Le guide de choix passe en test A/B sur 50 % du trafic. | Taux de retour : 4,3 % |
| 12 | Upsell étendu : deuxième offre proposée si la première est refusée. Nettoyage de la base courriel (désinscriptions inactives). | Taux de prise upsell : 8,8 % |
| 13 | Clôture. Recalcul de la cascade complète. Publication du nouveau MER seuil à toute l'équipe. | MER seuil EBITDA = 0 : 2,63 |

### 4.2 Le tableau de suivi mensuel

Tous les montants sont **HT** sauf la ligne CA TTC.

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

**La trésorerie ne monte pas seulement grâce à l'EBITDA.** Décomposition :

| | M1 | M2 | M3 | Cumul |
| --- | ---: | ---: | ---: | ---: |
| EBITDA | 12 024 € | 60 008 € | 78 397 € | 150 429 € |
| Libération de stock (baisse du volume) | +22 000 € | +14 000 € | +6 000 € | +42 000 € |
| Coûts ponctuels du plan (refonte, dev, migration) | −12 000 € | −4 000 € | 0 € | −16 000 € |
| **Variation de trésorerie** | **+22 024 €** | **+70 008 €** | **+84 397 €** | **+176 429 €** |

Les 42 000 € de stock sont un **encaissement de bilan, pas un résultat**. Ils ne se
reproduiront pas : dès que le volume remontera, le stock reconsommera du cash (E10).

---

## 5. Les résultats

| | M0 | M3 | Écart € | Écart en points |
| --- | ---: | ---: | ---: | ---: |
| CA TTC | 780 000 € | 672 000 € | −108 000 € | **−13,8 %** |
| Commandes | 15 000 | 12 150 | −2 850 | −19,0 % |
| Panier catalogue TTC | 52,00 € | 55,31 € | +3,31 € | +6,4 % |
| Panier encaissé TTC | 45,76 € | 52,36 € | +6,60 € | +14,4 % |
| COGS | 18,0 % | 18,0 % | — | 0,0 pt |
| Logistique | 14,0 % | 9,9 % | −20 691 € | **+4,1 pts** |
| PSP | 1,9 % | 1,9 % | — | 0,0 pt |
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
| Autonomie | 11 semaines | génération de cash | | |

**La ligne à lire deux fois est le nCAC : il n'a quasiment pas bougé.** 23,75 € contre
23,16 €. Aucun levier de ce cas n'a rendu l'acquisition moins chère. Ce qui a changé,
c'est ce que la première commande rapporte : 19,24 € de contribution devenus 24,24 €.
**LUMEN n'a pas mieux acheté ses clients. Elle a arrêté de les revendre à perte.**

Sur 90 jours, l'EBITDA cumulé est de **+150 429 €** contre **−156 000 €** si rien n'avait
été fait : un écart de **306 429 €** en un trimestre, sans un euro de chiffre d'affaires
supplémentaire.

---

## 6. Ce qui aurait pu mal tourner

**Le MER incrémental mesuré pouvait être faux.** Tout le levier 1 repose sur un test de
deux semaines. Le gain net vaut `90 000 − 90 000 × m ÷ 1,20 × 48,1 %` :

| MER incrémental réel *m* | 1,00 | 1,40 | 1,80 | 2,10 | **2,49** | 2,80 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Gain net mensuel | 53 925 € | **39 495 €** | 25 065 € | 14 243 € | **0 €** | −11 010 € |

Le point d'annulation tombe exactement sur le MER seuil de 2,49 — ce n'est pas une
coïncidence, c'est la définition du seuil. **La décision reste bonne pour tout *m* inférieur
à 2,49, et elle est bonne avec une marge d'erreur de 78 % sur la mesure.** C'est ce qui
autorise à couper vite. Un levier dont la valeur s'annule à 1,50 aurait exigé quatre
semaines de test — que LUMEN n'avait pas.

**La fin de la remise pouvait coûter beaucoup plus cher.** Le modèle retient une baisse de
6 % de la conversion des nouveaux visiteurs. À 12 %, le levier 3 tombe de 20 683 € à
**5 941 €**. Il reste positif — mais il faut le savoir avant, pas après.

**Les clients « remise » ont réagi, et ils l'ont dit.** 143 réclamations en trois semaines,
dont 38 sur les réseaux. La lecture juste : le code de bienvenue était réservé à la
première commande, donc les clients qui se plaignaient le plus fort étaient ceux qui
ouvraient un nouveau compte à chaque achat pour le réutiliser. **Ce segment achetait un prix,
pas un produit.** Le réachat de la base réelle n'a pas bougé de M0 à M3 : 3 750 commandes.

**L'équipe a résisté, et elle avait des arguments.** Le responsable acquisition a défendu
son budget avec un ROAS plateforme de 2,4 sur les campagnes coupées — un ROAS déclaratif
contre un MER mesuré par arrêt (E09). Deux personnes sont parties en semaine 6. Le gel des
CDI a été vécu comme un renoncement. Ce qui a débloqué la situation, semaine 5 : montrer à
toute l'équipe la cascade du § 1 et les onze semaines. **Un plan de redressement qui ne
publie pas ses chiffres passe pour une punition.**

**Le scénario dégradé, chiffré avant de commencer.** MER incrémental réel à 1,80, conversion
en baisse de 12 %, retours qui ne descendent qu'à 4,8 % au lieu de 3,8 % :

| Scénario à M3 | CA TTC | CM2 | EBITDA | % CA HT |
| --- | ---: | ---: | ---: | ---: |
| Nominal | 672 000 € | 61,1 % | +78 397 € | **+14,0 %** |
| Dégradé | 601 200 € | 60,1 % | +37 319 € | **+7,5 %** |
| Dégradé aggravé (migration 3PL ratée, base courriel brûlée) | 592 500 € | 57,7 % | +21 048 € | **+4,3 %** |

**Le pire scénario du plan de réparation reste 73 000 € par mois au-dessus de l'option
« ne rien faire ».** C'est ce que veut dire décider sous incertitude : on ne compare pas
l'espérance, on compare les planchers.

**Les risques réels restants.** La libération de 42 000 € de stock est non renouvelable. Les
frais fixes à 15,5 % du CA HT sont plus lourds qu'à M0 en pourcentage, parce que le CA a
baissé plus vite qu'eux — c'est le prochain sujet. Et un MER de 3,79 n'est pas une
performance : c'est un sous-investissement délibéré en acquisition, tenu trois mois pour
acheter de la sécurité.

---

## 7. Le mécanisme généralisable

> **La règle.** Quand la marge de contribution unitaire est négative, la croissance est un
> multiplicateur de perte. Tant que la première commande ne rapporte pas, chaque euro
> d'acquisition supplémentaire agrandit le trou proportionnellement au volume. **On répare
> la structure d'abord, on accélère ensuite. L'ordre n'est pas une préférence de style :
> c'est une contrainte arithmétique.**

Le test, en trois questions, dans cet ordre :

1. **Ma marge à la première commande est-elle positive ?** Si non, aucune dépense
   d'acquisition supplémentaire n'est défendable, quelle que soit la LTV projetée.
2. **Mon MER réel est-il au-dessus de mon MER seuil EBITDA ?** Si non, je ne pilote pas
   une entreprise, je pilote une vitesse de disparition.
3. **Alors seulement : où est mon CAC marginal ?**

Le fondateur de LUMEN attaquait la question 3 avec des réponses fausses aux questions 1
et 2. Ce n'est pas de l'incompétence, c'est un ordre inversé — et c'est la forme la plus
répandue de l'échec en DTC.

**Pourquoi la croissance redevient une bonne idée à M3, et pas avant.** À M3, le MER réel
(3,79) est **44,3 % au-dessus** du MER seuil EBITDA (2,63). Cet écart est du budget
disponible : LUMEN peut redépenser jusqu'à 255 547 € HT par mois avant de repasser sous
l'équilibre. Simulation d'une réaccélération prudente sur M4–M6, en remettant 32 850 € de
budget sur les campagnes qui mesurent **2,60 de MER incrémental** — pas celles à 1,40 :

| | M0 | M3 | M6 simulé |
| --- | ---: | ---: | ---: |
| CA TTC | 780 000 € | 672 000 € | **757 410 €** |
| Dépense publicitaire HT | 267 150 € | 177 150 € | 210 000 € |
| MER | 2,92 | 3,79 | 3,61 |
| EBITDA | −52 000 € | +78 397 € | **+88 679 €** |
| EBITDA % CA HT | −8,0 % | +14,0 % | **+14,1 %** |

Le chiffre d'affaires revient à 2,9 % de son niveau de départ **et la marge nette monte
encore**. La même dépense faite en M0, sur les mêmes campagnes marginales à 1,40, aurait
coûté 14 416 € par mois de perte supplémentaire.

**C'est le vrai sujet du cas.** Ce n'est pas « croissance ou marge » — c'est un ordre
d'opérations. La croissance sur une structure réparée est un investissement ; la même
croissance sur une structure percée est une fuite plus rapide. Renvoi :
[E01](../modules/E01-arithmetique-de-la-marque.md) pour l'arithmétique de la contribution
unitaire, [E10](../modules/E10-cash-et-operations.md) pour le cash et le BFR — c'est le cash
qui te donne ou non le droit de te tromper.

---

## 8. Questions

1. Recalcule les deux MER seuils de LUMEN à M0 à partir de la seule cascade du § 1, et
   dis de combien la marque est sous son seuil EBITDA.
2. Un groupe de campagnes pèse 42 000 € HT de budget mensuel et un test d'arrêt lui
   attribue un MER incrémental de **2,10**. Faut-il le couper à M0 ? Faut-il le couper à
   M3 ? Justifie par le calcul.
3. Le fondateur veut réserver le code aux inscrits mais le remonter à **−20 %** au lieu de
   −15 %. Chiffre l'effet sur la remise mensuelle et sur la marge nette de M3 (taux de
   prise inchangé, 38 % des 7 650 premières commandes).
4. Un élève multiplie 22,0 % par 650 000 € HT et trouve 143 000 €, alors que le pont des
   huit leviers donne 130 397 €. Qui a raison ? D'où viennent les 12 603 € d'écart ?
5. À M3, à partir de quel MER incrémental un euro de publicité supplémentaire
   **détruit-il** de l'EBITDA ? Et à partir de quel MER incrémental fait-il **monter le
   taux de marge nette** au-dessus de 14,0 % ?
6. La trésorerie a gagné 176 429 € en 90 jours pour 150 429 € d'EBITDA cumulé. Explique
   l'écart et dis ce qui se passe au trimestre suivant si le chiffre d'affaires remonte.
7. Reprends l'option B. À partir de quel MER incrémental le +50 % de budget aurait-il été
   **neutre** sur l'EBITDA de M0 ? Que remarques-tu ?

---

## 9. Corrigé des questions

**1.** La marge brute vaut 312 650 € sur 650 000 € HT, soit 48,1 %.

```
MER seuil CM3 = 0      : 1,20 ÷ 0,481 = 2,4948 → 2,49
Publicité max (EBITDA=0) : 312 650 − 97 500 = 215 150 € HT
MER seuil EBITDA = 0   : 780 000 ÷ 215 150 = 3,6254 → 3,63
Écart au seuil         : 215 150 ÷ 267 150 − 1 = −19,5 %
```

LUMEN dépense **19,5 % de plus** que ce que sa structure autorise. Contrôle : 52 000 €
de perte pour 52 000 € de dépense excédentaire (267 150 − 215 150). La perte **est**
l'excès publicitaire, à l'euro près.

**2.** Le critère de coupe d'une campagne est le seuil **CM3 = 0**, pas le seuil EBITDA :
une campagne au-dessus du premier contribue aux frais fixes même si l'entreprise perd de
l'argent globalement.

```
À M0 — seuil = 1,20 ÷ 0,481 = 2,49. MER 2,10 < 2,49 → couper.
  Gain = 42 000 − (42 000 × 2,10 ÷ 1,20 × 48,1 %) = 42 000 − 35 354 = +6 647 €/mois

À M3 — contribution 60,6 %, seuil = 1,20 ÷ 0,606 = 1,98. MER 2,10 > 1,98 → garder.
  Couper coûterait : 42 000 − (42 000 × 2,10 ÷ 1,20 × 60,6 %) = 42 000 − 44 541 = −2 541 €/mois
```

**La même campagne, au même MER, se coupe à M0 et se garde à M3.** Le seuil n'est pas une
propriété de la campagne, c'est une propriété de ta structure de coûts. Réparer la marge
brute de 13 points a fait descendre le seuil de coupe de 2,49 à 1,98 — et a rendu rentables
des campagnes qui ne l'étaient pas. C'est la deuxième raison, moins visible, pour laquelle
on répare avant d'accélérer.

**3.**

```
Remise à −15 % : 7 650 × 38 % × 40,00 € HT × 15 % = 2 907 × 6,00 € = 17 442 €
Remise à −20 % : 7 650 × 38 % × 40,00 € HT × 20 % = 2 907 × 8,00 € = 23 256 €
Surcoût mensuel : 23 256 − 17 442 = 5 814 €
EBITDA M3 : 78 397 − 5 814 = 72 583 €  →  72 583 ÷ 560 000 = 12,96 % → 13,0 %
```

Cinq points de remise supplémentaires coûtent **1,0 point de marge nette**. Le rapport est
brutal et vaut d'être mémorisé : sur cette structure, **1 point de remise consenti sur les
commandes concernées ≈ 0,2 point de marge nette**. Une remise n'est jamais « juste 5 % ».

**4.** Les deux ont raison, mais ils ne répondent pas à la même question. 22,0 points est
un **écart entre deux taux calculés sur deux dénominateurs différents** : −8,0 % porte sur
650 000 € HT, +14,0 % porte sur 560 000 € HT.

```
Si le CA HT était resté à 650 000 € : 650 000 × 14,0 % = 91 000 €
EBITDA réel de M3                   :                    78 397 €
Écart                               :                    12 603 €
Contrôle : 14,0 % × (650 000 − 560 000) = 14,0 % × 90 000 = 12 600 €
```

Les 12 603 € sont **la marge nette que LUMEN ne fait pas sur le chiffre d'affaires qu'elle
a volontairement abandonné**. Le pont en euros (130 397 €) est le chiffre à porter au
compte de résultat ; les 143 000 € sont une projection à volume constant, qui n'a jamais eu
lieu. **Quand tu annonces un redressement en points, dis toujours sur quel chiffre
d'affaires.**

**5.** Contribution marginale à M3 : 60,6 % du CA HT. Pour un euro de publicité
supplémentaire à MER incrémental *m* :

```
CA HT généré        = m ÷ 1,20
Contribution        = m ÷ 1,20 × 60,6 % = 0,505 m
Effet sur l'EBITDA  = 0,505 m − 1

Destruction d'EBITDA : 0,505 m − 1 < 0  →  m < 1,20 ÷ 0,606 = 1,98
Taux marginal ≥ 14,0 % : (0,505 m − 1) ÷ (m ÷ 1,20) ≥ 14,0 %  →  m ≥ 2,58
```

Trois zones : **sous 1,98**, la dépense détruit de l'EBITDA. **Entre 1,98 et 2,58**, elle
ajoute des euros d'EBITDA mais **dilue le taux** de marge nette. **Au-dessus de 2,58**, elle
fait les deux. La réaccélération du § 7 se fait à 2,60 : juste au-dessus de la borne haute.
C'est délibéré — on ne rachète pas de la croissance qui abîme le taux qu'on vient de
reconstruire.

**6.**

```
Variation de trésorerie 90 jours : +176 429 €
  dont EBITDA cumulé              : +150 429 €
  dont libération de stock (BFR)  :  +42 000 €
  dont coûts ponctuels du plan    :  −16 000 €
Contrôle : 150 429 + 42 000 − 16 000 = 176 429 €
```

Les 42 000 € viennent du **bilan**, pas de l'exploitation : le volume de commandes ayant
baissé de 19 %, LUMEN a cessé de réapprovisionner au rythme ancien et a vidé du stock déjà
payé. **C'est un encaissement unique.** Au trimestre suivant, si le chiffre d'affaires
remonte de 13 %, le stock doit être reconstitué : le même mécanisme joue en sens inverse et
**consomme** de la trésorerie. Une marque qui confond ce cash-là avec du résultat croit
avoir 176 429 € de bénéfice trimestriel alors qu'elle en a 150 429 € — et budgète sa
réaccélération sur un chiffre faux. Voir E10.

**7.**

```
Effet sur l'EBITDA = 133 575 × (m ÷ 1,20 × 48,1 % − 1) = 0
→ m ÷ 1,20 × 0,481 = 1
→ m = 1,20 ÷ 0,481 = 2,4948 → 2,49
```

Ce qu'on remarque : **c'est exactement le MER seuil CM3 = 0 de LUMEN**, calculé à la
question 1. Ce n'est pas un hasard — le MER seuil CM3 = 0 *est*, par construction, le MER
auquel un euro de publicité rend exactement un euro de contribution. Le plan du fondateur
supposait donc, sans l'avoir jamais écrit, que ses campagnes marginales tourneraient à
2,49 alors que la mesure donnait 1,40. **Tout plan de croissance contient une hypothèse de
MER incrémental. Si tu ne l'écris pas, tu l'as quand même faite.**

---

*Fin du cas C08. Suite : [C09 — Le piège du Black Friday, modélisé](C09-piege-du-black-friday.md).*
