# Séance S05 — La recherche client et les angles

> **Niveau requis :** L03 · **Durée :** 8 h (dont 5 h de dépouillement) · **Livrable :** un corpus codé et trois fiches d'angle complètes, adossées à du verbatim littéral · **Modules :** [E04](../modules/E04-psychologie-du-client.md), [E02](../modules/E02-marche-et-produit.md)
> **Ce que tu ne peux pas faire sans avoir fait cette séance :** écrire une publicité. Sans corpus, tu écriras ce que **toi** trouves convaincant, et tu paieras l'écart entre ton vocabulaire et celui de ton client au prix du média, tous les jours, pendant des années.

---

## 1. Où tu en es

Tu sors de [S04](S04-offre-prix-et-panier.md) avec une gamme à trois étages, des prix arrêtés, un tableau de construction de panier et un MER seuil passé sous ton MER atteignable. Ton offre existe et elle est arithmétiquement viable.

*Acronymes : **MER** — media efficiency ratio, CA TTC total ÷ dépense publicitaire totale. **nCAC** — coût d'acquisition d'un **nouveau** client. **UGC** — contenu tourné par un client ou un créateur, pas par un studio. **Verbatim** — une phrase de client copiée mot pour mot.*

**Décidé :** ce que tu vends, à quel prix, sous quelle forme, avec quelle marge par commande. **Pas décidé :** ce que tu **dis**. Pas le slogan — la chaîne de raisonnement qui fait qu'une personne qui ne te connaît pas et ne cherchait rien comprend en huit secondes qu'elle a un problème qu'elle nommait mal, et que ton produit agit sur la cause plutôt que sur le symptôme.

Un piège propre à ce moment du parcours : tu viens de passer trois séances dans le COGS, le coefficient et le MER seuil. Tu connais ton produit mieux que quiconque, et c'est exactement ce qui te rend mauvais pour en parler. **Tu vas spontanément écrire depuis le niveau de conscience 4 ou 5** — le flacon, la composition, le prix barré — devant une audience au niveau 1 ou 2. [E04](../modules/E04-psychologie-du-client.md) § 2.3 chiffre l'erreur : nCAC ×2,25, LTV/CAC à 12 mois à 0,96, payback qui passe de 1,8 mois à plus de douze. Ce n'est pas une dégradation de performance, c'est un changement de modèle de financement.

---

## 2. Ta mission

Produire **trois fiches d'angle complètes**, chacune adossée à du matériau client réel. Bornes :

1. **Dépouiller au moins 460 pièces** : 200 avis 1 et 2 étoiles de concurrents directs, 200 avis 5 étoiles, 60 questions ou commentaires publics pré-achat. Sortie minimale : **120 verbatims littéraux** codés.
2. **Mener 5 entretiens** de 25 minutes, enregistrés et retranscrits, avec les huit questions du § 4.2 — pas sept, pas les tiennes.
3. **Coder** l'ensemble : état mental, thème, fréquence, intensité, acte.
4. **Identifier trois écarts de croyance distincts** : trois endroits où ce que le corpus croit majoritairement est faux ou incomplet.
5. **Rédiger trois fiches d'angle** : chaîne de croyance en quatre maillons, trois preuves hiérarchisées, six objections traitées, niveau de conscience, format, destination.

Résultat attendu : six à huit pages que tu poses devant un monteur ou un créateur en [S06](S06-premier-lot-de-creas.md), et dont il tire une publicité sans te poser une question.

---

## 3. Ce dont tu disposes

| Ressource | Usage |
|---|---|
| Ton livrable [S04](S04-offre-prix-et-panier.md) | Un angle doit vendre le **panier**, pas l'unité |
| Ton livrable [S02](S02-prouver-la-demande.md) | Les concurrents identifiés : ce sont les fiches à dépouiller |
| [E04](../modules/E04-psychologie-du-client.md) § 2, 3, 4, 5, 7 | Niveaux de conscience, chaîne de croyance, six objections, hiérarchie des preuves. **Cette séance est la mise en œuvre chronométrée du § 7** |
| [canoniques § 5](../donnees/chiffres-canoniques.md) | nCAC par canal, 19,00 € à 55,00 € : le gradient de conscience vaut ×2,89 |
| [canoniques § 7](../donnees/chiffres-canoniques.md) | −10 % de nCAC = +1 793 047 € d'EBITDA annuel. C'est le prix d'un bon angle |
| `test_significativite.py --comparer` | Savoir si un motif à 11 % se distingue d'un motif à 7 % |

**Convention :** un verbatim se copie, jamais ne se reformule. Le jour où tu écris « les clients trouvent que c'est trop cher » au lieu de « 18 € une paire de chaussettes, il faut le vouloir », tu as détruit ce que tu étais venu chercher.

---

## 4. La méthode, pas à pas

### 4.1 Le dépouillement

| Source | Volume minimal | Ce que tu y cherches | Le piège |
|---|---:|---|---|
| Avis 1–2 étoiles concurrents | **200** | Objections réelles, vocabulaire de la déception | Mélanger défaut logistique et défaut produit : **deux piles** |
| Avis 5 étoiles concurrents | **200** | Les mots exacts du résultat obtenu | Les avis courts sollicités par remise ne disent rien |
| Questions, commentaires publics | **60** | L'objection à l'instant où elle bloque l'achat | Y répondre au lieu de les compter |
| Forums et groupes | 2 h | **Comment les gens s'expliquent la cause** | Une croyance répandue n'est pas une vérité |
| Entretiens | **5** de 25 min | Ce qui s'est passé **avant** l'achat | § 4.2 |
| Tickets SAV, si tu vends | tous, 30 j | Ce que ta page ne dit pas | Traiter le ticket sans compter le motif |

Pourquoi 200 et pas 40 : un motif présent dans 8 % du corpus peut porter un angle entier ; sur 40 avis, 8 % font 3 occurrences, et 3 occurrences ne se distinguent pas de zéro — vérifie-le avec `test_significativite.py --comparer --a-visiteurs 40 --a-conversions 3 --b-visiteurs 40 --b-conversions 1`. Le coût de ce volume est du temps, pas de l'argent : c'est pourquoi presque personne ne le fait, et c'est pourquoi ça marche encore.

