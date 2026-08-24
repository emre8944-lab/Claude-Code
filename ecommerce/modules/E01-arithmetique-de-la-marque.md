# Module E01 — L'arithmétique de la marque

> **Prérequis :** [E00](E00-cadrage.md). En parallèle : [module 13](../../modules/13-unit-economics.md) du cursus racine.
> **Objet :** construire, à partir de ta banque et de ton back-office, les six nombres qui décident si ta marque vit — et démontrer, plutôt qu'affirmer, la décision que chacun impose.
> **Temps de travail :** ~6 h (lecture + exercices, calculatrice obligatoire)

---

## 0. Pourquoi ce module existe

Il existe six nombres qui décident si une marque de e-commerce vit. Tout le reste — la charte graphique, le thème du site, le débat sur l'outil d'e-mailing — est du commentaire.

```
1. La marge brute (CM2) en % du CA HT
2. Le MER, et son seuil
3. Le nCAC — coût d'acquisition d'un NOUVEAU client
4. La LTV à 12 mois, en marge de contribution
5. Le payback du CAC, en mois
6. Les frais fixes en % du CA HT
```

Ces six-là suffisent à écrire le compte de résultat, à décider si tu peux augmenter le budget média demain matin, et à dire à quel moment tu meurs. Aucun n'est difficile à calculer. C'est pour ça que presque personne ne les vérifie.

Et voilà l'observation qui justifie ce module : **une marque sur deux en calcule au moins deux faux**, toujours les deux mêmes. Le premier est la part de la publicité dans le chiffre d'affaires, parce que le MER se lit sur du TTC et que la marge se calcule sur du HT — section 2, l'erreur vaut 2 988 412 € par an au palier P5 de NØRA. Le second est la LTV, calculée en chiffre d'affaires au lieu de marge de contribution — section 6, l'erreur est d'un facteur 1,95.

Une marque qui se trompe sur ces deux-là se croit rentable de sept points et riche du double. Elle scale. Elle meurt.

---

## 1. La cascade des marges

### 1.1 La définition, sans ambiguïté

Dire « ma marge » sans préciser laquelle, c'est dire « ma vitesse » sans dire si c'est en ville ou sur autoroute. Il y a quatre marges, elles ne servent pas à la même chose et n'ont pas le même responsable.

```
CA TTC        prix payé par le client, TVA incluse
   ÷ (1 + TVA)
CA HT         chiffre d'affaires comptable — TOUTE marge se calcule là-dessus
   − COGS                       coût marchandise rendu entrepôt
CM1           marge sur coût marchandise
   − logistique                 préparation, colis, transport, retour physique
   − PSP                        frais du prestataire de paiement
   − retours / SAV              remboursements, gestes commerciaux, casse
   − remises                    codes promo, ventes flash, codes créateurs
CM2 = MARGE BRUTE — ce qui reste pour payer la publicité et la structure
   − publicité                  média + production créative + honoraires d'agence
CM3           marge de contribution après acquisition
   − frais fixes                salaires, loyers, outils, honoraires
EBITDA        le résultat d'exploitation
```

Deux conventions à graver, parce que les violer produit des erreurs à six chiffres. **La TVA n'est pas ton argent** : un CA TTC de 4 333 196 € est un CA de 3 610 997 € et une dette fiscale de 722 199 €. **Une remise est un coût variable, pas une baisse de chiffre d'affaires** : comptablement tu peux la traiter des deux façons, mais en pilotage tu la mets en coût, ligne visible, avec un responsable. Sinon elle se dissout dans le prix moyen et personne ne la défend jamais.

### 1.2 La cascade complète du palier P5

Chiffres canoniques § 2 (volumes), § 2.1 (structure de coût), § 2.2 (compte de résultat). P5 : 60 200 commandes/mois, AOV mixte 71,98 € TTC, sept marchés, TVA moyenne pondérée 20 %.

| Étage | Montant mensuel | % du CA HT | Calcul |
| --- | ---: | ---: | --- |
| CA TTC | 4 333 196 € | 120,00 % | 60 200 × 71,98 € |
| TVA | −722 199 € | −20,00 % | 4 333 196 × 0,20 ÷ 1,20 |
| **CA HT** | **3 610 997 €** | **100,00 %** | 4 333 196 ÷ 1,20 |
| COGS | −523 595 € | −14,50 % | 3 610 997 × 0,145 |
| **CM1** | **3 087 402 €** | **85,50 %** | |
| Logistique | −397 210 € | −11,00 % | × 0,110 |
| PSP | −55 970 € | −1,55 % | × 0,0155 |
| Retours / SAV | −126 385 € | −3,50 % | × 0,035 |
| Remises | −288 880 € | −8,00 % | × 0,080 |
| **CM2 — marge brute** | **2 218 957 €** | **61,45 %** | canonique § 2.2 |
| Publicité | −1 494 206 € | −41,38 % | canonique § 2.2 |
| **CM3** | **724 751 €** | **20,07 %** | 2 218 957 − 1 494 206 |
| Frais fixes | −360 000 € | −9,97 % | canonique § 2.5 |
| **EBITDA** | **364 751 €** | **10,10 %** | canonique § 2.2 : 364 752 € |

Somme des coûts variables : 14,50 + 11,00 + 1,55 + 3,50 + 8,00 = 38,55 %. Marge brute = 100 − 38,55 = **61,45 %**. Le canonique § 2.1 affiche 61,5 % : même nombre, arrondi au dixième. **J'utilise 61,45 % partout**, parce que 0,05 point sur 3 610 997 € vaut 21 660 € par an et qu'on ne jette pas 21 660 € pour économiser deux décimales. L'euro d'écart sur le CM3 et l'EBITDA vient de là ; je conserve les valeurs canoniques comme référence.

### 1.3 Ce que chaque étage décide, et qui en répond

| Étage | Ce qu'il sert à décider | Responsable | Revue |
| --- | --- | --- | --- |
| CA HT | Rien. C'est une taille, pas une performance. | Direction | Mensuelle |
| **CM1** | Le prix tient-il ? Renégocier, changer de conditionnement, relocaliser ? | Achats / supply | Trimestrielle |
| **CM2** | Peut-on financer de la publicité ? Le mix se dégrade-t-il ? La remise dérape-t-elle ? | Opérations **+** direction commerciale | **Hebdomadaire** |
| **CM3** | Monter ou baisser le budget média demain ? | Acquisition / growth | **Quotidienne** |
| **EBITDA** | Recruter, ouvrir un marché, lever, ou couper ? | Le dirigeant, seul | Mensuelle |

La colonne de droite est la leçon. **Marge brute chaque semaine, CM3 chaque jour** : ce sont les deux seuls étages qui bougent vite. Le COGS bouge par cycle de négociation, tous les six mois ; les frais fixes bougent quand tu signes un contrat de travail. Regarder son COGS tous les matins est une occupation, pas un pilotage.

Le CM2 a deux responsables, et c'est volontaire : les opérations tiennent logistique, PSP et retours ; le commerce tient la remise. Sans cette séparation, la remise devient le levier de secours universel — on la sort pour sauver un mois, elle ne redescend jamais. Au canonique § 2.1, elle passe de 3,0 % du CA HT en P1 à 8,0 % en P5 : 5 points de marge brute, soit 3 610 997 × 0,05 = **180 550 € par mois**, 2 166 600 € par an. La moitié de l'EBITDA annuel de P5 (4 377 023 €, canonique § 7).

### 1.4 Les cinq paliers, en % du CA HT

Canoniques § 2.1, § 2.2 et § 2.5.

| Étage | P1 | P2 | P3 | P4 | P5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| COGS | 20,00 % | 18,00 % | 16,00 % | 15,00 % | 14,50 % |
| **CM1** | **80,00 %** | **82,00 %** | **84,00 %** | **85,00 %** | **85,50 %** |
| Logistique | 16,00 % | 14,00 % | 12,00 % | 11,50 % | 11,00 % |
| PSP | 1,80 % | 1,70 % | 1,65 % | 1,60 % | 1,55 % |
| Retours / SAV | 2,00 % | 2,50 % | 3,00 % | 3,50 % | 3,50 % |
| Remises | 3,00 % | 5,00 % | 7,00 % | 8,00 % | 8,00 % |
| **CM2** | **57,20 %** | **58,80 %** | **60,35 %** | **60,40 %** | **61,45 %** |
| Publicité | 66,67 % | 54,55 % | 44,44 % | 42,86 % | 41,38 % |
| **CM3** | **−9,47 %** | **4,25 %** | **15,91 %** | **17,54 %** | **20,07 %** |
| Frais fixes | 21,20 % | 14,60 % | 10,70 % | 9,41 % | 9,97 % |
| **EBITDA** | **−30,67 %** | **−10,34 %** | **5,20 %** | **8,13 %** | **10,10 %** |

