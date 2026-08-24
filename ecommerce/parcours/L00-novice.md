# Niveau L00 — Novice

> **Prérequis :** aucun. C'est le point d'entrée du parcours. Tu n'as jamais vendu, tu ne connais pas le vocabulaire, et c'est exactement la situation pour laquelle ce niveau est écrit.
> **Ce que tu sais faire à la sortie :**
> — tu convertis un montant TTC en HT et l'inverse sans réfléchir, et tu n'écris plus jamais un montant sans préciser lequel des deux c'est ;
> — tu calcules un coefficient, un panier moyen, un MER et un MER seuil à partir de données brutes, sans regarder une formule ;
> — tu nommes les six nombres qui décident si une marque vit, et tu dis pour chacun ce qu'il sert à trancher.
>
> **Temps de travail typique :** 8 à 12 h — 4 h de lecture, 3 à 6 h d'entraînement au calcul, 25 minutes d'épreuve.

---

## 0. Les deux échelles, et pourquoi tu dois lire ceci avant tout le reste

Ce cursus te mesure sur **deux règles graduées indépendantes**, et les confondre est la première erreur qu'on peut commettre ici.

| Échelle | Ce qu'elle mesure | Comment on la gagne | Où elle est définie |
|---|---|---|---|
| **Lxx**, de L00 à L10 | Ta **compétence** | Une épreuve notée, sur un dossier que tu n'avais jamais vu | ce dossier `parcours/` |
| **Nx**, de N0 à N4 | L'état de ton **business** | Ton chiffre d'affaires et tes indicateurs mesurés | [diagnostic](../mentorat/diagnostic.md) |

Elles ne se déduisent pas l'une de l'autre. On peut être **L07 sans entreprise** — c'est le profil d'un bon opérateur salarié en agence, qui sait lire une cascade de marges et allouer un budget mais n'a jamais possédé de stock. Et on peut être **N3 avec une compétence L04** : une marque à 500 000 € TTC par mois pilotée par quelqu'un qui n'a jamais calculé de CAC marginal.

**Ce second cas est le plus dangereux du métier, et c'est aussi le plus fréquent.** Le chiffre d'affaires masque l'incompétence tant que le marché est porteur : les concepts publicitaires marchent, la croissance couvre les erreurs de calcul, et personne n'a besoin de savoir lire. Le jour où le coût d'acquisition monte de 30 %, la marque découvre qu'elle n'a personne pour dire ce qui se passe — et elle le découvre avec du stock payé et six semaines de trésorerie.

Tu es peut-être N2 ou N3 en lisant ceci. Tu es quand même L00 tant que tu n'as pas passé l'épreuve ci-dessous. **La règle du parcours est de garder ton niveau L au-dessus de ton niveau N, toujours.** Si ton entreprise grandit plus vite que ta compétence, tu ne pilotes plus : tu subis, et tu appelles ça de la chance.

---

## 1. Les compétences du niveau

Une compétence n'est pas une connaissance. « Je sais ce qu'est un MER » ne se vérifie pas. « Je calcule un MER à partir d'un relevé bancaire et d'une facture média en moins de trente secondes » se vérifie. Les huit compétences de L00 sont donc écrites comme des actes.

