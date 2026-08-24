# Cas C09 — Le piège du Black Friday, modélisé

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des
> ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.
> **Ce que tu dois en tirer :** l'opération qui gagne les treize jours perd les douze
> mois, et le classement s'inverse pour des raisons calculables.
> **Modules rattachés :** E03, E06, E08, E09.

---

## 0. Comment ce cas est construit

NØRA est au palier **P4** ([chiffres canoniques](../donnees/chiffres-canoniques.md)
§ 2) : 42 000 commandes/mois, 2 931 600 € de CA TTC, marge brute 60,4 %, MER 2,80,
1 047 000 € de publicité, 230 000 € de fixes. On découpe au jour sur un mois de
30 jours (*convention déclarée*) :

```
Commandes/jour   = 42 000 ÷ 30 = 1 400   (924 nouveaux + 476 réachats, part réachat 34 %)
CA TTC/jour      = 924 × 63,00 + 476 × 83,00 = 97 720 €  (= 1 400 × 69,80 € ✓)
Publicité/jour   = 1 047 000 ÷ 30 = 34 900 €  (MER = 97 720 ÷ 34 900 = 2,80 ✓)
Frais fixes/jour = 230 000 ÷ 30 = 7 666,67 €
```

Les paniers 63,00 € (1ʳᵉ commande) et 83,00 € (réachat) sont canoniques (§ 2). La
période court du **20 novembre au 2 décembre : treize jours.**

**Convention de la remise.** Le canonique § 2.1 en fait un coût variable (8,0 % du CA
HT à P4). Une remise de **prix** n'est pas ça : elle réduit le chiffre d'affaires
encaissé pendant que le COGS, la logistique, le PSP et les retours restent adossés au
**panier catalogue**. Donc ici : le CA TTC affiché est ce que le client paie ; les
coûts physiques (**31,60 %** = 15,0 + 11,5 + 1,60 + 3,5) portent sur le CA HT
catalogue ; la remise se déduit du CA HT ; le taux effectif est marge brute ÷ CA HT
encaissé. Sur un mois ordinaire, elle redonne exactement 60,40 % : c'est le contrôle
de cohérence.

---

## 1. La situation

Les treize mêmes jours en septembre, aux enchères ordinaires, servent d'étalon. Pas
une option de novembre : une règle graduée.

| Référence — 13 jours ordinaires (septembre) | Valeur |
| --- | ---: |
| Commandes (12 012 nouveaux + 6 188 réachats) | 18 200 |
| CA TTC / CA HT — AOV mixte 69,80 € TTC | 1 270 360 € / 1 058 633 € |
| Marge brute 60,40 % — dont par commande | 639 415 € — 35,13 € |
| Budget publicitaire — MER | 453 700 € — 2,80 |
| **Marge de contribution (CM3)** | **185 715 €** |
| **Résultat après 99 667 € de fixes (EBITDA)** | **86 048 €** |

Le comité de novembre a trois propositions. Le directeur commercial veut −20 % sur
tout le site et le budget doublé ; le directeur financier ne veut rien faire ; la
responsable CRM propose une troisième voie.

**Hypothèse de marché, commune aux trois scénarios :** le **CPM monte de 45 %**. Ce
n'est pas une conséquence de ta décision, c'est un prix de marché : tu le paies même
si tu ne fais rien. Doubler ta propre enchère ajoute une pénalité de
saturation, portée à **+58 %** dans le scénario B (*hypothèse : 1,45 × 1,09*). D'où la
loi d'acquisition utilisée partout, où 37,77 € est le nCAC canonique de P4 (§ 2.4) :

```
nCAC_période = 37,77 € × (indice CPM) ÷ (indice de taux de conversion du site)
```

---

## 2. Le diagnostic

**Ce que le dirigeant croyait :** « une remise de 20 %, c'est 20 points de marge en
moins ; c'est cher, mais le volume compense. » Les deux moitiés sont fausses, et elles
se trompent en sens contraire.

**Une remise de 20 % ne coûte pas 20 points de marge.** La même commande (69,80 € TTC
catalogue), en plein tarif puis sous −20 %. Le panier promotionnel porte **+6 % d'unités**
et **+1,8 point de retours** (*hypothèses :* la remise fait ajouter un article, l'achat
impulsif revient plus souvent) ; les codes de bienvenue ne se cumulant pas, la ligne
« remises » tombe de 8,0 % à 2,0 % résiduels.

