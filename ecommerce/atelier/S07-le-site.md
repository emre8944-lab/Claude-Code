# Séance S07 — Le site qui convertit

> **Niveau requis :** L03 · **Durée :** 9 h · **Livrable :** la page produit rédigée bloc par bloc — les textes, pas des intentions —, la grille de contrôle du dépôt remplie et notée, le plan de mesure vérifié par réconciliation · **Modules :** [E07](../modules/E07-funnel-et-conversion.md), [E09](../modules/E09-mesure-et-incrementalite.md)
> **Ce que tu ne peux pas faire sans avoir fait cette séance :** envoyer un euro de média. Sans page cohérente tu paies pour amener des gens devant une porte fermée ; sans mesure juste tu paies structurellement plus cher chaque client, tous les mois, et rien dans tes tableaux ne te le dira.

---

## 1. Où tu en es

Tu sors de [S06](S06-premier-lot-de-creas.md) avec douze concepts et douze accroches écrites mot pour mot. [S04](S04-offre-prix-et-panier.md) a fixé ta gamme, ton panier cible et le MER à tenir ; [S05](S05-recherche-client-et-angles.md) a produit tes trois angles, tes neuf preuves et tes dix-huit objections.

**Décidé :** ce que tu dis, à qui, avec quelles preuves, et ce que la commande moyenne doit contenir. **Pas décidé :** ce que voit la personne qui clique, dans quel ordre, avec quels mots — et si le système qui la compte compte juste.

Les deux moitiés de cette séance n'ont pas le même public. La première se voit et flatte : c'est la page. La seconde ne se voit pas et décide : c'est la mesure. L'ordre de grandeur avant de commencer ([E07 § 1.3](../modules/E07-funnel-et-conversion.md)) : à P5, **220 735 clics payés par mois n'atteignent jamais une session** — 2 330 964 € par an, dont 896 524 € récupérables par le seul temps de chargement, soit plus que les 432 000 € d'une baisse de 10 % des frais fixes ([canoniques § 7](../donnees/chiffres-canoniques.md)).

*Sigles : **TC** — taux de conversion. **LCP** — délai d'affichage du plus grand élément visible, au 75ᵉ centile. **CPA** — coût par achat.*

---

## 2. Ta mission

Un site qui convertit et qui compte juste. Pas un beau site : la beauté n'est mesurée nulle part dans la grille.

1. **La page produit de ta SKU d'atterrissage publicitaire, rédigée bloc par bloc** — treize blocs, chacun avec son texte définitif. Pas « on parlera de la garantie » : la phrase de garantie, écrite.
2. **Trois variantes de haut de page**, une par angle de [S05](S05-recherche-client-et-angles.md).
3. **La [grille de contrôle](../modeles/checklist-page-produit.md) du dépôt remplie**, notée sur 100, avec les cinq corrections prioritaires classées **par rendement par jour-homme**.
4. **Le tunnel spécifié** : étapes, champs, moyens de paiement, ce qui est annoncé et quand.
5. **Le budget vitesse** : LCP mesuré sur téléphone en 4G, cible, trois corrections, valeur en euros.
6. **Le plan de mesure** : cinq événements, envoi serveur, clé de déduplication, consentement, et **le tableau de réconciliation rempli d'une semaine réelle**.

---

## 3. Ce dont tu disposes

| Ressource | Usage |
|---|---|
| Ton livrable [S05](S05-recherche-client-et-angles.md) | Les objections par fréquence — le bloc 10 s'écrit de là, jamais d'imagination |
| Ton livrable [S06](S06-premier-lot-de-creas.md) | Les douze accroches. Le bloc 1 en est la reprise **mot pour mot** |
| Ton livrable [S04](S04-offre-prix-et-panier.md) | Gamme, prix, franco, MER seuil. Le bloc 4 est l'application de ce tableau |
| [`modeles/checklist-page-produit.md`](../modeles/checklist-page-produit.md) | **La grille : 11 sections, 100 points.** Livrable 3 de la séance |
| [E07 § 4.3](../modules/E07-funnel-et-conversion.md) et [§ 5.1](../modules/E07-funnel-et-conversion.md) | Les treize blocs et leur indicateur ; les cinq causes d'abandon dans l'ordre |
| [E09 § 7.7](../modules/E09-mesure-et-incrementalite.md) | Une source unique, un dictionnaire écrit, un propriétaire par chiffre |
| `python3 ecommerce/outils/calculateur.py` | Ta marge brute unitaire — le nombre par lequel se multiplie chaque commande gagnée ou perdue |
| `python3 ecommerce/outils/test_significativite.py` | Combien de conversions avant d'avoir le droit de conclure d'un test de page |

---

## 4. La méthode, pas à pas

### 4.1 Le minimum viable : ce qu'il faut, ce qui attend

Le site n'est pas ton goulot ; ta créa et ton offre le sont ([canoniques § 6](../donnees/chiffres-canoniques.md)). Ce qui suit sert à ne pas gaspiller ce que [S06](S06-premier-lot-de-creas.md) a produit.

| Brique | Avant le 1ᵉʳ euro de média | Coût (€ HT) | Délai |
|---|---|---:|---:|
| Page produit de la SKU d'atterrissage, treize blocs | **oui** | ton temps | 2 j |
| Trois variantes de haut de page, une par angle | **oui** | ton temps | 0,5 j |
| Tunnel : une page, ou trois étapes numérotées | **oui** | inclus | 0,5 j |
| Deux moyens de paiement, dont un portefeuille mobile | **oui** | 1,70 % + 0,25 €/cmd | 1 j |
| Mentions légales, CGV, rétractation 14 j **distincte** de la garantie | **oui** | 0 à 400 € | 1 j |
| Consentement où refuser coûte un clic, comme accepter | **oui** | 0 à 20 €/mois | 0,5 j |
| Cinq événements, envoi serveur, déduplication (§ 4.6) | **oui** | 0 à 30 €/mois | 2 j |
| Confirmation de commande et suivi d'expédition automatiques | **oui** | inclus | 0,5 j |
| Identité : société, adresse, contact, délai de réponse | **oui** | 0 | 0,5 j |
| Relance de panier, trois messages ([modèle](../modeles/sequences-crm.md)) | **oui** | 20 à 40 €/mois | 1 j |
| Module d'avis vérifiés | non — tu n'as aucun avis | 30 à 90 €/mois | à J+45 |
| Fidélité, chat, blog, version anglaise, quiz de diagnostic | non | — | à P2 |
| Refonte graphique, charte complète, application mobile | non | — | jamais à ce stade |

