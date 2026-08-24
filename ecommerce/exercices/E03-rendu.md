# Exercices — Module E03 : L'offre et le prix

> **Avant de commencer :** rappel des règles — tout chiffre est marqué (obs) ou
> (est) ; tout montant est marqué TTC ou HT ; les seuils s'écrivent avant le test.
> **Ne lis pas le corrigé avant d'avoir rendu.**

Calculatrice obligatoire. Convention valable partout : TVA 20 %, la logistique est
un coût **par colis** et non un pourcentage du panier, et l'on sépare toujours les
coûts **fixes par commande** (marchandise, colis) des coûts **proportionnels au prix**
(PSP, retours/SAV, remises).

---

## Exercice 1 — La table de sensibilité au prix du palier P3

NØRA au palier P3 (Scale France, mois 10 à 18, France + Belgique). Toutes les
données dont tu as besoin sont ici — tu n'as rien d'autre à ouvrir.

| Donnée | Valeur |
| --- | ---: |
| Commandes par mois | 18 000 |
| Panier moyen (AOV mixte) | 65,40 € TTC |
| TVA | 20 % |
| COGS (coût marchandise) | 16,0 % du CA HT |
| Logistique | 12,0 % du CA HT |
| Prestataire de paiement (PSP) | 1,65 % du CA HT |
| Retours et SAV | 3,0 % du CA HT |
| Remises | 7,0 % du CA HT |
| Marge brute (CM2) de référence | 592 033 € / mois |
| Dépense publicitaire | 436 000 € / mois |
| Frais fixes | 105 000 € / mois |

Deux hypothèses de travail, imposées : le COGS et la logistique **ne bougent pas**
quand le prix affiché bouge — un flacon reste un flacon, un colis reste un colis ;
la **dépense publicitaire par commande** reste constante quel que soit le volume,
ce qui revient à supposer un coût d'acquisition qui ne se dégrade pas en achetant
des commandes supplémentaires. Cette seconde hypothèse est fausse et généreuse :
note-le, tu en auras besoin à la question 5.

**(1)** Chiffre d'affaires HT par commande : ______________ €

**(2)** Décomposition des coûts variables par commande :

| Bloc | Montant ou taux |
| --- | ---: |
| Fixe par commande — COGS | ______ € |
| Fixe par commande — logistique | ______ € |
| **Total fixe par commande** | **______ €** |
| **Total proportionnel au prix** (PSP + retours + remises) | **______ %** |

**(3)** Marge brute par commande : ______________ €
*Contrôle obligatoire :* ce nombre × 18 000 doit redonner 592 033 €. S'il ne tombe
pas, ne va pas plus loin — reprends la question 2.

**(4)** Volume nécessaire pour tenir la **marge brute** de 592 033 € :

| Scénario | CA HT / cmd | Marge brute / cmd | Commandes nécessaires | Variation |
| --- | ---: | ---: | ---: | ---: |
| Référence | | | 18 000 | — |
| Prix **−10 %** | | | | |
| Prix **−20 %** | | | | |

**(5)** Volume nécessaire pour tenir l'**EBITDA** de référence :

Publicité par commande : ______________ €
EBITDA de référence : ______________ € / mois
CM3 par commande (marge brute − publicité) : ______________ €

| Scénario | CM3 / cmd | Commandes nécessaires | Variation |
| --- | ---: | ---: | ---: |
| Référence | | 18 000 | — |
| Prix **−10 %** | | | |
| Prix **−20 %** | | | |

**(6)** Prix **+10 %**, à EBITDA constant : quelle perte de volume peux-tu tolérer ?

CM3 par commande à +10 % : ______ €  →  Commandes suffisantes : ______  →  Perte tolérable : ______ %

*Contrôle : la réponse (6) est comprise entre 25 % et 40 %.*

Écris la phrase, en toutes lettres : « Au palier P3, je peux perdre ______ % de mes
commandes après une hausse de 10 % et gagner exactement autant qu'avant. »

