# Module 11 — Rétention, email et LTV

> **Objet :** faire qu'un client en vaille deux ou trois. Là où l'acquisition devient
> chaque année plus chère, la rétention est la croissance la moins chère qui existe.
> **Prérequis :** module 01. Le module 13 du cursus business (section 1.3 : l'attrition
> domine tout) est le fondement théorique.
> **Devoirs :** `exercices/11-rendu.md`

---

## 0. Pourquoi la rétention décide de ta rentabilité à l'échelle

Au début, presque toute ta marge vient de la première commande. À l'échelle, le CPA
marginal monte (module 09) et la seule façon de continuer à acheter des clients à ce
prix, c'est **qu'ils rapportent davantage après leur premier achat**.

Deux marques avec le même CPA de 26 € :
- Marque A : ses clients ne reviennent pas. LTV 12 mois = CM2 de la première commande.
- Marque B : 35 % de ses clients rachètent dans l'année. Sa LTV est plus haute de
  30 %.

La marque B peut **payer ses clients plus cher** que A tout en gagnant autant. Elle
remportera donc les enchères publicitaires, touchera plus de monde, et grandira plus vite.
**À l'échelle, la rétention est un avantage d'acquisition.**

---

## 1. Les chiffres de la rétention

| Indicateur | Définition | Pourquoi |
|---|---|---|
| **Taux de réachat** | % de clients ayant passé ≥ 2 commandes, à 90, 180 et 365 jours | La mesure de base |
| **Délai entre deux commandes** | Médiane en jours | Cale le moment de tes relances |
| **Part du CA des clients existants** | CA des clients revenus ÷ CA total | À surveiller chaque mois |
| **LTV par cohorte** | Marge cumulée par client, par mois d'acquisition | **Le seul chiffre de LTV fiable** |
| **Attrition de l'abonnement** | % d'abonnés perdus par mois | Le terme qui domine la valeur d'un abonnement |
| **Part du CA venant de l'email et du SMS** | Selon l'outil d'emailing | Indicatif (section 9) |

### 1.1 L'analyse de cohortes

On regroupe les clients par **mois d'acquisition**, et on suit la marge cumulée par
client. **Cohortes de Nilo (CM2 cumulée par client acquis) :**

| Cohorte | Mois 0 | Mois 1 | Mois 3 | Mois 6 | Mois 12 |
|---|---|---|---|---|---|
| Mois 4 | 35,20 € | 36,40 € | 38,90 € | 40,80 € | 43,10 € |
| Mois 8 | 35,80 € | 37,10 € | 39,70 € | 41,90 € | 44,20 € |
| Mois 12 | 36,10 € | 37,60 € | 40,30 € | — | — |

