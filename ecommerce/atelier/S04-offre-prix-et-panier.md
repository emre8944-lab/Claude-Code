# Séance S04 — L'offre, le prix et le panier

> **Niveau requis :** L02–L03 · **Durée :** 5 h · **Livrable :** gamme à trois étages, prix arrêtés, tableau de construction d'AOV, seuil de franco de port, politique de remise · **Modules :** [E01](../modules/E01-arithmetique-de-la-marque.md), [E03](../modules/E03-offre-et-prix.md)
> **Ce que tu ne peux pas faire sans avoir fait cette séance :** acheter du trafic. Un panier moyen trop bas rend ton coût d'acquisition non finançable, et aucune créativité publicitaire ne répare une arithmétique de panier.

---

## 1. Où tu en es

Tu sors de [S03](S03-produit-et-cogs.md) avec un COGS rendu entrepôt au centime, un produit spécifié contre les défauts de tes concurrents, et un coefficient qui franchit — ou non — le plancher ×5,0 de la [Porte 0](../mentorat/jalons.md).

Décidé : ce que le produit est, ce qu'il coûte, chez qui il se fabrique.

Pas décidé : **à quel prix il se vend, sous quelles formes il s'achète, et quel montant moyen sort d'une commande.** Le prix de S03 était un prix cible provisoire ; il servait à tester la porte, pas à être imprimé.

Et un point que S03 a laissé ouvert : ton coefficient produit ne dit presque rien de ta capacité à financer un client. Le coefficient se calcule sur une unité ; ton coût d'acquisition et ta logistique se paient **par commande**. Deux comptabilités différentes, que cette séance réconcilie.

---

## 2. Ta mission

1. **Fixer le prix** de ton produit héros par trois méthodes indépendantes, et trancher quand elles divergent.
2. **Construire la gamme à trois étages**, avec le rôle chiffré de chacun.
3. **Remplir le tableau de construction d'AOV** : partir du prix unitaire, empiler les six leviers avec un taux d'adoption estimé, sortir un AOV cible.
4. **Calculer ton seuil de franco de port** à partir de ta distribution de paniers et de ton coût de transport réel.
5. **Écrire ta politique de remise**, dont la liste de ce que tu ne feras jamais.

*Acronymes : **AOV** — average order value, panier moyen par commande. **MER** — media efficiency ratio, CA TTC total ÷ dépense publicitaire totale. **COGS** — coût de revient marchandise rendu entrepôt.*

---

## 3. Ce dont tu disposes

| Ressource | Usage |
|---|---|
| Ton livrable S03 | Le COGS au centime, et ton coût logistique par commande |
| [canoniques § 2.1 et § 2.3](../donnees/chiffres-canoniques.md) | Structure de coût variable et MER seuil, palier par palier |
| [canoniques § 7 et § 8](../donnees/chiffres-canoniques.md) | +10 % d'AOV vaut 71,7 % de l'EBITDA annuel ; P5 → P5+ : AOV de 71,98 € à 77,20 € TTC, remises de 8,0 % à 5,5 % |
| [E01](../modules/E01-arithmetique-de-la-marque.md) § 7.2 | Pourquoi l'AOV bat la conversion : la logistique est un coût par commande, pas par euro |
| `python3 ecommerce/outils/calculateur.py` | Ta marge brute et ton MER seuil, panier par panier |

**Convention :** les prix de vente sont **TTC**, les coûts et les marges **HT**, la TVA est à 20 % comme dans tout le cursus.

---

## 4. La méthode, pas à pas

### 4.1 Fixer le prix par trois méthodes convergentes

Une seule méthode donne un prix qu'on ne sait pas défendre. Trois méthodes donnent trois nombres, et c'est leur écart qui t'apprend quelque chose.

**Méthode 1 — par la marge nécessaire.** Elle ne donne pas un prix mais un **plancher**, sous lequel l'acquisition payante ne se finance pas. Deux niveaux, et il faut les deux. Au niveau de l'unité, c'est le coefficient minimum de [C01](../etudes-de-cas/C01-coefficient-insuffisant.md) § 8, déjà calculé en S03 :

```
Prix plancher unitaire TTC = COGS × coefficient minimum
```

Au niveau du panier — le niveau qui décide vraiment — on part du MER seuil. Soit `M` le MER que ta catégorie permet, `L` ton coût logistique **par commande** en euros HT, `v` la somme de tes coûts variables proportionnels au chiffre d'affaires (COGS, paiement, retours, remises, en part du CA HT) et `t` la TVA :

```
MER seuil (CM3 = 0) = (1 + t) × a ÷ [ a × (1 − v) − L ]        où a = AOV en € HT

En posant MER seuil = M et en résolvant :

AOV plancher HT = M × L ÷ [ M × (1 − v) − (1 + t) ]
```

