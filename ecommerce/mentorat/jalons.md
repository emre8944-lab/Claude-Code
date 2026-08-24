# Les jalons — ce qu'il faut avoir démontré pour passer au palier suivant

> Une condition de passage est **binaire et vérifiable**. « L'équipe est plus
> mature » n'est pas une condition. « Taux de première à deuxième commande à 90
> jours ≥ 18 %, mesuré sur trois cohortes consécutives » en est une.
>
> Les seuils ci-dessous sont calibrés sur le
> [modèle de référence](../donnees/chiffres-canoniques.md). Ils ne sont pas
> arbitraires : chacun est le niveau en dessous duquel le palier suivant détruit
> de la valeur au lieu d'en créer. Quand un seuil mérite discussion, la
> justification est donnée sous le tableau.

---

## Pourquoi des portes

Le mode d'échec le plus courant de ce métier n'est pas de ne pas savoir quoi
faire. C'est de **faire au palier N+1 ce qui ne marchait déjà pas au palier N,
mais dix fois plus cher**. Une marque qui scale un compte publicitaire dont le
MER est sous le seuil ne découvre pas un problème : elle multiplie un problème
qu'elle avait déjà et qu'elle n'avait pas su lire.

Chaque porte a donc une fonction unique : **empêcher de multiplier une perte.**

Deux règles d'usage :

1. **Toutes les conditions, pas la majorité.** Une porte à 5 conditions sur 6 est
   une porte fermée. Les conditions ne se compensent pas entre elles : elles
   couvrent des modes de mort différents.
2. **Mesuré, pas estimé.** Une condition validée sur une estimation n'est pas
   validée. Si tu ne peux pas la mesurer, la construire est le chantier.

---

## Porte 0 → P1 — le droit de lancer

Tu n'as pas encore vendu. Cette porte coûte quelques milliers d'euros à franchir
et t'en économise des dizaines de milliers.

| # | Condition | Seuil | Où c'est traité |
|---|---|---|---|
| 1 | Coefficient du produit héros, **au coût complet rendu entrepôt** | **≥ ×5,0** | [E02](../modules/E02-marche-et-produit.md) § 6 |
| 2 | Score structurel du diagnostic bloc A | **≥ 21 / 35** | [diagnostic](diagnostic.md) |
| 3 | Tests de demande menés avec seuils écrits d'avance | **≥ 4 favorables sur 6** | [E02](../modules/E02-marche-et-produit.md) § 4 |
| 4 | Durée de consommation ou d'usage du produit | **≤ 8 mois** | [E02](../modules/E02-marche-et-produit.md) § 1 |
| 5 | Capital disponible ≥ pertes cumulées P1+P2 modélisées + BFR de P2 | calculé en [E10](../modules/E10-cash-et-operations.md) § 3 | |
| 6 | Critère d'arrêt écrit, daté, chiffré | existe | [diagnostic](diagnostic.md) G7 |

> **Sur le seuil ×5,0.** Il vient directement de l'arithmétique du MER seuil. Sous
> ×5, la marge brute après logistique, paiement, retours et remises tombe en
> dessous d'environ 50 %, ce qui porte le MER d'équilibre au-delà de 2,4 — un
> niveau que très peu de marques tiennent en acquisition payante froide. Le cas
> [C01](../etudes-de-cas/C01-coefficient-insuffisant.md) déroule le calcul complet
> sur un produit à ×2,53.

---

## Porte P1 → P2 — le droit de dépenser sérieusement

Tu vends. La question n'est plus « est-ce que ça se vend » mais « est-ce que ça se
vend de façon répétable ». On cherche un signal, pas un coup de chance.

| # | Condition | Seuil | Pourquoi ce seuil |
|---|---|---|---|
| 1 | Commandes cumulées | **≥ 200** | En dessous, aucune statistique n'est lisible : tu interprètes du bruit |
| 2 | Taux de marge brute CM2 mesuré | **≥ 55 %** | Le modèle de référence est à 57,2 % au palier P1 |
| 3 | Concepts créatifs gagnants **distincts** (pas des variations l'un de l'autre) | **≥ 2** | Un seul gagnant est une coïncidence ; deux est un début de méthode |
| 4 | Taux 1ʳᵉ → 2ᵉ commande à 90 jours, **mesuré sur une cohorte réelle** | **≥ 12 %** | En dessous, la perte sur la première commande n'est jamais remboursée |
| 5 | MER blended sur 4 semaines consécutives | **≥ 1,80** | Valeur canonique de P1 |
| 6 | Trésorerie couvrant la perte mensuelle projetée de P2 | **≥ 6 mois** | La perte canonique de P2 est de −19 838 €/mois |
| 7 | Coûts variables réels connus au centime, sans estimation | complet | Tu ne peux pas piloter une marge que tu n'as pas mesurée |

