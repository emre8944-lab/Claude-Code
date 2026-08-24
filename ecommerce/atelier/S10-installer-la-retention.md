# Séance S10 — Installer la rétention

> **Niveau requis :** L05 · **Durée :** 8 h (dont 3 h d'écriture pure) · **Livrable :** les sept flux automatisés rédigés message par message, le calendrier de consommation calculé, et le premier tableau de cohortes produit avec l'outil du dépôt · **Modules :** [E08](../modules/E08-retention-et-ltv.md), [E09](../modules/E09-mesure-et-incrementalite.md) § 3, [E04](../modules/E04-psychologie-du-client.md)
> **Ce que tu ne peux pas faire sans avoir fait cette séance :** franchir la [Porte P1 → P2](../mentorat/jalons.md). Sa condition 4 exige un taux de première à deuxième commande à 90 jours mesuré sur une cohorte réelle. Sans dispositif installé et sans tableau de cohortes, tu n'as ni le chiffre, ni ce qui le produit.

---

## 1. Où tu en es

[S09](S09-lire-les-premiers-chiffres.md) t'a appris à lire un dossier et à voir que le seul chiffre qui décide à ce stade — le passage de la première à la deuxième commande — n'était **pas encore observable**. Cette séance construit ce qui le produit, puis l'instrument qui le mesure.

**Décidé :** le produit et sa contribution unitaire, l'offre, les angles, les créas, la page, le plan de lancement, et un diagnostic qui te dit où tu perds de l'argent.

**Pas décidé :** ce qui se passe après le « merci pour votre commande ». Aujourd'hui, chez presque tout le monde, la réponse est : rien, puis une campagne le jeudi.

**L'enjeu, en une ligne.** Aux paliers P1 et P2, le modèle de référence perd de l'argent sur chaque première commande — **−4,93 €** puis **−3,83 €** de contribution nette du coût d'acquisition ([canoniques § 2.4](../donnees/chiffres-canoniques.md)). Cette perte est volontaire ; elle n'est un pari raisonnable que si le réachat vient. **La rétention n'est pas un supplément de croissance : c'est ce qui rend le modèle d'acquisition solvable.**

*Acronymes : **flux** — séquence automatisée déclenchée par un comportement, par opposition à une **campagne**, envoyée à une date. **Cohorte** — ensemble des clients dont la première commande tombe dans la même période, suivi dans le temps. **Passage 1 → 2** — part des clients d'une cohorte ayant passé une deuxième commande avant un âge donné. **Dernier clic** — modèle d'attribution qui crédite la totalité d'une vente au dernier point de contact.*

---

## 2. Ta mission

**Construire le dispositif de rétention complet, puis mesurer sa première cohorte.** Cinq résultats :

1. **Le calendrier de consommation** de ta gamme : la date d'épuisement réelle de chaque référence, croisée avec la variable d'usage qui la fait varier, et la fenêtre de relance qui en découle.
2. **Les sept flux rédigés**, message par message : déclencheur, condition de sortie, nombre de messages, délais, objet, accroche, corps, un seul appel à l'action, et ce qu'on n'y met pas.
3. **La chaîne post-achat** dans son ordre de rentabilité, avec ce que tu changes réellement sur chacun des cinq maillons.
4. **Ton premier tableau de cohortes**, produit par [`cohortes.py`](../outils/cohortes.py) depuis ton export de commandes.
5. **La lecture et une décision** : ton passage 1 → 2 à 90 jours, sa comparaison aux seuils des portes, et ce que tu en fais.

Tu ne « mets pas en place un CRM ». Tu écris des textes qui partiront à des gens réels, et tu produis un tableau qui dira dans 90 jours s'ils ont marché.

---

## 3. Ce dont tu disposes

Le modèle central de cette séance est [`modeles/sequences-crm.md`](../modeles/sequences-crm.md) : les sept séquences déjà rédigées pour une marque de soin capillaire premium. **Tu ne le recopies pas** — tu gardes la structure, les délais relatifs et les interdits, et tu changes le produit, le cycle et la preuve. L'outil central est [`cohortes.py`](../outils/cohortes.py) ; il lit un export de commandes brut et produit le tableau, la courbe de réachat, le passage 1 → 2 à 30, 60, 90 et 180 jours, la LTV, le payback et l'alerte de dégradation.

```bash
python3 ecommerce/outils/cohortes.py --generer-exemple      # pour voir la forme attendue
python3 ecommerce/outils/cohortes.py --fichier export.csv \
    --colonne-date "Created at" --colonne-client "Email" --colonne-montant "Total" \
    --valeur contribution --marge-brute 57,8 --ncac 28,60
```

Lectures indispensables : [E08](../modules/E08-retention-et-ltv.md) § 4 (le premier réachat, le calendrier de consommation) et § 5 (l'arithmétique du canal) · [E09](../modules/E09-mesure-et-incrementalite.md) § 3.1 (la récolte de demande existante) · [jalons](../mentorat/jalons.md), conditions 4 des portes P1 → P2 et P2 → P3.

---

## 4. La méthode, pas à pas

### 4.1 Le calendrier de consommation — on ne relance pas après un délai

**Un délai se recopie ; une date d'épuisement se calcule.** C'est la phrase entière de la séance, et elle sépare deux façons de travailler qui n'ont pas le même rendement.

Le geste, en quatre étapes. **Un —** pour chaque référence, écris la **quantité contenue** dans l'unité de vente : nombre de doses, millilitres, jours d'usage. **Deux —** identifie la **variable d'usage** qui fait varier la vitesse de consommation. C'est le point que tout le monde saute : ce n'est presque jamais une constante. Pour un complément, c'est la posologie ; pour un soin, la fréquence d'application ; pour une nutrition sportive, le nombre de séances par semaine. **Trois —** calcule la date d'épuisement `T = quantité ÷ consommation par jour` **pour chaque combinaison référence × valeur de la variable**, pas en moyenne. **Quatre —** capte la variable au moment de l'achat — une question dans le tunnel, un diagnostic en trois clics, ou la première question du flux post-achat — et stocke-la sur la fiche client.

**Pourquoi la moyenne est structurellement fausse.** Une distribution d'épuisement est presque toujours **bimodale ou étalée** : quelques références de grand format et quelques usagers intensifs suffisent à créer deux populations. La moyenne tombe entre les deux, donc juste pour personne. [E08](../modules/E08-retention-et-ltv.md) § 4.4 le démontre sur le modèle de référence : une relance à J+49, moyenne pondérée réelle des cycles, arrive **18 jours trop tard pour 67 % de la base et 44 jours trop tôt pour 25 %**.

**La fenêtre utile.** Un message de réapprovisionnement ne travaille que dans un intervalle : trop tôt, le produit est encore là et le message est dépensé ; trop tard, le client a déjà racheté ailleurs ou décroché. Retiens **[0,70 × T ; 1,10 × T]** — assez tôt pour que le colis arrive avant le dernier usage, assez tard pour que le besoin soit réel. Le premier message part à **78 % du cycle**, le deuxième à 100 %, le troisième à 118 %.

**Comment on chiffre l'écart entre les deux approches.** Compte la part de ta base pour laquelle un délai fixe tombe dans la fenêtre utile, applique un taux de conversion « dans la fenêtre » et un taux « hors fenêtre », et compare. Un seul couple d'hypothèses, appliqué à l'identique aux deux approches : la comparaison est alors propre, même si les niveaux ne le sont pas. Le § 7.2 déroule le calcul complet.

### 4.2 Les sept flux, par ordre de rentabilité

Les sept flux du dépôt, dans l'ordre où ils rapportent — et cet ordre dépend de ce que tu appelles « rapporter ».

| # | Flux | Déclencheur | Messages | Délais | Sortie |
|---|---|---|---:|---|---|
| 1 | **Panier abandonné** | Ajout au panier, rien sous 1 h | 3 + 1 SMS | +1 h, +4 h (SMS), +20 h, +48 h | Commande |
| 2 | **Réapprovisionnement** | Date d'épuisement calculée | 3 | 78 %, 100 %, 118 % du cycle | Commande |
| 3 | **Bienvenue et première commande** | Adresse captée, aucune commande | 4 (+1) | +15 min, J+1, J+3, J+6, J+10 | Première commande |
| 4 | **Post-achat et prise en main** | Commande expédiée | 4 | J+0, livraison, +3 j, J+21 | Aucune — il va au bout |
| 5 | **Navigation abandonnée** | 2 vues d'une fiche en 7 j, aucun ajout | 2 | +4 h, +36 h | Ajout au panier |
| 6 | **Réactivation des dormants** | 2 cycles sans commande | 3 | J+0, J+6, J+14 | Commande |
| 7 | **Anniversaire de la 1ʳᵉ commande** | 12 mois jour pour jour | 1 | J+0 | — |

**Trois règles qui traversent les sept.** *Un flux répond à un comportement ; une campagne part parce que c'est jeudi.* *Un message = une objection = **un seul** appel à l'action.* *Le déclencheur prime sur la copie* — un texte médiocre au bon moment bat un texte excellent au mauvais moment, et l'écart n'est pas serré.

**Le plafond de pression et l'ordre de priorité en cas de collision** sont dans [`sequences-crm.md`](../modeles/sequences-crm.md) : huit messages par personne et par mois flux compris, jamais deux le même jour, jamais deux séquences en parallèle, et priorité panier > réappro > post-achat > bienvenue > campagne.

**Et le classement change selon la mesure.** Classe tes sept flux deux fois : une fois par le chiffre d'affaires **attribué** au dernier clic, une fois par la contribution **incrémentale** estimée. Les deux classements ne se ressemblent pas, et le flux qui arrive dernier dans le premier arrive premier dans le second. Le § 7.3 le montre en euros.

### 4.3 L'expérience post-achat : les cinq maillons, dans l'ordre

Un client ne revient pas parce qu'on lui a écrit. Il revient parce que quelque chose a marché, et les relances ne font qu'exécuter une décision déjà prise. Les cinq leviers d'[E08](../modules/E08-retention-et-ltv.md) § 4.3, du plus déterminant au moins déterminant — c'est-à-dire dans l'ordre inverse de celui où on y travaille :

1. **Le produit.** Il plafonne tout le reste. Si ton produit satisfait 55 % de tes acheteurs, ton premier réachat ne dépassera pas durablement 55 %, quel que soit ton CRM. Mesure-le — une note sur 10 à J+21 — et traite ce chiffre comme un plafond, pas comme un indicateur de satisfaction.
2. **La livraison.** Première promesse tenue ou trahie, avant même l'essai. **L'écart entre le délai promis et le délai réel compte plus que le délai lui-même** : annoncer 5 jours et livrer en 4 satisfait davantage qu'annoncer 2 et livrer en 3.
3. **Le contenu d'accompagnement.** Le flux post-achat ne vend pas : il **fait réussir l'usage**. Dose, fréquence, les trois erreurs courantes, le résultat attendu et à quelle date. Meilleur rapport effort/rendement du module, et le plus négligé — parce qu'il ne produit aucune vente attribuée le jour de l'envoi.
4. **Le service client.** Une réponse en moins de 24 h, signée d'un prénom, avec un pouvoir de décision. Un client dont le problème a été résolu rachète plus qu'un client qui n'a jamais eu de problème : c'est la seule occasion de prouver que la marque existe derrière le colis.
5. **La relance commerciale.** Volontairement dernière. Une remise à qui n'a pas eu de résultat ne produit rien ; une remise à qui allait racheter au prix fort te coûte exactement le montant de la remise.

**Le test à s'appliquer :** si tu as passé plus de temps cette semaine sur le maillon 5 que sur les maillons 1 à 4 réunis, tu travailles sur le levier le moins puissant. C'est le cas de la quasi-totalité des marques, et c'est aussi pourquoi le passage 1 → 2 stagne partout autour des mêmes valeurs.

### 4.4 Construire le tableau de cohortes

Un export de commandes suffit : une date, un identifiant client stable, un montant TTC. Trois précautions avant de lancer l'outil. **L'identifiant doit être stable** — adresse électronique normalisée, ou couple adresse + téléphone ; un identifiant de commande produit un tableau où chaque client est nouveau. **Le mois incomplet est exclu**, sinon la dernière ligne plonge pour une raison purement calendaire — c'est l'erreur de lecture la plus répandue sur les cohortes, et `cohortes.py` l'écarte automatiquement en le signalant. **Les remboursements et annulations sortent**, sinon une cohorte à forte casse paraît meilleure qu'elle n'est.

Puis on lit **dans trois directions** ([E08](../modules/E08-retention-et-ltv.md) § 1.4). *En ligne :* la courbe d'une cohorte dans le temps. *En colonne :* le même âge d'une cohorte à l'autre — **c'est la seule direction qui détecte une dégradation**, et la seule qui autorise une comparaison. *En diagonale :* l'effet d'un événement calendaire sur toutes les cohortes à la fois.

**Le signal d'alarme numéro un** est une colonne qui baisse : les cohortes récentes sous-performent les anciennes au même âge. Il se lit sur M1 à M6 bien avant d'être lisible sur M12 ou sur l'EBITDA — [E08](../modules/E08-retention-et-ltv.md) § 2.1 chiffre à **32,2 % de l'EBITDA annuel** l'effet d'une dégradation de 11,8 % passée inaperçue quatre mois.

### 4.5 La lecture : le passage 1 → 2 à 90 jours, et pourquoi c'est le seul chiffre qui décide

Trois raisons, et aucune n'est une opinion.

**Un — il est une fois et demie plus difficile que tous les suivants.** Dans la décomposition d'[E08](../modules/E08-retention-et-ltv.md) § 4.1, le passage 1 → 2 vaut 44 % quand les passages 2 → 3, 3 → 4 et suivants valent entre 66 % et 71 %. Un client qui a commandé deux fois a vérifié que le produit marche, que le colis arrive et que le SAV répond ; un client qui a commandé une fois n'a rien vérifié. **Le premier réachat est le seul verrou ; les autres sont des portes.**

**Deux — tout le reste de la courbe lui est proportionnel.** À taux conditionnels constants, le nombre total de réachats est le passage 1 → 2 multiplié par une constante. `K = 1,24 ÷ 0,44 = 2,8182` sur le modèle de référence : **un point gagné sur le premier passage déplace toute la courbe de LTV.**

**Trois — il arrive assez tôt pour décider.** Une LTV à 36 mois est vraie et inutile : une décision média se prend sur l'argent qui revient avant que tu doives le redépenser. Le passage 1 → 2 à 90 jours est le premier chiffre à la fois stable et disponible.

Les seuils, à confronter à ton tableau : **≥ 12 %** pour la [Porte P1 → P2](../mentorat/jalons.md), **≥ 18 %** pour la [Porte P2 → P3](../mentorat/jalons.md), le second devant être tenu conjointement avec une part de chiffre d'affaires en réachat ≥ 15 %.

### 4.6 Le piège de l'attribution au dernier clic

Il faut le traiter maintenant, parce qu'il va se retourner contre toi exactement au moment où ton dispositif marchera.

**Le mécanisme.** Le courriel et le SMS se voient attribuer **22 à 30 % du chiffre d'affaires en dernier clic** (*ordre de grandeur sectoriel, pas chiffre canonique*). C'est arithmétiquement vrai et économiquement trompeur : un message envoyé à quelqu'un dont le flacon est vide s'attribue une vente qui allait avoir lieu. **Le dernier clic ne l'invente pas, il la récolte.** Sur le modèle de référence, à 25 % du chiffre d'affaires et une *hypothèse d'incrémentalité de 45 %*, **595 814 € TTC par mois seraient arrivés sans le CRM** ([`sequences-crm.md`](../modeles/sequences-crm.md)).

**Pourquoi c'est dangereux et pas seulement inexact.** Ces 595 814 € finiront par justifier une coupe ailleurs : « le courriel fait 25 % du chiffre d'affaires à coût nul, réduisons Meta ». Réduis Meta, et six mois plus tard tu as réduit la base à qui le courriel parle. **Un canal de récolte ne finance pas sa semence.** C'est le même mécanisme que la recherche de marque au § 4.6 de [S09](S09-lire-les-premiers-chiffres.md), appliqué à un canal qu'on croit gratuit.

**La seule mesure honnête : la retenue aléatoire.** Exclus **10 % de ta base**, tirés au sort, d'une séquence pendant un cycle complet, puis compare le chiffre d'affaires **par destinataire** entre les deux groupes. La différence est l'incrémentalité réelle du flux. C'est gratuit, c'est reproductible, et c'est la seule chose qui te dira laquelle de tes sept séquences mérite ton temps ([E09](../modules/E09-mesure-et-incrementalite.md)). Programme-la dès l'installation : une retenue mise en place après six mois d'exploitation ne te dira jamais ce que valaient les six premiers mois.

---

## 5. Ton livrable

```
=====================================================================
LIVRABLE S10 — LE DISPOSITIF DE RÉTENTION
Marque : ___________   Date : __/__/__   Temps passé : ____ h

A. LE CALENDRIER DE CONSOMMATION
Variable d'usage retenue : ______________  captée où ? ____________
| Référence | Quantité | Variable | Conso./jour | T | Fenêtre 0,70T–1,10T | Part |
|  |  |  |  |  |  |  |
Épuisement moyen pondéré ____ j   ← LE CHIFFRE À NE PAS UTILISER
Part de la base pour qui un délai fixe à J+___ tombe dans la fenêtre : ____ %

B. LES SEPT FLUX — un gabarit rempli par message
Séquence ____  Déclencheur ____  Sortie ____  Message n° __ / délai __
Objet (≤ 45 caractères) : _________________  Pré-en-tête : ___________
Accroche, une phrase : ____________________________________________
Corps, 3 blocs maximum : __________________________________________
Appel à l'action, un seul : _______________________________________
À ne pas y mettre : _______________________________________________
Contrôle : combien de messages contiennent un code ? ____
Contrôle : plafond de 8 messages/personne/mois respecté ? O / N

C. LA CHAÎNE POST-ACHAT — ce que tu changes sur chaque maillon
1. Produit — note à J+21 mesurée ? O / N   valeur ____ /10  → plafond ____ %
2. Livraison — délai promis ____ j   délai réel médian ____ j   écart ____
3. Contenu d'accompagnement — ce que tu ajoutes : ________________
4. Service client — délai de réponse ____ h   signé d'un prénom ? O / N
5. Relance commerciale — remise présente ? O / N   à quel message ? ____

D. LE TABLEAU DE COHORTES
Commande lancée : ________________________________________________
| Cohorte | Clients | J+30 | J+60 | J+90 | J+180 |
Cohortes observables à J+90 : ____   Cohortes exposées au dispositif : ____
Colonne J+30 : baisse-t-elle d'une cohorte à l'autre ? O / N   alerte ? O / N

E. LA LECTURE ET LA DÉCISION
Passage 1 → 2 à 90 jours, moyenne des cohortes observables : ____ %
Seuil porte P1 → P2 : 12 %   franchi ? O / N
Seuil porte P2 → P3 : 18 %   franchi ? O / N
Première cohorte exposée au dispositif : ____   son J+30 : ____ %
Écart au J+30 de référence ____ pt   σ = √(p(1−p)/n) = ____ pt   z = ____
Signal ou bruit ? ______   Décision : ______________________________
Retenue aléatoire programmée : séquence ____  10 % de la base
   du __/__/__ au __/__/__   mesure le __/__/__
=====================================================================
```

---

## 6. La grille d'évaluation

Barème sur 100, **seuil de validation 72**.

| # | Critère | Pts | Ce qui vaut les points | Ce qui les fait perdre |
|---|---|---:|---|---|
| 1 | **Calendrier de consommation** | 18 | Variable d'usage identifiée et captée, T calculé par combinaison référence × variable, fenêtre utile posée | Un seul T moyen pour toute la gamme : **éliminatoire** ; variable non captée à l'achat : −8 |
| 2 | **Les sept flux rédigés** | 22 | Les 7 existent, déclencheur et sortie écrits, messages **rédigés mot pour mot**, un seul appel à l'action | Un flux décrit au lieu d'être rédigé : −3 chacun ; deux appels à l'action : −2 par message |
| 3 | **Les interdits respectés** | 8 | Aucun code au premier message de bienvenue ; aucune remise en panier avant M3 ; aucune offre dans le post-achat | Un code dans le message de bienvenue : **−8** |
| 4 | **Chaîne post-achat** | 12 | Les 5 maillons traités dans l'ordre, avec une action mesurable sur chacun | Ne traiter que le maillon 5 : −10 |
| 5 | **Tableau de cohortes produit** | 15 | Sorti de l'outil, identifiant stable, mois incomplet exclu, âges non atteints marqués | Un « · » traité comme un zéro : **éliminatoire** ; identifiant de commande au lieu de client : −10 |
| 6 | **Lecture en colonne** | 10 | Comparaison à âge égal entre cohortes, test de bruit chiffré | Comparer deux âges différents : **éliminatoire** |
| 7 | **Décision et seuils** | 8 | Passage 1 → 2 confronté aux deux seuils de porte, décision écrite | Conclure « ça monte » sans z ni σ : −5 |
| 8 | **Retenue aléatoire programmée** | 7 | Séquence, taille, dates et date de mesure écrites d'avance | Absente : −7 |

**Quatre fautes éliminatoires.** **Un calendrier de relance calé sur une moyenne.** **Un « · » lu comme un zéro.** **Une comparaison entre deux âges de cohorte différents.** **Un code de réduction dans le premier message de bienvenue** — tu paies une remise sur une vente que la preuve aurait faite, et tu apprends à ta base à l'attendre.

---

## 7. Le corrigé exemplaire

> **Cas composite. Marque fictive.** SÉVANE n'existe pas ; les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels. Ce ne sont les comptes d'aucune entreprise réelle.

**SÉVANE** — nutrition sportive végétale, vente directe, France. Septième mois d'activité, **1 100 commandes par mois**, dont environ **1 000 premières commandes**.

| Référence | Contenu | PVC TTC | COGS | Coef. | Part des 1ʳᵉˢ cmd |
|---|---|---:|---:|---:|---:|
| Protéine 750 g | 25 doses | 39,00 € | 6,80 € | ×5,7 | 38 % |
| Protéine 1,5 kg | 50 doses | 69,00 € | 12,40 € | ×5,6 | 17 % |
| Récupération | 30 doses | 29,00 € | 4,60 € | ×6,3 | 14 % |
| Pack Duo (750 g + récup.) | 25 + 30 doses | 62,00 € | 11,40 € | ×5,4 | 31 % |

```
AOV 1ʳᵉ commande = 0,38×39 + 0,17×69 + 0,14×29 + 0,31×62      =  49,83 € TTC
                                                    HT         =  41,52 €
CM2 = 1 − 8,87/41,52 − 4,90/41,52 − 1,8 % − 2,2 % − 5,0 %      =  57,8 %
Contribution 1ʳᵉ commande = 41,52 × 57,8 %                     =  24,02 € HT
AOV de réachat observé 58,00 € TTC → contribution              =  27,88 € HT
nCAC 28,60 € HT → marge à la 1ʳᵉ commande                      =  −4,58 € HT
```

**−4,58 € par première commande** — très proche du −3,83 € canonique du palier P2 ([canoniques § 2.4](../donnees/chiffres-canoniques.md)). Tout ce qui suit existe pour rembourser ces 4,58 €, et il en faut `4,58 ÷ 27,88 = 16,4 %` de passage 1 → 2 pour y parvenir.

### 7.1 Le calendrier de consommation de SÉVANE

**La variable d'usage est le nombre de séances par semaine**, captée par une question unique dans le tunnel de commande — « Tu t'entraînes combien de fois par semaine ? 3 / 5 / 7 » — et stockée sur la fiche client. Une dose par séance.

| Référence | Doses | Séances/sem. | Part | **T (épuisement)** | Fenêtre utile 0,70 T – 1,10 T |
|---|---:|---:|---:|---:|---:|
| Protéine 750 g | 25 | 3 | 9,5 % | **58 j** | 41 – 64 j |
| Protéine 750 g | 25 | 5 | 18,2 % | **35 j** | 24 – 38 j |
| Protéine 750 g | 25 | 7 | 10,3 % | **25 j** | 18 – 28 j |
| Protéine 1,5 kg | 50 | 3 | 4,3 % | **117 j** | 82 – 129 j |
| Protéine 1,5 kg | 50 | 5 | 8,2 % | **70 j** | 49 – 77 j |
| Protéine 1,5 kg | 50 | 7 | 4,5 % | **50 j** | 35 – 55 j |
| Pack Duo | 25 (protéine d'abord) | 3 | 7,8 % | **58 j** | 41 – 64 j |
| Pack Duo | 25 | 5 | 14,9 % | **35 j** | 24 – 38 j |
| Pack Duo | 25 | 7 | 8,3 % | **25 j** | 18 – 28 j |
| Récupération | 30 | 3 | 3,5 % | **70 j** | 49 – 77 j |
| Récupération | 30 | 5 | 6,7 % | **42 j** | 29 – 46 j |
| Récupération | 30 | 7 | 3,8 % | **30 j** | 21 – 33 j |

**Regarde les trois premières lignes.** Même référence, même prix, même colis : **T va de 25 à 58 jours**, soit 33 jours d'écart entre deux clients qui ont acheté exactement le même produit. Aucun délai fixe ne peut être juste pour les deux. La variable d'usage n'est pas un raffinement : c'est ce qui détermine la date.

```
Épuisement moyen pondéré = Σ (part × T)                        =  45,7 jours
```

**Et c'est précisément le chiffre à ne pas utiliser.** Une relance à J+45 — le « standard » que tout le monde recopie — tombe dans la fenêtre utile pour les seules lignes 1, 6, 7 et 11 :

```
9,5 % + 4,5 % + 7,8 % + 6,7 %                                  =  28,5 %
```

**Un délai fixe calé sur la moyenne réelle atteint 28,5 % de la base au bon moment.** Pour 43,7 % il arrive trop tard — le sachet est vide depuis des semaines et le client a racheté ailleurs. Pour 27,8 % il arrive trop tôt, sur un sachet encore à moitié plein.

### 7.2 L'écart de performance, chiffré

*Hypothèse unique, appliquée à l'identique aux deux approches :* un message de réapprovisionnement qui tombe dans la fenêtre utile convertit à **9,0 %** ; hors fenêtre, à **2,2 %**. Les niveaux sont modélisés ; l'écart entre les deux approches ne dépend que de la part atteinte.

```
Approche 1 — délai fixe J+45 pour tout le monde
   0,285 × 9,0 % + 0,715 × 2,2 %                               =  4,14 %

Approche 2 — date d'épuisement, calculée par référence × séances
   hypothèse : 15 % des clients ont déclaré une fréquence fausse
   ou ont changé d'habitude → 85 % réellement dans la fenêtre
   0,85 × 9,0 % + 0,15 × 2,2 %                                 =  7,98 %

Écart : +3,84 points, soit ×1,93
```

**La même séquence, les mêmes textes, le même coût d'envoi : presque le double de commandes.** L'écart ne vient d'aucune amélioration de la copie. Il vient d'une division.

```
Sur 1 000 premières commandes par mois :
   +3,84 % × 1 000 = +38,4 commandes de réachat par mois
   × 27,88 € de contribution                    =  +1 071 € HT / mois
                                                =  12 852 € HT / an
```

Douze mille euros par an pour SÉVANE, qui fait 1 100 commandes par mois. Le § 8 montre ce que devient le même écart de 3,84 points au palier P5.

### 7.3 Les sept flux de SÉVANE, rédigés

**Flux 1 — Panier abandonné.** *Déclencheur : ajout au panier, rien sous 1 h. 3 messages + 1 SMS. Sortie : commande.*

- **M1 · +1 h · objet « Ton Pack Duo est encore là »** — Accroche : « Ton panier est réservé jusqu'à demain soir. » Corps : le produit exact avec photo et prix TTC · port et délai annoncés · le retour sous 30 jours. Appel à l'action : reprendre ma commande. **Aucune remise.** *Jamais :* de compte à rebours ni de faux stock.
- **SMS · +4 h · consentement explicite obligatoire** — « [SÉVANE] Ton panier est encore là, livraison en 48 h : [lien]. STOP pour ne plus recevoir. » *Jamais :* avant 9 h ni après 20 h, ni deux fois.
- **M2 · +20 h · objet « La question que tout le monde pose »** — Accroche : « Neuf sur dix hésitent sur la même chose : le goût. » Corps : l'objection dominante, traitée par un avis d'un profil proche · la garantie « pas convaincu, on rembourse le sachet entamé ». Appel à l'action : reprendre. **Toujours aucune remise.** *Jamais :* un deuxième argument — un message, une objection.
- **M3 · +48 h · objet « Je libère ton panier demain »** — Corps : la dernière preuve non utilisée — analyse d'acides aminés du lot, téléchargeable · le code **seulement si les quatre conditions de la règle de remise sont réunies** ([`sequences-crm.md`](../modeles/sequences-crm.md)) · date de fin réelle. *Jamais :* un quatrième message.

**Flux 2 — Réapprovisionnement.** *Déclencheur : date d'épuisement calculée au § 7.1. 3 messages, à 78 %, 100 % et 118 % du cycle propre au client.*

- **M1 · 78 % du cycle · objet « Il te reste environ 5 séances »** — Accroche : « À 5 séances par semaine, ton sachet est vide dans dix jours. » Corps : la référence exacte, réassort en un clic · le format 1,5 kg : `2 × 39,00 = 78,00 €` contre `69,00 € TTC`, et 50 doses au lieu de 50. Appel à l'action : réassortir. **Aucune remise** — elle allait racheter.
- **M2 · 100 % du cycle · objet « Ton sachet est vide aujourd'hui »** — Accroche : « L'interruption est ce qui casse la progression du deuxième mois. » Corps : ce que coûtent deux semaines d'arrêt sur la récupération · le réassort · l'abonnement. *Jamais :* deux produits dans un même message.
- **M3 · 118 % du cycle · objet « Tu as arrêté ? »** — Accroche : « Si tu as arrêté, dis-moi pourquoi — ça m'intéresse plus que la vente. » Corps : une question unique cliquable · le réassort · puis, si la règle de remise est satisfaite, une offre de retour. *Jamais :* un quatrième message ; ensuite le contact bascule en réactivation.

**Flux 3 — Bienvenue et première commande.** *Déclencheur : adresse captée, aucune commande. 4 messages à +15 min, J+1, J+3, J+6, un 5ᵉ conditionnel à J+10. Sortie : première commande.*

- **M1 · +15 min · « Par quoi commencer »** — le choix du format selon la fréquence d'entraînement, en trois lignes. **Jamais de code** : il détruit les quatre messages suivants et fabrique des chasseurs de promotion.
- **M2 · J+1 · « Pourquoi végétale, et sur quoi ça ne change rien »** — le mécanisme nommé, une preuve datée avec son effectif, et **ce que le produit ne fait pas**. *Jamais :* de superlatif ni d'allégation de santé.
- **M3 · J+3 · « 39 € ? Fais le calcul par séance »** — `39,00 ÷ 25 = 1,56 € TTC par séance` contre `69,00 ÷ 50 = 1,38 €`. Le coût comparé au problème, jamais au prix d'un concurrent nommé.
- **M4 · J+6 · « Et si le goût ne me plaît pas ? »** — six réponses de six profils · la garantie sur sachet entamé · le service client avec un prénom. **Première offre de la séquence.** *Jamais :* d'urgence fabriquée.
- **M5 · J+10 · conditionnel** — second angle de preuve, même appel à l'action que M4.

**Flux 4 — Post-achat et prise en main.** *Déclencheur : commande expédiée. 4 messages. Aucune sortie : il va au bout.* **Le plus rentable et le plus négligé**, parce qu'il ne produit aucune vente attribuée le jour de l'envoi.

- **M1 · J+0, expédition · « C'est parti — et quoi faire en ouvrant »** — le suivi · ce qu'il y a dans le colis · la première chose à faire. *Jamais :* de produit additionnel, elle vient d'acheter.
- **M2 · à la livraison · « Une dose, 30 g, dans 250 ml — et l'erreur n° 1 »** — le geste exact en trois lignes · les trois erreurs d'usage les plus fréquentes · combien de séances tient le sachet **selon sa fréquence déclarée**. *Jamais :* de lien vers la boutique.
- **M3 · +3 j après livraison · « Ce que tu verras, et quand »** — semaine 1 : rien · semaine 3 : la récupération · semaine 8 : la charge. Ce qui est normal, ce qui ne l'est pas, et le SAV avec un prénom. *Jamais :* de demande d'avis, il n'y a pas encore de résultat.
- **M4 · J+21 · « Trois semaines. Sur 10, tu en es où ? »** — la note en un clic · sous 7, routage SAV et rappel sous 24 h · à 8 et plus, demande d'avis. *Jamais :* mélanger avis et offre de réachat.

**Flux 5 — Navigation abandonnée.** *Déclencheur : 2 vues d'une fiche en 7 jours, aucun ajout. 2 messages, +4 h et +36 h. Sortie : ajout au panier — le flux 1 prend le relais.* M1 : « Deux visites : quelque chose t'arrête » — le produit vu, les deux questions les plus posées, le guide de choix des formats. M2 : « 750 g, 1,5 kg ou le Duo ? » — trois cas, trois recommandations, le prix par séance, le diagnostic en trois questions. **Aucune remise** : elle n'a même pas mis au panier. *Jamais :* un troisième message — trois relances sur une visite, c'est de la filature.

**Flux 6 — Réactivation des dormants.** *Déclencheur : deux cycles sans commande — 70 jours pour un acheteur de 750 g à 5 séances, 234 pour un 1,5 kg à 3 séances. 3 messages : J+0, J+6, J+14. Uniquement sur qui a ouvert dans les 180 jours ; au-delà on ne réactive pas, on supprime.* M1 : « Deux choses ont changé depuis ton dernier sachet » — la nouveauté, une preuve renouvelée et datée, rien de culpabilisant, **aucune remise**. M2 : « Pourquoi tu as arrêté ? » — trois boutons : trop cher · le goût · j'ai changé de routine ; chaque réponse route vers un contenu différent. M3 : l'offre de retour selon la règle de remise, avec sa date de fin réelle. *Jamais :* « tu nous manques ».

**Flux 7 — Anniversaire de la première commande.** *Déclencheur : 12 mois jour pour jour. Un message, pas deux.* « Ton premier sachet date d'il y a un an » — un chiffre personnel : nombre de commandes, nombre de séances couvertes · un geste **non monétaire** : accès anticipé au parfum de la saison · aucune demande. **Jamais de code** : un cadeau chiffré transforme la relation en transaction et apprend à attendre l'anniversaire pour acheter.

### 7.4 Les deux classements des sept flux

*Hypothèses de volume et de conversion propres à SÉVANE, à 1 000 nouveaux clients par mois. Incrémentalité estimée, à confirmer par retenue aléatoire (§ 4.6).*

| Flux | Entrées/mois | Conv. | Cmd attribuées | **Contribution attribuée** | Incrém. | **Contribution incrémentale** |
|---|---:|---:|---:|---:|---:|---:|
| Panier abandonné | 1 450 | 8,5 % | 123 | **2 954 €** | 30 % | 886 € |
| Réapprovisionnement | 1 000 | 7,98 % | 80 | **2 230 €** | 45 % | **1 004 €** |
| Bienvenue | 1 900 | 3,4 % | 65 | **1 561 €** | 55 % | 859 € |
| Navigation abandonnée | 1 600 | 1,4 % | 22 | 528 € | 25 % | 132 € |
| Réactivation | 480 | 2,7 % | 13 | 362 € | 70 % | 254 € |
| Anniversaire | 90 | 5,6 % | 5 | 139 € | 60 % | 84 € |
| **Post-achat** | 1 000 | — | **0** | **0 €** | — | **2 693 €** |

Le post-achat ne produit **aucune** commande attribuée. Son effet se calcule autrement : il déplace le passage 1 → 2 de **+2,1 point** sur une base de 18,7 % (§ 7.5), soit `2,1 ÷ 18,7 = +11,23 %` sur tous les réachats de la cohorte. *Hypothèse : 0,86 réachat par client sur 12 mois, valeur mesurée sur les cohortes M1 à M4 de SÉVANE.*

```
1 000 clients × 0,86 réachat sur 12 mois × 11,23 % × 27,88 €   =  2 693 € / mois
```

| Classement par **contribution attribuée** | Classement par **contribution incrémentale** |
|---|---|
| 1. Panier abandonné — 2 954 € | 1. **Post-achat — 2 693 €** |
| 2. Réapprovisionnement — 2 230 € | 2. Réapprovisionnement — 1 004 € |
| 3. Bienvenue — 1 561 € | 3. Panier abandonné — 886 € |
| 4. Navigation abandonnée — 528 € | 4. Bienvenue — 859 € |
| 5. Réactivation — 362 € | 5. Réactivation — 254 € |
| 6. Anniversaire — 139 € | 6. Navigation abandonnée — 132 € |
| 7. **Post-achat — 0 €** | 7. Anniversaire — 84 € |

> **À retenir :** **le flux le plus rentable de SÉVANE est celui que son tableau de bord classe dernier.** Ce n'est pas une curiosité : c'est la conséquence mécanique du fait que le post-achat ne vend rien le jour de son envoi. Toute marque pilotée au chiffre d'affaires attribué le sous-investira, et le fera avec de bonnes raisons apparentes.

Hors post-achat, les six autres flux s'attribuent **7 774 €** de contribution par mois et n'en créent réellement que **3 219 €** : **59 % de ce que le CRM revendique serait arrivé sans lui.** Cohérent avec l'ordre de grandeur d'[`sequences-crm.md`](../modeles/sequences-crm.md), qui pose 55 % sur le modèle de référence.

**Total incrémental du dispositif : 5 912 € HT par mois, soit 70 944 € HT par an**, pour un outil à 180 € HT par mois et environ 25 heures d'écriture.

### 7.5 Le tableau de cohortes de SÉVANE

Le dispositif a été installé au début du mois 6. La cohorte M6 est donc la **première exposée**.

```bash
python3 ecommerce/outils/cohortes.py --fichier commandes-sevane.csv \
    --colonne-client "email" --valeur contribution --marge-brute 57,8 --ncac 28,60
```

| Cohorte | Clients | J+30 | J+60 | J+90 |
|---|---:|---:|---:|---:|
| M1 | 402 | 6,2 % | 13,4 % | 18,6 % |
| M2 | 588 | 6,0 % | 13,1 % | 18,3 % |
| M3 | 741 | 6,4 % | 13,8 % | 19,1 % |
| M4 | 903 | 6,1 % | 13,5 % | 18,8 % |
| M5 | 1 042 | 6,3 % | 13,9 % | · |
| **M6** *(exposée)* | 1 118 | **8,1 %** | · | · |
| M7 | 1 084 | · | · | · |

**Lecture en colonne, la seule qui autorise une comparaison.** J+30 : 6,2 · 6,0 · 6,4 · 6,1 · 6,3 — stable, aucune dégradation. J+90 : 18,6 · 18,3 · 19,1 · 18,8, **moyenne 18,7 %**. J+180 n'est observable sur aucune cohorte.

**Confrontation aux portes.** [Porte P1 → P2](../mentorat/jalons.md), seuil 12 % : **franchie, largement.** [Porte P2 → P3](../mentorat/jalons.md), seuil 18 % : **franchie de 0,7 point** — marge de sécurité de 3,7 %, ce qui n'autorise aucune complaisance : une dégradation de deux points fait repasser SÉVANE sous la porte sans qu'aucun autre indicateur ne bouge.

**Le J+30 de M6 est-il un signal ?**

```
Référence J+30 sur M1–M5 : moyenne                             =  6,2 %
n = 1 118, p = 0,062  →  σ = √(0,062 × 0,938 ÷ 1 118)          =  0,72 point
Écart observé : 8,1 − 6,2                                       =  1,9 point
z = 1,9 ÷ 0,72                                                  =  2,63
```

**z = 2,63 : au-delà de 2σ, donc un signal.** Et pourtant la décision correcte est d'attendre.

**Pourquoi.** Un gain à J+30 peut être de deux natures, et elles ne se distinguent pas à 30 jours. Soit le dispositif fait **racheter plus de gens** — le gain sera encore là à J+90. Soit il fait **racheter les mêmes gens plus tôt** — la relance calée sur la date d'épuisement avance mécaniquement des commandes qui seraient tombées à J+50 ou J+60 —, et le gain se dissipe à J+90. **Un gain d'anticipation et un gain de rétention ont exactement la même signature à 30 jours.** Seul le J+90 de M6, observable au mois 9, tranchera.

**Décision inscrite au livrable :** maintenir le dispositif à l'identique, ne modifier aucun délai, et rouvrir le dossier au mois 9 sur le J+90 de M6. En parallèle, lancer la **retenue aléatoire** sur le flux de réapprovisionnement — 10 % des clients de la cohorte M8, tirés au sort, exclus de la séquence pendant un cycle complet, mesure du chiffre d'affaires par destinataire à 60 jours. C'est le seul dispositif qui distinguera l'incrémentalité de la récolte, et il doit être lancé maintenant : une retenue posée après six mois d'exploitation ne dira jamais ce que valaient ces six mois.

---

## 8. Les conséquences chiffrées de ton choix

Le passage 1 → 2 est le seul levier du cursus qui améliore **simultanément** la marge et la capacité d'acquisition. La démonstration se fait sur le modèle de référence, au palier P5, où tous les chiffres sont canoniques.

### 8.1 Ce que vaut un point, puis cinq

À taux conditionnels constants, le nombre total de réachats est proportionnel au premier passage : `K = 1,24 ÷ 0,44 = 2,8182` ([E08](../modules/E08-retention-et-ltv.md) § 4.1).

```
44 % → 45 % : 0,45 × 2,8182 = 1,268 réachat, soit +2,27 %
Levier canonique § 7 : +10 % de commandes de réachat = 1 194 871 € d'EBITDA/an
                       1 194 871 × (2,27 ÷ 10)       =   271 562 € / an
```

| Gain sur le passage 1 → 2 | Réachats 12 mois | Variation | **EBITDA annuel gagné** | En % de l'EBITDA P5 |
|---|---:|---:|---:|---:|
| +1 point (44 % → 45 %) | 1,268 | +2,27 % | **271 562 €** | 6,2 % |
| +3 points (44 % → 47 %) | 1,325 | +6,82 % | **814 663 €** | 18,6 % |
| **+5 points (44 % → 49 %)** | **1,381** | **+11,36 %** | **1 357 810 €** | **31,0 %** |

**Cinq points de passage de la première à la deuxième commande valent 1 357 810 € d'EBITDA par an, soit 31 % de l'EBITDA du palier P5.** Ces points ne coûtent **aucun euro de publicité**. Ils coûtent un flux post-achat écrit, un calendrier de consommation calculé, une livraison tenue et un service client qui répond.

Ordre de grandeur pour comparer : les mêmes 1 357 810 € demanderaient, par le levier du CAC, une baisse de 7,6 % du coût d'acquisition à volume constant (`−10 % de CAC = 1 793 047 €`, [canoniques § 7](../donnees/chiffres-canoniques.md)) — c'est-à-dire faire mieux que l'enchère sur sept marchés, tous les mois, indéfiniment.

### 8.2 Le même levier desserre la capacité d'acquisition

C'est la partie que presque personne ne calcule, et c'est la plus importante.

**a) Le plafond d'allocation monte.** La règle d'allocation d'[E06](../modules/E06-acquisition-payante.md) § 6.2 fixe le CAC marginal maximal acceptable à la LTV à 12 mois en contribution. À 49 % de passage :

```
LTV 12 mois = 32,77 € + 1,381 × 43,53 €                        =  92,88 €
Plafond : 86,75 € → 92,88 €                                     =  +6,13 €
LTV / nCAC = 92,88 ÷ 40,03                                      =  2,32  (contre 2,17)
```

Sur la courbe de saturation de Meta ([E06](../modules/E06-acquisition-payante.md) § 7.2), la tranche de 1,0 à 1,2 M€ par mois coûte **86,96 € de CAC marginal** : elle était refusée à 86,75 € de plafond, elle devient finançable à 92,88 €. **Ce sont 2 300 nouveaux clients par mois de plus, soit +6,2 % d'acquisition, sur exactement le même compte publicitaire et sans dégrader le ratio LTV/CAC.**

**b) Le payback raccourcit, donc le cash tourne plus vite.**

```
Réachats à 1 mois : 0,06 × (1,381 ÷ 1,24)                       =  0,0668
LTV 1 mois  = 32,77 + 0,0668 × 43,53                            =  35,68 €
LTV 3 mois  = 32,77 + 0,3786 × 43,53                            =  49,25 €
Payback = 1 + (40,03 − 35,68) ÷ (49,25 − 35,68) × 2             =  1,64 mois
```

**1,64 mois contre 1,76.** Ce n'est pas une nuance : à ce palier, la croissance mensuelle autofinançable vaut `EBITDA ÷ BFR` ([E10](../modules/E10-cash-et-operations.md) § 2.2).

```
EBITDA mensuel = 364 752 € + 1 357 810 ÷ 12                     =  477 903 €
g = 477 903 ÷ 2 264 655                                          =  21,10 % / mois
contre 364 752 ÷ 2 264 655                                       =  16,11 % / mois
Sur douze mois : ×10,0 contre ×6,0
```

> **À retenir :** cinq points de premier réachat augmentent l'EBITDA de 31 %, relèvent le plafond de CAC de 6,13 € — ce qui débloque 2 300 clients par mois inaccessibles autrement —, et font passer la croissance autofinançable de ×6,0 à ×10,0 par an. **Aucun autre levier du cursus ne fait les trois à la fois.** Une baisse de CAC améliore l'acquisition sans améliorer la marge unitaire. Une hausse de panier améliore la marge sans élargir l'audience atteignable. Le premier réachat fait les deux, parce qu'il change la **valeur** de ce que tu achètes, et non son prix.

### 8.3 Les deux trajectoires, à douze mois

Reprenons SÉVANE, à son échelle, sur douze mois et 12 000 nouveaux clients.

*Hypothèses déclarées.* Le passage 1 → 2 de la trajectoire B additionne les deux leviers du § 7 — post-achat +2,1 point, calendrier d'épuisement +3,84 points — **moins leur recouvrement** : une part des clients gagnés le sont par les deux à la fois et ne se comptent qu'une fois. À 36 % de recouvrement, `18,7 + (2,1 + 3,84) × 0,64 = 22,5 %`. Le coefficient de SÉVANE, `K = 0,86 ÷ 0,187 = 4,60`, est mesuré sur ses cohortes M1 à M4 ; il est plus élevé que le 2,82 canonique parce qu'un passage lu à 90 jours sous-estime davantage le réachat annuel quand une partie de la gamme a un cycle de 117 jours.

| | **A — délai fixe, post-achat négligé** | **B — calendrier d'épuisement, post-achat écrit** |
|---|---:|---:|
| Passage 1 → 2 à 90 jours | 18,7 % | **22,5 %** |
| Réachats par client sur 12 mois (× K = 4,60) | 0,86 | **1,03** |
| Contribution de réachat par client | 23,98 € | **28,72 €** |
| LTV 12 mois en contribution | 48,00 € | **52,74 €** |
| LTV / nCAC (28,60 € HT) | 1,68 | **1,84** |
| Contribution annuelle sur 12 000 clients | 576 000 € | **632 880 €** |
| **Écart annuel** | | **+56 880 € HT** |
| Plafond de CAC marginal acceptable | 48,00 € | **52,74 €** |

**+56 880 € HT par an, pour 25 heures d'écriture et 2 160 € d'outil**, sans un euro de budget publicitaire supplémentaire — les deux colonnes dépensent exactement `12 000 × 28,60 = 343 200 €`.

Et le plafond de CAC monte de 4,74 €. *Hypothèse sur la courbe de saturation de SÉVANE, calibrée comme celle d'[E06](../modules/E06-acquisition-payante.md) § 7.2 : le CAC marginal atteint 48,00 € à 12 000 clients par an et 52,74 € à 13 180.* Les **1 180 clients** de cette tranche étaient refusés par la règle d'allocation en trajectoire A ; ils deviennent finançables en trajectoire B, sur le même compte et sans dégrader le ratio.

**Ce que la trajectoire A ne verra jamais.** Son tableau de bord affichera un CRM qui « fait 24 % du chiffre d'affaires » — parce que le dernier clic crédite les flux de récolte. Elle en conclura que la rétention fonctionne, elle ne touchera pas au calendrier, et elle cherchera sa croissance là où elle coûte le plus cher : dans l'enchère.

---

## 9. Avant la séance suivante

1. **Calcule ton calendrier de consommation et capte ta variable d'usage.** Une question dans le tunnel de commande, trois réponses possibles, stockée sur la fiche client. C'est le geste qui conditionne le flux 2, qui est le deuxième plus rentable du dispositif.
2. **Écris les quatre messages du flux post-achat**, avant les six autres flux. Il est le premier au classement incrémental et il ne demande aucun outil sophistiqué.
3. **Lance `cohortes.py` sur ton export réel et programme ta retenue aléatoire.** Écris dès maintenant, dans ton livrable, la séquence retenue, les dates et la date de mesure. [S11](S11-passer-a-l-echelle.md) construira le plan de passage à l'échelle sur ces cohortes : sans elles, il n'y a rien à multiplier.

*Fin de la séance S10. Suite : [S11 — Passer à l'échelle](S11-passer-a-l-echelle.md).*
