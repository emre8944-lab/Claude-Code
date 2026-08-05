# Module 13 — Les chiffres qui décident : CAC, LTV, payback

> **Prérequis :** modules 1, 12, 10.
> **Objet :** te donner les six chiffres qui déterminent si ton activité gagne de
> l'argent, et les cinq pièges qui font que la plupart des gens calculent faux.

---

## 0. Pourquoi ce module vient après les deux autres

Hopkins te dit d'optimiser le coût par client. Sharp te dit que ce coût ment sur l'effet
réel. Les deux ont raison. **Le seul moyen d'arbitrer entre eux, au lieu d'en débattre,
est de savoir compter.**

Et il y a une raison plus profonde. Reviens au module 1 : ton revenu est le prix d'une
asymétrie. Les unit economics sont l'instrument qui mesure cette asymétrie et sa
durabilité.

- **LTV / CAC > 1** signifie : j'ai trouvé une asymétrie que le marché paie.
- **CAC qui monte plus vite que LTV** signifie : mon asymétrie se referme.

Les deux stratégies du module 1 se lisent directement dans ces chiffres. La stratégie
d'arbitrage (exploiter) se reconnaît à un CAC qui monte inexorablement — l'information se
diffuse. La stratégie de moat (créer) se reconnaît à une LTV qui monte. **Regarde la
trajectoire, pas le niveau.**

---

## 1. Les six chiffres

### 1.1 La marge de contribution — le seul chiffre d'affaires qui existe

Tout le monde raisonne en chiffre d'affaires. C'est l'erreur fondatrice.

```
Marge de contribution par vente
  = Prix de vente
  − coûts directement liés à cette vente
    (matière, sous-traitance, temps de livraison, commissions,
     frais de paiement, hébergement variable, SAV)
```

**Tout ce qui suit se calcule sur la marge de contribution, jamais sur le prix.** Une
entreprise qui compare son coût d'acquisition à son chiffre d'affaires se croit rentable
alors qu'elle achète des clients à perte.

### 1.2 Le CAC — coût d'acquisition client, entièrement chargé

```
CAC = (dépenses publicitaires
     + coût du temps commercial
     + outils et logiciels d'acquisition
     + salaires marketing
     + commissions d'apporteurs)
      ÷ nombre de NOUVEAUX clients de la période
```

Deux erreurs quasi universelles :

- **Ne compter que la dépense média.** Si tu passes trois heures par semaine à répondre à
  des prospects, ce temps a un coût. Chiffre-le à ton taux horaire réel.
- **Diviser par tous les clients au lieu des nouveaux.** Le CAC ne concerne que
  l'acquisition. Les réachats n'ont rien à y faire.

### 1.3 La LTV — valeur vie client, en marge

Deux formules selon ton modèle.

**Modèle transactionnel** (services, e-commerce, prestations) :

```
LTV = marge de contribution moyenne par commande
      × nombre moyen de commandes sur la durée de vie du client
```

**Modèle par abonnement** :

```
LTV = (revenu mensuel moyen par client × taux de marge de contribution)
      ÷ taux d'attrition mensuel
```

Le taux d'attrition (*churn*) est au dénominateur, donc **c'est le terme qui domine tout**.
Passer de 5 % à 3 % d'attrition mensuelle ne fait pas gagner 2 % : ça fait passer la durée
de vie de 20 à 33 mois, soit **+67 % de LTV**. Aucun levier d'acquisition n'a ce rendement.

> **Règle :** avant de dépenser un euro de plus en acquisition, regarde ton attrition.
> C'est presque toujours là que se trouve l'argent le moins cher.

### 1.4 Le ratio LTV / CAC

```
Ratio = LTV ÷ CAC
```

Les repères usuels :

| Ratio | Lecture |
|---|---|
| **< 1** | Tu perds de l'argent à chaque client. Arrête l'acquisition immédiatement. |
| **1 à 2** | Tu es rentable sur le papier mais tu ne couvres pas tes frais fixes. Fragile. |
| **≈ 3** | Zone saine dans la plupart des activités. |
| **> 5** | Tu sous-investis probablement en acquisition. Tu laisses de la croissance sur la table. |

