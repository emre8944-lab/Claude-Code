# Module E07 — Le funnel et la conversion

> **Prérequis :** [E01](E01-arithmetique-de-la-marque.md), [E03](E03-offre-et-prix.md), [E04](E04-psychologie-du-client.md), [E06](E06-acquisition-payante.md).
> **Objet :** transformer le trafic acheté en commandes, et chiffrer en euros annuels ce que vaut chaque fraction de point de conversion.
> **Temps de travail :** ~5 h (lecture + exercices)

---

## 0. Pourquoi ce module existe

Le taux de conversion n'est pas un indicateur de site. C'est **le prix auquel tu rachètes ton trafic**. Tu paies une session une fois ; le taux de conversion décide combien de sessions il te faut par commande, donc ce que coûte cette commande. Améliorer la conversion et négocier ton CPM produisent le même effet comptable — sauf que la conversion ne se renégocie pas chaque trimestre avec une régie.

*Hypothèse H0 :* le taux de conversion global de NØRA au palier P5 (sessions → commandes, tous trafics) est de **2,50 %**. Ce chiffre ne figure pas dans les [chiffres canoniques](../donnees/chiffres-canoniques.md) ; il est déclaré ici et sert de base à tout le module.

Tu gagnes **0,2 point** : 2,50 % → 2,70 %. À dépense publicitaire constante — 1 494 206 €/mois (chiffres canoniques § 5) — le trafic ne bouge pas. Seules les commandes bougent.

```
Gain relatif de conversion   = 0,20 ÷ 2,50            = +8,0 %
Commandes supplémentaires    = 60 200 × 8,0 %          = 4 816 / mois
CA TTC supplémentaire        = 4 816 × 71,98 €         = 346 656 € / mois
CA HT supplémentaire         = 346 656 € ÷ 1,20        = 288 880 € / mois
Marge brute (CM2 = 2 218 957 ÷ 3 610 997 = 61,45 %)
                             = 288 880 € × 61,45 %     = 177 517 € / mois
Publicité et frais fixes     : inchangés
EBITDA annuel supplémentaire = 177 517 € × 12          = 2 130 199 €
```

(Commandes, AOV et structure de coût : chiffres canoniques § 2 et § 2.2.)

Vérification indépendante : le § 7 donne **+2 662 749 €** d'EBITDA annuel pour +10 % relatif de conversion. Notre gain vaut 8,0 % relatif, soit 2 662 749 × 0,80 = **2 130 199 €**. Les deux chemins donnent le même euro.

Quatre lectures du même montant :

- **48,7 %** de l'EBITDA annuel de P5 (4 377 023 €, § 7), pour deux dixièmes de point.
- **40 965 €/semaine**, soit 11,9 % de la dépense hebdomadaire (344 817 €, § 5) : c'est exactement 11,9 % de remise sur tout ton média.
- Le nCAC passe de 40,03 € à 1 494 206 ÷ (37 324 × 1,08) = **37,07 €** (§ 2.4). Tu n'as pas touché tes enchères, tu as changé le prix.
- **48,1 %** de l'écart entre P5 et P5+ (4 428 560 €, § 8), sans un euro de média ni un recrutement.

> **À retenir :** un point de conversion ne se discute pas en pourcentage, il se discute en euros annuels. Tant que tu n'as pas écrit ce que vaut 0,1 point chez toi, tu ne peux arbitrer aucun chantier de site.

---

## 1. La chaîne complète et ses déperditions

### 1.1 Bloc d'hypothèses

Aucun de ces taux n'est canonique : ordres de grandeur déclarés, calibrés sur une marque de soin premium vendue en Europe sur trafic social payant.

| Réf. | Hypothèse | Valeur |
|---|---|---:|
| H1 | CPM mixte, tous canaux, Europe, catégorie soin | 11,00 € |
| H2 | Taux de clic mixte | 1,25 % |
| H3 | Clics n'atteignant jamais une page chargée | 13,0 % |
| H4 | Session chargée → vue produit | 62,0 % |
| H5 | Vue produit → ajout au panier | 11,0 % |
| H6 | Ajout au panier → début de paiement | 48,0 % |
| H7 | Début de paiement → commande | 62,0 % |

### 1.2 La chaîne, en volumes mensuels au palier P5

Point de départ : 1 494 206 € de média par mois (§ 5).

| Étape | Volume / mois | Taux de passage | Origine |
|---|---:|---:|---|
| Impressions | 135 836 909 | — | 1 494 206 € ÷ 11,00 € × 1 000 (H1) |
| Clics | 1 697 961 | 1,25 % | H2 — CPC dérivé : **0,88 €** |
| Sessions chargées | 1 477 226 | 87,0 % | H3 — coût par session : **1,01 €** |
| Vues produit | 915 880 | 62,0 % | H4 |
| Ajouts au panier | 100 747 | 11,0 % | H5 |
| Débuts de paiement | 48 358 | 48,0 % | H6 |
| **Commandes** | **29 982** | 62,0 % | H7 |

```
Taux composé session → commande    = 0,62 × 0,11 × 0,48 × 0,62 = 2,03 %
Taux composé clic → commande       = 29 982 ÷ 1 697 961         = 1,77 %
Taux composé impression → commande = 29 982 ÷ 135 836 909       = 0,0221 %
                                     soit 1 commande / 4 531 impressions
```

### 1.3 Le taux de conversion n'existe pas

P5 fait 60 200 commandes par mois (§ 2), la chaîne payante en produit 29 982. Les autres viennent de l'e-mail, du direct, de l'organique, du client qui revient.

```
Sessions totales           = 60 200 ÷ 2,50 % (H0)   = 2 408 000
Sessions payantes          = 1 477 226              → 61,3 % du trafic
Sessions non payantes                               =   930 774
Commandes non payantes     = 60 200 − 29 982        =    30 218
TC payant     = 29 982 ÷ 1 477 226                  = 2,03 %
TC non payant = 30 218 ÷ 930 774                    = 3,25 %
TC global                                           = 2,50 %
```

