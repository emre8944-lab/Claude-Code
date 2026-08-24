# Module E01 — L'arithmétique de la marque

> **Prérequis :** [E00](E00-cadrage.md). En parallèle : [module 13](../../modules/13-unit-economics.md) du cursus racine.
> **Objet :** construire, depuis ta banque et ton back-office, les six nombres qui décident si ta marque vit, et démontrer la décision que chacun impose.
> **Temps de travail :** ~6 h (lecture + exercices, calculatrice obligatoire)

---

## 0. Pourquoi ce module existe

Il existe six nombres qui décident si une marque de e-commerce vit. Tout le reste — la charte graphique, le thème du site, l'outil d'e-mailing — est du commentaire.

```
1. La marge brute (CM2) en % du CA HT
2. Le MER, et son seuil
3. Le nCAC — coût d'acquisition d'un NOUVEAU client
4. La LTV à 12 mois, en marge de contribution
5. Le payback du CAC, en mois
6. Les frais fixes en % du CA HT
```

Ces six-là suffisent à écrire le compte de résultat, à décider si tu peux augmenter le budget média demain matin, et à dire à quel moment tu meurs. Aucun n'est difficile à calculer — c'est pour ça que presque personne ne les vérifie.

Et voilà l'observation qui justifie ce module : **une marque sur deux en calcule au moins deux faux**, toujours les deux mêmes. La part de la publicité dans le chiffre d'affaires, parce que le MER se lit sur du TTC et la marge sur du HT — section 2, l'erreur vaut 2 988 412 € par an au palier P5 de NØRA. Et la LTV, calculée en chiffre d'affaires au lieu de marge de contribution — section 6, facteur 1,95. Une marque qui se trompe sur ces deux-là se croit rentable de sept points et riche du double. Elle scale. Elle meurt.

---

## 1. La cascade des marges

### 1.1 La définition, sans ambiguïté

Dire « ma marge » sans préciser laquelle, c'est dire « ma vitesse » sans dire si c'est en ville ou sur autoroute. Quatre marges, quatre usages, quatre responsables.

```
CA TTC        prix payé par le client, TVA incluse
   ÷ (1 + TVA)
CA HT         chiffre d'affaires comptable — TOUTE marge se calcule là-dessus
   − COGS                 coût marchandise rendu entrepôt
CM1           marge sur coût marchandise
   − logistique           préparation, colis, transport, retour physique
   − PSP                  frais du prestataire de paiement
   − retours / SAV        remboursements, gestes commerciaux, casse
   − remises              codes promo, ventes flash, codes créateurs
CM2 = MARGE BRUTE — ce qui reste pour la publicité et la structure
   − publicité            média + production créative + honoraires d'agence
CM3           marge de contribution après acquisition
   − frais fixes          salaires, loyers, outils, honoraires
EBITDA        le résultat d'exploitation
```

Deux conventions à graver. **La TVA n'est pas ton argent** : un CA TTC de 4 333 196 € est un CA de 3 610 997 € et une dette fiscale de 722 199 €. **Une remise est un coût variable** : ligne visible, responsable nommé — sinon elle se dissout dans le prix moyen et personne ne la défend.

### 1.2 La cascade complète du palier P5

Canoniques § 2 (volumes), § 2.1 (structure de coût), § 2.2 (compte de résultat). P5 : 60 200 commandes/mois, AOV mixte 71,98 € TTC, sept marchés, TVA moyenne pondérée 20 %.

| Étage | Montant mensuel | % du CA HT |
| --- | ---: | ---: |
| CA TTC (60 200 × 71,98 €) | 4 333 196 € | 120,00 % |
| TVA (× 0,20 ÷ 1,20) | −722 199 € | −20,00 % |
| **CA HT** (4 333 196 ÷ 1,20) | **3 610 997 €** | **100,00 %** |
| COGS (× 0,145) | −523 595 € | −14,50 % |
| **CM1** | **3 087 402 €** | **85,50 %** |
| Logistique (× 0,110) | −397 210 € | −11,00 % |
| PSP (× 0,0155) | −55 970 € | −1,55 % |
| Retours / SAV (× 0,035) | −126 385 € | −3,50 % |
| Remises (× 0,080) | −288 880 € | −8,00 % |
| **CM2 — marge brute** | **2 218 957 €** | **61,45 %** |
| Publicité | −1 494 206 € | −41,38 % |
| **CM3** | **724 751 €** | **20,07 %** |
| Frais fixes | −360 000 € | −9,97 % |
| **EBITDA** (canonique : 364 752 €) | **364 751 €** | **10,10 %** |

Somme des coûts variables : 14,50 + 11,00 + 1,55 + 3,50 + 8,00 = 38,55 %, donc marge brute = **61,45 %**. Le canonique § 2.1 affiche 61,5 %, arrondi au dixième ; **j'utilise 61,45 % partout**, parce que 0,05 point sur 3 610 997 € vaut 21 660 € par an. L'euro d'écart sur CM3 et EBITDA vient de là.

Le même exercice sur les cinq paliers (canonique § 2.1) dit une chose qu'on n'attend pas. COGS, logistique et PSP s'améliorent de P1 à P5 — 4 + 5 + 0,25 = **9,25 points gagnés**, c'est le volume qui négocie — mais retours et remises se dégradent de 5,00 % à 11,50 %, soit **6,5 points perdus**. Solde : la marge brute ne passe que de 57,20 % à 61,45 %. **Elle ne s'améliore pas parce que tu grandis** : elle s'améliore si, et seulement si, tu négocies le COGS et la logistique plus vite que tes retours et tes remises ne se dégradent — cas [C04](../etudes-de-cas/C04-scale-qui-detruit-la-marge.md).

### 1.3 Ce que chaque étage décide, et qui en répond

| Étage | Ce qu'il sert à décider | Responsable | Revue |
| --- | --- | --- | --- |
| CA HT | Rien. C'est une taille, pas une performance. | Direction | Mensuelle |
| **CM1** | Renégocier, changer de conditionnement, relocaliser ? | Achats / supply | Trimestrielle |
| **CM2** | Peut-on financer de la pub ? La remise dérape-t-elle ? | Opérations **+** commerce | **Hebdomadaire** |
| **CM3** | Monter ou baisser le budget média demain ? | Acquisition / growth | **Quotidienne** |
| **EBITDA** | Recruter, ouvrir un marché, lever, ou couper ? | Le dirigeant, seul | Mensuelle |

La colonne de droite est la leçon : marge brute chaque semaine, CM3 chaque jour, parce que ce sont les deux seuls étages qui bougent vite — **regarder son COGS tous les matins est une occupation, pas un pilotage.** Le CM2 a deux responsables volontairement : sans la séparation opérations / commerce, la remise devient le levier de secours universel. Au canonique § 2.1 elle passe de 3,0 % du CA HT en P1 à 8,0 % en P5, soit **180 550 € par mois** — la moitié de l'EBITDA annuel de P5 (4 377 023 €, canonique § 7).

---