**La grille de codage**, une ligne par verbatim, huit colonnes : `id` ; `source` (avis 2★ / avis 5★ / question / forum / entretien n°, jamais « internet ») ; `date` ; `verbatim` — **mot pour mot**, fautes comprises, sans crochets ni résumé ; `état mental` — les huit d'[E04](../modules/E04-psychologie-du-client.md) § 7.3 : symptôme, croyance sur la cause, tentative précédente, raison d'abandon, déclencheur, objection, bénéfice constaté, justification sociale ; `thème` — il se découvre en codant, il ne se décide pas avant ; `intensité` ; `acte` — la personne a-t-elle **fait** quelque chose.

**Le barème d'intensité, parce que la fréquence seule ment.** **1 — mentionné**, sans circonstance : *« pas terrible la tenue »*. **2 — raconté avec circonstance** : *« au bout de 25 km j'ai senti la brûlure »*. **3 — raconté avec conséquence**, abandon, dépense, consultation : *« j'ai fini le semi en marchant et j'ai jeté la paire »*.

**Score d'un thème = occurrences × intensité moyenne.** Un thème à 12 occurrences d'intensité 2,8 (33,6) bat un thème à 26 occurrences d'intensité 1,2 (31,2) : le premier décrit des gens qui ont agi, le second des gens qui ont haussé les épaules.

Trois disciplines : **tu codes tout**, le verbatim qui contredit ton produit compris — c'est ton objection principale, et elle existera de toute façon ; tu ne codes pas deux sessions dans le même état d'esprit, sinon tu retrouveras tes propres idées dans ton corpus ; un verbatim peut porter deux thèmes, mais **on ne découpe jamais une phrase pour la faire entrer dans une case**.

### 4.2 Les entretiens — cinq personnes, huit questions

**Recruter cinq personnes**, par rendement décroissant : tes acheteurs des 30 derniers jours, par courriel personnel du fondateur, 25 minutes annoncées et indemnité annoncée d'avance — bon d'achat ou 30 €, compte une quarantaine de messages pour cinq entretiens ; les acheteurs de tes concurrents dans les communautés où ils se rassemblent, en écrivant à l'administrateur avant de publier et en annonçant que tu ne vends rien pendant l'appel — **et tu ne vends rien pendant l'appel** ; ton entourage au second degré, jamais tes amis ; les panels payants en dernier recours, 60 à 120 € par participant, avec leur part de professionnels du panel.

**La règle qui décide de tout : tu recrutes sur un comportement, jamais sur une opinion.** « A acheté ce type de produit dans les six derniers mois » est un critère ; « est intéressé par le sujet » te donnera cinq personnes qui n'ont rien acheté et qui te diront ce que tu veux entendre.

**Les huit questions, dans cet ordre** ([E04](../modules/E04-psychologie-du-client.md) § 7.2) :

1. **Raconte-moi la dernière fois que tu as remarqué le problème. Où étais-tu, que faisais-tu ?**
2. **Qu'as-tu fait dans les 24 heures qui ont suivi ?**
3. **Qu'avais-tu essayé avant ? Concrètement, qu'est-ce que ça a donné ?**
4. **Pourquoi as-tu arrêté ?**
5. **Le jour où tu as commandé, qu'est-ce qui s'était passé ce jour-là ou la semaine d'avant ?**
6. **Entre le moment où tu as vu le produit et celui où tu as payé, qu'est-ce qui t'a fait hésiter, et qu'est-ce qui a levé l'hésitation ?**
7. **Comment as-tu expliqué cet achat à un proche ?**
8. **Si le produit disparaissait demain, qu'est-ce qui te manquerait exactement ?**

L'ordre n'est pas négociable. La 4 donne le **mécanisme d'échec de la catégorie**, matière du niveau 3 ; la 5 donne le **déclencheur**, la plus rentable des huit — l'événement qui transforme un problème toléré depuis des années en achat de mardi soir ; la 6 donne l'objection et sa levée, donc ta hiérarchie de preuves ; la 7 donne la **justification socialement acceptable**, qui est littéralement le texte de ton annonce. Conduite : tu parles 20 % du temps au maximum et tu le vérifies sur l'enregistrement ; tu comptes **trois secondes de silence** avant chaque relance, parce que c'est là que sortent les phrases qui valent le déplacement ; tu creuses sur les faits, jamais sur les opinions.

**Ce qu'on ne demande jamais.**

| Question interdite | La raison de fond |
|---|---|
| « Qu'est-ce que vous voudriez ? » | Elle met le client en position de concepteur, où il est mauvais. Sa réponse n'est reliée à aucun comportement observable : **tu ne peux ni la confirmer ni la réfuter**, et elle finit en réunion comme argument d'autorité. Elle produit une liste de fonctionnalités, puis « la même chose moins cher » |
| « Pourquoi avez-vous choisi cette marque ? » | Nisbett et Wilson, *Telling More Than We Can Know* (Psychological Review, 1977) : interrogés sur les causes de leur décision, les sujets produisent des explications cohérentes, fausses, énoncées avec une grande confiance. Ils ne mentent pas, ils reconstruisent |
| « Que pensez-vous de mon produit ? » | Rob Fitzpatrick, *The Mom Test* (2013) : parle de la vie du client, jamais de ton idée. Tu récoltes de la politesse |
| « Combien seriez-vous prêt à payer ? » | Un prix déclaré hors situation d'achat ne prédit rien ; [S04](S04-offre-prix-et-panier.md) § 4.1 en donne la seule forme exploitable |

**Un entretien qui demande « pourquoi » collecte des reconstructions ; un entretien qui demande « raconte » collecte des faits.**

**Ce que cinq entretiens peuvent et ne peuvent pas.** Ils ne sont pas un échantillon : ils ne mesurent rien et ne prouvent aucune fréquence. **Ils produisent des hypothèses ; ce sont les 460 pièces du § 4.1 qui les comptent.** L'erreur classique inverse cette division du travail — bâtir un angle sur une phrase brillante entendue en entretien 3 sans vérifier si le motif existe dans le corpus. S'il n'y est pas, ce n'est pas un angle, c'est une anecdote.

### 4.3 La chaîne de croyance en quatre maillons

```
1. PROBLÈME RESSENTI          ce que la personne vit, dans ses mots à elle
2. MÉCANISME DU PROBLÈME      pourquoi ça lui arrive — ce qu'elle ignore
3. MÉCANISME DE LA SOLUTION   pourquoi CE produit agit sur CE mécanisme
4. PREUVE                     pourquoi elle devrait te croire
```

Le classement est économique avant d'être créatif : le maillon 1 se copie **en une journée**, il est public dans les avis ; le maillon 4 s'achète ou se produit ([E04](../modules/E04-psychologie-du-client.md) § 5) ; le maillon 3 se copie en **trois mois** ([E02](../modules/E02-marche-et-produit.md) § 6.3). **Le maillon 2 ne se copie pas par lecture : il faut avoir compris.**