La part payante (61,3 %) n'est pas une hypothèse : c'est ce que l'arithmétique impose une fois posés le CPM, le CTR et le taux global. **Il n'existe pas de « taux de conversion du site »** — il existe un taux payant, un taux non payant, et une moyenne qui bouge quand le mix bouge sans qu'aucune page n'ait été touchée (§ 8.6).

### 1.4 Où l'argent se perd

**Le clic qui n'arrive jamais.** 1 697 961 clics, 1 477 226 sessions : **220 735 clics payés pour rien** chaque mois.

```
Perte mensuelle = 220 735 × 0,88 € = 194 247 €   →   2 330 964 € / an
```

Une partie est irréductible : robots, doubles clics, sorties d'application. *Hypothèse :* 5 points sur 13 sont récupérables par le seul temps de chargement, soit 1 494 206 × 5 % = **74 710 €/mois**, **896 524 €/an** — plus que les 432 000 € d'une baisse de 10 % des frais fixes (§ 7).

**Le paiement commencé et abandonné.** 48 358 ouvertures, 29 982 commandes : **18 376 abandons** par mois, des gens qui ont saisi une adresse. En récupérer 10 % vaut 1 838 × 36,86 € = 67 748 €/mois, soit **812 976 €/an** (marge unitaire dérivée au § 4.1).

Entre les deux, la vue produit → ajout au panier à 11 % est le taux le plus rigide de la chaîne : il dépend de l'offre et du prix ([E03](E03-offre-et-prix.md)), pas de la page. C'est pourtant là que tout le monde travaille.

**Dernier repère.** Coût par commande issue du clic payant = 1 494 206 ÷ 29 982 = **49,84 €**, contre un nCAC canonique de 40,03 € (§ 2.4) : **+24,5 %**. Le nCAC divise la même dépense par *tous* les nouveaux clients, y compris ceux arrivés en organique après avoir vu la publicité. Cet écart mesure le halo que le dernier clic ne voit pas — pendant exact des 11 % de sur-attribution du § 5 ([E09](E09-mesure-et-incrementalite.md)).

---

## 2. La cohérence publicité → page

### 2.1 Le mécanisme

Le visiteur arrive avec une attente formée moins d'une seconde plus tôt : une promesse, un visuel, trois mots. La première tâche de la page n'est pas de convaincre, c'est de **confirmer qu'il est au bon endroit**. Avant cette confirmation, aucun argument n'est lu.

D'où le résultat contre-intuitif : **une excellente page générique convertit moins bien qu'une page moyenne mais cohérente.** La générique est bonne pour un visiteur moyen qui n'existe pas ; la cohérente est passable dans l'absolu et juste pour la seule personne qui la regarde — celle qui vient de voir cette publicité-là.

*Hypothèse :* une rupture entre l'annonce et le haut de page fait passer le rebond immédiat de 22 % à 44 %. Tu as payé 1,01 € la session (§ 1.2) pour perdre un visiteur sur cinq de plus avant le premier mot lu.

Au-dessus de la ligne de flottaison, dans cet ordre : **la promesse exacte** (mêmes mots, pas des synonymes), **le visuel de l'annonce**, **le vocabulaire du client** ([E04](E04-psychologie-du-client.md)), **le prix et l'offre**. Si l'annonce dit « cheveux qui tombent après 40 ans », la page ne dit pas « densité capillaire » : pour le cerveau qui lit, ce sont deux marques différentes.

### 2.2 Combien de pages faut-il maintenir ?

Chiffres canoniques § 6, palier P5 : **57 concepts testés par semaine, 5,2 gagnants, 23 gagnants en rotation.**

*Hypothèses :* un gagnant tourne sur 3 des 7 marchés (§ 2) ; une déclinaison coûte 2,5 h (la trame existe, on change accroche, visuel, preuve, langue) ; une page active demande 0,5 h de maintenance par mois.

```
Production   = 5,2 × 3 × 2,5 h                             = 39,0 h / semaine
Parc actif   = 23 × 3 = 69 pages ; 69 × 0,5 h/mois         =  8,0 h / semaine
Total                                                      = 47,0 h / semaine
                                                           ≈ 1,34 ETP
Part de l'effectif P5 (38 ETP, § 2.5)                      = 3,5 %
```

Ce que ça rapporte. *Hypothèses :* les pages dédiées reçoivent 70 % du trafic payant ; la cohérence vaut +25 % relatif de conversion sur ce trafic.

```
Sessions concernées  = 1 477 226 × 70 %       = 1 034 058 / mois
Gain de conversion   = 2,03 % × 25 %          = +0,507 point
Commandes de plus    = 1 034 058 × 0,507 %    = 5 247 / mois
Marge brute annuelle = 5 247 × 36,86 € × 12   = 2 320 770 €
Coût (1,34 ETP chargé, hypothèse 60 000 €)    =    80 400 €
```

Rendement **×29**. Contrôle : ces 5 247 commandes valent +8,7 % relatif global, soit 2 662 749 × 0,87 = 2 316 592 € au § 7 — 0,2 % d'écart, arrondis.

**Un studio de pages n'est pas un coût de site, c'est une extension de la machine créative** ([E05](E05-machine-creative.md)). Produire 57 concepts par semaine et les envoyer sur la même page détruit la moitié du travail créatif à l'arrivée.

---

## 3. Les trois destinations

Quiz et publi-rédactionnel sont des sas placés devant la page produit, pas des substituts : toutes les routes y finissent, et elle n'est donc jamais optionnelle.

| Destination | Niveau de conscience ([E04](E04-psychologie-du-client.md)) | Conversion relative bout en bout | Coût de production (hypothèse) | Rentable quand |
|---|---|---:|---:|---|
| Page produit | Conscient du produit / de la solution | 1,00 (référence) | 1 500 – 4 000 € | Toujours. C'est le socle. |
| Publi-rédactionnel | Conscient du problème | 0,85 – 1,30 | 2 500 – 6 000 € | Le trafic froid dépasse ~40 % du média |
| Quiz / diagnostic | Inconscient / conscient du problème | 1,10 – 1,40 sur froid ; 0,60 – 0,80 sur chaud | 8 000 – 20 000 € + maintenance | § 3.2 |