Ce que ce tableau dit : les cohortes récentes font **mieux** que les anciennes au même
âge (grâce aux flows mis en place au mois 6 et à l'abonnement). C'est le signe d'une
rétention qui s'améliore. Si les cohortes récentes faisaient **moins bien**, ce serait
une alerte — souvent le signe qu'en scalant, tu acquiers des clients moins fidèles.

---

## 2. L'email et le SMS : les fondations

### 2.1 L'outil

Klaviyo est le standard du DTC sur Shopify ; Omnisend ou Brevo (français) sont des
alternatives. Ce qui compte : une intégration profonde avec Shopify (chaque achat,
chaque produit consulté, chaque panier), la segmentation, et les automatisations.

### 2.2 Construire la liste

- **Une fenêtre d'inscription** sur le site, avec une vraie raison de s'inscrire : une
  remise sur la première commande, un guide utile (« 7 astuces pour faire boire un chat
  difficile »), un tirage au sort. Visée : quelques pourcents des visiteurs.
- **Email et SMS** en deux étapes (email d'abord, puis numéro en option).
- **Au paiement** : case d'inscription.

### 2.3 Le consentement (France et UE)

- **Prospection par email et SMS** : il faut le **consentement préalable** du
  destinataire, sauf exception pour tes **clients existants**, pour des produits
  analogues, s'ils ont été informés et ont pu s'y opposer.
- **Chaque message** contient un moyen simple de se désinscrire.
- **SMS** : les usages professionnels français proscrivent les SMS commerciaux le
  dimanche, les jours fériés et la nuit ; vérifie les règles en vigueur avant tes
  premiers envois.

### 2.4 La délivrabilité : arriver dans la boîte de réception

Depuis 2024, Gmail et Yahoo imposent aux gros expéditeurs : une **authentification** de
ton domaine (SPF, DKIM, DMARC), un **désabonnement en un clic**, et un **taux de
plaintes pour spam** très bas (sous 0,3 %). Concrètement :
- Configure l'authentification **avant** le premier envoi.
- Envoie tes campagnes d'abord aux **abonnés engagés** (ceux qui ont ouvert ou cliqué
  récemment).
- **Nettoie** régulièrement ta liste (flow de fin de vie, section 3).

---

## 3. Les flows : l'argent automatique

Les **flows** sont des séquences déclenchées par un comportement. Ils travaillent jour et
nuit, et représentent souvent **la plus grosse part** du chiffre d'affaires email.

| Flow | Déclencheur | Séquence type | Objectif |
|---|---|---|---|
| **Bienvenue** | Inscription | 4-5 emails sur 7-10 jours : cadeau promis, histoire de la marque, éducation sur le problème, preuve sociale, objections, rappel de l'offre | Première commande |
| **Paiement abandonné** | Paiement commencé, non terminé | +1 h, +24 h, +72 h (et un SMS si consentement) | Récupérer la vente |
| **Panier abandonné** | Ajout au panier sans paiement | +2 h, +24 h | Idem |
| **Navigation abandonnée** | Produit consulté, rien ajouté | +4 h, +48 h | Rappeler, répondre aux doutes |
| **Après achat** | Commande | Confirmation, expédition, mode d'emploi, conseils, demande d'avis, vente croisée | Satisfaction, avis, 2e achat |
| **Réapprovisionnement** | Date prévisible de fin de consommable | Rappel au bon moment + proposition d'abonnement | Réachat |
| **Reconquête** | X jours sans achat | 2-3 emails | Réveiller |
| **Fin de vie** | Aucune ouverture ni clic depuis 120-180 jours | « Tu veux continuer à recevoir nos emails ? » puis suppression | Délivrabilité |
| **VIP** | 3 commandes ou plus | Accès en avant-première, remerciements | Fidélité |

### 3.1 Le flow après achat de Nilo (le plus rentable)

| Jour | Message | But |
|---|---|---|
| J0 | Confirmation + « voici ce qui va se passer » | Rassurer |
| Expédition | Suivi + la vidéo d'installation de 60 s | Préparer l'arrivée |
| Livraison + 1 | « Les 3 astuces pour que ton chat l'adopte » | Éviter les retours |
| Livraison + 7 | « Alors, il l'a adoptée ? » + demande d'avis | Avis |
| Livraison + 14 | « Filme son premier coup de langue » + concours mensuel | Contenus clients |
| Livraison + 21 | Le tapis anti-éclaboussures | Vente croisée |
| J+ (durée du filtre − 3 jours) | « On change le filtre ? » + abonnement −20 % | Réachat et abonnement |

Remarque : **aucun de ces emails n'est une promotion**. Ils sont utiles. C'est pour ça
qu'ils sont ouverts, et c'est pour ça qu'ils vendent.

---

## 4. Les campagnes

Les campagnes sont les envois ponctuels : lancement, contenu, temps forts.

- **Fréquence** : de 1 par semaine au début à 2-4 par semaine à l'échelle, **pour les
  segments engagés**. Moins pour les autres.
- **Contenu** : une majorité de **valeur** (conseils, histoires de clients, coulisses,
  humour de marque), une minorité de **produit**, et les **promotions** réservées aux
  vrais temps forts. Une liste qui ne reçoit que des remises devient une liste qui
  n'achète qu'en remise.
- **Segmentation minimale** : acheteurs / non-acheteurs, engagés 30 / 60 / 90 jours,
  abonnés / non-abonnés, par produit acheté.
- **Tests** : objet, texte simple contre email graphique, heure d'envoi.

---

## 5. L'abonnement

Présenté au module 06. Ce qui fait un abonnement qui dure :

- **La flexibilité** : décaler, sauter un envoi, changer la fréquence, en un clic. Un
  client qui peut **sauter** un envoi ne **résilie** pas.
- **La simplicité de résiliation** : obligatoire en France pour les contrats en ligne,
  et c'est ce qui rend les gens assez confiants pour s'abonner. Tu peux proposer une
  pause ou un décalage **au moment** de la résiliation, sans jamais la rendre plus
  difficile.
- **Le rappel avant chaque envoi.**
- **Des surprises** : un petit cadeau au 3e envoi, un accès en avant-première.

**Mesure l'attrition mensuelle par cohorte d'abonnés.** Rappelle-toi le module 13 du
cursus business : passer de 5 % à 3 % d'attrition mensuelle augmente la durée de vie
moyenne de 67 %.

---

## 6. Fidélité et parrainage

- **Les programmes à points** sont souvent une remise déguisée. Ils marchent pour les
  achats très fréquents ; pour les autres, ils coûtent plus qu'ils ne rapportent.
- **Le parrainage** marche mieux : « Offre 10 € à un ami, reçois 10 € ». Le client
  recruté par un ami est en général plus fidèle et moins cher à acquérir. Mets-le en
  avant dans le flow après achat, au moment où le client est le plus satisfait (après
  l'avis positif).
- **Les attentions** non prévues (une carte manuscrite, un filtre offert) créent plus de
  bouche-à-oreille qu'un barème de points.

---

## 7. Le service client : un outil de rétention

- **Délai de réponse** : moins de 12 heures au début, moins de 4 heures à l'échelle.
  Un client qui attend 3 jours une réponse ouvre un litige bancaire.
- **Le ton de la marque** jusque dans le service client.
- **Le pouvoir de décision** : l'agent peut rembourser ou renvoyer sans escalade jusqu'à
  un montant fixé. Un client bien traité après un problème devient souvent plus fidèle
  qu'un client sans problème.
- **Un outil de support** (Gorgias, Zendesk…) connecté à Shopify, avec des réponses
  préparées pour les questions récurrentes.
- **Les données** : chaque semaine, les 10 motifs de contact les plus fréquents. Ils
  alimentent la page produit (module 07), la FAQ, les flows, et le produit lui-même
  (module 04).
- **Les litiges bancaires** (*chargebacks*) : réponds-y toujours avec les preuves
  (suivi de livraison, échanges). Un taux trop élevé peut entraîner la suspension de tes
  moyens de paiement.

---

## 8. Mesurer honnêtement l'email

Les outils d'emailing attribuent généreusement : un client qui a ouvert un email et
acheté trois jours plus tard (peut-être à cause d'une pub) compte comme « vente email ».
Pour connaître l'**effet réel** d'un flow, garde un **groupe témoin** : 10 % des
personnes éligibles ne le reçoivent pas pendant un mois, puis tu compares leurs achats à
ceux des autres. C'est le même principe d'incrémentalité qu'au module 09.

---

## 9. Fil rouge — La rétention de Nilo au mois 20

| Indicateur | Valeur |
|---|---|
| Taux de réachat à 12 mois | 36 % |
| Part du CA des clients existants | 28 % |
| Abonnés filtres actifs | ≈ 18 000 (≈ 3 000 envois par mois) |
| Part du CA attribuée à l'email et au SMS | 22 % (dont les deux tiers par les flows) |
| Effet réel mesuré du flow après achat (groupe témoin) | +11 % de réachat à 90 jours |
| Délai moyen de première réponse du service client | 3 h 40 |

Ces chiffres expliquent en partie pourquoi le MER de Nilo **tient à 3,1** au mois 20
alors que son CPA marginal a monté : 28 % du chiffre d'affaires arrive sans coût
d'acquisition nouveau.

---

## 10. Les pièges

1. **Attendre d'être gros pour installer les flows.** Ils se mettent en place dès la
   première semaine de ventes.
2. **Envoyer uniquement des promotions.**
3. **Négliger la délivrabilité** : un domaine en spam, c'est un canal mort.
4. **Un abonnement difficile à quitter.**
5. **Croire l'attribution de l'outil d'emailing** sans jamais faire de groupe témoin.
6. **Laisser le service client en retard.** Il te coûte des avis, des litiges et des
   clients.
7. **Regarder la LTV moyenne au lieu des cohortes.**

---

## 11. Devoirs — à rendre dans `exercices/11-rendu.md`

**Exercice 1 — Les flows.** Écris la séquence complète de ton flow de bienvenue (objet,
contenu en 3 lignes, délai) et de ton flow après achat.

**Exercice 2 — Le moment du réachat.** Quel est le moment naturel de réachat de ton
produit (consommable, usure, saison, cadeau) ? Conçois le flow qui l'exploite. Si ton
produit n'a pas de réachat naturel, quel produit complémentaire en créerait un ?

**Exercice 3 — La cohorte.** Construis le tableau de cohortes de ta boutique (ou, si tu
n'as pas encore de ventes, le tableau vide avec les formules, prêt à remplir).

**Exercice 4 — La conformité.** Vérifie ta fenêtre d'inscription, tes formulaires et ton
premier flow contre la section 2.3. Qu'est-ce qui manque ?

**Exercice 5 — Le calcul.** Ta LTV à 12 mois est de 48 € avec 25 % de réachat. Tu passes
à 35 % de réachat, avec une CM2 de 14 € par réachat et 1,6 réachat par client qui
rachète. Quelle est ta nouvelle LTV ? De combien peux-tu augmenter ton CPA cible à marge
égale ?

---

*Module suivant : [12 — Scaler de 10 k€ à 1 M€ par mois](12-scaling-0-a-1m.md).*
