# Module E09 — Mesurer : attribution, incrémentalité, pilotage

> **Prérequis :** [E01](E01-arithmetique-de-la-marque.md), [E06](E06-acquisition-payante.md), [E07](E07-funnel-et-conversion.md), [E08](E08-retention-et-ltv.md).
> **Objet :** savoir quel euro de publicité produit une vente qui n'aurait pas eu lieu, le prouver par une expérience dimensionnée et et piloter sur des chiffres qu'aucune régie ne fabrique.
> **Temps de travail :** ~6 h (lecture + exercices)

---

## 0. Pourquoi ce module existe

Toutes les interfaces publicitaires répondent à *« combien cette campagne a-t-elle rapporté ? »*. Aucune ne répond à la seule qui compte : **« combien aurais-je vendu si je ne l'avais pas diffusée ? »**

La première se répond en observant. La seconde exige un monde où tu n'as pas diffusé, et ce monde n'existe pas : il faut le fabriquer. C'est la différence entre une corrélation et une décision.

L'écart se chiffre. Au palier P5, les six canaux du plan média revendiquent 41 364 nouveaux clients quand la marque en acquiert 37 324 ([chiffres canoniques](../donnees/chiffres-canoniques.md) § 5 et § 2.4) — et ce n'est que la partie visible : un canal peut afficher un rendement de 4,00 et n'en produire que 0,32.

Le canonique § 8 dit que P5+ fait le même chiffre d'affaires que P5 avec **219 725 € de publicité en moins par mois** et un EBITDA doublé. Ce module te dit **lesquels** de ces 219 725 € couper. Sans lui tu couperas au hasard et tu conclurais que la marge et la croissance s'opposent.

---

## 1. Pourquoi l'attribution est structurellement fausse

### 1.1 Le mécanisme

Une régie observe **son propre trafic** : elle a touché un identifiant, elle voit ensuite une conversion sur cet identifiant, elle relie les deux et l'inscrit à son crédit. Elle ne voit pas les cinq autres points de contact et n'a aucune raison de les chercher — ce n'est pas de la malveillance, c'est tout ce qu'elle peut faire avec ses données. **Six régies voient le même acheteur, six régies le comptent.**

### 1.2 La sur-attribution, mesurée sur le canonique

Plan média P5 (canonique § 5), colonne « nouveaux clients / mois » :

```
21 346 + 5 094 + 8 651 + 2 543 + 2 916 + 815 = 41 364 revendiqués
Nouveaux clients réels (canonique § 2.4)     = 37 324
Sur-attribution = 4 040 clients = 10,82 %

nCAC apparent (moyenne des lignes canal) = 1 494 206 ÷ 41 364 = 36,12 €
nCAC réel                                = 1 494 206 ÷ 37 324 = 40,03 €
Écart = 3,91 € par client → 3,91 × 37 324 × 12 = 1 751 244 €/an
```

1,75 M€ de coût d'acquisition annuel absent de tout tableau de bord de régie ([E01 § 3.2](E01-arithmetique-de-la-marque.md)).

### 1.3 Pourquoi 11 % est un plancher, jamais un plafond

41 364 vient d'un modèle propre : une ligne par canal, un client compté une fois. La réalité est pire, trois fois. **Double comptage interne** : une régie compte souvent un client dans deux types de campagne, quand le canonique n'a qu'une ligne par régie. **Vue sans clic** : élargis la fenêtre après impression de 1 à 7 jours, le nombre revendiqué grossit sans qu'une vente soit créée. **Identifiant instable** : qui commande sur mobile puis sur ordinateur est deux clients pour qui compte les cookies, un seul pour qui compte les e-mails.

### 1.4 Pourquoi l'écart enfle quand on multiplie les canaux

Note `s_c` la part des acheteurs réels qu'un canal `c` touche et revendique. La somme revendiquée vaut `37 324 × Σ s_c`, donc `Σ s_c = 41 364 ÷ 37 324 = 1,1082` : l'acheteur moyen est revendiqué par 1,108 canal.

Ajoute un septième canal — site de codes promo, comparateur, partenaire de cashback — placé **au moment du paiement**, donc touchant 15 % des acheteurs. *Hypothèse :* tu le finances par 3 % du budget existant, dépense totale inchangée.

```
Σ s_c = 1,1082 + 0,15 = 1,2582
Somme revendiquée = 37 324 × 1,2582 = 46 963  →  sur-attribution 25,8 %
nCAC apparent = 1 494 206 ÷ 46 963 = 31,82 €   (nCAC réel inchangé : 40,03 €)
```

**Le tableau de bord affiche un coût d'acquisition en baisse de 20,5 % le mois où tu ajoutes un canal qui ne crée aucune vente.** C'est ainsi que se financent les partenaires de dernière position : ils ne vendent pas de la demande, ils vendent de l'attribution.

> **À retenir :** la sur-attribution ne mesure pas la malhonnêteté des régies mais le nombre moyen de canaux qui touchent un acheteur. Elle monte donc avec la maturité de ton plan média, et le seul chiffre qui n'en dépend pas est le nCAC global : dépense totale ÷ nouveaux clients réels.

---

## 2. Les modèles d'attribution et l'hypothèse qu'ils partagent

### 2.1 Un parcours réel

Une acheteuse de NØRA sur 17 jours, panier 64,00 € TTC (AOV de première commande à P5, dérivé en [E01 § 3.3](E01-arithmetique-de-la-marque.md)). **J0** vidéo TikTok vue 6 s, sans clic. **J2** Meta prospection, clic, pas d'achat. **J5** une amie lui dit que le sérum a marché sur elle — **aucune trace**. **J9** reciblage Meta, vue. **J13** e-mail de panier abandonné, clic. **J17** recherche « nøra sérum densité », clic sur l'annonce de marque, achat.

### 2.2 Les cinq modèles sur ce parcours

Dégressif calculé avec une demi-vie de 7 jours, poids `0,5^(âge/7)`, somme des poids 2,5377.

| Modèle | TikTok | Meta prosp. | Amie | Reciblage | E-mail | Google marque |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Dernier clic | 0,00 € | 0,00 € | 0,00 € | 0,00 € | 0,00 € | **64,00 €** |
| Premier clic | 0,00 € | **64,00 €** | 0,00 € | 0,00 € | 0,00 € | 0,00 € |
| Linéaire (5 contacts) | 12,80 € | 12,80 € | 0,00 € | 12,80 € | 12,80 € | 12,80 € |
| Dégressif (demi-vie 7 j) | 4,68 € | 5,71 € | 0,00 € | 11,42 € | 16,97 € | **25,22 €** |
| Data-driven | boîte noire : entraînée par la régie, sur ses données, sur les conversions qu'elle a vues | | | | | |

