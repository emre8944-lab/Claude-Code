# Module 26 — La zone grise : la carte honnête

> **Prérequis :** tous les modules précédents du bloc.
> **Objet :** te donner la carte réelle du secteur, y compris ce dont on ne parle pas
> dans les formations. Non pas pour t'y envoyer, mais parce qu'un métier dont tu ne
> connais que la moitié te sera enseigné par tes concurrents, dans de mauvaises
> conditions.

---

## 0. Pourquoi ce module existe

Trois raisons, et aucune n'est morale.

1. **Tu vas y être confronté.** Tes concurrents dans la bibliothèque publicitaire
   utilisent des choses que tu ne comprends pas. Tu vas croire qu'ils ont un meilleur
   angle, alors qu'ils ont simplement un risque différent. **Comparer ta performance à
   la leur sans connaître leur exposition au risque est une erreur d'analyse.**
2. **On va te le proposer.** Un account manager de réseau, un « mentor », un vendeur
   de comptes. Tu dois savoir ce qu'on te vend et ce que ça coûte réellement.
3. **La plupart des gens classent mal.** Ils mettent dans le même sac des choses qui
   coûtent un compte publicitaire et des choses qui coûtent une condamnation pénale.
   Ce module sert d'abord à **trier**.

---

## 1. Le tri : trois axes, pas un

L'expression « grey hat » agrège trois questions totalement différentes. Sépare-les,
toujours, pour chaque pratique :

| Axe | Question | Sanction maximale |
|---|---|---|
| **A — Contrat** | Est-ce que ça viole les conditions d'une plateforme ou d'un réseau ? | Perte de compte, commissions annulées, éventuellement action contractuelle |
| **B — Loi** | Est-ce que c'est illégal ? | Amende administrative, pénal, responsabilité personnelle du dirigeant |
| **C — Client** | Est-ce que quelqu'un est lésé ? | Chargebacks, perte du compte marchand, actions de groupe, réputation |

```
Axe A seul       = risque d'exploitation.    Se gère, se provisionne, se calcule.
Axe B            = risque d'existence.       Ne se gère pas. Se refuse.
Axe C            = risque de destruction lente, souvent sous-estimé,
                   et qui active presque toujours A et B ensuite.
```

**La faute d'analyse la plus fréquente du secteur** consiste à traiter un risque de
type B comme s'il était de type A — « au pire je perds le compte ». Non : au pire tu
perds le compte, l'argent en réserve chez le PSP, l'entité, et tu réponds
personnellement. Les dirigeants condamnés dans les grandes affaires d'affiliation
(free-trial nutra aux États-Unis, mis en cause par la FTC ; réseaux de faux avis ;
lead gen crédit non autorisé) ne pensaient pas non plus être dans le pénal.

---

## 2. La logique économique de la zone grise

Le module 1 t'a donné l'outil : **le revenu est le prix d'une asymétrie.** La zone
grise est une asymétrie particulière — une asymétrie **d'application des règles** :

```
Rendement d'une pratique grise
  = (marge supplémentaire) × (durée avant détection)
  − (coût de la sanction) × (probabilité de sanction)
  − (coût du capital détruit : comptes, entité, réputation, temps)
```

Deux propriétés structurelles de ce calcul rendent l'exercice difficile :

1. **La durée avant détection se raccourcit chaque année.** La détection automatisée
   des plateformes (analyse d'image, correspondance de tunnel, empreinte de compte,
   graphe de paiement) s'améliore beaucoup plus vite que les techniques de
   contournement. Une pratique qui tenait 18 mois en 2018 en tient 6 semaines.
2. **Le coût de la sanction est convexe.** Rien pendant longtemps, puis tout d'un coup.
   Tu ne perds pas 5 % de ton activité : tu perds le compte, la trésorerie qui est
   dedans, et souvent la capacité à recommencer sous la même identité. **Un risque
   convexe ne se moyenne pas** — c'est le risque de ruine, et le module 18 t'expliquera
   pourquoi un risque de ruine, même improbable, domine tous les autres termes.

> **La conclusion que le calcul impose, pas la morale :** les pratiques de type A
> peuvent avoir une espérance positive si l'on provisionne correctement. Les pratiques
> de type B ont presque toujours une espérance négative **dès qu'on intègre
> correctement le terme de ruine**, même quand elles sont très rentables pendant
> 18 mois. Ce n'est pas un conseil de prudence, c'est une lecture correcte du calcul.

---

## 3. La carte des pratiques

Pour chacune : ce que c'est, sur quels axes elle tombe, et le risque réel.

### 3.1 Les pratiques de type A — contrat seulement

