# Niveau L06 — Gestionnaire

> **Prérequis :** niveau L05 validé.
>
> **Ce que tu sais faire à la sortie :**
> 1. Tu convertis un compte de résultat mensuel en semaines de trésorerie restantes, et tu dis lequel des deux chiffres commande la décision du trimestre.
> 2. Tu dimensionnes un stock par un point de recommande calculé, et tu chiffres ce que vaut en trésorerie une renégociation de MOQ ou de délai de paiement.
> 3. Tu produis un plan de redressement à 90 jours dont chaque levier est chiffré en points de marge, ordonné par rapport gain sur effort, daté, contrepartie écrite avant d'être subie.
>
> **Temps de travail typique :** 22 à 30 heures. Premier niveau dont l'épreuve n'a pas de réponse unique : elle a un plan défendable et une arithmétique qui doit tenir.

> **Lxx mesure ta compétence. Nx mesure l'état de ton business.** Les deux échelles sont indépendantes : un directeur financier peut être L06 sans posséder de marque, et une marque **N3** peut être pilotée par une compétence **L04** — quelqu'un qui alloue un budget publicitaire correctement, ne sait pas lire un besoin en fonds de roulement, et découvre sa contrainte de trésorerie six semaines avant qu'elle ne se referme. **C'est le cas le plus dangereux du métier**, et il devient mortel ici : jusqu'à L05, l'incompétence coûte de la marge ; à partir de L06, elle coûte l'entreprise ([diagnostic](../mentorat/diagnostic.md)).

---

## 1. Les compétences du niveau

1. **Je calcule les deux MER seuils de tête**, `1,20 ÷ CM2` et `1,20 ÷ (CM2 − fixes en % du CA HT)`, et je situe le MER réel entre les deux sans regarder la formule.
2. **Je convertis une perte mensuelle en semaines de trésorerie** en incluant ce que le compte de résultat ne montre pas : variation du BFR, échéances d'emprunt, TVA à reverser.
3. **Je calcule un point de recommande** avec un écart type mesuré sur la fenêtre du délai, jamais sur la journée, et je sais pourquoi la différence vaut un facteur dix.
4. **Je chiffre en euros de trésorerie une négociation fournisseur** — prix, MOQ, délai de paiement — et je sais laquelle des trois vaut le plus dans **ma** situation du moment.
5. **Je refuse un gain de marge qui coûte de la trésorerie** quand mon horizon est plus court que son délai de récupération, et je dis à quelle date je le reprendrai.
6. **Je chiffre un levier en points de marge sur un dénominateur figé**, contrepartie écrite d'avance, et j'ordonne mes leviers par rapport gain sur effort — en assumant qu'un levier plus rentable s'exécute après un levier plus lent.
7. **Je construis un plan de redressement sans hypothèse de croissance**, et je reconnais une opération promotionnelle de sauvetage pour ce qu'elle est : un emprunt dont personne ne calcule le taux.

## 2. Ce que tu lis

| # | Lecture | Ce qu'elle apporte **à ce niveau** |
|---|---|---|
| 1 | [**E10**](../modules/E10-cash-et-operations.md) § 1, § 2, § 5 | Le cycle de conversion du cash, l'intensité en cash par tranche de 100 000 € de CA, `g = EBITDA mensuel ÷ BFR` ; le point de recommande, l'écart type mesuré sur la fenêtre du délai, ce que vaut un MOQ. **Le cœur du niveau.** |
| 2 | [**E10**](../modules/E10-cash-et-operations.md) § 6 et § 7 | La logistique en euros par commande, 3PL contre internalisation, et pourquoi trente jours de délai fournisseur valent plus que 2 % de remise. |
| 3 | [**C08**](../etudes-de-cas/C08-redressement-90-jours.md), puis [**C05**](../etudes-de-cas/C05-abonnement-et-cac-negatif.md) et [**E01**](../modules/E01-arithmetique-de-la-marque.md) § 4-5 relu | C08 est le modèle de l'épreuve — lis-le **après** l'avoir tentée. C05 en est le symétrique : quand une contribution négative à la première commande est un calcul. E01 donne les deux MER seuils, relus ici comme une contrainte de trésorerie. |

## 3. Ce que tu fais