## 2. Le piège TTC / HT

Le MER (*Marketing Efficiency Ratio*) rapporte tout ton chiffre d'affaires à toute ta dépense publicitaire. Il se lit sur le TTC — ce que ta plateforme affiche et ce que ta banque encaisse — alors que ta marge se calcule sur le HT. Donc « la pub coûte quel pourcentage de mon CA ? » a une seule réponse, et ce n'est pas 1 ÷ MER. Pose t = TVA, R = CA TTC, P = dépense publicitaire.

```
MER = R ÷ P              donc    P = R ÷ MER
CA HT = R ÷ (1 + t)

Part de la pub en % du CA HT = P ÷ CA HT
                             = [ R ÷ MER ] ÷ [ R ÷ (1 + t) ]
                             = (1 + t) ÷ MER
```

**Part de la publicité en % du CA HT = (1 + TVA) ÷ MER.** Vérification sur P5 — canonique § 2 : CA TTC 4 333 196 €/mois ; § 2.3 : MER réel 2,90 ; § 2.2 : pub 1 494 206 €, soit 41,4 % du CA HT.

```
Dépense pub   = 4 333 196 ÷ 2,90       = 1 494 205,5 € ≈ 1 494 206 €   ✓
Part en % HT  = 1,20 ÷ 2,90            = 41,38 %                       ✓
Contre-vérif. = 1 494 206 ÷ 3 610 997  = 41,38 %                       ✓
```

Trois routes, un seul nombre. Celui qui n'a jamais fait la division écrit 1 ÷ 2,90 = 34,48 %.

```
Écart = 41,38 − 34,48 = 6,90 points de CA HT
Forme fermée : (1 + t) ÷ MER − 1 ÷ MER = t ÷ MER = 0,20 ÷ 2,90 = 6,897 %

Erreur mensuelle = 3 610 997 × 0,06897           = 249 034 €
   ou, plus court = 1 494 206 × (1 − 1 ÷ 1,20)
                  = 1 494 206 ÷ 6                = 249 034 €
Erreur annuelle  = 249 034 × 12                  = 2 988 412 €
```

**L'erreur vaut exactement un sixième de ta dépense publicitaire** — c'est la TVA contenue dans le CA que tu attribues à cette dépense. Face à l'EBITDA annuel de P5 (4 377 023 €) : 2 988 412 ÷ 4 377 023 = **68,3 % de l'EBITDA**. Celui qui commet cette erreur croit disposer de 68 % de résultat en plus qu'il n'en a.

À P5 il a de la réserve. À P2, MER réel 2,20, la même erreur donne 0,20 ÷ 2,20 = 9,09 points de CA HT, soit 191 833 × 0,0909 = 17 438 € par mois — pour un EBITDA réel de −19 838 €. **Il se croit à l'équilibre alors qu'il perd 238 056 € par an** : la vallée de la mort du cas [C02](../etudes-de-cas/C02-vallee-de-la-mort.md). Corollaire multi-pays : le canonique retient 20 % de TVA moyenne, mais l'Allemagne est à 19 % et l'Italie à 22 % — **ouvrir l'Italie fait monter ton MER seuil sans qu'aucun coût n'ait bougé** ([E11](E11-passage-a-echelle.md)).

---

## 3. Le MER, le ROAS, l'aMER

Le **ROAS plateforme** (CA attribué par une régie ÷ dépense sur cette régie) mesure ce que la régie s'attribue : il est manipulable par la partie qui vend l'espace. Le **MER blended** (CA total TTC ÷ dépense publicitaire totale) a pour numérateur le chiffre d'affaires de ta banque et pour dénominateur le total de tes factures média — aucune des deux n'est produite par une régie, c'est le seul des trois qui ne peut pas être truqué. L'**aMER** (CA total TTC ÷ prospection seule) mesure ce que rapporte l'euro qui va chercher un inconnu.

### 3.1 La sur-attribution, démontrée

Canonique § 5, plan média de P5. Somme des nouveaux clients attribués : 21 346 + 5 094 + 8 651 + 2 543 + 2 916 + 815 = **41 364**. Nouveaux clients réels (canonique § 2.4) : **37 324**.

```
Sur-attribution = 41 364 − 37 324 = 4 040 clients = 10,82 %  (canonique : 11 %)

nCAC apparent (moyenne des canaux) = 1 494 206 ÷ 41 364 = 36,12 €
nCAC réel                          = 1 494 206 ÷ 37 324 = 40,03 €
Sous-estimation : 3,91 € par client → 3,91 × 37 324 = 145 937 €/mois,
                                                     1 751 244 €/an
```

Quatre mille clients qui n'existent pas, et 1,75 M€ de coût d'acquisition annuel absent de tout tableau de bord de régie. Pas parce qu'une régie ment : six régies voient le même client, chacune a un point de contact vérifiable, chacune l'inscrit. C'est structurel.

### 3.2 Le nombre que tu dois calculer à la place

*Hypothèse de lecture :* chaque canal n'est crédité que de la première commande des clients qu'il s'attribue. L'AOV première commande n'est pas au canonique ; il se dérive de la contribution première commande (32,77 €, § 2.4) et de la marge brute.

```
AOV 1ʳᵉ cmd HT = 32,77 ÷ 0,6145 = 53,33 €   →   TTC = 64,00 €

Contrôle de cohérence du modèle :
CA nouveaux clients = 37 324 × 64,00 = 2 388 736 €
CA de réachat = 4 333 196 − 2 388 736 = 1 944 460 € sur 22 876 commandes
                                      = 85,00 € TTC par réachat
Vérif. contre la contribution de réachat canonique (§ 3, 43,53 €) :
   85,00 ÷ 1,20 × 0,6145 = 43,53 €                                 ✓
```

Le modèle tient au centime. Avec ces AOV, les six interfaces afficheront 41 364 × 64,00 = **2 647 360 €** de CA attribué contre 2 388 736 € réels — **3 103 488 € de CA fantôme par an**. Le vrai décomposé, lui :

```
MER acquisition = 2 388 736 ÷ 1 494 206 = 1,60
MER réachat     = 1 944 460 ÷ 1 494 206 = 1,30
MER blended     = 1,60 + 1,30           = 2,90    ✓ (canonique § 2.3)
```

C'est la phrase la plus importante de la section. **L'acquisition seule tourne à un MER de 1,60, sous le MER seuil de 1,95** (démontré § 4). Sans clients qui reviennent, NØRA perdrait de l'argent sur chaque euro de publicité : ce sont les 1,30 points apportés par la base installée qui rendent l'entreprise viable.

### 3.3 L'aMER, et la règle de pilotage

*Hypothèse de découpage :* Google Search et Shopping récoltent de la demande déjà créée, le reste est de la prospection.

```
aMER = 4 333 196 ÷ (1 494 206 − 164 363) = 4 333 196 ÷ 1 329 843 = 3,26
```