**Il est le plus négligé et le plus rentable, et les deux ont la même cause.** Négligé, parce qu'il ne se voit dans aucune interface — pas de test A/B de bouton, pas de réunion, ça ne ressemble pas à du travail. Rentable, parce qu'il est le seul des quatre à être **rare, vrai et coûteux à réémettre** : la définition d'une asymétrie d'information, donc d'une marge. Quand il est juste, le problème cesse d'être « normal », la catégorie générique devient insuffisante, et **ton prix cesse d'être comparé à celui du concurrent pour être comparé au coût du problème**. [E04](../modules/E04-psychologie-du-client.md) § 3.3 le chiffre sur NØRA : trois phrases sur le cycle du cheveu font basculer 8,70 % des commandes du flacon à 39,00 € TTC vers la cure à 99,00 € TTC — **2 040 852 € d'EBITDA annuel**, 46,6 % du total du palier P5.

**Trouver ton maillon 2 : cherche l'écart de croyance.** Isole la colonne « croyance sur la cause » et compte ; une croyance domine, souvent 60 à 80 % des verbatims du thème. Quatre questions décident si c'en est un.

1. **Fausse ou seulement incomplète ?** Les deux marchent : « c'est l'âge » est incomplet, « c'est le frottement » est faux.
2. **Fait-elle suivre le mauvais indicateur ?** Le test le plus discriminant. Compter les cheveux tombés, juger en trois semaines, monter d'une demi-taille : si la croyance fait mesurer la mauvaise chose, tu peux **donner le bon indicateur** — et un indicateur se retient.
3. **Sa correction change-t-elle ce que le client accepte d'acheter ?** Sinon c'est de la culture générale. Le mécanisme doit rendre évident un lot, une cure, un format ou un prix de ta gamme de [S04](S04-offre-prix-et-panier.md).
4. **Strictement vrai et documenté ?** Non négociable : c'est le seul maillon vérifiable auprès d'un tiers, et l'allégation engage ta responsabilité — un mécanisme qui déborde vers le thérapeutique change de régime juridique et de produit.

**Sans écart de croyance, tu n'as pas un angle : tu as une description** — copiable en une journée, et présente mot pour mot chez trois concurrents dans le trimestre.

### 4.4 Du matériau à l'angle, étape par étape

**1 — Trier les thèmes par score**, tableau complet, thèmes écartés compris : c'est le document que tu reliras en [S09](S09-lire-les-premiers-chiffres.md) quand un angle décrochera.

**2 — Vérifier que tes trois premiers thèmes sont trois problèmes différents.** Le test : **si la même phrase de maillon 2 peut servir aux trois, tu n'as qu'un angle.** Dans ce cas, garde-le et va chercher les deux autres à des niveaux de conscience différents — un sur le mécanisme d'échec de la catégorie (niveau 3), un sur l'objection dominante (niveau 4). C'est presque toujours la bonne sortie, et le corrigé du § 7 la prend.

**3 — Écrire le maillon 1 par copie.** Le verbatim d'intensité 3 le plus fréquent du thème, collé. Tu as le droit de couper, jamais de reformuler : « les coureurs souffrent d'ampoules sur les sorties longues » à la place de « à 25 km j'ai senti la brûlure, à 30 j'avais une cloque, j'ai fini en marchant », c'est remplacer une scène par une catégorie.

**4 — Écrire le maillon 2 en trois phrases maximum.** Structure imposée : *(a) ce n'est pas ce que tu crois — (b) voici ce qui se passe réellement — (c) donc l'indicateur que tu suis est le mauvais, et voici le bon.* La partie (c) est celle qu'on oublie, et c'est celle qui se retient.

**5 — Écrire le maillon 3 comme un pont, pas comme une fiche technique** : il reprend **le vocabulaire exact du maillon 2**, terme pour terme. Un maillon 3 qui ne le fait pas signale que le produit ne traite pas le mécanisme que tu viens d'exposer, et le lecteur le sent même s'il ne saurait pas le dire.

**6 — Attacher trois preuves de rangs différents** dans l'échelle d'[E04](../modules/E04-psychologie-du-client.md) § 5, dont **au moins une de rang 6 ou plus** : démonstration visible, caution d'expert, étude sous contrôle, garantie financière. Pour chacune, la source vérifiable, puis les deux tests — le client peut-il remonter à la source ? combien coûterait-il à un menteur d'écrire la même phrase ? Si la réponse est « la même chose que toi », la preuve ne te sépare pas de ton imitateur.

**7 — Traiter les six objections dans les mots du corpus** : c'est cher / est-ce que ça marche / pas pour moi / je n'ai pas le temps / et si ça rate / qui êtes-vous. Une objection sans verbatim signale que tu ne l'as pas cherchée : elles y sont toutes. Et **une objection traitée trop tôt en crée une** — annoncer la garantie avant d'avoir posé le mécanisme suggère que le produit en a besoin.

### 4.5 L'appariement angle × niveau de conscience × format

| Niveau de conscience | Ce que l'angle doit faire | Format | Destination | nCAC relatif |
|---|---|---|---|---:|
| **1 — inconscient du problème** | Nommer le symptôme, le rendre anormal | Vidéo native, récit à la 1ʳᵉ personne | Article, quiz | ×2,5 à ×3,0 |
| **2 — conscient du problème** | **Poser le mécanisme du problème** | Vidéo explicative, UGC témoignage | Page longue problème → mécanisme → produit | ×2,0 à ×2,5 |
| **3 — conscient de la solution** | Montrer pourquoi la catégorie échoue | Comparatif, avant/après | Page produit avec bloc comparatif | ×1,6 à ×2,0 |
| **4 — conscient du produit** | Preuve, offre, levée d'objection | Statique de preuve, remarketing | Page produit courte | ×1,2 à ×1,5 |
| **5 — le plus conscient** | Prix, disponibilité, garantie | Recherche de marque, courriel, SMS | Panier, paiement | ×1,0 |

**Jamais tes trois angles au même niveau.** Le gradient de nCAC du niveau 5 au niveau 1 vaut ×2,89 dans le plan média canonique — 19,00 € sur la recherche contre 55,00 € sur la découverte ([canoniques § 5](../donnees/chiffres-canoniques.md)) — mais tout mettre en bas de l'échelle est impossible : la récolte pèse 11,0 % du budget et livre 20,9 % des clients attribués **parce qu'elle est plafonnée**. On ne récolte que ce qui a été semé ; doubler le budget de récolte double le prix du clic, pas le nombre de recherches.

