# Séance S11 — Passer à l'échelle

> **Niveau requis :** L06 (visée L08) · **Durée :** 10 h · **Livrable :** le plan de passage de 30 000 € à 300 000 € TTC de CA mensuel en douze mois, chiffré mois par mois, **avec les trois contraintes traitées ensemble** — machine créative, trésorerie, organisation · **Modules :** [E05](../modules/E05-machine-creative.md), [E10](../modules/E10-cash-et-operations.md), [E11](../modules/E11-passage-a-echelle.md)
> **Ce que tu ne peux pas faire sans avoir fait cette séance :** multiplier ton budget par dix sans découvrir, au septième mois, que les trois choses qui devaient tenir ne tenaient pas — et qu'aucune des trois ne se répare en moins d'un trimestre.

---

## 1. Où tu en es

Tu as lancé ([S08](S08-le-lancement.md)), lu tes premiers chiffres sans te mentir ([S09](S09-lire-les-premiers-chiffres.md)), installé la rétention et produit un tableau de cohortes réel ([S10](S10-installer-la-retention.md)). Ta marque tourne à environ **30 000 € TTC par mois** et ne gagne pas d'argent : le modèle de référence est à −30,7 % d'EBITDA au palier P1 et −10,3 % à P2 ([canoniques § 2.2](../donnees/chiffres-canoniques.md)).

**Décidé :** catégorie, produit, prix, angles, page, flux de rétention. **Pas décidé :** à quelle vitesse tu montes, avec quel argent, et avec qui.

Multiplier par dix fait apparaître **trois contraintes en même temps**, et la plupart des gens n'en traitent qu'une. La **créa** : ton budget est nourri par une bibliothèque de gagnants qui s'épuise d'autant plus vite que tu dépenses. Le **cash** : la croissance immobilise du stock et de l'avance publicitaire **avant** de rendre de la marge. L'**organisation** : le fondateur qui fait tout finit par devenir le goulot de tout.

La boucle qu'elles forment est auto-renforçante : le budget monte, la créa ne suit pas, la fréquence monte, le MER baisse, le CM3 baisse, le cash baisse — donc on reporte l'embauche qui aurait fait suivre la créa. Six mois plus tard on est plus gros, plus lent et plus pauvre.

*Sigles : **MER** — CA TTC ÷ dépense publicitaire. **CM2** — marge brute après coûts variables. **CM3** — marge brute moins dépense publicitaire. **BFR** — cash immobilisé dans le cycle d'exploitation. **nCAC** — dépense publicitaire totale ÷ nouveaux clients. **ETP** — équivalent temps plein.*

---

## 2. Ta mission

Produire **un seul document** : le plan à douze mois, chiffré mois par mois, où les trois contraintes sont résolues ensemble et pas l'une après l'autre.

1. **Le verdict de porte** — les dix conditions de la [porte P2 → P3](../mentorat/jalons.md), valeurs **mesurées**, verdict par ligne, date d'exigibilité calculée pour celles qui ne sont pas encore contraignantes.
2. **Le plan de production créative** — concepts nouveaux par semaine mois par mois, sources, budget, et **le calcul du seuil de bascule** externalisation / internalisation.
3. **Le modèle de trésorerie sur dix-huit mois** — point bas daté, capital nécessaire, **taux de croissance maximal autofinançable calculé**.
4. **L'organigramme et l'ordre des recrutements** — chaque poste daté, adossé à un goulot mesuré, CA HT annuel par ETP avant et après.
5. **Les systèmes** — définitions écrites, tableau de bord à trois niveaux instancié avec tes seuils, rituel hebdomadaire figé.
6. **Le calendrier de montée du budget** — règle d'augmentation, ses trois conditions, plafond de CAC marginal calculé.

Ce n'est pas « un plan de croissance ». C'est **un plan qui refuse de monter le budget** dans trois cas précis, écrits d'avance.

---

## 3. Ce dont tu disposes

| Ressource | Usage |
|---|---|
| [`mentorat/jalons.md`](../mentorat/jalons.md) | **La porte P2 → P3**, dix conditions. Point de départ obligatoire |
| [canoniques § 6](../donnees/chiffres-canoniques.md) | Concepts testés/semaine et gagnants en rotation à P2, P3, P5 : la seule calibration disponible de la machine créative |
| [canoniques § 4](../donnees/chiffres-canoniques.md) et [§ 2.5](../donnees/chiffres-canoniques.md) | BFR et croissance autofinançable ; frais fixes en % du CA HT et CA HT par ETP. Tes deux formules en sortent |
| `simulateur_tresorerie.py` | **L'outil central.** Point bas, mois de rupture, capital à lever, sensibilité |
| `plan_objectif.py` · `cohortes.py` | Volumes (concepts, tickets, ETP, logistique) ; LTV à 12 mois mesurée, dont sort ton plafond de CAC marginal |
| [`tableau-de-bord.md`](../mentorat/tableau-de-bord.md) · [`revue-hebdomadaire.md`](../mentorat/revue-hebdomadaire.md) | Définitions, trois niveaux, format de rituel. **Tu les instancies, tu ne les réinventes pas** |
| Tes livrables [S06](S06-premier-lot-de-creas.md), [S09](S09-lire-les-premiers-chiffres.md), [S10](S10-installer-la-retention.md) | Registre créatif, tableau de seuils, cohortes réelles |

---

## 4. La méthode, pas à pas

### 4.1 Vérifier la porte, et accepter d'être arrêté

La [porte P2 → P3](../mentorat/jalons.md) est « la plus meurtrière du parcours ». Dix conditions, deux règles d'usage : **toutes**, pas la majorité ; **mesurées**, pas estimées. Recopie le tableau avec trois colonnes — valeur mesurée, fenêtre de mesure, verdict. Pas de « presque ». Puis trie tes « non » en deux tas :

| Type | Conditions | Ce qu'on en fait |
|---|---|---|
| **Structurel** | 1, 5, 6, 7, 8 — MER, réachat, LTV/CAC, payback | **Blocantes maintenant.** Monter le budget multiplie une structure qui ne rembourse pas. Tu ne montes pas d'un euro |
| **Datable** | 2, 3, 4, 9, 10 — rythme créatif, gagnants, âge, trésorerie, responsable créa | **Exigibles à une date calculée.** Tu écris le mois où chacune devient contraignante et tu remontes le calendrier |

