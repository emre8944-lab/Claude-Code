# Niveau L01 — Initié

> **Prérequis :** niveau [L00](L00-novice.md) validé — 80 / 100, sans question éliminatoire ratée.
> **Ce que tu sais faire à la sortie :**
> — tu construis, à partir d'un relevé bancaire et d'un export de commandes, la cascade complète CA TTC → CA HT → CM1 → CM2 → CM3 → EBITDA, en euros et en pourcentage du CA HT, et tu désignes l'étage où l'argent se perd ;
> — tu calcules les deux MER seuils, tu les compares au MER réel et tu prononces un verdict qui dit s'il faut accélérer, tenir ou couper ;
> — tu repères les trois erreurs de calcul les plus fréquentes du métier dans un document produit par quelqu'un d'autre, tu les corriges, et tu chiffres ce que chacune coûte par an.
>
> **Temps de travail typique :** 20 à 28 h — 6 h de lecture, 3 h d'étude de cas, 8 à 14 h d'atelier, 1 h 30 d'épreuve.

---

## 0. Les deux échelles — rappel, parce que c'est ici qu'on commence à confondre

| Échelle | Ce qu'elle mesure | Ce qui la fait monter |
|---|---|---|
| **Lxx** | Ta **compétence** | Une épreuve réussie sur un dossier inconnu |
| **Nx** | L'état de ton **business** | Ton chiffre d'affaires et tes indicateurs mesurés ([diagnostic](../mentorat/diagnostic.md)) |

À L00 la confusion était théorique. À L01 elle devient opérationnelle : c'est le niveau où l'on commence à savoir lire un compte, donc à croire qu'on sait piloter.

**On peut être L07 sans entreprise.** On peut aussi être **N3 avec une compétence L04** : 500 000 € TTC par mois, dix personnes, et personne dans l'entreprise qui ait jamais calculé un CAC marginal. C'est le cas le plus dangereux du métier et le plus répandu, parce que rien dans les tableaux de bord ne le signale. Le chiffre d'affaires monte, les recrutements suivent, la structure de coût se fige — et l'erreur de lecture, elle, se multiplie par le volume.

L'épreuve de ce niveau met en scène exactement cette situation : une marque qui vend bien, un directeur financier qui produit une note propre, et trois erreurs qui, ensemble, transforment « nous perdons 760 € par mois » en « doublons le budget média ».

**Garde ton niveau L au-dessus de ton niveau N.** Un L01 dans une entreprise N2 sait lire ; c'est déjà beaucoup, et ce n'est pas encore savoir décider — la décision d'allocation, c'est [L04](L04-acquéreur.md).

---

## 1. Les compétences du niveau

1. **Je construis une cascade de marges complète** à partir de données brutes — commandes, panier, taux de coût variables, dépense publicitaire, frais fixes — en euros **et** en pourcentage du CA HT, les deux colonnes cohérentes entre elles.
2. **Je désigne l'étage où l'argent se perd** et son responsable, sans confondre un problème de marge brute, un problème d'acquisition et un problème de structure.
3. **Je calcule le MER seuil de contribution** `(1 + TVA) ÷ marge brute` et **le MER seuil de résultat nul** `(1 + TVA) ÷ (marge brute − frais fixes en % du CA HT)`, et j'explique pourquoi le premier ne dépend pas de la taille et le second si.
4. **Je prononce un verdict en trois états** — sous le seuil de contribution : arrêter de scaler aujourd'hui ; entre les deux seuils : investissement légitime seulement si le réachat le rembourse ; au-dessus du seuil de résultat : question de volume marginal.
5. **Je calcule un nCAC, une contribution de première commande et une marge à la première commande**, et je dis à quelle condition une marge négative est rationnelle.
6. **Je calcule une LTV à 12 mois en marge de contribution** depuis un tableau de cohorte, et le payback du CAC par interpolation.
7. **Je repère les trois erreurs de calcul les plus fréquentes** dans un document que je n'ai pas écrit — la part de la publicité en `1 ÷ MER`, la LTV en chiffre d'affaires, le CAC divisé par toutes les commandes — et je chiffre chacune en euros par an.
8. **Je distingue un MER seuil d'un MER cible.** Le seuil est une propriété de la structure de coût ; la cible est une décision de pilotage, toujours au-dessus, et l'écart entre les deux est ta marge de sécurité.

