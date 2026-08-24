# Chiffres canoniques du cursus — marque fil rouge NØRA

> **Fichier généré.** Ne le modifie pas à la main : il est produit par
> `ecommerce/outils/modele_nora.py`. Change les hypothèses dans le script,
> relance-le, et tout le cursus reste cohérent.
>
> **NØRA est une marque fictive.** Le modèle est calibré sur des ordres de
> grandeur sectoriels publics (marges, MER, courbes de réachat d'une
> catégorie consommable premium). Ce ne sont les comptes réels d'aucune
> entreprise, et aucun chiffre ici ne doit être présenté comme tel.

Hypothèse fiscale : TVA moyenne pondérée **20 %** sur tous les marchés.
Tout ce qui est « TTC » est un prix client ; tout ce qui est « HT » est du
chiffre d'affaires comptable. **Les confondre est l'erreur n° 1 du métier.**

---

## 1. La gamme et ses marges marchandise

| Produit | PVC TTC | PVC HT | COGS | Marge marchandise | Taux | Coef. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Sérum Densité 50 ml (héros) | 39,00 € | 32,50 € | 4,80 € | 27,70 € | 85,2 % | ×8,1 |
| Shampooing Fortifiant 250 ml | 24,00 € | 20,00 € | 3,10 € | 16,90 € | 84,5 % | ×7,7 |
| Masque Réparateur 200 ml | 29,00 € | 24,17 € | 3,60 € | 20,57 € | 85,1 % | ×8,1 |
| Rituel Complet (les 3) | 74,00 € | 61,67 € | 11,50 € | 50,17 € | 81,4 % | ×6,4 |
| Cure 3 mois (3 serums) | 99,00 € | 82,50 € | 14,40 € | 68,10 € | 82,5 % | ×6,9 |

> **Lecture.** Le coefficient (PVC TTC ÷ COGS) est le réflexe métier : sous
> **×5**, une marque DTC qui achète son trafic ne survit pas à l'échelle. NØRA
> est entre ×6,4 et ×8,1 : c'est le minimum vital, pas un luxe. Le module E01
> démontre pourquoi.

---

## 2. Les cinq paliers — du premier euro à 1 M€/semaine

| Palier | Mois | Marchés | Cmd/mois | AOV mixte | CA TTC/mois | CA TTC/sem. |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| **P1 — Validation** | M1 – M3 | France | 800 | 46,00 € | 36 800 € | 8 492 € |
| **P2 — Traction** | M4 – M9 | France | 4 000 | 57,55 € | 230 200 € | 53 123 € |
| **P3 — Scale France** | M10 – M18 | France + Belgique | 18 000 | 65,40 € | 1 177 200 € | 271 662 € |
| **P4 — Multi-pays** | M19 – M30 | FR, BE, DE, ES, IT | 42 000 | 69,80 € | 2 931 600 € | 676 523 € |
| **P5 — 1 M€ / semaine** | M31 – M40 | FR, BE, DE, ES, IT, NL, UK | 60 200 | 71,98 € | 4 333 196 € | 999 968 € |

### 2.1 Structure de coût variable (en % du CA HT)

| Palier | COGS | Logistique | PSP | Retours/SAV | Remises | **Marge brute (CM2)** |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| P1 | 20,0 % | 16,0 % | 1,80 % | 2,0 % | 3,0 % | **57,2 %** |
| P2 | 18,0 % | 14,0 % | 1,70 % | 2,5 % | 5,0 % | **58,8 %** |
| P3 | 16,0 % | 12,0 % | 1,65 % | 3,0 % | 7,0 % | **60,3 %** |
| P4 | 15,0 % | 11,5 % | 1,60 % | 3,5 % | 8,0 % | **60,4 %** |
| P5 | 14,5 % | 11,0 % | 1,55 % | 3,5 % | 8,0 % | **61,5 %** |

> Les remises montent avec l'échelle (Black Friday, codes créateurs, paniers
> abandonnés). Les retours aussi : plus le trafic est large, moins il est
> qualifié. **La marge brute ne s'améliore pas mécaniquement en grandissant.**
> Elle s'améliore parce qu'on négocie le COGS et la logistique plus vite que
> les remises et les retours ne se dégradent.

### 2.2 Compte de résultat mensuel