> **Le piège de cette porte.** La condition 4 est celle que tout le monde saute,
> parce qu'elle demande d'attendre 90 jours. C'est précisément pour ça qu'elle est
> la plus importante : c'est la seule qui te dit si tu construis une marque ou si
> tu loues de l'attention.

---

## Porte P2 → P3 — le droit de scaler

C'est la porte la plus meurtrière du parcours. La plupart des marques la
franchissent sans la remplir, et c'est là qu'elles meurent — pas au lancement.

| # | Condition | Seuil | Pourquoi |
|---|---|---|---|
| 1 | MER blended sur **8 semaines consécutives** | **≥ 2,20** | Valeur canonique de P2. Huit semaines, parce que quatre peuvent être une saison |
| 2 | Gagnants créatifs distincts en rotation | **≥ 5** | En dessous, la mort d'un concept fait décrocher tout le compte |
| 3 | Concepts **nouveaux** testés par semaine, tenu 8 semaines | **≥ 10** | Le modèle de référence en teste ~14 à ce niveau de dépense ([canoniques § 6](../donnees/chiffres-canoniques.md)) |
| 4 | Âge moyen des gagnants qui portent la dépense | **≤ 8 semaines** | Au-delà, tu vis sur un actif qui s'épuise |
| 5 | Taux 1ʳᵉ → 2ᵉ commande à 90 jours | **≥ 18 %** | |
| 6 | Part du CA en réachat | **≥ 15 %** | Valeur canonique de P2 |
| 7 | LTV/CAC à 12 mois, **mesurée sur cohortes réelles** | **≥ 2,00** | Le modèle de référence est à 2,30 à P2 |
| 8 | Délai de récupération du CAC | **≤ 4 mois** | Au-delà, c'est ta trésorerie et non ta rentabilité qui plafonne ta croissance |
| 9 | Trésorerie ≥ BFR du palier P3 visé + 3 mois de frais fixes | calculé | Le BFR canonique de P3 est de 481 053 € |
| 10 | Une personne dont la créa est le métier principal (interne ou externe), avec un rythme documenté | existe | |

> **Ne négocie pas la condition 3.** C'est la seule qui est un *rythme* et non un
> *résultat*. Toutes les autres se dégraderont si celle-ci n'est pas tenue, avec
> six mois de retard — le délai exact qui rend la cause invisible quand l'effet
> arrive.

---

## Porte P3 → P4 — le droit d'ouvrir un marché

Tu gagnes de l'argent en France. La question devient organisationnelle.

| # | Condition | Seuil |
|---|---|---|
| 1 | EBITDA positif sur 3 mois consécutifs | **> 0** |
| 2 | MER blended sur 12 semaines | **≥ 2,60** |
| 3 | Concepts nouveaux testés par semaine | **≥ 30** |
| 4 | Part du canal publicitaire principal | **≤ 70 %** |
| 5 | Définitions écrites des indicateurs + tableau de bord à trois niveaux en service | existe |
| 6 | Au moins **un** test d'incrémentalité mené jusqu'au bout | fait |
| 7 | Prestataire logistique capable d'absorber 2,5 fois le volume actuel, contractuellement | vérifié |
| 8 | Trésorerie ≥ BFR de P4 + 4 mois de frais fixes | BFR canonique de P4 : 1 392 510 € |
| 9 | Un responsable identifié par fonction : créa, média, opérations | existe |
| 10 | Marge brute CM2 | **≥ 59 %** |

> **La condition 6 surprend toujours.** Pourquoi exiger un test d'incrémentalité
> avant d'ouvrir un pays ? Parce qu'ouvrir un marché multiplie ton budget média,
> et que multiplier un budget mal alloué multiplie la mauvaise allocation. Le cas
> [C06](../etudes-de-cas/C06-test-incrementalite.md) montre ce que ça représente :
> une part significative du budget peut être non incrémentale sans que rien dans
> les interfaces ne le signale.

---

## Porte P4 → P5 — le droit de viser le million hebdomadaire

| # | Condition | Seuil |
|---|---|---|
| 1 | EBITDA sur 6 mois | **≥ 7 % du CA HT** |
| 2 | Marchés à l'équilibre de contribution | **≥ 3** |
| 3 | Part du canal publicitaire principal | **≤ 60 %** |
| 4 | Part du CA en réachat | **≥ 35 %** |
| 5 | CA HT annuel par ETP | **≥ 900 000 €** |
| 6 | Concepts nouveaux testés par semaine | **≥ 50** |
| 7 | Registre des risques tenu, avec redondance publicitaire opérationnelle | existe |
| 8 | BFR financé sans dette à moins de 12 mois | vérifié |
| 9 | Taux de retour et taux de remise **stables ou en baisse** sur 6 mois | vérifié |

