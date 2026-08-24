# Registre des risques

> **À quoi ça sert :** transformer « ça pourrait mal tourner » en une ligne chiffrée, comparable au coût de ce qui l'empêcherait, et rattachée à quelqu'un. C'est un outil d'allocation, pas un document de conformité.
> **Quand l'utiliser :** une revue par trimestre, deux heures, comité complet. Hors calendrier, à chaque événement qui déclasse une ligne : ouverture d'un marché, changement de fournisseur, franchissement d'un seuil du § 5.
> **Module rattaché :** [E13](../modules/E13-risque-de-ruine.md) § 7. Compléments : [E10](../modules/E10-cash-et-operations.md) pour les lignes trésorerie, stock et TVA, [cahier-des-charges-fournisseur.md](cahier-des-charges-fournisseur.md) pour les lignes fournisseur et qualité.

---

## 1. La méthode, et ses trois limites

```
Espérance de perte annuelle  E = probabilité annuelle × impact en euros
Premier tri :  acheter la mesure si  coût annuel < réduction de E
Réduction de E = E × taux de réduction attendu de la mesure
```

[E13 § 7.1](../modules/E13-risque-de-ruine.md) définit six colonnes : le risque, sa probabilité annuelle, l'impact calculé, l'espérance, la mesure, son coût annuel. **Ce modèle en ajoute trois** — le drapeau de ruine, le responsable, la date de revue. Ce sont les trois qui décident si le registre est tenu, et les trois qui manquent partout.

Trois limites de méthode, qui sont la moitié de l'intérêt du document.

**L'espérance ne dit rien de la ruine.** Un tirage à 0,8 % qui coûte 2 557 333 € et un tirage à 20 % qui coûte 102 293 € ont la même espérance. Le premier peut tuer l'entreprise, le second est une mauvaise semaine. D'où le **drapeau R**, mis dès que l'impact dépasse la réserve du palier — 1 243 595 € à P5 ([E13 § 6.3](../modules/E13-risque-de-ruine.md)). Les lignes marquées R obéissent au § 6, pas à l'arithmétique.

**Les lignes sont corrélées.** Un bannissement fait chuter l'encaissement, ce qui tend la trésorerie, ce qui force à liquider du stock, ce qui crée une rupture. Additionner des espérances suppose une indépendance fausse précisément les jours où ça compte.

**Tes probabilités sont fausses.** Ce sont des ordres de grandeur, révisés chaque trimestre. Leur utilité n'est pas d'être exactes : c'est d'être **écrites avant** l'événement, donc opposables. Une probabilité corrigée après coup n'est pas une estimation, c'est une justification.

---

## 2. Le registre vierge

| Risque | Prob. annuelle | Impact € | Espérance € | Mesure de réduction | Coût annuel € | Responsable | Revue |
|---|---:|---:|---:|---|---:|---|---|
| | | | | | | | |

Quatre règles de remplissage. **L'intitulé nomme un événement daté et mesurable** — « coupure Meta de 11 jours », pas « dépendance aux plateformes ». **L'impact est un montant en euros sur douze mois**, en marge brute ou en contribution, jamais en chiffre d'affaires, avec sa ligne de calcul à côté. **La mesure a un coût annuel complet**, y compris ce qu'elle coûte en marge ou en conversion ; sans coût et sans nom, ce n'est pas une mesure, c'est une intention. **L'impact se met en gras dès qu'il dépasse la réserve du palier** : c'est le drapeau R.

---

## 3. Le registre pré-rempli — marque de type NØRA, palier P5

> *Repères.* [Canoniques](../donnees/chiffres-canoniques.md) : EBITDA 364 752 €/mois et 4 377 023 €/an, CM3 724 752 €/mois, stock 1 832 581 €, pub 1 494 206 €/mois, nCAC 40,03 €, LTV 12 mois 86,75 €. Réserve du palier **1 243 595 €** ([E13 § 6.3](../modules/E13-risque-de-ruine.md)). **R1 à R8 reprennent le registre de [E13 § 7.2](../modules/E13-risque-de-ruine.md) sans y changer un chiffre** ; R9 à R18 l'étendent, et leurs probabilités comme leurs coûts de mesure sont des hypothèses de travail, à remplacer par les tiennes.

