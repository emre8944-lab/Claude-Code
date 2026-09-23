# Module 07 — Le site et la conversion

> **Objet :** transformer un clic acheté en commande. Chaque point de conversion gagné
> baisse ton CPA sans toucher à la pub.
> **Prérequis :** modules 01, 05, 06.
> **Outil :** [checklist de lancement](../boite-a-outils/checklist-lancement.md)
> **Devoirs :** `exercices/07-rendu.md`

---

## 0. Le travail du site

Ta pub achète de l'attention. Ton site la transforme en argent — ou la gaspille. Tu as
vu au module 01 qu'une baisse de conversion de 2,8 % à 2,0 % fait passer Nilo de
rentable à quasi nulle. L'inverse est vrai : **passer de 2,0 % à 2,8 %, c'est baisser le
CPA de 29 % sans dépenser un euro de plus en pub.**

Le site n'a qu'une mission pour un visiteur venu d'une pub : **tenir la promesse de la
pub, lever les doutes, et rendre l'achat facile.** Tout ce qui ne sert pas l'une de ces
trois choses est à enlever.

---

## 1. Les fondations techniques

### 1.1 Shopify

Pour une marque DTC, Shopify est le choix par défaut : un tunnel de paiement parmi les
plus optimisés du marché, Shop Pay, un écosystème d'applications énorme, et une
intégration native avec Meta, TikTok, Google et les principaux outils. Tu n'as pas à
réinventer un tunnel de paiement ; tu as à bien construire ce qu'il y a avant.

- **Thème** : un thème gratuit récent et rapide suffit largement au départ. Un thème
  premium peut se justifier plus tard. Ce qui compte n'est pas le thème, c'est le
  contenu de la page.
- **Applications** : chaque application ajoute du code et ralentit le site. Règle :
  **pas plus de 10 à 15 applications**, et tu supprimes celles que tu n'utilises plus
  (en vérifiant qu'elles n'ont pas laissé de code dans le thème).

### 1.2 Le mobile d'abord — vraiment

Sur le trafic issu des réseaux sociaux, **l'immense majorité des visites se font sur
téléphone** (souvent plus de 80 %). Conséquences :
- Tu conçois, rédiges et valides **chaque page sur un téléphone**, pas sur ton écran
  d'ordinateur.
- Ce qui compte, c'est ce qu'on voit **sans faire défiler** sur un écran de téléphone.
- Les boutons se touchent avec un pouce ; les textes se lisent sans zoomer.

### 1.3 La vitesse

Un site lent perd des visiteurs **avant même qu'ils voient ta page** — tu paies le clic
pour rien. Repère : l'élément principal de la page doit s'afficher en **moins de
2,5 secondes** sur mobile (le seuil « bon » des Core Web Vitals de Google). Mesure avec
PageSpeed Insights.

Les causes habituelles, par ordre de fréquence : images trop lourdes (compresse-les,
format WebP), trop d'applications, vidéos lourdes en haut de page, polices multiples.

---

## 2. Les types de pages, et quand les utiliser

