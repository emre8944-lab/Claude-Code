# Diagnostic d'entrée

> 30 minutes. Tu le fais une fois avant de commencer, puis tu le refais tous les
> trimestres. Il ne sert pas à te noter : il sert à déterminer **ce qu'on ignore**,
> ce qui est la décision la plus rentable du cursus.
>
> Si tu n'as pas encore vendu, saute au bloc A et au bloc G, puis va directement
> à la section « Placement N0 ».

---

## Comment le remplir

Pour chaque chiffre, note **(obs)** s'il est observé dans tes données, **(est)**
s'il est estimé. Un diagnostic rempli d'estimations non signalées ne diagnostique
rien. Si tu ne sais pas, écris « je ne sais pas » — c'est une réponse, et souvent
la plus informative.

---

## Bloc A — La structure (le bloc le plus important)

C'est ce qui a été décidé avant ta première vente et qui plafonne tout le reste.
Aucune quantité de travail ne compense un mauvais bloc A.

| # | Question | Ta réponse | Points |
|---|---|---|---|
| A1 | Prix de vente TTC de ton produit principal | | |
| A2 | Coût de revient complet **rendu entrepôt** (produit + emballage + fret + douane + contrôle) | | |
| A3 | **Coefficient = A1 ÷ A2** | | ×8 et + : **5** / ×6 à 8 : **4** / ×5 à 6 : **3** / ×4 à 5 : **2** / ×3 à 4 : **1** / < ×3 : **0** |
| A4 | Au bout de combien de temps un client normal a-t-il épuisé ou usé le produit ? | | ≤ 2 mois : **5** / 3-4 mois : **4** / 5-8 mois : **3** / 9-18 mois : **1** / jamais : **0** |
| A5 | Taux de retour de ta catégorie | | < 5 % : **5** / 5-12 % : **4** / 12-20 % : **2** / 20-30 % : **1** / > 30 % : **0** |
| A6 | Coût de transport moyen d'une commande, en % du prix de vente TTC | | < 8 % : **5** / 8-14 % : **3** / 14-22 % : **1** / > 22 % : **0** |
| A7 | Ton produit est-il réglementé (santé, alimentaire, cosmétique, électrique, enfant) ? | | Barrière forte que tu franchis : **5** / Aucune contrainte : **3** / Contrainte que tu ne maîtrises pas : **0** |
| A8 | Combien de temps faudrait-il à un concurrent pour copier ton produit et le vendre ? | | > 18 mois : **5** / 6-18 mois : **3** / 2-6 mois : **1** / < 2 mois : **0** |

**Score A = ____ / 35**

### Verdict structurel — lis-le avant tout le reste

| Score A | Verdict |
|---|---|
| **28 à 35** | Structure compatible avec P5. Le reste est une question d'exécution. |
| **21 à 27** | P5 atteignable, mais tu paieras chaque point de marge. Travaille A3, A4 et A6 en priorité. |
| **14 à 20** | P5 improbable sans changer un élément structurel. Identifie lequel et traite-le comme le chantier du semestre, pas comme un détail. |
| **< 14** | **P5 est arithmétiquement hors d'atteinte avec ce produit.** Ce n'est pas un jugement sur toi. Lis [C01](../etudes-de-cas/C01-coefficient-insuffisant.md) : c'est exactement ce cas, chiffré. Deux sorties : changer de produit, ou changer d'objectif. Les deux sont respectables. Continuer sans choisir ne l'est pas. |

> **Le test qui tranche, en une ligne.** Si `A3 < 5`, calcule ton MER seuil comme
> l'explique [E01](../modules/E01-arithmetique-de-la-marque.md) § 4. S'il dépasse
> 3,5, tu ne pourras jamais acheter de trafic de façon rentable, quelle que soit
> ta créativité publicitaire. C'est de l'arithmétique, pas une opinion.

---

## Bloc B — Où tu en es

| # | Question | Ta réponse | (obs/est) |
|---|---|---|---|
| B1 | CA TTC des 30 derniers jours | | |
| B2 | Nombre de commandes des 30 derniers jours | | |
| B3 | AOV TTC (B1 ÷ B2) | | |
| B4 | CA TTC des 30 jours précédents | | |
| B5 | Croissance mensuelle (B1 ÷ B4 − 1) | | |
| B6 | Nombre de mois depuis ta première vente | | |
| B7 | Nombre de marchés (pays) actifs | | |

---

## Bloc C — L'économie réelle

C'est ici que la plupart des gens découvrent qu'ils calculaient faux. Prends le
temps. Renvoi : [E01](../modules/E01-arithmetique-de-la-marque.md) § 1.

