# Séance S08 — Le lancement : les 30 premiers jours

> **Niveau requis :** L04 · **Durée :** 8 h · **Livrable :** le plan de lancement complet — budget dérivé, structure de compte, calendrier jour par jour, préparation opérationnelle — et **le tableau des seuils de décision, écrits, datés et signés avant la première impression** · **Modules :** [E06](../modules/E06-acquisition-payante.md), [E09](../modules/E09-mesure-et-incrementalite.md), [E10](../modules/E10-cash-et-operations.md)
> **Ce que tu ne peux pas faire sans avoir fait cette séance :** dépenser un budget média sans le transformer en bruit. Sans seuils écrits d'avance, tu ne prendras pas de mauvaises décisions — tu prendras des décisions au hasard, en croyant lire des données.

---

## 1. Où tu en es

Tu as une catégorie prouvée ([S02](S02-prouver-la-demande.md)), un produit spécifié et un COGS au centime ([S03](S03-produit-et-cogs.md)), une gamme et un panier cible ([S04](S04-offre-prix-et-panier.md)), trois angles ([S05](S05-recherche-client-et-angles.md)), douze concepts ([S06](S06-premier-lot-de-creas.md)), une page rédigée et une mesure vérifiée ([S07](S07-le-site.md)).

**Décidé :** tout ce qui se décide sans données. **Pas décidé :** combien tu dépenses, sur combien de temps, dans quelle structure, et — la seule question qui compte vraiment — **ce que tu feras de chaque chiffre que tu vas voir.**

Cette dernière question se traite maintenant, pas dans trois semaines. Le lancement est le moment du cursus où le rapport entre le stress et la qualité de l'information est le plus défavorable de toute la vie d'une marque : tu n'as jamais eu aussi peu de données et tu n'as jamais eu autant envie d'agir. **La seule décision qu'on prend correctement sous stress est celle qu'on a écrite quand on ne l'était pas.**

*Sigles : **CPA** — coût par achat. **MER** — chiffre d'affaires TTC ÷ dépense publicitaire. **CM3** — marge après coûts variables et publicité. **Unité d'optimisation** — le niveau auquel l'algorithme d'enchère répartit un budget et apprend : un groupe d'annonces, en général.*

---

## 2. Ta mission

Écrire le plan de lancement **entier**, avant la première impression achetée.

1. **Le budget**, dérivé — pas choisi. Combien par semaine, sur combien de semaines, avec le calcul qui le produit à partir du nombre de conversions nécessaires.
2. **La structure de compte** : campagnes, unités d'optimisation, événement d'optimisation, et la démonstration que ton budget peut les financer.
3. **Le calendrier des 30 jours**, jour par jour : ce qu'on lance, dans quel ordre, **ce qu'on ne touche pas et pendant combien de temps**.
4. **Le tableau des seuils** : à J+7, J+14, J+21 et J+30, quel indicateur, sur quelle fenêtre, quel seuil, et **la décision écrite au futur pour chaque cas** — au-dessus, en dessous, et « pas assez de données ».
5. **La préparation opérationnelle** : stock et date de réapprovisionnement, expédition, service client, paiement, retours, mentions légales, trésorerie.
6. **Le protocole de la première commande** : ce qu'on fait, et la liste écrite de ce qu'on ne fait pas.

---

## 3. Ce dont tu disposes

| Ressource | Usage |
|---|---|
| Ton livrable [S07](S07-le-site.md) | La page et **le tableau de réconciliation**. Un seuil calculé sur une mesure à 55 % est un seuil faux |
| Ton livrable [S06](S06-premier-lot-de-creas.md) | Les douze concepts et le registre. Le lancement les consomme en six jours au rythme de P2 |
| Ton livrable [S04](S04-offre-prix-et-panier.md) | Panier cible, marge brute par commande, **MER seuil** — le plafond de CPA en découle |
| Ton livrable [S03](S03-produit-et-cogs.md) | Le MOQ et le délai fournisseur : ils décident de la date du réapprovisionnement |
| [`mentorat/jalons.md`](../mentorat/jalons.md) | La **Porte P1 → P2** : 200 commandes, 2 gagnants distincts, MER ≥ 1,80, 6 mois de trésorerie |
| [`modeles/protocole-test-creatif.md`](../modeles/protocole-test-creatif.md) | Décider avant de tester, pas après |
| [canoniques § 2.3](../donnees/chiffres-canoniques.md) et [§ 2.4](../donnees/chiffres-canoniques.md) | MER seuil et nCAC par palier |
| `python3 ecommerce/outils/test_significativite.py` | L'intervalle de confiance de ton CPA à n conversions. **L'outil central de cette séance** |
| `python3 ecommerce/outils/simulateur_tresorerie.py` | Ton point bas de trésorerie et ta croissance maximale autofinançable |

---

## 4. La méthode, pas à pas

### 4.1 Le budget de lancement, dérivé du nombre de conversions nécessaires

Un budget de lancement ne se choisit pas en fonction de ce qu'on peut se permettre. **Il se dérive du nombre de conversions nécessaires pour que le résultat soit lisible**, et si tu ne peux pas le financer, tu n'as pas un problème de budget : tu as un problème de coefficient ou de panier, à régler en [S03](S03-produit-et-cogs.md) et [S04](S04-offre-prix-et-panier.md).

**Combien de conversions faut-il ?** Un CPA observé est un rapport entre une dépense connue et un nombre d'achats aléatoire. La précision de ce rapport ne dépend que du nombre d'achats :

```
n ≈ (1,96 ÷ précision relative visée)²
±50 % → 16    ±30 % → 43    ±25 % → 62    ±20 % → 96    ±10 % → 385
```

Le calcul exact, par intervalle de Poisson — celui que produit `test_significativite.py` — donne des bornes asymétriques, plus larges vers le haut :

| Achats observés | Intervalle à 95 % sur le CPA | Rapport borne haute / borne basse |
|---:|---|---:|
| 1 | −82,1 % à +3 852 % | **×220** |
| 4 | −60,9 % à +267 % | ×9,4 |
| 10 | −45,6 % à +108 % | ×3,8 |
| 16 | −38,4 % à +74,9 % | ×2,8 |
| **43** | **−25,8 % à +38,2 %** | **×1,9** |
| 62 | −22,0 % à +30,4 % | ×1,7 |
| 96 | −18,1 % à +23,4 % | ×1,5 |
| 385 | −9,7 % à +11,6 % | ×1,2 |

