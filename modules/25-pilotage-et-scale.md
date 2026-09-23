# Module 25 — Pilotage et scale : le système d'exploitation quotidien

> **Prérequis :** modules 13 (unit economics), 20 (tracking), 24 (CRO).
> **Objet :** savoir quoi regarder, à quelle fréquence, et quelle décision prendre.
> Ce module remplace l'intuition par une procédure.

---

## 0. Le problème que ce module résout

Un acheteur média prend 30 à 200 décisions par semaine. Sans procédure écrite, chacune
est prise sous l'influence du dernier chiffre vu, de l'humeur, et surtout de
**l'aversion à la perte** (module 6) : on coupe les gagnantes trop tôt par peur de
rendre le gain, et on garde les perdantes trop longtemps pour ne pas acter la perte.

C'est exactement à l'envers de ce qu'il faut faire. **La procédure n'existe pas pour
être intelligente. Elle existe pour te protéger de toi-même.**

---

## 1. Les sept chiffres du tableau de bord

| Chiffre | Formule | Fréquence | Ce qu'il décide |
|---|---|---|---|
| **Dépense** | — | Quotidienne | Le rythme |
| **CPA** | dépense / conversions | Quotidienne | Couper / garder |
| **ROAS média** | CA / dépense média | Quotidienne | Le pilotage de campagne |
| **MER** | CA total / dépense média totale | Hebdo | La santé réelle |
| **Marge de contribution** | CA − COGS − média − frais | Hebdo | **Le seul chiffre qui compte** |
| **Payback** | jours pour récupérer le CAC | Mensuel | La vitesse de scale possible |
| **CAC marginal** | Δ dépense / Δ nouveaux clients | Hebdo | **La décision de scaler** |

### 1.1 MER contre ROAS : la distinction qui évite les catastrophes

```
ROAS plateforme = ce que Meta s'attribue        ← optimiste, dédoublé, court-termiste
MER             = CA TOTAL / dépense média TOTALE  ← inattaquable
```

Le MER n'a aucune finesse — il ne te dit pas quelle campagne couper. Mais **il ne ment
jamais**, parce que le numérateur est ton chiffre d'affaires réel et le dénominateur ta
dépense réelle. Quand le ROAS affiché monte et que le MER baisse, ton tracking te
raconte une histoire. Crois le MER.

**Le seuil de MER dont tu as besoin :**
```
MER minimum = 1 / (marge brute en % − marge nette visée en %)
Exemple : 70 % de marge brute, 20 % de marge nette visée → MER ≥ 2,0
```

### 1.2 Le CAC marginal : le chiffre que 90 % des gens ignorent

Le CAC moyen te ment quand tu scales. Ce qui compte, c'est le coût du **client
supplémentaire**.

| Semaine | Dépense | Clients | CAC moyen | **CAC marginal** |
|---|---|---|---|---|
| 1 | 10 000 € | 400 | 25 € | — |
| 2 | 15 000 € | 550 | 27 € | **33 €** |
| 3 | 20 000 € | 650 | 31 € | **50 €** |

Le CAC moyen semble tenir (25 → 31 €). Le CAC marginal a doublé. **Les 5 000 € ajoutés
en semaine 3 ont acheté des clients à 50 €.** Si ton plafond est à 35 €, cette
tranche-là perd de l'argent — et elle est masquée par la moyenne.

> **Règle de scale :** tu montes tant que `CAC marginal < CPA plafond`.
> Tu t'arrêtes le jour où ce n'est plus vrai, pas le jour où la moyenne décroche.
> Quand la moyenne décroche, tu as déjà brûlé plusieurs semaines.

---

## 2. Les rythmes : quotidien, hebdomadaire, mensuel

### 2.1 Le rituel quotidien (20 minutes, pas plus)

```
1. Dépense d'hier conforme au plan ?              [oui/non]
2. MER d'hier au-dessus du seuil ?                [oui/non]
3. Créas au-dessus de 2× le CPA cible sans vente  → COUPER
4. Créas à ≥ 10 conversions sous le CPA cible     → +20 % de budget
5. Anomalies : CPM qui bondit, taux de clic effondré, page HS ?
6. Nouvelles créas lancées aujourd'hui : combien ? (objectif du module 22)
```

**Ce que tu ne fais PAS tous les jours :** changer les enchères, modifier les audiences,
réécrire les pages, réagir à une mauvaise matinée. Chaque modification relance
l'apprentissage de l'algorithme et coûte 24 à 72 h de performance dégradée.

