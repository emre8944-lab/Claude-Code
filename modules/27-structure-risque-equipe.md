# Module 27 — Structure, risque et équipe : ce qui te garde en vie

> **Prérequis :** modules 19, 25, 26.
> **Objet :** l'infrastructure invisible. C'est elle qui décide si une bonne année
> devient une décennie ou un souvenir.

---

## 0. Les trois façons de mourir dans ce métier

Personne ne meurt d'un mauvais CPA. On meurt de trois choses, toujours les mêmes :

```
1. LA TRÉSORERIE   Tu gagnes, mais l'argent arrive après la dépense.
2. LE COMPTE       Publicitaire ou marchand. Coupé du jour au lendemain.
3. LE RISQUE JURIDIQUE  Accumulé silencieusement pendant 18 mois, puis exigible.
```

Les trois ont une propriété commune : **ils frappent au meilleur moment, pas au pire.**
C'est en scalant que le BFR explose, que les plateformes te regardent, et que tu
deviens une cible qui vaut la peine d'être poursuivie.

---

## 1. Le paiement : ton organe vital

### 1.1 L'anatomie

```
Client → PSP (Stripe, Adyen, PayPal, Checkout.com)
       → Acquéreur (la banque qui porte le risque)
       → Réseaux de carte (Visa / Mastercard) ← ce sont EUX qui fixent les seuils
```

L'acquéreur porte le risque de tes remboursements. Si tu disparais avec des commandes
non livrées, c'est lui qui rembourse. **Donc il te traite comme un débiteur, pas comme
un client.** Tout son comportement découle de là, et ça explique la réserve roulante,
les demandes de documents, et les résiliations brutales.

### 1.2 Les seuils à connaître par cœur

| Indicateur | Seuil d'alerte | Seuil de sortie |
|---|---|---|
| **Taux de chargeback** | 0,65 % | **0,9 % (VAMP Visa) / 1 % soutenu → résiliation** |
| **Taux de remboursement** | 5 % | 10 % attire un audit |
| **Ratio litiges gagnés** | < 20 % | Signal de fond : le problème est ton offre |

**Le taux de chargeback est le chiffre le plus important de ton entreprise, et c'est
celui que personne ne regarde avant qu'il soit trop tard.** Mets-le sur ton tableau
de bord hebdomadaire (module 25) dès la première vente.

### 1.3 Réduire les chargebacks : par ordre d'efficacité

1. **Un descripteur de relevé bancaire reconnaissable**, avec un numéro de téléphone.
   La première cause de chargeback est « je ne reconnais pas ce prélèvement ».
   Ce point seul enlève 20 à 40 % des litiges. C'est gratuit.
2. **Un SAV qui répond en moins de 24 h et rembourse sans discuter.**
   Un remboursement coûte le produit. Un chargeback coûte le produit + 15 à 40 € de
   frais + un point de ratio. **Rembourse toujours plutôt que de discuter.**
3. **Un email de confirmation immédiat** avec ce qui a été acheté, le montant,
   la récurrence s'il y en a une, et comment annuler.
4. **Un rappel avant chaque prélèvement récurrent.**
5. **Des délais de livraison tenus et communiqués.** Un colis en retard sans
   information devient un litige au jour 12.
6. **Ethoca / RDR** (alertes de litige, remboursement automatique avant chargeback)
   dès que tu dépasses ~100 k€/mois.

### 1.4 La réserve roulante

Le PSP retient 5 à 15 % de tes encaissements pendant 60 à 180 jours. Sur 500 k€/mois
à 10 % sur 6 mois, cela immobilise **300 000 €**. C'est un coût de financement réel
que presque personne ne fait figurer dans ses unit economics.

**Conséquence opératoire :** ouvre un deuxième PSP **avant** d'en avoir besoin.
Un compte marchand se prépare en 3 à 8 semaines quand tout va bien, et jamais quand
tu viens d'être résilié — parce que tu figures alors sur la liste MATCH/TMF de
Mastercard, où l'on reste cinq ans et qui rend l'ouverture d'un nouveau compte très
difficile.

---

## 2. La trésorerie : le tueur silencieux

```
BFR ≈ dépense média quotidienne × délai d'encaissement
    + stock en transit
    + réserve PSP
```

Exemple à 5 000 €/jour, paiement réseau à 45 jours, réserve à 10 % sur 6 mois :

```
Média en attente :  5 000 × 45          = 225 000 €
Réserve PSP      :  ~10 % × 6 mois de CA ≈ 150 000 €
Stock            :  ~30 jours de ventes  ≈  90 000 €
                                     ──────────────
Trésorerie immobilisée en permanence   ≈ 465 000 €
```