| Palier | CA HT | Marge brute | Pub | Pub % HT | **CM3** | Fixes | **EBITDA** | % CA HT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| P1 | 30 667 € | 17 541 € | 20 444 € | 66,7 % | **−2 903 €** | 6 500 € | **−9 403 €** | -30,7 % |
| P2 | 191 833 € | 112 798 € | 104 636 € | 54,5 % | **8 162 €** | 28 000 € | **−19 838 €** | -10,3 % |
| P3 | 981 000 € | 592 033 € | 436 000 € | 44,4 % | **156 033 €** | 105 000 € | **51 033 €** | 5,2 % |
| P4 | 2 443 000 € | 1 475 572 € | 1 047 000 € | 42,9 % | **428 572 €** | 230 000 € | **198 572 €** | 8,1 % |
| P5 | 3 610 997 € | 2 218 957 € | 1 494 206 € | 41,4 % | **724 752 €** | 360 000 € | **364 752 €** | 10,1 % |

> **Le piège du MER.** Le MER se calcule sur le CA **TTC**, la marge sur le CA
> **HT**. Un MER de 2,90 ne veut pas dire « la pub coûte 34,5 % du CA » : elle
> coûte **1,20 ÷ 2,90 = 41,4 % du CA HT**. Beaucoup de marques se croient
> rentables de 7 points parce qu'elles n'ont jamais fait cette division.

### 2.3 Seuils de MER

| Palier | MER réel | MER seuil (CM3 = 0) | MER seuil (EBITDA = 0) | Écart au seuil EBITDA |
| --- | ---: | ---: | ---: | ---: |
| P1 | 1,80 | 2,10 | 3,33 | -46,0 % |
| P2 | 2,20 | 2,04 | 2,71 | -19,0 % |
| P3 | 2,70 | 1,99 | 2,42 | 11,7 % |
| P4 | 2,80 | 1,99 | 2,35 | 19,0 % |
| P5 | 2,90 | 1,95 | 2,33 | 24,4 % |

> **C'est le tableau le plus important du cursus.** Le MER seuil est la ligne
> de flottaison : en dessous, chaque euro de CA supplémentaire te fait perdre
> de l'argent. Aux paliers P1 et P2, NØRA est **sous** son MER d'équilibre
> EBITDA : la marque perd de l'argent volontairement pour constituer une base
> de clients. C'est un pari sur le réachat, pas une erreur — mais c'en devient
> une si le réachat ne vient pas. Voir E08.

### 2.4 Acquisition — ce que coûte un client et ce qu'il rapporte

| Palier | Nouveaux clients/mois | nCAC | Contribution 1ʳᵉ cmd | Marge à la 1ʳᵉ cmd | Verdict |
| --- | ---: | ---: | ---: | ---: | --- |
| P1 | 768 | 26,62 € | 21,69 € | −4,93 € | financé par le réachat |
| P2 | 3 400 | 30,78 € | 26,95 € | −3,83 € | financé par le réachat |
| P3 | 13 140 | 33,18 € | 30,17 € | −3,01 € | financé par le réachat |
| P4 | 27 720 | 37,77 € | 31,71 € | −6,06 € | financé par le réachat |
| P5 | 37 324 | 40,03 € | 32,77 € | −7,26 € | financé par le réachat |

### 2.5 Productivité et structure

| Palier | ETP | Frais fixes/mois | % CA HT | CA HT annuel par ETP |
| --- | ---: | ---: | ---: | ---: |
| P1 | 1,5 | 6 500 € | 21,2 % | 245 333 € |
| P2 | 4 | 28 000 € | 14,6 % | 575 500 € |
| P3 | 12 | 105 000 € | 10,7 % | 981 000 € |
| P4 | 25 | 230 000 € | 9,4 % | 1 172 640 € |
| P5 | 38 | 360 000 € | 10,0 % | 1 140 315 € |

---

## 3. Cohortes et LTV (palier P5)

Base : nCAC = **40,03 €**, contribution 1ʳᵉ commande = **32,77 €**, contribution par réachat = **43,53 €**.

| Horizon | Cmd. cumulées / client | CA cumulé TTC | LTV en contribution | LTV / CAC |
| --- | ---: | ---: | ---: | ---: |
| 1 mois | 1,06 | 69,10 € | 35,38 € | 0,88 |
| 3 mois | 1,34 | 92,90 € | 47,57 € | 1,19 |
| 6 mois | 1,72 | 125,20 € | 64,11 € | 1,60 |
| 12 mois | 2,24 | 169,40 € | 86,75 € | 2,17 |
| 18 mois | 2,66 | 205,10 € | 105,03 € | 2,62 |
| 24 mois | 2,98 | 232,30 € | 118,96 € | 2,97 |
| 36 mois | 3,42 | 269,70 € | 138,11 € | 3,45 |