**La date d'exigibilité se calcule.** Le nombre de concepts à tester par semaine est une fonction du budget hebdomadaire. Les [canoniques § 6](../donnees/chiffres-canoniques.md) donnent deux points : **14 concepts pour 24 147 € HT/semaine** (P2), **38 pour 100 615 € HT** (P3). Interpole :

```
concepts nouveaux / semaine = 14 + (budget hebdo HT − 24 147) × 0,000 314
soit : chaque tranche de 3 186 € HT de budget hebdomadaire supplémentaire
       exige un concept nouveau de plus par semaine.
```

Le mois où ce rythme dépasse ce que tu produis aujourd'hui est ta date limite de recrutement.

> **À retenir :** on ne prépare pas une porte le jour où on l'atteint, on la rétro-planifie. Une condition tenue « huit semaines consécutives » se commence dix semaines avant la date où on en a besoin.

### 4.2 Dimensionner la machine créative, et calculer le seuil de bascule

```
concepts testés / semaine × taux de réussite      → gagnants nouveaux / semaine
                          × durée de vie          → gagnants distincts en rotation
```

Calibration sur les [canoniques § 6](../donnees/chiffres-canoniques.md) : à P2, 14 concepts donnent 1,7 gagnant/semaine (**12,1 %**) et 9 en rotation (**5,3 semaines** de vie) ; à P3, 38 → 4,2 (11,1 %) → 21 (5,0 sem.) ; à P5, 57 → 5,2 (9,1 %) → 23 (4,4 sem.).

**Lis la dérive.** Le taux de réussite tombe de 12,1 % à 9,1 % et la durée de vie de 5,3 à 4,4 semaines : plus le budget est gros, plus vite chaque gagnant est vu par tout le monde, et plus les angles faciles sont consommés. **La machine créative ne devient pas plus efficace en grandissant, elle devient plus grosse.** Dans la fourchette de cette séance, retiens **12,0 %** et **5,2 semaines**.

**Le seuil de bascule.** Externaliser un concept prêt à diffuser — créateur, montage, déclinaisons — coûte de l'ordre de **180 € HT**. Un créa-monteur interne coûte **4 500 € HT/mois** chargé, produit **10 concepts/semaine** (43 par mois), et consomme **32 € HT de rushes par concept**.

```
180 n = 4 500 + 32 n   →   148 n = 4 500   →   n = 30,4 concepts / mois
```

**Le seuil est à 30 concepts par mois, soit 7 par semaine.** En dessous tu externalises et tu as raison ; au-dessus, chaque concept externalisé coûte 148 € de trop. C'est un calcul, pas une préférence, et il se refait chaque trimestre avec tes coûts.

Deux garde-fous que le calcul ne donne pas : un créa interne plafonne à ~43 concepts/mois, et **jamais plus de 70 % des concepts ne viennent d'une seule source**. Un cerveau unique produit des concepts corrélés ; quand la corrélation monte, le taux de réussite s'effondre — invisible dans le coût unitaire, visible trois mois plus tard dans le MER.

### 4.3 Modéliser la trésorerie, et calculer ce que tu peux financer

```
python3 ecommerce/outils/simulateur_tresorerie.py \
    --ca 30000 --croissance 21 --horizon 18 --marge 58,8 --mer 2,2 \
    --fixes 6000 --croissance-fixes 12 --jours-stock 80 --dpo 30 --tresorerie 180000
```

Trois réglages décident du résultat et deux ne coûtent rien à changer : **jours de stock**, **délai fournisseur**, **acompte**. Lis la section « sensibilité » avant tout le reste. Puis calcule à la main le nombre que tu dois pouvoir poser n'importe où :

```
Taux de croissance maximal autofinançable  =  EBITDA mensuel  ÷  BFR
```

Vérifie-la sur les [canoniques § 4](../donnees/chiffres-canoniques.md), les cinq paliers, sans exception :

| Palier | EBITDA mensuel | BFR | EBITDA ÷ BFR | Croissance autofinançable publiée |
|---|---:|---:|---:|---:|
| P1 | −9 403 € | 21 603 € | **−43,5 %** | négative |
| P2 | −19 838 € | 104 462 € | **−19,0 %** | négative |
| P3 | 51 033 € | 481 053 € | **10,61 %** | 124 886 € sur 1 177 200 € = **10,61 %** |
| P4 | 198 572 € | 1 392 510 € | **14,26 %** | 418 046 € sur 2 931 600 € = **14,26 %** |
| P5 | 364 752 € | 2 264 655 € | **16,11 %** | 697 917 € sur 4 333 196 € = **16,11 %** |

La formule reproduit exactement le tableau canonique. **Ton EBITDA finance ton BFR, et rien d'autre.** S'il est négatif — c'est le cas à P1 et P2, donc c'est ton cas — ton taux maximal est **négatif** : même à chiffre d'affaires gelé, tu perds du cash. « À quelle vitesse puis-je croître sans lever ? » n'a alors qu'une réponse honnête : **aucune**.

Reste combien, et pour quand. Deux pièges. **Le point bas n'est jamais dans un horizon à douze mois** : on consomme du cash tant que `EBITDA < (jours de BFR ÷ 30,4) × croissance mensuelle du CA TTC`. Projette **dix-huit mois** ; si ton point bas tombe au dernier mois projeté, ton horizon est trop court et ton chiffre est faux. **Un tour de table prend trois à cinq mois** : la date où tu dois commencer à lever, c'est **le point bas moins cinq mois moins six mois de couverture**.

### 4.4 L'organigramme, et l'ordre des recrutements

**Règle 1 — le plafond de structure.** Les frais fixes ne dépassent jamais le taux du palier vers lequel tu vas, mesuré sur le CA HT que tu auras dans trois mois : **21,2 % à P1, 14,6 % à P2, 10,7 % à P3** ([canoniques § 2.5](../donnees/chiffres-canoniques.md)), interpolé entre les deux paliers qui t'encadrent. Un recrutement qui franchit ce plafond n'est pas autorisé, quelle que soit l'urgence ressentie.

**Règle 2 — l'ordre suit le goulot mesuré, pas le stress ressenti.**

