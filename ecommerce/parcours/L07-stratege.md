# Niveau L07 — Stratège

> **Prérequis :** niveau L06 validé.
>
> **Ce que tu sais faire à la sortie :**
> 1. Tu conçois un test géographique complet — appariement, puissance calculée d'avance, seuils de décision écrits et signés avant la première coupe — et tu sais dire quand il ne faut pas le lancer.
> 2. Tu détectes une cellule témoin contaminée, tu chiffres la contamination avec une zone de contrôle réservée, et tu corriges le lift au lieu de le rejeter.
> 3. Tu alloues au CAC incrémental **marginal** rapporté à l'horizon de LTV que ta trésorerie sait financer, et tu chiffres la réallocation en euros d'EBITDA mensuel.
>
> **Temps de travail typique :** 20 à 28 heures. Le niveau contient peu de lecture et beaucoup de calcul : c'est le seul du parcours dont la compétence centrale est de **refuser un chiffre**.

> **Lxx mesure ta compétence. Nx mesure l'état de ton business.** Les deux échelles sont indépendantes : un analyste peut être L07 sans posséder de marque, et une marque **N3** ou **N4** peut être pilotée par une compétence **L04** — quelqu'un qui lit des tableaux de bord de régie et croit y voir des causes. **C'est le cas le plus dangereux du métier**, et à ce niveau il prend une forme particulière : plus la marque grandit, plus les canaux qui s'auto-attribuent le mieux captent de budget, et **plus l'erreur d'allocation grandit avec le chiffre d'affaires**. Une marque N4 pilotée à l'attribution ne se trompe pas un peu plus qu'une N2 : elle se trompe de dix à vingt fois plus, en euros ([diagnostic](../mentorat/diagnostic.md)).

---

## 1. Les compétences du niveau

1. **Je distingue attribution et incrémentalité** en une phrase opérationnelle : l'attribution répartit un résultat déjà obtenu, l'incrémentalité mesure ce qui ne serait pas arrivé sans la dépense.
2. **Je constitue des paires de zones** sur 26 semaines d'historique quotidien, et je refuse de lancer sous `ρ = 0,80` en pré-test.
3. **Je calcule la puissance avant le test** avec `D ≥ [2,80 × CV × √(2(1−ρ)) ÷ e]²`, et je renonce quand l'effet détectable minimum dépasse l'effet sur lequel j'agirais.
4. **J'écris les seuils de décision avant la première coupe** et je les fais signer — seule protection contre l'interprétation *a posteriori*.
5. **Je repère une cellule contaminée** par un indice de période construit sur une zone de contrôle réservée, et je chiffre la contamination au lieu de la deviner.
6. **Je lis l'intervalle avant le z** : un test d'incrémentalité donne un ordre de grandeur et un signe, jamais une décimale.
7. **Je convertis un effet mesuré en décision** en rapportant les **clients** non acquis à leur LTV, jamais le chiffre d'affaires perdu à la dépense épargnée.
8. **J'alloue au CAC incrémental marginal**, comparé à la LTV que ma trésorerie sait financer — 12 mois si je m'autofinance, 24 si j'ai le BFR pour tenir.
9. **Je sais dire « je ne sais pas »** quand un test non significatif ne prouve rien, au lieu de le lire comme une preuve d'absence d'effet.

---

## 2. Ce que tu lis

| # | Lecture | Ce qu'elle apporte **à ce niveau** |
|---|---|---|
| 1 | [**E09**](../modules/E09-mesure-et-incrementalite.md) § 1 à § 3 | Pourquoi l'attribution est structurellement fausse, la sur-attribution de 11 % au minimum ([canoniques § 5](../donnees/chiffres-canoniques.md)), et les trois biais qui font paraître un canal meilleur qu'il n'est. |
| 2 | [**E09**](../modules/E09-mesure-et-incrementalite.md) § 5 | Le protocole du test géographique, la formule de puissance, et l'exemple chiffré complet — **le cœur de l'épreuve**. |
| 3 | [**E09**](../modules/E09-mesure-et-incrementalite.md) § 6 | CAC incrémental contre CAC attribué, la règle `ROAS incrémental > MER seuil de contribution`, et le § 6.4 : on alloue au **marginal**. |
| 4 | [**E09**](../modules/E09-mesure-et-incrementalite.md) § 7.6 | Le bruit : combien de variation est normale. C'est ce paragraphe qui t'évitera de réagir à une semaine. |
| 5 | [**C06**](../etudes-de-cas/C06-test-incrementalite.md) | Le test qui a supprimé 22 % du budget sans perdre de chiffre d'affaires, déroulé de la conception à la décision. |