**Le publi-rédactionnel** vend le problème avant le produit : il convertit souvent moins bien *sur la page* et mieux *de bout en bout*, parce qu'il filtre. Piège de mesure : compare les formats sur **clic → commande**, jamais sur session → commande, sinon tu conclus toujours à tort.

### 3.1 Le quiz : pourquoi il fonctionne, et ce qu'il coûte

Trois mécanismes distincts, souvent confondus en un seul.

1. **L'engagement.** Répondre à une question est un micro-engagement qui rend le suivant plus facile. Le quiz ne vend pas mieux : il fabrique un interlocuteur là où il y avait un lecteur.
2. **La personnalisation.** Ce qui en sort n'est plus un produit, c'est *ton* produit — et la comparaison devient difficile, l'objet comparé n'existant pas ailleurs sous cette forme.
3. **La donnée déclarative.** Âge, cheveux, problème, saison : elle alimente la segmentation de rétention ([E08](E08-retention-et-ltv.md)) et les créations ([E05](E05-machine-creative.md)), et survit à l'effondrement de la donnée comportementale tierce ([E09](E09-mesure-et-incrementalite.md)).

Le prix à payer est **la friction** : chaque question perd du monde. Quatre à six questions, une par écran, aucun champ libre. Au-delà de huit, la personnalisation coûte plus qu'elle ne rapporte.

### 3.2 L'arbitrage chiffré

Au palier P5. *Hypothèses :* 15 % du trafic payant routé vers le quiz ; 62 % le démarrent ; 71 % des démarreurs le terminent ; les complétions convertissent à 5,2 % ; les abandons de quiz à 0,4 %.

```
Segment routé            = 1 477 226 × 15 %      = 221 584 sessions / mois
Sans quiz (TC 2,03 %)                            =   4 497 commandes
Complétions              = 221 584 × 62 % × 71 % =  97 541
Commandes des complétions = 97 541 × 5,2 %       =   5 072
Commandes des abandons   = 124 043 × 0,4 %       =     496
Total avec quiz                                  =   5 568 commandes
Écart                                            =  +1 071  (+23,8 %)
Marge brute annuelle     = 1 071 × 36,86 € × 12  = 473 746 €
```

Coût an 1 (*hypothèse*) : 18 000 € de production + 2 500 €/mois d'outil et maintenance = 48 000 €.

```
Seuil = 48 000 € ÷ 36,86 € = 1 302 commandes/an = 109/mois = +2,41 % du segment
```

**Le quiz est rentable dès qu'il fait mieux que +2,4 %. Il fait +23,8 %.** Décision évidente — à P5.

Refais-le à P2. Marge unitaire P2 = (57,55 ÷ 1,20) × 58,8 % = **28,20 €** (§ 2 et § 2.1). *Hypothèse :* le quiz capte un segment produisant 250 commandes/mois.

```
Gain à +23,8 % = 60 commandes/mois            → 20 134 € / an
Coût an 1                                     = 48 000 €
Seuil = 48 000 ÷ 28,20 ÷ 12 = 142 cmd/mois    = +56,7 % du segment
```

Verdict : **le quiz n'est pas un outil de P1–P2** — non parce qu'il ne marche pas, mais parce que son coût fixe ne s'amortit pas sur le volume. Règle générale du module : à petit volume, tout ce qui coûte cher à produire est faux, même quand c'est vrai.

---

## 4. L'anatomie d'une page produit qui convertit

### 4.1 La marge brute unitaire, qui sert à tout le reste

```
AOV mixte P5 TTC                                      = 71,98 €  (§ 2)
AOV HT                        = 71,98 ÷ 1,20          = 59,98 €
CM2                           = 2 218 957 ÷ 3 610 997 = 61,45 %  (§ 2.2)
Marge brute par commande      = 59,98 × 61,45 %       = 36,86 €
Contrôle : 60 200 × 36,86 €                           = 2 218 957 € (conforme)
```

Chaque commande gagnée sur la page vaut 36,86 €. Chaque commande perdue aussi.

### 4.2 Ce que la page doit vendre, chez NØRA

L'AOV mixte est de 71,98 € TTC ; le sérum héros coûte 39,00 € TTC (§ 1). **La commande moyenne n'est donc pas un sérum.** Voici un mix qui reconstitue l'AOV canonique — *hypothèse de mix*, mais elle doit boucler, et elle boucle.

| Référence | PVC TTC (§ 1) | Part des commandes (hypothèse) | Contribution à l'AOV |
|---|---:|---:|---:|
| Sérum Densité 50 ml seul | 39,00 € | 13 % | 5,07 € |
| Shampooing Fortifiant seul | 24,00 € | 6 % | 1,44 € |
| Masque Réparateur seul | 29,00 € | 6 % | 1,74 € |
| Rituel Complet | 74,00 € | 42 % | 31,08 € |
| Cure 3 mois | 99,00 € | 33 % | 32,67 € |
| **Total** | | **100 %** | **72,00 €** |

Écart avec l'AOV canonique : 0,02 €, arrondi. **75 % des commandes sont un Rituel ou une Cure.** La page du sérum n'a donc pas pour objet de vendre un sérum, mais de faire choisir le format à 74 € ou 99 €. Une page qui met le flacon seul en avant et propose la Cure en bas est arithmétiquement une page à 45 € d'AOV — et NØRA meurt à 45 € d'AOV : vérifie-le sur le § 2.3.

### 4.3 La structure, bloc par bloc

Dans l'ordre où le visiteur les rencontre, sur mobile.

