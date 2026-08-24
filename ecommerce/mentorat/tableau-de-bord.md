# Le tableau de bord

> Trois niveaux, trois fréquences, trois usages. Regarder un indicateur mensuel
> tous les jours produit du bruit et des décisions absurdes. Regarder un indicateur
> quotidien une fois par mois laisse une hémorragie courir trente jours.

---

## 1. Les définitions — à écrire avant les chiffres

C'est la partie que tout le monde saute et qui provoque la moitié des désaccords
dans une équipe. Deux personnes qui donnent deux chiffres différents pour la même
question n'ont pas un problème d'outil : elles ont un problème de définition.

Recopie ce tableau, complète la colonne de droite avec **ta** convention, et ne la
change plus. Une définition médiocre mais stable vaut mieux qu'une définition
parfaite qui change en cours d'année : c'est la comparaison dans le temps qui
porte l'information.

| Terme | Définition retenue dans ce cursus | Ta convention |
|---|---|---|
| **CA TTC** | Montant payé par le client, remises déduites, frais de port inclus, **avant** retours | |
| **CA HT** | CA TTC ÷ (1 + taux de TVA moyen pondéré de tes marchés) | |
| **Commande** | Une transaction payée. Un remboursement total l'annule dans le mois où il survient | |
| **Nouveau client** | Première commande payée sous cette adresse e-mail. Jamais « nouveau visiteur » | |
| **Dépense publicitaire** | Tout ce qui achète de l'attention : média, forfaits d'influence, commissions d'affiliation, production créative externalisée. **Pas** les salaires internes | |
| **MER blended** | CA TTC total ÷ dépense publicitaire totale. Aucune attribution n'intervient | |
| **nCAC** | Dépense publicitaire **totale** ÷ nombre de **nouveaux** clients. Pas de nCAC par canal | |
| **Marge brute (CM2)** | CA HT − COGS − logistique − frais de paiement − retours/SAV − remises | |
| **CM3** | Marge brute − dépense publicitaire | |
| **LTV** | Marge de **contribution** cumulée par client acquis. Jamais du chiffre d'affaires. Plafonnée à 12 mois | |
| **Réachat à 90 jours** | Part des clients d'une cohorte ayant passé une 2ᵉ commande dans les 90 jours suivant la 1ʳᵉ | |
| **Concept créatif nouveau** | Angle **ou** mécanisme **ou** format différent. Un nouveau montage du même script n'est pas un concept nouveau, c'est une variation | |
| **Gagnant** | Concept ayant dépassé le budget de test minimal **et** battu le CPA cible sur cette dépense | |

---

## 2. Niveau 1 — quotidien : la survie

**10 minutes. Aucune décision, sauf incident.**

| Indicateur | Ce qu'il détecte | Seuil d'alerte |
|---|---|---|
| Dépense publicitaire de la veille | Emballement ou arrêt d'un compte | Écart > 30 % du budget prévu |
| CA TTC de la veille | Panne de site, de paiement, de suivi | Écart > 2 écarts-types de la moyenne 28 jours |
| Commandes de la veille | Confirme ou infirme les deux précédents | idem |
| MER du jour | Décrochage franc | 3 jours consécutifs sous le MER seuil CM3 |

> **La règle du bruit.** À moins de 100 commandes par jour, une variation
> quotidienne de ±25 % est normale. On n'agit jamais sur un seul jour. On agit sur
> **trois jours consécutifs dans le même sens**, ou sur un écart supérieur à deux
> écarts-types de la moyenne mobile 28 jours. Méthode complète en
> [E09](../modules/E09-mesure-et-incrementalite.md) § 8.
>
> Le nombre de comptes publicitaires cassés par un fondateur qui décidait tous les
> matins dépasse de loin le nombre de comptes sauvés par la même personne.

---

## 3. Niveau 2 — hebdomadaire : la décision

**45 minutes. C'est ici que se prennent les décisions.** Le rituel est décrit dans
[revue-hebdomadaire.md](revue-hebdomadaire.md).

### 3.1 Bloc économie

| Indicateur | Calcul | Seuil d'alerte |
|---|---|---|
| CA TTC | somme de la semaine | — |
| Commandes | somme | — |
| AOV TTC | CA ÷ commandes | Baisse 3 semaines de suite |
| Dépense publicitaire | somme | — |
| **MER blended** | CA TTC ÷ dépense | **Sous le MER seuil CM3** |
| Nouveaux clients | comptés | — |
| **nCAC** | dépense ÷ nouveaux clients | Hausse > 20 % à exécution constante |
| Taux de marge brute | CM2 ÷ CA HT | Baisse > 1,5 point |
| **CM3 en €** | marge brute − dépense pub | **Négatif** |

### 3.2 Bloc machine créative — le plus prédictif

| Indicateur | Seuil d'alerte |
|---|---|
| Concepts **nouveaux** testés cette semaine | Sous le seuil de ton palier ([jalons](jalons.md)) |
| Concepts devenus gagnants (4 dernières semaines) | Zéro sur 4 semaines |
| Gagnants distincts en rotation | < 3 |
| Âge du concept qui porte le plus de dépense | > 10 semaines |
| Part de la dépense sur des concepts de moins de 60 jours | < 40 % |

