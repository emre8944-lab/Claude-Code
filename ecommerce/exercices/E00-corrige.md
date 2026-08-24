# Corrigé — Module E00 : Le cadrage, ce métier vraiment

> **N'ouvre ce fichier qu'après avoir rendu [`E00-rendu.md`](E00-rendu.md).**
> Un corrigé lu avant l'exercice n'enseigne rien : il donne l'illusion d'avoir su.

Tous les nombres ci-dessous se recalculent à partir des
[chiffres canoniques](../donnees/chiffres-canoniques.md) et du module
[E00](../modules/E00-cadrage.md). Aucun n'est cité de mémoire.

---

## Exercice 1 — Le seuil d'un produit à ×3,5

### La réponse

```
1. COGS en % du CA HT = 1,20 ÷ 3,5                          = 34,29 %
2. Autres coûts variables, palier P3 (canonique § 2.1) :
      logistique 12,00 + PSP 1,65 + retours 3,00 + remises 7,00 = 23,65 %
3. Marge brute m = 100 − 34,29 − 23,65                       = 42,06 %
4. MER seuil (CM3 = 0) = 1,20 ÷ 0,42064                      = 2,85
5. f = 105 000 € ÷ 981 000 €                                 = 10,70 %
6. MER seuil (EBITDA = 0) = 1,20 ÷ (0,42064 − 0,10703)
                          = 1,20 ÷ 0,31361                   = 3,83
7. Écart du MER réel au seuil CM3 = 2,70 ÷ 2,85 − 1          = −5,4 %
```

Compte de résultat mensuel complet, à volume P3 identique :

| Ligne | NØRA à P3 | Produit à ×3,5 |
| --- | ---: | ---: |
| CA HT | 981 000 € | 981 000 € |
| Marge brute | 592 033 € (60,35 %) | **412 651 €** (42,06 %) |
| Publicité | −436 000 € | −436 000 € |
| **CM3** | **+156 033 €** | **−23 349 €** |
| Frais fixes | −105 000 € | −105 000 € |
| **EBITDA** | **+51 033 €** | **−128 349 €** |

```
11. Écart d'EBITDA annuel = (51 033 + 128 349) × 12 = 179 382 × 12
                                                    = 2 152 588 € par an
    Contre-vérification : (60,35 % − 42,06 %) × 981 000 × 12
                        = 18,29 points × 981 000 × 12 = 2 152 594 €   ✓
    (l'écart de 6 € est l'arrondi de la marge brute au centième de point)
```

**Ce que ça veut dire.** Le MER réellement atteint par NØRA à P3 est de 2,70. Le
produit à ×3,5 en exige **2,85 pour que sa publicité soit tout juste payée**, et
**3,83 pour que l'entreprise gagne un euro.** Il n'est pas « moins rentable » : il
est en dessous de sa propre ligne de flottaison de contribution, donc **chaque
euro de chiffre d'affaires supplémentaire détruit de la marge**. Le meilleur MER
du modèle canonique, tous paliers et tous marchés confondus, vaut 2,90
(canonique § 2.3) : 3,83 n'est pas un objectif difficile, c'est un nombre hors
de la plage observée.

Contrôle croisé avec le module [E02](../modules/E02-marche-et-produit.md) § 1.1,
qui donne pour ×3,5 un seuil CM3 de 2,88 et un seuil EBITDA de 3,79. L'écart avec
tes 2,85 et 3,83 est normal et il faut savoir le dire : E02 applique la structure
de coût de **P5** (v = 24,05 %, f = 9,97 %), l'exercice celle de **P3**
(v = 23,65 %, f = 10,70 %). Même formule, palier différent.

**La conclusion attendue, en une phrase :** *à ×3,5, ce produit exige un MER de
3,83 pour atteindre l'équilibre là où le meilleur MER du modèle vaut 2,90 — le
refus n'est pas un avis commercial, c'est une inégalité arithmétique.*

### Le barème — sur 20

| Critère | Points |
| --- | ---: |
| COGS = 34,29 % par la formule 1,20 ÷ k, et non 1 ÷ k | 3 |
| Somme des coûts variables du **bon palier** (23,65 %, pas 24,05 %) | 3 |
| Marge brute 42,06 % | 2 |
| MER seuil CM3 = 2,85 | 3 |
| f = 10,70 % calculé, pas recopié | 2 |
| MER seuil EBITDA = 3,83 | 3 |
| Compte de résultat complet et écart annuel ≈ 2,15 M€ | 2 |
| Conclusion qui compare 3,83 à un MER **observé**, pas à une intuition | 2 |