**Délai de récupération du CAC : ≈ 1,8 mois** (interpolation linéaire sur la courbe ci-dessus).

> **La règle de décision.** LTV/CAC à 12 mois ≥ 2,0 et payback ≤ 4 mois : on
> peut accélérer. LTV/CAC 12 mois < 1,5 : on ne scale pas, on répare. Un ratio
> > 5 ne signifie pas « excellent » mais « tu sous-investis » — voir E01 § 6.

### 3.1 Comparaison des cohortes entre paliers

| Palier | nCAC | LTV 12 m (contrib.) | LTV/CAC 12 m | LTV/CAC 24 m | Payback (mois) |
| --- | ---: | ---: | ---: | ---: | ---: |
| P1 | 26,62 € | 55,97 € | 2,10 | 2,87 | 1,8 |
| P2 | 30,78 € | 70,70 € | 2,30 | 3,15 | 1,3 |
| P3 | 33,18 € | 80,06 € | 2,41 | 3,31 | 1,1 |
| P4 | 37,77 € | 83,51 € | 2,21 | 3,03 | 1,6 |
| P5 | 40,03 € | 86,75 € | 2,17 | 2,97 | 1,8 |

---

## 4. Trésorerie et besoin en fonds de roulement

| Palier | Stock | Encaissements en attente | Avance pub | − Dettes fourn. | **BFR** | En jours de CA |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| P1 | 15 333 € | 4 907 € | 1 363 € | 0 € | **21 603 €** | 18 j |
| P2 | 80 570 € | 30 693 € | 10 464 € | 17 265 € | **104 462 €** | 14 j |
| P3 | 418 560 € | 117 720 € | 101 733 € | 156 960 € | **481 053 €** | 12 j |
| P4 | 1 160 425 € | 293 160 € | 488 600 € | 549 675 € | **1 392 510 €** | 14 j |
| P5 | 1 832 581 € | 433 320 € | 1 045 944 € | 1 047 189 € | **2 264 655 €** | 16 j |

| Palier | Cash immobilisé par +100 k€ de CA mensuel | EBITDA mensuel | Croissance autofinançable / mois |
| --- | ---: | ---: | ---: |
| P1 | 58 704 € | −9 403 € | **négative — la croissance consomme du cash** |
| P2 | 45 379 € | −19 838 € | **négative — la croissance consomme du cash** |
| P3 | 40 864 € | 51 033 € | 124 886 € de CA |
| P4 | 47 500 € | 198 572 € | 418 046 € de CA |
| P5 | 52 263 € | 364 752 € | 697 917 € de CA |

> **Ce tableau tue plus de marques que la publicité.** Une marque qui croît de
> 30 % par mois avec un BFR de 45 jours de CA est en faillite technique bien
> avant d'être non rentable. Module E10.

---

## 5. Plan média au palier P5

Dépense publicitaire totale : **1 494 206 € / mois** (**344 817 € / semaine**, **49 151 € / jour**).

| Canal | Part | Budget/mois | nCAC canal | Nouveaux clients/mois | Rôle |
| --- | ---: | ---: | ---: | ---: | --- |
| Meta (Advantage+ / ASC + prospection large) | 55 % | 821 813 € | 38,50 € | 21 346 | Volume, découverte, 1ᵉʳ contact |
| TikTok (Smart+ / Spark Ads UGC) | 15 % | 224 131 € | 44,00 € | 5 094 | Volume jeune, nouveaux angles |
| Google Search + Shopping (marque et générique) | 11 % | 164 363 € | 19,00 € | 8 651 | Récolte de la demande créée |
| Google PMax / Demand Gen / YouTube | 8 % | 119 536 € | 47,00 € | 2 543 | Extension de portée |
| Influence + affiliation (CPA et forfait) | 8 % | 119 536 € | 41,00 € | 2 916 | Preuve sociale, contenu source |
| Pinterest, Snap, native, presse | 3 % | 44 826 € | 55,00 € | 815 | Incrémentalité marginale, test |
| **Total** | 100 % | **1 494 206 €** | — | **41 364** | — |

> **Attention.** La somme des clients attribués par canal (41 364) dépasse
> les nouveaux clients réels (37 324), soit **11 % de sur-attribution**.
> C'est normal et universel : chaque plateforme s'attribue le même client.
> Le seul chiffre honnête est le nCAC global — module E09.

---

## 6. La machine créative — combien de publicités faut-il produire ?