| # | Bloc | Ce qu'il traite | Indicateur |
|---|---|---|---|
| 1 | Promesse, reprise mot pour mot de l'annonce | « Suis-je au bon endroit ? » | Rebond sous 5 s |
| 2 | Preuve visuelle immédiate (produit en main, avant/après) | « Est-ce que ça a l'air réel ? » | Scroll au-delà de 25 % |
| 3 | Note et nombre d'avis, en une ligne | « D'autres l'ont fait ? » | Clic sur la note |
| 4 | Choix d'offre et prix — Cure / Rituel / unité, Cure présélectionnée | « Quoi, et combien ? » | Part de la Cure dans les ajouts |
| 5 | Bouton d'ajout visible sans scroll | Passage à l'acte précoce | Ajouts issus du premier écran |
| 6 | Barre de réassurance : port, retour 30 j, paiements | Neutralise les coûts cachés | Abandon au paiement (§ 5) |
| 7 | Preuve sociale développée : 3 avis pour 3 objections différentes | « Pour quelqu'un comme moi ? » | Temps sur section |
| 8 | Mécanisme : pourquoi ça marche, 3 étapes et un schéma | « Pourquoi y croire ? » | Scroll jusqu'au bloc |
| 9 | Preuve dure : test d'usage, panel, ingrédient, chiffre daté | Ferme le doute rationnel | Taux de lecture |
| 10 | Objections traitées une par une, en accordéon | Les 5 raisons de ne pas acheter | Ouverture par objection |
| 11 | Garantie et inversion du risque | Transfère le risque vers toi | Ajouts après exposition ; taux de retour |
| 12 | Questions fréquentes : délai, usage, compatibilité, abonnement | Ce qui part au SAV | Tickets SAV avant-vente |
| 13 | Rappel d'offre et bouton final | Rattrape le lecteur long | Part des ajouts venant du bas |

**Le bloc 10 se remplit par la recherche client, pas par l'imagination** : les cinq objections se lisent dans les commentaires de tes publicités, les tickets SAV, les avis 3 étoiles des concurrents, les motifs de retour. Cinq objections, cinq réponses, par ordre de fréquence — ce classement est le seul travail sérieux de la page.

**Le bloc 11 se chiffre.** Une garantie plus large augmente les commandes *et* les retours. Chiffres canoniques § 7 : −1 point de retour vaut 433 320 €/an. Si passer de 30 à 90 jours ajoute 1,2 point de retour, il faut 433 320 × 1,2 ÷ 36,86 ÷ 12 = **1 176 commandes de plus par mois** (+2,0 %) pour être neutre. Décision arbitrable, pas opinion.

**Le bloc 4 est le vrai levier.** Chiffres canoniques § 7 : +10 % d'AOV vaut 3 139 401 €/an contre 2 662 749 € pour +10 % de conversion. **Le sélecteur d'offre rapporte plus que le bouton.**

---

## 5. Le paiement, et ce qu'on récupère après

### 5.1 Les causes d'abandon, par ordre d'importance

1. **Les frais de port découverts tard.** Ce n'est pas le montant qui fait fuir, c'est la modification d'un prix déjà mémorisé : un port de 4,90 € annoncé sur la fiche coûte moins qu'un port de 2,90 € révélé à l'étape 3.
2. **La création de compte obligatoire.** Un mur devant la caisse. Le compte se propose *après* le paiement, une fois l'e-mail et l'adresse saisis.
3. **Le moyen de paiement absent.** Cause n° 1 sur un marché nouvellement ouvert, invisible depuis la France (§ 5.3).
4. **Le délai de livraison.** Non annoncé, annoncé trop tard, ou annoncé « 3 à 10 jours ouvrés » — ce qui se lit « 10 ».
5. **Le doute sur le retour.** Qui paie, sous combien de jours, comment : trois lignes au paiement, pas dans les CGV.

### 5.2 Ce que vaut 1 % de paniers récupérés

```
Ajout → commande      = 48 % × 62 %        = 29,76 %   (H6 × H7)
Paniers créés / mois  = 60 200 ÷ 29,76 %   = 202 285
Paniers abandonnés    = 202 285 − 60 200   = 142 085
1 % récupéré                               =   1 421 commandes / mois
Marge brute mensuelle = 1 421 × 36,86 €    =  52 373 €
Marge brute annuelle                       = 628 470 €
```

Compare avec les chiffres canoniques § 7 : **−10 % de coût marchandise = 628 313 €/an.** Récupérer un pour cent des paniers abandonnés vaut donc autant que renégocier dix pour cent de tout ton COGS. La première opération demande un développeur et deux semaines ; la seconde, un an de volume et un rapport de force.

### 5.3 Les moyens de paiement locaux

P5 vend sur sept marchés : FR, BE, DE, ES, IT, NL, UK (§ 2). Le paiement n'est pas un sujet technique, c'est un sujet local ([E11](E11-passage-a-echelle.md)).

| Marché | Ce dont l'absence coûte le plus cher |
|---|---|
| Pays-Bas | iDEAL, moyen de paiement en ligne dominant du pays : son absence n'est pas une friction, c'est une fermeture |
| Allemagne | L'achat sur facture (*Rechnungskauf*) et le prélèvement SEPA — payer après réception est une norme culturelle |
| Belgique | Bancontact |
| Espagne | Bizum, en complément de la carte |
| Italie | Carte et portefeuilles, avec une présence résiduelle du paiement à la livraison |
| Royaume-Uni | Cartes, portefeuilles mobiles, paiement fractionné |

Chiffrage d'un seul bouton manquant. *Hypothèses :* les Pays-Bas font 8 % des commandes P5 ; sans iDEAL, le passage début de paiement → commande tombe de 62 % à 38 %.

```
Commandes NL potentielles = 60 200 × 8 %       = 4 816 / mois
Débuts de paiement NL     = 4 816 ÷ 62 %       = 7 768
Réalisées à 38 %          = 7 768 × 38 %       = 2 952
Perte                                          = 1 864 commandes / mois
Perte annuelle            = 1 864 × 36,86 × 12 = 824 599 €
```

**824 599 € par an pour un bouton.** Voilà la ligne à sortir quand on te dira que l'intégration d'iDEAL n'est pas prioritaire ce trimestre.