| Fonction | La mesure qui déclenche |
|---|---|
| **Créa** | Concepts produits/semaine < concepts exigés par le budget (§ 4.1) |
| **Média** | Unités d'optimisation finançables — budget hebdo ÷ (50 × CPA) — supérieures à 8, ou plus de 2 marchés |
| **Opérations / SAV** | Tickets/mois ÷ (50 par jour et par agent × 21,7 j) > 0,8 ; compter 0,32 ticket par commande |
| **Rétention** | Part du CA en réachat sous la cible du palier avec les 7 flux de [S10](S10-installer-la-retention.md) en service |
| **Data** | Plus de 3 h/semaine, chronométrées, à fabriquer des chiffres à la main |

Le premier poste est presque toujours la créa : c'est la seule fonction dont le sous-dimensionnement dégrade **toutes** les autres avec six mois de retard — exactement ce que dit la note sous la condition 3 de la porte.

### 4.5 Installer les systèmes avant d'en avoir besoin

Trois objets déjà écrits dans le dépôt ; ton travail est de les **instancier**. **Les définitions** : recopie le § 1 de [`tableau-de-bord.md`](../mentorat/tableau-de-bord.md) et complète la colonne « source » — de quel système sort le nombre, et qui le produit. Une définition sans source est une opinion, et c'est la condition 5 de la [porte P3 → P4](../mentorat/jalons.md). **Le tableau de bord à trois niveaux** : quotidien, cinq chiffres, cinq minutes, **aucune décision autorisée** ; hebdomadaire, les trois blocs avec **tes** seuils ; mensuel, compte de résultat, cohortes, point bas à six mois, CA HT par ETP. **Le rituel** : 45 minutes, ordre du jour figé, une décision, compte rendu écrit ([`revue-hebdomadaire.md`](../mentorat/revue-hebdomadaire.md)).

**Le seul niveau où l'on décide du budget et de la créa est l'hebdomadaire.** Le quotidien sert à détecter une panne. Décider au quotidien, ce n'est pas piloter fin : c'est réexplorer son compte tous les deux jours, et [S08 § 8](S08-le-lancement.md) chiffre ce que ça coûte.

### 4.6 La rampe : règle d'augmentation et CAC marginal

Le premier de chaque mois le budget monte de **20 %**, et uniquement si les **trois** conditions du mois précédent sont vertes. Une au rouge : budget gelé un mois. Deux gels consécutifs : budget **−15 %** et réparation complète.

| # | Condition | Seuil |
|---|---|---|
| 1 | **Créa** | Concepts nouveaux/semaine ≥ seuil du mois sur 4 semaines · gagnants distincts en rotation ≥ 5 · âge moyen ≤ 8 semaines |
| 2 | **Marge** | CAC marginal des 4 dernières semaines ≤ plafond · MER blended 4 semaines ≥ MER seuil CM3 |
| 3 | **Cash** | Trésorerie ≥ 6 × (perte mensuelle projetée + ΔBFR projeté du mois suivant) |

**Pourquoi 20 % et pas 50 %**, et aucune des trois raisons n'est de la prudence de principe. +20 %/mois exige +0,3 concept nouveau par semaine et par tranche de 3 186 € : c'est produisible. Un modèle d'enchère dont le budget bouge de plus de 20 à 30 % réexplore, et pendant qu'il réexplore tu paies plein tarif de l'apprentissage. Enfin, +20 % de budget mensuel c'est +20 % de BFR mensuel.

**Le CAC marginal est le seul chiffre qui compte quand on monte.** Le nCAC moyen dit ce qu'ont coûté tous tes clients ; le marginal dit ce que coûtent **les suivants** — les seuls que ta décision d'augmenter va acheter.

```
CAC marginal = (dépense₂ − dépense₁) ÷ (nouveaux clients₂ − nouveaux clients₁)
élasticité a = ln(clients₂ ÷ clients₁) ÷ ln(dépense₂ ÷ dépense₁)   →   CAC marginal ≈ nCAC ÷ a
```

Mesure sur deux périodes de quatre semaines comparables, jamais sur deux semaines. `a = 1` : réponse linéaire, tu es loin de la saturation. `a = 0,90` : le marginal vaut 1,11 fois la moyenne, c'est sain. `a = 0,75` : il vaut 1,33 fois la moyenne, et chaque hausse coûte un tiers de plus que ce qu'affiche ton tableau de bord. **Sous 0,75, tu n'as plus un problème de budget mais de créa ou d'offre.** Le plafond se calcule depuis la règle canonique LTV/CAC 12 mois ≥ 2,00 ([canoniques § 3](../donnees/chiffres-canoniques.md)) : `plafond = LTV 12 mois en contribution ÷ 2,00`. Au-dessus, le budget ne monte pas — le franchir signifie que les clients achetés en plus ne rembourseront jamais ce qu'ils ont coûté.

---

## 5. Ton livrable

**A — Verdict de porte P2 → P3.** Les dix conditions de [`jalons.md`](../mentorat/jalons.md), une ligne chacune, sept colonnes : condition · seuil · **ma valeur mesurée** · **fenêtre de mesure** · verdict oui/non/non mesuré · type structurel ou datable · **mois d'exigibilité**. Puis la décision en une phrase, signée et datée.

**B — Machine créative.** Par mois : budget pub HT · budget hebdo · concepts exigés/semaine · planifiés · gagnants attendus en rotation · part interne / externe · coût de production HT. Puis : seuil de bascule ……… concepts/mois · décision ……… · part maximale d'une source ……… %.

**C — Trésorerie, M1 à M18.** Par mois : CA TTC · CA HT · marge brute · pub HT · CM3 · fixes · EBITDA · BFR · Δ BFR · flux net · trésorerie. Puis : point bas ……… € au mois ……… · `g_max = EBITDA ÷ BFR` = ……… %/mois · capital à lever ……… € · **date d'ouverture du tour ………**

**D — Organisation.** Par poste : mois d'entrée · coût HT chargé · **goulot mesuré qui le déclenche** · ETP après · CA HT annuel par ETP après · fixes en % du CA HT à M+3 · plafond du palier.

**E — Systèmes.** Définitions : ……… indicateurs, colonne source remplie oui/non. Tableau de bord : seuils N1 ……… / N2 ……… / N3 ……… . Rituel : jour, heure, durée, participants, format du compte rendu.