**Neuf jours-homme et moins de 500 € HT.** La faute classique n'est pas de mal faire le haut de la liste : c'est de commencer par le bas.

### 4.2 La page bloc par bloc, dans l'ordre de lecture

Sur téléphone, à une main, en 4G. Chaque bloc répond à **une** question, a **un** indicateur, et renvoie à une section de la [grille de contrôle](../modeles/checklist-page-produit.md).

| # | Bloc | Question traitée | Indicateur | Grille |
|---|---|---|---|---|
| 1 | Promesse, reprise mot pour mot de l'annonce | Suis-je au bon endroit ? | Rebond sous 5 s | A1, A3 |
| 2 | Preuve visuelle : produit en main, démonstration | Est-ce que ça a l'air réel ? | Scroll > 25 % | A2, A4 |
| 3 | Note et nombre d'avis, une ligne, cliquable | D'autres l'ont fait ? | Clic sur la note | B1 |
| 4 | **Offre et prix**, cible présélectionnée, prix à l'usage | Quoi, et combien ? | Part de la SKU cible dans les ajouts | G1–G4 |
| 5 | Bouton visible sans scroll, qui dit la suite | Passage à l'acte précoce | Ajouts du 1ᵉʳ écran | A5, A7, A8 |
| 6 | Réassurance : port, retour, paiements, délai | Que va-t-on m'ajouter ? | Abandon au paiement | A9, H1 |
| 7 | Trois avis pour **trois objections différentes** | Pour quelqu'un comme moi ? | Temps sur la section | B2, B3 |
| 8 | Mécanisme : pourquoi ça marche, en trois étapes | Pourquoi y croire ? | Scroll jusqu'au bloc | C1, C2 |
| 9 | Preuve dure : protocole, effectif, date | Doute rationnel | Taux de lecture | C3 |
| 10 | Objections une par une, en accordéon | Les raisons de ne pas acheter | Ouverture par objection | D1–D6 |
| 11 | Garantie, **après** le mécanisme | Et si ça rate ? | Ajouts après exposition ; retours | E1–E3 |
| 12 | Questions fréquentes : délai, usage, taille, retour | Ce qui partirait au SAV | Tickets avant-vente | F1–F5 |
| 13 | Rappel d'offre et bouton final | Rattraper le lecteur long | Ajouts du bas de page | I7 |

**Le bloc 4 est le levier, pas le bloc 5.** [Canoniques § 7](../donnees/chiffres-canoniques.md) : +10 % de panier moyen vaut 3 139 401 € d'EBITDA annuel, +10 % de conversion 2 662 749 € — **17,9 % de plus pour le sélecteur d'offre que pour le bouton.** Une page qui met l'unité en avant et relègue le lot en bas est arithmétiquement une page à petit panier.

**Le bloc 11 vient après le bloc 8, jamais avant.** Une garantie annoncée d'entrée dit que le produit en a besoin ; après le mécanisme, elle dit que tu es sûr de toi.

**Le bloc 10 se recopie, il ne s'invente pas** : les mots de [S05](S05-recherche-client-et-angles.md), par fréquence décroissante. C'est le seul travail réellement sérieux d'une page produit, et celui que personne ne fait, parce qu'il consiste à recopier des choses désagréables que des inconnus ont écrites sur ta catégorie.

### 4.3 La continuité annonce → page : combien de pages maintenir ?

Le visiteur arrive avec une attente formée moins d'une seconde plus tôt. La première tâche de la page n'est pas de convaincre, c'est de **confirmer qu'il est au bon endroit** — avant cette confirmation, aucun argument n'est lu. D'où le résultat que tout le monde trouve faux et qui est arithmétique : **une excellente page générique convertit moins bien qu'une page moyenne mais cohérente.**

*Hypothèses ([E07 § 2.1](../modules/E07-funnel-et-conversion.md)) : une rupture entre l'annonce et le haut de page fait passer le rebond immédiat de 22 % à 44 %. La générique est objectivement meilleure : sur les visiteurs qui restent, elle convertit 15 % de mieux.*

```
Cohérente, notée 68/100 : 100 visiteurs → 78 restent → 2,31 % → 1,80 commande
Générique, notée 85/100 : 100 visiteurs → 56 restent → 2,66 % → 1,49 commande
Écart : −17,2 % pour la page objectivement meilleure.
```

Dix-sept points de qualité perdus contre vingt-deux points de rebond gagnés. La générique est bonne pour un visiteur moyen qui n'existe pas.

Combien de pages ? Pas une par concept — tu en as douze et tu en auras soixante avant la fin de l'année ([S06 § 8.1](S06-premier-lot-de-creas.md)). **Une par angle**, parce que la promesse est portée par l'angle et non par la variation.

```
Parc de départ = 3 pages d'angle + 1 générique + 1 du palier supérieur = 5 pages
Coût : trame 8 h + 3 déclinaisons × 2,5 h + 5 × 0,5 h/mois × 12
       = 45,5 h la première année, à 45 €/h                           = 2 048 €
```

À P5, le même calcul donne 69 pages, 1,34 ETP, rendement ×29 ([E07 § 2.2](../modules/E07-funnel-et-conversion.md)). Au lancement le rendement est plus faible — la trame est un coût fixe amorti sur peu de trafic — et il monte à chaque euro de média ajouté. **Trois pages, pas douze, pas une.**

### 4.4 Le tunnel : les cinq causes d'abandon, dans l'ordre

L'ordre compte plus que la liste : c'est celui des euros.

| Rang | Cause | Le correctif, précisément |
|---|---|---|
| 1 | **Port découvert tard** | Annoncé **sur la fiche**, bloc 6. Ce n'est pas le montant qui fait fuir, c'est la modification d'un prix mémorisé : 4,90 € annoncés coûtent moins que 2,90 € révélés à l'étape 3 |
| 2 | **Compte obligatoire** | Paiement invité par défaut ; le compte se propose **après**, adresse et courriel déjà saisis. Une case, pas un mur |
| 3 | **Moyen de paiement absent** | Carte + un portefeuille mobile dès le départ, le moyen local dominant dès l'ouverture d'un marché. Un bouton manquant vaut 824 599 € HT/an aux Pays-Bas à P5 ([E07 § 5.3](../modules/E07-funnel-et-conversion.md)) |
| 4 | **Délai de livraison** | Fourchette courte, en jours ouvrés, au bloc 6 et répétée à l'étape 1. « 3 à 10 jours » se lit « 10 » |
| 5 | **Doute sur le retour** | Trois lignes dans le tunnel : qui paie, sous quel délai, comment. Pas un lien vers les CGV |

