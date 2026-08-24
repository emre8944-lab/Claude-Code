# Corrigé — Module E01 : L'arithmétique de la marque

> **N'ouvre ce fichier qu'après avoir rendu [`E01-rendu.md`](E01-rendu.md).**

---

## Exercice 1 — Les deux MER seuils de P3

### La réponse

```
1. m = 100 − 16,00 − 12,00 − 1,65 − 3,00 − 7,00              = 60,35 %
2. MER seuil (CM3 = 0) = 1,20 ÷ 0,6035     = 1,9884          →  1,99   ✓
3. f = 105 000 € ÷ 981 000 €                                 = 10,70 %
4. MER seuil (EBITDA = 0) = 1,20 ÷ (0,6035 − 0,10703)
                          = 1,20 ÷ 0,49647 = 2,4171          →  2,42   ✓
5. Marge de sécurité = 2,70 ÷ 2,4171 − 1                     = +11,70 %
   (canonique § 2.3 : +11,7 %)                                          ✓
6. Marge brute minimale pour que 2,70 tienne l'équilibre d'EBITDA :
      m − f = 1,20 ÷ 2,70 = 0,44444   →   m = 0,44444 + 0,10703
                                         = 55,15 %
   Baisse supportable = 60,35 − 55,15                        = 5,20 points
7. En euros : 5,20 % × 981 000 €                             = 51 033 € / mois
```

**Le contrôle qui prouve tout.** La ligne 7 tombe sur **51 033 €**, exactement
l'EBITDA mensuel de P3 au canonique § 2.2. Ce n'est pas une coïncidence mais une
identité : la marge brute qu'une marque peut perdre avant l'équilibre **est** son
profit. Deux chemins, un nombre — c'est ainsi qu'on vérifie un modèle.

**Ce que ça veut dire.** La réserve de P3 vaut **5,20 points de marge brute** —
et les remises passent de 3,0 % à 8,0 % du CA HT entre P1 et P5 (canonique
§ 2.1), soit 5 points. **Toute la marge de sécurité de P3 tient dans la dérive
promotionnelle normale d'une marque qui grandit.**

**La phrase attendue en ligne 7 :** *les 5,20 points de réserve valent 51 033 €
par mois, c'est-à-dire la totalité de l'EBITDA — la marge de sécurité et le
profit sont le même nombre vu deux fois.*

### Le barème — sur 20

| Critère | Points |
| --- | ---: |
| m = 60,35 % à partir des cinq postes, pas recopié du canonique | 3 |
| Seuil CM3 = 1,99, avec 1,20 au numérateur | 4 |
| f = 10,70 % calculé | 2 |
| Seuil EBITDA = 2,42 | 4 |
| Marge de sécurité +11,70 %, calculée en **ratio** et non en écart de points | 3 |
| Baisse supportable = 5,20 points | 2 |
| Conversion en euros et identification avec l'EBITDA de P3 | 2 |

**Fautes éliminatoires.** Numérateur à 1,00 au lieu de 1,20 : les seuils
deviennent 1,66 et 2,01, et la marge de sécurité passe de +11,7 % à +34,3 %.
Marge de sécurité calculée comme `2,70 − 2,42 = 0,28` présenté en pourcentage :
un écart de MER n'est pas un pourcentage, c'est un ratio.

### L'erreur que presque tout le monde fait ici

**Traiter le MER seuil d'EBITDA comme une constante.** Il contient `f`, qui est
un rapport à un CA. Le module § 4.1 le démontre : si le CA HT de P5 baissait de
20 % à structure identique, f passerait de 9,97 % à 12,46 % et le seuil de 2,33 à
2,45. **En décroissance, le seuil monte pendant que le CA baisse — tu cours après
une ligne qui recule.** D'où la règle d'usage : ce seuil se **recalcule** chaque
mois, il ne se mémorise jamais.

---

## Exercice 2 — L'EBITDA de P5 avec 5,5 % de retours

### La réponse

