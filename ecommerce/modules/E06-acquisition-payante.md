# Module E06 — L'acquisition payante et les algorithmes

> **Prérequis :** [E01](E01-arithmetique-de-la-marque.md), [E03](E03-offre-et-prix.md), [E04](E04-psychologie-du-client.md), [E05](E05-machine-creative.md).
> **Objet :** savoir ce qu'un système d'enchères calcule réellement, pour décider d'un budget par le coût du prochain client au lieu du tableau de bord d'une régie.
> **Temps de travail :** ~7 h (lecture + exercices)

---

## 0. Pourquoi ce module existe

Tu n'achètes pas des clics. Tu participes à une enchère dont le prix de réserve n'est pas fixé par tes concurrents annonceurs mais par **le contenu organique qui occuperait ta place** : chaque emplacement d'un fil est retiré à une vidéo qu'un utilisateur aurait regardée gratuitement, et la plateforme te le vend au prix de ce qu'elle perd en te le vendant.

Ce qui décide de ton coût n'est donc pas ton enchère, mais **la probabilité que la plateforme estime que ton annonce produira l'événement pour lequel tu paies** — calculée à partir de deux entrées seulement : ce que ta créa provoque, et ce que ton signal lui renvoie. Le reste agit à la marge ou pas du tout.

1. **Une créa qui double le taux de conversion réel divise le coût par acquisition par deux** à inventaire constant, et d'environ 30 % si tu en profites pour acheter du volume (§ 1.2). Aucun autre levier du compte n'a cette taille : c'est pourquoi [E05](E05-machine-creative.md) précède ce module.
2. **Un signal dégradé fait payer plus cher la même performance** : +13,3 % de CPA dans le modèle du § 2.4, soit 1 311 504 € par an au palier P5.
3. **Un tableau de bord de régie n'est pas un instrument d'allocation.** Le plan média canonique revendique 41 364 nouveaux clients quand la marque en acquiert 37 324 ([chiffres canoniques](../donnees/chiffres-canoniques.md) § 5 et § 2.4), et Google y affiche un coût par client de 25,36 € quand il en coûte 79,95 € (§ 5.2).

Zéro tutoriel d'interface : les interfaces changent tous les trimestres, la mécanique de l'enchère et du signal n'a pas bougé depuis dix ans.

---

## 1. La mécanique de l'enchère

### 1.1 Second prix généralisé

Une **enchère de second prix** attribue l'objet au plus offrant et lui fait payer le prix du deuxième : enchérir sa vraie valeur y est optimal, tu ne peux pas gagner en mentant — d'où le fait que les plateformes te demandent ton coût par acquisition cible et pas ton enchère. La version **généralisée** est celle à plusieurs places : chacun paie le minimum qui lui aurait permis de garder son rang. Le mécanisme exact varie et se date — Google Ad Manager a basculé son inventaire display en premier prix en 2019 (annonce publique) — mais **ton coût reste fixé par le rapport entre ta valeur estimée et celle du suivant.**

```
Valeur totale par impression
   =  enchère (ce que tu paies au maximum pour l'événement)
   ×  probabilité estimée que cette impression produise l'événement
   ×  ajustement de qualité / d'engagement estimé

Prix payé par impression   ≈  valeur totale du concurrent suivant
Événements obtenus         =  impressions × taux d'événement RÉEL
Donc  CPA  =  valeur totale du suivant  ÷  taux d'événement RÉEL
```

Retiens la dissociation, elle porte tout le module : **ta valeur estimée décide de l'inventaire que tu gagnes ; ton taux réel décide de ce que cet inventaire coûte par vente.** Quand les deux divergent, tu paies.

### 1.2 Quatre créas, un seul compte

*Hypothèse de modélisation :* l'inventaire adressable par un ensemble de publicités se répartit en cinq tranches, le prix étant la valeur totale du concurrent suivant par mille impressions — 6,25 € (6 % de l'inventaire), 12,50 € (19 %), 15,50 € (25 %), 20,00 € (22 %), 28,00 € (28 %). Le taux d'achat de référence, **0,221 achat pour mille impressions**, n'est pas inventé : c'est le taux impression → commande de la chaîne de [E07 § 1.1](E07-funnel-et-conversion.md) à P5. L'enchère plafond est de 60,00 €, cohérente avec une LTV 12 mois en contribution de 86,75 € (canonique § 3).

| Créa | Taux **estimé** /1000 | Taux **réel** /1000 | Valeur /1000 | Inventaire gagné | CPM payé | **CPA réel** |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| **D** — faible | 0,110 | 0,110 | 6,60 € | 6 % | **6,25 €** | **56,82 €** |
| **A** — référence | 0,221 | 0,221 | 13,26 € | 25 % | 11,00 € | 49,77 € |
| **C** — engagement sans conversion | 0,276 | 0,221 | 16,56 € | 50 % | 13,25 € | **59,95 €** |
| **B** — conversion doublée | 0,442 | 0,442 | 26,52 € | 72 % | **15,31 €** | 34,64 € |
| **B'** — B, enchère ramenée à 30,00 € | 0,442 | 0,442 | 13,26 € | 25 % | 11,00 € | **24,89 €** |

```
A : valeur = 60,00 × 0,221 = 13,26 €/1000 → bat 12,50 et pas 15,50 → tranches 1-2
    CPM = (0,06 × 6,25 + 0,19 × 12,50) ÷ 0,25 = 11,00 €
    CPA = 11,00 ÷ 0,221 = 49,77 €
B : valeur = 26,52 €/1000 → tranches 1 à 4 (72 %)
    CPM = (0,375 + 2,375 + 3,875 + 4,400) ÷ 0,72 = 15,31 €
    CPA = 15,31 ÷ 0,442 = 34,64 €                       soit −30,4 %
B': même créa, enchère 30,00 € → même inventaire que A
    CPA = 11,00 ÷ 0,442 = 24,89 €                       soit −50,0 %, exactement
```

À inventaire constant, doubler le taux de conversion divise le CPA par deux : le numérateur ne bouge pas, le dénominateur double. Dans la vraie vie l'inventaire n'est pas constant — une meilleure créa gagne des enchères qu'elle perdait, donc plus chères, et le gain retombe vers −30 %. **La différence entre les deux, ce sont 47 points d'inventaire en plus** : le bon concept ne fait pas qu'économiser, il te vend du volume que tu n'avais pas le droit d'acheter. C'est le mur de [E11 § 1](E11-passage-a-echelle.md) vu depuis l'enchère.

*Contrôle :* les 49,77 € de la ligne A sont à l'arrondi près le coût par commande issue du clic payant établi indépendamment en [E07 § 1.3](E07-funnel-et-conversion.md), 49,84 €. Sur NØRA, Meta pèse 55 % du plan média à P5, **821 813 €/mois** pour **21 346 nouveaux clients** à **38,50 €** (canonique § 5).

```
Diviser par deux le CAC Meta à volume constant :
   dépense = 21 346 × 19,25 = 410 911 €/mois
   économie = 410 902 €/mois = 4 930 824 €/an
   ÷ EBITDA annuel P5 (4 377 023 €, canonique § 7) = 112,7 %
```

**Un facteur 2 sur la qualité créative de la seule ligne Meta vaut plus que l'EBITDA annuel entier.** Le canonique § 7 le dit en plus petit : −10 % de CAC à volume constant rapporte 1 793 047 € d'EBITDA annuel, soit exactement `1 494 206 × 0,10 × 12`.

> **À retenir :** l'algorithme n'est pas ton adversaire, c'est un système de prix qui te facture ton propre taux de conversion estimé. Tu ne le ruses pas, tu déplaces l'entrée qu'il mesure.

### 1.3 Le CPM n'est pas un coût, c'est un symptôme

Relis la colonne CPM. Le **plus bas**, 6,25 €, appartient à la pire créa : 6 % de l'inventaire, budget indépensable, 56,82 € la commande. Le **plus haut**, 15,31 €, appartient à la meilleure en volume, à 34,64 €. Et deux lignes affichent le **même CPM de 11,00 €** pour des CPA de 49,77 € et 24,89 €.