Le MER blended peut s'améliorer sans aucune acquisition nouvelle, en déplaçant du budget vers le retargeting et la marque — le tableau de bord s'améliore pendant que la machine s'arrête. **L'aMER attrape ce mouvement, le MER blended ne le voit pas.** MER qui monte et aMER qui baisse : tu récoltes ton stock de demande, et ce stock est fini.

D'où la règle, sans exception : **on ne pilote jamais sur la somme des ROAS plateforme.** Le MER blended décide du budget total, l'aMER surveille la dérive, les ROAS de plateforme n'arbitrent qu'à l'intérieur d'un même compte — là où le biais d'attribution est constant et s'annule. Module [E09](E09-mesure-et-incrementalite.md).

---

## 4. Le MER seuil

Le seul nombre qui transforme une intuition (« on dépense trop ? ») en comparaison de deux nombres. Notations : R = CA TTC, t = TVA, m = marge brute en % du CA HT, F = frais fixes, f = F ÷ CA HT.

### 4.1 Les deux seuils, démontrés

```
CM3 = m × CA HT − P = m × R ÷ (1 + t) − R ÷ MER

CM3 = 0
  ⇔  m × R ÷ (1 + t) = R ÷ MER
  ⇔  m ÷ (1 + t) = 1 ÷ MER          (division par R, avec R > 0)
  ⇔  MER = (1 + t) ÷ m

MER seuil (CM3 = 0) = (1 + TVA) ÷ taux de marge brute
Vérification P5 : 1,20 ÷ 0,6145 = 1,9528  →  1,95        ✓ (canonique § 2.3)
```

**R a disparu.** Le seuil de contribution ne dépend pas de ta taille, seulement de ta TVA et de ta marge brute — c'est ce qui le rend utilisable dès la première commande. Ajoute les frais fixes :

```
EBITDA = m × R ÷ (1 + t) − R ÷ MER − f × R ÷ (1 + t)

EBITDA = 0
  ⇔  (m − f) × R ÷ (1 + t) = R ÷ MER
  ⇔  MER = (1 + t) ÷ (m − f)

MER seuil (EBITDA = 0) = (1 + TVA) ÷ (marge brute − frais fixes en % du CA HT)

Vérification P5, frais fixes 360 000 € (canonique § 2.5) :
   f     = 360 000 ÷ 3 610 997 = 9,969 %
   m − f = 0,6145 − 0,09969    = 0,51481
   MER seuil = 1,20 ÷ 0,51481  = 2,3310  →  2,33            ✓
```

**Piège logique :** ici R n'a pas vraiment disparu, il est caché dans f, puisque F est fixe en euros — le seuil d'EBITDA n'est donc valable qu'au niveau de CA où tu l'as calculé. Si le CA HT de P5 baissait de 20 % à structure identique, f passerait à 12,46 % et le seuil à 1,20 ÷ (0,6145 − 0,1246) = **2,45**, marge de sécurité tombée de 24,4 % à 18,4 %. **En décroissance, le seuil monte pendant que le CA baisse : tu cours après une ligne qui recule.**

### 4.2 Lecture du canonique § 2.3, palier par palier

| Palier | MER réel | Seuil CM3 | Seuil EBITDA | Écart au seuil EBITDA |
| --- | ---: | ---: | ---: | ---: |
| P1 | 1,80 | 2,10 | 3,33 | **−46,0 %** |
| P2 | 2,20 | 2,04 | 2,71 | **−19,0 %** |
| P3 | 2,70 | 1,99 | 2,42 | +11,7 % |
| P4 | 2,80 | 1,99 | 2,35 | +19,0 % |
| P5 | 2,90 | 1,95 | 2,33 | +24,4 % |

Contrôle sur P1 : 1,20 ÷ 0,572 = 2,10 ✓ ; f = 6 500 ÷ 30 667 = 21,20 % ; 1,20 ÷ (0,572 − 0,212) = 3,33 ✓.

**Le seuil de contribution baisse à peine** : 2,10 → 1,95, soit 7 %, pour dix ans de croissance et 4,25 points de marge brute gagnés. Corollaire brutal : **l'échelle ne règle pas un problème de coefficient produit.** Si ton produit ne supporte pas un MER de 2,0, il ne le supportera pas mieux à 40 M€ de CA — cas [C01](../etudes-de-cas/C01-coefficient-insuffisant.md). **Le seuil d'EBITDA, lui, s'effondre** : 3,33 → 2,33, entièrement porté par les frais fixes qui passent de 21,20 % à 9,97 % du CA HT. L'effet joue une fois, entre P1 et P3 : ensuite les frais fixes ne descendent plus — 10,70 %, 9,41 %, puis 9,97 %, ils *remontent* en P5 avec le multi-pays. **L'économie d'échelle est un phénomène de démarrage, pas une rente perpétuelle.**

### 4.3 P1 et P2 tournent sous leur seuil : à quelle condition c'est rationnel

Le compte de résultat mensuel d'une marque en croissance rapide est trompeur : il additionne des cohortes jeunes, qui n'ont livré qu'une commande, et leur fait porter des frais fixes calibrés pour la taille future. **Le bon niveau d'analyse n'est pas le mois, c'est la cohorte.**

```
Condition de rendement :
   LTV 12 mois (contribution)  ≥  nCAC + frais fixes par nouveau client

P1 — canoniques § 3.1, § 2.4, § 2.5
   Fixes par nouveau client = 6 500 ÷ 768   =  8,46 €
   Coût total par client    = 26,62 + 8,46  = 35,08 €
   Surplus sur 12 mois      = 55,97 − 35,08 = +20,89 €  → cohorte : 16 044 €
   (le compte de résultat du mois affiche −9 403 €)

P2 : (28 000 ÷ 3 400 = 8,24 €) ; 70,70 − (30,78 + 8,24) = +31,68 € par client,
   soit 107 712 € par cohorte — pour un résultat mensuel de −19 838 €.
```

Les deux chiffres sont vrais : le premier décrit l'investissement, le second la trésorerie. Mais un investissement rentable peut te tuer si tu ne peux pas le financer, et la condition complète a trois clauses. **Rendement**, vérifié ci-dessus. **Trésorerie** : perte cumulée M1–M9 = 9 403 × 3 + 19 838 × 6 = **147 237 €**, plus le BFR (21 603 € en P1, 104 462 € en P2, canonique § 4), soit un **besoin de financement de l'ordre de 250 000 €** — sans lui, le pari n'est pas irrationnel, il est infaisable. **Mesure** : la LTV doit être *observée sur cohortes*, pas extrapolée — en P1 tu as trois mois de recul, tu ne peux pas savoir que la LTV 12 mois vaudra 55,97 €, tu paries. La discipline est de fixer à l'avance le taux de réachat à 90 jours en dessous duquel tu coupes.

> **À retenir :** perdre de l'argent en P1 et P2 est rationnel si — et seulement si — la LTV 12 mois couvre le nCAC *plus* les frais fixes par client, que tu as le cash pour tenir neuf mois de perte cumulée plus le BFR, et que tu as fixé à l'avance le seuil de réachat qui déclenche l'arrêt. Deux clauses sur trois ne suffisent pas.

