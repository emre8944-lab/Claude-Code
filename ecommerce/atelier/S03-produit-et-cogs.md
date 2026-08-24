# Séance S03 — Le produit et le coût de revient réel

> **Niveau requis :** L02 · **Durée :** 6 h · **Livrable :** cahier des charges produit + COGS rendu entrepôt au centime + verdict de coefficient · **Modules :** [E01](../modules/E01-arithmetique-de-la-marque.md), [E02](../modules/E02-marche-et-produit.md), [E10](../modules/E10-cash-et-operations.md)
> **Ce que tu ne peux pas faire sans avoir fait cette séance :** fixer un prix. Un prix décidé sans coût de revient complet n'est pas un prix, c'est un vœu — et [S04](S04-offre-prix-et-panier.md) prend ton COGS en entrée, ligne par ligne.

---

## 1. Où tu en es

Tu sors de [S01](S01-choisir-le-terrain.md) avec une catégorie choisie et défendue, et de [S02](S02-prouver-la-demande.md) avec six tests de demande dont quatre favorables au moins, seuils écrits d'avance — et un corpus de plusieurs centaines d'avis concurrents, dont la partie qui compte : les avis à une et deux étoiles, triés par motif.

Décidé : la catégorie, le segment, la fourchette de prix visée, la promesse. Pas décidé : **ce que le produit est physiquement**, ce qu'il coûte rendu entrepôt, et si ce couple prix-coût autorise une marque qui achète son trafic.

La porte à franchir — [jalons](../mentorat/jalons.md), Porte 0 → P1, condition 1 : **coefficient du produit héros, au coût complet rendu entrepôt, ≥ ×5,0.** Pas au prix sortie usine. Pas « environ ». Au centime.

---

## 2. Ta mission

Produire trois documents, dans cet ordre, en une séance :

1. **Un cahier des charges** rédigé contre les défauts recensés dans les avis négatifs concurrents, chaque exigence mesurable sur un échantillon.
2. **Un tableau de COGS rendu entrepôt** à onze lignes, au centime, à partir d'au moins deux devis fournisseurs réels obtenus pendant la séance.
3. **Un verdict de coefficient**, comparé au plancher ×5,0 et au coefficient minimum dérivé de ton MER, avec — si tu es dessous — les quatre leviers chiffrés et celui que tu actionnes.

Tu envoies de vraies demandes de devis pendant la séance. Si rien ne revient dans la journée, chiffre avec des hypothèses **déclarées comme telles** et remplace-les avant S04.

---

## 3. Ce dont tu disposes

| Ressource | Usage |
|---|---|
| [canoniques § 1 et § 2.1](../donnees/chiffres-canoniques.md) | La gamme de NØRA, ×6,4 à ×8,1 : ton étalon. Le COGS pèse 20,0 % du CA HT à P1, 14,5 % à P5 |
| [C01](../etudes-de-cas/C01-coefficient-insuffisant.md) § 8 | Le coefficient minimum, et pourquoi le minimum n'est pas la cible |
| [jalons](../mentorat/jalons.md), Porte 0 | Le seuil ×5,0 et sa justification |
| `python3 ecommerce/outils/calculateur.py` | Ta cascade de marge, ton MER seuil, ton verdict |

**Ce que tu apportes :** ton corpus d'avis de S02, une adresse de courriel à ton propre nom de domaine — le taux de réponse fournisseur n'est pas le même — et 300 à 600 € TTC pour les échantillons.

**Convention :** coûts de revient **HT**, prix **TTC**, `coefficient = PVC TTC ÷ COGS HT`. Ratio hybride assumé : c'est celui du métier, et il intègre la TVA que tu ne factures pas mais que ton client paie.

---

## 4. La méthode, pas à pas

### 4.1 Écrire le cahier des charges contre les défauts

Un produit conçu à partir de ce que tu aimes vise un marché d'une personne. Un produit conçu à partir des avis à une étoile de tes concurrents est conçu contre un défaut que des milliers de gens ont payé pour connaître.

1. **Trie les avis 1 et 2 étoiles par motif**, pas par produit. 200 avis minimum, 4 concurrents minimum. Un motif est une phrase de client, pas ta reformulation.
2. **Compte.** Sous 5 % des avis négatifs : du bruit. De 5 à 15 % : un irritant. Au-dessus de 15 % : un défaut structurel de la catégorie — c'est là que tu te différencies.
3. **Traduis chaque motif au-dessus de 5 % en exigence mesurable.** « Ça s'abîme vite » n'est pas une exigence ; « aucun trou après 40 lavages à 40 °C et 200 km, sur 3 exemplaires sur 3 » en est une.
4. **Chiffre le surcoût de chaque exigence**, en demandant au fournisseur la version avec et sans. Une exigence dont tu ignores le prix n'est pas une décision, c'est une préférence.
5. **Classe en trois blocs :** *bloquantes*, *différenciantes*, *renonçables*.