1. **L'événement causal reçoit zéro dans les cinq modèles.** La recommandation de J5 a probablement transformé une curieuse en acheteuse ; sans trace, elle ne pèse rien. Les modèles n'attribuent pas la cause, ils **répartissent le crédit entre les témoins**.
2. **Le même événement vaut de 0,00 € à 64,00 € selon la convention.** La recherche de marque — rendement incrémental 0,32 au § 6 — encaisse 100 % de la vente au dernier clic, 0 % au premier.

### 2.3 L'hypothèse commune, et pourquoi certains modèles servent quand même

Les cinq supposent que **le parcours observé est le parcours réel**. Or l'observé est un sous-ensemble non aléatoire du réel : il ne contient que ce qui est instrumenté, donc surtout du média payant, donc les modèles concluent toujours que le média payant explique les ventes. Le biais ne va pas au hasard, il va toujours dans le même sens.

Ils restent utiles parce qu'une convention biaisée mais **stable** a une dérivée informative : si ton modèle sous-estime TikTok de 30 % chaque semaine, comparer la semaine 12 à la 11 sur TikTok reste juste, le biais s'annulant dans la différence. Trois règles.

- **Choisis un modèle, écris-le, n'en change pas dans l'exercice.** Google marque capte 100 % de ce parcours au dernier clic, 39,4 % en dégressif : sur ses 249 832 € de CA TTC mensuels (§ 6.2), `249 832 × 0,606 = 151 398 €` de « chute » par mois, **1 816 776 € par an de chiffre d'affaires qui n'a jamais existé ni disparu**.
- **Ne compare jamais deux canaux avec** : le biais diffère entre récolte et semence, il ne s'annule pas dans la différence.
- **Ne t'en sers jamais pour arbitrer un budget total.** Ça, c'est le MER blended (§ 4).

---

## 3. Les trois biais qui font paraître un canal meilleur qu'il n'est

### 3.1 La récolte de demande existante

Un canal placé **après** que l'envie est née encaisse une vente qu'il n'a pas produite. La recherche de marque en est la forme pure : la personne tape ton nom, donc elle te connaît déjà, donc quelqu'un d'autre a payé pour ça. Chiffrage au § 6.2 :

```
Écart = 3,68 points × 62 458 € de dépense mensuelle = 229 845 € de CA TTC/mois
revendiqué et non causé → 2 758 140 €/an
```

**Fait public.** Le seul essai à grande échelle publié sur ce point reste celui d'eBay : en coupant ses mots-clés de marque sur une partie des États-Unis, l'entreprise a trouvé un rendement à court terme statistiquement indiscernable de zéro (Blake, Nosko & Tadelis, *Consumer Heterogeneity and Paid Search Effectiveness*, Econometrica, 2015). Non transposable tel quel — eBay a une notoriété que tu n'as pas — mais le mécanisme l'est.

### 3.2 La sélection : cibler ceux qui allaient acheter

Canonique § 5 : nCAC de 19,00 € sur Google Search contre 38,50 € sur Meta, facteur 2,03. Tentation immédiate, déplacer 20 % du budget Meta vers Google. Ce que le tableau de bord calcule :

```
Déplacement = 0,20 × 821 813 = 164 363 €
Gain affiché sur Google : 164 363 ÷ 19,00 = +8 651 clients
Perte affichée sur Meta : 164 363 ÷ 38,50 = −4 269 clients
Solde affiché           :                  +4 382 clients/mois
```

Or le nombre de gens qui tapent « nøra sérum » ce mois-ci n'est pas fixé par ton budget Google : il est fixé par le nombre de gens à qui Meta et TikTok ont montré le produit. *Hypothèse :* NØRA capte déjà 78 % des clics disponibles sur ses requêtes.

```
Plafond de volume Google = 8 651 ÷ 0,78 = 11 091  →  gain réel maximal +2 440
CAC marginal réel Google = 164 363 ÷ 2 440 = 67,36 €   (et non 19,00 €)
Solde réel = 2 440 − 4 269 = −1 829 clients/mois
Coût : 1 829 × 86,75 € (LTV 12 m, canonique § 3) = 158 666 €/mois = 1 903 992 €/an
```

**Le nCAC de 19,00 € n'est pas une performance média, c'est une position dans le parcours** : un canal de bout de chaîne ne paie que le dernier mètre. Le tableau de bord approuve une réallocation qui détruit 1,9 M€ par an.

### 3.3 Le décalage temporel

Une vente attribuée à J+7 qui aurait eu lieu à J+9 sans publicité n'est pas incrémentale : c'est la même vente, avancée. Le produit s'épuise en 31 à 93 jours ([E08](E08-retention-et-ltv.md)) ; *hypothèse :* cycle moyen 66 jours, relance avançant chaque réachat de 6 jours.

```
Réachats mensuels à P5 : 60 200 − 37 324 = 22 876
Commandes avancées le mois de transition : 22 876 × 6 ÷ 66 = 2 080
Effet apparent sur les réachats : +9,1 %   sur le total : +3,5 %
Contribution encaissée : 2 080 × 43,53 € = 90 542 €   UNE FOIS
Effet en régime établi : 0 commande, 0 €
```

Budgétée comme récurrente, cette ligne vaut `90 542 × 12 = 1 086 504 €` de contribution annuelle imaginaire. **Toute fenêtre de mesure plus courte qu'un cycle d'achat compte l'avancement comme de l'incrémentalité** : aucun test de moins de 90 jours ne tranche sur le réachat de NØRA, d'où l'obligation du § 5 d'analyser séparément nouveaux clients et réachats.

---

## 4. La hiérarchie des méthodes, de la moins à la plus fiable

