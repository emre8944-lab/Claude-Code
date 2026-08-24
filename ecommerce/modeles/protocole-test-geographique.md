# Protocole de test d'incrémentalité géographique

> **À quoi ça sert :** produire une **contrefactuelle réelle** — ce qui se serait passé sans la publicité — en coupant ou en augmentant franchement un bloc de budget sur une zone appariée, puis convertir l'écart en CAC incrémental et en décision d'allocation.
> **Quand l'utiliser :** avant tout arbitrage de plus de 100 000 € annuels sur une ligne média ; avant de croire un ROAS de régie ; avant de calibrer un MMM. Inutilisable sous P3 — tu paieras la coupe pour n'apprendre rien.
> **Module rattaché :** [E09](../modules/E09-mesure-et-incrementalite.md) § 5 et § 6. Compléments : [E10](../modules/E10-cash-et-operations.md) (le coût de trésorerie de la coupe), [C06](../etudes-de-cas/C06-test-incrementalite.md).

---

## 1. Ce que le test mesure, ce qu'il ne mesure pas

| Il mesure | Il ne mesure pas |
|---|---|
| L'effet **causal** d'un bloc de budget sur les commandes d'une zone, **dans sa fenêtre** | L'effet de marque au-delà — six semaines contre quatorze mois de latence ([E12](../modules/E12-marque-et-actif.md)) |
| Un **ordre de grandeur et un signe** | Une décimale : l'intervalle va couramment du simple au triple |
| L'incrémentalité **moyenne** du bloc coupé, ou **marginale** du bloc augmenté | Le budget canal par canal : on coupe un bloc, pas une plateforme dans un empilement |
| Ce qui est **géo-ciblable** dans toutes les régies | Le reste : influence nationale, presse, notoriété acquise |
| Les **nouveaux clients** de la fenêtre | Le réachat qu'ils auraient produit : hors fenêtre, à réintégrer par la LTV (§ 5.4) |

**Une coupe et une augmentation ne répondent pas à la même question.** Couper dit *ce bloc vaut-il son budget* ; augmenter dit *ce que vaut le prochain euro* — seul le second sert à allouer ([E09 § 6.4](../modules/E09-mesure-et-incrementalite.md)).

---

## 2. Les trois conditions préalables — sinon on ne lance pas

**A. Volume et puissance.** La durée dépend du **carré** de l'effet cherché, et pas du tout de la taille de la cellule : le bruit d'une zone est presque entièrement commun — créations, algorithme, météo, actualité — et ne se dilue pas dans le volume. Formule de [E09 § 5.2](../modules/E09-mesure-et-incrementalite.md) ; `CV` le coefficient de variation quotidien désaisonnalisé, `ρ` la corrélation test/témoin en pré-période, `e` l'effet relatif :

```
D ≥ [ 2,80 × CV × √(2 × (1 − ρ)) ÷ e ]²        (5 % bilatéral, 80 % de puissance)
Effet minimum détectable à D jours :  e_min = 2,80 × CV × √(2 × (1 − ρ)) ÷ √D
```

**Si `e_min` dépasse l'effet sur lequel tu agirais, le test est déjà mort : ne le lance pas.** Doubler la cellule ne le sauve pas ; mieux apparier, oui — passer de ρ = 0,70 à ρ = 0,85 divise la durée par deux.

**B. Marchés séparables.** Trois exigences cumulatives : l'unité est ciblable dans **toutes** les régies du plan ; elle est mesurable dans **tes** données de commande — code postal de livraison, jamais l'adresse IP ; les zones ne partagent ni télévision ni influence nationale. Une fuite de ciblage de l'ordre de 8 % est normale et **fait sous-estimer l'effet** : un résultat positif reste valide, un résultat nul reste ambigu.

**C. Période stable.** Pas de lancement produit, pas de vague promotionnelle, pas de Black Friday, pas de rupture prévisible, pas de changement de prix ou de page — ni pendant, ni dans les quatorze jours qui suivent. Une période chargée n'invalide pas le test si elle frappe les deux cellules à l'identique ; elle ne le fait presque jamais.

---

## 3. Formulaire de conception — à remplir et à faire signer AVANT

> Un seuil écrit après le résultat n'est pas un seuil, c'est une justification. Cette page est datée et signée avant le premier jour de coupe. C'est la seule protection contre la lecture *a posteriori*, et c'est là que la plupart des tests d'entreprise échouent.

**A — La question et le geste**

| Champ | À écrire |
|---|---|
| Question exacte, en une phrase | |
| Bloc testé (canal, campagnes, lignes) | |
| Dépense mensuelle du bloc, groupe entier | ……… € HT |
| Geste : **coupe totale** / **coupe partielle** / **augmentation de … %** | |
| Ce qu'il mesure : incrémentalité **moyenne** ou **marginale** | |
| Décision qui en dépend, et son enjeu annuel | ……… € |