### 5.4 Le paiement fractionné

Il augmente conversion et panier sur les montants élevés, et coûte 3,5 à 5,5 % de commission au lieu de 1,55 % de PSP (§ 2.1). L'arbitrage se calcule.

*Hypothèses :* proposé au-dessus de 60 €, donc sur le Rituel et la Cure — 75 % des commandes (§ 4.2) ; 25 % de ces commandes l'utilisent ; commission 4,5 % ; il apporte +7 % relatif de commandes sur le segment.

```
AOV du segment TTC = (0,42 × 74 + 0,33 × 99) ÷ 0,75   = 85,00 €  → HT 70,83 €
Marge brute du segment = 70,83 × 61,45 %              = 43,53 €
Commandes du segment   = 60 200 × 75 %                = 45 150 / mois

Surcoût = 45 150 × 25 % × 70,83 € × (4,50 % − 1,55 %) =  23 586 € / mois
Gain    = 45 150 × 7 % × 43,53 €                      = 137 567 € / mois
Net                                                   = 113 981 € / mois
                                                      = 1 367 774 € / an
Seuil : 23 586 ÷ 43,53 = 542 commandes/mois           = +1,20 % relatif
```

*(Que la marge du segment, 43,53 €, égale la contribution par réachat du § 3 est un hasard arithmétique, sans relation entre les deux grandeurs.)*

Le fractionné gagne dès qu'il apporte **+1,2 %** sur son segment. La question n'est donc jamais « la commission est-elle chère » mais « sais-je mesurer +1,2 % ». Le § 7 explique pourquoi, sous P3, la réponse est non — et qu'il faut décider quand même.

### 5.5 La récupération : relances de panier et de session

Les 60 200 commandes canoniques **incluent déjà** cette récupération : le calcul ci-dessous chiffre ce que tu perdrais en coupant la séquence, pas un gain à ajouter.

