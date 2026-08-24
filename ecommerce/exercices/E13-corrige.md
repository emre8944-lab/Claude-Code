# Corrigé — Module E13 : Le risque de ruine

> Ne lis ce fichier qu'après avoir rendu [`E13-rendu.md`](E13-rendu.md). Un corrigé lu
> avant l'effort donne le sentiment d'avoir compris, et rien d'autre.
>
> Rappel de méthode : toutes les probabilités de ce module sont des **estimations
> déclarées**. Ce qui se vérifie, ce sont les impacts et l'arithmétique qui les
> combine — et c'est déjà ce qui manque à presque tous les registres.

---

## Exercice 1 — La survie de NØRA

### La réponse

**(1) Le tableau.**

| | **p = 5 %** | **p = 10 %** | **p = 20 %** |
| --- | ---: | ---: | ---: |
| Survie à 3 ans | **85,7 %** | **72,9 %** | **51,2 %** |
| Survie à 5 ans | **77,4 %** | **59,0 %** | 32,8 % |
| Survie à 10 ans | **59,9 %** | 34,9 % | **10,7 %** |
| Survie à 20 ans | **35,8 %** | **12,2 %** | **1,2 %** |
| Une chance sur deux d'être mort au bout de | **13,5 ans** | **6,6 ans** | **3,1 ans** |
| Facteur annuel espéré | **1,71** | **1,62** | **1,44** |
| **Valeur espérée à 5 ans** | **14,62 ×** | **11,16 ×** | **6,19 ×** |
| Valeur espérée à 10 ans | **213,78 ×** | **124,49 ×** | **38,34 ×** |

```
Demi-vie : t tel que (1 − p)^t = 0,5,  soit  t = ln(0,5) ÷ ln(1 − p)
   p =  5 % : −0,693147 ÷ −0,051293 = 13,51 ans
   p = 10 % : −0,693147 ÷ −0,105361 =  6,58 ans
   p = 20 % : −0,693147 ÷ −0,223144 =  3,11 ans
Valeur à 5 ans : ((1 − p) × 1,80)^5
   1,71^5 = 14,6211      1,62^5 = 11,1577      1,44^5 = 6,1917
```

La colonne p = 10 % reproduit le § 0 à la décimale : 59,0 %, 34,9 %, 6,6 ans, 11,16 ×,
124,49 ×.

**(2) Ce que change la ligne « une chance sur deux ».** La survie à 5 ans est une
statistique ; la demi-vie est un calendrier. À 10 % par an, l'entreprise a une chance
sur deux d'être morte avant les 39 ans de son fondateur — et à 20 %, avant ses 36 ans.
**Une probabilité annuelle qui semble tolérable devient une date quand on l'intègre.**
C'est exactement pour ça qu'on l'intègre.

**(3) Le modèle lent.**

```
E[G] | survie = (1/5) × 3,0 + (4/5) × 1,15 = 0,60 + 0,92        = 1,52
Plafond absolu (p = 0) : 1,52^5                                 = 8,11 ×
p qui égalerait 11,16 × :  (1 − p) × 1,52 = 11,1577^(1/5) = 1,62
                           1 − p = 1,62 ÷ 1,52 = 1,0658  →  p   = −6,6 %
```

**Il n'existe pas.** Il faudrait une probabilité de ruine **négative**. Le modèle lent
plafonne à 8,11 × à cinq ans, quand le modèle rapide à 10 % de risque annuel — donc
avec 41 % de chances d'être mort — en fait 11,16 ×. **Aucune réduction de risque, même
totale, ne rachète 28 points de croissance annuelle espérée.**

**(4) La question renversée.**

```
((1 − p) × 1,80)^5 = 8,1137  →  (1 − p) × 1,80 = 1,52  →  p = 15,6 %
```

Le modèle rapide reste supérieur au modèle lent **parfait** tant que sa probabilité
annuelle de ruine reste sous **15,6 %**.

**(5) La phrase d'arbitrage.** « La survie ne se substitue pas à la croissance : elle
l'achète jusqu'à un prix, et ce prix vaut ici **15,6 points de probabilité annuelle de
ruine**. Au-delà, je préfère une machine lente et increvable ; en deçà, une machine
rapide et fragile gagne — et le § 0 dit seulement qu'à croissance égale, il faut
prendre la moins fragile. »

C'est la lecture honnête du § 0, et elle est plus étroite que ce que le module laisse
croire à la première lecture. Le § 0 compare deux valeurs de `p` **à croissance
constante** ; il ne dit nulle part qu'on doit sacrifier de la croissance pour du
risque. Ces deux exercices bornent l'échange : **1,8 point de croissance annuelle
espérée vaut environ 10 points de probabilité de ruine.**

### Le barème (sur 20)