**Fautes éliminatoires — copie à 0 quel que soit le reste.** Avoir écrit le COGS
en % du CA **TTC** (1 ÷ 3,5 = 28,57 %) : c'est l'erreur du module entier, et elle
donne une marge brute fausse de 5,7 points. Avoir conclu « il faudra optimiser les
campagnes » : aucune campagne ne comble 18,29 points de marge brute.

### L'erreur que presque tout le monde fait ici

**Diviser 1 par le coefficient au lieu de 1,20.** Le coefficient se calcule sur un
prix **TTC** et la marge sur du **HT** : il faut donc remonter la TVA avant de
comparer. Écrire `COGS % = 1 ÷ 3,5 = 28,57 %` donne une marge brute de 47,78 %
au lieu de 42,06 %, un MER seuil de 2,51 au lieu de 2,85, et fait passer pour
« serré mais jouable » un produit qui est mort. C'est la même faute que le § 2 du
module [E01](../modules/E01-arithmetique-de-la-marque.md) chiffre à 2 988 412 €
par an à P5, appliquée au coût produit au lieu de la publicité.

---

## Exercice 2 — Le mois de la mort

### La réponse

```
1. Fin de M3 : pertes P1 (3 × 9 403 €) + BFR P1
              = 28 209 € + 21 603 €                        =  49 812 €
2. Constitution mensuelle de BFR en P2 = (104 462 − 21 603) ÷ 6
                                       = 82 859 ÷ 6        =  13 810 €
3. Consommation mensuelle en P2 = 19 838 € + 13 810 €      =  33 648 €
4. Mois financés = (150 000 − 49 812) ÷ 33 648
                 = 100 188 ÷ 33 648                        =   2,98 mois
5. Zéro atteint à M3 + 2,98 mois                           →  fin du mois 6
6. Mois restants jusqu'à la fin de P2 (M9)                 →  3 mois
7. Capital pour atteindre M9 = 49 812 + 6 × 33 648         = 251 699 €
8. Capital additionnel = 251 699 − 150 000                 = 101 699 €
   (ou 370 874 − 150 000 = 220 874 € avec lancement et marge de sécurité)
```

**Le contrôle qui prouve que tu ne t'es pas trompé.** Le § 5.1 du module obtient
251 699 € par une tout autre route : pertes cumulées M1–M9 (147 237 €) + BFR de
P2 (104 462 €). Ton chemin passe par une constitution mensuelle de BFR, le sien
par le BFR terminal. Les deux tombent sur **251 699 €** au dernier euro. Quand
deux chemins indépendants donnent le même nombre, le modèle est cohérent — c'est
la seule vérification qui vaille.

**Ce que ça veut dire.** Trois choses, et la troisième est la seule qui compte.

D'abord, 150 000 € financent **six mois sur les neuf** de la trajectoire, alors
que le total à réunir n'est supérieur que de 68 %. La trésorerie ne s'épuise pas
proportionnellement au capital manquant : elle s'épuise plus vite, parce que la
consommation mensuelle **augmente** en P2 (33 648 € contre 16 604 € en moyenne
sur P1) au moment même où la marque va mieux.

Ensuite, la mort survient **trois mois avant la fin de la vallée** : la marque
n'a jamais vu son premier mois positif, et son dirigeant conclura que le modèle
était faux. Il ne l'était pas.

Enfin, sur les 150 000 € consommés,
`21 603 + 3 × 13 810 = 63 033 €` sont du **BFR** : du stock, des encaissements en
attente et des avances publicitaires. Ce n'est pas de l'argent perdu, c'est de
l'argent immobilisé — mais il est aussi indisponible que s'il avait été brûlé.
**Une marque rentable meurt de la deuxième ligne de son bilan, pas de la
dernière ligne de son compte de résultat.**

**Ce que la marque avait prouvé, ou non.** Elle avait prouvé que le produit se
vend (4 000 commandes par mois à P2) et que son coefficient tient. Elle n'avait
**pas** prouvé sa LTV à 12 mois : à M6, ses plus vieilles cohortes ont cinq mois
de recul. Elle meurt donc au moment exact où la question à laquelle elle payait
pour répondre est encore sans réponse.

### Le barème — sur 20

