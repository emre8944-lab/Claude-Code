# Niveau L04 — Acquéreur

> **Prérequis :** niveau L03 validé.
>
> **Ce que tu sais faire à la sortie :**
> 1. Tu calcules un CAC marginal à partir d'un relevé de compte brut, et tu sais dire à partir de quel euro la tranche suivante détruit de la valeur.
> 2. Tu alloues un budget entre six campagnes en écrivant tes seuils avant de regarder les chiffres, et tu justifies chaque mouvement par un nombre.
> 3. Tu distingues une variation qui est un signal d'une variation qui est du bruit, avec un calcul, et tu sais ce que coûte chacune des deux erreurs.
>
> **Temps de travail typique :** 20 à 30 heures, dont une partie complète de simulateur en interactif. C'est le niveau où l'on apprend à **ne rien faire** — le geste le plus difficile du métier.

> **Lxx mesure ta compétence. Nx mesure l'état de ton business.** Les deux sont indépendantes. Un acheteur média en agence peut être L04 sans posséder une seule marque. Et le cas symétrique est le plus fréquent du métier : **N3 avec une compétence L04** — une marque à 500 000 € TTC par mois pilotée par quelqu'un qui n'a jamais calculé un CAC marginal. Tant que le marché porte, personne ne le voit. Le jour où il ne porte plus, l'entreprise n'a personne pour lire ce qui se passe, et les décisions se prennent au ressenti sur un budget à six chiffres. Garde ton L au-dessus de ton N ([diagnostic](../mentorat/diagnostic.md)).

---

## 1. Les compétences du niveau

1. **Je calcule un CAC marginal de tête** : dépense supplémentaire ÷ clients supplémentaires, et je refuse de juger une hausse de budget sur le CAC moyen.
2. **Je sais pourquoi la courbe de CAC monte toujours**, et je retrouve le rapport structurel entre marginal et moyen dans un jeu de données réel.
3. **J'écris mes seuils avant de regarder les chiffres**, dérivés de ma LTV à 12 mois et non d'une habitude de place.
4. **Je décide de ne rien faire** quand le marginal tombe entre mes deux seuils, et j'explique pourquoi bouger coûterait plus que d'attendre.
5. **Je distingue une saturation d'audience d'une fatigue créative** en croisant fréquence, CPA et âge du concept.
6. **Je calcule si une variation est du bruit** avant de réagir, et je chiffre la fausse alerte comme l'attente.
7. **Je reconnais un canal de récolte** — CPA excellent, volume plafonné, marginal explosif — et je sais qu'il appelle un test d'incrémentalité et non un arbitrage budgétaire.
8. **Je relie l'allocation au compte de résultat** : MER, ses deux seuils, et donc budget total à monter, tenir ou descendre.
9. **Je monte un budget par paliers bornés**, pour ne pas détruire l'apprentissage d'une campagne.

---

## 2. Ce que tu lis