Le troisième bloc est celui que personne n'écrit, et c'est le plus important : décider **avant** de connaître ton coefficient ce que tu sacrifieras t'évite de sacrifier, sous pression, le seul attribut qui te différenciait.

> **À retenir :** une exigence sans son surcoût unitaire n'est pas une spécification, c'est une opinion.

### 4.2 Chercher et qualifier des fournisseurs

**Où chercher**, par qualité décroissante : les salons professionnels de la catégorie ; les annuaires sectoriels et syndicats, où se trouvent les fabricants européens absents du web ; les places de marché B2B, beaucoup de vendeurs et peu de fabricants ; la rétro-ingénierie des concurrents par leurs étiquettes — long, et la source la plus fiable.

**Le piège de l'intermédiaire.** Sur une place de marché B2B, la majorité de ce qui se présente comme fabricant est un négociant : il achète à l'usine et te revend avec **15 à 35 %** de marge, sur ton coût le plus lourd. Le prix n'est pas le pire : il répond commercialement en dix minutes et techniquement en trois jours ; il ne peut t'engager sur aucun niveau de qualité contractuel, faute de contrôler la production ; et il catalogue des familles de produits sans rapport entre elles, quand un fabricant fait une chose. Deux demandes le démasquent : **la facture sortie usine** et le **numéro d'enregistrement de l'établissement de production**.

**Les huit questions qui filtrent en dix minutes.** Un seul message, numérotées. Six réponses sur huit en moins de 48 h valent un échantillon ; « yes, no problem, send your design » à tout n'en vaut aucun.

1. Êtes-vous le fabricant ? Adresse de l'usine, effectif, machines utilisées.
2. Quelle position tarifaire douanière déclarez-vous, et sur quelle base ?
3. Votre MOQ **par coloris et par taille**, pas seulement au global ?
4. Quel niveau de qualité acceptable contractuel, et qui paie la ré-inspection ?
5. Délai de production après contre-échantillon validé, et délai de transit porte à porte ?
6. Paiement : quel acompte, quel solde, contre quel document ?
7. Lot refusé au contrôle : retouche, remplacement ou avoir ?
8. Quels certificats, et un rapport d'essai de moins de douze mois ?

La 3 élimine le plus de dossiers : un MOQ « 500 pièces » qui devient « 500 par coloris et par taille » fait 5 000 pièces au premier lot sur cinq tailles et deux coloris — un autre projet de trésorerie. La 6 vaut plus que la négociation du prix : passer de « 100 % avant expédition » à « 30 % à la commande, 70 % contre document de transport » ne change pas ton COGS d'un centime et change ton besoin en fonds de roulement de plusieurs semaines de CA ([canoniques § 4](../donnees/chiffres-canoniques.md)).

### 4.3 L'échantillonnage et le test à l'aveugle

**Combien.** 25 fournisseurs contactés → 10 à 14 réponses → 5 ou 6 passent les huit questions → **4 échantillons** → 2 pré-séries → 1 retenu. Sous quatre échantillons tu ne compares rien, tu confirmes le premier. Coût, fret express compris : 300 à 600 € TTC, la dépense la mieux rentabilisée de ton lancement.

**Le protocole s'écrit avant la réception des colis**, sinon il s'écrit autour de ce que tu préfères. Marquages retirés, remballage en A, B, C, D, un tiers garde la clé. Grille écrite avant : une ligne par exigence bloquante et différenciante, notée de 0 à 5, chaque note définie. Trois évaluateurs, dont deux clients de la catégorie qui ne sont pas toi ; notation individuelle sans discussion, puis mise en commun. Fais subir au produit ce que le client lui fera, en accéléré, sur une durée fixée d'avance — le test qui compte n'est jamais celui du déballage. Photographie tout, avant et après : ce dossier sert à décider, puis à écrire la publicité en S06. Lève la clé en dernier, et le prix après : le connaître avant de noter suffit à faire glisser une note de 3 à 4.

### 4.4 Le chiffrage complet du COGS rendu entrepôt

Le COGS est le coût complet d'une unité **disponible à la vente dans ton entrepôt**. Onze lignes, aucune ne se saute. **Tableau vierge à copier :**

| # | Ligne | Base de calcul | Lot € HT | Unité € HT |
|---|---|---|---:|---:|
| 1 | Produit sortie usine (EXW) | prix négocié hors tout × quantité | | |
| 2 | Conditionnement primaire | ce qui touche le produit et part avec lui | | |
| 3 | Conditionnement secondaire | regroupement, calage, palettisation | | |
| 4 | Notice et étiquetage | étiquette, notice, code-barres, mentions légales | | |
| 5 | Contrôle qualité | inspection tierce, forfait ÷ taille du lot | | |
| 6 | Fret | principal + frais portuaires + dossier | | |
| 7 | Assurance | ad valorem, avec minimum de perception | | |
| | **Valeur en douane (CIF)** | 1+2+3+4+6+7 | | |
| 8 | Droits de douane + frais de dédouanement | taux × CIF ; forfait ÷ quantité | | |
| 10 | Transport jusqu'à l'entrepôt | post-acheminement, déchargement, mise en stock | | |
| | **Sous-total** | 1 à 10 | | |
| 11 | Perte et casse | % × sous-total | | |
| | **COGS rendu entrepôt** | | | |
| 9 | *Taxes à l'importation* | *TVA, 20 % × (CIF + droits)* | | |