| # | Méthode | Ce qu'elle mesure | Coût | Taille minimale | Décision autorisée |
| --- | --- | --- | --- | --- | --- |
| a | ROAS plateforme | Ce que la régie s'attribue | 0 € | Aucune | Créa A contre créa B **dans le même compte** |
| b | MER blended | Efficacité de la dépense totale | 0 € | ~30 commandes/jour | Le budget **total** |
| c | Cohortes | Valeur durable d'un mois d'acquisition | Un analyste, données propres | ~10 000 nouveaux clients/mois | Le plafond de CAC finançable |
| d | Test géographique | Incrémentalité causale d'un bloc | Marge non faite pendant la coupe | Cellules appariables, § 5.3 | Le budget **par canal** |
| e | Holdout d'audience | Incrémentalité d'une campagne | CA non fait sur la part retenue | ~392 conversions par bras | Garder ou couper une campagne |
| f | MMM | Décomposition d'un historique | 80 000 à 250 000 €/an *(hyp.)* | ≥ 3 ans **avec variation** | L'allocation annuelle |

Deux notes sur les deux premières lignes, qui décident du reste. **Le ROAS plateforme** est produit par la partie qui vend l'espace, sur ses données, avec sa fenêtre : son seul usage légitime est de comparer deux objets d'un même compte, même période, même fenêtre, où le biais s'annule des deux côtés. **Le MER blended**, lui, a pour numérateur ta banque et pour dénominateur tes factures — aucune régie ne produit ni l'un ni l'autre. Il se lit contre le MER seuil du palier : 1,95 en contribution, 2,33 en EBITDA à P5 (canonique § 2.3, [E01 § 4](E01-arithmetique-de-la-marque.md)). Son piège est qu'il s'améliore sans acquisition nouvelle si tu déplaces du budget vers la récolte, d'où l'aMER (CA total ÷ prospection seule) : **MER qui monte pendant que l'aMER baisse = tu vides ton stock de demande.**

**(c) Les cohortes** mesurent non l'incrémentalité mais la **valeur** de ce que tu as acquis, donc le plafond de CAC finançable — une cohorte magnifique acquise par un canal à incrémentalité nulle reste de l'argent jeté. Taille minimale ([E07 § 7.1](E07-funnel-et-conversion.md)) pour détecter **2 points** sur un premier réachat de 44 % :

```
n = 15,68 × (1 − p) ÷ (p × r²)   avec p = 0,44 et r = 2 ÷ 44 = 0,04545
  = 15,68 × 0,56 ÷ (0,44 × 0,0020661) = 9 659 clients par cohorte
```

Lisible mensuellement à P3 (13 140 nouveaux clients/mois). À P2 (3 400/mois), la formule inversée donne 7,66 % relatif, soit **3,4 points** — en dessous tu regardes du bruit : passe en cohortes trimestrielles.

**(d) Le test géographique** est la seule méthode qui produise une **contrefactuelle réelle** à un coût compatible avec une marque de cette taille : § 5, où son coût net ressort à 45 530 € pour arbitrer 12 564 000 € de média annuel, **0,36 % de l'enjeu**. **(e) Le holdout d'audience** randomise au niveau individuel, donc plus propre — mais **exécuté par la régie** : exige protocole écrit, taille des bras, définition de la conversion. Minimum pour un écart relatif de 20 % : `15,68 ÷ 0,20² = 392 conversions par bras`, une semaine à P5 sur Meta, cinq à six mois à P2. Les deux sont **inutilisables avant P3**.

**(f) Le MMM** régresse ton CA hebdomadaire sur tes dépenses par canal, prix, saisonnalité et promotions, avec par canal une courbe de rémanence (adstock) et une de saturation. Il ne fabrique aucune contrefactuelle : il **infère** de la variation historique. Trois conditions dures.

*Assez d'observations par paramètre.* Six canaux × 3 paramètres = 18, plus tendance, saisonnalité, prix, distribution, promotions, jours fériés ≈ 10 : ~28 paramètres pour 104 semaines, soit 3,7 observations par paramètre quand la pratique en demande 10 à 20. **Un MMM honnête sur deux ans n'existe qu'en réduisant brutalement le nombre de paramètres** — regrouper des canaux, fixer les rémanences, poser des a priori **calibrés par des tests géographiques**. Le test géographique n'est pas un concurrent du MMM : il est ce qui le rend identifiable.

*De la variation, pas de la corrélation.* Si Meta et TikTok montent et descendent ensemble avec le budget total à une corrélation de 0,95, le facteur d'inflation de variance vaut `1 ÷ (1 − 0,95²) = 10,26` : les écarts-types des coefficients sont multipliés par 3,20, et retrouver la même précision demanderait `104 × 10,26 = 1 067 semaines`, vingt ans. **Il faut créer la variation exprès** — un MMM nourri par un plan média « qui suit le chiffre d'affaires » retrouve ta propre règle d'allocation et te la revend comme un résultat.

*Un coût inférieur à ce qu'il arbitre.* Sous 1 % du média annuel, c'est de la superstition coûteuse : 5 232 000 € de média annuel à P3 n'autorisent que 52 320 € de mesure, sous le plancher ; 12 564 000 € à P4 en autorisent 125 640 €. **Le MMM commence à P4, avec trois ans d'historique et de la variation délibérée.**

---

## 5. Le test géographique, en détail opérationnel

### 5.1 Le protocole

**1. L'unité géographique** doit être ciblable dans *toutes* les régies du plan et mesurable dans **tes** données de commande — code postal de livraison, jamais l'adresse IP. *Hypothèse :* 8 % de fuite de ciblage, ce qui **fait sous-estimer l'effet** : un résultat positif reste valide, un résultat nul reste ambigu.

**2. Les paires** se constituent sur 26 semaines d'historique quotidien, appariées sur ventes par habitant, tendance, mix produit, exposition promotionnelle et profil hebdomadaire. Critère : ρ ≥ 0,80 en pré-test, ratio test/témoin stable à ±5 %.

**3. Calcule la puissance AVANT** (§ 5.2) : si l'effet détectable minimum dépasse l'effet sur lequel tu agirais, ne lance pas le test — tu paieras la coupe pour n'apprendre rien.

**4. Écris les seuils de décision AVANT, et fais-les signer.** « Au-delà de X % de baisse on remet le budget ; sous Y % on coupe définitivement ; entre les deux on relance plus long. » Seule protection contre l'interprétation *a posteriori*, et c'est là que la plupart des tests d'entreprise échouent.

**5. Coupe franchement, ou augmente franchement.** La durée varie comme l'inverse du **carré** de l'effet : une réduction de 30 % produit un effet trois fois plus petit et demande neuf fois plus de temps — 37 jours deviennent 333. Différence de nature : **une coupe mesure l'incrémentalité moyenne du bloc coupé, une augmentation mesure la marginale**, seule utile à l'allocation (§ 6.4).