Un CPM se déplace pour quatre raisons : audience plus disputée, saison plus chère (§ 7.5), format plus valorisé, ou **valeur estimée en hausse qui te donne accès à de l'inventaire premium**. Trois sur quatre sont de bonnes nouvelles — « faire baisser le CPM » est donc un objectif atteignable en dégradant la créa. Le seul enchaînement qui compte est celui de [E07 § 1](E07-funnel-et-conversion.md) : `coût par commande = CPM ÷ (CTR × 1000) ÷ taux de conversion`. Le premier terme se négocie mal avec une régie ; les deux autres se travaillent gratuitement.

---

## 2. Le signal

### 2.1 Ce que la plateforme apprend

Une plateforme ne sait rien de ton produit. Elle observe des couples (impression servie → événement survenu ou non) et ajuste un modèle qui prédit la probabilité d'événement de l'impression suivante. Il lui faut une masse minimale d'observations **par entité qui porte un budget**, parce que c'est à ce niveau que la diffusion est arbitrée. Deux paramètres pilotent tout ce qu'on appelle « le pixel » : **l'événement optimisé** — tu choisis ce que la plateforme cherche à produire, elle le produira, y compris quand ce n'est pas ce que tu veux (§ 3) — et **la fenêtre d'attribution**, c'est-à-dire combien de jours après un clic ou une simple impression un achat est rattaché. Élargis la fenêtre après impression de 1 à 7 jours et le nombre d'achats revendiqués grossit **sans qu'une vente soit créée** ([E09 § 1.3](E09-mesure-et-incrementalite.md)) : c'est une convention comptable, pas une mesure.

### 2.2 Le seuil d'apprentissage, et pourquoi il vaut quelques dizaines

L'ordre de grandeur annoncé par les régies est d'**une cinquantaine de conversions par semaine et par ensemble de publicités**. Ce n'est pas magique, c'est de la statistique : l'erreur-type relative sur un comptage de `k` événements vaut environ `1 ÷ √k`.

| Conversions / semaine | 10 | 26 | **50** | 100 | 200 | 400 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Erreur-type relative | 31,6 % | 19,6 % | **14,1 %** | 10,0 % | 7,1 % | 5,0 % |

À 50 événements, le modèle connaît ton taux à ±14 % près : assez pour te classer correctement dans l'enchère, pas assez pour trancher entre deux créas proches. À 10, il se trompe d'un tiers et diffuse en conséquence, avec ton argent. Pour **toi**, la barre est bien plus haute : distinguer deux ensembles dont les CPA diffèrent de 20 %, à 5 % de risque de faux positif et 80 % de puissance, demande

```
(1,96 + 0,84) × √(2 ÷ k) ≤ ln(1,20) = 0,1823
→ √(2 ÷ k) ≤ 0,0651 → k ≥ 472 conversions par bras
```

**50 pour que la machine apprenne, 470 pour que toi tu décides.** La distance entre les deux explique la moitié des erreurs de gestion de compte (§ 8). *Hypothèse déclarée, ordre de grandeur :* un ensemble maintenu sous le seuil paie son CPA **20 à 35 %** plus cher que le même ensemble stabilisé ; on retient 25 % dans tous les chiffrages qui suivent.

### 2.3 La qualité du signal : quatre chantiers

L'objectif n'est pas « avoir un pixel », c'est que **la plateforme voie la même chose que ton back-office, pour les mêmes personnes.**

- **Le suivi côté serveur.** Le navigateur perd des événements — bloqueurs, onglets fermés, restrictions de suivi intégrées. L'envoi depuis ton serveur à la validation de commande supprime cette perte et transmet ce que le navigateur ignore : remboursement, annulation, commande passée par téléphone.
- **La correspondance des données client.** Un événement rattaché à personne ne sert à rien. Tu transmets des identifiants hachés — e-mail, téléphone, prénom, code postal, identifiant de clic capté à l'arrivée — et la régie te renvoie un score d'appariement. **Un événement non apparié est un événement qui n'existe pas.**
- **La déduplication navigateur / serveur.** Sans identifiant d'événement partagé, le même achat est compté deux fois : le taux estimé gonfle, ton rendement affiché aussi, tu accélères sur un mirage. **Contrôle : si ton rendement plateforme monte de 25 % sans que ton MER bouge, tu n'as pas eu une bonne semaine, tu as un doublon** — le MER se calcule sur le back-office, insensible à la duplication.
- **Le consentement.** Un refus retire l'utilisateur de la mesure navigateur, et selon ton implémentation de la mesure serveur aussi. Le taux d'acceptation dépend du design de la bannière : un des rares chantiers où deux jours de travail déplacent une variable de premier ordre.

Fréquences et seuils de contrôle : tableau de bord du § 10.

### 2.4 Pourquoi un signal dégradé coûte structurellement plus cher

L'intuition fausse veut qu'un signal partiel te fasse « enchérir trop bas » — en second prix, tu compenses en relevant ton plafond et le classement se rétablit. Le vrai coût est ailleurs : **la plateforme optimise sur la population qu'elle mesure, et le morceau manquant n'est pas un échantillon aléatoire.**

*Hypothèses :* 45 % du trafic sur un environnement à suivi restreint, 55 % à suivi complet ; taux de conversion réels 3,10 % et 2,10 % — le premier segment convertit mieux, cas fréquent, pouvoir d'achat plus élevé ; le signal remonte 100 % des conversions du second et 55 % de celles du premier.

```
Ce que la plateforme croit voir :
   restreint : 3,10 % × 0,55 = 1,705 %   ← paraît deux fois moins bon
   complet   : 2,10 %
Elle déplace la diffusion. Hypothèse : de 45/55 vers 15/85.

Taux RÉEL avant : 0,45 × 3,10 + 0,55 × 2,10 = 2,55 %
Taux RÉEL après : 0,15 × 3,10 + 0,85 × 2,10 = 2,25 %
2,25 ÷ 2,55 = 0,882  →  CPA réel × 1,133, soit +13,3 %

Sur la ligne Meta à P5, à volume de clients constant :
   nCAC dégradé = 38,50 × 1,133 = 43,62 €
   surcoût = 21 346 × 5,12 = 109 292 €/mois = 1 311 504 €/an
           = 30,0 % de l'EBITDA annuel (4 377 023 €, canonique § 7)
```

**Ni la créa, ni le ciblage, ni le budget n'ont changé. La population a changé, sans que personne le sache.** Trente pour cent de l'EBITDA annuel, pour un chantier technique de quelques jours.

---

## 3. La valeur d'optimisation

### 3.1 Trois choix, trois entreprises différentes

Optimiser sur l'**achat** maximise le nombre de commandes, donc va chercher l'acheteur le plus facile quel que soit son panier ; sur la **valeur**, la somme des prix payés, donc le gros panier quelle que soit sa marge ; sur la **valeur nette de coût**, la somme des marges de contribution. Les deux premières sont proposées par défaut ; la troisième demande dix lignes de code et personne ne la met en place.

### 3.2 La marge par commande ne se lit pas dans le prix

```
Logistique = 11,0 % du CA HT (canonique § 2.1) sur 3 610 997 € (§ 2.2) = 397 210 €
÷ 60 200 commandes / mois (§ 2)  =  6,60 € par colis
```

**La logistique n'est pas un pourcentage, c'est 6,60 € par colis** — 33,0 % d'un panier de shampooing à 20,00 € HT, 8,0 % d'une cure à 82,50 € HT. Refaisons la contribution de chaque référence (canonique § 1) avec les taux P5 du § 2.1 : PSP 1,55 %, retours et SAV 3,5 %, remises 8,0 %.

| Produit | PVC HT | COGS | Logist. | PSP | Retours | Remise | **Contribution** | **Taux** |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Shampooing 250 ml | 20,00 € | 3,10 € | 6,60 € | 0,31 € | 0,70 € | 1,60 € | **7,69 €** | 38,5 % |
| Masque 200 ml | 24,17 € | 3,60 € | 6,60 € | 0,37 € | 0,85 € | 1,93 € | **10,82 €** | 44,8 % |
| Sérum 50 ml | 32,50 € | 4,80 € | 6,60 € | 0,50 € | 1,14 € | 2,60 € | **16,86 €** | 51,9 % |
| Rituel Complet | 61,67 € | 11,50 € | 6,60 € | 0,96 € | 2,16 € | 4,93 € | **35,52 €** | 57,6 % |
| Cure 3 mois | 82,50 € | 14,40 € | 6,60 € | 1,28 € | 2,89 € | 6,60 € | **50,73 €** | 61,5 % |