Deux règles de structure : **une page, ou trois étapes numérotées avec récapitulatif permanent** — la question « combien reste-t-il d'étapes » fait abandonner à elle seule ; **aucun champ de code promo visible avant le paiement** — un champ vide envoie chercher un code ailleurs, et on ne revient pas toujours.

```
Commandes gagnées/mois = débuts de paiement × points de taux récupérés
Valeur annuelle        = commandes gagnées × marge brute unitaire × 12
```

### 4.5 La vitesse : ce qu'on mesure, les seuils, les trois corrections

**Ce qu'on mesure :** le LCP au 75ᵉ centile, sur téléphone, en 4G, sur données de terrain — pas depuis ton poste en fibre, qui mesure ton bureau. Repère public : **≤ 2,5 s** (Core Web Vitals, Google). Au-delà de 4 s, tu ne travailles plus la conversion, tu travailles la perte de clics.

**Les trois corrections, par rendement.** *Un :* les **images du premier écran** — format moderne, dimensionnées à la taille réellement affichée, une seule bloquante. Premier poste d'effet, toujours, une demi-journée. *Deux :* les **scripts tiers** — inventaire écrit, un propriétaire nommé par ligne, et pour chacun « qu'est-ce qui casse si je le retire ? ». Tout script sans réponse est retiré ; personne n'est jamais chargé d'en enlever, donc ils s'accumulent. *Trois :* les **polices et les applications de la boutique** — aucune police chargée avant le premier rendu, aucune application exécutée sur un gabarit où elle ne sert pas.

Le rendement est calculé au § 8, aux trois paliers. Il est le plus élevé du cursus et le moins glorieux : **le rendement d'un chantier est inversement proportionnel au nombre de gens qui veulent y être associés.**

### 4.6 La mesure — le seul chantier de cette séance qui se paie en CAC

Une marque qui mesure mal ne se trompe pas seulement dans ses tableaux : **elle paie structurellement plus cher son acquisition, tous les mois, sans qu'aucun indicateur ne le signale.** Les six gestes, puis la démonstration.

**(a) La source de vérité est ton back-office, jamais une régie.** Le nombre de commandes du mois est celui de ta base, net des annulations. Les plateformes sont des **entrées**, jamais la référence ([E09 § 7.7](../modules/E09-mesure-et-incrementalite.md)). Un chiffre qui n'en sort pas n'entre pas dans une décision, capture d'écran comprise.

**(b) Cinq événements, pas quarante.** `page_vue`, `produit_vu`, `ajout_panier`, `debut_paiement`, `achat` — avec valeur, devise, et identifiant de commande sur `achat`. Quarante événements ne donnent pas quarante fois plus d'information : quarante fois plus de surface de panne, et personne ne les vérifie.

**(c) Double envoi, navigateur *et* serveur.** Le navigateur seul perd les blocages d'extensions, les fermetures d'onglet et les restrictions de suivi ; le serveur seul perd le haut de parcours et une partie de l'appariement. `achat` part du serveur **au moment où le paiement est confirmé**, pas au chargement de la page de remerciement, qu'un client sur dix ne voit jamais.

**(d) La déduplication : un identifiant d'événement partagé.** Navigateur et serveur envoient le **même** `id_evenement` pour le même achat, généré une fois et stocké avec la commande. Sans cette clé, la plateforme compte deux conversions pour une vente. Ce n'est pas bénin : c'est **la seule erreur de mesure qui te fasse dépenser plus au lieu de moins**, parce qu'elle divise ton CPA apparent par deux et t'invite à accélérer.

**(e) Le consentement.** Refuser coûte exactement un clic, comme accepter — c'est la loi, et c'est la condition pour que ton taux de consentement soit un chiffre honnête. **L'envoi côté serveur n'est pas un moyen de contourner un refus.** Un visiteur qui a refusé le suivi publicitaire ne part pas côté serveur non plus : ce que le serveur récupère, ce sont les événements des visiteurs **consentants** que le navigateur a perdus pour des raisons techniques. Écris cette phrase dans ton plan de mesure, datée. Le jour d'un contrôle, elle vaut plus que ton chiffre d'affaires du mois.

**(f) La vérification, chaque semaine, en un tableau.** La partie que tout le monde saute, la seule qui prouve quelque chose. Trois seuils, écrits avant de regarder : **≥ 95 %**, la mesure est saine, on décide avec ; **85 à 95 %**, réparation ouverte sous quinze jours, on décide en sachant que le CPA affiché est surestimé du complément ; **< 85 %**, **on ne monte aucun budget** — c'est conduire en lisant un compteur qui affiche 70 % de la vitesse.

**(g) Ce que coûte une mesure fausse.** Le modèle d'enchère d'une plateforme a besoin d'un nombre minimal de conversions par semaine et par unité optimisée pour cesser d'explorer au hasard : de l'ordre de **50**. C'est une valeur d'interface, elle changera ; le mécanisme, lui, ne changera pas — un modèle a besoin d'exemples. Et il ne compte que les conversions **qu'il reçoit**.

```
Taux de remontée r = achats dédupliqués ÷ commandes du back-office
Budget minimal lisible / semaine = (50 ÷ r) × CPA

Avec un CPA de lancement de 35,93 € HT :
  r = 100 %  →  50 cmd/sem  →  1 797 € HT/sem     référence
  r =  88 %  →  57 cmd/sem  →  2 042 € HT/sem     +13,6 %
  r =  55 %  →  91 cmd/sem  →  3 267 € HT/sem     +81,8 %
  r =  40 %  → 125 cmd/sem  →  4 491 € HT/sem     +150,0 %
```