| Critère | Points |
| --- | ---: |
| Fin de M3 = 49 812 €, pertes **et** BFR comptés | 4 |
| Constitution mensuelle de BFR = 13 810 €, dérivée et non inventée | 4 |
| Consommation mensuelle P2 = 33 648 € | 3 |
| Mois de la mort = fin M6 | 3 |
| Capital pour M9 = 251 699 €, avec le contrôle croisé du § 5.1 | 3 |
| Capital additionnel = 101 699 € (et/ou 220 874 €) | 2 |
| Distinction explicite entre perte et BFR immobilisé | 1 |

**Faute éliminatoire.** Avoir compté les pertes sans le BFR — c'est-à-dire avoir
répondu `(150 000 − 28 209) ÷ 19 838 = 6,1 mois de P2`, donc une mort au mois 10.
Cette réponse fait vivre la marque quatre mois de plus qu'elle ne vit et donne
l'illusion qu'elle franchit P2. C'est exactement l'erreur qui tue.

### L'erreur que presque tout le monde fait ici

**Croire que le BFR se rembourse.** Il ne se rembourse pas tant que l'entreprise
tourne : le stock est remplacé dès qu'il est vendu, les encaissements en attente
sont remplacés par les suivants. Le BFR est une **immobilisation permanente et
croissante**, pas une avance ponctuelle. La conséquence est contre-intuitive et
elle est au canonique § 4 : à P3, chaque tranche de +100 000 € de CA mensuel
immobilise 40 864 € de plus. **Plus la marque réussit, plus elle a besoin de cash.**

---

## Exercice 3 — Ton coefficient et ton seuil

### La grille de lecture

Il n'y a pas de bonne réponse : il y a ta bande, ton diagnostic et ton action.
Lis d'abord sur ton **coefficient au prix réellement encaissé**, jamais au prix
affiché.

| Ton coefficient encaissé | MER seuil CM3 (structure P5) | Diagnostic | Action |
| --- | ---: | --- | --- |
| **< ×3** | ≥ 3,34 | Mort. Aucun MER observé ne l'atteint | Change de produit ou de prix. Rien d'autre n'a d'effet |
| **×3 à ×4** | 2,61 à 3,34 | Ne peut exister qu'en récolte de demande pure | Vérifie que ton Search sature ton volume cible. Sinon, arrête |
| **×4 à ×5** | 2,31 à 2,61 | Très fragile. Un point de remise te ramène à zéro | Remonte le prix ou renégocie le COGS **avant** de dépenser un euro de média |
| **×5 à ×6,4** | 2,10 à 2,31 | Limite basse, jouable si les remises restent sous 5 % | Plafonne la remise par écrit. Vise ×6,7 (E02 § 1.1) |
| **×6,4 à ×8** | 1,96 à 2,10 | Zone NØRA. Le modèle tient | Passe au travail sur l'AOV et le réachat |
| **> ×8** | < 1,96 | Confortable — ou tu as oublié des coûts | Refais le COGS rendu entrepôt poste par poste (E02 § 6.2) |

Puis lis l'**écart entre ton MER réel et ton seuil CM3** :

| Écart | Diagnostic | Action |
| --- | --- | --- |
| **< −20 %** | Situation P1 : chaque commande creuse la perte | Ne monte **aucun** budget. Remonte le MER par le prix, l'offre ou la créative |
| **−20 % à 0 %** | Sous le seuil. C'est une décision si tu l'as prise, une dérive sinon | Écris la date à laquelle tu repasses au-dessus, et le montant que tu acceptes de perdre d'ici là |
| **0 % à +10 %** | Tu paies ta pub, pas ta structure | Travaille les frais fixes en % du CA et l'AOV |
| **+10 % à +25 %** | Zone P3–P5. Tu peux investir | Vérifie ton payback avant d'accélérer (E01) |
| **> +25 %** | Tu sous-investis en média | Monte le budget jusqu'à ce que l'écart redescende vers +20 % |

**Trois pièges de mesure.** Si l'écart entre tes lignes 1 et 2 dépasse 15 %, ta
remise n'est pas une promotion, c'est ton prix : recalcule tout sur la ligne 2.
La sortie usine vaut 88,1 % du COGS chez NØRA (E02 § 6.2) ; l'oublier fait passer
le sérum de ×8,1 à ×9,2, et jusqu'à 22,7 % d'erreur sur un produit importé. Et
écris ta logistique **deux fois** — `X €/commande` et `X ÷ AOV HT` : le
pourcentage est une conséquence de ton panier, pas une propriété de ton contrat.

### Le barème — sur 20

