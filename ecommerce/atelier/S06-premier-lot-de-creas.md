# Séance S06 — Le premier lot de créas

> **Niveau requis :** L03 · **Durée :** 10 h (dont 3 h d'écriture pure) · **Livrable :** douze concepts prêts à tourner — matrice, douze accroches rédigées, trois scripts complets, douze briefs, plan et budget de production, droits d'usage, registre ouvert · **Modules :** [E05](../modules/E05-machine-creative.md), [E04](../modules/E04-psychologie-du-client.md)
> **Ce que tu ne peux pas faire sans avoir fait cette séance :** ouvrir un compte publicitaire. Avec trois créas, tu ne testes rien : tu paies pour découvrir que tu n'avais pas assez de matière, et tu attribues à l'algorithme ce qui est un défaut de stock.

---

## 1. Où tu en es

Tu sors de [S05](S05-recherche-client-et-angles.md) avec trois fiches d'angle : trois écarts de croyance, trois chaînes de croyance rédigées, neuf preuves hiérarchisées, dix-huit objections traitées, trois niveaux de conscience.

**Décidé :** ce que tu dis, à qui, et pourquoi c'est vrai. **Pas décidé :** sous quelle forme, en quelle quantité, à quel coût, avec quels droits, et selon quel calendrier.

La quantité est le sujet réel de cette séance, et c'est celui que tout le monde sous-estime. Les [chiffres canoniques § 6](../donnees/chiffres-canoniques.md) donnent le rythme d'une marque à chaque palier : **14 concepts nouveaux par semaine** à P2, **38** à P3, **57** à P5 — dont 5,2 seulement survivent. Ce n'est ni le produit, ni le budget, ni l'algorithme qui plafonne une marque à l'échelle : c'est la capacité à produire et à juger ce flux. La [Porte P2 → P3](../mentorat/jalons.md) en fait une condition binaire, la seule qui soit un **rythme** et non un résultat : au moins 10 concepts nouveaux par semaine, tenus huit semaines.

*Acronymes : **UGC** — contenu tourné par un client ou un créateur, pas par un studio. **CPA** — coût par achat. **CPM** — coût pour mille impressions. **CM3** — marge après coûts variables et publicité. **Concept** — une idée testable ; **variation** — la même idée avec une accroche, une musique ou un cadrage différents.*

---

## 2. Ta mission

Produire **douze concepts prêts à tourner**. « Prêts à tourner » veut dire : quelqu'un d'autre que toi peut les produire sans te poser de question.

1. **La matrice** angle × format × preuve, douze cellules remplies, chacune avec sa preuve et son niveau de conscience.
2. **Douze accroches rédigées mot pour mot** — pas des intentions d'accroche. Plus, pour ton angle principal, **une accroche par famille**, soit huit, dont les non retenues partent au registre.
3. **Trois scripts complets**, segment par segment, avec les durées : un par angle, dans trois formats différents.
4. **Douze briefs créatifs remplis**, sur le modèle du dépôt.
5. **Le plan de production** : source choisie par concept, calendrier, budget chiffré en euros HT, droits d'usage écrits.
6. **La convention de nommage et le registre ouvert**, avec les douze lignes créées.

---

## 3. Ce dont tu disposes

| Ressource | Usage |
|---|---|
| Ton livrable [S05](S05-recherche-client-et-angles.md) | Les trois angles, les neuf preuves, les verbatims — **matière première unique de cette séance** |
| Ton livrable [S04](S04-offre-prix-et-panier.md) | Le panier que la créa doit vendre, et le MER à tenir |
| [`modeles/brief-creatif.md`](../modeles/brief-creatif.md) | Le brief à copier douze fois |
| [`modeles/protocole-test-creatif.md`](../modeles/protocole-test-creatif.md) | Les seuils de décision, **écrits avant le test** |
| [canoniques § 6](../donnees/chiffres-canoniques.md) | Le rythme par palier, le budget de test, le taux de réussite |
| [E04](../modules/E04-psychologie-du-client.md) § 5 | La hiérarchie des preuves, et les 80 à 250 € d'une vidéo UGC |
| `python3 ecommerce/outils/plan_objectif.py` | Traduit ton objectif en concepts par semaine (`--budget-concept`, `--taux-reussite`, `--variations`, `--duree-vie`) |
| `python3 ecommerce/outils/test_significativite.py --creatif` | Combien il faut dépenser sur un concept **avant** d'avoir le droit de le juger |

---

## 4. La méthode, pas à pas

### 4.1 La matrice angle × format × preuve

Douze concepts ne s'inventent pas : ils se **génèrent**. Trois angles × quatre formats = douze cellules, et chaque cellule reçoit une preuve distincte prise dans la fiche d'angle correspondante.

Les quatre formats, choisis parce qu'ils sollicitent des mécanismes de preuve différents :

| Format | Ce qu'il fait mieux que les autres | Ce qu'il ne sait pas faire |
|---|---|---|
| **F1 — UGC témoignage face caméra** | Porter une scène et une justification sociale ; couvrir l'objection « pas pour moi » par le profil | Démontrer un mécanisme : une personne qui affirme ne prouve rien |
| **F2 — Démonstration filmée** | Montrer le mécanisme et la preuve de rang 6 ; se passer de mots | Porter un récit ; tenir au-delà de 30 secondes |
| **F3 — Statique ou carrousel** | Poser un chiffre vérifiable, un calcul, un comparatif ; se lire sans son ni patience | Créer de l'émotion, servir une audience froide |
| **F4 — Récit natif, voix off et b-roll** | Dérouler les quatre maillons en entier ; servir le niveau de conscience 1 ou 2 | Convertir vite : c'est le format le plus long à rentabiliser |

**Trois règles de remplissage.** *Une preuve par cellule*, jamais deux fois la même dans le même lot — sinon tu ne testes plus la preuve, tu testes le montage. *Deux cellules ne partagent jamais le couple (famille d'accroche, preuve)* : c'est ce qui garantit que ce sont douze concepts et non douze variations. *Chaque cellule doit être tournable dans les trois semaines* avec ce que tu as réellement — c'est la liste que [S05](S05-recherche-client-et-angles.md) § 9 t'a fait écrire ; une cellule qui exige une étude à 30 000 € n'entre pas dans le premier lot, elle entre au registre avec sa date.

**Concept ou variation ?** Un concept change le **mécanisme exposé** ou la **preuve apportée**. Une variation change l'accroche, la musique, le cadrage, la voix, la première seconde. Les deux sont utiles, mais ils ne se comptent pas ensemble : la [Porte P1 → P2](../mentorat/jalons.md) exige deux gagnants **distincts**, et deux variations d'un même concept comptent pour un. C'est aussi la raison pour laquelle un compte qui ne vit que de variations décroche d'un coup : quand le concept-mère fatigue, ses douze variations fatiguent le même jour.

La matrice vierge, à copier :

| # | Angle | Niveau | Format | Preuve mobilisée | Famille d'accroche | Durée | Tournable en 3 sem. |
|---|---|---|---|---|---|---|---|
| C01 | | | | | | | |
| … | | | | | | | |
| C12 | | | | | | | |

### 4.2 Les huit familles d'accroches

L'accroche n'est pas l'angle : c'est sa porte d'entrée. Elle a trois secondes, et son seul travail est d'acheter les huit suivantes. Voici les huit familles, chacune avec une accroche **rédigée** pour l'angle NØRA d'[E04](../modules/E04-psychologie-du-client.md) § 7.5 — la queue de cheval qui s'amincit sans que la chute augmente.

| # | Famille | Mécanisme | Accroche rédigée (NØRA) | Contrainte |
|---|---|---|---|---|
| 1 | **La négation de la croyance** | Contredit frontalement ce que le corpus croit | « Ce n'est pas ta chute de cheveux, le problème. » | Il faut que la croyance soit réellement majoritaire, comptée en [S05](S05-recherche-client-et-angles.md) |
| 2 | **La question de diagnostic** | Fait s'auto-tester le spectateur en deux secondes | « Ton élastique fait-il encore le même nombre de tours qu'il y a cinq ans ? » | Une seule question, fermée, vérifiable dans l'instant |
| 3 | **Le mauvais indicateur** | Nomme la mesure que la personne suit, et la disqualifie | « Compter les cheveux sur l'oreiller est le mauvais indicateur. » | Doit être suivie du bon indicateur dans les cinq secondes |
| 4 | **La scène, au verbatim** | Rejoue le maillon 1 tel qu'il a été dit | « J'ai racheté le même élastique. Il fait deux tours de plus qu'avant. » | Verbatim du corpus, jamais reformulé |
| 5 | **L'erreur commune nommée** | Décrit un geste répandu et montre qu'il aggrave | « Un soin capillaire jugé en trois semaines est jugé sur un tiers de cycle. » | **Interdit d'inventer une fréquence** : « la plupart » sans source est une faute |
| 6 | **La démonstration muette** | Deux secondes d'image avant le premier mot | *Deux élastiques identiques, deux épaisseurs de queue de cheval, aucun commentaire.* | Le plan doit être lisible sur un écran de téléphone, sans texte |
| 7 | **Le chiffre vérifiable** | Un nombre **et sa source**, jamais un nombre seul | « 18 % d'actif, imprimé sur le flacon, analyse du lot par QR code. » | Un chiffre non sourcé est pire que pas de chiffre ([E04](../modules/E04-psychologie-du-client.md) § 5.1) |
| 8 | **La comparaison de dénominateur** | Change l'unité de comparaison du prix | « La cure, c'est 1,10 € par jour pendant trois mois. » | Le calcul doit être affiché, hypothèses comprises |

**Comment on choisit.** Tu écris **trois accroches pour chaque concept**, prises dans trois familles différentes, puis tu en gardes une avec quatre critères, dans cet ordre :

1. **Contient-elle le maillon 1 ou le maillon 2, et non le produit ?** Une accroche qui commence par le produit s'adresse au niveau de conscience 4 devant une audience de niveau 2. C'est l'erreur chiffrée à ×2,25 de nCAC par [E04](../modules/E04-psychologie-du-client.md) § 2.3.
2. **Tient-elle en trois secondes ?** Douze mots à l'oral, huit à l'écrit sur une image. Compte-les. Une accroche qu'il faut lire deux fois n'est pas lue une fois.
3. **La destination tient-elle la promesse ?** Si la page ne contient pas la réponse annoncée, tu paies un clic pour produire une déception. La continuité message → page est traitée en [S07](S07-le-site.md), mais elle se décide ici.
4. **Un concurrent pourrait-il l'écrire à l'identique, gratuitement, ce soir ?** Si oui, elle ne te sépare de rien. Les familles 6, 7 et 8 sont les plus résistantes à ce test, parce qu'elles demandent respectivement une démonstration, une source et un calcul.

**Les deux accroches non retenues ne se jettent pas** : elles vont au registre avec leur famille. Le jour où un concept gagne, elles sont ses deux premières variations — et tu les auras écrites à froid, avant de savoir laquelle gagne, donc sans le biais du succès.

### 4.3 Le script, segment par segment

Un script se compte en secondes, pas en paragraphes. Voici la structure d'un 45 secondes, qui est la forme longue du premier lot.

| Segment | Durée | Ce qu'il contient | Le mode d'échec |
|---|---:|---|---|
| **1. Accroche** | 0–3 s | La famille choisie au § 4.2, avec le maillon 1 ou 2 | Le logo, le nom de marque, le produit en main |
| **2. Le problème, dans ses mots** | 3–8 s | Le verbatim, joué ou dit tel quel | Le reformuler en langage de marque |
| **3. Le mécanisme du problème** | 8–18 s | Le maillon 2 : (a) ce n'est pas ce que tu crois, (b) ce qui se passe, (c) le bon indicateur | Le sauter — c'est le segment le plus coupé au montage, et le seul irremplaçable |
| **4. Le mécanisme de la solution** | 18–28 s | Le maillon 3, reprenant les termes du maillon 2 | La liste de caractéristiques produit |
| **5. La preuve** | 28–38 s | Une seule preuve, montrée et non affirmée | En empiler trois : au-delà d'une, la crédibilité baisse |
| **6. L'offre et l'appel à l'action** | 38–45 s | Le format acheté — le lot, la cure — et la destination nommée | « Lien en bio », « découvrez » : un appel sans objet |

Les deux autres durées du premier lot se déduisent de celle-ci, en supprimant des segments entiers et jamais en accélérant :

- **30 secondes** — segments 1, 3, 4, 5, 6 : on supprime le récit du problème, pas le mécanisme.
- **15 secondes** — segments 1, 3 compressé en une phrase, 6. Format réservé aux angles de niveau 4, où le mécanisme est déjà connu du spectateur.

**Cinq règles d'écriture, chacune avec sa raison.** Les **sous-titres sont obligatoires** et font partie du script — la vidéo sera vue sans le son. **Une seule idée par script** : deux mécanismes dans une même vidéo produisent deux publicités moyennes au lieu d'une bonne. **Le premier plan doit être tournable avec ce que tu as** — un script dont l'ouverture exige un drone ne sera pas tourné. **L'appel à l'action nomme la destination** et l'unité d'achat : « le pack de trois », pas « notre site ». Et **on écrit le script avant de choisir qui le tourne**, jamais l'inverse : un brief écrit après avoir trouvé un créateur épouse ce que le créateur sait faire.

### 4.4 Le brief créatif

Copie [`modeles/brief-creatif.md`](../modeles/brief-creatif.md), une fois par concept. Douze champs, et deux que presque personne ne remplit correctement.

**Les droits d'usage** — durée, périmètre, territoire, exclusivité. Un brief sans droits écrits produit une créa que tu ne peux légalement pas diffuser en publicité payante, ou que tu devras renégocier au pire moment (§ 4.5).

**La liste exacte des livrables** — les ratios attendus (9:16, 4:5, 1:1), la présence ou non des sous-titres incrustés, la livraison ou non des rushes bruts. Les rushes sont le champ le plus rentable du brief : ils permettent de produire trois variations sans retourner, donc de faire baisser le coût par asset — et c'est exactement le mécanisme qui fait passer le ratio d'assets par concept de 3,10 à 5,04 entre les paliers P2 et P5 ([canoniques § 6](../donnees/chiffres-canoniques.md), § 8.1 ci-dessous).

### 4.5 La production : trois sources, comparées

*Hypothèses de coûts : ordres de grandeur de marché, en euros HT par concept livré. La fourchette UGC vient d'[E04](../modules/E04-psychologie-du-client.md) § 5.*

| Source | Coût par concept | Délai | Variance de qualité | Droits | Rythme soutenable |
|---|---:|---|---|---|---|
| **Interne** — toi, un téléphone, un trépied, une fenêtre | 40 à 80 € (temps) | 1 à 2 j | Forte | Totaux, immédiats | 3 à 6 par semaine, puis ton temps s'épuise |
| **Créateur UGC** — plateforme ou direct | 80 à 250 € | 7 à 14 j | Moyenne, réductible par le brief | **À négocier — le point critique** | 10 à 40 par semaine dès qu'un vivier existe |
| **Studio ou agence** | 600 à 2 500 € | 3 à 6 semaines | Faible | Chers, souvent limités | 2 à 4 par mois : incompatible avec le rythme requis |

**Le calcul du budget du premier lot** se fait en cinq lignes, et il faut les cinq : production des concepts sources, déclinaisons (ratios et variantes d'accroche), majoration pour droits d'usage, média de test, et le temps interne de brief et de jugement. Les quatre premières se paient en euros ; la cinquième se paie en heures et c'est celle qui sature en premier.

**La négociation des droits d'usage.** Quatre dimensions se négocient séparément : la **durée** (3, 6, 12 mois, perpétuité), le **périmètre** (organique seul, publicité payante, diffusion depuis le compte du créateur), le **territoire**, l'**exclusivité** (interdiction de tourner pour un concurrent). Le forfait de base couvre presque toujours l'organique seul ; la publicité payante se paie 30 à 100 % de majoration.

La règle est contre-intuitive et elle est absolue : **achète douze mois de droits publicitaires dès le premier contrat, sur les douze concepts, avant de savoir lesquels gagnent.** Raison : renégocier après avoir trouvé un gagnant inverse le rapport de force. Un créateur dont la vidéo porte plusieurs milliers d'euros de dépense mensuelle ne renouvelle pas au tarif d'origine, et tu n'as pas d'alternative — le concept est devenu ton actif. Le § 8.4 chiffre l'écart. La majoration payée d'avance sur douze concepts coûte moins cher que la renégociation d'un seul.

### 4.6 Le nommage et le registre

Sans convention de nommage, tu ne sauras pas, à la trentième créa, quel concept a produit quel résultat. À 38 par semaine (palier P3), c'est déjà ingérable de mémoire ; c'est aussi la raison pour laquelle la condition 4 de la [Porte P2 → P3](../mentorat/jalons.md) — âge moyen des gagnants qui portent la dépense ≤ 8 semaines — est **mesurable ou non selon que tu as tenu ce registre**.

```
AAAAMMJJ_ANGLE_FORMAT_ACCROCHE_PREUVE_RATIO_vNN
20260907_A1-AMPOULE_F2-DEMO_H6-MUET_P-PESEE_9x16_v01
```

Le registre, une ligne par asset, treize colonnes : `id` · `date de mise en ligne` · `angle` · `format` · `famille d'accroche` · `preuve` · `source de production` · `coût HT` · `fin des droits` · `dépense de test` · `indicateur amont` (rétention à 3 s) · `CPA observé` · `décision et date`. La colonne **fin des droits** est celle qu'on oublie, et c'est la seule qui puisse te faire couper un gagnant du jour au lendemain.

---
## 5. Ton livrable

```
=====================================================================
LIVRABLE S06 — LE PREMIER LOT DE CRÉAS
Marque : ___________   Date : __/__/__   Temps passé : ____ h

A. LA MATRICE — douze cellules
| # | Angle | Niveau | Format | Preuve | Famille d'accroche | Durée | Tournable |
| C01 |  |  |  |  |  |  | O / N |
| … jusqu'à C12 |
Contrôle : aucune preuve utilisée deux fois ?            O / N
Contrôle : aucun couple (accroche, preuve) répété ?      O / N

B. LES DOUZE ACCROCHES, RÉDIGÉES MOT POUR MOT
C01 : « ______________________________________________ »  (famille __)
…
C12 : « ______________________________________________ »  (famille __)
LES HUIT FAMILLES SUR L'ANGLE PRINCIPAL — une accroche chacune
F1 négation ______  F2 question ______  F3 mauvais indicateur ______
F4 scène ______  F5 erreur commune ______  F6 démonstration muette ______
F7 chiffre vérifiable ______  F8 dénominateur ______
Retenue : ____   Au registre : ____ , ____

C. TROIS SCRIPTS COMPLETS — un par angle, trois formats différents
Pour chacun : segment | durée | image | voix ou texte | sous-titre
  1. Accroche            0–3 s
  2. Problème            3–8 s
  3. Mécanisme du problème  8–18 s
  4. Mécanisme de la solution  18–28 s
  5. Preuve              28–38 s
  6. Offre et appel à l'action  38–45 s
Contrôle : le maillon 2 occupe-t-il au moins 8 secondes ?    O / N
Contrôle : l'appel à l'action nomme-t-il l'unité d'achat ?   O / N

D. PRODUCTION
| Concept | Source | Coût HT | Délai | Droits (fin) | Livrables (ratios) |
Production des concepts sources ______ € HT
Déclinaisons ____ assets × ______ €                = ______ € HT
Majoration droits d'usage 12 mois                  = ______ € HT
Média de test ____ concepts × ______ €             = ______ € HT
Temps interne (brief + jugement) ____ h
TOTAL DU PREMIER LOT ______ € HT
Gagnants attendus = 12 × taux de réussite ____ %   = ______
Coût par gagnant attendu                           = ______ € HT

E. NOMMAGE ET REGISTRE
Convention retenue : ____________________________________
Registre ouvert le __/__/__ , ____ lignes créées
Colonnes présentes : id · date · angle · format · accroche · preuve ·
source · coût · FIN DES DROITS · dépense de test · rétention 3 s ·
CPA · décision et date
=====================================================================
```

---

## 6. La grille d'évaluation

Barème sur 100, **seuil de validation 72**. En dessous, tu ne lances pas : [S08](S08-le-lancement.md) construira un plan de lancement sur ces douze concepts, et un lot qui n'en contient que trois de réellement distincts produit un lancement qui s'éteint en trois semaines.

| # | Critère | Pts | Ce qui vaut les points | Ce qui les fait perdre |
|---|---|---:|---|---|
| 1 | Matrice complète | 10 | 12 cellules, angle, format, preuve et niveau renseignés | Cellule vide : −2 ; format unique sur les 12 : −6 |
| 2 | **Concepts réellement distincts** | 15 | Preuve différente par cellule, aucun couple (accroche, preuve) répété | 12 variations d'un même mécanisme : **éliminatoire** ; 2 cellules identiques : −5 |
| 3 | **Douze accroches rédigées** | 15 | Écrites mot pour mot, famille identifiée, ≤ 12 mots à l'oral | Accroche décrite au lieu d'être écrite : −3 chacune |
| 4 | Les huit familles travaillées | 8 | Une accroche par famille sur l'angle principal, les non retenues au registre | Familles non utilisées : −1 chacune |
| 5 | **Trois scripts complets** | 20 | Segments datés, image et voix séparées, sous-titres, appel à l'action nommant l'unité d'achat | Script sans durées : −7 ; **maillon 2 absent ou sous 5 s : −10 par script** |
| 6 | Briefs remplis | 8 | 12 briefs, dont droits et livrables exacts | Droits non écrits : **−8** ; ratios non précisés : −3 |
| 7 | Plan et budget de production | 12 | Trois sources comparées, coût par concept, budget total en € HT, calendrier | Budget non chiffré : **−12** ; une seule source envisagée : −5 |
| 8 | Droits d'usage négociés | 7 | Durée, périmètre, territoire, exclusivité, écrits par concept | Droits organiques seuls sur une créa destinée au payant : −7 |
| 9 | Nommage et registre | 5 | Convention appliquée aux 12, registre ouvert avec la colonne « fin des droits » | Registre sans date de fin des droits : −3 |

**Quatre fautes éliminatoires.** **Douze variations d'un seul concept** — tu n'as pas douze concepts, tu en as un, et la [Porte P1 → P2](../mentorat/jalons.md) le comptera comme tel. **Une accroche qui promet ce que la page ne contient pas** : tu achètes un clic pour produire une déception, et tu paieras deux fois. **Un concept sans preuve attachée** : c'est une affirmation, et une affirmation coûte le même prix à un menteur ([E04](../modules/E04-psychologie-du-client.md) § 5.1). **Un budget de production non chiffré** — sans lui, tu ne peux pas savoir combien de lots tu peux te payer avant d'avoir un gagnant, ce qui est la seule question de cette séance.

---

## 7. Le corrigé exemplaire

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.

**KALIS**, la marque des corrigés de [S03](S03-produit-et-cogs.md) à [S05](S05-recherche-client-et-angles.md) — chaussettes de course techniques. Ses trois angles, sortis de [S05](S05-recherche-client-et-angles.md) : **A1 « Ce n'est pas ta chaussure »** (niveau 2, cisaillement et humidité), **A2 « Le trou n'est pas une question de qualité »** (niveau 3, reprise élastique morte), **A3 « Dix centimes par sortie »** (niveau 4, dénominateur). Panier cible 57,48 € TTC, marge brute 28,87 € HT par commande, MER atteignable 2,20, environ 1 000 commandes par mois.

### 7.1 Les douze concepts, accroches rédigées

| # | Angle | Format | Preuve mobilisée | Famille | Durée | **Accroche, mot pour mot** |
|---|---|---|---|---|---|---|
| **C01** | A1 | F1 UGC | Témoignage + garantie | 4 — scène | 45 s | « J'ai fini mon premier semi en marchant, à cause d'une cloque. J'ai mis six mois à comprendre que ce n'était pas ma chaussure. » |
| **C02** | A1 | F2 démo | Pesée 9 g contre 38 g | 6 — muette | 30 s | *[2 s : deux chaussettes sur une balance de cuisine, aucun son]* puis « Même sortie. Même pointure. Deux chaussettes. » |
| **C03** | A1 | F3 statique | Caution du podologue | 1 — négation | — | « Ce n'est pas ta chaussure qui te donne des ampoules. » |
| **C04** | A1 | F4 natif | Mécanisme illustré + garantie | 3 — mauvais indicateur | 45 s | « Ta pointure est le mauvais indicateur. Le bon : au bout d'une heure, est-elle encore sèche ? » |
| **C05** | A2 | F1 UGC | Avis sur la durée + garantie | 2 — question | 30 s | « Combien de temps tiennent tes chaussettes avant le trou au gros orteil ? » |
| **C06** | A2 | F2 démo | Courbe de reprise, 0/10/20/30 lavages | 6 — muette | 30 s | *[2 s : quatre chaussettes à plat, alignées]* puis « Zéro, dix, vingt, trente lavages. Regarde le bord. » |
| **C07** | A2 | F3 carrousel | Rapport d'abrasion du laboratoire | 7 — chiffre vérifiable | — | « 600 km garantis. Rapport d'abrasion téléchargeable par numéro de lot. » |
| **C08** | A2 | F4 natif | Mécanisme du glissement | 1 — négation | 45 s | « Ta chaussette ne perce pas parce qu'elle est fine. Elle perce parce qu'elle glisse. » |
| **C09** | A3 | F1 UGC | Justification sociale | 4 — scène | 30 s | « Ma femme m'a demandé pourquoi 45 € de chaussettes. Je lui ai montré le calcul sur l'année. » |
| **C10** | A3 | F2 démo | Deux tas usés côte à côte | 8 — dénominateur | 15 s | « Cinq paires à 12 €, ou trois à 45. Sur l'année : dix centimes d'écart par sortie. » |
| **C11** | A3 | F3 carrousel | Le calcul + avis en volume | 7 — chiffre vérifiable | — | « 52,00 € contre 36,00 € sur douze mois. L'écart tient en trois lignes. » |
| **C12** | A3 | F4 natif | Garantie 600 km | 5 — erreur commune | 30 s | « On compare le prix à la paire. La bonne unité, c'est la sortie. » |

**Contrôles.** Neuf preuves distinctes réparties sur douze cellules, aucune utilisée plus de deux fois, jamais dans le même format. Aucun couple (famille d'accroche, preuve) répété. Quatre formats, trois niveaux de conscience, trois durées. Les douze sont tournables en trois semaines : la pesée et les lavages sont des démonstrations internes, le rapport de laboratoire est commandé et arrive à J+18, le podologue a signé.

### 7.2 Les huit familles sur l'angle A1, et la sélection

Les huit accroches écrites pour le concept C02, dont **une** sera retenue et deux versées au registre :

| Famille | Accroche écrite pour A1 |
|---|---|
| 1 — négation | « Ce n'est pas ta chaussure qui te donne des ampoules. » |
| 2 — question | « Tes chaussettes sont-elles encore sèches au bout d'une heure ? » |
| 3 — mauvais indicateur | « Ta pointure est le mauvais indicateur. » |
| 4 — scène | « À 25 km, la brûlure. À 30, la cloque. J'ai fini en marchant. » |
| 5 — erreur commune | « La vaseline et une demi-taille au-dessus : les deux gestes qui n'agissent sur rien. » |
| 6 — démonstration muette | *Deux chaussettes sur une balance, après la même sortie. Aucun mot pendant deux secondes.* |
| 7 — chiffre vérifiable | « 9 grammes d'eau après 20 km. 38 pour du coton. Protocole publié. » |
| 8 — dénominateur | « 15,00 € la paire, sur 600 km. Deux centimes et demi du kilomètre. » |

**Le choix, par les quatre critères du § 4.2.** La famille 6 est retenue pour C02. Critère 1 : elle montre le maillon 2 au lieu de l'énoncer — l'eau, donc le glissement, donc le cisaillement. Critère 2 : zéro mot pendant deux secondes, donc aucun risque de dépassement. Critère 3 : la page longue s'ouvre exactement sur la même pesée, la promesse est tenue à l'image près. Critère 4 : un concurrent qui voudrait la copier doit faire la pesée, et s'il la fait honnêtement avec du coton, il obtient le résultat de KALIS. **C'est la seule des huit dont la copie coûte quelque chose.**

Versées au registre pour les variations futures : la 3 (« ta pointure est le mauvais indicateur »), qui deviendra la variante d'ouverture de C02 si le concept gagne, et la 7, qui sert de version pour les audiences déjà exposées. La 5 est écartée pour une raison de fond : elle attaque un geste que le spectateur fait, ce qui produit une réaction de défense avant que le mécanisme ne soit posé.

### 7.3 Trois scripts complets

**Script C02 — A1 × démonstration — 30 secondes — format 9:16, sans musique**

| Segment | Durée | Image | Voix et texte |
|---|---:|---|---|
| Accroche | 0–3 s | Plan fixe serré : deux chaussettes posées sur une balance de cuisine, encore humides. Le chiffre change à l'écran : 47 g / 76 g | *Aucun son pendant 2 s.* Sous-titre : « Après la même sortie de 20 km. » |
| Mécanisme du problème | 3–13 s | Mains qui essorent la chaussette coton au-dessus d'un verre ; l'eau coule. Puis gros plan sur un pied qui glisse d'un centimètre dans la chaussure | « Une ampoule, ce n'est pas une brûlure de surface. C'est un décollement entre deux couches de ta peau, provoqué par un cisaillement. Et une chaussette gorgée d'eau glisse — donc elle transmet ce cisaillement à chaque foulée. » |
| Mécanisme de la solution | 13–22 s | Gros plan sur la maille KALIS, puis sur le bord-côte qui reprend sa forme après étirement | « Deux choses, pas une : une maille qui reste sèche — 9 grammes contre 38 — et un maintien qui l'empêche de bouger. Sèche et immobile : le cisaillement n'a plus de support. » |
| Preuve | 22–27 s | Retour sur la balance, plan large montrant qu'il n'y a pas eu de coupe : le protocole imprimé est posé à côté | « La pesée est filmée sans coupe, le protocole est publié. » |
| Offre et appel à l'action | 27–30 s | Le pack de trois, à plat | « Il en faut une sèche par sortie : c'est le pack de trois. Lien vers la page pack de 3. » |

*Note de production : le plan 3–13 s se tourne en une prise, en lumière du jour, avec un verre transparent. Rushes bruts exigés au brief pour produire les variations d'ouverture.*

**Script C04 — A1 × récit natif — 45 secondes — format 9:16, voix off**

| Segment | Durée | Image | Voix et texte |
|---|---:|---|---|
| Accroche | 0–3 s | Une main referme un tube de vaseline, en gros plan | « Ta pointure est le mauvais indicateur. » |
| Le problème | 3–8 s | B-roll : fin de course, quelqu'un s'assoit sur un trottoir et retire sa chaussure | « À 25 km la brûlure, à 30 la cloque, et on finit en marchant. » |
| Mécanisme du problème | 8–20 s | Animation simple à deux couches : la peau qui se décolle sous l'effet du glissement, puis la chaussette qui coulisse | « Ce n'est pas le frottement de la chaussure. L'ampoule est un décollement entre deux couches de ta peau, provoqué par un cisaillement répété — et l'humidité augmente le frottement de la peau, donc le cisaillement transmis. Une demi-taille au-dessus ne fait qu'augmenter le glissement. » |
| Le bon indicateur | 20–26 s | Chronomètre, puis main qui touche la chaussette au bout d'une heure | « Le bon indicateur n'est pas ta pointure : au bout d'une heure, est-elle encore sèche, et a-t-elle bougé ? » |
| Mécanisme de la solution | 26–35 s | Tricotage de la maille, bord-côte, arche | « Une maille qui reste sèche, un maintien qui l'empêche de bouger. Les deux, sinon ça ne sert à rien. » |
| Preuve | 35–41 s | Le podologue, à son cabinet, plan simple, nom et fonction en sous-titre | « Ce mécanisme, ce n'est pas nous qui l'inventons. » (le praticien explique en une phrase) |
| Offre et appel à l'action | 41–45 s | Pack de trois | « Une ampoule sur ta première sortie longue : remboursé, tu gardes la paire. Le pack de trois est sur la page. » |

*Note : la caution est en position 6 et non en position 1 — une preuve d'autorité placée avant le mécanisme fait entendre « croyez-moi » au lieu de « regardez ».*

**Script C11 — A3 × carrousel statique — 5 volets — format 4:5**

| Volet | Visuel | Texte, mot pour mot |
|---|---|---|
| 1 | Deux tas côte à côte : cinq paires de coton à gauche, trois paires KALIS à droite. Un seul chiffre entre les deux : **0,10 €** | « 52,00 € contre 36,00 € sur douze mois. L'écart tient en trois lignes. » |
| 2 | Le calcul, en trois lignes, police unique | « Pack de 3 à 45,00 € TTC · 600 km garantis par paire · 40 km par semaine = 45 semaines de rotation. Sur 12 mois : 52,00 €. » |
| 3 | Le calcul du coton, même mise en forme | « 5 paires à 12,00 €, tenue ≈ 4 mois à 3 sorties par semaine, soit 3 lots par an : 36,00 €. » |
| 4 | Une paire usée, photographiée sans retouche, à côté du rapport d'abrasion | « L'écart : 16,00 € par an, 0,31 € par semaine, 0,10 € par sortie. Les 600 km sont garantis contractuellement, le rapport d'abrasion est téléchargeable par numéro de lot. » |
| 5 | Fiche société : atelier, pays, numéro de SAV, nombre de commandes livrées | « Si elles ne tiennent pas 600 km, on remplace, sans retour. » |

*Note : les hypothèses du calcul sont affichées sur le volet même, pas en mention légale. Une comparaison dont les hypothèses sont cachées se retourne dès le premier commentaire qui la conteste.*

### 7.4 Le plan et le budget de production

| Lot | Concepts | Source | Coût unitaire HT | Total HT | Délai |
|---|---|---|---:|---:|---|
| Témoignages | C01, C05, C09 + 2 profils supplémentaires | 5 créateurs UGC | 150 € | 750 € | J+14 |
| Démonstrations | C02, C06, C10, C08 | Interne, téléphone et trépied | 60 € | 240 € | J+7 |
| Statiques et carrousels | C03, C07, C11 | Graphiste indépendant | 90 € | 270 € | J+10 |
| Déclinaisons | 24 assets (3 ratios × 12 − 12 sources) | Montage interne | 15 € | 360 € | J+18 |
| Droits d'usage 12 mois, payant, FR+BE | sur les 5 vidéos UGC | Majoration 40 % du forfait | 60 € | 300 € | à la signature |
| **Production** | | | | **1 920 €** | |
| Média de test | 12 concepts | — | 150 € | 1 800 € | J+21 à J+35 |
| **TOTAL DU PREMIER LOT** | | | | **3 720 € HT** | |

Temps interne non facturé : 6 h de brief, 4 h de tournage, 3 h de jugement — **13 heures**, et c'est cette ligne qui saturera en premier au lot suivant.

**Ce que ce lot produit, en espérance.** Au taux de réussite du palier P2 des [canoniques § 6](../donnees/chiffres-canoniques.md) — 1,7 gagnant pour 14 concepts, soit 12,14 % :

```
Gagnants attendus  = 12 × 12,14 %                       =  1,46
Coût par gagnant   = 3 720 ÷ 1,46                       =  2 548 € HT
```

**Et ce que porte un gagnant, à l'échelle de KALIS.** Dépense publicitaire 26 127 € par mois (1 000 commandes × 26,13 €), 5 gagnants en rotation :

```
Média porté par gagnant = 26 127 ÷ 5                    =  5 225 € / mois
CA TTC porté (MER 2,20) = 5 225 × 2,20                  = 11 495 €
CA HT                   = 11 495 ÷ 1,20                 =  9 579 €
Marge brute (60,3 %)                                     =  5 776 €
CM3 = 5 776 − 5 225                                      =    551 € / mois
CM3 annuelle par gagnant                                 =  6 612 €
Rendement = 6 612 ÷ 2 548                                =  ×2,6
```

**×2,6 seulement**, quand [E04](../modules/E04-psychologie-du-client.md) § 7.6 calcule ×38,0 au palier P5 sur le seul média de test. L'écart n'est pas une erreur : **le rendement d'un concept est proportionnel au budget qu'il porte.** Le même travail de création, la même heure de tournage, rapporte quinze fois plus à P5 qu'au lancement — et c'est précisément pour ça que P1 et P2 perdent de l'argent dans le modèle canonique. Tu ne construis pas une machine créative parce qu'elle est rentable aujourd'hui ; tu la construis parce qu'elle est la seule chose qui te fera arriver au palier où elle le devient.

### 7.5 Les droits d'usage, et ce que coûte de les acheter trop tard

Contrat type retenu par KALIS pour les cinq créateurs : forfait 150 € HT, majoration 40 % soit 60 € HT, **douze mois**, périmètre **publicité payante depuis le compte de la marque**, territoire France et Belgique, **non exclusif**, diffusion depuis le compte du créateur non incluse.

Le calcul qui justifie de payer les 300 € d'avance sur les cinq, alors qu'un seul gagnera :

```
Coût des droits achetés d'avance, 5 créas          = 5 × 60 €   =   300 € HT
Coût d'un renouvellement négocié après un gagnant  *hypothèse : ×5 du forfait,
    parce que le créateur voit la créa tourner*    = 750 € HT
Coût d'un gagnant perdu faute d'accord :
    CM3 annuelle du concept                         = 6 612 € HT
    + reproduction d'un concept équivalent          = 2 548 € HT
```

**300 € payés d'avance contre un risque de 9 160 €.** Le rapport est de 1 à 30, et il se dégrade encore à mesure que le budget grandit : au palier P3, un gagnant porte 88 868 € de CM3 annuelle (§ 8.3). C'est la décision la moins spectaculaire de la séance et l'une des mieux rémunérées.

### 7.6 Le nommage et le registre

```
20260907_A1-AMPOULE_F2-DEMO_H6-MUET_P-PESEE_9x16_v01
20260907_A1-AMPOULE_F2-DEMO_H3-INDIC_P-PESEE_9x16_v02   ← variation d'accroche
20260909_A2-TROU_F3-CARR_H7-CHIFFRE_P-LABO_4x5_v01
```

| id | Date | Angle | Format | Accroche | Preuve | Source | Coût HT | Fin des droits | Test | Rétention 3 s | CPA | Décision |
|---|---|---|---|---|---|---|---:|---|---:|---:|---:|---|
| C02-v01 | 07/09 | A1 | F2 | H6 | pesée | interne | 60 € | illimité | 150 € | 31 % | 24,80 € | conserver, 21/09 |
| C05-v01 | 07/09 | A2 | F1 | H2 | avis | UGC-03 | 210 € | 07/09/2027 | 150 € | 19 % | 41,20 € | couper, 21/09 |
| C11-v01 | 09/09 | A3 | F3 | H7 | calcul | graphiste | 90 € | illimité | 150 € | — | 29,60 € | prolonger, 28/09 |

**Pourquoi la colonne « fin des droits » est la troisième plus importante du registre**, après la décision et le CPA : c'est la seule qui peut te faire couper un gagnant sans que rien dans les indicateurs ne l'annonce. Une créa dont les droits expirent pendant qu'elle porte 20 % de la dépense se retire un lundi matin, et l'écart apparaît dans le compte de résultat du mois.

---
## 8. Les conséquences chiffrées de ton choix

### 8.1 Le rythme réel, palier par palier

Les trois lignes des [chiffres canoniques § 6](../donnees/chiffres-canoniques.md), et ce qu'on en dérive par simple division. Le facteur de conversion est 52 ÷ 12 = 4,333 semaines par mois.

| | **P2** | **P3** | **P5** |
|---|---:|---:|---:|
| Budget publicitaire par semaine (canonique) | 24 147 € | 100 615 € | 344 817 € |
| Budget de test, 15 % (canonique) | 3 622 € | 15 092 € | 51 722 € |
| **Concepts nouveaux par semaine** (canonique) | **14** | **38** | **57** |
| Gagnants par semaine (canonique) | 1,7 | 4,2 | 5,2 |
| Gagnants en rotation (canonique) | 9 | 21 | 23 |
| Assets produits par mois (canonique) | 188 | 654 | 1 245 |
| *Concepts par mois* | *60,7* | *164,7* | *247,0* |
| *Concepts par an* | *728* | *1 976* | *2 964* |
| *Assets par concept* | *3,10* | *3,97* | *5,04* |
| *Budget de test par concept* | *258,71 €* | *397,16 €* | *907,40 €* |
| *Taux de réussite* | *12,14 %* | *11,05 %* | *9,12 %* |
| *Durée de vie d'un gagnant* | *5,29 sem.* | *5,00 sem.* | *4,42 sem.* |
| **Durée de vie du lot de douze** | **6,0 jours** | **2,2 jours** | **1,5 jour** |

Trois lectures, dont deux ne sont pas dans le canonique.

**Le premier lot de douze ne dure pas une semaine.** Au rythme de P2 — celui de la [Porte P2 → P3](../mentorat/jalons.md), qui exige au moins 10 concepts nouveaux par semaine tenus huit semaines — douze concepts couvrent **six jours**. Sur un an, il faut **soixante lots comme celui que tu viens d'écrire**, et 165 à P3. Ce que tu as produit aujourd'hui n'est pas une bibliothèque : c'est un rythme de départ, et le vrai livrable de la séance est la chaîne qui le reproduira.

**Le nombre d'assets par concept monte avec le palier** — 3,10, puis 3,97, puis 5,04 — et ce n'est pas de la gourmandise. À P5, sept marchés ([canoniques § 2](../donnees/chiffres-canoniques.md)) imposent le sous-titrage et l'adaptation ; à P2, un seul marché et trois ratios suffisent. C'est aussi ce qui rend le champ « rushes bruts » du brief (§ 4.4) rentable : les déclinaisons se produisent au montage, à 15 € pièce, pas au tournage à 150 €.

**Le taux de réussite baisse quand on grandit** — 12,14 %, 11,05 %, 9,12 %. Le budget de test par concept, lui, monte de 258,71 € à 907,40 €. **Grandir coûte plus cher par idée testée et produit moins de gagnants par idée** ; c'est la définition même d'un goulot, et la raison pour laquelle la [Porte P4 → P5](../mentorat/jalons.md) exige 50 concepts nouveaux par semaine.

### 8.2 Ce que produit vraiment un lot de douze

*Hypothèse : les douze concepts réussissent indépendamment, au taux de P2 de 12,14 %. Loi binomiale.*

```
P(aucun gagnant sur 12)  = (1 − 0,1214)^12                     = 21,2 %
P(exactement 1 gagnant)  = 12 × 0,1214 × (1 − 0,1214)^11       = 35,1 %
P(au moins 2 gagnants)   = 1 − 21,2 % − 35,1 %                 = 43,8 %
Espérance                = 12 × 0,1214                          = 1,46 gagnant
```

La [Porte P1 → P2](../mentorat/jalons.md) exige **deux gagnants distincts**. Ton premier lot a donc **43,8 % de chances de la franchir**, et **21,2 % de chances de ne rien produire du tout**. Ce n'est pas un échec de créativité : c'est la forme normale d'une distribution à queue épaisse. Combien en faut-il pour 90 % de chances d'avoir deux gagnants ?

```
n = 30 → P(≥ 2) = 89,4 %        n = 31 → P(≥ 2) = 90,4 %
```

**Trente et un concepts.** Entre deux et trois lots comme celui-ci. **Écris le lot 2 avant d'avoir jugé le lot 1** : c'est la seule décision de planification qui découle de ce calcul, et c'est celle que presque personne ne prend, parce qu'elle demande de produire pendant qu'on attend.

**Et tu ne pourras pas juger le lot 1 sur le CPA.** Vérifie-le sur ton propre cas :

```
python3 ecommerce/outils/test_significativite.py --creatif \
    --depense 150 --achats 4 --cpa-cible 26
```

À 150 € de test et 4 achats, l'intervalle de confiance du CPA va de **14,65 € à 137,63 €** : il enjambe la cible de 26 €. L'outil réclame **938 € de plus par concept**, soit 1 088 € au total — 13 056 € pour les douze, la moitié d'un mois de budget publicitaire de KALIS. **Le premier lot se juge donc en amont** : rétention à 3 secondes, taux de clic, taux d'ajout au panier. Le CPA ne départage que les deux ou trois concepts qui survivent à ce premier tri, et sur eux, on paie les 1 088 €.

### 8.3 Le coût annuel de la machine créative, à P3 et à P5

*Hypothèses de coût, déclarées : mix de production 65 % créateurs UGC à 150 € HT, 25 % interne à 60 € HT, 10 % studio à 700 € HT, soit **182,50 € HT par concept source** ; déclinaison 15 € HT à P3 et 18 € HT à P5 (sous-titrage et localisation sur sept marchés) ; équipe créative 2,5 ETP à P3 et 6 ETP à P5, valorisée au coût moyen d'un ETP du palier — 105 000 ÷ 12 = 8 750 € à P3, 360 000 ÷ 38 = 9 474 € à P5 ([canoniques § 2.5](../donnees/chiffres-canoniques.md)).*

| Poste | **P3** | **P5** |
|---|---:|---:|
| Concepts sources | 164,7 × 182,50 € = **30 052 €** | 247,0 × 182,50 € = **45 078 €** |
| Déclinaisons | 489 × 15 € = **7 340 €** | 998 × 18 € = **17 964 €** |
| Équipe créative | 2,5 × 8 750 € = **21 875 €** | 6 × 9 474 € = **56 842 €** |
| **Total par mois** | **59 267 €** | **119 884 €** |
| **Total par an** | **711 204 €** | **1 438 608 €** |
| En % de la ligne publicitaire | 13,6 % | **8,0 %** |
| En % du CA HT | 6,0 % | 3,3 % |

**La machine créative coûte moins cher, relativement, à mesure qu'elle grossit** — 13,6 % du média à P3, 8,0 % à P5 — parce que l'équipe est un coût fixe et que les déclinaisons sont bien moins chères que les sources. C'est l'un des rares postes du cursus où l'échelle joue vraiment en ta faveur.

**Attention à la ligne comptable.** Le modèle canonique ne sépare pas la production créative : les salaires sont dans les frais fixes, et la production externalisée doit être prélevée sur la ligne publicitaire. Traitée ainsi, elle coûte à P3 30 052 + 7 340 = **37 392 € de média en moins par mois**, soit, au MER de 2,70, **100 958 € de CA TTC non achetés**. C'est le vrai prix de la machine, et il se paie tous les mois.

**Ce que coûte et ce que rapporte un gagnant.**

| | **P3** | **P5** |
|---|---:|---:|
| Gagnants par an | 218,4 | 270,4 |
| Production par gagnant | 3 256 € | 5 320 € |
| Média de test par gagnant | 3 593 € | 9 947 € |
| **Coût complet d'un gagnant** | **6 849 €** | **15 267 €** |
| CM3 annuelle portée par un gagnant | 88 868 € | 378 144 € |
| **Rendement** | **×13,0** | **×24,8** |

Le calcul de P3, déroulé : chacun des 21 gagnants porte 100 615 ÷ 21 = 4 791 € de média par semaine, soit 12 936 € de CA TTC au MER de 2,70, donc 10 780 € HT, dont 60,3 % de marge brute = 6 500 €, moins les 4 791 € de média = **1 709 € de CM3 par semaine**, soit 88 868 € par an.

Contrôle sur le canonique : 21 × 1 709 € = 35 889 € par semaine, soit 155 519 € par mois, contre **156 033 € de CM3** au tableau des [canoniques § 2.2](../donnees/chiffres-canoniques.md) — 0,33 % d'écart, dû aux arrondis. **Le compte de résultat du palier P3 se reconstruit intégralement à partir de ses 21 concepts en rotation.**

Note enfin l'écart avec [E04](../modules/E04-psychologie-du-client.md) § 7.6, qui annonce ×38,0 à P5 : ce calcul-là ne compte que le média de test. En ajoutant la production, le rendement réel tombe à **×24,8**. Les deux sont justes ; celui-ci est celui qui décide d'un budget.

### 8.4 Deux trajectoires : douze concepts par trimestre, ou quatorze par semaine

Deux marques identiques — même produit, même offre, mêmes angles, même MER de 2,20. La seule différence est le rythme de production.

*Le canonique implique qu'un gagnant porte environ 24 147 ÷ 9 = **2 683 € de dépense hebdomadaire** au palier P2. On suppose ce plafond stable : au-delà, la fréquence d'exposition monte, le CPM avec elle, et le concept se met à coûter plus cher qu'il ne rapporte. Le nombre de gagnants en rotation plafonne donc la dépense.*

```
Gagnants en rotation = concepts/semaine × taux de réussite × durée de vie
Marque X : 0,92 × 12,14 % × 5,29 sem.                        = 0,59 gagnant
Marque Y :   14 × 12,14 % × 5,29 sem.                        = 9,0 gagnants
```

(Contrôle : Y retombe exactement sur les 9 gagnants en rotation du canonique.)

| | **X — 12 concepts par trimestre** | **Y — 14 par semaine** |
|---|---:|---:|
| Concepts par an | 48 | 728 |
| Gagnants par an | 5,8 | 88,4 |
| Gagnants en rotation | **0,59** | **9,0** |
| Dépense publicitaire soutenable / semaine | **1 592 €** | **24 147 €** |
| CA TTC soutenable / semaine (MER 2,20) | **3 502 €** | **53 123 €** |
| CA TTC par mois | 15 176 € | 230 200 € |
| Position sur les paliers | **sous P1** | **P2 exactement** |
| Coût de production annuel (182,50 € le concept) | 8 760 € | 132 860 € |

**L'écart n'est pas une différence de performance, c'est un plafond.** La marque X n'a pas un moins bon coût d'acquisition que Y : elle a un compte publicitaire qui ne peut pas absorber davantage de budget sans se répéter. Elle plafonne à 15 176 € de chiffre d'affaires TTC par mois — **en dessous du palier P1** — et aucune quantité d'argent ne l'en sort, parce que ce qui lui manque ne s'achète pas en média. Y dépense quinze fois plus, non pas parce qu'elle a plus d'argent, mais parce qu'elle a **de quoi le dépenser**.

Le coût de cette différence, en production : 132 860 € contre 8 760 € par an. **124 100 € pour multiplier par quinze le chiffre d'affaires atteignable.** C'est le meilleur rapport de tout le cursus, et c'est le poste que les marques coupent en premier quand le mois est difficile.

> **À retenir :** ton lot de douze n'est pas un stock, c'est le premier tour d'une machine. Ce que tu dois savoir produire à la fin de cette séance n'est pas douze concepts, mais **douze concepts par semaine, indéfiniment** — parce que c'est la seule chose qui détermine combien tu peux dépenser, donc combien tu peux vendre.

---

## 9. Avant la séance suivante

1. **Lance la production des quatre démonstrations internes cette semaine.** Ce sont les seules qui ne dépendent de personne : téléphone, trépied, lumière du jour. Une créa produite vaut mieux que trois créas briefées.
2. **Signe les droits d'usage avant la première livraison**, douze mois, publicité payante incluse. Après, tu paieras cinq fois le prix, et tu le paieras sur le concept qui gagne.
3. **Écris les douze accroches du lot 2**, à partir des familles non retenues et du registre. Tu dois les avoir écrites avant de connaître le résultat du lot 1, sinon tu n'écriras que des variations du gagnant — et une bibliothèque de variations d'un seul concept meurt le jour où ce concept fatigue.
4. **Ouvre ton registre et remplis les treize colonnes des douze premières lignes**, dont la date de fin des droits. C'est le document que [S09](S09-lire-les-premiers-chiffres.md) te fera lire pour diagnostiquer ton compte, et il ne se reconstitue pas après coup.

---

*Fin de la séance S06. Suite : [S07 — Le site qui convertit](S07-le-site.md), où tu écriras la page qui doit tenir, mot pour mot, la promesse que ces douze accroches viennent de faire — et où tu découvriras que la moitié des créas qui échouent ne meurent pas dans le fil, mais entre le clic et le paiement.*
