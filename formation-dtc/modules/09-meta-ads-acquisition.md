# Module 09 — Meta Ads et acquisition payante

> **Objet :** installer, structurer et scaler un compte publicitaire de 50 €/jour à
> 10 000 €/jour, sans le brûler — puis ajouter TikTok, Google et les autres canaux au
> bon moment.
> **Prérequis :** modules 01, 03, 07, 08.
> **Devoirs :** `exercices/09-rendu.md`

> **Avertissement de durée de vie.** Meta, TikTok et Google renomment leurs campagnes et
> déplacent leurs boutons plusieurs fois par an. Les **principes** de ce module sont
> stables depuis des années ; les **noms d'options** sont ceux en vigueur au moment de
> la rédaction. Si un nom a changé, cherche la fonction, pas le libellé.

---

## 0. Ce que fait la pub, et ce qu'elle ne fait pas

La publicité payante **n'invente rien** : elle amplifie un produit, une offre, une page et
des créas qui existent déjà. Un compte mal structuré peut gâcher une bonne machine ; un
compte parfaitement structuré ne sauvera jamais une mauvaise machine. Si ton CPA est
mauvais, **regarde d'abord les modules 06, 07 et 08**. Neuf fois sur dix, c'est là.

Pourquoi Meta en premier ? Parce que Facebook et Instagram restent, pour la plupart des
marques DTC européennes, **le canal qui permet de créer de la demande à grande échelle**
auprès de gens qui ne cherchaient pas ton produit — de 25 à 70 ans, dans tous les pays.

---

## 1. La mise en place (une fois, proprement)

### 1.1 Les comptes

- Un **portefeuille Business** (Business Manager) au nom de ta société, avec ta Page
  Facebook, ton compte Instagram et ton compte publicitaire.
- **Au moins deux administrateurs**, tous avec la **double authentification**. Si ton
  seul compte personnel est piraté ou bloqué, tu perds l'accès à tout.
- La **vérification d'entreprise** et la **vérification du nom de domaine** de ta
  boutique.
- Un moyen de paiement fiable, avec un plafond suffisant. Les échecs de paiement
  répétés dégradent la confiance de Meta envers ton compte.

### 1.2 Le suivi des conversions

- Le **pixel** (dans le navigateur) **et l'API Conversions** (de serveur à serveur),
  installés via l'intégration officielle de Shopify. Les deux ensemble compensent une
  partie des pertes de signal (iOS, bloqueurs), et Meta les dédoublonne.
- Dans le Gestionnaire d'événements, vérifie la **qualité de correspondance des
  événements** (le score qui indique si Meta arrive à relier tes achats à des personnes) :
  plus il est élevé, mieux l'algorithme apprend.
- **Fais un achat test** et vérifie que l'événement « Achat » remonte, avec le bon
  montant. Note si le montant est TTC ou HT (module 01).
- Ajoute des **paramètres UTM** à toutes tes pubs, pour retrouver leur trafic dans
  Shopify et Google Analytics.

### 1.3 La santé du compte

Meta note ton compte en continu : respect des règles publicitaires, **retours des
clients** sur leur expérience d'achat (délais, qualité, conformité à la pub). Un
mauvais score peut renchérir ou restreindre tes pubs. Ta meilleure assurance : un
produit conforme à la pub, livré vite, et des pubs dans les règles (module 08,
section 8).

> ⚠️ Fuis toute offre de « comptes publicitaires non bannissables » ou de techniques pour
> contourner une restriction. Tu mettrais en danger toute ton entreprise pour gagner
> quelques semaines. Les comptes d'agence légitimes existent (partenaires officiels) ;
> le reste est un piège.

---

## 2. Les principes du compte moderne

1. **Ciblage large.** Le pays, l'âge (souvent 18-65+), les deux sexes sauf produit
   clairement genré, sans centres d'intérêt. La créa fait le ciblage (module 08).
2. **Placements automatiques.** Laisse Meta diffuser sur Facebook, Instagram, Reels,
   Stories. Fournis les formats adaptés (9:16 pour Reels et Stories, 4:5 pour les fils).
