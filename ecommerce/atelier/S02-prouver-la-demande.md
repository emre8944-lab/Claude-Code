# Séance S02 — Prouver la demande avant de produire

> **Niveau requis :** L02 · **Durée :** 8 h réparties sur ~5 semaines · **Livrable :** les six tests d'[E02](../modules/E02-marche-et-produit.md) § 4 avec seuils écrits d'avance, résultats, verdict go / no-go · **Modules :** [E02](../modules/E02-marche-et-produit.md) § 4, [E04](../modules/E04-psychologie-du-client.md)
>
> **Ce que tu ne peux pas faire sans cette séance :** commander du stock. La condition 3 de la porte 0 → P1 exige quatre tests favorables sur six, seuils écrits d'avance ([jalons](../mentorat/jalons.md)).

---

## 1. Où tu en es

Tu as une catégorie, un segment et un angle supposé, décidés en [S01](S01-choisir-le-terrain.md), notés sur la grille à 45 points d'[E02](../modules/E02-marche-et-produit.md) § 3, avec un MER seuil confronté au MER atteignable.

Décidé : **le terrain.** Pas décidé : que quelqu'un veuille acheter ce que tu vendras, à ton prix, sans te connaître.

C'est là que meurent les lancements. Une catégorie viable dit seulement que la structure **autorise** une marque, pas que la tienne mérite d'exister. Deux critères de S01 — la demande exprimée et la charge de preuve créative — n'étaient que des estimations : cette séance les mesure, sur cinq semaines, parce que quatre des six tests ont besoin de temps réel. C'est pourquoi la plupart des fondateurs les sautent.

---

## 2. Ta mission

**Exécuter les six tests d'[E02](../modules/E02-marche-et-produit.md) § 4, budget borné et six seuils chiffrés écrits AVANT de commencer, puis rendre un verdict go / no-go argumenté.**

Trois résultats obligatoires :

1. **La feuille des seuils, datée avant le premier euro dépensé.** Six lignes recopiées d'[E02](../modules/E02-marche-et-produit.md) § 4.7 sans ajustement. Tu ne la modifies plus.
2. **Les six tests exécutés en cascade**, dans le budget annoncé, résultats bruts compris ceux qui te déplaisent.
3. **Un verdict** — go, no-go, ou go conditionnel avec sa condition écrite — plus les **lignes de cahier des charges produit** que le test (c) fait apparaître : l'entrée de [S03](S03-produit-et-cogs.md).

Budget plafond : **≈ 3 500 € TTC**, soit **1,40 % du capital que le lancement engagera** ([E02](../modules/E02-marche-et-produit.md) § 4.7). Un budget non borné transforme un test en investissement, et un investissement ne s'interrompt plus.

---

## 3. Ce dont tu disposes

[`test_significativite.py`](../outils/test_significativite.py) pour savoir combien de visiteurs il faut avant de conclure · [`calculateur.py`](../outils/calculateur.py) pour recalculer ton MER seuil si un test déplace ton prix · [`E02`](../modules/E02-marche-et-produit.md) § 4, dont cette séance est l'exécution · [`jalons`](../mentorat/jalons.md), porte 0 → P1 · [`C02`](../etudes-de-cas/C02-vallee-de-la-mort.md) pour ce que coûte un lancement qu'on n'arrête pas.

Outils extérieurs, gratuits ou quasi : un planificateur de mots-clés, un outil de tendance de recherche, les **bibliothèques publicitaires** que les grandes plateformes tiennent ouvertes au titre de la réglementation européenne, la marketplace dominante de ton pays, un tableur, un constructeur de page, un compte publicitaire, un prestataire de paiement. Je nomme des fonctions, pas des marques : les outils changent tous les dix-huit mois, les fonctions non.

Ce qui ne vaut pas preuve : l'avis de tes proches, le nombre de « j'aime », une liste d'attente sans prix, « le marché est énorme ». Aucun n'a jamais prédit une vente.

---

## 4. La méthode, pas à pas

**Les six tests sont une cascade, pas une liste.** Ordonnés par budget croissant, et **tu t'arrêtes au premier seuil non franchi.** C'est toute l'économie du dispositif : un no-go au test (a) coûte 0 € et un jour, le même au test (f) coûte 3 500 € et cinq semaines. L'ordre n'est pas une commodité, c'est ce qui rend la validation abordable.