**6** le tableau complet, ±0,2 point sur les survies · **3** les trois demi-vies avec
la formule logarithmique posée · **3** les trois valeurs à 5 ans, ±0,05 × · **2** la
phrase du (2), qui doit opposer statistique et calendrier · **3** le `E[G]` de 1,52 et
le plafond de 8,11 × · **2** la conclusion d'**impossibilité** en (3), énoncée comme
telle · **1** les 15,6 % du (4).

**Fautes éliminatoires.** Avoir écrit un `p` positif en (3) : le signe **est** la
réponse. Avoir calculé `E[G]` en moyennant 3,0 et 1,15 sans les pondérer par 1/5 et
4/5. Avoir confondu survie à 5 ans et valeur espérée à 5 ans — l'une est une
probabilité, l'autre un multiple, et les additionner n'a aucun sens.

### L'erreur que presque tout le monde fait ici

**Lire le § 0 comme « la sécurité bat la croissance ».** Le § 0 démontre que diviser
`p` par cinq augmente l'espérance à cinq ans de 53 % — **à croissance inchangée**. Ce
« à croissance inchangée » porte toute la démonstration, et l'exercice le prouve par
l'absurde : dès qu'une mesure de sécurité coûte de la croissance, le calcul se
renverse, et il se renverse vite. Une entreprise qui refuse tout risque finit par
avoir une espérance de croissance de 1,15 et une survie parfaite, ce qui vaut moins
qu'une entreprise à 1,80 qui meurt une année sur sept. **La bonne question n'est jamais
« comment réduire le risque » mais « quelles mesures réduisent le risque sans toucher
au facteur de croissance ».** Le registre du § 7.2 ne contient presque que celles-là :
une clé matérielle, un deuxième administrateur, un référentiel d'allégations ne coûtent
pas un point de croissance.

---

## Exercice 2 — Le registre recalculé

### La réponse

**(1) Les trois jeux de probabilités.**

| | Espérance totale | Espérance résiduelle | Gain | Coût | **Solde** |
| --- | ---: | ---: | ---: | ---: | ---: |
| Référence | 559 697 € | 147 638 € | 412 059 € | 429 165 € | **−17 106 €** |
| **a** — ÷ 2 | **279 849 €** | **73 819 €** | **206 030 €** | 429 165 € | **−223 135 €** |
| **b** — × 2 | **1 119 394 €** | **295 276 €** | **824 118 €** | 429 165 € | **+394 953 €** |
| **c** — R1 à 40 % | **621 864 €** | 147 638 € | **474 226 €** | 429 165 € | **+45 061 €** |

```
a et b : les deux colonnes d'espérance sont linéaires en p, donc le gain aussi.
c : R1 passe de 0,25 × 414 464 = 103 619 € à 0,40 × 414 464 = 165 786 €
    Total = 559 697 − 103 619 + 165 786 = 621 864 €
    La résiduelle ne bouge pas : la mesure est toujours aussi efficace.
```

**(2) Le multiplicateur de rentabilité en espérance seule.**

```
k × 412 059 ≥ 429 165  →  k ≥ 1,0415
```

**Il suffit que tes probabilités soient sous-estimées de 4,2 % pour que le programme
devienne rentable en espérance.** C'est le résultat le plus important de l'exercice.
Le solde de −17 106 € du § 7.3 n'est pas une conclusion, c'est un **bruit** : il vaut
0,39 % de l'EBITDA annuel et repose sur huit probabilités estimées à la main. Toute
personne qui décide de ne pas faire le programme sur la foi de ces 17 106 € décide sur
une précision qu'elle n'a pas.

**(3) Le multiplicateur par ligne.**

| Ligne | R1+R2 | R8 | R6 | R4 | R5 | R7 | R3 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Gain en espérance | 99 888 € | 58 500 € | 83 868 € | 55 413 € | 39 390 € | 36 000 € | 39 000 € |
| Coût annuel | 36 000 € | 9 000 € | 75 398 € | 60 000 € | 71 500 € | 69 267 € | 108 000 € |
| **`k*`** | **0,360** | **0,154** | **0,899** | **1,083** | **1,815** | **1,924** | **2,769** |
| Positive à ÷ 2 | **oui** | **oui** | non | non | non | non | non |
| Positive à × 2 | **oui** | **oui** | **oui** | **oui** | **oui** | **oui** | non |

Deux lignes seulement — la conformité publicitaire et les accès — restent rentables
même en divisant toutes les probabilités par deux. Ce sont aussi les deux moins chères
du registre : 36 000 € et 9 000 €. **À × 2, tout devient rentable sauf le conseil
juridique**, dont le `k*` de 2,769 dit qu'il ne se justifie jamais sur le seul
périmètre de la sanction — le § 3.3 le rend positif en lui affectant la part de R4 et
R5 qu'il couvre aussi.

**(4) Le rapport de l'impact à la réserve** (1 243 595 €) :