---

## 2. Ce que tu lis

| Ordre | Lecture | Ce que ça apporte **à ce niveau précisément** |
|---|---|---|
| 1 | [**E01 — L'arithmétique de la marque**](../modules/E01-arithmetique-de-la-marque.md), **en entier** | Le module central du cursus. § 1 la cascade et ses responsables ; § 2 le piège TTC/HT chiffré ; § 3 la sur-attribution et la décomposition du MER ; § 4 les deux seuils, démontrés ; § 5 le nCAC et le CAC marginal ; § 6 la LTV en contribution, l'horizon 12 mois, le payback ; § 7 la sensibilité. **Fais les sept exercices.** |
| 2 | [**C01 — Le produit à ×2,5 qui ne pouvait pas gagner**](../etudes-de-cas/C01-coefficient-insuffisant.md) | Le même appareil de calcul sur une marque dont la structure interdit l'objectif. Un MER seuil peut être **inatteignable** — et la question n'est alors plus « comment optimiser » mais « changer de produit ou changer d'objectif ». Première fois du parcours où le calcul dit d'arrêter. |
| 3 | [Chiffres canoniques](../donnees/chiffres-canoniques.md) **§ 2.1 à § 2.3**, le calcul en main | Recalcule les dix MER seuils toi-même : dix divisions, dix contrôles. Tant que tu ne les as pas retrouvés, tu n'as pas lu ce tableau, tu l'as regardé. |

---

## 3. Ce que tu fais

| Travail | Livrable attendu |
|---|---|
| **[Atelier S01 — Choisir le terrain](../atelier/S01-choisir-le-terrain.md)** | La décision de catégorie écrite : douze candidates, filtre structurel, grille à 9 critères sur les trois finalistes, cascade complète du finaliste jusqu'au MER seuil. Note-toi sur la grille de la section 6 **avant** d'ouvrir le corrigé exemplaire. |
| **[Atelier S02 — Prouver la demande](../atelier/S02-prouver-la-demande.md)** | Les six tests de demande, chacun avec **son seuil écrit et daté avant le lancement**. Le livrable n'est pas le résultat des tests : c'est le document de seuils, signé avant la moindre donnée. |
| **Reconstruire les cinq paliers canoniques** — à partir du seul § 2 (volumes) et § 2.1 (structure de coût), retrouve le § 2.2 et le § 2.3. | Un tableau de ta main. Écart toléré : 1 € sur l'EBITDA de chaque palier, dû aux arrondis. Si tu ne retombes pas dessus, tu as un trou dans la cascade, et tu sais lequel. |
| **Le simulateur, mode `--comparer`** — `python3 ecommerce/outils/simulateur_marque.py --comparer` | Une page d'analyse écrite : quelle stratégie survit, laquelle meurt, à quel mois, et **par quel étage de la cascade** la mort arrive. |
| **[E01 exercices 1 à 7](../modules/E01-arithmetique-de-la-marque.md)** | Les réponses numériques déroulées pour NØRA, la grille de lecture remplie pour ton activité, et pour l'exercice de décision : la réponse **et** la condition sous laquelle l'autre option serait la bonne. |

---

## 4. L'épreuve

> **Cas fictif. Marque fictive.** VELDA est inventée pour cette épreuve. Les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.

**Temps imparti : 1 h 30.** Calculatrice et tableur autorisés. Aucun document, aucune formule sous les yeux. **Barème sur 100.**

### 4.1 Le dossier

VELDA vend un complément alimentaire pour le sommeil, en direct au consommateur, en France uniquement. Seizième mois d'activité. TVA 20 %.

**Activité des 30 derniers jours**

| Donnée | Valeur |
|---|---|
| Commandes livrées | 4 200 |
| Panier moyen mixte | 58,00 € TTC |
| Dont commandes de **nouveaux** clients | 2 800, panier moyen 52,00 € TTC |
| Dont commandes de clients **déjà acquis** | 1 400, panier moyen 70,00 € TTC |
| Dépense publicitaire totale (toutes régies, production créative et honoraires inclus) | 87 000 € |
| Frais fixes mensuels (salaires chargés, loyer, outils, honoraires) | 31 500 € |

**Structure de coût variable, mesurée sur les 30 derniers jours, en % du CA HT**

| Poste | % du CA HT |
|---|---:|
| Coût marchandise rendu entrepôt (COGS) | 18,00 % |
| Logistique complète (préparation, emballage, transport, retour physique) | 13,50 % |
| Frais du prestataire de paiement (PSP) | 1,70 % |
| Retours, casse et gestes commerciaux | 2,60 % |
| Remises, codes promo et codes créateurs | 6,20 % |

**Cohorte de 1 000 clients acquis il y a 12 mois — contribution cumulée par client**

| Mois écoulés | 1 | 3 | 6 | 12 |
|---|---:|---:|---:|---:|
| Contribution cumulée par client | 25,13 € | 36,50 € | 46,80 € | 57,27 € |
| Commandes cumulées par client | 1,00 | 1,38 | 1,67 | 1,95 |

**Trésorerie**

| Donnée | Valeur |
|---|---|
| Trésorerie disponible | 96 000 € |
| Consommation nette de trésorerie du dernier mois | 12 400 € |

**Hypothèse de rendement décroissant de l'acquisition**, fournie par le responsable média et à prendre pour argent comptant : sur la prochaine tranche de 43 500 € de budget mensuel, le **CAC marginal** serait de 46,00 € ; sur la tranche suivante de 43 500 €, de 58,00 €.

### 4.2 La note du directeur financier

> **NOTE DE SYNTHÈSE — 30 derniers jours**
> *Direction financière, VELDA*
>
> 1. Chiffre d'affaires du mois : **243 600 € TTC**.
> 2. Notre MER blended s'établit à **2,80**.
> 3. La publicité pèse donc `1 ÷ 2,80 = 35,7 %` de notre chiffre d'affaires. C'est un très bon niveau pour notre secteur.
> 4. Notre taux de marge brute est de **58,0 %**.
> 5. Nos frais fixes sont de **31 500 €** par mois.
> 6. Notre CAC ressort à `87 000 ÷ 4 200 = 20,71 €` par client.
> 7. Notre LTV à 12 mois est de `1,95 commande × 58,00 € = 113,10 €`, soit un ratio LTV/CAC de `113,10 ÷ 20,71 = 5,46`.
> 8. Le diagnostic du cursus indique qu'au-dessus de 5,0 on sous-investit. **Recommandation : doubler le budget média dès le mois prochain**, de 87 000 € à 174 000 €.

**Trois des huit affirmations de cette note contiennent une erreur de calcul.** Les cinq autres sont exactes.

### 4.3 Les questions

**Q1 — La cascade complète (25 points).**
Construis la cascade de VELDA sur les 30 derniers jours, **en euros et en pourcentage du CA HT**, de CA TTC jusqu'à l'EBITDA, avec les étages CM1, CM2 et CM3 nommés. Termine par une phrase : à quel étage l'argent se perd-il, et qui en répond ?

**Q2 — Les seuils (15 points).**
Calcule le MER réel, le MER seuil de contribution (CM3 = 0) et le MER seuil de résultat nul (EBITDA = 0). Donne l'écart en pourcentage entre le MER réel et le seuil de résultat nul. Puis explique en trois lignes pourquoi le premier seuil ne dépend pas du niveau de chiffre d'affaires et le second si.

**Q3 — L'acquisition (10 points).**
Calcule le nCAC, la contribution de la première commande d'un nouveau client, et la marge à la première commande. Dis en une phrase à quelle condition le signe obtenu est acceptable.

**Q4 — La cohorte (12 points).** *(Question éliminatoire.)*
Donne la LTV à 12 mois en marge de contribution, le ratio LTV/CAC à 12 mois, et le délai de récupération du CAC (payback) par interpolation linéaire sur le tableau de cohorte. Situe le ratio obtenu dans la grille de lecture du cursus.

**Q5 — Les trois erreurs (24 points, 8 points chacune).**
Identifie les trois affirmations fausses de la note du directeur financier. Pour chacune : **(a)** cite le numéro de l'affirmation et nomme l'erreur ; **(b)** donne le calcul correct ; **(c)** chiffre ce que l'erreur coûte ou fausse, en euros par an ou en facteur d'écart.

**Q6 — Le verdict et la décision (14 points).**
En dix lignes maximum : VELDA gagne-t-elle ou perd-elle de l'argent, et de combien ? Faut-il suivre la recommandation du point 8 de la note ? Justifie par le calcul, en utilisant l'hypothèse de CAC marginal fournie, et donne l'effet de la décision sur la trésorerie.

---

## 5. Le corrigé

### Q1 — La cascade complète (25 points)

```
CA TTC        4 200 × 58,00                        =  243 600 €     120,00 %
TVA           243 600 × 0,20 ÷ 1,20                =  − 40 600 €    − 20,00 %
CA HT         243 600 ÷ 1,20                       =  203 000 €     100,00 %
COGS          203 000 × 18,00 %                    =  − 36 540 €    − 18,00 %
CM1                                                =  166 460 €      82,00 %
Logistique    203 000 × 13,50 %                    =  − 27 405 €    − 13,50 %
PSP           203 000 ×  1,70 %                    =  −  3 451 €    −  1,70 %
Retours/SAV   203 000 ×  2,60 %                    =  −  5 278 €    −  2,60 %
Remises       203 000 ×  6,20 %                    =  − 12 586 €    −  6,20 %
CM2 — MARGE BRUTE                                  =  117 740 €      58,00 %
Publicité                                          =  − 87 000 €    − 42,86 %
CM3                                                =   30 740 €      15,14 %
Frais fixes                                        =  − 31 500 €    − 15,52 %
EBITDA                                             =   −  760 €    −  0,37 %
```

Contrôles : somme des coûts variables `18,00 + 13,50 + 1,70 + 2,60 + 6,20 = 42,00 %`, donc marge brute `100 − 42 = 58,00 %` ✓. En euros : `36 540 + 27 405 + 3 451 + 5 278 + 12 586 = 85 260 €`, et `203 000 − 85 260 = 117 740 €` ✓. Part de la publicité : `87 000 ÷ 203 000 = 42,86 %`, à comparer à `1,20 ÷ 2,80 = 42,86 %` ✓ — deux routes, un seul nombre.

**Où l'argent se perd, et qui en répond.** Nulle part et partout : aucun étage n'est catastrophique, l'EBITDA est négatif de 0,37 point. La marge brute à 58,00 % est correcte pour un complément alimentaire — le modèle de référence est à 58,8 % au palier P2. Deux étages à surveiller : la ligne **remises à 6,20 %** — opérations et commerce conjointement, revue hebdomadaire — et les **frais fixes à 15,52 % du CA HT** contre 14,6 % au P2 canonique, dont le dirigeant répond seul. Réponse la plus juste : **VELDA n'a pas un problème de marge, elle a un problème de taille.** À structure de coût et à MER identiques, la marge de contribution vaut 15,14 % du CA HT, donc l'équilibre demande `31 500 ÷ 0,1514 = 208 018 €` de CA HT : il lui manque **environ 5 000 € de CA HT par mois, soit 2,5 %**.

*Barème.* 8 points la colonne en euros ; 8 points la colonne en % du CA HT ; 5 points les trois étages CM1, CM2, CM3 nommés et placés ; 4 points la conclusion. **−4 points** par ligne oubliée. **Éliminatoire** si le CA HT est obtenu en retranchant 20 % au TTC (194 880 € au lieu de 203 000 €), ou si une marge est calculée sur le TTC.

### Q2 — Les seuils (15 points)

```
MER réel                    = 243 600 ÷ 87 000                = 2,80

MER seuil (CM3 = 0)         = 1,20 ÷ 0,5800                   = 2,07
MER seuil (EBITDA = 0)      :
   frais fixes en % du CA HT = 31 500 ÷ 203 000               = 15,52 %
   marge brute − frais fixes = 58,00 % − 15,52 %              = 42,48 %
   seuil                     = 1,20 ÷ 0,4248                  = 2,82

Écart au seuil de résultat  = 2,80 ÷ 2,82 − 1                 = − 0,9 %
```

Contrôle du seuil de résultat : à MER 2,8247, la dépense publicitaire vaudrait `243 600 ÷ 2,8247 = 86 239 €`, et `117 740 − 86 239 = 31 501 €`, soit exactement les frais fixes ✓.

**Pourquoi l'un dépend de la taille et pas l'autre.** Le seuil de contribution s'obtient en posant `m × CA HT − pub = 0`. Le chiffre d'affaires apparaît des deux côtés et se simplifie : il ne reste que la TVA et la marge brute. C'est ce qui rend ce seuil utilisable dès la première commande. Le seuil de résultat, lui, fait intervenir des frais fixes exprimés **en euros** ; les ramener en pourcentage du CA HT réintroduit le chiffre d'affaires au dénominateur. Conséquence à connaître : **en décroissance, ce seuil monte pendant que le chiffre d'affaires baisse.** Si le CA HT de VELDA reculait de 20 %, les frais fixes passeraient à 19,40 % du CA HT et le seuil à `1,20 ÷ (0,58 − 0,194) = 3,11` — la ligne de flottaison recule plus vite que le nageur.

*Barème.* 3 points le MER réel ; 3 points le seuil de contribution ; 4 points le seuil de résultat avec le calcul de `f` ; 2 points l'écart ; 3 points l'explication. **Éliminatoire** si un seuil est calculé avec `1 ÷ m` au lieu de `1,20 ÷ m`.

### Q3 — L'acquisition (10 points)

```
nCAC = 87 000 ÷ 2 800                                        = 31,07 €

Contribution de la 1ʳᵉ commande
   = AOV nouveaux clients HT × marge brute
   = (52,00 ÷ 1,20) × 0,5800 = 43,3333 × 0,5800              = 25,13 €

Marge à la 1ʳᵉ commande = 25,13 − 31,07                      = − 5,94 €
```

Sur les 2 800 nouveaux clients du mois, cela représente `2 800 × 5,94 = 16 632 €` de perte à la première commande.

**Condition d'acceptabilité.** Une marge négative à la première commande est normale — le modèle de référence est entre −4,93 € et −7,26 € à tous ses paliers. Elle n'est acceptable qu'à trois conditions cumulées : la LTV à 12 mois couvre le nCAC **plus** les frais fixes par nouveau client (`31 500 ÷ 2 800 = 11,25 €`, donc il faut `LTV ≥ 42,32 €`) ; la trésorerie tient la perte cumulée plus le besoin en fonds de roulement ; et le taux de réachat en dessous duquel on coupe a été écrit à l'avance. Ici la première condition est remplie — `57,27 € ≥ 42,32 €` — avec une marge de 35 %.

*Barème.* 3 points le nCAC ; 3 points la contribution ; 2 points la marge ; 2 points la condition. **−3 points** si le nCAC est calculé sur les 4 200 commandes. **−2 points** si la contribution utilise l'AOV mixte de 58,00 € (28,03 €, perte minorée de 49 %).

### Q4 — La cohorte (12 points) — éliminatoire

```
LTV 12 mois en contribution   = 57,27 €    (lecture directe du tableau)

Contrôle par construction :
   contribution par réachat = (70,00 ÷ 1,20) × 0,5800        = 33,83 €
   25,13 + (1,95 − 1,00) × 33,83 = 25,13 + 32,14             = 57,27 €   ✓

LTV / CAC à 12 mois           = 57,27 ÷ 31,07                 = 1,84

Payback — interpolation entre le mois 1 (25,13 €) et le mois 3 (36,50 €) :
   (31,07 − 25,13) ÷ (36,50 − 25,13) = 5,94 ÷ 11,37           = 0,522
   payback = 1 + 0,522 × 2                                    = 2,04 mois
```

**Lecture.** Un ratio de 1,84 tombe dans la zone **1,3 à 2,0 : fragile**. On peut croître, lentement et sans à-coups, en surveillant la trésorerie ; on ne double pas un budget. Le payback de 2,0 mois est bon — sous le seuil de 4 mois — mais il est calculé sur le nCAC **moyen** ; la question du Q6 porte sur le CAC **marginal**, qui est un autre nombre et donne un autre payback.

*Barème.* 4 points la LTV en contribution ; 3 points le ratio ; 3 points le payback avec l'interpolation écrite ; 2 points la lecture. **Éliminatoire** si la LTV est donnée en chiffre d'affaires (`1,95 × 58,00 = 113,10 €`).

### Q5 — Les trois erreurs (24 points)

**Erreur n° 1 — affirmation 3 : la part de la publicité, calculée sans la TVA.**

```
Écrit  : 1 ÷ 2,80          = 35,7 %
Correct: 1,20 ÷ 2,80       = 42,86 % du CA HT
Contrôle : 87 000 ÷ 203 000 = 42,86 %                          ✓

Écart = 0,20 ÷ 2,80 = 7,14 points de CA HT
      = 203 000 × 0,0714 = 14 500 € par mois
   ou, plus court, 87 000 ÷ 6 = 14 500 €   — un sixième de la dépense pub
      = 174 000 € par an
```
Le directeur financier croit disposer de 7,14 points de marge qu'il n'a pas. Face à un EBITDA réel de −760 € par mois, l'erreur est décisive à elle seule : elle transforme une perte en un résultat apparent de +13 740 € par mois. **La formulation « de notre chiffre d'affaires » est en outre ambiguë** — le MER se lit sur du TTC, la marge sur du HT ; un pourcentage de chiffre d'affaires sans mention de base est une donnée manquante.

**Erreur n° 2 — affirmation 6 : un CAC blended présenté comme un CAC.**

```
Écrit  : 87 000 ÷ 4 200 commandes    = 20,71 €
Correct: 87 000 ÷ 2 800 NOUVEAUX     = 31,07 €     (nCAC)

Sous-estimation : 10,36 € par client, soit un facteur ×1,50
```
Le dénominateur inclut 1 400 commandes de clients déjà acquis, que la publicité n'a pas eu à conquérir. Le vice de ce nombre n'est pas seulement qu'il est faux : c'est qu'il **s'améliore mécaniquement quand la part de réachat monte**. VELDA verra son « CAC » baisser au moment exact où son acquisition se dégradera.

**Erreur n° 3 — affirmation 7 : une LTV en chiffre d'affaires, divisée par un CAC déjà faux.**

```
Écrit  : 1,95 × 58,00 = 113,10 €, ratio 113,10 ÷ 20,71 = 5,46
Correct: 57,27 € de contribution, ratio 57,27 ÷ 31,07  = 1,84

Décomposition du facteur d'erreur :
   LTV en CA au lieu de contribution : 113,10 ÷ 57,27 = ×1,97
   CAC blended au lieu de nCAC       :  31,07 ÷ 20,71 = ×1,50
   Effet combiné                     : 1,97 × 1,50    = ×2,96
   Contrôle : 5,46 ÷ 1,84                             = ×2,97   ✓ (arrondis)
```
Trois vices dans cette seule ligne : l'AOV mixte de 58,00 € est utilisé alors que la cohorte mélange une première commande à 52,00 € et des réachats à 70,00 € ; le montant est du TTC, donc il contient de la TVA ; il est brut, donc il ne retranche ni le COGS, ni la logistique, ni le paiement, ni les retours, ni les remises. **Les deux erreurs se composent dans le même sens.** Personne ne se trompe jamais en sous-estimant sa LTV ni en surestimant son CAC : le biais ne s'annule pas dans la moyenne des décisions, il s'accumule.

*Barème par erreur.* 3 points l'identification (numéro et nom de l'erreur) ; 3 points le calcul correct ; 2 points le chiffrage de l'écart. **Ne pas trouver l'erreur n° 1 est éliminatoire.** Signaler comme fausse l'une des cinq affirmations exactes coûte 4 points : accuser au hasard n'est pas une méthode.