*Contrôle :* AOV mixte P5 71,98 € TTC, soit 59,98 € HT ; à 61,5 % de marge brute, `59,98 × 0,615 = 36,89 €`, et [E07 § 4.1](E07-funnel-et-conversion.md) établit indépendamment 36,86 €.

**Le verdict est contre-intuitif : sur la gamme canonique de NØRA, optimiser sur la valeur ne détruit rien.** L'ordre des prix et celui des contributions sont identiques, parce que le coût fixe par colis avantage mécaniquement le gros panier.

### 3.3 Le jour où ça casse

Le problème naît quand tu ajoutes une référence qui rompt cette monotonie. *Hypothèse de scénario, hors gamme canonique :* une brosse chauffante à 129,00 € TTC, COGS 58,00 €, colis plus lourd (8,40 €), retours 8 % — c'est un appareil.

```
PVC HT 107,50 − COGS 58,00 − logistique 8,40 − PSP 1,67
              − retours 8,60 − remises 8,60  =  contribution 22,23 €  →  20,7 %
```

**129,00 € de prix pour 22,23 € de marge, contre 99,00 € pour 50,73 €.** Une optimisation sur la valeur préfère l'appareil sans hésiter — c'est exactement ce que tu lui as demandé. *Hypothèse :* elle déplace 12 % des commandes de la cure vers l'appareil, soit 7 224 par mois.

```
Perte de contribution = 7 224 × 28,50 = 205 884 €/mois
Gain de CA TTC        = 7 224 × 30,00 = 216 720 €/mois
Nouveau MER   = 4 549 916 ÷ 1 494 206 = 3,05   (contre 2,90, canonique § 2.3)
Nouvel EBITDA = 364 752 − 205 884 = 158 868 €/mois
En % du CA HT = 158 868 ÷ 3 791 597 = 4,2 %    (contre 10,1 %)
Coût annuel   = 2 470 608 €  =  56,4 % de l'EBITDA
```

**Le MER monte de 5,2 %, le chiffre d'affaires de 216 720 € par mois, et la marge nette tombe de 10,1 % à 4,2 %.** Tous les tableaux de bord publicitaires affichent une amélioration. C'est la mécanique du cas [C04](../etudes-de-cas/C04-scale-qui-detruit-la-marge.md).

### 3.4 La correction, et ce qu'elle fait à tes seuils

Tu transmets comme valeur de l'événement, non le prix payé, mais **la marge de contribution** : `montant HT − COGS − logistique du colis − frais de paiement − provision de retour − remise consentie`. Trois précautions : jamais zéro ni négatif, les modèles les ignorent ou pire (plancher à 1,00 €) ; le jour de la bascule tes séries historiques meurent, donc recalcule tes seuils le même jour et écris-les avant ; et envoie l'événement de remboursement si la régie l'accepte, c'est le seul moyen d'apprendre au modèle à éviter les acheteurs qui retournent.

Le bénéfice caché est la lisibilité du seuil : le rendement affiché devient un rendement en contribution.

```
Rendement actuel = 2 218 957 ÷ 1 494 206 = 1,49       (canonique § 2.2)
Seuil CM3 = 0     : 1,00
Seuil EBITDA = 0  : (1 494 206 + 360 000) ÷ 1 494 206 = 1,24
```

Trois nombres — 1,00, 1,24, 1,49 — qui ne bougent pas quand le mix produit bouge. Le MER de 2,90, lui, se déplace à chaque changement de panier sans rien dire de ta rentabilité : c'est le piège du canonique § 2.2, le MER se calcule sur du TTC et la marge sur du HT.

---

## 4. La structure de compte

### 4.1 Trente ensembles à petit budget apprennent moins bien qu'un seul

Démonstration au palier P2, là où la question se pose vraiment.

```
Budget P2 = 104 636 €/mois (canonique § 2.2) = 24 147 €/semaine (§ 6 ✓)
nCAC P2 = 30,78 € (§ 2.4)  →  24 147 ÷ 30,78 = 785 clients / semaine
Plafond théorique d'ensembles = 785 ÷ 50 = 15,7
```

*Hypothèse de répartition :* la diffusion suit une loi 70/30 — 6 ensembles sur 30 captent 70 % du budget.

| Groupe | Ensembles | Budget/sem. | Conversions/sem. | Par ensemble | Au-dessus du seuil ? |
| --- | ---: | ---: | ---: | ---: | --- |
| Tête | 6 | 16 903 € | 549 | **91,5** | oui |
| Queue | 24 | 7 244 € | 235 | **9,8** | non |

```
CPA de la queue en apprentissage = 30,78 × 1,25 = 38,48 €
Clients : 7 244 ÷ 38,48 = 188   au lieu de   7 244 ÷ 30,78 = 235
Perte = 47/semaine = 204 clients/mois
Contribution nette par client à P2 = 70,70 − 30,78 = 39,92 € (canonique § 3.1)
Perte = 204 × 39,92 = 8 143 €/mois     EBITDA mensuel P2 = −19 838 €
8 143 ÷ 19 838 = 41,0 %
```

**Quarante et un pour cent de la perte mensuelle de NØRA en traction est une faute d'architecture de compte, pas une faute de marché.** Et la même structure interdit la décision : à 9,8 conversions par semaine l'erreur-type sur le CPA est de 32 % (§ 2.2), soit 48 semaines pour distinguer honnêtement le meilleur du pire de ces 24 ensembles.

**La règle :** le nombre d'entités portant un budget est plafonné par tes conversions hebdomadaires divisées par 50, puis divisé encore par deux pour l'inégalité de diffusion — sept ou huit à P2, pas trente. À P5, avec 8 613 nouveaux clients par semaine, la contrainte se desserre mais se déplace vers les **marchés** et les **langues**, qui fragmentent réellement.

### 4.2 Les campagnes automatisées

Une campagne automatisée — Advantage+ chez Meta, Smart+ chez TikTok, Performance Max chez Google — **fusionne les pools** (prospection, reciblage, clients existants dans la même enchère), **choisit les combinaisons** créa × audience × placement à ta place, ce qui est presque toujours mieux que ton intuition parce qu'elle mesure et pas toi, et **te retire la capacité de retenir un segment**, donc de mesurer.

Le premier point décide de ton résultat : il gouverne combien de ton budget rachète tes propres clients, et le seul vrai levier est le **plafond de clients existants**. *Hypothèses :* la campagne porte 55 % du budget Meta, soit 452 000 €/mois ; AOV d'un client existant 85,05 € TTC, d'un nouveau 64,00 € (dérivés au § 4.4).

| Plafond de clients existants | Achats déclarés | dont existants | dont nouveaux | CA déclaré | **Rendement affiché** | **nCAC réel** |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 40 % | 14 100 | 5 640 | 8 460 | 1 021 122 € | **2,26** | 53,43 € |
| 15 % | 12 400 | 1 860 | 10 540 | 832 753 € | **1,84** | **42,88 €** |

```
+2 080 nouveaux clients/mois × 86,75 € de LTV 12 mois = 180 440 €/mois
                        = 2 165 280 €/an = 49,5 % de l'EBITDA annuel
```

**Tu baisses ton rendement affiché de 18,6 % et tu gagnes 2 165 280 € de contribution par an.** C'est le module en une ligne : quand le tableau de bord de la régie et le compte de résultat divergent, c'est le compte de résultat qui a raison.

**Elle bat une structure manuelle** quand ton signal est propre (§ 2.3), ton débit créatif élevé (57 concepts/semaine à P5, canonique § 6) et ton catalogue large : elle a plus de combinaisons à explorer que toi et les explore plus vite. **Elle ne la bat pas** quand ton volume de conversions est trop faible pour qu'elle apprenne (§ 4.1), quand tu dois protéger une zone de mesure ([E09 § 5](E09-mesure-et-incrementalite.md)), quand une offre en rupture doit être coupée en quelques heures, ou quand ton catalogue contient une référence à faible marge que le modèle ira chercher (§ 3.3).

