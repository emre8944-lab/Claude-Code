# Module 01 — L'économie unitaire e-commerce

> **Objet :** savoir, pour chaque commande, combien tu gagnes réellement — et donc
> combien tu as le droit de payer pour l'obtenir. C'est le module le plus important du
> cursus. Tout ce qui suit (choix du produit, prix, pub, scaling) en dépend.
> **Prérequis :** module 00. Le module 13 du cursus business
> ([CAC, LTV, payback](../../modules/13-unit-economics.md)) est le fondement théorique ;
> ici, on l'applique au e-commerce, au centime.
> **Devoirs :** `exercices/01-rendu.md`

---

## 0. Pourquoi ce module passe avant le produit

Parce que **c'est l'économie unitaire qui dit quel produit tu as le droit de vendre.**
Un produit à 24,90 € avec 60 % de marge ne peut pas, mathématiquement, être vendu de
façon rentable avec de la publicité Meta en Europe s'il n'y a pas de réachat. Pas
« difficilement ». Pas « avec de très bonnes créas ». **Mathématiquement.** Tu vas voir
pourquoi, et tu ne perdras plus jamais d'argent à tester ce genre de produit.

---

## 1. Le piège n° 1 : la TVA

En France, les prix affichés au consommateur sont **TTC**. Sur un produit vendu 59 €,
**9,83 € appartiennent à l'État** (TVA à 20 %). Ils transitent par ton compte, ils ne
sont pas à toi.

```
Prix HT = Prix TTC ÷ 1,20        (taux normal français)
59 € TTC → 49,17 € HT → 9,83 € de TVA
```

Conséquences pratiques :

- **Tous tes calculs de marge se font en HT.** Toujours.
- **Shopify et Meta affichent en général du TTC.** Un « ROAS de 2 » affiché par Meta
  est un ROAS de 1,67 en HT. Vérifie dans ton intégration ce que ton pixel remonte
  (montant avec ou sans taxes, avec ou sans frais de port) et **note-le** : toutes tes
  règles de décision en dépendent.
- **Mets la TVA de côté** sur un compte séparé, chaque semaine. Le nombre de marques
  qui ont financé leur croissance avec la TVA collectée, puis ont été incapables de la
  reverser, est considérable.
- Quand tu vendras dans d'autres pays de l'UE (au-delà de 10 000 € de ventes
  transfrontalières annuelles), tu factureras la **TVA du pays du client** (19 % en
  Allemagne, 22 % en Italie, 21 % en Espagne…) via le guichet unique **OSS**
  (module 13). Tes prix HT changent donc d'un pays à l'autre à prix TTC égal.

---

## 2. Le compte de résultat d'une commande

On découpe la marge en trois étages. C'est le vocabulaire standard des marques DTC
sérieuses, et c'est celui qu'on utilise dans tout le cursus.

```
CA HT
− Coût du produit rendu (achat + transport jusqu'à ton entrepôt + douane)
= CM1  (marge brute produit)

− Emballage, préparation, transport jusqu'au client
− Frais de paiement
− Provision retours, remboursements, casse, SAV
= CM2  (marge de contribution avant marketing)     ← le chiffre qui décide

− Coût d'acquisition (pub, influence, créas)
= CM3  (marge de contribution après marketing)     ← ce qui paie tes frais fixes

− Frais fixes (équipe, outils, loyer, comptable)
= EBITDA (résultat opérationnel)
```

### Exemple Nilo — une fontaine seule à 59 € TTC

| Ligne | Montant | % du CA HT |
|---|---|---|
| Prix TTC | 59,00 € | |
| TVA (20 %) | −9,83 € | |
| **CA HT** | **49,17 €** | 100 % |
| Coût produit rendu (usine + fret + douane) | −11,00 € | 22,4 % |
| **CM1** | **38,17 €** | **77,6 %** |
| Emballage d'expédition | −0,70 € | |
| Préparation logistique (3PL) | −2,20 € | |
| Transport vers le client | −5,30 € | |
| Frais de paiement (≈ 1,8 % + 0,25 €) | −1,31 € | |
| Provision retours / SAV / casse (4 % du HT) | −1,97 € | |
| **CM2** | **26,69 €** | **54,3 %** |