**Pourquoi 3 et pas 1,5 ?** Ce n'est pas une loi, c'est une provision pour trois
incertitudes : ta LTV est une estimation qui se révélera optimiste ; tes frais fixes ne
sont pas dans le calcul ; et ton CAC va monter quand tu grandiras (section 2.2). Le
coefficient 3 absorbe ces trois erreurs. Si tu as des données longues et fiables sur des
cohortes réelles, tu peux descendre. Sinon, garde-le.

### 1.5 Le délai de récupération (*payback*) — le chiffre qui te tue ou te sauve

```
Payback = temps nécessaire pour que la marge cumulée d'un client
          rembourse son coût d'acquisition
```

**C'est le chiffre le plus important pour toi, et presque personne ne le regarde.**

Raison : *les entreprises ne meurent pas d'être non rentables, elles meurent de manquer de
trésorerie.* Un LTV/CAC de 4 avec un payback à 20 mois te met en faillite avant d'avoir
touché le gain, parce que tu finances 20 mois d'acquisition avant le premier euro
récupéré.

Repères :

| Situation | Payback acceptable |
|---|---|
| Autofinancé, sans réserve | **Sur la première transaction.** Idéalement le client s'auto-finance. |
| Autofinancé avec réserve | ≤ 3 mois |
| Financé par de la dette | ≤ 6-9 mois |
| Financé en fonds propres | ≤ 12 mois |

Hopkins avait déjà compris ça en 1923 : *« Il arrive que les coûts publicitaires soient
amortis avant même l'échéance des factures. Cela signifie que le produit peut être promu
sans investissement initial »* (ch. 15). **Un payback inférieur à ton délai de paiement
fournisseur, c'est de la croissance à capital nul.** C'est la structure financière la plus
puissante qui existe pour quelqu'un qui démarre sans argent.

### 1.6 Le CAC marginal

```
CAC marginal = (dépense supplémentaire) ÷ (clients supplémentaires obtenus)
```

Pas le CAC moyen. Le CAC **du prochain euro**. Section 2.2 : c'est le seul qui décide.

---

## 2. Les cinq pièges

### 2.1 Le CAC mélangé (*blended*) masque la dégradation

Tu dépenses 5 000 € en publicité, tu gagnes 20 clients — dont 12 seraient venus par le
bouche-à-oreille de toute façon.

- CAC mélangé : 5 000 / 20 = **250 €**. Rassurant.
- CAC payant réel : 5 000 / 8 = **625 €**. La vérité.

Ton organique subventionne ton payant et masque sa détérioration. Et quand tu doubles la
dépense, l'organique ne double pas — la moyenne s'effondre et tu ne comprends pas
pourquoi.

**Sépare toujours acquisition payante et acquisition organique.** Ce sont deux économies
différentes.

### 2.2 Le CAC moyen ment ; seul le CAC marginal décide

C'est le piège le plus coûteux du module, alors prenons des chiffres.

| Dépense mensuelle | Clients obtenus | CAC moyen | **CAC marginal** |
|---|---|---|---|
| 5 000 € | 8 | 625 € | — |
| 10 000 € | 13 | 769 € | **1 000 €** |
| 15 000 € | 16 | 938 € | **1 667 €** |

Ton CAC moyen à 15 000 € de dépense est de 938 € et paraît encore acceptable. Mais les
cinq derniers clients t'ont coûté **1 667 € chacun**. Si ta LTV est de 1 620 €, tu as
dépassé le point où tu perds de l'argent — et ton tableau de bord, qui affiche 938 €, ne
te le dit pas.

> **La courbe de CAC est croissante. Toujours.** Tu commences par les prospects les plus
> faciles, et chaque euro supplémentaire va chercher quelqu'un de plus difficile à
> convaincre. La question de croissance n'est jamais « mon CAC est-il bon » mais
> **« jusqu'où mon CAC marginal reste-t-il inférieur à ma LTV »**.

C'est aussi la traduction financière exacte du module 10, section 4 : quand ton CAC
marginal s'envole malgré une exécution constante, tu as épuisé la demande existante. C'est
le signal de bascule vers la construction de marque — pas le signal de pousser plus fort.