### 4.3 Prospection et reciblage : une séparation qui s'efface

**Les campagnes automatisées fusionnent les pools par construction** : maintenir deux campagnes séparées à côté revient à les mettre en concurrence dans la même enchère, sur les mêmes personnes, en payant pour enchérir contre soi-même. **Le pool de reciblage rétrécit et vieillit** : il ne contient que les visiteurs identifiables — 677 250 personnes pour NØRA à P5 quand le site voit 2 408 000 sessions par mois (§ 5.3). **Et le reciblage est un sous-produit de la prospection, pas un canal** : son volume est fixé par le trafic que la prospection a produit ; tu ne peux pas en faire plus, seulement en faire plus **souvent** aux mêmes personnes.

Reste vrai : la récupération de panier à J+1 et J+3 fonctionne, mais comme opération de CRM et non comme canal ([E07 § 5.5](E07-funnel-et-conversion.md)). Et la séparation redevient obligatoire dès que tu veux **mesurer** — tu ne peux pas estimer un coût d'acquisition si ton budget rachète tes clients.

### 4.4 Les exclusions

Chiffrons d'abord ce qu'on exclut, au palier P5.

```
Commandes de réachat = 60 200 − 37 324 = 22 876 / mois
Contribution du réachat  = 22 876 × 43,53 € (canonique § 3)  =   995 792 €
Contribution 1ᵉʳˢ achats = 37 324 × 32,77 € (§ 2.4)          = 1 223 108 €
Total = 2 218 900 €   contre marge brute canonique (§ 2.2) = 2 218 957 €

CA de réachat = 4 333 196 × 44,9 % (§ 8) = 1 945 605 € TTC
AOV réachat = 1 945 605 ÷ 22 876 = 85,05 €
AOV 1ʳᵉ cmd = (4 333 196 − 1 945 605) ÷ 37 324 = 63,97 €
```

Écart de 57 € sur 2,2 M€ : le modèle est bouclé, et il produit au passage les deux AOV du § 4.2 — dont les 64,00 € utilisés par [E09 § 2.1](E09-mesure-et-incrementalite.md) et dérivés en [E01](E01-arithmetique-de-la-marque.md).

| Exclusion | Verdict | Pourquoi |
| --- | --- | --- |
| Acheteurs des 30 derniers jours, sur les campagnes d'acquisition | **Sert** | Sinon tu mesures du réachat payant, pas de l'acquisition |
| Zone de retenue d'un test d'incrémentalité | **Sert** | C'est la condition du test ([E09 § 5](E09-mesure-et-incrementalite.md)) |
| **Tous les acheteurs, sur toutes les campagnes** | **Nuit** | Un acheteur de l'an dernier n'est plus un client, c'est ton meilleur prospect |
| Exclusions croisées entre douze ensembles | **Nuit** | Chacune rétrécit l'audience et pousse la fréquence (§ 5.3) |
| Visiteurs récents, sur une campagne large | **Nuit** | Tu t'interdis la poche qui convertit le mieux |
| Similarité entraînée sur « tous les acheteurs » | **Nuit** | Elle apprend la moyenne ; entraîne-la sur les 20 % de meilleure LTV ([E08](E08-retention-et-ltv.md)) |

**Exclure sert à isoler une mesure, pas à optimiser une diffusion.** Chaque fois que tu exclus pour « éviter de payer un client qui serait revenu », tu retires du signal à la machine et tu perds plus en apprentissage que tu ne gagnes en dépense évitée.

### 4.5 La règle de modification de budget

L'ordre de grandeur enseigné partout — **+20 à +30 % toutes les 48 à 72 heures** — n'est pas une superstition, mais sa justification est mal comprise. Une variation de budget oblige le système de diffusion à re-résoudre son problème de rythme : à quel prix acheter, à quelle vitesse, sur quel inventaire. Il repasse en exploration. Si l'entité était très au-dessus du seuil du § 2.2, l'épisode dure quelques heures ; si elle était près du seuil, elle repart de zéro.

```
Meta à P5 : 821 813 ÷ 30,4 = 27 033 €/jour. Tu doubles d'un coup à 54 066 €.
Hypothèse : 4 jours d'apprentissage à +30 % de CPA.
   Dépense = 54 066 × 4 = 216 264 €
   Clients à 38,50 × 1,30 = 50,05 €  →  4 321
   Clients au CPA stabilisé          →  5 617      Manque : 1 296
   Contribution 12 mois non créée = 1 296 × (86,75 − 38,50) = 62 532 €
```

62 532 € pour gagner trois jours. Et surtout, **la règle ne te ralentit pas** : `1,25^10 = ×9,31`, une multiplication du budget par 9,3 en trente jours. Si elle te gêne, ton problème n'est pas la règle mais ta machine créative (canonique § 6) ou ton cash (canonique § 4, [E10](E10-cash-et-operations.md)).

**Sa date de péremption.** La règle est née à l'époque des budgets portés par l'ensemble de publicités ; avec un budget porté par la campagne et une structure consolidée, la re-résolution est bien moins brutale. Le critère n'est donc pas la règle mais le mécanisme : **si l'entité fait déjà cinq à dix fois le seuil de conversions, le saut est indolore ; si elle est au seuil, il est fatal.**

---

## 5. Les canaux

### 5.1 TikTok : ce qui diffère réellement de Meta

**L'intention de session.** L'utilisateur est venu pour être diverti : ton annonce ne concurrence pas les autres annonces, elle concurrence **la vidéo suivante**, qui est gratuite et bonne. Le coût d'un balayage est nul, la fenêtre d'accroche se compte en une seconde, et la valeur d'usage que la plateforme perd en te vendant l'emplacement est élevée — ce qui remonte dans le terme de qualité du § 1.1.

**La durée de vie des créas**, que le canonique § 6 permet de dériver :

```
Gagnants en rotation à P5 = 23 ; nouveaux gagnants = 5,2 / semaine
Durée de vie moyenne = 23 ÷ 5,2 = 4,4 semaines

Hypothèse : 6 semaines sur Meta, 2,5 sur TikTok.
Gagnants attribués à TikTok au prorata de 15 % du budget = 3,5
Besoin = 3,5 ÷ 2,5 = 1,40 gagnant / semaine
Part de la charge créative totale = 1,40 ÷ 5,2 = 26,9 %
```

**TikTok pèse 15 % du budget et consomme 26,9 % de la charge créative.** À `51 722 ÷ 57 = 907 €` de média par concept testé (canonique § 6), c'est le vrai coût du canal, et il ne se lit dans aucune interface : [E05](E05-machine-creative.md).

**Le son.** Une annonce sans son sur TikTok n'est pas une annonce mal faite, c'est une annonce absente : le modèle d'engagement est bâti sur la durée de visionnage, portée par le son. Corollaire coûteux — les droits musicaux d'un contenu organique ne sont pas ceux d'un contenu sponsorisé.

**Les publications sponsorisées depuis les comptes de créateurs.** Elles ne marchent **pas** parce que « l'engagement fait baisser le CPM » : relis la ligne **C** du § 1.2 — une créa qui gonfle son taux estimé sans améliorer son taux réel gagne 50 % de l'inventaire au lieu de 25 %, paie 13,25 € de CPM au lieu de 11,00 €, et voit son CPA réel monter à **59,95 €**. **Un bon taux d'engagement qui ne se traduit pas en ventes ne fait pas économiser : il fait acheter plus cher**, et la plateforme révise son estimation en quelques jours, ce qui donne à l'appât à engagement une demi-vie qui se compte en jours. Elles marchent pour trois raisons réelles : la preuve sociale visible dans l'unité publicitaire relève le taux de conversion **réel** ; le même asset reçoit une diffusion non payée ; et le créateur produit du volume créatif que ton studio ne produirait pas.

**TikTok est rentable** quand le produit se démontre visuellement en quelques secondes, que le prix n'exige pas une longue délibération et que la machine créative encaisse une rotation deux fois plus rapide. **Il ne l'est pas** quand l'offre exige une preuve écrite, quand le panier est élevé à cycle long, et surtout quand la production ne suit pas — un compte TikTok sans renouvellement se dégrade en trois semaines quand un compte Meta tient trois mois sur la même erreur.