*Note sur l'affirmation 8.* Elle n'est pas comptée comme erreur de **calcul** — la règle citée existe bien : au-dessus de 5,0, un ratio LTV/CAC signale un sous-investissement. C'est une **conclusion fausse tirée d'un chiffre faux**, et c'est le sujet du Q6.

### Q6 — Le verdict et la décision (14 points)

**VELDA perd de l'argent, très peu : −760 € par mois, soit −0,37 % du CA HT.** Elle est au-dessus de son seuil de contribution (2,80 contre 2,07) — chaque euro de CA supplémentaire apporte 58 centimes de marge brute — mais 0,9 % sous son seuil de résultat (2,80 contre 2,82). Elle finance sa structure avec son capital, pour un montant faible.

**Non, il ne faut pas doubler le budget.** Trois raisons, dans l'ordre de force.

*1. Le vrai ratio interdit l'accélération.* 1,84, pas 5,46. La grille de lecture range 1,3 à 2,0 dans « fragile : croissance lente, surveillance du cash ». La recommandation du point 8 s'appuie sur un nombre qui vaut 2,96 fois le vrai.

*2. Les tranches marginales ne se remboursent pas dans les délais.*
```
Seuil de valeur d'une tranche marginale, tout compris, sur 12 mois :
   CAC marginal maximal = LTV 12 mois − frais fixes par nouveau client
                        = 57,27 − (31 500 ÷ 2 800 = 11,25)      = 46,02 €

Tranche 1 — 43 500 € à 46,00 € de CAC marginal
   nouveaux clients      = 43 500 ÷ 46,00                       =   946
   valeur créée à 12 mois= 946 × (57,27 − 46,00 − 11,25)        =  + 19 €
   payback marginal, interpolé entre le mois 3 et le mois 6 :
      (46,00 − 36,50) ÷ (46,80 − 36,50) = 0,922
      3 + 0,922 × 3                                             = 5,77 mois

Tranche 2 — 43 500 € à 58,00 € de CAC marginal
   nouveaux clients      = 43 500 ÷ 58,00                       =   750
   valeur créée à 12 mois= 750 × (57,27 − 58,00 − 11,25)        = − 8 985 €
   payback marginal : la contribution cumulée à 12 mois (57,27 €)
   ne rattrape jamais le CAC de 58,00 €                         = jamais
```
La première tranche est exactement à l'équilibre — 19 € de valeur créée sur 43 500 € engagés, c'est-à-dire rien — et son payback de 5,8 mois dépasse déjà la limite de 4 mois. La seconde détruit 8 985 € sur douze mois et ne se rembourse jamais. **Doubler le budget, c'est acheter 1 696 clients pour perdre environ 9 000 € et immobiliser 87 000 € de plus par mois.**

