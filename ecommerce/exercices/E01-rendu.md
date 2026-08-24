# Exercices — Module E01 : L'arithmétique de la marque

> **Avant de commencer :** rappel des règles — tout chiffre est marqué (obs) ou
> (est) ; tout montant est marqué TTC ou HT ; les seuils s'écrivent avant le test.
> **Ne lis pas le corrigé avant d'avoir rendu.**

Module source : [`E01-arithmetique-de-la-marque.md`](../modules/E01-arithmetique-de-la-marque.md).
Données : [chiffres canoniques](../donnees/chiffres-canoniques.md). Fais les
calculs à la main. Deux décimales partout, virgule décimale, TVA 20 %.

Les quatre formules du module, à recopier en haut de ta copie :

```
Part de la pub en % du CA HT = (1 + TVA) ÷ MER
MER seuil (CM3 = 0)          = (1 + TVA) ÷ m
MER seuil (EBITDA = 0)       = (1 + TVA) ÷ (m − f)
Point mort en commandes/mois = frais fixes ÷ CM3 par commande
                               (m = marge brute % du CA HT ; f = frais fixes ÷ CA HT)
```

---

## Exercice 1 — Recalcule les deux MER seuils de P3 (données NØRA)

Données autorisées, et elles seules : les cinq postes de coût variable du palier
P3, ses frais fixes, son CA HT, la TVA. Les voici :

| Grandeur, palier P3 | Valeur |
| --- | ---: |
| COGS | 16,00 % du CA HT |
| Logistique | 12,00 % du CA HT |
| PSP | 1,65 % du CA HT |
| Retours / SAV | 3,00 % du CA HT |
| Remises | 7,00 % du CA HT |
| CA HT mensuel | 981 000 € |
| Frais fixes mensuels | 105 000 € |
| MER réel | 2,70 |

| # | Grandeur | Ta valeur |
| ---: | --- | ---: |
| 1 | Taux de marge brute m, deux décimales | % |
| 2 | MER seuil de contribution (CM3 = 0) | |
| 3 | Frais fixes f en % du CA HT | % |
| 4 | MER seuil d'EBITDA | |
| 5 | Marge de sécurité du MER réel de 2,70 contre le seuil d'EBITDA | % |
| 6 | Baisse de marge brute, **en points**, que le MER de 2,70 supporte encore avant que l'équilibre d'EBITDA ne soit perdu | pts |
| 7 | La même baisse, convertie en euros d'EBITDA mensuel | € |

*Contrôle imposé : tu dois retrouver 1,99 et 2,42 exactement (chiffres canoniques
§ 2.3). Si tu ne les retrouves pas, ne continue pas : cherche l'erreur.*

**Ce que la ligne 7 vaut au juste — une phrase :**

_(à remplir)_

> **CORRECTION —** voir [E01-corrige.md](E01-corrige.md) § 1

---

## Exercice 2 — L'EBITDA de P5 si le taux de retour passe de 3,5 % à 5,5 %

Tout le reste est inchangé : même chiffre d'affaires, même dépense publicitaire,
mêmes frais fixes, même mix.

| Grandeur, palier P5 | Valeur |
| --- | ---: |
| CA HT mensuel | 3 610 997 € |
| Marge brute actuelle | 61,45 % |
| Dépense publicitaire mensuelle | 1 494 206 € |
| Frais fixes mensuels | 360 000 € |
| Ligne retours / SAV actuelle | 3,50 % du CA HT |
| MER réel | 2,90 |

| # | Grandeur | Ta valeur |
| ---: | --- | ---: |
| 1 | Nouveau taux de marge brute | % |
| 2 | Nouvelle marge brute mensuelle | € |
| 3 | Nouveau CM3 mensuel | € |
| 4 | Nouvel EBITDA mensuel, et en % du CA HT | € / % |
| 5 | Perte d'EBITDA annuelle | € |
| 5 bis | La même, par la voie courte `CA HT × 2 points × 12` | € |
| 6 | Nouveau MER seuil d'EBITDA, et marge de sécurité restante contre 2,90 | / % |
| 7 | Taux de retour auquel l'EBITDA de P5 devient nul | % |

*Contrôle imposé : la perte annuelle doit être proche de 866 640 €, et la marge de
sécurité doit tomber sous 20 %.*

**Ce que tu changes dans ton tableau de bord après cet exercice :**

_(à remplir)_

> **CORRECTION —** voir [E01-corrige.md](E01-corrige.md) § 2

---

## Exercice 3 — Ta cascade des marges (tes chiffres)

Sur tes **90 derniers jours**. Une ligne vide est une réponse fausse ; une ligne
à zéro assumée est une réponse.

| Étage | Montant | % du CA HT | (obs) / (est) |
| --- | ---: | ---: | :---: |
| CA TTC | € | 120,00 % | |
| − TVA collectée | € | −20,00 % | |
| **= CA HT** | € | **100,00 %** | |
| − COGS rendu entrepôt | € | % | |
| **= CM1** | € | % | |
| − Logistique (préparation, colis, transport, retour physique) | € | % | |
| − PSP | € | % | |
| − Retours / SAV, **comptés par cohorte de commandes** | € | % | |
| − Remises, codes promo, codes créateurs | € | % | |
| **= CM2, marge brute** | € | % | |
| − Publicité : média | € | % | |
| − Publicité : production créative | € | % | |
| − Publicité : honoraires d'agence et freelances | € | % | |
| **= CM3** | € | % | |
| − Frais fixes | € | % | |
| **= EBITDA** | € | % | |