**Comptes publicitaires multiples / comptes d'agence.** Détenir plusieurs Business
Managers, ou louer des comptes via une agence partenaire, pour se prémunir d'une
suspension. Sur le papier c'est un contournement du « un compte par entité » ; en
pratique, la redondance de comptes est **la norme du secteur au-dessus de 5 000 €/jour**,
y compris chez des annonceurs parfaitement conformes, parce que les suspensions
arbitraires existent. *Risque :* perte des comptes liés en cascade quand la plateforme
recolle l'empreinte. *Ligne à ne pas franchir :* acheter des comptes ouverts avec
l'identité d'autrui — on passe alors en usurpation d'identité et souvent en
blanchiment (axe B, pénal).

**Le brand bidding** (enchérir sur la marque d'un concurrent ou de son propre
annonceur). Légal en UE dans les limites du § 2.3 du module 23. Presque toujours
interdit par le contrat d'affiliation. *Risque :* annulation des commissions,
exclusion du programme. Purement A — et fréquent.

**Le « tir sur la marque » de l'annonceur** (capter les recherches de marque de
l'annonceur pour toucher une commission sur des ventes qui auraient eu lieu sans toi).
Le parfait exemple du module 10 : tu es payé pour une valeur que tu n'as pas créée.
Rentable, détectable, et c'est ce qui pousse les annonceurs à passer en incrémental.

**Les angles à la limite de la règle publicitaire** — parler d'un problème sans le
nommer, utiliser la suggestion plutôt que l'affirmation. C'est l'essentiel du travail
créatif réel dans les verticales régulées, et c'est légitime **tant que le message
n'est pas trompeur pour le client** (sinon on bascule en B et C).

### 3.2 Le cloaking — la pratique emblématique, et son vrai coût

**Ce que c'est.** Servir une page différente selon le visiteur : une page conforme et
anodine (*whitepage*) au robot de modération de la plateforme, la vraie page de vente
(*moneypage*) au trafic réel. La détection du modérateur se fait sur l'IP, l'agent
utilisateur, l'empreinte du navigateur, la géolocalisation, le comportement.

**Pourquoi c'est utilisé.** Deux motifs très différents, qu'il faut distinguer :

- *Motif défensif :* protéger une page légitime de la copie par les concurrents, ou
  éviter qu'un modérateur voie une page hors contexte. Argument invoqué souvent,
  vraiment fondé parfois.
- *Motif offensif :* faire passer une publicité qui serait refusée si elle était vue
  telle qu'elle est. C'est le cas réel dans la très grande majorité des usages.

**Le classement honnête.** Le cloaking en lui-même est de type A : c'est une violation
de contrat (Meta, Google et TikTok l'interdisent explicitement, et Google le qualifie
de « sneaky redirect »). Mais il n'est **presque jamais employé seul** : on cloake
pour diffuser quelque chose qui ne passerait pas, et ce quelque chose est en général
de type B ou C — claim santé interdit, faux témoignage, rebill dissimulé. **Le cloaking
n'est donc pas le risque : c'est le symptôme que le risque est ailleurs, en aval.**

**Le coût réel, souvent mal évalué :** suspension de l'ensemble des actifs liés
(compte, BM, pages, domaine, moyens de paiement, et fréquemment les comptes
personnels des administrateurs), sans préavis et sans recours utile. Blacklist de
domaine. Et, depuis les procédures civiles engagées par les plateformes contre des
réseaux de cloaking organisés, un risque contractuel réel. Je n'écrirai pas de guide
opérationnel de contournement de la modération : ce serait t'aider à construire une
dépendance à un avantage qui expire, à mes yeux le pire conseil qu'on puisse donner
dans ce métier.

### 3.3 Les pratiques de type C — le client est lésé

Ce sont les plus dangereuses **parce qu'elles paraissent inoffensives** et qu'elles
sont très rentables à court terme.

| Pratique | Ce que c'est | Pourquoi ça finit mal |
|---|---|---|
| **Faux compteur / faux stock** | Urgence fabriquée | Pratique trompeuse par nature (dir. 2005/29/CE, annexe I, pt 7). Sanctionnée en UE. |
| **Advertorial déguisé en article de presse** | Publicité maquillée en rédactionnel | Interdit en toutes circonstances (annexe I, pt 11). + contrefaçon si logo de média |
| **Rebill peu clair** | Abonnement dont le client n'a pas conscience | 3–8 % de chargebacks → perte du compte marchand → fin de l'activité |
| **Annulation rendue difficile** | Téléphone seul, files d'attente | Illégal en France (L215-1-1) et visé par la règle FTC click-to-cancel |
| **Résultats atypiques présentés comme typiques** | « −18 kg en 3 semaines » | Trompeur ; en santé, potentiellement dangereux |
| **Revente de leads non consentie** | Le formulaire alimente 12 courtiers | RGPD : jusqu'à 4 % du CA mondial. La CNIL sanctionne activement ce modèle |