### 5.2 Google : quatre briques, une incrémentalité très inégale

Google n'est pas un canal, c'est quatre mécanismes qui n'ont en commun que leur facture. Le canonique § 5 les regroupe en deux lignes — 164 363 € sur Search + Shopping à 19,00 € le client, 119 536 € sur PMax, Demand Gen et YouTube à 47,00 € — commode pour un plan média, trompeur pour une décision. *Hypothèse de découpage,* cohérente avec [E09 § 6.2](E09-mesure-et-incrementalite.md) qui pose 38 % du Search + Shopping sur les requêtes de marque :

| Brique | Part | Budget/mois | nCAC affiché | Clients affichés |
| --- | ---: | ---: | ---: | ---: |
| Recherche sur la marque | 38 % | 62 458 € | 12,00 € | 5 205 |
| Recherche générique | 27 % | 44 378 € | 34,00 € | 1 305 |
| Shopping | 35 % | 57 527 € | 26,87 € | 2 141 |
| **Search + Shopping** | 100 % | **164 363 €** | **19,00 €** | **8 651** |

*Contrôle :* `164 363 ÷ 8 651 = 19,00 €`. Le découpage respecte le canonique.

**La recherche sur la marque, le cas d'école.** Quelqu'un tape « nøra sérum densité » : il te connaît déjà, donc quelqu'un a déjà payé pour ça — Meta, TikTok, une amie, un article. La question n'est pas « cette annonce a-t-elle converti » mais « cette personne serait-elle arrivée par le résultat naturel juste en dessous ». [E09 § 6.2](E09-mesure-et-incrementalite.md) chiffre le cas : rendement affiché 4,00, incrémentalité 8 %, rendement incrémental **0,32**, solde **−52 223 € par mois**.

**Comment on le teste** — le seul test de ce module que tu peux lancer cette semaine : coupe tes mots-clés de marque sur une partie géographique de ton territoire, garde-les ailleurs, et compare le chiffre d'affaires **total**, pas le chiffre d'affaires Google, sur cinq à six semaines (dimensionnement en [E09 § 5](E09-mesure-et-incrementalite.md)). **Et la réponse dépend de la concurrence** : si personne n'enchérit sur ton nom, le résultat naturel occupe la première place et l'annonce paie un clic gratuit ; si un concurrent, un revendeur non autorisé ou un site de codes promo enchérit dessus, la première place lui appartient et une part de ta demande part chez lui. **L'incrémentalité de ta recherche de marque n'est pas une propriété de ta marque mais du paysage concurrentiel, et elle change sans prévenir** — d'où la décision « couper, surveiller mensuellement, réactiver dès qu'un concurrent apparaît ». *Fait public :* le seul essai à grande échelle publié reste celui d'eBay, rendement à court terme statistiquement indiscernable de zéro après coupure de ses mots-clés de marque sur une partie des États-Unis (Blake, Nosko & Tadelis, *Consumer Heterogeneity and Paid Search Effectiveness*, Econometrica, 2015) — sa notoriété n'est pas la tienne, le résultat n'est pas transposable, le mécanisme l'est.

**La recherche générique** est l'inverse : la personne décrit son problème, pas ton produit ; elle n'est pas venue pour toi, elle est captable. Brique la plus incrémentale, et la plus chère au clic. **Shopping** est ambigu : il capte de la comparaison de prix en fin de parcours et cannibalise en partie ta marque et ton résultat naturel.

**Performance Max et la boîte noire.** Une campagne PMax mélange search de marque, search générique, Shopping, YouTube, Display et Gmail dans une enveloppe unique et te rend un chiffre agrégé. La conséquence est mécanique : **plus la part de trafic de marque est élevée dans le mélange, meilleur est le rendement affiché et plus faible est l'incrémentalité réelle.** Une campagne non contrainte dérive naturellement vers le trafic de marque, parce que c'est là que son propre modèle trouve les conversions les moins chères. Elle optimise exactement ce que tu lui as demandé, et ce n'est pas ce que tu veux.

```
Hypothèse : 35 % des conversions PMax sur intention de marque (8 % d'incrémentalité),
            65 % sur découverte (60 %)
Taux = 0,35 × 0,08 + 0,65 × 0,60 = 0,418  →  2 543 × 0,418 = 1 063 clients
CAC incrémental = 119 536 ÷ 1 063 = 112,45 €   ;   86,75 ÷ 112,45 = 0,77
```

On exclut le trafic de marque — mots-clés négatifs de marque, séparation des flux produits — puis on remesure. **Si le rendement s'effondre après exclusion, il n'a jamais existé.**

| Brique | Budget/mois | Incrémentalité *(hyp.)* | Clients incrém. | **CAC incrémental** | LTV 12 m ÷ CAC | Verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Recherche de marque | 62 458 € | 8 % | 416 | **150,14 €** | 0,58 | détruit |
| Recherche générique | 44 378 € | 80 % | 1 044 | **42,51 €** | 2,04 | garder |
| Shopping | 57 527 € | 48 % | 1 028 | **55,96 €** | 1,55 | surveiller |
| PMax / Demand Gen / YT | 119 536 € | 41,8 % | 1 063 | **112,45 €** | 0,77 | réparer, sinon couper |
| **Google, ensemble** | **283 899 €** | — | **3 551** | **79,95 €** | 1,08 | — |

Et la comparaison qui tue la lecture naïve du plan média. *Hypothèses :* 88 % du budget Meta en prospection à 50 % d'incrémentalité, 12 % en reciblage à 22 % (découpages de [E09 § 6.3](E09-mesure-et-incrementalite.md)).

```
Meta : 18 784 affichés × 0,50 = 9 392  +  2 562 × 0,22 = 564   →  9 956
CAC incrémental Meta = 821 813 ÷ 9 956 = 82,54 €

Rapport affiché     : 38,50 ÷ 19,00 → Google paraît 2,03 fois meilleur
Rapport incrémental : 79,95 ÷ 82,54 → Google coûte 0,97 fois Meta
```

**Tout l'avantage apparent de Google est de l'attribution.** Contrôle global, en étendant les hypothèses à TikTok 60 %, influence 55 %, autres 62 % : `9 956 + 3 056 + 3 551 + 1 604 + 505 = 18 672` clients incrémentaux pour 37 324 réels, soit **50,0 %** — contre les 44,0 % mesurés à P4 par [E09 § 6.1](E09-mesure-et-incrementalite.md), écart cohérent puisqu'à P5 la marque et sa base de trafic naturel sont plus grandes. **Un client sur deux serait arrivé sans publicité**, et ce chiffre ne se lit dans aucune interface.

**La règle de lecture de Google, en une phrase :** il récolte une demande créée ailleurs, donc son rendement apparent est structurellement flatteur, et sa vraie valeur ne se mesure qu'en coupant — [E09](E09-mesure-et-incrementalite.md).

### 5.3 Le reciblage : le rendement le plus mensonger du compte

Le reciblage montre une annonce à quelqu'un qui a déjà visité ton site. Par construction, il sélectionne les personnes les plus proches de l'achat : il ne crée pas la demande, il se place devant. Sa saturation est plus parlante que son rendement.

```
Sessions / mois à P5 (E07 § 1.2)                     = 2 408 000
Hypothèse : 1,6 session par visiteur → 1 505 000 visiteurs uniques
Hypothèse : 45 % ré-adressables (consentement, suivi, applications)
Pool                                                 =   677 250 personnes
Budget de reciblage (E09 § 6.3, 12 % de Meta)        =    98 618 €/mois
À un CPM de 11,00 € (E07 H1)                         = 8 965 273 impressions
Fréquence = 13,2 par mois = 3,06 par semaine
```

Le seuil d'alerte de [E11 § 1.4](E11-passage-a-echelle.md) est de 3,5 par semaine **en prospection large**, sur des gens qui ne te connaissent pas. Tu es à 3,06 sur des gens qui te connaissent et n'ont pas acheté : tu ne les convaincs pas, tu les uses. Rendement affiché 6,50, incrémentalité 22 %, soit **1,43** contre un seuil de contribution de 1,95 (canonique § 2.3) : **−26 402 € par mois**.