*3. La trésorerie ne le permet pas.*
```
Aujourd'hui : 96 000 ÷ (12 400 ÷ 4,33)                          = 33,5 semaines

Après doublement — estimation généreuse, en créditant les clients marginaux
de la contribution de première commande des clients actuels (25,13 €) :
   contribution immédiate des 1 696 nouveaux clients            = 42 620 €
   surcoût net de trésorerie = 87 000 − 42 620                  = 44 380 €
   consommation mensuelle    = 12 400 + 44 380                  = 56 780 €
   autonomie = 96 000 ÷ (56 780 ÷ 4,33)                         =  7,3 semaines
```
De 33,5 à 7,3 semaines en un mois. Sous 13 semaines, tu n'as plus de stratégie, tu as une contrainte. Et l'estimation est **généreuse** : le trafic marginal convertit moins bien et à panier plus faible, donc la contribution immédiate réelle serait inférieure.

**Ce qu'il faut faire à la place.** Il manque 760 € par mois. La ligne remises pèse 6,20 % du CA HT, soit 12 586 € : **un point et demi de remise récupéré vaut 3 045 € par mois**, quatre fois le déficit, sans un euro de média ni de trésorerie engagé. Premier chantier. Le second est le CAC marginal lui-même — 46,00 € puis 58,00 € contre 31,07 € de moyenne signalent une saturation du ciblage, qui se traite par la machine créative, pas par le budget.