**6. Ne change rien d'autre** — promotion, prix, page — dans aucune des deux cellules, pendant le test et les deux semaines suivantes.

**7. Mesure en double différence**, en gardant 14 jours de rebond après remise du budget, et analyse **séparément** nouveaux clients et réachats (§ 3.3).

### 5.2 La puissance, calculée

`μ` = ventes quotidiennes moyennes de la cellule, `CV` = coefficient de variation quotidien après neutralisation du jour de semaine, `ρ` = corrélation quotidienne test/témoin, `D` = durée en jours, `e` = effet relatif à détecter.

```
σ cumulé sur D jours    = CV × μ × √(2 × (1 − ρ)) × √D
Effet cumulé à détecter = e × μ × D

Détection à 5 % bilatéral, 80 % de puissance  (1,96 + 0,84 = 2,80) :
   e × μ × D  ≥  2,80 × CV × μ × √(2(1 − ρ)) × √D
   D ≥ [ 2,80 × CV × √(2(1 − ρ)) ÷ e ]²
```

**μ disparaît :** à coefficient de variation donné, **agrandir la cellule ne raccourcit pas le test**, parce que le bruit d'une cellule géographique est presque entièrement commun — créations, algorithme, météo, actualité — et ne se dilue pas dans le volume. Sur une cellule à 159 commandes/jour, le bruit de Poisson ne vaut que `1 ÷ √159 = 7,93 %` d'un CV total de 28 % : doubler la cellule ramène le CV à 27,4 %, rien. Améliorer l'appariement de ρ = 0,70 à ρ = 0,85 divise en revanche la durée par deux (`(0,548 ÷ 0,775)² = 0,50`). **Une semaine passée à mieux apparier vaut plus qu'un doublement de cellule.**

### 5.3 Exemple chiffré complet — NØRA au palier P4

*Hypothèses :* répartition du CA et du budget à P4 — FR 46 %, DE 20 %, ES 13 %, IT 13 %, BE 8 % ; budget géo-ciblable et coupable 82 % ; CV quotidien désaisonnalisé 28 % ; ρ = 0,70 après appariement. Les résultats du test sont modélisés, cohérents avec les canoniques sans être canoniques.

```
Canoniques § 2 et § 2.2 : 2 931 600 € TTC/mois, 1 047 000 € de pub/mois, AOV 69,80 €
CA France     = 0,46 × 2 931 600 = 1 348 536 € TTC/mois
Budget France = 0,46 × 1 047 000 =   481 620 €/mois
Cellule test = 25 % du volume France :
   CA cellule     = 337 134 € TTC/mois = 11 083 €/jour  →  159 commandes/jour
   Budget cellule = 120 405 €/mois     =  3 958 €/jour, dont coupable 3 245,6 €

Puissance, pour détecter une baisse de 10 % :
   σ quotidien double diff. = 0,28 × 11 083 × √(2 × 0,30) = 3 103 × 0,7746 = 2 404 €
   Effet quotidien à détecter = 0,10 × 11 083 = 1 108 €
   D ≥ (2,80 × 2 404 ÷ 1 108)² = 6,073² = 36,9  →  42 jours (multiple de 7)
   Sur 14 jours : effet minimum détectable = 25 190 ÷ 155 162 = 16,2 %
   Pour détecter 5 % : (2,80 × 2 404 ÷ 554)² = 147 jours
```

**Sous 16,2 %, un test de deux semaines sur cette cellule ne conclut rien** : l'effet réel étant de 10 à 20 %, il rendra « non significatif » une fois sur deux et quelqu'un lira « la publicité ne sert à rien ». **Le test géographique ne mesure pas les petits effets : ne lui pose que de grandes questions.**

**Résultat** — coupe totale du budget géo-ciblable pendant 42 jours. Cellule test : 458 900 € avant, 376 500 € pendant. Cellule témoin : 471 300 € avant, 489 500 € pendant.

```
Ratio pré-test  = 458 900 ÷ 471 300 = 0,97369
Contrefactuelle = 0,97369 × 489 500 = 476 621 € TTC
Effet mesuré    = 376 500 − 476 621 = −100 121 € TTC, soit −21,01 %

σ cumulé : moyenne quotidienne contrefactuelle 476 621 ÷ 42 = 11 348 €
   0,28 × 11 348 × 0,7746 × √42 = 2 461 × 6,4807 = 15 951 €
z = 100 121 ÷ 15 951 = 6,28
IC 95 % = 100 121 ± 31 264 = [68 857 € ; 131 385 €], soit 14,5 % à 27,6 %
```

**Regarde l'intervalle avant le z.** Le test est massivement significatif *et* son intervalle va du simple au double : un test d'incrémentalité donne un ordre de grandeur et un signe, jamais une décimale.

```
Dépense économisée sur 42 jours = 3 245,6 × 42 = 136 315 €
MER incrémental de la coupe     = 100 121 ÷ 136 315 = 0,73
MER seuil de contribution à P4  = 1,20 ÷ 0,604 = 1,99   (canonique § 2.3 ✓)
```

0,73 contre 1,99 : sur six semaines, le bloc coupé détruit de la valeur. **Et cette lecture est fausse**, parce que la fenêtre tronque l'effet — les clients non acquis ne repasseront pas commande non plus, et ces réachats sont hors fenêtre.

```
AOV 1ʳᵉ commande P4 = 31,71 ÷ 0,604 = 52,50 € HT = 63,00 € TTC  (canonique § 2.4)
Clients non acquis  = 100 121 ÷ 63,00 = 1 589
LTV 24 mois P4      = 3,03 × 37,77 = 114,44 €                   (canonique § 3.1)
Valeur perdue    = 1 589 × 114,44 = 181 845 €
Dépense épargnée =                  136 315 €
Solde            =                 +45 530 € en faveur du maintien du budget
Contrôle : 181 845 ÷ (1 589 × 37,77 €) = 3,03 = LTV/CAC 24 mois canonique ✓
```

**Le bloc coupé est non rentable sur six semaines et rentable sur vingt-quatre mois.** Le test a mesuré juste ; c'est sa lecture naïve qui aurait tué un budget profitable.

> **À retenir :** un test d'incrémentalité mesure un effet **dans sa fenêtre**. Le convertir en décision exige de rapporter les clients perdus à leur LTV, et non le chiffre d'affaires perdu à la dépense épargnée. Sauter cette étape est la façon la plus fréquente de couper un budget qui gagne de l'argent.