| Ligne | R5 | R4 | R6 | R7 | R2 | R8 | R3 | R1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Impact ÷ réserve | **2,03** | **1,27** | **1,20** | **0,96** | **0,87** | **0,72** | **0,52** | **0,33** |
| > 1,00 | **oui** | **oui** | **oui** | non | non | non | non | non |

**(5) Le croisement, et ce qu'il implique.** Trois lignes dépassent la réserve : R5,
R4, R6. Deux d'entre elles — **R5 et R4** — sont couvertes par une mesure d'espérance
négative à la référence (`k*` de 1,815 et 1,083). R6 est à 0,899, donc positive de
justesse. En ajoutant R7, à 0,96 de la réserve et `k*` de 1,924, on retrouve le compte
du § 7.4 : **les mesures que le tri par rentabilité supprime sont précisément celles
qui couvrent les impacts que ta réserve n'absorbe pas.**

Ce que ça implique : **un registre se trie deux fois.** Le tri par gain net dit dans
quel ordre dépenser un budget donné. Le tri par impact ÷ réserve dit lesquelles ne sont
pas négociables, quel que soit le budget. La première question est « qu'est-ce qui
rapporte », la seconde « qu'est-ce qui me tue » — et on répond à la seconde d'abord.

**(6) La lecture en survie.**

```
Valorisation de P5 = 6 × 4 377 023 €                = 26 262 138 €
Points de survie à 5 ans : 90,4 % − 59,0 %          =      31,4 pts
Valeur de survie créée = 0,314 × 26 262 138 €       =  8 246 311 €
Coût du programme sur 5 ans = 5 × 429 165 €         =  2 145 825 €
Rapport                                             =   3,84 pour 1
```

*(Le § 7.4 affiche 8 231 342 € : l'écart de 14 969 € vient d'un arrondi sur les 31,4
points. Le rapport de 3,84 pour 1 est identique.)*

> **Une incohérence à connaître dans le module.** L'impact de R4 vaut **1 583 244 €**
> au § 7.2 et **1 433 244 €** au § 3.2, pour le même événement — 150 000 € d'écart. Le
> § 3.2 est celui qui se recalcule : `(43,23 − 40,03) × 37 324 × 12 = 1 433 242 €`. Le
> registre du § 7.2, lui, est cohérent avec lui-même : ses 79 162 € d'espérance et son
> total de 559 697 € supposent 1 583 244 €. **Cet exercice s'aligne sur le registre**,
> pour que les totaux tombent. Avec la valeur du § 3.2, l'espérance de R4 tomberait à
> 71 662 €, le total à 552 197 €, et le solde à −24 606 € — sans rien changer aux
> conclusions. Signale l'écart plutôt que de le corriger en silence : un modèle dont on
> répare les chiffres sans le dire devient invérifiable.

**Le même programme vaut −17 106 € en espérance et +6 100 486 € en survie.** Ce n'est
pas une contradiction : ce sont deux questions différentes. L'espérance demande « qu'
est-ce que ça me rapporte en moyenne » ; la survie demande « qu'est-ce que ça vaut
qu'il y ait encore une entreprise dans cinq ans ». La moyenne compte les mondes où
l'entreprise est morte comme des mondes à zéro. Son propriétaire, lui, n'y est pas.

### Le barème (sur 20)

**5** les trois lignes a, b, c, à 1 000 € près, avec la linéarité de a et b énoncée ·
**3** le `k` de 1,042 **et** le commentaire qui en tire que le −17 106 € est du bruit ·
**4** les sept `k*` à ±0,01 · **2** les deux colonnes « positive à ÷2 / ×2 » · **3** le
classement par impact ÷ réserve, et les trois lignes au-dessus de 1,00 · **2** le
croisement et la règle des deux tris · **1** les 3,84 pour 1.

**Fautes éliminatoires.** Avoir laissé la probabilité résiduelle fixe en a et b — la
convention est écrite dans l'énoncé, et l'ignorer fausse tous les soldes. Avoir fait
bouger l'espérance résiduelle en c. Avoir conclu de la référence « le programme n'est
pas rentable, on ne le fait pas » sans avoir calculé le `k` de 1,042. Un rapport
impact ÷ réserve calculé sur l'impact résiduel.

### L'erreur que presque tout le monde fait ici

**Prendre le solde de −17 106 € pour un résultat.** Il est présenté comme un total, il
est calculé juste, et il ne signifie rien : c'est la différence de deux sommes de huit
produits dont chaque facteur est une estimation à la louche. Un écart de 4,2 % sur les
probabilités le renverse ; un écart de 10 % le rend franchement positif. **Quand la
conclusion d'un tableau bascule sur une variation plus petite que la précision de ses
entrées, la conclusion n'est pas dans le tableau.** Elle est ailleurs — ici, dans la
colonne impact ÷ réserve, qui ne dépend d'**aucune** probabilité et qui est donc la
seule colonne robuste du registre.

---

## Exercice 3 — Ton registre des risques

### La réponse : la grille de lecture