| Risque | Prob. | Impact € | Espér. € | Mesure de réduction | Coût €/an | Resp. | Revue |
|---|---:|---:|---:|---|---:|---|---|
| R1 Bannissement Meta, 11 j | 25 % | 414 464 | 103 619 | référentiel d'allégations, comptes redondants légitimes, contact plateforme | 36 000 | Acquisition | 31/03 |
| R2 Coupure Meta ≥ 30 j | 6 % | 1 077 639 | 64 658 | *(même mesure que R1)* | — | Acquisition | 31/03 |
| R3 Sanction allégations, pratiques trompeuses | 8 % | 650 000 | 52 000 | conseil juridique permanent, DPO | 108 000 | Juridique | 30/09 |
| R4 Traceurs non conformes, perte de signal | 5 % | **1 583 244** | 79 162 | mesure côté serveur, gestion du consentement | 60 000 | Tech | 31/12 |
| R5 Rappel de lot sur le héros | 2 % | **2 519 502** | 50 390 | traçabilité lot → client, garantie frais de retrait | 71 500 | Ops | 30/06 |
| R6 Rupture fournisseur unique, 45 j | 6 % | **1 497 806** | 89 868 | double fournisseur, 70 / 30 | 75 398 | Ops | 30/06 |
| R7 Rétrofacturations au-dessus du seuil PSP | 4 % | 1 200 000 | 48 000 | scoring, 3DS ciblé, libellé bancaire, délai | 69 267 | Finance | 31/12 |
| R8 Perte des accès critiques | 8 % | 900 000 | 72 000 | double administrateur, clés matérielles, propriété société | 9 000 | DG | 30/09 |
| R9 Dépendance mono-canal, arrêt ≥ 90 j | 3 % | **2 842 229** | 85 267 | Meta de 55 % à 40 % du budget | 1 161 774 | Acquisition | 31/03 |
| R10 Rupture de trésorerie | 6 % | 733 032 | 43 982 | ligne confirmée non tirée de 1 500 000 €, compte TVA séparé | 11 250 | Finance | 31/03 |
| R11 Perte d'une personne clé, hors accès | 25 % | 157 000 | 39 250 | doublure documentée, procédures écrites, pacte d'associés | 45 000 | DG | 30/09 |
| R12 Panne de la plateforme de vente | 60 % | 32 390 | 19 434 | page de secours, coupure média sur sonde, engagement de service | 14 000 | Tech | 31/12 |
| R13 Incendie ou sinistre entrepôt | 0,8 % | **2 557 333** | 20 459 | multirisque avec perte d'exploitation, 15 % du stock en 2ᵉ site | 56 200 | Ops | 30/06 |
| R14 Cyberattaque, fuite de la base clients | 5 % | 895 744 | 44 787 | MFA, chiffrement, test d'intrusion annuel, police cyber | 68 000 | Tech | 31/12 |
| R15 Hausse brutale du coût des enchères | 30 % | **1 793 047** | 537 914 | 23 gagnants tenus en rotation, bascule Google Search préparée | 95 000 | Acquisition | 31/03 |
| R16 Invendu saisonnier | 25 % | 641 403 | 160 351 | commande en deux vagues 60 / 40, option sur la seconde | 18 000 | Ops | 30/09 |
| R17 Changement réglementaire | 12 % | 831 743 | 99 809 | veille contractualisée, formule de secours qualifiée | 44 000 | Juridique | 30/09 |
| R18 Dérive du taux de retour et du SAV | 30 % | 649 980 | 194 994 | NQA majeur à 1,0, guide d'usage, suivi hebdomadaire par motif | 57 343 | Ops | 30/06 |
| **Total** | | **20 976 556** | **1 805 944** | | **1 999 732** | | |

**D'où viennent les impacts.** R1 à R8 sont dérivés dans [E13](../modules/E13-risque-de-ruine.md) § 1.2, 3.2, 4.1, 4.2, 5.2 et 6.2. Pour les dix autres :

```
R9  arrêt de 90 j : 900 061 × 90 ÷ 30,4 + 177 578 d'apprentissage (E13 § 1.2).
    Coût de la mesure : E13 § 1.3, 15 points de budget réalloués
R10 liquidation de 105 j de stock en 30 j, décote 40 % (E10 § 8)
R11 arrêt de 3 semaines du pilotage acquisition, 8 % de dérive du MER
    = 122 000 € (E13 § 6.2) + 35 000 € d'intérim et de recrutement
R12 8 h d'arrêt : 0,333 × (48 117 € de marge brute nette de rattrapage
    + 49 151 € de pub du jour, canoniques § 5)
R13 stock 1 832 581 € (§ 4) + 30 j de rupture = 724 752 € de CM3
R14 forensic 120 000 + notification 60 000 + 3 j d'arrêt 291 804 + sanction
    modélisée 250 000 (plafond RGPD : 4 % du CA mondial, soit 1 733 279 €)
    + 3 mois à −8 % de conversion 173 940
R15 +20 % de nCAC pendant 6 mois : § 7 donne 1 793 047 €/an par tranche de 10 %
R16 mauvaise saison sur la commande de pic : 2 565 613 ÷ 4 (E13 § 7.5)
R17 reformulation 85 000 + notification 12 000 + articles imprimés obsolètes
    0,42 € × 49 087 × 4 mois = 82 466 + 60 j de rupture héros 652 277
R18 +1,5 point de taux de retour sur 12 mois = 1,5 × 433 320 € (§ 7)
```