**La destination doit continuer l'angle, mot pour mot.** Un angle de niveau 2 qui atterrit sur une page produit courte perd son mécanisme entre le clic et le paiement, et la conversion s'effondre sans que rien dans l'interface publicitaire ne le signale ([S07](S07-le-site.md)) : **un angle sans page à sa mesure n'est pas un angle, c'est un coût.**

**Un angle par format, pas un angle décliné douze fois.** La différence entre un concept et une variation est exactement ce que mesure la condition 3 de la [Porte P1 → P2](../mentorat/jalons.md) : deux gagnants **distincts**, pas deux versions du même.

---

## 5. Ton livrable

```
=====================================================================
LIVRABLE S05 — RECHERCHE CLIENT ET ANGLES
Marque : ___________   Date : __/__/__   Temps passé : ____ h

A. CORPUS
Avis 1-2★ ____ sur ____ concurrents, du __/__ au __/__   Avis 5★ ____
Questions ____   Forums ____ h   Entretiens ____
VERBATIMS LITTÉRAUX CODÉS : ____           (plancher : 120)

B. TABLEAU DES THÈMES — tous, y compris les écartés
| Thème | Occurrences | % corpus | Intensité moy. | Score | Acte oui % |

C. LES TROIS ÉCARTS DE CROYANCE — pour chacun :
  Croyance dominante (verbatim + occurrences) : ____________
  Ce qu'elle a de faux ou d'incomplet         : ____________
  Mauvais indicateur qu'elle fait suivre      : ____________
  Bon indicateur                              : ____________
  Ce que sa correction change dans l'achat    : ____________
  Source technique du mécanisme               : ____________

D. FICHE D'ANGLE — à remplir TROIS fois
ANGLE n° __ | NOM : ____________
Thème ____ Occurrences ____ Intensité ____ Score ____
Niveau ____ Format ____ Destination ____ nCAC relatif ×____
VERBATIMS SOURCES (deux au moins, littéraux, avec id)
  V___ : « ______________ »   V___ : « ______________ »
CHAÎNE DE CROYANCE
  1. PROBLÈME  ______________________________________
  2. MÉCANISME (a) ce n'est pas ______ (b) ce qui se passe ______
     DU PROBLÈME (c) mauvais indicateur ______ , bon ______
  3. MÉCANISME DE LA SOLUTION ________________________
     (termes du maillon 2 repris : ____________)
  4. PREUVE    ______________________________________
TROIS PREUVES — au moins une de rang ≥ 6
| # | Preuve | Rang E04 § 5 | Source vérifiable | Coût pour un menteur |
SIX OBJECTIONS
| # | Objection | Verbatim du corpus | Ma réponse écrite | Où elle apparaît |
  1 c'est cher · 2 ça marche ? · 3 pas pour moi
  4 pas le temps · 5 et si ça rate · 6 qui êtes-vous
TROIS HOOKS : visuel ______ / parlé ______ / écrit ______
CE QUE JE NE DIRAI JAMAIS : 1. ______ 2. ______ 3. ______

E. CONTRÔLE FINAL
Trois niveaux de conscience différents ?                     O / N
Une même phrase de maillon 2 couvre-t-elle les trois ?       O / N
Chaque angle vend-il le PANIER de S04 ou l'unité ?           ______
Chaque angle a-t-il une destination qui le continue ?        O / N
=====================================================================
```

---

## 6. La grille d'évaluation

Barème sur 100, **seuil de validation 72** — plus haut que celui de [S04](S04-offre-prix-et-panier.md), parce que [S06](S06-premier-lot-de-creas.md) produira douze concepts à partir de ces trois fiches. Un angle faible ne donne pas quatre créas moyennes : il donne quatre créas mortes et brûle deux semaines de budget de test.

| # | Critère | Pts | Ce qui vaut les points | Ce qui les fait perdre |
|---|---|---:|---|---|
| 1 | Volume du corpus | 10 | ≥ 200 avis négatifs, ≥ 200 positifs, ≥ 60 questions, ≥ 120 verbatims | Source sous son plancher : −4 ; sans dates : −3 |
| 2 | Entretiens | 12 | 5, enregistrés, retranscrits, 8 questions dans l'ordre | 4 entretiens : −4 ; questions modifiées : −4 ; **question hypothétique posée : −6** |
| 3 | Verbatims littéraux | 10 | Mot pour mot, avec id, source, date | Un reformulé : −5 ; tous : **éliminatoire** |
| 4 | Codage et intensité | 10 | 8 états mentaux, intensité argumentée, colonne « acte » | Codage par thème produit seul : −6 ; intensité absente : −5 |
| 5 | Comptage et scores | 8 | Tableau complet, écartés inclus, score = occ. × intensité | Fréquence sans effectif : −4 |
| 6 | **Les trois écarts de croyance** | **18** | Trois croyances citées en verbatim, fausses ou incomplètes, avec le mauvais **et** le bon indicateur | Un seul écart : −8 ; « le client ne connaît pas notre produit » : **−18** |
| 7 | Chaînes de croyance rédigées | 14 | Quatre maillons, maillon 3 reprenant les termes du maillon 2 | Maillon 2 absent ou remplacé par un bénéfice : −10 par angle |
| 8 | Preuves | 10 | 3 par angle, rangs différents, ≥ 1 de rang ≥ 6, source vérifiable | Rang 1 ou 2 comptée comme preuve : −4 ; aucune source : −6 |
| 9 | Objections | 8 | Les 6, avec verbatim et réponse rédigée | Objection sans verbatim : −1,5 chacune |
| 10 | Appariement niveau × format × destination | 10 | Trois niveaux différents, destination cohérente | Trois angles au même niveau : −7 ; destination absente : −4 |

**Cinq fautes éliminatoires**, note ramenée à 0. **Aucun verbatim littéral** : tu as écrit ce que tu penses que le client pense, précisément ce que la séance existe pour empêcher. **Les trois angles sont le même angle.** **Un maillon 2 faux, invérifiable, ou qui déborde sur une allégation que ta catégorie n'autorise pas** — risque juridique, pas faute de rédaction. **Des fréquences sans effectif** : « la majorité des clients disent que » sans le compte est une opinion déguisée. **Un angle construit sur un seul entretien**, sans vérification de fréquence.

---

## 7. Le corrigé exemplaire

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.