---

## 5. Le CAC

### 5.1 nCAC contre CAC blended

```
nCAC        = TOUTE la dépense publicitaire ÷ nombre de NOUVEAUX clients
CAC blended = dépense publicitaire ÷ TOUS les clients ayant commandé

nCAC P5        = 1 494 206 ÷ 37 324 = 40,03 €     (canonique § 2.4)
CAC blended P5 = 1 494 206 ÷ 60 200 = 24,82 €     ×1,61 d'écart, −38 %
```

L'asymétrie du nCAC est voulue : toute la dépense au numérateur, seulement les nouveaux clients au dénominateur. Elle répond à « combien me coûte le fait de faire entrer un client de plus dans ma base ? », la seule question que le budget média doive trancher. Le CAC blended, lui, divise la dépense d'acquisition par un dénominateur incluant 22 876 commandes de clients déjà acquis. Pire, **il s'améliore mécaniquement quand la part de réachat monte** — il flatte au moment exact où l'acquisition se dégrade.

### 5.2 NØRA perd de l'argent sur la première commande. À tous les paliers.

Canonique § 2.4 :

| Palier | nCAC | Contribution 1ʳᵉ cmd | Marge 1ʳᵉ cmd | Contribution ÷ nCAC |
| --- | ---: | ---: | ---: | ---: |
| P1 | 26,62 € | 21,69 € | **−4,93 €** | 0,81 |
| P2 | 30,78 € | 26,95 € | **−3,83 €** | 0,88 |
| P3 | 33,18 € | 30,17 € | **−3,01 €** | 0,91 |
| P4 | 37,77 € | 31,71 € | **−6,06 €** | 0,84 |
| P5 | 40,03 € | 32,77 € | **−7,26 €** | 0,82 |

À P5 : 37 324 × 7,26 = **270 972 € perdus par mois** sur les premières commandes, 3 251 664 € par an. Le déficit se creuse de P3 à P5 parce que le nCAC monte de 33,18 € à 40,03 € (+20,6 %) — on achète du volume de plus en plus loin du cœur de cible — quand la contribution première commande ne gagne que 8,6 %. **C'est un choix, pas un accident.** Sa condition de validité :

```
contribution de réachat × réachats par client sur l'horizon
   ≥  (nCAC − contribution 1ʳᵉ commande)  +  frais fixes par nouveau client

P5 — canonique § 3 : contribution par réachat 43,53 €, 2,24 commandes cumulées
     à 12 mois donc 1,24 réachat. Fixes par client : 360 000 ÷ 37 324 = 9,65 €.
   Gauche = 43,53 × 1,24 = 53,98 €
   Droite = 7,26 + 9,65  = 16,91 €        53,98 ≥ 16,91  ✓  soit ×3,19
```

Le réachat pourrait être divisé par trois avant que le pari ne devienne perdant. En seuil actionnable : le minimum de réachats par client sur 12 mois est 16,91 ÷ 43,53 = **0,39**, soit 1,39 commande cumulée quand le modèle en produit 2,24. **Ton alerte se déclenche sous 1,39 commande cumulée par client à 12 mois** — un seuil dérivé, pas inventé.

### 5.3 Le CAC marginal

Le nCAC est une moyenne, et une moyenne ne décide de rien : la décision porte toujours sur la *prochaine* tranche de budget — **CAC marginal = dépense supplémentaire ÷ nouveaux clients supplémentaires**.

La courbe de CAC est croissante, toujours, et le canonique § 5 le prouve : dans le même mois, NØRA achète à 19,00 € sur Google Search et à 55,00 € sur Pinterest/Snap, ×2,9. Si le CAC était constant on mettrait tout le budget sur Google Search — il sature à 8 651 clients par mois. **Le CAC marginal de NØRA à P5 est donc de l'ordre de 55 €, pas 40,03 €**, et toute hausse de budget se juge contre 55 €.

```
LTV 12 m ÷ CAC marginal = 86,75 ÷ 55,00 = 1,58      (canonique § 3)

Payback marginal, interpolé entre 3 mois (47,57 €) et 6 mois (64,11 €) :
   (55,00 − 47,57) ÷ (64,11 − 47,57) = 0,449  →  3 + 0,449 × 3 = 4,35 mois
```

Au-dessus de 1,5, la tranche reste créatrice de valeur — tout juste. Mais **le client marginal met 2,4 fois plus longtemps à se rembourser que le client moyen** (4,35 mois contre 1,8). C'est là, et pas dans le ratio LTV/CAC, que se trouve la vraie limite de croissance.

---

## 6. LTV, payback et le ratio

### 6.1 La LTV en chiffre d'affaires est le mensonge le plus répandu du métier

Canonique § 3, cohorte P5 à 12 mois : CA cumulé TTC par client 169,40 €, soit 4,23 fois le nCAC de 40,03 € ; LTV en contribution 86,75 €, soit 2,17 fois le nCAC.

```
169,40 € TTC
÷ 1,20                    = 141,17 €   ← on retire la TVA
× 61,45 % de marge brute  =  86,75 €   ← on retire COGS, logistique, PSP,
                                          retours, remises
Facteur d'écart : 169,40 ÷ 86,75 = 1,953  ≈  ×2
```

Celui qui présente 169,40 € comme sa LTV annonce un ratio de 4,23 quand le vrai est 2,17 : il croit avoir une marge de sécurité de ×4, il a ×2. L'erreur est *systématiquement dans le même sens* — personne ne se trompe jamais en sous-estimant sa LTV — donc le biais ne s'annule pas dans la moyenne des décisions, il s'accumule. La suite est mécanique : il voit 4,23, double son budget, le CAC marginal monte à 55 €, il calcule 169,40 ÷ 55 = 3,08 et continue, alors que la vérité est 86,75 ÷ 55 = 1,58, c'est-à-dire la zone de réparation. **Règle sans exception : une LTV se calcule en marge de contribution.** Si quelqu'un te donne une LTV, demande « en CA ou en contribution ? » — s'il hésite, c'est du CA.

### 6.2 L'horizon : 12 mois, pas 36

| Horizon (canonique § 3) | 1 m | 3 m | 6 m | **12 m** | 18 m | 24 m | 36 m |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| LTV contribution | 35,38 € | 47,57 € | 64,11 € | **86,75 €** | 105,03 € | 118,96 € | 138,11 € |
| LTV / CAC | 0,88 | 1,19 | 1,60 | **2,17** | 2,62 | 2,97 | 3,45 |