| Test | Ce qu'il mesure | Budget | Durée | Seuil de passage |
|---|---|---:|---|---|
| **(a)** Recherche et tendance | La demande déjà formulée | 0 – 99 € | 1 j | ≥ 20 000 recherches/mois |
| **(b)** Concurrents payants | La rentabilité que la catégorie autorise | 0 € | 2 j | ≥ 5 annonceurs > 6 mois |
| **(c)** Marketplaces et avis 1-2★ | L'irritant, et ton cahier des charges | 200 – 400 € | 1 sem. | Top 3 des défauts ≥ 45 % |
| **(d)** Communautés | Les mots de ton client | 0 € | 1 sem. | ≥ 30 verbatims |
| **(e)** Smoke test | L'intérêt pour ta promesse | 1 000 € | 7 j | ≤ 3,50 €/inscr. et ≥ 25 % |
| **(f)** Pré-commande réelle | L'intention, avec de l'argent | 2 200 € | 14 j | ≥ 40 cmd et ≤ 40 €/cmd |
| | | **≈ 3 500 €** | **~5 sem.** | |

**Écris tes six seuils maintenant**, au plus tard avant le premier relevé. Un seuil écrit après le test est une justification — [protocole](../mentorat/protocole.md) § 6, faute n° 4. Je la sanctionne le plus durement parce qu'elle est invisible : celui qui la commet croit de bonne foi avoir testé.

### (a) Volume de recherche et tendance — 0 à 99 €, 1 jour

Tu comptes les recherches mensuelles sur le champ sémantique du **problème**, pas du produit. Le seuil se dérive ([E02](../modules/E02-marche-et-produit.md) § 4.1) : 800 commandes en P1, dont 15 % par la recherche, à 2,5 % de conversion et 20 % de demande captée, exigent 24 000 recherches par mois.

**FAVORABLE** — ≥ 20 000 recherches mensuelles sur le pays principal, **et** tendance à 24 mois qui ne décroît pas de plus de 15 %. En dessous, tu devras créer toute ta demande en publicité de découverte et le canal le moins cher du plan média disparaît : la recherche livre un client à 19,00 € quand le nCAC blended vaut 40,03 € (canoniques § 5 et § 2.4).

### (b) Concurrents payants — 0 €, 2 jours

Tu ouvres les bibliothèques publicitaires publiques et tu comptes, pour ta catégorie et ton pays : les **annonceurs distincts** qui diffusent, **depuis combien de temps**, avec **combien de créations actives**. **FAVORABLE** — ≥ 5 annonceurs depuis ≥ 6 mois, dont ≥ 2 avec ≥ 20 créations actives.

**Pourquoi l'ancienneté est le cœur du test.** Une publicité encore diffusée après six mois n'est pas une publicité aimée, c'est une publicité **rentable** : personne ne subventionne dix-huit mois de média par plaisir. La présence d'un annonceur installé est la **preuve, par le comportement, que la catégorie supporte un MER au-dessus de son seuil** — le seul indicateur public de rentabilité d'un concurrent.

#### Le piège : une catégorie sans concurrence publicitaire est un signal NÉGATIF

L'erreur la plus coûteuse du métier, et elle se déguise en lucidité : « personne ne fait de publicité là-dessus, le terrain est libre ».

Le marché publicitaire est une enchère continue où des dizaines de milliers d'annonceurs testent en permanence, budgets réels et retours immédiats. Si personne n'achète de trafic sur une catégorie, l'explication la plus probable n'est pas que personne n'y a pensé : c'est que **quelqu'un a essayé et que les chiffres n'ont pas tenu.** [E02](../modules/E02-marche-et-produit.md) § 4.2 en donne trois causes, toutes mauvaises : la marge brute est trop basse pour financer du trafic payant ; la demande existe mais ne se convertit pas à froid, parce que l'achat exige une délibération que la publicité de découverte ne déclenche pas ; ou la catégorie est réglementairement interdite de publicité, et tu peux vendre légalement sans avoir le droit de rien dire.

**Les rares exceptions**, où le vide est réel et non un cimetière. Quatre, et dans chacune tu dois pouvoir **nommer le mécanisme** qui tient les autres à l'écart : une **réglementation qui vient de changer**, vide daté qui se referme en 18 à 36 mois ; un **produit de moins de 24 mois**, vérifiable au fait que la catégorie n'a pas d'avis antérieurs ; un **décalage géographique** — la vérification la plus rentable du test, la bibliothèque publicitaire du pays saturé donnant le vide *et* le message qui marche ; une **restriction contournable légalement** en changeant l'objet annoncé, rare et fragile.

La question n'est donc pas *pourquoi personne n'y est*, c'est **quelle contrainte a arrêté les autres, et qu'est-ce que je sais qu'ils ne savaient pas.** **Si tu ne peux pas l'écrire en une phrase, il n'y a pas de marché.**

### (c) Marketplaces et avis 1 et 2 étoiles — 200 à 400 €, 1 semaine