| Travail | Livrable | Comment on sait que c'est fait |
|---|---|---|
| [**S12**](../atelier/S12-la-crise.md), première partie | Un **plan de crise à 14 jours** : ce que tu coupes lundi, ce que tu appelles, ce que tu ne touches pas | Chaque ligne a un montant, une date, un responsable. Une ligne sans montant n'est pas une décision |
| [**S11**](../atelier/S11-passer-a-l-echelle.md), volet trésorerie | Le plan de trésorerie à 12 mois du passage 30 k€ → 300 k€ | Le creux est daté au mois près, le montant à réunir écrit avant la première dépense |
| **`simulateur_tresorerie.py`**, scénario de crise **imposé** | Trois exécutions : trajectoire subie, avec ton plan, avec le plan inverse | Tu nommes la semaine où la trésorerie passe sous le point de non-retour dans le cas subi |

```
python3 ecommerce/outils/simulateur_tresorerie.py \
    --ca 780000 --croissance 0 --marge 0.51 --mer 2.50 \
    --fixes 78000 --jours-stock 90 --dso 3 --dpo 60 \
    --tresorerie 165000 --horizon 12
```

Tu notes la semaine où la trésorerie franchit zéro, puis tu rejoues en modifiant **un seul paramètre à la fois** — `--jours-stock 60`, `--dpo 30`, `--mer 2.85`, `--marge 0.565` — et tu classes les quatre par trésorerie gagnée au 90ᵉ jour.

> **Ce que la série te fait découvrir.** `--dpo 30` **détruit plus de trésorerie sur le trimestre que le gain de marge obtenu en l'échangeant** ; `--jours-stock 60`, qui ne change rien au compte de résultat, en rapporte plus que la marge brute passée de 51 % à 56,5 %.

## 4. L'épreuve

**Durée : 4 h 00.** Calculatrice autorisée, aucun document. **Barème sur 100. Passage à 70. Pénalité de plan : −15 points** si le plan rendu à la question 6 dépend, en tout ou partie, d'une hausse du chiffre d'affaires pour atteindre l'équilibre — quelle que soit la qualité du reste de la copie, et cumulable avec les fautes éliminatoires du § 6.

### Le dossier — KANOPÉ

> *Cas composite. Marque fictive. Les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.*

KANOPÉ vend des compléments alimentaires en direct, en France et en Belgique. Trente-quatre mois d'existence, quatre références, un produit héros qui pèse 46 % du coût marchandise. Le fondateur t'appelle un lundi de mars : l'expert-comptable vient de rendre les comptes de février, il perd de l'argent depuis cinq mois.

**Février — mois complet, non saisonnier.** CA **780 000 € TTC**, soit **650 000 € HT**. 13 000 commandes, dont 9 000 premières et 4 000 réachats. Panier moyen 60,00 € TTC / 50,00 € HT, identique en première commande et en réachat. Croissance sur six mois : +0,4 % — **la marque est plate**. Publicité 312 000 €. Frais fixes 78 000 € HT. Trésorerie au 1ᵉʳ mars **165 000 €**, échéance mensuelle d'emprunt 6 500 €, capital mobilisable **0 €**.

| Coût variable, en % du CA HT | Taux | Détail |
|---|---:|---|
| Coût marchandise (COGS) | 19,0 % | Dont 72 % chez un fournisseur unique |
| Logistique complète | 13,5 % | 6,75 € HT/commande : préparation 1,85 € + transport 4,20 € + emballage 0,45 € + retours 0,25 € |
| Frais de paiement (PSP) | 1,7 % | |
| Retours, casse, gestes commerciaux | 3,8 % | Dont **41 % au motif « ne correspond pas à la description »**, sur deux références |
| Remises et codes | 11,0 % | Code de bienvenue permanent −10 %, code panier abandonné −15 %, codes créateurs non plafonnés |

**BFR au 1ᵉʳ mars :** stock au coût de revient 370 500 € + encours d'encaissement 78 000 € (3 jours de CA TTC) + avance publicitaire 72 800 € (7 jours de dépense) − dettes fournisseurs 190 000 € (délai de paiement 60 jours) = **331 300 €**.

**Le produit héros.** 8 000 unités/mois, coût de revient rendu entrepôt 6,00 €/unité, délai fournisseur complet 75 jours, écart type de la demande **mesuré sur des fenêtres glissantes de 75 jours** égal à 22 % de la demande moyenne sur la fenêtre, service visé 97,5 % (`Z = 1,96`), cycle de commande actuel 90 jours, **MOQ négocié 8 000 unités**.

**La courbe de réponse publicitaire** — deux tests d'augmentation, par tranches de 78 000 € mensuels.

| Dépense mensuelle cumulée | 78 000 € | 156 000 € | 234 000 € | **312 000 € — actuel** | 390 000 € — proposé |
|---|---:|---:|---:|---:|---:|
| Premières commandes cumulées | 3 400 | 5 900 | 7 700 | **9 000** | 9 900 |

