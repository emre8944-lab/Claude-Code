# Niveau L09 — Architecte

> **Prérequis :** niveau L08 validé.
>
> **Ce que tu sais faire à la sortie :**
> 1. Tu transformes un compte de résultat à 9 % d'EBITDA en un plan chiffré à 18 % sans un euro de chiffre d'affaires en plus, en chantiers dont la somme tombe juste et qui ont chacun une date de premier euro.
> 2. Tu construis du capital de marque en payant à la performance, et tu chiffres la part de marge qui vient de la demande que tu n'achètes plus.
> 3. Tu tiens un registre des risques chiffré, et tu sais dire quelles mesures ne valent pas leur prix.
>
> **Temps de travail typique :** 40 à 55 heures, dont quinze sur ton propre compte de résultat.

> **Lxx mesure ta compétence. Nx mesure l'état de ton business.** Les deux sont indépendantes. On est L09 sans posséder de marque — c'est le profil d'un directeur général sous contrat. Et on est **N4**, deux millions d'euros de chiffre d'affaires par mois, avec une compétence **L04** : quelqu'un qui alloue un budget correctement et n'a jamais su d'où venait sa marge. **C'est le cas le plus dangereux du métier, et le plus fréquent à ce niveau de chiffre d'affaires**, parce que le chiffre d'affaires paie les salaires et fait taire la question. Le jour où elle revient, personne ne sait y répondre. Garde ton L au-dessus de ton N ([diagnostic](../mentorat/diagnostic.md)).

---

## 1. Les compétences du niveau

1. **Je reconstitue un compte de résultat en points de CA HT** à partir de montants bruts, et je place le MER et ses deux seuils — contribution et résultat — sans regarder les formules.
2. **Je décompose un objectif de marge en chantiers indépendants**, chacun en points d'EBITDA, et je démontre pourquoi ils ne s'additionnent qu'à chiffre d'affaires constant.
3. **Je calcule le volume que j'ai le droit de perdre** en supprimant une remise, et je l'écris avant de couper.
4. **Je distingue un gain de marge d'un transfert de coût** : une baisse de COGS obtenue en dégradant le produit est une dette payable en retours et en réachat, et je sais la chiffrer.
5. **Je nomme, pour chaque chantier, le risque qu'il crée**, son seuil d'alerte chiffré et sa règle de retour arrière — écrits avant le lancement.
6. **Je chiffre une espérance de perte annuelle** — probabilité × durée × part de CA touchée × contribution hebdomadaire —, je la compare au coût de la mesure, et je sais écrire qu'une mesure ne vaut pas son prix.
7. **Je sais quand une mesure qui ne vaut pas son prix se prend quand même** : la survie ne s'arbitre pas sur une espérance.
8. **Je valorise en multiple d'EBITDA normalisé**, hypothèses déclarées, et je sépare ce qui vient du résultat de ce qui vient de la confiance qu'on lui accorde.

---

## 2. Ce que tu lis

| # | Lecture | Ce qu'elle apporte **à ce niveau** |
|---|---|---|
| 1 | [**E12**](../modules/E12-marque-et-actif.md) § 1 à § 7 | Le test de coupure, la contradiction marque/performance, et la construction de capital de marque **en payant à la performance** — avec la preuve que le MER visé est hors d'atteinte par l'optimisation : la courbe de rendement l'interdit. |
| 2 | [**E12**](../modules/E12-marque-et-actif.md) § 8 | Ce qui fait monter et descendre un multiple, et pourquoi un point de marge vaut plus qu'une année de bénéfice. |
| 3 | [**E13 — Le risque de ruine**](../modules/E13-risque-de-ruine.md) | La différence entre un risque qui coûte et un risque qui termine ; la limite de la colonne d'espérance. |
| 4 | [**E14**](../modules/E14-plan-1M-semaine.md) § 6 | Le passage P5 → P5+ en cinq chantiers chiffrés ([jalons](../mentorat/jalons.md)). Le dossier de l'épreuve en est une variante déformée : refais les cibles, ne les recopie pas. |
| 5 | [**C09 — Le piège du Black Friday**](../etudes-de-cas/C09-piege-du-black-friday.md) | Une remise se juge sur la cohorte à douze mois. Le chantier le plus lourd de l'épreuve. |
| 6 | [**C10 — Compte publicitaire banni**](../etudes-de-cas/C10-compte-publicitaire-banni.md) | Onze jours d'arrêt, chiffrés. L'événement que tout le monde redoute n'est pas celui qui tue. |

---

## 3. Ce que tu fais