---

## 4. Ce que le total dit, et ce qu'il ne dit pas

```
Espérance de perte annuelle brute                        1 805 944 €   41,3 % de l'EBITDA
  dont R1 à R8, registre de E13 § 7.2                      559 697 €
  dont R9 à R18, extension                                1 246 247 €
Coût total des mesures                                   1 999 732 €   45,7 %
Espérance résiduelle après mesures                         703 955 €
Réduction achetée                                        1 101 989 €
Rapport réduction ÷ coût                                       0,55
```

Taux de réduction retenus, R9 à R18 : 60, 85, 60, 60, 75, 55, 45, 70, 55 et 60 % ; R1 à R8 reprennent les espérances résiduelles de [E13 § 7.2](../modules/E13-risque-de-ruine.md), soit 147 638 € au total.

**Le programme complet coûte 1,8 fois ce qu'il retire en espérance.** Un comité qui ne lirait que ce rapport le refuserait, et aurait tort pour trois raisons, toutes lisibles dans le tableau.

**Un.** Six impacts dépassent la réserve du palier — R4, R5, R6, R9, R13, R15 — et quinze des dix-huit en dépassent la moitié. L'espérance moyenne d'une entreprise qui ne survit pas au tirage ne veut rien dire ; c'est la démonstration de [E13 § 7.4](../modules/E13-risque-de-ruine.md), et elle se déplace avec le registre.

**Deux.** La somme des probabilités vaut **2,61**. Tu ne gères pas un risque par an, tu en gères deux ou trois. Et si les dix-huit tiraient la même année, l'addition ferait 20 976 556 €, soit **4,79 fois l'EBITDA annuel**.

**Trois.** Une seule ligne, R9, porte 58 % du coût total du programme — et c'est la seule qui **change la nature** du risque au lieu d'en réduire la probabilité. Retire-la : les dix-sept autres coûtent 837 958 € pour 1 050 829 € d'espérance retirée, et le programme redevient rentable. **Ce que tu paies cher, ce n'est jamais la prévention : c'est l'indépendance.**

Six lignes portent 65,7 % de l'espérance — R15, R18, R16, R1, R17, R6. C'est là que passent les deux heures du trimestre.

---

## 5. Les trois seuils de dépendance à ne jamais dépasser

[E13 § 2.1](../modules/E13-risque-de-ruine.md) en recense six et les dérive tous d'une règle unique : **aucune dépendance ne doit pouvoir consommer plus de la moitié de ta réserve avant que tu aies eu le temps de la remplacer.** Trois de ces six tuent ; les voici avec leur conséquence chiffrée.