**F — Rampe.** Par mois : budget HT · nCAC projeté · CAC marginal projeté · plafond · marge au plafond. Puis **les trois cas de refus écrits au futur** : *si ……… alors je ………* (×3).

---

## 6. La grille d'évaluation

Barème sur 100, **seuil de validation 80** — le plus élevé de l'atelier : une erreur ici ne coûte plus des points, elle coûte une entreprise.

| # | Critère | Pts | Ce qui vaut les points | Ce qui les fait perdre |
|---|---|---:|---|---|
| 1 | **Verdict de porte** | 14 | Dix lignes, valeur mesurée **et** fenêtre, tri structurel/datable, mois d'exigibilité calculé | « Non mesuré » compté comme oui : **éliminatoire** · fenêtre absente : −2/ligne |
| 2 | **Production créative** | 18 | Concepts/semaine dérivés du budget mois par mois, seuil de bascule calculé, part maximale d'une source | « On produira plus de créas » sans nombre : **éliminatoire** · seuil non calculé : −8 |
| 3 | **Trésorerie** | 20 | 18 mois, point bas daté, **g_max = EBITDA ÷ BFR calculé**, capital et date d'ouverture du tour | Point bas au dernier mois projeté : −10 · g_max absent : **éliminatoire** |
| 4 | **Organigramme** | 12 | Poste daté, adossé à un goulot **mesuré**, CA HT/ETP avant et après, plafond de fixes vérifié | « On est débordés » : −4 par poste · plafond non vérifié : −6 |
| 5 | **Systèmes** | 12 | Définitions avec source, trois niveaux instanciés avec tes seuils, rituel daté | Budget décidé au niveau quotidien : −6 · définitions sans source : −5 |
| 6 | **Rampe et CAC marginal** | 18 | Règle des trois conditions, plafond **calculé depuis la LTV**, élasticité mesurée, trois refus au futur | Plafond au doigt mouillé : −8 · aucun cas de refus : **éliminatoire** |
| 7 | Cohérence d'ensemble | 6 | Recrutement créa avant le mois d'exigibilité, tour ouvert avant le point bas moins cinq mois | Trois plans juxtaposés sans dates communes : −6 |

**Quatre fautes éliminatoires.** Une condition de porte **non mesurée comptée comme remplie** — c'est le mode d'échec que la porte existe pour empêcher. Un **plan créatif sans nombre de concepts par semaine** : ce n'est pas un plan, c'est une intention. Un **plan de budget sans g_max** : tu proposes de dépenser un argent dont tu n'as pas montré qu'il existait. **Aucun cas de refus écrit** : une rampe qui ne peut pas s'arrêter n'est pas un plan, c'est une trajectoire balistique.

---

## 7. Le corrigé exemplaire

> **Cas composite. Marque fictive.** Les chiffres sont un modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes d'aucune entreprise réelle.

**MIRVA** — compléments alimentaires du sommeil et de la récupération, cure mensuelle, DTC, France et Belgique. Mois 22 d'existence.

### 7.1 État au mois 0

CA TTC 30 000 €/mois, CA HT 25 000 €. 600 commandes, **AOV mixte 50,00 € TTC** (1ʳᵉ commande 48,00 €, réachat 63,38 €). Part des commandes en réachat 13,0 %, part du CA en réachat 16,5 %. **Marge brute CM2 58,8 %** du CA HT = 14 700 €. Publicité 13 636 € HT (**MER 2,20**). CM3 1 064 €. Frais fixes 6 000 € HT (24,0 % du CA HT). **EBITDA −4 936 €.** Trésorerie 180 000 €. BFR à 14 jours de CA TTC : 13 816 €. 522 nouveaux clients, **nCAC 26,12 €**, contribution de première commande 23,52 € — soit **−2,60 € à la première commande**. LTV 12 mois en contribution 57,69 €, **LTV/CAC 2,21**, payback 1,9 mois, sur cohortes réelles. 1,2 ETP. **8 concepts nouveaux testés par semaine, 5 gagnants en rotation, âge moyen 9,4 semaines.**

### 7.2 Verdict de porte P2 → P3

| # | Condition | Seuil | MIRVA | Fenêtre | Verdict | Type | Exigible |
|---|---|---|---|---|---|---|---|
| 1 | MER blended | ≥ 2,20 | **2,21** | 8 sem. | oui | structurel | M0 |
| 2 | Gagnants en rotation | ≥ 5 | **5** | à date | oui, limite | datable | M0 |
| 3 | Concepts nouveaux/sem. | ≥ 10 | **8** | 8 sem. | **non** | datable | **M7** |
| 4 | Âge moyen des gagnants | ≤ 8 sem. | **9,4** | à date | **non** | datable | **M4** |
| 5 | 1ʳᵉ → 2ᵉ à 90 jours | ≥ 18 % | **19,4 %** | 3 cohortes | oui | structurel | M0 |
| 6 | Part du CA en réachat | ≥ 15 % | **16,5 %** | 3 mois | oui | structurel | M0 |
| 7 | LTV/CAC 12 mois | ≥ 2,00 | **2,21** | cohortes M1–M10 | oui | structurel | M0 |
| 8 | Payback | ≤ 4 mois | **1,9** | cohortes | oui | structurel | M0 |
| 9 | Trésorerie ≥ BFR cible + 3 mois de fixes | 137 741 + 72 000 = **209 741 €** | **180 000 €** | à date | **non** | datable | **M7** |
| 10 | Responsable créa | existe | **non** | — | **non** | datable | **M3** |

**Les cinq conditions structurelles sont vertes, aucune n'a été estimée.** Quatre datables sont rouges et se ramènent à deux chantiers : **une personne dont la créa est le métier** (résout 3, 4 et 10) et **de l'argent** (résout 9).

**Le calcul du mois d'exigibilité de la condition 3**, pour montrer le geste : le seuil de 10 concepts/semaine est atteint quand le budget hebdomadaire vaut `24 147 − (14 − 10) ÷ 0,000 314 = 11 404 € HT`, soit **49 690 € HT par mois**. La rampe y arrive au mois 7 (`13 636 × 1,20⁷ = 48 862 €`, puis 58 634 € au mois 8). Le créa doit donc être **opérationnel** au mois 6 — donc signé au mois 3, avec deux mois de recherche et un mois de montée en compétence.