> Ce bloc prédit ta performance **des six prochains mois**, pas celle de la
> semaine. C'est exactement pour ça qu'on l'oublie : rien ne se dégrade le jour où
> on arrête de tester. Tout se dégrade six mois plus tard, quand la cause est
> devenue invisible.

### 3.3 Bloc rétention et cash

| Indicateur | Seuil d'alerte |
|---|---|
| Part du CA en réachat | Baisse 3 semaines de suite |
| Commandes de réachat | — |
| Trésorerie disponible | — |
| **Semaines de trésorerie restantes** | **< 13** |
| Jours de stock du produit héros | < délai de réapprovisionnement + sécurité |

---

## 4. Niveau 3 — mensuel : la structure

**2 heures. On ne cherche pas la performance, on cherche la dérive.**

| Indicateur | Ce qu'il révèle | Seuil d'alerte |
|---|---|---|
| **Tableau de cohortes** (commandes cumulées par client, par mois d'acquisition) | La qualité des clients que tu achètes | Cohortes récentes sous les anciennes au même âge |
| LTV 12 mois par cohorte | La valeur réelle d'un client | Baisse 2 cohortes de suite |
| LTV/CAC 12 mois | La marge de manœuvre d'acquisition | < 1,5 → on répare. > 5 → on sous-investit |
| Payback en mois | Ce que ta trésorerie peut financer | > 4 mois |
| EBITDA réel et en % du CA HT | La vérité | Sous l'objectif du palier |
| BFR et BFR en jours de CA | Le cash absorbé par la croissance | Hausse plus rapide que le CA |
| Taux de retour | La qualité du trafic et des attentes créées | +1 point |
| Taux de remise | La discipline commerciale | +1 point |
| Part du canal publicitaire principal | Le risque de ruine | > seuil du palier ([jalons](jalons.md)) |
| CA HT annuel par ETP | La productivité de la structure | Baisse 2 mois de suite |

> **Les deux lignes qui tuent silencieusement** sont le taux de retour et le taux
> de remise. Elles montent d'un demi-point par trimestre sans que personne ne le
> décide, et au bout de deux ans elles ont mangé la moitié de l'EBITDA. Dans le
> modèle de référence, un seul point de taux de retour en moins vaut **433 320 €
> d'EBITDA annuel** au palier P5
> ([canoniques § 7](../donnees/chiffres-canoniques.md)).

---

## 5. Le tableau à remplir chaque semaine

```
SEMAINE ____  du __/__ au __/__        Palier visé : P__

ÉCONOMIE                    Cette sem.   S−1     S−4    Alerte ?
  CA TTC ...................  _______  _______  _______   ☐
  Commandes ................  _______  _______  _______   ☐
  AOV TTC ..................  _______  _______  _______   ☐
  Dépense publicitaire .....  _______  _______  _______   ☐
  MER blended ..............  _______  _______  _______   ☐
  MER seuil CM3 (1,20÷CM2) .  _______                     ☐
  Nouveaux clients .........  _______  _______  _______   ☐
  nCAC .....................  _______  _______  _______   ☐
  Taux de marge brute CM2 ..  _______  _______  _______   ☐
  CM3 en € .................  _______  _______  _______   ☐

MACHINE CRÉATIVE
  Concepts NOUVEAUX testés .  _______  _______  _______   ☐
  Gagnants (4 dern. sem.) ..  _______                     ☐
  Gagnants en rotation .....  _______                     ☐
  Âge du plus gros porteur .  ____ sem.                   ☐
  Part dépense < 60 jours ..  _______                     ☐

RÉTENTION ET CASH
  Part du CA en réachat ....  _______  _______  _______   ☐
  Trésorerie disponible ....  _______                     ☐
  Semaines de trésorerie ...  _______                     ☐
  Jours de stock (héros) ...  _______                     ☐

LE SEUL CHANTIER DE LA SEMAINE PROCHAINE
  ______________________________________________________________
  Indicateur qui dira si ça a marché : ___________________________
  Seuil écrit d'avance : _________________________________________
```

---

## 6. Comment construire ce tableau sans y passer ta vie

Par ordre de préférence :

1. **Un tableur, à la main, 20 minutes par semaine.** C'est ce que je recommande
   jusqu'à P3 inclus. Remplir à la main force à regarder les chiffres, ce qu'un
   tableau de bord automatique ne fait pas.
2. **Un tableur alimenté par exports.** Extraction hebdomadaire depuis ta
   plateforme de vente et tes régies, collée dans le même classeur.
3. **Un outil de visualisation branché sur ta base.** À partir de P4, quand
   plusieurs personnes ont besoin du même chiffre au même moment.

Quel que soit l'outil : **une seule source de vérité**. Si le chiffre d'affaires de
la semaine existe à trois endroits différents, il y aura trois valeurs, et les
réunions porteront sur la réconciliation au lieu de porter sur la décision.

> **À retenir :** un tableau de bord ne sert pas à savoir comment ça va. Il sert à
> déclencher **une** décision par semaine. S'il ne débouche sur aucune décision
> pendant un mois, il est trop long — supprime des lignes.

---

*Suite : le [rituel de revue hebdomadaire](revue-hebdomadaire.md), qui transforme
ce tableau en décision.*