On reprend **KALIS**, la marque des corrigés de [S03](S03-produit-et-cogs.md) et [S04](S04-offre-prix-et-panier.md) : chaussettes de course techniques, COGS 2,77 € HT la paire, paire seule 18,00 € TTC, pack de 3 à 45,00 €, pack de 6 à 78,00 €, AOV cible **57,48 € TTC**, marge brute **28,87 € HT par commande** (60,3 %), MER seuil 2,11 pour un MER atteignable de 2,20, environ **1 000 commandes par mois** au lancement.

### 7.1 Le corpus

| Source | Volume | Extraction |
|---|---:|---:|
| Avis 1–2 étoiles, 6 concurrents directs, 18 mois | 214 | 58 verbatims |
| Avis 5 étoiles, mêmes concurrents | 206 | 41 verbatims |
| Questions et commentaires sous publicités et fiches, 30 jours | 63 | 17 verbatims |
| Fils de forum et groupes de club | 4 h | 9 verbatims |
| Entretiens : 2 acheteurs de la pré-série, 3 acheteurs de concurrents | 5 × 25 min | 12 verbatims |
| **Total** | **488 pièces** | **137 verbatims codés** |

Temps réel : 7 h 40, dont 5 h 10 de dépouillement. Indemnités : 5 × 30 € = **150 € TTC**.

### 7.2 Le tableau des thèmes

Un verbatim peut porter deux thèmes : le total des occurrences (174) dépasse le nombre de verbatims (137).

| Thème | Occ. | % des 137 | Intensité | **Score** | Acte « oui » |
|---|---:|---:|---:|---:|---:|
| T1 — Ampoule ou brûlure en sortie longue | 41 | 29,9 % | 2,7 | **110,7** | 78 % |
| T2 — Trou prématuré au gros orteil ou au talon | 31 | 22,6 % | 2,1 | **65,1** | 61 % |
| T3 — Perte de maintien après lavages, « ça tirebouchonne » | 22 | 16,1 % | 2,3 | **50,6** | 55 % |
| T4 — Prix jugé indéfendable pour une chaussette | 26 | 19,0 % | 1,6 | **41,6** | 12 % |
| T5 — Taille incohérente d'un modèle à l'autre | 18 | 13,1 % | 1,8 | 32,4 | 39 % |
| T8 — Compression qui marque la cheville | 12 | 8,8 % | 2,4 | 28,8 | 58 % |
| T6 — Couture qui blesse l'orteil | 9 | 6,6 % | 2,6 | 23,4 | 89 % |
| T7 — Odeur | 15 | 10,9 % | 1,4 | 21,0 | 20 % |

**Deux lectures qu'un classement par fréquence seule aurait ratées.** T6 n'a que 9 occurrences mais 2,6 d'intensité et **89 % d'actes** : ceux qui en parlent ont changé de marque. Trop rare pour porter le premier lot, il part en réserve pour le troisième. T7 a plus d'occurrences que T6 et ne mérite rien — intensité 1,4, 20 % d'actes : **les gens en parlent, ils n'en font rien.**

**Étape 2 du § 4.4 appliquée.** T2 et T3 se laissent couvrir par la même phrase de mécanisme : la chaussette perce **parce qu'**elle glisse, et elle glisse parce que sa reprise élastique est morte. Deux symptômes, une cause, donc **un seul angle**. Les trois angles de KALIS seront T1 (niveau 2), T2+T3 fusionnés (niveau 3) et T4 (niveau 4).

### 7.3 Les trois écarts de croyance

| | **Écart 1 — T1** | **Écart 2 — T2+T3** | **Écart 3 — T4** |
|---|---|---|---|
| Croyance dominante | *« l'ampoule vient du frottement de la chaussure »* — 33 des 41 verbatims, 80 % | *« elles sont trouées parce que mes ongles sont durs »* — 24 des 53, 45 % | *« une chaussette, c'est une chaussette »* — 26 verbatims, dont 19 comparent au supermarché |
| Mauvais indicateur | La pointure, la vaseline | L'épaisseur du tissu au toucher | Le prix à la paire |
| Bon indicateur | « Au bout d'une heure, est-elle sèche, et a-t-elle bougé ? » | La reprise élastique **après 30 lavages** | Le coût par sortie sur douze mois |
| Ce que la correction change | Il faut une paire sèche par sortie : **le pack de 3, pas la paire** | Justifie le prix, l'instruction de lavage, et une garantie en kilomètres | Rend le pack de 6 rationnel, déplace la comparaison vers le coût du problème |
| Source du mécanisme | Podologie du sport, validée par le praticien qui caution l'angle | Mesure de reprise, protocole publié ; abrasion en laboratoire | Le calcul, vérifiable ligne à ligne |

### 7.4 Fiche d'angle 1 — « Ce n'est pas ta chaussure »

**T1** · 41 occurrences · intensité 2,7 · score 110,7 · **niveau 2** · vidéo explicative UGC 45 s · destination page longue *problème → mécanisme → pack de 3* · nCAC relatif ×2,0 à ×2,5.

**Verbatims sources.** V014 (avis 2★, 12/03) : *« à 25 km j'ai senti la brûlure, à 30 j'avais une cloque sous l'avant-pied, j'ai fini en marchant »*. V027 (forum, 04/02) : *« je mets de la vaseline et je prends une demi-taille au-dessus, ça marche une fois sur deux »*. V103 (entretien 1) : *« je me suis dit que les ampoules, c'était le prix à payer pour le marathon »*.

```
1. PROBLÈME     « À 25 km j'ai senti la brûlure, à 30 j'avais une cloque sous
                l'avant-pied, j'ai fini en marchant. » Et tu as fait ce que tout le
                monde fait : de la vaseline, et une demi-taille au-dessus.
2. MÉCANISME    (a) Ce n'est pas ta chaussure. (b) Une ampoule n'est pas une brûlure
   DU PROBLÈME  de surface : c'est un décollement entre deux couches de ta peau,
                provoqué par un cisaillement répété — et l'humidité augmente le
                frottement de la peau, donc le cisaillement transmis. Une chaussette
                chargée d'eau glisse et transmet ce cisaillement à chaque foulée.
                (c) Le bon indicateur n'est pas ta pointure : c'est « au bout d'une
                heure, est-elle encore sèche, et a-t-elle bougé ? »
3. MÉCANISME    KALIS traite les deux termes du mécanisme, pas un seul : une maille
   DE LA        qui reste sèche — 9 g d'eau reprise après 20 km contre 38 g pour du
   SOLUTION     coton — et un maintien qui l'empêche de bouger, bord-côte et arche
                tricotés en densité différenciée. Sèche et immobile : le cisaillement
                n'a plus de support. Et comme il en faut une sèche par sortie, la
                bonne unité d'achat est le pack de trois.
4. PREUVE       La pesée, le podologue, la garantie — détail ci-dessous.
```