| Envoi | Délai | Contenu | Remise |
|---|---|---|---|
| 1 | 45 min – 1 h | Rappel du panier, visuel, réassurance port et retour | Aucune |
| 2 | +20 h | Objection principale traitée, un avis, rappel garantie ; SMS si consentement | Aucune |
| 3 | +48 h | Rareté honnête (stock, fin d'offre réelle) et code limité | −10 % |
| 4 (session sans panier) | +4 h | « Voici ce que tu regardais » et guide de choix | Aucune |

*Hypothèses :* 30 % des paniers abandonnés sont identifiés (e-mail ou téléphone capturé) ; la séquence convertit 12 % des relançables ; 40 % des commandes récupérées portent le code, soit 4 % de remise moyenne TTC, soit 2,40 € HT de marge en moins ; coût direct 4 800 €/mois.

```
Relançables            = 142 085 × 30 %              = 42 625 / mois
Commandes récupérées   = 42 625 × 12 %               =  5 115 / mois
                         (3,6 % des abandons ; 8,5 % des commandes du palier)
Marge nette de remise  = 36,86 € − 2,40 €            = 34,46 €
Contribution mensuelle = 5 115 × 34,46 € − 4 800 €   = 171 465 €
Contribution annuelle                                = 2 057 579 €
```

Ne t'arrête pas là : une partie de ces clients serait revenue seule, et la séquence encaisse une commande qu'elle n'a pas créée. *Hypothèse d'incrémentalité : 60 %*, à mesurer par suppression sur échantillon aléatoire, jamais par l'attribution de l'outil ([E09](E09-mesure-et-incrementalite.md)).

```
Valeur incrémentale annuelle = 2 057 579 € × 60 % = 1 234 547 €   (28,2 % de l'EBITDA P5)
```

Ces clients entrent ensuite dans les cohortes du § 3 — contribution par réachat 43,53 €, LTV 12 mois 86,75 € ([E08](E08-retention-et-ltv.md)).

---

## 6. La vitesse et le mobile — le même chantier

### 6.1 La vitesse

Fait public : l'étude *Milliseconds Make Millions* (Deloitte Digital pour Google, 2020) mesure sur un panel de sites que 0,1 s d'amélioration du chargement mobile s'accompagne d'environ **+8,4 % de conversion** dans la vente au détail. Traite-la pour ce qu'elle est : une corrélation sur un échantillon, dont l'effet décroît fortement une fois passé sous les 2 secondes.

*Hypothèse de travail, plus prudente que le chiffre publié :* **−0,5 s de chargement = +5 % relatif de conversion.**

```
Gain = 2 662 749 € × 0,50 (§ 7, référence +10 % relatif) = 1 331 374 € / an
```

Coût (*hypothèse*) : 20 jours-homme à 500 € et 1 200 €/an d'outillage = 11 200 €. **Rendement ×119.** Ajoute les 896 524 € de clics récupérés entre le clic et la page (§ 1.4) : le même chantier travaille les deux bouts.

C'est le chantier le plus rentable et le moins glorieux du métier. Personne ne présente une réduction de poids de bundle JavaScript en comité : pas de capture d'écran, pas d'avant/après, pas de mérite créatif. C'est pour ça qu'il n'est jamais fait, et pour ça qu'il rapporte — le rendement d'un chantier est inversement proportionnel au nombre de gens qui veulent y être associés.

Par ordre d'effet : images au-dessus du pli, scripts tiers, polices chargées avant le premier rendu, applications de la boutique qui s'exécutent partout. Repère public : **LCP au 75ᵉ centile ≤ 2,5 s** (Core Web Vitals de Google), mesuré sur mobile en 4G, jamais sur ton ordinateur en fibre.

### 6.2 Le mobile

*Hypothèses :* 78 % des sessions et 73 % des commandes sont sur mobile.

```
Mobile     : 1 878 240 sessions, 43 946 commandes  → TC 2,340 %
Ordinateur :   529 760 sessions, 16 254 commandes  → TC 3,068 %
Écart relatif                                      = +31,1 %
```

L'écart est en partie normal — le mobile porte plus de trafic froid — mais pas entièrement structurel. *Hypothèse :* un chantier sérieux en récupère le tiers.

```
Gain = 0,728 point ÷ 3 = +0,243 point         → TC mobile 2,583 %
Commandes de plus = 1 878 240 × 0,243 %       = 4 561 / mois
Marge brute annuelle = 4 561 × 36,86 € × 12   = 2 017 247 €
Contrôle § 7 : +7,58 % relatif global → 2 662 749 × 0,758 = 2 017 234 €
```

Les contraintes qui expliquent l'écart :

- **La ligne de flottaison mobile fait environ 600 pixels de haut, pas 900 de large.** Sur ordinateur, promesse, visuel, prix et bouton tiennent côte à côte ; sur mobile ils s'empilent et le bouton part sous le pli. Une page conçue en paysage puis « rendue responsive » place son bouton au mauvais endroit.
- **Les zones cliquables :** **44 × 44 pt** (Apple Human Interface Guidelines), **48 × 48 dp** (Material Design), deux repères publics. En dessous, tu ne mesures plus une intention mais une adresse de doigt.
- **Les formulaires :** un champ par ligne, clavier adapté, autocomplétion d'adresse, remplissage automatique non bloqué. Chaque champ supprimé se voit dans le taux du § 5.
- **Le pouce :** la zone atteignable d'une main couvre le bas et le centre de l'écran ; un bouton principal en haut à droite est un bouton pour ordinateur.

**Conçois sur un téléphone, à une main, dans le métro**, puis adapte à l'ordinateur. L'ordre inverse produit une page qui plaît en réunion et perd 31 % de conversion sur 78 % du trafic.

---

## 7. Tester quand on peut, trancher par principe quand on ne peut pas

### 7.1 La formule

Pour comparer deux taux de conversion, avec 5 % de risque de faux positif et 80 % de puissance :

```
n (sessions par variante) = (1,96 + 0,84)² × 2 × p (1 − p) ÷ (p × r)²
                          = 15,68 × (1 − p) ÷ (p × r²)

p = taux de conversion de référence
r = écart RELATIF à détecter (0,10 pour +10 %)
```

Multiplie par p, et il se passe quelque chose de remarquable :

```
Conversions nécessaires par variante ≈ 15,68 ÷ r²
```

**Le nombre de conversions à collecter ne dépend pas de ton taux de conversion, seulement de l'écart que tu veux détecter.** Un site à 1 % et un site à 5 % ont besoin du même nombre de commandes par variante ; le premier a simplement besoin de cinq fois plus de trafic pour les obtenir.

| Écart relatif visé | Conversions / variante | Total | Durée à P5 (60 200 cmd/mois) | Durée à P2 (4 000 cmd/mois, test sur 45 % du trafic) |
|---:|---:|---:|---:|---:|
| +30 % | 174 | 348 | 0,2 jour | 6 jours |
| +20 % | 392 | 784 | 0,4 jour | 13 jours |
| +10 % | 1 568 | 3 136 | 1,6 jour | 1,7 mois |
| +5 % | 6 272 | 12 544 | 6,3 jours | 7,0 mois |
| +2 % | 39 200 | 78 400 | 40 jours | 3,6 ans |
| +1 % | 156 800 | 313 600 | 158 jours | 14,5 ans |

*(La correction (1 − p) abaisse un peu ces nombres : à p = 2,5 % et r = 10 %, 1 529 au lieu de 1 568. Garde la version simple, elle est conservatrice.)*

### 7.2 Ce que ce tableau dit

**À P2, la quasi-totalité des tests sont ininterprétables.** Les vrais effets d'une modification d'interface valent +2 à +5 % : sept mois pour un test à +5 %, pendant lesquels tu changeras d'offre, de créations, de mix de trafic et de saison. Ce que tu mesureras alors n'est pas ta variante, c'est décembre contre juin.

**À P5, tu peux tester sérieusement**, et c'est l'un des rares avantages structurels du volume : 1,6 jour pour +10 %, 6,3 jours pour +5 %, soit deux tests concluants par mois sur le seul tunnel de paiement.

### 7.3 Ce qu'on fait quand on ne peut pas tester

On décide par **principe** et par **recherche client** — ce que font aussi les grandes marques pour tout effet attendu sous le seuil de détection.

- **Les principes** ont survécu à des décennies de tests chez d'autres, on n'a donc pas à les retester : ne pas cacher un coût, ne pas imposer un compte, mettre la promesse au-dessus du pli, une question par écran, un champ de moins vaut mieux qu'un champ de plus.
- **La recherche client** a un bien meilleur rapport signal/bruit : dix entretiens de vingt minutes donnent l'ordre des objections, ce qu'aucun test A/B ne donne à P2 — et cet ordre vaut plus que n'importe quel gain de 3 %.
- **Ne teste que du gros** : une offre, un prix, une destination (§ 3). +30 % se détecte en six jours à P2. Si tu ne peux tester que du gros, teste du gros, et arrête de tester du petit.

### 7.4 Le piège de l'arrêt au moment favorable

Tu lances un test, tu regardes tous les jours, au jour 6 la variante B est à p = 0,04. Tu arrêtes, tu déploies, tu annonces +9 %. Tu viens de fabriquer un faux positif.

Le seuil de 5 % ne vaut que pour **un seul regard, à une taille d'échantillon fixée d'avance**. Regarder plusieurs fois et s'arrêter à la première significativité, c'est se donner plusieurs chances de tomber sur le hasard. Résultat classique de la théorie des tests séquentiels (Armitage et al., 1969) : avec cinq regards, le taux réel de faux positifs monte autour de 14 % ; avec un regard quotidien sur un mois, il dépasse 25 %.

La conséquence est pire que le test perdu : tu déploies une variante neutre, ton taux ne bouge pas, tu conclus que la conversion « ne se travaille pas », et tu remets le budget sur le média. Une décision de portefeuille prise sur un artefact statistique.

Trois règles non négociables : **calcule la taille d'échantillon avant de lancer** et écris la date de fin, à laquelle le test s'arrête ; **ne fais rien des résultats intermédiaires**, ou emploie une méthode séquentielle qui ajuste le seuil au nombre de regards ; **une seule métrique de décision, choisie d'avance** — tester dix indicateurs jusqu'à ce que l'un soit significatif est la même erreur sous un autre nom.

---

## 8. Les erreurs qui coûtent cher

**8.1 — Tester la couleur d'un bouton pendant que la promesse est fausse.**
Une couleur produit typiquement moins de 1 % d'écart relatif : 313 600 conversions au total (§ 7.1), soit **158 jours à P5 et plus de quatorze ans à P2**. Le test est mathématiquement impossible, et le temps passé est le vrai coût — pendant ce temps, la promesse en haut de page n'est pas celle de l'annonce, défaut qui vaut 2 320 770 €/an (§ 2.2).

**8.2 — La refonte complète sans mesure.**
Une refonte qui perd 8 % relatif de conversion coûte 2 662 749 × 0,80 = **2 130 199 €/an** (§ 7), et tu ne peux pas revenir sur la partie fautive puisque tout a bougé ensemble. Déploie par blocs, dans l'ordre du § 4.3, avec une mesure entre chaque.

**8.3 — Empiler les fenêtres surgissantes.**
*Hypothèse :* trois fenêtres (bienvenue, roue, intention de sortie) coûtent 6 % relatif de conversion et rapportent 2,5 points de capture d'e-mail.

```
Perte = 2 662 749 € × 0,60                            = 1 597 649 € / an
Gain  = 2 408 000 × 2,5 % = 60 200 e-mails/mois = 722 400 / an
        à 0,80 € de contribution annuelle (hypothèse) =   577 920 € / an
Net                                                   = −1 019 729 € / an
```

Le calcul se retourne si un e-mail vaut plus de 2,21 €/an (1 597 649 ÷ 722 400) : fais-le avec ta vraie valeur ([E08](E08-retention-et-ltv.md)). Une fenêtre bien placée est presque toujours gagnante — c'est l'empilement qui tue.

**8.4 — Cacher les frais de port jusqu'à l'étape 3.**
*Hypothèse :* +6 points d'abandon au paiement.

```
Débuts de paiement totaux = 60 200 ÷ 62 %      = 97 097 / mois
Commandes perdues         = 97 097 × 6 %       =  5 826 / mois
Perte annuelle            = 5 826 × 36,86 × 12 = 2 576 871 €
```

**2,58 M€ par an pour avoir déplacé une ligne de trois mots.** Annonce le port sur la fiche, ou intègre-le au prix et affiche « livraison offerte » — mais vérifie alors le coefficient du § 1.

**8.5 — Promettre un délai de livraison qu'on ne tient pas.**
*Hypothèses :* 12 % des commandes arrivent hors délai annoncé ; ces clients réachètent 40 % de moins.

```
Clients touchés / mois         = 37 324 × 12 %      = 4 479   (§ 2.4)
Part réachat de la LTV 12 mois = 86,75 − 32,77      = 53,98 € (§ 3)
Perte par client               = 53,98 × 40 %       = 21,59 €
Perte annuelle                 = 4 479 × 21,59 × 12 = 1 160 496 €
```

Le gain obtenu en annonçant « 48 h » au lieu de « 3 à 5 jours » est immédiat ; la perte est différée, invisible dans un tableau de bord de conversion, et supérieure. Gain de funnel payé par la rétention ([E08](E08-retention-et-ltv.md)) et les opérations ([E10](E10-cash-et-operations.md)).

**8.6 — Lire le taux global sans le segmenter.**
Payant 2,03 %, non payant 3,25 % (§ 1.3). Si la part payante tombe de 61,3 % à 55 % :

```
Commandes   = 2 408 000 × 55 % × 2,03 % + 2 408 000 × 45 % × 3,25 % = 62 059
Taux global = 62 059 ÷ 2 408 000                                    = 2,58 %
```

**+0,08 point sans qu'une seule page ait changé.** Segmente par source, compare à mix constant — prolongement du problème d'attribution ([E09](E09-mesure-et-incrementalite.md)).

---

## 9. Ce que ce module ne dit pas

**Que ces gains s'additionnent.** Vitesse (§ 6.1), mobile (§ 6.2), cohérence (§ 2.2) et paiement (§ 5) portent en partie sur les mêmes commandes ; leur somme dépasse l'EBITDA de P5+ (§ 8), ce qui est absurde. Chaque chiffre vaut *contre la situation actuelle, toutes choses égales par ailleurs* — pas en cumul. Chiffre les chantiers un par un, exécute par ordre de rendement, re-mesure la base après chacun.

**Que le taux de conversion peut monter indéfiniment.** Il a un plafond structurel imposé par la catégorie et le prix, et ce plafond ne se franchit pas avec du travail de page. Ordres de grandeur déclarés :

| Catégorie et prix | Plage de conversion usuelle |
|---|---:|
| Consommable sous 40 €, achat répété | 3 – 6 % |
| Soin premium 40 – 100 € (le terrain de NØRA) | 2 – 4 % |
| Équipement 150 – 400 € | 0,8 – 1,8 % |
| Bien considéré au-delà de 500 € | 0,3 – 0,8 % |

NØRA à 2,50 % est dans le haut du milieu de sa plage : 3,2 % est difficile mais atteignable, viser 6 % est une erreur de catégorie, pas une ambition. Un site qui affiche 6 % à ces prix ne convertit pas mieux — il a un autre mix de trafic, avec beaucoup de reciblage compté comme acquisition.

**Qu'au-delà de ce plafond, le levier reste le site.** Il ne l'est plus. Chiffres canoniques § 7 : +10 % d'AOV vaut 3 139 401 € contre 2 662 749 € pour +10 % de conversion — **17,9 % de plus**. Le § 8 est plus net encore : le passage de P5 à P5+ (+4 428 560 € d'EBITDA annuel) se fait sans un euro de CA supplémentaire, par le panier, le réachat et la discipline sur la remise. Quand la conversion touche son plafond, le chantier suivant s'appelle l'offre et le prix ([E03](E03-offre-et-prix.md)).