Entre 12 et 36 mois la contribution gagne encore 51,36 €, soit +59 % : un dirigeant tenté annoncera 3,45 au lieu de 2,17. Trois raisons de refuser. **Tu ne l'as pas observé** : une LTV 36 mois mesurée demande trois ans de cohortes suivies, et une marque qui atteint P5 en M31–M40 n'a de cohortes matures que sur ses premiers mois, acquises en P1, sur un mix qui n'a plus rien à voir. **Le biais du survivant joue dans un seul sens** : les clients encore observables à 36 mois sont ceux qui sont restés. **Et ce n'est pas ta décision** : financer 36 mois d'acquisition avant le premier euro récupéré coûte du cash — à P5, +100 000 € de CA mensuel immobilisent 52 263 € (canonique § 4). **Une entreprise ne meurt pas d'être non rentable, elle meurt de manquer de trésorerie.** Position du cursus : **LTV 12 mois pour toute décision d'investissement, 24 mois comme borne haute de scénario, jamais au-delà** ([E08](E08-retention-et-ltv.md)).

### 6.3 Le payback, et pourquoi il prime sur le ratio

```
Payback = temps pour que la contribution cumulée d'un client rembourse le nCAC

Reconstruction du payback P5 : on cherche l'horizon où la LTV atteint 40,03 €.
   Fraction = (40,03 − 35,38) ÷ (47,57 − 35,38) = 4,65 ÷ 12,19 = 0,3815
   Payback  = 1 + 0,3815 × 2 = 1,76  →  ≈ 1,8 mois       ✓ (canonique § 3)
```

Canonique § 3.1 : le payback vaut 1,8 mois en P1, **1,3 en P2, 1,1 en P3**, puis remonte à 1,6 en P4 et 1,8 en P5 — il se dégrade exactement quand le ratio LTV/CAC se dégrade (2,41 en P3, 2,17 en P5), parce que P4 et P5 achètent du volume plus cher et plus loin.

Le ratio te dit *si* un client vaut son coût ; le payback te dit *quand*. Une entreprise ne fait pas faillite parce que ses clients ne valent pas leur coût, mais parce qu'elle a payé ce coût en janvier et touchera la valeur en novembre. Canonique § 4 : à P5, 364 752 € d'EBITDA mensuel ÷ 52 263 € de cash immobilisé par tranche de 100 000 € de CA donnent 6,979, soit **697 917 € de CA mensuel supplémentaire finançable sans apport** — **16,1 % de croissance mensuelle autofinançable**. L'expérience de pensée qui tranche : une marque au **même** ratio de 2,17, mais avec un payback de 9 mois au lieu de 1,8 — réachat lent, consommable à cycle long. Elle achète la même valeur au même prix.

```
Avance de trésorerie à 1,8 mois = 1 494 206 × 1,8 =  2 689 571 €
Avance de trésorerie à 9,0 mois = 1 494 206 × 9,0 = 13 447 854 €
Écart                                             = 10 758 283 €
```

Dix millions et demi d'euros de trésorerie supplémentaire, à ratio LTV/CAC rigoureusement identique. **Le ratio ne l'a pas vu. Le payback, oui.** D'où les repères : **sur la première commande** si tu es autofinancé sans réserve, **≤ 3 mois** avec réserve, **≤ 6 mois** en dette, **≤ 12 mois** en fonds propres levés. NØRA est à 1,8 mois sur le client moyen, mais à 4,35 mois sur le marginal (§ 5.3) — c'est ce nombre-là qui borne la vitesse ([E10](E10-cash-et-operations.md)).

### 6.4 Le ratio LTV/CAC et son interprétation contre-intuitive

| Ratio LTV 12 m / nCAC | Lecture | Action |
| --- | --- | --- |
| **< 1** | Chaque client détruit de la valeur | Coupe l'acquisition aujourd'hui |
| **1 à 1,5** | Rentable à l'unité, ne couvre pas les frais fixes | **On répare**, on ne scale pas |
| **1,5 à 2** | Zone de survie sous surveillance | On travaille l'AOV et le réachat |
| **2 à 4** | Zone saine | **On accélère**, jusqu'à la limite du payback |
| **> 5** | **Tu sous-investis** | Augmente le budget jusqu'à faire baisser le ratio |

La dernière ligne n'est pas intuitive, et c'est la plus rentable. *Hypothèse :* une marque à LTV 12 mois de 86,75 € en contribution — celle de P5, canonique § 3 — envisage son budget par tranches de 100 000 €. La courbe de CAC marginal ci-dessous est **modélisée** ; sa forme croissante, elle, est établie (§ 5.3).

| Tranche de 100 000 € | 1ʳᵉ | 2ᵉ | 3ᵉ | 4ᵉ | 5ᵉ | 6ᵉ | 7ᵉ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Clients de la tranche | 5 000 | 3 571 | 2 632 | 2 041 | 1 613 | 1 266 | 990 |
| CAC marginal | 20,00 € | 28,00 € | 38,00 € | 49,00 € | 62,00 € | 79,00 € | 101,00 € |
| **Résultat 12 m** | **+333 750** | **+209 784** | **+128 326** | **+77 056** | **+39 928** | **+9 826** | **−14 117** |

Chaque tranche crée de la valeur tant que son CAC marginal reste sous 86,75 €. La sixième (79,00 €) passe, la septième (101,00 €) détruit : **l'optimum est à six tranches, 600 000 € de budget.**

```
A — s'arrête à une tranche, parce que son ratio est superbe
   100 000 € / 5 000 clients / CAC moyen 20,00 € / ratio 4,34 « excellent »
   Contribution = 5 000 × 86,75 − 100 000 = 333 750 €

B — va jusqu'à l'optimum
   600 000 € / 16 123 clients / CAC moyen 37,22 € / ratio 2,33 « moyen »
   Contribution = 16 123 × 86,75 − 600 000 = 798 670 €

798 670 ÷ 333 750 = ×2,39
```

**Le dirigeant au « mauvais » ratio de 2,33 gagne 2,39 fois plus de contribution que celui au « bon » ratio de 4,34.** Le ratio de A est élevé précisément *parce qu'il n'a acheté que les clients les moins chers* : il a laissé 464 920 € de contribution sur la table pour préserver un indicateur. La règle porte sur le marginal, jamais sur la moyenne : **continue d'acheter tant que le CAC marginal reste inférieur à la LTV 12 mois en contribution.** Le ratio moyen ne sert qu'à détecter qu'on est trop loin à gauche de la courbe — **un ratio supérieur à 5 est une alerte au même titre qu'un ratio inférieur à 1,5** : dans un cas tu détruis de la valeur, dans l'autre tu refuses d'en créer.

Deux garde-fous. Le payback : à 79 € de CAC marginal, l'interpolation entre 6 mois (64,11 €) et 12 mois (86,75 €) donne **9,9 mois** — une marque autofinancée s'arrêtera bien avant la sixième tranche, non parce que c'est non rentable mais parce que c'est infinançable. Et l'incrémentalité : la courbe suppose que les clients supplémentaires le sont réellement, ce que l'attribution ne sait pas prouver ([E09](E09-mesure-et-incrementalite.md)).

> **À retenir :** le CAC moyen raconte le passé, le CAC marginal décide du futur. Compare le CAC marginal à la LTV 12 mois pour savoir si tu *peux*, et le payback marginal à ta réserve de trésorerie pour savoir si tu peux *te le permettre*.

---