**La rétention.** Réachats cumulés par client à 12 mois : **1,10**. Panier de réachat identique au panier d'acquisition.

**Les trois propositions du fondateur.** **α :** **−7 % sur les prix** contre un engagement de volume de douze mois **et** le passage du délai de paiement de 60 à 30 jours, les dettes fournisseurs tombant de 190 000 € à 95 000 €. **β :** appel d'offres ramenant le transport de 4,20 € à 3,75 € par commande et l'emballage de 0,45 € à 0,33 €, pour 12 000 € d'outillage, le contrat 3PL imposant un **préavis de 60 jours**. **γ :** **−25 % sur dix jours** pour refaire de la trésorerie — *hypothèses fournies :* volume de la période ×**2,2** ; **45 %** des commandes supplémentaires auraient eu lieu au prix plein sous soixante jours ; **60 %** des commandes de la période sont des premières commandes ; une cohorte promotionnelle réachète **42 % moins souvent** ([simulateur](../outils/README-simulateur.md) § 8).

```
Deux conventions, à respecter dans toute la copie :
1. Un « point de marge » vaut 1 % du CA HT de février, soit 6 500 €/mois.
   Le dénominateur ne bouge pas, quoi que fasse le plan : sans dénominateur
   figé, deux leviers ne s'additionnent pas.
2. Frais fixes et échéance d'emprunt sont les seuls décaissements hors
   exploitation. Pas d'impôt (résultat négatif), pas d'investissement.
```

### Les questions

**Q1 — Le diagnostic, en chiffres. (12 points)** (a) CM2, CM3 et EBITDA, en euros et en % du CA HT. (b) MER réel, MER seuil de contribution, MER seuil d'EBITDA, écart en % au seuil d'EBITDA. (c) Semaines de trésorerie restantes au 1ᵉʳ mars, calcul déroulé. (d) En deux lignes : le problème de KANOPÉ n'est pas celui que son fondateur croit — écris lequel c'est.

**Q2 — Le stock. (14 points)** (a) Point de recommande du héros, en unités et en euros, stock de sécurité déroulé ; puis le résultat qu'aurait donné un écart type **quotidien** de 22 % avec une racine de 75, et pourquoi il est faux. (b) Trésorerie libérée par un cycle de commande ramené de 90 à 30 jours, sur le héros puis extrapolée à la gamme — le MOQ le permet-il ? (c) L'audit révèle en plus 56 152 € de surstock sur deux références en fin de vie : donne l'objectif de stock du plan, en euros et en jours de coût marchandise.

**Q3 — La dépense publicitaire. (16 points)** (a) CAC marginal des quatre tranches et de celle que propose le fondateur. (b) LTV à 12 mois en marge de contribution, aux conditions de février. (c) Le niveau de dépense que tu retiens, pourquoi, et l'effet immédiat sur l'EBITDA mensuel. (d) Ce que ta décision coûte en LTV sur douze mois — conclus.

**Q4 — Les leviers de marge. (18 points)** Pour chacun : gain **en points de marge** et **en euros/mois**, contrepartie chiffrée, délai avant premier effet.