**Que la conversion mesure le site.** Elle mesure le produit du site, du trafic, de l'offre, du prix, de la saison et de la notoriété ; ce module isole la part du site en supposant le reste constant, supposition fausse dès que le mix média bouge ([E09](E09-mesure-et-incrementalite.md)).

**Non traité ici :** la valeur des cohortes ([E08](E08-retention-et-ltv.md)), l'incrémentalité ([E09](E09-mesure-et-incrementalite.md)), les conséquences opérationnelles d'un délai promis ([E10](E10-cash-et-operations.md)), et le fait qu'une hausse de conversion accélère la consommation de trésorerie via le BFR (§ 4, et [E13](E13-risque-de-ruine.md)) : plus de commandes, c'est plus de stock à financer avant d'être payé.

---

## 10. Le tableau de bord du module

Six lignes, hebdomadaires, segmentées payant / non payant. Chacune a un seuil qui déclenche une action.

| # | Indicateur | Référence P5 | Seuil d'alerte | Ce que l'alerte signifie |
|---|---|---:|---|---|
| 1 | Taux de conversion **payant** | 2,03 % | −8 % sur 2 semaines à mix constant | La page ou l'offre décroche, pas le média |
| 2 | Écart clic → session chargée | 13,0 % | > 18 % | Tu paies des clics qui n'arrivent pas (§ 1.4) |
| 3 | Coût par session payante | 1,01 € | +15 % à CPM constant | Le CTR ou la page d'atterrissage se dégrade |
| 4 | Début de paiement → commande | 62,0 % | < 58 % | Frais, moyen de paiement ou délai (§ 5) |
| 5 | LCP mobile, 75ᵉ centile | — | > 2,5 s (seuil public Core Web Vitals) | Chantier vitesse, rendement ×119 (§ 6.1) |
| 6 | Récupération des paniers relançables | 12,0 % | < 8 % | Séquence cassée ou délivrabilité en chute |