**Le nombre de lignes.** Dix est un plancher, pas une cible.

| Lignes écrites | Diagnostic |
| ---: | --- |
| **< 6** | Tu n'as pas fait le tour. Il manque au moins une des six familles : plateforme, conformité, produit, paiement, concentration invisible, personne |
| **6 à 12** | Régime normal. Vérifie que chaque famille est représentée au moins une fois |
| **> 20** | Tu as écrit une liste de soucis, pas un registre. Fusionne : un registre se revoit chaque trimestre par une personne nommée, et vingt lignes ne se revoient pas |

**La qualité de chaque ligne**, dans l'ordre où on la perd :

| Défaut | Ce que ça produit |
| --- | --- |
| Un risque formulé en catégorie — « dépendance aux plateformes » | Impossible à chiffrer, donc jamais chiffré, donc jamais traité. La formulation correcte est un **événement daté et mesurable** : « coupure Meta de 11 jours » |
| Un impact sans ligne de calcul | Un nombre rond, toujours sous-estimé. Un impact qui finit par trois zéros a été deviné |
| Une probabilité laissée vide | La ligne sort du total et disparaît du registre. **Écris un nombre faux plutôt que rien** |
| Un coût de mesure exprimé seulement en euros de facture | Tu oublies le coût en marge et en conversion — les 559 177 € par an du 3DS systématique (§ 5.2) ne sont sur aucune facture |

**L'espérance totale, rapportée à ton EBITDA annuel :**

| Espérance ÷ EBITDA annuel | Diagnostic |
| ---: | --- |
| **< 5 %** | Soit tu es très protégé, soit — beaucoup plus probable — tu as sous-estimé tes impacts ou oublié une famille |
| **5 à 20 %** | Zone normale. NØRA à P5 est à 12,8 % sans mesures, 3,4 % avec |
| **> 30 %** | Ton exploitation finance une structure de risque qu'elle ne peut pas porter. Le chantier du trimestre est là, pas dans l'acquisition |

**Le nombre de lignes dont l'impact dépasse ta réserve** — l'indicateur n° 6 du tableau
de bord, seul indicateur du cursus dont le seuil est **zéro** :

| Lignes au-dessus de la réserve | Ce que tu fais |
| ---: | --- |
| **0** | Ta réserve est calibrée. Vérifie qu'elle l'est pour la bonne raison et non parce que tes impacts sont optimistes |
| **1 à 3** | Normal, et ce sont **exactement** tes trois chantiers. Chacune se traite par une mesure ou par de la réserve — jamais par un report |
| **> 3** | Ce n'est plus un registre de risques, c'est un diagnostic de sous-capitalisation. Relis [E10](../modules/E10-cash-et-operations.md) § 3 |

**Le test des deux tris.** Si les deux classements donnent le même ordre, tu as
sous-estimé au moins un impact — parce que le gain net est proportionnel à la
probabilité et l'impact ÷ réserve n'en dépend pas du tout. Deux colonnes indépendantes
qui donnent le même ordre sur dix lignes, c'est que l'une des deux a été remplie en
regardant l'autre. Le suspect habituel : le rappel produit, ou la perte des accès —
les deux risques dont l'impact est grand et la probabilité que personne ne sait poser.

### Le barème (sur 20)

**5** dix lignes, chacune formulée comme un événement daté et mesurable · **5** chaque
impact accompagné de **sa ligne de calcul** dans le tableau — un impact sans calcul
vaut 0 pour sa ligne · **3** chaque probabilité écrite, marquée (est) · **3** chaque
coût annuel, **y compris** en marge et en conversion · **2** les deux tris faits et les
changements de rang notés · **2** la réponse honnête au test des deux tris.

**Fautes éliminatoires.** Un risque formulé en catégorie. Une case de probabilité vide.
Un impact rond sans calcul. Avoir omis la famille « personne » (§ 6.2) : c'est la moins
chère à traiter et celle que tout le monde oublie. Un montant sans mention TTC ou HT.

### L'erreur que presque tout le monde fait ici

**Écrire le registre sans écrire la réserve à côté.** Sans réserve, la colonne impact
n'est qu'une échelle de gravité relative, et le tri se fait forcément par gain net —
donc on supprime exactement les trois mesures qui maintiennent en vie (§ 7.4). La
réserve n'est pas une donnée du décor : c'est **l'unité de mesure du registre**. Un
impact de 400 000 € est bénin pour une entreprise qui en a 2 millions en banque et
mortel pour celle qui en a 300 000, et c'est le même nombre. Écris ta réserve en haut
de la page, avant la première ligne.

---

## Exercice 4 — Ta trésorerie de survie

### La réponse : la grille de lecture