| Critère | Points |
| --- | ---: |
| COGS rendu entrepôt décomposé en au moins six postes | 4 |
| Coefficient calculé **deux fois** : prix affiché et prix encaissé | 3 |
| Chaque ligne marquée (obs) ou (est), sans exception | 3 |
| Structure de coût variable réelle, pas celle de NØRA recopiée | 4 |
| MER seuil calculé avec 1,20 au numérateur | 3 |
| MER réel des 90 derniers jours, calculé banque ÷ factures média | 3 |

**Faute éliminatoire.** Avoir repris les taux de NØRA pour ta logistique, tes
retours ou tes remises. L'exercice ne mesure pas ta capacité à recopier un
tableau : il mesure si tu connais tes propres coûts. Une ligne (est) honnête vaut
mieux qu'une ligne empruntée.

### L'erreur que presque tout le monde fait ici

**Oublier la remise dans le coefficient et la compter une fois dans les coûts.**
Elle apparaît alors une seule fois dans la cascade alors qu'elle frappe deux
choses : le prix encaissé (donc le coefficient) et la marge brute. Le canonique
tranche la convention — la remise est un **coût variable**, ligne visible — mais
alors le coefficient doit se lire sur le PVC **affiché**, et l'écart avec le prix
encaissé doit être ta ligne « remises ». Un des deux, jamais les deux, jamais
aucun.

---

## Exercice 4 — Le capital nécessaire à ta marque

### La grille de lecture

Le tableau du § 5.1 donne 370 874 € pour NØRA, dont 251 699 € strictement
canoniques. Ce ne sont pas tes nombres. Ce qui est transposable, c'est la
**structure** : trois blocs, dont un que presque personne ne compte.

| Bloc | Part chez NØRA | Ce qui le fait varier chez toi |
| --- | ---: | --- |
| Pertes cumulées jusqu'au premier mois positif | 39,7 % | La durée de ta vallée, donc ton coefficient et ton réachat |
| BFR au même moment | 28,2 % | Ton délai fournisseur, ton MOQ, ton délai d'encaissement |
| Lancement hors modèle | 12,1 % | Ta réglementation, ton outillage, ton nombre de références |
| Marge de sécurité | 20,0 % | Le nombre de fois où tu acceptes de te tromper |

Puis lis l'écart entre ton **capital à réunir** et ton **capital de ruine** :

| Ratio capital de ruine ÷ capital à réunir | Diagnostic | Action |
| --- | --- | --- |
| **≥ 1,3** | Tu peux absorber un accident complet | Lance. Écris à l'avance le seuil de réachat à 90 jours qui déclenche l'arrêt |
| **1,0 à 1,3** | Tu franchis, sans réserve | Lance, mais aucun deuxième produit et aucun deuxième pays avant P3 |
| **0,6 à 1,0** | Tu meurs entre 60 % et 100 % du chemin | Réduis l'ambition **ou** trouve le complément **avant** la première commande fournisseur, jamais après |
| **< 0,6** | Tu meurs avant d'avoir la réponse | Change de moteur d'acquisition. Le DTC financé par la publicité payante n'est pas ton métier |

**La règle qui rend cet exercice utile :** ton capital de ruine s'écrit **avant**
de calculer le capital nécessaire, et il ne se révise jamais à la hausse après
avoir vu le total. Une révision à la hausse en cours de calcul n'est pas une
décision de financement, c'est un biais d'engagement — et il coûte, en moyenne,
la maison.

Trois erreurs de chiffrage récurrentes. **Le lancement hors modèle est
sous-estimé d'un facteur 2 à 3** — on compte le produit et le site, on oublie la
photo, le dossier réglementaire (30 000 € pour trois références cosmétiques,
E02 § 1.5), le juridique, la comptabilité et le premier salaire. **Le BFR est
compté hors acompte fournisseur** : le canonique § 4.1 chiffre l'écart de 0 % à
P1 à 13,9 % à P5, et le chiffre à financer est le plus grand des deux. **La marge
de sécurité est confondue avec l'optimisme** : 25 % couvre un retard de trois
mois, pas un échec de produit.

### Le barème — sur 20

| Critère | Points |
| --- | ---: |
| Les quatre postes chiffrés, aucun laissé vide | 4 |
| Pertes cumulées dérivées d'une trajectoire mensuelle écrite, pas d'un forfait | 4 |
| BFR décomposé en ses quatre composantes | 4 |
| Capital de ruine écrit en **un seul nombre**, sans fourchette ni condition | 3 |
| Écart calculé et arbitrage coché | 3 |
| Le « comment » écrit en trois lignes opérationnelles | 2 |