> **La règle des 3 jours :** ne juge jamais une campagne sur moins de 3 jours,
> sauf catastrophe évidente (0 conversion à 3× le CPA cible).

### 2.2 Le rituel hebdomadaire (90 minutes)

- Marge de contribution réelle de la semaine — **encaissements moins décaissements**,
  pas le tableau de bord.
- CAC marginal de la semaine contre la précédente.
- Taux de succès créatif : combien lancées, combien retenues ?
- Fatigue : fréquence, CTR, CPM par campagne — trajectoires, pas niveaux.
- Concurrence : 20 minutes dans les bibliothèques publicitaires. Qu'est-ce qui est neuf ?
- Trésorerie à 30 jours : encaissements attendus, dépenses engagées, point bas.
- **Une décision structurelle par semaine.** Une seule : un test d'offre, un nouveau
  tunnel, une nouvelle source. Sinon tu ne fais que du réglage, et le réglage a un
  rendement ×1,05 (module 19, § 5).

### 2.3 Le rituel mensuel (une demi-journée)

- Cohortes : les clients de janvier valent-ils plus à J+60 que ceux de décembre ?
- Payback réel par source.
- Taux de remboursement et de chargeback par offre. **Trajectoire.**
- Concentration : quelle part du CA sur la source n° 1 ? sur l'offre n° 1 ?
- Revue du dossier de tests (asymétrie A4) : qu'as-tu appris ce mois-ci qui est
  généralisable ?
- Risque : comptes, réserves PSP, conformité, stock.

---

## 3. Scaler : les quatre méthodes et quand les employer

### 3.1 Vertical — augmenter le budget

- **+20 % tous les 2 à 3 jours** en régime normal. La limite n'est pas technique :
  c'est que l'algorithme repasse en phase d'apprentissage au-delà de ~20-30 % de
  variation, et l'apprentissage coûte de la performance.
- On peut aller plus vite (+50 à 100 %/jour) sur une créa qui tient depuis une semaine
  avec un volume confortable. Accepte alors 2 à 3 jours de CPA dégradé.
- **Plafond réel :** l'audience s'épuise. Le signal est la fréquence qui monte pendant
  que le CTR baisse et que le CPM monte. À ce stade, le vertical ne donne plus rien.

### 3.2 Horizontal — dupliquer

Nouvelles audiences, nouvelles géos, nouveaux placements, nouvelles campagnes avec
les mêmes créas. C'est ce qui donne le plus de volume sans dégrader le CPA — et c'est
la méthode principale au-delà de 5 000 €/jour.

### 3.3 Créatif — le seul scale vraiment illimité

Plus de créas, plus d'angles, plus de formats. **C'est le seul levier qui augmente le
volume sans augmenter le coût unitaire**, parce que chaque nouvel angle ouvre une
poche d'audience que les précédents n'atteignaient pas. C'est pour ça que le module 22
insiste autant sur le débit.

### 3.4 Structurel — scaler la monétisation

Améliorer l'offre, ajouter un upsell, augmenter la LTV. Tu ne scales pas la dépense :
tu **augmentes le plafond** de dépense soutenable. Rendement le plus élevé, délai le
plus long.

```
Ordre de priorité quand tu veux plus de volume :
1. Créatif  (rapide, illimité)
2. Horizontal (rapide, large)
3. Structurel (lent, meilleur rendement)
4. Vertical (facile, plafonné, dégrade le CPA)
```

**Le réflexe de tout le monde est le 4.** C'est le moins bon.

---

## 4. Quand tout se dégrade : le protocole de diagnostic

Ton CPA a doublé du jour au lendemain. Dans l'ordre, et **une cause à la fois** :

```
1. TRACKING        Le pixel fonctionne ? Le postback arrive ? La page charge ?
                   → 30 % des « effondrements » sont un problème technique.
                     Vérifie ÇA en premier, toujours, avant de toucher à quoi que ce soit.

2. OFFRE/PAGE      Rupture de stock ? PSP qui refuse des cartes ? Page lente ?
                   Un checkout cassé ressemble exactement à une campagne morte.

3. CONCURRENCE     Un concurrent a lancé ? Les CPM du marché ont monté ?
                   Regarde le CPM : s'il a monté et que ton CTR est stable,
                   c'est le marché, pas toi.

4. FATIGUE CRÉA    Fréquence en hausse + CTR en baisse = saturation d'audience.
                   → Nouvelles créas, pas nouveaux réglages.

5. PLATEFORME      Mise à jour d'algorithme, changement de règles, restriction de compte.

6. SAISONNALITÉ    Périodes de forte demande (Black Friday, fêtes) = +40 à 120 % de CPM.
                   Ce n'est pas ta campagne qui est mauvaise, c'est l'enchère qui est chère.
```