## 7. Quel levier vaut le plus, et où est ton point mort

### 7.1 Le tableau de sensibilité

Canonique § 7 : effet sur l'EBITDA annuel d'une amélioration de 10 % de chaque levier au palier P5, toutes choses égales par ailleurs. Référence : 4 377 023 €.

| Levier | Gain d'EBITDA annuel | En % de l'EBITDA |
| --- | ---: | ---: |
| +10 % de panier moyen (AOV, à commandes constantes) | 3 139 401 € | **71,7 %** |
| +10 % de taux de conversion (à budget pub constant) | 2 662 749 € | 60,8 % |
| −10 % de CAC à volume constant | 1 793 047 € | 41,0 % |
| +10 % de commandes de réachat | 1 194 871 € | 27,3 % |
| −10 % de COGS | 628 313 € | 14,4 % |
| −1 point de taux de retour / SAV | 433 320 € | 9,9 % |
| −10 % de frais fixes | 432 000 € | **9,9 %** |

Rapport entre le premier et le dernier levier : 3 139 401 ÷ 432 000 = **×7,3**. Et c'est sur le dernier que la plupart des dirigeants passent leurs journées.

### 7.2 Pourquoi le panier moyen bat la conversion

Les deux leviers ajoutent le même chiffre d'affaires : +10 % de CA HT, soit +361 100 €. Ils ne rapportent pas la même chose, et l'explication tient en une phrase : **la logistique est un coût par commande, pas un coût par euro.** +10 % de conversion à budget constant, c'est +10 % de commandes au même panier : tous les coûts variables restent au même pourcentage du CA — la logistique aussi, puisqu'il y a 10 % de colis en plus — donc la marge brute reste à 61,45 %.

```
Gain annuel = 3 610 997 × 0,10 × 0,6145 × 12 = 2 662 749 €  ✓ canonique § 7
```

+10 % d'AOV **à commandes constantes** : toujours 60 200 commandes, chacune valant 10 % de plus. Chaque poste se comporte alors selon sa nature réelle.

```
CA HT 3 610 997 € → 3 972 097 € (+361 100 €). Commandes : 60 200, INCHANGÉ.

COGS        proportionnel au CA   523 595 → 575 954 €   (+52 359 €)
Logistique  FIXE PAR COMMANDE     397 210 → 397 210 €   (+0 €)
PSP         proportionnel          55 970 →  61 568 €   (+5 598 €)
Retours     proportionnel         126 385 → 139 023 €   (+12 638 €)
Remises     proportionnel         288 880 → 317 768 €   (+28 888 €)

Coûts variables = 1 491 523 €  →  marge brute 3 972 097 − 1 491 523
                               = 2 480 574 € contre 2 218 957 €
Gain mensuel 261 617 €  →  annuel 3 139 405 €   ✓ canonique 3 139 401 €

Écart entre les deux leviers :
3 139 405 − 2 662 749 = 476 656 €/an = 10 % de la logistique annuelle
```

**L'intégralité de la supériorité du panier moyen sur la conversion est la logistique qui ne suit pas.** Rien d'autre. Le taux de marge brute passe de 61,45 % à 2 480 574 ÷ 3 972 097 = **62,45 %** : un point gagné sans toucher à un contrat fournisseur. Généralisation : **tout coût fixe par commande s'allège relativement quand l'AOV monte**, et c'est la raison arithmétique pour laquelle P5+ fonctionne (canonique § 8) — +7 % d'AOV, −7 % de commandes, même CA, +4,5 points de marge brute ([E03](E03-offre-et-prix.md), [E12](E12-marque-et-actif.md)).

### 7.3 Pourquoi COGS et frais fixes sont les leviers les plus faibles

Ce sont les deux plus petites lignes de la cascade, et on n'en retire que 10 %.

```
COGS        = 14,50 % du CA HT  →  −10 % = 1,45 point de CA HT
Frais fixes =  9,97 % du CA HT  →  −10 % = 1,00 point de CA HT
AOV         = +7,24 points de CA HT d'EBITDA  (261 617 ÷ 3 610 997)

Vérifications du canonique § 7 :
COGS        : 3 610 997 × 0,145 × 0,10 × 12 = 628 314 €   ✓ canonique 628 313 €
Frais fixes : 360 000 × 0,10 × 12           = 432 000 €   ✓ canonique 432 000 €
Retours     : 3 610 997 × 0,01 × 12         = 433 320 €   ✓ canonique 433 320 €
```

Alors pourquoi les dirigeants y passent-ils leurs journées ? Parce que ce sont les seuls leviers entièrement sous leur contrôle — renégocier un fournisseur est unilatéral, augmenter l'AOV demande de changer l'offre et le marché a un droit de veto ; parce que le gain est immédiat et certain, là où une hausse d'AOV se teste, échoue une fois sur deux et met un trimestre à se stabiliser ; et parce que couper des coûts a l'air d'être du management. Ce qui n'annule pas le ×7,3 : **la part du temps consacrée à un levier ne doit pas dépasser sa part dans ce tableau.**

### 7.4 Le point mort en commandes par jour

Un seuil de rentabilité en euros ne parle à personne dans une équipe ; en commandes par jour, tout le monde le comprend et il se vérifie chaque matin sur un écran. Méthode, à mix constant :

```
CM3 par commande      = marge brute par commande − dépense pub par commande
Point mort (cmd/mois) = frais fixes mensuels ÷ CM3 par commande
Point mort (cmd/jour) = point mort mensuel ÷ 30,33

30,33 est la convention du modèle : un mois vaut 52 ÷ 12 = 4,3333 semaines.
C'est ce qui rend le canonique § 9 exact (60 200 ÷ 30,33 = 1 985 cmd/jour).

Déroulé de P5 :
   Marge brute par commande = 2 218 957 ÷ 60 200 = 36,86 €
   Pub par commande         = 1 494 206 ÷ 60 200 = 24,82 €
   CM3 par commande         = 36,86 − 24,82      = 12,04 €
   Contrôle : 60 200 × 12,04 = 724 808 € ≈ 724 752 € de CM3 canonique   ✓
   Point mort = 360 000 ÷ 12,04 = 29 900 cmd/mois ÷ 30,33 = 986 cmd/jour
```

| Palier | Marge brute /cmd | Pub /cmd | **CM3 /cmd** | Point mort /mois | **/jour** | Réel /jour | Sécurité |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| P1 | 21,93 € | 25,56 € | **−3,63 €** | — | **jamais** | 26 | — |
| P2 | 28,20 € | 26,16 € | **+2,04 €** | 13 725 | **452** | 132 | **−70,8 %** |
| P3 | 32,89 € | 24,22 € | **+8,67 €** | 12 111 | **399** | 593 | +48,6 % |
| P4 | 35,13 € | 24,93 € | **+10,20 €** | 22 549 | **743** | 1 385 | +86,4 % |
| P5 | 36,86 € | 24,82 € | **+12,04 €** | 29 900 | **986** | 1 985 | +101,3 % |