| # | Preuve | Rang | Source vérifiable | Coût pour un menteur |
|---|---|---:|---|---|
| 1 | Pesée avant/après 20 km, +9 g contre +38 g | **6** | Vidéo non coupée, protocole écrit publié | Faible s'il triche au montage — d'où « sans coupe » |
| 2 | Caution d'un podologue du sport nommé | **7** | Nom, cabinet, rémunération déclarée | Il engage sa réputation professionnelle |
| 3 | Garantie « une ampoule = remboursé », 60 j | **9** | À l'usage, immédiatement | **Un produit qui ne marche pas ne peut pas la payer** |

| Objection | Verbatim | Ce que KALIS écrit |
|---|---|---|
| C'est cher | *« 18 € une paire de chaussettes, il faut le vouloir »* | « 15,00 € la paire en pack de trois, sur 600 km garantis : dix centimes de plus par sortie. » |
| Ça marche ? | *« pourtant elles sont annoncées anti-ampoules »* | « On ne dit pas anti-ampoules. On dit sèche et immobile, et on montre la pesée. » |
| Pas pour moi | *« moi c'est surtout au talon »* | Quatre témoignages, quatre zones, quatre distances. |
| Pas le temps | *« je n'ai pas envie de me tartiner avant chaque sortie »* | « Plus de gel, plus de pansement préventif. Tu enfiles, tu pars. » |
| Et si ça rate | *« j'ai déjà acheté trois marques soi-disant techniques »* | Garantie 60 jours sans retour, annoncée **après** le mécanisme. |
| Qui êtes-vous | *« marque inconnue, fabriquée où ? »* | Atelier nommé, pays, numéro de lot sur l'emballage, SAV téléphonique. |

**Hooks.** *Visuel :* deux chaussettes sur une balance de cuisine après la même sortie, 9 g contre 38 g, sans commentaire pendant deux secondes. *Parlé :* « Si tu as une ampoule à 25 km, ce n'est pas ta chaussure. » *Écrit :* « Ta pointure n'a rien à voir avec tes ampoules. » — **Jamais :** « prévient les ampoules » sans réserve ; toute formulation à connotation médicale ; « recommandé par les podologues » au pluriel quand un seul praticien est engagé.

### 7.5 Fiche d'angle 2 — « Le trou n'est pas une question de qualité »

**T2 + T3** · 53 occurrences · intensité 2,2 · score 115,7 · **niveau 3** · comparatif filmé 30 s · destination page produit avec bloc comparatif · nCAC relatif ×1,6 à ×2,0.

**Verbatims sources.** V008 (avis 2★, 21/01) : *« trouées au gros orteil au bout de deux mois, à raison de trois sorties par semaine »*. V061 (forum, 09/03) : *« au bout d'une vingtaine de lavages elles tirebouchonnent et glissent dans la chaussure »*. V119 (entretien 4) : *« c'est mon podologue qui m'a dit d'arrêter le coton »*.

```
1. PROBLÈME     « Trouées au gros orteil au bout de deux mois, à trois sorties par
                semaine. » Tu en as conclu que c'était de la mauvaise qualité, ou
                que tes ongles étaient en cause.
2. MÉCANISME    (a) Le trou n'est pas la cause, c'est la fin de l'histoire.
   DU PROBLÈME  (b) Ce qui meurt en premier, c'est la reprise élastique du bord-côte :
                l'adoucissant et le sèche-linge la détruisent en une vingtaine de
                lavages. Sans reprise, la chaussette descend, coulisse sur l'orteil à
                chaque foulée, et l'abrasion se concentre sur deux centimètres carrés.
                (c) L'indicateur n'est pas l'épaisseur que tu tâtes en magasin :
                c'est la reprise du bord-côte après trente lavages.
3. MÉCANISME    KALIS tricote bord-côte et arche en densité différenciée, sur un fil
   DE LA        dont la reprise est mesurée à 0, 10, 20 et 30 lavages — courbe publiée
   SOLUTION     avec celle de trois modèles concurrents anonymisés. Le maintien tient,
                la chaussette ne coulisse pas, l'abrasion se répartit. Et l'étiquette
                dit ce qui la tue : adoucissant, sèche-linge.
4. PREUVE       Laboratoire, courbe de reprise, garantie 600 km — détail ci-dessous.
```

| # | Preuve | Rang | Source vérifiable | Coût pour un menteur |
|---|---|---:|---|---|
| 1 | Test d'abrasion en laboratoire indépendant | **8** | Rapport téléchargeable par numéro de lot | Même prix — **et le résultat peut être mauvais** |
| 2 | Courbe de reprise sur 30 lavages, 4 modèles | **6** | Protocole publié, modèles achetés en boutique | Reproductible par quiconque, donc coûteux à truquer |
| 3 | Garantie 600 km ou 6 mois | **9** | À l'usage | Proportionnel au mensonge |

| Objection | Verbatim | Ce que KALIS écrit |
|---|---|---|
| C'est cher | *« à ce prix-là elles ont intérêt à durer »* | « Elles durent 600 km, c'est dans la garantie. Sinon on remplace. » |
| Ça marche ? | *« toutes les marques disent renforcé au talon »* | « Renforcé ne veut rien dire. Voici la courbe, et celle de trois concurrents. » |
| Pas pour moi | *« je cours sur route, pas en trail »* | Deux courbes d'usure, route et sentier, même modèle. |
| Pas le temps | *« je ne vais pas laver mes chaussettes à la main »* | « 30°, sans adoucissant, sans sèche-linge. C'est tout, et c'est sur l'étiquette. » |
| Et si ça rate | *« j'en ai eu des soi-disant increvables »* | Remplacement sans retour ni justificatif, six mois. |
| Qui êtes-vous | *« encore une marque de plus »* | Le rapport de laboratoire est signé et daté par un tiers nommé. |

**Hooks.** *Visuel :* la même chaussette après 0, 10, 20 et 30 lavages, posée à plat, l'écart de bord-côte visible à l'œil. *Parlé :* « Ta chaussette ne perce pas parce qu'elle est fine. Elle perce parce qu'elle glisse. » *Écrit :* « Ce qui tue une chaussette technique, c'est ton adoucissant. » — **Jamais :** « indestructible », « à vie » ; une durée de vie non adossée au protocole publié ; un comparatif nommant un concurrent — modèles anonymisés, achetés en boutique, facture conservée.

