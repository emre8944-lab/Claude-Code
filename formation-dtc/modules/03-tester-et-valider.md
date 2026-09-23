# Module 03 — Tester et valider

> **Objet :** transformer 3 à 5 finalistes en **un** produit validé, en dépensant le
> moins possible, et sans te mentir sur ce que disent les chiffres.
> **Prérequis :** modules 01 et 02. Le module 12 du cursus business (Hopkins, le test à
> perte bornée) est le fondement de ce module.
> **Outil :** [journal de test](../boite-a-outils/templates.md#journal-de-test)
> **Devoirs :** `exercices/03-rendu.md`

---

## 0. Ce qu'est un test (et ce qu'il n'est pas)

Un test est **une expérience à perte bornée, avec des seuils de décision écrits avant
le lancement**. Tu décides à l'avance combien tu acceptes de perdre, et quels chiffres
te feront tuer, itérer ou pousser.

Ce que ce n'est pas : « je mets 50 €/jour et je vois ». Sans seuils écrits, tu verras
toujours ce que tu as envie de voir. Tu prolongeras le produit que tu aimes, tu tueras
trop vite celui qui t'ennuie, et tu appelleras ça de l'intuition.

> **Règle absolue du module :** pas de lancement sans le tableau de la section 5 rempli.

---

## 1. Ce qu'on teste, dans quel ordre

Un produit qui ne vend pas peut échouer à quatre endroits :

1. **Le produit-marché** — personne ne veut ça, à ce prix.
2. **L'angle** — les gens le voudraient, mais ton message ne leur parle pas.
3. **L'offre** — ils le veulent, mais pas à ces conditions (prix, livraison, garantie).
4. **La page** — ils le veulent, mais ta page ne les convainc pas ou les perd.

Le test de produit vise la question 1. Mais pour y répondre proprement, les trois
autres doivent être **correctes** — pas parfaites, correctes. Sinon tu tues un bon
produit à cause d'une mauvaise page. D'où le kit minimum.

---

## 2. Le kit de test minimum

| Élément | Standard minimum | Pourquoi |
|---|---|---|
| **Page produit** | Une page par produit, propre, mobile d'abord, avec **tes propres photos et vidéos** faites avec l'échantillon | Les visuels du fournisseur sont vus partout : ils crient « dropshipping » |
| **Créas** | 3 angles × 2 à 3 pubs = 6 à 9 pubs par produit | Tester un seul angle, c'est tester ton message, pas ton produit |
| **Offre** | Le produit seul + un bundle | Tu apprends dès le test si le panier peut monter |
| **Livraison** | Délai **réel** affiché, **idéalement 2 à 5 jours** | Voir ci-dessous |
| **Suivi** | Pixel + API de conversions installés, achat test vérifié | Sans données fiables, pas de décision |
| **Pages légales** | CGV, mentions légales, rétractation, confidentialité (module 13) | Obligatoires, et les plateformes vérifient |

### Le point livraison — là où la plupart se trompent

En Europe, le client attend sa commande en **2 à 5 jours**. Un dropshipping depuis la
Chine en 10 à 20 jours produit mécaniquement : des demandes de remboursement, des
litiges bancaires (*chargebacks*), des avis négatifs, et une **baisse de ton score de
satisfaction client chez Meta**, qui peut renchérir ou restreindre tes pubs. Tu
sabotes ton test et ton compte en même temps.

**Mes recommandations pour tester :**
- **Idéal :** achète 30 à 100 unités par avion (7 à 10 jours) et expédie depuis chez
  toi ou un petit prestataire logistique. Coût : quelques centaines d'euros par
  produit, mais le test est propre.
- **Acceptable :** un agent de sourcing avec un **stock en Europe**.
- **À éviter :** l'expédition directe depuis la Chine en 2 à 3 semaines. Si tu n'as pas
  le choix, **affiche le délai réel** — le cacher est illégal et suicidaire.

---

## 3. Le budget de test

### 3.1 La règle

```
Budget par angle   ≥ 2 × CPA d'équilibre     (avant de conclure quoi que ce soit)
Budget par produit ≈ 3 angles × 2 à 3 × CPA d'équilibre
                   ≈ 6 à 10 × CPA d'équilibre
```

Pour un produit avec un CPA d'équilibre de 35 €, ça fait **≈ 200 à 350 € au minimum**,
et en pratique **400 à 800 € sur 4 à 7 jours**. Pour 3 produits : 1 200 à 2 400 €.

### 3.2 Pourquoi pas moins

Parce qu'en dessous, tu mesures du bruit. Ce qui nous amène à la section la plus
importante du module.

---

## 4. Le bruit statistique : pourquoi 3 ventes ne prouvent rien

Les ventes arrivent au hasard, même quand le « vrai » taux est fixe. Les statisticiens
modélisent ça par une loi de Poisson. Ce qu'elle dit, concrètement :

| Ventes observées | Fourchette plausible du « vrai » nombre (à 95 %) | Ce que ça veut dire pour ton CPA |
|---|---|---|
| 3 | 0,6 à 8,8 | Ton vrai CPA peut être 3 fois meilleur ou 5 fois pire. **Aucune information.** |
| 5 | 1,6 à 11,7 | Du simple au triple. Un indice, pas une preuve. |
| 20 | 12,2 à 30,9 | ± 40 à 50 %. Une tendance. |
| 50 | 37,1 à 65,9 | ± 25 %. Une décision. |
| 100 | 81,4 à 121,6 | ± 20 %. Une certitude opérationnelle. |

**Conséquences :**
- Tu ne célèbres pas 2 ventes le premier jour. Tu ne pleures pas 0 vente après 40 €.
- Au stade du test, tu décides avec **les indicateurs avancés** (CTR, ajouts au panier),
  qui arrivent en centaines d'événements et sont donc bien plus fiables que les achats.
- Un produit n'est **validé** qu'avec **au moins 50 achats** à un CPA sous la cible
  (section 8).

---

## 5. Les seuils, écrits avant le lancement

Voici les ordres de grandeur que j'utilise pour de l'acquisition froide sur Meta en
France, sur des produits grand public. Ce ne sont pas des lois : ce sont des repères
pour savoir **où** regarder.

| Indicateur | Définition | Mauvais | Correct | Bon |
|---|---|---|---|---|
| **Taux d'accroche** (*hook rate*) | Vues de 3 s ÷ impressions | < 20 % | 20-30 % | > 30 % |
| **CTR lien** | Clics sur le lien ÷ impressions | < 0,8 % | 0,8-1,5 % | > 1,5 % |
| **CPC lien** | Dépense ÷ clics sur le lien | > 1,50 € | 0,70-1,50 € | < 0,70 € |
| **Taux d'ajout au panier** | Ajouts au panier ÷ sessions | < 4 % | 4-8 % | > 8 % |
| **Paiements initiés ÷ ajouts** | | < 30 % | 30-50 % | > 50 % |
| **Taux de conversion** | Achats ÷ sessions | < 1 % | 1-2,5 % | > 2,5 % |
| **CPA** | Dépense ÷ achats | > 1,5 × équilibre | 1 à 1,5 × équilibre | < équilibre |

### Les trois décisions possibles

| Décision | Condition (à adapter, mais à écrire **avant**) |
|---|---|
| **TUER** | L'angle a dépensé ≥ 2 × CPA d'équilibre sans achat **et** CTR < 0,8 %. Le produit a dépensé ≥ 6 × CPA d'équilibre et son CPA est > 2 × l'équilibre sur tous les angles. |
| **ITÉRER** | CPA entre 1 et 1,5 × l'équilibre **avec** des indicateurs avancés bons (CTR ≥ 1,2 %, ajout panier ≥ 6 %). Tu identifies l'étape faible, tu la corriges, tu relances avec un nouveau budget de 4 à 6 × l'équilibre. Une seule itération sans amélioration nette → tuer. |
| **VALIDER** | CPA ≤ CPA d'équilibre avec au moins 5 achats sur un angle → phase de validation (section 8). |

---

## 6. L'arbre de diagnostic

Quand un test ne donne pas ce que tu veux, **ne change pas tout**. Descends l'entonnoir
et trouve la première étape sous le repère.

```
Le CPM est anormalement élevé (> 20 € en France hors Q4) ?
 └─ OUI → pub peu engageante, catégorie sensible, ou audience trop restreinte.
          Élargis le ciblage, vérifie les refus de pub, change le format.

Le CTR est < 0,8 % ?
 └─ OUI → problème de CRÉA ou d'ANGLE. Nouvelles accroches, nouveaux angles.
          Si les 3 angles sont < 0,8 % → le produit n'intéresse pas. TUER.

Les clics sont bons, mais les sessions sur le site sont < 70 % des clics ?
 └─ OUI → le site est trop LENT (mobile). Allège la page.

L'ajout au panier est < 4 % ?
 └─ OUI → la PAGE ou le PRIX ne tient pas la promesse de la pub.
          Vérifie la cohérence pub → page (même promesse, même visuel en haut),
          le prix (choc ?), la preuve (avis, vidéo), la clarté.

Les ajouts sont bons, mais peu de paiements initiés ?
 └─ OUI → SURPRISE au panier : frais de port, délai, création de compte forcée.

Les paiements initiés sont bons, mais peu d'achats ?
 └─ OUI → le CHECKOUT : moyens de paiement manquants (Apple Pay, PayPal,
          paiement en plusieurs fois), bug, confiance.
```

Ce diagnostic est aussi la raison pour laquelle on regarde les indicateurs avancés : un
produit avec un CTR de 2 % et un ajout au panier de 3 % n'a pas un problème de produit.
Il a un problème de page ou de prix. **Le tuer serait une erreur.**

---

## 7. La structure de campagne de test (résumé)

Le détail est au module 09. Pour un test :

- **1 campagne** par produit, objectif **Ventes**, optimisation sur l'**achat**.
- **1 ensemble de publicités par angle**, 2 à 3 pubs par ensemble.
- **Ciblage large** : le pays, 18-65+, les deux sexes sauf produit clairement genré, sans
  centres d'intérêt. La créa fait le ciblage.
- **Budget** : 30 à 50 € par jour et par ensemble.
- **Ne touche à rien pendant 72 heures.** Chaque modification perturbe l'apprentissage
  de l'algorithme.

---

## 8. La phase de validation : du « prometteur » au « prouvé »

Un bon test n'est pas une validation. Avant d'engager de l'argent sérieux (stock de
private label, marque, équipe), tu confirmes sur **2 à 4 semaines** :