| Semaines de survie | Régime | Ce que tu fais |
| ---: | --- | --- |
| **> 26** | Confort | Tu peux investir et prendre des risques d'allocation |
| **13 à 26** | Normal | Un cycle fournisseur complet est couvert |
| **8 à 13** | **Vigilance** | Gel de tout engagement nouveau au-delà de 8 semaines |
| **4 à 8** | **Alerte** | Le plan de réduction s'exécute, il ne s'écrit plus |
| **< 4** | Ruine à vue | Tu appelles tes fournisseurs avant qu'ils ne t'appellent |

**Le seuil n'est pas 13 semaines : c'est ton délai fournisseur réel plus quatre.** Le
13 du module vient d'un délai de 90 jours en cosmétique à façon. Si tu achètes en Asie
avec 120 jours de cycle, ton seuil est 21 semaines ; si tu produis en 3 semaines, il
est 7. **Recalcule-le, ne le recopie pas.**

**Les cinq soustractions, et ce qu'elles coûtent quand on les oublie.** C'est ici que
tout le monde triche, et rarement de mauvaise foi.

| Soustraction oubliée | Ce qu'elle vaut, typiquement | Pourquoi on l'oublie |
| --- | --- | --- |
| TVA collectée non reversée | 1 à 2 mois de TVA sur ton CA | Elle est sur ton compte, elle n'est pas à toi. C'est la plus grosse et la plus fréquente |
| Commandes encaissées non expédiées | 2 à 5 jours de CA TTC | Un client a payé une marchandise qu'il n'a pas : c'est une dette, pas un encaissement |
| Charges sociales et fiscales dues | 1 mois de masse salariale chargée | Elles sont prélevées sans que tu aies à agir, donc on ne les voit pas venir |
| Dettes fournisseurs à 30 jours | Un mois de COGS | On les compte comme « du temps », pas comme du passif |
| Crédit remboursable à vue | Le solde de ta ligne | Une ligne de trésorerie tirée n'est pas de la trésorerie |

**Ordre de grandeur du redressement :** sur un compte bancaire qui affiche 100, ces
cinq soustractions retirent couramment **50 à 70**. Si les tiennes en retirent moins de
20 %, refais-les — tu as sauté la TVA ou les commandes non expédiées.

**Le cas de NØRA, pour te situer.** Réserve du palier 1 243 595 €, engagements
fournisseurs en cours 916 291 €, frais fixes hebdomadaires 83 077 € :
`(1 243 595 − 916 291) ÷ 83 077 = 3,9 semaines`. **Une entreprise à 52 M€ de CA TTC
annuel, avec une réserve calibrée pour un choc d'exploitation, tient 3,9 semaines face
à un choc de ruine.** Il lui manque `916 291 + 13 × 83 077 − 1 243 595 = 752 697 €`,
soit 2,1 mois d'EBITDA. Si ton résultat est meilleur que 3,9 semaines, vérifie
d'abord tes soustractions.

**Si ton écart est négatif**, trois issues, dans cet ordre de préférence :

| Issue | Délai | Coût |
| --- | --- | --- |
| Allonger le délai fournisseur (le seuil baisse au lieu que le cash monte) | 1 à 2 cycles | Souvent gratuit, parfois 1 à 2 points de COGS |
| Réduire les engagements non annulables — fractionner les commandes (§ 7.6) | Immédiat | *Hypothèse du module :* 3 % de COGS pour trois lots au lieu d'un |
| Réunir le cash manquant | 2 à 6 mois | Le plus cher, et le seul qu'on envisage en premier |

### Le barème (sur 20)

**6** les cinq soustractions faites, chacune avec un montant — une seule oubliée coûte
ses points · **4** les engagements non annulables listés **avec leur date
d'exigibilité**, pas seulement leur montant · **3** le nombre de semaines, calculé et
non estimé · **3** le délai fournisseur **mesuré sur les trois dernières commandes**,
pas le délai contractuel · **2** l'écart, et le seuil recalculé sur ton propre cycle ·
**2** si l'écart est négatif : le montant, la date, et le moyen.

**Fautes éliminatoires.** Avoir pris le solde bancaire pour la trésorerie nette
disponible. Avoir oublié la TVA collectée. Avoir utilisé le délai fournisseur du
contrat au lieu du délai réellement constaté. Avoir compté une ligne de crédit non
tirée comme de la trésorerie disponible — elle se retire le jour où tu en as besoin.

### L'erreur que presque tout le monde fait ici

**Compter en mois de chiffre d'affaires.** « J'ai trois mois de CA en banque » est la
phrase la plus dangereuse de l'exercice : le CA n'est pas ce que tu dois payer. Ce que
tu dois payer, ce sont des frais fixes hebdomadaires et des engagements déjà signés. Un
même solde vaut vingt semaines pour une marque à frais fixes légers et cinq pour une
marque qui a recruté six personnes le trimestre dernier. **La trésorerie ne se mesure
jamais en fraction de ce qui rentre, toujours en durée de ce qui sort** — et la durée
se compare au délai fournisseur, parce que c'est lui qui fixe ton temps de réaction.