C'est la formule la plus utile de la séance. **Ton panier minimum ne dépend pas de ton produit mais de ton colis** : plus ta logistique par commande est chère, plus ton AOV plancher monte, et pas linéairement — le dénominateur s'effondre quand `M` s'approche de `(1+t)/(1−v)`.

**Méthode 2 — par la référence concurrentielle.** Relève les prix de cinq à huit concurrents directs, sur trois points de vente chacun (leur site, une place de marché, un revendeur), le même jour, remises en cours notées à part. Tu obtiens une fourchette et une médiane, donc la **zone de plausibilité** de ta catégorie — l'ancrage que ton client a déjà en tête. Ce que ça ne te donne pas : un prix. Un prix aligné sur la médiane d'une catégorie n'a aucune raison d'être choisi.

**Méthode 3 — par la valeur perçue.** Quarante réponses minimum, recrutées dans ta cible et pas dans ton entourage, sur le produit décrit et montré, sans prix affiché. Quatre questions, dans cet ordre : à partir de quel prix ce produit vous paraîtrait **trop cher** ; à partir de quel prix **cher mais justifiable** ; en dessous de quel prix **bon marché** ; en dessous de quel prix vous **douteriez de sa qualité**.

La zone acceptable va de la médiane de la question 4 à celle de la question 1 ; le point d'indifférence est l'intersection des courbes cumulées des questions 2 et 3. **Ce test ne prédit pas les ventes** — on y répond sur une intention, pas sur un acte — mais il détecte deux choses avec fiabilité : un prix qui déclenche du doute par le bas, et la **dispersion** des réponses, qui dit si ta catégorie a un ancrage ferme ou flou.

**L'arbitrage quand les trois divergent.** Quatre situations, quatre décisions :

| Situation | Décision |
|---|---|
| Plancher (M1) < référence (M2) < valeur perçue (M3) — le cas confortable | Prends le haut de la fourchette, pas le milieu |
| Plancher **au-dessus** de la référence : ton format ne finance pas ton acquisition | Ne monte pas le prix unitaire, **change l'unité de vente** — § 4.2 |
| Valeur perçue très dispersée : tu parles à deux segments | Choisis-en un ; le prix suivra |
| Valeur perçue sous la référence : le produit ne porte pas sa preuve | Le problème est en S05 et S07, pas ici |

La deuxième ligne est la plus fréquente et la plus mal traitée. Quand la marge nécessaire exige un prix que la catégorie refuse, augmenter le prix unitaire ne marche presque jamais — l'ancrage est solide. **Vendre autre chose que l'unité, si.**

### 4.2 Construire la gamme en trois étages

| Étage | Rôle | Part de volume visée | Ce qu'il ne doit jamais être |
|---|---|---|---|
| **1. La porte d'entrée** | Exister au prix d'essai, capter la recherche générique, servir d'ancrage de comparaison | 10 à 20 % | La page d'atterrissage de tes publicités |
| **2. Le héros** | Porter le volume et financer le coût d'acquisition | 55 à 70 % | Un produit dont le MER seuil dépasse ton MER atteignable |
| **3. L'étage de marge** | Tirer l'AOV, améliorer la marge brute mixte, rendre le héros raisonnable par contraste | 10 à 25 % | Un produit qu'on pousse — il se choisit, il ne se vend pas |

**Le piège du coefficient sur les lots**, cœur de la séance. Un lot se vend avec une remise au volume : son coefficient par SKU **baisse**. Sa marge brute par commande **monte**, parce que la logistique, la préparation et la part fixe du paiement ne se dupliquent pas. Les deux indicateurs partent en sens contraire :

> **À retenir :** le plancher ×5,0 s'applique au **produit héros au prix catalogue unitaire**, jamais au lot remisé. Un lot se juge sur le **MER seuil du panier**, qui est le seul nombre comparable à ton MER réel.

Calcule donc, pour chaque étage, la ligne complète : CA HT, COGS, logistique par commande, paiement, retours, marge brute, taux de marge brute, MER seuil. C'est trois colonnes de tableur et c'est ce qui décide quelle SKU ton compte publicitaire a le droit de pousser.

### 4.3 Les six leviers d'AOV et le tableau de construction

Les six mécaniques d'[E03](../modules/E03-offre-et-prix.md) § 4, dans l'ordre décroissant de leur effet habituel :

1. **Le lot** — plusieurs unités dans une commande, avec remise au volume. De loin le plus puissant : il agit sur le mix, pas sur les marges.
2. **La montée en gamme** — version ou format supérieur du même produit, sur la fiche.
3. **La vente croisée** — accessoire complémentaire, sur la fiche et dans le panier.
4. **Le seuil de franco de port** — le palier qui déclenche la livraison offerte (§ 4.4).
5. **Le réapprovisionnement programmé** — engagement sur *n* livraisons contre remise, ou abonnement.
6. **L'ajout après paiement** — offre en un clic sur la page de confirmation, sans re-saisie.