| Ligne (par commande) | Plein tarif | Sous −20 % |
| --- | ---: | ---: |
| Panier catalogue HT | 58,17 € | 61,66 € |
| **CA HT encaissé** | **58,17 €** | **49,33 €** |
| COGS (15,0 % du catalogue) | −8,73 € | −9,25 € |
| Logistique (11,5 %) | −6,69 € | −7,09 € |
| PSP (1,60 %) | −0,93 € | −0,99 € |
| Retours / SAV (3,5 % → 5,3 %) | −2,04 € | −3,27 € |
| Remises (8,0 % → 2,0 % résiduels) | −4,65 € | −0,99 € |
| **Marge brute** | **35,13 €** | **27,74 €** |
| **Taux de marge brute effectif** | **60,40 %** | **56,23 %** |

**Regarde les deux dernières lignes ensemble.** Le taux ne perd que **4,17 points** —
un tableau de bord qui ne suit que lui dira « la promo s'est bien passée ». Les euros
par commande, eux, perdent **7,39 €, soit 21,0 %** : le dénominateur a rétréci en même
temps que le numérateur. **Piloter une promotion au taux de marge est la façon la plus
fiable de ne pas la voir coûter.**

**Et le volume ne « compense » pas, il déplace.** Trois effets échappent au compte de
résultat de la période : la cohorte acquise en promotion réachète moins et à panier
plus bas, une part des ventes aurait eu lieu en décembre à plein tarif, l'audience
apprend à attendre. Chiffrés au § 5.

---

## 3. Les options

### 3.1 Les hypothèses de chaque scénario, déclarées

| Hypothèse | A — rien | B — −20 % site | C — offre sans remise |
| --- | ---: | ---: | ---: |
| Budget publicitaire | ×1,0 | ×2,0 | ×1,6 |
| Indice CPM | 1,45 | 1,58 | 1,45 |
| Indice de taux de conversion | 1,00 | 2,05 | 1,15 |
| Activation de la base (réachats) | ×1,10 | ×2,90 | ×1,75 |
| Unités par commande | ×1,00 | ×1,06 | ×1,12 (1ʳᵉ) / ×1,08 (réachat) |
| Remises résiduelles (% CA HT) | 8,0 % | 2,0 % | 3,0 % |
| Coût du cadeau au seuil | — | — | 1,10 €/commande |

**A** ne fait rien. Indice de conversion 1,00 : l'intention saisonnière est annulée par
la comparaison avec les concurrents qui remisent (*hypothèse*). **B** remise 20 %
partout et double le budget — sur une audience en intention haute, c'est un choc de
demande : **+105 % de conversion.**

**C** ne touche pas au prix unitaire. Trois briques : un **bundle exclusif** « Rituel
Signature » à 79,00 € TTC, qui n'existe que sur la période (les trois produits du
canonique § 1 plus une trousse) ; un **cadeau au-delà de 79,00 € TTC de panier**
(masque découverte, 1,80 € de COGS, seuil franchi par 61 % des commandes, soit
0,61 × 1,80 = **1,10 €**/commande) ; un **accès anticipé de quatre jours réservé à la
base.**

### 3.2 Le résultat de la période, treize jours

Dérivation du scénario C, à refaire pour les autres :

```
nCAC = 37,77 × 1,45 ÷ 1,15 = 47,62 €   Budget = 453 700 × 1,6 = 725 920 €
Nouveaux = 725 920 ÷ 47,62 = 15 244    Réachats = 6 188 × 1,75 = 10 829
CA TTC = 15 244 × 70,56 € + 10 829 × 89,64 € = 2 046 328 €  →  CA HT 1 705 274 €
Marge brute = 1 705 274 × (1 − 0,3160 − 0,0300) − 26 073 × 1,10 = 1 086 569 €
EBITDA = 1 086 569 − 725 920 − 99 667 = 260 982 €
```