Pour 5 000 €/jour de dépense — un niveau que beaucoup atteignent en dix-huit mois.
**C'est la vraie barrière du métier**, et c'est pour ça que le ralentissement volontaire
est parfois la décision la plus rentable.

**Les leviers, par ordre de préférence :**
1. Négocier le paiement hebdomadaire avec le réseau (possible dès 3 mois de volume propre).
2. Négocier le délai fournisseur / le stock en consignation.
3. Cartes à paiement différé pour le média (gain de 15 à 45 jours, gratuit).
4. Financement de créances / affacturage : cher (2–6 %/mois) mais moins cher
   que l'arrêt de la croissance.
5. **Ralentir.** C'est un levier, pas un aveu d'échec. Une activité qui croît de 15 %
   par mois en autofinancement survit ; une qui croît de 60 % à crédit saute au
   premier accident.

> **La règle du point bas.** Chaque semaine, projette ta trésorerie à 30 jours et
> note le point le plus bas. **Si ce point passe sous un mois de charges fixes,
> tu ne scales pas cette semaine, quelle que soit la performance de tes campagnes.**

---

## 3. La structure juridique et la conformité

### 3.1 Le cloisonnement

Le principe : **aucun événement unique ne doit pouvoir tout emporter.**

```
Holding
 ├── Société A — verticale 1, PSP 1, comptes pub 1
 ├── Société B — verticale 2, PSP 2, comptes pub 2
 └── Société C — actifs (marques, domaines, listes, code)
```

Ce n'est pas de l'optimisation fiscale, c'est de la gestion de risque. Quand le
verticale 1 se durcit, le verticale 2 continue. Et les actifs (ta liste email, tes
marques) ne sont pas exposés au risque d'exploitation.

**Ne monte pas cette structure au premier jour** — c'est du coût et de la complexité
pour rien. Monte-la quand tu as deux activités rentables ou que tu dépasses
~30 k€/mois de marge.

### 3.2 Les obligations qu'on découvre trop tard

| Domaine | L'obligation | La sanction |
|---|---|---|
| **RGPD** | Base légale, registre, consentement prouvé, DPA avec les sous-traitants | Jusqu'à 4 % du CA mondial |
| **Cookies** | Consentement préalable réel, refus aussi simple que l'accord | CNIL, amendes régulières à 7 chiffres |
| **Droit de rétractation** | 14 jours, formulaire type, remboursement sous 14 jours | Nullité + amende |
| **Résiliation en ligne** | Bouton de résiliation obligatoire (L215-1-1) | Amende administrative |
| **Identification de la publicité** | Toute communication commerciale identifiable | Pratique trompeuse |
| **Influence** | Mention du partenariat (loi du 9 juin 2023) | 2 ans, 300 000 € |
| **Claims** | Santé (règl. 1924/2006), environnement, prix barrés | Pratique trompeuse |
| **TVA / OSS** | TVA au taux du pays du client au-delà de 10 k€ de ventes UE | Redressement + intérêts |

Le point à retenir : **ces obligations sont bon marché à respecter et très chères à
rattraper.** Un tunnel conforme coûte deux jours de travail. Un redressement TVA sur
trois ans de ventes européennes, ça se chiffre en centaines de milliers d'euros.

### 3.3 Le moment de prendre un avocat

Repère simple : **dès 20 k€/mois de chiffre d'affaires**, une revue de conformité
(2 000 à 5 000 €) sur ton tunnel, tes CGV, ton traitement de données et tes claims.
C'est la dépense au meilleur rendement de tout ce module, parce qu'elle achète la
seule chose que tu ne peux pas acheter après coup : l'antériorité de la conformité.

---

## 4. L'équipe lean : qui, dans quel ordre

Le principe : **tu recrutes toujours sur ton goulot d'étranglement, jamais sur ton
confort.** Le goulot se déplace, l'ordre ci-dessous suit ce déplacement.

| Ordre | Poste | Seuil de déclenchement | Ce qu'il débloque | Coût indicatif |
|---|---|---|---|---|
| 1 | **Éditeur vidéo / créa** | 3 000 €/mois de marge | Le débit créatif — ton vrai goulot | 800–2 500 €/mois |
| 2 | **Acteurs UGC** (à la mission) | Dès le début | La matière première des tests | 80–250 €/vidéo |
| 3 | **SAV / support** | 50 commandes/jour | Chargebacks ↓, temps ↑ | 600–1 500 €/mois |
| 4 | **Média buyer junior** | 5 000 €/jour de dépense | Ton temps pour la stratégie | 2 000–4 000 € + variable |
| 5 | **Créa/angle strategist** | 10 000 €/jour | L'industrialisation des angles | 3 000–6 000 € |
| 6 | **Data / analyste** | 15 000 €/jour | Les décisions justes à l'échelle | 3 000–6 000 € |
| 7 | **Ops / finance** | 30 000 €/jour | Trésorerie, PSP, conformité | 3 000–6 000 € |