**A — Le canal d'acquisition, mesuré en nouveaux clients réels, jamais en budget.** Vigilance 40 %, alerte 55 %, critique 70 %. NØRA est à **51,6 %** sur Meta (canoniques § 5, après correction des 11 % de sur-attribution) : entre vigilance et alerte. Un arrêt de 90 jours vaut 2 842 229 €, soit `÷ 364 752 = 7,8 mois d'EBITDA` et **2,29 fois la réserve**. Ramener Meta à 40 % du budget ramène le même arrêt à `2 842 229 × 40 ÷ 55 = 2 067 076 €`, soit 1,66 fois la réserve : toujours au-dessus. **Le seuil ne rend pas la coupure indolore, il la rend survivable.**

**B — Le fournisseur, mesuré en part du COGS annuel, pas en nombre de références.** Vigilance 50 %, alerte 70 %, critique : mono-source. NØRA est en **mono-source, donc en critique**. Quarante-cinq jours de rupture valent 1 497 806 €, soit 1,20 fois la réserve ; la double source 70 / 30 ramène l'impact résiduel à 400 000 €, soit 0,32 ([E13 § 7.2](../modules/E13-risque-de-ruine.md)). Trois produits chez le même façonnier, c'est une dépendance à 100 %, et le catalogue donne l'illusion contraire.

**C — Le marché, mesuré en part de la marge brute.** Vigilance 40 %, alerte 55 %, critique 70 %. Le seuil de 40 % n'est pas un chiffre rond : [E13 § 7.6](../modules/E13-risque-de-ruine.md) montre qu'un arrêt total à 40 % d'exposition laisse **4,9 mois** de trésorerie, contre 2,7 à 60 % et 1,8 à 80 %. **Quatre virgule neuf mois, c'est la durée d'ouverture d'un nouveau marché.** Le seuil achète exactement le temps de le remplacer.

> **À retenir :** les seuils se surveillent sur un tableau de bord mensuel, pas au registre trimestriel. Le registre chiffre les conséquences ; le tableau de bord dit si tu es dedans.

---

## 6. La règle de plafonnement de l'exposition

> **Aucune ligne ne conserve, après mesure, un impact supérieur à la réserve du palier — 1 243 595 € à P5. Et la somme des impacts laissés sans aucune mesure ne dépasse jamais la moitié de la réserve, 621 798 €.**

C'est la règle dont [E13 § 2.1](../modules/E13-risque-de-ruine.md) dérive ses six seuils, appliquée ligne à ligne au lieu de dépendance à dépendance. Une ligne au-dessus du plafond se traite dans cet ordre, jamais dans un autre :

1. **Réduire l'impact.** Découper l'exposition : deux entrepôts, deux fournisseurs, deux comptes publicitaires, deux prestataires de paiement. Seul levier dont l'effet est mécanique.
2. **Transférer.** Assurance, plafond de responsabilité contractuel, provision dédiée. Effet certain mais partiel : une police couvre le stock, pas la rupture qui suit.
3. **Réduire la probabilité.** Procédures, formation, veille. En dernier, parce que c'est le seul levier dont tu ne prouveras jamais l'effet — et celui que les comités choisissent en premier, parce qu'il est le moins cher à décider.

Trois plafonds opérationnels traduisent la règle en décisions quotidiennes, tous dérivés au [§ 7.6 de E13](../modules/E13-risque-de-ruine.md) : la trésorerie nette ne descend jamais sous **un mois de dépense publicitaire plus treize semaines de frais fixes** (2 574 207 € à P5) ; aucune commande fournisseur unique ne dépasse **25 % de la trésorerie nette** ni 60 jours de couverture — 643 552 € à P5, donc au minimum trois commandes en rotation, ce qui coûte 188 494 € par an de fractionnement ; aucun marché ne dépasse **40 % de la marge brute**.

**Application au registre du § 3.** Après mesures, deux lignes restent au-dessus du plafond : **R4 à 1 583 244 € et R9 à 2 067 076 €** — R7 les suit de près à 1 200 000 €. Les six autres lignes marquées R passent sous la barre par l'assurance ou le doublement. Et les deux qui restent ont le même profil : **leur mesure réduit la probabilité, pas l'impact.** Une architecture de mesure côté serveur et un mix de canaux ne se décident pas ligne à ligne dans un tableau ; ils se décident en comité, une fois, pour deux ans. **On n'achète pas une réduction d'espérance, on achète le droit de survivre à un tirage.**

---

# Les erreurs qu'on voit tout le temps

1. **Chiffrer l'impact en chiffre d'affaires.** Un mois sans Meta ne coûte pas 4,3 M€ de CA : il coûte 900 061 € de contribution nette, et il **améliore** la trésorerie du mois de 190 499 € ([E00 § 4.4](../modules/E00-cadrage.md)). Un registre en chiffre d'affaires surestime tout d'un facteur cinq, rend toutes les mesures rentables, et ne produit donc aucune priorité.
2. **Classer par gain net.** Les six lignes dont l'impact dépasse la réserve sont majoritairement couvertes par des mesures que l'espérance condamne. Trier par rentabilité supprime exactement les mesures qui te maintiennent en vie — le piège complet est démonté en [E13 § 7.4](../modules/E13-risque-de-ruine.md), et il se referme sur les opérateurs les plus rigoureux.
3. **Additionner les espérances comme si elles étaient indépendantes.** Les trois lignes les plus corrélées du registre sont R1, R10 et R16 : la coupure crée la tension de trésorerie, qui force à liquider le stock du pic. Une revue sérieuse teste au moins un scénario à trois lignes simultanées.
4. **Une mesure sans coût annuel et sans nom.** « Diversifier les canaux » n'est pas une mesure ; 1 161 774 € par an, portés par le responsable acquisition, revus le 31 mars, en est une. Toute case vide dans la colonne coût est une ligne non traitée qui se croit traitée.
5. **Un registre qui n'a jamais fait annuler une décision.** S'il n'a bloqué aucun lancement, aucun engagement de volume, aucune ouverture de marché depuis quatre trimestres, ce n'est pas un outil de pilotage : c'est un document de conformité, et il coûte deux heures par trimestre à tout un comité.

*Rattaché à [E13](../modules/E13-risque-de-ruine.md) § 7. Voir [E10](../modules/E10-cash-et-operations.md) pour les lignes R10 et R16, et le [cahier des charges fournisseur](cahier-des-charges-fournisseur.md) pour R5, R6 et R18.*