| Période 20/11 – 02/12 | Référence | A | B | C |
| --- | ---: | ---: | ---: | ---: |
| Budget publicitaire | 453 700 € | 453 700 € | 907 400 € | 725 920 € |
| **nCAC de la période** | **37,77 €** | **54,77 €** | **29,11 €** | **47,62 €** |
| Nouveaux clients / réachats | 12 012 / 6 188 | 8 284 / 6 807 | 31 171 / 17 945 | 15 244 / 10 829 |
| **Commandes** | **18 200** | **15 091** | **49 116** | **26 073** |
| AOV mixte TTC | 69,80 € | 72,02 € | 59,62 € | 78,48 € |
| **CA TTC** | **1 270 360 €** | **1 086 873 €** | **2 928 124 €** | **2 046 328 €** |
| CA HT (÷ 1,20) | 1 058 633 € | 905 728 € | 2 440 103 € | 1 705 274 € |
| **MER** | **2,80** | **2,40** | **3,23** | **2,82** |
| Marge brute | 639 415 € | 547 059 € | 1 372 558 € | 1 086 569 € |
| **Taux de marge brute effectif** | **60,40 %** | **60,40 %** | **56,25 %** | **63,72 %** |
| Marge brute par commande | 35,13 € | 36,25 € | 27,95 € | 41,67 € |
| **Marge de contribution (CM3)** | **185 715 €** | **93 359 €** | **465 158 €** | **360 649 €** |
| **Résultat, après 99 667 € de fixes** | **86 048 €** | **−6 308 €** | **365 491 €** | **260 982 €** |
| En % du CA HT | 8,13 % | −0,70 % | 14,98 % | 15,30 % |

**Classement sur la période : B (365 491 €) > C (260 982 €) > A (−6 308 €).**

**A perd de l'argent en ne faisant rien.** Budget normal, CPM +45 % : les mêmes
453 700 € n'achètent plus que 8 284 clients au lieu de 12 012, −31,0 %, et les frais
fixes courent. **Ne pas participer n'est pas neutre : c'est payer les enchères de
Black Friday sans en avoir la conversion.**

**B affiche le meilleur MER de l'année : 3,23 contre 2,80** — et c'est ce qui rend le
piège efficace. Le MER se lit sur le CA TTC ; la remise gonfle le volume plus vite
qu'elle ne rogne le panier, donc le ratio monte pendant que la marge par commande
s'effondre de 35,13 € à 27,95 €. **C fait le meilleur taux d'EBITDA (15,30 %) avec
47 % de commandes en moins que B.**

---

## 4. La décision et l'exécution

C est retenu. Découpage en trois phases, budget quotidien indexé sur les 34 900 € de
référence.

| Phase | Jours | Budget | Nouveaux | Réachats | CA TTC | MER |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 — Accès anticipé, base client seule (e-mail et SMS) | 20–23/11 (4 j) | 83 760 € (×0,60) | 900 | 4 800 | 493 776 € | **5,90** |
| 2 — Ouverture publique du bundle | 24–27/11 (4 j) | 237 320 € (×1,70) | 4 800 | 2 600 | 571 752 € | 2,41 |
| 3 — Pic, cadeau au seuil activé | 28/11–02/12 (5 j) | 404 840 € (×2,32) | 9 544 | 3 429 | 980 800 € | 2,42 |
| **Total** | **13 j** | **725 920 €** | **15 244** | **10 829** | **2 046 328 €** | **2,82** |

**La phase 1 fait 24,1 % du CA de l'opération avec 11,5 % du budget**, à MER 5,90 :
ces 4 800 réachats ne coûtent aucun média, ils coûtent une base d'e-mails constituée
sur douze mois. La commande sans CAC porte la marge brute entière — même mécanisme
qu'en [C02](C02-vallee-de-la-mort.md) § 4.3.

Trois règles écrites avant le 20 novembre : **aucun code de remise n'est créé** (les
codes de bienvenue sont suspendus, le résiduel de 3,0 % couvre parrainage et gestes
SAV) ; **le bundle disparaît le 3 décembre**, parce qu'une offre exclusive qui survit
à sa fenêtre devient un prix, et qu'un prix ne se relève jamais ; **le cadeau est
plafonné** à 16 000 unités — au-delà, le seuil monte, le cadeau ne change pas.

---

## 5. Les résultats

### 5.1 Avant / après — la période contre son étalon

