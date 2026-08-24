# Module E03 — L'offre et le prix

> **Prérequis :** [E01](E01-arithmetique-de-la-marque.md), [E02](E02-marche-et-produit.md). En parallèle : [module 1](../../modules/01-asymetries-information.md) du cursus racine.
> **Objet :** construire une offre dont le panier moyen finance l'acquisition, et manier le levier qui déplace l'EBITDA plus vite que tous les autres — le prix.
> **Temps de travail :** ~6 h (lecture + exercices, calculatrice obligatoire)

---

## 0. Pourquoi ce module existe

Canonique § 7, palier P5. Sur les sept leviers de NØRA, +10 % de panier moyen vaut **3 139 401 € d'EBITDA annuel**, soit 71,7 % de l'EBITDA de référence ; le deuxième, la conversion, 2 662 749 € — **17,9 % de moins** ; le troisième, le CAC, 1 793 047 €.

Le levier n° 1, donc. Et personne ne le pilote : il est *constaté* dans un rapport mensuel pendant que l'équipe passe ses journées sur les créations, l'algorithme et le coût marchandise.

Le prix est le même levier, en plus brutal. +10 % à commandes constantes est un +10 % de panier **sans un euro de coût marchandise supplémentaire** : 3 767 712 €/an, soit +86,1 % d'EBITDA (§ 1.3). −10 % exige **+76,4 % de commandes** rien que pour revenir à l'EBITDA de départ (§ 1.2). Le levier pardonne la hausse et punit la baisse.

Enfin, § 8 : le passage de P5 à P5+ — 4 428 560 € d'EBITDA de plus — ne demande **aucun euro de chiffre d'affaires supplémentaire**, seulement un panier de 77,20 € et une marge brute de 66,0 %. Ce module est le mode d'emploi de ces deux nombres.

---

## 1. Le prix

### 1.1 Le prix de référence interne

Un client ne juge pas un prix dans l'absolu : il le compare à un **prix de référence interne**, mémoire de ce qu'il s'attend à payer dans la catégorie. **L'ordre d'affichage l'écrit** — la Cure à 99,00 € montrée avant le sérum à 39,00 € ne donne pas la même référence que l'inverse. **Ta première remise le devient** : découvert à −20 %, ton prix plein est pour lui une majoration de 25 % (§ 5.2). **Il appartient à la catégorie** : en sortir se paie en preuve, donc en créations ([E05](E05-machine-creative.md)).

### 1.2 Ce que coûte réellement une baisse de prix

Base : P5, AOV mixte **71,98 € TTC**, marge brute **61,5 % du CA HT**, structure du canonique § 2.1. Sépare les coûts qui suivent le prix de ceux qui ne le suivent pas — c'est toute la finesse du calcul.

```
CA HT par commande = 71,98 ÷ 1,20                              = 59,98 €

Coûts FIXES par commande (indépendants du prix affiché) :
  COGS       14,5 % × 59,98                                    =  8,70 €
  Logistique 11,0 % × 59,98   (un colis reste un colis)        =  6,60 €
                                                         total = 15,30 €
Coûts PROPORTIONNELS au prix :
  PSP 1,55 % + retours/SAV 3,5 % + remises 8,0 %               = 13,05 %

Marge brute (p) = p × (1 − 0,1305) − 15,30
Contrôle : 59,98 × 0,8695 − 15,30 = 36,86 €
           36,86 × 60 200 = 2 218 957 € — canonique § 2.2. Conforme.
```

| Variation de prix | CA HT/cmd | Marge brute/cmd | Commandes pour tenir la **marge brute** |
| --- | ---: | ---: | ---: |
| Référence | 59,98 € | 36,86 € | — |
| **−10 %** | 53,99 € | 31,64 € | **+16,5 %** |
| **−20 %** | 47,99 € | 26,43 € | **+39,5 %** |
| **+10 %** | 65,98 € | 42,08 € | **−12,4 % tolérables** |

La formule courte, `volume = d ÷ (m − d)`, suppose tous les coûts fixes par commande : à m = 61,5 % et d = 10, elle donne **+19,4 %** — elle sur-estime, parce que 13,05 points de coûts baissent avec le prix.

Mais **la marge brute n'est pas le bon repère** : elle ignore la publicité, premier poste de NØRA. *Hypothèse explicite :* la publicité par commande reste de 1 494 206 ÷ 60 200 = **24,82 €**, donc un CAC qui ne se dégraderait pas en achetant 76 % de commandes en plus — faux, et généreux ([module 13](../../modules/13-unit-economics.md) § 2.2).

| Variation de prix | CM3 par commande | Commandes pour tenir l'EBITDA de 364 752 €/mois | Écart |
| --- | ---: | ---: | ---: |
| Référence | 12,04 € | 60 200 | — |
| **−10 %** | 6,82 € | 106 214 | **+76,4 %** |
| **−20 %** | 1,61 € | 450 728 | **+648,7 %** |

> **À retenir :** une baisse de prix ne se compense jamais par le volume, parce qu'elle s'applique à **100 %** de tes commandes pendant que le volume supplémentaire ne concerne que la marge.

### 1.3 Le calcul symétrique : et si tu montes de 10 % ?

```
Prix +10 %, commandes constantes, unités vendues constantes.
CA HT/mois = 3 610 997 × 1,10                              = 3 972 097 €
  − COGS       inchangé (mêmes flacons) 0,145 × 3 610 997  =   523 595 €
  − Logistique inchangée (mêmes colis)  0,110 × 3 610 997  =   397 210 €
  − PSP     0,0155 × 3 972 097                             =    61 568 €
  − Retours 0,035  × 3 972 097                             =   139 023 €
  − Remises 0,080  × 3 972 097                             =   317 768 €
Marge brute 2 532 933 €  contre 2 218 957 € (§ 2.2)
Gain mensuel 313 976 €  →  annuel 3 767 712 €
EBITDA annuel : 4 377 023 € → 8 144 735 €, soit +86,1 %.

Combien de commandes peux-tu perdre à EBITDA inchangé ?
CM3/commande à +10 % = 42,08 − 24,82                       = 17,25 €
N = 724 752 ÷ 17,25 = 42 004 commandes   contre 60 200     = −30,2 %
```

**Tu peux perdre presque un tiers de tes commandes après une hausse de 10 % et gagner exactement autant qu'avant.** Il faudrait une élasticité de −3,0 pour y arriver : niveau des commodités indifférenciées, pas d'un soin acheté pour un résultat.