### 2.3 La LTV projetée est presque toujours fausse dans le même sens

Tu observes six mois de données, tu extrapoles sur trois ans. Deux biais systématiques :

- **Le survivant.** Les clients que tu observes encore sont ceux qui sont restés. Les
  cohortes récentes n'ont pas eu le temps de partir.
- **L'attrition n'est pas constante.** Elle est forte au début puis décroît. Extrapoler le
  taux du premier mois sous-estime la LTV ; extrapoler celui du douzième la surestime.

**Correctif :** raisonne en **cohortes**. Regarde le mois d'acquisition, et suis chaque
cohorte séparément. Et pour toute décision d'investissement, utilise une **LTV plafonnée à
12 ou 24 mois** — pas une LTV à l'infini. Si ton activité ne tient pas debout sur 12 mois,
elle ne tient pas debout.

### 2.4 L'attribution ment, et pas au hasard

Ta plateforme publicitaire s'attribue des ventes qui auraient eu lieu sans elle. C'est
structurel, pas malveillant : elle voit un contact et une vente, elle relie les deux.

La question correcte n'est pas « d'où vient ce client » mais **« combien de clients en
plus ai-je à cause de cette dépense »**. C'est l'**incrémentalité**, et elle se mesure
d'une seule façon fiable : par l'expérience. Coupe la dépense sur une zone géographique
comparable, garde-la ailleurs, compare les ventes totales.

C'est exactement le protocole de Hopkins au chapitre 16 : *« Essayez une ville d'une
certaine manière, une autre d'une autre manière. Comparez les ventes totales. »*
Cent ans après, ça reste le seul instrument non contaminé.

### 2.5 La LTV n'est pas la même selon le canal

Reviens à Hopkins, chapitre 16 : *« Les personnes qui achètent sur la base de
recommandations informelles sont rarement fidèles. »* Un client acquis par conviction, un
client acquis par remise et un client acquis par recommandation n'ont pas la même durée de
vie ni la même marge.

Une LTV moyenne unique conduit mécaniquement à **sur-investir dans les canaux qui
produisent les clients les moins fidèles** — parce que ce sont souvent ceux qui affichent
le CAC le plus bas.

**Segmente ta LTV par canal d'acquisition.** C'est l'une des analyses au meilleur rapport
effort/rendement disponibles, et presque personne ne la fait.

---

## 3. Exemple complet

Activité de services. Voici le calcul, en entier.

**Les données**

| Élément | Valeur |
|---|---|
| Prix moyen d'une mission | 1 500 € |
| Coûts directs (temps de livraison, sous-traitance) | 600 € |
| **Marge de contribution par mission** | **900 €** |
| Nombre moyen de missions par client | 1,8 |
| Dépense publicitaire mensuelle | 5 000 € |
| Prospects générés | 40 |
| Clients signés | 8 |

**Étape 1 — La LTV**

```
LTV = 900 € × 1,8 = 1 620 €
```

**Étape 2 — Le CAC, entièrement chargé**

Les 40 prospects consomment 45 minutes chacun (qualification, appel, devis, relance) :
30 heures. Au coût réel de 40 €/h, cela fait 1 200 €.

```
CAC = (5 000 € + 1 200 €) ÷ 8 = 775 €
```

Note l'écart : le CAC « publicitaire » est de 625 €, le CAC réel de 775 €. **24 % d'erreur**
si on oublie le temps commercial — et c'est un ordre de grandeur typique.

**Étape 3 — Le ratio**

```
LTV / CAC = 1 620 ÷ 775 = 2,09
```

Sous le seuil de 3. L'activité est rentable à l'unité, mais la marge de sécurité est
mince. Deux leviers, par ordre de rendement :

1. **Faire passer le nombre de missions par client de 1,8 à 2,5** → LTV = 2 250 €,
   ratio = 2,9. Coût : presque nul, c'est du travail de rétention.
2. **Améliorer le taux de signature de 20 % à 27 %** (soit 11 clients au lieu de 8) →
   CAC = 564 €, ratio = 2,87. C'est le module 12 appliqué : le titre, la précision, le
   patron Schlitz, l'inversion du risque.