**Trois règles rendent le tableau honnête.** Le taux d'adoption s'écrit **avant** la mise en ligne, comme un pari, puis se mesure — écrit après coup, c'est une justification. Un levier dont tu ne sauras pas mesurer l'adoption ne rentre pas dans le tableau. Et on n'empile pas plus de trois leviers au lancement : au-delà, la page devient un couloir de vente et la conversion paie ce que l'AOV gagne.

**Le tableau vierge à copier :**

| # | Levier | Mécanique retenue | Taux d'adoption estimé | Effet unitaire TTC | Effet pondéré TTC | AOV cumulé TTC |
|---|---|---|---:|---:|---:|---:|
| — | *Base : prix unitaire catalogue* | | | | | |
| 1 | Le lot | | | | | |
| 2 | La montée en gamme | | | | | |
| 3 | La vente croisée | | | | | |
| 4 | Le franco de port | | | | | |
| 5 | Le réappro. programmé | | | | | |
| 6 | L'ajout après paiement | | | | | |
| | **AOV cible** | | | | | |

Puis, sous le tableau, la vérification qui donne son sens à l'exercice : recalcule la marge brute et le **MER seuil** de ce panier cible, et compare-le à ton MER atteignable. Si le MER seuil reste au-dessus, ton AOV cible est encore trop bas — retourne empiler.

### 4.4 Le seuil de franco de port

**La méthode fausse**, qui circule partout : fixer le seuil au point mort du transport, `coût du port × (1 + TVA) ÷ marge brute avant port`. Elle donne un seuil ridiculement bas — souvent moins de 10 € — parce qu'elle traite le franco comme une opération à l'équilibre alors que c'est un **levier de comportement**. Un seuil sous ton panier naturel n'incite personne à rien : il offre le port à des gens qui l'auraient payé.

**La bonne méthode**, en quatre lignes, sur ta distribution réelle de paniers :

1. Découpe tes commandes en trois ou quatre tranches de montant, avec l'effectif et le panier moyen de chaque tranche.
2. Pour un seuil candidat, compte la **cannibalisation** : les commandes déjà au-dessus du seuil, à qui tu offres un port qu'elles payaient.
3. Estime la **remontée** : quelle part de chaque tranche monte jusqu'au seuil, et de combien. Une tranche proche du seuil remonte beaucoup ; une tranche très en dessous ne remonte pas.
4. Solde = marge sur le chiffre d'affaires remonté − port encaissé perdu. Teste **trois seuils**, pas un.

La règle qui sort de ce calcul, quelle que soit la catégorie : **le seuil doit se placer nettement au-dessus de ton panier naturel, autour de 1,3 à 1,45 fois.** En dessous de ton AOV, il détruit de la marge à coup sûr. Et retiens que le seuil qui maximise l'AOV n'est pas celui qui maximise la marge : **une hausse d'AOV achetée par du port offert n'est pas une hausse d'AOV.**

### 4.5 La politique de remise

Une remise se juge sur le volume qu'il faut pour la rembourser, jamais sur le chiffre d'affaires qu'elle produit.

```
Volume nécessaire = contribution unitaire avant remise ÷ contribution unitaire après remise
```

La contribution après remise se calcule ligne à ligne : ton COGS et ta logistique ne baissent pas de 20 % parce que ton prix baisse de 20 %. C'est pour ça qu'une remise de 20 % coûte bien plus de 20 % de marge — le § 8 le déroule.

Ta politique tient en cinq lignes chiffrées : le **budget annuel de remise** en pourcentage du CA HT (cible ≤ 5,5 %, valeur du palier P5+ des [canoniques § 8](../donnees/chiffres-canoniques.md)) ; le **taux maximum** d'une opération ; le **nombre de jours par an** où le héros peut être remisé ; qui a le **droit de signer** une exception ; et la **liste des jamais**. Cette dernière est la seule partie qui protège vraiment, parce qu'elle s'écrit avant le mois où le chiffre d'affaires est en retard.

---

## 5. Ton livrable