**Un taux de remontée de 55 % multiplie par 1,82 le budget minimal nécessaire au même signal** : sur trente jours, 14 000 € HT au lieu de 7 698 € HT, soit **6 302 € HT brûlés pour rien**, au moment où tu en as le moins. Le second effet est pire. Les visiteurs dont l'événement remonte ne sont pas un échantillon aléatoire des acheteurs ; le modèle apprend sur une sous-population, puis va en chercher d'autres qui lui ressemblent. **Tu ne paies pas seulement plus cher : tu paies plus cher pour cibler moins bien.**

*Hypothèse déclarée, non mesurable en test A/B — on ne mesure pas avec un instrument cassé la valeur de le réparer : passer de 55 % à 88 % de couverture vaut 6 % de CAC.* Aux [canoniques § 7](../donnees/chiffres-canoniques.md), −10 % de CAC vaut 1 793 047 € d'EBITDA annuel à P5 ; **−6 % en vaut 1 075 828 € par an.** Pour deux jours d'intégration.

---

## 5. Ton livrable

```
SKU d'atterrissage : ..........  Prix TTC : ......  Angle : ......

BLOC 1  Titre (≤ 12 mots, repris de l'accroche n° ...) : ....................
        Sous-titre (bénéfice daté ou chiffré) : ............................
BLOC 2  Visuel : ......  Ce qu'il montre : ......  Repris de l'annonce ? O/N
BLOC 3  Ligne de note : ............................................
BLOC 4  Offre 1 : ....  TTC : ....  Prix à l'usage : ....
        Offre 2 (présélectionnée) : ....  TTC : ....  Économie affichée : ....
        Offre 3 : ....  TTC : ....  Économie affichée : ....
BLOC 5  Texte du bouton : ....................................
BLOC 6  Port : ....  Franco : ....  Délai : ....  Retour : ....  Paiements : ....
BLOC 7  Avis 1 (objection ....) / Avis 2 (objection ....) / Avis 3 (objection ....)
BLOC 8  Étape 1 : ....  Étape 2 : ....  Étape 3 : ....  Nom du mécanisme : ....
BLOC 9  Preuve dure : protocole ....  effectif ....  date ....  résultat ....
BLOC 10 Objection 1 (fréq. ... %) : ....  Réponse : ....        [× 5 ou 6]
BLOC 11 Garantie : durée ....  conditions ....  taux d'équilibre ... %
BLOC 12 Cinq questions issues du corpus S05, avec réponses
BLOC 13 Rappel d'offre : ....  Texte du bouton final : ....

Variantes de haut de page : angle A1 ....  A2 ....  A3 ....
Tunnel : étapes ....  champs étape 1 ....  compte obligatoire O/N
Moyens de paiement : ....   Port et délai annoncés au bloc 6 : O/N
LCP (mobile, 4G, 75ᵉ c.) : ... s   Cible : ... s   Valeur de l'écart : ... € HT/an
Trois corrections vitesse : 1) ....  2) ....  3) ....
Source de vérité : ....   Cinq événements : ....   Envoi serveur sur : ....
Clé de déduplication : ....   Refus en 1 clic : O/N   Consentement mesuré : ... %
Phrase signée : « aucun événement n'est envoyé, navigateur ou serveur, pour un
visiteur ayant refusé le suivi publicitaire. »            Date : ....
```

| Section de la grille | A | B | C | D | E | F | G | H | I | J | K | **Total** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Poids | 18 | 10 | 8 | 12 | 6 | 5 | 15 | 12 | 7 | 5 | 2 | **100** |
| Obtenu | | | | | | | | | | | | |

| Correction prioritaire | Section | Hypothèse d'effet | € HT/mois | j-h | **€ / j-h** |
|---|---|---|---:|---:|---:|

| Semaine | Navigateur | Serveur | Après dédup. | Back-office | Remontée | Décision |
|---|---:|---:|---:|---:|---:|---|

---

## 6. La grille d'évaluation

Barème sur 100, **seuil de validation 75** — plus haut que celui de [S06](S06-premier-lot-de-creas.md), parce que cette séance est la dernière porte avant la dépense : [S08](S08-le-lancement.md) construit un plan de lancement qui suppose cette page et cette mesure en place.

| # | Critère | Pts | Ce qui vaut les points | Ce qui les fait perdre |
|---|---|---:|---|---|
| 1 | **Treize blocs rédigés** | 20 | Texte définitif dans chacun, pas une intention | Bloc décrit au lieu d'être écrit : −3 chacun ; bloc absent : −4 |
| 2 | **Continuité annonce → page** | 12 | Trois variantes de haut de page, accroche reprise **mot pour mot** | Synonymes au lieu des mots exacts : −6 ; page unique pour 12 concepts : −12 |
| 3 | **Bloc 4 : offre et paliers** | 14 | Trois formats achetables, cible présélectionnée, prix à l'usage, économie chiffrée | SKU unique achetable : **éliminatoire** ; cible non présélectionnée : −5 |
| 4 | Bloc 10 : objections | 10 | 5 ou 6 objections, **par fréquence mesurée** en S05, réponses rédigées | Objections inventées, sans fréquence : −7 |
| 5 | Blocs 8 et 9 | 8 | Mécanisme nommé en 3 étapes ; preuve avec protocole, effectif et date | Liste d'ingrédients ou de caractéristiques : −5 |
| 6 | Grille de contrôle | 10 | 11 sections notées, total, 5 corrections classées par € / j-h | Corrections classées par gain absolu : −4 ; grille non remplie : −10 |
| 7 | **Tunnel spécifié** | 10 | Étapes, champs, paiements, port et délai annoncés au bloc 6 | Compte obligatoire : −6 ; port révélé à l'étape 3 : −6 |
| 8 | Vitesse | 6 | LCP mesuré sur mobile en 4G, cible, 3 corrections, valeur annuelle | LCP mesuré sur ordinateur : −4 ; non chiffré en euros : −3 |
| 9 | **Mesure et réconciliation** | 10 | 5 événements, envoi serveur, clé de dédup., consentement, **tableau rempli sur une semaine réelle** | Tableau vide : **éliminatoire** ; dédup. non spécifiée : −6 |

**Quatre fautes éliminatoires.** **Un tableau de réconciliation non rempli** — tu déclares une mesure que tu n'as pas vérifiée, et tout le cursus s'appuiera dessus. **Une SKU unique achetable sur la page d'atterrissage** — tu as travaillé ton panier cible en [S04](S04-offre-prix-et-panier.md) pour rien, et ton MER seuil redevient celui de l'unité. **Une promesse que l'annonce ne fait pas, ou l'inverse** — tu achètes un clic pour produire une déception, et tu la paies deux fois. **Un envoi serveur qui contourne un refus de consentement** — faute réglementaire, et elle invalide la mesure qu'elle prétend améliorer.