| Critère de validation | Seuil |
|---|---|
| Achats cumulés | ≥ 50 |
| CPA sur les 7 derniers jours | ≤ CPA cible (module 01) |
| Budget quotidien atteint | 150 à 300 €/jour sans dégradation forte du CPA |
| Taux de remboursement / litiges | < 5 % |
| Avis clients | Majoritairement positifs, pas de défaut récurrent |
| Délais de livraison | Tenus |

Pendant la validation, tu **itères déjà** : tu coupes les angles perdants, tu déclines
les gagnants (nouvelles accroches sur le même corps de vidéo), tu testes le bundle en
avant. C'est le début de la machine créative (module 08).

---

## 9. Les autres façons de tester

### 9.1 Le test organique (budget < 2 000 €)

Tu crées un compte TikTok dédié au produit et tu publies **2 à 3 vidéos par jour
pendant 14 jours** (démonstrations, réactions, avant/après). Tu regardes les vues, les
commentaires (« où l'acheter ? » est le meilleur signal), et les ventes via le lien. Une
vidéo qui dépasse 100 000 vues et génère des ventes est une validation gratuite — et
une créa toute prête pour la pub payante (module 10).

### 9.2 La précommande

Possible et légale **si** la date de livraison est clairement indiquée avant l'achat et
tenue. Elle valide la demande **et** finance le stock. Idéale pour un produit fabriqué
sur mesure. Attention à ne pas l'utiliser pour masquer du dropshipping lent.

### 9.3 La liste d'attente

« Lancement le 15 octobre — inscris-toi pour −15 % et un accès en avant-première ». Tu
mesures le coût par inscription et le taux de conversion à l'ouverture. Signal plus
faible qu'un achat, mais utile pour un produit de marque (route B).

### 9.4 L'envoi à des micro-créateurs

Tu envoies 20 échantillons à des créateurs de ton marché (module 10). Leurs réactions,
leurs commentaires et les ventes générées par leurs codes sont un signal — et une
source de contenus pour tes pubs.

---

## 10. Fil rouge — Le test de Nilo

Trois produits, 4 jours chacun, environ 500 € par produit.

| Produit | Angle | Dépense | CTR | Ajout panier | Achats | CPA |
|---|---|---|---|---|---|---|
| **Fontaine** | A1 — « Ton chat ne boit pas assez » (problème) | 180 € | 1,6 % | 9,5 % | 11 | **16,36 €** |
| | A2 — « Silencieuse et sans fil » (produit) | 165 € | 0,9 % | 4,8 % | 3 | 55,00 € |
| | A3 — « Le chat qui boit au robinet » (comportement, humour) | 172 € | 2,3 % | 5,1 % | 6 | 28,67 € |
| | **Total fontaine** | **517 €** | | | **20** | **25,85 €** |
| **Oreiller cervical** | 3 angles | 510 € | 1,4 % | 3,0 % | 6 | 85,00 € |
| **Tapis d'acupression** | 3 angles | 480 € | 1,9 % | 7,2 % | 9 | 53,33 € |

### Les décisions, et pourquoi

**Tapis — TUER.** C'est le cas le plus instructif. Ses indicateurs d'engagement sont
bons (CTR 1,9 %, ajout panier 7,2 %). Les gens aiment la pub. Mais le panier moyen est
de 44 € et le CPA de 53 € : ROAS = 396 € ÷ 480 € = **0,83**. Son CPA d'équilibre est
d'environ 17 à 18 €. Il faudrait diviser son CPA par trois **juste pour atteindre
l'équilibre**. **Le
produit qui plaît le plus est le pire business des trois.** C'est le module 01 qui
tranche, pas l'enthousiasme.

**Oreiller — TUER.** CTR correct, mais ajout au panier à 3 % : les gens cliquent et ne
sont pas convaincus. L'arbre de diagnostic dit : page ou prix. On pourrait itérer…
mais le score de différenciation était de 4/8 au module 02 : trop de concurrents
vendent le même produit. Une itération ne changerait pas ce fait. On économise le
budget.

**Fontaine — VALIDER, en itérant.** 20 achats à 25,85 €, sous le CPA d'équilibre du mix
(≈ 36 €). Attention au bruit : l'angle A1 n'a que 11 achats — la fourchette plausible
est large. Mais ses indicateurs avancés sont cohérents (CTR 1,6 %, ajout panier 9,5 %).
Décisions :
- Couper A2 (CTR 0,9 % : « silencieuse et sans fil » parle du produit, pas du chat).
- Garder A1, produire 6 nouvelles pubs sur cet angle.
- **Hybrider** : l'accroche de A3 (le chat au robinet, CTR 2,3 %) + le corps de A1 (la
  question de l'hydratation). Le meilleur arrêt de pouce + le meilleur argument.
- Mettre le bundle filtres en avant sur la page.

### La validation (3 semaines)

Budget monté progressivement de 150 à 300 €/jour. Résultat : **212 achats, CPA
23,10 €, conversion 3,1 %, panier moyen 71 €, remboursements 2,5 %**. MER ≈ 3,1.

Tous les critères de la section 8 sont remplis. **Le produit est validé.** Le fondateur
peut maintenant engager de l'argent dans un produit à sa marque (module 04) et une
identité (module 05).

Coût total de la découverte : ≈ 1 500 € de tests perdus (oreiller, tapis, angles
coupés). C'est le prix normal d'un produit validé. Ceux qui refusent de payer ce prix
paient beaucoup plus cher en s'acharnant sur leur premier choix.

---

## 11. Les pièges

1. **Tester sans seuils écrits.** Tu te raconteras une histoire.
2. **Juger sur les achats trop tôt.** Regarde d'abord les indicateurs avancés.
3. **Tester un seul angle.** Tu testes ton copywriting, pas ton produit.
4. **Toucher à la campagne toutes les 6 heures.** Laisse 72 heures.
5. **Des visuels de fournisseur.** Ta pub ressemble à 40 autres ; ton CTR s'effondre.
6. **Livrer en 15 jours.** Tu empoisonnes ton compte publicitaire et tes avis.
7. **S'acharner.** Une itération sans amélioration nette → on tue. Il y a d'autres
   produits dans ta liste.
8. **Tuer un produit rentable parce qu'il est « ennuyeux ».** L'argent se moque de ton
   ennui.

---

## 12. Devoirs — à rendre dans `exercices/03-rendu.md`

**Exercice 1 — Ton plan de test.** Pour tes 3 finalistes : les 3 angles de chacun, le
budget par angle et par produit (avec le calcul), la durée, et le tableau de seuils
TUER / ITÉRER / VALIDER **rempli avant le lancement**.

**Exercice 2 — Diagnostic.** Pour chacun des cas suivants, dis où est le problème et ce
que tu fais :
(a) CTR 0,6 %, CPC 1,90 €, 1 achat pour 150 € ;
(b) CTR 2,4 %, ajout panier 2,1 %, 2 achats pour 200 € ;
(c) CTR 1,5 %, ajout panier 9 %, paiements initiés 18 % des ajouts ;
(d) CTR 1,3 %, ajout panier 7 %, 14 achats pour 280 €, CPA d'équilibre 30 €.

**Exercice 3 — Le bruit.** Un ami te dit : « Mon produit est validé, j'ai fait 4 ventes
pour 60 € de pub, CPA de 15 € ! » Réponds-lui en trois phrases, chiffres à l'appui.

**Exercice 4 — Ton kit.** Liste ce qui te manque pour lancer ton premier test (section
2), avec une date pour chaque élément.

---

*Module suivant : [04 — Sourcing et supply chain](04-sourcing-supply-chain.md).*