| # | Lecture | Ce qu'elle apporte **à ce niveau** |
|---|---|---|
| 1 | [**E06 — L'acquisition payante**](../modules/E06-acquisition-payante.md) § 1 et § 2 | La mécanique de l'enchère et du signal. Pourquoi tu n'achètes pas des impressions mais une place dans un classement, et pourquoi la plateforme a besoin d'événements pour apprendre. |
| 2 | [**E06**](../modules/E06-acquisition-payante.md) § 3 | La structure de compte : ce que la consolidation fait au signal, et pourquoi multiplier les ensembles de publicités appauvrit chacun. |
| 3 | [**E06**](../modules/E06-acquisition-payante.md) § 4 et § 5 | Le rendement décroissant, le CAC marginal, la saturation d'audience et sa signature en fréquence. **Le cœur du niveau.** |
| 4 | [**E06**](../modules/E06-acquisition-payante.md) § 6 | La période d'apprentissage : pourquoi une hausse de budget trop brutale coûte plus cher que la hausse elle-même. |
| 5 | Rappel obligatoire : [**E01**](../modules/E01-arithmetique-de-la-marque.md) § 5.3 et § 6.3 | Le CAC marginal se juge contre la LTV, et surtout contre le **payback marginal** : 4,35 mois pour le client marginal du modèle de référence contre 1,8 pour le moyen. |
| 6 | Rappel obligatoire : [**E09**](../modules/E09-mesure-et-incrementalite.md) § 7.6 | Le bruit : combien de variation est normale, les cinq règles de déclenchement, et le calcul qui compare le coût d'attendre à celui de réagir à tort. |

> **Ce que ce niveau ne traite pas encore.** L'incrémentalité ([E09](../modules/E09-mesure-et-incrementalite.md) § 4 et § 5) est un niveau L07. À L04 tu alloues sur des chiffres **attribués**, en sachant qu'ils sont faux dans un sens connu — et tu repères les canaux où cette fausseté décide de tout.

---

## 3. Ce que tu fais

| Travail | Livrable | Comment on sait que c'est fait |
|---|---|---|
| [**S08 — Les 30 premiers jours**](../atelier/S08-le-lancement.md) | Le plan de lancement et son **tableau de seuils écrits d'avance** : budget par palier, CPA d'arrêt, CPA de montée, durée minimale avant jugement | Aucune case du tableau n'est remplie après coup. La date d'écriture est dans le fichier |
| [**S09 — Lire les chiffres et décider**](../atelier/S09-lire-les-premiers-chiffres.md) | Un diagnostic sur dossier piégé, avec une décision écrite et sa justification chiffrée | Tu as identifié au moins un piège du dossier sans qu'on te dise qu'il y en avait |
| **Simulateur, une partie complète en interactif** | Le rapport markdown de la partie, 36 mois minimum | `simulateur_marque.py --interactif --graine 7 --rapport partie-L04.md` |
| **La même partie rejouée** | Une seule décision changée | Tu nommes le mois où la courbe se retourne et tu comptes les mois écoulés depuis la décision qui l'a causée |

> **Pourquoi le simulateur est obligatoire ici et pas avant.** Le mécanisme central du niveau — `CAC marginal = CAC moyen ÷ 0,72`, soit 39 % de plus — s'énonce en une ligne et ne s'apprend pas en une ligne. Le tableau de bord affiche `CACm` et `CACx` côte à côte tous les mois, exprès. Après trente-six tours, tu ne regardes plus jamais le CAC moyen pour décider d'une hausse.

---

## 4. L'épreuve

**Durée : 2 h 30.** Calculatrice autorisée, aucun document. **Barème sur 100. Passage à 72.**

### Le dossier — ORÈNE

> *Marque fictive, chiffres modélisés sur des ordres de grandeur sectoriels : ce ne sont les comptes d'aucune entreprise réelle.*

ORÈNE vend une cure mensuelle de compléments alimentaires en direct, en France et en Belgique, entre les paliers **P2 et P3** ([canoniques § 2](../donnees/chiffres-canoniques.md)).

**L'économie de la marque, mesurée, pas estimée**

| | |
|---|---:|
| Panier moyen d'une **première** commande | 61,00 € TTC — 50,83 € HT |
| Taux de marge brute CM2 | 59,0 % |
| Contribution de la première commande | **29,99 € HT** |
| LTV à 12 mois en contribution, mesurée sur 14 cohortes | **80,00 € HT** |
| Part du chiffre d'affaires en réachat | 28,0 % |
| Frais fixes, par tranche de deux semaines | 22 000 € HT |

**Les seuils d'allocation, écrits le 3 janvier, avant la période observée**

```
Seuil d'AJOUT     : LTV 12 mois ÷ 2,0 = 80,00 ÷ 2,0 = 40,00 € HT
    → on n'ajoute du budget que si le CAC marginal reste sous 40,00 € HT.
Seuil de RETRAIT  : LTV 12 mois ÷ 1,5 = 80,00 ÷ 1,5 = 53,33 € HT, arrondi à 53,00 €
    → on retire du budget dès que le CAC marginal dépasse 53,00 € HT.
Entre les deux    : ON NE TOUCHE À RIEN.
```

**Note de méthode.** Les nombres de clients ci-dessous sont les **nouveaux clients dédoublonnés** de l'entrepôt, comptés à la date de commande. Sur T4, les régies revendiquent **2 492** achats ; l'entrepôt en compte **2 245**, soit **11,0 %** de sur-attribution — le comportement normal décrit aux [chiffres canoniques § 5](../donnees/chiffres-canoniques.md). Toute réponse fondée sur les 2 492 est fausse.

---

### Tableau 1 — Le compte, semaine par semaine

| Semaine | Dépense HT | Nouveaux clients | nCAC HT |
|---|---:|---:|---:|
| S1 | 24 000 € | 762 | 31,50 € |
| S2 | 24 000 € | 779 | 30,81 € |
| S3 | 28 000 € | 871 | 32,15 € |
| S4 | 28 000 € | 892 | 31,39 € |
| S5 | 33 000 € | 988 | 33,40 € |
| S6 | 33 000 € | 1 006 | 32,80 € |
| S7 | 39 000 € | 1 108 | 35,20 € |
| S8 | 39 000 € | 1 137 | 34,30 € |

Les semaines sont regroupées en quatre **tranches** de deux semaines : T1 = S1+S2, T2 = S3+S4, T3 = S5+S6, T4 = S7+S8.

### Tableau 2 — Dépense HT par campagne et par tranche

| Campagne (€ HT) | T1 | T2 | T3 | T4 |
|---|---:|---:|---:|---:|
| **#1** Prospection large | 18 000 € | 21 400 € | 25 000 € | 29 200 € |
| **#2** Prospection intérêts | 9 000 € | 10 000 € | 12 000 € | 14 400 € |
| **#3** Retargeting 7 jours | 4 000 € | 5 200 € | 6 800 € | 8 800 € |
| **#4** TikTok UGC | 6 000 € | 7 600 € | 10 000 € | 12 400 € |
| **#5** Search marque | 5 000 € | 5 000 € | 5 200 € | 5 400 € |
| **#6** Search générique | 6 000 € | 6 800 € | 7 000 € | 7 800 € |
| **Total** | **48 000 €** | **56 000 €** | **66 000 €** | **78 000 €** |

### Tableau 3 — Nouveaux clients par campagne et par tranche

| Campagne | T1 | T2 | T3 | T4 |
|---|---:|---:|---:|---:|
| **#1** Prospection large | 500 | 578 | 652 | 740 |
| **#2** Prospection intérêts | 250 | 268 | 290 | 305 |
| **#3** Retargeting 7 jours | 200 | 238 | 272 | 300 |
| **#4** TikTok UGC | 148 | 205 | 292 | 380 |
| **#5** Search marque | 263 | 265 | 268 | 270 |
| **#6** Search générique | 180 | 209 | 220 | 250 |
| **Total** | **1 541** | **1 763** | **1 994** | **2 245** |

### Tableau 4 — Fréquence moyenne d'exposition, par tranche

| Campagne | T1 | T2 | T3 | T4 |
|---|---:|---:|---:|---:|
| **#1** Prospection large | 1,6 | 1,8 | 2,0 | 2,3 |
| **#2** Prospection intérêts | 2,2 | 2,8 | 3,6 | 4,5 |
| **#3** Retargeting 7 jours | 2,1 | 3,3 | 5,0 | 6,8 |
| **#4** TikTok UGC | 1,3 | 1,4 | 1,4 | 1,5 |
| **#5** et **#6** Search | — | — | — | — |

### Tableau 5 — La campagne #4, semaine par semaine

| Campagne #4 | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Dépense HT | 3 000 € | 3 000 € | 3 800 € | 3 800 € | 5 000 € | 5 000 € | 6 200 € | 6 200 € |
| Nouveaux clients | 72 | 76 | 100 | 105 | 141 | 151 | 178 | 202 |
| CPA HT | 41,67 € | 39,47 € | 38,00 € | 36,19 € | 35,46 € | 33,11 € | 34,83 € | 30,69 € |

---

### Les questions

**Question 1 — Le CAC marginal du compte. (20 points)**

(a) Calcule le CAC **moyen** du compte pour les quatre tranches. *(4 pts)*
(b) Calcule le CAC **marginal** des **deux dernières** tranches — c'est-à-dire T2 → T3 et T3 → T4 — en déroulant le calcul. *(8 pts)*
(c) Donne le rapport `CAC marginal ÷ CAC moyen` sur T3 → T4, et dis en deux lignes ce que ce rapport signifie sur la forme de la courbe d'acquisition. *(8 pts)*

**Question 2 — Couper et augmenter. (20 points)**

(a) Nomme les **deux** campagnes dont tu retires du budget le mois prochain. Pour chacune : le CAC marginal T3 → T4 calculé, et la seconde donnée du dossier qui confirme le diagnostic. *(8 pts)*
(b) Nomme les **deux** campagnes auxquelles tu ajoutes du budget, avec leur CAC marginal T3 → T4. *(6 pts)*
(c) Une **cinquième** campagne dépasse aussi le seuil de retrait. Nomme-la, et explique en trois lignes pourquoi elle n'appelle pas la même décision que les deux de la question (a). *(6 pts)*

**Question 3 — L'allocation de la tranche suivante. (25 points)**

Écris l'allocation de T5, campagne par campagne, en euros HT, avec le total. Justifie chaque montant modifié par un nombre. Contraintes :
- aucune campagne ne monte de plus de **30 %** d'une tranche à la suivante ;
- toute campagne dont le CAC marginal est entre 40,00 € et 53,00 € HT reste **inchangée** ;
- tu dis explicitement si le budget **total** monte, tient ou descend, et pourquoi.

**Question 4 — Signal ou bruit. (20 points)**

Quatre variations observées, **une seule** est du bruit. Dis laquelle et démontre-le par un calcul ; pour les trois autres, une ligne suffit.

| | Variation observée |
|---|---|
| (α) | Campagne #4 : le CPA passe de 34,83 € en S7 à 30,69 € en S8, soit −11,9 % |
| (β) | Campagne #2 : le CPA passe de 36,00 € en T1 à 47,21 € en T4, soit +31,1 % |
| (γ) | Campagne #3 : la fréquence passe de 2,1 en T1 à 6,8 en T4 |
| (δ) | Campagne #4 : le CPA passe de 40,54 € en T1 à 32,63 € en T4, soit −19,5 % |

**Question 5 — Ce que le compte de résultat dit de ton allocation. (15 points)**

Sur la tranche T4 :
(a) Calcule le chiffre d'affaires TTC total, puis le MER. *(5 pts)*
(b) Calcule le MER seuil de contribution nulle (CM3 = 0) et le MER seuil de résultat nul (EBITDA = 0). *(6 pts)*
(c) En une phrase : ce que ces trois nombres imposent au budget **total** de la question 3. *(4 pts)*

---

## 5. Le corrigé

### Question 1 — Le CAC marginal du compte

**(a) Le CAC moyen, par tranche**

```
T1 : 48 000 ÷ 1 541 = 31,15 € HT
T2 : 56 000 ÷ 1 763 = 31,76 € HT
T3 : 66 000 ÷ 1 994 = 33,10 € HT
T4 : 78 000 ÷ 2 245 = 34,74 € HT
```

**(b) Le CAC marginal des deux dernières tranches**

```
T2 → T3 : (66 000 − 56 000) ÷ (1 994 − 1 763) = 10 000 ÷ 231 = 43,29 € HT
T3 → T4 : (78 000 − 66 000) ÷ (2 245 − 1 994) = 12 000 ÷ 251 = 47,81 € HT
```

**(c) Le rapport, et ce qu'il dit**

```
47,81 ÷ 34,74 = 1,376
```

Le client marginal coûte **37,6 % de plus** que le client moyen. Ce rapport n'est pas un accident de période : c'est la signature d'une courbe d'acquisition à rendement décroissant de la forme `clients = A × budget^a`, pour laquelle le rapport vaut exactement `1 ÷ a`.

```
a = 1 ÷ 1,376 = 0,727
```

Le simulateur du cursus modélise `a = 0,72`, soit un rapport de 1,389 — le compte d'ORÈNE se comporte comme le modèle, à trois centièmes près. Sur T2 → T3 : `43,29 ÷ 33,10 = 1,308`, soit `a = 0,765` : le compte était **moins** saturé une tranche plus tôt. La saturation s'aggrave, et elle s'aggrave visiblement.

> **Ce que cette question mesure.** Les derniers euros du compte n'achètent pas des clients à 34,74 € : ils les achètent à 47,81 €. Juger une hausse de budget sur le CAC moyen, c'est se tromper de 37,6 % sur le prix de ce qu'on achète — et se tromper **toujours dans le sens qui encourage à dépenser**.

**Barème.** (a) 1 par tranche. (b) 4 par marginal — 2 la formule (différence sur différence), 2 le résultat ; utiliser le CAC moyen à la place : 0 sur toute la question. (c) 3 le rapport, 3 le lien avec le rendement décroissant, 2 la comparaison T2 → T3 contre T3 → T4.

---

### Question 2 — Couper et augmenter

**Les six CAC marginaux T3 → T4, calculés d'abord**

| Campagne | Δ dépense HT | Δ clients | **CAC marginal HT** | CPA moyen T4 HT | Verdict au seuil |
|---|---:|---:|---:|---:|---|
| **#1** Prospection large | 4 200 € | 88 | **47,73 €** | 39,46 € | zone morte — **on ne touche pas** |
| **#2** Prospection intérêts | 2 400 € | 15 | **160,00 €** | 47,21 € | **retrait** |
| **#3** Retargeting 7 j | 2 000 € | 28 | **71,43 €** | 29,33 € | **retrait** |
| **#4** TikTok UGC | 2 400 € | 88 | **27,27 €** | 32,63 € | **ajout** |
| **#5** Search marque | 200 € | 2 | **100,00 €** | 20,00 € | cas particulier — voir (c) |
| **#6** Search générique | 800 € | 30 | **26,67 €** | 31,20 € | **ajout** |

**(a) Les deux campagnes dont on retire du budget : #2 et #3.**

**#2 — Prospection intérêts.** Marginal 160,00 € HT, trois fois le seuil de retrait. La donnée qui confirme : la **fréquence** passe de 2,2 à 4,5 (tableau 4). Une audience d'intérêts est finie par construction ; on l'a vidée. Le CPA qui monte de 36,00 € à 47,21 € et la fréquence qui double disent la même chose deux fois.

**#3 — Retargeting 7 jours.** Marginal 71,43 € HT — pour **le meilleur CPA moyen du compte après le search**, 29,33 €. C'est exactement le piège. Confirmation par la fréquence : **6,8** expositions par personne sur sept jours contre 2,1 au départ. Un pool de visiteurs à sept jours est un stock fini ; y verser 8 800 € au lieu de 4 000 € ne crée pas de visiteurs, ça reachète les mêmes.

**(b) Les deux campagnes auxquelles on ajoute : #4 et #6.**

**#4 — TikTok UGC**, marginal **27,27 € HT**, très sous le seuil de 40,00 €. Et il **s'améliore** de tranche en tranche (28,07 → 27,59 → 27,27) : la campagne n'est pas encore sur sa partie décroissante.

**#6 — Search générique**, marginal **26,67 € HT** — le meilleur du compte, sur une campagne qui n'a reçu que 10,0 % du budget de T4.

**(c) La cinquième : #5, Search marque.**

Son CAC marginal est de 100,00 € HT, bien au-dessus du seuil de retrait. Elle n'appelle pourtant pas la même décision, pour trois raisons.

1. **Le calcul repose sur deux clients.** 200 € de dépense supplémentaire, 2 clients de plus : à ce volume, l'écart-type de Poisson sur 270 clients est de 16,4. Une différence de 2 est indiscernable de zéro. Le nombre est vrai et il ne démontre rien.
2. **Le volume est plafonné, pas saturé.** Le search de marque n'est pas piloté par le budget mais borné par le nombre de gens qui tapent ton nom. Y mettre 200 € de plus n'achète rien, ce que le tableau montre.
3. **La vraie question n'est pas budgétaire, elle est d'incrémentalité.** Un CPA de 20,00 € sur des gens qui cherchent déjà ta marque signale une **récolte**, pas une création de demande ([E09](../modules/E09-mesure-et-incrementalite.md) § 6.2). La décision correcte est un test de suspension géographique, pas un arbitrage de budget — et c'est un travail de niveau L07.

**Ce que la question mesure.** Trois campagnes dépassent le seuil ; deux se traitent au budget, une à la mesure. Couper #5 « parce que la règle le dit », c'est appliquer une règle hors de son domaine ; la garder sans rien faire, c'est ignorer un signal. On la laisse en l'état et **on ouvre un test**.

**Barème.** (a) 4 points par campagne : 1 pour le nom, 2 pour le CAC marginal calculé, 1 pour la donnée de confirmation (fréquence). Nommer #3 sans mentionner sa fréquence : 3 sur 4. (b) 3 points par campagne : 1 pour le nom, 2 pour le marginal. (c) 2 points pour nommer #5, 4 points pour la justification — au moins deux des trois raisons, dont **obligatoirement** soit la faiblesse statistique, soit l'incrémentalité. Répondre « on la coupe puisqu'elle dépasse le seuil » : 0 sur la question (c).

---

### Question 3 — L'allocation de la tranche T5

| Campagne | T4 (€ HT) | **T5 (€ HT)** | Δ | Justification chiffrée |
|---|---:|---:|---:|---|
| **#1** Prospection large | 29 200 € | **29 200 €** | 0 | Marginal 47,73 € : entre 40,00 € et 53,00 €. Zone morte, on ne touche pas |
| **#2** Prospection intérêts | 14 400 € | **9 000 €** | −5 400 € | Retour au niveau de T1, le dernier où le marginal (55,56 €) était encore proche du seuil |
| **#3** Retargeting 7 j | 8 800 € | **5 200 €** | −3 600 € | Retour au niveau de T2, où le marginal valait 47,06 € et la fréquence 3,3 |
| **#4** TikTok UGC | 12 400 € | **16 100 €** | +3 700 € | +29,8 %, sous la borne de 30 %. Marginal observé 27,27 € |
| **#5** Search marque | 5 400 € | **5 400 €** | 0 | Inchangée. Un test de suspension est ouvert en parallèle |
| **#6** Search générique | 7 800 € | **10 100 €** | +2 300 € | +29,5 %, sous la borne. Marginal observé 26,67 € |
| **Total** | **78 000 €** | **75 000 €** | **−3 000 €** | |

**Pourquoi le total descend.** Le CAC marginal du **compte entier** sur T3 → T4 vaut 47,81 € HT, au-dessus du seuil d'ajout de 40,00 € : les deux dernières tranches ont acheté des clients à un prix qui ne respecte pas la règle écrite le 3 janvier. On ne cherche pas à dépenser plus, on cherche à dépenser **ailleurs**. Les 9 000 € retirés de #2 et #3 financent 6 000 € d'ajout et 3 000 € d'économie.

**Pourquoi la borne de 30 %.** Une hausse brutale renvoie la campagne en apprentissage et détruit temporairement l'efficacité du budget déjà en place ([E06](../modules/E06-acquisition-payante.md) § 6). Monter #4 de 12 400 € à 24 000 € parce que son marginal est bon, c'est payer l'apprentissage pour découvrir qu'il n'était bon que jusqu'à 16 000 €.

**Ce que ça donne, projeté.** *Hypothèses déclarées, prudentes : le marginal de #4 se dégrade de 27,27 € à 32,00 € sur la tranche ajoutée ; celui de #6 de 26,67 € à 31,00 € ; #2 revient à 39,00 € de CPA moyen — au-dessus de ses 36,00 € de T1, parce que l'audience a vieilli ; #3 revient au CPA de T2, 21,85 €.*

| Campagne | Budget T5 HT | Clients projetés | Calcul |
|---|---:|---:|---|
| #1 | 29 200 € | 740 | inchangé |
| #2 | 9 000 € | 231 | 9 000 ÷ 39,00 |
| #3 | 5 200 € | 238 | 5 200 ÷ 21,85 |
| #4 | 16 100 € | 496 | 380 + 3 700 ÷ 32,00 |
| #5 | 5 400 € | 270 | inchangé |
| #6 | 10 100 € | 324 | 250 + 2 300 ÷ 31,00 |
| **Total** | **75 000 €** | **2 299** | |

```
CAC moyen projeté   = 75 000 ÷ 2 299 = 32,62 € HT   (contre 34,74 € en T4, −6,1 %)
Clients gagnés      = 2 299 − 2 245 = +54           (+2,4 %)
Budget économisé    = 78 000 − 75 000 = 3 000 €

Valeur créée par tranche, en contribution de première commande :
   54 × 29,99 € + 3 000 € = 4 619 €      →  × 26 tranches = 120 106 € / an
Valeur créée par tranche, en LTV 12 mois :
   54 × 80,00 € + 3 000 € = 7 320 €      →  × 26 tranches = 190 320 € / an
```

**Aucune campagne créée, aucune créa produite, aucun euro ajouté.** On a déplacé 9 000 € et rendu 3 000 €.

**Barème.** 2 points par ligne correctement chiffrée et justifiée (12). 4 pour le respect des trois contraintes. 5 pour la décision explicite sur le budget **total**, justifiée par le CAC marginal du compte — 0 si le total monte. 4 pour la projection chiffrée : 0 si ses hypothèses ne sont pas déclarées.

---

### Question 4 — Signal ou bruit

**La réponse : (α) est du bruit.** Les trois autres sont des signaux.

**La démonstration pour (α).** Le nombre d'achats hebdomadaires est un comptage d'événements rares : sa dispersion naturelle est celle d'une loi de Poisson, d'écart-type `√k`. Hypothèse nulle : le CPA vrai de #4 est constant sur les quatre dernières semaines. On l'estime en regroupant S5 à S8 :

```
Dépense S5→S8 = 5 000 + 5 000 + 6 200 + 6 200 = 22 400 € HT
Clients S5→S8 = 141 + 151 + 178 + 202         =    672
CPA groupé    = 22 400 ÷ 672                  = 33,33 € HT

Clients attendus en S7 = 6 200 ÷ 33,33 = 186,0   →  observés 178
   z = (178 − 186,0) ÷ √186,0 = −8,0 ÷ 13,64 = −0,59
Clients attendus en S8 = 6 200 ÷ 33,33 = 186,0   →  observés 202
   z = (202 − 186,0) ÷ √186,0 = +16,0 ÷ 13,64 = +1,17
```

Les deux semaines sont **dans la bande de ±2σ**. L'écart de −11,9 % sur le CPA entre S7 et S8 est entièrement contenu dans le bruit d'échantillonnage de deux semaines à ~186 achats. Réagir à cet écart — en montant le budget parce que S8 est « meilleure » — c'est prendre une décision sur un tirage.

**Les trois signaux, en une ligne chacun.**

**(β) #2.** Sous l'hypothèse que le CPA vrai est resté à 36,00 €, T4 aurait dû rendre `14 400 ÷ 36,00 = 400` clients ; elle en rend 305, soit `z = (305 − 400) ÷ √400 = −4,75`. Au-delà de 4σ, et corroboré par la fréquence : signal.

**(γ) #3.** Une fréquence n'est pas un comptage aléatoire, c'est un rapport mécanique entre impressions servies et taille de pool. Quatre tranches consécutives de hausse monotone, ×3,2 au total : il n'existe pas de bruit qui produise ça.

**(δ) #4.** Sous l'hypothèse d'un CPA resté à 40,54 €, T4 aurait dû rendre `12 400 ÷ 40,54 = 305,9` clients ; elle en rend 380, soit `z = +4,24`. Signal — et c'est celui sur lequel on agit à la question 3.

> **Ce que coûtent les deux erreurs.** [E09](../modules/E09-mesure-et-incrementalite.md) § 7.6 fait le calcul sur le modèle de référence : attendre quatre jours de trop coûte 56 012 € de contribution, réagir à tort 54 743 €. Même prix — mais les fausses alertes sont **dix fois plus fréquentes** que les vraies pannes. C'est cette asymétrie, et non le sang-froid, qui justifie d'écrire une règle de déclenchement et de s'y tenir.

**Barème.** 8 points pour identifier (α) et **uniquement** (α). 6 pour la démonstration : 2 le regroupement S5–S8, 2 le nombre attendu, 2 le z comparé à 2σ. 2 par signal justifié (6). Identifier (α) sans calcul : 8 sur 20. Déclarer (δ) du bruit : 0 sur la question — l'erreur symétrique, celle qui fait rater la meilleure campagne du compte.

---

### Question 5 — Ce que le compte de résultat impose

**(a) Le chiffre d'affaires et le MER, sur T4**

```
CA TTC des premières commandes = 2 245 × 61,00 €        = 136 945 € TTC
Le réachat pèse 28,0 % du CA total, donc les premières commandes en pèsent 72,0 % :
CA TTC total                   = 136 945 ÷ 0,72         = 190 201 € TTC
MER                            = 190 201 ÷ 78 000       = 2,44
```

**(b) Les deux seuils**

```
MER seuil CM3 = 0      = 1,20 ÷ CM2 = 1,20 ÷ 0,590            = 2,03

CA HT                  = 190 201 ÷ 1,20                       = 158 501 € HT
Frais fixes en % du CA HT = 22 000 ÷ 158 501                  = 13,88 %
MER seuil EBITDA = 0   = 1,20 ÷ (0,590 − 0,1388) = 1,20 ÷ 0,4512 = 2,66
```

Contrôle par le compte de résultat, qui doit tomber juste :

```
Marge brute CM2 = 158 501 × 59,0 %                  =  93 516 € HT
CM3             = 93 516 − 78 000                   =  15 516 € HT
EBITDA          = 15 516 − 22 000                   =  −6 484 € HT
                                                       soit −4,09 % du CA HT
```

**(c) Ce que ces trois nombres imposent.**

ORÈNE est **au-dessus** de son seuil de contribution (2,44 > 2,03) et **sous** son seuil de résultat (2,44 < 2,66) : chaque euro de chiffre d'affaires supplémentaire crée de la marge de contribution mais l'entreprise perd de l'argent. Le budget total ne peut donc pas monter tant que le CAC marginal du compte reste à 47,81 €. La question 3 était déjà tranchée avant même de regarder les campagnes.

> **À retenir :** le CAC marginal dit **où** mettre l'argent. Le MER comparé à ses deux seuils dit **combien** il y en a à mettre. Ce sont deux décisions différentes, et confondre les deux est la faute d'allocation la plus commune du métier.

**Barème.** (a) 2 pour le CA TTC total — oublier le réachat, donc diviser par 1 au lieu de 0,72, coûte les 5 points ; 3 pour le MER. (b) 3 par seuil, calcul déroulé. (c) 2 pour le positionnement entre les deux seuils, 2 pour la conclusion sur le budget total.

---

## 6. Le critère de passage

**Note minimale : 72 / 100.** Le seuil est plus haut qu'à L03 parce qu'on ne juge plus une production mais une **décision engageant un budget**.

**Quatre fautes éliminatoires** :

1. **Juger une hausse de budget sur le CAC moyen.** C'est la faute que le niveau existe pour éliminer. Elle se trompe systématiquement dans le sens qui encourage à dépenser plus.
2. **Confondre TTC et HT** dans le calcul du MER ou de ses seuils. Le MER se calcule sur le CA **TTC**, la marge sur le CA **HT**. Un MER de 2,44 ne veut pas dire que la publicité coûte 41 % du chiffre d'affaires : elle en coûte `1,20 ÷ 2,44 = 49,2 %` du CA HT.
3. **Utiliser les 2 492 achats revendiqués par les régies** au lieu des 2 245 nouveaux clients dédoublonnés. L'écart de 11,0 % est annoncé en toutes lettres dans l'énoncé. Additionner des chiffres de plateformes est une faute de fond, pas d'inattention.
4. **Réagir à (α)**, c'est-à-dire traiter une variation hebdomadaire à z = 1,17 comme un fait. Un compte piloté à la semaine sur du bruit ne converge jamais : il oscille.

**Deux fautes lourdes**, non éliminatoires : couper #5 sans mentionner l'incrémentalité (−8) ; augmenter une campagne de plus de 30 % en une tranche (−6).

**En cas d'échec**, tu repasses sur un dossier de même structure aux nombres différents — huit semaines, six campagnes, une variation de bruit plantée quelque part. Jamais celui-ci.

---

## 7. Les pièges de ce niveau

**1. Croire qu'on comprend le CAC marginal parce qu'on sait le calculer.** La division est triviale, le réflexe ne l'est pas. Le test honnête : la prochaine fois que tu veux monter un budget de 20 %, calcule le prix de la tranche **avant** de la lancer. La plupart de ceux qui savent le définir ne s'en sont jamais servis pour refuser une hausse.

**2. Prendre un bon CPA moyen pour une autorisation de scaler.** La campagne #3 a le meilleur CPA du compte hors search et le pire marginal après #2. Un CPA moyen est un **historique** ; un CAC marginal est le **prix affiché de la prochaine tranche**. On n'achète jamais au prix historique.

**3. Croire que la zone morte est une absence de décision.** Ne rien faire sur #1 — 29 200 € de budget, un tiers du compte — **est** la décision, et c'est la plus difficile du dossier. Bouger un budget situé entre les deux seuils, c'est payer une période d'apprentissage pour un gain que la règle dit inexistant.

**4. Confondre saturation d'audience et fatigue créative.** Les deux font monter le CPA ; la fréquence les distingue, en montant fortement dans le premier cas et pas dans le second. Le dossier contient les deux profils : #2 et #3 saturent (×2,0 et ×3,2), #4 progresse à fréquence constante. Se tromper, c'est produire des créas pour un problème d'audience ou changer d'audience pour un problème de créa. Les deux coûtent un trimestre.

**5. Réagir à la semaine.** Une semaine de campagne, c'est une centaine d'achats et un écart-type de 10 %. Un compte piloté à la semaine réagit à des tirages, et chaque réaction remet des campagnes en apprentissage. Le rythme est **hebdomadaire pour l'observation, mensuel pour la structure** ([E09](../modules/E09-mesure-et-incrementalite.md) § 7.5) — et les deux ne se mélangent jamais.

**6. Croire que le budget total est une variable libre.** Il est borné par les deux nombres de la question 5. Un compte sous son seuil de résultat ne se répare ni en dépensant plus ni en dépensant moins au hasard : il se répare en déplaçant l'argent vers les marginaux les plus bas.

**7. Croire que L04 mesure ta marque.** C'est ici que l'écart entre les deux échelles est le plus dangereux. Une marque à **N3** — 500 000 € TTC par mois — dont personne ne sait faire la question 1 dépense chaque mois des centaines de milliers d'euros à un prix marginal que personne ne connaît. Tant que le marché porte, la croissance couvre l'erreur d'allocation et l'entreprise attribue son succès à ses décisions. Le jour où elle s'arrête, il ne reste ni méthode, ni instrument, ni personne pour lire le compte — et les premières décisions prises en urgence sont presque toujours des hausses de budget.

---

*Fin du niveau L04. Suite : [L05 — Constructeur](L05-constructeur.md), où l'on cesse d'allouer un budget pour fabriquer ce qui le rend rentable.*