| Travail | Livrable | Comment on sait que c'est fait |
|---|---|---|
| **Le chantier P5 → P5+ sur ta marque** (ou sur MAVELLE) | Six à huit chantiers : cible, points, mécanisme, date de premier euro, risque créé | La somme ramenée à ton EBITDA actuel donne exactement ta cible. Pas 17,8. Pas 18,3 |
| [**S12 — La crise**](../atelier/S12-la-crise.md) | Le plan de crise et l'auto-évaluation finale | Ton plan nomme la fonction qui décide, pas la personne — et il tient sans toi |
| **Le registre des risques** ([modèle](../modeles/registre-des-risques.md)) | Une ligne par risque : probabilité, durée, part de CA touchée, espérance, mesure, coût, résiduel | Au moins une ligne porte **« mesure non retenue »** avec son calcul. Un registre où tout est traité n'a rien arbitré |
| **Simulateur : une partie jusqu'à P5+** | Ton journal de décisions, et l'écart entre ton EBITDA final et 20,3 % | Tu identifies le mois de la décision qui a coûté le plus, et les mois écoulés avant qu'elle se voie |

```bash
python3 ecommerce/outils/plan_objectif.py --ca-hebdo 1000000 --ebitda-cible 18
```

> **Le travail qui compte le plus est le registre, pas le plan.** Le plan est borné : c'est de l'arithmétique. Le registre exige d'écrire une probabilité en face d'un événement qu'on préfère ne pas imaginer, puis de conclure par écrit qu'on ne fera rien contre certains d'entre eux. C'est le seul document du cursus qui demande de choisir ce qu'on accepte de subir. **Lis E13 avant E12 § 8** : valoriser sans savoir chiffrer un risque produit des valorisations qui ne tiennent pas la première question d'un audit.

---

## 4. L'épreuve

**Durée : 4 h 00**, trois parties. Calculatrice autorisée, aucun document. **Barème sur 100 — (a) 55, (b) 25, (c) 20. Passage à 75, minimums par partie au § 6.**

### Le dossier — MAVELLE

> *Marque fictive, chiffres modélisés sur des ordres de grandeur sectoriels : ce ne sont les comptes d'aucune entreprise réelle.*

MAVELLE vend du soin du corps premium en direct sur sept marchés européens. Elle est arrivée au volume — **999 969 € de CA TTC par semaine** — et n'y gagne pas ce qu'elle devrait. Mission de dix-huit mois : **porter l'EBITDA de 9,4 % à 18,0 % du CA HT sans croissance du chiffre d'affaires.**

**Compte de résultat mensuel** (moyenne stabilisée sur 12 mois)

| Poste | Montant mensuel |
|---|---:|
| CA TTC | 4 333 200 € |
| **CA HT** | **3 611 000 €** |
| Coût marchandise (COGS) | 577 760 € |
| Logistique (préparation, emballage, transport, retours) | 433 320 € |
| Frais de paiement | 57 776 € |
| Retours, casse, gestes commerciaux | 144 440 € |
| Remises et codes promotionnels | 343 045 € |
| Dépense publicitaire | 1 390 235 € |
| Frais fixes (44 ETP, outils, loyers, honoraires) | 324 990 € |

**Exploitation** — panier moyen mixte 70,00 € TTC ; 61 903 commandes et 41 235 nouveaux clients par mois ; part du CA en réachat 41 % ; croissance du CA sur 12 mois +2 % ; TVA moyenne pondérée 20 %. **Plan média** : Meta 62 %, TikTok 14 %, Google 18 %, influence et autres 6 %.

**Structure et dépendances** — sérum héros : 71 % du CA HT, **fournisseur unique**, réapprovisionnement en 105 jours. Logistique : **prestataire unique**, 100 % des expéditions. Marque déposée en France, Belgique et Royaume-Uni seulement — **les quatre autres marchés, 50 % du CA HT, ne sont pas couverts**. Trésorerie 2 150 000 € ; BFR 2 480 000 € ; ligne de crédit 1 200 000 € tirés à 0. La fondatrice se verse 90 000 € par an ; le marché pour ce poste est à 180 000 €.

**Le registre des risques, tel qu'il t'est remis** — probabilités et durées sont des *hypothèses déclarées du dossier*, pas des mesures.