---

## 6. CAC incrémental contre CAC attribué

### 6.1 Le résultat sur NØRA à P4

```
CAC incrémental (test § 5.3) = 136 315 ÷ 1 589 = 85,79 €
nCAC attribué (canonique § 2.4)                = 37,77 €   →  facteur 2,27

Étendu au budget entier (hypothèse : le bloc non géo-ciblable a la même
incrémentalité que le bloc testé) :
   Clients incrémentaux/mois = 1 047 000 ÷ 85,79 = 12 204
   Nouveaux clients affichés (canonique § 2.4)   = 27 720
   Taux d'incrémentalité = 44,0 %
```

Un peu moins d'un client sur deux revendiqué par le plan média existe à cause de lui — et c'est une **moyenne**, que le § 6.4 rend utilisable.

### 6.2 Recherche de marque : rendement 4,00, incrémentalité 0,32

*Hypothèse de découpage :* dans les 164 363 € mensuels de Google Search + Shopping à P5 (canonique § 5), 38 % sont sur les requêtes de marque, soit 62 458 €. *Hypothèse de résultat :* un holdout géographique sur 3 marchés pendant 5 semaines mesure 8 % d'incrémentalité, ordre de grandeur cohérent avec le résultat public du § 3.1.

```
CA attribué      = 62 458 × 4,00  = 249 832 € TTC/mois
CA incrémental   = 0,08 × 249 832 =  19 987 €
ROAS incrémental = 19 987 ÷ 62 458 = 0,32

Contribution incrémentale = (19 987 ÷ 1,20) × 0,6145 = 10 235 €/mois
Solde = 10 235 − 62 458 = −52 223 €/mois = −626 676 €/an
soit 14,3 % de l'EBITDA annuel de P5 (4 377 023 €, canonique § 7)
```

### 6.3 La règle de décision, démontrée

Un canal mérite son budget si sa contribution incrémentale dépasse sa dépense. `D` la dépense, `CA_inc` le CA TTC incrémental, `m` le taux de marge brute, `t` la TVA :

```
(CA_inc ÷ (1 + t)) × m  >  D
⇔  CA_inc ÷ D  >  (1 + t) ÷ m
⇔  ROAS incrémental  >  MER seuil de contribution     (1,95 à P5, canonique § 2.3)
```

**C'est la formule centrale du module** : elle ne compare pas un canal à un autre ni un ROAS à une cible sortie de nulle part, mais un rendement causal à la structure de coût de ton entreprise.

| Ligne | Dépense/mois | ROAS plateforme | Incrémentalité | ROAS incrémental | Verdict (seuil 1,95) |
| --- | ---: | ---: | ---: | ---: | --- |
| Google marque | 62 458 € | 4,00 | 8 % *(hyp.)* | **0,32** | détruit |
| Reciblage Meta | 98 618 € | 6,50 | 22 % *(hyp.)* | **1,43** | détruit |
| Point mort de la marque | 62 458 € | 4,00 | **48,8 %** | 1,95 | seuil exact |

Reciblage — *hypothèse de découpage,* 12 % des 821 813 € de Meta (canonique § 5) :

```
CA attribué = 98 618 × 6,50 = 641 017 € ; incrémental = 0,22 × 641 017 = 141 024 €
Contribution = (141 024 ÷ 1,20) × 0,6145 = 72 216 €
Solde = 72 216 − 98 618 = −26 402 €/mois = −316 824 €/an

Coupe des deux lignes :
   Dépense épargnée    = 62 458 + 98 618 = 161 076 €/mois
   Contribution perdue = 10 235 + 72 216 =  82 451 €/mois
   Gain d'EBITDA       =                  = +78 625 €/mois = +943 500 €/an
   Nouveau MER = (4 333 196 − 161 011) ÷ (1 494 206 − 161 076) = 3,13  (contre 2,90)
   Marge au seuil EBITDA (2,33) : de 24,4 % à 34,3 %
```

**Tu viens de supprimer les deux lignes au meilleur ROAS de ton compte, ton tableau de bord de régie s'est dégradé, et ton EBITDA a gagné 943 500 € par an.** Ces 161 076 € couvrent 73,3 % de l'écart de dépense entre P5 et P5+ (219 725 €/mois, canonique § 8) ; le reste vient du panier et de la remise ([E03](E03-offre-et-prix.md), [E08](E08-retention-et-ltv.md)).

Deux réserves : la marque nue laisse le champ libre à un concurrent qui enchérit sur ton nom, donc la décision est « couper, surveiller mensuellement, réactiver si un concurrent apparaît » ; et le reciblage garde une fonction de récupération de panier, dont le rendement se calcule à part ([E07 § 5.5](E07-funnel-et-conversion.md)).

### 6.4 On alloue au CAC incrémental MARGINAL

Le CAC incrémental moyen (85,79 €) dit si le **bloc entier** vaut son budget, jamais ce que vaut le **prochain euro** : pour ça il faut des tests d'**augmentation** (§ 5.1, étape 5). *Hypothèse :* trois d'entre eux à P4 donnent cette courbe.

| Budget du bloc / mois | Clients incrémentaux / mois | CAC incrémental **moyen** | CAC incrémental **marginal** |
| ---: | ---: | ---: | ---: |
| 700 000 € | 9 800 | 71,43 € | — |
| 850 000 € | 11 100 | 76,58 € | **115,38 €** |
| 1 047 000 € *(actuel)* | 12 204 | 85,79 € | **178,44 €** |
| 1 200 000 € | 12 900 | 93,02 € | **219,83 €** |

```
Marginal 850 000 → 1 047 000 : 197 000 ÷ 1 104 = 178,44 €
LTV 24 mois P4 (canonique § 3.1)                = 114,44 €
Destruction par client marginal = 64,00 €  →  1 104 × 64,00 = 70 656 €/mois
                                              = 847 872 €/an
```

L'optimum de contribution est à **850 000 €/mois**, où le CAC marginal (115,38 €) croise la LTV 24 mois (114,44 €). NØRA dépense 1 047 000 € : défendable, puisqu'elle achète du volume vers P5 — mais **ce volume coûte 847 872 € par an, et une décision de croissance qu'on n'a pas chiffrée est une fuite, pas une stratégie.**