```
=====================================================================
LIVRABLE S04 — OFFRE, PRIX ET PANIER
Marque : ___________   Date : __/__/__

--- A. LE PRIX -----------------------------------------------------
Méthode 1, plancher : COGS ______ € × coef. min. ×______ = ______ € TTC
  AOV plancher = M ______ × L ______ € ÷ [M × (1 − v ______) − 1,20]
               = ______ € HT = ______ € TTC
Méthode 2, référence : ____ concurrents relevés le __/__ ;
  fourchette ______ à ______ € TTC ; médiane ______ € TTC
Méthode 3, valeur perçue : ____ réponses ; zone ______ à ______ € ;
  point d'indifférence ______ € ; dispersion forte / moyenne / faible
Situation retenue au § 4.1 : ______
PRIX HÉROS ARRÊTÉ ______ € TTC   Justification en une phrase : ________

--- B. LA GAMME ----------------------------------------------------
Une ligne par étage (entrée, héros, marge) : SKU | PVC TTC | COGS € |
coefficient | marge brute € | % du CA HT | MER seuil
Mon MER atteignable ______ (source ____________)
La SKU poussée en publicité est l'étage ____ parce que : ______________

--- C. TABLEAU DE CONSTRUCTION D'AOV -------------------------------
Base : prix unitaire catalogue ______ € TTC
| # | Levier | Mécanique | Adoption % | Effet unit. TTC | Pondéré | AOV cumulé |
|---|--------|-----------|-----------:|----------------:|--------:|-----------:|
| 1 | lot                  |  |  |  |  |  |
| 2 | montée en gamme      |  |  |  |  |  |
| 3 | vente croisée        |  |  |  |  |  |
| 4 | franco de port       |  |  |  |  |  |
| 5 | réappro programmé    |  |  |  |  |  |
| 6 | ajout après paiement |  |  |  |  |  |
AOV CIBLE ______ € TTC
Vérification : marge brute ______ % du CA HT → MER seuil ______
Mon MER atteignable ______  →  MARGE SUFFISANTE : OUI / NON

--- D. FRANCO DE PORT ----------------------------------------------
Coût du port supporté ______ € HT   Port facturé ______ € TTC
Distribution par tranche : <____ € : ____ % des cmd, AOV ______ € ; etc.
AOV naturel ______ € TTC
Trois seuils testés : seuil | cannibalisation | remontée | marge brute | écart
SEUIL RETENU ______ € TTC  =  ______ × mon AOV naturel

--- E. POLITIQUE DE REMISE -----------------------------------------
Budget annuel de remise ____ % du CA HT
Taux maximum d'une opération ____ %   Jours remisés par an ____
Volume nécessaire pour rembourser une remise de ____ % : + ____ %
Qui signe une exception ____________
CE QUE JE NE FERAI JAMAIS — au moins cinq lignes :
  1. ______________________________  4. ______________________________
  2. ______________________________  5. ______________________________
  3. ______________________________
=====================================================================
```

---

## 6. La grille d'évaluation

Barème sur 100, **seuil de validation 70**. En dessous, tu refais la séance : S06 écrira des publicités pour cette offre et S08 un plan de lancement à partir de cet AOV.

| # | Critère | Pts | Ce qui vaut les points | Ce qui les fait perdre |
|---|---|---:|---|---|
| 1 | Les trois méthodes de prix | 15 | Les trois menées, avec source et date | Méthode manquante : −5 ; relevé sans date : −3 |
| 2 | AOV plancher calculé | 10 | Formule appliquée avec **ton** L et **ton** v, en € TTC | Non calculé : −10 ; L en pourcentage au lieu d'euros par commande : −6 |
| 3 | Arbitrage explicite | 8 | La divergence est nommée et tranchée avec sa raison | « J'ai pris un prix intermédiaire » : −8 |
| 4 | Gamme à trois étages | 10 | Les trois existent, rôle écrit et part de volume visée | Deux étages : −5 ; rôles non écrits : −4 |
| 5 | MER seuil par étage | 12 | Calculé par SKU, logistique en euros par commande | Coefficient seul, sans MER seuil : **−12** |
| 6 | **Tableau d'AOV** | **20** | Six leviers examinés, adoption écrite d'avance, effets pondérés, AOV cumulé | Levier non examiné : −3 chacun ; adoption absente : **−10** |
| 7 | Vérification du MER seuil cible | 8 | Recalculé sur le panier cible et comparé au MER atteignable | Non fait : −8 |
| 8 | Franco de port | 10 | Trois seuils testés sur une distribution réelle, cannibalisation chiffrée | Un seul seuil : −5 ; méthode du point mort : **−10** |
| 9 | Politique de remise | 7 | Budget annuel, taux maximum, jours par an, signataire, ≥ 5 « jamais » | Moins de 5 « jamais » : −4 ; budget non chiffré : −3 |

**Quatre fautes éliminatoires** ramènent la note à 0 : **un AOV cible sans taux d'adoption écrits** — c'est un souhait, pas une construction ; **une logistique traitée en pourcentage du chiffre d'affaires** dans les calculs de panier, ce qui efface mécaniquement l'effet de l'AOV et rend toute la séance fausse ; **un seuil de franco placé sous l'AOV naturel** sans démonstration ; **une gamme dont la SKU poussée en publicité a un MER seuil supérieur au MER atteignable** — tu programmes une perte à chaque commande.