**B — Les cellules**

| Champ | Test | Témoin |
|---|---|---|
| Unité géographique (départements, codes postaux) | | |
| Part du volume national | ……… % | ……… % |
| CA TTC quotidien moyen sur 26 semaines | ……… € | ……… € |
| Commandes/jour | | |
| Budget quotidien, dont géo-ciblable | ……… € / ……… € | ……… € / ……… € |
| ρ en pré-période (exigence : ≥ 0,80) — apparié sur ventes/habitant, tendance, mix produit, exposition promo, profil hebdomadaire | | |
| Stabilité du ratio test/témoin (exigence : ±5 %) | | |

**C — Puissance et durée**

| Champ | Valeur |
|---|---|
| CV quotidien désaisonnalisé sur 26 semaines | ……… % |
| ρ retenu | |
| Effet `e` sur lequel on agirait | ……… % |
| Durée `D` | ……… j → multiple de 7 supérieur : ……… j |
| `e_min` à la durée retenue | ……… % |
| **Verdict go / no-go** (`e_min` < `e` attendu ?) | |

**D — Le gel : ce qu'on ne touche dans aucune des deux cellules**

Prix et remises · paliers de livraison gratuite · page produit · séquences CRM et fréquence d'envoi · budget des canaux **non** testés · créations en rotation · zones de livraison · SAV. **Pendant le test et les quatorze jours suivants.** Toute exception est datée au journal ; une exception non notée invalide le test et ne se rattrape par aucun retraitement.

**E — Les seuils de décision, écrits d'avance**

| Si… | Alors, décidé d'avance |
|---|---|
| Borne **basse** de l'IC 95 % du CAC incrémental > LTV finançable | |
| Borne **haute** de l'IC 95 % du CAC incrémental < LTV finançable | |
| L'intervalle contient la LTV finançable | |
| Résultat non significatif (`z` < 1,96) | |
| Le test est cassé (contamination, promo, rupture) | |

*LTV finançable = LTV 12 mois si tu es autofinancé, 24 mois si ton BFR tient la durée ([E10](../modules/E10-cash-et-operations.md)). Écris-la ici : ……… €.*

**F — Signatures.** Conception : ……… Validation budget : ……… Date : ……… **Aucune modification de A à E après cette date.**

---

## 4. Le recueil, jour par jour

Une ligne par jour et par cellule, sur les 26 semaines de pré-période **et** la durée du test. Source unique : ton back-office, par code postal de livraison, hors annulations et hors B2B.

| Jour | Sem. | Phase | Cellule | CA TTC | Cmd | Nouv. cl. | Réachats | Dép. géo-ciblable | Dép. hors géo | Incidents |
|---|---|---|---|---|---|---|---|---|---|---|
| | | pré / test / rebond | test | | | | | | | |
| | | | témoin | | | | | | | |

Trois colonnes que tout le monde oublie : **nouveaux clients et réachats séparés** — l'effet publicitaire porte sur les premiers, un effet sur les seconds signale une contamination CRM ; **dépense hors géo-ciblable** — si elle bouge, ta coupe n'est pas ta coupe ; **incidents** — rupture, panne de paiement, grève transporteur.

---

## 5. La lecture — quatre calculs, dans cet ordre

**5.1 Double différence.** Jamais avant/après, jamais test/témoin seul.

```
ratio_pré       = CA test (pré) ÷ CA témoin (pré)
contrefactuelle = ratio_pré × CA témoin (pendant)
effet           = CA test (pendant) − contrefactuelle
lift            = effet ÷ contrefactuelle
```

**5.2 L'incertitude, avant tout commentaire.**

```
μ      = contrefactuelle ÷ D                            (CA quotidien moyen)
σ      = CV × μ × √(2 × (1 − ρ)) × √D
z      = |effet| ÷ σ            IC 95 % = effet ± 1,96 × σ
```

**5.3 Le CAC incrémental — aux bornes, pas seulement au point.**

```
clients incrémentaux = effet ÷ AOV de la 1ʳᵉ commande TTC
CAC incrémental      = dépense en jeu ÷ clients incrémentaux
ROAS incrémental     = effet ÷ dépense en jeu
```

Le ROAS incrémental se compare au **MER seuil de contribution** de ton palier, `(1 + TVA) ÷ marge brute`, et à rien d'autre ([E09 § 6.3](../modules/E09-mesure-et-incrementalite.md)). Calcule le CAC aux **deux bornes** : si la décision y est la même, elle est solide malgré l'imprécision.