Deux mouvements opposés se croisent. COGS, logistique et PSP s'améliorent : 4 + 5 + 0,25 = **9,25 points gagnés** entre P1 et P5, c'est le volume qui négocie. Retours et remises se dégradent : de 5,00 % à 11,50 %, **6,5 points perdus**. Solde net : +4,25 points de marge brute (57,20 % → 61,45 %).

D'où la conclusion, contre-intuitive : **la marge brute ne s'améliore pas parce que tu grandis.** Elle s'améliore si — et seulement si — tu négocies le COGS et la logistique plus vite que tes retours et tes remises ne se dégradent. NØRA gagne cette course de 4,25 points sur dix ans. Ce n'est pas beaucoup. Une marque qui la perd découvre à 40 M€ de CA qu'elle est moins rentable qu'à 2 M€ : cas [C04](../etudes-de-cas/C04-scale-qui-detruit-la-marge.md).

Deuxième lecture : la ligne publicité tombe de 66,67 % à 41,38 %. Ce n'est pas le média qui devient moins cher — le nCAC *monte* de 26,62 € à 40,03 € (canonique § 2.4). C'est la part du CA produite par des clients déjà acquis qui augmente : 44,9 % du CA de P5 vient du réachat (canonique § 8), et cette part-là ne coûte pas de publicité. **La rentabilité d'une marque DTC à l'échelle n'est pas une performance d'acquisition, c'est une performance de base installée.** Module [E08](E08-retention-et-ltv.md).

---

## 2. Le piège TTC / HT

### 2.1 La démonstration

Le MER (*Marketing Efficiency Ratio*) rapporte tout ton chiffre d'affaires à toute ta dépense publicitaire. Il se lit sur le TTC, parce que c'est ce que ta plateforme affiche et ce que ta banque encaisse. Ta marge, elle, se calcule sur le HT. Donc la question « la publicité, ça me coûte quel pourcentage de mon CA ? » a une réponse et une seule, et ce n'est pas 1 ÷ MER.

Pose : t = TVA, R = CA TTC, P = dépense publicitaire.

```
MER = R ÷ P                donc    P = R ÷ MER
CA HT = R ÷ (1 + t)

Part de la pub en % du CA HT = P ÷ CA HT
                             = [ R ÷ MER ] ÷ [ R ÷ (1 + t) ]
                             = (1 + t) ÷ MER
```

**Part de la publicité en % du CA HT = (1 + TVA) ÷ MER.** Cette formule vaut à elle seule le prix du module.

### 2.2 Vérification sur P5

Canonique § 2 : CA TTC 4 333 196 €/mois. Canonique § 2.3 : MER réel 2,90. Canonique § 2.2 : pub 1 494 206 €, soit 41,4 % du CA HT.

```
Dépense pub   = 4 333 196 ÷ 2,90        = 1 494 205,5 €  ≈ 1 494 206 €   ✓
Part en % HT  = 1,20 ÷ 2,90             = 0,413793 = 41,38 %            ✓
Contre-vérif. = 1 494 206 ÷ 3 610 997   = 0,41379  = 41,38 %            ✓
```

Trois routes, un seul nombre.

### 2.3 L'erreur de sept points, chiffrée

Celui qui n'a jamais fait la division écrit 1 ÷ 2,90 = 34,48 %.

```
Écart = 41,38 % − 34,48 % = 6,90 points de CA HT
Forme fermée : (1 + t) ÷ MER − 1 ÷ MER = t ÷ MER = 0,20 ÷ 2,90 = 6,897 %
```

En euros sur P5 :

```
Erreur mensuelle = 3 610 997 × 0,06897              = 249 034 €
   ou, plus court = 1 494 206 × (1 − 1 ÷ 1,20)
                  = 1 494 206 ÷ 6                   = 249 034 €
Erreur annuelle  = 249 034 × 12                     = 2 988 412 €
```

**L'erreur vaut exactement un sixième de ta dépense publicitaire** — c'est la TVA contenue dans le CA que tu attribues à cette dépense. Mise en face de l'EBITDA annuel de P5 (4 377 023 €, canonique § 7) :

```
2 988 412 ÷ 4 377 023 = 68,3 % de l'EBITDA annuel
```

Le dirigeant qui commet cette erreur ne se trompe pas « un peu » : il croit disposer de 68 % de résultat en plus qu'il n'en a. À P5, il a de la réserve. À P2, où le MER réel est 2,20, la même erreur donne 0,20 ÷ 2,20 = 9,09 points de CA HT, soit 191 833 × 0,0909 = 17 438 € par mois — pour un EBITDA réel de −19 838 €. **Il se croit à l'équilibre alors qu'il perd 238 056 € par an.** Il scale. C'est la vallée de la mort du cas [C02](../etudes-de-cas/C02-vallee-de-la-mort.md).

Corollaire multi-pays : ton (1 + t) est une moyenne pondérée. Le canonique retient 20 % pour NØRA, c'est une hypothèse déclarée en tête du fichier. En vrai l'Allemagne est à 19 %, l'Espagne à 21 %, l'Italie à 22 %. **Ouvrir l'Italie fait monter ton MER seuil sans qu'aucun de tes coûts n'ait bougé.** Module [E11](E11-passage-a-echelle.md).

---

## 3. Le MER, le ROAS, l'aMER

### 3.1 Trois indicateurs, trois usages

| Indicateur | Formule | Ce qu'il mesure | Manipulable ? |
| --- | --- | --- | --- |
| **ROAS plateforme** | CA attribué par la régie ÷ dépense sur cette régie | Ce que la régie s'attribue | **Oui, entièrement** |
| **MER blended** | CA total TTC ÷ dépense publicitaire totale | L'efficacité réelle de l'euro média | **Non** |
| **aMER** | CA total TTC ÷ dépense de prospection seule | L'efficacité de l'euro qui va chercher un inconnu | Non, si la frontière est stable |

Le MER blended est le seul des trois qui ne peut pas être truqué, pour une raison arithmétique : son numérateur est le chiffre d'affaires de ta banque, son dénominateur le total de tes factures média. Aucune des deux quantités n'est produite par une régie. Un ROAS plateforme, si.

### 3.2 La sur-attribution, démontrée

Canonique § 5, plan média de P5. Somme des nouveaux clients attribués par canal : 21 346 + 5 094 + 8 651 + 2 543 + 2 916 + 815 = **41 364**. Nouveaux clients réels du mois (canonique § 2.4) : **37 324**.

```
Sur-attribution = 41 364 − 37 324 = 4 040 clients
                = 4 040 ÷ 37 324  = 10,82 %     (le canonique arrondit à 11 %)
```

Quatre mille clients qui n'existent pas. Pas parce qu'une régie ment : parce que six régies voient le même client, chacune a un point de contact vérifiable dans son parcours, chacune l'inscrit dans son compteur. C'est structurel et universel.

```
nCAC apparent (moyenne des canaux) = 1 494 206 ÷ 41 364 = 36,12 €
nCAC réel                          = 1 494 206 ÷ 37 324 = 40,03 €   (canonique § 2.4)
Sous-estimation = 3,91 € par client, soit 9,8 %
Sur 37 324 clients : 3,91 × 37 324 = 145 937 €/mois, 1 751 244 €/an
```

Un million sept cent cinquante mille euros de coût d'acquisition annuel qui n'apparaît dans aucun tableau de bord de régie.

### 3.3 Le ROAS que tu vas lire, et le nombre que tu dois calculer

*Hypothèse de lecture :* chaque canal n'est crédité que de la première commande des clients qu'il s'attribue, à l'AOV première commande de P5. Cet AOV n'est pas donné tel quel au canonique ; il se dérive de la contribution première commande (32,77 €, canonique § 2.4) et de la marge brute :

```
AOV 1ʳᵉ commande HT  = 32,77 ÷ 0,6145 = 53,33 €
AOV 1ʳᵉ commande TTC = 53,33 × 1,20   = 64,00 €
```

Contrôle de cohérence avec le modèle : CA des nouveaux clients = 37 324 × 64,00 = 2 388 736 € ; CA total 4 333 196 € ; donc CA de réachat = 1 944 460 € sur 60 200 − 37 324 = 22 876 commandes de réachat, soit **85,00 € TTC** par réachat. Contre-vérification par la contribution de réachat canonique (§ 3 : 43,53 €) : 85,00 ÷ 1,20 × 0,6145 = 43,53 €. ✓ Le modèle tient au centime.