**Les trois erreurs de recrutement du secteur :**

1. **Recruter un média buyer en premier.** C'est le réflexe, et c'est faux : le goulot
   n'est presque jamais l'achat, c'est la créa. Un média buyer sans flux de créas
   neuves ne fait que du réglage — rendement ×1,05 (module 19).
2. **Recruter avant d'avoir un process écrit.** Si tu ne peux pas écrire ce que tu fais
   chaque jour, tu ne peux pas le déléguer ; tu vas juste payer quelqu'un pour te
   regarder travailler.
3. **Recruter en haut de cycle.** Une équipe de 8 personnes calibrée sur une offre qui
   meurt en trois mois, c'est une structure de coût fixe adossée à un revenu variable.
   **Garde tes coûts fixes sous 15 % de ta marge de contribution.** Sous-traite, paie
   à la mission, indexe sur la performance.

### 4.1 La structure type à 50 k€/mois de marge nette

```
Toi          : offres, angles, arbitrages, réseaux, risque
Créa (1–2)   : montage, déclinaisons, UGC
Buyer (1)    : exécution quotidienne, rituels du module 25
SAV (1, ext.): support, remboursements, avis
Externes     : comptable, avocat, acteurs UGC, développeur ponctuel
```

Cinq personnes. **Le métier ne demande pas de grosses équipes** — il demande un débit
créatif élevé et des décisions justes. C'est pour ça que les structures qui gagnent
sont petites et restent petites.

---

## 5. La pile d'outils, par palier

| Palier | Outils | Coût/mois |
|---|---|---|
| **Démarrage** | Shopify ou un builder de pages, pixel + CAPI, Google Sheets, Canva/CapCut | 50–150 € |
| **1–10 k€/mois** | + Tracker (Binom/RedTrack), outil email/SMS, outil d'upsell, tableur structuré | 200–500 € |
| **10–50 k€/mois** | + Outil de veille créa, outil de tests, outil d'avis, gestion des litiges | 500–1 500 € |
| **50 k€+** | + Entrepôt de données, alertes de litige (Ethoca/RDR), PSP secondaire, automatisations | 2 000–5 000 € |

**Règle :** un outil s'achète pour résoudre un goulot **déjà identifié et mesuré**.
La pile d'outils sophistiquée sans campagne rentable est la forme la plus répandue
de procrastination du métier.

---

## 6. Limites

1. **Toute cette infrastructure a un coût en vitesse.** Des process, des contrôles, une
   équipe : c'est plus lent qu'un individu seul qui décide en dix secondes. Le bon
   dosage dépend de ce que tu as à perdre — construis l'infrastructure **juste avant**
   d'en avoir besoin, pas trois ans avant.
2. **Le cloisonnement a une limite légale.** Séparer les risques d'exploitation entre
   entités est légitime ; créer des sociétés écrans pour échapper à ses obligations
   envers des clients ou des créanciers ne l'est pas et peut engager ta responsabilité
   personnelle. La différence est l'intention, et elle se lit très bien dans les actes.
3. **Rien de ce module ne remplace une offre qui marche.** Une infrastructure parfaite
   autour d'une offre médiocre est une manière très propre de perdre de l'argent.
   L'ordre reste : offre → créa → tunnel → **puis** structure.

---

## 7. Exercice 27

À rendre dans `exercices/27-rendu.md`.

1. **Projette ta trésorerie à 90 jours** au rythme de scale que tu vises, avec BFR,
   réserve PSP et stock. Note le point bas. **S'il est négatif, ton plan de scale est
   faux, pas ambitieux.**
2. **Écris ton plan « mon compte principal saute demain » :** que fais-tu à H+1,
   J+1, J+7 ? Quels actifs as-tu déjà en secours ?
3. **Passe en revue les 8 obligations du § 3.2** sur ton tunnel actuel.
   Combien sont respectées ? Corrige les plus faciles cette semaine.
4. **Mesure ton taux de chargeback et ton taux de remboursement.** Si tu ne peux pas
   les mesurer, c'est ton chantier n° 1 avant tout le reste.
5. **Identifie ton goulot actuel** en une phrase, et le premier recrutement (ou la
   première externalisation) qui le lève. Si tu ne sais pas nommer le goulot,
   ne recrute personne.