---

## 7. Le corrigé exemplaire

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle. Le résultat de panel du bloc 9 est un chiffre **modélisé** pour les besoins de l'exercice.

**KALIS**, la marque des corrigés de [S03](S03-produit-et-cogs.md) à [S06](S06-premier-lot-de-creas.md) — chaussettes de course techniques. Données d'entrée : SKU d'atterrissage **pack de 3 à 45,00 € TTC**, gamme 18,00 € / 45,00 € / 78,00 €, franco à 69,00 €, port 4,90 € TTC, **marge brute 28,87 € HT par commande** au panier cible de 57,48 € TTC, MER seuil 2,11, MER atteignable 2,20. Angle de la page principale : **A1 « Ce n'est pas ta chaussure »**, celui du concept C02 de [S06](S06-premier-lot-de-creas.md).

**KALIS n'a aucun avis client** — elle n'a pas encore vendu. Le corrigé montre ce qu'on met dans les blocs 3 et 7 ce jour-là, et la grille est notée en conséquence, sans complaisance.

### 7.1 La page, rédigée

**BLOC 1.** L'annonce C02 s'ouvre sur deux secondes muettes : une chaussette de coton et une chaussette KALIS sur une balance, après trente minutes de course. Puis la voix. La page reprend ces mots exactement, sans les améliorer.

> # Ce n'est pas ta chaussure qui te fait des ampoules.
> C'est la chaussette qui a pris 29 grammes d'eau, et qui glisse dessous.

**BLOC 2.** La photographie de la balance — la vignette de l'annonce — en premier écran : deux chaussettes, deux affichages, **38 g** et **9 g**. Aucune légende : l'image est la légende.

**BLOC 3.** Pas d'avis, donc pas de fausse note. On met ce qu'on a, daté et vérifiable :

> **40 coureurs, 6 semaines de test, 3 100 km cumulés.** Protocole complet plus bas.

**BLOC 4.** Pack de 3 présélectionné, pack de 6 le plus visible, chaque ligne portant son prix à l'usage.

| | Prix TTC | À la paire | Par sortie (3/sem., 6 mois) | |
|---|---:|---:|---:|---|
| 1 paire | 18,00 € | 18,00 € | 0,23 € | |
| **3 paires** | **45,00 €** | **15,00 €** | **0,19 €** | **présélectionné** |
| 6 paires | 78,00 € | 13,00 € | **0,10 €** | **économisez 30,00 €** |

> Une paire dure 5 à 7 mois à trois sorties par semaine. Trois paires, c'est une rotation complète : une aux pieds, une au lavage, une au sec.

**BLOC 5.** → *Ajouter les 3 paires — 45,00 € · expédié demain, livré en 2 à 3 jours ouvrés*

**BLOC 6.** Sous le bouton, une ligne, quatre informations, aucun lien à cliquer :

> Livraison 4,90 € TTC · offerte dès 69,00 € · 2 à 3 jours ouvrés en France · retour gratuit sous 30 jours, même portées et lavées · carte bancaire et portefeuille mobile.

**BLOC 7.** Les testeurs du panel, nommés, avec leur profil et l'objection qu'ils traitent — pas trois inconnus qui disent « super produit ».

> **« J'ai fait un semi sans y penser. »** — Rachid, 41 ans, 4 sorties/semaine. *(ça marche ?)*
> **« Je fais du 39, j'ai toujours du tissu qui plisse sous l'orteil. Là, non. »** — Léa, 28 ans, trail. *(pas pour moi ?)*
> **« 15 € la paire, j'ai tiqué. Puis j'ai calculé ce que j'avais jeté en un an. »** — Marc, 52 ans. *(c'est cher ?)*

**BLOC 8.**

> ### Pourquoi ça marche : la maille sèche et le maintien
> **1. Le coton absorbe.** Après trente minutes, une chaussette de coton a pris jusqu'à quatre fois son poids en eau. Elle devient molle et lourde.
> **2. Ce qui est mouillé glisse.** Une chaussette gorgée d'eau se déplace de quelques millimètres à chaque foulée, entre la peau et la chaussure. C'est ce frottement — le cisaillement — qui décolle l'épiderme. Pas ta chaussure.
> **3. Ce qui ne bouge pas ne frotte pas.** La maille KALIS évacue au lieu d'absorber : 9 g contre 38 g au même moment. Le maintien de voûte, **tricoté et non cousu**, l'empêche de se déplacer.
> Sèche et immobile : le cisaillement n'a plus de support.

**BLOC 9.**

> **Le test.** 40 coureurs, 6 semaines, mars-avril, 3 100 km cumulés. Chacun a couru une semaine sur deux avec ses chaussettes habituelles, une semaine sur deux avec les nôtres, et rempli la même fiche après chaque sortie de plus de 90 minutes.
> **Le résultat.** Sur les sorties longues : **34 coureurs sur 40 déclarent zéro ampoule** avec les nôtres, **19 sur 40** avec les leurs.
> **Ce que ça ne dit pas.** Le test n'est pas en aveugle : chacun savait ce qu'il portait. Nous le publions quand même, avec ses limites, parce qu'un chiffre honnête vaut mieux qu'un superlatif.

**BLOC 10.** Six objections, par fréquence mesurée dans le corpus de 412 avis de [S02](S02-prouver-la-demande.md), en accordéon, fermées.