| Canal | Budget | Clients attribués | CA attribué (× 64,00 €) | ROAS affiché |
| --- | ---: | ---: | ---: | ---: |
| Meta | 821 813 € | 21 346 | 1 366 144 € | 1,66 |
| TikTok | 224 131 € | 5 094 | 326 016 € | 1,45 |
| Google Search | 164 363 € | 8 651 | 553 664 € | 3,37 |
| Google PMax | 119 536 € | 2 543 | 162 752 € | 1,36 |
| Influence | 119 536 € | 2 916 | 186 624 € | 1,56 |
| Pinterest / Snap | 44 826 € | 815 | 52 160 € | 1,16 |
| **Somme** | **1 494 206 €** | **41 364** | **2 647 360 €** | **1,77** |

CA attribué 2 647 360 € contre 2 388 736 € réels : **258 624 € de CA fantôme par mois**, 3 103 488 € par an.

Le vrai décomposé, lui :

```
MER acquisition = 2 388 736 ÷ 1 494 206 = 1,60
MER réachat     = 1 944 460 ÷ 1 494 206 = 1,30
MER blended     = 1,60 + 1,30           = 2,90    ✓ (canonique § 2.3)
```

C'est la phrase la plus importante de la section. **L'acquisition seule tourne à un MER de 1,60, sous le MER seuil de 1,95** (démontré § 4). Sans clients qui reviennent, NØRA perdrait de l'argent sur chaque euro de publicité. Ce sont les 1,30 points apportés par la base installée qui rendent l'entreprise viable.

### 3.4 L'aMER

L'aMER rapporte le chiffre d'affaires **total** à la dépense de **prospection seule**. *Hypothèse de découpage :* Google Search et Shopping récoltent de la demande déjà créée, tout le reste est de la prospection. C'est une simplification — en pratique on sépare les requêtes de marque des génériques et on sort le retargeting des budgets Meta et TikTok.

```
Dépense de prospection = 1 494 206 − 164 363 = 1 329 843 €
aMER                   = 4 333 196 ÷ 1 329 843 = 3,26
```

Son intérêt : le MER blended peut s'améliorer sans aucune acquisition nouvelle, simplement en déplaçant du budget vers le retargeting et la marque. C'est le mensonge le plus confortable du métier — le tableau de bord s'améliore pendant que la machine s'arrête. **L'aMER attrape ce mouvement, le MER blended ne le voit pas.** MER qui monte et aMER qui baisse : tu n'as pas amélioré ta rentabilité, tu as commencé à récolter ton stock de demande, et ce stock est fini.

Règle sans exception : **on ne pilote jamais sur la somme des ROAS plateforme.** Le MER blended décide du budget total, l'aMER surveille la dérive, les ROAS de plateforme n'arbitrent qu'à l'intérieur d'un même compte — là où le biais d'attribution est constant et s'annule dans la comparaison. Module [E09](E09-mesure-et-incrementalite.md).

---

## 4. Le MER seuil

C'est le nombre le plus utile du cursus : le seul qui transforme une intuition (« on dépense trop ? ») en une comparaison de deux nombres.

### 4.1 Le seuil de contribution (CM3 = 0)

Notations : R = CA TTC, t = TVA, m = taux de marge brute en % du CA HT, P = dépense publicitaire.

```
CM3 = m × CA HT − P = m × R ÷ (1 + t) − R ÷ MER

CM3 = 0
  ⇔  m × R ÷ (1 + t) = R ÷ MER
  ⇔  m ÷ (1 + t) = 1 ÷ MER          (division par R, avec R > 0)
  ⇔  MER = (1 + t) ÷ m
```

```
MER seuil (CM3 = 0) = (1 + TVA) ÷ taux de marge brute
```

**R a disparu.** Le seuil de contribution ne dépend pas de ta taille, seulement de ta TVA et de ta marge brute. C'est ce qui le rend utilisable dès la première commande.

Vérification sur P5, marge brute 61,45 % :

```
MER seuil = 1,20 ÷ 0,6145 = 1,9528  →  1,95     ✓ (canonique § 2.3)
```

Contre-vérification en euros : à MER 1,95, la pub coûterait 4 333 196 ÷ 1,95 = 2 222 152 €, et le CM3 vaudrait 2 218 957 − 2 222 152 = −3 195 €, soit zéro à l'arrondi du seuil près. ✓

### 4.2 Le seuil d'EBITDA

Ajoute les frais fixes F, note f = F ÷ CA HT.

```
EBITDA = m × CA HT − P − F = m × R ÷ (1 + t) − R ÷ MER − f × R ÷ (1 + t)

EBITDA = 0
  ⇔  (m − f) × R ÷ (1 + t) = R ÷ MER
  ⇔  MER = (1 + t) ÷ (m − f)
```

```
MER seuil (EBITDA = 0) = (1 + TVA) ÷ (marge brute − frais fixes en % du CA HT)
```

Vérification sur P5 (frais fixes 360 000 €, canonique § 2.5) :

```
f         = 360 000 ÷ 3 610 997 = 9,969 %
m − f     = 0,6145 − 0,09969    = 0,51481
MER seuil = 1,20 ÷ 0,51481      = 2,3310  →  2,33     ✓ (canonique § 2.3)
```

**Piège logique.** Contrairement au seuil de contribution, R n'a pas vraiment disparu ici : il est caché dans f, puisque F est fixe en euros. Le seuil d'EBITDA n'est valable qu'au niveau de CA où tu l'as calculé. Si le CA HT de P5 baissait de 20 % à structure identique, f passerait à 360 000 ÷ 2 888 798 = 12,46 % et le seuil à 1,20 ÷ (0,6145 − 0,1246) = **2,45**. Ton MER de 2,90 serait encore au-dessus, mais ta marge de sécurité tomberait de 24,4 % à 18,4 %. **En décroissance, le seuil monte pendant que le chiffre d'affaires baisse : tu cours après une ligne qui recule.**

### 4.3 Lecture du canonique § 2.3, palier par palier

| Palier | MER réel | Seuil CM3 | Seuil EBITDA | Écart au seuil EBITDA |
| --- | ---: | ---: | ---: | ---: |
| P1 | 1,80 | 2,10 | 3,33 | **−46,0 %** |
| P2 | 2,20 | 2,04 | 2,71 | **−19,0 %** |
| P3 | 2,70 | 1,99 | 2,42 | +11,7 % |
| P4 | 2,80 | 1,99 | 2,35 | +19,0 % |
| P5 | 2,90 | 1,95 | 2,33 | +24,4 % |

Chaque seuil est reconstructible. Contrôle sur P1 : 1,20 ÷ 0,572 = 2,098 → 2,10 ✓ ; f = 6 500 ÷ 30 667 = 21,20 % ; 1,20 ÷ (0,572 − 0,212) = 1,20 ÷ 0,360 = 3,333 → 3,33 ✓.

**Le seuil de contribution baisse à peine** : de 2,10 à 1,95, soit 7 %, pour dix ans de croissance, sept marchés et 4,25 points de marge brute gagnés. Corollaire brutal : **l'échelle ne règle pas un problème de coefficient produit.** Si ton produit ne supporte pas un MER de 2,0, il ne le supportera pas mieux à 40 M€ de CA. C'est tout le cas [C01](../etudes-de-cas/C01-coefficient-insuffisant.md).

**Le seuil d'EBITDA, lui, s'effondre** : de 3,33 à 2,33, soit −30 %, entièrement porté par les frais fixes qui passent de 21,20 % à 9,97 % du CA HT. C'est le seul effet d'échelle réel de ce métier, et il joue une fois, entre P1 et P3. Ensuite les frais fixes ne descendent plus — 10,70 %, puis 9,41 %, puis 9,97 % : ils *remontent* en P5 avec la structure multi-pays. **L'économie d'échelle est un phénomène de démarrage, pas une rente perpétuelle.**

### 4.4 P1 et P2 tournent sous leur seuil : à quelle condition c'est rationnel

Perdre de l'argent pour acquérir des clients n'est ni une faute ni une évidence : c'est un investissement, et un investissement s'évalue. Le compte de résultat mensuel d'une marque en croissance rapide est structurellement trompeur — il additionne des cohortes jeunes, qui n'ont livré qu'une commande, et leur fait porter des frais fixes calibrés pour la taille future. **Le bon niveau d'analyse n'est pas le mois, c'est la cohorte.**

```
Condition de rendement :
   LTV 12 mois (contribution)  ≥  nCAC + frais fixes par nouveau client
```

P1 — canoniques § 3.1 (LTV 12 m 55,97 €, nCAC 26,62 €), § 2.4 (768 nouveaux clients/mois), § 2.5 (6 500 € de fixes) :

```
Fixes par nouveau client = 6 500 ÷ 768   =  8,46 €
Coût total par client    = 26,62 + 8,46  = 35,08 €
Surplus sur 12 mois      = 55,97 − 35,08 = +20,89 € par client
Par cohorte mensuelle    = 768 × 20,89   = 16 044 €
```