Le test le plus rentable des six, et le seul qui produise un livrable réutilisable. **D'abord la profondeur** : **≥ 3 produits avec ≥ 500 avis** sur la marketplace dominante — la preuve que des gens achètent, à un prix connu, et pas seulement qu'ils cherchent. **Puis le vrai travail** : tu lis **200 avis à 1 et 2 étoiles** sur les cinq premiers produits et tu les codes — une ligne par avis, **un** poste principal, le dominant, plus un verbatim de dix mots maximum. Les avis de plus de 18 mois décrivent une formule qui n'existe plus : exclus-les.

| Poste | Ce qu'il recouvre | Poste | Ce qu'il recouvre |
|---|---|---|---|
| **A** Efficacité insuffisante | le résultat promis n'est pas obtenu | **E** Prix et quantité | rapport quantité-prix jugé mauvais |
| **B** Délai d'effet | le résultat vient, trop tard | **F** Livraison, emballage | casse, retard, suremballage |
| **C** Effet indésirable | irritation, odeur, texture, goût | **G** Service client | remboursement, non-réponse |
| **D** Format et contenant | contenance, dosage, fuite | **H** Écart promesse / produit | ne correspond pas à la publicité |

**FAVORABLE** — les **trois postes les plus fréquents couvrent ≥ 45 %** des critiques. Sous 30 %, l'insatisfaction est idiosyncratique : chaque client est mécontent pour une raison différente et aucune modification produit ne la capte. Entre 30 et 45 %, tu as un axe mais pas un produit.

**Deux lectures que le seuil ne donne pas.** Si **F et G** dominent, les concurrents sont mauvais en **exécution**, pas en produit — et l'exécution logistique est le terrain où l'échelle gagne toujours. Si un poste unique dépasse 55 %, c'est un problème que les leaders corrigent déjà : ta réponse arriverait quand elle cesse d'être différenciante.

**Le geste professionnel.** Compte les **postes**, pas les avis, puis convertis chaque poste au-dessus de 12 % en **une ligne de cahier des charges opposable à un fournisseur** : exigence, vérification, seuil d'acceptation. C'est ce document qui est le livrable de (c), et il entre dans [S03](S03-produit-et-cogs.md). Achète enfin les 4 à 6 produits les mieux notés — c'est le budget du test — et vérifie chaque défaut de tes mains : on n'écrit pas un cahier des charges contre un produit qu'on n'a pas ouvert ni utilisé quinze jours.

### (d) Communautés et vocabulaire — 0 €, 1 semaine

Forums, fils de discussion, groupes privés, commentaires sous les vidéos des concurrents. Tu ne cherches pas des idées, tu cherches **des mots**. **FAVORABLE** — ≥ 3 communautés actives (au moins un message par jour) et ≥ 30 formulations verbatim du problème, dont ≥ 10 vues au moins 5 fois.

Si tu ne réunis pas 30 façons dont de vraies personnes décrivent le problème avec leurs mots, c'est qu'il n'est pas assez douloureux pour qu'on en parle — ou qu'il est **tabou**, information différente et parfois excellente : un problème tabou produit peu de messages publics et beaucoup d'anonymes. Ce corpus vaut plus qu'un cahier des charges : le goulot de P5, ce sont 57 concepts nouveaux par semaine (canoniques § 6), et ils sortent d'un stock d'angles qui sort de là.

### (e) Smoke test — 1 000 €, 5 à 7 jours

Une page unique, une promesse, un mécanisme, **un prix affiché**, un bouton de pré-inscription. Du trafic payant froid dessus. Pas « inscris-toi pour être informé du lancement » : sans prix, tu mesures la curiosité, pas l'intention.

**FAVORABLE** — **≤ 3,50 € par inscription ET ≥ 25 % d'inscriptions** sur les visiteurs. Le seuil de coût se dérive ([E02](../modules/E02-marche-et-produit.md) § 4.5) : une inscription vaut 0,12 client, puisque ~12 % d'une liste chaude achète dans les 60 jours ; à un nCAC de P1 de 26,62 € (canoniques § 2.4), elle ne peut donc pas coûter plus de 26,62 × 0,12 = 3,19 €. **Entre 3,50 € et 5,00 €, tu retestes — avec un autre angle, pas un autre produit.** Au-dessus de 5,00 €, tu arrêtes.

**Trois angles créatifs distincts**, budgets séparés, et **ne lis jamais la moyenne** : c'est la seule information du test qui ne serve à rien. Un test moyen à 28 % peut contenir un angle à 38 % et un angle à 17 %, et c'est l'écart que tu es venu chercher.