Contrôles contre le CM3 du canonique § 2.2 : P1, 800 × (−3,63) = −2 904 € contre −2 903 € ✓ ; P2, 4 000 × 2,04 = 8 160 € contre 8 162 € ✓ ; P3, 18 000 × 8,67 = 156 060 € contre 156 033 € ✓ ; P4, 42 000 × 10,20 = 428 400 € contre 428 572 € ✓ — arrondis au centime sur la contribution unitaire.

**P1 n'a pas de point mort** : sa contribution après publicité est négative, −3,63 € par commande, donc vendre plus creuse la perte. C'est la situation la plus dangereuse du métier, parce qu'elle ressemble exactement à un problème de volume sans en être un — le seul remède est de remonter le MER au-dessus de 2,10, en changeant le prix, le produit ou la publicité, pas la quantité. **P2 est à 29 % de son point mort** : 132 commandes par jour contre 452, soit ×3,4 de volume à structure inchangée. Faisable — P3 en fait 593 — mais P2 n'est pas un palier stationnaire : on y transite, on n'y campe pas. **De P3 à P5, la marge de sécurité double**, et c'est cette réserve qui autorise à parier sur de nouveaux marchés ([E13](E13-risque-de-ruine.md)).

---

## 8. Les erreurs qui coûtent cher

**1 — Compter la publicité en % du CA TTC.** Un MER de 2,90 devient « 34,5 % du CA » ; la réalité est 41,4 %. Coût : 1 494 206 ÷ 6 = 249 034 €/mois, **2 988 412 €/an** à P5, soit 68,3 % de l'EBITDA (§ 2). Antidote : (1 + TVA) ÷ MER écrit en dur dans le tableau de bord.

**2 — Présenter la LTV en chiffre d'affaires.** 169,40 € au lieu de 86,75 € à 12 mois : **facteur 1,95** (§ 6.1). Le ratio annoncé passe de 2,17 à 4,23, et le dirigeant accélère.

**3 — Extrapoler la LTV à 36 mois pour justifier un CAC.** 138,11 € au lieu de 86,75 €, soit +59 % sortis d'un modèle et non d'une observation (§ 6.2). Le coût est en trésorerie : à payback 9 mois, l'avance sur la dépense média de P5 passe de 2 689 571 € à 13 447 854 €.

**4 — Présenter un CAC blended comme un nCAC.** 24,82 € au lieu de 40,03 € : **38 % de sous-estimation** (§ 5.1), par un indicateur qui s'améliore quand la part de réachat monte.

**5 — Ne pas compter les remises comme un coût variable.** De 3,0 % à 8,0 % du CA HT entre P1 et P5 : 5 points, **180 550 €/mois, 2 166 600 €/an** à P5 (§ 1.3). Antidote : ligne visible, propriétaire nommé, plafond mensuel décidé à l'avance.

**6 — Ne pas provisionner les retours.** Ils arrivent 15 à 45 jours après la vente, et une marque en croissance rapide les sous-estime structurellement : le dénominateur du mois a explosé pendant que le numérateur reflète les ventes du mois précédent. Un point d'erreur à P5 : **433 320 €/an**. Antidote : taux de retour par cohorte de commandes, pas par mois calendaire.

**7 — Croire que le MER seuil est une constante.** Il bouge dès que la marge brute bouge, et le seuil d'EBITDA bouge en plus avec le niveau de CA, puisque f = frais fixes ÷ CA HT (§ 4.1). Un taux de retour passant de 3,5 % à 5,5 % le porte de 2,33 à 2,43 (exercice 2) ; un CA en baisse de 20 % le porte à 2,45. Antidote : le recalculer chaque mois par la formule, jamais de mémoire.

**8 — Piloter au ROAS de plateforme, ou s'arrêter parce que le ratio est beau.** À P5, 41 364 clients attribués contre 37 324 réels, et **3 103 488 €/an de CA fantôme** (§ 3.2). Symétriquement, un ratio de 4,34 sur une tranche produit 333 750 € de contribution là où un ratio de 2,33 sur six tranches en produit 798 670 € (§ 6.4). Antidote : MER blended pour le budget total, CAC marginal pour la tranche suivante.

---

## 9. Ce que ce module ne dit pas

**Ce module suppose l'attribution résolue. Elle ne l'est pas.** La section 5 traite le nCAC comme un nombre connu : 1 494 206 € ÷ 37 324 nouveaux clients. Le dénominateur est solide — un décompte de comptes créés dans ta base — et le numérateur aussi — des factures. Mais savoir *lesquels* de ces clients existent **à cause de** la dépense reste entier. Module [E09](E09-mesure-et-incrementalite.md).

**La marge de contribution ne dit rien de l'incrémentalité.** C'est la limite la plus sérieuse du module. Le § 6.4 suppose que les clients supplémentaires de chaque tranche sont réellement supplémentaires. Si 30 % d'entre eux seraient venus de toute façon, le CAC marginal vrai vaut 1 ÷ 0,7 = **1,43 fois** l'observé, et l'optimum se déplace de plusieurs tranches vers la gauche. Aucune arithmétique de marge ne détecte ça ; seule l'expérimentation le peut — cas [C06](../etudes-de-cas/C06-test-incrementalite.md).

**Le CAC ne mesure pas l'effet mémoriel de long terme, et Byron Sharp a raison de le dire.** Le [module 10](../../modules/10-sharp-distinctivite.md) du cursus racine soutient que l'essentiel de la croissance vient de la disponibilité mentale accumulée chez des acheteurs légers qui n'achèteront pas ce trimestre — et qu'une publicité dont l'effet se manifeste dans dix-huit mois est comptée comme un échec par un tableau de bord à fenêtre de sept jours. La critique n'est pas réfutable par les chiffres de ce module : elle porte sur ce qu'ils ne mesurent pas. Une part des 1 494 206 € mensuels de la cascade P5 construit une mémoire qui produira des ventes hors de toute fenêtre d'attribution, et le nCAC de 40,03 € l'ignore. Position du cursus : **le nCAC et le MER seuil sont des instruments de contrainte budgétaire, pas des mesures de la valeur créée par la publicité.** Module [E12](E12-marque-et-actif.md).

**Trois angles morts techniques.** Les frais fixes sont fixes *par palier*, pas par mois : +56 % entre P4 et P5 (canonique § 2.5), par marches. Le module ignore la saisonnalité, alors que le Black Friday déforme simultanément AOV, remise, MER et taux de retour ([C09](../etudes-de-cas/C09-piege-du-black-friday.md)). Et il ne traite la trésorerie qu'au travers du payback, alors que le BFR de P5 atteint 2 264 655 € (canonique § 4) — module [E10](E10-cash-et-operations.md). Enfin, NØRA est fictive : la cohérence au centime de son modèle est une propriété du modèle, pas du monde.

---

## 10. Le tableau de bord du module

Six indicateurs. Pas sept. Si tu ne peux en tenir que trois à jour, garde les trois premiers.