---

## 3. Ce que tu fais

**Un seul travail, et il est long : concevoir un test géographique complet**, sur ta propre marque si tu en as une, sur le dossier fourni sinon. Le livrable tient en six pièces, et il se rend **avant** d'avoir dépensé un euro.

| Pièce | Contenu | Le critère de recevabilité |
|---|---|---|
| 1 | La question, en une phrase, avec l'action qui suivra chaque réponse possible | Si deux réponses différentes conduisent à la même action, le test ne sert à rien : on ne le lance pas |
| 2 | Les paires de zones, avec `ρ` mesuré sur 26 semaines et le ratio test/témoin | `ρ ≥ 0,80`, ratio stable à ±5 % |
| 3 | **Une zone de contrôle réservée**, non traitée, non utilisée dans l'appariement | Sans elle, tu n'as aucun moyen de détecter une contamination |
| 4 | Le calcul de puissance et la durée retenue | Multiple de 7 jours ; effet détectable minimum écrit |
| 5 | Les seuils de décision, datés et signés | Trois issues écrites : on remet, on coupe, on relance plus long |
| 6 | Le protocole de gel | Rien d'autre ne change dans aucune cellule, pendant le test et les deux semaines suivantes |

> **La pièce 3 est celle que personne n'écrit**, et c'est celle que l'épreuve mesure. Une cellule témoin est un instrument de mesure : elle peut se dérégler, et sans second instrument tu ne le sauras jamais. Le coût de la pièce 3 est nul — il suffit de réserver une zone et de ne pas y toucher. Le coût de son absence est un test entier à refaire, six semaines plus tard, sur un budget qu'on ne recoupera pas deux fois.

---

## 4. L'épreuve

**Durée : 3 h 30.** Calculatrice autorisée, aucun document. **Barème sur 100. Passage à 72.**

### Le dossier — SOLVANE

> *Cas composite. Marque fictive. Les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.*

SOLVANE vend du soin du corps premium en direct, sur cinq marchés européens, au voisinage du palier **P4** du modèle de référence.

| L'économie de la marque | |
|---|---:|
| CA mensuel | 1 620 000 € TTC, soit 1 350 000 € HT |
| Panier moyen | 67,20 € TTC / 56,00 € HT |
| Taux de marge brute CM2 | **59,0 %** |
| Contribution d'une première commande | 56,00 × 59,0 % = **33,00 € HT** *(arrondi de 33,04 €)* |
| **LTV 12 mois** en contribution | **72,00 € HT** |
| **LTV 24 mois** en contribution | **102,00 € HT** |
| Dépense publicitaire mensuelle | 480 000 € |
| Trésorerie | 9 mois d'EBITDA disponibles, BFR intégralement financé sans dette à moins de 12 mois |

**Le plan média mensuel**

| Bloc | Budget | ROAS plateforme | Incrémentalité |
|---|---:|---:|---|
| Prospection Meta + TikTok, **géo-ciblable** | 300 000 € | 3,1 | l'objet du test |
| Google Search — requêtes de marque | 52 000 € | 4,2 | **9 %**, holdout de 5 semaines sur 3 marchés |
| Reciblage | 68 000 € | 6,8 | **21 %**, holdout de 4 semaines |
| Autres (influence, Pinterest, native) | 60 000 € | — | non mesuré |

**Le test géographique qui vient de se terminer.** Coupe totale du budget géo-ciblable dans la cellule test. Pré-test 28 jours, test 42 jours. Budget de la cellule test : 4 100 € par jour, dont **3 500 € géo-ciblables et coupables**. Appariement : `ρ = 0,78`. Coefficient de variation quotidien désaisonnalisé : `CV = 26 %`.

| Cellule | CA TTC pré-test (28 j) | CA TTC pendant le test (42 j) |
|---|---:|---:|
| **A — test**, budget coupé | 1 200 000 € | 1 449 000 € |
| **B — témoin**, budget maintenu | 1 250 000 € | 1 968 750 € |
| **C — contrôle réservé**, budget maintenu, non appariée | 1 000 000 € | 1 530 000 € |