**Le taux mesure l'intérêt pour ta promesse dans un défilement payant, à coût d'entrée nul — c'est-à-dire la qualité de ton angle et l'existence d'un problème ressenti. C'est beaucoup, et c'est tout. Ce qu'il ne dit pas :** rien sur la conversion payante, car **une inscription est gratuite pour celui qui la donne** et mesure une curiosité, pas un consentement à payer. Rien sur le réachat, qui décide de tout ([S01](S01-choisir-le-terrain.md) § 8). Rien sur ton coefficient. Et surtout **il est manipulable par toi-même** : une promesse exagérée fait monter le taux et détruit la marque un an plus tard. D'où la règle — **la promesse de la page doit être celle que le produit tiendra.** Un smoke test réussi sur une promesse intenable est le pire des six résultats : il finance une erreur au lieu de l'arrêter. Dernier piège : n'inclus jamais les inscriptions de ton entourage.

### (f) La pré-commande réelle — 2 200 €, 10 à 14 jours

Le seul test qui vaut vraiment : page produit complète, prix, paiement qui débite, date d'expédition annoncée. Le client engage son argent.

**FAVORABLE — deux seuils dérivés** ([E02](../modules/E02-marche-et-produit.md) § 4.6) : **≤ 40 € par pré-commande**, soit le nCAC de P1 majoré de 50 % parce qu'au lancement tu n'as ni pixel, ni preuve sociale, ni audience de reciblage ; et **≥ 40 pré-commandes en 14 jours**, parce qu'à 40 conversions l'erreur-type relative vaut 1 ÷ √40 = 15,8 % et qu'en dessous tu lis du bruit.

**Contrôle croisé obligatoire :** compare le **panier moyen** à ton hypothèse de S01. S'il sort 15 % sous la cible, personne ne prend le lot et ton modèle d'AOV est faux avant d'avoir commencé ([E03](../modules/E03-offre-et-prix.md)). Et **exige que la moitié des pré-commandes vienne de trafic froid** : une pré-commande vendue à un inscrit du test (e) mesure ta liste, pas la demande.

**Le coût en réputation si tu échoues.** Le coût direct est modeste et calculable : sur 40 pré-commandes à 46,00 € TTC, 1 840 € à rembourser, 38,52 € de frais non restitués et le média dépensé, soit ≈ 1 640 € ([E02](../modules/E02-marche-et-produit.md) § 4.6). **Ce n'est pas le sujet.** Le sujet est que quarante personnes ont donné leur argent pour un produit qui n'existera pas et qu'elles l'écriront : tu commences ta vie de marque avec un passif public.

La contre-mesure n'est pas de renoncer au test, c'est de le rendre **honnête d'avance** : date d'expédition annoncée, condition de réalisation écrite sur la page de paiement (« production lancée à partir de N commandes »), remboursement automatique si le seuil n'est pas atteint. Une pré-commande annoncée comme telle qui échoue proprement coûte peu ; déguisée en stock disponible, elle coûte la marque. Trois conditions avant de lancer : devis fournisseur signé avec délai écrit, cash pour l'acompte, trente jours de marge sur la date annoncée. **Le vrai risque n'est pas le remboursement, c'est le retard** — trois mois de retard font plus de dégâts qu'un remboursement immédiat, parce que le client a attendu, relancé et raconté.

### La règle de verdict

Trois issues par test : **favorable**, **non concluant**, **défavorable** ; un non concluant compte comme non favorable, il n'y a pas de demi-point, et la cascade s'arrête au premier seuil non franchi. **≥ 4 favorables sur 6 → go** (condition 3 de la porte 0 → P1). **≤ 3 → no-go**, retour à S01 sur ta deuxième finaliste. Un test non concluant se rejoue **une fois**, même méthode, budget déclaré d'avance — et pour (e), avec un autre angle, pas un autre produit. Une fois, pas deux : au troisième essai tu cherches le résultat qui t'arrange.

---

## 5. Ton livrable