3. **Optimisation sur l'achat.** Même avec un petit budget. Optimiser sur « ajout au
   panier » ou « clic » te donne des gens qui cliquent et ajoutent — pas des acheteurs.
4. **Consolidation.** Peu de campagnes, peu d'ensembles, beaucoup de budget par
   ensemble. L'algorithme sort de sa **phase d'apprentissage** vers **≈ 50 achats par
   semaine et par ensemble** ; éparpiller ton budget sur 15 ensembles l'empêche
   d'apprendre.
5. **Diversité créative.** Plus de concepts réellement différents dans un même
   ensemble = plus d'audiences atteintes (module 08, section 0).
6. **Patience.** Chaque modification importante (budget fortement changé, nouvelles
   pubs, nouveau ciblage) peut relancer l'apprentissage. Ne touche pas à ce qui marche
   toutes les six heures.

---

## 3. La structure recommandée : deux campagnes

```
CAMPAGNE A — TEST CRÉATIF        (10 à 20 % du budget)
  Objectif : Ventes, optimisation Achat
  Budget au niveau de l'ensemble (pour garantir une dépense à chaque concept)
  ├── Ensemble « Concept 1 : robinet » — 3 à 6 pubs, ciblage large
  ├── Ensemble « Concept 2 : vétérinaire » — 3 à 6 pubs
  └── Ensemble « Concept 3 : nous contre eux » — 3 à 6 pubs
      Budget par ensemble ≈ 1 à 2 × CPA cible par jour

CAMPAGNE B — SCALING             (80 à 90 % du budget)
  Campagne Ventes en mode Advantage+ (ex-« Advantage+ Shopping »)
  ou campagne à budget au niveau de la campagne, ciblage large
  └── Les gagnants « diplômés » de la campagne A
      (10 à 30 pubs de concepts différents, reprises avec leur identifiant
       de publication pour conserver likes et commentaires)
```