Le compte de résultat du mois affiche −9 403 €. Les deux chiffres sont vrais : le premier décrit l'investissement, le second la trésorerie.

P2 — LTV 12 m 70,70 €, nCAC 30,78 €, 3 400 nouveaux clients, 28 000 € de fixes :

```
Fixes par client   = 28 000 ÷ 3 400 =  8,24 €
Coût total         = 30,78 + 8,24   = 39,02 €
Surplus 12 mois    = 70,70 − 39,02  = +31,68 €
Par cohorte        = 3 400 × 31,68  = 107 712 €     (résultat mensuel : −19 838 €)
```

Le pari est plus rentable en P2 qu'en P1. Mais un investissement rentable peut te tuer si tu ne peux pas le financer. La condition complète comporte trois clauses, et il faut les trois.

1. **Rendement.** Vérifié : +20,89 € en P1, +31,68 € en P2.
2. **Trésorerie.** P1 : 9 403 × 3 mois = 28 209 €. P2 : 19 838 × 6 mois = 119 028 €. Perte cumulée M1–M9 = **147 237 €**, plus le BFR — 21 603 € en P1, 104 462 € en P2 (canonique § 4). **Besoin de financement du parcours M1–M9 : de l'ordre de 250 000 €.** Sans ce montant, le pari n'est pas irrationnel, il est infaisable, et l'entreprise meurt solvable sur le papier.
3. **Mesure.** La LTV utilisée doit être *observée sur cohortes*, pas extrapolée. En P1 tu as trois mois de recul : tu ne peux pas encore savoir que la LTV 12 mois vaudra 55,97 €. Tu paries. La seule discipline honnête est de fixer, avant de commencer, le taux de réachat à 90 jours en dessous duquel tu coupes.

> **À retenir :** perdre de l'argent en P1 et P2 est rationnel si — et seulement si — la LTV 12 mois couvre le nCAC *plus* les frais fixes par client, que tu as le cash pour tenir neuf mois de perte cumulée plus le BFR, et que tu as fixé à l'avance le seuil de réachat qui déclenche l'arrêt. Deux clauses sur trois ne suffisent pas.

---

## 5. Le CAC

### 5.1 nCAC contre CAC blended

```
nCAC        = TOUTE la dépense publicitaire ÷ nombre de NOUVEAUX clients
CAC blended = dépense publicitaire ÷ TOUS les clients ayant commandé
```

Le numérateur du nCAC contient toute la dépense, retargeting compris ; le dénominateur ne contient que les nouveaux clients. C'est asymétrique, et c'est voulu : cela répond à « combien me coûte le fait de faire entrer un client de plus dans ma base ? », la seule question que le budget média doive trancher.

```
nCAC P5        = 1 494 206 ÷ 37 324 = 40,03 €     (canonique § 2.4)
CAC blended P5 = 1 494 206 ÷ 60 200 = 24,82 €
Écart : 40,03 ÷ 24,82 = ×1,61, soit 38 % de sous-estimation
```

Le CAC blended n'a aucun sens économique : il divise la dépense d'acquisition par un dénominateur incluant 22 876 commandes de clients déjà acquis, qui n'ont rien coûté ce mois-ci. Pire, **il s'améliore mécaniquement quand la part de réachat monte** — un indicateur qui flatte au moment exact où l'acquisition se dégrade.

### 5.2 NØRA perd de l'argent sur la première commande. À tous les paliers.

Canonique § 2.4 :

| Palier | nCAC | Contribution 1ʳᵉ cmd | Marge 1ʳᵉ cmd | Contribution ÷ nCAC |
| --- | ---: | ---: | ---: | ---: |
| P1 | 26,62 € | 21,69 € | **−4,93 €** | 0,81 |
| P2 | 30,78 € | 26,95 € | **−3,83 €** | 0,88 |
| P3 | 33,18 € | 30,17 € | **−3,01 €** | 0,91 |
| P4 | 37,77 € | 31,71 € | **−6,06 €** | 0,84 |
| P5 | 40,03 € | 32,77 € | **−7,26 €** | 0,82 |

Au palier P5 : 37 324 × 7,26 = **270 972 € perdus par mois** sur les premières commandes, 3 251 664 € par an.

Le déficit se creuse de P3 à P5, pour deux raisons visibles au canonique. Le nCAC monte de 33,18 € à 40,03 € (+20,6 %) parce qu'on achète du volume de plus en plus loin du cœur de cible — le plan média § 5 le montre : 19,00 € sur Google Search, 55,00 € sur Pinterest/Snap. Et la contribution première commande ne monte que de 30,17 € à 32,77 € (+8,6 %), parce que l'AOV première commande passe seulement de 60,00 € à 64,00 € TTC (dérivé § 3.3), très en dessous de l'AOV mixte de 71,98 €.

**C'est un choix, pas un accident.** Sa condition de validité :

```
contribution de réachat × commandes de réachat par client sur l'horizon
   ≥  (nCAC − contribution 1ʳᵉ commande)  +  frais fixes par nouveau client
```

P5 — canonique § 3 : contribution par réachat 43,53 €, commandes cumulées à 12 mois 2,24, donc 1,24 réachat. Fixes par nouveau client : 360 000 ÷ 37 324 = 9,65 €.

```
Gauche = 43,53 × 1,24            = 53,98 €
Droite = (40,03 − 32,77) + 9,65
       = 7,26 + 9,65             = 16,91 €
53,98 ≥ 16,91   ✓   marge de sécurité : ×3,19
```

Le réachat de NØRA pourrait être divisé par trois avant que le pari ne devienne perdant. Traduis-le en seuil actionnable : le minimum de commandes de réachat par client sur 12 mois est 16,91 ÷ 43,53 = **0,39**, soit 1,39 commande cumulée. Le modèle en produit 2,24. **Ton alerte se déclenche sous 1,39 commande cumulée par client à 12 mois.** Un seuil dérivé, pas inventé.

### 5.3 Le CAC marginal

Le nCAC est une moyenne, et une moyenne ne décide de rien : la décision porte toujours sur la *prochaine* tranche de budget.

```
CAC marginal = dépense supplémentaire ÷ nouveaux clients supplémentaires
```

La courbe de CAC est croissante, toujours, et le canonique § 5 en donne la preuve directe : dans le même mois, NØRA achète à 19,00 € sur Google Search et à 55,00 € sur Pinterest/Snap, un rapport de ×2,9. Si le CAC était constant, on mettrait 100 % du budget sur Google Search. On ne le fait pas parce que Google Search sature — il ne récolte que la demande déjà créée, et il n'y en a que 8 651 clients par mois à ce prix.

**Le CAC marginal de NØRA à P5 est donc de l'ordre de 55 €, pas 40,03 €.** Toute décision d'augmenter le budget se juge contre 55 €.

```
LTV 12 m ÷ CAC marginal = 86,75 ÷ 55,00 = 1,58     (canonique § 3)
```

Au-dessus de 1,5, la tranche reste créatrice de valeur — tout juste. Mais son payback est bien plus long. Interpolation sur la courbe canonique § 3, entre 3 mois (47,57 €) et 6 mois (64,11 €) :

```
(55,00 − 47,57) ÷ (64,11 − 47,57) = 7,43 ÷ 16,54 = 0,449
Payback marginal = 3 + 0,449 × 3 = 4,35 mois       (contre 1,8 pour le client moyen)
```

**Le client marginal met 2,4 fois plus longtemps à se rembourser que le client moyen.** C'est là, et pas dans le ratio LTV/CAC, que se trouve la vraie limite de croissance.

---

## 6. LTV, payback et le ratio

### 6.1 La LTV en chiffre d'affaires est le mensonge le plus répandu du métier

Canonique § 3, cohorte P5 à 12 mois :

| | Valeur | Rapport au nCAC de 40,03 € |
| --- | ---: | ---: |
| CA cumulé TTC par client | 169,40 € | 4,23 |
| CA cumulé HT par client | 141,17 € | 3,53 |
| **LTV en contribution** | **86,75 €** | **2,17** |

```
169,40 € TTC
÷ 1,20                    = 141,17 €   ← on retire la TVA
× 61,45 % de marge brute  =  86,75 €   ← on retire COGS, logistique, PSP,
                                          retours, remises
Contrôle : 141,17 × 0,6145 = 86,75 €    ✓
Facteur d'écart : 169,40 ÷ 86,75 = 1,953  ≈  ×2
```

Celui qui présente 169,40 € comme sa LTV annonce un ratio de 4,23 quand le vrai est 2,17. Il croit avoir une marge de sécurité de ×4 ; il a ×2. Et l'erreur est *systématiquement dans le même sens* — personne ne se trompe jamais en sous-estimant sa LTV. Ce biais unidirectionnel ne s'annule pas dans la moyenne des décisions, il s'accumule.