> **CORRECTION —** voir [E03-corrige.md](E03-corrige.md) § 1

---

## Exercice 2 — Le seuil de franco de port optimal de NØRA

NØRA au palier P5 : 60 200 commandes/mois, 4 333 196 € de CA TTC/mois, AOV mixte
71,98 € TTC, CA HT 3 610 997 €, EBITDA annuel de référence 4 377 023 €.

Mix des formats à P5 (part des commandes) :

| Format | PVC TTC | Part des commandes |
| --- | ---: | ---: |
| Sérum Densité seul | 39,00 € | 17 % |
| Shampooing Fortifiant seul | 24,00 € | 9 % |
| Masque Réparateur seul | 29,00 € | 7 % |
| Rituel Complet | 74,00 € | 40 % |
| Cure 3 mois | 99,00 € | 27 % |

Contributions par commande, en convention colis : Rituel **35,52 €**, Cure **50,73 €**.
Coût réel d'une expédition : **6,60 €**. Frais de port facturés : **4,90 € TTC**, soit
**4,08 € HT**. Un ajout de shampooing (24,00 € TTC → 20,00 € HT) dans un colis déjà
constitué rapporte **14,29 €** de contribution : 20,00 − 3,10 de COGS − 13,05 % de
coûts proportionnels, et zéro colis supplémentaire.

Seuil actuel : **59,00 €**, hérité du palier P2 et jamais révisé. À P5, 26 % des
commandes passent en dessous et paient donc le port — c'est ce qui produit les
1,27 € de port facturé contenus dans l'AOV de 71,98 €.

**Hypothèses de comportement, imposées et identiques dans tous les scénarios.**
Une bande de commandes ne réagit à un seuil que s'il est **atteignable en un seul
ajout**, c'est-à-dire si `panier de la bande + 24,00 € ≥ seuil`.

| Situation de la bande | Ajoutent une référence | Paient le port | Abandonnent |
| --- | ---: | ---: | ---: |
| Sous le seuil, seuil **atteignable en un ajout** | 25 % | 72 % | 3 % |
| Sous le seuil, seuil **hors de portée** | 0 % | 94 % | 6 % |
| Au-dessus du seuil | — | — | — |

Les bandes mono-format sont déjà sous le seuil actuel et paient déjà le port : leur
comportement ne change dans aucun scénario, elles n'entrent donc dans aucun écart.

Remplis, pour les trois seuils :

| | **59,00 €** (actuel) | **89,00 €** | **109,00 €** |
| --- | ---: | ---: | ---: |
| Bandes nouvellement sous le seuil | — | | |
| Pour chacune : atteignable en un ajout ? | — | | |
| Commandes concernées | — | | |
| Ajouts : nombre × 14,29 € | — | | |
| Port encaissé : nombre × 4,08 € HT | — | | |
| Abandons : nombre × contribution perdue | — | | |
| **(2) Gain mensuel de marge brute** | **0 €** | | |
| **(1) Part des commandes qui paient le port** | 26 % | | |
| **(3) Nouvel AOV TTC** | 71,98 € | | |
| **(4) Gain annuel d'EBITDA** | **0 €** | | |
| Gain annuel en % de l'EBITDA de référence | 0 % | | |

*Contrôle : à 89,00 €, tu dois retrouver 1 573 440 € par an et un AOV de 75,81 €.*

**(5)** À 109,00 €, le port encaissé est presque deux fois plus élevé qu'à 89,00 €,
et l'AOV est plus haut. Pourtant le seuil à 109,00 € est le moins bon des deux.
Écris la raison en trois lignes maximum, et nomme la contrainte violée.

________________________________________________________________

________________________________________________________________

________________________________________________________________

> **CORRECTION —** voir [E03-corrige.md](E03-corrige.md) § 2

---

## Exercice 3 — Ta gamme, référence par référence

Tes chiffres. Une ligne par référence que tu vends réellement, y compris celles dont
tu as honte. La **contribution en convention colis** se calcule ainsi :