| Palier | Budget pub/sem. | Budget de test (15 %) | Concepts testés/sem. | Gagnants/sem. | Gagnants en rotation | Assets produits/mois |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| P2 | 24 147 € | 3 622 € | 14 | 1,7 | 9 | 188 |
| P3 | 100 615 € | 15 092 € | 38 | 4,2 | 21 | 654 |
| P5 | 344 817 € | 51 722 € | 57 | 5,2 | 23 | 1 245 |

> **Voilà le vrai goulot d'étranglement d'une marque à 1 M€/semaine.** Ce n'est
> ni le produit, ni le budget, ni l'algorithme : c'est la capacité à produire
> et juger ~**57 concepts publicitaires nouveaux par semaine**, dont ~5 seulement
> survivront. Module E05.

---

## 7. Quel levier vaut le plus ? (au palier P5)

Effet sur l'**EBITDA annuel** d'une amélioration de 10 % de chaque levier,
toutes choses égales par ailleurs.

EBITDA annuel de référence : **4 377 023 €**.

| Levier | Gain d'EBITDA annuel | En % de l'EBITDA |
| --- | ---: | ---: |
| +10 % de panier moyen (AOV, à commandes constantes) | 3 139 401 € | 71,7 % |
| +10 % de taux de conversion du site (à budget pub constant) | 2 662 749 € | 60,8 % |
| −10 % de CAC à volume constant | 1 793 047 € | 41,0 % |
| +10 % de commandes de réachat | 1 194 871 € | 27,3 % |
| −10 % de coût marchandise (COGS) | 628 313 € | 14,4 % |
| −1 point de taux de retour / SAV | 433 320 € | 9,9 % |
| −10 % de frais fixes | 432 000 € | 9,9 % |

> **Lis ce tableau deux fois.** Le levier le plus rentable n'est presque jamais
> celui sur lequel l'équipe passe ses journées. Refais-le avec **tes** chiffres :
> c'est l'exercice 4 du module E01.

---

## 8. Le même chiffre d'affaires, piloté sur la marge

P5 fait 1 M€/semaine à 10,1 % d'EBITDA. P5+ fait le même
chiffre d'affaires avec moins de commandes, un panier plus élevé, plus de
réachat et moins de remises.

|  | P5 — piloté volume | P5+ — piloté marge | Écart |
| --- | ---: | ---: | ---: |
| CA TTC / semaine | 999 968 € | 999 978 € |  |
| Commandes / mois | 60 200 | 56 130 | -7 % |
| AOV mixte TTC | 71,98 € | 77,20 € | +7 % |
| Part du CA en réachat | 44,9 % | 52,4 % | +7,6 pts |
| MER | 2,90 | 3,40 |  |
| Marge brute (CM2) | 61,5 % | 66,0 % | +4,5 pts |
| Dépense pub / mois | 1 494 206 € | 1 274 481 € | -15 % |
| **EBITDA / mois** | **364 752 €** | **733 799 €** | **+101 %** |
| **EBITDA en % du CA HT** | **10,1 %** | **20,3 %** | **+10,2 pts** |
| **EBITDA annuel** | **4 377 023 €** | **8 805 583 €** | **4 428 560 €** |

> **C'est là que se trouve l'argent.** Le passage de P5 à P5+ ne demande
> aucun euro de chiffre d'affaires supplémentaire. Il demande un panier moyen
> plus élevé, une base de clients qui revient, et de la discipline sur la
> remise. **Ton objectif n'est pas 1 M€/semaine. Ton objectif est P5+.**

---

## 9. Le tableau de conversion à connaître par cœur

| CA TTC / semaine | CA TTC / mois | CA TTC / an | Commandes/jour à 72 € d'AOV | Dépense pub/jour à MER 2,9 |
| ---: | ---: | ---: | ---: | ---: |
| 10 000 € | 43 333 € | 520 000 € | 20 | 493 € |
| 25 000 € | 108 333 € | 1 300 000 € | 50 | 1 232 € |
| 50 000 € | 216 667 € | 2 600 000 € | 99 | 2 463 € |
| 100 000 € | 433 333 € | 5 200 000 € | 198 | 4 926 € |
| 250 000 € | 1 083 333 € | 13 000 000 € | 496 | 12 315 € |
| 500 000 € | 2 166 667 € | 26 000 000 € | 992 | 24 631 € |
| 1 000 000 € | 4 333 333 € | 52 000 000 € | 1 984 | 49 261 € |

*Fin des chiffres canoniques. Généré par `ecommerce/outils/modele_nora.py`.*