Le mécanisme de mort est mécanique. Le dirigeant voit 4,23, se dit « largement au-dessus de 3 », double son budget. Le CAC marginal monte à 55 €. Il calcule 169,40 ÷ 55 = 3,08, « toujours au-dessus de 3 », il continue. La vérité est 86,75 ÷ 55 = 1,58 : il vient d'entrer en zone de réparation. Il le découvrira neuf mois plus tard, quand la trésorerie manquera.

**Règle sans exception : une LTV se calcule en marge de contribution.** Si quelqu'un te donne une LTV, ta première question est « en CA ou en contribution ? ». S'il hésite, c'est du CA.

### 6.2 L'horizon : 12 mois, pas 36

Canonique § 3, même cohorte P5 :

| Horizon | LTV contribution | LTV/CAC | Gain vs horizon précédent |
| --- | ---: | ---: | ---: |
| 1 mois | 35,38 € | 0,88 | — |
| 3 mois | 47,57 € | 1,19 | +12,19 € |
| 6 mois | 64,11 € | 1,60 | +16,54 € |
| **12 mois** | **86,75 €** | **2,17** | +22,64 € |
| 18 mois | 105,03 € | 2,62 | +18,28 € |
| 24 mois | 118,96 € | 2,97 | +13,93 € |
| 36 mois | 138,11 € | 3,45 | +19,15 € |

Entre 12 et 36 mois la contribution gagne encore 51,36 €, soit +59 % de LTV. Un dirigeant tenté prendra 138,11 € et annoncera 3,45 au lieu de 2,17. Trois raisons de refuser, aucune n'est de la prudence de principe.

**Tu ne l'as pas observé.** Une LTV 36 mois mesurée demande trois ans de cohortes suivies. Une marque qui atteint P5 en M31–M40 n'a de cohortes matures que sur ses tout premiers mois — acquises en P1, sur un mix produit, pays et canal qui n'ont plus rien à voir. La LTV 36 mois d'une marque de trois ans est une extrapolation habillée en mesure.

**Le biais du survivant joue dans un seul sens.** Les clients encore observables à 36 mois sont ceux qui sont restés ; les cohortes récentes n'ont pas eu le temps de partir.

**Ce n'est pas ta décision.** Augmenter le budget aujourd'hui sur une LTV 36 mois, c'est financer 36 mois d'acquisition avant le premier euro récupéré sur la dernière tranche. Le canonique § 4 dit ce que ça coûte : à P5, +100 000 € de CA mensuel immobilisent 52 263 € de cash. **Une entreprise ne meurt pas d'être non rentable, elle meurt de manquer de trésorerie.**

Position du cursus : **LTV 12 mois pour toute décision d'investissement, LTV 24 mois comme borne haute de scénario, jamais au-delà.** Module [E08](E08-retention-et-ltv.md).

### 6.3 Le payback, et pourquoi il prime sur le ratio

```
Payback = temps pour que la contribution cumulée d'un client rembourse le nCAC
```

Reconstruction du payback P5, pour que tu saches le faire sur tes chiffres. On cherche l'horizon où la LTV atteint 40,03 € : elle vaut 35,38 € à 1 mois, 47,57 € à 3 mois.

```
Fraction = (40,03 − 35,38) ÷ (47,57 − 35,38) = 4,65 ÷ 12,19 = 0,3815
Payback  = 1 + 0,3815 × 2 = 1,76  →  ≈ 1,8 mois     ✓ (canonique § 3)
```

| Palier | nCAC | LTV 12 m | LTV/CAC | **Payback** |
| --- | ---: | ---: | ---: | ---: |
| P1 | 26,62 € | 55,97 € | 2,10 | 1,8 mois |
| P2 | 30,78 € | 70,70 € | 2,30 | **1,3 mois** |
| P3 | 33,18 € | 80,06 € | 2,41 | **1,1 mois** |
| P4 | 37,77 € | 83,51 € | 2,21 | 1,6 mois |
| P5 | 40,03 € | 86,75 € | 2,17 | 1,8 mois |

Le ratio te dit *si* un client vaut son coût ; le payback te dit *quand*. Une entreprise ne fait pas faillite parce que ses clients ne valent pas leur coût, mais parce qu'elle a payé ce coût en janvier et touchera la valeur en novembre. Canonique § 4 :

| Palier | Cash immobilisé par +100 k€ de CA mensuel | EBITDA mensuel | Croissance autofinançable |
| --- | ---: | ---: | ---: |
| P3 | 40 864 € | 51 033 € | +124 886 € de CA/mois |
| P4 | 47 500 € | 198 572 € | +418 046 € de CA/mois |
| P5 | 52 263 € | 364 752 € | +697 917 € de CA/mois |

Vérification de la ligne P5 : 364 752 ÷ 52 263 = 6,979, donc 697 917 € de CA mensuel supplémentaire finançable sans apport, soit 697 917 ÷ 4 333 196 = **16,1 % de croissance mensuelle autofinançable**.

L'expérience de pensée qui tranche : prends une marque au **même** ratio de 2,17 que P5, mais avec un payback de 9 mois au lieu de 1,8 — réachat lent, consommable à cycle long. Elle achète exactement la même valeur au même prix.

```
Dépense pub mensuelle P5        = 1 494 206 €
Avance de trésorerie à 1,8 mois = 1 494 206 × 1,8 =  2 689 571 €
Avance de trésorerie à 9,0 mois = 1 494 206 × 9,0 = 13 447 854 €
Écart                                             = 10 758 283 €
```

Dix millions et demi d'euros de trésorerie supplémentaire, à ratio LTV/CAC rigoureusement identique. **Le ratio ne l'a pas vu. Le payback, oui.**

| Financement | Payback maximum |
| --- | --- |
| Autofinancé, sans réserve | **Sur la première commande** |
| Autofinancé avec réserve | ≤ 3 mois |
| Dette bancaire ou revenue-based | ≤ 6 mois |
| Fonds propres levés | ≤ 12 mois |

NØRA est à 1,8 mois sur le client moyen, mais à **4,35 mois sur le client marginal** (§ 5.3). C'est ce nombre-là qui borne la vitesse d'accélération. Module [E10](E10-cash-et-operations.md).

### 6.4 Le ratio LTV/CAC et son interprétation contre-intuitive

| Ratio LTV 12 m / nCAC | Lecture | Action |
| --- | --- | --- |
| **< 1** | Chaque client détruit de la valeur | Coupe l'acquisition aujourd'hui |
| **1 à 1,5** | Rentable à l'unité, ne couvre pas les frais fixes | **On répare**, on ne scale pas |
| **1,5 à 2** | Zone de survie sous surveillance | On tient le budget, on travaille l'AOV et le réachat |
| **2 à 4** | Zone saine | **On accélère**, jusqu'à la limite du payback |
| **> 5** | **Tu sous-investis** | Augmente le budget jusqu'à faire baisser le ratio |

Les trois premières lignes sont intuitives. La dernière ne l'est pas, et c'est la plus rentable.

*Hypothèse de travail :* une marque dont la LTV 12 mois en contribution est 86,75 € — celle de P5, canonique § 3 — envisage son budget par tranches de 100 000 €. La courbe de CAC marginal ci-dessous est **modélisée** ; sa forme croissante, elle, est établie (§ 5.3).

| Tranche | Clients de la tranche | CAC marginal | Contribution 12 m | Résultat |
| --- | ---: | ---: | ---: | ---: |
| 1ʳᵉ — 100 000 € | 5 000 | 20,00 € | 433 750 € | **+333 750 €** |
| 2ᵉ — 100 000 € | 3 571 | 28,00 € | 309 784 € | **+209 784 €** |
| 3ᵉ — 100 000 € | 2 632 | 38,00 € | 228 326 € | **+128 326 €** |
| 4ᵉ — 100 000 € | 2 041 | 49,00 € | 177 056 € | **+77 056 €** |
| 5ᵉ — 100 000 € | 1 613 | 62,00 € | 139 928 € | **+39 928 €** |
| 6ᵉ — 100 000 € | 1 266 | 79,00 € | 109 826 € | **+9 826 €** |
| 7ᵉ — 100 000 € | 990 | 101,00 € | 85 883 € | **−14 117 €** |

Chaque tranche crée de la valeur tant que son CAC marginal reste sous 86,75 €. La sixième (79,00 €) passe ; la septième (101,00 €) détruit. **L'optimum est à six tranches, 600 000 € de budget.** Compare deux dirigeants :