---

## 7. Le corrigé exemplaire

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.

On reprend **KALIS**, la marque du corrigé de [S03](S03-produit-et-cogs.md) — une autre marque fictive que la CLARÈNE de S01, choisie pour une catégorie où le panier unitaire est trop petit pour financer un client, ce qui rend la mécanique de cette séance visible : chaussettes de course techniques, COGS rendu entrepôt **2,77 € HT la paire**, prix cible provisoire 16,00 € TTC, coefficient ×5,78, marge de sécurité 1,25 — franchi de justesse.

Coûts par commande retenus, mesurés chez son prestataire logistique et son prestataire de paiement : **préparation et emballage 1,35 € HT**, **transport aval 3,60 € HT** (colis sous 500 g, point relais), **paiement 1,70 % du TTC + 0,25 €**, **taux de retour 3,0 %** avec 4,20 € HT de transport retour et 80 % de remise en stock.

### 7.1 Le prix, par les trois méthodes

**Méthode 1 — la marge nécessaire.** Au niveau unitaire, S03 a donné un coefficient minimum de ×4,63, soit un plancher de 2,77 × 4,63 = **12,83 € TTC** la paire. Au niveau du panier, avec M = 2,20 (MER canonique de P2), L = 4,95 € HT et v = 32,7 % (COGS 22,2 %, paiement 2,7 %, retours 2,8 %, remises 5,0 %) :

```
AOV plancher HT = 2,20 × 4,95 ÷ [ 2,20 × (1 − 0,327) − 1,20 ]
                = 10,89 ÷ [ 1,4806 − 1,20 ]
                = 10,89 ÷ 0,2806 = 38,81 € HT  =  46,57 € TTC
```

**46,57 € TTC de panier minimum.** Le prix cible provisoire était de 16,00 €. L'écart n'est pas un détail de positionnement : c'est un facteur 2,9, et il dit que **la paire seule ne peut pas être l'unité de vente de KALIS.**

**Méthode 2 — la référence.** Sept concurrents relevés le même jour sur trois points de vente chacun. Fourchette 8,90 à 24,00 € TTC la paire, médiane **14,50 €** ; les packs de trois existent chez quatre sur sept, de 32,00 à 48,00 €, médiane 39,00 €.

**Méthode 3 — la valeur perçue.** 46 réponses recrutées dans deux clubs de course. Doute de qualité sous **11,00 €**, trop cher au-dessus de **26,00 €**, point d'indifférence **17,50 €**, dispersion faible — la catégorie a un ancrage ferme.

**L'arbitrage.** Le plancher unitaire (12,83 €) est sous la référence (14,50 €) : à l'unité, tout va bien. Le plancher de **panier** (46,57 €) est très au-dessus de tout ce que la catégorie vend à l'unité — deuxième ligne du tableau du § 4.1 : **on ne monte pas le prix unitaire, on change l'unité de vente.**

Prix arrêtés : **paire seule 18,00 € TTC**, au-dessus de la médiane et sous le seuil de « trop cher », parce que la spécification de S03 le justifie ; **pack de 3 à 45,00 €** (15,00 € la paire, −16,7 %) ; **pack de 6 à 78,00 €** (13,00 € la paire, −27,8 %).

### 7.2 La gamme, et le piège du coefficient

| Étage | SKU | PVC TTC | CA HT | COGS | Logist. | Paiem. | Retours | Marge brute | % CA HT | **Coef.** | **MER seuil** |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Paire seule | 18,00 € | 15,00 € | 2,77 € | 4,95 € | 0,56 € | 0,51 € | 6,21 € | 41,4 % | **×6,50** | **2,90** |
| 2 | Pack de 3 | 45,00 € | 37,50 € | 8,31 € | 4,95 € | 1,02 € | 1,05 € | 22,17 € | 59,1 % | ×5,42 | **2,03** |
| 3 | Pack de 6 | 78,00 € | 65,00 € | 16,62 € | 5,40 € | 1,58 € | 1,69 € | 39,71 € | 61,1 % | ×4,69 | **1,96** |

*Prix catalogue TTC, hors remise ; tous les coûts et marges en € HT. Retours : 3,0 % de la valeur, plus le transport retour, moins le COGS remis en stock.*

**Lis les deux dernières colonnes ensemble.** Le coefficient tombe de ×6,50 à ×4,69 pendant que le MER seuil s'améliore de 2,90 à 1,96. La paire seule est la seule SKU qui passe le plancher ×5,0 du cursus, et c'est la seule qu'il est **interdit** de pousser en publicité : son MER seuil de 2,90 est très au-dessus du MER de 2,20 que KALIS peut espérer à son palier. Le pack de 6 échoue au plancher ×5,0 et produit 39,71 € de marge brute par commande contre 6,21 €.