**Nombre de commandes sur la période :** _(à remplir)_

**Ma ligne « remises » est-elle sortie d'un rapport, ou reconstituée à la main ?**

_(à remplir)_

**Le responsable nommé de ma ligne CM2, et celui de ma ligne CM3 :**

_(à remplir)_

> **CORRECTION —** voir [E01-corrige.md](E01-corrige.md) § 3

---

## Exercice 4 — Ton tableau de sensibilité (tes chiffres)

Reproduis les sept leviers du canonique § 7 avec **tes** nombres. Traite chaque
poste selon sa nature réelle : proportionnel au CA, ou **fixe par commande**
(c'est le cas de la logistique — c'est toute la différence entre les deux
premières lignes).

| Levier | Gain d'EBITDA annuel | En % de mon EBITDA | Heures de direction consommées le mois dernier |
| --- | ---: | ---: | ---: |
| +10 % de panier moyen (à commandes constantes) | | | |
| +10 % de taux de conversion (à budget pub constant) | | | |
| −10 % de CAC à volume constant | | | |
| +10 % de commandes de réachat | | | |
| −10 % de COGS | | | |
| −1 point de taux de retour / SAV | | | |
| −10 % de frais fixes | | | |
| **Total** | | **100 %** | |

**Mon levier n° 1 :** _(à remplir)_

**Le levier sur lequel j'ai passé le plus d'heures :** _(à remplir)_

**Rapport entre sa part de gains et sa part d'heures :** ×_(à remplir)_

> **CORRECTION —** voir [E01-corrige.md](E01-corrige.md) § 4

---

## Exercice 5 — Tes deux seuils et ton point mort (tes chiffres)

| # | Grandeur | Ta valeur |
| ---: | --- | ---: |
| 1 | Ton MER seuil de contribution `(1 + TVA) ÷ m` | |
| 2 | Ton MER seuil d'EBITDA `(1 + TVA) ÷ (m − f)` | |
| 2 bis | **Le niveau de CA HT mensuel auquel ce seuil est valable** | € |
| 3 | Marge brute par commande | € |
| 4 | Dépense publicitaire par commande | € |
| 5 | **CM3 par commande** | € |
| 6 | Point mort en commandes par mois | |
| 7 | Point mort en commandes par jour (÷ 30,33) | |
| 8 | Commandes par jour réellement réalisées | |
| 9 | Marge de sécurité en volume | % |

**Le post-it collé à mon écran. Trois nombres, rien d'autre :**

```
Point mort           : ............ commandes / jour
MER seuil d'EBITDA   : ............
MER des 7 derniers j : ............
```

> **CORRECTION —** voir [E01-corrige.md](E01-corrige.md) § 5

---

## Exercice 6 — Décision : la tranche de budget supplémentaire

Ta marque ressemble à NØRA au palier P5.

| Donnée | Valeur |
| --- | ---: |
| LTV 12 mois en contribution | 86,75 € |
| LTV en contribution à 3 mois / 6 mois | 47,57 € / 64,11 € |
| Payback moyen | 1,8 mois |
| MER blended | 2,90 |
| MER seuil d'EBITDA | 2,33 |
| Contribution de la 1ʳᵉ commande | 32,77 € |
| Panier moyen de la 1ʳᵉ commande | 64,00 € TTC |
| Trésorerie disponible | 400 000 € |
| BFR immobilisé par +100 000 € de CA mensuel | 52 263 € |

Ton directeur de l'acquisition propose **100 000 € de budget mensuel
supplémentaire** sur un nouveau canal. Son test sur trois semaines a produit
**1 266 nouveaux clients pour 100 000 €.**

- **Option A —** valider la tranche.
- **Option B —** refuser et réallouer sur les canaux existants.

| # | Grandeur | Ta valeur |
| ---: | --- | ---: |
| 1 | CAC marginal de la tranche | € |
| 2 | Résultat de la tranche sur 12 mois | € |
| 3 | Rendement de la tranche sur 12 mois, en % des 100 000 € | % |
| 4 | Payback marginal, par interpolation sur la courbe de LTV | mois |
| 5 | Avance de trésorerie média `dépense mensuelle × payback` | € |
| 6 | CA TTC mensuel supplémentaire, et BFR qu'il immobilise | € / € |
| 7 | **Besoin de trésorerie total** contre les 400 000 € disponibles | € / × |
| 8 | LTV en dessous de laquelle la tranche détruit de la valeur | € |
| 9 | Marge d'erreur restante sur la LTV, en % | % |

**Je tranche pour l'option :** ☐ A ☐ B

**Ma justification, en cinq lignes maximum, qui doit contenir le résultat à
12 mois, le payback marginal et le besoin de trésorerie :**

_(à remplir)_

**La condition exacte sous laquelle je changerais d'avis :**

_(à remplir)_

> **CORRECTION —** voir [E01-corrige.md](E01-corrige.md) § 6

---

## Ma synthèse

Cinq lignes, écrites après avoir rendu et avant d'ouvrir le corrigé.

1. Ce que j'ai appris et que je ne savais pas avant ce module :

2. Le chiffre qui m'a le plus surpris, et pourquoi :

3. L'indicateur que je calculais faux, et de combien :

4. La décision que ça change, concrètement, cette semaine :

5. Ce que je dois mesurer avant de pouvoir trancher pour de bon :

---

*Fin des exercices du module E01. Corrigé : [`E01-corrige.md`](E01-corrige.md).
Suite : [E02 — Choisir le terrain](../modules/E02-marche-et-produit.md).*
