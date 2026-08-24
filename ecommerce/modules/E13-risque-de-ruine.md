# Module E13 — Le risque de ruine

> **Prérequis :** [E00](E00-cadrage.md), [E01](E01-arithmetique-de-la-marque.md), [E06](E06-acquisition-payante.md), [E10](E10-cash-et-operations.md), [E12](E12-marque-et-actif.md).
> **Objet :** identifier ce qui peut détruire ton entreprise d'un seul coup, chiffrer chaque menace, et savoir combien tu es prêt à payer pour qu'aucune ne soit mortelle.
> **Temps de travail :** ~7 h (lecture + exercices)

---

## 0. Pourquoi ce module existe

La croissance composée ne survit pas à un zéro. Un multiplicateur nul annule tout ce qui le précède et tout ce qui le suit, quelle que soit la performance accumulée.

*Modèle. Hypothèse pédagogique, trois issues par an :* la marque meurt avec une probabilité `p` ; sinon elle triple une année sur trois et croît de 20 % les deux autres.

```
E[G] conditionnel à la survie = (1/3) × 3,0 + (2/3) × 1,2 = 1,80
Facteur annuel espéré, ruine comprise = (1 − p) × 1,80
   p = 10 % → 1,62   →  1,62^5  = 11,1577
   p =  2 % → 1,764  →  1,764^5 = 17,0802
   17,0802 ÷ 11,1577 = 1,531  →  +53,1 % d'espérance à 5 ans
```

| | p = 10 % / an | p = 2 % / an |
| --- | ---: | ---: |
| Survie à 5 ans | **59,0 %** (0,90⁵) | **90,4 %** (0,98⁵) |
| Survie à 10 ans | 34,9 % | 81,7 % |
| Une chance sur deux d'être mort au bout de | **6,6 ans** | **34,3 ans** |
| Valeur espérée à 5 ans (base 1) | 11,16 × | **17,08 ×** |
| Valeur espérée à 10 ans | 124,49 × | 291,73 × |

**Diviser par cinq la probabilité annuelle de mourir augmente l'espérance à cinq ans de 53 %, sans toucher un levier d'exploitation.** Aucun des sept leviers du § 7 des [chiffres canoniques](../donnees/chiffres-canoniques.md) ne produit ça : le meilleur, +10 % de panier moyen, vaut 71,7 % de l'EBITDA d'une année, pas 53 % de la valeur de cinq.

Les paliers du § 2 vont du mois 1 au mois 40, soit 3,33 ans : `0,90^3,3333 = 70,4 %` contre `0,98^3,3333 = 93,5 %`. **À 10 % de risque annuel, tu as près d'une chance sur trois de ne pas atteindre P5 pour des raisons étrangères à ton marketing.** Le § 7 chiffre le passage de 10 % à 2 %, et démontre que ce coût n'est pas justifiable par l'espérance de perte.

---

## 1. Le bannissement du compte publicitaire

### 1.1 Pourquoi ça arrive

Un compte publicitaire n'est pas un actif que tu possèdes : c'est une autorisation révocable, accordée par une entreprise dont tu n'es pas le client mais le fournisseur d'inventaire. Cinq mécanismes la révoquent.

1. **La politique produit.** Catégorie autorisée mais bordée, classée par une machine à partir de ta page et de ta créa, pas de ton dossier réglementaire.
2. **L'allégation**, seul motif qui déclenche des refus en série puis une fermeture. La conformité s'apprécie sur ce que la publicité **laisse croire**.
3. **La page de destination**, lue par un robot : mention absente, prix barré non conforme, compte à rebours qui se réinitialise, avis sans origine, écart entre l'annonce et la page.
4. **L'historique de compte.** Une accumulation de refus, même corrigés, dégrade un score interne invisible.
5. **L'activité liée.** Un compte personnel, un moyen de paiement, un domaine ou un partenaire déjà sanctionné contamine le tien — le motif le moins contestable, le lien étant établi par une machine.

### 1.2 Ce que ça coûte réellement

Le réflexe est de calculer le CA perdu. C'est faux : à P5, NØRA dépense **49 151 € par jour** (canonique § 5), donc couper Meta *améliore* la trésorerie du mois. Le tableau de bord de court terme s'éclaircit pendant que l'entreprise se vide.

Le § 5 attribue 21 346 nouveaux clients à Meta sur 41 364, pour 37 324 réels (§ 2.4) — 11 % de sur-attribution, répartie uniformément : `21 346 ÷ 41 364 = 51,61 %`, soit **19 261 clients réels par mois**. [E00](E00-cadrage.md) § 4.4 en tire **900 061 €** de contribution nette détruite par mois de coupure — LTV 12 mois des clients non acquis (86,75 €, § 3) moins leur CAC non engagé (40,03 €) —, soit `900 061 ÷ 30,4 = 29 607 € par jour`. S'y ajoute la reprise : un compte rouvert repart en exploration, et [E06](E06-acquisition-payante.md) § 4.5 chiffre l'apprentissage à +30 % de CPA sur les premiers jours.

```
7 jours de reprise = 7 × (821 813 ÷ 30,4)              = 189 233 €
à 38,50 € : 4 915 clients   à 50,05 € (+30 %) : 3 781
Écart = 1 134 attribués × 0,9023 = 1 023 réels × 86,75 € = 88 789 €
```

| Durée de coupure | Contribution détruite | Apprentissage | **Total** | Mois d'EBITDA P5 |
| --- | ---: | ---: | ---: | ---: |
| 3 jours | 88 821 € | 88 789 € | **177 610 €** | 0,49 |
| 11 jours ([C10](../etudes-de-cas/C10-compte-publicitaire-banni.md)) | 325 675 € | 88 789 € | **414 464 €** | 1,14 |
| 30 jours | 900 061 € | 177 578 € | **1 077 639 €** | 2,95 |
| 45 jours | 1 332 195 € | 177 578 € | **1 509 773 €** | 4,14 |

**Un incident de trois jours coûte déjà 177 610 €, dont la moitié en apprentissage** : le coût fixe de redémarrage domine les coupures courtes, ce qui rend une série de petits incidents plus chère qu'un seul long. Ces montants sont un plancher — le § 5 affecte 100 % du média à l'acquisition alors qu'en coupure réelle le réachat tombe aussi ([E12](E12-marque-et-actif.md) § 1.3 : −12 %). **À P2, la même coupure est une sentence** (§ 2.3).

### 1.3 Les mesures, et ce qu'elles valent