```
Dirigeant A — s'arrête à une tranche, parce que son ratio est superbe
   Budget 100 000 €   Clients 5 000    CAC moyen 20,00 €
   Ratio = 86,75 ÷ 20,00 = 4,34                      « excellent »
   Contribution = 5 000 × 86,75 − 100 000 = 333 750 €

Dirigeant B — va jusqu'à l'optimum
   Budget 600 000 €
   Clients 5 000+3 571+2 632+2 041+1 613+1 266 = 16 123
   CAC moyen = 600 000 ÷ 16 123 = 37,22 €
   Ratio = 86,75 ÷ 37,22 = 2,33                      « moyen »
   Contribution = 16 123 × 86,75 − 600 000 = 1 398 670 − 600 000 = 798 670 €

798 670 ÷ 333 750 = ×2,39
```

**Le dirigeant au « mauvais » ratio de 2,33 gagne 2,39 fois plus de contribution que celui au « bon » ratio de 4,34.** Le ratio de A est élevé précisément *parce qu'il n'a acheté que les clients les moins chers*. Il a laissé 464 920 € de contribution sur la table pour préserver un indicateur. La règle générale porte sur le marginal, jamais sur la moyenne :

```
Continue d'acheter tant que :  CAC marginal  <  LTV 12 mois en contribution
```

Le ratio moyen ne sert qu'à détecter qu'on est trop loin à gauche de la courbe. **Un ratio supérieur à 5 est une alerte au même titre qu'un ratio inférieur à 1,5** : dans un cas tu détruis de la valeur, dans l'autre tu refuses d'en créer.

Deux garde-fous. Le payback d'abord : à 79 € de CAC marginal, l'interpolation entre 6 mois (64,11 €) et 12 mois (86,75 €) donne 6 + (79 − 64,11) ÷ 22,64 × 6 = **9,9 mois**. Une marque autofinancée s'arrêtera bien avant la sixième tranche, non parce que c'est non rentable mais parce que c'est infinançable. L'incrémentalité ensuite : la courbe suppose que les clients supplémentaires sont réellement supplémentaires, ce que l'attribution ne sait pas prouver — module [E09](E09-mesure-et-incrementalite.md).

> **À retenir :** le CAC moyen raconte le passé, le CAC marginal décide du futur. Compare le CAC marginal à la LTV 12 mois pour savoir si tu *peux*, et le payback marginal à ta réserve de trésorerie pour savoir si tu peux *te le permettre*.

---

## 7. Quel levier vaut le plus, et où est ton point mort

### 7.1 Le tableau de sensibilité

Canonique § 7 : effet sur l'EBITDA annuel d'une amélioration de 10 % de chaque levier au palier P5, toutes choses égales par ailleurs. EBITDA annuel de référence : 4 377 023 €.

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

Les deux leviers ajoutent le même chiffre d'affaires : +10 % de CA HT, soit +361 100 €. Ils ne rapportent pas la même chose, et l'explication tient en une phrase : **la logistique est un coût par commande, pas un coût par euro.**

+10 % de conversion à budget constant, c'est +10 % de commandes au même panier. Tous les coûts variables restent au même pourcentage du CA — la logistique aussi, puisqu'il y a 10 % de colis en plus. La marge brute reste à 61,45 %.

```
Gain mensuel = 3 610 997 × 0,10 × 0,6145 = 221 896 €
Gain annuel  = 221 896 × 12               = 2 662 749 €   ✓ canonique § 7, à l'euro
```

+10 % d'AOV **à commandes constantes** : toujours 60 200 commandes, chacune valant 10 % de plus. Chaque poste se comporte selon sa nature réelle.

```
CA HT initial 3 610 997 €   →   CA HT nouveau 3 972 097 €   (+361 100 €)
Commandes : 60 200 — INCHANGÉ

COGS        proportionnel au CA (panier plus gros = plus de produit)
            523 595 €  →  3 972 097 × 0,145 = 575 954 €     (+52 359 €)
Logistique  FIXE PAR COMMANDE — mêmes colis, même transport
            397 210 €  →  397 210 €                          (+0 €)
PSP         proportionnel (commission sur le montant encaissé)
             55 970 €  →  3 972 097 × 0,0155 =  61 568 €     (+5 598 €)
Retours     proportionnel (on rembourse la valeur du panier)
            126 385 €  →  139 023 €                          (+12 638 €)
Remises     proportionnel (les codes sont en %)
            288 880 €  →  317 768 €                          (+28 888 €)

Coûts variables nouveaux = 575 954 + 397 210 + 61 568 + 139 023 + 317 768
                         = 1 491 523 €
Marge brute nouvelle = 3 972 097 − 1 491 523 = 2 480 574 €
Marge brute initiale                          = 2 218 957 €
Gain mensuel                                  =   261 617 €
Gain annuel = 261 617 × 12                    = 3 139 405 €
```

Le canonique affiche 3 139 401 € : quatre euros d'écart sur 3,1 M€, imputables aux arrondis. ✓ Et l'écart entre les deux leviers s'isole exactement :

```
3 139 405 − 2 662 749 = 476 656 €/an = 39 721 €/mois × 12
                                     = 10 % de la logistique mensuelle × 12
```

**L'intégralité de la supériorité du panier moyen sur la conversion est la logistique qui ne suit pas.** Rien d'autre. Le taux de marge brute passe de 61,45 % à 2 480 574 ÷ 3 972 097 = **62,45 %** : un point gagné sans toucher à un contrat fournisseur.

Généralisation : **tout coût fixe par commande s'allège relativement quand l'AOV monte** — logistique, part fixe du PSP, préparation, emballage, une partie du SAV. C'est la raison arithmétique pour laquelle le passage de P5 à P5+ (canonique § 8) fonctionne : +7 % d'AOV, −7 % de commandes, même chiffre d'affaires, +4,5 points de marge brute. Modules [E03](E03-offre-et-prix.md) et [E12](E12-marque-et-actif.md).

### 7.3 Pourquoi COGS et frais fixes sont les leviers les plus faibles

Rien de mystérieux : ce sont les deux plus petites lignes de la cascade, et on n'en retire que 10 %.

```
COGS        = 14,50 % du CA HT  →  −10 % = 1,45 point de CA HT
Frais fixes =  9,97 % du CA HT  →  −10 % = 1,00 point de CA HT
AOV         = +7,24 points de CA HT d'EBITDA  (261 617 ÷ 3 610 997)

Vérifications :
COGS        : 3 610 997 × 0,145 × 0,10 × 12 = 628 314 €   ✓ canonique 628 313 €
Frais fixes : 360 000 × 0,10 × 12           = 432 000 €   ✓ canonique 432 000 €
Retours     : 3 610 997 × 0,01 × 12         = 433 320 €   ✓ canonique 433 320 €
```

Le tableau canonique § 7 est reconstructible intégralement. Alors pourquoi les dirigeants passent-ils leurs journées sur les deux plus faibles ? Trois raisons, et aucune n'est bête. **Ce sont les seuls leviers entièrement sous contrôle** : renégocier un fournisseur est une décision unilatérale, augmenter l'AOV de 10 % demande de changer l'offre et le marché a un droit de veto. **Le gain est immédiat et certain** : une baisse de COGS se voit sur la facture suivante, une hausse d'AOV se teste, échoue une fois sur deux et met un trimestre à se stabiliser. **C'est visible** : couper des coûts a l'air d'être du management, passer six semaines à concevoir une vente en lot a l'air de ne rien faire.

Ce qui n'annule pas le ×7,3. L'arbitrage correct n'est pas d'abandonner le COGS, c'est de refuser qu'il consomme plus de temps de direction que l'AOV : **la part du temps consacrée à un levier ne doit pas dépasser sa part dans le tableau de sensibilité.**

### 7.4 Le point mort en commandes par jour

Un seuil de rentabilité en euros ne parle à personne dans une équipe. En commandes par jour, tout le monde le comprend et il se vérifie chaque matin sur un écran. Méthode, à mix constant (même répartition première commande / réachat) :

```
CM3 par commande      = marge brute par commande − dépense pub par commande
Point mort (cmd/mois) = frais fixes mensuels ÷ CM3 par commande
Point mort (cmd/jour) = point mort mensuel ÷ 30,33
```

Le diviseur 30,33 est la convention du modèle : un mois vaut 52 ÷ 12 = 4,3333 semaines. C'est ce qui rend le canonique § 9 exact (60 200 ÷ 30,33 = 1 985 commandes/jour ; il affiche 1 984 à 72 € d'AOV). Déroulé de P5 :

```
Marge brute par commande = 2 218 957 ÷ 60 200 = 36,86 €
Pub par commande         = 1 494 206 ÷ 60 200 = 24,82 €
CM3 par commande         = 36,86 − 24,82      = 12,04 €
Contrôle : 60 200 × 12,04 = 724 808 € ≈ 724 752 € de CM3 canonique   ✓
Point mort = 360 000 ÷ 12,04 = 29 900 cmd/mois = 29 900 ÷ 30,33 = 986 cmd/jour
```