**5.4 La conversion en décision.** Comparer le CA perdu à la dépense épargnée est l'erreur la plus chère du métier : les clients non acquis ne repasseront pas commande non plus, et ces réachats sont **hors fenêtre**. Sur une coupe, `solde = clients incrémentaux × LTV finançable − dépense épargnée`.

---

## 6. Exemple entièrement rempli — NØRA, palier P4

> *Bloc d'hypothèses.* Répartition P4 : FR 46 % du CA et du budget ; cellule test = 25 % du volume France ; budget géo-ciblable 82 % ; CV quotidien désaisonnalisé 28 %. Les données du test sont modélisées ; les canoniques mobilisées sont le § 2 (CA 2 931 600 € TTC/mois, pub 1 047 000 €/mois, AOV 69,80 €), le § 2.1 (marge brute 60,4 %), le § 2.4 (nCAC 37,77 €, contribution 1ʳᵉ commande 31,71 €) et le § 3.1 (LTV/CAC 24 mois de 3,03, soit **3,03 × 37,77 = 114,44 €** de LTV en contribution).

**A — Question et geste.** *« Le prochain euro de prospection payante achète-t-il un client à moins que sa LTV à 24 mois ? »* Bloc : tout le budget géo-ciblable de prospection, toutes régies, soit `0,82 × 1 047 000 = 858 540 €` HT/mois. Geste : **augmentation de 80 %** dans la cellule test — donc la **marginale**. Enjeu : l'écart au budget d'optimum, chiffré à 847 872 €/an en [E09 § 6.4](../modules/E09-mesure-et-incrementalite.md).

**B — Cellules.**

```
CA France       = 0,46 × 2 931 600 = 1 348 536 € TTC/mois
Cellule test    = 0,25 × 1 348 536 =   337 134 € TTC/mois = 11 083 €/jour
                                                          = 159 commandes/jour
Budget cellule  = 0,25 × 0,46 × 1 047 000 = 120 405 €/mois = 3 958 €/jour
    dont géo-ciblable  = 0,82 × 3 958 = 3 245,60 €/jour     (E09 § 5.3 ✓)
Augmentation +80 %     = +2 596,50 €/jour  →  6 554,50 €/jour pendant le test
```

Test : 21 départements du quart nord-ouest. Témoin : 23 départements appariés sur ventes par habitant, tendance, mix produit, exposition promo et profil hebdomadaire. **ρ = 0,85** après deux itérations, contre 0,70 au premier jet ; ratio stable à ±3,2 % sur 26 semaines.

**C — Puissance.**

```
k = 2,80 × 0,28 × √(2 × 0,15) = 0,784 × 0,547723 = 0,4294
Pour e = 8 % :  D ≥ (0,4294 ÷ 0,08)² = 28,8 j  →  35 jours (5 semaines)
e_min à 35 j  =  0,4294 ÷ √35 = 7,26 %
À ρ = 0,70, la même détection aurait demandé (0,6073 ÷ 0,08)² = 58 j → 63 jours.
```

**Les deux itérations d'appariement ont fait gagner quatre semaines.** Go : `e_min` 7,26 % < 8 % attendu.

**E — Seuils, signés le 2 mars.** LTV finançable = **114,44 €** (24 mois ; le BFR de 1 392 510 € tient la durée, canonique § 4). Borne basse du CAC incrémental > 114,44 € → **on redescend le budget vers l'optimum**. Borne haute < 114,44 € → **on augmente durablement de 80 %**. Intervalle contenant 114,44 € → relance sur 63 jours avec la cellule symétrique. `z` < 1,96 → **non conclusif, on ne réaugmente pas** : l'absence de preuve d'un gain n'est pas une preuve de gain.

**Résultat**, 35 jours, du 9 mars au 12 avril.

| Cellule | Pré-période (35 j appariés) | Pendant (35 j) |
|---|---:|---:|
| Test | 388 400 € TTC | 415 770 € TTC |
| Témoin | 396 100 € TTC | 402 800 € TTC |

```
ratio_pré       = 388 400 ÷ 396 100 = 0,98056
contrefactuelle = 0,98056 × 402 800 = 394 970 € TTC
effet           = 415 770 − 394 970 = +20 800 € TTC,  soit +5,27 %

μ = 394 970 ÷ 35 = 11 285 €
σ = 0,28 × 11 285 × 0,547723 × √35 = 1 731 × 5,9161 = 10 239 €
z = 20 800 ÷ 10 239 = 2,03
IC 95 % = 20 800 ± 20 068 = [732 € ; 40 868 €], soit [0,19 % ; 10,35 %]
```

**Lis l'intervalle avant le z.** L'effet observé (5,27 %) est **sous** l'effet minimum détectable (7,26 %) et franchit pourtant tout juste le seuil : c'est ce que veut dire « 80 % de puissance ». L'intervalle va de rien à 10 %.