---

## Exercice 5 — Tes six dépendances

### La réponse : la grille de lecture

**Les unités, d'abord.** Chaque ligne se mesure dans une unité et une seule, et le
choix de l'unité est le vrai contenu du § 2.1.

| Dépendance | L'unité imposée | L'unité fausse que tout le monde emploie |
| --- | --- | --- |
| Premier canal | part des **nouveaux clients réels** | part du budget — elle flatte le canal cher et minore le canal efficace |
| Premier produit | part du **CA HT** | nombre de références au catalogue |
| Premier fournisseur | part du **COGS annuel** | nombre de produits — trois produits chez le même façonnier font une dépendance à 100 % |
| Premier marché | part de la **marge brute** | part du CA — elle masque un marché à forte marge |
| Premier logisticien | part des **colis expédiés** | nombre de contrats signés |
| Premier PSP | part des **encaissements** | nombre de moyens de paiement affichés |

**Les seuils, et ce qu'ils veulent dire.** Ils ne sont pas des chiffres ronds : ils
dérivent tous de la même règle — *aucune dépendance ne doit pouvoir consommer plus de
la moitié de ta réserve avant que tu aies eu le temps de la remplacer* (§ 7.6).

| Niveau atteint | Ce que tu fais |
| --- | --- |
| **Sous le seuil de vigilance** | Rien. Écris la valeur, revois-la dans six mois |
| **Vigilance** | La ligne entre au registre avec une probabilité et un impact. Aucune action encore |
| **Alerte** | Une mesure est budgétée ce trimestre, avec un responsable et une date |
| **Critique** | La mesure s'exécute avant tout chantier commercial. À ce niveau, la dépendance n'est plus un risque, c'est une décision déjà prise contre toi |

**Le classement qui compte : délai de substitution × perte hebdomadaire.** Le
pourcentage dit combien tu perds ; le produit dit **combien de temps tu le perds**, et
c'est lui qui se compare à ta réserve.

| Produit ÷ réserve | Diagnostic |
| ---: | --- |
| **< 0,25** | Absorbable. La dépendance est un inconfort, pas un risque |
| **0,25 à 0,60** | Sérieux : un incident consomme plus du quart de ta réserve et te laisse sans marge pour le suivant |
| **0,60 à 1,00** | La règle du § 7.6 est franchie. Mesure obligatoire, quel que soit le pourcentage affiché |
| **> 1,00** | Ligne de ruine. Elle entre dans l'indicateur n° 6, dont le seuil est zéro |

**Les délais de substitution typiques**, à comparer aux tiens — la plupart des gens les
sous-estiment d'un facteur deux :

| Dépendance | Délai réaliste | Ce qui le fixe |
| --- | ---: | --- |
| Canal d'acquisition | 8 à 20 semaines | Le temps de trouver des concepts qui marchent sur un autre inventaire, pas le temps d'ouvrir un compte |
| Fournisseur | **12 à 26 semaines** | Qualification, stabilité, challenge test, dossier d'information produit, premier lot |
| Logisticien | 6 à 12 semaines | Migration de stock, intégration, reprise des retours |
| PSP | 3 à 8 semaines | Souscription, tests, mais surtout la période de réserve du nouveau |
| Produit | 20 à 40 semaines | C'est un développement, pas un remplacement |
| Marché | 20 semaines | La durée d'ouverture d'un marché ([E11](../modules/E11-passage-a-echelle.md)) |

**Le résultat attendu de l'exercice**, et qui surprend presque tout le monde : **la
dépendance la plus grave n'est presque jamais celle dont le pourcentage est le plus
élevé.** Un PSP à 95 % des encaissements se remplace en 5 semaines ; un fournisseur à
60 % du COGS se remplace en 20. Si ta perte hebdomadaire est comparable, le second
pèse quatre fois plus lourd avec un pourcentage inférieur de 35 points.

### Le barème (sur 20)

**6** les six lignes mesurées **dans l'unité imposée**, sur douze mois — une ligne dans
la mauvaise unité vaut 0 · **4** les six délais de substitution, justifiés par ce qu'il
faut faire et non posés au jugé · **4** les six produits délai × perte hebdomadaire ·
**3** le classement par ce produit et son rapport à la réserve · **3** la réponse à la
dernière question, avec l'explication du décrochage entre pourcentage et gravité.

**Fautes éliminatoires.** Le canal mesuré en part de budget. Le fournisseur mesuré en
nombre de références. Un délai de substitution égal au délai de signature d'un contrat.
Avoir répondu « oui » à la dernière question sans avoir calculé les six produits.

### L'erreur que presque tout le monde fait ici