```
1. Nouvelle marge brute = 61,45 − 2,00                      = 59,45 %
2. Marge brute mensuelle = 3 610 997 € × 59,45 %            = 2 146 738 €
3. CM3 = 2 146 738 − 1 494 206                              =   652 532 €
4. EBITDA = 652 532 − 360 000                               =   292 532 €
   En % du CA HT = 292 532 ÷ 3 610 997                      =      8,10 %
                                                (contre 10,10 % au canonique)
5. Perte annuelle = (364 752 − 292 532) × 12 = 72 220 × 12  =   866 639 €
5 bis. Voie courte = 3 610 997 × 2 % × 12                   =   866 639 €   ✓
6. f = 360 000 ÷ 3 610 997 = 9,97 %
   MER seuil EBITDA = 1,20 ÷ (0,5945 − 0,0997) = 1,20 ÷ 0,49480 = 2,43
   Marge de sécurité = 2,90 ÷ 2,4252 − 1                    =    +19,58 %
                                                (contre +24,4 % au canonique)
7. EBITDA = 0  ⟺  m × 3 610 997 = 1 494 206 + 360 000 = 1 854 206 €
   m = 51,35 %  →  baisse de 61,45 − 51,35 = 10,10 points
   Taux de retour d'annulation = 3,50 + 10,10                =     13,60 %
```

**Ce que ça veut dire.** Deux points de taux de retour coûtent **866 639 € par
an**, soit 19,8 % de l'EBITDA annuel de 4 377 023 € (canonique § 7). Aucune ligne
de chiffre d'affaires n'a bougé, aucun contrat n'a été renégocié, personne n'a
rien décidé : c'est la définition d'un poste qui dérive.

La ligne 6 est la plus instructive. Le seuil passe de 2,33 à **2,43**, sans que
la marque n'ait touché à sa publicité ni à ses frais fixes. **Un tableau de bord
qui affiche « MER seuil : 2,33 » écrit en dur dans une cellule montre le mois
suivant une marge de sécurité fausse de 5 points.** C'est l'erreur n° 7 du § 8 du
module, et c'est aussi pourquoi le tableau de bord § 10 impose de le recalculer.

La ligne 7 donne le vrai repère : **NØRA supporte 13,60 % de ligne retours avant
EBITDA nul** — le niveau de l'électronique grand public et du bijou au tableau du
module [E02](../modules/E02-marche-et-produit.md) § 1.3. Une marque de soin qui
dériverait vers le taux de retour d'une catégorie d'accessoires perdrait la
totalité de son résultat sans jamais voir une ligne rouge sur son compte de
résultat mensuel, les retours arrivant 15 à 45 jours après la vente.

### Le barème — sur 20

| Critère | Points |
| --- | ---: |
| Nouvelle marge brute = 59,45 % (soustraction de 2 points, pas de 5,5) | 3 |
| Marge brute, CM3 et EBITDA en euros, les trois justes | 4 |
| EBITDA en % du CA HT = 8,10 % | 2 |
| Perte annuelle = 866 639 €, **vérifiée par la voie courte** | 4 |
| Nouveau seuil = 2,43 et marge de sécurité +19,6 % | 4 |
| Taux d'annulation = 13,60 %, démontré et non tâtonné | 3 |

**Fautes éliminatoires.** Avoir recalculé le CA (« il y aura moins de ventes ») :
l'énoncé impose tout inchangé, et changer une hypothèse imposée rend la copie non
comparable. Avoir remplacé la marge brute par `61,45 − 5,50 = 55,95 %` : c'est
l'ancienne ligne retours effacée au lieu d'être remplacée, et l'erreur vaut
3,5 points de marge, soit 1,5 M€ par an.

### L'erreur que presque tout le monde fait ici

**Mesurer le taux de retour par mois calendaire.** Le dénominateur du mois — les
commandes expédiées — a explosé pendant que le numérateur — les retours reçus —
reflète les ventes de 15 à 45 jours plus tôt. Une marque en croissance de 20 %
par mois sous-estime donc structurellement son taux de retour d'environ 20 %.
À P5, un point d'erreur vaut 433 320 € par an. **Le taux de retour se compte par
cohorte de commandes**, jamais par mois de réception.

---

## Exercice 3 — Ta cascade des marges

### La grille de lecture

Lis d'abord ta **marge brute (CM2)**, en % du CA HT, remises incluses en coût.