**Ne change qu'une chose à la fois.** Un diagnostic dans lequel tu as modifié cinq
paramètres simultanément ne produit aucune connaissance — et tu revivras le même
problème dans trois semaines.

---

## 5. Les règles d'arrêt, écrites à l'avance

Le moment où tu décides est le pire moment pour décider : tu es engagé, tu as dépensé,
tu espères. **Écris ces seuils quand tu es calme, et respecte-les.**

| Situation | Règle écrite |
|---|---|
| Nouvelle offre | Budget de test = 3× le CPA cible. Zéro conversion → stop. |
| Nouvelle source | Budget d'apprentissage écrit et daté. Atteint sans rentabilité → stop. |
| Créa | 2× CPA cible sans conversion → coupée. Aucune exception. |
| Campagne qui décroche | 3 jours consécutifs au-dessus du plafond → pause, diagnostic §4. |
| Perte cumulée | Seuil mensuel de perte maximale. Atteint → tout est mis en pause 48 h. |
| Offre en fin de vie | Marge en baisse 3 semaines de suite malgré des créas neuves → chercher la suivante. |

> **La règle des 48 heures.** Quand tu atteins ton seuil de perte mensuelle, tu mets
> tout en pause pendant 48 h. Pas pour réfléchir : pour sortir de l'état mental
> d'engagement. La quasi-totalité des ruines de ce métier vient d'une séquence de
> décisions prises en poursuivant des pertes.

---

## 6. Les paliers : ce qui change à chaque échelle

| Dépense/jour | La contrainte dominante | Ce qu'il faut ajouter |
|---|---|---|
| **0–100 €** | Ta connaissance | Tester, lire, échouer vite. N'engage rien. |
| **100–1 000 €** | Le débit de créa | 15–30 créas/semaine, tracker propre |
| **1 000–5 000 €** | La trésorerie et les comptes | BFR, comptes de secours, 1ᵉʳ éditeur vidéo |
| **5 000–20 000 €** | La structure d'équipe | Média buyer ou créa à temps plein, process écrits |
| **20 000 €+** | Le risque et la conformité | Juridique, PSP multiples, diversification, contrôle interne |

**Le franchissement de palier tue plus que le palier lui-même.** À chaque saut, la
contrainte change de nature, et ce qui t'a amené là cesse de fonctionner. La plupart
des affiliés qui « explosent » puis disparaissent ont scalé leur dépense sans scaler
ni leur trésorerie, ni leur débit créatif, ni leur gestion du risque.

---

## 7. Limites

1. **Toute cette mesure est du dernier clic.** Module 10 : elle surévalue le bas du
   tunnel. Garde 10 à 20 % du budget hors procédure, en exploration.
2. **Optimiser exactement les bons chiffres te mène à un maximum local.** Les gains
   ×5 viennent de changements que le tableau de bord ne suggère jamais : une autre
   offre, un autre marché, un autre modèle. La procédure sert à ne pas mourir ;
   elle ne sert pas à trouver la prochaine grosse chose.
3. **La rapidité peut battre la justesse.** Sur une opportunité courte (A1/A2 du
   module 19), celui qui décide vite avec 70 % d'information bat celui qui attend
   la significativité statistique. Sache quand tu es dans ce régime — et sache que
   la plupart du temps, tu n'y es pas.

---

## 8. Exercice 25

À rendre dans `exercices/25-rendu.md`.

1. **Construis ton tableau de bord** avec les 7 chiffres du § 1. Un onglet, pas dix.
2. **Calcule ton MER minimum** à partir de ta marge brute réelle.
3. **Calcule ton CAC marginal** sur tes 3 dernières semaines. **Est-il sous ton plafond ?**
4. **Écris tes six règles d'arrêt** (§ 5) avec des nombres, pas des adjectifs.
   Affiche-les là où tu travailles.
5. **Écris ton rituel quotidien en 6 lignes** et tiens-le 14 jours sans y déroger.
   Note ce que tu as eu envie de faire hors procédure, et si tu avais raison.