La règle tient en une ligne : **dépense l'euro suivant si et seulement si son CAC incrémental marginal est inférieur à la LTV que ta trésorerie sait financer** — 12 mois si tu es autofinancé, 24 mois si tu as le BFR pour tenir (1 392 510 € à P4, canonique § 4 ; [E10](E10-cash-et-operations.md)).

---

## 7. Le pilotage : trois niveaux, le bruit, la gouvernance

### 7.1 Trois horizons, trois questions

| Niveau | Question | Fréquence | Nature de l'action |
| --- | --- | --- | --- |
| Quotidien | **Suis-je en vie ?** | Chaque jour, 10 min | Détecter une panne |
| Hebdomadaire | **Que décide-t-on ?** | Chaque semaine, 1 h | Réallouer, couper, lancer |
| Mensuel | **La structure tient-elle ?** | Chaque mois, 3 h | Changer le modèle |

### 7.2 Le quotidien — survie (seuils au palier P5)

| Indicateur | Seuil d'alerte |
| --- | --- |
| Dépense pub du jour | Écart > ±15 % au plan — repère 49 151 €/j (canonique § 5) |
| CA TTC du jour | Hors bande ±2σ (§ 7.6) — repère 142 445 €/j (4 333 196 ÷ 30,42) |
| Commandes du jour | Hors bande ±2σ — repère 1 979/j (60 200 ÷ 30,42) |
| MER, moyenne mobile 7 j | < 2,33 trois jours de suite — repère 2,90 (canonique § 2.3) |
| Taux de commande du site | −20 % relatif sur 7 j glissants |
| Diffusion effective des comptes | Tout compte livrant 0 € |

Rien d'autre : un tableau de bord quotidien qui contient une LTV n'est plus ouvert au bout de trois semaines.

### 7.3 L'hebdomadaire — décision

| Indicateur | Seuil d'alerte |
| --- | --- |
| nCAC hebdomadaire | > 43,38 € (= 86,75 ÷ 2,0) — repère 40,03 € (canonique § 2.4) |
| Marge de contribution CM3 | Négative, ou 2 semaines de baisse — repère 724 752 €/mois (canonique § 2.2) |
| aMER, moyenne mobile 28 j | Baisse pendant que le MER monte — repère 3,26 ([E01 § 3.4](E01-arithmetique-de-la-marque.md)) |
| Premier réachat à 60 j, cohorte échue | −2 pts sous la médiane des 6 précédentes |
| Concepts testés / gagnants | < 40 testés ou < 3 gagnants — repère 57 / 5,2 par sem. (canonique § 6) |
| Part de dépense sur créas > 60 j | > 50 % |

### 7.4 Le mensuel — structure

| Indicateur | Seuil d'alerte |
| --- | --- |
| Réachats cumulés M+3 par cohorte | 3 cohortes consécutives en baisse — repère canonique § 3 |
| EBITDA en % du CA HT | Sous le plan du palier — repère 10,1 % (canonique § 2.2) |
| BFR en jours de CA | +3 jours en un mois — repère 16 j (canonique § 4) |
| LTV 12 mois ÷ nCAC, par cohorte | < 2,0 : on n'accélère plus — repère 2,17 (canonique § 3) |
| Marge brute CM2 | −1 point — repère 61,5 % (canonique § 2.1) |
| Sur-attribution (Σ attribué ÷ réel) | > 1,15, ou +3 pts en un mois — repère 1,108 (canonique § 5) |

### 7.5 Pourquoi les fréquences ne se mélangent jamais

**Regarder un indicateur mensuel tous les jours est nuisible :** il n'a pas de valeur quotidienne interprétable. La LTV 12 mois de la cohorte de janvier ne bouge pas entre mardi et mercredi ; ce qui bouge est l'échantillon partiel du mois, du bruit pur. Et le bruit appelle l'action : tu coupes un budget, tu réinitialises l'apprentissage des campagnes, tu fabriques le décrochage que tu croyais observer.

**Regarder un indicateur quotidien une fois par mois est fatal**, et ça se chiffre. Le MER dérive de 2,90 à 2,20 — pixel cassé, plafond mal réglé, catalogue non synchronisé — et personne n'ouvre pendant 30 jours :

```
CA TTC à MER 2,20, dépense inchangée = 1 494 206 × 2,20 = 3 287 253 €
Manque à gagner = 4 333 196 − 3 287 253               = 1 045 943 € TTC
Contribution perdue = (1 045 943 ÷ 1,20) × 0,6145     =   535 610 €
Même incident détecté à J+3 : 535 610 × 3 ÷ 30        =    53 561 €
```

**Facteur 10 sur un seul incident** — et ces incidents ([C10](../etudes-de-cas/C10-compte-publicitaire-banni.md)) arrivent plusieurs fois par an à qui dépense 49 151 € par jour.

### 7.6 Le bruit : combien de variation est normale

Quatre gestes. **Un**, neutralise le jour de semaine : sur 90 jours, ratio moyen de chaque jour à la moyenne globale, puis divise chaque valeur par son indice — sinon tu alerteras tous les dimanches. **Deux**, moyenne mobile 7 jours et écart-type des valeurs corrigées sur 28 jours. **Trois**, trace la bande à ±2σ — *hypothèse à P5 :* CV quotidien corrigé de 9 %, cohérent avec le § 5.2 (1 979 commandes/jour ne donnent que 2,3 % de bruit de Poisson, le reste est commun).

```
Moyenne quotidienne = 4 333 196 ÷ 30,42 = 142 445 € TTC
σ = 0,09 × 142 445 = 12 820 €   →   bande ±2σ = ±25 640 €, soit ±18,0 %
```

**Quatre**, applique une règle de déclenchement écrite, pas ton intuition :

| Règle | Probabilité sous bruit pur | Fréquence attendue |
| --- | ---: | --- |
| Un point au-delà de 2σ | 2,28 % | 1 fois tous les 44 jours |
| Un point au-delà de 3σ | 0,13 % | 1 fois tous les 2 ans |
| Neuf points consécutifs du même côté de la moyenne | 0,39 % | 1 fois tous les 256 jours |
| Deux points sur trois au-delà de 2σ, même côté | ≈ 0,15 % | 1 fois tous les 1,8 an |

**Un jour à −18 % n'est pas un signal** : sous bruit pur, on l'attend six à sept fois par an. Quatre jours consécutifs à 121 000, 118 500, 112 000 et 108 900 € donnent z = −1,67 ; −1,87 ; −2,37 ; −2,62 : rien avant le quatrième, où deux points sur trois franchissent 2σ du même côté.

