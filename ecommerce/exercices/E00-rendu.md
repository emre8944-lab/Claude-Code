# Exercices — Module E00 : Le cadrage, ce métier vraiment

> **Avant de commencer :** rappel des règles — tout chiffre est marqué (obs) ou
> (est) ; tout montant est marqué TTC ou HT ; les seuils s'écrivent avant le test.
> **Ne lis pas le corrigé avant d'avoir rendu.**

Module source : [`E00-cadrage.md`](../modules/E00-cadrage.md). Données de référence :
[chiffres canoniques](../donnees/chiffres-canoniques.md). Calculatrice obligatoire,
virgule décimale, deux décimales sauf indication contraire.

Trois formules servent partout dans ce devoir. Écris-les en haut de ta copie avant
de commencer, tu les utiliseras cinq fois :

```
COGS en % du CA HT     = (1 + TVA) ÷ coefficient        = 1,20 ÷ k
MER seuil (CM3 = 0)    = (1 + TVA) ÷ marge brute %      = 1,20 ÷ m
MER seuil (EBITDA = 0) = (1 + TVA) ÷ (m − f)   avec f = frais fixes ÷ CA HT
```

---

## Exercice 1 — Le seuil d'un produit à ×3,5 (données NØRA)

Un façonnier te propose une référence dont le coefficient rendu entrepôt vaut
**×3,5** : prix de vente conseillé TTC divisé par coût marchandise rendu entrepôt.
Tu la vendrais avec la structure de coût variable du **palier P3** de NØRA, que
voici en entier pour que tu n'aies rien à chercher (chiffres canoniques § 2.1,
§ 2.2, § 2.5) :

| Poste, palier P3 | Valeur |
| --- | ---: |
| TVA | 20 % |
| Logistique | 12,00 % du CA HT |
| PSP (prestataire de paiement) | 1,65 % du CA HT |
| Retours / SAV | 3,00 % du CA HT |
| Remises | 7,00 % du CA HT |
| CA HT mensuel | 981 000 € |
| Dépense publicitaire mensuelle | 436 000 € |
| Frais fixes mensuels | 105 000 € |
| MER réel de P3 | 2,70 |
| EBITDA mensuel de NØRA à P3 | 51 033 € |

Remplis :

| # | Grandeur | Ta valeur |
| ---: | --- | ---: |
| 1 | COGS en % du CA HT | |
| 2 | Somme des autres coûts variables (% du CA HT) | |
| 3 | Marge brute m (% du CA HT) | |
| 4 | MER seuil CM3 = 0 | |
| 5 | Frais fixes f en % du CA HT | |
| 6 | MER seuil EBITDA = 0 | |
| 7 | Écart entre le MER réel (2,70) et le seuil CM3, en % | |
| 8 | Marge brute mensuelle en € | |
| 9 | CM3 mensuel en € | |
| 10 | EBITDA mensuel en € | |
| 11 | Écart d'EBITDA annuel avec NØRA à P3 | |

**Ta conclusion, en une phrase, et une seule :**

_(à remplir)_

> **CORRECTION —** voir [E00-corrige.md](E00-corrige.md) § 1

---

## Exercice 2 — Le mois de la mort (données NØRA)

Tu as réuni **150 000 €** et tu suis exactement la trajectoire canonique : P1 sur
les mois M1 à M3, P2 sur les mois M4 à M9. Données autorisées :

| Grandeur | Valeur |
| --- | ---: |
| EBITDA mensuel P1 (perte) | −9 403 € |
| EBITDA mensuel P2 (perte) | −19 838 € |
| BFR (besoin en fonds de roulement) à P1 | 21 603 € |
| BFR à P2 | 104 462 € |

*Hypothèse imposée, la même qu'au § 5.3 du module : le BFR se constitue
linéairement à l'intérieur de chaque palier, et il n'est jamais remboursé.*

| # | Grandeur | Ta valeur |
| ---: | --- | ---: |
| 1 | Trésorerie consommée à la fin de M3 (pertes + BFR) | |
| 2 | Constitution mensuelle de BFR pendant P2 | |
| 3 | Consommation mensuelle totale pendant P2 | |
| 4 | Nombre de mois de P2 que tes 150 000 € financent | |
| 5 | **Le mois où ta trésorerie atteint zéro** | |
| 6 | Nombre de mois qui te séparaient de la fin de P2 | |
| 7 | Capital nécessaire pour atteindre M9 sans réserve | |
| 8 | Capital additionnel qu'il aurait fallu réunir | |

**Ce que la marque avait déjà prouvé, ou non, au moment où elle meurt :**

_(à remplir)_

> **CORRECTION —** voir [E00-corrige.md](E00-corrige.md) § 2

---

## Exercice 3 — Ton coefficient et ton seuil (tes chiffres)

Sur ta référence principale. Si tu n'as pas encore vendu, prends ton devis
fournisseur et marque toutes tes lignes **(est)**.

| Ligne | Valeur | (obs) ou (est) |
| --- | ---: | :---: |
| PVC TTC affiché | € | |
| Taux de TVA appliqué | % | |
| PVC HT | € | |
| Prix moyen TTC **réellement encaissé** (remises comprises) | € | |
| Coût de fabrication sortie usine | € | |
| Emballage primaire et secondaire | € | |
| Transport amont et fret | € | |
| Droits de douane | € | |
| Contrôle qualité, provision casse, amortissement d'outillage | € | |
| **= COGS rendu entrepôt** | € | |

