# Module 20 — Le tracking : le système nerveux

> **Prérequis :** module 19.
> **Objet :** installer une mesure sur laquelle tu peux t'appuyer pour décider.
> Tant que ce module n'est pas maîtrisé, toutes tes décisions d'achat média sont
> du bruit habillé en chiffres.

---

## 0. Pourquoi ce module passe avant tout le reste

Hopkins (module 12) : *« la publicité qu'on ne mesure pas est une dépense, pas un
investissement. »* Il écrivait ça en 1923 avec des coupons numérotés. Le principe
n'a pas bougé d'un millimètre ; seule la plomberie a changé.

Mais il y a une raison plus dure. En achat média payant, **tu prends 30 à 200
décisions par semaine** (couper une créa, monter un budget, tuer une audience).
Chacune est prise sur un chiffre. Si le chiffre est biaisé de 20 %, tu ne prends pas
20 % de mauvaises décisions : tu prends **systématiquement** les mauvaises, dans le
même sens, jour après jour, et tu construis ton activité sur une illusion cohérente.

> **Loi du métier :** un tracking approximatif est pire que pas de tracking.
> Pas de tracking rend prudent. Un mauvais tracking rend confiant.

---

## 1. La chaîne de mesure : les six maillons

```
[1] IMPRESSION      plateforme média
        │
[2] CLIC            ← clic_id généré ici (fbclid, ttclid, gclid…)
        │
[3] REDIRECT / LP   ← ton tracker enregistre le clic + les paramètres
        │
[4] PRE-LANDER      ← advertorial, quiz, VSL
        │
[5] OFFRE / CHECKOUT
        │
[6] CONVERSION      → postback serveur vers le tracker
                    → CAPI / Conversions API vers la plateforme
                    → webhook vers ton entrepôt de données
```

Chaque flèche est un endroit où de l'information se perd. Ton travail est de savoir
**combien** se perd à chaque maillon, pas d'espérer que rien ne se perde.

---

## 2. Les trois couches de mesure (et pourquoi il en faut trois)

### Couche 1 — Le pixel navigateur (côté client)

Le script de la plateforme dans ta page. Il voit ce qui se passe dans le navigateur.

- **Avantage :** installation triviale, alimente l'algorithme d'optimisation.
- **Faiblesse :** bloqué par les bloqueurs de pub (15 à 35 % selon la géo),
  par ITP/Safari (cookies first-party plafonnés à 7 jours, 24 h dans certains cas),
  par le refus de consentement. **Tu perds entre 20 et 50 % des événements.**

### Couche 2 — Le postback serveur-à-serveur (S2S)

Quand une conversion a lieu, le serveur de l'annonceur appelle une URL de ton tracker :

```
https://ton-tracker.tld/postback?cid={click_id}&payout={payout}&status=approved
```

- **Avantage :** aucun navigateur impliqué, donc rien à bloquer. **C'est la source
  de vérité.** C'est sur cette couche, et elle seule, que tu prends tes décisions
  de coupe et de scale.
- **Condition :** il faut passer ton `click_id` de bout en bout, sans jamais le perdre.
  99 % des problèmes de tracking en affiliation sont un `click_id` perdu entre deux
  redirections.

### Couche 3 — L'API de conversion de la plateforme (CAPI / Events API)

Tu renvoies l'événement de conversion *depuis ton serveur* vers Meta, TikTok, Google.

- **Avantage :** l'algorithme d'optimisation retrouve les conversions que le pixel a
  ratées. Sur Meta, un CAPI correctement déduplicaté **récupère typiquement 10 à 25 %
  de conversions attribuées** et améliore mécaniquement la performance, parce que
  l'algorithme apprend sur des données moins trouées.
- **Piège majeur — la déduplication :** il faut envoyer le **même `event_id`** dans le
  pixel et dans le CAPI. Sans ça, tu comptes chaque conversion deux fois, ton ROAS
  affiché double, et tu scales une campagne qui perd de l'argent. C'est l'erreur la
  plus coûteuse et la plus fréquente du métier.

> **Règle :** la couche 2 décide. La couche 3 nourrit l'algorithme.
> La couche 1 ne sert qu'à alimenter la 3 et à faire du remarketing.