**Estimer sa part incrémentale**, de la plus grossière à la plus honnête. *(a)* **Coupure sèche** : deux semaines sans reciblage, et tu regardes le chiffre d'affaires **total** ; contaminé par la saison, mais si le total ne bouge pas plus que ton bruit hebdomadaire, tu as ta réponse. *(b)* **Retenue d'audience** : exclus 20 % du pool, tirés au hasard et non par comportement, compare les taux d'achat sur trente jours — la seule des trois qui produit un chiffre défendable. *(c)* **Borne haute par le délai** : la part de tes acheteurs jamais reciblés qui achète dans les 7 jours estime directement ce que le reciblage n'a pas créé.

---

## 6. La répartition du budget

### 6.1 Ce que dit le plan média canonique, et ce qu'il ne dit pas

| Canal | Part | Budget/mois | nCAC canal | Clients/mois |
| --- | ---: | ---: | ---: | ---: |
| Meta | 55 % | 821 813 € | 38,50 € | 21 346 |
| TikTok | 15 % | 224 131 € | 44,00 € | 5 094 |
| Google Search + Shopping | 11 % | 164 363 € | 19,00 € | 8 651 |
| Google PMax / DG / YouTube | 8 % | 119 536 € | 47,00 € | 2 543 |
| Influence + affiliation | 8 % | 119 536 € | 41,00 € | 2 916 |
| Pinterest, Snap, native, presse | 3 % | 44 826 € | 55,00 € | 815 |
| **Total** | 100 % | **1 494 206 €** | — | **41 364** |

*(chiffres canoniques § 5)*

```
41 364 revendiqués − 37 324 réels (§ 2.4) = 4 040 clients = 10,8 %
nCAC apparent = 1 494 206 ÷ 41 364 = 36,12 €
nCAC réel     = 1 494 206 ÷ 37 324 = 40,03 €
Écart = 3,91 € par client → 1 751 244 € par an d'acquisition invisible
```

Ni bug ni malhonnêteté : six régies voient le même acheteur, six régies le comptent. La sur-attribution monte avec le nombre de canaux, d'où la propriété la plus perverse du métier — **ton coût d'acquisition affiché baisse le mois où tu ajoutes un canal qui ne crée aucune vente** ([E09 § 1.4](E09-mesure-et-incrementalite.md)). Conséquence pratique : les 19,00 € de Google et les 38,50 € de Meta ne mesurent pas la même chose, et le § 5.2 a montré que l'écart s'évapore une fois corrigé.

### 6.2 On alloue au CAC marginal, pas au CAC moyen

Le CAC moyen d'un canal dit si tu **as bien fait** d'y mettre ce que tu y as mis. Il ne dit rien de l'euro suivant, qui est pourtant le seul que tu peux encore décider. *Hypothèses de mesure,* issues de tests d'augmentation de budget par canal ([E09 § 5.1](E09-mesure-et-incrementalite.md)) :

| Canal | Budget actuel | nCAC moyen | **CAC marginal** | Rapport |
| --- | ---: | ---: | ---: | ---: |
| Google Search + Shopping | 164 363 € | 19,00 € | **41,00 €** | ×2,16 |
| Influence + affiliation | 119 536 € | 41,00 € | **52,00 €** | ×1,27 |
| Meta | 821 813 € | 38,50 € | **52,93 €** | ×1,37 |
| TikTok | 224 131 € | 44,00 € | **58,00 €** | ×1,32 |
| Pinterest, Snap, native | 44 826 € | 55,00 € | **88,00 €** | ×1,60 |
| Google PMax / DG / YT | 119 536 € | 47,00 € | **96,00 €** | ×2,04 |

Le 52,93 € de Meta n'est pas une hypothèse : il est dérivé de la courbe du § 7.2. Deux lectures. Google, le moins cher en moyenne, est celui dont le coût marginal double le plus vite — la signature d'un canal de **récolte**, qui épuise une demande finie. Et PMax, médian en moyenne, est le plus cher à la marge.

**La méthode, en quatre gestes.** **(1) Fixe le plafond** — le CAC marginal maximal est la LTV que ta trésorerie sait financer : 86,75 € à 12 mois, 118,96 € à 24 mois si ton BFR le permet (2 264 655 € à P5, canonique § 4, [E10](E10-cash-et-operations.md)). **(2) Égalise les marginaux** : tant que deux canaux diffèrent, déplacer un euro du plus cher vers le moins cher achète des clients **à budget total inchangé** ; l'optimum est atteint quand ils sont tous égaux. **(3) Sors le budget de test du calcul** : les 15 % du canonique § 6, soit 224 128 €/mois — autant que la ligne TikTok entière — n'ont pas de CAC marginal, ils achètent une option sur les gagnants de la semaine 12. **(4) Refais-le sur l'incrémental** ([E09 § 6.4](E09-mesure-et-incrementalite.md)).

### 6.3 La réallocation, chiffrée

*Hypothèse :* les CAC marginaux s'appliquent par tranche de 40 000 €, chaque tranche étant plus chère que la précédente.

| Mouvement | Tranche | CAC marginal | Clients |
| --- | ---: | ---: | ---: |
| Retiré de PMax | 40 000 € | 96,00 € | −417 |
| Retiré de PMax | 40 000 € | 89,00 € | −449 |
| Retiré de « autres » | 40 000 € | 88,00 € | −455 |
| Ajouté à Google Search | 40 000 € | 41,00 € | +976 |
| Ajouté à Google Search | 40 000 € | 49,00 € | +816 |
| Ajouté à l'influence | 40 000 € | 52,00 € | +769 |
| **Solde** | **0 €** | — | **+1 240** |

```
1 240 × 86,75 € = 107 570 €/mois = 1 290 840 €/an = 29,5 % de l'EBITDA annuel
```

**Zéro euro de budget en plus, 1 240 nouveaux clients par mois.** Et le mouvement n'est pas fini : après réallocation la prochaine tranche de Google est à 58,00 € et ce qui reste sur PMax à environ 82,00 €. Deux précautions honnêtes : ces marginaux sont **attribués**, donc optimistes — la version incrémentale du § 5.2 place Shopping à 55,96 € et PMax à 112,45 €, ce qui conserve la direction et divise l'ampleur ; et la contribution arrive sur douze mois, `1 240 × 32,77 = 40 635 €` atterrissant à la première commande, le reste suivant les cohortes ([E08](E08-retention-et-ltv.md)).

---

## 7. Le passage à l'échelle et la saturation

### 7.1 Vertical contre horizontal

**Vertical** : plus de budget sur les mêmes audiences, marchés et placements — simple, immédiat, à rendement décroissant garanti, puisque tu achètes de la fréquence et non de la portée. **Horizontal** : nouveaux placements, formats, langues, audiences de similarité, marchés — plus lent à mettre en place, **à rendement quasi constant tant qu'il reste des audiences vierges**.

### 7.2 La courbe de saturation de Meta

*Hypothèse de modélisation,* construite pour passer exactement par le point canonique (821 813 € → 21 346 clients → 38,50 €) :

| Budget Meta / mois | Nouveaux clients | nCAC moyen | **CAC marginal** |
| ---: | ---: | ---: | ---: |
| 500 000 € | 14 620 | 34,20 € | — |
| 650 000 € | 18 100 | 35,91 € | **43,10 €** |
| **821 813 €** *(canonique)* | **21 346** | **38,50 €** | **52,93 €** |
| 1 000 000 € | 24 000 | 41,67 € | **67,14 €** |
| 1 200 000 € | 26 300 | 45,63 € | **86,96 €** |

```
650 000 → 821 813     : 171 813 ÷ 3 246 = 52,93 €
821 813 → 1 000 000   : 178 187 ÷ 2 654 = 67,14 €
1 000 000 → 1 200 000 : 200 000 ÷ 2 300 = 86,96 €
Plafond = LTV 12 mois en contribution = 86,75 € (canonique § 3)
```

**La dernière tranche coûte 86,96 € pour une LTV de 86,75 € : la saturation de Meta se situe à 1,2 M€ par mois, et le tableau de bord ne le dira jamais** — à ce niveau le nCAC moyen affiche encore 45,63 €, soit un LTV/CAC de 1,90 qui passerait pour acceptable dans les trois quarts des comptes. **La courbe de saturation, et non le budget disponible, est la vraie limite de croissance d'un compte.**