**Ce qu'on t'apprend après coup.** Pendant les six semaines du test, l'équipe *retail* a acheté, sans coordination avec le média, une campagne d'affichage de six semaines **dans la zone B**. Elle n'a touché ni A ni C.

```
Rappels de formules
   Contrefactuelle    = (CA pré-test A ÷ CA pré-test B) × CA test B
   σ cumulé sur D j   = CV × μ × √(2 × (1 − ρ)) × √D      μ = moyenne
                                                   quotidienne contrefactuelle
   Durée nécessaire   = [ 2,80 × CV × √(2(1 − ρ)) ÷ e ]²     e = effet relatif
   IC 95 %            = effet ± 1,96 × σ cumulé
```

### Les questions

**Q1 — Le lift brut. (14 points)** Calcule le ratio pré-test, la contrefactuelle, l'effet en euros TTC et en pourcentage. Puis dis, en une ligne, ce que ce chiffre signifierait s'il était valide.

**Q2 — Pourquoi le résultat brut est invalide. (16 points)** (a) Nomme l'hypothèse du test que l'affichage en zone B a détruite. (b) Sans faire de calcul, dis dans quel **sens** le résultat brut est biaisé, et justifie. (c) Dis pourquoi rejeter le test entier serait une erreur.

**Q3 — La correction. (18 points)** (a) Construis un indice de période pour B et pour C, et chiffre la contamination en pourcentage. (b) Corrige le CA test de B, recalcule la contrefactuelle et l'effet corrigé, en euros et en pourcentage. (c) Écris en deux lignes l'hypothèse que ta correction suppose, et ce qui l'invaliderait.

**Q4 — L'intervalle, le bruit et la puissance. (18 points)** (a) Calcule σ cumulé et le z de l'effet corrigé. (b) Donne l'intervalle de confiance à 95 %, en euros et en pourcentage : **c'est l'intervalle dans lequel se situe la vraie incrémentalité.** (c) Quel était l'effet détectable minimum de ce test à 42 jours ? Combien de jours auraient été nécessaires pour détecter un effet de 5 % ? (d) En deux lignes : ce que tu réponds à un directeur qui te demande le chiffre exact de l'incrémentalité.

**Q5 — La décision sur le bloc testé. (12 points)** (a) Calcule la dépense épargnée par la coupe et le MER incrémental de la coupe. (b) Compare-le au MER seuil de contribution de SOLVANE et tranche. (c) Refais la lecture en clients et en LTV 24 mois, et dis si elle change la conclusion.

**Q6 — La réallocation, chiffrée. (22 points)** (a) Calcule le ROAS incrémental de Google marque et du reciblage, compare-les au seuil, et chiffre le gain d'EBITDA mensuel de chaque coupe. (b) Trois tests d'augmentation sur le bloc de prospection donnent la courbe ci-dessous : calcule les CAC incrémentaux marginaux.

| Budget mensuel du bloc prospection | 240 000 € | **300 000 € — actuel** | 360 000 € | 420 000 € |
|---|---:|---:|---:|---:|
| Clients incrémentaux par mois | 4 800 | **5 600** | 6 200 | 6 650 |

(c) Décide de la réallocation, chiffrée, et donne le compte de résultat mensuel du mouvement. (d) Écris la règle d'arrêt : jusqu'où réalloues-tu, et sous quelle condition de trésorerie la réponse changerait.

---

## 5. Le corrigé

### Q1 — Le lift brut

```
Ratio pré-test    = 1 200 000 ÷ 1 250 000            = 0,96
Contrefactuelle   = 0,96 × 1 968 750                 = 1 890 000 € TTC
Effet mesuré      = 1 449 000 − 1 890 000            =  −441 000 € TTC
En relatif        = −441 000 ÷ 1 890 000             =  −23,33 %
```

S'il était valide, il signifierait que **23,33 % du chiffre d'affaires de la cellule disparaît quand on coupe le bloc de prospection géo-ciblable** — c'est-à-dire que ce bloc est fortement incrémental, et qu'il ne faut surtout pas le couper.

**Barème.** 3 le ratio, 3 la contrefactuelle, 4 l'effet en euros, 2 le pourcentage, 2 l'interprétation. Diviser B par A au lieu de A par B coûte les 14 points.