**Quarante-trois achats, c'est le premier niveau où l'on peut dire quelque chose.** En dessous de seize, on ne peut littéralement rien conclure : à quatre achats, la borne haute vaut neuf fois la borne basse.

**Le second cadran donne le même nombre.** Le modèle d'enchère d'une plateforme a besoin d'un nombre minimal de conversions par semaine et par unité d'optimisation pour cesser d'explorer au hasard — de l'ordre de **50**. C'est une valeur d'interface, donc datée ; le mécanisme, lui, ne l'est pas : un modèle a besoin d'exemples, et il ne les invente pas.

Deux raisonnements indépendants, une statistique et une algorithmique, convergent sur **50 conversions par semaine et par unité d'optimisation**. C'est de là que sort le budget :

```
Budget minimal lisible / semaine = 50 × CPA de lancement
```

**Le CPA de lancement n'est pas ton CPA cible.** Au lancement, il n'y a ni base de clients, ni avis, ni notoriété, ni historique dans le modèle d'enchère. *Hypothèse de travail :* un MER de lancement de **1,60**, soit en dessous du 1,80 canonique du palier P1 ([canoniques § 2.3](../donnees/chiffres-canoniques.md)), et à réviser dès la quatrième semaine avec ta valeur mesurée.

| CPA de lancement | Budget / semaine | Sur 30 jours | Par jour |
|---:|---:|---:|---:|
| 20,00 € | 1 000 € | 4 286 € | 143 € |
| 30,00 € | 1 500 € | 6 429 € | 214 € |
| 40,00 € | 2 000 € | 8 571 € | 286 € |
| 60,00 € | 3 000 € | 12 857 € | 429 € |
| 100,00 € | 5 000 € | 21 429 € | 714 € |

*Tous montants en € HT. Trente jours = 4,29 semaines.*

**Sur combien de temps ? Trente jours, concentrés.** L'erreur symétrique du budget trop petit est le budget correct étalé trop longtemps. Le même montant réparti sur quatre-vingt-dix jours donne un tiers des conversions hebdomadaires : le modèle ne sort jamais de sa phase d'exploration, tu paies la pénalité tout du long, et tu brûles trois mois de trésorerie au lieu d'un. **En lancement, la concentration bat la durée**, et c'est le seul moment du cursus où c'est vrai.

### 4.2 La structure de compte : plus simple que ce que tu crois

Tu vas vouloir huit campagnes, cinq audiences, douze créas séparées, et une matrice de tests. Fais la division avant :

```
Unités d'optimisation finançables = budget hebdomadaire ÷ (50 × CPA)
```

| Palier | Budget pub / sem. | nCAC | Coût d'une unité (50 conv.) | **Unités finançables** |
|---|---:|---:|---:|---:|
| **Lancement** (hypothèse) | 1 797 € | 35,93 € | 1 797 € | **1,0** |
| P1 ([canoniques § 2.2](../donnees/chiffres-canoniques.md)) | 4 718 € | 26,62 € | 1 331 € | 3,5 |
| P2 | 24 147 € | 30,78 € | 1 539 € | 15,7 |
| P3 | 100 615 € | 33,18 € | 1 659 € | 60,6 |
| P5 | 344 817 € | 40,03 € | 2 002 € | 172,3 |

**Au lancement, tu peux financer exactement une unité d'optimisation.** Ce n'est pas une opinion sur la structure de compte, c'est une division. La structure qui en découle :

| Élément | Ce qu'on fait au lancement | Pourquoi |
|---|---|---|
| Campagne de prospection | **Une**, ciblage large, une seule unité d'optimisation, **les douze concepts dedans** | C'est la seule que ton budget peut nourrir à 50 conversions/semaine |
| Événement d'optimisation | **L'achat**, jamais l'ajout au panier | Optimiser sur un proxy fait acheter des gens qui font le proxy |
| Recherche sur ta marque | Une campagne, budget plafonné à quelques euros par jour | Défensive. Sa performance affichée est une récolte, pas une création ([E09 § 3.1](../modules/E09-mesure-et-incrementalite.md)) |
| Retargeting | **Rien le premier mois** | Tu n'as pas d'audience. À ouvrir vers J+21, quand la base atteint une taille utile |
| Convention de calcul | **100 % du média compte dans le CPA**, retargeting inclus | Celle des [canoniques § 5](../donnees/chiffres-canoniques.md). Isoler 10 % de budget en retargeting améliore le CPA affiché sans qu'un euro ait bougé |
| Répartition manuelle du budget entre concepts | **Aucune** | Douze unités à 150 € par semaine donnent 4 conversions chacune : rien n'est décidable, rien n'apprend |

**Les concepts se jugent en amont, pas au CPA.** À 43 conversions par concept, il faudrait 43 × 35,93 × 12 = **18 540 € HT** pour départager les douze — deux mois et demi de budget de lancement. On les juge donc sur la rétention à trois secondes, le taux de clic et le taux d'ajout au panier, exactement comme le prévoit [S06 § 8.2](S06-premier-lot-de-creas.md) ; le CPA ne départage que les deux ou trois qui survivent à ce premier tri.

### 4.3 Le calendrier des 30 jours