*La ligne 9 est placée après le total, parce qu'elle n'entre pas dans le COGS. Voir le premier piège ci-dessous.*

**Trois pièges, et ils coûtent cher.**

**La ligne 9 n'est pas un coût.** La TVA à l'importation est déductible et le plus souvent autoliquidée : l'inclure dans ton COGS gonfle ton coût de revient et t'amène à surfixer ton prix. Elle sort en revanche de ta trésorerie au dédouanement si tu n'es pas en autoliquidation — ligne séparée, marquée « trésorerie, non COGS ».

**La ligne 8 se calcule sur la valeur en douane**, qui comprend le produit, les emballages, le fret et l'assurance jusqu'à la frontière de l'Union — pas, en général, une inspection facturée par un tiers. Quelques points d'erreur de position tarifaire pèsent plus lourd que toute la négociation dont tu es capable : fais confirmer ta position par écrit.

**La ligne 11 n'est pas une coquetterie** : rebut, casse, écart d'inventaire, produits offerts aux créateurs de contenu, retours non remis en stock. Premier lot chez un fournisseur nouveau, 3 à 4 % ; inspection à la source et fournisseur rodé, 1,5 à 2,5 %.

### 4.5 La vérification : la porte du coefficient

```
Coefficient = PVC TTC ÷ COGS rendu entrepôt HT

Coefficient minimum = (1 + TVA)
                    ÷ [ (1 − remise moyenne)
                        × (1 − (1 + TVA)/MER_atteignable − autres coûts variables en % du CA HT) ]

« autres coûts variables » = logistique + paiement + retours, hors COGS.  Formule : C01 § 8.
```

Compare ton coefficient au plancher **×5,0** de la Porte 0, puis à ton coefficient minimum. Le rapport `réel ÷ minimum` est ta **marge de sécurité** ; NØRA la tient à 2,09 sur son Rituel. Sous 1,5, aucune tolérance : la première hausse de taux de retour ou la première dégradation de MER en ouvrant un second pays te fait passer sous ta ligne de flottaison.

**Si tu es sous ×5,0 : quatre leviers, et rien d'autre.**

| Levier | Ordre de grandeur réaliste | Ce qu'il coûte |
|---|---|---|
| **1. Le prix de vente** | +10 % de prix = +10 % de coefficient | Le marché a un droit de veto — c'est [S04](S04-offre-prix-et-panier.md) |
| **2. Le prix sortie usine** | −15 à −30 % en supprimant un négociant ; −5 à −12 % par palier de volume | Du temps, parfois du MOQ |
| **3. Les coûts de lot** | Contrôle, fret, dédouanement, post-acheminement sont fixes par lot : doubler la quantité les divise par deux | Du cash immobilisé — § 4.6 |
| **4. L'origine et la position tarifaire** | 0 à 12 points de droits ; fret et délai divisés en zone proche | Un prix sortie usine plus élevé |

Le levier 4 est celui qu'on oublie : un sourcing dans l'Union supprime les droits et le dédouanement, divise le fret et raccourcit le délai de plusieurs semaines — donc réduit ton stock de couverture, donc ton besoin en fonds de roulement. **L'arbitrage ne se tranche pas sur le coefficient seul, mais sur le coefficient et sur le cash.**

### 4.6 MOQ : le prix unitaire contre le cash immobilisé

Ton fournisseur proposera un palier : « deux fois la quantité, moins 8 % ». L'offre paraît toujours bonne et l'est rarement au démarrage. Cinq lignes suffisent à trancher, déroulées en entier au § 7.5 : le **vrai gain** et non la remise annoncée, puisque doubler le lot divise aussi les coûts fixes de lot ; un **horizon de consommation identique**, pas un lot contre un lot ; le **cash moyen immobilisé**, environ la moitié du lot au COGS ; le **prix de ce cash** — le taux de ton financement si tu n'es pas contraint, le rendement de l'euro publicitaire que tu ne dépenses pas si tu l'es, ce qui est le cas de toute marque en P1 ou P2 ; et la **perte espérée sur invendu**, plus le coût du blocage : avec deux fois plus de stock, un défaut découvert au deuxième mois ne se corrige plus avant le huitième.

---

## 5. Ton livrable

Copie ce formulaire et remplis-le entièrement. Toute case vide vaut zéro à la grille du § 6.