| | Référence (13 j) | C réalisé | Écart |
| --- | ---: | ---: | ---: |
| Commandes — AOV mixte TTC | 18 200 — 69,80 € | 26 073 — 78,48 € | +43,3 % — +12,4 % |
| CA TTC | 1 270 360 € | 2 046 328 € | +775 968 € |
| Taux de marge brute — par commande | 60,40 % — 35,13 € | 63,72 % — 41,67 € | **+3,32 pts** |
| **Résultat de la période** | **86 048 €** | **260 982 €** | **+174 934 €** |
| **En % du CA HT** | **8,13 %** | **15,30 %** | **+7,17 pts** |

C gagne des points de marge **en même temps** que du volume : son levier est le
panier, pas le prix — levier n° 1 du canonique § 7.

### 5.2 La qualité de la cohorte acquise

La partie que presque personne ne fait. Une cohorte de Black Friday n'est pas une
cohorte de septembre, et l'écart se calcule. Trois populations, chacune avec son
indice de réachat (*hypothèses*) : **acheteurs cadeaux** — l'acheteur n'est
pas l'utilisateur — **0,25** ; **chasseurs de promotion**, qui ne rachètent qu'en
promotion, **0,35** ; **clients normaux**, **1,00**.

| Cohorte | Cadeaux | Chasseurs | Normaux | Indice pondéré | Rapport à la base |
| --- | ---: | ---: | ---: | ---: | ---: |
| Base (septembre) | 4 % | 6 % | 90 % | 0,931 | 1,000 |
| A — plein tarif | 14 % | 6 % | 80 % | 0,856 | 0,919 |
| B — acquise à −20 % | 22 % | 34 % | 44 % | 0,614 | 0,660 |
| C — bundle sans remise | 15 % | 9 % | 76 % | 0,829 | 0,890 |