*Contrôle d'élasticité :* avec `clients = k × budget^α`, `α = ln(1,7989) ÷ ln(2,40) = 0,67`, entre l'élasticité multi-marchés de 0,85 ([E11 § 1.2](E11-passage-a-echelle.md)) et celle à audience constante de 0,55 ([E11 § 1.3](E11-passage-a-echelle.md)). Cohérent : Meta à P5 couvre sept marchés, dont plusieurs jeunes.

### 7.3 Pourquoi l'horizontal gagne au-delà du coude

NØRA est passée de P4 à P5 en ajoutant les Pays-Bas et le Royaume-Uni (canonique § 2).

```
Réel (horizontal) :
   447 206 € de dépense en plus ÷ 9 604 clients = 46,56 €  (= E11 § 1.1)
Contrefactuel (vertical ; hypothèse : extrapolation de la courbe du § 7.2
au-delà de 1,2 M€ à un CAC marginal moyen de 105,00 €) :
   9 604 × 105,00 = 1 008 420 €/mois
   Écart = 561 214 €/mois = 6 734 568 €/an
```

**Les mêmes 9 604 clients coûtent 46,56 € par la géographie et environ 105,00 € par le budget.** Et l'horizontal ne se limite pas au pays : par coût croissant, nouveau placement dans la même régie, nouveau format, nouvelle langue sur un marché ouvert, nouvelle audience de similarité entraînée sur un autre segment de LTV, puis nouveau marché. Les quatre premiers sont gratuits ou presque, et presque personne ne les épuise avant d'ouvrir un pays.

### 7.4 Ce qui casse quand on va trop vite

| Ce qui casse | Le mécanisme | Le chiffre |
| --- | --- | --- |
| L'apprentissage | Toute entité qui saute de budget repasse en exploration | 62 532 € pour un doublement brutal (§ 4.5) |
| La machine créative | Le budget monte, le nombre de concepts non : la fréquence monte à sa place | 57 concepts/semaine à P5 (canonique § 6) |
| Le signal | Plus de marchés, plus de régimes de consentement et de suivi | +13,3 % de CPA (§ 2.4) |
| Le cash | Chaque +100 k€ de CA mensuel immobilise du BFR | 52 263 € à P5 (canonique § 4) |
| Le SAV et la logistique | Un trafic plus large est moins qualifié | Retours de 2,0 % à P1 à 3,5 % à P5 (§ 2.1) |
| Le compte lui-même | Un changement brutal de comportement déclenche des contrôles | 11 jours de coupure = 325 675 € ([C10](../etudes-de-cas/C10-compte-publicitaire-banni.md)) |

Le signal décisif reste celui de [E11 § 1.4](E11-passage-a-echelle.md) : si tu tiens ton débit créatif, que tes gagnants entrent en rotation et que le CAC marginal monte quand même, le problème n'est plus la créa, c'est un mur. Tant que ce signal manque, **tu as un problème de créa**, et tu es de retour dans [E05](E05-machine-creative.md).

### 7.5 La saisonnalité : le ciseau de fin d'année

*Ordre de grandeur, à traiter comme une fourchette et à re-mesurer sur ton compte :* les CPM en Europe montent de **25 à 50 %** entre la mi-novembre et le 24 décembre, avec un pic sur les quatre jours autour du Black Friday. Cause mécanique : même inventaire, davantage d'annonceurs, et des annonceurs dont l'enchère est temporairement plus élevée parce que leur propre valeur estimée l'est. Le piège n'est pas que la publicité coûte plus cher : c'est que **les deux lames du ciseau bougent en sens contraire.**

```
Lame 1 — ton MER réalisé baisse.
   Hypothèse : CPM +35 %, taux de conversion +20 % (la remise convertit)
   CPA × 1,35 ÷ 1,20 = × 1,125  →  MER réalisé = 2,90 ÷ 1,125 = 2,58

Lame 2 — ton MER seuil monte.
   Hypothèse : les remises passent de 8,0 % à 18,0 % du CA HT
   Marge brute = 61,5 − 10 = 51,5 %
   Seuil de contribution = 1,20 ÷ 0,515 = 2,33  (contre 1,20 ÷ 0,615 = 1,95)
   Marge brute mensuelle = 3 610 997 × 0,515 = 1 859 663 €
   Publicité maximale    = 1 859 663 − 360 000 = 1 499 663 €
   Seuil EBITDA = 4 333 196 ÷ 1 499 663 = 2,89  (contre 2,33, canonique § 2.3)

Réalisé 2,58 contre seuil 2,89 :
   Publicité = 4 333 196 ÷ 2,58      = 1 679 533 €
   CM3       = 1 859 663 − 1 679 533 =   180 130 €
   EBITDA    = 180 130 − 360 000     =  −179 870 €/mois
   Écart avec un mois normal (+364 752 €) = −544 622 €
```

*Contrôle de la formule :* `1,20 ÷ 0,615 = 1,95` reproduit exactement le seuil de contribution canonique de P5, et `4 333 196 ÷ (2 220 763 − 360 000) = 2,33` son seuil EBITDA.

**Et la décision qui en découle n'est pas celle qu'on croit.** Couper le budget de 30 % uniformément ne répare rien : à 2,58, au-dessus du seuil de contribution de 2,33, chaque euro produit encore de la contribution positive, et une coupe uniforme retire autant d'euros à 41 € de CAC marginal qu'à 96 € (§ 6.2) — elle dégrade ton MER au lieu de l'améliorer. Trois décisions défendables, par ordre de rendement : **couper le marginal**, c'est-à-dire les lignes dont le CAC marginal explose en saison, à commencer par la recherche de marque dont la concurrence sur ton nom est maximale ces semaines-là ; **tenir la remise** plutôt que le budget, puisque c'est la remise et non le CPM qui a déplacé le seuil de 2,33 à 2,89 ; **accepter la perte, chiffrée et plafonnée d'avance**, si et seulement si tu as vérifié que les cohortes de novembre réachètent comme les autres, ce qui est rarement le cas ([E08](E08-retention-et-ltv.md)). Calcul complet dans [C09](../etudes-de-cas/C09-piege-du-black-friday.md).

---

## 8. Les erreurs qui coûtent cher

**1. Piloter au rendement affiché par la plateforme.** Le plan média revendique 41 364 clients pour 37 324 réels, et la correction n'est pas uniforme : Google affiche 25,36 € et coûte 79,95 € (§ 5.2). *Coût :* 1 751 244 €/an d'acquisition absente de tout tableau de bord, plus toutes les allocations prises à l'envers.

**2. Couper un ensemble avant la fin de son apprentissage.** À 26 conversions par semaine l'erreur-type sur le CPA est de 19,6 %, et il faut ~470 conversions par bras pour affirmer un écart de 20 % (§ 2.2). *Coût :* tu coupes des gagnants au hasard, avec la conviction d'avoir optimisé.

**3. Empiler les campagnes et les ensembles.** À P2, trente ensembles en laissent vingt-quatre sous le seuil. *Coût :* 8 143 €/mois, **41,0 % de la perte mensuelle** (§ 4.1) — une perte d'architecture, pas de marché.

**4. Changer les budgets tous les jours.** Un doublement brutal coûte 1 296 clients et 62 532 € de contribution pour gagner trois jours, quand la règle des +25 % / 72 h autorise ×9,3 en un mois (§ 4.5).

**5. Exclure les acheteurs de toutes les campagnes.** Le réachat pèse 22 876 commandes et 995 792 € de contribution par mois, 44,9 % de la marge brute (§ 4.4). *Coût :* tu retires du signal à la machine et t'interdis ta poche la plus rentable.

**6. Transmettre le prix au lieu de la marge.** Au § 3.3 le MER monte de 2,90 à 3,05, le CA gagne 216 720 €/mois et l'EBITDA en perd 205 884 €. *Coût :* 2 470 608 €/an, 56,4 % de l'EBITDA, tous voyants au vert.

**7. Sur-segmenter le ciblage.** Chaque segmentation divise le signal (§ 4.1), rétrécit l'audience, pousse la fréquence (§ 5.3) et empêche la mesure. Levier de la décennie 2010, devenu un moyen coûteux d'interdire aux modèles de la plateforme — meilleurs que les tiens — de travailler. *Coût :* 25 % de CPA sur la part du budget sous le seuil.