```
=====================================================================
LIVRABLE S03 — SPÉCIFICATION PRODUIT ET COÛT DE REVIENT
Marque : ___________  Produit héros : ___________  Date : __/__/__

--- A. CAHIER DES CHARGES CONTRE LES DÉFAUTS ------------------------
Corpus : ____ avis négatifs, ____ concurrents, du __/__ au __/__
Une ligne par motif au-dessus de 5 % : motif (verbatim) | fréq. % |
exigence mesurable | surcoût €/u HT | bloc B, D ou R
Total des surcoûts B + D : ______ € HT / unité
Ce que je coupe si le coefficient ne passe pas : ___________________

--- B. FOURNISSEURS -------------------------------------------------
Contactés ____ Réponses ____ Passent les 8 questions ____
Échantillons ____ Coût ______ € TTC
Une ligne par fournisseur retenu : nom | pays | fabricant ou négociant |
MOQ /coloris /taille | paiement | délai porte à porte | EXW € HT
Test à l'aveugle le __/__ , ____ évaluateurs. Grille écrite avant : oui / non
Gagnant ______ note ___/___    Deuxième ______ note ___/___

--- C. COGS RENDU ENTREPÔT -----------------------------------------
Lot : ______ unités        Fournisseur retenu : ___________
Recopie ici le tableau à onze lignes du § 4.4, rempli au centime. Report :
  valeur en douane (CIF) ______ €   droits ______ €   sous-total ______ €
  perte et casse ____ % = ______ €   COGS RENDU ENTREPÔT ______ € HT / unité
  TVA import (trésorerie, non COGS) ______ € sur le lot
Position tarifaire : ________  Confirmée par écrit par : ___________

--- D. VERDICT ------------------------------------------------------
Prix cible provisoire (S04 le fixera) ______ € TTC
Coefficient = ______ ÷ ______ = ×______
MER atteignable ______ (source ________)  Remise attendue ____ %
Autres coûts variables hors COGS ____ % du CA HT
Coefficient minimum ×______  Marge de sécurité ______ ÷ ______ = ______
PORTE 0 CONDITION 1 (coefficient ≥ ×5,0) :  FRANCHIE / NON FRANCHIE
Si non franchie, pour chacun des quatre leviers : de ______ à ______,
coefficient obtenu ×______.  Levier actionné et décision : ___________

--- E. ARBITRAGE MOQ ------------------------------------------------
Option A ______ u. à ______ €/u.  Option B ______ u. à ______ €/u.
Horizon ____ mois, ______ unités vendues
Économie marchandise de B                               + ______ €
Cash moyen supplémentaire immobilisé par B                ______ €
Prix de ce cash (financier ____ % / opportunité pub)    − ______ €
Perte espérée sur invendu (____ % × ____ %)             − ______ €
SOLDE ______ €   Option retenue ____   Parce que : _________________
=====================================================================
```

---

## 6. La grille d'évaluation

Barème sur 100, **seuil de validation 70**. En dessous, tu refais la séance : sans COGS solide, S04 produit un prix faux et S08 un plan de lancement faux.

| # | Critère | Pts | Ce qui vaut les points | Ce qui les fait perdre |
|---|---|---:|---|---|
| 1 | Corpus d'avis | 10 | ≥ 200 avis, ≥ 4 concurrents, verbatim, fréquences | < 100 avis : −6 ; reformulé : −4 ; sans fréquence : −5 |
| 2 | Exigences mesurables | 12 | Quoi mesurer, comment, sur combien, à quel seuil | Exigence qualitative (« bonne qualité ») : −3 chacune |
| 3 | Surcoûts chiffrés | 8 | Chaque exigence B et D porte un surcoût du fournisseur | Estimés sans devis : −4 ; absents : −8 |
| 4 | Blocs B / D / R | 6 | Les trois remplis, dont ≥ 2 renonçables | Aucun bloc R : −6, l'arbitrage n'est pas préparé |
| 5 | Sourcing | 10 | ≥ 15 contactés, 8 questions envoyées, statut tranché | < 5 contactés : −6 ; statut non tranché : −4 |
| 6 | Échantillonnage | 10 | ≥ 3 échantillons, grille écrite avant, ≥ 3 évaluateurs, test accéléré | Un seul échantillon : −7 ; grille après : −5 ; prix connu avant : −4 |
| 7 | **COGS complet** | **22** | Les 11 lignes au centime, avec leur base de calcul | Ligne manquante ou à zéro sans justification : **−4** chacune |
| 8 | TVA d'importation | 6 | Sortie du COGS, portée en trésorerie, calculée | Incluse dans le COGS : **−6** |
| 9 | Verdict de coefficient | 10 | Comparé à ×5,0 **et** au coefficient minimum | Calculé sur le prix EXW : **−10** |
| 10 | Arbitrage MOQ | 6 | Horizon égal, cash valorisé, invendu chiffré | Lot contre lot : −4 ; cash non valorisé : −3 |