---

## 3. Le tracker : à quoi il sert vraiment

Un tracker (Voluum, RedTrack, Binom, Keitaro, BeMob…) fait quatre choses :

1. **Il enregistre chaque clic** avec ses variables : source, campagne, créa, placement,
   géo, appareil, navigateur, heure, et jusqu'à 10 variables libres.
2. **Il redirige** vers la bonne page — et permet la rotation entre plusieurs versions.
3. **Il reçoit les postbacks** et recolle la conversion au clic d'origine.
4. **Il agrège** : tu peux voir la marge par placement, par créa, par heure, par appareil.

### 3.1 Le schéma de nommage — la compétence qui paraît triviale et qui ne l'est pas

```
{source}_{vertical}_{offre}_{geo}_{angle}_{creatif}_{lander}_{date}
tt_nutra_sleepdrops_FR_stress_v14-ugc-sarah_lp3-advertorial_0923
```

Pourquoi c'est critique : **tu ne peux analyser que ce que tu as nommé.** Dans six
mois, tu auras lancé 800 créas. Si tu ne peux pas répondre à « est-ce que l'angle
*stress* bat l'angle *insomnie* toutes sources confondues ? » en une requête, tu ne
construis pas l'asymétrie A4 du module 19. Tu repars de zéro chaque trimestre.

**Fixe la convention avant le premier euro dépensé, et ne la change plus jamais.**

### 3.2 Les variables à toujours faire remonter

| Variable | Pourquoi |
|---|---|
| `click_id` plateforme (fbclid/ttclid/gclid) | Recoller côté plateforme |
| `sub_id` unique généré par toi | Recoller côté réseau, seul identifiant que tu contrôles |
| Placement / site ID | La donnée la plus rentable en native et en push : 80 % du gaspillage vient de 20 % des placements |
| Appareil + OS + navigateur | Les écarts de conversion iOS/Android vont de 1 à 3 |
| Géo + ville | Les écarts intra-pays sont énormes |
| Heure locale | Le dayparting est le réglage le plus sous-utilisé |

---

## 4. Les six façons dont ton tracking te ment

### 4.1 La double comptabilisation pixel + CAPI
Traitée en § 2. Vérification : le nombre de conversions dans le Gestionnaire doit
être **proche** de celui du tracker, jamais le double. Si c'est le double, `event_id`.

### 4.2 La fenêtre d'attribution
Meta attribue par défaut en 7 jours après clic / 1 jour après vue. Ton réseau attribue
peut-être en 30 jours. **Tu compares deux objets différents.** Aligne les fenêtres
avant de comparer quoi que ce soit, ou n'utilise qu'une seule source pour décider.

### 4.3 L'attribution vue (view-through)
Une conversion « après vue » signifie : la personne a vu ta pub, n'a pas cliqué, et a
acheté plus tard. C'est parfois réel, souvent c'est **du vol d'attribution** : la
plateforme s'attribue une vente qui aurait eu lieu sans elle. Pour décider de ton
scale, **regarde d'abord les chiffres clic-only.**

### 4.4 Le dernier clic écrase tout le reste
Le module 10 (Sharp) l'a démontré. Le canal qui clôt reçoit tout le crédit ; celui qui
a créé la demande n'en reçoit aucun. En pratique : ton retargeting et ta marque
affichent des ROAS mirobolants et ne créent presque rien d'incrémental. Ne scale
jamais un canal de fin de tunnel sur son ROAS déclaré.

### 4.5 Le décalage de reporting
Un lead validé à J+9, un remboursement à J+21, un chargeback à J+60. **Ton ROAS de J+0
est toujours faux, systématiquement dans le sens optimiste.** Construis un facteur de
maturation à partir de ton historique :

```
ROAS_final ≈ ROAS_J0 × facteur_maturation
(mesure-le sur tes 3 derniers mois, par offre — il est souvent entre 0,80 et 0,95)
```