- **Conformité des allégations en amont** : un référentiel écrit d'allégations autorisées par produit, avec preuve et source, par lequel toute créa passe avant production. Seule mesure qui agit sur la cause n° 1.
- **Structures de compte redondantes et légitimes** : une entité par marché, avec son domaine, son moyen de paiement, son gestionnaire déclaré, son activité réelle. Redondant ne veut pas dire clandestin — un réseau de comptes créés pour contourner une sanction est lui-même un motif de fermeture définitive.
- **Un représentant de plateforme.** Il n'empêche rien, il raccourcit le délai de traitement — à 29 607 € par jour, ça vaut son poids en réunions.
- **Diversification des canaux**, seule mesure qui change la nature du risque au lieu d'en réduire la probabilité. Ramener Meta de 55 % à 40 % déplace 224 131 € par mois vers des canaux plus chers (§ 5) :

```
224 131 € à 38,50 €                              = 5 822 clients attribués
Réalloué moitié TikTok (44 €), moitié queue (55 €)
   112 066 ÷ 44 = 2 547  +  112 066 ÷ 55 = 2 038 = 4 585 attribués
Écart = 1 237 attribués × 0,9023                  = 1 116 réels/mois
Coût annuel = 1 116 × 86,75 € × 12                = 1 161 774 €
```

**Quinze points de diversification coûtent 1,16 M€ par an, soit 26,5 % de l'EBITDA annuel de P5** (4 377 023 €, § 7). Le calcul surestime — il utilise des CAC moyens quand le CAC marginal de Meta est plus élevé ([E06](E06-acquisition-payante.md) § 6.2) — mais l'ordre de grandeur tient.

> **À retenir :** les trois premières mesures réduisent la probabilité d'un bannissement, aucune ne t'en protège. La seule protection réelle est de ne pas dépendre d'un canal unique, et elle se paie en marge tous les mois, y compris ceux où rien n'arrive. C'est la définition d'une prime d'assurance.

---

## 2. La dépendance, mesurée

### 2.1 Les six concentrations

| Dépendance | Ce qu'on mesure | Vigilance | Alerte | Critique |
| --- | --- | ---: | ---: | ---: |
| Premier canal d'acquisition | part des **nouveaux clients réels**, pas du budget | > 40 % | > 55 % | > 70 % |
| Premier produit | part du CA HT | > 40 % | > 55 % | > 70 % |
| Premier fournisseur | part du COGS annuel | > 50 % | > 70 % | mono-source |
| Premier marché | part de la marge brute | > 40 % | > 55 % | > 70 % |
| Premier prestataire logistique | part des colis expédiés | > 60 % | > 80 % | site unique |
| Premier prestataire de paiement | part des encaissements | > 70 % | > 90 % | PSP unique |

Ces seuils dérivent d'une règle unique : **aucune dépendance ne doit pouvoir consommer plus de la moitié de ta réserve avant que tu aies eu le temps de la remplacer** (§ 7.6). Deux pièges : le canal se compte en clients réels et non en budget ; le fournisseur en COGS annuel et non en références — trois produits chez le même façonnier, c'est une dépendance à 100 %.

### 2.2 NØRA à P5 : ce que Meta pèse vraiment

```
Part du budget publicitaire (§ 5)                              = 55,0 %
Part des nouveaux clients réels  = 19 261 ÷ 37 324             = 51,6 %
Part du CA TTC du mois           = 19 261 × 64,00 ÷ 4 333 196  = 28,4 %
```

La troisième est la plus rassurante et la plus fausse : **elle ignore que 44,9 % du CA est du réachat (§ 2) et que tout client qui réachète a d'abord été acquis quelque part.** En régime établi, 51,6 % de la base vient de Meta, donc 51,6 % du réachat aussi. La dépendance réelle est **51,6 % de tout ce que l'entreprise fera dans les douze mois suivants**.

**Une dépendance à l'acquisition se transmet à la rétention avec un décalage.** Le jour où le canal s'arrête, le CA baisse de 28 % et personne ne panique ; douze mois plus tard la base s'est vidée de moitié, et il est trop tard pour reconstruire un canal.

### 2.3 La même coupure à P2

*Hypothèse : à P2, Meta pèse 80 % des nouveaux clients* — concentration normale à un palier où l'équipe n'a ni le budget ni les bras pour tenir six canaux.

```
Nouveaux clients Meta = 3 400 × 80 %              = 2 720/mois   (§ 2.4)
Contribution détruite = 2 720 × (70,70 − 30,78)   = 108 582 €    (§ 3.1)
Réserve du palier P2                              =  90 530 €    (E10 § 3.1)
```

**Un mois de coupure à P2 détruit 120 % de la réserve du palier** — et le compte de résultat s'améliore : la publicité économisée (83 709 €) dépasse la marge brute perdue, l'EBITDA passe de −19 838 € à environ −12 800 €. La marque publie un meilleur mois et vient de perdre un tiers de son année. À P2, NØRA est **sous** son MER d'équilibre EBITDA (§ 2.3) : elle achète des clients à perte en pariant sur le réachat, et couper l'acquisition annule le pari après avoir payé la mise.

---

## 3. La conformité en Europe

Ce module n'est pas un avis juridique. Il fait deux choses qu'un avocat ne fera pas : dire **où une marque DTC se met réellement en danger**, et **chiffrer** chaque risque contre l'EBITDA.

### 3.1 Les six domaines

| Domaine | Risque et texte | Sanction, ordre de grandeur | Prévention |
| --- | --- | --- | --- |
| **Allégations produit** | Un cosmétique qui prétend traiter une maladie devient un médicament (dir. 2001/83/CE). Cosmétique : règl. (CE) 1223/2009 et (UE) 655/2013 ; santé sur denrées et compléments : règl. (CE) 1924/2006, limité au registre de l'Union | *Fait public :* en France, 2 ans et 300 000 €, **portés à 10 % du CA moyen annuel** des trois derniers exercices (art. L. 132-2 code de la consommation) | Référentiel du § 1.3, un dossier de preuve par allégation, interdiction écrite des formulations de guérison |
| **Pratiques trompeuses** | Fausse urgence, faux avis, prix barré. Dir. 2005/29/CE modifiée « Omnibus » (UE) 2019/2161 : faux avis en liste noire (annexe I) ; une réduction se réfère au **prix le plus bas des 30 derniers jours** (dir. 98/6/CE) | Même L. 132-2, plus un plafond Omnibus d'au moins **4 % du CA annuel** dans les États concernés | Aucun compte à rebours qui se réinitialise, aucun prix barré sans historique, aucun avis sans traçabilité de commande |
| **Rétractation** | Dir. 2011/83/UE : 14 jours, **prolongés de 12 mois si le professionnel n'a pas informé du droit de rétractation** (art. 10) ; l'art. 8 exige un bouton mentionnant l'obligation de payer | Pas une amende : un taux de retour qui change de régime (§ 3.2) | Relecture du parcours par un juriste, une fois, avant l'échelle |
| **Données et suivi** | RGPD (règl. (UE) 2016/679) ; consentement préalable aux traceurs non essentiels (dir. 2002/58/CE art. 5.3) | **20 M€ ou 4 % du CA mondial**, le plus élevé (art. 83.5). *Fait public :* CNIL, décembre 2021, 150 M€ et 60 M€ contre deux plateformes où refuser les traceurs était plus difficile que les accepter | Bannière conforme, base légale par traitement, registre, mesure côté serveur ([E06](E06-acquisition-payante.md) § 2.3) |
| **Étiquetage et sécurité** | Règl. 1223/2009 : personne responsable dans l'Union, dossier d'information produit, rapport de sécurité signé, notification CPNP, étiquetage (INCI, lot, durabilité). Règl. (UE) 2023/988, applicable depuis le 13 décembre 2024 : opérateur responsable et procédure de rappel ; régime britannique distinct | Retrait du marché, interdiction de vente, coût du rappel (§ 4.1) | Chaque marché ouvert dans [E11](E11-passage-a-echelle.md) est une ligne de conformité, pas de traduction |
| **TVA et guichet unique** | Depuis le 1ᵉʳ juillet 2021, seuil unique de **10 000 € HT** de ventes à distance ; au-delà, TVA du pays de destination, déclarable à l'OSS. Risque : facturer au taux d'établissement quand les taux vont de 19 % à 22 % | Rattrapage sur trois exercices, majoration de 40 % pour manquement délibéré (art. 1729 CGI), intérêt de 0,20 %/mois (art. 1727 CGI) | Enregistrement OSS dès le deuxième marché, taux par pays, provision mensuelle |