---

### Q2 — Pourquoi le résultat brut est invalide

**(a) L'hypothèse détruite.** La double différence suppose que **la cellule témoin subit exactement les mêmes chocs que la cellule test, sauf le traitement**. C'est l'hypothèse des tendances parallèles. L'affichage en zone B est un traitement supplémentaire appliqué au témoin : B n'est plus un contrefactuel, c'est une deuxième cellule traitée.

**(b) Le sens du biais.** La campagne d'affichage **gonfle** le CA de B pendant la période de test. La contrefactuelle, qui est proportionnelle au CA de B, est donc **surestimée**. L'effet mesuré, qui est `A − contrefactuelle`, est donc **surestimé en valeur absolue** : le test fait paraître le bloc coupé **plus** incrémental qu'il ne l'est.

**C'est le contre-pied que la question mesure.** L'intuition dit qu'une pollution du témoin détruit la mesure au détriment de la publicité ; ici elle joue en sa faveur. Un directeur média qui ne connaît pas l'affichage repart avec un chiffre qui protège son budget, et il n'a aucune raison de le remettre en cause.

**(c) Pourquoi ne pas jeter le test.** Parce que la contamination est **mesurable**. La zone C n'a subi ni la coupe ni l'affichage : elle donne la variation de période propre à la catégorie. Rejeter un test contaminé quand on dispose d'un contrôle réservé, c'est jeter six semaines de coupe et 147 000 € de budget déjà dépensés en apprentissage, pour rien.

**Barème.** (a) 6 : la réponse doit nommer les **tendances parallèles** ou l'idée d'un témoin qui subit un second traitement ; « le témoin est pollué » sans plus vaut 2. (b) 6 : 3 le sens, 3 la justification par la chaîne contrefactuelle ; répondre « le test sous-estime l'incrémentalité » vaut 0. (c) 4, la réponse devant nommer la zone C.

---

### Q3 — La correction

**(a) L'indice de période**

```
Indice B = (1 968 750 ÷ 42) ÷ (1 250 000 ÷ 28) = 46 875,00 ÷ 44 642,86 = 1,05
Indice C = (1 530 000 ÷ 42) ÷ (1 000 000 ÷ 28) = 36 428,57 ÷ 35 714,29 = 1,02

Contamination = 1,05 ÷ 1,02 − 1 = +2,94 %
```

B a crû de 5,0 % entre les deux périodes, C de 2,0 %. Les 2,0 % sont la saison, la catégorie, le reste du plan média — tout ce qui touche les deux. Les **2,94 %** d'écart sont ce que l'affichage a ajouté.

**(b) L'effet corrigé**

```
CA test B corrigé  = 1 968 750 ÷ 1,0294         = 1 912 500 € TTC
Contrefactuelle    = 0,96 × 1 912 500           = 1 836 000 € TTC
Effet corrigé      = 1 449 000 − 1 836 000      =  −387 000 € TTC
En relatif         = −387 000 ÷ 1 836 000       =  −21,08 %
```

L'incrémentalité passe de 23,33 % à **21,08 %** : le résultat brut surestimait l'effet de **2,25 points**, soit 54 000 € TTC sur six semaines.

**(c) L'hypothèse de la correction.** Elle suppose que **C aurait suivi la même trajectoire que B en l'absence d'affichage** — autrement dit que C est un témoin valide de B sur cette fenêtre. Ce qui l'invaliderait : un choc propre à C sur la même période (rupture de stock locale, concurrent qui ouvre, météo régionale extrême), ou un écart structurel de mix produit entre C et B qui rendrait leurs saisons différentes. **On vérifie donc C avant de s'en servir**, exactement comme on avait vérifié B.

**Barème.** (a) 8 : 3 par indice, 2 le rapport. Prendre les CA bruts sans les ramener au jour — 42 jours contre 28 — coûte les 8 points, et c'est l'erreur la plus fréquente. (b) 6, calcul déroulé. (c) 4 : 2 l'hypothèse, 2 au moins un invalidant concret.

---

### Q4 — L'intervalle, le bruit et la puissance