### 7.6 Fiche d'angle 3 — « Dix centimes par sortie »

**T4** · 26 occurrences · intensité 1,6 · score 41,6 · **niveau 4** · carrousel de preuve, 5 volets · destination page produit courte, pack de 6 · nCAC relatif ×1,2 à ×1,5.

**Verbatims sources.** V046 (commentaire sous publicité, 27/02) : *« 18 € une paire de chaussettes, il faut le vouloir »*. V052 (avis 1★) : *« pour ce prix j'ai cinq paires en supermarché »*. V131 (entretien 3, justification sociale) : *« je l'ai expliqué à ma femme en disant que c'était moins cher qu'une séance de kiné »*.

```
1. PROBLÈME     « Pour ce prix j'ai cinq paires en supermarché. » C'est exact, et
                c'est la bonne objection.
2. MÉCANISME    (a) Ce n'est pas le prix qui cloche, c'est le dénominateur.
   DU PROBLÈME  (b) Tu compares un prix d'achat à un prix d'achat, alors que l'unité
                réelle de la catégorie est la sortie effectuée : cinq paires de coton
                tiennent environ quatre mois à trois sorties par semaine, et il en
                faut trois lots par an. (c) Le bon indicateur n'est pas le prix à la
                paire, c'est le coût par sortie sur douze mois.
3. MÉCANISME    Pack de 3 à 45,00 € TTC, 600 km garantis par paire, soit ~45 semaines
   DE LA        de rotation à 40 km par semaine : 52,00 € TTC sur douze mois, contre
   SOLUTION     36,00 € TTC pour trois lots de cinq paires de coton. Écart : 16,00 €
                par an, 0,31 € par semaine, 0,10 € par sortie. Dix centimes par
                sortie, et l'ampoule en moins.
4. PREUVE       Le calcul n'est pas une preuve, c'est un recadrage. Ce qui le rend
                vrai, c'est la durée de vie — détail ci-dessous.
```

| # | Preuve | Rang | Source vérifiable | Coût pour un menteur |
|---|---|---:|---|---|
| 1 | Rapport d'abrasion, qui soutient les 600 km du calcul | **8** | Par numéro de lot | Le résultat peut être mauvais |
| 2 | Avis vérifiés en volume, filtrés sur le mot « durée » | **3** | Plateforme d'avis tierce | Peu cher — **et délictuel** |
| 3 | Garantie 600 km | **9** | À l'usage | Proportionnel au mensonge |

| Objection | Verbatim | Ce que KALIS écrit |
|---|---|---|
| C'est cher | *« pour ce prix j'ai cinq paires en supermarché »* | Le calcul ligne à ligne, hypothèses affichées : 0,10 € de plus par sortie. |
| Ça marche ? | *« la durée annoncée, c'est du marketing »* | « 600 km garantis contractuellement. Garanti n'est pas annoncé. » |
| Pas pour moi | *« je cours 10 km par semaine, pas 40 »* | « À 10 km par semaine une paire tient plus de deux ans : l'écart annuel tombe sous 5 €. » |
| Pas le temps | *« je ne vais pas calculer le prix de mes chaussettes »* | Le carrousel fait le calcul, trois volets, hypothèses en bas. |
| Et si ça rate | *« et si elles ne durent pas 600 km »* | « On remplace. C'est le seul cas où la garantie nous coûte, et c'est le but. » |
| Qui êtes-vous | *« jamais entendu parler »* | Volet 5 : lot, atelier, SAV, date de création, commandes livrées. |

**Hooks.** *Visuel :* deux tas — cinq paires de coton, trois paires KALIS — et un seul chiffre entre les deux : 0,10 €. *Parlé :* « Cinq paires à 12 €, ou trois à 45. Fais le calcul sur l'année, il tient en trois lignes. » *Écrit :* « Dix centimes de plus par sortie. C'est tout l'écart. » — **Jamais :** un prix barré permanent ; « économisez X € » sans afficher les hypothèses ; la comparaison à une séance de kinésithérapie en communication publique — c'est la justification sociale d'un client en entretien, pas une allégation que la marque peut porter.

### 7.7 Le contrôle final

Trois niveaux de conscience : 2, 3, 4. Aucune phrase de maillon 2 ne couvre les trois — cisaillement, reprise élastique et dénominateur sont trois mécanismes disjoints. Chaque angle vend un **panier** : l'angle 1 le pack de 3 par le besoin d'une paire sèche par sortie, l'angle 3 le pack de 6 par le coût par sortie. Et les trois convergent sur la même garantie, ce qui n'est pas un hasard : c'est la seule preuve dont le coût est proportionnel au mensonge.

**Ce qu'elle coûte, calculé avant de la promettre.** Marge brute 28,87 € par commande ; coûts engagés non récupérés sur un remboursement : COGS mixte 11,30 € + logistique 5,20 € + paiement 1,23 € = 17,73 €, soit **46,60 € de perte par commande remboursée**. *Hypothèse :* +6 % de conversion en relatif, +1,5 point de réclamations.

```
Gain = 1 000 × 6 % × 28,87 €                      = 1 732 € / mois
Coût = 1 060 × 1,5 % × 46,60 €                    =   741 € / mois
Net                                                = + 991 € / mois
Réclamation d'équilibre = 1 732 ÷ (1 060 × 46,60) =  3,51 %
```

**Tant que la garantie n'ajoute pas plus de 3,51 points de remboursements, elle est rentable.** Ce nombre s'écrit avant le lancement, pas après.

---

## 8. Les conséquences chiffrées de ton choix

### 8.1 L'écart de CAC, déclaré comme un ordre de grandeur

*Hypothèse H1, ordre de grandeur déclaré et non mesuré :* **un angle écrit sans matériau client coûte 25 % de nCAC de plus** qu'un angle issu d'un corpus, à produit, prix, budget et compte publicitaire identiques.

D'où il sort et pourquoi il est prudent : [E04](../modules/E04-psychologie-du-client.md) § 2.3 chiffre le cas extrême — parler produit à une audience froide — à **×2,25 sur le nCAC**, par une chaîne mesurable (rétention à 3 secondes de 12 % contre 27 %, taux de clic identique parmi les retenus). Le cas courant n'est pas celui-là : un angle inventé par quelqu'un qui connaît sa catégorie est plausible, vise à peu près le bon niveau de conscience, et rate le mécanisme. **+25 % est une borne basse, pas une prévision.** Refais tout ce qui suit avec +15 % : aucune conclusion ne change de signe, seule la date change.