| Indicateur | Fréquence | Seuil d'alerte | Réf. P5 |
| --- | --- | --- | ---: |
| **Marge brute (CM2)** | Hebdo. | **−1,5 point sur 4 semaines glissantes** | 61,45 % |
| **MER blended** (CA TTC ÷ pub) | **Quotidienne**, 7 j glissants | **Sous le seuil EBITDA**, ou 2 jours d'affilée sous le seuil CM3 | 2,90 |
| **MER seuil EBITDA** (1 + TVA) ÷ (m − f) | Mensuelle, **recalculé** | **+0,10 en un mois** | 2,33 |
| **nCAC** (pub totale ÷ nouveaux clients) | Hebdo. | **+15 % sur 4 semaines** sans hausse de LTV | 40,03 € |
| **LTV 12 m / nCAC** (en contribution) | Mensuelle | **< 1,5 → on répare. > 5 → on sous-investit** | 2,17 |
| **Payback marginal** (sur le CAC marginal) | Mensuelle | **> 3 mois si autofinancé, > 6 si endetté** | 4,35 mois |

Trois règles d'usage valent autant que le tableau. **Le MER seuil se recalcule, il ne se mémorise pas** : c'est le seul indicateur dont la valeur bouge sans qu'aucune décision n'ait été prise. **Les indicateurs 2 et 3 se lisent ensemble** : le nombre à afficher est leur écart, +24,4 % à P5. **Le payback se mesure sur le CAC marginal** : le payback moyen rassure à 1,8 mois, le marginal est à 4,35 mois et c'est lui qui borne ta vitesse. Aucun ROAS de plateforme n'y figure, et ce n'est pas un oubli.

---

## 11. Exercices

Formulaire vierge : [`E01-rendu.md`](../exercices/E01-rendu.md) ; corrigé : [`E01-corrige.md`](../exercices/E01-corrige.md). Fais les calculs à la main avant de l'ouvrir.

**Exercice 1 — Recalcule les deux MER seuils de P3** (réponse numérique unique). Données autorisées, et elles seules : canoniques § 2.1, § 2.2, TVA 20 %. Calcule (1) le taux de marge brute de P3 à partir des cinq postes de coût variable, deux décimales, (2) le MER seuil de contribution, (3) les frais fixes en % du CA HT, (4) le MER seuil d'EBITDA, (5) la marge de sécurité du MER réel de 2,70, à retrouver au canonique § 2.3, et (6) de combien de points la marge brute pourrait baisser avant qu'un MER de 2,70 ne suffise plus à l'équilibre d'EBITDA. *Contrôle : tu dois retrouver 1,99 et 2,42 exactement.*

**Exercice 2 — L'EBITDA de P5 si le taux de retour passe de 3,5 % à 5,5 %** (réponse numérique unique). Canoniques § 2.1 et § 2.2 ; tout le reste est inchangé — même CA, même dépense publicitaire, mêmes frais fixes. Calcule (1) le nouveau taux de marge brute, (2) la nouvelle marge brute mensuelle, (3) le nouveau CM3, (4) le nouvel EBITDA mensuel et en % du CA HT, (5) la perte d'EBITDA annuelle, vérifiée par la voie courte CA HT × 2 points × 12, (6) le nouveau MER seuil d'EBITDA et la marge de sécurité qui reste contre 2,90, et (7) le taux de retour auquel l'EBITDA de P5 devient nul. *Contrôle : la perte annuelle doit être proche de 866 640 € et la marge de sécurité tomber sous 20 %.*

**Exercice 3 — Ta cascade des marges** (tes chiffres). Reconstruis sur tes 90 derniers jours la cascade complète du § 1.1, en euros et en % du CA HT, avec les remises en ligne séparée, les retours comptés par cohorte de commandes, et une ligne publicité incluant production créative et honoraires d'agence. *Grille de lecture : sous 50 % de marge brute, ton MER seuil de contribution vaut au moins 1,20 ÷ 0,50 = 2,40 — un niveau que très peu de marques DTC tiennent durablement en prospection. Ce n'est pas un problème de publicité, c'est un problème de prix ou de coût produit ([E02](E02-marche-et-produit.md), [E03](E03-offre-et-prix.md)).*

**Exercice 4 — Ton tableau de sensibilité** (tes chiffres). Reproduis les sept lignes du canonique § 7 avec tes nombres, en traitant chaque poste selon sa nature réelle comme au § 7.2 : proportionnel au CA, ou fixe par commande. En regard, écris les heures de direction que chaque levier a consommées le mois dernier. *Grille de lecture : la part du temps consacrée à un levier devrait être du même ordre que sa part dans le total des gains ; un écart supérieur à ×3 est un problème d'allocation d'attention, et ce sont presque toujours le COGS et les frais fixes qui sur-consomment.*

**Exercice 5 — Tes deux seuils et ton point mort** (tes chiffres). Calcule (1) ton MER seuil de contribution, (2) ton MER seuil d'EBITDA avec le niveau de CA HT auquel il est valable, (3) ton CM3 par commande puis ton point mort en commandes par jour (§ 7.4), et écris (4) trois nombres sur un post-it collé à ton écran : point mort en commandes/jour, MER seuil d'EBITDA, MER des 7 derniers jours. *Grille de lecture : un CM3 par commande négatif te met en situation P1, et aucun volume ne t'en sortira. Un volume réel sous 1,5 fois ton point mort ne te laisse aucune réserve pour absorber un incident — hausse de CPM, rupture de stock, compte publicitaire suspendu ([C10](../etudes-de-cas/C10-compte-publicitaire-banni.md)).*

**Exercice 6 — Décision : la septième tranche de budget.** Ta marque ressemble à NØRA au palier P5 : LTV 12 mois 86,75 € en contribution, payback moyen 1,8 mois, MER blended 2,90, MER seuil d'EBITDA 2,33. Ton directeur de l'acquisition propose 100 000 € de budget mensuel supplémentaire sur un nouveau canal ; son test sur trois semaines donne **1 266 nouveaux clients pour 100 000 €**, soit un CAC marginal de 79,00 €. Ta trésorerie disponible est de 400 000 €, et ton BFR augmente de 52 263 € par tranche de 100 000 € de CA mensuel (canonique § 4). **Option A :** valider. **Option B :** refuser et réallouer sur les canaux existants. Tranche, et justifie par des nombres : ton raisonnement doit contenir le résultat sur 12 mois de la tranche, son payback marginal, et le besoin de trésorerie qu'elle crée avant le premier euro récupéré. *Le corrigé donne la réponse, la condition exacte sous laquelle l'autre option devient la bonne, et le seul test qui trancherait pour de bon — celui du module [E09](E09-mesure-et-incrementalite.md).*

---

*Fin du module E01. Suite : [E02 — Choisir le terrain : marché, catégorie, produit](E02-marche-et-produit.md). E01 t'a donné les six nombres ; E02 et [E03](E03-offre-et-prix.md) déterminent lesquels tu peux atteindre, parce que la marge brute et l'AOV se décident au moment du choix du produit et du prix — pas après.*