**Le mécanisme de destruction est toujours le même, et il est financier avant d'être
juridique :** les pratiques de type C produisent des chargebacks. Les chargebacks
au-dessus de **0,9 %** te placent dans les programmes de surveillance des réseaux de
carte (VAMP chez Visa, ECP chez Mastercard) ; au-dessus de **1 %** soutenu, ton
acquéreur te résilie. Sans compte marchand, tu ne peux plus encaisser. **Ton entreprise
s'arrête un mardi matin, avec trois mois de réserve bloqués chez le PSP.** Module 27.

### 3.4 Les pratiques de type B — le pénal

Je les nomme pour que tu les reconnaisses quand on te les proposera, ce qui arrivera.
Je n'expliquerai pas comment les mettre en œuvre.

- **Cookie stuffing** — déposer des cookies d'affiliation sans clic, pour capter des
  commissions sur des ventes auxquelles on n'a pas contribué. Qualifié de fraude
  informatique ; condamnation pénale (l'affaire *Hogan* / eBay, 5 M$ fraudés, prison
  ferme, est la référence du secteur).
- **Fraude au clic / trafic robotisé** — générer du faux trafic ou de fausses
  conversions. Escroquerie en bande organisée ; les affaires *Methbot* et *3ve*
  ont donné lieu à des condamnations pénales internationales.
- **Usurpation d'identité** — comptes publicitaires, comptes bancaires ou entités
  ouverts au nom de tiers. Usurpation + souvent blanchiment.
- **Faux avis et faux témoignages** — y compris générés par IA. FTC : jusqu'à ~51 000 $
  par avis depuis 2024. France : pratique commerciale trompeuse, 2 ans de prison,
  300 000 € d'amende portés à 10 % du CA.
- **Deepfakes de personnalités ou de médecins** — atteinte au droit à l'image,
  contrefaçon, escroquerie. C'est aujourd'hui la pratique la plus poursuivie du
  secteur, et celle où la responsabilité personnelle du dirigeant est la plus
  facilement engagée.
- **Claims santé interdits** — guérir, traiter, prévenir une maladie avec un produit
  qui n'est pas un médicament. Règlement UE 1924/2006 et Code de la santé publique.
  Au-delà de l'amende : si quelqu'un arrête un traitement à cause de ta publicité,
  tu es dans un autre univers juridique.
- **Détournement de commission** (*toolbar hijacking*, injection d'affiliation,
  extension qui réécrit les liens) — fraude et souvent atteinte à un système de
  traitement automatisé de données.

**Le point commun de tout l'axe B :** il n'y a pas de version « prudente ». Tu ne peux
pas le faire à petite échelle sans risque, parce que le risque n'est pas proportionnel
au volume — il est déclenché par un seul signalement, une seule plainte, un seul
audit de réseau.

---

## 4. Ce que je t'apprendrai, et ce que je ne t'apprendrai pas

**Ce que je t'apprends volontiers**, parce que ça fait partie du métier et que ne pas
le savoir te handicape :

- Comment fonctionnent ces mécanismes, pour que tu les repères chez tes concurrents
  et que tu comprennes leurs chiffres.
- Comment lire un contrat d'affiliation et savoir ce qui est réellement interdit,
  ce qui ne l'est pas, et ce qui est toléré.
- Comment écrire des angles **agressifs et conformes** : c'est une compétence bien
  plus rare et bien mieux payée que le contournement.
- Comment arbitrer un risque de type A : provisionner, cloisonner, diversifier.
- Comment ne pas se faire escroquer par un réseau (scrub, retenues abusives,
  changement de payout rétroactif).

**Ce que je ne ferai pas :** rédiger un mode d'emploi de contournement de modération,
écrire de faux témoignages ou de faux avis, formuler des claims santé interdits,
construire un tunnel à rebill dissimulé, ou aider à ouvrir des comptes sous identité
d'emprunt. Ce n'est pas de la prudence de principe : c'est que ce sont des actifs à
durée de vie négative, et que je serais en train de t'aider à construire quelque chose
qui te coûtera l'entreprise.

---

## 5. Le contre-argument sérieux, et la réponse

*« Mais les gros font tous ça. »*

C'est faux au sens où on l'entend, et l'erreur est instructive.

Ce que font réellement les opérateurs à très haut volume :