```
LIVRABLE S02 — PREUVE DE DEMANDE                        Date : __/__/____
Catégorie / segment / angle (repris de S01) : ___________________________

PARTIE 1 — LES SEUILS, ÉCRITS LE __/__/____ AVANT TOUT RELEVÉ
 Test  Ce que je mesure     Seuil FAVORABLE  Seuil DÉFAVORABLE  Budget
 (a)   _________________    _____________    _____________      ____ €
 …  (une ligne par test jusqu'à (f))      BUDGET PLAFOND     ____ €

PARTIE 2 — LES RÉSULTATS, DANS L'ORDRE DE LA CASCADE
 Test  Résultat brut        Verdict (fav./non concl./défav.)  Dépensé
 (a)   _________________    _____________________________     ____ €
 …
 TOTAL favorables : __/6              TOTAL dépensé : ____ € TTC

PARTIE 3 — LE DÉPOUILLEMENT DES AVIS (c)
 Profondeur : ___ produits à ≥ 500 avis   (seuil : ≥ 3)
 Corpus : ___ avis 1-2 étoiles, ___ produits, < 18 mois  (seuil : ≥ 200)
 Nombre  A ___ B ___ C ___ D ___ E ___ F ___ G ___ H ___
 En %    A ___ B ___ C ___ D ___ E ___ F ___ G ___ H ___
 TOP 3 CUMULÉ : ____ %   (seuil : ≥ 45 %)
 LIGNES DE CAHIER DES CHARGES (une par poste > 12 %) :
 1. Exigence : ____________ Vérification : ______ Seuil : ________

PARTIE 4 — LA CONCURRENCE PAYANTE (b)
 Annonceurs actifs : ____  dont > 6 mois : ____  dont ≥ 20 créas : ____
 Plus ancienne créa active : ____ jours (annonceur ____)
 Si < 5 annonceurs > 6 mois — QUELLE CONTRAINTE A ARRÊTÉ LES AUTRES, ET
 QUE SAIS-JE QU'ILS NE SAVAIENT PAS ? ______________
 (si tu ne peux pas l'écrire, il n'y a pas de marché)

PARTIE 5 — LE VERDICT      ☐ GO   ☐ NO-GO   ☐ GO CONDITIONNEL
 Les trois faits chiffrés qui le portent : ____ / ____ / ____
 Le test le plus défavorable, et ce que j'en fais : ______________
 Si GO CONDITIONNEL — la condition, chiffrée et datée : __________
 Ce que je m'interdis d'invoquer pour ne pas appliquer un no-go : ____
```

---

## 6. La grille d'évaluation

| # | Critère | Pts | Ce qui vaut les points | Ce qui les fait perdre |
|---|---|---:|---|---|
| 1 | **Seuils écrits d'avance** | 20 | Les six, chiffrés, datés avant le premier relevé | Seuils postérieurs aux résultats : **0 à toute la séance** |
| 2 | Cascade respectée | 12 | Tests dans l'ordre, arrêt au premier seuil non franchi | Tests menés en parallèle : −6. Test sauté : −4 chacun |
| 3 | Budget tenu | 8 | Dépense ≤ budget annoncé | Dépassement > 30 % non expliqué : −8 |
| 4 | **Dépouillement des avis** | 18 | Profondeur vérifiée, ≥ 200 avis, 8 postes, top 3 chiffré | < 200 avis : −8. Top 3 non calculé : −10. Aucun cahier des charges : −6 |
| 5 | **Lecture de la concurrence payante** | 15 | Annonceurs, ancienneté **et** volume de créas | Ancienneté absente : −8. « Pas de concurrence donc opportunité » : **−15** |
| 6 | Smoke test lu correctement | 12 | Prix affiché, trois angles, résultat par angle | Sans prix affiché : −10. En moyenne seule : −5 |
| 7 | Pré-commande et part froide | 8 | Paiement réel, condition de réalisation écrite, part froide | Sans condition écrite : −8. Liste seule : −6 |
| 8 | Verdict et discipline | 7 | Verdict conforme, trois faits chiffrés, auto-interdiction | Verdict contraire aux seuils sans justification : −7 |

**Seuil de validation : 70/100. Fautes éliminatoires, séance à refaire :** un seuil écrit ou modifié après avoir vu un résultat ; une absence de concurrence payante présentée comme une opportunité sans contrainte nommée ; un smoke test sans prix affiché présenté comme une preuve ; une pré-commande encaissée sans devis fournisseur signé ni condition de réalisation écrite ; un « go » avec moins de 4 favorables sur 6.

---

## 7. Le corrigé exemplaire

> **Cas composite. Marque fictive.** CLARÈNE n'existe pas ; le projet est celui décidé en [S01](S01-choisir-le-terrain.md) § 7. Tous les chiffres sont modélisés : ce sont ceux qu'un relevé réaliste produirait. Les concurrents sont anonymisés en A1…A11.

**LIVRABLE S02 — CLARÈNE, soin visage anti-imperfections adulte**

### Partie 1 — Les seuils, écrits le 3 avant tout relevé

Recopiés d'[E02](../modules/E02-marche-et-produit.md) § 4.7 sans ajustement : (a) ≥ 20 000 recherches/mois, tendance ≥ −15 % · (b) ≥ 5 annonceurs depuis ≥ 6 mois, dont ≥ 2 à ≥ 20 créas · (c) ≥ 3 produits à ≥ 500 avis, top 3 des défauts ≥ 45 % sur 200 avis · (d) ≥ 3 communautés, ≥ 30 verbatims dont ≥ 10 vus 5 fois · (e) ≤ 3,50 €/inscription **et** ≥ 25 % · (f) ≥ 40 pré-commandes, ≤ 40 €/commande, panier ≥ 85 % de la cible, part froide ≥ 50 %. Plafond **3 500 € TTC**.