L'explication est celle d'[E01](../modules/E01-arithmetique-de-la-marque.md) § 7.2 : **le colis coûte 4,95 € qu'il contienne une paire ou six.** Sur un panier de 15,00 € HT il pèse 33 % ; sur 65,00 € HT, 8,3 %.

Rôles arrêtés : **étage 1**, la paire seule, pour la recherche générique et l'ancrage — 15 % du volume visé, jamais de budget publicitaire dessus. **Étage 2**, le pack de 3, seule page d'atterrissage publicitaire — 62 % visés. **Étage 3**, le pack de 6, se choisit mais ne se pousse pas — 23 % visés.

### 7.3 Le tableau de construction d'AOV, rempli

Base : la paire seule à 18,00 € TTC. Taux d'adoption écrits avant la mise en ligne, à réviser après 300 commandes.

| # | Levier | Mécanique retenue | Adoption | Effet unitaire TTC | Pondéré | AOV cumulé |
|---|---|---|---:|---:|---:|---:|
| — | *Base* | prix unitaire catalogue | — | — | — | 18,00 € |
| 1 | Le lot | Mix visé 15 % paire / 62 % pack 3 / 23 % pack 6 | — | — | **+30,54 €** | 48,54 € |
| 2 | Montée en gamme | Version laine mérinos hiver, +4,00 € sur le pack | 18 % | +4,00 € | +0,72 € | 49,26 € |
| 3 | Vente croisée | Manchons de compression 24,00 €, proposés sur la fiche | 9 % | +24,00 € | +2,16 € | 51,42 € |
| 4 | Franco de port | Seuil 69,00 € ; 22 % des commandes sous le seuil remontent | 22 % | +12,50 € | +2,75 € | 54,17 € |
| 5 | Réappro. programmé | 2 livraisons par an, −10 % ; le client bascule du pack 3 au pack 6 | 7,4 % | +25,20 € | +1,88 € | 56,05 € |
| 6 | Ajout après paiement | Filet de lavage + spray anti-odeur, 9,00 € en un clic | 16 % | +9,00 € | +1,44 € | 57,49 € |
| | **AOV cible** | | | | | **57,48 € TTC** |

*Levier 1 : 0,15 × 18,00 + 0,62 × 45,00 + 0,23 × 78,00 = 48,54 €. Levier 5 : 12 % d'abonnés parmi les 62 % du pack de 3, soit 7,4 % des commandes, qui passent de 45,00 € à 78,00 × 0,90 = 70,20 €.*

**La vérification, qui est le vrai résultat de la séance.** Le panier cible contient en moyenne 3,61 paires et quelques accessoires :

```
CA HT                          57,48 ÷ 1,20                    = 47,90 €
COGS mixte                     3,61 paires + accessoires        = 11,30 €  → 23,6 %
Logistique par commande        colis un peu plus lourd          =  5,20 €  → 10,9 %
Paiement                       1,70 % × 57,48 + 0,25            =  1,23 €  →  2,6 %
Retours                        3,0 %, net de remise en stock    =  1,30 €  →  2,7 %
Marge brute                                                     = 28,87 €  → 60,3 %
MER seuil (CM3 = 0)            1,20 ÷ 0,603                     =  1,99
Avec 3,5 % de remises          marge brute 56,8 %               =  2,11
```

**Le MER seuil passe de 2,90 sur la paire seule à 2,11 sur le panier cible**, pour un MER atteignable de 2,20. KALIS est passée du mauvais côté au bon côté de sa ligne de flottaison sans changer un centime de son COGS et sans monter le prix à la paire. Marge brute de 60,3 % : c'est le niveau du palier P3 de NØRA ([canoniques § 2.1](../donnees/chiffres-canoniques.md)), atteint dès le lancement, parce que la structure de panier a été conçue et non subie.

### 7.4 Le seuil de franco de port

Distribution observée sur les 1 000 premières commandes, port facturé 4,90 € TTC à tout le monde, coût réel 3,60 € HT, marge brute avant port aval 67,8 % du CA HT.

| Tranche | Part des commandes | AOV de la tranche |
|---|---:|---:|
| Moins de 40 € | 34 % | 27,00 € |
| 40 à 59 € | 41 % | 48,00 € |
| 60 € et plus | 25 % | 84,00 € |

AOV naturel : 0,34 × 27 + 0,41 × 48 + 0,25 × 84 = **49,86 € TTC**. Marge brute de référence, port facturé partout : **28 654 €** par mois.