```
Coût des 4 jours d'attente :
   (142 445 × 4) − 460 400 = 109 380 € TTC  →  contribution 56 012 €
Coût d'une fausse alerte (hypothèse : une coupe brutale coûte 3 jours à −25 %
d'efficacité, le temps que les campagnes réapprennent) :
   3 × 49 151 × 2,90 × 0,25 = 106 903 € TTC  →  contribution 54 743 €
```

**Attendre quatre jours coûte 56 012 €, réagir à tort 54 743 €.** Même prix — et comme les fausses alertes sont dix fois plus fréquentes que les vraies pannes, la règle patiente gagne largement en espérance. C'est ce calcul, pas du sang-froid, qui empêche de casser un compte qui va bien.

### 7.7 La gouvernance de la donnée

Deux personnes de la même équipe qui annoncent deux chiffres différents pour le même mois n'ont pas un problème d'outil mais de **définition**, donc d'organisation.

```
CA TTC brut (canonique § 2)                     = 4 333 196 €
CA HT net des remises (8 %) et retours (3,5 %)  = 3 610 997 × 0,885 = 3 195 732 €
Écart entre deux réponses honnêtes : 35,6 %

Même mécanique sur la dépense. Hypothèse : agence 4 % + production 6 % du média.
Si « dépense pub » = média acheté seul : 1 494 206 ÷ 1,10 = 1 358 369 €
MER apparent = 4 333 196 ÷ 1 358 369 = 3,19    (au lieu de 2,90)
Marge au seuil EBITDA de 2,33 : 36,9 % affichés contre 24,4 % réels
```

**Tu te crois à 37 % du gouffre quand tu es à 24 %.** Quatre décisions.

- **Une source unique** : un entrepôt, un traitement nocturne, un propriétaire nommé. Les régies sont des **entrées**, jamais la référence. Un chiffre qui ne sort pas du système de référence n'entre pas en réunion, capture d'écran de régie comprise.
- **Un dictionnaire écrit**, versionné, daté. *Nouveau client* : première commande jamais passée sur un identifiant stable (e-mail normalisé + téléphone), à la date de commande, nette des annulations sous 14 jours, dédoublonnée entre marchés. *Dépense pub* : média HT + honoraires + influence et produits offerts + commissions d'affiliation + production créative + outils de mesure. *CA* : TTC brut pour le MER, HT net de remises et retours pour la marge, jamais l'inverse.
- **Un chiffre, un propriétaire**, qui répond de la définition et de sa stabilité, pas de sa valeur.
- **Un journal des changements** : toute modification est datée et l'historique recalculé, sinon tu compares des mois qui ne mesurent pas la même chose.

---

## 8. Les erreurs qui coûtent cher

**1. Additionner les ROAS de plateforme pour arbitrer un budget.** 41 364 clients revendiqués contre 37 324 réels (canonique § 5 et § 2.4) : nCAC apparent 36,12 € contre 40,03 €, soit **1 751 244 € de coût d'acquisition annuel absent du tableau de bord** — et 25,8 % d'écart dès qu'un septième partenaire de fin de parcours s'ajoute (§ 1.4).

**2. Changer de modèle d'attribution en cours d'exercice.** Passer du dernier clic au dégressif fait « chuter » la ligne Google marque de **1 816 776 € de CA annuel** (§ 2.4) sans qu'une vente ait bougé. Quelqu'un coupera le canal, ou félicitera un autre canal pour un transfert comptable.

**3. Juger un test avant sa fin.** Le seuil de 5 % ne vaut que pour **un seul regard, à une taille fixée d'avance**. À cinq regards, le taux réel de faux positifs monte autour de 14 % ; à un regard quotidien pendant un mois, il dépasse 25 % ([E07 § 7.4](E07-funnel-et-conversion.md)).

**4. Conclure d'un test géographique sous-dimensionné.** Sur la cellule du § 5.3, un test de 14 jours ne détecte rien sous **16,2 %** : un vrai effet de 10 % ressort « non significatif », et « la publicité n'est pas incrémentale » fait couper le bloc.

```
Bloc géo-coupable = 0,82 × 1 047 000 = 858 540 €/mois épargnés
Clients incrémentaux perdus = 0,82 × 12 204 = 10 007
Valeur perdue = 10 007 × 114,44 € = 1 145 201 €/mois
Solde = 858 540 − 1 145 201 = −286 661 €/mois = −3 439 932 €/an
```

**5. Confondre saisonnalité et effet publicitaire.** Novembre à P4 sans cellule témoin : budget +40 %, chiffre d'affaires +55 %.

```
Naïf : ΔCA ÷ Δdépense = 1 612 380 ÷ 418 800 = 3,85   → « excellent »
Hypothèse : la demande de novembre est de +38 % à dépense constante
   Part calendaire   = 0,38 × 2 931 600 = 1 114 008 €
   Part publicitaire = 1 612 380 − 1 114 008 = 498 372 €
   ROAS incrémental marginal = 498 372 ÷ 418 800 = 1,19   < 1,99 (seuil P4)
   Contribution = (498 372 ÷ 1,20) × 0,604 = 250 847 €
   Solde du surbudget = 250 847 − 418 800 = −167 953 € pour le mois
```

Tu recommences chaque année parce que l'interface affiche 3,85 ([C09](../etudes-de-cas/C09-piege-du-black-friday.md)).

---

## 9. Ce que ce module ne dit pas

**Il ne mesure pas l'effet de marque de long terme, et aucun instrument de la liste ne le fait.** Chaque méthode du § 4 a une fenêtre : six semaines pour un test géographique, cinq pour un holdout, huit à treize semaines de rémanence dans un MMM standard. Une structure de mémoire installée dans une tête, qui se déclenche quatorze mois plus tard, est mécaniquement **hors de toutes ces fenêtres**. *Hypothèse :* 12 % des nouveaux clients convertissent au-delà de 90 jours après leur première exposition.

```
CAC incrémental mesuré (§ 6.1) = 85,79 €  →  corrigé : 85,79 × 0,88 = 75,50 €
CAC marginal à 850 000 € (§ 6.4) : 115,38 × 0,88 = 101,53 €
```