| Ta CM2 | MER seuil de contribution | Diagnostic | Action |
| ---: | ---: | --- | --- |
| **< 40 %** | > 3,00 | Aucune marque DTC ne tient ce MER en prospection | Ce n'est pas un problème de publicité : c'est le prix ou le coût produit (E02, E03) |
| **40 à 50 %** | 2,40 à 3,00 | Viable en récolte de demande uniquement | Vérifie que le Search sature ton volume. Sinon, remonte le prix |
| **50 à 57 %** | 2,10 à 2,40 | Zone P1–P2 de NØRA. Perte volontaire acceptable | Écris le montant que tu acceptes de perdre et jusqu'à quand |
| **57 à 61 %** | 1,97 à 2,10 | Zone P2–P4. Le modèle tient | Passe au payback et au CAC marginal |
| **> 61 %** | < 1,97 | Zone P5. Ou tu as oublié une ligne | Vérifie remises et retours : ce sont les deux qui manquent |

Puis les quatre contrôles qui disent si ta cascade est **vraie**.

| Contrôle | Ce que ça révèle si ça cloche |
| --- | --- |
| Ligne remises ≥ 3 % du CA HT | À zéro ou absente, elle est cachée dans ton prix moyen. Reconstitue-la : `CA au prix catalogue − CA encaissé` |
| Retours comptés par cohorte | Par mois calendaire en croissance, tu les sous-estimes d'environ ton taux de croissance |
| Publicité en trois lignes | Média seul, sans production ni honoraires, sous-estime le coût d'acquisition de 10 à 25 % |
| `CM2 % × CA HT` = CM2 € | Un écart signale une ligne comptée en TTC dans une cascade HT |

**La règle de propriété.** Le CM2 a **deux** responsables — opérations et
commerce — parce que sans cette séparation la remise devient le levier de secours
universel du commerce, financé par la marge des opérations. Le CM3 en a **un**,
revu **chaque jour**. Le même nom partout n'est pas une organisation, c'est un
point de défaillance unique.

### Le barème — sur 20

| Critère | Points |
| --- | ---: |
| Les seize lignes remplies, aucune vide | 4 |
| Remises en ligne séparée et non nulle | 4 |
| Retours comptés par cohorte, méthode écrite | 3 |
| Publicité décomposée média / production / honoraires | 3 |
| Colonne % du CA HT cohérente avec la colonne euros | 3 |
| Deux responsables distincts nommés | 3 |

**Faute éliminatoire.** Avoir calculé un pourcentage sur le CA TTC dans une
colonne intitulée « % du CA HT ». Toute la cascade devient fausse de 20 %, et
c'est l'erreur que ce module entier existe pour tuer.

### L'erreur que presque tout le monde fait ici

**Faire disparaître la remise dans le prix moyen.** Elle n'est alors nulle part :
ni en coût, ni en chiffre d'affaires perdu. La marge brute paraît correcte et
personne ne défend jamais la ligne, puisqu'elle n'existe pas. Chez NØRA elle vaut
5 points entre P1 et P5, soit 180 550 € par mois et 2 166 600 € par an à P5 —
la moitié de l'EBITDA annuel.

---

## Exercice 4 — Ton tableau de sensibilité

### La grille de lecture