**Quatre fautes éliminatoires** ramènent la note à 0, parce que chacune produit une décision fausse avec l'air d'être juste : **un coefficient calculé sur le prix sortie usine** — l'erreur qui a tué ATLAS dans [C01](../etudes-de-cas/C01-coefficient-insuffisant.md) ; **une ligne de COGS à zéro sans justification écrite**, alors que le fret et le contrôle ne sont jamais gratuits ; **la TVA à l'importation comptée en coût de revient** ; **aucun devis réel**, car un COGS hypothétique n'est pas un COGS.

---

## 7. Le corrigé exemplaire

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle. Les taux de droits de douane retenus sont ceux du modèle et doivent être vérifiés pour ta position tarifaire réelle.

*Le corrigé de [S01](S01-choisir-le-terrain.md) suivait CLARÈNE. Celui-ci suit une autre marque fictive, dans une catégorie volontairement différente : un produit importé hors Union est le seul qui fasse apparaître les onze lignes du COGS, dont les droits de douane et la TVA d'importation, qu'un façonnage européen laisserait à zéro. Reprends la méthode, pas la catégorie.*

**KALIS** — chaussettes de course techniques, vendues en direct en France puis en Europe. Catégorie retenue en S01 pour trois raisons : durée d'usage de 5 à 7 mois, donc réachat (condition 4 de la Porte 0) ; poids emballé sous 100 g, donc transport aval bas — la leçon de [C01](../etudes-de-cas/C01-coefficient-insuffisant.md) § 2.4 ; et des avis négatifs massifs et convergents.

### 7.1 Le cahier des charges

Corpus : **412 avis** à 1 et 2 étoiles, **6 concurrents**, collectés en S02 sur trois places de marché et deux sites de marque.

| Motif (verbatim) | Fréq. | Exigence mesurable | Surcoût €/u HT | Bloc |
|---|---:|---|---:|---|
| « Trouées au talon en deux mois » | 31,3 % | Aucune perforation après 40 lavages à 40 °C + 200 km, sur 3/3. Talon et pointe en polyamide 6.6 renforcé, ≥ 30 % de la zone | 0,22 | B |
| « L'élastique lâche, elles tombent » | 22,1 % | Perte de rétraction ≤ 8 % après 40 lavages, sur banc. Maintien de voûte tricoté, pas cousu | 0,11 | B |
| « Ampoules dès la première sortie longue » | 17,5 % | Zéro couture en relief sous l'avant-pied ; orteil remaillé à plat | 0,14 | D |
| « Ça pue au bout d'une heure » | 12,9 % | Réduction d'odeur mesurée après 6 h d'effort contre témoin | 0,09 | D |
| « La taille ne correspond à rien » | 9,7 % | Trois tailles, longueur de pied publiée en cm | 0,00 | B |
| « Trop fines, aucun amorti » | 6,1 % | Bouclettes zonées, 3 densités, épaisseur en mm sous le talon | 0,18 | D |
| « Le coloris a déteint » | 4,3 % | sous le seuil de 5 %, écarté | — | — |

Total des surcoûts B + D : **0,74 € HT par paire**, soit 43 % du prix sortie usine que KALIS va négocier. **Le produit différencié coûte plus cher ; la question n'est pas de l'éviter, mais de savoir si le prix peut le porter.** Renonçables écrits d'avance : l'odeur (0,09 €) et la troisième densité (0,18 €).

### 7.2 Le sourcing

**23 fournisseurs contactés** en trois heures : 11 sur une place de marché B2B, 7 via l'annuaire d'un syndicat textile européen, 5 identifiés par les étiquettes de concurrents. **12 réponses** en 48 h, **5 passent les huit questions.** Le tri s'est fait sur la question 1 : sept des onze contacts de la place de marché n'ont pas su décrire la machine utilisée, et quatre proposaient au catalogue chaussettes, sacs à dos et bouteilles isothermes. **Négociants** — et le devis le plus alléchant venait de l'un d'eux.

| Devis | Origine et statut | MOQ | Paiement | Délai | EXW € HT |
|---|---|---|---|---|---:|
| A | Asie non précisée, **négociant** | 1 000 global | 100 % avant expédition | 9 sem. | 2,35 |
| B | Vietnam, **fabricant** | 1 000 / coloris / taille, soit 3 000 | 30 % / 70 % contre document de transport | 11 sem. | 1,72 |
| C | Portugal, **fabricant** | 600 / coloris / taille, soit 1 800 | 30 % / 70 % à 30 j. | 4 sem. | 2,55 |

Test à l'aveugle sur 4 échantillons, 3 évaluateurs dont deux coureurs, grille de 6 lignes écrite avant réception, 40 lavages et 210 km cumulés. Gagnant **B**, 25/30 ; deuxième **C**, 23/30. L'échantillon du négociant A a perdu sur le talon : il venait, comme il l'a admis ensuite, d'une autre usine que celle promise.