**La correction déplace l'optimum vers le haut, et elle n'est elle-même pas mesurable.** Donc : traite l'optimum incrémental comme un **plancher** de budget, jamais comme un plafond. Ce que l'on ne peut pas mesurer est traité en [E12](E12-marque-et-actif.md), sur la base du module racine [10 — Sharp](../../modules/10-sharp-distinctivite.md) ; l'exigence expérimentale opposée vient du module racine [12 — Hopkins](../../modules/12-hopkins-publicite-scientifique.md). Les deux ont raison, et ce module est ce qui permet de les arbitrer au lieu d'en débattre.

**Il ne s'applique pas en dessous de P3.** Refais le § 5.2 sur 25 % de la France au palier P2 (230 200 € TTC/mois) : 1 892 € et 33 commandes par jour, CV de 32,1 %, appariement effondré à ρ ≈ 0,40, donc `D ≥ (2,80 × 665 ÷ 189)² = 97 jours`. Trois mois à couper un quart de ton unique marché, dans un palier qui perd déjà 19 838 € par mois : ce n'est pas une question de puissance statistique, c'est une question de survie. Avant P3, les seuls instruments honnêtes sont le MER blended, la cohorte à 90 jours, et l'extinction d'un canal à la fois en regardant le total.

**Il ne traite pas** de la mécanique de collecte — consentement, marquage côté serveur, API de conversion —, qui relève de [E06](E06-acquisition-payante.md) et [E07](E07-funnel-et-conversion.md), ni de ce qu'on fait quand on est déjà trop engagé pour couper : [E13](E13-risque-de-ruine.md).

> **À retenir :** l'incrémentalité mesurable est une borne inférieure de la valeur de ta publicité, pas sa valeur. Qui pilote uniquement sur les tests sous-investit lentement ; qui les ignore surinvestit vite. La discipline est de connaître le plancher et de décider consciemment de combien tu montes au-dessus.

---

## 10. Le tableau de bord du module

| # | Indicateur | Calcul | Fréquence | Seuil d'alerte |
| --- | --- | --- | --- | --- |
| 1 | Taux de sur-attribution | Σ clients attribués ÷ nouveaux clients réels | Mensuel | > 1,15, ou +3 pts en un mois |
| 2 | MER blended | CA TTC ÷ dépense totale, mobile 7 j | Quotidien | < MER seuil EBITDA du palier (canonique § 2.3) |
| 3 | aMER | CA TTC ÷ dépense de prospection, mobile 28 j | Hebdomadaire | Baisse 3 semaines de suite pendant que le MER monte |
| 4 | Couverture expérimentale | Part du budget annuel passée par un test valide depuis 12 mois | Trimestriel | < 60 % |
| 5 | Âge du dernier test par canal | Mois depuis le dernier test conclusif | Trimestriel | > 6 mois sur un canal à plus de 10 % du budget |
| 6 | Sources de vérité en circulation | Systèmes cités en réunion de pilotage | Mensuel | > 1 |

Les indicateurs 4 et 5 sont ceux que personne ne tient, et les seuls qui garantissent que les autres veulent dire quelque chose : un plan média dont 40 % du budget n'a jamais été testé a 40 % de son budget en croyance.

---

## 11. Exercices

À rendre dans [`ecommerce/exercices/E09-rendu.md`](../exercices/E09-rendu.md) ; corrigés dans `E09-corrige.md`.

**1 — La sur-attribution avec un canal de plus (réponse numérique unique).** Canonique § 5. Tu ajoutes un partenaire de cashback placé au paiement, qui touche 22 % des acheteurs, financé par 4 % du budget existant, dépense totale inchangée. Calcule (a) la nouvelle somme revendiquée, (b) le taux de sur-attribution, (c) le nCAC apparent, (d) l'écart au nCAC réel par client et par an. Puis dis en trois lignes ce que ce partenaire a réellement vendu.

**2 — Le point mort d'incrémentalité (réponse numérique unique).** Google marque, 62 458 €/mois, ROAS plateforme 4,00 (§ 6.2). Calcule (a) la part d'incrémentalité minimale pour l'équilibre en contribution à P5, (b) la même à P4 (marge brute 60,4 %), (c) le coût annuel de la ligne à 8 % d'incrémentalité, (d) le ROAS plateforme qu'il faudrait afficher pour être à l'équilibre à 8 %. Commente (d).

**3 — Ton audit d'attribution.** Sur ton dernier mois complet, additionne les nouveaux clients revendiqués par chaque régie, ton e-mail et tes partenaires, divise par les nouveaux clients réels de ta base de commandes, puis calcule ton nCAC apparent, ton nCAC réel, l'écart par client et l'écart annualisé. Écris le nombre de canaux qui touchent ton acheteur moyen.

**4 — Ta bande de bruit.** Sur 90 jours de CA quotidien : les sept indices de jour de semaine, la correction, l'écart-type des 28 derniers jours, ta bande à ±2σ en euros et en pourcentage. Combien de jours sont sortis de la bande, combien de fois as-tu réagi, et que t'ont coûté ces réactions selon la méthode du § 7.6 ?

**5 — Tes définitions écrites.** Rédige la définition de six termes : nouveau client, dépense publicitaire, chiffre d'affaires, commande, retour, remise. Fais calculer le même mois indépendamment par deux personnes à partir de ces définitions seules et mesure l'écart. S'il dépasse 2 %, identifie la phrase qui manquait.

**6 — Décision : concevoir un test géographique complet, seuils écrits d'avance.** Tu soupçonnes ton second canal dominant de faire de la récolte. **Option A** : couper 100 % de ce canal sur une cellule appariée. **Option B** : l'augmenter de 80 % sur une cellule appariée. Rends le protocole complet — unités et critère d'appariement, σ et ρ estimés sur ton historique, durée pour détecter 10 % par la formule du § 5.2, effet minimum détectable à 14 jours, seuils de décision chiffrés **écrits avant le lancement**, conversion en CAC incrémental, LTV de comparaison. Tranche, justifie, et écris la condition sous laquelle l'autre option deviendrait la bonne — indice : elles ne mesurent pas la même quantité (§ 5.1, étape 5).

---

*Fin du module E09. Suite : [E10](E10-cash-et-operations.md), parce qu'un CAC incrémental de 85,79 € financé sur 24 mois est d'abord un problème de trésorerie ; [E12](E12-marque-et-actif.md) pour ce que ce module ne sait pas mesurer ; et [C06 — Le test qui a supprimé 22 % du budget sans perdre de CA](../etudes-de-cas/C06-test-incrementalite.md) pour le protocole du § 5 exécuté de bout en bout.*