| Jour | Ce qu'on fait | Ce qu'on ne touche pas |
|---|---|---|
| **J−14** | Stock reçu et compté. **Trois commandes de test payées avec une vraie carte**, expédiées, reçues, retournées, remboursées | — |
| **J−10** | Une semaine complète de réconciliation de la mesure ([S07 § 7.4](S07-le-site.md)). Taux de remontée ≥ 95 % ou on ne lance pas | — |
| **J−7** | Douze concepts chargés et nommés selon la convention de [S06](S06-premier-lot-de-creas.md). Trois pages d'angle en ligne. Six réponses types du service client écrites | — |
| **J−3** | **Les seuils écrits, datés, signés, imprimés et affichés.** Le budget de réapprovisionnement engagé (§ 4.5) | — |
| **J−1** | Vingt colis pré-emballés. Coupure d'expédition fixée et écrite sur la page | — |
| **J1** | Mise en diffusion, budget nominal, unité unique | **Tout** |
| **J2 – J7** | Rien. On expédie, on répond au service client, on écrit le lot 2 de concepts | **Tout** : budget, ciblage, créas, page, événement |
| **J+7** | Point n° 1, 30 minutes, tableau des seuils en main | La page reste figée |
| **J8 – J14** | **Au plus un** changement structurel, appliqué le jour du point | Le budget, sauf décision du tableau |
| **J+14** | Point n° 2 | La page reste figée |
| **J15 – J21** | Un changement structurel maximum. Ouverture éventuelle du retargeting | La page |
| **J+21** | Point n° 3 | La page reste figée |
| **J22 – J30** | Un changement structurel maximum. Lot 2 de concepts prêt à charger | La page |
| **J+30** | Revue complète, décision de budget, mise à jour des seuils pour les 30 jours suivants | — |

**Les cinq règles de « on ne touche pas ».**

1. **Rien ne bouge pendant les sept premiers jours.** Ni budget, ni ciblage, ni créa, ni page, ni événement d'optimisation.
2. **Un seul changement structurel par semaine**, décidé à un point de contrôle et appliqué le même jour de la semaine.
3. **Budget : +25 % au maximum par semaine, à la hausse seulement**, et seulement si le CPA sur 14 jours glissants est sous le plafond. Une baisse est autorisée à tout moment, mais décidée à un point de contrôle.
4. **La page ne bouge pas pendant 30 jours**, sauf panne. Si elle bouge, aucune variation de CPA ne sera attribuable à quoi que ce soit.
5. **Aucun concept n'est jugé au CPA sous 43 conversions.** Avant, il se juge sur les indicateurs amont, ou pas du tout.

**Ce que coûte une intervention.** *Hypothèse déclarée : une modification structurelle relance la phase d'exploration, soit trois jours à +30 % de CPA.*

```
3 jours à 257 € HT/jour                     = 771 € HT de média
   à 35,93 € de CPA                         = 21,5 commandes
   à 46,71 € de CPA (+30 %)                 = 16,5 commandes
Perte : 5,0 commandes × 28,87 € de marge    = 143 € HT par intervention
```

Cent quarante-trois euros paraissent supportables, et c'est exactement le piège. **À une intervention tous les deux jours, le compte ne sort jamais de l'exploration** : ce n'est plus une pénalité de trois jours, c'est le mois entier à +30 %. Sur 7 800 € HT de média, **167 commandes au lieu de 217** — 50 commandes et **1 447 € HT de marge brute perdus le premier mois**, pour un enchaînement de gestes dont aucun, pris seul, ne semblait déraisonnable.

### 4.4 Les seuils écrits d'avance

C'est le cœur de la séance, et la seule partie qui ne se rattrape pas après coup.

**Les quatre règles d'écriture d'un seuil.**

1. **Un seuil est un nombre**, jamais un adjectif. « Si le CPA est décevant » n'est pas un seuil ; « si le CPA sur 14 jours glissants dépasse 43,00 € » en est un.
2. **Un seuil a une décision attachée, écrite au futur et à la première personne.** Pas « il faudra envisager de » : « je coupe les quatre concepts les plus chers et j'en charge quatre du lot 2 ».
3. **Un seuil a une fenêtre de mesure**, et ce n'est jamais « hier ». Quatorze jours glissants au minimum, sept par exception.
4. **Un seuil a un cas « je ne sais pas ».** C'est la règle que personne n'écrit et qui décide de tout : **sous n conversions, la décision est de ne rien faire.** Sans elle, l'absence de données se lit comme une mauvaise nouvelle, et l'on agit — ce qui est la définition exacte du pilotage au ressenti.