### 7.3 Le COGS, devis A contre devis B

Prix de vente cible provisoire, arrêté en S01 sur l'analyse concurrentielle : **16,00 € TTC la paire.**

| # | Ligne | A — lot 1 000, €/paire HT | B — lot 3 000, €/paire HT |
|---|---|---:|---:|
| 1 | Produit sortie usine | 2,35 | 1,72 |
| 2 | Conditionnement primaire | 0,22 | 0,14 |
| 3 | Conditionnement secondaire | 0,05 | 0,03 |
| 4 | Notice et étiquetage | 0,12 | 0,09 |
| 5 | Contrôle qualité (320 € ÷ lot) | 0,32 | 0,11 |
| 6 | Fret (LCL, minimum 2 m³ : 540 € ÷ lot) | 0,54 | 0,18 |
| 7 | Assurance (0,35 %, min. 45 € ÷ lot) | 0,05 | 0,02 |
| | **Valeur en douane (CIF)** = 1+2+3+4+6+7 | **3,33** | **2,18** |
| 8 | Droits de douane, 12,0 % du CIF | 0,40 | 0,26 |
| | Dédouanement (95 € ÷ lot) | 0,10 | 0,03 |
| 10 | Transport jusqu'à l'entrepôt (380 € ÷ lot) | 0,38 | 0,13 |
| | **Sous-total** | **4,53** | **2,71** |
| 11 | Perte et casse — 3,5 % sans inspection, 2,2 % avec | 0,16 | 0,06 |
| | **COGS rendu entrepôt** | **4,69** | **2,77** |
| — | *TVA à l'importation, 20 % × (CIF + droits)* | *0,75* | *0,49* |
| | **Coefficient à 16,00 € TTC** | **×3,41** | **×5,78** |

Devis A : **Porte 0 condition 1 non franchie**, il manque un facteur 1,47. Devis B : **franchie.** Le pont entre les deux, levier par levier :

| Levier | Ce qui bouge | Gain €/paire |
|---|---|---:|
| 2. Prix sortie usine | Suppression du négociant : 2,35 → 1,72 € (−26,8 %) | −0,63 |
| 3. Coûts de lot | 1 000 → 3 000 : contrôle, fret, assurance, dédouanement, post-acheminement | −0,92 |
| — | Conditionnement dessiné au lieu du standard fournisseur | −0,13 |
| 4. Droits de douane | 12,0 % appliqués à une valeur en douane plus basse | −0,14 |
| — | Perte ramenée de 3,5 % à 2,2 % par l'inspection à la source | −0,10 |
| | **Total** | **−1,92** |

**Le levier le plus puissant n'est pas la négociation du prix : c'est l'amortissement des coûts de lot, à −0,92 €.** Le prix sortie usine, la ligne sur laquelle tout le monde passe ses appels, arrive deuxième. La TVA à l'importation ne figure dans aucun de ces coûts : 1 470 € sortis de la trésorerie le jour du dédouanement, récupérés plus tard.

### 7.4 Le verdict complet, et la vérité désagréable

Le coefficient passe la porte, et ne suffit pas pour autant. Formule de C01 § 8 — MER atteignable 2,20 (valeur canonique de P2), remise moyenne 5,0 %, autres coûts variables hors COGS 18,2 % du CA HT (logistique 14,0 %, paiement 1,7 %, retours 2,5 %) :

```
1,20 ÷ 2,20                          = 0,5455
1 − 0,5455 − 0,182                   = 0,2725
0,2725 × (1 − 0,05)                  = 0,2589
Coefficient minimum = 1,20 ÷ 0,2589  = ×4,63
Marge de sécurité   = 5,78 ÷ 4,63    = 1,25
```

| Marque | Coefficient minimum | Coefficient réel | Marge de sécurité |
|---|---:|---:|---:|
| NØRA Rituel Complet (P5) | ×3,06 | ×6,4 | 2,09 |
| ATLAS Studio, après redressement | ×3,42 | ×6,63 | 1,94 |
| **KALIS, paire seule à 16,00 € TTC** | **×4,63** | **×5,78** | **1,25** |

**1,25, c'est mince.** Si le taux de retour double, ou si le MER tombe de 2,20 à 1,90 en ouvrant un second pays, KALIS repasse sous sa ligne de flottaison. Et son coefficient minimum est élevé — ×4,63 contre ×3,06 pour NØRA — pour une raison unique : **la logistique pèse 14,0 % du CA HT sur un panier de 16 € TTC**, contre 11 à 12 % chez NØRA sur un panier de 65 à 72 €. Le colis coûte le même prix ; le panier est quatre fois plus petit.