```
(a)  √(2 × (1 − 0,78)) = √0,44                       = 0,6633
     μ = 1 836 000 ÷ 42                              = 43 714 € / jour
     σ cumulé = 0,26 × 43 714 × 0,6633 × √42
              = 0,26 × 43 714 = 11 366
              × 0,6633 = 7 539  ;  × 6,4807          = 48 859 €
     z = 387 000 ÷ 48 859                            = 7,92

(b)  IC 95 % = 387 000 ± 1,96 × 48 859 = 387 000 ± 95 764
             = [291 236 € ; 482 764 €]
             = [15,9 % ; 26,3 %] du CA contrefactuel

(c)  Effet détectable minimum à 42 jours :
     e = 2,80 × 0,26 × 0,6633 ÷ √42 = 0,4829 ÷ 6,4807 = 7,45 %
     Durée pour détecter 5 % : (0,4829 ÷ 0,05)² = 93,3 → 98 jours (14 semaines)
```

**(d) Ce qu'on répond au directeur.** Qu'il n'y a pas de chiffre exact : le test dit que l'incrémentalité du bloc se situe **entre 15,9 % et 26,3 %**, avec 21,1 % comme meilleure estimation, et que cet intervalle va du simple au double parce qu'un test géographique mesure un ordre de grandeur et un signe. **Regarde l'intervalle avant le z** — ici le z vaut 7,92, le résultat est massivement significatif, et il reste imprécis. Les deux propositions sont vraies en même temps, et confondre « significatif » avec « précis » est la faute qui transforme un bon test en fausse certitude.

**Ce que le (c) enseigne.** Ce test pouvait détecter 7,45 % et a mesuré 21,1 % : il était correctement dimensionné. Mais il aurait fallu **98 jours** pour trancher un effet de 5 %, contre 42 pour un effet de 10 %. La durée varie comme l'inverse du **carré** de l'effet. **Ne pose au test géographique que de grandes questions** ; les petits arbitrages se tranchent autrement.

**Barème.** (a) 6 : 2 le facteur `√(2(1−ρ))`, 2 σ, 2 le z. (b) 4 : 2 les euros, 2 les pourcentages. (c) 4 : 2 l'effet détectable minimum, 2 les 98 jours. (d) 4 : 2 pour refuser un chiffre unique, 2 pour distinguer significatif et précis. Répondre « 21,1 % » sans intervalle vaut 0 sur (d).

---

### Q5 — La décision sur le bloc testé

```
(a)  Dépense épargnée = 3 500 € × 42                 = 147 000 €
     MER incrémental de la coupe = 387 000 ÷ 147 000 = 2,63

(b)  MER seuil de contribution = 1,20 ÷ 0,590        = 2,03
     2,63 > 2,03  →  le bloc coupé **crée** de la valeur, même dans la fenêtre
```

**(c) La lecture en clients.** Elle ne change pas la conclusion, elle la renforce, et il faut quand même la faire — parce que dans la plupart des tests c'est elle qui retourne le verdict.

```
AOV première commande             = 67,20 € TTC
Clients non acquis  = 387 000 ÷ 67,20                = 5 759 clients
Valeur perdue       = 5 759 × 102,00 € (LTV 24 mois) = 587 418 €
Dépense épargnée                                     = 147 000 €
Solde                                            = +440 418 € en faveur du maintien
```

**On remet le budget.** Et on remarque que la fenêtre de six semaines ne captait qu'une fraction de la valeur : `387 000 ÷ 1,20 × 59,0 % = 190 275 €` de contribution dans la fenêtre, contre 587 418 € en LTV à 24 mois. **Un test d'incrémentalité mesure un effet dans sa fenêtre ; le convertir en décision exige de rapporter les clients non acquis à leur LTV**, jamais le chiffre d'affaires perdu à la dépense épargnée ([E09](../modules/E09-mesure-et-incrementalite.md) § 5.3).

**Barème.** (a) 4. (b) 4, dont 2 pour le seuil calculé et non récité. (c) 4 : 2 le nombre de clients, 2 la valorisation en LTV. Utiliser le CA HT pour compter les clients — division par 56,00 € au lieu de 67,20 € — coûte 2 points.

---

### Q6 — La réallocation

**(a) Les deux blocs à couper**

| Bloc | Dépense | ROAS plateforme | Incrémentalité | **ROAS incrémental** | Seuil 2,03 |
|---|---:|---:|---:|---:|---|
| Google marque | 52 000 € | 4,2 | 9 % | **0,38** | détruit |
| Reciblage | 68 000 € | 6,8 | 21 % | **1,43** | détruit |