*Barème.* 3 points le verdict chiffré ; 3 points le refus argumenté par le ratio corrigé ; 4 points le calcul des tranches marginales ; 2 points l'effet trésorerie ; 2 points la contre-proposition chiffrée. Répondre « oui, il faut doubler » plafonne le Q6 à 0, quelle que soit la qualité du calcul qui suit.

---

## 6. Le critère de passage

| | |
|---|---|
| **Note minimale** | **75 / 100** |
| **Questions éliminatoires** | **Q4** — une LTV donnée en chiffre d'affaires. **Q1 ou Q2** — un CA HT obtenu en retranchant la TVA, ou un seuil calculé en `1 ÷ m`. **Q5** — ne pas avoir identifié l'erreur n° 1 (la part de la publicité). |
| **Temps** | 1 h 30. Au-delà de 1 h 45, épreuve échouée. |

Le seuil descend de 80 à 75 parce que la nature de l'épreuve change. À L00 on mesurait des automatismes, où 70 % n'a pas de sens. À L01 on mesure une construction : quatorze lignes de cascade, quatre seuils, trois erreurs à débusquer. Une copie à 75 % tient debout avec des scories ; une copie à 60 % se trompe de diagnostic. Les éliminatoires, elles, ne bougent pas : elles couvrent les trois fautes qui produisent la décision **inverse** de la bonne, et une décision inverse ne s'améliore pas parce que le reste du dossier était bien tenu.