| Risque | Probabilité annuelle | Durée d'impact | Part du CA touchée | Coût annuel de la mesure proposée | Effet de la mesure |
|---|---:|---:|---:|---:|---|
| **R1** — Bannissement du compte publicitaire principal | 8 % | 11 sem. | 45 % | 55 000 € | durée 11 → 4 sem., part 45 % → 34 % |
| **R2** — Défaillance du fournisseur unique du sérum | 12 % | 15 sem. | 71 % | 105 998 € | durée 15 → 6 sem. |
| **R3** — Défaillance du prestataire logistique | 5 % | 4 sem. | 100 % | 30 000 € | durée 4 → 1 sem. |
| **R4** — Opposition de marque sur les marchés non déposés | 6 % | 26 sem. | 50 % | 6 000 € + 38 000 € une fois | le risque disparaît |

### Partie (a) — Le plan de marge (55 points)

**A1 — Le point de départ. (8 points)** Reconstitue le compte de résultat en pourcentage du CA HT jusqu'à l'EBITDA. Donne le MER blended et ses deux seuils. Conclus en une phrase : où est l'argent de MAVELLE, et où il n'est pas.

**A2 — Les six chantiers. (30 points, 5 par chantier)** Construis un plan de six chantiers qui porte l'EBITDA à 18,0 %. Pour chacun : la ligne visée, sa valeur de départ et sa cible en % du CA HT, le gain en **points d'EBITDA**, le gain en **euros par an**, le mécanisme, la durée avant plein effet. Un chantier sans mécanisme vaut 2 sur 5.

**A3 — La somme. (7 points)** Montre que 9,40 % plus tes six gains fait exactement 18,00 %. Explique **pourquoi ils s'additionnent ici**, et les deux situations où ils cesseraient de le faire.

**A4 — Le calendrier. (10 points)** Ordonne les six chantiers sur dix-huit mois : mois de lancement, mois du premier euro. Justifie l'ordre par deux critères et deux seulement — durée avant effet, dépendance entre chantiers. Termine par la trajectoire d'EBITDA par trimestre.

### Partie (b) — Le risque (25 points)

**B1 — Le risque que chaque chantier crée. (12 points, 2 par chantier)** Pour chacun : le risque qu'il **crée** — pas un risque général de l'entreprise —, son seuil d'alerte chiffré et observable en moins de quatre semaines, la règle de retour arrière.

**B2 — Le registre. (8 points)** Calcule l'espérance de perte annuelle de R1 à R4 — `probabilité × durée en semaines × part du CA touchée × contribution hebdomadaire` — et classe-les. Puis, pour chacun : ce que la mesure fait réellement gagner, son coût, et le verdict **retenue / non retenue**.

**B3 — La limite de la colonne « espérance ». (5 points)** Un de tes quatre verdicts doit être révisé pour une raison absente du calcul d'espérance. Nomme-le, et démontre par un calcul de trésorerie pourquoi l'espérance ne suffit pas ici.

### Partie (c) — La valorisation (20 points)

**C1 — Les deux valeurs. (8 points)** Estime la valeur de MAVELLE aujourd'hui et à l'arrivée. Déclare tes multiples en trois scénarios, justifie chacun par au moins trois éléments du dossier. Attention à l'EBITDA que tu multiplies.

**C2 — La décomposition. (6 points)** Décompose l'écart de valeur central en deux parts — celle qui vient de l'EBITDA gagné, celle qui vient du multiple — et donne le pourcentage de chacune.

**C3 — Ce que vaut un point. (6 points)** Combien vaut un point de marge d'EBITDA à la revente ? Compare-le à deux repères du dossier et conclus en une phrase.

---

## 5. Le corrigé

### A1 — Le point de départ

```
                        € / mois    % du CA HT
CA HT                  3 611 000       100,00
COGS                     577 760        16,00
Logistique               433 320        12,00
Frais de paiement         57 776         1,60
Retours, casse, gestes   144 440         4,00
Remises                  343 045         9,50
MARGE BRUTE (CM2)      2 054 659        56,90
Publicité              1 390 235        38,50
CM3                      664 424        18,40
Frais fixes              324 990         9,00
EBITDA                   339 434         9,40
```

```
MER blended           = 4 333 200 ÷ 1 390 235       = 3,12
MER seuil CM3         = 1,20 ÷ 0,5690               = 2,11
MER seuil EBITDA      = 1,20 ÷ (0,5690 − 0,0900)    = 2,51
Écart au seuil EBITDA = 3,12 ÷ 2,51 − 1             = +24,3 %
```

**La phrase attendue :** *l'argent de MAVELLE n'est pas dans la publicité — elle achète son trafic 24 % au-dessus de son seuil de résultat, comme le modèle canonique à P5 ([§ 2.3](../donnees/chiffres-canoniques.md) : +24,4 %) — il est dans les 43,10 points de coûts variables.*