```
Google marque : CA incrémental = 52 000 × 4,2 × 0,09          =  19 656 €
                contribution   = 19 656 ÷ 1,20 × 59,0 %       =   9 664 €
                gain           = 52 000 − 9 664               = +42 336 €/mois
Reciblage     : CA incrémental = 68 000 × 6,8 × 0,21          =  97 104 €
                contribution   = 97 104 ÷ 1,20 × 59,0 %       =  47 743 €
                gain           = 68 000 − 47 743              = +20 257 €/mois
                                                        Total = +62 593 €/mois
```

**Tu viens de supprimer les deux lignes au meilleur ROAS affiché du compte** — 4,2 et 6,8 contre 3,1 pour la prospection — **et ton résultat gagne 751 116 € par an.** Aucun tableau de bord de régie ne te dira que c'était juste ; tous afficheront une dégradation.

**(b) Les CAC incrémentaux marginaux**

| Budget | 240 000 € | 300 000 € | 360 000 € | 420 000 € |
|---|---:|---:|---:|---:|
| Clients incrémentaux | 4 800 | 5 600 | 6 200 | 6 650 |
| CAC incrémental **moyen** | 50,00 € | **53,57 €** | 58,06 € | 63,16 € |
| CAC incrémental **marginal** | — | **75,00 €** | **100,00 €** | **133,33 €** |

```
300 → 360 :  60 000 ÷ 600 = 100,00 €      360 → 420 :  60 000 ÷ 450 = 133,33 €
```

**(c) La décision**

```
Coupe de Google marque et du reciblage                       −120 000 € de dépense
Réinjection sur la prospection : 300 000 → 360 000 €          + 60 000 € de dépense
   CAC marginal 100,00 €  <  LTV 24 mois 102,00 €   →  on prend la tranche
   CAC marginal 133,33 €  >  102,00 €               →  on refuse la suivante

Compte de résultat mensuel du mouvement
   Gain des deux coupes                                        +62 593 €
   Coût de la tranche ajoutée                                  −60 000 €
   Contribution immédiate  600 × 33,00 €                       +19 800 €
   EBITDA mensuel                                              +22 393 €
   Valeur à 24 mois de la tranche  600 × 102,00 € − 60 000 €    +1 200 €
   Dépense publicitaire totale : 480 000 → 420 000 €           −12,5 %
```

**(d) La règle d'arrêt.** On réalloue tant que le **CAC incrémental marginal reste inférieur à la LTV que la trésorerie sait financer**. SOLVANE dispose de neuf mois d'EBITDA et d'un BFR financé sans dette courte : elle peut tenir un horizon de 24 mois, donc la borne est 102,00 € et la tranche 300 → 360 passe — de justesse, pour 1 200 € par mois.

**Sous une contrainte de trésorerie, la réponse s'inverse.** Si SOLVANE devait se rembourser à 12 mois, la borne deviendrait **72,00 €**, et la tranche à 100,00 € serait refusée : on garderait les 120 000 € libérés en résultat, et l'EBITDA gagnerait 62 593 € par mois au lieu de 22 393 €.

> **À retenir :** ce n'est pas la mesure qui décide de l'allocation, c'est la mesure **et** l'horizon que ton bilan peut porter. Deux marques identiques, avec le même test et le même CAC marginal, prennent légitimement deux décisions opposées si l'une a neuf mois de trésorerie et l'autre trois.

**Barème.** (a) 8 : 2 par ROAS incrémental, 4 les deux gains chiffrés. Comparer un ROAS incrémental à un ROAS cible au lieu du MER seuil coûte 4. (b) 4, 2 par CAC marginal. (c) 6 : 2 la coupe, 2 la tranche retenue justifiée par la comparaison au CAC marginal, 2 le compte de résultat. (d) 4 : 2 la règle, 2 le renversement sous contrainte de trésorerie — une réponse qui ne mentionne pas l'horizon de LTV plafonne à 1.

---

## 6. Le critère de passage

**Note minimale : 72 / 100**, dont **au moins 10 / 18 à la question 3** — un stratège qui ne sait pas corriger un test contaminé n'a pas de test.

**Quatre fautes éliminatoires**, quelle que soit la note :

