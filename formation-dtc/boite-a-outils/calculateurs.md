# Calculateurs — toutes les formules du cursus

> Prêtes à recopier dans un tableur. Les exemples chiffrés sont ceux de Nilo, pour que
> tu puisses vérifier ton tableur en retrouvant les mêmes résultats.

---

## 1. Le P&L d'une commande (module 01)

Mets les entrées dans une colonne, par exemple :

| Cellule | Entrée | Exemple Nilo (fontaine seule) |
|---|---|---|
| B2 | Prix TTC | 59,00 |
| B3 | Taux de TVA | 20 % |
| B4 | Coût produit rendu | 11,00 |
| B5 | Emballage | 0,70 |
| B6 | Préparation (3PL) | 2,20 |
| B7 | Transport | 5,30 |
| B8 | Frais de paiement : % | 1,8 % |
| B9 | Frais de paiement : fixe | 0,25 |
| B10 | Provision retours / SAV (% du HT) | 4 % |

Puis les calculs :

| Cellule | Calcul | Formule | Résultat Nilo |
|---|---|---|---|
| B12 | CA HT | `=B2/(1+B3)` | 49,17 |
| B13 | CM1 | `=B12-B4` | 38,17 |
| B14 | Frais de paiement | `=B2*B8+B9` | 1,31 |
| B15 | Provision | `=B12*B10` | 1,97 |
| B16 | **CM2** | `=B13-B5-B6-B7-B14-B15` | **26,69** |
| B17 | CM2 en % du HT | `=B16/B12` | 54,3 % |

---

## 2. Les seuils (module 01)

```
CPA d'équilibre          = CM2
ROAS d'équilibre (HT)    = CA HT ÷ CM2
ROAS d'équilibre (TTC)   = Prix TTC ÷ CM2
CM3 cible                = CA HT × % de CM3 visé (repère : 15 %)
CPA cible                = CM2 − CM3 cible
ROAS cible (TTC)         = Prix TTC ÷ CPA cible
```

Nilo (panier moyen 74,50 € TTC, CM2 35,79 €) : CPA d'équilibre 35,79 € ; ROAS
d'équilibre TTC 2,08 ; CPA cible 26,48 € ; ROAS cible TTC 2,81.

---

## 3. L'entonnoir publicitaire (modules 00, 01)

```
CPC  = CPM ÷ (1 000 × CTR)
CPA  = CPM ÷ (1 000 × CTR × CR)
ROAS = Panier moyen × 1 000 × CTR × CR ÷ CPM
```