Seul des six à se calculer directement, *hypothèses : 60 % du CA hors France, écart moyen de 0,8 point de taux* :

```
CA TTC hors France = 0,60 × 51 998 352 €                = 31 199 011 €/an
TVA sur TTC : 0,208 ÷ 1,208 = 17,219 % contre 0,200 ÷ 1,200 = 16,667 %
Écart = 0,552 pt de CA TTC × 31 199 011                 =    172 219 €/an
Trois ans majorés de 40 % : 516 657 × 1,40 = 723 320 €, plus intérêts
                                                        ≈    742 000 €
```

### 3.2 Ce que chaque risque coûte, rapporté à l'EBITDA

EBITDA annuel de référence à P5 : **4 377 023 €** (§ 7). CA HT annuel : 3 610 997 × 12 = **43 331 964 €**.

| Événement chiffré | Coût | % de l'EBITDA annuel |
| --- | ---: | ---: |
| Amende au plafond L. 132-2 : 10 % du CA HT moyen | 4 333 196 € | **99,0 %** |
| Plafond Omnibus transfrontalier : 4 % du CA HT | 1 733 279 € | 39,6 % |
| Rétractation non informée : retours de 3,5 % à 7,0 %, soit 3,5 pts × 433 320 € (§ 7) | 1 516 620 € | 34,6 % |
| Traceurs : dérive de nCAC de 8 %, 40,03 → 43,23 €, × 37 324 × 12 | 1 433 244 € | 32,7 % |
| Rappel de lot (§ 4.1) | 2 519 502 € | 57,6 % |
| TVA multi-pays : rattrapage de trois ans, majoré | ≈ 742 000 € | 17,0 % |

**Une seule sanction au plafond de l'article L. 132-2 efface 99,0 % d'une année d'EBITDA de P5.** Ce n'est pas un aléa d'exploitation, c'est une année blanche.

### 3.3 À quel palier prendre un conseil, et ce que ça coûte

*Hypothèses de marché.* **P1** — CGV, mentions, rétractation, bannière, CPNP, rapport de sécurité : ≈ 5 000 € une fois. **P2** — relecture des allégations : 18 000 à 36 000 €/an. **P3** — OSS et TVA du deuxième marché : + 8 000 à 15 000 €. **P4** — DPO externalisé, audit, RC produit, personne responsable par régime : + 40 000 à 70 000 €. **P5** — conseil permanent et veille multi-pays : 120 000 à 180 000 €.

À P5, **144 000 € par an représentent 3,3 % de l'EBITDA annuel** — 30 pour 1 face à une sanction à 4 333 196 €. Mais le conseil ne ramène pas la probabilité à zéro, il la divise :

```
Probabilité annuelle estimée d'une sanction : 8 % sans conseil, 2 % avec
Espérance économisée = (8 % − 2 %) × 4 333 196 €      =  259 992 €/an
Coût du conseil                                       = −144 000 €/an
                                                        -----------
Gain net en espérance                                    115 992 €/an
```

**C'est l'une des rares lignes du module qui se justifie par l'espérance seule**, et elle le doit à un plafond exprimé en pourcentage du chiffre d'affaires : le seul risque dont l'impact grandit au rythme de ton entreprise.

---

## 4. Le risque produit

### 4.1 Le coût d'un rappel de lot

*Hypothèses de volume, déduites des canoniques § 2 et § 2.1 :* 2,0 unités par commande, le sérum héros fait 45 % des unités, les lots couvrent 60 jours. *Hypothèses de rappel :* la moitié du lot est en entrepôt, l'autre chez les clients ; 35 % des unités vendues sont retournées ; la reformulation prend 45 jours, pendant lesquels la rupture ampute 45 % des commandes.

```
Unités/mois = 60 200 × 2,0 = 120 400
Contrôle du COGS unitaire = 14,5 % × 3 610 997 ÷ 120 400 = 4,35 €
   (cohérent avec la gamme du § 1 : 3,10 € à 4,80 € l'unité)
Unités du héros/mois = 45 % × 120 400 = 54 180 → lot = 108 360 unités
```

| Poste | Calcul | Coût |
| --- | --- | ---: |
| Marchandise détruite en entrepôt | 54 180 × 4,80 € | 260 064 € |
| CA HT annulé sur les unités reprises | 54 180 × 35 % × 39,00 € ÷ 1,2 | 616 298 € |
| Logistique inverse et destruction | 18 963 × 4,50 € | 85 334 € |
| Notification, communication, renfort SAV | *hypothèse* | 60 000 € |
| Rupture : 60 200 × 45 % × 1,5 mois × 36,86 € de marge brute | (§ 2.2 ÷ § 2) | 1 497 806 € |
| **Total** | | **2 519 502 €** |

**Un rappel sur le héros coûte 2,52 M€, soit 6,9 mois d'EBITDA de P5 et 2,03 fois la réserve du palier** (1 243 595 €, [E10](E10-cash-et-operations.md) § 3.1). Et 59 % du total ne vient pas du rappel mais de la rupture qui le suit, ce qui désigne la mesure.

### 4.2 Les mesures, et leur rendement