### Partie 2 — Les résultats

| Test | Résultat | Verdict | Dépensé |
|---|---|---|---:|
| **(a)** | **48 100** recherches/mois sur 12 requêtes ; tendance 24 mois **+38 %** | **Fav.** | 0 € |
| **(b)** | **11 annonceurs**, 285 créas ; 6 depuis > 6 mois, 3 à ≥ 20 créas ; plus ancienne **412 j** | **Fav.** | 0 € |
| **(c)** | 5 produits à ≥ 500 avis ; 200 avis dépouillés ; **top 3 = 67,0 %** (A 30,5 · C 23,5 · D 13,0) | **Fav.** | 287 € |
| **(d)** | 4 communautés actives ; **34 verbatims**, dont 12 vus ≥ 5 fois | **Fav.** | 0 € |
| **(e)** | 1 186 visiteurs, 332 inscriptions = **28,0 %** ; **3,01 € TTC**/inscription | **Fav.** | 1 000 € |
| **(f)** | **61 pré-commandes** à **36,07 €**, panier 53,18 € TTC, part froide 55,7 % | **Fav.** | 2 200 € |
| | | **6 / 6** | **3 487 €** |

**(a), le détail.** Douze requêtes, dont « acné adulte » 9 900 (+41 %), « niacinamide » 8 100 (+180 %), « acide azélaïque » 4 400 (+260 %). Total **48 100**, et sept des douze décrivent le problème et non le produit : la demande est ressentie, pas seulement informée.

### Partie 3 — Le dépouillement des avis (c)

Profondeur : 5 produits dépassent 500 avis, le premier en compte 4 210. Corpus : 200 avis 1 et 2 étoiles, 5 produits (2 leaders, 2 marques de vente directe, 1 de distributeur), 40 chacun, moins de 18 mois.

| Poste | A | B | C | D | E | F | G | H | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Nombre | **61** | 18 | **47** | **26** | 21 | 9 | 7 | 11 | **200** |
| % | **30,5** | 9,0 | **23,5** | **13,0** | 10,5 | 4,5 | 3,5 | 5,5 | 100 |

**Top 3 = A + C + D = 67,0 %**, très au-dessus du seuil de 45 % : le mécontentement est concentré et **dans le produit**, pas dans la logistique — F et G ne pèsent que 8,0 %. Aucun poste ne dépasse 55 %, donc aucun n'est déjà corrigé chez les leaders. **Favorable.**

**Les trois lignes de cahier des charges** — le vrai livrable de (c), entrée de [S03](S03-produit-et-cogs.md) :

| # | Poste | Exigence | Vérification | Seuil |
|---|---|---|---|---|
| 1 | C — 23,5 % | Tolérance cutanée : sans parfum, sans alcool dénaturé, pH 5,0–5,5, actif exfoliant plafonné à 8 % | Usage 21 jours, 32 sujets à peau réactive | Irritation ≤ 5 % des sujets |
| 2 | A — 30,5 % | Efficacité mesurée et non revendiquée : actif principal à concentration documentée | Comptage des lésions à 8 semaines, photo standardisée | Réduction ≥ 40 % |
| 3 | D — 13,0 % | Pompe airless opaque 30 ml, dose calibrée 0,40 ml | Comptage sur 5 flacons pilotes | 75 doses ± 3 |

**Et la ligne 3 ferme une boucle.** 75 doses à une application par jour font **2,5 mois d'usage** — la fréquence retenue en [S01](S01-choisir-le-terrain.md), qui donnait un MER atteignable de 2,28 pour un seuil de 1,99. La contenance n'est pas un détail d'emballage : **c'est elle qui fixe ta fréquence, et la fréquence est la moitié de ton résultat à 24 mois.** Un flacon de 50 ml l'aurait portée à 4,2 mois et la marge au seuil de 14,9 % à 7,3 %.

### Partie 4 — La concurrence payante (b)

| Annonceur | A1 | A2 | A3 | A4 | A5 | A6 | A7 à A11 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Créas actives | **84** | **51** | **37** | 29 | 22 | 18 | 44 cumulées |
| Plus ancienne créa active | **412 j** | **268 j** | **196 j** | 141 j | 97 j | 88 j | 61 j au mieux |

Onze annonceurs, six depuis plus de six mois, trois avec ≥ 20 créations actives. **Favorable sur les deux conditions.** A1 diffuse une création depuis 412 jours : elle rembourse son coût tous les jours depuis plus d'un an. La distribution — onze entrants, trois installés — est celle d'une catégorie saine ; une catégorie où *tous* auraient des créations de plus de six mois serait au contraire fermée.