**Barème.** 4 le tableau (−0,5 par ligne fausse), 3 les trois MER, 1 la phrase. **0 à la question si le MER est calculé sur le CA HT** (éliminatoire, § 6).

### A2 — Les six chantiers

| # | Ligne visée | De | À | Points d'EBITDA | € / an |
|---|---|---:|---:|---:|---:|
| 1 | Remises et codes promotionnels | 9,50 % | **6,50 %** | **3,00** | 1 299 960 € |
| 2 | Logistique (par le panier moyen) | 12,00 % | **11,00 %** | **1,00** | 433 320 € |
| 3 | Retours, casse, gestes | 4,00 % | **3,10 %** | **0,90** | 389 988 € |
| 4 | COGS | 16,00 % | **14,80 %** | **1,20** | 519 984 € |
| 5 | Publicité (par le MER) | 38,50 % | **36,70 %** | **1,80** | 779 976 € |
| 6 | Frais fixes | 9,00 % | **8,30 %** | **0,70** | 303 324 € |
| | | | **Total** | **8,60** | **3 726 552 €** |

*Un point de CA HT vaut `3 611 000 × 12 ÷ 100 = 433 320 €` par an — le repère canonique.*

**1 — la remise (3,00 pts).** Bandeaux permanent et de sortie supprimés, codes créateurs plafonnés à 10 % pendant 72 heures, fin de la remise de réactivation, opération de fin d'année basculée vers un coffret exclusif à prix plein. **Durée : 9 mois**, le temps d'un cycle promotionnel. 35 % du plan.

**2 — le panier moyen (1,00 pt).** De 70,00 € à **76,40 € TTC** par l'offre — format cure trois mois, lot de trois, seuil de livraison offerte relevé de 49 € à 69 € TTC — **et non par une hausse de prix**.

```
Commandes = 4 333 200 ÷ 70,00 = 61 903  →  4 333 200 ÷ 76,40 = 56 717   (−8,38 %)
Le coût logistique est majoritairement par colis, pas par euro :
Logistique cible = 12,00 % × (56 717 ÷ 61 903) = 12,00 % × 0,91622 = 11,00 %
```

Le nombre d'unités vendues est inchangé : **le COGS en pourcentage ne bouge pas**, ni les frais de paiement, proportionnels au montant. **Durée : 6 mois.**

**3 — les retours (0,90 pt).** Fiche produit décrivant les quatorze premiers jours d'usage, guide de dosage dans le colis, contact à J+10, retrait des deux références qui font 41 % des retours. **Durée : 6 mois.**