**Mesurer le premier canal en part de budget.** C'est l'unité qu'affichent tous les
outils, et elle ment dans les deux sens. À P5, Meta pèse **55 % du budget** mais
**51,6 % des nouveaux clients réels** et seulement **28,4 % du CA du mois** — trois
chiffres pour un seul fait, et le troisième est le plus rassurant et le plus faux. Il
ignore que 44,9 % du CA est du réachat et que tout client qui réachète a d'abord été
acquis quelque part : en régime établi, 51,6 % de la base vient de Meta, donc 51,6 %
du réachat aussi. **La dépendance réelle est 51,6 % de tout ce que l'entreprise fera
dans les douze mois suivants** — et le jour où le canal s'arrête, le CA baisse de 28 %,
personne ne panique, et douze mois plus tard la base s'est vidée de moitié.

---

## Exercice 6 — Décision : diversifier ou tenir

### La réponse

**(1) L'état actuel et le coût de la diversification.**

```
Clients du canal 1 = 12 000 × 62 %                    =  7 440 / mois
Budget canal 1     = 7 440 × 34,00 €                  = 252 960 € / mois
Budget des autres  = 4 560 × 48,00 €                  = 218 880 € / mois
Budget total                                          = 471 840 € / mois

Cible 45 / 55, à budget constant :
CAC moyen pondéré = 0,45 × 34,00 + 0,55 × 48,00       =   41,70 €
Clients totaux    = 471 840 ÷ 41,70                   = 11 315 / mois
Clients perdus    = 12 000 − 11 315                   =    685 / mois
Contribution perdue = 685 × 86,75 €                   =  59 424 € / mois
                                                      = 713 088 € / an
Clients du canal 1 après = 45 % × 11 315              =  5 092 / mois
```

**Diversifier de 17 points coûte 713 088 € par an**, soit 12,6 % du budget publicitaire
annuel — et pas un euro n'apparaît en dépense nouvelle. C'est une perte de rendement,
la forme de coût la plus difficile à faire accepter parce qu'elle n'a pas de facture.

**(2) L'impact d'une coupure de 45 jours.**

```
Contribution détruite = clients du canal × (86,75 − 34,00) × 1,5 mois
   Avant : 7 440 × 52,75 × 1,5                        = 588 690 €
   Après : 5 092 × 52,75 × 1,5                        = 402 905 €
Apprentissage : 7 jours de reprise à +30 % de CPA
   Avant : 252 960 ÷ 30,4 × 7 = 58 247 € de budget
           58 247 ÷ 34,00 = 1 713 clients contre 58 247 ÷ 44,20 = 1 318
           395 clients × 86,75 €                      =  34 296 €
   Après : 173 128 ÷ 30,4 × 7 = 39 863 € → 1 172 contre 902
           270 clients × 86,75 €                      =  23 472 €
```

| | Avant (62 %) | Après (45 %) |
| --- | ---: | ---: |
| Contribution détruite | 588 690 € | 402 905 € |
| Apprentissage | 34 296 € | 23 472 € |
| **Impact total** | **622 986 €** | **426 377 €** |
| **Impact ÷ réserve (480 000 €)** | **×1,30** | **×0,89** |
| Au-dessus de la réserve ? | **oui** | **non** |

**(3) La lecture en espérance, sur 24 mois.**

```
Réduction d'impact          = 622 986 − 426 377      = 196 609 €
Espérance annuelle évitée   = 2,5 % × 196 609        =   4 915 €
Sur 24 mois                                          =   9 830 €
Coût de la diversification  = 713 088 × 2            = 1 426 176 €
Rapport                     = 1 426 176 ÷ 9 830      = 145 pour 1
```

**En espérance, la diversification coûte 145 fois ce qu'elle rapporte.** Ton directeur
de l'acquisition a raison, et pas de justesse : il a raison d'un facteur cent. Toute
personne qui décide à l'espérance décidera de tenir, et personne ne pourra lui opposer
un tableau.

**La décision du cursus est pourtant : diversifier.** Pas parce que le calcul est faux
— il est juste — mais parce qu'il répond à la mauvaise question. La ligne qui décide
est celle du (2) : **l'impact passe de 1,30 fois ta réserve à 0,89 fois.** Au-dessus de
1,00, l'événement ne coûte pas de l'argent, il ferme l'entreprise ; en dessous, il
coûte de l'argent. Ce sont deux natures différentes, et l'espérance les additionne
comme si c'était la même chose. C'est le § 7.4 en un seul exemple : *un registre lu en
espérance dit de ne rien faire, le même registre lu en survie dit de tout faire.*

**(4) Les trois conditions exactes.**