1. **Ils sont agressifs sur l'axe A et quasi propres sur B et C.** Redondance de
   comptes, structures multiples, angles au bord de la règle publicitaire — oui.
   Faux témoignages et rebill caché — non, parce qu'ils ont trop à perdre et que leurs
   PSP les auditent.
2. **Ils ont internalisé la conformité comme un avantage concurrentiel.** C'est le
   point que presque personne ne comprend. Quand un secteur se durcit, ceux qui
   survivent captent le volume de ceux qui sautent. **La conformité n'est pas un coût :
   c'est une barrière à l'entrée que tu construis contre des concurrents plus
   rentables que toi à court terme et morts à moyen terme.** C'est un moat, au sens
   du module 2.
3. **Ils cloisonnent.** Entités séparées par verticale et par géographie, PSP
   multiples, aucune exposition unique capable de tout emporter.
4. **Ceux qui ont été très agressifs sur B ont fini d'une des deux façons connues :**
   soit ils ont converti tôt une manne en activité légitime, soit ils sont sortis du
   secteur par la porte judiciaire. Le biais de survie (mentionné dans le README du
   cursus) joue à plein ici : tu vois ceux qui roulent encore, jamais les dossiers.

---

## 6. Le cadre de décision, en trois questions

Avant toute pratique dont tu n'es pas sûr :

```
Q1. Est-ce que c'est illégal ?  (axe B)
    → OUI : on arrête là. Aucun calcul de rendement n'est pertinent.
    → INCERTAIN : c'est un avis d'avocat, pas un forum. Le coût de l'avis
      est de 500 à 2 000 €. Le coût de l'erreur est ton entreprise.

Q2. Est-ce qu'un client normalement informé se sentirait trompé ?  (axe C)
    → OUI : espérance négative une fois les chargebacks intégrés. Fais le calcul,
      il ne passe jamais.

Q3. Est-ce que ça viole un contrat ?  (axe A)
    → OUI, mais A seul : décision économique légitime. Alors :
      - Quelle est la durée de vie estimée ? (sois pessimiste, divise par deux)
      - Qu'est-ce que je perds si ça saute demain matin ?
      - Est-ce que je peux cloisonner pour que ça n'emporte pas le reste ?
      - Est-ce que la marge supplémentaire finance la reconstruction ?
      Si tu ne peux pas répondre aux quatre, tu n'évalues pas un risque : tu paries.
```

---

## 7. Limites de ce module

1. **Le droit varie et bouge.** Tout ce qui précède est une cartographie générale,
   orientée France/UE avec des repères américains. Ce n'est pas un avis juridique.
   Dès que tu dépasses ~20 k€/mois, prends un avocat en droit de la consommation et
   de la publicité. C'est le meilleur rapport coût/risque de toutes tes dépenses.
2. **La frontière A/B est mouvante.** Des choses hier contractuelles deviennent
   légales ou illégales : le DSA a créé des obligations nouvelles sur la publicité
   en ligne, la loi influenceurs de 2023 a fait basculer en infraction des pratiques
   qui étaient de simples usages. **Ce qui était A l'an dernier peut être B cette
   année.** Fais une revue annuelle.
3. **Ce module ne prétend pas que le blanc pur est optimal.** L'affilié parfaitement
   conforme qui refuse tout risque de type A sera plus lent, et perdra souvent
   l'enchère face à quelqu'un de plus agressif. L'objectif n'est pas zéro risque :
   c'est un **risque choisi, dimensionné, cloisonné et provisionné**, au lieu d'un
   risque subi par ignorance.

---

## 8. Exercice 26

À rendre dans `exercices/26-rendu.md`.

1. **Prends 5 publicités concurrentes de ta verticale.** Pour chacune, classe ce
   qu'elles font sur les trois axes A/B/C. Combien sont sur B ou C ? Que t'apprend
   leur performance apparente, une fois ce risque intégré ?
2. **Lis en entier** les règles publicitaires de ta source et le contrat de ton
   réseau. Liste **10 choses interdites** que tu ignorais.
3. **Écris ta propre ligne** : qu'est-ce que tu acceptes de faire, qu'est-ce que tu
   refuses ? Par écrit, daté, **avant** d'être sous pression financière. C'est le seul
   moment où cette décision peut être prise honnêtement.
4. **Prends un angle agressif de ta verticale qui viole une règle, et réécris-le en
   version conforme** en gardant la force persuasive. Compare les deux. Cet exercice
   est, de loin, le plus rentable du module.
5. **Chiffre ton scénario de perte maximale** : si ton compte principal saute demain
   matin, que perds-tu en euros, et en combien de temps redémarres-tu ?