### 1.4 L'élasticité, et pourquoi tu ne la connais pas

L'élasticité-prix est la variation relative du volume divisée par celle du prix. À −1,0, +10 % de prix coûte 10 % de volume : le CA est inchangé et **la marge monte**, puisque tu vends moins d'unités pour le même chiffre. Elle n'est pas celle de ta catégorie (elle dépend de ta distinctivité, [module 10](../../modules/10-sharp-distinctivite.md)), n'est pas constante (faible autour de la référence, elle explose au franchissement d'un seuil, § 2.1), et n'est pas observable passivement — tes ventes passées mélangent prix, saison, budget et créations. Seule mesure propre : deux marchés comparables, prix différents, quatre semaines, ventes totales comparées — Hopkins chapitre 16 ([module 12](../../modules/12-hopkins-publicite-scientifique.md)) et [E09](E09-mesure-et-incrementalite.md).

### 1.5 L'effet de gamme

**Ancrage haut :** la Cure à 99,00 € rend le Rituel à 74,00 € raisonnable et le sérum à 39,00 € bon marché. **Compression :** trois prix trop rapprochés (39, 44, 49) ne créent aucune hiérarchie ; chez NØRA, 39 → 74 (×1,90) et 74 → 99 (×1,34). **Aversion aux extrêmes :** une part du marché prend toujours l'option du milieu — le produit d'appel n'a pas pour objet d'être acheté, mais de faire acheter le suivant.

---

## 2. Le prix psychologique

### 2.1 Les seuils

La demande a des marches : 10, 20, 30, 50, 100, 150, 200 €. Ce qui compte est l'arbitrage **quand tu décides de franchir**. Convention colis : 6,60 € par expédition (§ 2.1 : 11,0 % × 3 610 997 ÷ 60 200).

```
Cure à  99,00 € TTC → 82,50 € HT : 82,50 × 0,8695 − 14,40 − 6,60 = 50,73 €
Cure à 109,00 € TTC → 90,83 € HT : 90,83 × 0,8695 − 14,40 − 6,60 = 57,98 €
Perte de volume tolérable = 1 − 50,73 ÷ 57,98 = 12,50 %
```

**Franchir les 100 € est gagnant tant que cela coûte moins de 12,5 % du volume de la Cure.** Un seuil n'est pas un interdit : c'est un péage dont on calcule le tarif.

### 2.2 Les terminaisons

| Terminaison | Ce qu'elle dit | Où elle a sa place |
| --- | --- | --- |
| **,99 / ,95** | « prix travaillé, bonne affaire » | Discount, marketplace, déstockage |
| **,90** | Compromis mou : ni bonne affaire ni premium | Presque nulle part |
| **,00** | « prix assumé, marque qui ne négocie pas » | DTC premium — le cas de NØRA |

Les cinq références de NØRA finissent par ,00 (§ 1). Passer à ,90 revient à consentir 0,10 € TTC par commande.

```
0,10 € TTC ÷ 1,20 = 0,0833 € HT, dont 13,05 % de coûts proportionnels tombent
Perte nette par commande = 0,0833 × 0,8695 = 0,0725 €
× 60 200 commandes × 12 mois = 52 344 € d'EBITDA par an
```

**Le « 9 » coûte 52 344 € par an**, pour un gain jamais démontré sur ce type de catégorie. Là où le prix bas *est* la proposition il reste cohérent : il a simplement un prix, qui se calcule.

### 2.3 La précision d'un prix est un signal

Un prix rond (40,00 €) signale une décision de positionnement ; un prix précis (38,74 €) signale un calcul, donc un coût, donc une contrainte — sur un bien premium, il détruit la prime. Exception, le prix *comparé* : « Économisez 18,00 € » est un slogan, « Économisez 18,00 € sur les 117,00 € du même contenu à l'unité » est une démonstration (§ 4.4).

### 2.4 Le prix comme information sur la qualité

Reviens au [module 1](../../modules/01-asymetries-information.md). Akerlof (1970) : là où l'acheteur ne peut pas vérifier la qualité avant l'achat, le prix bas est le comportement rationnel du mauvais vendeur, parce que le bon ne peut pas y survivre — un prix bas se lit donc comme **l'aveu d'une qualité basse**, et statistiquement c'est vrai. Spence (1973) : un signal ne fonctionne que si son coût est plus élevé pour le mauvais type. Un prix élevé n'est un signal **que si** le mauvais type ne peut pas le pratiquer ; là où n'importe qui affiche 89 € pour un produit blanc à 4 €, l'équilibre est mélangeant et le signal est mort.

**Le prix ne signale la qualité que s'il est accompagné d'un coût que le menteur ne peut pas payer** — garantie longue (§ 7), composition publiée et testable, délai de fabrication vérifiable. C'est la raison arithmétique du [E02](E02-marche-et-produit.md) § 1.1 : sous un coefficient de ×5, tu ne finances plus les signaux qui rendent ton prix crédible. Le ×6,4 à ×8,1 de NØRA (§ 1) est le budget du signal.

---

## 3. La construction de gamme

### 3.1 Les quatre rôles

| Rôle | Fonction économique | Ce qu'on mesure dessus |
| --- | --- | --- |
| **Produit d'appel** | Entrer dans la catégorie, jamais porter l'acquisition payante | Taux d'attache au panier |
| **Produit héros** | Porter 100 % de la publicité, de la promesse et de la preuve | nCAC, taux de conversion |
| **Produit de panier** | Élever l'AOV sur la commande du héros | Part des commandes multi-format |
| **Produit premium / prépayé** | Porter la marge, le cash et le réachat anticipé | Part du CA, avance de trésorerie |

### 3.2 La règle du héros, démontrée

**Un seul produit porte l'acquisition** — contrainte de production créative, pas préférence esthétique. Canonique § 6, P5 : 57 concepts testés par semaine, **5,2 gagnants** (9,1 %), pour tenir une rotation de **23 gagnants**.

```
Tout le budget de test sur UN héros :
  23 ÷ 5,2 = 4,4 semaines pour reconstituer la rotation
Budget réparti sur les 5 références :
  57 ÷ 5 = 11,4 concepts par référence et par semaine
  11,4 × 9,1 % = 1,04 gagnant par référence et par semaine
  23 ÷ 1,04 = 22,1 semaines pour reconstituer la rotation d'UNE référence
```

**Facteur 5 sur le délai de renouvellement.** Or un concept gagnant vit quelques semaines ([E05](E05-machine-creative.md)) : une rotation qui met 22 semaines à se reconstituer est morte avant d'exister. Les autres produits ne sont pas moins bons — ils n'ont pas droit au budget de test.

### 3.3 La gamme NØRA, référence par référence

Canonique § 1 pour les prix et les COGS. Contribution en **convention colis** — la logistique est un coût par expédition (6,60 €), pas un pourcentage du panier ([E08](E08-retention-et-ltv.md) § 6.1) : seule façon de comparer des références de tailles différentes.

| Référence | PVC TTC | Coef. | Contribution | vs nCAC 40,03 € (§ 2.4) | Rôle |
| --- | ---: | ---: | ---: | ---: | --- |
| Shampooing Fortifiant | 24,00 € | ×7,7 | 7,69 € | −32,34 € | Produit d'appel — **jamais** en acquisition |
| Masque Réparateur | 29,00 € | ×8,1 | 10,81 € | −29,22 € | Panier et réachat |
| **Sérum Densité (héros)** | **39,00 €** | **×8,1** | **16,86 €** | **−23,17 €** | **Porte toute la publicité** |
| Rituel Complet | 74,00 € | ×6,4 | 35,52 € | −4,51 € | Porte le panier |
| Cure 3 mois | 99,00 € | ×6,9 | 50,73 € | **+10,70 €** | Porte la marge et le cash |

**Une seule référence rembourse son coût d'acquisition à la première commande.** Le héros, sur lequel passe 100 % du budget média, est à −23,17 € — cohérent avec le canonique § 2.4 (−7,26 € sur la première commande moyenne) : l'acquisition de NØRA est structurellement déficitaire au premier achat et le pari repose sur le réachat ([E08](E08-retention-et-ltv.md)). D'où la règle : **la publicité vend le héros, la page vend le format** ([E07](E07-funnel-et-conversion.md) § 4.2).

Contre-intuitif : le Rituel a le **plus mauvais** coefficient de la gamme (×6,4) et la deuxième meilleure contribution absolue. Un taux de marge ne paie pas les salaires ; des euros, oui. Le coefficient sélectionne une catégorie ([E02](E02-marche-et-produit.md)), il n'arbitre pas à l'intérieur d'une gamme.

---

## 4. Le panier moyen — le module dans le module

### 4.1 L'identité de départ

```
AOV = Σ (part des commandes portées par le format i × prix du format i)
      + frais de port facturés par commande
      + valeur moyenne des ajouts avant paiement
      + valeur moyenne des ajouts après paiement
```

Quatre termes, six leviers, aucun euro de publicité supplémentaire : +10 % d'AOV vaut 3 139 401 €/an **à budget média inchangé** (§ 7).

### 4.2 (a) Le mix produit — le levier maître

| Format | PVC TTC | Part P1 | Part P5 | Écart |
| --- | ---: | ---: | ---: | ---: |
| Sérum seul | 39,00 € | 61 % | 17 % | −44 pts |
| Shampooing seul | 24,00 € | 9 % | 9 % | — |
| Masque seul | 29,00 € | 7 % | 7 % | — |
| Rituel Complet | 74,00 € | 19 % | 40 % | +21 pts |
| Cure 3 mois | 99,00 € | 4 % | 27 % | +23 pts |
| **Valeur du mix** | | **46,00 €** | **67,15 €** | **+21,15 €** |

*Hypothèse :* cette répartition est une modélisation, contrainte par l'obligation de reconstituer exactement l'AOV canonique de P1 (46,00 €, § 2) et, additionnée des trois autres termes, celui de P5 (71,98 €, § 2). [E07](E07-funnel-et-conversion.md) § 4.2 en donne une version plus grossière, sans port ni ajout, qui aboutit au même AOV. La part des formats multi passe de **23 % à 67 %**.

```
Rituel : +21 pts × (74,00 − 39,00) = 21 % × 35,00 € =  7,35 €
Cure   : +23 pts × (99,00 − 39,00) = 23 % × 60,00 € = 13,80 €
                                              total = 21,15 €
```

**Avertissement d'honnêteté comptable.** Une partie du déplacement n'est pas le mérite de l'offre : à P5, 38 % des commandes sont des réachats contre 4 % à P1, et un client qui revient prend la Cure. Tout se dérive — panier = contribution ÷ taux de marge brute.

```
1ʳᵉ commande : 21,69 ÷ 57,2 %  × 1,20 = 45,50 € (P1)   (§ 2.1, § 2.4)
               32,77 ÷ 61,45 % × 1,20 = 64,00 € (P5)
Réachat  : (55,97 − 21,69) ÷ 1,24 ÷ 57,2 % × 1,20 = 58,00 € (P1) (§ 3, § 3.1)
                         43,53 ÷ 61,45 % × 1,20 = 85,00 € (P5)   (§ 3)
Parts de réachat : 4,0 % (P1) et 38,0 % (P5)
Contrôle § 8 : 0,38 × 85,00 ÷ 71,98 = 44,9 % du CA en réachat. Conforme.

Structure de commandes de P5 appliquée aux paniers de P1 :
  0,62 × 45,50 € + 0,38 × 58,00 € = 50,25 €, soit +4,25 € sur les 46,00 € de P1
```

Sur les 21,15 € de la ligne mix, **4,25 € appartiennent à [E08](E08-retention-et-ltv.md)** et 16,90 € au travail d'offre. Rien ne pourrit plus vite une équipe que deux services qui facturent le même euro.

### 4.3 (b) Le bundle et sa remise optimale

Le Rituel réunit les trois références. À l'unité : 39 + 24 + 29 = **92,00 €**. Prix du bundle : **74,00 €**, remise de 19,6 %.

```
Contribution de 3 achats séparés (3 colis, 3 fois les proportionnels) :
  16,86 + 7,69 + 10,81 = 35,36 €     Contribution du Rituel (1 colis) = 35,52 €

Remise maximale d'un bundle
  = économie logistique + (marge marchandise × probabilité que la vente
                           n'aurait PAS eu lieu sans le bundle)
```

**Une remise de 19,6 % qui rapporte 0,16 € de plus qu'aucune remise du tout** : le bundle ne « donne » pas 18,00 €, il en récupère l'essentiel en économisant deux expéditions (13,20 €). Le premier terme de la formule est certain, le second est un pari sur l'incrémentalité qui se teste ([E09](E09-mesure-et-incrementalite.md)). Au-delà de leur somme, le bundle **cannibalise** (§ 8.3).

### 4.4 (c) Le palier de quantité

La Cure est le même produit, en quantité. À l'unité : 3 × 39,00 = **117,00 €**. Prix : **99,00 €**, remise de 15,4 %.

```
Contribution de 3 sérums achetés séparément : 3 × 16,86 €   = 50,58 €
Contribution de la Cure                                     = 50,73 €
Prix plancher à contribution égale :
  0,72458 × P − 21,00 = 50,58  →  P = 98,79 € TTC (remise max 15,6 %)

Mais le vrai contrefactuel n'est pas 3 commandes : c'est 2,24 (§ 3).
  2,24 × 16,86 € = 37,77 €  →  0,72458 × P − 21,00 = 37,77  →  P = 81,10 €
  Remise maximale contre ce contrefactuel : 1 − 81,10 ÷ 117,00 = 30,7 %
```

NØRA est à 15,4 %, soit 0,21 € du plancher le plus strict. **Le taux acceptable dépend entièrement du contrefactuel retenu** : 15,6 % si le client aurait tout racheté, 30,7 % si tu comptes ce qu'il rachète réellement. Écris ton contrefactuel avant ton prix — presque tout le désaccord entre marketing et finance vient de ce qu'aucun des deux ne l'a écrit.

### 4.5 (d) Le seuil de franco de port

Le franco n'est pas un coût logistique, c'est un **prix conditionnel** : tu vends la livraison et tu l'offres contre un engagement de panier. Coût réel **6,60 € par colis** (§ 2.1) ; frais facturés, *hypothèse*, **4,90 € TTC** soit 4,08 € HT — tu en subventionnes déjà 2,52 €.

```
Contrainte 1 — le seuil doit MORDRE :  S > AOV
   Sous le panier moyen, il est franchi par la majorité des commandes sans
   qu'aucune n'ait bougé. Il ne fait rien, et il coûte le port.
Contrainte 2 — le seuil doit être ATTEIGNABLE en un ajout :
   S ≤ panier courant du segment visé + prix de la plus petite référence
```

*Hypothèse d'état des lieux :* NØRA est à P5 avec un seuil de **59,00 €** hérité de P2, jamais révisé. En dessous ne restent que les commandes mono-produit — 26 % du total, d'où les 1,27 € de port facturé du § 4.8. À 82 % de l'AOV, **il viole la contrainte 1** : les 67 % de commandes qui portent la marge ne le voient jamais.

Le bon seuil se lit sur la gamme : au-dessus de 74,00 € (le Rituel, qu'on veut faire bouger) et à moins d'un shampooing d'écart (98,00 €). Retiens **89,00 €**, sous les 99,00 € de la Cure pour que les meilleurs clients gardent le port offert sans rien faire. *Hypothèses de comportement, à mesurer et non à croire :* sur les 40 % de commandes Rituel, 25 % ajoutent une référence, 72 % paient le port, 3 % abandonnent.

```
Contribution d'un ajout : shampooing 24,00 € TTC → 20,00 € HT
  − COGS 3,10 € − proportionnels 13,05 % × 20,00 = 2,61 € − colis 0 € = 14,29 €

Commandes Rituel/mois : 60 200 × 40 %                         = 24 080
  montent (25 %)   6 020 × 14,29 €                            = +86 026 €
  paient  (72 %)  17 338 × 4,08 € HT de port encaissé         = +70 739 €
  abandonnent (3 %)  722 × 35,52 € de contribution perdue     = −25 645 €
Gain mensuel de marge brute 131 120 €  →  annuel 1 573 440 €
Nouvel AOV : 4 509 173 € ÷ 59 478 commandes = 75,81 €  (+3,83 €)
```

**1 573 440 € d'EBITDA par an, soit +35,9 %, pour un nombre changé dans un champ de configuration** — et à lui seul, ce réglage couvre **73,4 %** de l'écart d'AOV entre P5 et P5+ (§ 8).

### 4.6 (e) L'upsell pré-achat

Deux emplacements : la page produit (le sélecteur de format, déjà compté au § 4.2) et le panier. Reste le petit ajout — mini-format, recharge, accessoire. *Hypothèse :* attache 8 %, ticket moyen 11,50 € TTC → **0,92 € par commande**. Trois règles : **l'ajout est un complément, jamais une version du produit principal** (le 30 ml à côté du 50 ml fait descendre le panier) ; **prix ≤ 40 % du panier en cours**, au-delà il rouvre l'arbitrage sur l'achat entier ; **il se mesure sur le CA de l'étape, jamais sur son taux d'acceptation** — 14 % d'attache contre 0,3 point de passage au paiement détruit de la valeur ([E07](E07-funnel-et-conversion.md)).

### 4.7 (f) L'upsell post-achat en un clic

Une offre présentée **après** l'encaissement, acceptée d'un clic sans ressaisie de paiement, expédiée dans le même colis.

```
Shampooing proposé en post-achat, à prix plein :
  CA HT 20,00 € − COGS 3,10 € − PSP 1,55 % (0,31 €)
                − retours/SAV 3,5 % (0,70 €)
                − logistique 0 € (même colis) − remise 0 €    = 15,89 €
  Soit 79,5 % du CA HT, contre 61,45 % en moyenne (§ 2.2)

Hypothèse d'acceptation 11 % (ordre de grandeur sectoriel : 8 à 15 %) :
  0,11 × 60 200 = 6 622 acceptations/mois × 15,89 €  = 105 224 €/mois
                                        = 1 262 688 € d'EBITDA annuel
```

Quatre raisons structurelles. **Coût d'acquisition nul** : les 40,03 € de nCAC (§ 2.4) sont engagés sur la commande d'avant. **Coût logistique nul** : même colis, les 6,60 € ne sont pas dupliqués — d'où les 18 points de marge d'écart. **Aucun risque sur la commande principale** : l'offre vient après le paiement. **Aucune remise** : le client vient d'acheter au prix plein.

Au canonique § 2.4, la première commande rapporte 32,77 € pour 40,03 € de CAC, soit **−7,26 €** : à P5, l'acquisition ne produit aucun euro positif au premier achat. Les seuls euros immédiatement positifs viennent du réachat et de cet upsell — trois lignes de back-office qui pèsent 28,8 % de l'EBITDA annuel du palier.

### 4.8 Le pont complet : 46,00 € → 71,98 €

| # | Levier | Calcul | Δ AOV | AOV cumulé |
| --- | --- | --- | ---: | ---: |
| — | **Point de départ P1** | canonique § 2 | | **46,00 €** |
| b | Bundle Rituel : part 19 % → 40 % | 21 % × (74,00 − 39,00) | **+7,35 €** | 53,35 € |
| c | Palier de quantité — Cure : 4 % → 27 % | 23 % × (99,00 − 39,00) | **+13,80 €** | 67,15 € |
| a | *(mix produit = b + c, non recompté)* | *formats multi 23 % → 67 %* | *(21,15 €)* | |
| d | Franco à 59,00 € : 26 % des commandes paient | 26 % × 4,90 € | **+1,27 €** | 68,42 € |
| e | Upsell pré-achat : attache 8 %, ticket 11,50 € | 8 % × 11,50 € | **+0,92 €** | 69,34 € |
| f | Upsell post-achat : acceptation 11 %, ticket 24,00 € | 11 % × 24,00 € | **+2,64 €** | **71,98 €** |
| | **Total** | | **+25,98 €** | **71,98 €** |

Le total tombe au centime sur le canonique § 2. **Le mix fait 81,4 % du chemin** (21,15 sur 25,98) : à chantier unique, c'est la page produit. **Les 4,83 € restants ne se valorisent pas au prorata** — le port encaissé n'a ni COGS ni colis, l'upsell post-achat non plus (§ 8.6). **Les six leviers n'ont pas le même coût d'exécution** : le mix demande une refonte de page, un an de tests et une équipe créative ; le franco demande de changer un nombre qui vaut 1 573 440 €/an.

> **À retenir :** ton panier moyen n'est pas un résultat, c'est une **construction** : chacun de ses six termes se décide, se mesure et se teste séparément. Une marque qui « constate » son AOV a un problème d'attribution de responsabilité — personne n'a ce nombre dans ses objectifs.

---

## 5. Le coût réel d'une remise

### 5.1 Ce que la remise coûte, et ce que vaut un point

Canonique § 2.1 : à P5, les remises pèsent **8,0 % du CA HT**. Ce n'est pas un pourcentage, c'est une facture.

```
8,0 % × 3 610 997 € de CA HT mensuel (§ 2.2) = 288 880 €/mois = 3 466 557 €/an
1 point de remise = 1 % × 3 610 997 €        =  36 110 €/mois =   433 320 €/an
```

Face aux 360 000 €/mois de frais fixes (§ 2.5), NØRA distribue chaque année en codes promo **9,6 mois de la totalité de sa structure**. Et la trajectoire du § 2.1 — 3,0 % à P1 jusqu'à 8,0 % à P5 — dit que **la remise croît avec l'échelle** : seul poste de coût variable qui se dégrade quand tout le reste s'améliore.

Sur un point en moins, aucune autre ligne ne bouge : **un point vaut 433 320 € d'EBITDA net**, la valeur canonique d'un point de taux de retour (§ 7). Le passage à P5+ gagne 4,5 points de marge brute (§ 8). *Hypothèse de décomposition* : COGS −1,0 pt, logistique −0,5 pt, PSP −0,05 pt, retours −0,5 pt, **remises −2,5 pts** — contrôle : 1 − (13,5 + 10,5 + 1,5 + 3,0 + 5,5) % = 66,0 %. Conforme.

```
2,5 points de remise = 2,5 × 433 320 € = 1 083 300 €/an
Soit 24,5 % de l'écart d'EBITDA annuel entre P5 et P5+ (4 428 560 €, § 8)
```

**Un quart du chemin vers la vraie destination du cursus se joue sur la discipline promotionnelle.** Pas sur un nouveau canal, pas sur un nouveau pays.

### 5.2 L'accoutumance

Le mécanisme qui rend la remise irréversible, et ne figure sur aucune ligne comptable : un client qui achète en promotion mémorise ce prix comme référence (§ 1.1), à la suivante il attend, à la troisième il n'achète plus qu'en promotion. La population « plein tarif » se vide dans l'autre — jamais l'inverse. *Hypothèses :* le Black Friday pèse 6 % du CA annuel et se fait à −25 %.

```
CA TTC annuel P5 : 4 333 196 × 12                      = 51 998 352 €
Opération : 6 %                          → TTC 3 119 901 €, HT 2 599 918 €
Valeur avant remise : 2 599 918 ÷ 0,75                 =  3 466 557 €
Remise consentie                                       =    866 639 €
```

Seule est utile la part qui achète des commandes **incrémentales** ; le reste est offert à des clients qui auraient payé plein tarif. *Hypothèse :* la part non incrémentale démarre à 55 % et gagne 8 points par an.

| Année | Part non incrémentale | Remise offerte à des ventes acquises |
| ---: | ---: | ---: |
| 1 | 55 % | 476 652 € |
| 2 | 63 % | 545 983 € |
| 3 | 71 % | 615 314 € |

Et les semaines qui précèdent l'opération se vident, puisque la base attend. Mécanisme complet dans le cas [C09](../etudes-de-cas/C09-piege-du-black-friday.md).

### 5.3 Le seuil d'incrémentalité d'une promotion

La question n'est jamais « la promotion a-t-elle bien vendu » mais **« combien de commandes en plus fallait-il pour qu'elle ne détruise rien »** — le § 1.2 donne le moteur.

| Taux de remise | Commandes en plus pour tenir la marge brute | Pour tenir l'EBITDA |
| ---: | ---: | ---: |
| −10 % | +16,5 % | +76,4 % |
| −20 % | +39,5 % | +648,7 % |
| **−25 %** | **+54,7 %** | *au-delà du domaine de validité* |

**Une opération à −25 % doit produire plus de la moitié de commandes en plus rien que pour ne pas perdre de marge brute** — et le double si la moitié seraient venues de toute façon. Seul instrument qui tranche : opération sur une zone, pas sur une zone comparable, ventes **totales** comparées sur la période plus huit semaines ([E09](E09-mesure-et-incrementalite.md), [C06](../etudes-de-cas/C06-test-incrementalite.md)).

---

## 6. L'abonnement

### 6.1 La formule et le plafond d'attrition

L'abonnement est une remise permanente échangée contre une durée. La question n'est pas « faut-il en faire un » mais **« quel taux de remise, contre quelle durée minimale »**.

```
C(d) = PVC_HT × (1 − d) × (1 − PSP − retours) − COGS − logistique par colis
     = 32,50 × (1 − d) × (1 − 0,0155 − 0,035) − 4,80 − 6,60
       (pas de ligne remise : le prix est déjà le prix remisé)

LTV_abonnement(d, a) = C(d) ÷ a        avec a = attrition mensuelle
Seuil de destruction de valeur :
   a* = C(d) ÷ LTV naturelle à 24 mois = C(d) ÷ 118,96 €  (canonique § 3)
Contrôle à d = 15 % : C = 14,83 €, a* = 12,47 % — identique à E08 § 6.2.
```

| Remise | Contribution mensuelle | **Attrition maximale** | LTV à 10 % d'attrition |
| ---: | ---: | ---: | ---: |
| 0 % | 19,46 € | 16,36 % | 194,59 € |
| 10 % | 16,37 € | 13,76 % | 163,73 € |
| **15 %** | **14,83 €** | **12,47 %** | **148,30 €** |
| 20 % | 13,29 € | 11,17 % | 132,87 € |
| 25 % | 11,74 € | 9,87 % | 117,44 € |
| 30 % | 10,20 € | 8,58 % | 102,01 € |

**Chaque tranche de 5 points de remise abaisse le plafond d'attrition d'environ 1,3 point.** Au-delà de 12,47 % à −15 %, l'abonné rapporte moins que le même client laissé à son rythme naturel — à qui tu as pourtant offert 15 % à vie. *Hypothèse sectorielle :* l'attrition d'un abonnement consommable DTC se situe entre 8 et 15 %/mois. À −30 % le plafond tombe à 8,58 % : il faut être au niveau des tout meilleurs **rien que pour égaler l'inaction**.

### 6.2 Le cash, et quand ne pas le lancer

**L'abonnement au fil de l'eau n'apporte aucun cash** : tu prélèves quand tu expédies, le BFR est celui d'une vente normale, et tu as consenti la remise en plus. **Le prépayé finance ton BFR** : [E08](E08-retention-et-ltv.md) § 6.4 chiffre à 369 518 € le produit payé et non livré porté par les Cures, soit **16,3 % du BFR de P5** (2 264 655 €, § 4) — le seul financement qui ne se négocie ni avec une banque ni avec un fonds ([E10](E10-cash-et-operations.md)). Entre un abonnement mensuel à −15 % et une cure prépayée à −15,4 %, **prends la cure** : un colis au lieu de trois (§ 4.4), avance de trésorerie en prime.

Un abonnement ne crée pas la fidélité, il la facture d'avance : sur une base à faible réachat naturel, il convertit un problème de rétention en problème d'attrition. [E08](E08-retention-et-ltv.md) § 6.3 : réachat à 20 %, attrition à 25 %, LTV de 59,32 € pour 40,03 € de nCAC, ratio **1,48** — sous le seuil de 1,5 où la règle canonique dit « on ne scale pas, on répare ». Condition de lancement : premier réachat naturel > 40 %, stable sur six cohortes.

---

## 7. La garantie, le risque inversé et le paiement fractionné

### 7.1 Ce qu'une garantie est vraiment

Une garantie n'est pas un argument commercial : c'est un **transfert de risque** doublé d'un signal séparateur au sens de Spence ([module 1](../../modules/01-asymetries-information.md) § 3). Sur un produit qui marche le taux d'usage reste bas, sur un produit qui ne marche pas il explose : **c'est l'un des rares signaux que le menteur ne peut pas copier gratuitement.** Réserve du même module : tout signal efficace migre vers l'équilibre mélangeant, et « satisfait ou remboursé 30 jours » ne sépare plus rien. Ce qui sépare encore — durées longues, garantie **sur résultat** plutôt que sur retour, mention « gardez le produit » — migrera aussi.

### 7.2 Le coût réel et l'arbitrage

Canonique § 2.1 : la ligne retours/SAV vaut **3,5 % du CA HT** à P5, soit 126 385 €/mois et 1 516 619 €/an — la provision qui couvre la garantie actuelle. Allonger de 30 à 90 jours augmente le taux d'usage : plus de temps, plus de réclamations, et un consommable est largement entamé au 90ᵉ jour. *Hypothèse :* +0,9 point. Le coût est certain, le gain est un pari : convertis les deux dans la même unité, la commande.

```
Coût mensuel : 0,9 % × 3 610 997 €          =  32 499 €   (389 988 €/an)
Marge brute par commande (§ 1.2)            =   36,86 €
Commandes nécessaires : 32 499 ÷ 36,86      =     882   →  1,46 % du volume
```

**La garantie 90 jours est rentable dès qu'elle produit 1,46 % de commandes en plus.** Sur un taux de conversion de 2,40 % (*hypothèse* : ce nombre n'est pas canonique), c'est un passage à 2,435 % — **3,5 centièmes de point**. Personne de sérieux ne pariera contre.

Refais toujours le calcul dans ce sens — *coût certain ÷ marge par commande = commandes à trouver* — pour la garantie comme pour le retour gratuit ou l'échange offert. Bordure : très généreuse, une garantie attire des clients moins qualifiés dont le taux de retour est plus élevé ; surveille-le par cohorte ([E01](E01-arithmetique-de-la-marque.md) § 8).

### 7.3 Le paiement fractionné

Le paiement en trois ou quatre fois déplace la contrainte de « ai-je 90 € » à « ai-je 30 € ce mois-ci ». Il relève donc le panier des commandes où le montant est la contrainte — et de celles-là seulement. *Hypothèses, à mesurer chez toi :* 12 % des commandes l'utilisent, panier supérieur de 18 %, commission 4,0 % du TTC en remplacement du PSP à 1,55 % du HT.

```
Base concernée : 0,12 × 60 200 × 71,98 €               = 519 984 € TTC/mois
Marge sur l'incrément (COGS oui, colis non) :
   taux = 1 − 14,5 % − 13,05 %                          = 72,45 %
   519 984 ÷ 1,20 × 18 % × 72,45 %                      =  56 509 €/mois
Surcoût de commission :
   4,00 % du TTC − 1,55 % du HT (= 1,29 % du TTC)       =   2,71 % du TTC
   519 984 × 1,18 × 2,71 %                              =  16 618 €/mois
Gain net = 39 891 €/mois = 478 692 €/an

Seuil de rentabilité, en hausse de panier u :
   marge par point : 519 984 ÷ 1,20 × 1 % × 72,45 %     =   3 139 €
   313 940 × u = 14 083 × (1 + u)   →   u = 4,70 %
```

**Le paiement fractionné devient rentable dès qu'il relève le panier de 4,7 %.** En dessous, tu paies 2,71 points de commission sur tout le volume concerné pour rien.

Le piège : la commission s'applique à **toutes** les commandes qui utilisent le service, y compris celles qui auraient été payées comptant, alors que la hausse ne concerne que les commandes contraintes. *Hypothèse :* si la moitié seulement des utilisateurs relèvent leur panier, le seuil double à environ 9,4 %. Le test n'est donc pas « le fractionné augmente-t-il le panier des utilisateurs » — il l'augmente toujours, par sélection — mais **« l'activer augmente-t-il le panier moyen de la boutique »**. Deux marchés, un avec, un sans, quatre semaines. Financé par un prestataire il ne coûte **rien en trésorerie** ([E10](E10-cash-et-operations.md)) ; financé par toi, il transforme chaque commande en créance et alourdit le BFR de 2 264 655 € de P5 (§ 4). Ne le fais jamais.

---

## 8. Les erreurs qui coûtent cher

**8.1 — Baisser le prix pour vendre plus.** −10 % exige **+16,5 % de commandes** pour tenir la marge brute et **+76,4 %** pour tenir l'EBITDA (§ 1.2), à CAC supposé stable ; à −20 %, il faut multiplier le volume par 7,5. *Antidote :* écris le volume d'équilibre, et demande à celui qui propose la baisse s'il s'engage dessus.

**8.2 — Installer la remise en permanence.** 8,0 % du CA HT à P5 = **3 466 557 €/an**, soit 9,6 mois de frais fixes complets ; un point en moins vaut 433 320 €/an, et les 2,5 points d'écart avec P5+ valent 1 083 300 €/an (§ 5.1). *Antidote :* ligne de coût variable, propriétaire nommé, plafond mensuel décidé à l'avance.

**8.3 — Un bundle qui cannibalise la référence à forte marge.** Un Rituel bradé à 64,00 € : contribution 28,27 € au lieu de 35,52 €. Pour tenir la contribution des 24 080 Rituels mensuels, il en faudrait **30 252, soit 50,3 % de toutes les commandes** au lieu de 40 %. Et si 5 points de la Cure y migrent, chaque migration coûte 22,46 € : `0,05 × 60 200 × 22,46 € × 12 = 811 135 €/an` détruits, avant tout gain. *Antidote :* la formule du § 4.3, contrefactuel écrit avant le prix.

**8.4 — Le franco de port sous le panier moyen.** Un seuil à 59,00 € quand l'AOV est de 71,98 € n'est vu par aucune des 67 % de commandes qui portent la marge ; le porter à 89,00 € vaut **1 573 440 €/an** (§ 4.5). *Antidote :* il se recalcule à chaque révision de gamme, comme le MER seuil.

**8.5 — L'abonnement lancé avant le réachat naturel.** À 20 % de premier réachat, l'abonnement à −15 % donne 59,32 € de LTV pour 40,03 € de nCAC, ratio **1,48**, sous le seuil canonique de 1,5 ([E08](E08-retention-et-ltv.md) § 6.3). *Antidote :* réachat naturel > 40 % sur six cohortes.

**8.6 — Une marge moyenne appliquée à un euro qui n'a pas la structure moyenne.** Le port encaissé n'a ni COGS ni colis, l'upsell post-achat est à 79,5 %, la commande moyenne à 61,45 %. *Antidote :* une ligne de calcul par levier (§ 4.5, § 4.7).

**8.7 — Confondre prix psychologique et prix bas.** Les terminaisons en ,90 coûtent **52 344 €/an** (§ 2.2) pour un gain jamais démontré sur du premium ; et sur un bien invérifiable avant l'achat, un prix bas est un signal **négatif** (§ 2.4). *Antidote :* la terminaison se teste géographiquement, comme un prix.

**8.8 — Ne pas relire son prix pendant deux ans.** Seule variable qui ne se dégrade pas toute seule et n'exige aucun investissement : +10 % vaut 3 767 712 €/an et tolère −30,2 % de volume (§ 1.3). *Antidote :* une revue de prix au calendrier, test géographique à l'appui.

---

## 9. Ce que ce module ne dit pas

**Il ne traite pas des marchés où le prix bas EST la stratégie.** Hard discount, marketplaces de revente, distribution de commodités : modèles viables, exclus de ce cursus pour une raison arithmétique et non idéologique. Formule du [E02](E02-marche-et-produit.md) § 1.1 avec un coefficient de ×2 :

```
COGS en % du CA HT = 1,20 ÷ 2                                = 60,0 %
Marge brute = 1 − 60,0 % − 24,05 % (autres variables, § 2.1)  = 15,95 %
MER seuil de contribution = 1,20 ÷ 0,1595                     = 7,52
```

Un MER de 7,52 est hors de portée de toute acquisition payante — les paliers canoniques § 2.3 vont de 1,80 à 2,90. **Un modèle de prix bas n'est viable que si son coût d'acquisition est proche de zéro** : marketplace, flux physique de magasin, référencement organique, ou BFR négatif. Ces modèles gagnent par le coût du trafic et la rotation du stock, pas par la marge unitaire ; tout ce module, qui suppose qu'on achète son trafic, leur est inapplicable ([E00](E00-cadrage.md)).

**Il ne mesure aucune élasticité.** Les sensibilités calculées ici disent *combien de volume il faudrait*, jamais *combien tu en perdras* — ce nombre-là ne s'obtient que par un test géographique ([E09](E09-mesure-et-incrementalite.md)).

**Il ignore le cadre juridique.** L'affichage des réductions annoncées est réglementé dans l'Union européenne (directive dite Omnibus, transposée en 2022) : le prix barré doit être le plus bas pratiqué sur une période antérieure définie. Fait public à vérifier dans ta juridiction ; il contraint les mécaniques du § 5.

**Il traite le prix comme un scalaire**, alors qu'il est un vecteur : par pays, canal, device, segment. La TVA moyenne pondérée à 20 % sur sept marchés (§ 2) masque des écarts de prix nets réels — [E11](E11-passage-a-echelle.md).

**Il suppose la concurrence immobile** : une hausse de 10 % qui déclenche une campagne comparative n'a pas le rendement du § 1.3. **Et NØRA est fictive** — la cohérence au centime de son modèle est une propriété du modèle, pas du monde.

---

## 10. Le tableau de bord du module

| Indicateur | Fréquence | Seuil d'alerte | Réf. P5 |
| --- | --- | --- | ---: |
| **AOV mixte TTC** | Hebdo., 4 sem. glissantes | **−2 % sur 4 semaines** | 71,98 € |
| **Taux de remise** (% du CA HT) | Mensuelle | **> 8,0 %**, ou **+1 pt en 3 mois** | 8,0 % |
| **Part des commandes multi-format** | Hebdo. | **< 60 %** | 67 % |
| **Seuil de franco ÷ AOV** | Mensuelle, **recalculé** | **< 1,15** | 0,82 — *en alerte* |
| **Acceptation de l'upsell post-achat** | Hebdo. | **< 8 %** | 11 % |
| **Marge brute par commande, en €** | Mensuelle | **−1,00 € sur 3 mois** | 36,86 € |

Si tu n'en tiens que trois, garde les trois premiers. **Le ratio franco ÷ AOV se recalcule, il ne se mémorise pas** : seul indicateur qui se dégrade tout seul, son dénominateur montant pendant que son numérateur dort dans un champ de configuration — NØRA est à 0,82, en alerte permanente (§ 4.5). **L'AOV se lit en euros par commande** : +3 % dû à la part de réachat n'est pas une victoire de l'offre (§ 4.2). **La marge brute par commande est le juge de paix** : elle attrape remise, mix et COGS, là où l'AOV seul n'attrape rien.

---

## 11. Exercices

Formulaire vierge : [`E03-rendu.md`](../exercices/E03-rendu.md) ; corrigé : [`E03-corrige.md`](../exercices/E03-corrige.md). Fais les calculs à la main avant de l'ouvrir.

**Exercice 1 — La table de sensibilité au prix de P3** (réponse numérique unique). Canoniques § 2, § 2.1, § 2.2, TVA 20 %. P3 : 18 000 commandes/mois, AOV 65,40 € TTC, marge brute 60,3 %, publicité 436 000 €/mois, fixes 105 000 €/mois. Calcule (1) le CA HT par commande, (2) la part fixe par commande et la part proportionnelle au prix, (3) la marge brute par commande — contrôle : × 18 000 doit redonner 592 033 €, (4) les commandes nécessaires pour tenir la marge brute à −10 % puis −20 % de prix, (5) le même calcul à EBITDA constant, publicité par commande inchangée, (6) la perte de volume tolérable à +10 %, à EBITDA constant. *Contrôle : la réponse (6) est entre 25 % et 40 %.*

**Exercice 2 — Le seuil de franco optimal de NØRA** (réponse numérique unique). Canoniques § 1, § 2, § 2.1, § 2.2 ; mix du § 4.2 et hypothèses du § 4.5. Pour 59,00 €, 89,00 € et 109,00 €, calcule (1) la part des commandes qui paient le port, (2) le gain mensuel de marge brute contre le seuil actuel, (3) le nouvel AOV, (4) le gain annuel d'EBITDA, (5) pourquoi 109,00 € est moins bon que 89,00 € malgré un port encaissé plus élevé. *Contrôle : à 89,00 €, retrouve 1 573 440 €/an et 75,81 € d'AOV.*

**Exercice 3 — Ta gamme, référence par référence** (tes chiffres). Reproduis le tableau du § 3.3 : PVC TTC, coefficient, contribution en **convention colis**, écart au nCAC. Puis le rôle de chaque référence parmi les quatre du § 3.1, et le nom de son responsable. *Grille de lecture : si aucune référence ne rembourse son nCAC à la première commande, ton modèle est un pari sur le réachat et doit être piloté comme tel ([E08](E08-retention-et-ltv.md)). Si plus d'une référence porte du budget média, relis le § 3.2.*

**Exercice 4 — Ta hausse de prix de 10 %** (tes chiffres). Sépare tes coûts variables en deux blocs — fixes par commande, proportionnels au prix — puis calcule (1) ta marge brute par commande aujourd'hui, (2) la même à +10 %, (3) ta publicité par commande, (4) ton CM3 par commande dans les deux cas, (5) le nombre de commandes qui te ramène à ton EBITDA actuel, (6) la perte de volume tolérable. Écris ensuite : « je peux perdre X % de mes commandes et gagner autant qu'aujourd'hui. » *Grille de lecture : au-dessus de 20 % de perte tolérable, la seule raison de ne pas augmenter est une élasticité mesurée — pas supposée ([E09](E09-mesure-et-incrementalite.md)).*

**Exercice 5 — Ta facture de remise et ton audit d'accoutumance** (tes chiffres). Sur 12 mois : (1) le total des remises en euros HT et en % du CA HT, (2) la valeur d'un point en EBITDA annuel, (3) la répartition par mécanique — accueil, panier abandonné, créateurs, opérations calendaires, geste SAV, (4) la part de CA réalisée pendant les cinq journées les plus promotionnelles de l'année, (5) l'évolution sur trois ans de la part de clients dont **toutes** les commandes ont été passées en promotion. *Grille de lecture : le point (5) mesure l'accoutumance, et il est presque toujours croissant. Au-delà de 30 % de ta base active, la remise n'est plus un levier — c'est ton prix, et ton prix affiché est une fiction.*

**Exercice 6 — Décision : le prix ou le seuil.** Ta marque ressemble à NØRA au palier P5. Le comité te demande un seul chantier pour le trimestre, les deux options étant exclusives parce qu'elles déplacent le même prix perçu. **Option A :** hausse de 6 % sur toute la gamme, perte de volume estimée à 4 % (estimation interne, non testée). **Option B :** seuil de franco porté de 59,00 € à 89,00 €, hypothèses du § 4.5. Chiffre les deux en EBITDA annuel et en variation d'AOV, tranche, justifie. Ton raisonnement doit contenir les deux gains annuels, les deux nouveaux AOV, le coût d'exécution de chaque option, et la phrase qui dit **laquelle des deux estimations comportementales est la plus fragile et pourquoi**. *Le corrigé donne la réponse, la condition exacte sous laquelle l'autre option devient la bonne, et le test à quatre semaines qui trancherait pour de bon.*

---

*Fin du module E03. Suite : [E04 — Le client dans sa tête](E04-psychologie-du-client.md). E03 a donné les nombres de l'offre ; E04 explique pourquoi un client accepte 99,00 € et refuse 101,00 €, et [E07](E07-funnel-et-conversion.md) donne la page qui le lui fait choisir.*