**La traçabilité des lots.** Le numéro de lot est déjà obligatoire sur l'emballage (règl. 1223/2009 art. 19) ; ce qui manque, c'est la correspondance **lot → commande → client**. Sans elle, un défaut sur un lot devient un rappel sur tout : `260 064 €` de marchandise détruite contre `1 832 581 €` de stock (§ 4), **1 572 517 € d'écart**, pour environ 26 500 € la première année (ERP/WMS et sérialisation à 0,01 € l'unité).

**L'assurance responsabilité civile produit.** *Hypothèse de marché : 0,15 à 0,45 % du CA HT, plafond 5 à 10 M€* — à 0,25 %, 108 330 € par an. **Elle couvre les dommages causés à des tiers, presque jamais le rappel lui-même** : les frais de retrait sont une garantie distincte, la perte d'exploitation une troisième. Une marque assurée en RC seule découvre au pire moment qu'elle a payé pour autre chose.

**Le double fournisseur.** Assurance de disponibilité, mais aussi de qualité : deux sites, deux lots, deux chaînes de matières premières — un défaut ne peut plus atteindre 100 % du volume.

```
COGS annuel P5 = 14,5 % × 43 331 964 €                     = 6 283 135 €
Part transférée 30 %                                        = 1 884 941 €
Surcoût (hypothèse : perte de remise de volume, 4 %)        =    75 398 €/an
Qualification du second (stabilité, challenge test, dossier
   d'information produit)                                   =    25 000 € une fois
Seuil contre une rupture de 45 j : 75 398 ÷ 1 497 806       = 5,0 %/an
```

**Si tu estimes à plus de 5 % par an la probabilité qu'un fournisseur unique t'arrête 45 jours** — défaut, incendie, faillite, litige, blocage douanier, non-conformité —, il est rentable en espérance avant même de compter ce qu'il apporte sur le rappel. Il l'est presque toujours.

**Le dépôt de marque**, contre la contrefaçon. Sans lui, tu ne peux ni faire retirer une copie sur une place de marché, ni empêcher un tiers de déposer ton nom là où tu n'es pas encore, ni vendre sans décote : l'actif de [E12](E12-marque-et-actif.md) n'existe juridiquement pas. *Fait public :* le barème EUIPO d'une marque de l'Union déposée en ligne est de 850 € pour une classe et 150 € par classe supplémentaire, pour dix ans. **Meilleur rapport protection/prix du cursus, manqué par presque toutes les marques avant P3.**

---

## 5. Le risque de paiement

### 5.1 Le seuil qui ferme le compte

Une rétrofacturation (*chargeback*) est un rejet de paiement à l'initiative du porteur de carte, après livraison. Les réseaux surveillent ton taux mensuel et l'imposent à ton prestataire de paiement (PSP). *Ordres de grandeur publics, barèmes révisés régulièrement :* surveillance vers **0,9 % de litiges et au moins 100 cas** chez Visa, **1,5 % et 100 cas** chez Mastercard. Ton PSP réagit avant : questions vers 0,3 %, réserve glissante vers 0,5 %, plan de remédiation vers 1 %, résiliation au-delà de 1,5 %.

Le coût d'un cas n'est pas le montant remboursé : c'est le chiffre d'affaires qui disparaît alors que tous les coûts variables ont été engagés, plus les frais de dossier. `71,98 ÷ 1,2 = 59,98 € de CA HT` (§ 2), plus 20,00 € de frais — *hypothèse de marché* — soit **79,98 € par cas**.

| Taux | Cas/mois sur 60 200 cmd | Coût mensuel | Coût annuel | % de l'EBITDA annuel |
| ---: | ---: | ---: | ---: | ---: |
| 0,35 % | 211 | 16 876 € | 202 512 € | 4,6 % |
| 1,00 % | 602 | 48 148 € | 577 776 € | 13,2 % |
| 1,50 % | 903 | 72 222 € | 866 664 € | **19,8 %, et le compte ferme** |

La ligne du bas n'est pas un problème de marge : à 1,5 %, la perte de 866 664 € est le moindre des soucis.

```
CA TTC quotidien = 4 333 196 ÷ 30,4                 =  142 539 €
Une semaine sans encaisser                           =  997 773 €
Réserve glissante PSP (hypothèse : 7,5 % sur 90 j)   =  962 138 €
Effet sur le BFR de 2 264 655 € (§ 4)                 =  + 42,5 %
```

**Une suspension d'encaissement transforme un problème de fraude en problème de trésorerie du jour au lendemain** — seul risque du module qui coupe les entrées de cash au lieu d'augmenter les sorties, donc le plus rapide à tuer.

### 5.2 La prévention, et son prix en conversion

L'authentification forte (3-D Secure 2), imposée par la directive (UE) 2015/2366 et ses normes techniques, déplace la responsabilité de la fraude vers l'émetteur de la carte. Elle coûte de la conversion.

```
Hypothèse : 3DS systématique fait perdre 2 points d'autorisation sur
   une base de 95 %, soit −2,1 % en relatif.
Le § 7 donne : +10 % de conversion = 2 662 749 € d'EBITDA annuel.
   Coût de la mesure = 2 662 749 × (2,1 ÷ 10)        = 559 177 €/an
Gain : passer de 1,00 % à 0,35 % → 577 776 − 202 512 = 375 264 €/an
                                                       -----------
Solde en régime normal                                 −183 913 €/an
```

**Le 3DS systématique n'est pas rentable en régime normal, et il l'est absolument en régime dégradé** — parce qu'à ce moment-là il n'achète pas de la marge, il achète le droit de continuer à encaisser. C'est le raisonnement du § 0 : une mesure d'espérance négative devient obligatoire quand l'issue qu'elle évite est absorbante.

Entre les deux, quatre mesures au coût faible ou nul. **Le libellé sur le relevé bancaire** : la première cause de rétrofacturation en DTC n'est pas la fraude, c'est le client qui ne reconnaît pas la ligne — coût zéro, meilleur rendement du module. **Le délai de livraison** : un colis à douze jours produit des litiges « marchandise non reçue », donc le SAV de [E10](E10-cash-et-operations.md) § 6 est une mesure anti-fraude. **Le 3DS ciblé par score.** **Les plafonds** par carte, par adresse et par fenêtre de temps.

---

## 6. Les concentrations invisibles

### 6.1 La saison

Une marque qui fait 40 % de son année en novembre-décembre n'a pas un problème de calendrier : elle a une structure de risque différente.

```
CA TTC annuel P5 = 4 333 196 × 12 = 51 998 352 €
40 % sur deux mois = 20 799 341 € contre 8 666 392 € en régime plat
   Intensité du pic = ×2,40
Les dix autres mois = 3 119 901 €, soit 72,0 % du régime
```

**Le stock.** Le pic exige 2,40 fois le stock du régime : `1 832 581 × 2,40 = 4 398 194 €`, soit **2 565 613 € de trésorerie immobilisée en plus**, engagés 90 à 120 jours avant, sur une prévision. Et l'erreur de prévision est asymétrique :