**Décision, écrite et datée.** *« La rampe démarre le 1er du mois prochain à +20 % de budget par mois. Le créa entre le 1er du mois 3. Le tour ouvre cette semaine. Si au 1er d'un mois une condition datable arrivée à échéance n'est pas remplie, le budget ne monte pas ce mois-là — sans discussion, sans exception, y compris si le mois a été bon. »*

### 7.3 Le plan de production créative

| Mois | Budget pub HT | Budget hebdo HT | Exigés/sem. | Planifiés | Gagnants en rotation | Interne / externe | Production HT/mois |
|---|---:|---:|---:|---:|---:|---|---:|
| M1–M2 | 16 364 → 19 636 € | 3 768 → 4 522 € | 7,6 → 7,8 | **9** | 5,6 | 0 % / 100 % | 1 620 € |
| M3–M5 | 23 564 → 33 932 € | 5 426 → 7 813 € | 8,1 → 8,9 | **11** | 6,9 | 63 % / 37 % | 5 690 € |
| M6–M8 | 40 718 → 58 634 € | 9 375 → 13 500 € | 9,4 → 10,7 | **13** | 8,1 | 77 % / 23 % | 6 424 € |
| M9–M12 | 70 361 → 121 583 € | 16 200 → 27 995 € | 11,5 → 15,2 | **18** | 11,2 | 55 % / 45 % | 9 777 € |

**Seuil de bascule.** MIRVA teste 35 concepts par mois contre un seuil calculé à 30,4 : `35 × 180 = 6 300 €` externalisé contre `4 500 + 32 × 35 = 5 620 €` interne, **680 € d'écart**. Ce n'est pas ce qui justifie l'embauche — c'est la condition 10 de la porte. Mais au mois 12, à 78 concepts par mois, l'écart passe à `14 040 €` contre `4 500 + 2 496 + 3 888 = 10 884 €`, soit **3 156 € par mois**, et la décision serait la même sans la porte.

**Le mélange du dernier trimestre.** 78 concepts par mois, dont 43 par le créa interne : les 35 restants sont externalisés **volontairement**, parce que 43 sur 78 font 55 % d'une source unique, sous le plafond de 70 %. Un second interne coûterait 9 000 € et porterait la source unique à 100 %.

**Coût complet de la machine créative au mois 12 :** production 9 777 € + média de test à 15 % du budget ([canoniques § 6](../donnees/chiffres-canoniques.md)) 18 237 € = **28 014 € HT par mois, soit 23,0 % du budget publicitaire.** C'est le vrai prix de la créa, et il n'apparaît dans aucune interface publicitaire.

### 7.4 La trésorerie sur dix-huit mois

*Hypothèses déclarées : budget publicitaire +20,0 %/mois · MER 2,20 → 2,46 en linéaire sur 12 mois, plafonné ensuite · marge brute CM2 58,8 % → 60,0 % (COGS aux paliers de volume, contrat 3PL) · AOV mixte 50,00 € → 56,00 € TTC · part des commandes en réachat 13 % → 25 % · BFR = 14 jours de CA TTC · trésorerie de départ 450 000 € = 180 000 € existants + 270 000 € levés. Les colonnes CA HT et marge brute se déduisent : `CA HT = CA TTC ÷ 1,2`, `marge brute = CA HT × taux du mois`.*

**Le chiffre d'affaires n'est pas un objectif, c'est un résultat.** MIRVA pilote son budget : `CA = budget × MER`. À +20 % de budget et un MER de 2,20 à 2,46, le CA croît de **21,1 % par mois**, et `30 000 × 1,211¹² = 299 095 €` — la cible est atteinte sans avoir été visée. **Et l'amélioration du MER n'est pas un vœu, c'est le panier** : `MER = AOV ÷ CPA`, donc à CPA constant, passer l'AOV de 50,00 € à 56,00 € TTC (+12,0 %) fait passer le MER de 2,20 à 2,46 (+11,8 %). Ces 12 % sont le chantier de [S04](S04-offre-prix-et-panier.md) et [S10](S10-installer-la-retention.md) : cure de 3 mois mise en avant, franco relevé, part de réachat de 13 % à 25 %.

| Mois | CA TTC | Pub HT | MER | CM3 | Fixes | EBITDA | BFR | Δ BFR | Flux | Trésorerie |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| M1 | 36 355 € | 16 364 € | 2,22 | 1 480 € | 6 000 € | −4 520 € | 16 742 € | 2 926 € | −7 446 € | 442 554 € |
| M2 | 44 051 € | 19 636 € | 2,24 | 2 022 € | 6 000 € | −3 978 € | 20 287 € | 3 544 € | −7 522 € | 435 032 € |
| M3 | 53 372 € | 23 564 € | 2,27 | 2 722 € | 10 800 € | −8 078 € | 24 579 € | 4 292 € | −12 371 € | 422 661 € |
| M4 | 64 659 € | 28 276 € | 2,29 | 3 622 € | 10 800 € | −7 178 € | 29 777 € | 5 198 € | −12 376 € | 410 285 € |
| M5 | 78 326 € | 33 932 € | 2,31 | 4 774 € | 10 800 € | −6 026 € | 36 071 € | 6 294 € | −12 320 € | 397 965 € |
| M6 | 94 873 € | 40 718 € | 2,33 | 6 244 € | 16 200 € | −9 956 € | 43 691 € | 7 620 € | −17 576 € | 380 389 € |
| M7 | 114 906 € | 48 862 € | 2,35 | 8 113 € | 16 200 € | −8 087 € | 52 917 € | 9 226 € | −17 313 € | 363 076 € |
| M8 | 139 158 € | 58 634 € | 2,37 | 10 481 € | 16 200 € | −5 719 € | 64 086 € | 11 169 € | −16 887 € | 346 188 € |
| M9 | 168 514 € | 70 361 € | 2,40 | 13 475 € | 21 600 € | −8 125 € | 77 605 € | 13 519 € | −21 644 € | 324 544 € |
| M10 | 204 046 € | 84 433 € | 2,42 | 17 250 € | 21 600 € | −4 350 € | 93 968 € | 16 363 € | −20 713 € | 303 831 € |
| M11 | 247 050 € | 101 319 € | 2,44 | 22 000 € | 22 800 € | −800 € | 113 773 € | 19 805 € | −20 605 € | 283 226 € |
| **M12** | **299 095 €** | **121 583 €** | **2,46** | **27 964 €** | **24 000 €** | **+3 964 €** | **137 741 €** | **23 968 €** | **−20 004 €** | **263 222 €** |
| M15 | 516 836 € | 210 096 € | 2,46 | 48 322 € | 31 000 € | +17 322 € | 238 016 € | 39 669 € | −22 347 € | 190 094 € |
| M18 | 893 092 € | 363 045 € | 2,46 | 83 500 € | 46 000 € | +37 500 € | 411 292 € | 68 549 € | −31 048 € | **116 889 €** |