1. **Je convertis un montant TTC en HT et un montant HT en TTC de tête ou à la calculatrice, sans hésiter sur le sens de la division**, et je sais dire combien de TVA contient un chiffre d'affaires donné.
2. **Je n'écris jamais un montant sans la mention TTC ou HT** — et quand je lis un montant sans mention, je le traite comme une donnée manquante, pas comme un montant.
3. **Je calcule un coefficient** (prix de vente TTC ÷ coût de revient rendu entrepôt) et j'en déduis directement la part du coût marchandise dans le chiffre d'affaires HT, par la division `1,20 ÷ coefficient`.
4. **Je calcule un panier moyen** à partir d'un chiffre d'affaires et d'un nombre de commandes, et je distingue le panier moyen mixte du panier moyen des nouveaux clients.
5. **Je calcule un MER** (chiffre d'affaires TTC ÷ dépense publicitaire totale) et j'en déduis la part de la publicité en pourcentage du chiffre d'affaires **HT** par la division `1,20 ÷ MER` — sans jamais écrire `1 ÷ MER`.
6. **Je calcule un MER seuil de contribution** par la division `1,20 ÷ taux de marge brute`, et je dis si la marque gagne ou perd de l'argent sur son euro de publicité suivant.
7. **Je calcule un nCAC** en divisant **toute** la dépense publicitaire par les **nouveaux** clients seulement, et je sais dire pourquoi le dénominateur exclut les clients qui reviennent.
8. **Je nomme les six nombres qui décident** ([E01](../modules/E01-arithmetique-de-la-marque.md) § 0) et j'associe à chacun la décision qu'il tranche.

Aucune de ces huit compétences n'est difficile. C'est précisément le problème : elles sont si simples que presque personne ne les vérifie, et une marque sur deux en calcule au moins deux faux.

---

## 2. Ce que tu lis

Dans cet ordre. Les deux lectures font environ quatre heures ; ne les étale pas sur trois semaines, l'effet recherché est que le vocabulaire devienne réflexe.

| Ordre | Lecture | Ce que ça apporte **à ce niveau précisément** |
|---|---|---|
| 1 | [**E00 — Le cadrage**](../modules/E00-cadrage.md), en entier | Le décor : ce qu'est physiquement une marque à 1 M€ TTC par semaine, les quatre façons de gagner de l'argent, les cinq modes de mort. Le § 1 y définit le **coefficient** et la formule `COGS en % du CA HT = 1,20 ÷ coefficient`, qui est la moitié de l'épreuve. |
| 2 | [**E01 — L'arithmétique**](../modules/E01-arithmetique-de-la-marque.md), **sections 0 à 2 seulement** | Le § 0 donne les six nombres. Le § 1 donne la cascade CA TTC → CA HT → CM1 → CM2 → CM3 → EBITDA, avec qui est responsable de chaque étage. Le § 2 démontre le piège TTC/HT et chiffre ce qu'il coûte : un sixième de ta dépense publicitaire, tous les mois. |
| 3 | [Chiffres canoniques](../donnees/chiffres-canoniques.md), **§ 1, § 2 et § 9** | Les ordres de grandeur de référence. Tu ne les apprends pas par cœur ; tu apprends à retrouver un nombre dedans en moins de quinze secondes, parce que toutes les épreuves suivantes s'y adossent. |

**Ne lis pas E01 § 3 à § 11 maintenant.** C'est le programme de L01, et le lire trop tôt produit la pire chose qui puisse arriver à ce stade : le sentiment d'avoir compris, qui arrête la recherche.

---

## 3. Ce que tu fais

À L00, il n'y a ni séance d'atelier ni simulateur : tu n'as pas encore de quoi décider quoi que ce soit. Tu fais des gammes.

| Travail | Livrable attendu |
|---|---|
| **Le tableau de conversion** — recopie à la main les sept lignes du § 9 des chiffres canoniques, puis reconstruis-les à partir de la seule colonne « CA TTC / semaine ». | Une feuille où les colonnes « CA TTC/mois », « CA TTC/an », « commandes/jour » et « dépense pub/jour » ont été **recalculées**, pas recopiées, avec les divisions écrites. |
| **Cinquante conversions TTC/HT chronométrées** — tire cinquante montants au hasard entre 9 € et 900 €, convertis dans les deux sens, vérifie. | Le chronomètre. L'objectif est **moins de 8 secondes par conversion** et **zéro erreur de sens**. Tant que tu hésites sur « je divise ou je multiplie », tu n'es pas L00. |
| **Les six nombres, de mémoire** — écris les six nombres de E01 § 0, puis pour chacun la décision qu'il tranche et qui en est responsable. | Une page. Compare-la ensuite à E01 § 1.3, et note les écarts : ce sont tes trous. |
| **La chasse aux montants sans mention** — reprends n'importe quelle page de vente, publication ou fiche produit d'une marque que tu suis, et surligne chaque montant sans TTC ni HT. | La liste. Elle t'apprendra plus vite que n'importe quel cours que cette faute est partout, y compris chez des gens qui vendent beaucoup. |
| **[E01 exercices 1 et 2](../modules/E01-arithmetique-de-la-marque.md) uniquement** (les autres exigent E01 § 3 et suivants). | Les réponses numériques, avec le calcul déroulé et pas seulement le résultat. |

---

## 4. L'épreuve

> **Marque fictive.** MIRAN est une marque inventée pour cette épreuve. Ses chiffres sont un modèle cohérent, ce ne sont les comptes d'aucune entreprise réelle.

**Temps imparti : 25 minutes.** Calculatrice autorisée, aucun document, aucune formule sous les yeux, aucun accès au cursus. Vingt-cinq questions, **barème sur 100**.

Vingt-cinq minutes pour vingt-cinq questions, ce n'est pas une brimade : à ce niveau on ne mesure pas ce que tu sais, on mesure ce qui est devenu automatique. Un opérateur qui met trois minutes à convertir un TTC en HT ne le fera pas dans la vraie vie — il devinera. Arrondis à deux décimales sauf mention contraire.

### Le dossier MIRAN

MIRAN vend un complément alimentaire en direct au consommateur, en France uniquement. TVA 20 %.

| Donnée | Valeur |
|---|---|
| Prix de vente du produit héros | 34,80 € TTC |
| Coût de revient complet rendu entrepôt du héros | 5,80 € |
| Commandes des 30 derniers jours | 1 800 |
| Chiffre d'affaires des 30 derniers jours | 84 600 € TTC |
| Dont : nouveaux clients | 1 200 commandes, panier moyen 44,00 € TTC |
| Dont : clients déjà acquis | 600 commandes, panier moyen 53,00 € TTC |
| Dépense publicitaire des 30 derniers jours (toutes régies, production créative incluse) | 36 000 € |
| Taux de marge brute (CM2) mesuré | 55,0 % du CA HT |
| Frais fixes mensuels (salaires chargés, outils, honoraires) | 9 000 € |

---

### Partie A — Vocabulaire (10 questions, 3 points chacune, 30 points)

Réponse en une à trois lignes. On note la précision, pas la longueur.

**Q1.** Cite les six nombres qui décident si une marque de e-commerce vit. *(0,5 point par nombre correctement nommé.)*

**Q2.** Un fondateur te dit : « je fais 4 millions d'euros par mois ». Quelle information viens-tu de recevoir sur la santé de son entreprise ? Justifie en une phrase.

**Q3.** Qu'est-ce que la TVA, du point de vue de la trésorerie d'une marque ? À qui appartient-elle ?

**Q4.** Définis le COGS. Cite trois postes qu'il contient **en plus** du prix payé au fabricant.

**Q5.** Donne la formule du coefficient d'un produit, et dis sur quel prix elle se calcule — TTC ou HT.

**Q6.** Définis le nCAC. Précise son numérateur et son dénominateur, et dis en une phrase pourquoi le dénominateur exclut les clients qui reviennent.

**Q7.** Définis la LTV. Dans quelle unité se calcule-t-elle, et sur quel horizon ce cursus la plafonne-t-il ?

**Q8.** Définis le MER. Sur quel chiffre d'affaires — TTC ou HT — se lit son numérateur, et pourquoi cette précision n'est pas un détail ?

**Q9.** Définis l'AOV. Donne sa formule et cite une raison pour laquelle l'AOV mixte peut être trompeur.

**Q10.** Nomme, dans l'ordre, ce qu'on retranche pour passer du CA HT à CM1, de CM1 à CM2, de CM2 à CM3, et de CM3 à l'EBITDA.

---

### Partie B — Lecture (5 questions, 4 points chacune, 20 points)

**Q11.** Trois affirmations. Pour chacune, dis si elle est correctement formulée, et si non, ce qui manque.
 (a) « Notre panier moyen est de 62 €. »
 (b) « On a fait 210 000 € de chiffre d'affaires HT le mois dernier. »
 (c) « Le produit nous coûte 4,80 € et on le vend 39,00 €, ça fait 85 % de marge. »

**Q12.** Remets ces six lignes dans l'ordre d'une cascade de marges, de haut en bas : *frais fixes, publicité, CA HT, COGS, logistique, remises*.

**Q13.** Un prestataire te présente une « LTV de 169,40 € » pour un coût d'acquisition de 40,03 €. Quelle est **la seule question** à lui poser avant d'exploiter ce chiffre, et pourquoi ?

**Q14.** Au palier P1 du modèle de référence, l'EBITDA vaut −30,7 % du CA HT. Cite les deux causes structurelles de ce signe négatif, et dis si cela suffit à conclure que la marque est mal gérée.

**Q15.** Deux marques ont exactement le même chiffre d'affaires TTC hebdomadaire — 999 968 € et 999 978 €. L'une dégage 10,1 % d'EBITDA, l'autre 20,3 %. Que t'apprend cette comparaison sur la valeur du chiffre d'affaires comme objectif ?

---

### Partie C — Calculs (10 questions, 5 points chacune, 50 points)

Le calcul doit être **écrit**, pas seulement le résultat. Une réponse juste sans calcul vaut 2 points sur 5.

**Q16.** Le produit héros de MIRAN est vendu 34,80 € TTC. Quel est son prix hors taxes ?

**Q17.** MIRAN prévoit 187 500 € de chiffre d'affaires **HT** le mois prochain. Quel chiffre d'affaires **TTC** cela représente-t-il, et quel montant de TVA la marque devra-t-elle reverser ?

**Q18.** Quel est le coefficient du produit héros ?

**Q19.** Quel pourcentage du chiffre d'affaires **HT** le coût marchandise du héros représente-t-il ? Réponds **sans** utiliser les euros du Q16 : utilise le coefficient.

**Q20.** Quel est le panier moyen (AOV) mixte des 30 derniers jours ?

**Q21.** Quel est le MER blended des 30 derniers jours ?

**Q22.** Quelle part du chiffre d'affaires **HT** la publicité représente-t-elle ? *(Question éliminatoire.)*

**Q23.** Quel est le MER seuil de contribution de MIRAN — le MER en dessous duquel chaque euro de chiffre d'affaires supplémentaire détruit de la marge ?

**Q24.** Calcule le MER seuil de résultat nul (EBITDA = 0), puis dis si MIRAN gagne ou perd de l'argent ce mois-ci, et combien.

**Q25.** Calcule le nCAC de MIRAN, puis la contribution de la première commande d'un nouveau client, puis la marge à la première commande. Conclus en une phrase.

---

## 5. Le corrigé

### Partie A

**Q1 — 3 points.** Les six nombres ([E01](../modules/E01-arithmetique-de-la-marque.md) § 0) : (1) la marge brute CM2 en % du CA HT ; (2) le MER et son seuil ; (3) le nCAC ; (4) la LTV à 12 mois en marge de contribution ; (5) le payback du CAC, en mois ; (6) les frais fixes en % du CA HT. *0,5 point par nombre. « Le chiffre d'affaires », « le taux de conversion » et « le ROAS » ne valent aucun point : aucun des trois ne tranche une décision seul.*

**Q2 — 3 points.** Aucune information sur la santé de l'entreprise. Un CA de 4 M€ TTC par mois peut correspondre à un EBITDA de +364 752 € comme à une perte de 500 000 € : le chiffre d'affaires est une taille, pas une performance. *3 points pour « aucune information » assortie de la justification ; 1 point pour une réponse hésitante ; 0 point pour « c'est une grosse entreprise ».*

**Q3 — 3 points.** La TVA est un impôt collecté sur le client pour le compte de l'État. Elle transite par ton compte bancaire mais ne t'appartient jamais : c'est une dette fiscale. Sur 4 333 196 € TTC encaissés, 722 199 € sont de la TVA et 3 610 997 € sont du chiffre d'affaires. *2 points pour la nature, 1 point pour « ce n'est pas mon argent ».*

**Q4 — 3 points.** Le COGS (*cost of goods sold*) est le coût marchandise **rendu entrepôt**. En plus du prix usine : le fret, les droits de douane, le contrôle qualité et les analyses libératoires, la provision pour casse et non-conformité, l'amortissement de l'outillage, l'emballage primaire et l'étui. *1 point pour la définition, 2 points pour trois postes corrects. « Le transport vers le client » ne compte pas : c'est de la logistique, pas du COGS.*

**Q5 — 3 points.** `Coefficient = prix de vente TTC ÷ COGS rendu entrepôt`. Il se calcule sur le prix **TTC**. *2 points pour la formule, 1 point pour TTC. Répondre « sur le prix HT » coûte le point : c'est une convention métier, et l'ignorer fausse toutes les comparaisons de catégorie.*

**Q6 — 3 points.** `nCAC = toute la dépense publicitaire ÷ nombre de NOUVEAUX clients`. Le numérateur prend tout, y compris le retargeting et la production créative ; le dénominateur ne prend que les nouveaux, parce que la seule question que le budget média doit trancher est : « combien me coûte le fait de faire entrer un client de plus dans ma base ? ». Un dénominateur incluant les clients qui reviennent produit un CAC qui **s'améliore mécaniquement quand la part de réachat monte**, c'est-à-dire qui flatte au moment exact où l'acquisition se dégrade. *1 point numérateur, 1 point dénominateur, 1 point justification.*

**Q7 — 3 points.** La LTV est la valeur cumulée d'un client sur un horizon donné. Elle se calcule **en marge de contribution**, jamais en chiffre d'affaires, et le cursus la plafonne à **12 mois** — une extrapolation à 24 ou 36 mois n'est pas une mesure. *1 point définition, 1 point contribution, 1 point 12 mois. Une réponse en chiffre d'affaires vaut 0 sur toute la question.*

**Q8 — 3 points.** `MER = chiffre d'affaires total TTC ÷ dépense publicitaire totale`. Le numérateur se lit sur le **TTC** — c'est ce que la banque encaisse — alors que toute marge se calcule sur le HT. La précision décide de tout : la part de la publicité vaut `(1 + TVA) ÷ MER` et non `1 ÷ MER`, un écart de 6,9 points de CA HT à MER 2,90. *1 point formule, 1 point TTC, 1 point conséquence.*

**Q9 — 3 points.** `AOV = chiffre d'affaires ÷ nombre de commandes`, sur la même période et la même base (TTC ou HT, précisée). L'AOV mixte mélange les nouveaux clients et les clients qui reviennent, dont les paniers diffèrent nettement ; l'utiliser pour calculer une contribution de première commande surestime celle-ci. *2 points formule et unité, 1 point piège.*

**Q10 — 3 points.** CA HT → CM1 : le COGS. CM1 → CM2 : logistique, frais de paiement (PSP), retours et SAV, remises. CM2 → CM3 : la publicité, production créative et honoraires compris. CM3 → EBITDA : les frais fixes. *0,75 point par passage. Oublier la ligne « remises » coûte le passage entier : c'est un coût variable, pas une réduction de prix affichée.*

### Partie B

**Q11 — 4 points.**
 (a) **Incorrecte** : montant sans mention TTC ou HT. Manque la base. *(1,5 point)*
 (b) **Correcte** : la base est précisée. *(1 point)*
 (c) **Incorrecte** : 39,00 € est un prix TTC et 4,80 € un coût. Le rapport `(32,50 − 4,80) ÷ 32,50 = 85,2 %` est une **marge marchandise**, pas « la marge » — il ne reste rien après logistique, paiement, retours, remises, publicité et frais fixes. *(1,5 point)*

**Q12 — 4 points.** CA HT, COGS, logistique, remises, publicité, frais fixes. *(Logistique et remises sont tous deux entre CM1 et CM2 ; leur ordre relatif est indifférent. 4 points si l'ordre des cinq blocs est juste, 2 points si une seule ligne est mal placée, 0 si la publicité passe avant les remises.)*

**Q13 — 4 points.** « **En chiffre d'affaires ou en marge de contribution ?** » — et s'il hésite, c'est du chiffre d'affaires. Sur le modèle de référence, 169,40 € de CA cumulé TTC à 12 mois valent 86,75 € de contribution : `169,40 ÷ 1,20 × 61,45 % = 86,75 €`, facteur 1,95. Le ratio annoncé serait 4,23, le vrai est 2,17. *3 points pour la question, 1 point pour l'ordre de grandeur du facteur (environ ×2).*

**Q14 — 4 points.** Deux causes : (1) les frais fixes pèsent 21,2 % du CA HT à P1 contre 10,0 % à P5 — l'entreprise porte une structure calibrée pour sa taille future ; (2) le MER réel de 1,80 est sous le MER seuil EBITDA de 3,33, la marque achète volontairement des clients à perte sur la première commande. **Non, cela ne suffit pas à conclure qu'elle est mal gérée** : c'est rationnel si la LTV 12 mois couvre le nCAC plus les frais fixes par client, si le cash tient neuf mois de perte cumulée plus le BFR, et si le seuil de réachat déclenchant l'arrêt a été écrit d'avance. *2 points causes, 2 points nuance. Répondre « oui, elle est mal gérée » plafonne à 2.*

**Q15 — 4 points.** Que le chiffre d'affaires ne dit rien du résultat. Le même CA produit 4 377 023 € ou 8 805 583 € d'EBITDA annuel selon la façon dont il est fabriqué — panier, part de réachat, discipline sur la remise, MER. **Le chiffre d'affaires est une conséquence, pas un objectif.** *3 points pour le raisonnement, 1 point pour l'ordre de grandeur de l'écart (environ ×2, environ 4,4 M€ par an).*

### Partie C

**Q16 — 5 points.**
```
34,80 ÷ 1,20 = 29,00 € HT
```
*Diviser par 1,20, jamais retrancher 20 %. Retrancher 20 % donne 27,84 €, soit 1,16 € d'erreur par unité — 4,0 % du prix HT.*

**Q17 — 5 points.**
```
CA TTC = 187 500 × 1,20              = 225 000 € TTC
TVA    = 225 000 − 187 500           =  37 500 €
   ou    187 500 × 0,20              =  37 500 €
```
*2,5 points par grandeur.*

**Q18 — 5 points.**
```
34,80 ÷ 5,80 = 6,00     →  ×6,00
```

**Q19 — 5 points.**
```
COGS en % du CA HT = 1,20 ÷ coefficient = 1,20 ÷ 6,00 = 20,00 %
Contrôle (non demandé) : 5,80 ÷ 29,00 = 20,00 %        ✓
```
*Le 1,20 du numérateur est le `1 + TVA`. Écrire `1 ÷ 6,00 = 16,67 %` vaut 0 : c'est le même oubli de TVA qu'au Q22, et il minore le coût marchandise de 3,33 points de CA HT.*

**Q20 — 5 points.**
```
AOV mixte = 84 600 ÷ 1 800 = 47,00 € TTC
Contrôle : (1 200 × 44,00 + 600 × 53,00) ÷ 1 800
         = (52 800 + 31 800) ÷ 1 800 = 47,00 €        ✓
```
*Une réponse sans la mention TTC plafonne à 3 points.*

**Q21 — 5 points.**
```
MER = 84 600 ÷ 36 000 = 2,35
```
*Le MER est un ratio sans unité ; son numérateur est du TTC par définition.*

**Q22 — 5 points, éliminatoire.**
```
CA HT = 84 600 ÷ 1,20                            = 70 500 €
Part de la pub = 1,20 ÷ 2,35                     = 51,06 % du CA HT
Contrôle : 36 000 ÷ 70 500                       = 51,06 %      ✓
```
*La réponse fausse attendue est `1 ÷ 2,35 = 42,55 %`. L'écart vaut `0,20 ÷ 2,35 = 8,51` points de CA HT, soit `70 500 × 0,0851 = 5 999 €` par mois — ou plus court, `36 000 ÷ 6 = 6 000 €`, un sixième de la dépense publicitaire. **72 000 € par an**, pour une entreprise dont le résultat mensuel est de −6 225 € (Q24). Cette question est éliminatoire parce qu'aucune décision de budget ne peut être prise correctement par quelqu'un qui la rate.*

**Q23 — 5 points.**
```
MER seuil (CM3 = 0) = 1,20 ÷ taux de marge brute
                    = 1,20 ÷ 0,550 = 2,1818  →  2,18
```
*MIRAN tourne à 2,35, donc au-dessus de 2,18 : chaque euro de CA supplémentaire apporte de la marge de contribution. Ce seuil ne dépend ni de la taille ni du panier — seulement de la TVA et de la marge brute.*

**Q24 — 5 points.**
```
Frais fixes en % du CA HT   =  9 000 ÷ 70 500      = 12,77 %
Marge brute − frais fixes   =  55,00 − 12,77       = 42,23 %
MER seuil (EBITDA = 0)      =  1,20 ÷ 0,4223       = 2,84

MER réel 2,35  <  2,84  →  MIRAN perd de l'argent.

Vérification par la cascade :
   CA HT                                     70 500 €
   Marge brute  (70 500 × 55,0 %)            38 775 €
   − Publicité                              −36 000 €
   = CM3                                      2 775 €      (+3,94 % du CA HT)
   − Frais fixes                             −9 000 €
   = EBITDA                                  −6 225 €      (−8,83 % du CA HT)
```
*2 points le seuil, 1 point le verdict, 2 points la vérification chiffrée. Répondre « rentable parce que le MER dépasse 2,18 » vaut 1 point : c'est confondre les deux seuils, et c'est exactement l'erreur qui fait recruter une marque qui perd de l'argent.*

**Q25 — 5 points.**
```
nCAC = 36 000 ÷ 1 200                                 = 30,00 €

Contribution de la 1ʳᵉ commande
   = AOV nouveaux clients HT × marge brute
   = (44,00 ÷ 1,20) × 0,550 = 36,6667 × 0,550         = 20,17 €

Marge à la 1ʳᵉ commande = 20,17 − 30,00               = −9,83 €
```
*Conclusion attendue : MIRAN perd 9,83 € sur chaque premier achat, soit `1 200 × 9,83 = 11 796 €` par mois. Ce n'est pas anormal en soi — le modèle de référence perd de 4,93 € à 7,26 € à tous les paliers — mais ce n'est finançable que par le réachat, qu'il faut donc mesurer. Utiliser l'AOV mixte de 47,00 € au lieu de 44,00 € donne 21,54 € et minore la perte de 20 % : −1 point.*

---

## 6. Le critère de passage

| | |
|---|---|
| **Note minimale** | **80 / 100** |
| **Questions éliminatoires** | **Q22** — la part de la publicité en % du CA HT. **Q7** — une LTV définie en chiffre d'affaires. **Q16 ou Q17** — un sens de conversion TTC/HT inversé. |
| **Temps** | 25 minutes. Au-delà de 30 minutes, l'épreuve est comptée comme échouée quelle que soit la note. |

Quatre-vingts sur cent est volontairement haut, et plus haut que le seuil des niveaux suivants. La raison est simple : **on ne mesure pas ici des connaissances, on mesure des automatismes.** Une connaissance à 70 % est une connaissance partielle, avec laquelle on travaille. Un automatisme à 70 % n'est pas un automatisme : c'est une erreur qui se déclenche trois fois par semaine, dans les trois décisions où tu n'auras pas pris le temps de vérifier.

Les questions éliminatoires ne se rachètent pas par la note globale. Une erreur de sens TTC/HT ou une LTV en chiffre d'affaires sont les deux fautes qui coûtent le plus cher dans la vraie vie — 2 988 412 € par an au palier P5 du modèle de référence pour la première, un facteur 1,95 sur toutes les décisions d'acquisition pour la seconde. Elles coûtent donc cher ici.

**En cas d'échec :** tu refais les cinquante conversions chronométrées, tu relis E01 § 2 en refaisant chaque calcul à la main, et tu repasses une **variante** de l'épreuve — pas la même. Une épreuve repassée à l'identique mesure ta mémoire, pas ta compétence.

---

## 7. Les pièges de ce niveau

Voici ce que les gens croient avoir compris à la sortie de L00, et qu'ils n'ont pas compris. Chacun de ces sept points a été observé chez des opérateurs qui vendaient déjà.

**1. « Ma marge est de 85 %. »** Non : ta **marge marchandise** est de 85 %. C'est le premier étage de six. Sur le modèle de référence, 85,5 % de marge marchandise deviennent 61,45 % de marge brute, 20,07 % de marge de contribution, et 10,10 % d'EBITDA. Le nombre que tu cites en soirée et le nombre qui te paie n'ont aucun rapport.

**2. « La pub, c'est un tiers de mon chiffre d'affaires. »** Presque toujours faux, et toujours faux dans le même sens. Si tu as calculé `1 ÷ MER`, tu as oublié la TVA, et tu te crois rentable de `TVA ÷ MER` points que tu n'as pas. Le raccourci qui te sauvera : **l'erreur vaut exactement un sixième de ta dépense publicitaire** quand la TVA est à 20 %.

**3. « Mon produit est à ×3, donc il me reste 66 % de marge. »** Non. `1,20 ÷ 3 = 40 %` de coût marchandise sur le CA HT, donc 60 % avant logistique, paiement, retours et remises. Après ce bloc, il reste environ 36 % de marge brute, ce qui porte le MER seuil de contribution à 3,34 — un niveau qu'aucune marque ne tient en acquisition payante froide. Un coefficient est un verdict, pas une indication.

**4. « Mon CAC, c'est ce que la plateforme m'affiche. »** Ce que la plateforme affiche est un coût par achat attribué, sur son seul périmètre, avec sa seule fenêtre d'attribution, et sans distinguer les nouveaux clients des anciens. Ton nCAC est un autre nombre, souvent supérieur de 10 à 40 %. Tant que tu n'as pas fait la division toi-même, tu n'as pas de CAC.

**5. « J'ai une LTV de 170 €. »** Tu as un chiffre d'affaires cumulé. La LTV en marge de contribution vaut environ la moitié. Personne ne se trompe jamais en sous-estimant sa LTV : le biais est systématiquement dans le même sens, donc il ne s'annule pas dans la moyenne de tes décisions, il s'accumule.

**6. « La TVA que j'encaisse, je la récupère de toute façon. »** Tu la reverses. Elle occupe ton compte bancaire entre l'encaissement et la déclaration, ce qui fait qu'une marque en croissance a en permanence sur son compte de l'argent qui n'est pas à elle — et qu'elle finit par considérer comme de la trésorerie disponible. C'est un des chemins les plus courants vers la crise de liquidité.

**7. « Je connais tout ça, je peux sauter L00. »** C'est la phrase que dit exactement le profil décrit au § 0 : N2 ou N3, chiffre d'affaires réel, compétence L00. Le test est gratuit et dure vingt-cinq minutes. Passe-le. Le cursus a été écrit en partant de l'observation qu'il révèle presque toujours deux automatismes manquants, y compris chez des gens qui vendent depuis trois ans — et qu'un automatisme manquant ne se voit pas dans un compte de résultat annuel, il se voit dans les quarante décisions hebdomadaires qu'il a faussées.

> **À retenir :** L00 ne t'apprend rien sur le e-commerce. Il installe les six ou sept divisions sans lesquelles tout ce que tu liras ensuite sera de la culture générale. Tant que `1,20 ÷ MER` n'est pas un réflexe, tu n'as pas d'arithmétique — tu as des opinions chiffrées.

---

*Fin du niveau L00. Suite : [L01 — Initié](L01-initie.md), où tu construis une cascade complète sur un dossier réel et où tu apprends à repérer les erreurs de calcul d'un directeur financier.*