Décision inscrite au livrable : **on ne répare pas ça sur le COGS, on le répare sur le panier** — l'objet de [S04](S04-offre-prix-et-panier.md), et la raison pour laquelle KALIS vendra des lots et non des paires.

**Levier 4, chiffré et écarté pour le premier lot.** Le devis C portugais coûte 2,55 € sortie usine mais ne paie ni droits de douane ni dédouanement et voyage pour 0,09 € : COGS **3,06 €**, coefficient **×5,23**. Il perd 0,55 point de coefficient face au Vietnam et gagne sept semaines de délai, donc deux mois de couverture de stock — à 1 000 paires par mois, environ 6 000 € de trésorerie immobilisée en moins. **Décision : Vietnam pour le premier lot, pré-série de 300 paires en parallèle au Portugal**, parce que le jour où KALIS ouvrira un second marché et devra réapprovisionner vite, un fournisseur européen déjà qualifié vaudra plus que 0,29 € de COGS.

### 7.5 L'arbitrage MOQ, en entier

Le fabricant propose **6 000 paires au lieu de 3 000, à 1,58 € au lieu de 1,72 €, soit −8,1 %.** Recalcul complet :

| Ligne, en € HT par paire | Lot 3 000 | Lot 6 000 |
|---|---:|---:|
| Produit sortie usine | 1,72 | 1,58 |
| Conditionnements, notice, étiquetage | 0,26 | 0,26 |
| Contrôle, fret, assurance, dédouanement, transport entrepôt | 0,73 | 0,46 |
| Perte et casse | 0,06 | 0,05 |
| **COGS** | **2,77 €** | **2,35 €** |
| **Coefficient à 16,00 € TTC** | ×5,78 | **×6,81** |

**Une remise annoncée de 8,1 % produit un COGS inférieur de 15,2 %** : le gain d'un palier de MOQ dépasse toujours la remise, parce qu'il amortit aussi les coûts de lot. Un fournisseur qui t'offre 8 % t'en offre 15.

Maintenant le vrai calcul. KALIS vend **1 000 paires par mois** au lancement ; horizon **six mois, 6 000 paires** dans les deux scénarios.

```
A — deux lots de 3 000 : marchandise 16 620 € HT, décaissée 8 310 € en M0 et en M3,
    TVA d'import 1 470 € à chaque fois, stock moyen 1 500 × 2,77 € = 4 155 €
B — un lot de 6 000    : marchandise 14 100 € HT, décaissée en M0,
    TVA d'import 2 604 € en M0, stock moyen 3 000 × 2,35 € = 7 050 €

Économie marchandise de B sur six mois          = 16 620 − 14 100  = + 2 520 €
Cash moyen supplémentaire immobilisé par B      =  7 050 −  4 155  =   2 895 €

Cas 1 — marque NON contrainte en trésorerie
   coût financier : 2 895 € × 9,0 % l'an × 0,5 an                  = −   130 €
   invendu : 6 000 × 25 % de probabilité × 20 % du lot × 2,35 €    = −   705 €
   SOLDE                                                           = + 1 685 €

Cas 2 — marque CONTRAINTE, avec de l'acquisition rentable disponible
   2 895 € ÷ 26,62 € de nCAC (canoniques § 2.4, P1)  = 108 clients
   contribution nette à 12 mois : 108 × (55,97 − 26,62)            = − 3 170 €
   invendu et coût financier                                       = −   835 €
   SOLDE                                                           = − 1 485 €
```

**Le même palier rapporte 1 685 € à une marque qui a du cash et coûte 1 485 € à une marque qui n'en a pas.** L'écart de 3 170 € n'est pas un coût de stockage : c'est la valeur des 108 clients que KALIS n'a pas achetés parce que son argent dormait en chaussettes.

Reste le risque non chiffré, qui a tranché : KALIS lance une spécification jamais produite en série. Avec 3 000 paires, un défaut découvert au deuxième mois se corrige au troisième lot ; avec 6 000, au huitième, sur 4 000 paires défectueuses déjà payées. **Décision : lot de 3 000, palier à 6 000 au troisième réapprovisionnement.**

---

## 8. Les conséquences chiffrées de ton choix

Prends la décision qui se joue ici — **négocier ou non ton COGS de 15 %** — sur vingt-quatre mois. Deux marques identiques suivent le sentier canonique de NØRA : P1 trois mois, P2 six, P3 neuf, P4 six. La première obtient les taux de COGS des [canoniques § 2.1](../donnees/chiffres-canoniques.md) ; la seconde paie **15 % de plus** — un négociant non éliminé, un MOQ trop petit, une position tarifaire mal déclarée, ou personne qui n'a demandé un second devis.