**En cas d'échec :** reprends E01 § 1, § 2 et § 6, refais les cinq cascades canoniques à la main jusqu'à retomber à l'euro près, et repasse une **variante** du dossier — mêmes mécanismes, autres chiffres, autres erreurs plantées.

---

## 7. Les pièges de ce niveau

**1. « J'ai une marge brute de 58 %, donc je gagne de l'argent. »** La marge brute ne dit rien du résultat. VELDA a 58,00 % de marge brute et perd de l'argent ; une marque à 52 % avec des frais fixes à 8 % du CA HT en gagne. Le nombre qui décide n'est jamais un étage seul, c'est **la distance entre ton MER réel et ton seuil de résultat**.

**2. Confondre le seuil de contribution et le seuil de résultat.** C'est l'erreur la plus fréquente à ce niveau exactement, parce qu'on vient d'apprendre à calculer le premier et qu'il est plus facile. Le seuil de contribution répond à « dois-je arrêter de dépenser aujourd'hui ? ». Le seuil de résultat répond à « est-ce que je gagne ma vie ? ». Passer le premier et rater le second est une situation ordinaire, parfois volontaire — c'est le cas des paliers P1 et P2 du modèle de référence — mais elle ne se déclare pas « rentable ».

**3. Confondre un seuil et une cible.** Le seuil est une propriété de la structure de coût : il ne se négocie pas. La cible est une décision de pilotage, toujours au-dessus du seuil, et l'écart entre les deux est ta marge de sécurité. Piloter **sur** son seuil, c'est piloter sans marge d'erreur, un mois où la logistique dérape de deux points.