| Palier | Marge brute /cmd | Pub /cmd | **CM3 /cmd** | Point mort /mois | **Point mort /jour** | Réel /jour | Marge de sécurité |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| P1 | 21,93 € | 25,56 € | **−3,63 €** | — | **jamais atteint** | 26 | — |
| P2 | 28,20 € | 26,16 € | **+2,04 €** | 13 725 | **452** | 132 | **−70,8 %** |
| P3 | 32,89 € | 24,22 € | **+8,67 €** | 12 111 | **399** | 593 | +48,6 % |
| P4 | 35,13 € | 24,93 € | **+10,20 €** | 22 549 | **743** | 1 385 | +86,4 % |
| P5 | 36,86 € | 24,82 € | **+12,04 €** | 29 900 | **986** | 1 985 | +101,3 % |

Contrôles contre le canonique § 2.2 : P1, 800 × (−3,63) = −2 904 € contre −2 903 € ✓ ; P2, 4 000 × 2,04 = 8 160 € contre 8 162 € ✓ ; P3, 18 000 × 8,67 = 156 060 € contre 156 033 € ✓ ; P4, 42 000 × 10,20 = 428 400 € contre 428 572 € ✓. Les écarts sont des arrondis au centime sur la contribution unitaire.

**P1 n'a pas de point mort.** Sa contribution après publicité est négative : −3,63 € par commande. Aucun volume ne le sauve — vendre plus creuse la perte. C'est la situation la plus dangereuse du métier, parce qu'elle ressemble exactement à un problème de volume sans en être un. Le seul remède est de remonter le MER au-dessus de 2,10 : changer le prix, le produit ou la publicité, pas la quantité.

**P2 est à 29 % de son point mort** : 132 commandes par jour contre 452 nécessaires, soit ×3,4 de volume à structure inchangée. Faisable — P3 en fait 593 — mais cela dit que P2 n'est pas un palier stationnaire. On y transite, on n'y campe pas.

**De P3 à P5, la marge de sécurité double** : +48,6 %, +86,4 %, +101,3 %. À P5, NØRA peut perdre la moitié de ses commandes avant de repasser sous zéro. C'est cette réserve qui autorise à parier sur de nouveaux marchés — module [E13](E13-risque-de-ruine.md).

---

## 8. Les erreurs qui coûtent cher

**1 — Compter la publicité en % du CA TTC.** Un MER de 2,90 devient « 34,5 % du CA » ; la réalité est 41,4 %. Coût : 1 494 206 ÷ 6 = 249 034 €/mois, **2 988 412 €/an** à P5, soit 68,3 % de l'EBITDA (§ 2.3). Antidote : (1 + TVA) ÷ MER écrit en dur dans le tableau de bord.

**2 — Présenter la LTV en chiffre d'affaires.** 169,40 € au lieu de 86,75 € à 12 mois : **facteur 1,95** (§ 6.1). Le ratio annoncé passe de 2,17 à 4,23 et le dirigeant accélère. Antidote : la LTV se calcule en marge de contribution, point.

**3 — Extrapoler la LTV à 36 mois pour justifier un CAC.** 138,11 € au lieu de 86,75 € : +59 % sortis d'un modèle, pas d'une observation (§ 6.2). Le coût est en trésorerie : à payback 9 mois au lieu de 1,8, l'avance sur la dépense média de P5 passe de 2 689 571 € à 13 447 854 € (§ 6.3).

**4 — Présenter un CAC blended comme un nCAC.** 24,82 € au lieu de 40,03 € : **38 % de sous-estimation** (§ 5.1). Pire, l'indicateur s'améliore mécaniquement quand la part de réachat monte — il flatte au moment exact où l'acquisition se dégrade.

**5 — Ne pas compter les remises comme un coût variable.** Elles se dissolvent dans le prix moyen et personne ne les défend. De 3,0 % à 8,0 % du CA HT entre P1 et P5 : 5 points, **180 550 €/mois, 2 166 600 €/an** à P5 (§ 1.3). Antidote : ligne visible, propriétaire nommé, plafond mensuel décidé à l'avance.

**6 — Ne pas provisionner les retours.** Ils arrivent 15 à 45 jours après la vente ; une marque en croissance rapide les sous-estime structurellement, parce que le dénominateur du mois a explosé pendant que le numérateur reflète les ventes du mois précédent. Un point d'erreur à P5 : 3 610 997 × 0,01 × 12 = **433 320 €/an**. Antidote : taux de retour par cohorte de commandes, pas par mois calendaire.

**7 — Croire que le MER seuil est une constante.** Il bouge dès que la marge brute bouge, et le seuil d'EBITDA bouge en plus avec le niveau de CA, puisque f = frais fixes ÷ CA HT (§ 4.2). Un taux de retour passant de 3,5 % à 5,5 % fait monter le seuil de 2,33 à 2,43 (exercice 2) ; un CA en baisse de 20 % le fait monter à 2,45. Antidote : recalculer les deux seuils chaque mois par les formules, jamais de mémoire.

**8 — Piloter sur le ROAS de plateforme, ou s'arrêter parce que le ratio est beau.** À P5, 41 364 clients attribués contre 37 324 réels — 10,8 % de sur-attribution — et **3 103 488 €/an de CA fantôme** (§ 3.3). Symétriquement, un ratio de 4,34 sur une tranche produit 333 750 € de contribution là où un ratio de 2,33 sur six tranches en produit 798 670 €, soit ×2,39 (§ 6.4). Antidote : MER blended pour le budget total, CAC marginal pour la tranche suivante.

---

## 9. Ce que ce module ne dit pas

**Ce module suppose l'attribution résolue. Elle ne l'est pas.** Toute la section 5 traite le nCAC comme un nombre connu : 1 494 206 € divisés par 37 324 nouveaux clients. Le dénominateur est solide — un décompte de comptes créés dans ta base — et le numérateur aussi — des factures. Mais savoir *lesquels* de ces 37 324 clients existent **à cause de** la dépense reste entier. Module [E09](E09-mesure-et-incrementalite.md).

**La marge de contribution ne dit rien de l'incrémentalité.** C'est la limite la plus sérieuse du module. Le calcul du § 6.4 — « continue tant que le CAC marginal est sous la LTV » — suppose que les clients supplémentaires de chaque tranche sont réellement supplémentaires. Si 30 % d'entre eux seraient venus de toute façon, le CAC marginal vrai vaut 1 ÷ 0,7 = **1,43 fois** le CAC marginal observé, et l'optimum se déplace de plusieurs tranches vers la gauche. Aucune arithmétique de marge ne détecte ça ; seule l'expérimentation le peut — coupure géographique, holdout, test d'incrémentalité. Cas [C06](../etudes-de-cas/C06-test-incrementalite.md).

**Le CAC ne mesure pas l'effet mémoriel de long terme, et Byron Sharp a raison de le dire.** Le [module 10](../../modules/10-sharp-distinctivite.md) du cursus racine soutient que l'essentiel de la croissance vient de la disponibilité mentale accumulée chez des acheteurs légers qui n'achèteront pas ce trimestre — et qu'une publicité dont l'effet se manifeste dans dix-huit mois est comptée comme un échec par un tableau de bord à fenêtre de sept jours. Cette critique n'est pas réfutable par les chiffres de ce module : elle porte sur ce qu'ils ne mesurent pas. Regarde la ligne publicité de la cascade P5 — 1 494 206 € par mois. Une part de cette dépense construit une mémoire qui produira des ventes hors de toute fenêtre d'attribution, et le nCAC de 40,03 € l'ignore intégralement. Position du cursus, explicite : **le nCAC et le MER seuil sont des instruments de contrainte budgétaire, pas des mesures de la valeur créée par la publicité.** Ils disent ce que tu peux te permettre, pas ce que tu construis. Module [E12](E12-marque-et-actif.md).

**Trois angles morts plus techniques.** Les frais fixes sont fixes *par palier*, pas par mois : de 230 000 € à 360 000 € entre P4 et P5 (canonique § 2.5), soit +56 %, par marches, quand on recrute ou qu'on ouvre un marché. Le module ignore la saisonnalité, alors que le Black Friday déforme simultanément AOV, remise, MER et taux de retour — cas [C09](../etudes-de-cas/C09-piege-du-black-friday.md). Et il ne traite la trésorerie qu'au travers du payback, alors que le BFR de P5 atteint 2 264 655 € (canonique § 4) — module [E10](E10-cash-et-operations.md).

**Enfin, sur les chiffres eux-mêmes.** NØRA est une marque fictive, le canonique le dit en tête de fichier. Son modèle est cohérent au centime — j'ai vérifié dans ce module la reconstruction complète des § 2.2, § 2.3, § 3, § 5 et § 7. Cette cohérence est une propriété du modèle, pas du monde. Une marque réelle a des mois où le taux de retour double sans explication.

---