| Palier | Mois | CA HT / mois | COGS % → €/mois | Surcoût 15 %/mois | Cumul | EBITDA cumulé |
|---|---|---:|---:|---:|---:|---:|
| P1 | 3 | 30 667 € | 20,0 % → 6 133 € | 920 € | 2 760 € | −28 209 € |
| P2 | 6 | 191 833 € | 18,0 % → 34 530 € | 5 179 € | 31 077 € | −119 028 € |
| P3 | 9 | 981 000 € | 16,0 % → 156 960 € | 23 544 € | 211 896 € | +459 297 € |
| P4 | 6 | 2 443 000 € | 15,0 % → 366 450 € | 54 968 € | 329 805 € | +1 191 432 € |
| | **24** | | | | **575 538 €** | **+1 503 492 €** |

La colonne d'EBITDA reprend les [canoniques § 2.2](../donnees/chiffres-canoniques.md), mois par palier.

| | A — COGS négocié | B — COGS payé 15 % trop cher |
|---|---:|---:|
| EBITDA cumulé 24 mois | **1 503 492 €** | **927 954 €** |
| Écart | | **−575 538 €, soit −38,3 %** |
| Perte cumulée de la vallée de la mort (M1–M9) | −147 237 € | −181 074 € |
| Capital à apporter pour tenir jusqu'à M9 | | **+23,0 %** |
| MER seuil d'EBITDA au palier P2 | 2,71 | **2,89** |
| Écart au seuil, à MER réel 2,20 | −19,0 % | **−23,9 %** |
| Besoin en fonds de roulement au palier P3 | 481 053 € | **520 293 €** |

Trois lectures, par gravité croissante. **Un.** 575 538 €, c'est 38,3 % de tout l'EBITDA de la période : pas une ligne de coût, plus d'un tiers du résultat. **Deux.** Le plus dangereux n'est pas le montant mais **la vallée de la mort qui s'approfondit de 23 %** : B doit apporter 33 837 € de plus avant d'avoir rien prouvé, quand son EBITDA est négatif et que lever coûte le plus cher en dilution. **Trois.** Le MER seuil d'EBITDA de P2 passe de 2,71 à 2,89 pour un MER réel de 2,20 : l'écart au seuil se creuse de −19,0 % à −23,9 %. **La marque B doit être meilleure en publicité pour survivre au même endroit** — et rien, dans son compte publicitaire, ne signale la cause.

**La trajectoire inverse.** Une marque qui négocie 15 % **mieux** gagne les mêmes 575 538 € : l'écart entre les deux trajectoires opposées atteint **1 151 076 € sur deux ans**, sans un euro de chiffre d'affaires supplémentaire. Réinvestis en acquisition à P3, ces 575 538 € achètent 575 538 ÷ 33,18 = **17 346 clients** ([canoniques § 3.1](../donnees/chiffres-canoniques.md)), dont la contribution nette à 12 mois vaut 17 346 × (80,06 − 33,18) = **813 380 €**. **Le COGS mal négocié coûte 575 538 € plus les 813 380 € que ces euros auraient produits.**

**Le rappel qui remet tout en place.** Au palier P5 ([canoniques § 7](../donnees/chiffres-canoniques.md)), une baisse de 10 % du COGS vaut 628 313 € d'EBITDA annuel, soit **14,4 %** : le levier le plus faible du tableau, loin derrière le panier moyen à 71,7 %. Aucune contradiction, et c'est le point le plus fin de la séance. **À P5, le COGS est un petit levier : il ne pèse plus que 14,5 % du CA HT et on ne peut plus en gratter que quelques pour cent. À l'instant du sourcing, c'est un très grand levier, parce qu'un facteur 1,5 y est encore disponible — et qu'il sera ensuite verrouillé pour des années.**

> **À retenir :** ton COGS n'est pas une donnée que tu subis, c'est une décision que tu prends une fois et que tu paies pendant vingt-quatre mois. Sur la trajectoire canonique, 15 % d'écart de négociation valent 575 538 € d'EBITDA, 23 % de vallée de la mort en plus, et 0,18 point de MER seuil.

---

## 9. Avant la séance suivante

1. **Obtiens un devis réel de plus**, d'un fabricant identifié comme tel, et remplace toute ligne hypothétique de ton COGS par un chiffre sourcé — zéro hypothèse sur les lignes 1, 5, 6 et 8.
2. **Fais confirmer ta position tarifaire par écrit** par un commissionnaire en douane, et recalcule la ligne 8.
3. **Lance ton test d'usage accéléré** sur les deux meilleurs échantillons : il doit être fini avant S06, quand tu écriras les publicités qui promettent ce qu'il aura prouvé.
4. **Passe ton COGS dans le calculateur**, pour arriver en S04 avec ta cascade de marge posée :

```bash
python3 ecommerce/outils/calculateur.py --cogs <COGS en % du CA HT> --logistique <…>
```

---

*Fin de la séance S03. Suite : [S04 — L'offre, le prix et le panier](S04-offre-prix-et-panier.md), qui prend ton COGS en entrée et te fait découvrir que ton coefficient produit ne dit presque rien de ta capacité à financer un client.*