**4. Lire le mois au lieu de la cohorte.** Le compte de résultat mensuel d'une marque en croissance additionne des cohortes jeunes, qui n'ont livré qu'une commande, et leur fait porter des frais fixes calibrés pour la taille future. Il dit la vérité sur la trésorerie et ment sur le rendement. Les deux lectures sont nécessaires ; les confondre fait soit couper une acquisition rentable, soit financer une hémorragie.

**5. Croire que les remises sont une réduction de prix et non un coût.** Tant que la remise se dissout dans le prix moyen, elle n'a pas de responsable, elle n'a pas de ligne, elle n'est jamais défendue — et elle devient le levier de secours universel de tout le monde dans l'entreprise. Sur VELDA elle vaut 12 586 € par mois, seize fois le déficit.

**6. Croire qu'avoir trouvé les erreurs du directeur financier signifie qu'on en sait plus que lui.** Non : qu'on applique une méthode qu'il n'applique pas. Il connaît probablement mieux que toi la fiscalité et le financement. Ce que L01 installe, c'est le jeu de contrôles qui rend une note de synthèse vérifiable en trois divisions — et le jour où tu produiras la note, quelqu'un devra pouvoir faire pareil sur la tienne.

**7. Croire que savoir lire, c'est savoir décider.** L01 te rend capable de dire « ne double pas ». Pas de dire **où** mettre le budget, ni de distinguer un CAC marginal d'une saturation créative, ni de savoir si un canal est incrémental : ce sont [L04](L04-acquéreur.md), L05 et L07. Le danger propre à ce niveau est la confiance — on y comprend assez pour avoir des convictions, pas encore assez pour savoir lesquelles sont fausses.

**8. Croire que la structure se rattrape à l'échelle.** Le seuil de contribution passe de 2,10 à 1,95 entre le premier euro et 1 M€ TTC par semaine : 7 % pour dix ans de croissance. Si ton produit ne supporte pas un MER de 2,0, il ne le supportera pas mieux à 40 M€ de chiffre d'affaires — leçon de [C01](../etudes-de-cas/C01-coefficient-insuffisant.md), et sujet du niveau suivant.

> **À retenir :** un verdict L01 tient en trois nombres — le MER réel, le seuil de contribution, le seuil de résultat — et en une phrase qui dit lequel des trois états tu occupes. Si ton diagnostic prend plus d'une page, tu n'as pas diagnostiqué, tu as décrit.

---

*Fin du niveau L01. Suite : [L02 — Praticien](L02-praticien.md), où tu cesses de lire une structure pour en choisir une.*