**8. Croire qu'un CPM bas est une bonne nouvelle.** Le CPM le plus bas du § 1.2 est 6,25 € pour un CPA de 56,82 € ; le CPA le plus bas est 24,89 € pour un CPM de 11,00 €. *Coût :* toute une catégorie d'optimisations qui améliorent l'indicateur en dégradant l'entreprise.

---

## 9. Ce que ce module ne dit pas

**Il ne mesure pas l'incrémentalité, il la suppose.** Tous les taux des § 5.2 et § 5.3 sont des hypothèses déclarées, alignées sur [E09](E09-mesure-et-incrementalite.md). Aucune interface ne produit ce chiffre et aucun modèle d'attribution ne s'en approche : il faut une expérience, avec zone de retenue, durée et puissance calculées. Rien ici ne remplace ce travail.

**Il ne dit rien de l'effet de marque à long terme.** Le système décrit ici optimise sur un événement, dans une fenêtre de quelques jours ; ce qui construit la disponibilité mentale d'une marque sur trois ans — distinctivité des actifs, portée sur les non-acheteurs, mémoire — n'entre dans aucun de ces modèles et n'apparaît dans aucune de ces courbes. **Un compte parfaitement optimisé au sens de ce module peut détruire lentement l'actif qui le fait fonctionner** : [E12](E12-marque-et-actif.md) et le [module 10](../../modules/10-sharp-distinctivite.md), contradicteur assumé de tout ce qui précède.

**Il ne fabrique pas les créas** — 1 245 assets par mois et 57 concepts jugés par semaine sont un problème d'organisation ([E05](E05-machine-creative.md), [C03](../etudes-de-cas/C03-anatomie-creative-gagnante.md)) — **ne traite pas ce qui se passe après le clic** ([E07](E07-funnel-et-conversion.md)), **ni le cash** que la dépense immobilise (1 045 944 € d'avance publicitaire à P5, canonique § 4, [E10](E10-cash-et-operations.md)), **ni le risque de plateforme** : un compte publicitaire est un actif que tu ne possèdes pas ([C10](../etudes-de-cas/C10-compte-publicitaire-banni.md), [E13](E13-risque-de-ruine.md)). Marketplaces, retail media et télévision segmentée, de mécanique d'enchère différente, sont aussi hors champ.

**Et toutes ses courbes de saturation sont des hypothèses.** Les tableaux des § 6.2 et § 7.2 passent par les points canoniques : justes pédagogiquement, invérifiables sur ton compte tant que tu n'as pas mené tes propres tests d'augmentation. **La forme de la courbe est une loi, ses paramètres sont à mesurer.**

---

## 10. Le tableau de bord du module

| # | Indicateur | Fréquence | Seuil d'alerte |
| --- | --- | --- | --- |
| 1 | Achats déclarés par les plateformes ÷ achats du back-office | Hebdo | Écart > 10 %, ou toute **variation** de l'écart |
| 2 | Part du budget portée par des entités > 50 conversions/semaine | Hebdo | < 70 % du budget |
| 3 | CAC marginal du dernier palier ÷ LTV 12 mois (86,75 € à P5) | À chaque hausse de budget | > 0,80 — au-delà tu achètes du volume, pas de la marge |
| 4 | Fréquence hebdomadaire en prospection large | Hebdo | > 3,5 ([E11 § 1.4](E11-passage-a-echelle.md)) |
| 5 | MER global ÷ MER seuil EBITDA (2,33 à P5, canonique § 2.3) | Hebdo | < 1,05 |
| 6 | Score d'appariement, taux de consentement, taux de doublons | Mensuel | Baisse deux mois consécutifs ; doublons > 2 % |

L'écart de l'indicateur 1 ne sera jamais nul et ne doit pas l'être — la régie compte selon sa fenêtre, ton back-office selon la date de commande. C'est sa **stabilité** qui compte : toute variation est un incident technique jusqu'à preuve du contraire. Les indicateurs 1 et 6 sont de la plomberie que personne ne regarde et valent 1 311 504 € par an à eux deux (§ 2.4) ; les 3 et 5 sont des indicateurs de décision — le 3 dit si tu peux dépenser un euro de plus, le 5 si tu peux dépenser tout court.

> **À retenir :** un compte publicitaire ne se pilote pas au rendement, il se pilote à trois nombres — le coût du prochain client, le seuil au-delà duquel ce coût détruit de la marge, et la part de ton budget qui apprend réellement. Les trois se calculent, aucun ne s'affiche.

---

## 11. Exercices

À rendre dans [`ecommerce/exercices/E06-rendu.md`](../exercices/E06-rendu.md). Corrigé dans `E06-corrige.md`.

**1 — Le CAC marginal entre deux paliers (réponse numérique unique).** À partir du § 7.2, calcule le CAC marginal entre 1 000 000 € et 1 200 000 € de budget Meta mensuel, puis l'élasticité α sur ce seul intervalle. Compare-le aux LTV 12 et 24 mois (canonique § 3) et dis à quel budget tu t'arrêtes selon que ton BFR est financé ou non (canonique § 4). Conclus : de combien le nCAC **moyen** sous-estime-t-il le coût du prochain client à ce niveau ?

**2 — L'allocation, sur les chiffres canoniques (réponse numérique unique).** Reprends le plan média canonique § 5 et les CAC marginaux du § 6.2. Déplace 200 000 € par tranches de 40 000 €, en respectant l'égalisation des marginaux et le plafond de 86,75 €. *Hypothèse à poser et à écrire toi-même :* de combien monte le CAC marginal d'un canal à chaque tranche ajoutée. Donne le nouveau plan média, les clients gagnés, la contribution 12 mois créée et le nouveau nCAC global — puis refais-le avec les CAC incrémentaux du § 5.2.

**3 — L'audit de ton signal.** Sur quatre semaines, remplis les six lignes du § 10 avec tes chiffres ; pour la ligne 1, donne l'écart semaine par semaine et son écart-type, c'est la variation qui compte. Puis applique le modèle du § 2.4 à ton mix d'environnements et chiffre, en euros par an, ce que te coûte l'écart entre ton signal actuel et un signal complet.

**4 — Ton compte fait-il apprendre quelque chose ?** Liste les entités qui portent un budget : conversions des sept derniers jours, budget hebdomadaire, au-dessus ou en dessous de 50. Calcule la part de ton budget portée par des entités au-dessus du seuil ; sous 70 %, écris le plan de consolidation — entités gardées, entités fusionnées, conversions hebdomadaires de chacune après fusion.

**5 — Ta courbe de saturation.** Prends tes deux derniers **niveaux** de dépense sur ton canal principal, pas deux mois différents, et calcule le CAC marginal et α. Si tu n'as jamais eu deux paliers, conçois le test : durée, amplitude, seuil de décision écrit d'avance, et ce que tu fais si le résultat tombe dans la zone d'incertitude. Un test dont la conclusion n'est pas écrite avant de commencer n'est pas un test.

**6 — La décision.** Une ligne pèse 22 % de ton budget à un rendement plateforme de 4,10. Ton MER global est de 2,65 pour un seuil EBITDA de 2,40, ta marge brute de 58 %. Un test de retenue d'audience sur cinq semaines mesure 19 % d'incrémentalité, intervalle de 6 % à 32 %. *(a)* Calcule le rendement incrémental et le seuil de contribution, puis tranche. *(b)* Refais-le aux deux bornes : la décision change-t-elle ? *(c)* Donne la condition sous laquelle la décision inverse serait la bonne, et le chiffre à mesurer pour l'établir. *(d)* Si tu coupes, dis où vont les 22 % libérés et pourquoi, en te servant du § 6.2 et pas de ton intuition.

---

*Fin du module E06. Suite : [E07 — Le funnel et la conversion](E07-funnel-et-conversion.md), qui prend le clic acheté ici et démontre ce qu'il devient — puis [E09 — Mesurer : attribution, incrémentalité, pilotage](E09-mesure-et-incrementalite.md), qui remplace toutes les hypothèses d'incrémentalité de ce module par des mesures.*