| Page | Ce que c'est | Pour quel trafic |
|---|---|---|
| **Page produit** | La page standard du produit | Tout trafic ; la base |
| **Page d'atterrissage dédiée** | Une page construite pour **un angle** de pub précis, avec le même titre, les mêmes visuels, la même promesse | Trafic froid d'une pub qui performe, dès que tu scales un angle |
| **Publireportage** (*advertorial*) | Un article (« Pourquoi tant de chats ne boivent pas assez — et ce qu'une vétérinaire recommande ») qui éduque avant de présenter le produit | Trafic froid qui ne connaît ni le problème ni la solution ; public plus âgé |
| **Liste** (*listicle*) | « 5 raisons pour lesquelles 20 000 propriétaires de chats sont passés à Nilo » | Trafic froid, format rapide à lire |
| **Quiz** | Quelques questions → recommandation personnalisée | Gammes larges (soin, beauté, nutrition) ; collecte d'emails |
| **Page d'accueil** | La vitrine de la marque | Trafic de marque et organique ; peu utile pour la pub froide |

⚠️ **Un publireportage doit être identifiable comme de la publicité.** En France, toute
publicité en ligne doit être clairement reconnaissable comme telle. Une mention visible
(« Publicité », « Contenu sponsorisé par Nilo ») est obligatoire ; un faux article de
presse est une pratique trompeuse.

### La cohérence pub → page (*message match*)

C'est la cause n° 1 des pages qui ne convertissent pas. Si ta pub dit « Ton chat boit
au robinet ? » et que ta page s'ouvre sur « Fontaine inox 2,5 L avec pompe
silencieuse », le visiteur a l'impression de s'être trompé de porte.

**Règle :** le haut de la page reprend **la promesse et le visuel** de la pub qui
envoie le trafic. Quand un angle scale, il mérite sa propre page d'atterrissage.

---

## 3. L'anatomie d'une page produit qui convertit

### 3.1 Ce qu'on voit sans défiler (sur téléphone)

| # | Élément | Règle |
|---|---|---|
| 1 | **Galerie** | La première image montre **le produit en usage** (le chat qui boit), pas un produit sur fond blanc. Puis : démonstration animée, infographie des bénéfices, comparaison, photo client, contenu de la boîte |
| 2 | **Étoiles et nombre d'avis** | Réels, cliquables vers les avis |
| 3 | **Titre = bénéfice** | « La fontaine qui donne envie de boire. » Le nom du produit peut être en sous-titre |
| 4 | **3 ou 4 bénéfices** | Courts, avec icônes. Le bénéfice d'abord, la caractéristique en preuve : « Silencieuse — 30 dB, moins qu'un chuchotement » |
| 5 | **L'offre** | Les paliers du module 06, le palier du milieu présélectionné |
| 6 | **Le bouton** | Gros, contrasté, verbe d'action |
| 7 | **La ligne de confiance** | Date de livraison, essai de 60 jours, moyens de paiement |

### 3.2 Ce qu'on trouve en défilant (dans cet ordre)

1. **Comment ça marche** en 3 étapes illustrées.
2. **La vidéo de démonstration** (30 à 60 secondes, sous-titrée).
3. **Le problème** : une section éducative courte (« Pourquoi les chats boivent peu à la
   gamelle »), sans promesse médicale.
4. **Le tableau comparatif** : Nilo contre la gamelle contre la fontaine plastique
   générique. Trois colonnes, 6 à 8 lignes, des coches.
5. **Le mur de contenus clients** : photos et vidéos de vrais clients et de leurs chats.
6. **Les avis**, avec photos, filtrables, **y compris les négatifs** (ils rendent les
   positifs crédibles).
7. **La FAQ**, qui est en réalité une **liste d'objections** (section 4).
8. **La garantie**, en grand.
9. **L'histoire du fondateur**, en 4 lignes et une photo.
10. **Un bouton d'achat collant** en bas de l'écran, visible pendant tout le défilement.

---

## 4. Écrire la page : lever les objections

Un visiteur n'achète pas tant qu'il lui reste une question sans réponse. Ton travail
est de **lister toutes ses objections et d'y répondre avant qu'il les formule**.

**Où les trouver :** tes emails de service client, les commentaires sous tes pubs, les
avis négatifs des concurrents, les questions posées aux créateurs, et une question
posée à chaque acheteur après l'achat (section 7).

**Les objections de Nilo, et leurs réponses sur la page :**

| Objection | Réponse, et où |
|---|---|
| « Mon chat ne va pas l'utiliser. » | 60 jours pour essayer, et les conseils d'adoption (FAQ + vidéo) |
| « Ça va faire du bruit la nuit. » | « 30 dB mesurés » + une vidéo avec le son (bénéfice n° 1) |
| « C'est pénible à nettoyer. » | « Au lave-vaisselle » + vidéo de démontage de 20 secondes |
| « Il faut racheter des filtres, c'est un piège. » | Prix des filtres affiché clairement, abonnement facultatif et résiliable |
| « La pompe va lâcher. » | Garantie 3 ans |
| « C'est plus cher que sur Amazon. » | Tableau comparatif : inox contre plastique, garantie, SAV européen |
| « Est-ce que c'est sûr (électricité, eau) ? » | Basse tension, conformité CE, informations de sécurité |

**Les règles d'écriture** (ce sont celles de Hopkins, module 12 du cursus business) :
- **Précis plutôt que superlatif** : « 30 dB » bat « ultra-silencieuse ».
- **Les mots du client** plutôt que les tiens : s'ils disent « il squatte l'évier »,
  écris « il squatte l'évier ».
- **Le bénéfice, puis la preuve.**
- **Des phrases courtes.** On lit sur un téléphone, dans le métro, d'un œil.

---

## 5. Le panier et le paiement

- **Un tiroir de panier** (qui s'ouvre sur la page) plutôt qu'une page panier séparée :
  une étape de moins.
- **Aucune surprise** : si des frais existent, ils sont annoncés avant le panier.
  Les frais surprises sont la première cause d'abandon.
- **La date de livraison** est rappelée au panier.
- **Les paiements express** (Apple Pay, Google Pay, Shop Pay, PayPal) en haut du
  paiement.
- **Pas de création de compte obligatoire.**
- **Ne bricole pas le tunnel de paiement de Shopify** : il est plus optimisé que tout
  ce que tu pourrais faire. Travaille ce qui vient avant.

---

## 6. La confiance et les obligations légales visibles

- **Mentions légales, CGV, politique de retour, politique de confidentialité**,
  accessibles depuis chaque page (module 13 pour le contenu).
- **Un moyen de contact** visible (email, formulaire, idéalement messagerie) et une
  entreprise identifiable.
- **Les informations de sécurité produit** exigées par le GPSR (module 04).
- **Le bandeau cookies** conforme : en France, la CNIL exige que **refuser soit aussi
  simple qu'accepter**. Un bandeau non conforme expose à des sanctions — et un bandeau
  agressif fait fuir.
- **Les avis** : indique si et comment tu vérifies qu'ils viennent de vrais acheteurs.

---

## 7. La méthode d'optimisation (CRO)

L'optimisation du taux de conversion n'est pas une liste d'astuces. C'est un
processus :

```
1. RECHERCHE     Où les visiteurs partent-ils ? Pourquoi ?
2. HYPOTHÈSES    « Si on fait X, la conversion monte, parce que Y. »
3. PRIORITÉS     Impact × Confiance × Facilité
4. TEST          Mesurer honnêtement (section 8)
5. APPRENDRE     Garder, jeter, et nourrir les hypothèses suivantes
```

### 7.1 Les outils de recherche

| Outil | Ce qu'il te dit |
|---|---|
| **Entonnoir Shopify** (sessions → panier → paiement → achat) | **Où** les visiteurs partent |
| **Cartes de chaleur et enregistrements de sessions** (Microsoft Clarity, gratuit) | **Ce qu'ils font** : où ils cliquent, jusqu'où ils défilent, où ils hésitent |
| **La question après l'achat** : « Qu'est-ce qui a failli t'empêcher de commander ? » | **Pourquoi** ils hésitent — la question la plus rentable du e-commerce |
| **Le service client** | Les questions récurrentes = les trous de ta page |
| **Regarder 20 sessions enregistrées** | Plus instructif que n'importe quel rapport |

### 7.2 Prioriser

Note chaque idée de 1 à 10 sur trois critères — **Impact** potentiel, **Confiance** que
ça marche, **Facilité** de mise en œuvre — et commence par le meilleur score. Les
premiers chantiers sont presque toujours les mêmes : la cohérence pub → page, la
première image, le titre, les avis, les objections, la vitesse.

---

## 8. Les tests A/B : ce que personne ne te dit

### 8.1 Le problème de taille d'échantillon

Pour détecter une amélioration avec une confiance raisonnable, il faut **beaucoup plus
de visiteurs qu'on ne le croit**. Une règle approchée (puissance de 80 %, seuil de 5 %) :

```
Visiteurs nécessaires PAR VARIANTE ≈ 16 × p × (1 − p) ÷ δ²
  p = ton taux de conversion actuel
  δ = l'écart absolu que tu veux détecter
```

**Exemple Nilo :** conversion de 2,8 %, on veut détecter +10 % relatif (2,8 % → 3,08 %,
soit δ = 0,0028) :

```
16 × 0,028 × 0,972 ÷ 0,0028² ≈ 55 500 visiteurs par variante ≈ 111 000 au total
```

À 2 000 visites par jour, il faut **56 jours**. Pour **un seul** test.

Si on cherche un effet de +30 % (δ = 0,0084) :

```
16 × 0,028 × 0,972 ÷ 0,0084² ≈ 6 200 visiteurs par variante ≈ 12 400 au total → 6 jours
```

### 8.2 Ce que ça implique

- **Tant que tu as peu de trafic, ne teste pas les petits détails** (couleur du bouton,
  une phrase). Tu ne pourras jamais mesurer leur effet ; tu mesureras du bruit.
- **Teste des changements importants** : nouvelle page contre ancienne, nouvel angle en
  haut de page, nouvelle offre. Des effets de +20 à +50 % sont mesurables vite.
- **Ne t'arrête pas au premier jour où ta variante « gagne »** : les résultats oscillent.
  Fixe la durée à l'avance, et teste par semaines complètes (le comportement change entre
  semaine et week-end).
- **Mesure la CM3 par visiteur**, pas seulement la conversion (module 06).

---

## 9. Fil rouge — La page de Nilo, avant et après

Pendant le test (module 03), Nilo utilisait une page produit générique : photo sur fond
blanc en premier, titre « Fontaine à eau pour chat inox 2,5 L », pas de comparatif,
FAQ de quatre lignes. Conversion : **2,2 %**.

Pour la phase de validation, le fondateur a construit une page d'atterrissage pour
l'angle gagnant (« Ton chat ne boit pas assez ») :

| Changement | Pourquoi |
|---|---|
| Première image : un chat qui boit à la fontaine, en gros plan | Cohérence avec la pub, bénéfice visible |
| Titre : « Ton chat boit enfin assez. » | Reprend la promesse de la pub |
| Section « Pourquoi les chats boivent peu à la gamelle » | Éducation du trafic froid |
| Tableau comparatif gamelle / plastique / Nilo | Répond à « c'est plus cher qu'Amazon » |
| FAQ réécrite à partir des 30 premiers emails clients | Objections réelles |
| Palier « Complet » présélectionné | Panier moyen |
| Date de livraison affichée | Réduit l'incertitude |

Conversion pendant la validation : **3,1 %**. Soit, à CPM et CTR égaux, un CPA
**29 % plus bas** (2,2 ÷ 3,1 = 0,71). Aucune de ces modifications n'a coûté plus d'une
journée de travail.

Note : ce n'était pas un test A/B propre (les périodes diffèrent, les créas aussi). On
ne peut pas attribuer les +41 % à la page seule. Mais l'écart est assez grand pour que
la décision de garder la nouvelle page ne fasse aucun doute. **Savoir quand une preuve
imparfaite suffit, c'est aussi une compétence.**

---

## 10. Les pièges

1. **Concevoir sur ordinateur.**
2. **La page générique pour toutes les pubs.** Chaque angle qui scale mérite sa page.
3. **Trop d'applications** : pop-ups, compteurs, badges qui ralentissent et
   décrédibilisent.
4. **Cacher les avis négatifs.**
5. **Tester la couleur d'un bouton avec 300 visites par jour.**
6. **Les frais surprises au paiement.**
7. **Oublier les pages légales et le bandeau cookies** : les plateformes publicitaires
   et les processeurs de paiement vérifient.

---

## 11. Devoirs — à rendre dans `exercices/07-rendu.md`

**Exercice 1 — L'audit.** Prends la page produit d'un concurrent (ou la tienne). Note
chacun des 7 éléments du haut de page et des 10 sections du bas (section 3) : présent,
absent, faible. Trois améliorations prioritaires.

**Exercice 2 — Les objections.** Liste 10 objections de ton client et, pour chacune,
la réponse et l'endroit de la page où elle apparaît.

**Exercice 3 — La maquette.** Construis (sur papier, Figma ou directement sur Shopify)
le haut de ta page produit tel qu'il apparaît sur un téléphone. Envoie une capture.

**Exercice 4 — Le calcul de test.** Ta conversion est de 2,4 %, tu as 1 200 visites par
jour. Combien de jours pour détecter un effet de +15 % ? De +40 % ? Qu'en conclus-tu
sur ce que tu dois tester maintenant ?

---

*Module suivant : [08 — Créatives et copywriting](08-creatives-copywriting.md). Le
module le plus important pour scaler.*