**L'EBITDA devient positif au mois 12, à 3 964 € — soit 1,6 % du CA HT.** Après douze mois d'exécution parfaite et un chiffre d'affaires multiplié par dix, MIRVA gagne l'équivalent d'un salaire. Ce n'est pas un échec : le modèle de référence n'atteint +5,2 % d'EBITDA qu'au palier P3, à 1 177 200 € TTC par mois. **300 000 € par mois n'est pas la rentabilité, c'est l'entrée de la vallée — pas la sortie.**

**Le flux net reste négatif jusqu'au mois 18 inclus.** `g_max = EBITDA ÷ BFR` vaut `−4 936 ÷ 13 816 = −35,7 %` au mois 0 — négatif, donc aucun rythme n'est autofinançable, pas même zéro ; `3 964 ÷ 137 741 = +2,9 %` au mois 12 contre 21,1 % de croissance réelle ; `37 500 ÷ 411 292 = +9,1 %` au mois 18. **Le plan n'est jamais autofinancé sur son horizon. Il est financé — et c'est une phrase différente.**

**Point bas : 116 889 € au mois 18**, dernier mois projeté, donc le vrai point bas est plus loin. Cumul consommé : `186 778 €` sur 12 mois, `333 111 €` sur 18. **Sans le tour**, avec les seuls 180 000 €, la trésorerie tombe à `−6 778 €` au mois 12 et MIRVA meurt au mois 11. La rampe n'est pas conditionnée à un souhait de levée, elle est conditionnée à un virement.

```
Trésorerie sous 6 mois de couverture (règle 3 de la rampe)  :  mois 7
Délai moyen d'un tour de table                              :  4 mois
Marge de sécurité                                           :  1 mois
Date d'ouverture du tour  =  M7 − 5  =  MOIS 2
```

Et comme un tour se prépare avec des données propres — cohortes, MER par cohorte, registre créatif, modèle à 18 mois — il commence **cette semaine** : c'est le document de cette séance.

### 7.5 L'organigramme et l'ordre des recrutements

| Poste | Entrée | Coût HT chargé | Goulot mesuré | ETP après | CA HT annuel/ETP à M+3 | Fixes / CA HT à M+3 | Plafond |
|---|---|---:|---|---:|---:|---:|---:|
| **Créa-monteur** | M3 | 4 500 € | 8 concepts/sem. produits contre 10 exigés au M7 ; condition 10 de la porte | 2,2 | 431 242 € | 13,7 % | 19,2 % |
| **Acquisition / média** | M6 | 5 000 € | 4 unités d'optimisation finançables au M6, 12 au M9 ; ouverture Belgique | 3,2 | 526 605 € | 11,5 % | 17,3 % |
| **Opérations / SAV** | M9 | 5 000 € | 3 092 commandes × 0,32 = 989 tickets/mois ÷ (50 × 21,7) = **0,91 ETP** | 4,2 | 712 130 € | 8,7 % | 14,3 % |

Rétention et données ne sont pas recrutées : la première reste portée par le fondateur avec les sept flux en service depuis [S10](S10-installer-la-retention.md), la seconde est mesurée à 2 h par semaine, sous le seuil de 3 h.

**Trois recrutements en douze mois pour multiplier le chiffre d'affaires par dix.** À la fin, 4,2 ETP produisent **712 130 € de CA HT annuel par ETP** — entre P2 (575 500 €) et P3 (981 000 €) des [canoniques § 2.5](../donnees/chiffres-canoniques.md) — avec des frais fixes à 9,6 % du CA HT, sous le 10,7 % de P3. Pas de responsable de marque, pas d'assistant, pas de directeur des opérations : chacun se justifie par un ressenti, aucun par un goulot mesuré. **Si tu ne peux pas écrire le nombre qui déclenche le poste, le poste n'existe pas.**

### 7.6 Les systèmes

Les 14 définitions de [`tableau-de-bord.md`](../mentorat/tableau-de-bord.md) § 1 sont reprises avec leur source et leur producteur. Deux sont durcies pour MIRVA : un **concept nouveau** exige un changement d'angle, de mécanisme **ou** de format — le remontage d'un même script reste une variation ; un **gagnant** est un concept ayant dépassé 43 conversions et battu le CPA cible sur cette dépense ([S08 § 4.1](S08-le-lancement.md)).

| Niveau | Rythme | Contenu | Seuils MIRVA | Décisions autorisées |
|---|---|---|---|---|
| **N1** | Quotidien, 5 min | CA TTC, dépense, MER du jour, commandes, jours de stock | Stock < 21 j · MER jour < 1,60 · dépense hors bornes ±25 % | **Aucune.** Détection de panne |
| **N2** | Hebdo, 45 min | Économie, machine créative, rétention et cash | MER 4 sem. < 2,02 · nCAC +20 % à exécution constante · concepts < seuil du mois · âge moyen > 8 sem. · CAC marginal > 33,65 € · trésorerie < 26 semaines | Budget, créa, offre |
| **N3** | Mensuel, 2 h | Compte de résultat, cohortes, point bas à 6 mois, CA HT/ETP | Cohorte récente sous les anciennes au même âge · fixes > plafond du palier · point bas < 6 mois de charges | Recrutement, prix, marchés, financement |

*MER seuil CM3 de MIRVA : `1,2 ÷ 0,588 = 2,04` au mois 0, `1,2 ÷ 0,600 = 2,00` au mois 12. Sous cette ligne, chaque euro de CA supplémentaire coûte de l'argent.*