```
Sous-estimation de 25 % : 0,25 × 20 799 341 = 5 199 835 € TTC non faits
   → 5 199 835 ÷ 71,98 = 72 240 cmd × 36,86 € de marge brute = 2 662 766 €
Surestimation de 25 % : le stock se vendra, à −30 % de prix
   CA HT/cmd 59,98 → 41,99 €, marge brute 36,86 → 18,87 €
   → 72 240 × 17,99 €                                        = 1 299 598 €
Rapport = 2,05
```

**Se tromper par défaut coûte deux fois plus que se tromper par excès** — à condition de pouvoir porter le surstock (§ 6.3). C'est la seule justification chiffrée de la sur-commande saisonnière, et elle s'annule le jour où le cash manque.

**La plateforme.** Le même incident coûte 2,40 fois plus cher en saison : `29 607 × 2,40 = 71 057 €` par jour, soit **781 627 € pour les onze jours de [C10](../etudes-de-cas/C10-compte-publicitaire-banni.md)** contre 325 675 €. Et sa probabilité monte au même moment : plus de créas neuves, plus de pages modifiées, plus d'allégations promotionnelles, plus de contrôles. **Le risque n'est pas la moyenne annuelle rapportée à un mois, c'est un pic de probabilité multiplié par un pic d'impact.** Le CPM y monte aussi de 25 à 50 % ([E06](E06-acquisition-payante.md) § 7.5) ; [C09](../etudes-de-cas/C09-piege-du-black-friday.md) chiffre le ciseau complet.

**La mesure.** Lisser : passer de 40 % à 28 % ramène le pic à ×1,68 et libère `1 832 581 × 0,72 = 1 319 458 €`. Leviers — rechargement et abonnement ([E08](E08-retention-et-ltv.md)), marchés à saisonnalité décalée ([E11](E11-passage-a-echelle.md)), et ne pas construire l'offre autour de la remise. *Seuil d'alerte :* **plus de 35 % du CA annuel sur un trimestre.**

### 6.2 La personne

Le test tient en une phrase : **que se passe-t-il si cette personne s'arrête trois semaines, sans préavis ?** Le pilotage de l'acquisition coûte cher sans tuer — *hypothèse : 8 % de dérive du MER*, ≈ 122 000 € de marge brute sur trois semaines. La relation fournisseur devient grave à partir de P3 : commandes en cours, spécifications non écrites, conditions négociées. Deux fonctions seulement sont des risques de ruine, et ce sont les deux les moins chères à supprimer.

**Les accès.** Un seul administrateur sur le Business Manager, le domaine, le DNS, le PSP, la banque ou l'ERP est une porte unique : départ conflictuel, accident, compte compromis. Mesures : deux administrateurs par système, gestionnaire de secrets, clé matérielle sur les comptes sensibles, domaine et DNS enregistrés **au nom de la société**, procédure de départ écrite. *Environ 9 000 € par an* — la meilleure ligne du registre (§ 7.3).

**L'associé.** Pacte avec vesting sur quatre ans et cliff d'un an, clauses *good leaver* / *bad leaver*, promesse croisée, clause d'agrément ; *hypothèses : 6 000 à 15 000 € de rédaction, assurance homme clé 0,3 à 0,8 % du capital assuré par an.* Il s'écrit quand tout va bien, parce qu'il ne s'écrit jamais après.

**La documentation.** Le test n'est pas « existe-t-il une procédure » mais « une personne compétente qui n'était pas là peut-elle reprendre le poste avec ce qui est écrit ». *Seuil d'alerte :* **tout processus critique à porte unique qui touche l'entrée ou la sortie de cash.**

### 6.3 La trésorerie, sous l'angle de la ruine

[E10](E10-cash-et-operations.md) traite le cash comme une contrainte de croissance. Ici il n'est plus qu'une chose : **le nombre de semaines qui te séparent du moment où tu ne peux plus payer un fournisseur.**

```
Semaines de trésorerie de survie
   = (Trésorerie nette disponible − engagements non annulables à moins de 90 j)
     ÷ Frais fixes hebdomadaires
```

Les définitions comptent plus que la formule, parce que c'est là que tout le monde triche. **Trésorerie nette disponible** = solde bancaire + encaissements PSP à recevoir sous 7 jours, **moins** TVA collectée non reversée, dettes fournisseurs échues ou à 30 jours, commandes encaissées non expédiées, charges sociales et fiscales dues, crédit remboursable à vue. **Engagements non annulables** = commandes fournisseurs signées, loyers et contrats à préavis long, recrutements signés, engagements média forfaitaires.

```
Réserve du palier P5 = 2 mois de fixes + 1 mois de COGS  = 1 243 595 €
Frais fixes hebdomadaires = 360 000 ÷ 4,3333             =    83 077 €
Engagements fournisseurs en cours (stock 1 832 581 € à 60 j
   de couverture, soit un mois de commande engagé)       =   916 291 €
Semaines de survie = (1 243 595 − 916 291) ÷ 83 077      =   3,9 semaines
```

**La réserve calibrée pour un choc d'exploitation tient 3,9 semaines face à un choc de ruine.** Pas une contradiction avec E10 : E10 dimensionne pour réagir, E13 pour ne pas mourir pendant qu'on réagit. Le seuil dérive de ton délai de réaction le plus long — le délai fournisseur, 90 jours en cosmétique à façon ([E10](E10-cash-et-operations.md) § 5).

| Semaines de survie | Régime | Ce que tu fais |
| ---: | --- | --- |
| > 26 | Confort | Tu peux investir et prendre des risques d'allocation |
| 13 à 26 | Normal | Un cycle fournisseur complet est couvert |
| 8 à 13 | **Vigilance** | Gel de tout engagement nouveau au-delà de 8 semaines |
| 4 à 8 | **Alerte** | Le plan de réduction s'exécute, il ne s'écrit plus |
| < 4 | Ruine à vue | Tu appelles tes fournisseurs avant qu'ils ne t'appellent |

Trésorerie requise à P5 : `916 291 + 13 × 83 077 = 1 996 292 €` contre 1 243 595 € de réserve, soit **752 697 € manquants — 2,1 mois d'EBITDA.**

---

## 7. Le registre des risques, et la règle de Kelly

### 7.1 La méthode

Six colonnes, revues chaque trimestre, tenues par une personne nommée. Pas un document de conformité : un outil d'allocation. **Le risque**, formulé comme un événement daté et mesurable — « coupure Meta de 11 jours », pas « dépendance aux plateformes ». **La probabilité annuelle**, déclarée comme une estimation : tu ne la connais pas, écris-la quand même — un nombre faux se corrige, une intuition non écrite ne se corrige jamais. **L'impact en euros**, calculé. **L'espérance** = probabilité × impact. **La mesure**, et ce qu'elle change. **Son coût annuel**, y compris en marge ou en conversion.