```
Contribution = PVC HT − COGS − (taux de coûts proportionnels × PVC HT) − coût d'un colis
```

où les coûts proportionnels sont ceux qui suivent le prix : PSP, retours/SAV, remises.

Mon coût de colis (obs / est) : ______ €  —  Mon taux de coûts proportionnels : ______ %
Mon coût d'acquisition d'un **nouveau** client (nCAC) : ______ €  (obs / est)

| Référence | PVC TTC | COGS | Coef. | Contribution | Écart au nCAC | Rôle | Responsable |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

Un seul rôle par référence : **produit d'appel** (entrer dans la catégorie, jamais
porter l'acquisition payante) — **héros** (porte 100 % de la publicité et de la
preuve) — **produit de panier** (élève l'AOV sur la commande du héros) —
**premium ou prépayé** (porte la marge, le cash et le réachat anticipé).

Combien de références portent aujourd'hui du budget média ? ______

Combien de références remboursent leur nCAC dès la première commande ? ______

Si une référence n'a aucun des quatre rôles, écris ce qu'elle fait dans ta gamme :

________________________________________________________________

> **CORRECTION —** voir [E03-corrige.md](E03-corrige.md) § 3

---

## Exercice 4 — Ta hausse de prix de 10 %

Tes chiffres, sur ton dernier mois complet.

**(0) Sépare tes coûts variables en deux blocs.** Un coût est « fixe par commande »
s'il ne change pas quand tu changes l'étiquette : marchandise, colis, préparation.
Il est « proportionnel au prix » s'il est un pourcentage de l'encaissement : PSP,
retours et SAV, remises, commissions d'affiliation.

| Poste de coût variable | Montant/mois | Fixe par cmd | Proportionnel au prix |
| --- | ---: | :---: | :---: |
| | | ☐ | ☐ |
| | | ☐ | ☐ |
| | | ☐ | ☐ |
| | | ☐ | ☐ |

| Ligne | Aujourd'hui | À prix **+10 %** |
| --- | ---: | ---: |
| Commandes du mois | | *(inchangé pour le calcul)* |
| CA HT par commande | | |
| Total fixe par commande (€) | | *(identique)* |
| Total proportionnel au prix (%) | | *(identique)* |
| **(1) et (2) Marge brute par commande** | | |
| **(3) Publicité par commande** | | *(identique)* |
| **(4) CM3 par commande** | | |
| Frais fixes du mois | | *(identiques)* |
| EBITDA du mois | | |

**(5)** Nombre de commandes qui me ramène exactement à mon EBITDA actuel, au
nouveau prix : ______________

**(6)** Perte de volume tolérable : ______ %

Écris la phrase : « Je peux perdre ______ % de mes commandes après une hausse de
10 % et gagner autant qu'aujourd'hui. »

Date de ma dernière hausse de prix : ______________
Mon élasticité-prix est-elle **mesurée** ou **supposée** ? ☐ mesurée ☐ supposée
Si supposée : le test géographique qui la mesurerait — zones, durée, métrique de
décision, seuils écrits d'avance.

| Élément | Ma décision |
| --- | --- |
| Zone test / zone témoin | |
| Durée | |
| Métrique de décision | |
| Seuil de généralisation, écrit avant | |
| Seuil d'abandon, écrit avant | |

> **CORRECTION —** voir [E03-corrige.md](E03-corrige.md) § 4

---

## Exercice 5 — Ta facture de remise et ton audit d'accoutumance

Tes chiffres, sur 12 mois glissants.

**(1)** Total des remises consenties : ______________ € HT, soit ______ % du CA HT.

**(2)** Valeur d'un point de remise en moins, en EBITDA annuel : ______________ €
*(1 % de ton CA HT annuel ; aucune autre ligne ne bouge, donc ce montant est net.)*

**(3)** Répartition par mécanique :

| Mécanique | Montant € HT | % du total | Propriétaire | Plafond écrit ? |
| --- | ---: | ---: | --- | :---: |
| Remise d'accueil (1ʳᵉ commande) | | | | ☐ |
| Panier abandonné | | | | ☐ |
| Codes créateurs / affiliation | | | | ☐ |
| Opérations calendaires | | | | ☐ |
| Geste commercial SAV | | | | ☐ |
| **Total** | | **100 %** | | |

**(4)** Part du CA annuel réalisée pendant les **cinq journées les plus
promotionnelles** de l'année : ______ %
Et pendant les **huit semaines qui les précèdent**, l'écart au CA hebdomadaire
moyen du reste de l'année : ______ %

**(5)** Audit d'accoutumance — part des clients actifs dont **toutes** les commandes
ont été passées en promotion :

| Année | Part de la base active | Part du CA qu'ils représentent |
| --- | ---: | ---: |
| N−2 | | |
| N−1 | | |
| N | | |

Tendance sur trois ans : ☐ croissante ☐ stable ☐ décroissante

> **CORRECTION —** voir [E03-corrige.md](E03-corrige.md) § 5

---

## Exercice 6 — Décision : le prix ou le seuil

Ta marque ressemble à NØRA au palier P5 : 60 200 commandes/mois, AOV 71,98 € TTC,
CA HT 3 610 997 €/mois, marge brute 2 218 957 €/mois, publicité 1 494 206 €/mois,
frais fixes 360 000 €/mois, EBITDA 364 752 €/mois, soit 4 377 023 €/an. Coûts fixes
par commande 15,30 € (COGS 8,70 € + colis 6,60 €), coûts proportionnels au prix
13,05 %.

Le comité te demande **un seul chantier** pour le trimestre. Les deux options sont
exclusives : elles déplacent le même prix perçu, et les mener ensemble rendrait
impossible d'attribuer le résultat à l'une ou à l'autre.

**Option A — Hausse de 6 % sur toute la gamme.** Perte de volume estimée à 4 %
(estimation interne, jamais testée). La hausse porte sur tout ce qui est facturé,
port et ajouts compris. La publicité **par commande** reste inchangée.

**Option B — Seuil de franco porté de 59,00 € à 89,00 €.** Hypothèses de
comportement de l'exercice 2, résultats de l'exercice 2.

| | **Option A** | **Option B** |
| --- | ---: | ---: |
| Marge brute par commande, après | | |
| CM3 par commande, après | | |
| Commandes par mois, après | | |
| EBITDA mensuel, après | | |
| **Gain d'EBITDA annuel** | | |
| **Nouvel AOV TTC** | | |
| Variation d'AOV | | |
| Coût d'exécution (jours-homme, systèmes touchés) | | |
| Réversibilité | | |
| Délai avant de savoir si ça a marché | | |

**Ma décision :** ☐ Option A ☐ Option B

**Ma justification** — elle doit contenir les deux gains annuels, les deux nouveaux
AOV, le coût d'exécution de chaque option, et la phrase qui dit **laquelle des deux
estimations comportementales est la plus fragile et pourquoi** :

________________________________________________________________

________________________________________________________________

________________________________________________________________

________________________________________________________________

**Le seuil de bascule.** À partir de quelle perte de volume réelle l'option A
devient-elle moins bonne que l'option B, en euros ? ______ %

**Le test à quatre semaines qui trancherait pour de bon :**

| Élément | Ma décision |
| --- | --- |
| Ce que je teste | |
| Zone test / zone témoin | |
| Métrique de décision | |
| Seuil de généralisation, écrit avant | |
| Seuil d'abandon, écrit avant | |

> **CORRECTION —** voir [E03-corrige.md](E03-corrige.md) § 6

---

## Ma synthèse

1. Ce que j'ai appris : ________________________________________________

2. Ce qui m'a surpris : ________________________________________________

3. Le chiffre de ma marque que je ne connaissais pas : __________________

4. La décision que ça change, cette semaine : __________________________

5. Ce que je mesurerai pour savoir si j'avais raison : _________________