### 4.6 Le consentement (RGPD)
En UE, un bandeau de consentement bien fait supprime 20 à 40 % de tes événements
navigateur. Ça ne supprime pas les ventes : ça supprime **la vue** que tu en as. Les
gens confondent les deux et coupent des campagnes rentables. Le S2S et le
Consent Mode côté plateforme existent précisément pour ça.

---

## 5. Le seul test qui dit la vérité : le test d'incrémentalité

Toute la mesure ci-dessus est **corrélationnelle**. La seule mesure causale est
l'expérience : couper, et regarder.

**Le test de blackout géographique (geo holdout) — le plus accessible :**

1. Prends deux ensembles de régions comparables (CA, saisonnalité, démographie proches).
2. Coupe totalement la dépense sur l'ensemble A pendant 2 à 4 semaines. Maintiens B.
3. Compare l'évolution du CA **total** (tous canaux, y compris direct et organique)
   entre A et B.
4. La différence est ton effet incrémental réel.

Le résultat surprend presque toujours. Selon la maturité de ta marque, l'incrémentalité
réelle d'un canal se situe souvent entre **40 % et 80 %** de ce qu'il déclare. Sur du
retargeting pur, elle descend fréquemment sous 30 %.

> **Quand faire ce test :** dès que ta dépense mensuelle dépasse ~30 k€, une fois
> par trimestre, sur ton canal principal. Le coût du test est très inférieur au coût
> de scaler pendant un an un canal qui ne crée rien.

---

## 6. Ce que tu dois construire, dans l'ordre

| Palier | Ce que tu mets en place | Coût mensuel |
|---|---|---|
| **0 → 1 k€/mois** | Pixel + CAPI dédupliqué, UTM disciplinés, un Google Sheet quotidien | ~0 € |
| **1 → 10 k€/mois** | Tracker (Binom/RedTrack), S2S postbacks, convention de nommage figée | 50–150 € |
| **10 → 50 k€/mois** | Tableau de bord marge (pas ROAS) par créa/placement/heure, facteur de maturation | 200–500 € |
| **50 k€+/mois** | Entrepôt de données (BigQuery), cohortes, geo holdouts trimestriels, MMM léger | 1–3 k€ |

**Ne saute pas de palier.** Un entrepôt de données à 500 €/mois de dépense média
est une façon très élaborée de ne pas lancer de campagne.

---

## 7. Limites

1. **Plus tu mesures finement, plus tu optimises court-termiste.** C'est l'avertissement
   central du module 10. Le tracking parfait te pousse vers le bas du tunnel, où la
   mesure est facile et la création de valeur faible. Garde une part de budget — 10 à
   20 % — sur des choses que tu ne sais pas mesurer proprement (contenu, marque,
   nouvelles sources). Appelle ça un budget d'exploration, pas du gaspillage.
2. **Le tracking se dégrade structurellement**, année après année (ITP, ATT, fin des
   cookies tiers, Consent Mode, SKAN sur mobile). Le sens de l'histoire est : **moins
   de mesure individuelle, plus de mesure agrégée et expérimentale.** Les affiliés qui
   survivront à la décennie sont ceux qui savent lire un geo holdout, pas ceux qui
   savent bricoler un pixel.
3. **Aucune mesure ne remplace la marge en banque.** Le contrôle final, hebdomadaire :
   `encaissements réels − dépenses réelles`. Si ce chiffre contredit ton tableau de
   bord, c'est ton tableau de bord qui a tort.

---

## 8. Exercice 20

À rendre dans `exercices/20-rendu.md`.

1. **Dessine ta chaîne de mesure complète** sur l'offre retenue au module 19, maillon
   par maillon, en indiquant à chaque flèche ce qui peut se perdre.
2. **Écris ta convention de nommage** et engage-toi dessus par écrit.
3. **Fais un test de bout en bout** : un clic réel, une conversion de test, et vérifie
   qu'elle remonte dans les trois couches avec le bon `click_id`. Note le délai.
4. **Trouve un écart.** Compare sur 7 jours : conversions plateforme / conversions
   tracker / conversions réseau / encaissements réels. Quatre chiffres différents.
   **Explique chaque écart.** Un écart inexpliqué est une fuite d'argent qui grossit.
5. Calcule ton **facteur de maturation** sur l'historique dont tu disposes.