1. **Se tromper de sens sur le biais** (question 2b) : conclure que la contamination fait sous-estimer l'incrémentalité. C'est l'erreur qui protège les budgets et que l'épreuve existe pour attraper.
2. **Comparer des périodes de longueurs différentes** sans les ramener au jour — 42 jours contre 28 — dans la construction de l'indice de période.
3. **Donner l'incrémentalité comme un nombre unique** sans intervalle, ou conclure « non significatif, donc pas d'effet ». Un test non concluant ne prouve rien ; il coûte le même prix qu'un test concluant et n'autorise aucune décision.
4. **Convertir un effet en décision en comparant le CA perdu à la dépense épargnée**, sans passer par les clients et leur LTV. C'est la façon la plus fréquente de couper un budget qui gagne de l'argent.

**Deux fautes lourdes :** comparer un ROAS incrémental à un ROAS cible plutôt qu'au MER seuil de contribution (−4) ; allouer sur le CAC incrémental **moyen** au lieu du marginal (−6).

**En cas d'échec**, tu repasses sur un test dont le résultat corrigé devient **non significatif**. La bonne réponse n'est plus un chiffre : c'est de dire ce que le test n'a pas permis d'apprendre, ce qu'il aurait fallu changer pour qu'il l'apprenne, et quelle décision on prend en attendant.

---

## 7. Les pièges de ce niveau

**1. Croire qu'on a compris l'incrémentalité parce qu'on sait la définir.** Tout le monde sait dire que l'attribution répartit et que l'incrémentalité mesure une causalité. Presque personne ne sait dire ce que coûte une cellule témoin contaminée, ni combien de jours il faut pour trancher un effet de 5 %. La compétence L07 n'est pas dans la définition, elle est dans les deux calculs que la définition rend obligatoires.

**2. Croire qu'un test significatif est un test précis.** L'épreuve donne un z de 7,92 et un intervalle qui va du simple au double. Ce sont les deux visages du même résultat. Un directeur à qui l'on répond « 21,08 % » retiendra 21,08 % et bâtira un plan dessus ; le même, à qui l'on répond « entre 16 % et 26 %, probablement autour de 21 % », prendra la même décision et ne sera pas surpris six mois plus tard.

**3. Croire qu'un résultat non significatif signifie « pas d'effet ».** Il signifie « ce test-ci, avec ce nombre de jours, cette corrélation et ce coefficient de variation, ne peut pas distinguer l'effet de zéro ». Ce sont deux propositions très différentes, et l'écart entre les deux se chiffre : c'est l'effet détectable minimum, 7,45 % ici. Sous ce seuil, ne rien voir n'est pas une information.

**4. Croire que le canal au meilleur ROAS est le meilleur canal.** La question 6 supprime les deux lignes au meilleur ROAS affiché et gagne 751 116 € par an. La raison est mécanique : plus un canal intervient tard dans le parcours, plus il s'attribue de conversions qui auraient eu lieu sans lui, et **plus son ROAS affiché est élevé pour la même dépense**. Le ROAS de plateforme classe les canaux par leur position dans le parcours, pas par leur valeur.

**5. Croire que la mesure décide.** Elle ne décide jamais seule. Le même CAC marginal de 100,00 € justifie une tranche de budget pour une marque à neuf mois de trésorerie et l'interdit à une marque à trois. C'est ici que L07 rejoint L06 : une décision d'allocation est autant une décision de bilan qu'une décision de mesure, et le stratège qui ignore la contrainte de trésorerie produit des recommandations que personne ne peut exécuter.

**6. Croire que L07 mesure ta marque.** Un consultant peut être L07 sans avoir jamais rien opéré. Et une marque **N4** — plusieurs millions d'euros par mois — peut n'avoir jamais mené un seul test d'incrémentalité, ce que la porte P3 → P4 des [jalons](../mentorat/jalons.md) interdit précisément pour cette raison : ouvrir un marché multiplie le budget média, et multiplier un budget mal alloué multiplie la mauvaise allocation. **L'erreur d'allocation croît proportionnellement au chiffre d'affaires** — c'est la seule erreur du métier dont le coût grandit exactement à la vitesse du succès.

---

*Fin du niveau L07. Suite : [L08 — Bâtisseur](L08-batisseur.md) — tu sais où mettre l'argent. Reste à construire ce qui saura le dépenser.*