**Faute éliminatoire.** Avoir écrit un capital de ruine sous la forme « ça dépend »
ou « entre X et Y ». Une fourchette est une façon de ne pas décider, et le jour où
la question se pose réellement tu prendras la borne haute.

### L'erreur que presque tout le monde fait ici

**Confondre le budget et le capital de ruine.** Le budget est ce que tu as prévu
de dépenser ; le capital de ruine est ce que tu peux perdre sans que ta vie
change. Le premier est une intention, le second une contrainte. Les marques
sous-capitalisées du § 5.3 n'ont pas manqué de budget : elles ont découvert au
mois 5 que leur capital de ruine était très inférieur à ce qu'elles croyaient,
parce qu'elles ne l'avaient jamais écrit.

---

## Exercice 5 — Ma catégorie autorise-t-elle P5 ?

### La réponse

```
Option A — coefficient ×7,2, 1,2 commande par client à 12 mois
   COGS % CA HT   = 1,20 ÷ 7,2                        = 16,67 %
   Marge brute    = 100 − 16,67 − 23,65               = 59,68 %
   Contribution/commande = 50,00 € HT × 59,68 %       = 29,84 €
   LTV 12 mois    = 1,2 × 29,84                       = 35,81 €
   LTV / nCAC     = 35,81 ÷ 35,00                     =  1,02

Option B — coefficient ×4,2, 3,1 commandes par client à 12 mois
   COGS % CA HT   = 1,20 ÷ 4,2                        = 28,57 %
   Marge brute    = 100 − 28,57 − 23,65               = 47,78 %
   Contribution/commande = 50,00 € HT × 47,78 %       = 23,89 €
   LTV 12 mois    = 3,1 × 23,89                       = 74,06 €
   LTV / nCAC     = 74,06 ÷ 35,00                     =  2,12
```

| # | Grandeur | Option A | Option B |
| ---: | --- | ---: | ---: |
| 1 | COGS en % du CA HT | 16,67 % | 28,57 % |
| 2 | Marge brute | 59,68 % | 47,78 % |
| 3 | Contribution par commande | 29,84 € | 23,89 € |
| 4 | LTV 12 mois en contribution | 35,81 € | 74,06 € |
| 5 | LTV / nCAC | **1,02** | **2,12** |
| 6 | MER seuil CM3 = 0 | 2,01 | 2,51 |
| 7 | MER seuil EBITDA = 0 | 2,45 | 3,24 |
| 8 | MER atteint sur 12 mois | 2,06 | **5,31** |
| 9 | EBITDA par client sur 12 mois | **−5,61 €** | **+22,47 €** |

Détail de la ligne 8, celle que presque personne ne calcule :

```
MER atteint = CA TTC produit par un client sur 12 mois ÷ ce qu'il a coûté
Option A : 1,2 × 60,00 € ÷ 35,00 € = 72,00 ÷ 35,00   = 2,06
Option B : 3,1 × 60,00 € ÷ 35,00 € = 186,00 ÷ 35,00  = 5,31
```

Et la ligne 9, qui referme le raisonnement :

```
Frais fixes par client = 10,70 % × CA HT du client sur 12 mois
Option A : 0,1070 × 1,2 × 50,00 =  6,42 €   →  35,81 − 35,00 − 6,42 = −5,61 €
Option B : 0,1070 × 3,1 × 50,00 = 16,59 €   →  74,06 − 35,00 − 16,59 = +22,47 €
```

**(a) La bonne réponse est l'option B.**

**(b) La règle canonique invoquée**, citée textuellement (§ 3) : *« LTV/CAC à
12 mois ≥ 2,0 et payback ≤ 4 mois : on peut accélérer. LTV/CAC 12 mois < 1,5 :
on ne scale pas, on répare. »* B est à 2,12, au-dessus du seuil d'accélération.
A est à 1,02, sous le seuil de réparation.

**La démonstration doit tenir les deux routes, parce que l'exercice est construit
pour qu'elles semblent se contredire.** Sur le seul critère du coefficient, A
gagne : ×7,2 franchit le test A du § 7 (`≥ ×5`), B à ×4,2 échoue. Sur le seul
critère de la fréquence, B gagne. Le tableau tranche parce que les lignes 8 et 9
mesurent ce qui arrive **réellement** : le MER atteint par B (5,31) écrase son
propre seuil d'EBITDA (3,24) de 64 %, quand celui de A (2,06) reste **sous** son
seuil d'EBITDA (2,45) de 16 %. A vend un produit à forte marge à des clients qui
ne reviennent pas ; B vend un produit à marge moyenne à des clients qui
reviennent trois fois. Le second gagne 22,47 € par client là où le premier en
perd 5,61 €, soit un écart de 28,08 € par client acquis.