**Rituel.** Lundi 9 h 00, 45 minutes chronométrées : chiffres (10 min), alertes (10 min), goulot (10 min), **une** décision (10 min), clôture (5 min). Compte rendu de dix lignes avant midi. Interdits : ouvrir une interface publicitaire pendant la revue, débattre d'un chiffre non produit par le tableau de bord, prendre une seconde décision.

### 7.7 La rampe et le CAC marginal

Au mois 12 : contribution de première commande `54,00 ÷ 1,2 × 60,0 % = 27,00 €`, contribution par réachat `62,00 ÷ 1,2 × 60,0 % = 31,00 €`, commandes cumulées par client à 12 mois **2,30** (cohortes réelles).

```
LTV 12 mois = 27,00 + 1,30 × 31,00 = 67,30 €
Plafond du CAC marginal = 67,30 ÷ 2,00 = 33,65 € HT
```

| Mois | Budget HT | Nouveaux clients | nCAC | **CAC marginal** | % du plafond |
|---|---:|---:|---:|---:|---:|
| M1 | 16 364 € | 619 | 26,43 € | 28,09 € | 83,5 % |
| M3 | 23 564 € | 871 | 27,07 € | 28,80 € | 85,6 % |
| M6 | 40 718 € | 1 450 | 28,08 € | 29,95 € | 89,0 % |
| M9 | 70 361 € | 2 412 | 29,17 € | 31,19 € | 92,7 % |
| M12 | 121 583 € | 4 006 | 30,35 € | **32,54 €** | **96,7 %** |

**Élasticité mesurée sur douze mois :** `ln(4 006 ÷ 619) ÷ ln(121 583 ÷ 16 364) = 1,867 ÷ 2,005 = 0,931` ; vérification `30,35 ÷ 0,931 = 32,60 €` contre 32,54 € calculé directement — les deux méthodes concordent. Au mois 12, MIRVA consomme 96,7 % de sa marge au plafond : **il n'y a pas de treizième mois à +20 % sans avoir d'abord bougé la LTV, donc le plafond, ou l'élasticité, donc la créa et l'offre.** C'est ce qu'un plan doit produire — non pas une trajectoire infinie, mais la date à laquelle elle s'arrête.

**Les trois cas de refus, écrits au futur.**

1. *Si au 1er du mois les concepts nouveaux des quatre dernières semaines sont sous le seuil du mois, le budget reste au niveau du mois précédent et 100 % du temps créa passe en production jusqu'au rattrapage.*
2. *Si le CAC marginal des quatre dernières semaines dépasse 33,65 € HT, le budget est gelé et je lance un test d'offre — pas un test de ciblage — parce que le problème est dans ce que j'achète, pas dans qui je le montre.*
3. *Si la trésorerie passe sous six mois de perte projetée augmentée du ΔBFR du mois suivant, le budget baisse de 15 % le jour même et le tour passe en priorité absolue devant toute action commerciale.*

---

## 8. Les conséquences chiffrées de ton choix

Deux marques : même produit, même page, même équipe, **même trésorerie de 450 000 €**, même mois 0 à 30 000 € TTC. **MIRVA-A** monte son budget de **20 % par mois**, avec la créa dimensionnée mois par mois et la règle des trois conditions. **MIRVA-B** monte de **50 % par mois**, garde ses 8 concepts par semaine, et regarde son chiffre d'affaires plutôt que son CM3.

*Hypothèse de saturation créative, déclarée. Le budget hebdomadaire qu'une bibliothèque peut porter se déduit de la relation du § 4.1 inversée : à 8 concepts/semaine, `24 147 − 6 × 3 186 = 5 031 € HT` par semaine, soit 21 852 € par mois. Au-delà, `MER = 2,20 × (capacité ÷ dépense)^0,12`. B garde sa marge brute à 58,8 % trois mois puis la laisse tomber à 57,0 % parce qu'il soutient le volume par la remise, et son panier passe de 50,00 € à 47,00 € TTC pour la même raison. B gèle son budget au mois 6, quand le relevé bancaire devient impossible à ignorer.*

| Mois | **A** budget | **A** CA TTC | **A** EBITDA | **A** trésorerie | **B** budget | **B** MER | **B** CA TTC | **B** EBITDA | **B** trésorerie |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| M1 | 16 364 € | 36 355 € | −4 520 € | 442 554 € | 20 455 € | 2,20 | 45 001 € | −4 405 € | 430 792 € |
| M2 | 19 636 € | 44 051 € | −3 978 € | 435 032 € | 30 682 € | 2,11 | 64 739 € | −7 960 € | 403 354 € |
| M3 | 23 564 € | 53 372 € | −8 078 € | 422 661 € | 46 023 € | 2,01 | 92 506 € | −13 695 € | 362 257 € |
| M4 | 28 276 € | 64 659 € | −7 178 € | 410 285 € | 69 034 € | 1,92 | 132 545 € | −25 075 € | 297 670 € |
| M5 | 33 932 € | 78 326 € | −6 026 € | 397 965 € | 103 551 € | 1,83 | 189 498 € | −39 539 € | 201 927 € |
| **M6** | 40 718 € | **94 873 €** | −9 956 € | 380 389 € | 103 551 € | 1,80 | **186 392 €** | −47 015 € | 157 977 € |
| M7 | 48 862 € | 114 906 € | −8 087 € | 363 076 € | 103 551 € | 1,84 | 190 534 € | −51 047 € | 102 843 € |
| M8 | 58 634 € | 139 158 € | −5 719 € | 346 188 € | 103 551 € | 1,88 | 194 676 € | −49 080 € | 49 675 € |
| **M9** | 70 361 € | 168 514 € | −8 125 € | 324 544 € | 103 551 € | 1,92 | 198 818 € | −47 112 € | **−1 525 €** |
| M10 | 84 433 € | **204 046 €** | −4 350 € | 303 831 € | 103 551 € | 1,95 | **201 924 €** | −43 637 € | −48 228 € |
| M11 | 101 319 € | 247 050 € | −800 € | 283 226 € | 103 551 € | 1,98 | 205 031 € | −40 161 € | −91 455 € |
| M12 | 121 583 € | **299 095 €** | **+3 964 €** | **263 222 €** | 103 551 € | 2,00 | **207 102 €** | −37 178 € | **−130 676 €** |