```
Dépense supplémentaire = 2 596,50 × 35 = 90 878 €
ROAS incrémental marginal = 20 800 ÷ 90 878 = 0,23
MER seuil de contribution P4 = 1,20 ÷ 0,604 = 1,99      (canonique § 2.3 ✓)

AOV 1ʳᵉ commande P4 = 31,71 ÷ 0,604 = 52,50 € HT = 63,00 € TTC
                        clients incrémentaux    CAC incrémental marginal
   point       20 800 € →        330                    275,25 €
   borne haute 40 868 € →        649                    140,09 €
   borne basse    732 € →         12                  7 821,65 €
```

**Décision, sans discussion possible :** même à la **borne la plus favorable**, le client marginal coûte 140,09 € et vaut 114,44 € à 24 mois. Le seuil E s'applique. Contrôle : [E09 § 6.4](../modules/E09-mesure-et-incrementalite.md) donne 219,83 € de CAC marginal pour +14,6 % de budget ; on mesure 275,25 € pour +80 %, donc plus haut sur une courbe décroissante. ✓

```
Extrapolation au groupe : +80 % = +686 832 €/mois de dépense
Clients incrémentaux     = 686 832 ÷ 275,25 = 2 495/mois
Destruction par client   = 275,25 − 114,44 = 160,81 €
Destruction totale       = 2 495 × 160,81 = 401 221 €/mois = 4 814 652 €/an
```

**Un test à 90 878 € vient d'interdire une décision qui aurait coûté 4,8 M€ par an.**

---

## 7. Les trois pièges

**La saisonnalité.** Elle ne se corrige pas, elle s'annule — à condition de frapper les deux cellules à l'identique. Deux protections : un `CV` calculé **après** neutralisation du jour de la semaine, et un ratio stable à ±5 % sur 26 semaines. Un test qui chevauche une fête locale ou un férié régional n'est pas dégradé : il est faux.

**La contamination entre zones.** Elle va toujours dans le même sens : elle **rapproche** les cellules et **rabote** l'effet. Par ordre de gravité : audiences similaires bâties sur des acheteurs de la cellule coupée ; reciblage national qui continue de la servir ; influence non géo-ciblable ; code créateur utilisé partout. Gèle les similaires trente jours avant, sors la cellule du reciblage, et si l'influence n'est pas isolable, exclus-la du bloc testé — et écris-le au champ A.

**Les effets de report.** Une coupe ne détruit pas les ventes, elle en **décale** une partie : à la remise du budget, la cellule rattrape, et sans les quatorze jours de rebond au recueil ce rattrapage se compte comme une incrémentalité permanente. Symétriquement, une augmentation **avance** des achats qui venaient : d'où la séparation nouveaux clients / réachats, et d'où le fait qu'aucun test de moins de 90 jours ne tranche sur le réachat de NØRA — cycle de 31 à 93 jours ([E08](../modules/E08-retention-et-ltv.md)).

---

# Les erreurs qu'on voit tout le temps

1. **Lancer sans calculer la puissance.** Sur la cellule du § 6, un test de 14 jours ne détecte rien sous 11,5 % : un vrai effet de 8 % ressort « non significatif », quelqu'un lit « la publicité ne sert à rien », le budget saute. Le no-go du champ C est la ligne la plus rentable.
2. **Couper 20 % « pour ne pas risquer gros ».** La durée varie comme l'inverse du carré de l'effet : une coupe de 30 % au lieu de 100 % demande **neuf fois** plus de temps — 37 jours deviennent 333. On coupe franchement, ou on ne coupe pas.
3. **Écrire les seuils après le résultat.** Le seul verrou est la signature datée du champ F : sans elle, le test ne produit pas une décision mais un argument pour celle qui était déjà prise. Corollaire, le champ D se diffuse à toute l'entreprise et pas au seul service média — une promotion lancée en cellule témoin par une équipe non prévenue coûte cinq semaines de coupe.
4. **Rapporter le CA perdu à la dépense épargnée.** La façon la plus fréquente de couper un budget rentable : sur [E09 § 5.3](../modules/E09-mesure-et-incrementalite.md), la lecture naïve donne un MER incrémental de 0,73 contre un seuil de 1,99 ; la lecture en LTV 24 mois donne **+45 530 € en faveur du maintien**. Même test, décision inverse.
5. **Confondre significatif et précis.** `z` = 6,28 avec un intervalle de 14,5 % à 27,6 % reste un intervalle qui va du simple au double.
*Rattaché à [E09](../modules/E09-mesure-et-incrementalite.md). Voir [protocole-test-creatif.md](protocole-test-creatif.md) : il compare des concepts entre eux et ne mesure aucune incrémentalité — c'est normal.*