| Seuil testé | Commandes en franco | AOV après | Marge brute | Écart |
|---:|---:|---:|---:|---:|
| Aucun seuil | 0 | 49,86 € | 28 654 € | — |
| 49,00 € | 636 | 51,80 € | 27 157 € | **−1 497 €** |
| 59,00 € | 462 | 53,22 € | 28 668 € | +14 € |
| **69,00 €** | 318 | 52,69 € | **28 955 €** | **+301 €** |

Trois enseignements, tous contre-intuitifs. **Un.** Le seuil à 49,00 €, juste sous l'AOV naturel — exactement ce que fait la majorité des sites — **détruit 1 497 € de marge par mois**, 17 964 € par an : il offre le port à 47 % de commandes qui le payaient, pour faire remonter des paniers de quelques euros. **Deux.** Le seuil qui maximise l'AOV n'est pas celui qui maximise la marge : 59,00 € donne le meilleur panier (53,22 €) et 287 € de marge de moins que 69,00 €. Un tableau de bord qui suit l'AOV sans la marge brute te fera choisir le mauvais seuil, avec un indicateur en hausse. **Trois.** Le seuil retenu, 69,00 €, vaut **1,38 fois l'AOV naturel** et ne rapporte que 301 € par mois, 1,1 % de la marge brute. **Le franco de port est un levier de comportement modeste, pas une machine à marge** : il vaut d'être bien réglé, pas d'être espéré.

### 7.5 La politique de remise de KALIS

Budget annuel : **5,0 % du CA HT**, sous la cible P5+ de 5,5 % des [canoniques § 8](../donnees/chiffres-canoniques.md). Taux maximum d'une opération : **20 %**. Jours par an où le produit héros peut être remisé : **8**. Signature d'une exception : le fondateur, par écrit, avec le calcul de volume nécessaire joint.

Le calcul qui fixe le taux maximum, sur le pack de 3 :

```
Marge brute à 45,00 € TTC                                    = 22,17 €
Marge brute à 36,00 € TTC (−20 %)                            = 15,05 €
   — le COGS (8,31 €) et la logistique (4,95 €) n'ont pas bougé
Volume nécessaire pour rembourser = 22,17 ÷ 15,05 = 1,473    → +47,3 %
```

**Une remise de 20 % coûte 32,1 % de la marge et exige 47,3 % de volume en plus** — et ce calcul ignore encore la publicité nécessaire pour aller chercher ce volume.

Ce que KALIS ne fera jamais, écrit avant le premier mois en retard :

1. Aucun code de bienvenue affiché sur le site : il remise ceux qui allaient acheter au prix fort.
2. Aucune relance de panier abandonné avec remise dans les 24 h — on apprend au client à abandonner.
3. Aucun empilement : un code ne s'applique jamais sur un lot déjà remisé au volume.
4. Aucune remise à un client déjà remisé plus fort qu'une fois — on ne construit pas une base qui n'achète qu'en promotion.
5. Aucun prix barré permanent : un prix jamais pratiqué est un mensonge, et il détruit la crédibilité du prix réel.
6. Aucune remise sur le pack de 6 : le remiser supprime la raison d'être de l'étage de marge.

---

## 8. Les conséquences chiffrées de ton choix

### 8.1 Ce que coûte 10 % de prix, et ce que rapporte 10 %

Sur le palier P5 de NØRA, marge brute 61,45 %, dont **25,5 points de coûts fixes par unité** (COGS 14,5 %, logistique 11,0 %) et 13,05 points de coûts proportionnels au prix (paiement 1,55 %, retours 3,5 %, remises 8,0 %). Publicité à MER constant de 2,90, soit 41,38 % du CA HT.

| Variation de prix | Marge brute par unité | Volume nécessaire (vue CM2) | Volume nécessaire (vue CM3, publicité incluse) |
|---|---:|---:|---:|
| **−10 %** | 0,6145 → 0,5275 | **+16,5 %** | **+29,4 %** |
| **+10 %** | 0,6145 → 0,7015 | on peut perdre **12,4 %** | on peut perdre **18,5 %** |

La colonne de droite est la seule vraie, et presque personne ne la calcule : à MER constant, la publicité coûte un pourcentage du chiffre d'affaires, donc baisser le prix de 10 % réduit la facture publicitaire par commande mais exige **29,4 % de commandes en plus** pour retrouver le même euro de marge après publicité. **Une baisse de prix de 10 % est un pari sur une élasticité supérieure à 2,9** ; une hausse de 10 % est un pari sur une élasticité inférieure à 1,85, bien plus souvent gagné.

Chez KALIS, dont la marge après publicité est mince au lancement (1,72 € par commande de pack de 3 à MER 2,20), les mêmes 10 % exigent **×8,4 sur le volume** pour compenser une baisse et autorisent d'en perdre **47 %** en montant. Plus ta marge après publicité est fine, plus le prix est un levier violent dans les deux sens.