**Les formules inversées** (ce qu'il te faut pour atteindre ta cible) :

```
Taux de conversion nécessaire = CPM ÷ (1 000 × CTR × CPA cible)
CTR nécessaire                = CPM ÷ (1 000 × CR × CPA cible)
CPM maximum supportable       = CPA cible × 1 000 × CTR × CR
```

Nilo : CPM 9 €, CTR 1,3 %, CPA cible 26,48 € → conversion nécessaire =
9 ÷ (1 000 × 0,013 × 26,48) = **2,61 %**.

---

## 4. Le pilotage (modules 01, 09)

```
MER                    = CA total TTC ÷ Dépense marketing totale
MER d'équilibre (TTC)  = (1 + TVA) ÷ CM2 en % du HT          → CM3 = 0
MER pour EBITDA = 0    = CA TTC ÷ (CM2 totale − frais fixes)
nCAC                   = Dépense d'acquisition ÷ Nouveaux clients
nc-ROAS                = CA des nouveaux clients ÷ Dépense d'acquisition
CM3 estimée du jour    = CA HT × CM2 % − Dépense marketing du jour
```

---

## 5. Le CPA marginal (module 09)

```
CPA marginal = (Dépense palier 2 − Dépense palier 1) ÷ (Achats palier 2 − Achats palier 1)
CM3 marginale par commande = CM2 − CPA marginal
```

Nilo : de 1 000 €/j (40 achats) à 1 300 €/j (49 achats) → CPA marginal = 300 ÷ 9 =
33,33 € ; CM3 marginale = 35,79 − 33,33 = 2,46 €.

**Règle :** tu arrêtes d'augmenter le budget quand la CM3 marginale approche de zéro.

---

## 6. LTV et payback (modules 01, 11, 14)

**Transactionnel :**
```
LTV 12 mois = CM2 1re commande + Σ (part de clients qui rachètent × nb de réachats × CM2 du réachat) − coût de rétention
```

**Abonnement (par la courbe de rétention) :**
```
LTV 12 mois = CM2 1re commande + CM2 d'un renouvellement × Σ (% d'actifs au mois m, pour m = 1 à 12)
```

**Abonnement (approximation par l'attrition constante) :**
```
LTV = (Revenu mensuel × taux de CM2) ÷ attrition mensuelle
```

**Payback :**
```
Payback = premier mois où la CM2 cumulée par client ≥ CAC
Trésorerie immobilisée ≈ Σ (CAC − CM2 cumulée) sur les cohortes pas encore remboursées
```

---

## 7. Promotions et garanties (module 06)

**Effet d'une remise :**
```
Remise HT         = Panier moyen TTC × % de remise ÷ (1 + TVA)
CM2 après remise  ≈ CM2 − Remise HT (+ petites économies de frais et de provision)
CPA nécessaire pour garder la même CM3 = CM2 après remise − CM3 actuelle par commande
Baisse de CPA nécessaire = 1 − (CPA nécessaire ÷ CPA actuel)
```

**Seuil de rentabilité d'une garantie commerciale :**
```
r = hausse du taux de remboursement (en part des commandes)
L = perte par remboursement (≈ CA HT de la commande)
Hausse de conversion minimale = CM2 ÷ (CM2 − r × L) − 1
```
Nilo : 35,79 ÷ (35,79 − 0,02 × 62) − 1 = **+3,6 %**. Au-delà, la garantie est
rentable.

**Seuil de livraison offerte (repère) :**
```
Seuil ≈ Panier moyen actuel × 1,15 à 1,30
```

---

## 8. Le stock (modules 01, 04)

```
Délai total        = production + transport + dédouanement + réception (jours)
Stock de sécurité  = Ventes par jour × jours de sécurité (15 à 30)
Point de commande  = Ventes par jour × Délai total + Stock de sécurité
Quantité à commander = Ventes prévues sur la période de couverture (avec la croissance)
Trésorerie de la commande = Quantité × Coût rendu
Stock à financer (ordre de grandeur) = Coût produit mensuel × 3,5
```

**Ventes prévues avec croissance mensuelle g :**
```
Ventes par jour dans n mois = Ventes par jour aujourd'hui × (1 + g)^n
```

Nilo : 150/jour, délai 60 jours, sécurité 20 jours → point de commande = 150 × 60 +
3 000 = **12 000 unités**. À +20 % par mois : dans 2 mois, 150 × 1,2² = 216 par jour.

---

## 9. Les statistiques utiles (modules 03, 07)

**Fourchette plausible (95 %) du « vrai » nombre d'achats** autour d'un nombre observé
*k* (approximation, valable à partir de k ≈ 10) :

```
k ± 2 × √k
```
Exemple : 20 achats → environ 11 à 29. (La table exacte du module 03 donne 12,2 à 30,9.)

**Taille d'échantillon d'un test A/B** (puissance 80 %, seuil 5 %) :
```
Visiteurs par variante ≈ 16 × p × (1 − p) ÷ δ²
p = taux de conversion actuel ; δ = écart absolu à détecter
```

---

## 10. L'influence (module 10)

```
Vues attendues            = moyenne des vues des 10 dernières publications (pas les abonnés)
Coût pour 1 000 vues      = Prix demandé ÷ Vues attendues × 1 000
À comparer à              = ton CPM publicitaire (+ la valeur de la vidéo réutilisable en pub)
```

---

## 11. La trésorerie à 13 semaines (module 12)

Une ligne par semaine, pour les 13 prochaines :

```
Trésorerie de fin de semaine = Trésorerie de début
  + Encaissements (ventes TTC encaissées, financements reçus)
  − Pub et marketing
  − Fournisseurs (acomptes et soldes aux dates prévues)
  − Logistique et transport
  − Salaires et freelances
  − Outils et frais fixes
  − TVA à reverser (aux dates d'échéance)
  − Remboursements de financements
```

**Alerte :** le point le plus bas des 13 semaines doit rester au-dessus de 6 semaines de
dépenses courantes. Sinon : ralentir, négocier, ou financer — **avant** d'y arriver.