| # | Question | Ta réponse | (obs/est) |
|---|---|---|---|
| C1 | CA **HT** des 30 derniers jours (= B1 ÷ 1,20 en France) | | |
| C2 | COGS en % du CA HT | | |
| C3 | Logistique complète en % du CA HT (préparation + emballage + transport + retours logistiques) | | |
| C4 | Frais de paiement en % du CA HT | | |
| C5 | Retours, casse et gestes commerciaux en % du CA HT | | |
| C6 | **Remises et codes promo** en % du CA HT (n'oublie pas les codes créateurs) | | |
| C7 | **Taux de marge brute CM2 = 100 % − (C2+C3+C4+C5+C6)** | | |
| C8 | Dépense publicitaire des 30 derniers jours | | |
| C9 | **MER blended = B1 ÷ C8** | | |
| C10 | **Part de la pub en % du CA HT = C8 ÷ C1** | | |
| C11 | **CM3 = C7 − C10** (en points) | | |
| C12 | Frais fixes mensuels (salaires chargés, outils, loyer, honoraires) | | |
| C13 | Frais fixes en % du CA HT | | |
| C14 | **EBITDA en % du CA HT = C11 − C13** | | |

### Les deux calculs qui décident

```
MER seuil (marge de contribution nulle)  =  1,20  ÷  C7
MER seuil (résultat nul)                 =  1,20  ÷  (C7 − C13)
```

| Ton MER (C9) comparé au seuil | Ce que ça veut dire |
|---|---|
| **C9 < seuil CM3** | Chaque euro de CA supplémentaire te fait perdre de l'argent. Tu n'as pas un problème de croissance, tu as un problème de structure. **Arrête de scaler aujourd'hui.** |
| **seuil CM3 ≤ C9 < seuil EBITDA** | Tu finances ta structure avec ton capital. C'est légitime **seulement** si ta courbe de réachat le rembourse (bloc E). Sinon c'est une hémorragie déguisée en croissance. |
| **C9 ≥ seuil EBITDA** | Tu gagnes de l'argent. La question devient : combien de volume peux-tu ajouter avant que le CAC marginal ne te ramène au seuil ? |

> Points de repère du modèle de référence
> ([chiffres canoniques § 2.3](../donnees/chiffres-canoniques.md)) : le MER seuil
> CM3 est de 1,95 à 2,10 selon le palier, le MER seuil EBITDA de 2,33 à 3,33. Si
> ton seuil CM3 dépasse 2,5, retourne au bloc A : ta marge brute est trop faible.

---

## Bloc D — L'acquisition et la machine créative

| # | Question | Ta réponse | (obs/est) |
|---|---|---|---|
| D1 | Nombre de **nouveaux** clients sur 30 jours | | |
| D2 | **nCAC = C8 ÷ D1** (toute la dépense pub, divisée par les NOUVEAUX clients) | | |
| D3 | Contribution de la première commande = (AOV new HT × C7) | | |
| D4 | **Marge à la première commande = D3 − D2** | | |
| D5 | Part du canal principal dans la dépense publicitaire | | |
| D6 | Concepts créatifs **nouveaux** (pas des variations) testés la semaine dernière | | |
| D7 | Concepts devenus gagnants sur les 4 dernières semaines | | |
| D8 | Nombre de gagnants actuellement en rotation | | |
| D9 | Âge du concept qui porte le plus de dépense | | |

### Lecture

- **D4 négatif** est normal — c'est le cas à tous les paliers du modèle de
  référence ([canoniques § 2.4](../donnees/chiffres-canoniques.md), de −4,93 € à
  −7,26 €). Ça devient un problème seulement si le bloc E ne le rembourse pas.
- **D5 > 70 %** : dépendance mono-canal. Ce n'est pas un risque marketing, c'est un
  risque de ruine. Lis [E13](../modules/E13-risque-de-ruine.md) § 2 et
  [C10](../etudes-de-cas/C10-compte-publicitaire-banni.md).
- **D6** est l'indicateur le plus prédictif de ta croissance des six prochains mois,
  et presque personne ne le suit. Ordres de grandeur du modèle de référence
  ([canoniques § 6](../donnees/chiffres-canoniques.md)) : ~14 concepts nouveaux par
  semaine à 53 k€ de CA hebdomadaire, ~38 à 272 k€, ~57 à 1 M€.
  **Si D6 vaut 0 ou 1, c'est ton unique chantier**, quel que soit ton niveau.
- **D9 > 10 semaines** avec un D6 faible : tu vis sur un actif qui s'épuise. Le jour
  où ce concept meurt, ton CAC explose et tu n'auras rien pour le remplacer.

---

## Bloc E — La rétention

| # | Question | Ta réponse | (obs/est) |
|---|---|---|---|
| E1 | Sur les clients acquis il y a 90 jours, quel pourcentage a passé une **deuxième** commande ? | | |
| E2 | Part du CA des 30 derniers jours provenant de clients déjà acquis | | |
| E3 | Nombre moyen de commandes par client sur 12 mois | | |
| E4 | **LTV 12 mois en marge de contribution** = (E3 × AOV HT × C7) | | |
| E5 | **LTV / CAC à 12 mois = E4 ÷ D2** | | |
| E6 | **Payback** : au bout de combien de mois la contribution cumulée d'un client dépasse-t-elle D2 ? | | |

### Lecture

| E5 | Verdict |
|---|---|
| **< 1,3** | Tu n'as pas de marque, tu as un canal de vente. Ne scale pas : répare la rétention ou l'offre. |
| **1,3 à 2,0** | Fragile. Tu peux croître lentement, sans à-coups, en surveillant le cash. |
| **2,0 à 4,0** | Zone de croissance. C'est là que se trouve le modèle de référence (2,17 à 12 mois au palier P5). Accélère. |
| **> 5,0** | **Tu sous-investis.** Contre-intuitif mais démontré en [E01](../modules/E01-arithmetique-de-la-marque.md) § 7 : un ratio très élevé signifie que tu laisses du volume rentable sur la table. Augmente la dépense jusqu'à ce que le CAC marginal fasse redescendre le ratio vers 3. |

> **E1 est le chiffre le plus important de tout ce bloc.** Le passage de la première
> à la deuxième commande est de très loin la marche la plus haute. Tout le reste de
> la courbe en découle. Renvoi : [E08](../modules/E08-retention-et-ltv.md) § 4.

---

## Bloc F — Le cash

| # | Question | Ta réponse | (obs/est) |
|---|---|---|---|
| F1 | Trésorerie disponible aujourd'hui | | |
| F2 | Valeur du stock au coût de revient | | |
| F3 | Encours d'encaissement (argent chez le prestataire de paiement) | | |
| F4 | Dettes fournisseurs à payer sous 60 jours | | |
| F5 | **BFR ≈ F2 + F3 − F4** | | |
| F6 | Consommation nette de trésorerie du dernier mois | | |
| F7 | **Semaines de trésorerie restantes = F1 ÷ (F6 ÷ 4,33)** | | |
| F8 | Capital supplémentaire que tu peux mobiliser sans mettre ta vie en jeu | | |

### Lecture

| F7 | Verdict |
|---|---|
| **> 26 semaines** | Tu peux prendre des risques mesurés et tester. |
| **13 à 26 semaines** | Zone de vigilance. Chaque décision de stock ou de budget devient une décision de trésorerie. |
| **6 à 13 semaines** | **Tu n'as plus de stratégie, tu as une contrainte.** Va lire [C08](../etudes-de-cas/C08-redressement-90-jours.md) et applique-le. |
| **< 6 semaines** | Urgence. Le seul sujet est la trésorerie : encaisser plus vite, dépenser moins, décaler le fournisseur. Pas de croissance, pas de test, pas de recrutement. |

> Repère du modèle de référence ([canoniques § 4](../donnees/chiffres-canoniques.md)) :
> le BFR représente 12 à 17 jours de CA à chaque palier, et chaque tranche de
> +100 000 € de CA mensuel immobilise 40 000 à 58 000 € de cash. **La croissance
> s'achète en cash avant de rapporter de la marge.**

---

## Bloc G — Toi

Sans chiffres cette fois, mais c'est le bloc qui prédit le mieux l'abandon.

| # | Question | Ta réponse |
|---|---|---|
| G1 | Heures réellement disponibles par semaine (pas celles que tu voudrais) | |
| G2 | Nombre de personnes dans l'équipe, en équivalent temps plein | |
| G3 | Parmi créa, achat média, produit, opérations, données : ce que tu sais faire toi-même | |
| G4 | Et ce que tu ne sais pas faire du tout | |
| G5 | Combien peux-tu perdre au total avant d'être obligé d'arrêter ? | |
| G6 | Combien de mois peux-tu tenir sans revenu de cette activité ? | |
| G7 | Qu'est-ce qui te ferait arrêter ? **Écris-le maintenant, pendant que tu es lucide.** | |

> G7 est l'exercice le plus désagréable du diagnostic et le plus utile. Un critère
> d'arrêt écrit à froid vaut mille décisions prises à chaud. Il t'évitera soit de
> t'obstiner deux ans de trop, soit — plus fréquent — d'arrêter au mois 7 alors que
> ta courbe de réachat était en train de se retourner.

---

## Placement

Croise ton bloc B (où tu en es) et tes blocs C à F (comment tu y es).

| CA mensuel TTC (B1) | Niveau | Palier de référence | Le seul goulot à cette étape |
|---|---|---|---|
| Aucune vente | **N0** | avant P1 | Le choix de terrain — bloc A |
| < 30 000 € | **N1** | P1 | L'offre et la preuve de demande |
| 30 000 à 300 000 € | **N2** | P2 | La machine créative et le cash |
| 300 000 € à 2 M€ | **N3** | P3 – P4 | L'organisation et la mesure |
| > 2 M€ | **N4** | P4 – P5 | La marge et le risque de ruine |

**Puis applique les trois correctifs.** Ils priment sur le placement par le CA :

1. **Si score A < 14** → tu es en réalité en N0, quel que soit ton chiffre
   d'affaires. Ton chantier est structurel, pas marketing.
2. **Si F7 < 13 semaines** → tu es en régime de trésorerie. Tout le reste attend.
   Ton programme est [C08](../etudes-de-cas/C08-redressement-90-jours.md), point.
3. **Si D6 ≤ 1** → ton chantier est la machine créative avant tout autre, même si
   tes chiffres sont bons par ailleurs. Un compte qui ne teste pas meurt à terme
   fixe, il ne le sait pas encore.

---

## Ce que tu fais dans les 90 jours qui suivent

| Ton placement | Les trois chantiers du trimestre, dans l'ordre |
|---|---|
| **N0** | 1. Noter ta catégorie avec la grille de [E02](../modules/E02-marche-et-produit.md) § 3. 2. Mener les six tests de demande de E02 § 4 avec les seuils écrits d'avance. 3. Construire l'offre et le prix avec [E03](../modules/E03-offre-et-prix.md). |
| **N1** | 1. Recherche client et construction de trois angles ([E04](../modules/E04-psychologie-du-client.md) § 8). 2. Porter l'AOV au niveau qui finance ton CAC ([E03](../modules/E03-offre-et-prix.md) § 4). 3. Mettre en route un rythme de test créatif — au moins 5 concepts nouveaux par semaine. |
| **N2** | 1. Industrialiser la créa jusqu'au volume de ton palier ([E05](../modules/E05-machine-creative.md) § 6 et § 7). 2. Installer les flux de rétention et mesurer E1 par cohorte ([E08](../modules/E08-retention-et-ltv.md)). 3. Modéliser ton BFR et ta croissance autofinançable ([E10](../modules/E10-cash-et-operations.md) § 2). |
| **N3** | 1. Un test géographique d'incrémentalité sur tes deux canaux les plus flatteurs ([E09](../modules/E09-mesure-et-incrementalite.md) § 5). 2. Écrire les définitions et le tableau de bord à trois niveaux. 3. Préparer l'ouverture d'**un seul** marché ([E11](../modules/E11-passage-a-echelle.md) § 2). |
| **N4** | 1. Le chantier P5 → P5+ décomposé ([E14](../modules/E14-plan-1M-semaine.md) § 6). 2. Le registre des risques et la réduction de la dépendance ([E13](../modules/E13-risque-de-ruine.md) § 9). 3. La mesure du capital de marque ([E12](../modules/E12-marque-et-actif.md) § 3). |

---

## La synthèse à m'envoyer

```
DIAGNOSTIC DU __/__/____

Score A : ___/35        Verdict structurel : ______________________
Placement : N_          Palier : P_
MER réel : ____   MER seuil CM3 : ____   MER seuil EBITDA : ____
Marge à la 1re commande : ______     LTV/CAC 12 mois : ______
Concepts nouveaux testés / semaine : ____
Semaines de trésorerie : ____
Correctif déclenché : ☐ A<14   ☐ F7<13   ☐ D6≤1   ☐ aucun

LES TROIS CHANTIERS DU TRIMESTRE
1.
2.
3.

CE QUE J'ARRÊTE CE TRIMESTRE

MON CRITÈRE D'ARRÊT (G7), ÉCRIT À FROID
```

---

*Une fois le diagnostic fait, va lire le [protocole](protocole.md) § 3 pour ton
parcours de lecture, puis [jalons.md](jalons.md) pour savoir ce que tu dois
démontrer avant de passer au palier suivant.*