### 7.2 Le registre de NØRA au palier P5

*Toutes les probabilités sont des estimations déclarées, pas des mesures. Les impacts sont dérivés dans les sections précédentes.*

| # | Risque | p/an | Impact | Espérance | Mesure | Coût/an | p rés. | Impact rés. | Espér. rés. |
| --- | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| R1 | Bannissement Meta, 11 j (§ 1.2) | 25 % | 414 464 € | 103 619 € | Référentiel d'allégations, comptes redondants, contact plateforme | 36 000 € | 10 % | 414 464 € | 41 448 € |
| R2 | Coupure Meta ≥ 30 j (§ 1.2) | 6 % | 1 077 639 € | 64 658 € | *(même mesure)* | — | 2,5 % | 1 077 639 € | 26 941 € |
| R3 | Sanction allégations (§ 3.2) | 8 % | 650 000 € | 52 000 € | Conseil juridique permanent, DPO | 108 000 € | 2 % | 650 000 € | 13 000 € |
| R4 | Traceurs, perte de signal (§ 3.2) | 5 % | 1 583 244 € | 79 162 € | Mesure côté serveur, gestion du consentement | 60 000 € | 1,5 % | 1 583 244 € | 23 749 € |
| R5 | Rappel de lot (§ 4.1) | 2 % | 2 519 502 € | 50 390 € | Traçabilité lot → client, garantie frais de retrait | 71 500 € | 1 % | 1 100 000 € | 11 000 € |
| R6 | Rupture fournisseur, 45 j (§ 4.2) | 6 % | 1 497 806 € | 89 868 € | Double fournisseur, 70 / 30 | 75 398 € | 1,5 % | 400 000 € | 6 000 € |
| R7 | Rétrofacturations > seuil PSP (§ 5.1) | 4 % | 1 200 000 € | 48 000 € | Scoring, 3DS ciblé, libellé bancaire, délai | 69 267 € | 1 % | 1 200 000 € | 12 000 € |
| R8 | Perte des accès critiques (§ 6.2) | 8 % | 900 000 € | 72 000 € | Double administrateur, clés matérielles, propriété société | 9 000 € | 1,5 % | 900 000 € | 13 500 € |
| | **Total** | | | **559 697 €** | | **429 165 €** | | | **147 638 €** |

### 7.3 L'espérance de perte contre le coût des mesures

```
Espérance de perte annuelle, sans mesures   =  559 697 €  = 12,8 % de l'EBITDA
Espérance de perte annuelle, avec mesures   =  147 638 €  =  3,4 % de l'EBITDA
Gain en espérance                            =  412 059 €
Coût annuel des mesures                      = −429 165 €  =  9,8 % de l'EBITDA
                                               ----------
Solde                                            −17 106 €
```

**Le programme coûte 17 106 € de plus qu'il ne rapporte en espérance.** Ligne par ligne :

| Ligne | Gain en espérance | Coût | **Net** | Impact ÷ réserve |
| --- | ---: | ---: | ---: | ---: |
| R1 + R2 — conformité publicitaire | 99 888 € | 36 000 € | **+63 888 €** | × 0,33 et × 0,87 |
| R8 — accès | 58 500 € | 9 000 € | **+49 500 €** | × 0,72 |
| R6 — double fournisseur | 83 868 € | 75 398 € | **+8 470 €** | **× 1,20** |
| R4 — traceurs | 55 413 € | 60 000 € | −4 587 € | **× 1,27** |
| R5 — rappel | 39 390 € | 71 500 € | −32 110 € | **× 2,03** |
| R7 — paiement | 36 000 € | 69 267 € | −33 267 € | × 0,96 |
| R3 — conseil juridique | 39 000 € | 108 000 € | −69 000 € | × 0,52 |