**(c) À quel nCAC A deviendrait-elle la bonne option.**

```
Pour atteindre la règle canonique de 2,0 : nCAC = 35,81 ÷ 2,0     = 17,91 €
Pour seulement sortir de la zone de réparation (1,5) : 35,81 ÷ 1,5 = 23,87 €
Pour que l'EBITDA par client redevienne nul : 35,81 − 6,42        = 29,39 €
Pour dépasser le ratio de B (2,12) : 35,81 ÷ 2,116                = 16,92 €
```

**(d) Le canal, et la condition.** Le plan média canonique § 5 ne contient qu'un
seul canal sous 20 € : **Google Search + Shopping, à 19,00 € de nCAC**. Et il ne
suffit pas. À 19,00 €, A plafonne à `35,81 ÷ 19,00 = 1,88` — au-dessus de 1,5,
sous 2,0 : zone de survie sous surveillance, jamais zone d'accélération. La
condition exacte est donc double, et il faut écrire les deux : *A ne devient
jouable qu'en récolte de demande pure, et même là elle n'atteint pas le seuil
canonique.* Or Search **récolte** une demande créée ailleurs et sature — 8 651
clients par mois chez NØRA (canonique § 5). Une catégorie à faible fréquence
n'est pas une catégorie à financer par la création de demande : c'est une
catégorie où quelqu'un d'autre paie la création et où tu prends la récolte, ce
qui interdit la prime de marque et ramène au § 1.3 du module.

**(e) Ce qu'il faut conclure sur le test « coefficient ≥ ×5 ».** Il est
**nécessaire mais pas suffisant, et il n'est pas non plus toujours nécessaire.**
Le vrai test est le couple `(coefficient, fréquence)`, parce que la fréquence
entre dans le MER atteint et le coefficient dans le MER seuil. Le seuil de ×5 est
une abréviation calibrée sur une fréquence de l'ordre de 2,2 commandes à 12 mois
— celle de NØRA. À 3,1 commandes, le coefficient nécessaire descend ; à 1,2, ×7,2
ne suffit plus. C'est exactement le sens de la phrase du § 3.2 du module : les
deux verrous se posent le jour du choix de la catégorie, et il y en a **deux**.

### Le barème — sur 20

| Critère | Points |
| --- | ---: |
| Les deux COGS par 1,20 ÷ k | 2 |
| Les deux marges brutes et les deux contributions par commande | 3 |
| Les deux LTV 12 mois **en contribution**, pas en CA | 3 |
| Les deux ratios, et B tranchée | 3 |
| Règle canonique citée, pas paraphrasée | 2 |
| Ligne 8 ou ligne 9 calculée — la démonstration qui lève la contradiction | 3 |
| nCAC de bascule = 17,91 € | 2 |
| Canal nommé **et** son insuffisance chiffrée (1,88) | 2 |

**Fautes éliminatoires.** Avoir tranché A au seul motif que ×7,2 > ×5 : c'est
appliquer un test sans savoir ce qu'il mesure. Avoir calculé la LTV en chiffre
d'affaires (A : 1,2 × 60 = 72 € ; B : 3,1 × 60 = 186 €), ce qui donne des ratios
de 2,06 et 5,31 et fait passer les deux options pour bonnes.

### L'erreur que presque tout le monde fait ici

**Choisir A parce que sa marge brute est meilleure.** 59,68 % contre 47,78 %,
l'écart est de 11,9 points et il est réel — il ne décide de rien. La marge brute
mesure ce que rapporte **une** commande ; la décision porte sur ce que rapporte
**un client**. Entre les deux il y a la fréquence, et elle vaut ici un facteur
2,58 sur la LTV. Le réflexe « meilleure marge = meilleur produit » est le plus
coûteux du métier parce qu'il est vrai à commandes égales, et qu'elles ne le sont
jamais.

---

*Fin du corrigé du module E00. Formulaire : [`E00-rendu.md`](E00-rendu.md).
Module suivant : [E01 — L'arithmétique de la marque](../modules/E01-arithmetique-de-la-marque.md).*