```
a — Probabilité annuelle de coupure
      p × 196 609 ≥ 713 088  →  p ≥ 362,6 %
    Aucune probabilité ne rend cette mesure rentable en espérance : il faudrait
    3,6 coupures de 45 jours par an. La justification n'est pas là, et ne peut
    pas y être.

b — Trésorerie
      Réserve nécessaire pour absorber l'impact = 622 986 €
      À réunir = 622 986 − 480 000                       = 142 986 €
      Coût annuel de la diversification                  = 713 088 €
      Rapport = 713 088 ÷ 142 986                        = ×5,0
    → Reconstituer la réserve coûte cinq fois moins cher que diversifier,
      une seule fois au lieu de chaque année, et produit le même effet sur
      la ligne du registre. C'est la bonne réponse à l'exercice.

c — Part réelle du canal dans le CA à 12 mois (§ 2.2)
      Calcul naïf : 62 % × 60 % de premières commandes   = 37,2 % du CA
      Part réelle en régime établi                       = 62,0 %
      Écart ignoré par le calcul naïf                    = 24,8 points
      Après diversification : 45,0 % réel contre 27,0 % naïf
    Seuils du § 2.1 : vigilance 40 %, alerte 55 %, critique 70 %.
    → 62 % est en ALERTE, 45 % en vigilance. La diversification fait
      descendre d'un cran de gravité.
    → Si tes réachats étaient portés par un actif que le canal ne contrôle
      pas — e-mail, abonnement, marque —, la part réelle tomberait vers les
      37,2 % du calcul naïf, sous le seuil de vigilance à 40 %, et tenir
      redeviendrait défendable.
```

**(5) La phrase.** « Je ne diversifie pas, je reconstitue **142 986 €** de réserve —
cinq fois moins cher que les 713 088 € par an de la diversification, et cela fait
passer l'impact d'une coupure de 45 jours de 1,30 à 0,77 fois ma réserve. Je
diversifierai le jour où la part réelle du canal dépassera 70 %, ou le jour où je ne
pourrai plus reconstituer la réserve. »

*(`622 986 ÷ 622 986 = 1,00` exactement à la réserve visée ; à 480 000 + 142 986 =
622 986 €, le rapport tombe à 1,00, et toute réserve supérieure le fait passer en
dessous. La phrase énonce 0,77 pour une réserve portée à 810 000 €, un choix de
sécurité qu'il faut alors écrire.)*

**Les deux réponses, et le point où elles s'inversent.** L'espérance dit *tenir* tant
que `p < 362,6 %`, c'est-à-dire toujours. La survie dit *agir* dès que l'impact dépasse
la réserve, c'est-à-dire dès maintenant. Elles ne s'inversent jamais sur `p` — elles
s'inversent sur la **réserve** : au-dessus de 622 986 € de trésorerie disponible, les
deux lectures disent la même chose, *tenir*. **Le point de bascule de cet exercice
n'est pas une probabilité, c'est un solde bancaire** — et c'est pour ça que la bonne
réponse est de le changer plutôt que de changer le plan média.

### Le barème (sur 20)

**3** le budget total de 471 840 € et le CAC moyen pondéré de 41,70 € · **3** les 685
clients perdus et les 713 088 € par an · **4** les deux impacts, 622 986 € et
426 377 €, apprentissage inclus · **2** les deux rapports à la réserve et le
franchissement de 1,00 · **2** le rapport de 145 pour 1 en espérance, **et** le refus
motivé de conclure dessus · **4** les trois conditions, chacune chiffrée : 362,6 % ·
142 986 € et le facteur ×5,0 · 62,0 % contre 37,2 % · **2** la phrase de décision, avec
son chiffre.

**Fautes éliminatoires.** Avoir oublié le coût d'apprentissage : il vaut 34 296 €, soit
5,5 % de l'impact, et surtout il est le même quelle que soit la durée de la coupure —
c'est lui qui rend une série de petits incidents plus chère qu'un seul long (§ 1.2).
Avoir conclu « on tient » sur le seul rapport de 145 pour 1, sans regarder la ligne
impact ÷ réserve. Avoir conclu « on diversifie » sans avoir calculé les 713 088 €.
Avoir donné la part du canal dans le CA à 28 % ou 37,2 % sans dire que c'est le chiffre
faux du § 2.2.

### L'erreur que presque tout le monde fait ici

**Croire qu'on a le choix entre deux options.** L'énoncé en propose deux — diversifier
ou tenir — et il en existe une troisième, moins chère que les deux, que personne ne
cherche parce qu'elle n'est pas dans la question : **changer la réserve au lieu de
changer l'exposition.** Les 142 986 € à réunir une fois font exactement le même travail
que les 713 088 € par an de diversification sur la seule ligne qui décide, celle du
rapport impact ÷ réserve. C'est une règle générale du registre, et elle mérite d'être
retenue telle quelle : **toute ligne dont l'impact dépasse la réserve a deux
solutions — réduire l'impact, ou augmenter la réserve — et la seconde est presque
toujours la moins chère, parce qu'elle traite toutes les lignes du registre à la fois.**
Une mesure spécifique ne protège que d'un risque ; du cash protège de tous, y compris
de ceux que tu n'as pas su nommer.

---

*Fin du corrigé E13. Suite : [E14-rendu.md](E14-rendu.md), qui place les plafonds du
§ 7.6 comme contraintes du plan et non comme conseils.*