Regarde l'écart entre CM1 (77,6 %) et CM2 (54,3 %) : **23 points** disparaissent dans
la logistique, le paiement et les retours. C'est l'erreur classique du débutant :
« je l'achète 11 €, je le vends 59 €, je fais ×5 » — non. Tu gagnes 26,69 € avant
publicité, pas 48 €.

> **Règle.** Si tu ne connais pas ta CM2 au centime près, tu ne sais pas si tu gagnes de
> l'argent. Tout le reste de ce module en découle.

---

## 3. Le seuil de rentabilité : CPA et ROAS d'équilibre

### 3.1 Les formules

```
CPA d'équilibre   = CM2 par commande
ROAS d'équilibre  = Panier moyen ÷ CM2 par commande
                  = 1 ÷ (CM2 en % du CA)      (en HT)
                  = 1,20 ÷ (CM2 en % du HT)   (si ton ROAS est lu en TTC, TVA 20 %)
```

Pour la fontaine seule :

```
CPA d'équilibre = 26,69 €
ROAS d'équilibre (TTC) = 59 ÷ 26,69 = 2,21
ROAS d'équilibre (HT)  = 49,17 ÷ 26,69 = 1,84
```

Si Meta t'affiche un ROAS de 2,0 sur cette fontaine (en TTC), **tu perds de l'argent sur
chaque commande**. Beaucoup de débutants célèbrent un « ROAS de 2 » qui les ruine.

### 3.2 La table à connaître par cœur

| CM2 en % du CA HT | ROAS d'équilibre (HT) | ROAS d'équilibre (lu en TTC, TVA 20 %) |
|---|---|---|
| 40 % | 2,50 | 3,00 |
| 50 % | 2,00 | 2,40 |
| 55 % | 1,82 | 2,18 |
| 60 % | 1,67 | 2,00 |
| 65 % | 1,54 | 1,85 |
| 70 % | 1,43 | 1,71 |

### 3.3 Pourquoi un produit à 24,90 € sans réachat est mort

Prends un produit à 24,90 € TTC (20,75 € HT), qui coûte 4 € rendu. Même avec une
logistique légère (5 € de préparation et transport, 0,70 € de paiement, 0,80 € de
provision), la CM2 vaut ≈ **10,25 €**.

Or, en France, un CPA de 10 € sur de l'acquisition froide Meta est **exceptionnel**.
Les CPA réalistes pour un produit grand public nouveau se situent plutôt entre
**15 et 40 €**. Donc chaque commande coûte plus qu'elle ne rapporte. Il n'y a que trois
issues : augmenter le panier (bundles, module 06), avoir un réachat fort et prouvé
(consommable, module 11), ou vendre sans pub payante (organique, module 10).

> **Règle de sélection produit qui en découle** (module 02) : vise un prix de vente
> d'au moins **35-40 € TTC** et une CM2 d'au moins **50 %** — sauf consommable à
> réachat prouvé.

---

## 4. Le panier moyen change tout

Nilo propose trois offres (on les construit au module 06). Même calcul pour chacune :

| | Fontaine seule | Fontaine + 6 filtres | Duo (2 fontaines) |
|---|---|---|---|
| Prix TTC | 59,00 € | 79,00 € | 109,00 € |
| CA HT | 49,17 € | 65,83 € | 90,83 € |
| Coût produit rendu | 11,00 € | 13,40 € | 22,00 € |
| Emballage + préparation + transport | 8,20 € | 8,40 € | 10,40 € |
| Frais de paiement | 1,31 € | 1,67 € | 2,21 € |
| Provision retours/SAV (4 %) | 1,97 € | 2,63 € | 3,63 € |
| **CM2** | **26,69 €** | **39,73 €** | **52,59 €** |
| CM2 en % du HT | 54,3 % | 60,4 % | 57,9 % |
| ROAS d'équilibre (TTC) | 2,21 | 1,99 | 2,07 |