### 8.2 Deux trajectoires chez KALIS, à douze mois

Mêmes 1 000 commandes par mois, même offre, même MER visé de 2,20. *Hypothèses locales :* frais fixes 4 500 € par mois, trésorerie de lancement 45 000 €.

```
B — angle issu du corpus
  Publicité par commande = 57,48 ÷ 2,20        = 26,13 €
  Marge brute par commande (S04 § 7.3)         = 28,87 €
  CM3 par commande                             = + 2,74 €
A — angle inventé, nCAC + 25 %
  Publicité par commande = 26,13 × 1,25        = 32,66 €
  MER effectif = 57,48 ÷ 32,66                 =   1,76
  CM3 par commande                             = − 3,79 €
```

| | **A — angle inventé** | **B — angle issu du corpus** |
|---|---:|---:|
| MER effectif | 1,76 | 2,20 |
| MER seuil CM3 = 0 (S04 § 7.3) | 2,11 | 2,11 |
| Position | **sous la ligne de flottaison** | au-dessus |
| CM3 mensuelle, 1 000 commandes | −3 790 € | +2 740 € |
| EBITDA mensuel | **−8 290 €** | **−1 760 €** |
| EBITDA sur 12 mois | **−99 480 €** | **−21 120 €** |
| Trésorerie épuisée en | **5,4 mois** | 25,6 mois |
| Commandes nécessaires pour l'équilibre | **aucune quantité ne suffit** | 1 642 par mois |

**Écart sur douze mois : 78 360 €**, pour le même produit, le même prix et le même budget publicitaire. Mais la ligne qui compte est la dernière. B a un chemin — 1 642 commandes par mois, soit +64 % de volume, c'est-à-dire un objectif de travail. **A n'en a aucun : sa contribution par commande est négative, donc chaque commande supplémentaire creuse la perte.** Et A ne se voit pas dans les interfaces : le taux de conversion du site est identique dans les deux cas, puisque c'est le même site. Seuls le coût du clic et le coût par achat montent — ce qu'un fondateur attribue neuf fois sur dix à « la concurrence » ou à « l'algorithme ».

### 8.3 Le même écart au palier P5, par le MER

Chez NØRA, la dépense publicitaire canonique est de **1 494 206 € par mois** pour un nCAC de **40,03 €** et 37 324 nouveaux clients : 40,03 × 37 324 = 1 494 080 €, soit la quasi-totalité de la ligne publicitaire ([canoniques § 2.2 et § 2.4](../donnees/chiffres-canoniques.md)). À volume de clients constant, un nCAC dégradé se paie directement en publicité.

| Dégradation du nCAC | Publicité annuelle en plus | EBITDA annuel | MER résultant |
|---|---:|---:|---:|
| Référence | — | **4 377 023 €** | 2,90 |
| +10 % | 1 793 047 € | 2 583 976 € | 2,64 |
| +15 % | 2 689 571 € | 1 687 452 € | 2,52 |
| **+24,4 %** | **4 377 023 €** | **0 €** | **2,33** |
| +25 % | 4 482 618 € | −105 595 € | 2,32 |
| +35 % | 6 275 665 € | −1 898 642 € | 2,15 |

Deux vérifications donnent sa solidité au tableau. **Un.** La ligne +10 % vaut 1 494 206 × 0,10 × 12 = 1 793 047 €, exactement le levier « −10 % de CAC » des [canoniques § 7](../donnees/chiffres-canoniques.md) : le calcul est symétrique et retombe à l'euro. **Deux.** Le point d'annulation, 364 752 ÷ 1 494 206 = **24,41 %**, est le même nombre que la colonne « écart au seuil EBITDA » de P5 des [canoniques § 2.3](../donnees/chiffres-canoniques.md), **24,4 %**. Ce n'est pas une coïncidence : les deux mesurent la même distance à la ligne de flottaison, l'une en pourcentage de CAC, l'autre en MER.

**Traduction.** Une entreprise à 52 M€ TTC par an, 38 personnes, un produit qui marche, passe de 4,4 M€ d'EBITDA à zéro pour **un quart de coût d'acquisition en plus**. Aucune ligne du compte de résultat n'a bougé : ni le prix, ni le COGS, ni la logistique, ni les frais fixes. Seul le message a changé.

### 8.4 Ce que la recherche a coûté

7 h 40 de temps fondateur (*hypothèse :* 45 € HT de coût complet par heure) = 345 € HT, plus 150 € TTC d'indemnités, plus zéro euro d'outil : **environ 470 € TTC**. Rapporté aux 78 360 € d'écart à douze mois chez KALIS, le rendement est de **×167** — et il est sous-estimé. Le corpus resservira en [S06](S06-premier-lot-de-creas.md) pour douze accroches, en [S07](S07-le-site.md) pour la page produit, en [S10](S10-installer-la-retention.md) pour les objets de courriel. Les six objections traitées réduisent le volume de tickets SAV. Et le maillon 2 ne se périme pas : c'est le seul actif de cette séance qui vaudra encore quelque chose dans cinq ans.

> **À retenir :** un angle n'est pas une idée, c'est un écart de croyance vérifié par comptage. Le prix d'un angle inventé ne se paie pas en créativité perdue mais en pourcentage de coût d'acquisition — et à l'échelle, un quart de CAC vaut la totalité de l'EBITDA.

---

## 9. Avant la séance suivante

1. **Termine ton corpus jusqu'au plancher.** À 180 avis négatifs ou 4 entretiens, tu n'as pas fini : c'est précisément la marge où les fréquences deviennent lisibles.
2. **Vérifie tes trois fréquences sur 100 avis que tu n'as pas codés**, pris chez un septième concurrent et codés à l'aveugle. Un écart de plus de 5 points sur ton thème principal signale un corpus biaisé — souvent une seule marque surreprésentée.
3. **Fais relire ton maillon 2 par quelqu'un qui connaît la technique** — fabricant, praticien, ingénieur produit. Une seule question : « est-ce que c'est vrai ? » Si la réponse est « en gros », ce n'est pas oui.
4. **Prépare l'entrée de [S06](S06-premier-lot-de-creas.md)** : pour chaque angle, liste les preuves que tu peux produire dans les trois semaines et celles qui demandent un budget ou un délai. C'est cette liste qui décidera de tes douze concepts.

---

*Fin de la séance S05. Suite : [S06 — Le premier lot de créas](S06-premier-lot-de-creas.md), où ces trois angles deviennent douze concepts — et où tu découvriras que douze n'est pas une bibliothèque, mais six jours de production au rythme du palier P2.*