**Au mois 6, B fait 1,96 fois le chiffre d'affaires de A** — 186 392 € contre 94 873 €. À ce moment précis, tous les signaux visibles donnent raison à B : plus de commandes, plus de clients, une équipe plus grande. A a l'air prudent là où B a l'air ambitieux. **Au mois 9, B est en cessation de paiement** — −1 525 € au compte, avec 198 818 € de chiffre d'affaires, le meilleur mois de son histoire. **Au mois 10, A le dépasse** : 204 046 € contre 201 924 €, sans l'avoir visé — A pilotait son budget et ses conditions, pas son chiffre.

### 8.1 D'où vient l'écart

| Sur 12 mois | **A** | **B** | Écart |
|---|---:|---:|---:|
| Dépense publicitaire HT cumulée | 647 681 € | 994 602 € | **+53,6 % pour B** |
| Nouveaux clients acquis | 22 340 | 35 108 | +57,2 % pour B |
| nCAC moyen | 28,99 € | 28,33 € | −2,3 % pour B |
| MER moyen | 2,37 | 1,95 | −17,7 % pour B |
| EBITDA cumulé | **−62 853 €** | **−405 904 €** | **342 951 €** |
| Trésorerie fin M12 | +263 222 € | −130 676 € | **393 898 €** |
| LTV 12 mois en contribution | 67,30 € | 47,55 € | −29,3 % pour B |
| **LTV / CAC à 12 mois** | **2,22** | **1,76** | seuil canonique : 2,00 |

**B a acheté 57 % de clients en plus, à un CAC moyen légèrement inférieur, et il est mort.** Trois raisons, par ordre d'importance.

**Un.** Le MER de B passe sous son seuil CM3 dès le mois 3 : le seuil vaut `1,2 ÷ 0,588 = 2,04`, puis `1,2 ÷ 0,570 = 2,11` quand la remise abîme la marge brute, et B est à 2,01 au mois 3 puis 1,80 au mois 6. **À partir du mois 3, chaque euro de budget supplémentaire détruit de la marge.** Son chiffre d'affaires monte pendant que sa contribution descend : le seul cas de figure où grandir appauvrit à coup sûr.

**Deux.** B a acheté des clients moins bons — panier 47,00 € contre 56,00 €, aucun travail de rétention faute de temps, LTV 12 mois de 47,55 € contre 67,30 €. Son ratio **LTV/CAC de 1,76** est sous le seuil canonique de 2,00, celui qui dit « on ne scale pas, on répare » ([canoniques § 3](../donnees/chiffres-canoniques.md)). B a scalé.

**Trois, le mécanisme qu'on ne voit jamais venir.** B a commandé son stock à l'aveugle sur une projection à +50 % par mois : **trente jours de BFR contre quatorze pour A.** Au mois 5, la seule augmentation de son BFR vaut 56 204 €, plus que sa perte du mois, et `g_max = −39 539 ÷ 187 005 = −21,1 %`. La formule dit qu'il aurait fallu **décroître de 21 % par mois** pour rester à flot. Il montait de 50 %.

### 8.2 Le rattrapage, et pourquoi il n'a pas lieu

B n'est pas mort de sa perte : il est mort de ne plus pouvoir en financer une de plus. Ramener le budget sous la capacité créative coûte deux mois à −79 % de chiffre d'affaires ; reconstruire cinq gagnants distincts frais, trois mois ; sortir de la remise permanente pour remonter la marge brute de 57,0 % à 58,8 %, 11 % des commandes pendant deux mois ; remonter l'AOV de 47,00 € à 56,00 €, quatre mois ([S04](S04-offre-prix-et-panier.md)) ; refinancer 250 000 € après quatre trimestres de pertes, cinq à huit mois à une valorisation divisée par deux à trois.

**Douze à quinze mois pour revenir là où A est arrivé en douze** — et le refinancement n'a pas de solution : on ne lève pas sur une trajectoire dont la courbe de contribution descend depuis neuf mois. B n'a pas seulement perdu de l'argent, il a perdu **la démonstration** qu'il savait en gagner, et c'est ça qu'on présente à un investisseur.

**Le chiffre qui résume la séance.** Les deux fondateurs ont travaillé autant. B a dépensé 346 921 € HT de publicité de plus que A, et finit avec 393 898 € de trésorerie de moins et une entreprise en cessation de paiement. **L'écart, 740 819 €, tient dans une décision prise une fois : monter de 20 % au lieu de 50 %, et écrire les trois conditions qui autorisent chaque hausse.**

> **À retenir :** passer à l'échelle n'est pas un problème de budget, c'est un problème de **cadence** — la vitesse à laquelle ta machine créative, ta trésorerie et ton organisation absorbent du volume. Ces trois cadences ont chacune un délai de réparation de trois à six mois. La seule vitesse soutenable est celle des trois, et la vitesse des trois est toujours celle de la plus lente.

---

## 9. Avant la séance suivante

1. **Calcule ton `g_max = EBITDA ÷ BFR` et garde la feuille.** S'il est négatif — c'est probable — écris à côté : *« ma croissance est financée, pas autofinancée, et elle s'arrête le mois où le financement s'arrête. »* Puis pose la soustraction : point bas moins cinq mois moins six mois de couverture.
2. **Compte tes concepts nouveaux des quatre dernières semaines**, en appliquant strictement la définition — angle **ou** mécanisme **ou** format différent, un remontage n'en est pas un. Compare au seuil que ton budget des trois prochains mois exigera : l'écart est ta date limite de recrutement créa, et elle est plus proche que tu ne le crois.
3. **Écris tes trois cas de refus et affiche-les.** Pas dans un document : sur un mur. Une rampe budgétaire sans mécanisme d'arrêt écrit d'avance ne s'arrêtera jamais au bon moment, parce que le bon moment est toujours un moment où les chiffres du mois ont l'air bons.

---

*Fin de la séance S11. Suite : [S12 — La crise, et la revue générale](S12-la-crise.md), la dernière de l'atelier. On tirera au sort la manière dont ta marque va casser, tu écriras le plan des quatorze premiers jours, puis tu reliras les onze décisions prises depuis [S01](S01-choisir-le-terrain.md) pour voir lesquelles se paient encore.*