**Les cinq familles à couvrir**, dans cet ordre : la **mesure** (le tableau ne vaut rien si l'instrument ment), le **coût d'acquisition**, la **créa**, l'**opération** (retours, délais, service client), la **trésorerie**. La trésorerie est toujours en dernier dans le tableau et toujours prioritaire dans la décision : **un seuil de trésorerie franchi annule tous les autres.**

Le squelette à remplir :

| Jour | Famille | Indicateur | Fenêtre | Seuil | Décision écrite d'avance |
|---|---|---|---|---|---|

### 4.5 La préparation opérationnelle

| Poste | La question tranchée avant J1 | La règle écrite |
|---|---|---|
| **Stock** | Combien de commandes le stock couvre-t-il, et à quelle date faut-il recommander ? | Date de réappro. = date de rupture projetée − délai fournisseur. **Elle tombe souvent avant J1** |
| **Expédition** | Qui emballe, à partir de quelle heure de coupure, en combien de temps ? | La coupure est écrite sur la page (bloc 6) et tenue. Un délai annoncé et raté coûte 40 % de réachat ([E07 § 8.5](../modules/E07-funnel-et-conversion.md)) |
| **Service client** | Quel canal, quel délai, quelles réponses types ? | 24 h ouvrées. Les six réponses types sont les six objections de [S07](S07-le-site.md), déjà rédigées |
| **Paiement** | Deux moyens actifs, testés avec de l'argent réel | Trois commandes de test payées, expédiées, retournées, remboursées avant J−10 |
| **Retours** | Étiquette, adresse, délai, qui paie | Écrit dans le tunnel **et** dans le courriel de confirmation |
| **Juridique** | Mentions, CGV, rétractation 14 j distincte de la garantie, consentement | Relu par un juriste avant J1, pas après le premier litige |
| **Comptabilité** | TVA, seuil de vente à distance, facturation, taux par pays | Ouvert avant la première commande. Une régularisation rétroactive coûte dix fois le conseil initial |
| **Trésorerie** | Combien de mois de perte projetée le compte couvre-t-il, **une fois le prochain lot de réapprovisionnement retranché** ? | **≥ 4 mois.** En dessous, le budget est divisé par deux, quels que soient les autres indicateurs. Le stock est la moitié du problème : l'oublier rend le seuil inopérant |

**Le piège du stock est un piège de calendrier, pas de quantité.** Le délai fournisseur se compte à partir du moment où tu paies l'acompte, et il court pendant que tu vends. Pose la soustraction : si ton stock couvre onze semaines de ventes projetées et que ton fournisseur livre en onze semaines, ta date de réapprovisionnement est **le jour du lancement** — avant d'avoir vendu une seule unité, et donc avant d'avoir la moindre preuve que tu devrais racheter. C'est un vrai risque, il se prend en connaissance de cause, et il se réduit en négociant un second lot plus petit plutôt qu'en repoussant la décision.

### 4.6 Le jour où tombe la première commande

**Ce qu'on fait, dans l'ordre.**

1. **Vérifier la chaîne de bout en bout** : paiement encaissé, événement `achat` compté **une seule fois** (réconciliation de [S07](S07-le-site.md)), commande arrivée à l'expédition, courriel de confirmation parti, lien de suivi actif. Une chaîne se vérifie sur la première commande ou sur la deux-centième, quand elle est cassée depuis deux cents commandes.
2. **L'expédier soi-même, le jour même**, avec un mot écrit à la main.
3. **Appeler le client 48 h après réception.** Dix minutes, cinq questions écrites d'avance : où as-tu vu l'annonce · qu'est-ce qui t'a fait cliquer · qu'est-ce qui t'a presque arrêté · qu'as-tu cherché sur la page sans le trouver · qu'attends-tu du produit.
4. **Consigner les réponses dans le registre d'objections de [S05](S05-recherche-client-et-angles.md).** Une commande vaut cinq lignes de recherche client, et c'est la seule chose qu'elle vaut aujourd'hui.

**Ce qu'on ne fait surtout pas.**

- **Monter le budget.** n = 1. L'intervalle de confiance du CPA sur une conversion va de **−82,1 % à +3 852 %** (§ 4.1), un facteur 220 entre les bornes. Tu ne sais rien, et tu n'as même pas commencé à savoir.
- **Modifier la page « puisque ça marche ».** Tu casses la seule chose dont tu peux dire, dans trois semaines, qu'elle n'a pas bougé.
- **Couper les onze autres concepts** parce que celui-ci a converti. Un gagnant est une coïncidence ; la [Porte P1 → P2](../mentorat/jalons.md) en demande deux, **distincts**.
- **Publier la capture d'écran.** Ce n'est pas interdit, c'est simplement du temps que la deuxième commande n'aura pas.
- **En conclure que le produit est validé.** La porte demande 200 commandes cumulées, une marge brute mesurée ≥ 55 %, et un taux de première à deuxième commande à 90 jours ≥ 12 %. Aucun de ces trois nombres ne se connaît aujourd'hui, et le troisième ne se connaîtra pas avant trois mois.

---

## 5. Ton livrable

```
LE BUDGET
CPA de lancement retenu : ....  Dérivé de : MER de lancement ....  AOV ....
Conversions/semaine visées : ....   Budget/semaine : .... € HT
Budget sur 30 jours : .... € HT     Par jour : .... € HT
Ce budget représente .... mois de ma trésorerie disponible.

LA STRUCTURE
Unités d'optimisation finançables = .... ÷ (.... × ....) = ....
Campagnes ouvertes : ....................
Événement d'optimisation : ....   Retargeting ouvert le : ....
Concepts chargés : ....   Jugés sur : ....................

LA PRÉPARATION
Stock à J1 : .... unités = .... commandes = .... jours de vente projetée
Délai fournisseur : .... semaines  →  DATE DE RÉAPPROVISIONNEMENT : ....
Coupure d'expédition : ....   Délai annoncé sur la page : ....
SAV : canal ....  délai ....  réponses types écrites : .... / 6
Trésorerie disponible : .... €  −  prochain lot .... €  =  .... mois de perte projetée
```

**Le calendrier des 30 jours** — une ligne par jour ou par bloc de jours :

| Jour | Ce qu'on fait | Ce qu'on ne touche pas |
|---|---|---|

**Le tableau des seuils** — au minimum douze lignes, couvrant les cinq familles aux quatre points de contrôle :

| Jour | Famille | Indicateur | Fenêtre | Seuil | Décision écrite d'avance |
|---|---|---|---|---|---|

```
Écrit le ....  Signé ....
« Je m'engage à ne prendre, pendant 30 jours, aucune décision structurelle
qui ne figure pas dans ce tableau. »
```

---

## 6. La grille d'évaluation

Barème sur 100, **seuil de validation 78**. Le plus haut de l'atelier : c'est la séance où l'argent commence à sortir, et une erreur ici se paie en trésorerie, pas en points.

| # | Critère | Pts | Ce qui vaut les points | Ce qui les fait perdre |
|---|---|---:|---|---|
| 1 | **Budget dérivé, pas choisi** | 14 | Le calcul complet : conversions nécessaires → CPA de lancement → budget hebdomadaire → 30 jours | Budget posé sans calcul : **éliminatoire** ; conversions nécessaires non justifiées : −7 |
| 2 | **Structure de compte démontrée** | 12 | La division « unités finançables » faite et écrite, structure qui en découle | Plus d'unités que le budget n'en finance : −10 ; optimisation sur l'ajout au panier : −6 |
| 3 | **Tableau des seuils** | 26 | ≥ 12 lignes, 5 familles, 4 points de contrôle, un nombre et une fenêtre par ligne | Seuil sans fenêtre de mesure : −2 chacun ; **aucun cas « pas assez de données » : −10** |
| 4 | **Décisions écrites au futur** | 12 | « Je fais X » pour chaque cas : au-dessus, en dessous, indéterminé | Décision formulée en « il faudra envisager » : −3 chacune |
| 5 | Calendrier jour par jour | 10 | Les 30 jours couverts, avec la colonne « ce qu'on ne touche pas » | Colonne absente : −8 ; pas de période figée de 7 jours : −6 |
| 6 | **Préparation opérationnelle** | 12 | Les huit postes tranchés, **dont la date de réapprovisionnement calculée** | Date de réappro. absente : −6 ; commandes de test non passées : −4 |
| 7 | Seuil de trésorerie | 8 | Exprimé en mois de perte projetée, avec la décision de division du budget | Trésorerie exprimée en euros sans horizon : −5 |
| 8 | Protocole de première commande | 6 | Les quatre gestes et la liste écrite de ce qu'on ne fait pas | Liste des interdits absente : −4 |

**Quatre fautes éliminatoires.** **Un budget posé sans dérivation** — tu ne sauras pas si l'absence de signal vient du marché ou de ton échantillon. **Un tableau de seuils écrit après le lancement**, même d'un jour : il n'aura plus aucune valeur, parce qu'il aura été écrit en connaissance des premiers chiffres. **Un seuil sans décision attachée** — c'est un indicateur, pas un seuil, et tu improviseras quand même. **Un lancement planifié sans réconciliation de mesure préalable** ([S07](S07-le-site.md)) : tous tes seuils portent alors sur des nombres faux, et tu passeras trente jours à décider sur du vent.

---

## 7. Le corrigé exemplaire

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.

**KALIS**, chaussettes de course techniques, la marque des corrigés de [S03](S03-produit-et-cogs.md) à [S07](S07-le-site.md). Données d'entrée : panier cible **57,48 € TTC**, **marge brute 28,87 € HT par commande**, MER seuil 2,11 (avec remises), MER cible de régime 2,20, COGS mixte 11,30 € HT par commande, 3,61 paires par commande. Fournisseur B, Vietnam, MOQ 3 000 paires à 2,77 € HT rendu entrepôt, **délai 11 semaines**, paiement 30 % / 70 %. Capital disponible : **45 000 €**. Frais fixes : **2 500 € HT par mois**.

### 7.1 Le budget

```
CPA de plafond de contribution (CM3 = 0)  = 57,48 ÷ 1,99      = 28,88 €  ≈ marge brute
CPA cible de régime (MER 2,20)            = 57,48 ÷ 2,20      = 26,13 €
CPA de lancement retenu (MER 1,60, hyp.)  = 57,48 ÷ 1,60      = 35,93 €

Budget minimal lisible = 50 × 35,93 €     = 1 796,50 € HT / semaine
Sur 30 jours (4,29 semaines)              = 7 698 € HT       → arrondi 7 800 € HT
Par jour                                  =   257 € HT
Commandes payantes attendues              = 7 800 ÷ 35,93    = 217
```

**KALIS lance en dessous de son plafond de contribution, volontairement et pour un mois.** À 35,93 € de CPA contre 28,87 € de marge brute, chaque commande du premier mois perd **7,06 €**. Ce n'est pas une erreur : c'est le prix des données. Ce qui serait une erreur, c'est de ne pas l'avoir écrit avant, et de le découvrir à J+20 en se croyant en train d'échouer.

```
Perte du mois 1 = 217 × (−7,06 €) − 2 500 € de fixes = −4 032 € HT
7 800 € de budget = 3,1 mois de la perte mensuelle projetée à ce rythme.
```

### 7.2 La structure de compte

```
Unités finançables = 1 796,50 ÷ (50 × 35,93) = 1,0
```

| Élément | Décision de KALIS |
|---|---|
| Prospection | **Une campagne, une unité d'optimisation**, ciblage large, 1 700 € HT/semaine, **les douze concepts dedans** |
| Événement | **Achat.** Pas l'ajout au panier, pas le début de paiement |
| Recherche de marque | Une campagne à 100 € HT/semaine, plafonnée, défensive |
| Retargeting | **Fermé jusqu'à J+21.** À J+21, la base atteindra ~1 500 visiteurs sur 30 jours : ouverture à 150 € HT/semaine, jamais plus de 10 % du budget |
| Jugement des concepts | Rétention à 3 s, taux de clic, taux d'ajout au panier. **CPA seulement au-delà de 43 conversions** |

Ce que KALIS ne fait pas, et pourquoi le calcul le lui interdit : douze unités d'optimisation à 150 € HT par semaine produiraient **4,2 conversions par semaine chacune** — intervalle de confiance du CPA de ×9,4 entre les bornes (§ 4.1), et aucune n'atteindrait jamais son seuil d'apprentissage. **Douze fois rien reste rien.**

### 7.3 Le calendrier

| Jour | KALIS fait | KALIS ne touche pas |
|---|---|---|
| **J−14** | 3 000 paires reçues, comptées, 2,2 % de casse constatée. Trois commandes de test payées carte, expédiées, retournées, remboursées | — |
| **J−10** | Semaine 4 de réconciliation : **98,2 %** de remontée ([S07 § 7.4](S07-le-site.md)). Feu vert | — |
| **J−7** | 12 concepts chargés, 3 pages d'angle en ligne, 6 réponses types écrites depuis les objections du bloc 10 | — |
| **J−3** | **Seuils écrits, signés, imprimés, affichés au mur.** Acompte de 30 % du 2ᵉ lot versé (§ 7.5) | — |
| **J−1** | 20 colis pré-emballés. Coupure d'expédition : 14 h | — |
| **J1** | Diffusion. 257 € HT/jour | Tout |
| **J2–J7** | Expédition, service client, rédaction du lot 2 de concepts | Tout |
| **J+7** | Point n° 1 (30 min) | La page |
| **J8–J14** | Un changement : les 4 concepts au plus faible taux d'ajout au panier sortent, 4 du lot 2 entrent | Budget, page |
| **J+14** | Point n° 2 | La page |
| **J15–J21** | Ouverture du retargeting à 150 € HT/semaine | La page, la prospection |
| **J+21** | Point n° 3 | La page |
| **J22–J30** | Lot 2 complet prêt. Première relance d'avis à J+21 après livraison | La page |
| **J+30** | Revue, décision de budget, seuils réécrits pour le mois 2 | — |

### 7.4 Le tableau des seuils de KALIS, écrit à J−3

| Jour | Famille | Indicateur | Fenêtre | Seuil | Décision écrite d'avance |
|---|---|---|---|---|---|
| **J+7** | Mesure | Achats dédupliqués ÷ commandes back-office | 7 j | **≥ 95 %** | 85–95 % : je gèle le budget et je répare sous 5 jours. < 85 % : **je coupe la diffusion** le jour même |
| J+7 | Acquisition | Commandes cumulées | cumul | ≥ 25 | **< 15 : je ne touche à rien.** L'échantillon n'est pas lisible, et l'absence de signal n'est pas un signal |
| J+7 | Créa | Taux d'ajout au panier, toutes créas | 7 j | **≥ 6,0 %** | < 3,0 % : j'arrête la production créa et je reprends la page. Le problème n'est pas l'annonce |
| J+7 | Opération | Commandes expédiées sous 24 h | 7 j | 100 % | < 90 % : j'arrête la diffusion 48 h et je règle l'expédition. Un retard précoce coûte du réachat, pas des excuses |
| **J+14** | Acquisition | CPA | 14 j glissants | **≤ 43,00 €** | > 43 € : je coupe les 4 concepts au plus faible taux d'ajout et j'en charge 4 du lot 2. Rien d'autre |
| J+14 | Créa | Concepts ayant atteint 43 conversions | cumul | ≥ 1 | 0 : je concentre le budget sur les 4 meilleurs au taux d'ajout, au lieu de 12 |
| J+14 | Trésorerie | (Trésorerie − prochain lot) ÷ perte mensuelle projetée | — | **≥ 4 mois** | < 4 mois : **je divise le budget par deux**, quels que soient tous les autres indicateurs |
| **J+21** | Acquisition | CPA | 14 j glissants | **≤ 38,00 €** | > 38 € **et** ajout au panier ≥ 6 % : le problème est le tunnel, je reprends [S07 § 4.4](S07-le-site.md). > 38 € **et** ajout < 6 % : le problème est l'offre ou la page |
| J+21 | Acquisition | Contribution cumulée (marge brute − média) | cumul | **> −2 500 €** | < −2 500 € : je divise le budget par deux et je ne le remonte qu'après un concept sous 30 € de CPA sur 43 conversions |
| J+21 | Opération | Taux de retour | cumul | **≤ 5,0 %** | > 8 % : **j'arrête la diffusion.** C'est un problème de produit ou de taille, et le média le multiplie |
| **J+30** | Acquisition | CPA | 14 j glissants | **≤ 35,93 €** | ≤ 35,93 € : je monte le budget de 25 %. 35,93 à 43,00 € : je tiens le budget un mois de plus. > 43,00 € : **j'arrête la diffusion** et je retourne à [S05](S05-recherche-client-et-angles.md) et [S06](S06-premier-lot-de-creas.md) |
| J+30 | Créa | Gagnants distincts (≥ 43 conv. **et** CPA ≤ 32 €) | cumul | **≥ 2** | < 2 : **je ne monte pas le budget**, quelle que soit la marge. [Porte P1 → P2](../mentorat/jalons.md), condition 3 |
| J+30 | Acquisition | Commandes cumulées | cumul | ≥ 180 | < 120 avec un CPA conforme : mon budget était trop petit, pas mon offre. Je remonte le budget avant de conclure |
| J+30 | Mesure | Taux de remontée | 30 j | ≥ 95 % | < 95 % : aucune décision de budget n'est prise ce mois-ci. Réparation d'abord |
| J+30 | Trésorerie | (Trésorerie − prochain lot) ÷ perte mensuelle projetée | — | **≥ 4 mois** | < 4 mois : budget divisé par deux. **Cette ligne prime sur les treize autres.** |

*Écrit le J−3, signé. « Je m'engage à ne prendre, pendant 30 jours, aucune décision structurelle qui ne figure pas dans ce tableau. »*

**Trois lignes méritent d'être relues.** La ligne J+7 « commandes cumulées » écrit **l'inaction** comme une décision : c'est la seule protection contre l'interprétation du bruit, et c'est celle que personne n'écrit. La ligne J+21 sur le CPA **bifurque selon un second indicateur** : le même CPA élevé appelle deux réparations opposées, et sans le taux d'ajout au panier on répare au hasard. La ligne J+30 « commandes cumulées » protège contre la conclusion inverse de la précédente : un CPA conforme avec trop peu de commandes ne dit pas que l'offre est mauvaise, il dit que le budget était trop petit — et la décision est d'en remettre, pas d'arrêter.

### 7.5 La préparation opérationnelle de KALIS

| Poste | Décision |
|---|---|
| Stock | 3 000 paires (2 934 nettes de casse) = **812 commandes** à 3,61 paires |
| **Réapprovisionnement** | Rupture projetée en semaine 12 au rythme du plan. Délai fournisseur 11 semaines. **Date de commande : J+7** — acompte de 30 % (2 493 €) versé dès J−3 pour sécuriser le créneau usine |
| Expédition | Coupure 14 h, expédition le jour même. Annoncé « livré en 2 à 3 jours ouvrés » sur la page |
| Service client | Courriel + formulaire, 24 h ouvrées, six réponses types = les six objections du bloc 10 de [S07](S07-le-site.md) |
| Paiement | Carte + portefeuille mobile. Trois commandes de test réelles à J−14 |
| Retours | Étiquette prépayée dans le colis, adresse de retour, 30 jours, remboursement sous 5 jours ouvrés après réception |
| Juridique | Mentions, CGV, rétractation 14 j séparée de la garantie 30 j, consentement à un clic. Relu à J−12 |
| Comptabilité | TVA française, seuil de vente à distance surveillé dès la Belgique |
| Trésorerie | 45 000 € − 8 310 € (1ᵉʳ lot) = **36 690 €**. Perte projetée du mois 1 : 4 032 €. **7,0 mois de couverture** une fois le lot suivant retranché (36 690 − 8 310 = 28 380 €) — et le calcul est refait à chaque point de contrôle, parce que la perte projetée change avec le budget |

**La ligne de réapprovisionnement est la plus difficile à signer.** Elle demande d'engager 8 310 € de marchandise à J+7, avec vingt-cinq commandes derrière soi et un intervalle de confiance de CPA encore large. Le refus de la signer ne supprime pas le risque : il le déplace vers une rupture de stock de onze semaines au mois 3, au moment précis où les premiers concepts gagnants tournent. **On réduit ce risque en négociant un second lot plus petit, pas en repoussant la décision.**

### 7.6 Ce qui s'est passé à J+30

| Indicateur | Valeur | Seuil | Décision appliquée |
|---|---:|---:|---|
| Commandes cumulées | 219 | ≥ 180 | ✓ |
| CPA sur 14 jours glissants | 34,80 € | ≤ 35,93 € | **Budget +25 %** → 9 400 € HT au mois 2 |
| Gagnants distincts | 2 (C02 à 29,10 €, C07 à 31,40 €) | ≥ 2 | ✓ Condition 3 de la porte franchie |
| Taux de remontée | 97,4 % | ≥ 95 % | ✓ |
| Taux de retour | 3,6 % | ≤ 5,0 % | ✓ |
| Contribution cumulée | −1 533 € | > −2 500 € | ✓ |
| (Trésorerie − prochain lot) ÷ perte projetée | 6,4 mois | ≥ 4 mois | ✓ |

Sept lignes vertes, une décision : **+25 % de budget, rien d'autre.** Pas de refonte de page, pas de nouvelle campagne, pas de changement d'événement d'optimisation. Le mois 2 se lance avec les mêmes seuils, réécrits et resignés, avec un plafond de CPA abaissé de 43,00 € à 38,00 €.

---

## 8. Les conséquences chiffrées de ton choix

Deux lancements. Même produit, même page, mêmes douze concepts, même capital de 45 000 €, **et exactement le même budget média total sur six mois : 91 800 € HT.** La seule différence est la manière dont les décisions sont prises.

**KALIS-A** applique le tableau du § 7.4 : quatre points de contrôle, un changement structurel par semaine au maximum, aucun concept jugé sous 43 conversions.

**KALIS-B** pilote au ressenti quotidien : le tableau de bord est ouvert le matin et le soir, un ajustement tous les deux jours, les concepts sont jugés au troisième jour, le budget suit l'humeur des chiffres de la veille.

*Hypothèses du modèle, toutes déclarées. **CPA de référence**, identique pour les deux, décroissant à mesure que le compte accumule des données, que les gagnants se dégagent et que la base de clients grandit : 35,93 € · 33,50 € · 31,00 € · 29,00 € · 27,50 € · 26,13 €. **Pénalité d'apprentissage de B : ×1,30 constante** — à une intervention tous les deux jours et trois jours de réexploration, le compte n'est jamais hors de sa phase d'exploration. **Pénalité de bibliothèque de B**, croissante : ×1,00 · 1,06 · 1,13 · 1,21 · 1,29 · 1,36.*

**D'où vient la seconde pénalité, et c'est le vrai mécanisme.** B juge ses concepts au troisième jour. Trois jours à 257 € HT font 771 € de média, répartis sur douze concepts : **65 € par concept**. Un vrai gagnant à 26 € de CPA y produit 2,5 achats en espérance, un vrai perdant à 55 € en produit 1,2. La règle de B — « je coupe tout ce qui dépasse 36 € de CPA » — revient à couper tout concept sous deux achats :

```
P(couper un vrai gagnant)  = P(X ≤ 1 | λ = 2,50) = 28,7 %
P(garder un vrai perdant)  = P(X ≥ 2 | λ = 1,18) = 33,0 %
```

**B élimine plus d'un vrai gagnant sur quatre et conserve un perdant sur trois.** Au taux de réussite de 12,14 % dérivé en [S06 § 8.1](S06-premier-lot-de-creas.md), son taux effectif tombe à 8,66 % : sa probabilité d'avoir deux gagnants distincts au bout d'un lot de douze passe de **43,8 % à 27,4 %**. À chaque lot, sa bibliothèque se dégrade — moins de gagnants en rotation, donc plus de fréquence sur ceux qui restent, donc un coût pour mille qui monte. **B ne juge pas mal : il juge tôt, ce qui revient à tirer au sort.**

### 8.1 Six mois, mois par mois

| Mois | **A** budget | **A** CPA | **A** cmd | **A** résultat | **B** budget | **B** CPA | **B** cmd | **B** résultat |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 7 800 € | 35,93 € | 217 | −4 033 € | 9 600 € | 46,71 € | 206 | −6 166 € |
| 2 | 9 400 € | 33,50 € | 281 | −3 799 € | 6 800 € | 46,16 € | 147 | −5 047 € |
| 3 | 12 200 € | 31,00 € | 394 | −3 338 € | 17 400 € | 45,54 € | 382 | −8 869 € |
| 4 | 15 800 € | 29,00 € | 545 | −2 571 € | 8 200 € | 45,62 € | 180 | −5 510 € |
| 5 | 20 500 € | 27,50 € | 745 | −1 479 € | 21 000 € | 46,12 € | 455 | −10 354 € |
| 6 | 26 100 € | 26,13 € | 999 | **+237 €** | 28 800 € | 46,20 € | 623 | **−13 302 €** |
| **Total** | **91 800 €** | **28,86 €** | **3 180** | **−14 983 €** | **91 800 €** | **46,05 €** | **1 993** | **−49 249 €** |

*Résultat = marge brute (28,87 € par commande) − média − 2 500 € de frais fixes mensuels.*

**Même budget. 1 187 commandes d'écart, 34 266 € de résultat cumulé d'écart, et un CAC supérieur de 59,5 %.**

Trois choses à lire dans ce tableau.

**Le CAC moyen de A sur six mois est de 28,86 €, sa marge brute par commande de 28,87 €.** A finit sa première demi-année exactement à l'équilibre sur l'acquisition, ses frais fixes étant financés par ce que le réachat commencera à produire. Ce n'est pas de la chance : c'est ce que produit le respect d'un plafond de CPA écrit d'avance.

**B ne s'améliore jamais.** Son CPA est de 46,71 € au mois 1 et de 46,20 € au mois 6. Les trois mécanismes de progression — le modèle qui accumule des données, les gagnants qui se dégagent, la base qui grandit — sont neutralisés par les interventions. **Le compte de B n'a pas six mois d'expérience : il a le même premier jour, cent quatre-vingts fois.**

**Le sixième mois de B est son pire mois.** Il dépense 28 800 € pour perdre 13 302 €, contre 26 100 € dépensés par A pour gagner 237 €. Plus B grandit, plus il perd, parce que ce qu'il multiplie est une structure fausse. C'est le mode d'échec de la [Porte P2 → P3](../mentorat/jalons.md) : *faire au palier N+1 ce qui ne marchait déjà pas au palier N, mais dix fois plus cher.*

### 8.2 La trésorerie, et la vérité désagréable sur A

*Ajout au modèle : chaque commande consomme 3,61 paires ; un lot de 3 000 paires coûte 8 310 € HT et se recommande quand le stock projeté descend sous 1,5 mois de consommation.*

| Fin de mois | **A**, capital 45 000 € | **B**, capital 45 000 € |
|---|---:|---:|
| 1 | 32 657 € | 30 524 € |
| 2 | 20 548 € | 25 476 € |
| 3 | 17 210 € | 8 297 € |
| 4 | 6 329 € | 2 787 € |
| 5 | **−3 460 €** | **−15 877 €** |
| 6 | **−19 843 €** | **−37 489 €** |

**A aussi manque de trésorerie, et pas pour la même raison.** B manque d'argent parce qu'il perd de l'argent. **A manque d'argent parce qu'il grandit** : sa croissance immobilise du stock plus vite que sa marge n'en produit — exactement le mécanisme des [canoniques § 4](../donnees/chiffres-canoniques.md), où la croissance autofinançable est négative aux paliers P1 et P2.

C'est pour cela que la ligne de trésorerie prime sur toutes les autres, et pour cela qu'elle retranche le prochain lot avant de diviser. Au point de contrôle de fin de mois 3, A dispose de 17 210 € ; sa perte projetée du mois 4 est de 2 571 € et son prochain lot coûte 8 310 €.

```
(17 210 − 8 310) ÷ 2 571 = 3,5 mois   <  4 mois   →   le seuil se déclenche
```

**La décision écrite d'avance s'applique : le budget est plafonné à 10 000 € HT par mois.** Sans le retranchement du lot, le même calcul aurait donné 6,7 mois — le seuil n'aurait pas bougé, et A aurait découvert le problème au mois 5, avec un stock à payer et plus rien pour le payer.

| Trajectoire | Capital | Budget mois 6 | Clients à 6 mois | CAC moyen | Trésorerie fin M6 |
|---|---:|---:|---:|---:|---:|
| **A — rampe pleine** | 70 000 € | 26 100 € | 3 180 | 28,86 € | **+5 157 €** |
| **A′ — seuil de trésorerie appliqué** | 45 000 € | 10 000 € | 1 911 | 29,93 € | **+3 053 €** |
| **B — au ressenti** | 45 000 € | 28 800 € | 1 993 | 46,05 € | **−37 489 €** |

**Lis la deuxième ligne : c'est la plus utile des trois.** Avec 45 000 €, une marque disciplinée ne va pas à 999 commandes par mois au sixième mois. Elle va à 383, elle est vivante, son CAC est sous sa marge brute, et sa machine fonctionne — il lui manque du capital, pas une méthode. C'est un problème finançable, et il se présente à un banquier ou à un investisseur avec six mois de données propres.

**B, lui, n'a rien à présenter.** Même capital, même budget dépensé, et à la fin : un CAC de 46,05 € pour une marge brute de 28,87 €, aucune bibliothèque de gagnants, aucune série de mesures interprétable — parce qu'aucune période n'a été assez stable pour être comparée à une autre. Il ne peut même pas dire *pourquoi* ça n'a pas marché. **A′ a un problème de trésorerie ; B a un problème d'ignorance, et l'ignorance ne se finance pas.**

### 8.3 Ce que valent les clients déjà payés

L'écart ne s'arrête pas au sixième mois. *Hypothèse : le produit dure 5 à 7 mois, donc 42 % des clients passent une commande de renouvellement dans les douze mois, à 28,87 € de marge brute — soit 12,13 € de contribution future par client acquis.*

```
A (rampe pleine) : 3 180 × 12,13 €  = 38 573 €
A′ (freinée)     : 1 911 × 12,13 €  = 23 180 €
B                : 1 993 × 12,13 €  = 24 175 €
Écart A − B, déjà payé et non encore encaissé : 14 398 €
Écart total sur six mois, résultat + réachat futur : 48 664 €
```

**Quarante-huit mille euros d'écart sur six mois, sur un budget média identique, entre deux fondateurs qui ont travaillé autant.** La différence tient en une page imprimée et affichée trois jours avant le lancement.

> **À retenir :** au lancement, ton problème n'est pas de prendre les bonnes décisions — tu n'as pas les données pour ça. Ton problème est de **ne pas prendre de décisions du tout** là où les données n'en autorisent aucune. Le tableau de seuils n'existe pas pour te dire quoi faire : il existe pour t'interdire d'agir quand tu ne sais rien, ce qui est l'essentiel des trente premiers jours.

---

## 9. Avant la séance suivante

1. **Écris ton tableau de seuils en entier, imprime-le, signe-le et affiche-le.** Douze lignes minimum, cinq familles, quatre points de contrôle, un cas « pas assez de données » par famille. Fais-le avant de lancer, ou il ne vaudra rien : un seuil écrit après le premier chiffre est un chiffre déguisé en seuil.
2. **Pose la soustraction du réapprovisionnement** : date de rupture projetée moins délai fournisseur. Si le résultat tombe avant ou près de J1, tu as une décision à prendre cette semaine, pas dans deux mois. Négocie un second lot plus petit plutôt que de repousser.
3. **Passe trois commandes de test avec une vraie carte**, expédie-les, retourne-en une, rembourse-la. Vérifie au passage que l'événement `achat` est compté une seule fois, et que le remboursement ne laisse pas une conversion fantôme dans le compte.
4. **Écris le lot 2 de concepts avant de lancer le lot 1.** [S06 § 8.2](S06-premier-lot-de-creas.md) l'a démontré : il faut trente et un concepts pour avoir 90 % de chances de deux gagnants. Si tu attends le résultat du lot 1 pour écrire le lot 2, tu n'écriras que des variations du gagnant, et ta bibliothèque mourra le jour où il fatiguera.

---

*Fin de la séance S08. Suite : [S09 — Lire les premiers chiffres et décider](S09-lire-les-premiers-chiffres.md), où l'on te donnera trente jours de données piégées — du bruit qui ressemble à un signal, un gagnant qui n'en est pas, une cohorte trop jeune pour être lue — et où ton tableau de seuils sera la seule chose qui te protégera.*