**20 € de plus sur le prix (seule → pack filtres) = 13 € de CM2 en plus, soit +49 %.**
Pourquoi ? Parce que les coûts fixes par colis (préparation, transport, emballage) ne
bougent presque pas. Chaque euro de panier supplémentaire tombe quasiment entier dans
la marge. C'est pour ça que les marques rentables sont obsédées par le panier moyen.

Avec un mix réaliste (45 % seule, 40 % pack filtres, 15 % duo) :

```
Panier moyen TTC = 0,45 × 59 + 0,40 × 79 + 0,15 × 109 = 74,50 €
Panier moyen HT  = 62,08 €
CM2 moyenne      = 0,45 × 26,69 + 0,40 × 39,73 + 0,15 × 52,59 = 35,79 €   (57,7 % du HT)
CPA d'équilibre  = 35,79 €
ROAS d'équilibre (TTC) = 74,50 ÷ 35,79 = 2,08
```

---

## 5. Le CPA cible et le ROAS cible

L'équilibre ne suffit pas : il faut payer les frais fixes et dégager un profit. Tu
fixes donc une **CM3 cible par commande**. Un repère de départ : **15 % du CA HT**
(assez pour couvrir des frais fixes de 8-12 % à l'échelle et laisser un profit).

```
CM3 cible        = 15 % × 62,08 € = 9,31 €
CPA cible        = CM2 − CM3 cible = 35,79 − 9,31 = 26,48 €
ROAS cible (TTC) = 74,50 ÷ 26,48 = 2,81
```

**Nilo doit donc obtenir des clients à 26 € ou moins, soit un ROAS de 2,8 en TTC.**

### Est-ce atteignable ? L'équation du module 00 répond

```
CPA = CPM ÷ (1 000 × CTR × CR)
Avec CPM 9 €, CTR 1,3 %, conversion 2,8 % :
CPA = 9 ÷ (1 000 × 0,013 × 0,028) = 9 ÷ 0,364 = 24,73 €   → sous la cible ✓
```

Et regarde ce qui se passe si la conversion tombe de 2,8 % à 2,0 % (une page moins
bonne, un délai de livraison qui s'allonge, une rupture de l'offre bundle) :

```
CPA = 9 ÷ (1 000 × 0,013 × 0,020) = 34,62 €
CM3 = 35,79 − 34,62 = 1,17 € par commande
```

**Une baisse de 0,8 point de conversion fait passer la marque de rentable à
quasi nulle.** C'est pour ça qu'on suit le taux de conversion tous les jours.

---

## 6. Mesurer la vérité : ROAS plateforme, MER, nc-ROAS

### 6.1 Pourquoi le ROAS de Meta ment

Ce n'est pas malveillant, c'est structurel :

- **Attribution par défaut :** Meta s'attribue une vente si la personne a cliqué dans
  les 7 jours **ou vu** la pub dans la journée précédente. Une partie de ces ventes
  aurait eu lieu sans la pub.
- **Double comptage :** si le client a vu ta pub Meta, cliqué sur une pub Google, puis
  sur une vidéo TikTok, **les trois plateformes s'attribuent la même vente**.
- **Perte de signal :** à l'inverse, certaines ventes réellement causées par Meta ne
  sont pas vues (iOS, bloqueurs, navigation multi-appareils).

Exemple réel de ce qu'on observe : Shopify affiche 100 000 € de ventes sur la semaine.
Meta revendique 70 000 €, Google 35 000 €, TikTok 20 000 €. Total revendiqué :
**125 000 €**, soit 125 % des ventes réelles. Quelqu'un ment — tout le monde, en fait.

### 6.2 Le MER : ton étoile polaire

```
MER (Marketing Efficiency Ratio) = CA total ÷ Dépense marketing totale
```

Le MER ne se soucie pas de l'attribution : il prend **toutes** les ventes réelles
(Shopify) et **toutes** les dépenses marketing (pub + influence + créas). Il ne peut pas
mentir. Dans ce cursus, on le calcule **sur le CA TTC**, parce que c'est ce que Shopify
affiche ; choisis une convention et ne la change jamais.

```
MER d'équilibre (CM3 = 0, TTC, TVA 20 %) = 1,20 ÷ CM2 en % du HT
Nilo : 1,20 ÷ 0,577 = 2,08
```

### 6.3 Le nc-ROAS : pour ne pas se mentir sur l'acquisition

Le MER inclut les ventes des clients existants (réachats, emails). Quand ta base
client grossit, le MER monte tout seul et peut masquer une acquisition qui se dégrade.

```
nc-ROAS (ou aMER) = CA des NOUVEAUX clients ÷ Dépense d'acquisition
nCAC              = Dépense d'acquisition ÷ Nombre de NOUVEAUX clients
```

Shopify distingue nouveaux et anciens clients dans ses rapports. **Pilote
l'acquisition au nCAC, le business au MER.**

### 6.4 L'incrémentalité : la seule vérité causale

La vraie question n'est pas « d'où vient cette vente » mais « **combien de ventes en
plus** ai-je grâce à cette dépense ». Elle ne se mesure que par l'expérience : coupe
une dépense sur une zone ou une période comparable et regarde ce que deviennent les
ventes **totales**. C'est le protocole de Hopkins (module 12 du cursus business), et le
module 09 te montre comment le faire sur Meta à partir de 50 k€/mois de dépense.

---

## 7. La LTV : quand as-tu le droit d'acheter un client à perte ?

La LTV (*lifetime value*), calculée **en marge**, pas en CA. Chez Nilo, sur 12 mois :

| Source de marge | Calcul | CM2 |
|---|---|---|
| Première commande | mix du chapitre 4 | 35,79 € |
| Réachats de filtres (pack de 6 à 19,90 € en abonnement, module 06) | 38 % des clients × 1,8 commande × 9,34 € de CM2 | 6,39 € |
| Achat croisé (2e produit) | 10 % × 20 € de CM2 | 2,00 € |
| Coût de rétention (email, SMS) | | −0,80 € |
| **LTV 12 mois (en marge)** | | **43,38 €** |

Avec un nCAC de 26,48 € : **LTV / CAC = 1,64**, et le client est rentable **dès la
première commande** (payback immédiat).

> **Nuance importante avec le module 13 du cursus business.** Là-bas, je te donnais le
> repère LTV/CAC ≈ 3. En e-commerce où l'achat unique domine, ce ratio est rarement
> atteint — et ce n'est pas grave **si le client est rentable dès la première
> commande** : le payback immédiat remplace la marge de sécurité, parce que tu ne
> finances rien dans le temps. Le module 13 le disait déjà : un payback sur la première
> transaction, c'est de la croissance à capital nul.
>
> Le repère opérationnel devient donc :
> - **Produit à réachat faible :** CM3 de la première commande ≥ 0, toujours.
> - **Consommable à réachat prouvé par des cohortes réelles :** tu peux accepter une
>   première commande à perte, à condition que la LTV à 90 jours couvre le CAC et que
>   ta trésorerie finance ce délai. Là, le repère LTV/CAC ≈ 3 redevient pertinent.
>   Cas complet au module 14 (cas d'école B).

**Ne jamais acheter à perte sur une LTV estimée.** Seulement sur une LTV **observée**
sur des cohortes réelles d'au moins 60 à 90 jours.

---

## 8. Les frais fixes et le point mort

Au début, tes frais fixes sont petits mais pas nuls :

| Poste | Mensuel |
|---|---|
| Shopify + applications | 150 € |
| Email (Klaviyo ou équivalent) | 50 € |
| Outils créa (CapCut, Canva…) | 30 € |
| Monteur vidéo freelance | 800 € |
| Comptable | 150 € |
| Banque, assurance, divers | 70 € |
| **Total** | **1 250 €** |

```
Commandes nécessaires pour couvrir les fixes = Frais fixes ÷ CM3 par commande
Nilo : 1 250 ÷ 9,31 = 135 commandes / mois ≈ 5 par jour
```

Note que ton propre salaire n'est pas dedans. Il devrait l'être dès que possible — sinon
tu confonds un emploi non rémunéré avec une entreprise rentable.

---

## 9. La trésorerie : pourquoi les marques rentables font faillite

Tu peux être rentable sur chaque commande et manquer de cash. Voici pourquoi :

```
Jour 0    tu paies 30 % d'acompte à l'usine
Jour 25   tu paies les 70 % restants avant expédition
Jour 60   la marchandise arrive à l'entrepôt
Jour 60+  tu paies la pub tous les jours (carte bancaire)
Jour 62+  les ventes sont encaissées (Shopify reverse sous quelques jours)
Jour 120  le stock est écoulé
```

Tu décaisses le stock **60 à 90 jours avant** de l'encaisser. Quand tu grandis, ce
décalage grandit avec toi. Calcul simple de la trésorerie immobilisée en stock :

```
Stock à financer ≈ Coût produit mensuel × Mois de couverture
Mois de couverture ≈ délai d'approvisionnement (2) + stock en entrepôt (1) + sécurité (0,5) = 3,5
```

| CA mensuel TTC | Coût produit mensuel (20 % du HT) | Stock immobilisé (× 3,5) |
|---|---|---|
| 100 000 € | 16 700 € | ≈ 58 000 € |
| 300 000 € | 50 000 € | ≈ 175 000 € |
| 1 000 000 € | 166 700 € | ≈ 583 000 € |

**Passer de 100 k€ à 300 k€ par mois exige ≈ 117 000 € de trésorerie supplémentaire,
rien que pour le stock.** Si ta marque dégage 30 000 € par mois à ce stade, il lui faut
4 mois de profits entièrement réinvestis — pendant lesquels toute croissance plus rapide
est impossible. Les solutions (conditions fournisseur, financement sur revenus,
précommandes, prêt bancaire) sont au module 12. Retiens pour l'instant : **la
croissance consomme de la trésorerie, et la vitesse de croissance maximale est une
décision financière autant que marketing.**

Deux détails français qui aident :
- **Autoliquidation de la TVA à l'importation** : depuis 2022, les entreprises
  françaises déclarent la TVA d'import sur leur déclaration de TVA au lieu de la payer
  en douane. Tu n'avances plus ces 20 %.
- **La TVA collectée** n'est pas ta trésorerie (section 1). Ne la compte jamais dedans.

---

## 10. Le P&L à 1 M€ par mois : deux marques, même chiffre d'affaires

Deux marques font 1 000 000 € TTC en un mois. Même structure de coûts produit. La
seule différence : l'efficacité marketing.

| Ligne | Marque A (MER 3,1) | Marque B (MER 2,2) |
|---|---|---|
| CA TTC | 1 000 000 € | 1 000 000 € |
| **CA HT** | **833 300 €** | **833 300 €** |
| Coût produit rendu (20 %) | −166 700 € | −166 700 € |
| Logistique et transport (11 %) | −91 700 € | −91 700 € |
| Frais de paiement (2,2 %) | −18 300 € | −18 300 € |
| Retours, SAV, casse (3 %) | −25 000 € | −25 000 € |
| **CM2** | **531 600 €** (63,8 %) | **531 600 €** (63,8 %) |
| Marketing total | −320 000 € | −454 500 € |
| **CM3** | **211 600 €** (25,4 %) | **77 100 €** (9,3 %) |
| Frais fixes (équipe, outils, locaux) | −95 000 € | −95 000 € |
| **EBITDA** | **+116 600 €** (14 %) | **−17 900 €** (−2,1 %) |

La marque B a exactement le même chiffre d'affaires, le même produit, la même équipe.
Elle perd de l'argent. Et comme elle grandit, elle consomme en plus du cash pour son
stock (section 9). **Elle est en train de mourir avec 1 M€ de CA par mois.**

Les seuils de cette structure :

```
MER pour CM3 = 0      : 1 000 000 ÷ 531 600 = 1,88
MER pour EBITDA = 0   : 1 000 000 ÷ (531 600 − 95 000) = 2,29
```

Sous un MER de 2,29, cette marque perd de l'argent. Au-dessus de 3, elle en gagne
beaucoup. **Toute la différence entre A et B se joue sur les créas, la conversion, le
panier et la rétention** — c'est-à-dire sur les modules 06 à 11.

---

## 11. Ton tableau de bord quotidien

Neuf lignes. Chaque matin. Dans un tableur ou un outil (module 13). Le template est dans
[boîte à outils › templates](../boite-a-outils/templates.md).

| # | Indicateur | Source | Alerte si… |
|---|---|---|---|
| 1 | CA TTC et HT de la veille | Shopify | — |
| 2 | Nombre de commandes, panier moyen | Shopify | Panier −10 % sur 7 jours |
| 3 | Dépense marketing totale | Plateformes | — |
| 4 | **MER** | Calcul | Sous ton MER cible 3 jours de suite |
| 5 | Nouveaux clients et **nCAC** | Shopify + calcul | Au-dessus du CPA cible 3 jours de suite |
| 6 | **CM3 estimée** = CA HT × CM2 % − marketing | Calcul | Négative |
| 7 | Taux de conversion du site | Shopify | −15 % sur 3 jours |
| 8 | Jours de stock restants par produit | Stock ÷ ventes/jour | < délai d'approvisionnement + 15 jours |
| 9 | Trésorerie disponible (hors TVA due) | Banque | < 6 semaines de dépenses |

---

## 12. Les pièges

1. **Calculer en TTC.** Tu te crois 20 % plus riche que tu ne l'es.
2. **Oublier les « petits » coûts.** Frais de paiement, provision retours, emballage :
   5 à 8 € par commande, c'est souvent toute ta marge nette.
3. **Calculer la CM2 sur le meilleur produit** alors que le mix réel est différent.
   Calcule-la sur le panier réel.
4. **Piloter au ROAS de la plateforme.** Pilote au MER et au nCAC ; utilise le ROAS de
   la plateforme seulement pour comparer des pubs **entre elles**.
5. **Confondre marge et trésorerie** (section 9).
6. **Oublier que le CPA marginal monte** quand tu augmentes le budget (module 13 du
   cursus business, section 2.2) : ton CPA moyen de 25 € à 500 €/jour ne sera pas ton
   CPA à 5 000 €/jour.
7. **Oublier la saisonnalité.** Les CPM grimpent fortement en novembre-décembre (tout le
   monde fait sa pub de Black Friday et de Noël). Ton CPA de septembre n'est pas celui
   de novembre.

---

## 13. Devoirs — à rendre dans `exercices/01-rendu.md`

**Exercice 1 — Le P&L d'une commande.** Prends un produit que tu envisages (ou, si tu
n'en as pas encore, un produit vu en pub cette semaine). Estime chaque ligne du
tableau du chapitre 2 et calcule CM1, CM2, CPA d'équilibre et ROAS d'équilibre en TTC.
Indique la source de chaque estimation.

**Exercice 2 — Le panier.** Imagine deux offres de panier supérieur pour ce produit
(bundle, quantité, accessoire). Refais le calcul pour chacune. De combien la CM2
augmente-t-elle ?

**Exercice 3 — Le CPA cible.** Avec une CM3 cible de 15 % du HT, calcule ton CPA cible
et ton ROAS cible. Puis, avec un CPM de 10 € et un CTR de 1,2 %, calcule le taux de
conversion minimum dont ton site a besoin pour l'atteindre.

**Exercice 4 — Le faux ROAS.** Une marque voit : Shopify 48 000 € TTC sur la semaine,
dépense Meta 14 000 €, dépense Google 3 000 €, Meta revendique 41 000 € de ventes,
Google 12 000 €. Sa CM2 est de 58 % du HT. Calcule le ROAS Meta affiché, le MER réel,
le MER d'équilibre. Gagne-t-elle de l'argent ?

**Exercice 5 — La trésorerie.** Ton produit coûte 20 % du HT, ton délai
d'approvisionnement est de 2 mois. Combien de trésorerie te faut-il immobiliser en stock
à 50 000 €, 150 000 € et 500 000 € de CA mensuel TTC ?

---

*Module suivant : [02 — Trouver le produit](02-trouver-le-produit.md). Maintenant que tu
sais ce qu'un produit doit rapporter, on va en chercher un qui le fait.*