## 10. Le tableau de bord du module

Six indicateurs. Pas sept. Si tu ne peux en tenir que trois à jour, garde les trois premiers.

| # | Indicateur | Formule | Fréquence | Seuil d'alerte | Référence P5 |
| --- | --- | --- | --- | --- | ---: |
| 1 | **Marge brute (CM2)** | (CA HT − COGS − log. − PSP − retours − remises) ÷ CA HT | Hebdomadaire | **−1,5 point sur 4 semaines glissantes** | 61,45 % |
| 2 | **MER blended** | CA TTC total ÷ dépense pub totale | **Quotidienne** (7 j glissants) | **Sous le seuil EBITDA**, ou 2 jours d'affilée sous le seuil CM3 | 2,90 |
| 3 | **MER seuil EBITDA** | (1 + TVA) ÷ (marge brute − frais fixes ÷ CA HT) | Mensuelle, **recalculé** | **+0,10 en un mois** | 2,33 |
| 4 | **nCAC** | dépense pub totale ÷ nouveaux clients | Hebdomadaire | **+15 % sur 4 semaines** sans hausse de LTV | 40,03 € |
| 5 | **LTV 12 m / nCAC** | LTV 12 m en contribution ÷ nCAC | Mensuelle | **< 1,5 → on répare. > 5 → on sous-investit** | 2,17 |
| 6 | **Payback marginal** | mois pour couvrir le **CAC marginal** | Mensuelle | **> 3 mois si autofinancé, > 6 si endetté** | 4,35 mois |

Quatre règles d'usage valent autant que le tableau. **Le MER seuil se recalcule, il ne se mémorise pas** : c'est le seul indicateur dont la valeur bouge sans qu'aucune décision n'ait été prise — un point de retour en plus, deux points de remise, un recrutement, une ouverture de marché à TVA plus élevée. **Les indicateurs 2 et 3 se lisent ensemble** : le nombre qui compte est leur écart, 2,90 ÷ 2,33 − 1 = +24,4 % à P5 ; c'est cet écart qu'il faut afficher, pas les deux valeurs côte à côte. **L'indicateur 6 utilise le CAC marginal, pas le nCAC** — c'est ce qui rend ce tableau différent de celui de tout le monde : le payback moyen de P5 est de 1,8 mois et il rassure, le marginal est de 4,35 mois et c'est lui qui borne ta vitesse. **Aucun ROAS de plateforme n'y figure**, et ce n'est pas un oubli.

---

## 11. Exercices

Formulaire vierge : [`E01-rendu.md`](../exercices/E01-rendu.md). Corrigé : [`E01-corrige.md`](../exercices/E01-corrige.md). Fais les calculs à la main avant d'ouvrir le corrigé — la valeur est dans le déroulé, pas dans le résultat.

### Exercice 1 — Recalcule les deux MER seuils de P3 (réponse numérique unique)

Données autorisées, et elles seules : canoniques § 2.1 (structure de coût P3), § 2.2 (CA HT et frais fixes P3), TVA 20 %.

1. Le taux de marge brute de P3, à partir des cinq postes de coût variable, avec deux décimales.
2. Le MER seuil de contribution (CM3 = 0).
3. Les frais fixes en % du CA HT de P3.
4. Le MER seuil d'EBITDA.
5. Le MER réel de P3 est 2,70 : exprime la marge de sécurité en pourcentage et retrouve la valeur du canonique § 2.3.
6. Raisonnement : de combien de points la marge brute de P3 pourrait-elle baisser avant qu'un MER de 2,70 ne suffise plus à atteindre l'équilibre d'EBITDA ?

*Contrôle :* tu dois retrouver 1,99 et 2,42 exactement.

### Exercice 2 — L'EBITDA de P5 si le taux de retour passe de 3,5 % à 5,5 % (réponse numérique unique)

Canoniques § 2.1 et § 2.2, palier P5. Tout le reste est inchangé : même CA, même dépense publicitaire, mêmes frais fixes.

1. Nouveau taux de marge brute.
2. Nouvelle marge brute mensuelle en euros.
3. Nouveau CM3 mensuel.
4. Nouvel EBITDA mensuel, et en % du CA HT.
5. Perte d'EBITDA annuelle ; vérifie-la par la voie courte, CA HT × 2 points × 12.
6. Nouveau MER seuil d'EBITDA, et nouvelle marge de sécurité contre le MER réel de 2,90.
7. Raisonnement : à quel taux de retour l'EBITDA de P5 devient-il nul ?

*Contrôle :* la perte annuelle doit être proche de 866 640 € et la marge de sécurité doit tomber sous 20 %.

### Exercice 3 — Ta cascade des marges (tes chiffres)

Reconstruis sur tes 90 derniers jours la cascade complète du § 1.1 : CA TTC, CA HT, CM1, CM2, CM3, EBITDA, chacun en euros et en % du CA HT. Contraintes : les remises apparaissent en ligne séparée ; les retours sont comptés par cohorte de commandes, pas par mois calendaire ; la publicité inclut production créative et honoraires d'agence, pas seulement le média.

Compare ta ligne CM2 au tableau du § 1.4. Grille de lecture : sous 50 % de marge brute avec un modèle publicitaire, ton MER seuil de contribution vaut au moins 1,20 ÷ 0,50 = 2,40 — un niveau que très peu de marques DTC tiennent durablement en prospection. Ce n'est pas un problème de publicité, c'est un problème de prix ou de coût produit. Modules [E03](E03-offre-et-prix.md) et [E02](E02-marche-et-produit.md).

### Exercice 4 — Ton tableau de sensibilité (tes chiffres)

Reproduis le tableau canonique § 7 avec tes nombres, en traitant chaque poste selon sa nature réelle comme au § 7.2 : proportionnel au CA, ou fixe par commande. Sept lignes : +10 % d'AOV à commandes constantes, +10 % de conversion, −10 % de CAC, +10 % de réachat, −10 % de COGS, −1 point de retours, −10 % de frais fixes.

En regard, écris honnêtement le nombre d'heures de direction que chaque levier a consommées le mois dernier. Grille de lecture : la part du temps consacrée à un levier devrait être du même ordre que sa part dans le total des gains. Un écart supérieur à ×3 est un problème d'allocation d'attention, et ce sont presque toujours le COGS et les frais fixes qui sur-consomment.

### Exercice 5 — Tes deux seuils et ton point mort (tes chiffres)

1. Ton MER seuil de contribution : (1 + ta TVA moyenne pondérée) ÷ ton taux de marge brute.
2. Ton MER seuil d'EBITDA — et note à côté le niveau de CA HT auquel il est valable.
3. Ton CM3 par commande, puis ton point mort en commandes par jour, méthode du § 7.4.
4. Écris trois nombres sur un post-it collé à ton écran : point mort en commandes/jour, MER seuil d'EBITDA, MER des 7 derniers jours.

Grille de lecture : si ton CM3 par commande est négatif, tu es en situation P1 et aucun volume ne te sauvera. Si ton volume réel est sous 1,5 fois ton point mort, tu n'as pas de réserve pour absorber un incident — hausse de CPM, rupture de stock, compte publicitaire suspendu ([C10](../etudes-de-cas/C10-compte-publicitaire-banni.md)).

### Exercice 6 — Décision : la septième tranche de budget

Ta marque ressemble à NØRA au palier P5 : LTV 12 mois en contribution 86,75 €, payback moyen 1,8 mois, MER blended 2,90, MER seuil d'EBITDA 2,33. Ton directeur de l'acquisition propose d'ajouter 100 000 € de budget mensuel sur un nouveau canal. Ses données de test sur trois semaines : **1 266 nouveaux clients pour 100 000 €**, soit un CAC marginal de 79,00 €. Ta trésorerie disponible est de 400 000 € et ton BFR augmente de 52 263 € par tranche de 100 000 € de CA mensuel supplémentaire (canonique § 4).

**Option A :** valider la tranche. **Option B :** la refuser et réallouer les 100 000 € sur les canaux existants.

Tranche, et justifie par des nombres. Ton raisonnement doit obligatoirement contenir le résultat sur 12 mois de la tranche, son payback marginal, et le besoin de trésorerie qu'elle crée avant le premier euro récupéré.

*Le corrigé donne la réponse, la condition exacte sous laquelle l'autre option devient la bonne, et le seul test qui permettrait de trancher pour de bon — celui du module [E09](E09-mesure-et-incrementalite.md).*

---

*Fin du module E01. Suite : [E02 — Choisir le terrain : marché, catégorie, produit](E02-marche-et-produit.md). E01 t'a donné les six nombres ; E02 et [E03](E03-offre-et-prix.md) déterminent lesquels tu peux réellement atteindre, parce que la marge brute et l'AOV se décident au moment du choix du produit et du prix — pas après.*