Note que le levier d'acquisition et le levier de rétention donnent ici le même résultat.
Fais les deux.

**Étape 4 — Le payback**

La première mission rapporte 900 € de marge, pour un CAC de 775 €.

```
Payback = dès la première mission
```

**C'est excellent, et c'est le vrai bon signal de ce tableau.** Malgré un ratio de 2,09
médiocre, l'activité s'autofinance : chaque client remboursé avant d'en acquérir le
suivant. Tu peux croître sans capital.

**Étape 5 — La décision de passage à l'échelle**

Tu veux doubler à 10 000 €. Tu obtiens 13 clients et non 16.

```
CAC marginal = 5 000 € ÷ 5 clients supplémentaires = 1 000 €
              (+ temps commercial ≈ 1 150 €)
```

LTV = 1 620 € contre un CAC marginal de 1 150 €. **Ratio marginal = 1,41.** Positif, donc
tu peux le faire — mais tu viens de voir que la marge de sécurité fond vite. Le palier
suivant sera très probablement sous 1.

**La bonne décision n'est pas de doubler la dépense. C'est de travailler la LTV et le taux
de signature d'abord, ce qui décale toute la courbe vers le haut, puis de redépenser.**

C'est la différence entre acheter de la croissance et construire une machine.

---

## 4. Ton tableau de bord minimal

Six lignes. Mensuel. Pas une de plus tant que celles-ci ne sont pas fiables.

| # | Indicateur | Fréquence | Alerte |
|---|---|---|---|
| 1 | Marge de contribution par vente | Mensuel | Baisse deux mois de suite |
| 2 | CAC payant (hors organique) | Mensuel | Hausse > 20 % à exécution constante |
| 3 | CAC marginal du dernier palier | À chaque hausse de budget | Approche de la LTV |
| 4 | LTV par cohorte d'acquisition | Trimestriel | Cohortes récentes sous les anciennes |
| 5 | Délai de récupération | Mensuel | Dépasse ta trésorerie disponible |
| 6 | Attrition / taux de réachat | Mensuel | C'est le levier n° 1, surveille-le en premier |

---

## 5. Exercices — à rendre dans `exercices/13-rendu.md`

**Exercice 1 — Ta marge de contribution.**
Prends ta dernière vente réelle. Décompose : prix, puis chaque coût directement causé par
cette vente, y compris ton temps de livraison valorisé. Donne le montant et le taux.

**Exercice 2 — Ton CAC réel.**
Sur les 3 derniers mois : dépense publicitaire + temps commercial valorisé + outils,
divisé par le nombre de **nouveaux** clients. Puis calcule aussi le CAC mélangé, et
écris l'écart entre les deux.

**Exercice 3 — Ta LTV et ton ratio.**
Applique la formule qui correspond à ton modèle. Indique honnêtement si tes chiffres sont
observés ou estimés — et si estimés, plafonne à 12 mois.

**Exercice 4 — Ton payback.**
Combien de temps entre le paiement de l'acquisition et sa récupération en marge ? Compare
à ta trésorerie disponible. Si le payback dépasse ce que ta trésorerie peut financer, tu
as une contrainte de croissance qui n'a rien à voir avec ta rentabilité — nomme-la.

**Exercice 5 — Ton CAC marginal.**
Prends tes deux derniers paliers de dépense. Calcule le CAC marginal entre les deux. S'il
n'y a jamais eu deux paliers différents, conçois le test qui te le donnera (module 12,
exercice 6 : seuils écrits d'avance).

**Exercice 6 — Le levier prioritaire.**
Compare le gain de : (a) +20 % de taux de conversion, (b) −20 % d'attrition, (c) +20 % de
prix. Chiffre les trois sur ton propre tableau. Celui qui gagne est ton chantier du
trimestre — et ce n'est presque jamais celui qu'on croit.

---

*Fin du module 13. Avec les modules 1, 10, 12 et 13, tu disposes maintenant de la chaîne
complète : où se trouve l'argent (1), comment le message le capte (12), ce que la mesure
ne voit pas (10), et comment savoir si tu gagnes (13). Le reste du cursus approfondit ;
ce socle-là suffit déjà à décider.*