*(R3 n'est chiffré ici que sur le périmètre de la sanction ; le § 3.3 le rend positif dès qu'on lui affecte la part de R4 et R5 qu'il couvre aussi. Une mesure couvre plusieurs lignes.)*

### 7.4 Pourquoi le résultat est négatif, et pourquoi on le fait quand même

Lis la dernière colonne. Quatre impacts approchent ou dépassent la réserve du palier (1 243 595 €) : R4, R5, R6, R7. **Trois d'entre eux — R4, R5, R7 — sont couverts par des mesures que l'espérance de perte condamne.** Classe ton registre par gain net et tu supprimes exactement les trois mesures qui te maintiennent en vie.

> *Hypothèse liant ce tableau au § 0 :* l'ensemble de ces mesures fait passer la probabilité annuelle de ruine — la conjonction d'un choc et d'une trésorerie insuffisante pour l'absorber — d'environ **10 %** à environ **2 %**. C'est une estimation, pas une mesure ; c'est la seule chose du module que tu ne pourras pas vérifier avant de l'avoir vécue.

```
Valorisation de P5 à 6 × EBITDA (hypothèse, E10 § 4.2)
   6 × 4 377 023 €                                 = 26 262 138 €
Survie à 5 ans : 90,4 % au lieu de 59,0 % (§ 0)    = +31,4 points
Valeur de survie créée = 0,314 × 26 262 138 €      =  8 231 342 €
Coût du programme sur 5 ans = 5 × 429 165 €        =  2 145 825 €
                                                     -----------
Rapport                                                   3,84 pour 1
```

> **À retenir :** la réduction du risque ne se justifie presque jamais par l'espérance de perte annuelle. Elle se justifie par la probabilité de survie multipliée par la valeur de l'actif. Un registre lu en espérance dit de ne rien faire, le même registre lu en survie dit de tout faire. **Le second a raison, et c'est le premier qu'on présente en réunion.**

Trois limites. Les risques ne sont **pas indépendants** — un rappel en novembre, une rupture qui provoque un pic de litiges : sommer des espérances indépendantes sous-estime la queue de distribution. Les probabilités sont **tes** estimations, donc tes biais. Et le registre ne contient que les risques que tu as su nommer.

### 7.5 La règle de Kelly, appliquée informellement

Le critère de Kelly détermine la fraction du capital à miser pour maximiser la croissance à long terme d'une série de paris. Sa conclusion opérationnelle tient en une phrase.

```
Aucun pari, si favorable soit-il, ne doit être dimensionné de telle sorte
qu'une issue défavorable te retire la capacité de faire le pari suivant.
```

**La demi-Kelly.** La fraction optimale est déjà agressive quand on connaît les probabilités — or on ne les connaît pas, et surestimer la probabilité de gain fait croître le risque de ruine bien plus vite que la sous-estimer ne coûte de rendement. **Quand tu hésites entre deux tailles de pari, prends la plus petite.**

**La mise n'est pas ce que tu peux perdre.** Applique Kelly à la commande du § 6.1 : mise 2 565 613 €, gain de l'ordre de 4,2 fois la mise, perte limitée à un quart puisque le stock se vend, plus tard, en remise. Kelly te répond de miser plus de 100 % du capital, et il a raison sur la marge. Mais tu paies en septembre et tu encaisses en décembre : si un bannissement, un rappel ou une suspension de PSP tombe entre les deux, tu as un entrepôt plein et pas un euro. **Dans une marque DTC, la mise de Kelly n'est pas ce que tu risques de perdre, c'est ce que tu immobilises.** La faillite n'arrive pas parce que tu as perdu de l'argent, elle arrive parce que ton argent est dans un entrepôt.

### 7.6 Les trois plafonds

**Dépense publicitaire.** La dépense d'un mois est engagée sans savoir si elle produira ; le cycle fournisseur est ta durée de réaction. `Trésorerie nette minimale = dépense d'un mois + 13 semaines de frais fixes`, soit à P5 `1 494 206 + 13 × 83 077 = 2 574 207 €`. En dessous, chaque euro de budget supplémentaire augmente ton risque de ruine plus qu'il n'augmente ton EBITDA.

**Commande fournisseur.** Aucune commande unique ne dépasse **25 % de la trésorerie nette disponible**, ni **60 jours de couverture** au rythme des huit dernières semaines. À P5 : `25 % × 2 574 207 = 643 552 €` quand le stock vaut 1 832 581 € — donc trois commandes en rotation permanente au minimum. *Coût de la règle, hypothèse : trois lots au lieu d'un coûtent 3 % sur le COGS, soit 188 494 € par an.* **C'est le prix explicite de la survie, et il n'apparaît sous ce nom dans aucun compte de résultat.**

**Exposition à un marché.** Aucun marché ne dépasse **40 % de la marge brute**, seuil dérivé du temps de réaction et non d'un chiffre rond. Face à un arrêt total — interdiction de vente, retrait réglementaire, blocage douanier :

```
Marge brute mensuelle P5 = 2 218 957 €, fixes 360 000 € (§ 2.2)
Trésorerie de référence  = 2 574 207 €
Exposition 40 % : EBITDA = 364 752 − 887 583   =   −522 831 €/mois → 4,9 mois
Exposition 60 % : EBITDA = 364 752 − 1 331 374 =   −966 622 €/mois → 2,7 mois
Exposition 80 % : EBITDA = 364 752 − 1 775 166 = −1 410 414 €/mois → 1,8 mois
```

**Le seuil de 40 % achète cinq mois : c'est la durée d'ouverture d'un nouveau marché** ([E11](E11-passage-a-echelle.md), [C07](../etudes-de-cas/C07-ouverture-allemagne.md)). Au-delà, le choc arrive plus vite que ta capacité à le compenser.

---

## 8. Les erreurs qui coûtent cher

**1 — N'avoir qu'un compte publicitaire, qu'un fournisseur, qu'un entrepôt.** Deux se chiffrent : un bannissement de 11 jours vaut **414 464 €** (§ 1.2), une rupture fournisseur de 45 jours **1 497 806 €** (§ 4.2). Le troisième ne se chiffre pas — un incendie arrête 100 % des expéditions, l'impact est le CA et pas une fraction. *Correction :* 36 000 € de conformité, 75 398 € de double fournisseur, un second site de préparation à partir de P4.

**2 — Ne pas lire les politiques publicitaires de sa catégorie.** Publiques, quelques dizaines de pages, écrites pour dire ce qui fait fermer un compte. *Coût de ne pas les lire :* la probabilité de R1 passe de 10 % à 25 %, soit `0,15 × 414 464 = 62 170 €` par an. *Coût de les lire :* une journée.

**3 — Faire une allégation de santé sur un cosmétique.** L'erreur la plus rentable à court terme du secteur : elle améliore le clic, la conversion, le CAC, tous les indicateurs à sept jours. Elle expose à une requalification en médicament (dir. 2001/83/CE) et à l'article L. 132-2, dont le plafond vaut **4 333 196 €, soit 99,0 % de l'EBITDA annuel de P5** (§ 3.2). Une année d'exploitation pour un point de conversion.

**4 — Ignorer un taux de rétrofacturation qui monte.** Il monte lentement, de 0,3 % à 0,5 % puis 0,9 %, sur des mois où personne ne le regarde parce qu'il ne pèse que 4,6 % de l'EBITDA (§ 5.1). Puis le PSP constitue une réserve de **962 138 €**, soit 42,5 % du BFR, et l'entreprise passe de « légère dégradation de marge » à « rupture de trésorerie » sans étape intermédiaire. *Correction :* un indicateur glissant sur 30 jours, seuil écrit à 0,50 %.

**5 — Ne pas avoir trois mois de trésorerie.** Trois mois est déjà le mauvais chiffre : la bonne mesure est le cycle fournisseur plus quatre semaines, soit **13 semaines de frais fixes après déduction des engagements non annulables** (§ 6.3). À P5, la réserve d'E10 en couvre 3,9. *Manque : 752 697 €*, soit 2,1 mois d'EBITDA.

**6 — Tenir un registre et le classer par gain net.** Le § 7.4 le démontre : les trois impacts qui dépassent la réserve sont couverts par des mesures d'espérance négative, et le tri par rentabilité les supprime toutes les trois. *Coût :* l'écart entre 59,0 % et 90,4 % de survie à cinq ans, soit **8 231 342 €** de valeur d'entreprise.

**7 — Sur-commander à la saison avec la trésorerie de la basse saison.** L'asymétrie du § 6.1 justifie la sur-commande — 2 662 766 € contre 1 299 598 € — **et cesse de la justifier dès que le surstock ne peut plus être porté.**

---

## 9. Ce que ce module ne dit pas

**Les risques macroéconomiques.** Le change n'est pas traité : acheter en dollars expose le COGS annuel de P5, **6 283 135 €**, à 628 313 € pour dix points de parité — la ligne « −10 % de COGS » du § 7 des canoniques, dans le mauvais sens et sans contrepartie. Douane, énergie, fret et coût du capital relèvent de la même famille : ils frappent la marge brute sans prévenir, ne se réduisent pas par une mesure interne, et se couvrent par des instruments que ce cursus n'enseigne pas. **Ils appartiennent au registre, avec une probabilité et un impact, même quand aucune mesure n'existe** — une ligne sans mesure dimensionne la réserve.

**Le détail juridique national.** Le § 3 énonce des textes européens et des ordres de grandeur. Il ne dit ni ce qui s'applique à ta forme juridique, à ton pays d'établissement et à ton statut d'importateur ou de distributeur, ni comment l'autorité de chaque marché applique réellement ces règles. Seuils, taux et régimes changent. **Responsabilité produit, fiscalité transfrontalière et données personnelles exigent un conseil identifié, pas une lecture de module.**

**Trois absences volontaires.** L'assurance, traitée seulement par la RC produit (§ 4.2) : perte d'exploitation, cyber, responsabilité des dirigeants et crédit client relèvent d'un courtier. Le risque de réputation, non modélisable en espérance, qui se gère par la marque ([E12](E12-marque-et-actif.md)). La restructuration, qui commence là où ce module s'arrête ([C08](../etudes-de-cas/C08-redressement-90-jours.md)).

**Ce module suppose que tu veux survivre**, et ce n'est pas toujours le bon objectif. Une marque financée en capital-risque, dont l'actionnaire tient vingt lignes, maximise rationnellement l'espérance et non la survie : la ruine d'une ligne ne le ruine pas. [E10](E10-cash-et-operations.md) § 4.2 chiffre le prix de cette assurance — le capital-risque coûte six fois la dette la plus chère. **Si tu es le seul actionnaire, la seule ligne de ton portefeuille est ton entreprise, et le § 0 s'applique intégralement.**

---

## 10. Le tableau de bord du module

| # | Indicateur | Calcul | Fréquence | Seuil d'alerte |
| --- | --- | --- | --- | --- |
| 1 | **Semaines de trésorerie de survie** | (Trésorerie nette − engagements non annulables < 90 j) ÷ frais fixes hebdo. (§ 6.3) | Hebdomadaire | < 13 semaines |
| 2 | **Part du premier canal** | Nouveaux clients **réels** du premier canal ÷ total (§ 2.1) | Mensuelle | > 55 % |
| 3 | **Taux de rétrofacturation glissant** | Cas ÷ transactions, fenêtre de 30 jours (§ 5.1) | Hebdomadaire | > 0,50 % |
| 4 | **Processus critiques à porte unique** | Processus touchant l'entrée ou la sortie de cash qu'une seule personne sait exécuter (§ 6.2) | Trimestrielle | > 0 |
| 5 | **Part du trimestre le plus fort** | CA TTC du meilleur trimestre ÷ CA TTC annuel glissant (§ 6.1) | Trimestrielle | > 35 % |
| 6 | **Lignes du registre non couvertes** | Risques dont l'impact dépasse la réserve du palier et dont la mesure n'est pas exécutée (§ 7.4) | Trimestrielle | > 0 |

Le 1 est le seul qui ne ment jamais — à condition que ses soustractions soient faites honnêtement. Le 6 est le seul indicateur du cursus dont le seuil est zéro : une ligne d'impact supérieur à la réserve n'est pas un risque à surveiller mais une décision à prendre. Aucun des six ne figure dans une interface publicitaire ou un logiciel de comptabilité — ils se tiennent à la main.

---

## 11. Exercices

À rendre dans [`ecommerce/exercices/E13-rendu.md`](../exercices/E13-rendu.md) ; corrigés dans `E13-corrige.md`.

**1 — La survie de NØRA (réponse numérique unique).** Reprends le modèle du § 0 : survie à 3, 5, 10 et 20 ans pour `p = 5 %`, `10 %` et `20 %`, durée au bout de laquelle il y a une chance sur deux d'être mort, espérance de valeur à 5 ans. Modifie ensuite le modèle — la marque triple une année sur cinq, les autres à ×1,15. Quel `p` faut-il pour que l'espérance à 5 ans égale celle de l'ancien modèle à `p = 10 %` ? Conclus en une phrase sur l'arbitrage croissance / survie.

**2 — Le registre recalculé (réponse numérique unique).** Reprends le § 7.2 avec trois jeux de probabilités : les tiennes divisées par deux, multipliées par deux, et le cas où R1 passe à 40 %. Pour chacun : espérance totale, espérance résiduelle, solde contre les 429 165 € de coût, mesures qui deviennent positives. À partir de quel multiplicateur le programme devient-il rentable **en espérance seule** ?

**3 — Ton registre des risques.** Six colonnes (§ 7.1), dix lignes minimum. Chaque impact est calculé et sa ligne de calcul figure dans le tableau ; chaque probabilité est un nombre écrit ; chaque mesure a un coût annuel, y compris en marge ou en conversion. Fais les deux tris — par gain net, et par rapport de l'impact à ta réserve — et note les lignes qui changent de rang. *Grille de lecture : si les deux classements donnent le même ordre, tu as sous-estimé au moins un impact.*

**4 — Ta trésorerie de survie.** Applique la formule du § 6.3 sur ton dernier relevé, avec toutes les soustractions. Liste tes engagements non annulables à moins de 90 jours avec leur date. Donne ton nombre de semaines, ton délai fournisseur réel mesuré sur tes trois dernières commandes, et l'écart. S'il est négatif, chiffre le montant à réunir et la date à laquelle il doit l'être.

**5 — Tes six dépendances.** Mesure les six lignes du § 2.1 sur douze mois, dans les unités indiquées. Ajoute pour chacune **le délai de substitution** : le nombre de semaines nécessaires pour la remplacer si elle disparaissait demain. Multiplie ce délai par ta perte hebdomadaire dans ce scénario, compare à ta réserve, et classe tes dépendances par ce produit. La première est ton vrai risque, quel que soit son pourcentage.

**6 — Décision : diversifier ou tenir.** Ton premier canal pèse 62 % de tes nouveaux clients réels, à 34 € de CAC quand les autres sont à 48 €. Diversifier jusqu'à 45 % coûterait, par la méthode du § 1.3, un montant que tu calculeras sur tes volumes. Ton directeur de l'acquisition refuse : le canal est rentable, le CAC marginal du second dépasse la LTV 12 mois, et la diversification dégrade le MER. Tranche, en chiffrant les deux options sur 24 mois, puis écris la condition précise — en probabilité annuelle de bannissement, en semaines de trésorerie, ou en part du réachat dans ton CA — sous laquelle la décision inverse serait la bonne. *La correction donne les deux réponses et le point où elles s'inversent.*

---

*Fin du module E13. Suite : [E14](E14-plan-1M-semaine.md), qui assemble le cursus en un plan daté et intègre les plafonds du § 7.6 comme contraintes et non comme conseils. Pour la dépendance de plateforme vécue de l'intérieur, [C10](../etudes-de-cas/C10-compte-publicitaire-banni.md) ; pour la trésorerie que ce module resserre, [E10](E10-cash-et-operations.md) ; pour le pic saisonnier du § 6.1, [C09](../etudes-de-cas/C09-piege-du-black-friday.md) ; pour la sortie de crise quand une de ces lignes s'est réalisée, [C08](../etudes-de-cas/C08-redressement-90-jours.md).*