| # | Grandeur | Ta valeur |
| ---: | --- | ---: |
| 1 | Coefficient sur le PVC affiché | × |
| 2 | Coefficient sur le prix réellement encaissé | × |
| 3 | COGS en % de ton CA HT | % |

Puis ta structure de coût variable **réelle**, pas celle de NØRA :

| Poste | % de ton CA HT | (obs) / (est) |
| --- | ---: | :---: |
| Logistique (préparation, colis, transport, retour physique) | | |
| PSP | | |
| Retours / SAV | | |
| Remises et codes promo | | |
| **Somme** | | |

| # | Grandeur | Ta valeur |
| ---: | --- | ---: |
| 4 | Ta marge brute m | % |
| 5 | Ton MER seuil CM3 = 0 | |
| 6 | Ton MER réel des 90 derniers jours (CA TTC ÷ pub totale) | |
| 7 | Écart entre les deux, en % | % |

> **CORRECTION —** voir [E00-corrige.md](E00-corrige.md) § 3

---

## Exercice 4 — Le capital nécessaire à ta marque (tes chiffres)

Reproduis le tableau du § 5.1 du module avec **tes** nombres.

| Poste | Montant HT | Origine et (obs) / (est) |
| --- | ---: | --- |
| Pertes cumulées jusqu'à ton premier mois d'EBITDA positif | | |
| BFR à ce moment-là (stock + encaissements en attente + avance pub − dettes fournisseurs) | | |
| Lancement hors modèle (formule, moules, packaging, dépôt de marque, site, juridique) | | |
| **Sous-total** | | |
| Marge de sécurité (déclare ton taux) | | |
| **= Capital total à réunir** | | |

**Mon capital de ruine** — le montant que je peux perdre sans que ma vie change,
un seul nombre, pas une fourchette :

_(à remplir)_ €

**Écart entre le capital à réunir et mon capital de ruine :** _(à remplir)_ €

**Ce que je fais de cet écart. Coche une case et une seule, puis écris en trois
lignes comment :**

- ☐ Je le comble (dette, apport, associé, revenus externes)
- ☐ Je réduis l'ambition (palier cible plus bas, croissance plus lente)
- ☐ Je change de moteur d'acquisition (organique, communauté, retail, B2B)

_(à remplir)_

> **CORRECTION —** voir [E00-corrige.md](E00-corrige.md) § 4

---

## Exercice 5 — Décision : ma catégorie autorise-t-elle P5 ?

Deux produits te sont proposés. Hypothèses communes et imposées :

| Hypothèse commune | Valeur |
| --- | ---: |
| Panier moyen | 60,00 € TTC, soit 50,00 € HT |
| TVA | 20 % |
| Coûts variables hors COGS | 23,65 % du CA HT |
| Frais fixes | 10,70 % du CA HT |
| nCAC (coût d'acquisition d'un **nouveau** client) | 35,00 € |

| | **Option A** | **Option B** |
| --- | ---: | ---: |
| Coefficient rendu entrepôt | ×7,2 | ×4,2 |
| Commandes cumulées par client à 12 mois | 1,2 | 3,1 |

Remplis les deux colonnes :

| # | Grandeur | Option A | Option B |
| ---: | --- | ---: | ---: |
| 1 | COGS en % du CA HT | | |
| 2 | Marge brute m | | |
| 3 | Contribution par commande | | |
| 4 | LTV 12 mois en contribution | | |
| 5 | LTV / nCAC | | |
| 6 | MER seuil CM3 = 0 | | |
| 7 | MER seuil EBITDA = 0 | | |
| 8 | MER réellement atteint sur 12 mois (CA TTC du client ÷ nCAC) | | |
| 9 | EBITDA par client sur 12 mois | | |

**(a) Je tranche pour l'option :** ☐ A ☐ B

**(b) La règle canonique que j'invoque, citée textuellement :**

_(à remplir)_

**(c) À quel nCAC l'option perdante deviendrait-elle la bonne ?** _(à remplir)_ €

**(d) Quel canal du plan média délivre ce nCAC, et à quelle condition ?**

_(à remplir)_

**(e) Ce que je conclus sur le seul test « coefficient ≥ ×5 » :**

_(à remplir)_

> **CORRECTION —** voir [E00-corrige.md](E00-corrige.md) § 5

---

## Ma synthèse

Cinq lignes, écrites après avoir rendu et avant d'ouvrir le corrigé.

1. Ce que j'ai appris et que je ne savais pas avant ce module :

2. Le chiffre qui m'a le plus surpris, et pourquoi :

3. La croyance que j'avais et qui vient d'être invalidée :

4. La décision que ça change, concrètement, cette semaine :

5. Ce que je dois mesurer avant de pouvoir trancher pour de bon :

---

*Fin des exercices du module E00. Corrigé : [`E00-corrige.md`](E00-corrige.md).
Suite : [E01 — L'arithmétique de la marque](../modules/E01-arithmetique-de-la-marque.md).*