### Partie 5 — Le smoke test (e), lu par angle

Page unique, prix affiché 34,00 € TTC le sérum et 79,00 € TTC la routine, promesse identique au cahier des charges. Sept jours, ciblage large France 25–45 ans, 1 000 € TTC de média, 1 299 clics, **1 186 visiteurs**.

| Angle | Média TTC | Visiteurs | Inscr. | Taux | Coût / inscr. |
|---|---:|---:|---:|---:|---:|
| **A1** « L'acné à 32 ans, ce n'est pas de l'adolescence attardée » | 372,00 € | 441 | 168 | **38,1 %** | **2,21 €** |
| **A2** « 8 semaines, 47 % de lésions en moins » | 334,00 € | 389 | 104 | 26,7 % | 3,21 € |
| **A3** « La routine à 3 produits qui ne décape pas » | 294,00 € | 356 | 60 | **16,9 %** | 4,90 € |
| **Total** | **1 000,00 €** | **1 186** | **332** | **28,0 %** | **3,01 €** |

**Ce que la moyenne cachait.** Le test passe à 28,0 % et 3,01 €, mais il contient un angle à 38,1 % et un angle à 16,9 % qui, seul, tomberait dans la zone de reprise. Lire la moyenne, c'est jeter l'information la plus chère du test. A1, qui parle d'identité — l'âge, la honte d'un problème « d'adolescent » à 32 ans — fait 2,3 fois le taux de A3, qui parle du produit. C'est l'orientation de [S05](S05-recherche-client-et-angles.md), et A3 est abandonné.

**Une alerte que le chiffre ne montre pas.** A2, promesse quantifiée « 47 % de lésions en moins », n'obtient que 26,7 % : elle ne surperforme pas la promesse d'identité et elle m'engagerait sur un résultat à financer — la ligne 2 du cahier des charges. **Je la retire du plan de lancement tant que le test d'efficacité à 8 semaines n'est pas rendu.**

### Partie 6 — La pré-commande (f)

Page produit complète, expédition annoncée au 15 du troisième mois, condition de réalisation écrite sur la page de paiement (« production lancée à partir de 40 commandes »), remboursement automatique sinon. Devis fournisseur signé, délai écrit à 9 semaines, 30 jours de marge. 2 000 € TTC de média et 200 € de frais, quatorze jours.

| Source | Média TTC | Visiteurs | Pré-commandes | Taux |
|---|---:|---:|---:|---:|
| Trafic froid | 1 400,00 € | 1 592 | **34** | **2,14 %** |
| Reciblage des visiteurs de (e) | 400,00 € | 662 | 19 | 2,87 % |
| Courriel aux 332 inscrits | 0 € | 96 | 8 | 8,3 % |
| **Total** | **1 800,00 €** | **2 350** | **61** | **2,60 %** |

Les quatre conditions : 61 ≥ 40 ✓ · coût 2 200 ÷ 61 = **36,07 €** ≤ 40 € ✓ · panier 3 244,00 ÷ 61 = **53,18 € TTC**, **102,3 %** de la cible ✓ · part froide 34/61 = **55,7 %** ≥ 50 % ✓. **Favorable.**

Composition : 26 routines à 79,00 € TTC et 35 sérums à 34,00 € TTC, soit **3 244,00 € TTC encaissés**, dont la contribution à 60,41 % de marge brute vaut 3 244,00 ÷ 1,2 × 0,6041 = **1 633,08 € HT**. Le test le plus cher du dispositif est donc celui qui rapporte : les 3 487 € TTC dépensés sont compensés à 93 % par la trésorerie encaissée. **Et le coût d'un échec était borné d'avance** : 3 244 € à rembourser, 65,53 € de frais de prestataire non restitués, 2 000 € de média dépensé, soit **2 065,53 €** de coût direct.

### Partie 7 — Le verdict

**GO. 6 favorables sur 6**, pour une porte à 4. Les trois faits qui le portent : **un top 3 de défauts à 67,0 %, tous dans le produit**, qui donne trois lignes de cahier des charges opposables ; **une création concurrente diffusée depuis 412 jours**, preuve publique que la catégorie rembourse son coût d'acquisition ; **61 pré-commandes à 36,07 € pièce, dont 55,7 % en froid**, panier à 102,3 % de la cible, sans dépendance à la remise.

Le test le plus fragile est (e), porté par un seul angle sur trois : les douze concepts de [S06](S06-premier-lot-de-creas.md) seront bâtis sur la famille A1. Ce que je m'interdis d'invoquer pour ne pas appliquer un no-go : « les tests ne captent pas l'effet de marque », « il faut du temps », « mes proches adorent ça ».