### 8.2 Deux trajectoires : un AOV de 46 € contre un AOV de 72 €

Même machine d'acquisition, même coût d'acquisition, même nombre de commandes ; seul l'AOV change. Structure du palier P5 des [canoniques](../donnees/chiffres-canoniques.md) : 60 200 commandes par mois, 1 494 206 € de publicité, 360 000 € de frais fixes. Avec `a` = panier en euros HT :

```
Coûts proportionnels au CA : COGS 14,5 % + paiement 1,55 % + retours 3,5 % + remises 8,0 % = 27,55 %
   → il reste 1 − 0,2755                                                                   = 0,7245
Logistique par commande    : 11,0 % × 59,98 €                                              =  6,60 €
Publicité par commande     : 1 494 206 ÷ 60 200                                            = 24,82 €
Frais fixes par commande   : 360 000 ÷ 60 200                                              =  5,98 €

EBITDA par commande = 0,7245 × a − (6,60 + 24,82 + 5,98)
                    = 0,7245 × a − 37,40
```

Contrôle sur le canonique : à a = 59,98 € HT (soit 71,98 € TTC), EBITDA par commande = 6,06 €, donc 364 751 € par mois — les canoniques § 2.2 affichent 364 752 €. La formule est juste.

| | Trajectoire A — AOV 46,00 € TTC | Trajectoire B — AOV 71,98 € TTC |
|---|---:|---:|
| Panier HT | 38,33 € | 59,98 € |
| Marge brute par commande | 21,17 € | 36,85 € |
| Marge brute en % du CA HT | 55,2 % | 61,5 % |
| Publicité par commande | 24,82 € | 24,82 € |
| Frais fixes par commande | 5,98 € | 5,98 € |
| **EBITDA par commande** | **−9,63 €** | **+6,06 €** |
| **EBITDA mensuel** | **−579 511 €** | **+364 751 €** |
| **EBITDA sur 12 mois** | **−6 954 134 €** | **+4 377 017 €** |

**Écart sur douze mois : 11 331 151 €.** Pour le même nombre de clients, le même coût d'acquisition, le même produit et la même publicité.

Trois lectures. **Un.** Le coefficient directeur est 0,7245 : **chaque euro hors taxes de panier supplémentaire dépose 72,45 centimes dans l'EBITDA**, parce que la logistique, la publicité et les frais fixes sont des coûts par commande qui ne bougent pas. C'est le nombre à retenir de la séance.

**Deux.** Inverse la formule et tu obtiens un seuil directement utilisable :

```
AOV de rentabilité = 37,40 ÷ 0,7245 × 1,20 = 61,94 € TTC
```

**Avec cette structure de coûts et ce coût d'acquisition, aucune quantité de commandes ne rend l'entreprise rentable sous 61,94 € de panier.** Ce n'est pas un objectif de croissance, c'est un seuil d'existence — et c'est exactement ce que ton tableau du § 4.3 sert à atteindre.

**Trois.** Le canonique § 7 dit que +10 % d'AOV vaut 3 139 401 € d'EBITDA annuel, soit 71,7 % de l'EBITDA total. Retrouve-le : 0,7245 × 5,998 € × 60 200 × 12 = 3 139 416 €, à quinze euros près sur 3,1 millions. Et le passage de P5 à P5+ ([canoniques § 8](../donnees/chiffres-canoniques.md)) — 71,98 € à 77,20 € de panier — est la même mécanique poussée de sept pour cent de plus.

> **À retenir :** ton panier moyen n'est pas une statistique que tu observes, c'est une structure que tu construis, une fois, dans un tableau à six lignes. Le mix de gamme fait 80 % du travail ; les cinq autres leviers font le reste. Et à structure de coûts fixée, chaque euro HT de panier vaut 72 centimes d'EBITDA.

---

## 9. Avant la séance suivante

1. **Mets tes trois SKU en ligne** avec leurs prix, même sans publicité, et laisse-les tourner deux semaines pour observer le mix réel contre le mix visé.
2. **Écris tes six taux d'adoption sur un papier daté**, puis programme la mesure : sans instrumentation, tu ne sauras jamais lequel des six leviers a produit ton AOV.
3. **Recalcule ton MER seuil sur ton mix réel** dès 100 commandes, et compare-le à celui du mix visé. L'écart est ton premier vrai diagnostic d'offre.
4. **Relis ton livrable S03** : si ton prix a bougé, ton coefficient a bougé, et la Porte 0 doit être revérifiée.

---

*Fin de la séance S04. Suite : [S05 — Recherche client et angles](S05-recherche-client-et-angles.md), où tu découvriras que l'offre que tu viens de construire ne se vend pas avec les mots que tu utiliserais spontanément pour la décrire.*