**A** — remise de 11,0 % à 7,5 % du CA HT (*hypothèse : la suppression du code de bienvenue permanent et du code panier abandonné coûte **6 % des commandes***). **B** — proposition α. **C** — proposition β. **D** — retours de 3,8 % à 2,9 %, par refonte des deux fiches produit et retrait de trois concepts sur-promettants (*14 000 € non récurrents ; hypothèse : aucun effet sur le volume, la dépense étant réallouée*). **E** — frais fixes de 78 000 € à 68 500 € HT (*arrêt d'une prestation créative externalisée, indemnité de préavis de 19 000 € payée immédiatement*).

**Q5 — L'arbitrage fournisseur. (12 points)** (a) Gain annuel de marge de α. (b) Effet immédiat sur la trésorerie et sur les semaines restantes, si elle est acceptée le 1ᵉʳ mars. (c) Délai de récupération en trésorerie, en mois. (d) Ta décision, la date à laquelle tu la reconsidères, et ce que tu proposes au fournisseur à la place.

**Q6 — Le plan à 90 jours. (28 points)** (a) Un tableau des leviers retenus **ordonnés par rapport gain sur effort**, avec gain mensuel, effort, date d'effet et contrepartie assumée. (b) Le compte de résultat projeté des mois 1 à 3 et le tableau de trésorerie des trois mois. (c) La position au 31 mai et le nouveau MER seuil d'EBITDA. (d) La proposition γ : chiffre son effet immédiat sur la contribution de la période, l'effet de la demande avancée, l'effet sur la LTV de la cohorte acquise ; conclus, puis donne **la condition précise** dans laquelle il faudrait quand même la lancer.

---

## 5. Le corrigé

### Q1 — Le diagnostic

```
CM2 = 100 % − (19,0 + 13,5 + 1,7 + 3,8 + 11,0) = 51,0 %
Marge brute = 650 000 × 51,0 %        = 331 500 € HT
Publicité                             = 312 000 €    → 48,0 % du CA HT
CM3         = 331 500 − 312 000       =  19 500 € HT →  3,0 % du CA HT
Frais fixes                           =  78 000 € HT → 12,0 % du CA HT
EBITDA      =  19 500 − 78 000        = −58 500 € HT → −9,0 % du CA HT

MER réel         = 780 000 ÷ 312 000       = 2,50
MER seuil CM3    = 1,20 ÷ 0,510            = 2,35
MER seuil EBITDA = 1,20 ÷ (0,510 − 0,120)  = 3,08
Écart au seuil EBITDA = 2,50 ÷ 3,08 − 1    = −18,8 %

Consommation nette = 58 500 (EBITDA) + 6 500 (emprunt)   = 65 000 €/mois
   la marque étant plate, la variation du BFR est nulle
Par semaine = 65 000 ÷ 4,33 = 15 012 €
Semaines restantes = 165 000 ÷ 15 012 = 11,0 semaines
```

**(d)** KANOPÉ est **au-dessus** de son seuil de contribution et **18,8 % sous** son seuil d'EBITDA : la zone que le [diagnostic](../mentorat/diagnostic.md) bloc C nomme « tu finances ta structure avec ton capital », légitime seulement si le réachat rembourse — et ici il ne rembourse pas. Le fondateur croit donc avoir un problème de rentabilité ; il a **onze semaines de trésorerie**. Sa contrainte active est le calendrier : un levier qui rapporte au mois 5 ne compte pas, et un levier qui rapporte de la marge en consommant de la trésorerie l'achève.

**Barème.** (a) 4, une par ligne. (b) 4. (c) 2, dont 1 pour l'échéance d'emprunt — l'oublier donne 12,2 semaines et vaut 0. (d) 2, la réponse devant nommer le **calendrier** ou la **contrainte de trésorerie** ; « sa marge est trop faible » vaut 0.

---

### Q2 — Le stock

```
(a)  Consommation quotidienne = 8 000 ÷ 30      =    266,67 unités
     Demande sur le délai     = 266,67 × 75     = 20 000 unités
     σ sur la fenêtre         = 22 % × 20 000   =  4 400 unités
     Stock de sécurité        = 1,96 × 4 400    =  8 624 unités  (32,3 jours)
     Point de recommande      = 20 000 + 8 624  = 28 624 u = 171 744 € de COGS
     Avec un σ QUOTIDIEN : 1,96 × (22 % × 266,67) × √75 = 996 u = 3,7 jours
```

La racine carrée suppose les écarts quotidiens **indépendants**. En vente directe ils ne le sont jamais : une publicité qui gagne, une rupture concurrente, un pic saisonnier sont des décalages de niveau qui durent des semaines. Le σ quotidien sous-estime ici la sécurité d'un **facteur 8,7** ([E10](../modules/E10-cash-et-operations.md) § 5.1).

**(b)** Sécurité et transit ne bougent pas : seul le **stock de travail** dépend du cycle, et vaut la moitié du cycle.

```
Cycle 90 j : 45 j × 266,67 u × 6,00 € = 72 000 €
Cycle 30 j : 15 j × 266,67 u × 6,00 € = 24 000 €
Libéré sur le héros                   = 48 000 €
Gamme entière (héros = 46 % du COGS) : 48 000 ÷ 0,46 = 104 348 €
```

Le MOQ le permet **tout juste** : 8 000 unités par commande, MOQ à 8 000. **Ce MOQ vaut 104 348 € de trésorerie** — la ligne qu'on cède contre 2 % de remise sans l'avoir jamais chiffrée.

```
(c)  104 348 + 56 152 = 160 500 € libérés
     Stock cible = 370 500 − 160 500 = 210 000 €
     COGS mensuel du plan (Q6) = 19,0 % × 549 900 = 104 481 €
     Stock cible = 210 000 ÷ 104 481 × 30 = 60,3 jours
```

**Barème.** (a) 7 : 1 la consommation quotidienne, 1 la demande sur le délai, 2 la sécurité, 1 les euros, 2 l'explication du σ — elle doit contenir l'**indépendance** ou le décalage durable, « il n'a pas pris le bon σ » vaut 0. (b) 5, dont 2 pour la moitié du cycle et 1 pour le MOQ ; appliquer le cycle au stock **total** coûte les 5. (c) 2.

---

### Q3 — La dépense publicitaire

| Tranche | Dépense | Cmd. cumulées | De la tranche | **CAC marginal** |
|---|---:|---:|---:|---:|
| 1 | 78 000 € | 3 400 | 3 400 | **22,94 €** |
| 2 | 156 000 € | 5 900 | 2 500 | **31,20 €** |
| 3 | 234 000 € | 7 700 | 1 800 | **43,33 €** |
| **4 — actuelle** | **312 000 €** | **9 000** | **1 300** | **60,00 €** |
| 5 — proposée | 390 000 € | 9 900 | 900 | **86,67 €** |

Le nCAC moyen vaut `312 000 ÷ 9 000 = 34,67 €` : il ne décrit **aucune** des quatre tranches.

```
(b) Contribution d'une commande = 50,00 € HT × 51,0 % = 25,50 € HT
    LTV 12 mois = 25,50 × (1 + 1,10) = 53,55 € HT

(c) CAC marginal tranche 4 = 60,00 € > 53,55 €  → détruit, on coupe
    CAC marginal tranche 3 = 43,33 € < 53,55 €  → conservé
    Dépense épargnée                    = 78 000 €
    Contribution perdue 1 300 × 25,50 € = 33 150 €
    Gain net                            = +44 850 € par mois

(d) 1 300 × 53,55 € = 69 615 € de LTV 12 mois abandonnée par mois
    Sur douze mois : 936 000 € épargnés contre 835 380 € abandonnés
```

La proposition du fondateur ferait l'inverse : `900 × 25,50 = 22 950 €` pour 78 000 € de dépense, soit **−55 050 € par mois**. **La coupe est légèrement positive sur douze mois et décisive sur le trimestre** — 44 850 € dès le premier mois contre 8 385 € abandonnés sur l'année. Avec deux ans de trésorerie, garder la tranche 4 se défendrait, à condition de l'écrire comme un achat de volume chiffré.

**Barème.** (a) 5, 1 par CAC marginal ; répondre par le CAC moyen vaut 0 sur la question. (b) 3. (c) 5 : 2 la comparaison marginal/LTV, 2 le chiffrage, 1 l'écartement des 390 000 €. (d) 3 ; « on coupe, c'est tout bénéfice » vaut 1.

---

### Q4 — Les leviers de marge

| Levier | Gain mensuel | En points | Contrepartie chiffrée | Premier effet |
|---|---:|---:|---|---|
| **A** — remise 11,0 → 7,5 % | **+20 215 €** | **+3,11** | −6 % des commandes ; deux créateurs sous contrat à renégocier | **Jour 2** |
| **B** — fournisseur α | +6 224 € | +0,96 | **−95 000 € de trésorerie immédiate** | Mois 1 |
| **C** — logistique β | +7 410 € | +1,14 | 12 000 € d'outillage ; préavis 3PL de 60 jours | **Mois 3** |
| **D** — retours 3,8 → 2,9 % | +5 850 € | +0,90 | 14 000 € ; trois concepts au meilleur CPA affiché retirés | Mois 2 |
| **E** — fixes 78 000 → 68 500 € | +9 500 € | +1,46 | 19 000 € d'indemnité ; capacité créative à reconstruire | Mois 2 |

**A — le piège de l'épreuve.** Le gain brut de 3,5 points, soit 22 750 €, n'est pas le gain.

```
Gain brut              3,5 pts × 6 500 €               = 22 750 €
Commandes perdues      6 % × 13 000                    =    780
Contribution perdue au NOUVEAU taux de marge (54,5 %) :
                       780 × 50,00 € × 54,5 %          = 21 255 €
Gain net à budget publicitaire figé                    =  1 495 €

Mais on pilote AU MER, pas au budget : les 780 commandes disparues
n'ont plus besoin d'être achetées.
Dépense à MER constant : 611 000 × 1,20 ÷ 2,50 = 293 280 €, soit −18 720 €
Gain net réel = 1 495 + 18 720 = +20 215 €, soit +3,11 points
```

```
B : 123 500 € × 72 % × 7 %                                = 6 224 €/mois
C : (4,20 − 3,75) + (0,45 − 0,33) = 0,57 € ; × 13 000     = 7 410 €/mois
    la logistique passe de 6,75 € à 6,18 € par commande, soit de 13,50 %
    à 12,36 % du CA HT à panier constant
D : 0,9 point × 6 500 €                                   = 5 850 €/mois
    les 41 % de retours « ne correspond pas à la description » pèsent
    3,8 % × 0,41 = 1,56 point ; en reprendre 0,9, c'est en traiter 58 %
```

C est le meilleur rapport gain sur effort du dossier **et** le seul levier dont on ne verra rien pendant le trimestre.

**Barème.** 3 par levier pour B, C, D, E (gain, contrepartie, délai) = 12. 6 pour A, dont **4 pour l'effet de volume** : annoncer 3,5 points sans déduire les commandes perdues vaut 2 sur 6, et c'est l'erreur la plus fréquente de l'épreuve.

---

### Q5 — L'arbitrage fournisseur

```
(a) 123 500 € × 72 % × 7 % = 6 224 €/mois = 74 693 €/an  (+0,96 point)
(b) Trésorerie = 165 000 − 95 000 = 70 000 €
    Semaines   = 70 000 ÷ 15 012  = 4,7 semaines
(c) Délai de récupération = 95 000 ÷ 6 224 = 15,3 mois
```

**(d) On refuse — en mars.** Un levier qui met **15,3 mois** à rembourser sa trésorerie ne se prend pas avec **11,0 semaines** devant soi : il ferait tomber KANOPÉ sous cinq semaines — la zone d'urgence du [diagnostic](../mentorat/diagnostic.md) bloc F. On le reconsidère **au 1ᵉʳ juin**, avec 289 466 € en caisse (Q6). À la place : **le prix sans le délai** — 3 à 4 % contre l'engagement de volume seul, en gardant les 60 jours ; et si le fournisseur refuse de dissocier, l'échelonnement sur six mois, ~16 000 € par mois au lieu de 95 000 € d'un coup. **Trente jours de délai valent ici plus que 7 % de prix** ([E10](../modules/E10-cash-et-operations.md) § 7.1).

**Barème.** (a) 2. (b) 4, dont 2 les semaines. (c) 2. (d) 4 : 2 le refus argumenté par **15,3 mois contre 11 semaines** — « c'est trop cher » vaut 0 —, 1 la date de réexamen, 1 la contre-proposition.

---

### Q6 — Le plan à 90 jours

| Rang | Levier | Gain mensuel | Effort | Date d'effet | Contrepartie assumée |
|---|---|---:|---|---|---|
| 1 | **F** — publicité 312 000 → 234 000 € | **+44 850 €** | 1 après-midi | **1ᵉʳ mars** | −1 300 premières cmd/mois ; 8 385 €/an de LTV |
| 2 | **A** — remise 11,0 → 7,5 % | **+20 215 €** | 2 jours | **2 mars** | −6 % de commandes ; 2 créateurs à renégocier |
| 3 | **G** — stock 370 500 → 210 000 € | 0 de marge, **+160 500 € de trésorerie** | 2 semaines | mars-mai | Risque de rupture pendant l'écoulement |
| 4 | **E** — frais fixes −9 500 € | **+9 500 €** | 1 semaine + préavis | **1ᵉʳ avril** | 19 000 € ; créa externe à reconstruire |
| 5 | **D** — retours 3,8 → 2,9 % | **+5 850 €** | 3 semaines | **1ᵉʳ avril** | 14 000 € ; 3 concepts retirés |
| 6 | **C** — logistique −0,57 €/cmd | **+7 410 €** | Appel d'offres | **1ᵉʳ mai** | 12 000 € ; p90 du délai à surveiller |
| — | **B** — fournisseur α | +6 224 € | 1 réunion | **reporté au 1ᵉʳ juin** | −95 000 € : incompatible avec 11 semaines |

C a un meilleur rapport gain sur effort que D et E et arrive **dernier** : un préavis de 60 jours ne se négocie pas. **Le rapport gain sur effort ordonne les priorités ; le calendrier ordonne l'exécution.** Volume du plan, stable sur le trimestre : `(7 700 + 4 000) × 0,94 = 10 998` commandes, soit **549 900 € HT** et **659 880 € TTC**. Les 4 000 réachats viennent de cohortes déjà acquises et ne bougent pas dans la fenêtre.

| | **M1 — mars** | **M2 — avril** | **M3 — mai** |
|---|---:|---:|---:|
| Leviers actifs | F, A | + E, D | + C |
| CA HT | 549 900 € | 549 900 € | 549 900 € |
| Coûts variables | 45,50 % | 44,60 % | 43,46 % |
| **CM2** | **54,50 %** | **55,40 %** | **56,54 %** |
| Marge brute | 299 696 € | 304 645 € | 310 913 € |
| Publicité | 234 000 € | 234 000 € | 234 000 € |
| **CM3** | **65 696 €** | **70 645 €** | **76 913 €** |
| Frais fixes | 78 000 € | 68 500 € | 68 500 € |
| **EBITDA** | **−12 305 €** | **+2 145 €** | **+8 413 €** |
| **% du CA HT** | **−2,24 %** | **+0,39 %** | **+1,53 %** |

| Trésorerie | M1 | M2 | M3 |
|---|---:|---:|---:|
| EBITDA | −12 305 € | +2 145 € | +8 413 € |
| Échéance d'emprunt | −6 500 € | −6 500 € | −6 500 € |
| Déstockage (levier G) | +40 000 € | +60 000 € | +60 500 € |
| Baisse mécanique du BFR | +30 212 € | — | — |
| Coûts non récurrents | −33 000 € | −12 000 € | — |
| **Flux net** | **+18 408 €** | **+43 645 €** | **+62 413 €** |
| **Trésorerie en fin de mois** | **183 408 €** | **227 052 €** | **289 466 €** |

Baisse mécanique du BFR au mois 1 : `78 000 − 65 988 = 12 012 €` d'encours, `72 800 − 54 600 = 18 200 €` d'avance publicitaire.

```
Trésorerie au 31 mai      = 289 466 €, contre 165 000 €        (+75 %)
Flux mensuel positif dès le mois 2
MER réel                  = 659 880 ÷ 234 000            = 2,82
MER seuil de contribution = 1,20 ÷ 0,5654                = 2,12
Fixes en % du CA HT       = 68 500 ÷ 549 900             = 12,46 %
MER seuil EBITDA          = 1,20 ÷ (0,5654 − 0,1246)     = 2,72
Écart au seuil EBITDA     = 2,82 ÷ 2,72 − 1              = +3,7 %
```

**Le plan en une ligne : le CA TTC passe de 780 000 € à 659 880 €, soit −15,4 %, et l'EBITDA de −58 500 € à +8 413 €.** Aucune ligne ne suppose un client de plus. Un plan qui atteint l'équilibre en faisant décroître le chiffre d'affaires de 15 % s'exécute en mars ; celui qui l'atteint en supposant +20 % de croissance est une prière.

**(d) La proposition γ**

```
Volume de dix jours au régime du plan = 10 998 ÷ 30 × 10  =  3 666 commandes
Volume promotionnel = 3 666 × 2,2                         =  8 065 commandes
Panier HT à −25 %   = 50,00 × 0,75                        =  37,50 € HT

Contribution unitaire en promotion :
   37,50 − 9,50 (COGS) − 6,75 (logistique)
        − 0,64 (PSP 1,7 %) − 1,43 (retours 3,8 %)         =  19,19 € HT
Contribution unitaire au prix plein : 50,00 × 54,5 %      =  27,25 € HT

1. Effet immédiat  8 065 × 19,19 − 3 666 × 27,25
                 = 154 752 − 99 899                       = +54 853 €
2. Demande avancée (8 065 − 3 666) × 45 % = 1 980 cmd
                 × (27,25 − 19,19)                        = −15 961 €
3. LTV de la cohorte  8 065 × 60 % = 4 839 clients
                 × 1,10 × 42 % × 27,25 €                  = −60 922 €
                                              TOTAL       = −22 030 €
```

**Verdict : on ne la lance pas.** 54 853 € de trésorerie en dix jours contre 22 030 € de valeur détruite — et elle **contredit le levier A** : réapprendre à ta base d'acheter à −25 % six semaines après lui avoir retiré son −10 % permanent, c'est payer deux fois pour installer le réflexe que ton plan existe pour désinstaller.

**La condition dans laquelle il faudrait quand même la lancer :** une trésorerie passée sous **quatre semaines**. 54 853 € encaissés en dix jours contre 76 883 € payés sur douze mois est alors un emprunt cher mais **immédiat et sans garantie**, ce qu'aucune banque ne propose en quinze jours — et une entreprise en défaut ne vaut plus rien. **Ce qui distingue un gestionnaire d'un amateur n'est pas de refuser cette opération : c'est de savoir à quel niveau de trésorerie elle cesse d'être une erreur.**

**Barème de la question 6.** (a) 6 : 3 un ordre gain sur effort défendable, 3 la distinction priorité / exécution. (b) 10 : 6 le compte de résultat (2 par mois, l'EBITDA du mois 3 devant tomber entre +6 000 € et +11 000 €), 4 la trésorerie dont **2 pour le déstockage** — une trésorerie bâtie sur le seul EBITDA plafonne à 2. (c) 2. (d) 10 : 6 les trois calculs, 2 le verdict s'il mentionne la contradiction avec A, 2 la condition, qui doit être **un seuil de trésorerie chiffré**. **Pénalité de −15** si l'équilibre repose sur une hausse du chiffre d'affaires.

---

## 6. Le critère de passage

**Note minimale : 70 / 100**, dont **au moins 15 / 28 à la question 6** — le plan est l'épreuve, le reste en est l'outillage. **Quatre fautes éliminatoires**, quelle que soit la note :

1. **Un plan qui atteint l'équilibre par une hausse du chiffre d'affaires.** La croissance coûte du cash avant d'en rapporter ([canoniques § 4](../donnees/chiffres-canoniques.md)) : on se l'autorise **après** un redressement, jamais comme son moyen.
2. **Accepter la proposition α au mois 1** — faire tomber la trésorerie de onze à moins de cinq semaines pour 0,96 point de marge : la faute la plus chère du dossier, et celle que le fondateur voudra commettre parce qu'elle « améliore la marge ».

3. **Confondre CAC moyen et CAC marginal** : arbitrer la tranche 4 sur les 34,67 € du nCAC moyen conduit à la conserver, puis à financer la cinquième.
4. **Un montant sans mention HT ou TTC**, ou un MER calculé sur du CA HT : les confondre déplace le seuil d'équilibre de 20 % dans le sens qui rassure.

**Fautes lourdes :** oublier l'échéance d'emprunt (−4) ; bâtir la trésorerie sur le seul EBITDA (−6) ; chiffrer A sans déduire les commandes perdues (−4). **En cas d'échec**, tu repasses sur une marque à contrainte inversée : trésorerie confortable, marge légèrement positive, croissance de 18 % par mois consommant plus de trésorerie que l'EBITDA n'en produit. Mêmes leviers, ordre entièrement différent — et c'est l'ordre qui est noté.

---

## 7. Les pièges de ce niveau

**1. Confondre la marge et la trésorerie, puis croire qu'on ne les confond plus.** À l'épreuve, la moitié des candidats accepte α : « −7 % sur les achats » se lit comme une amélioration, « 60 jours qui deviennent 30 » comme une modalité. Les deux chiffres sont dans la même phrase du fournisseur et vont en sens opposés — l'un rapporte 6 224 € par mois, l'autre en coûte 95 000 € tout de suite. **Un fournisseur qui t'offre du prix contre du délai ne te fait pas une remise : il te vend de la dette au taux qui l'arrange.**

**2. Croire qu'un plan de redressement est une liste de leviers, et confondre le rapport gain sur effort avec l'ordre d'exécution.** C'est une liste de leviers **datés** : six leviers qui rapportent 95 000 € par mois au mois 4 ne valent rien pour une marque qui a onze semaines — regarde la date de premier effet de chaque ligne de ton dernier plan, et si la moitié tombe au-delà du trimestre, tu as écrit une intention. Ici, le levier logistique est le mieux placé des deux points de vue et arrive dernier, à cause d'un préavis. Le déstockage ne rapporte pas un centime de marge et arrive troisième, parce qu'il apporte 160 500 € de trésorerie — deux fois et demie le meilleur levier de marge sur le trimestre. **Un levier de trésorerie et un levier de marge ne se comparent pas ; ils s'exécutent ensemble.**

**3. Croire que « je perds de l'argent » est un diagnostic.** C'est un symptôme à quatre causes : MER sous le seuil de contribution (structure — produit ou prix) ; MER entre les deux seuils (taille) ; croissance supérieure à `EBITDA ÷ BFR` (financement, pas rentabilité) ; BFR qui dérive à volume constant (opérations). KANOPÉ est dans le deuxième cas **et** dans le quatrième — qui traite le deuxième en coupant les frais fixes laisse 160 500 € sur la table.

**4. Croire que L06 mesure ta marque.** Une marque **N3** à 780 000 € par mois est, aux yeux de sa banque et de son entourage, une réussite — elle est à onze semaines de la fin. Le chiffre d'affaires ne mesure ni la compétence ni la solidité : il mesure la vitesse à laquelle une erreur de structure se paie.

---

*Fin du niveau L06. Suite : [L07 — Stratège](L07-stratege.md) — tu sais redresser une marge sur les chiffres qu'on te donne. Reste à savoir lesquels sont vrais.*