> **La condition 9 est celle que personne ne met dans ses objectifs et qui décide
> de tout.** C'est exactement ce qui différencie P5 de P5+ dans le modèle de
> référence, et c'est aussi ce qui a détruit VERSO dans le cas
> [C04](../etudes-de-cas/C04-scale-qui-detruit-la-marge.md) : une croissance de
> chiffre d'affaires achetée par la remise et l'élargissement du ciblage.

---

## Porte P5 → P5+ — la seule qui compte vraiment

Tu fais 1 M€ par semaine. Le modèle de référence te donne **10,1 % d'EBITDA**, soit
4 377 023 € par an. Le même chiffre d'affaires, autrement fabriqué, en donne
**20,3 %**, soit 8 805 583 €. L'écart — 4,4 M€ par an — ne demande pas un euro de
chiffre d'affaires supplémentaire.

Voici les cinq chantiers, chacun avec sa cible chiffrée
([canoniques § 8](../donnees/chiffres-canoniques.md)) :

| # | Chantier | De | À | Module |
|---|---|---:|---:|---|
| 1 | Panier moyen mixte TTC | 71,98 € | **77,20 €** | [E03](../modules/E03-offre-et-prix.md) § 4 |
| 2 | Part du CA en réachat | 44,9 % | **52,4 %** | [E08](../modules/E08-retention-et-ltv.md) |
| 3 | Taux de remise (en % du CA HT) | 8,0 % | **5,5 %** | [E03](../modules/E03-offre-et-prix.md) § 5 |
| 4 | MER blended | 2,90 | **3,40** | [E05](../modules/E05-machine-creative.md), [E12](../modules/E12-marque-et-actif.md) |
| 5 | COGS + logistique (en % du CA HT) | 25,5 % | **24,0 %** | [E10](../modules/E10-cash-et-operations.md) § 6 et § 9 |

> **Le chantier 4 est le plus difficile et le plus mal compris.** Passer d'un MER
> de 2,90 à 3,40 ne s'obtient pas en optimisant des campagnes. Il s'obtient parce
> qu'une part croissante de la demande n'a plus besoin d'être achetée — c'est la
> définition même du capital de marque
> ([E12](../modules/E12-marque-et-actif.md) § 7). C'est le seul chantier du cursus
> qui prend des années et non des trimestres, et c'est pour ça qu'il faut le
> commencer bien avant P5.

---

## Ce qui n'est **pas** un critère de passage

Ces chiffres circulent, ils flattent, et ils ne décident rien :

| Faux critère | Pourquoi il ne vaut rien |
|---|---|
| Le chiffre d'affaires seul | Se pilote par la remise et le budget média. Ne dit rien de l'entreprise. |
| Le ROAS affiché par une plateforme | Non incrémental, non additionnable, manipulable par l'attribution. [E09](../modules/E09-mesure-et-incrementalite.md) § 1 |
| Le nombre d'abonnés sur les réseaux | Sans corrélation démontrée avec le CAC. |
| Le taux de conversion du site | Dépend du mix de trafic. Un CAC qui monte fait souvent monter le taux de conversion. |
| Une LTV extrapolée à 24 ou 36 mois | Une extrapolation n'est pas une mesure. Plafonne à 12 mois. |
| « Le meilleur mois de l'histoire » | Une saison, une promotion, un concept chanceux. Regarde 8 semaines. |
| Une levée de fonds | Change ta trésorerie, pas ta structure de marge. |

---

## Le rituel de porte

Une fois par trimestre, une heure, seul ou avec ton associé.

1. Tu recopies le tableau de la porte que tu vises.
2. Pour chaque ligne : **oui / non / non mesuré**. Rien d'autre. Pas de « presque ».
3. Toute ligne « non mesuré » devient un chantier de mise en mesure — c'est
   prioritaire sur toute action commerciale, parce que sans mesure tu décideras
   au ressenti pendant encore trois mois.
4. La première ligne « non » de la liste est **ton unique chantier du trimestre**.
5. Tu écris la date du prochain rituel de porte.

> **Franchir une porte sans la remplir n'accélère rien.** Ça ne fait qu'avancer la
> date à laquelle tu découvriras le problème, à un moment où il coûtera dix fois
> plus cher à réparer.

---

*Suite : le [tableau de bord](tableau-de-bord.md), qui produit les chiffres dont
ces portes ont besoin.*