La cohorte canonique de P4 fait **1,24 réachat par client sur douze mois** (§ 3 ;
contrôle : 31,71 € + 1,24 × 41,78 € = 83,52 €, la LTV 12 mois de P4 du § 3.1 — 83,51 €
— à l'arrondi près). On applique l'indice, plus pour C un bonus de **×1,18**
(*hypothèse :* le bundle fait essayer trois produits au lieu d'un, donc trois chances
qu'un rachat s'installe — mécanisme de [C02](C02-vallee-de-la-mort.md) § 4.2). Le
panier de réachat suit l'**ancrage de prix** : le client de B a payé 53,42 €, son
point de référence est descendu.

| Cohorte | Nouveaux clients | Réachats / client (12 m) | Panier de réachat TTC | Contribution / réachat | **Valeur de cohorte (12 m)** |
| --- | ---: | ---: | ---: | ---: | ---: |
| Référence | 12 012 | 1,24 | 83,00 € | 41,78 € | **622 308 €** |
| A | 8 284 | 1,14 | 83,00 € | 41,78 € | **394 560 €** |
| B | 31 171 | **0,82** | **73,87 €** (−11,0 %) | 37,18 € | **950 329 €** |
| C | 15 244 | **1,30** | **85,49 €** (+3,0 %) | 43,03 € | **852 734 €** |

**B achète 2,05 fois plus de clients que C pour 11,4 % de valeur de cohorte en plus.**
Le volume ne compense pas la qualité : il la rattrape à peine.

### 5.3 L'anticipation d'achat

Une part des commandes aurait eu lieu en décembre ou janvier au plein tarif.
*Hypothèses :* **26 % des commandes de B**, **11 % de C**, **0 % de A**. Attention au
raisonnement facile : « ces ventes n'étaient pas incrémentales, donc retirons-les du
gain » est faux sur douze mois, décembre et janvier étant *dans* la fenêtre. Le vrai
coût est le **différentiel de marge** — tu as vendu maintenant, moins cher, ce que tu
aurais vendu plus tard, au prix.

| | Commandes transférées | MB réalisée (vs 35,13 € plein tarif) | Écart | **Coût** |
| --- | ---: | ---: | ---: | ---: |
| A | 0 | 36,25 € | — | **0 €** |
| B | 12 770 | 27,95 € | −7,18 € | **−91 689 €** |
| C | 2 868 | 41,67 € | +6,54 € | **0 €** (retenu) |

Le calcul brut donnerait à C un *gain* de 18 757 €, **retenu à zéro** par prudence.
**L'anticipation n'est coûteuse que si tu avances la vente en baissant le prix** ; au
prix catalogue, elle est neutre.

### 5.4 L'accoutumance

Une part de l'audience apprend à attendre la remise suivante. *Hypothèses sur les six
mois suivants (décembre à mai), à budget constant :* **B −6,0 %** de conversion hors
promotion, **C −1,5 %** (offre exclusive et datée, pas un prix), **A 0 %**. Un client
non acquis vaut, sur ce qu'il reste de la fenêtre, sa contribution de 1ʳᵉ commande plus
la moitié de ses réachats : 31,71 € + 0,5 × 51,80 € = **57,61 €** (*prorata déclaré*).

| | Effet sur la conversion | Clients non acquis sur 6 mois | **Coût** |
| --- | ---: | ---: | ---: |
| A | 0,0 % | 0 | **0 €** |
| B | −6,0 % | 27 720 × 6 × 0,060 = **9 979** | **−574 890 €** |
| C | −1,5 % | 27 720 × 6 × 0,015 = **2 495** | **−143 737 €** |

### 5.5 La valeur sur douze mois — et le renversement

| Ligne | Référence | A | B | C |
| --- | ---: | ---: | ---: | ---: |
| Résultat de la période | 86 048 € | −6 308 € | **365 491 €** | 260 982 € |
| + Valeur de cohorte 12 mois | 622 308 € | 394 560 € | 950 329 € | 852 734 € |
| − Anticipation d'achat | 0 € | 0 € | −91 689 € | 0 € |
| − Accoutumance | 0 € | 0 € | −574 890 € | −143 737 € |
| **VALEUR SUR 12 MOIS** | **708 356 €** | **388 252 €** | **649 241 €** | **969 979 €** |
| Rang sur la période | — | 3ᵉ | **1ᵉʳ** | 2ᵉ |
| Rang sur 12 mois | — | 3ᵉ | 2ᵉ | **1ᵉʳ** |

```
B gagne la période de     365 491 − 260 982 =  104 509 €
B perd les douze mois de  969 979 − 649 241 = −320 738 €
```

**Le classement s'inverse en tête**, et le chiffre le plus dur n'est pas là : B, avec
le meilleur MER de l'année, 49 116 commandes et 2,93 M€ de CA TTC en treize jours,
finit **59 115 € en dessous** des 708 356 € de treize jours ordinaires. **B a travaillé
quatre fois plus pour détruire de la valeur** ; A en détruit plus encore
(−320 104 €) ; seul C dépasse l'étalon, de **261 623 €**.

---

## 6. Ce qui aurait pu mal tourner

**Le bundle cannibalise.** Le panier de 1ʳᵉ commande monte de 12,0 % : le CA net baisse
dès que la conversion perd plus de 10,7 %, puisque 1,120 × (1 − 0,107) = 1,000. **Il
fallait garder le sérum seul en vente, et visible.**

**L'indice de conversion de C se révèle à 1,00, non 1,15.** Les 725 920 € n'achètent
que 725 920 ÷ 54,77 = **13 254 clients** au lieu de 15 244, −13,1 % :

| | C à indice 1,15 | C à indice 1,00 |
| --- | ---: | ---: |
| Nouveaux clients | 15 244 | 13 254 |
| CA TTC | 2 046 328 € | 1 905 914 € |
| Résultat de la période | 260 982 € | 186 645 € |
| Valeur sur 12 mois | 969 979 € | 784 324 € |

C reste devant B (649 241 €) et devant l'étalon (708 356 €). **La conclusion tient à
−13 % d'efficacité sur l'hypothèse la plus fragile.**

**Le concurrent remise à −40 %.** Risque non chiffrable ici : il déplace la référence
de prix de la catégorie. On ne s'aligne pas en novembre.

**Les hypothèses de cohorte sont fausses de moitié.** Si B ne perd que 19 % de
réachats au lieu de 34 % (indice 0,82 → 1,00), sa cohorte vaut 1 158 938 € et sa
valeur 12 mois 857 850 € — toujours **derrière C**, mais devant l'étalon. **Le
classement tient ; le verdict « B détruit de la valeur » ne tient qu'à la moitié de
la dégradation supposée.** Ne le récite pas : mesure-le sur tes cohortes.

---

## 7. Le mécanisme généralisable

> **À retenir :** une remise achète du volume immédiat avec de la marge future. Elle
> est rationnelle quand ce futur n'a pas de valeur, destructrice quand il en a.

**La règle en trois termes.** Une remise agressive vaut le coup si :

```
gain immédiat > dégradation de cohorte + anticipation + accoutumance
```

Scénario B : 365 491 − 86 048 = **+279 443 €** de gain immédiat contre
622 308 − 950 329 + 91 689 + 574 890 = **+338 558 €** de coûts différés. Le compte ne
tombe pas, de 59 115 €.

**Quand elle est rationnelle.** Trois situations, et trois seulement :

1. **Déstockage.** La marchandise a une date — fin de série, saison morte, péremption.
   Sa valeur alternative est la casse : tout prix au-dessus du coût de destruction est
   un gain, sans aucun futur à protéger.
2. **Catégorie sans réachat.** Matelas, valise, vélo électrique : la valeur de cohorte
   à douze mois est proche de zéro, le terme de droite s'annule. Les mêmes 20 % sont
   raisonnables là, suicidaires en cosmétique.
3. **Notoriété payée sciemment.** Acheter une base à perte pour amorcer une courbe de
   réachat — le pari de [C02](C02-vallee-de-la-mort.md). Mais la remise doit alors
   **recruter**, pas récompenser : réservée aux nouveaux, jamais offerte à une base
   qui allait payer le prix.

**Quand elle est destructrice.** Quand ta catégorie a du réachat, que ta base fait un
tiers de tes commandes et que la remise s'applique à tout le monde. Tu paies trois
fois : la marge donnée à ceux qui auraient payé, la cohorte de chasseurs recrutée, le
prix de référence abaissé pour la suite. Le canonique § 8.1 chiffre la sortie :
**2,50 points de marge brute** sur les 4,55 qui séparent P5 de P5+ viennent de la
seule ligne « remises ».

**Le corollaire.** Ne remplace pas la remise par rien : A le montre, −6 308 € sur la
période et le dernier rang sur douze mois. Remplace-la par une raison d'acheter
maintenant qui ne touche pas au prix unitaire — **rareté** (bundle daté), **seuil**
(cadeau au-delà d'un panier), **statut** (accès anticipé). Les trois font monter le
panier, et aucune n'apprend à ton client que ton prix est négociable.

---

## 8. Questions

1. Recalcule le nCAC des trois scénarios avec la loi du § 1, puis leurs nouveaux
   clients. Pourquoi B a-t-il le nCAC le plus **bas** en payant le CPM le plus **haut** ?
2. Une remise de 20 % ne coûte que 4,17 points de taux de marge brute. Pourquoi, et
   quel indicateur fallait-il regarder à la place ?
3. Le MER de B vaut 3,23, contre 2,80 en régime normal et 2,35 au seuil d'équilibre
   EBITDA de P4 (canonique § 2.3). B est-il une bonne opération ? Par un calcul.
4. Calcule la valeur de cohorte 12 mois de B et de C. Combien de clients de plus B
   acquiert-il, et combien d'euros de plus en tire-t-il ?
5. À partir de quel nombre de réachats par client la cohorte de B rattraperait-elle la
   valeur 12 mois de C, tout le reste inchangé ?
6. Déroule la valeur 12 mois des trois scénarios, compare-la aux 708 356 € de treize
   jours ordinaires, et dis ce que ce classement révèle qu'un compte de résultat de
   période ne dit pas.
7. NØRA lance une valise de voyage à 240 € TTC, sans réachat mesurable. La règle du
   § 7 s'applique-t-elle ? Que fais-tu en novembre ?

---

## 9. Corrigé des questions

**1.**

```
A : 37,77 × 1,45 ÷ 1,00 = 54,77 €  →  453 700 ÷ 54,77 =  8 284 clients
B : 37,77 × 1,58 ÷ 2,05 = 29,11 €  →  907 400 ÷ 29,11 = 31 171 clients
C : 37,77 × 1,45 ÷ 1,15 = 47,62 €  →  725 920 ÷ 47,62 = 15 244 clients
```

B paie le clic 58 % plus cher **et** obtient le CAC le plus bas, parce que sa
conversion double : 1,58 ÷ 2,05 = 0,77, soit −23 %. **Le CAC est un rapport, pas un
prix** — et c'est ce qui rend la remise si séduisante en tableau de bord d'acquisition.

**2.** Parce que la remise réduit le numérateur *et* le dénominateur : le CA HT
encaissé tombe de 58,17 € à 49,33 € (−15,2 %) pendant que la marge brute tombe de
35,13 € à 27,74 € (−21,0 %). Le rapport ne perd que la différence,
27,74 ÷ 49,33 = 56,23 % contre 60,40 %, soit **−4,17 points**. L'indicateur à regarder
est la **marge brute en euros par commande** : −7,39 €, soit sur les 49 116 commandes
de B **362 967 €** évaporés à volume donné.

**3.** Non. Le MER est un rapport au CA **TTC** : il ne voit ni le prix unitaire ni la
qualité de la cohorte. À MER 3,23, B fait 465 158 ÷ 49 116 = **9,47 € de CM3 par
commande** ; l'étalon de septembre fait 185 715 ÷ 18 200 = **10,20 €**. **B est
au-dessus de tous ses seuils de MER et sous sa référence en contribution par
commande**, et finit à 649 241 € contre 708 356 € sur douze mois. Un MER record est
compatible avec une destruction de valeur dès qu'il vient d'une baisse de prix.

**4.** B : 31 171 × 0,82 × 37,18 € = **950 329 €.** C : 15 244 × 1,30 × 43,03 € =
**852 734 €.** Écart en clients : 31 171 − 15 244 = **15 927** (+104,5 %) ; écart en
valeur : 950 329 − 852 734 = **97 595 €** (+11,4 %). **B acquiert deux fois plus de
clients pour 11,4 % de valeur de cohorte en plus**, en payant 907 400 € de média
contre 725 920 €. Par client : 950 329 ÷ 31 171 = **30,49 €** pour B,
852 734 ÷ 15 244 = **55,94 €** pour C, soit **1,83 fois plus**.

**5.** Les trois autres lignes de B sont figées à 365 491 − 91 689 − 574 890 =
−301 088 €. Pour atteindre les 969 979 € de C, sa cohorte doit valoir
969 979 + 301 088 = **1 271 067 €**, soit
1 271 067 ÷ (31 171 × 37,18 €) = **1,097 réachat par client** contre 0,82 : une cohorte
promotionnelle **meilleure** que la cohorte plein tarif de A (1,14) alors qu'elle
contient 34 % de chasseurs de promotion. **L'hypothèse à laquelle B devrait croire
pour gagner est celle qu'il vient de rendre fausse.**

**6.**

```
A :  −6 308 + 394 560 −      0 −       0 =  388 252 €   (étalon − 320 104 €)
B : 365 491 + 950 329 − 91 689 − 574 890 =  649 241 €   (étalon −  59 115 €)
C : 260 982 + 852 734 −      0 − 143 737 =  969 979 €   (étalon + 261 623 €)
```

Période : **B, C, A.** Douze mois : **C, B, A.** La période dit que B a gagné de
104 509 € ; les douze mois disent qu'il a perdu de 320 738 €, et même détruit
59 115 € contre treize jours ordinaires. **Un compte de résultat de campagne ne mesure
pas une campagne : il mesure la moitié qui arrange.** La seule unité honnête est la
valeur sur l'horizon complet de la cohorte — module E09.

**7.** Oui, et elle bascule dans l'autre sens. Sans réachat mesurable, la valeur de
cohorte à douze mois tend vers zéro : « dégradation de cohorte » et « accoutumance »
s'annulent presque — ni deuxième achat à protéger, ni prix de référence à défendre
auprès d'un client qui ne reviendra pas. Reste le différentiel d'anticipation, borné à
quelques semaines. **Sur la valise, une remise agressive en novembre est
rationnelle** — à deux conditions : que le coefficient la supporte (canonique § 1 :
sous ×5, une remise de 20 % ramène le coefficient effectif à ×4 et la marge ne finance
plus le CAC), et qu'elle soit **cloisonnée** — page dédiée, gamme distincte, aucun
prix barré sur les soins capillaires. **Deux catégories, deux politiques de prix, deux
audiences publicitaires :** ce que l'algorithme apprend sur l'une contamine ce qu'il
sert sur l'autre.

---

*Fin du cas C09. Suite : [E03](../modules/E03-offre-et-prix.md),
[E08](../modules/E08-retention-et-ltv.md), puis
[C06](C06-test-incrementalite.md).*