D'abord, l'ordre attendu. Chez NØRA le rapport entre le premier levier (+10 %
d'AOV, 3 139 401 €) et le dernier (−10 % de frais fixes, 432 000 €) vaut **×7,3**.
Cet ordre n'est pas universel — il dépend de ta structure — mais deux propriétés
le sont, et ta copie doit les retrouver :

| Propriété | Pourquoi | Si tu ne la retrouves pas |
| --- | --- | --- |
| L'AOV bat la conversion | La logistique est un coût **par commande**, pas par euro. L'écart chez NØRA est de 476 656 €/an, soit exactement 10 % de la logistique annuelle | Tu as traité la logistique en % du CA dans la ligne AOV. Refais-la à euros de logistique constants |
| COGS et frais fixes ferment la marche | Ce sont les deux plus petites lignes de la cascade, et on n'en retire que 10 % | Si ton COGS dépasse 25 % du CA HT, l'ordre change légitimement — dis-le |

Puis la lecture qui décide, et elle porte sur toi.

| Écart entre la part de gains et la part d'heures | Diagnostic | Action |
| --- | --- | --- |
| **≤ ×1,5** | Ton attention est allouée correctement | Rien. C'est rare |
| **×1,5 à ×3** | Dérive ordinaire | Déplace une réunion hebdomadaire du levier sur-servi vers le levier n° 1 |
| **×3 à ×6** | Problème d'allocation d'attention | Le levier n° 1 doit avoir un propriétaire nommé et un point hebdomadaire. Sinon il n'avancera jamais |
| **> ×6** | Tu confonds contrôle et impact | Écris pourquoi. La réponse honnête est presque toujours : « parce que c'est le seul levier que je décide seul » |

**Pourquoi ce sont presque toujours le COGS et les frais fixes qui
sur-consomment.** Renégocier un fournisseur est **unilatéral** quand une hausse
d'AOV demande l'accord du marché ; le gain est **immédiat et certain** quand une
hausse d'AOV échoue une fois sur deux ; et couper des coûts **a l'air** d'être du
management. Trois raisons rationnelles, et aucune ne change le ×7,3.

### Le barème — sur 20

| Critère | Points |
| --- | ---: |
| Les sept lignes chiffrées | 4 |
| Ligne AOV traitée à **logistique constante en euros** | 5 |
| Ligne conversion traitée à marge brute % constante | 3 |
| Heures de direction renseignées honnêtement, y compris quand c'est gênant | 3 |
| Les deux parts (gains / heures) converties en pourcentages comparables | 3 |
| Rapport calculé et commenté | 2 |

**Faute éliminatoire.** Avoir donné le même gain aux lignes AOV et conversion.
Les deux ajoutent le même chiffre d'affaires ; elles ne rapportent pas la même
chose, et l'intégralité de l'écart est la logistique qui ne suit pas. Ne pas
l'avoir vu, c'est n'avoir rien retiré de la section 7.

### L'erreur que presque tout le monde fait ici

**Traiter le levier « +10 % d'AOV » comme « +10 % de CA ».** Un panier moyen qui
monte à commandes constantes ne fait pas grossir la logistique : le nombre de
colis ne change pas. Le taux de marge brute lui-même monte — de 61,45 % à
62,45 % chez NØRA, un point gagné sans toucher à un seul contrat fournisseur.
C'est la raison arithmétique pour laquelle P5+ existe (canonique § 8) : +7 %
d'AOV, −7 % de commandes, même chiffre d'affaires, +4,5 points de marge brute.

---

## Exercice 5 — Tes deux seuils et ton point mort

### La grille de lecture

Ta **CM3 par commande** d'abord. C'est le seul nombre de ce module qui répond par
oui ou par non.

| Ta CM3 par commande | Diagnostic | Action |
| --- | --- | --- |
| **Négative** | Situation P1 (−3,63 €/commande chez NØRA). Vendre plus creuse la perte | Tu n'as **pas** de point mort. Aucun volume ne t'en sortira. Remonte le MER par le prix, l'offre ou la créative — jamais par la quantité |
| **0 à 3 €** | Point mort hors d'atteinte à structure constante | Coupe des frais fixes **et** remonte le MER. Un seul des deux ne suffit pas |
| **3 à 8 €** | Zone P2–P3. Transitoire | On y transite, on n'y campe pas. Fixe la date de sortie |
| **8 à 12 €** | Zone P3–P4 | Vérifie le payback marginal avant d'accélérer |
| **> 12 €** | Zone P5 | Le sujet devient l'AOV et le réachat, plus le volume |

Puis ta **marge de sécurité en volume**, `commandes réelles ÷ point mort − 1` :

| Marge de sécurité | Ce que ça veut dire | Action |
| --- | --- | --- |
| **< 0 %** | Tu es sous ton point mort | Le seul plan acceptable tient sur une page et a une date |
| **0 à +50 %** | Un incident te fait basculer : hausse de CPM, rupture, compte suspendu | Aucune embauche, aucun nouveau marché. Constitue la réserve d'abord |
| **+50 à +100 %** | Zone P3–P4. Tu absorbes un accident, pas deux | Tu peux parier sur un nouveau marché, un seul à la fois |
| **> +100 %** | Zone P5 (+101,3 % chez NØRA) | Cette réserve **est** ce qui autorise les paris |

**Le piège de la ligne 2 bis, et c'est pour ça qu'elle est notée.** Ton MER seuil
d'EBITDA n'est valable qu'au niveau de CA HT où tu l'as calculé, parce que `f`
est un rapport à ce CA. Écrire « mon seuil est 2,45 » sans écrire « à 900 000 €
de CA HT mensuel » est une phrase incomplète — et elle devient fausse le premier
mois de baisse.

**Sur le post-it.** Trois nombres, pas quatre : le point mort en commandes par
jour parce que toute l'équipe le vérifie sur un écran chaque matin, le MER seuil
d'EBITDA parce qu'il bouge sans qu'aucune décision ne l'ait autorisé, et le MER
des 7 derniers jours parce qu'il est le seul indicateur non truquable —
numérateur de ta banque, dénominateur de tes factures média.

### Le barème — sur 20

| Critère | Points |
| --- | ---: |
| Les deux seuils, avec 1,20 au numérateur | 4 |
| **Niveau de CA HT de validité du seuil d'EBITDA écrit** | 3 |
| CM3 par commande décomposée en marge brute /cmd − pub /cmd | 4 |
| Point mort mensuel puis journalier, division par 30,33 | 3 |
| Marge de sécurité en volume calculée | 3 |
| Post-it écrit, trois nombres et trois seulement | 3 |

**Faute éliminatoire.** Avoir calculé un point mort avec une CM3 par commande
négative. Il n'existe pas : la formule `frais fixes ÷ CM3` donne alors un nombre
négatif qu'il faut refuser d'écrire, et non un objectif de volume.

### L'erreur que presque tout le monde fait ici

**Chercher le point mort par le volume quand la CM3 par commande est négative.**
C'est la situation la plus dangereuse du métier parce qu'elle **ressemble
exactement** à un problème de volume sans en être un : l'équipe demande plus de
budget, le CA monte, la perte s'aggrave proportionnellement, et chacun conclut
qu'il faut encore plus de volume. Le seul remède est de remonter le MER au-dessus
du seuil de contribution — par le prix, le produit ou la publicité.

---

## Exercice 6 — La tranche de budget supplémentaire

### La réponse

```
1. CAC marginal = 100 000 € ÷ 1 266                            =  78,99 €
2. Résultat 12 mois = 1 266 × 86,75 € − 100 000 €              =  +9 826 €
3. Rendement sur 12 mois = 9 826 ÷ 100 000                     =   +9,83 %
4. Payback marginal, interpolation entre 6 mois (64,11 €) et 12 mois (86,75 €) :
      (78,99 − 64,11) ÷ (86,75 − 64,11) = 14,88 ÷ 22,64 = 0,657
      Payback = 6 + 0,657 × 6                                  =  9,9 mois
5. Avance média = 100 000 € × 9,9 mois                         = 994 318 €
6. CA TTC mensuel ajouté = 1 266 × 64,00 €                     =  81 024 €
   BFR immobilisé = 81 024 ÷ 100 000 × 52 263 €                =  42 346 €
7. Besoin total = 994 318 + 42 346 = 1 036 664 €   →  2,59 × les 400 000 €
8. LTV d'annulation = 100 000 ÷ 1 266                          =  78,99 €
9. Marge d'erreur = (86,75 − 78,99) ÷ 86,75                    =   8,95 %
```

**La bonne réponse est l'option B : refuser la tranche.**

La démonstration ne tient pas au signe du résultat — il est positif — mais à
trois nombres que la proposition ne contient pas.

**Le rendement réel n'est pas 9,83 %, il est de 0,99 %.** Les 9 826 € ne se
gagnent pas sur les 100 000 € du mois : ils se gagnent sur les 994 318 € de
trésorerie que la tranche immobilise pendant qu'elle se rembourse.
`9 826 ÷ 994 318 = 0,99 %`. Aucune dette, aucun apport, aucun découvert
n'est disponible à ce prix-là. La tranche est rentable en comptabilité et
destructrice en trésorerie — c'est la définition exacte de ce qui tue les marques
rentables.

**Le besoin de trésorerie vaut 2,59 fois la réserve** : 1 036 664 € contre
400 000 €. Et dès le premier mois le trou vaut
`100 000 − 1 266 × 32,77 = 58 513 €`.

**La marge d'erreur est de 8,95 %.** La tranche meurt si la LTV réelle descend
sous 78,99 € — or 86,75 € est une moyenne de cohortes acquises sur les canaux
existants, et les clients d'un canal neuf sont par construction plus loin du cœur
de cible. Le même seuil se lit en incrémentalité : il suffit que **8,95 % des
1 266 clients seraient venus de toute façon** pour que la tranche détruise de la
valeur. À 30 % de non-incrémentalité (§ 9 du module), le résultat devient
`1 266 × 0,70 × 86,75 − 100 000 = −23 122 €`.

**Enfin, 9,9 mois de payback violent le seuil d'alerte du tableau de bord du
module** — *« > 3 mois si autofinancé, > 6 si endetté »* — d'un facteur 3,3.

### La condition exacte sous laquelle l'option A devient la bonne

Elle est chiffrable, et il y a trois portes. Une seule suffit.

| Porte | Condition exacte | Lecture |
| --- | --- | --- |
| **Le CAC marginal** | Le test doit livrer **≥ 2 102 nouveaux clients pour 100 000 €**, soit un CAC marginal **≤ 47,57 €** | 47,57 € est la LTV en contribution à 3 mois : à ce CAC, le payback tombe à 3 mois et respecte le seuil autofinancé |
| **La trésorerie** | Réserve ≥ **1 036 664 €**, ou financement externe à un coût annuel **< 0,99 %** | La seconde branche n'existe pas dans le monde réel. C'est ce qui rend la première obligatoire |
| **L'horizon de financement** | Capital propre levé, dont le seuil de payback est 12 mois | 9,9 mois passe alors — mais le rendement reste 0,99 % sur le cash avancé, ce qui reste un mauvais emploi de fonds levés |

Le seuil absolu : la tranche ne détruit de la valeur qu'en dessous de
**1 153 clients** (`100 000 ÷ 86,75`). Entre 1 153 et 2 102, elle crée de la
valeur **et** reste infinançable — c'est la zone où se prennent les mauvaises
décisions, parce que le tableur dit oui.

### Le seul test qui trancherait pour de bon

Aucun des nombres ci-dessus ne prouve que les 1 266 clients existent **à cause
de** la dépense. Le test qui le prouve est un **test d'incrémentalité par zones
géographiques** : tu coupes le nouveau canal sur une moitié des marchés tirée au
sort, tu la maintiens sur l'autre, et tu compares le **chiffre d'affaires total**
des deux groupes — pas le CA attribué. C'est la seule mesure dont le numérateur
ne soit pas produit par la partie qui vend l'espace. Module
[E09](../modules/E09-mesure-et-incrementalite.md), cas
[C06](../etudes-de-cas/C06-test-incrementalite.md). La tolérance étant de 8,95 %,
la décision se joue entièrement dans la zone que l'attribution ne sait pas
mesurer — et c'est pour ça que le test précède l'engagement, jamais l'inverse.

### Le barème — sur 20

| Critère | Points |
| --- | ---: |
| CAC marginal 78,99 € et résultat 12 mois +9 826 € | 3 |
| Payback marginal 9,9 mois par interpolation déroulée | 4 |
| Besoin de trésorerie chiffré, avance média **et** BFR | 4 |
| Option B tranchée | 2 |
| Rendement recalculé sur le cash avancé (0,99 %) **ou** comparaison explicite au seuil de payback | 3 |
| Condition de bascule chiffrée (2 102 clients / 47,57 €) | 3 |
| Test d'incrémentalité nommé | 1 |

**Fautes éliminatoires.** Avoir validé la tranche au seul motif que 9 826 € > 0 :
un résultat positif sur 12 mois ne dit rien de la capacité à le financer. Avoir
comparé le CAC marginal de 78,99 € au nCAC moyen de 40,03 € pour conclure « c'est
deux fois trop cher » : le CAC marginal se compare à la **LTV**, jamais à un CAC
moyen, sans quoi tu commets l'erreur inverse du § 6.4 — s'arrêter trop tôt parce
que le ratio est beau.

### L'erreur que presque tout le monde fait ici

**Juger la tranche sur son ratio LTV/CAC.** `86,75 ÷ 78,99 = 1,10`, ce qui semble
« faible mais positif », et la discussion s'installe sur ce nombre. Or le ratio ne
voit ni le temps ni le cash : deux tranches au même ratio de 1,10, l'une à 3 mois
de payback et l'autre à 9,9, sont deux décisions opposées. **Le ratio te dit si
un client vaut son coût ; le payback te dit si tu peux te le permettre.** Ici la
réponse au premier est oui, et au second non — et c'est le second qui décide.

---

*Fin du corrigé du module E01. Formulaire : [`E01-rendu.md`](E01-rendu.md).
Module suivant : [E02 — Choisir le terrain](../modules/E02-marche-et-produit.md).*