**Un indicateur global non segmenté ne déclenche jamais rien** (§ 8.6), et **toute alerte se convertit en euros annuels avant d'être arbitrée** : à ce palier, 1 point de conversion payante vaut environ 2 662 749 ÷ 10 × (1 ÷ 0,203) ≈ 1,31 M€/an sur la seule chaîne payante.

> **À retenir :** tu ne pilotes pas un taux de conversion, tu pilotes un prix d'achat de commande. Coût par session ÷ taux de conversion = ce que tu paies une commande. Les deux termes se travaillent, et le second est gratuit.

---

## 11. Exercices

À rendre dans [`ecommerce/exercices/E07-rendu.md`](../exercices/E07-rendu.md). Corrigé dans [`E07-corrige.md`](../exercices/E07-corrige.md).

**Exercice 1 — La chaîne de NØRA avec un CPM dégradé.**
Reprends le § 1.2 avec un CPM de 14,00 € au lieu de 11,00 €, tous autres taux inchangés, sur la dépense canonique de 1 494 206 €/mois (§ 5). Donne impressions, clics, CPC, sessions payantes, coût par session, commandes payantes et coût par commande issue du clic payant.

**Exercice 2 — Le seuil de conversion qui rend P5 déficitaire.**
À partir du § 0 et du § 2.2 (EBITDA P5 = 364 752 €/mois, marge unitaire 36,86 €), calcule de combien de points le taux de conversion global peut baisser, à dépense publicitaire et frais fixes constants, avant que l'EBITDA mensuel n'atteigne zéro. En points absolus et en relatif. Compare ensuite à l'écart au seuil de MER du § 2.3 (+24,4 %) : les deux mesures disent-elles la même chose ?

**Exercice 3 — Ta chaîne réelle.**
Sur tes 90 derniers jours, remplis la table du § 1.2 avec tes chiffres. Calcule les taux de passage, le taux composé, ton coût par session et ton coût par commande attribuée, en séparant payant et non payant. La correction est une grille de lecture : quel taux est hors norme, et dans quel ordre attaquer.

**Exercice 4 — La valeur d'un point de conversion chez toi.**
Refais le § 0 avec tes chiffres : commandes/mois, AOV TTC, TVA, taux de marge brute, dépense publicitaire. Donne la valeur annuelle en EBITDA de +0,1, +0,2 et +0,5 point, compare chacune au coût complet du chantier qui la produirait, et conclus : « chez moi, 0,1 point vaut X €/an, donc je peux justifier jusqu'à Y jours-homme. »

**Exercice 5 — Ton test est-il faisable ?**
Prends le prochain test que tu comptes lancer. Estime l'écart relatif attendu, applique la formule du § 7.1, calcule la durée nécessaire au volume du segment testé. Si elle dépasse six semaines, écris la décision que tu prendras **sans test** et le principe qui la fonde (§ 7.3).

**Exercice 6 — Décision : le quiz ou la vitesse ?**
Palier P3 (§ 2 et § 2.2 : 18 000 commandes/mois, AOV 65,40 € TTC, CM2 60,3 %, pub 436 000 €/mois, EBITDA 51 033 €/mois). Tu as 45 000 € et un trimestre d'équipe. **Option A** — un quiz de diagnostic sur 15 % du trafic payant, rendements du § 3.2. **Option B** — un chantier vitesse, rendement du § 6.1. Chiffre les deux en EBITDA annuel, tranche, justifie. La correction donne la bonne réponse **et** la condition sous laquelle l'autre devient la bonne — indice : elle porte sur la part de trafic froid et sur ton LCP actuel.

---

*Fin du module E07. Suite : [E08 — La rétention, les cohortes et la LTV](E08-retention-et-ltv.md), qui reprend les commandes que ce module a fait entrer et démontre que le prix payé pour la première n'a de sens qu'au regard de la troisième.*