| Objection (fréq.) | La réponse écrite sur la page |
|---|---|
| **Trouées au talon (31,3 %)** | Talon et pointe en polyamide 6.6 renforcé, sur 30 % de la surface. Notre cahier des charges fournisseur : zéro perforation après 40 lavages à 40 °C et 200 km. Si la tienne se troue avant six mois, on la remplace. |
| **L'élastique va lâcher (22,1 %)** | Le maintien est **tricoté dans la maille**, pas cousu par-dessus. Perte de rétraction sur banc : moins de 8 % après 40 lavages. C'est le point sur lequel nous avons changé de fournisseur. |
| **15 € la paire, c'est cher (transversale)** | Cinq paires de coton à 7,00 € durent 3 mois : 52,00 € sur l'année. Trois KALIS à 15,00 € durent 6 mois : 36,00 € sur l'année. **0,10 € par sortie.** |
| **Pas pour moi — la taille (9,7 %)** | Trois tailles, et la longueur de pied en centimètres publiée pour chacune : pas une pointure, une mesure. Une feuille, un crayon, ta longueur de pied — le tableau est en dessous. |
| **Ça va sentir (12,9 %)** | Traitement anti-odeur mesuré après 6 heures d'effort contre témoin. C'est l'exigence que nous avons failli abandonner pour tenir le prix ; nous l'avons gardée. |
| **Qui êtes-vous ? (jamais écrite dans les avis)** | KALIS, [adresse complète], fabriqué au Vietnam dans l'usine [nom], contrôlée sur place. Une adresse, un numéro, une réponse sous 24 h ouvrées. |

**BLOC 11.**

> **Trente jours, portées, lavées, courues.** Tu les mets, tu cours avec, tu les laves. Si elles ne tiennent pas ce que dit cette page, tu nous les renvoies — retour payé par nous — et on te rembourse. Sans photo, sans motif, sans discussion.

Le taux de réclamation d'équilibre, calculé **avant** de l'écrire :

```
Marge brute par commande                                        = 28,87 € HT
Coûts variables non récupérés (COGS non revendable 40 %,
   logistique aller + retour)                                   = 13,10 € HT
Perte par remboursement            = 28,87 + 13,10              = 41,97 € HT
Hypothèse : la garantie apporte +6 % de commandes
Seuil d'équilibre = 0,06 × 28,87 ÷ 41,97                        =  4,13 %
```

**KALIS supporte 4,13 % de remboursements avant que la garantie ne devienne perdante**, pour un taux de retour modélisé de 3,0 %. La marge est mince : ce chiffre passe sous surveillance hebdomadaire dès la première commande, et la garantie est le premier levier à retirer s'il dépasse 4,1 %.

**BLOC 12.** Cinq questions, dans l'ordre où elles se poseront : taille et mesure en centimètres · délai et transporteur · lavage (40 °C, pas de sèche-linge, pas d'adoucissant — l'adoucissant tue la maille) · à partir de quelle distance c'est utile · comment retourner.

**BLOC 13.** Reprise du tableau du bloc 4, pack de 3 toujours présélectionné, même texte de bouton. Barre collante prix + bouton au scroll à partir du bloc 7.

### 7.2 Les trois variantes de haut de page

| Angle | Accroche de l'annonce, reprise en titre | Visuel du 1ᵉʳ écran |
|---|---|---|
| **A1** — cisaillement et humidité | « Ce n'est pas ta chaussure qui te fait des ampoules. » | La balance, 38 g / 9 g |
| **A2** — reprise élastique morte | « Le trou n'est pas une question de qualité. » | Le bord-côte étiré qui reprend sa forme |
| **A3** — dénominateur | « Dix centimes par sortie. » | Deux tas : 5 paires de coton, 3 KALIS, et « 0,10 € » |

Blocs 4 à 13 identiques dans les trois. **Seuls les blocs 1, 2 et l'ordre du bloc 10 changent** — sur A2, « l'élastique va lâcher » remonte en première position. Coût des deux déclinaisons : 5 heures.

### 7.3 Le tunnel et la vitesse, chiffrés

Trois étapes numérotées, récapitulatif permanent avec le port déjà inclus, paiement invité par défaut, compte proposé **après** la confirmation. Sept champs à l'étape 1, un par ligne, clavier adapté, autocomplétion d'adresse. Carte et portefeuille mobile. Aucun champ de code promo avant l'étape 3, replié.

*Chaîne au lancement, hypothèses : CPM 9,00 € HT, CTR 1,44 %, 87 % des clics atteignent la session, TC payant 2,00 %.* Sur 7 800 € HT de média par mois : 866 667 impressions, 12 471 clics à 0,63 €, **10 850 sessions à 0,72 €**, 976 ajouts au panier (9,0 %), 434 débuts de paiement (44,5 %), **217 commandes (50,0 %)**. Le passage début de paiement → commande à 50,0 % est le point faible : le repère de [E07 § 1.1](../modules/E07-funnel-et-conversion.md) est 62,0 %. Douze points, répartis sur les cinq causes du § 4.4 :

| Cause | Points | Cmd/mois | **€ HT/an** | Effort |
|---|---:|---:|---:|---:|
| 1. Port découvert à l'étape 3 → annoncé au bloc 6 | 5,0 | 21,7 | **7 518 €** | 0,25 j |
| 2. Compte obligatoire → paiement invité | 3,0 | 13,0 | **4 504 €** | 0,25 j |
| 3. Portefeuille mobile absent | 2,0 | 8,7 | **3 014 €** | 1 j |
| 4. Délai non annoncé → fourchette bloc 6 et étape 1 | 1,5 | 6,5 | **2 252 €** | 0,10 j |
| 5. Retour non expliqué dans le tunnel | 0,5 | 2,2 | **762 €** | 0,10 j |
| **Total** | **12,0** | **52,1** | **18 050 €** | **1,7 j** |

**18 050 € HT par an pour un jour et sept dixièmes**, dont 12 022 € pour la demi-journée des deux premières lignes. Aucune de ces corrections n'est visible sur une capture d'écran.

**La vitesse.** LCP mobile 4G au 75ᵉ centile : **4,2 s**, cible **2,3 s**. Images du premier écran −1,1 s ; sept scripts tiers inventoriés, quatre retirés dont deux dont personne ne connaissait l'usage, −0,5 s ; police non bloquante et application de fidélité désactivée sur le gabarit produit, −0,3 s. **Total −1,9 s.**

```
Hypothèse (E07 § 6.1, plus prudente que le chiffre public) : −1 s = +10 % relatif
Effet conversion = 217 × 19 % = 41,2 cmd/mois × 28,87 € × 12  = 14 273 € HT/an
Clics récupérés  = 7 800 € × 5 % × 12                         =  4 680 € HT/an
Total 18 953 € HT/an · coût 2,5 j-h = 1 250 € · rendement = ×15,2
```

**N'additionne pas** ce gain avec celui du tableau ci-dessus : les deux portent en partie sur les mêmes commandes ([E07 § 9](../modules/E07-funnel-et-conversion.md)). On chiffre un par un, on fait dans l'ordre du rendement, **et on re-mesure la base après chacun**.