**4 — le COGS (1,20 pt).** Seconde source qualifiée, engagement de volume sur douze mois, revue du packaging secondaire. **Durée : 12 mois** (cinq de qualification, quatre d'écoulement, trois de montée en charge). **Condition suspensive : voir B1.**

**5 — le MER (1,80 pt).** MER de 3,12 à **3,27**, réachat de 41 % à 48 % du CA, trafic direct et de marque de 19 % à 26 %, par bascule de 5 % du budget média vers des formats qui construisent la mémoire. **Durée : 18 mois, et le chiffre ne bouge pas avant le mois 9** ([E12](../modules/E12-marque-et-actif.md) § 7.1 : la courbe de rendement interdit d'y arriver par l'optimisation).

**6 — les frais fixes (0,70 pt).** De 324 990 € à **299 713 €** par mois, −7,8 % : trois départs non remplacés, quatre outils redondants arrêtés, partie fixe du contrat logistique renégociée. **Durée : 12 mois.**

**Barème par chantier (5 pts).** 1 la cible, 1 les points, 1 les euros par an, 1 le mécanisme, 1 la durée. **−2 au chantier 2 si la baisse du nombre de commandes est appliquée au COGS** (les unités n'ont pas bougé). **−3 au chantier 5 si le mécanisme est « optimiser les campagnes ».**

### A3 — La somme, et pourquoi elle s'additionne

```
9,40 + 3,00 + 1,00 + 0,90 + 1,20 + 1,80 + 0,70 = 18,00 %
En euros : 339 434 + 310 546 = 649 980 € par mois, soit 7 799 760 € par an
Contre 4 073 208 € au départ.  Écart : 3 726 552 € = 8,60 × 433 320 €
```

**Pourquoi ça s'additionne.** Le CA HT est tenu constant par la mission. Chaque chantier réduit une ligne distincte exprimée en pourcentage du **même** dénominateur, et six fractions de même dénominateur s'additionnent : arithmétique, pas hypothèse de gestion.

**Les deux exceptions.** **Si le chiffre d'affaires bouge**, les points cessent d'être commensurables : logistique et COGS sont variables, les fixes ne le sont pas, la publicité est un budget. **Si deux chantiers touchent le même levier physique**, ils ne s'ajoutent pas, ils se multiplient — le chantier 2 réduit la logistique par le nombre de colis, une renégociation tarifaire la réduirait par le prix ; les additionner surestime le gain d'un dixième environ.

**Barème.** 3 la somme juste, 2 l'additivité, 2 les deux exceptions. **0 si la somme n'est pas entre 17,9 et 18,1 %.**

### A4 — Le calendrier

| Lancement | Chantier | Premier euro | Plein effet | Pourquoi ici |
|---:|---|---:|---:|---|
| **M1** | 5 — le MER | M9 | M18 | Le plus lent : ce qui met dix-huit mois se lance en premier, sinon il ne rentre pas |
| **M1** | 4 — le COGS | M13 | M18 | Cinq mois de qualification avant toute décision de bascule |
| **M1** | 3 — les retours | M2 | M6 | Le plus rapide à encaisser ; il finance la trésorerie des autres |
| **M4** | 2 — le panier moyen | M5 | M10 | Précède le chantier 1 : un panier plus élevé rend la coupe de remise supportable |
| **M10** | 1 — les remises | M11 | M18 | Dépend du 2 : couper avant d'avoir relevé le panier, c'est le faire payer au volume |
| **M12** | 6 — les frais fixes | M13 | M18 | **En dernier, délibérément :** couper avant les cinq autres supprime les gens qui les mènent |

| Fin de | Ce qui a rendu | EBITDA |
|---|---|---:|
| T1 (M3) | retours partiel (+0,3) | **9,7 %** |
| T2 (M6) | retours plein (+0,9), panier partiel (+0,2) | **10,5 %** |
| T3 (M9) | +0,9 / +0,7 / MER partiel +0,4 | **11,4 %** |
| T4 (M12) | +0,9 / +1,0 / +0,9 / COGS +0,6 / remises +0,5 | **13,3 %** |
| T5 (M15) | +0,9 / +1,0 / +1,3 / +1,2 / +1,8 / fixes +0,4 | **16,0 %** |
| T6 (M18) | +0,9 / +1,0 / +1,8 / +1,2 / +3,0 / +0,7 | **18,0 %** |

**Ce que le barème cherche : rien de significatif ne se produit avant le mois 10.** Qui juge ce plan au trimestre 2 conclura qu'il ne marche pas et coupera le chantier 5 — le seul qui ne se rattrape pas. D'où la règle : **la trajectoire trimestrielle s'écrit et se signe au mois 1.** Ce n'est pas une prévision, c'est une protection contre la décision qu'on prendra au mois 6. *Le plan consomme environ 640 000 € de trésorerie sur neuf mois contre 2 150 000 € disponibles : finançable sans tirer la ligne de crédit.*

**Barème.** 4 l'ordre et ses deux critères, 3 la dépendance 2 → 1 explicitée, 3 la trajectoire. **−3 si les frais fixes sont coupés au premier trimestre.**

### B1 — Le risque que chaque chantier crée

| Chantier | Le risque qu'il crée | Seuil d'alerte | Retour arrière |
|---|---|---|---|
| **1 — remises** | La frange qui n'achetait qu'en promotion s'en va | Commandes hebdomadaires **−5,3 %** sur 3 semaines, hors saisonnalité | Remise ciblée sur les segments perdus, jamais publique |
| **2 — panier moyen** | Le seuil de livraison offerte relevé fait chuter la conversion | Conversion **−6 %** sur 2 semaines, ou abandon panier **+4 pts** | Seuil redescendu à 59 € TTC, panier repris par l'offre |
| **3 — retours** | Le contact à J+10 **déclenche** des retours qui n'auraient pas eu lieu | Écart de taux de retour entre groupe contacté et témoin **> 0,5 pt** sur 4 semaines | On arrête le contact, on garde le guide |
| **4 — COGS** | Le changement de spécification dégrade le produit perçu | Panel aveugle de 120 clients : note **< 4,4 / 5**, ou retours du lot pilote **> lot actuel + 0,3 pt** | **Condition suspensive : on ne bascule pas.** Le chantier vaut 0, le plan tombe à 16,8 % |
| **5 — MER** | Le chantier est coupé au premier trimestre difficile, avant d'avoir rien produit | Aucun seuil de performance avant M9 — c'est **la règle**, pas une tolérance | Seuil d'arrêt écrit au M1 : trafic de marque non progressé à M12 |
| **6 — frais fixes** | On coupe dans les fonctions qui portent les cinq autres chantiers | Toute coupe touchant la créa ou la donnée | Règle écrite : ces fonctions sont hors périmètre |

**Le seuil de 5,3 % se démontre** — c'est la perte de volume au-delà de laquelle supprimer la remise devient perdant :

```
Gain du chantier                 3,00 % × 3 611 000 €   = 108 330 € / mois
Coût d'un point de volume perdu    1 % × 2 054 659 €    =  20 547 € / mois
Volume qu'on a le droit de perdre  108 330 ÷ 2 054 659  =   5,27 %
```

Le seuil réel est un peu plus favorable, une partie de la publicité suivant le volume. On retient 5,3 % : un seuil d'alerte se calcule dans le sens prudent.

**Barème.** 2 par chantier : 1 pour un risque réellement **créé par le chantier**, 1 pour un seuil chiffré et observable ; un risque générique vaut 0. La condition suspensive du chantier 4 sépare un plan d'un vœu — c'est la décision qui détruit la marque du dossier de [L10](L10-expert-mondial.md).

### B2 — Le registre

Contribution hebdomadaire : `664 424 € × 12 ÷ 52 = 153 328 €` de CM3.

| Risque | Calcul | Espérance annuelle | Rang |
|---|---|---:|---:|
| **R2** fournisseur | 0,12 × 15 × 0,71 × 153 328 € | **195 953 €** | 1 |
| **R4** marque | 0,06 × 26 × 0,50 × 153 328 € | **119 596 €** | 2 |
| **R1** bannissement | 0,08 × 11 × 0,45 × 153 328 € | **60 718 €** | 3 |
| **R3** logistique | 0,05 × 4 × 1,00 × 153 328 € | **30 666 €** | 4 |
| | **Total** | **406 933 €** | |

`406 933 ÷ 433 320 = 0,94` — **ton registre vaut 0,94 point d'EBITDA par an, davantage que le chantier des frais fixes.** Personne ne le porte au budget.

| Risque | Espérance résiduelle | Gain de la mesure | Coût annuel | Verdict |
|---|---:|---:|---:|---|
| **R4** | 0 € | **119 596 €** | 6 000 € + 38 000 € une fois | **Retenue.** Payback du dépôt : `38 000 ÷ 113 596 = 4,0 mois` |
| **R2** | 0,12 × 6 × 0,71 × 153 328 = **78 381 €** | **117 572 €** | 105 998 € | **Retenue de justesse** : +11 574 € par an |
| **R1** | 0,08 × 4 × 0,34 × 153 328 = **16 682 €** | 44 036 € | 55 000 € | **Non retenue à ce prix** : −10 964 € par an |
| **R3** | 0,05 × 1 × 1,00 × 153 328 = **7 666 €** | 23 000 € | 30 000 € | **Non retenue à ce prix** : −7 000 € par an |

Le résultat est inconfortable, et c'est pour ça qu'il est dans l'épreuve : **la mesure que tout le monde prend en premier — la redondance du compte publicitaire — ne paie pas**, et celle que personne ne porte en comité — déposer sa marque — rapporte vingt fois son entretien.

**Barème.** 4 les espérances et le classement, 4 les verdicts avec leur gain net. Un verdict sans gain net vaut 0,5.

### B3 — La limite de la colonne « espérance »

Le verdict à réviser est **R2**, « retenu de justesse » à 11 574 € de gain net par an. Lecture fausse : l'espérance mélange deux choses incomparables, un coût et une fin.

```
Perte de contribution sur 15 semaines  15 × 0,71 × 153 328 €  = 1 632 944 €
Trésorerie disponible                                         = 2 150 000 €
Reste après l'événement                                       =   517 056 €
Frais fixes mensuels                                          =   324 990 €
Autonomie restante                     517 056 ÷ 324 990      =   1,6 mois
```

Et le calcul est optimiste : le BFR de 2 480 000 € ne se dénoue pas pendant une rupture — le stock invendable ne redevient pas du cash. **R2 n'est pas un risque qui coûte 195 953 € par an ; c'est un risque qui, une fois sur huit, laisse MAVELLE avec sept semaines de trésorerie et un produit héros indisponible pendant huit semaines encore.**

**La règle :** *l'espérance décide des risques qui coûtent, jamais de ceux qui terminent ; pour ceux-là le critère est la survie du scénario le pire.* R2 se traite donc quel que soit son prix. R1 et R3 restent non retenus : MAVELLE en régime dégradé reste à l'équilibre, ses fixes ne pesant que 9,0 % du CA HT et sa publicité tombant avec son volume.

**Barème.** 2 désigner R2, 2 le calcul de trésorerie, 1 la règle. Désigner R1 vaut 0 : c'est le réflexe que la question existe pour attraper.

### C1 — Les deux valeurs

**L'EBITDA à multiplier est l'EBITDA normalisé**, retraité de la sous-rémunération de la fondatrice : un acquéreur paiera ce poste 180 000 € par an.

```
EBITDA publié aujourd'hui    339 434 × 12          = 4 073 208 €
EBITDA normalisé             4 073 208 − 90 000    = 3 983 208 €
EBITDA publié à l'arrivée    649 980 × 12          = 7 799 760 €
EBITDA normalisé             7 799 760 − 90 000    = 7 709 760 €
```

> *Hypothèses de multiples.* Marque de soin DTC européenne de cette taille, opération de gré à gré, EBITDA normalisé. **Aujourd'hui : 4,0× / 5,0× / 6,5×. À l'arrivée : 6,0× / 7,5× / 9,5×.** Ordre de grandeur pédagogique, pas une donnée de marché sourcée.

**Ce qui justifie 5,0× aujourd'hui :** CA en plateau (+2 %) ; 9,50 % de remises, donc un CA qu'un acquéreur sait ne pas pouvoir maintenir ; 62 % de la dépense sur une plateforme ; fournisseur unique sur 71 % du CA ; **marque non déposée sur 50 % du CA — cette ligne n'abaisse pas le prix, elle arrête l'opération** ; fondatrice visage de la marque.

**Ce qui justifie 7,5× à l'arrivée :** remises à 6,50 % ; réachat à 48 %, donc une demande qui n'a plus besoin d'être achetée ; seconde source ; marque déposée partout ; EBITDA à 18,0 %.

| Scénario | Aujourd'hui | À l'arrivée |
|---|---:|---:|
| Bas | 4,0× → **15 932 832 €** | 6,0× → **46 258 560 €** |
| **Central** | 5,0× → **19 916 040 €** | 7,5× → **57 823 200 €** |
| Haut | 6,5× → **25 890 852 €** | 9,5× → **73 242 720 €** |

Écart central : **37 907 160 €**, soit **×2,90**. Bas de fourchette 30 325 728 €, haut 47 351 868 €.

**Barème.** 2 la normalisation (0 si le candidat multiplie 4 073 208 €), 2 les trois scénarios, 3 les justifications, 1 l'écart central. **Éliminatoire : valoriser en multiple de chiffre d'affaires.**

### C2 — La décomposition

```
Part venant de l'EBITDA, à multiple constant
   (7 709 760 − 3 983 208) × 5,0              = 18 632 760 €   49,2 %
Part venant du multiple, sur l'EBITDA d'arrivée
   7 709 760 × (7,5 − 5,0)                    = 19 274 400 €   50,8 %
                                                -----------
                                                37 907 160 €
Vérification :  ×1,9356 (EBITDA) × ×1,50 (multiple) = ×2,9034
```

**La moitié de la création de valeur ne vient pas des euros gagnés, mais de la raison qu'on a de croire qu'ils reviendront l'année suivante.** Aucun chantier financier ne la fabrique : c'est le chantier 5 — le plus lent, le seul dont l'effet est invisible dans la fenêtre où il se décide, et le premier qu'on coupe.

**Barème.** 3 les montants, 2 les pourcentages, 1 la vérification. Attribuer l'effet croisé à l'une des parts sans le dire vaut 3 sur 6.

### C3 — Ce que vaut un point

```
37 907 160 ÷ 8,6 points               = 4 407 809 € par point d'EBITDA
EBITDA annuel normalisé d'aujourd'hui = 3 983 208 €
CA TTC hebdomadaire                   =   999 969 €
37 907 160 ÷ 999 969                  = 37,9 semaines de CA TTC
```

**Un point de marge d'EBITDA vaut, à la revente, 4 407 809 € — davantage que l'année entière de bénéfice d'exploitation de MAVELLE aujourd'hui.** Et les 37 907 160 € d'écart valent près de neuf mois de chiffre d'affaires, créés sans un euro de vente supplémentaire.

**La phrase attendue :** *une année de travail sur le volume vaut moins qu'un point de marge — et personne dans l'entreprise n'a de prime indexée sur un point de marge.*

**Barème.** 2 le montant par point, 2 les comparaisons, 2 la conclusion. Recommander d'aller chercher de la croissance vaut 0 : la mission l'interdisait, et c'était le vrai enseignement.

---

## 6. Le critère de passage

**Note minimale : 75 / 100**, avec **38 / 55 en (a), 15 / 25 en (b), 12 / 20 en (c)**. Les parties ne se compensent pas : qui construit une marge sans registre construit une marge que le premier événement emporte, et qui chiffre un risque sans savoir bâtir un plan n'a rien à protéger.

**Cinq fautes éliminatoires, quelle que soit la note :**

1. **Un MER calculé sur le CA HT.** Le MER se calcule sur le TTC, la marge sur le HT. Erreur n° 1 du métier : elle fait paraître une marque rentable de plusieurs points.
2. **Une somme de chantiers hors de 17,9–18,1 %.** Un plan qui n'atteint pas sa cible n'est pas approximatif, il est faux : on l'exécutera entièrement et on n'arrivera pas.
3. **Atteindre 18 % en coupant le budget média sans démontrer que le CA tient.** Cinq points d'EBITDA s'obtiennent en cinq minutes sur un tableur en supprimant cinq points de publicité — et ce plan garantit la baisse que la mission interdisait.
4. **Valoriser en multiple de chiffre d'affaires**, ou multiplier un EBITDA non normalisé.
5. **Un registre où les quatre mesures sont retenues.** Qui n'arbitre rien n'est pas un registre, c'est une liste de bonnes intentions.

**Deux fautes lourdes :** appliquer la baisse du nombre de commandes au COGS (−2) ; désigner R1 en B3 (−5).

**En cas d'échec**, tu repasses sur un autre compte de résultat — cette fois une marque dont le MER est **sous** son seuil de résultat. La contrainte « sans croissance » y est intenable, et la première compétence évaluée est de le dire.

---

## 7. Les pièges de ce niveau

**1. Croire qu'un plan de marge est un exercice de coûts.** Deux des six chantiers — le panier moyen et le MER — se gagnent du côté du client et pèsent 2,80 des 8,60 points. Un directeur financier seul produit un plan à 5,80 points et le trouve complet : le reste ne figure sur aucune ligne qu'il contrôle.

**2. Croire qu'un gain de COGS est un gain.** Le piège le plus cher du niveau : il se présente comme une victoire signée et datée — 1,20 point, 519 984 € par an, obtenus en une négociation. Le dossier de [L10](L10-expert-mondial.md) est cette décision prise sans panel aveugle, chez une marque qui a économisé 0,42 € par unité et perdu treize fois plus. **Une baisse de COGS par changement de spécification n'est pas un gain tant que le lot pilote n'a pas été jugé par des clients.**

**3. Croire que la remise se supprime par décision, et qu'un plan de dix-huit mois se juge au bout de six.** La remise se supprime par substitution : le calendrier place le panier moyen **avant** elle, seule séquence où le client a une raison de rester ; inversée, la même paire produit −5 % de volume et un plan à 15 %. Et la trajectoire est à 10,5 % au trimestre 2, un point au-dessus du départ après six mois de contrariété — c'est là que quelqu'un demandera à quoi sert le chantier 5, qui porte 1,80 point et la moitié du multiple de sortie.

**4. Croire que le registre se remplit par prudence.** Il se remplit par calcul, et son résultat contredit les priorités que toute équipe se donne spontanément. Le classement par espérance est la partie facile ; la difficile est d'écrire « non retenue » en face d'une ligne, en sachant qu'il existe des risques où cette écriture est interdite.

**5. Croire que L09 mesure ton entreprise.** C'est le niveau où l'écart entre les deux échelles fait le plus de dégâts : la compétence L09 est celle qu'une marque **N4** croit posséder du seul fait d'être arrivée au volume. Or arriver au volume ne démontre rien sur la marge — le modèle canonique atteint 1 M€ par semaine à 10,1 % d'EBITDA, et le même chiffre d'affaires en produit 20,3 % ([canoniques § 8](../donnees/chiffres-canoniques.md)). Une marque N4 pilotée en L04 a bâti son organisation et ses contrats autour du premier chiffre, et découvrira en la vendant que la moitié de sa valeur n'a jamais été fabriquée.

---

*Fin du niveau L09. Suite : [L10 — Expert mondial](L10-expert-mondial.md) — où la question n'est plus de construire un plan, mais de trouver en trente minutes lequel des huit problèmes d'un dossier est le seul qui compte.*