> **La phrase honnête.** 6 sur 6 ne veut pas dire que ça marchera : **rien de ce qui est vérifiable avant de produire ne s'y oppose**, c'est tout. Les six tests éliminent des erreurs, ils ne créent pas de succès.

---

## 8. Les conséquences chiffrées de ton choix

Le dispositif coûte **3 500 € TTC et cinq semaines**. Combien coûte la même information plus tard ?

### 8.1 Les deux trajectoires

**Trajectoire V — tu fais les tests.** 3 487 € TTC, dont 3 244 € reviennent en pré-commandes encaissées. Si le verdict est go, tu entres en P1 avec trois lignes de cahier des charges chiffrées, un angle validé sur 1 186 visiteurs, 34 verbatims et un prix confirmé par 61 paiements réels.

**Trajectoire N — tu produis directement.** Deux fins.

| | V | N, arrêt lucide au M3 | N, sans critère d'arrêt, jusqu'au M9 |
|---|---:|---:|---:|
| Pertes cumulées d'exploitation | 0 € | **28 209 €** | **147 239 €** |
| Stock non récupérable | 0 € | 11 562 € | inclus au BFR |
| BFR immobilisé | 0 € | récupérable | 166 819 € |
| **Capital consommé** | **3 487 € TTC** | **39 771 €** | **314 058 €** |
| Temps perdu | 5 semaines | 3 mois | 9 mois |
| **Rapport au coût de S02** | **1** | **11** | **90** |

*Pertes canoniques : −9 403 €/mois en P1 sur trois mois, −19 838 €/mois en P2 sur six mois (§ 2.2). Les 39 771 € et 314 058 € viennent de [C02](../etudes-de-cas/C02-vallee-de-la-mort.md) : le seul montant certain d'un arrêt au M3, et le capital consommé au M9.*

**Contre les pertes cumulées de P1 et P2 — 147 239 € — le rapport est de 1 à 42.** C'est le cas courant : le fondateur sans critère d'arrêt écrit découvre le problème quand la trésorerie le lui apprend. Contre le capital réellement consommé, BFR compris, il monte à 1 à 90 ; même dans le meilleur cas — arrêt lucide au troisième mois — il reste de 1 à 11.

### 8.2 Ce que ça vaut vraiment

Les tests ne suppriment pas l'échec, ils réduisent sa probabilité.

*Si la probabilité d'échec au-delà du M3 passe de 70 % sans validation à 45 % avec, le gain espéré vaut 0,25 × 147 239 € = **36 810 €** pour 3 487 € TTC, soit **×10,6**. Dans l'hypothèse pessimiste où le dispositif ne gagne que 10 points : 0,10 × 147 239 € = **14 724 €**, soit **×4,2**.*

**Même au pire, le dispositif rapporte quatre fois son coût.** Et le calcul ignore deux effets qui vont dans le même sens : les lignes de cahier des charges de (c), qui améliorent le produit, et l'angle validé de (e), qui réduit le coût d'acquisition des premiers mois — celui-là même qui creuse les pertes de P1.

### 8.3 Le prix de la même information selon le moment

Le fait « le poste C, l'irritation, concentre 23,5 % du mécontentement du marché » se paie très différemment selon la date où on l'apprend : **0 €** au M0, par une semaine de dépouillement, le produit étant corrigé avant d'exister ; une reformulation, un lot invendable et 28 209 € de pertes déjà engagées au M3, par ses propres avis ; 147 239 € de pertes cumulées et la porte P1 → P2 fermée au M9, par un taux de première à deuxième commande sous 12 %.

**L'information est la même. Son prix est multiplié par 42.** C'est tout ce que cette séance a à dire.

---

## 9. Avant la séance suivante

**1. Mets tes lignes de cahier des charges au propre.** Exigence, vérification, seuil d'acceptation, par poste au-dessus de 12 %. C'est le document que [S03](S03-produit-et-cogs.md) enverra aux fournisseurs, et un fournisseur ne répond bien qu'à une spécification chiffrée.

**2. Classe tes verbatims.** Les 30 du test (d) plus ceux des avis, en deux piles : irritants (1–2 étoiles) et vocabulaire du bénéfice (5 étoiles). [S05](S05-recherche-client-et-angles.md) construira les angles dessus, et un angle sans verbatim se reconnaît immédiatement.

**3. Si ton verdict est no-go, reprends S01 sur ta deuxième finaliste.** Ne modifie pas le dispositif pour qu'il passe : recommence avec le même. Un no-go à 3 500 € TTC est le meilleur retour sur investissement de l'atelier, et le plus dur à accepter.

---

*Fin de la séance S02. Suite : [S03 — Le produit et le coût réel](S03-produit-et-cogs.md).*