### 7.4 La mesure de KALIS, vérifiée

Source de vérité : la base de commandes, nette des annulations sous 14 jours. Cinq événements. `achat` envoyé côté serveur à la confirmation du paiement, `id_evenement` = identifiant de commande, le même que celui du navigateur.

| Semaine | Navigateur | Serveur | Après dédup. | Back-office | Remontée | Décision |
|---|---:|---:|---:|---:|---:|---|
| S1 | 28 | 0 | 28 | 51 | **54,9 %** | < 85 % : budget gelé. Envoi serveur non branché, chantier ouvert |
| S2 | 29 | 96 | **96** | 53 | **181,1 %** | Dédup. cassée : `id_evenement` régénéré côté serveur. Envoi serveur coupé le jour même |
| S3 | 31 | 54 | 55 | 58 | **94,8 %** | Zone 85–95 % : on décide, en sachant le CPA affiché surestimé de 5,5 % |
| S4 | 30 | 53 | 54 | 55 | **98,2 %** | ≥ 95 % : mesure saine. Le budget peut monter |

**Lis la semaine 2 deux fois.** 181 % n'est pas un bon chiffre : c'est la panne la plus chère du tableau. Sans le back-office en regard, KALIS voyait **96 conversions pour 1 796 € HT de média**, soit un CPA affiché de **18,71 €** — très sous son plafond de contribution de 28,87 € — quand le CPA réel était de **33,89 €**, au-dessus. Contribution apparente +973 €, contribution réelle −27 €. Le fondateur qui ne tient pas ce tableau triple son budget la semaine suivante, sur une conversion qui n'existe pas.

Taux de consentement mesuré : **71 %**. La phrase est écrite et datée : *aucun événement n'est envoyé, navigateur ou serveur, pour un visiteur ayant refusé le suivi publicitaire.* Les 29 % manquants ne sont pas récupérés — ils sont **modélisés** dans le tableau de bord, et jamais renvoyés à la régie.

### 7.5 La grille de contrôle de KALIS

**A 16/18 · B 5/10 · C 8/8 · D 10/12 · E 6/6 · F 4/5 · G 14/15 · H 9/12 · I 6/7 · J 3/5 · K 2/2 — total 83/100.**

Ce qui échoue, et pourquoi c'est assumé : **B 5/10**, aucun avis, aucun volume, aucune date — incompressible avant la première vente, et correction n° 1 à J+45. **H 9/12**, portefeuille mobile pas encore branché. **J 3/5**, chantier vitesse planifié, pas fait au jour de la notation. **D 10/12**, deux objections du corpus restent sans preuve dure. Aucune section sous la moitié de son poids, donc pas de plafonnement à 69. **83/100 : « page correcte »** — la règle du modèle est alors *corrige les deux points les plus chers, puis laisse-la et va travailler la créa ou l'offre.*

| Correction | Section | € HT/mois | j-h | **€ / j-h** |
|---|---|---:|---:|---:|
| Port annoncé au bloc 6 + paiement invité | H1, H2 | 1 002 € | 0,5 | **2 004 €** |
| Délai et retour dans le tunnel | H1, F5 | 251 € | 0,2 | **1 255 €** |
| Chantier vitesse, 4,2 s → 2,3 s | J1–J5 | 1 579 € | 2,5 | 632 € |
| Portefeuille mobile | H3 | 251 € | 1,0 | 251 € |
| Collecte d'avis dès la 1ʳᵉ commande (relance J+21) | B1–B4 | *à mesurer* | 1,0 | *—* |

**Les deux premières lignes valent 15 036 € HT par an pour sept dixièmes de journée** — le meilleur rendement de tout le dossier KALIS, et la ligne que personne ne met dans un plan de refonte, parce qu'elle ne se photographie pas.

---

## 8. Les conséquences chiffrées de ton choix

### 8.1 Ce que vaut un point de taux de conversion

*Hypothèse commune, tirée de [E07 § 1.2](../modules/E07-funnel-et-conversion.md) : TC global 2,50 %, donc sessions = commandes ÷ 2,50 %. Marge brute unitaire dérivée du canonique : marge brute mensuelle ÷ commandes.*

| | **P2** | **P3** | **P5** |
|---|---:|---:|---:|
| Commandes / mois ([canoniques § 2](../donnees/chiffres-canoniques.md)) | 4 000 | 18 000 | 60 200 |
| AOV mixte TTC | 57,55 € | 65,40 € | 71,98 € |
| **Marge brute unitaire HT** | **28,20 €** | **32,89 €** | **36,86 €** |
| Sessions / mois (dérivé) | 160 000 | 720 000 | 2 408 000 |
| +1 point de TC → commandes / mois | 1 600 | 7 200 | 24 080 |
| **Valeur annuelle d'un point de TC** | **541 430 €** | **2 841 758 €** | **10 650 994 €** |
| Valeur annuelle de 0,1 point | 54 143 € | 284 176 € | 1 065 099 € |
| EBITDA annuel du palier | −238 056 € | 612 396 € | 4 377 024 € |
| **Un point de TC, rapporté à l'EBITDA** | **la survie** | **×4,64** | **×2,43** |

*Contrôle : +10 % de TC, soit +0,25 point, vaut 2 662 749 € aux [canoniques § 7](../donnees/chiffres-canoniques.md). Quatre fois cette valeur donne 10 650 996 € — l'écart est un arrondi.*

**En euros absolus, un point vaut 19,7 fois plus à P5 qu'à P2.** C'est l'argument qui justifie une équipe de conversion à l'échelle, et il est juste. **En proportion de ce que tu gagnes, c'est l'inverse :** à P2, un point transforme **−238 056 € de perte annuelle en +303 374 € de bénéfice** — il ne fait pas mieux, il fait passer de mort à vivant ; à P5, il ajoute 2,4 années d'EBITDA à une entreprise déjà rentable. Survie contre allocation : on ne pilote pas les deux avec la même urgence.

**À P2 un point est atteignable ; à P5, non.** Un point sur 2,50 %, c'est **+40 % relatif** — exactement ce que produit une page qui passe de 39,5/100 à 85/100, dont l'exemple rempli de la [grille](../modeles/checklist-page-produit.md) chiffre les cinq corrections à 548 004 € HT par an sur les chiffres de NØRA à P2. Une page déjà notée 85 ne trouvera pas un point : l'unité de travail y devient **0,1 point**, soit 1 065 099 € par an à P5 — qui finance encore 2 130 jours-homme à 500 €.