**Pourquoi reprendre l'identifiant de publication ?** Une pub qui scale accumule des
réactions et des commentaires (« le mien l'adore ! »). C'est de la preuve sociale. Si tu
la recrées de zéro dans la campagne de scaling, tu repars à zéro.

**Les clients existants :** dans les campagnes automatisées, définis qui sont tes
clients existants (liste email, acheteurs) et, si l'option est disponible, limite la part
de budget qui leur est consacrée. Sinon Meta peut dépenser une partie de ton budget
d'acquisition à « reconquérir » des gens qui auraient racheté par email.

**Le reciblage :** au début, n'en fais pas de campagne séparée. Les campagnes larges
touchent déjà ceux qui ont visité ton site. Une campagne de reciblage séparée se
justifie à l'échelle, **si** un test montre qu'elle est incrémentale.

---

## 4. Les règles de décision

Écrites à l'avance (module 03). Voici celles de Nilo, avec un CPA cible de 26,50 € et un
CPA d'équilibre de 35,80 € :

| Situation | Règle | Action |
|---|---|---|
| Pub en test | Dépense ≥ 1,5 × CPA cible, **aucun ajout au panier** | Couper |
| Pub en test | Dépense ≥ 3 × CPA cible, CPA > CPA d'équilibre | Couper |
| Pub en test | CPA ≤ CPA cible avec ≥ 3 à 5 achats | **Diplômer** vers la campagne B |
| Pub en test | Entre les deux, bons indicateurs avancés | Laisser tourner 48 h de plus |
| Campagne B | CPA 3 jours ≤ CPA cible | Augmenter le budget (section 5) |
| Campagne B | CPA 3 jours entre cible et équilibre | Ne rien toucher, ajouter des créas |
| Campagne B | CPA 3 jours > CPA d'équilibre | Baisser le budget de 20 %, diagnostiquer (créas usées ? page ? stock ?) |
| Une pub dans B | Sa part de dépense s'effondre et son CPA monte depuis 7 jours | Fatigue : la remplacer par une itération (nouvelle accroche) |

**Toujours sur 3 jours minimum**, jamais sur une journée. Un mauvais mardi n'est pas une
tendance.

---

## 5. Scaler un compte

### 5.1 Scaling vertical : plus de budget

- Sur la campagne de scaling, augmente le budget de **20 à 30 % toutes les 48 à 72
  heures** tant que le CPA reste sous la cible.
- Des hausses plus fortes sont possibles sur un compte stable avec beaucoup de données,
  mais elles perturbent davantage l'apprentissage.
- **Les plafonds de coût** (*cost cap*) : à grande échelle, tu peux indiquer à Meta un
  coût par achat cible ; il ne dépense que quand il pense pouvoir le tenir. Ta dépense
  devient moins prévisible, mais ton CPA plus stable. Outil précieux au-delà de quelques
  milliers d'euros par jour.

### 5.2 Le CPA marginal : le chiffre qui arrête le scaling

C'est le module 13 du cursus business, section 2.2, appliqué. Quand tu montes le budget,
ton CPA **moyen** peut rester correct pendant que le CPA des commandes
**supplémentaires** explose.

**Nilo, au mois 6 :**

| Budget / jour | Nouvelles commandes / jour | CPA moyen | CPA marginal |
|---|---|---|---|
| 1 000 € | 40 | 25,00 € | — |
| 1 300 € | 49 | 26,53 € | 300 ÷ 9 = **33,33 €** |
| 1 700 € | 57 | 29,82 € | 400 ÷ 8 = **50,00 €** |

À 1 300 €/jour, le CPA moyen (26,53 €) est à la cible. Mais les 9 commandes
supplémentaires ont coûté 33,33 € chacune : chacune ne rapporte que 35,79 − 33,33 =
**2,46 €** de CM3. À 1 700 €/jour, les 8 commandes supplémentaires coûtent **50 €** : au
dessus du CPA d'équilibre, **chacune fait perdre 14 €**. Le tableau de bord, qui affiche
un CPA moyen de 29,82 €, ne le dit pas.

**Décision :** rester à ≈ 1 300 €/jour et **produire de nouveaux concepts**. C'est le
seul moyen de faire baisser toute la courbe (module 08). Le budget suit les créas, pas
l'inverse.

### 5.3 Scaling horizontal : plus de surface

Quand le vertical plafonne, on élargit :
1. **Nouveaux concepts créatifs** → nouvelles audiences. Toujours le levier n° 1.
2. **Nouveaux pays** : traduire les gagnants (module 12). Souvent le levier le plus
   rapide après les créas.
3. **Nouveaux canaux** : TikTok, Google, YouTube (sections 7 à 9).
4. **Nouvelles pages d'atterrissage** par angle (module 07).
5. **Nouvelles offres** (module 06).

### 5.4 La saisonnalité

Les CPM grimpent en novembre-décembre, parfois fortement. Deux stratégies
complémentaires : **accumuler des emails** en octobre (liste d'attente Black Friday) pour
vendre en novembre par email à coût quasi nul, et **acquérir en janvier** quand les CPM
retombent.

---

## 6. Mesurer sans se mentir

### 6.1 Ce que tu regardes, et à quoi ça sert

| Chiffre | Source | Sert à… |
|---|---|---|
| **ROAS et CPA dans Meta** | Gestionnaire de publicités | **Comparer des pubs entre elles**, rien de plus |
| **MER** | Shopify ÷ dépenses totales | Piloter l'entreprise (module 01) |
| **nCAC et nc-ROAS** | Shopify (nouveaux clients) ÷ dépenses d'acquisition | Piloter l'acquisition |
| **« Comment nous avez-vous connus ? »** | Question après l'achat | Voir les canaux que l'attribution ne voit pas (bouche-à-oreille, TikTok organique, podcast) |
| **Outils d'attribution** (Triple Whale, Polar Analytics, Northbeam…) | Données croisées | Utiles à partir de quelques dizaines de milliers d'euros par mois de dépense ; aucun n'est « la vérité » |

### 6.2 L'incrémentalité

La seule question qui compte : **combien de ventes en plus** grâce à cette dépense ?

- **Les tests de lift de Meta** (*Conversion Lift*) : Meta retient un groupe témoin qui
  ne voit pas tes pubs et compare. Accessibles à partir d'un certain niveau de dépense.
- **Le test géographique maison** : tu coupes les pubs dans quelques régions comparables
  pendant 2 à 4 semaines, tu les gardes ailleurs, et tu compares l'évolution des ventes
  **totales** (Shopify) entre les deux groupes. Le protocole de Hopkins, cent ans après.
- À faire au moins une fois par an sur chaque canal important, et **avant** d'augmenter
  fortement un canal dont tu doutes (le reciblage et la recherche sur ta marque sont
  souvent beaucoup moins incrémentaux qu'ils n'en ont l'air).

---

## 7. TikTok

### 7.1 Pourquoi et quand

TikTok touche une audience énorme — plus seulement des adolescents — avec des CPM
souvent plus bas que Meta. Mais il exige des créas **natives** : tournées au téléphone,
rythmées, qui ressemblent à du contenu TikTok, pas à des pubs.

**Quand :** en général une fois Meta stable et rentable (souvent à partir de 50 à
100 k€/mois de CA). **Plus tôt** si ton produit est né sur TikTok (vidéo organique
virale, module 10).

### 7.2 Les leviers

- **Spark Ads** : tu sponsorises des vidéos existantes (les tiennes ou celles de
  créateurs, avec leur autorisation). Elles gardent l'apparence d'un contenu organique
  et leurs interactions. Souvent le format le plus performant.
- **Les campagnes automatisées** (Smart+) : l'équivalent des campagnes Advantage+ de
  Meta.
- **TikTok Shop** (ouvert en France en 2025) : la boutique intégrée à l'application,
  avec son programme d'**affiliation** (des créateurs vendent ton produit contre une
  commission) et ses campagnes publicitaires automatisées dédiées. Un canal à part
  entière, détaillé au module 10.

### 7.3 Démarrer

Budget de test de quelques milliers d'euros sur 2 à 3 semaines, avec des créas
**conçues pour TikTok** (pas tes pubs Meta recadrées), suivi par le pixel TikTok et son
API d'événements. Même logique de test et de diplôme que sur Meta.

---

## 8. Google et YouTube

Google capte la **demande existante** : les gens qui cherchent « fontaine à eau chat ».
Meta et TikTok **créent** de la demande. Les deux se complètent : plus tes pubs sociales
tournent, plus les gens cherchent ta marque et ta catégorie sur Google.

| Campagne | Rôle | Quand |
|---|---|---|
| **Recherche sur ta marque** | Protéger ton nom (sinon un concurrent l'achète) ; très bon ROAS apparent, mais peu incrémental | Dès que des gens cherchent ta marque |
| **Shopping / Performance Max** | Tes produits dans les résultats Google avec photo et prix ; capte les recherches de catégorie | Dès 30-50 k€/mois de CA, avec un flux produit propre (Merchant Center) |
| **Recherche sur les problèmes** | « chat ne boit pas assez », « fontaine chat silencieuse » | Selon le volume de recherche de ta catégorie |
| **YouTube / Demand Gen** | Vidéos plus longues, créer de la demande à grande échelle | Au-delà de 150-300 k€/mois de CA |

⚠️ **Performance Max cannibalise ta marque** : elle diffuse volontiers sur les recherches
de ton nom (des ventes qui auraient eu lieu de toute façon) et se les attribue. Exclus ta
marque de Performance Max pour mesurer ce qu'elle apporte vraiment.

---

## 9. Les autres canaux

| Canal | Pour qui | Quand |
|---|---|---|
| **Pinterest** | Maison, déco, mode, beauté, cuisine ; audience majoritairement féminine | Test à partir de 100 k€/mois si ta catégorie s'y prête |
| **Snapchat** | Audience jeune | Si ta cible a moins de 30 ans |
| **Sponsoring YouTube et podcasts** | Tout produit qui s'explique bien à l'oral | À partir de 150 k€/mois ; mesurer avec codes et « comment nous avez-vous connus ? » |
| **Publicité native** (Taboola, Outbrain) + publireportages | Public de plus de 45 ans, produits qui demandent de l'explication | À partir de 200-300 k€/mois |
| **Nouveaux réseaux publicitaires** (par exemple AppLovin, qui s'est ouvert aux annonceurs e-commerce en 2025) | À surveiller et tester avec prudence | À l'échelle, en test borné |
| **TV / télévision connectée** | Marques installées qui veulent de la notoriété | Au-delà de 1 M€/mois, avec mesure géographique |

---

## 10. La répartition du budget par palier

Ordre de grandeur, à adapter à ta catégorie :

| CA mensuel | Meta | TikTok | Google | Influence | Autres |
|---|---|---|---|---|---|
| < 50 k€ | 90-100 % | 0-10 % | Marque seulement | Envoi de produits | — |
| 50-150 k€ | 75-85 % | 5-15 % | 5-10 % | ≈ 5 % | — |
| 150-500 k€ | 60-70 % | 10-15 % | 10-15 % | 5-10 % | 0-5 % |
| 500 k€ - 1 M€+ | 50-65 % | 10-20 % | 10-20 % | 5-10 % | ≈ 5 % |

La dépendance à un seul canal est un **risque vital** : une restriction de compte Meta
pour une marque qui en dépend à 100 %, c'est un chiffre d'affaires qui tombe à zéro du
jour au lendemain. La diversification est d'abord une assurance.

---

## 11. Fil rouge — Le compte Nilo, du test au million

| Période | Budget / jour | Structure | CPA | MER |
|---|---|---|---|---|
| Test (module 03) | 150 € (3 produits) | 1 campagne de test par produit | 25,85 € (fontaine) | — |
| Validation (sem. 1-3) | 150 → 300 € | Test + 1 campagne de scaling | 23,10 € | 3,1 |
| Mois 3 | 600 € | Test (6 concepts/sem.) + Advantage+ | 24 € | 3,0 |
| Mois 6 | 1 300 € | Idem + premiers plafonds de coût | 26,50 € | 3,0 |
| Mois 9 (Q4) | 3 500 € | + Allemagne, + TikTok Spark Ads | 29 € (CPM de fin d'année) | 2,9 |
| Mois 14 | 6 000 € | 5 pays (lancement Italie et Espagne), Meta + TikTok + Google Shopping | 27 € | 3,0 |
| Mois 20 | ≈ 9 300 € (pub seule) | 6 pays, 5 canaux, ≈ 180 pubs actives | 26 € | 3,1 |

Remarque ce qui ne change pas : le CPA reste autour de 25-29 € du début à la fin. Le
budget a été multiplié par 60 **parce que** la surface a été multipliée (pays, canaux,
concepts), pas parce qu'on a poussé plus fort sur la même audience. Le détail est au
module 14.

---

## 12. Les pièges

1. **Découper son budget en 20 ensembles** : rien ne sort d'apprentissage.
2. **Optimiser sur les clics ou les ajouts au panier.**
3. **Toucher aux campagnes tous les jours.**
4. **Scaler au CPA moyen** sans regarder le CPA marginal.
5. **Croire le ROAS de la plateforme.** Pilote au MER et au nCAC.
6. **Dépendre d'un seul canal.**
7. **Un seul administrateur, sans double authentification.**
8. **Pousser le budget quand les créas sont usées** : tu achètes plus cher les mêmes
   personnes.

---

## 13. Devoirs — à rendre dans `exercices/09-rendu.md`

**Exercice 1 — La mise en place.** Coche chaque point de la section 1 pour ton compte
(ou ton futur compte). Pour chaque point manquant : comment et quand.

**Exercice 2 — Ta structure.** Dessine tes deux campagnes (section 3) avec tes premiers
concepts, le nombre de pubs et le budget de chaque ensemble, calculé à partir de ton CPA
cible.

**Exercice 3 — Tes règles.** Remplis le tableau de décision de la section 4 avec tes
propres CPA cible et d'équilibre.

**Exercice 4 — Le CPA marginal.** Budget 800 €/jour → 32 achats ; 1 100 €/jour →
39 achats ; 1 500 €/jour → 45 achats. CM2 par commande : 38 €. Calcule les CPA moyens et
marginaux et dis à quel budget tu t'arrêtes, et ce que tu fais ensuite.

**Exercice 5 — Le test géographique.** Conçois un test d'incrémentalité pour ta
campagne de recherche sur ta marque : régions, durée, indicateur mesuré, et seuil de
décision écrit à l'avance.

---

*Module suivant : [10 — Organique, influence et UGC](10-organique-influence-ugc.md).*