### 8.2 Ce que vaut une seconde de temps de chargement

*Hypothèse déclarée, plus prudente que le chiffre public de l'étude* Milliseconds Make Millions *(Deloitte Digital pour Google, 2020 : +8,4 % de conversion pour 0,1 s) : **−1 s = +10 % relatif**, entre 2 s et 5 s, effet fortement décroissant sous 2 s. Second effet : 5 points des 13 % de clics payés qui n'atteignent jamais la session sont récupérables par le chargement seul ([E07 § 1.3](../modules/E07-funnel-et-conversion.md)), soit 5 % du budget média.*

| | **P2** | **P3** | **P5** |
|---|---:|---:|---:|
| Commandes gagnées / mois | 400 | 1 800 | 6 020 |
| Effet conversion, € HT / an | 135 358 € | 710 440 € | 2 662 748 € |
| Budget média / mois ([canoniques § 2.2](../donnees/chiffres-canoniques.md)) | 104 636 € | 436 000 € | 1 494 206 € |
| Clics payés récupérés (5 %), € HT / an | 62 782 € | 261 600 € | 896 524 € |
| **Valeur annuelle d'une seconde** | **198 139 €** | **972 040 €** | **3 559 272 €** |
| Coût du chantier (20 j-h à 500 € + 1 200 € d'outillage) | 11 200 € | 11 200 € | 11 200 € |
| **Rendement** | **×17,7** | **×86,8** | **×317,8** |
| **Jours-homme finançables à 500 €/jour** | **396** | **1 944** | **7 119** |

Lis la dernière ligne. **Au palier P2 — la vallée de la mort, celui où l'on coupe tout — une seconde de chargement finance 396 jours-homme.** Presque deux années de travail d'une personne, pour une seule seconde. Personne ne les dépense : une seconde ne se voit pas en réunion, un nouveau visuel de page d'accueil si. Et le chantier est identique aux trois paliers — images, scripts tiers, polices. Il ne devient pas plus difficile en grandissant, seulement plus rentable et plus dur à faire accepter, parce que plus de gens ont mis un script sur ta page.

### 8.3 Deux trajectoires à douze mois, au palier P2

Deux marques identiques : 4 000 commandes par mois, même AOV, même EBITDA de départ de **−19 838 € par mois** ([canoniques § 2.2](../donnees/chiffres-canoniques.md)). Chacune dispose de 28,5 jours-homme, soit 14 250 € à 500 € la journée. C'est le seul arbitrage.

**X met les 28,5 jours dans la page et la mesure** — les cinq corrections de l'exemple rempli de la [grille](../modeles/checklist-page-produit.md) : port sur la fiche, garantie, prix et bouton au-dessus du pli, paliers de panier, vitesse. **45 667 € HT de marge brute par mois.** **Y met les 14 250 € dans le média** : au MER de 2,20, 31 350 € TTC de CA, soit 26 125 € HT, dont 58,8 % de marge brute = 15 361 €, moins les 14 250 € dépensés.

| | **X — la page** | **Y — le média** |
|---|---:|---:|
| Investissement | 14 250 € | 14 250 € |
| Contribution la 1ʳᵉ année | **548 004 €** | **1 111 €** |
| Contribution la 2ᵉ année, sans rien refaire | **548 004 €** | **0 €** |
| EBITDA mensuel après (départ −19 838 €) | **+25 829 €** | −19 745 € |
| Rendement la 1ʳᵉ année | **×38,5** | ×0,08 |

**Y a acheté du chiffre d'affaires une fois. X a acheté un taux**, qui s'applique à toutes les commandes futures — y compris à celles que le média de Y aurait apportées. C'est la différence entre un flux et un actif. Et X peut désormais dépenser davantage en média que Y : sa marge brute par commande a monté, donc son MER seuil a baissé, donc sa ligne de flottaison est plus basse.

Le troisième effet n'apparaît dans aucun de ces tableaux. X convertit mieux, donc son CAC baisse, donc son avance publicitaire par euro de chiffre d'affaires baisse, donc son besoin en fonds de roulement baisse ([canoniques § 4](../donnees/chiffres-canoniques.md)). **Le travail de page se paie trois fois : en marge, en coût d'acquisition, et en trésorerie.**

> **À retenir :** tu ne pilotes pas un taux de conversion, tu pilotes un prix d'achat de commande. Coût par session ÷ taux de conversion = ce que tu paies une commande. Les deux termes se travaillent, et le second est gratuit — mais seulement si tu le mesures juste, sinon tu paies le premier plus cher sans jamais le savoir.

---

## 9. Avant la séance suivante

1. **Branche l'envoi côté serveur et remplis une vraie ligne du tableau de réconciliation.** Une seule semaine réelle. C'est la condition d'entrée de [S08](S08-le-lancement.md) : un seuil calculé sur une mesure à 55 % est un seuil faux. Si tu ne dois faire qu'une chose de cette liste, fais celle-là.
2. **Mesure ton LCP sur un téléphone, en 4G, hors de ton bureau**, et fais les deux corrections d'images. Une demi-journée. Note l'avant et l'après : [S09](S09-lire-les-premiers-chiffres.md) te demandera l'écart.
3. **Fais lire ta page à trois personnes de ta cible qui ne connaissent pas la marque**, sur leur téléphone, pendant que tu te tais. Chronomètre le temps qu'elles mettent à trouver le prix, puis le délai de livraison. Au-delà de dix secondes pour l'un des deux, ton bloc 4 ou ton bloc 6 est mal placé.
4. **Écris les trois variantes de haut de page.** Cinq heures. Sans elles, les douze concepts de [S06](S06-premier-lot-de-creas.md) atterrissent tous au même endroit, et tu détruis à l'arrivée la moitié du travail créatif que tu viens de payer.

---

*Fin de la séance S07. Suite : [S08 — Le lancement : les 30 premiers jours](S08-le-lancement.md), où tu écriras le budget, la structure de compte et surtout **tous les seuils de décision avant de voir le premier chiffre** — parce que la seule décision qu'on prend correctement sous stress est celle qu'on a écrite quand on ne l'était pas.*
