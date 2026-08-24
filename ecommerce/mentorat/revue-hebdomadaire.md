# La revue hebdomadaire — 45 minutes, une décision

> C'est le seul rituel obligatoire du cursus. Tout le reste peut glisser d'une
> semaine ; celui-ci, non. Une marque se pilote au rythme hebdomadaire : assez
> lent pour que le bruit s'efface, assez rapide pour corriger avant que ça coûte.

---

## Le format

Toujours le même jour, toujours la même heure, 45 minutes chronométrées. Seul si
tu es seul, avec les responsables de fonction à partir de P3. Ordinateur fermé
pendant les trois premiers blocs : on lit le tableau, on ne fouille pas les
interfaces.

| Bloc | Durée | Question unique |
|---|---|---|
| 1. Les chiffres | 10 min | Que s'est-il passé ? |
| 2. Les alertes | 10 min | Est-ce du bruit ou un signal ? |
| 3. Le goulot | 10 min | Qu'est-ce qui limite vraiment ? |
| 4. La décision | 10 min | Que fait-on, avec quel seuil écrit d'avance ? |
| 5. La clôture | 5 min | Qu'est-ce qu'on arrête ? |

---

## Bloc 1 — Les chiffres (10 minutes)

Tu lis le [tableau de bord](tableau-de-bord.md) à voix haute, dans l'ordre, sans
commenter. **Aucune interprétation à ce stade.** L'erreur classique est de
commenter chaque ligne au fur et à mesure : on se raconte alors une histoire, et
on trouve une explication à tout, y compris au bruit.

Trois colonnes obligatoires : cette semaine, la semaine dernière, il y a quatre
semaines. Un chiffre seul ne veut rien dire ; c'est la trajectoire qui informe.

---

## Bloc 2 — Les alertes (10 minutes)

Pour chaque case cochée « alerte » au bloc 1, une seule question : **bruit ou
signal ?**

Le test, dans l'ordre :

1. **L'écart dépasse-t-il deux écarts-types de la moyenne mobile sur 28 jours ?**
   Si non → bruit. On note, on ne fait rien.
2. **Est-ce la troisième semaine consécutive dans le même sens ?**
   Si oui → signal, même si l'écart est faible. Une dérive lente est plus
   dangereuse qu'un décrochage brutal, parce qu'elle ne déclenche jamais d'alarme.
3. **Un événement identifié l'explique-t-il ?** (rupture de stock, panne de suivi,
   jour férié, changement de politique publicitaire, concurrent en promotion)
   Si oui → ce n'est pas un problème de performance, c'est un incident. Traite
   l'incident, pas l'indicateur.
4. Sinon → **signal non expliqué**. C'est le cas le plus important et il devient
   automatiquement candidat au goulot du bloc 3.

> **La discipline la plus dure du métier :** ne rien faire quand c'est du bruit.
> Chaque intervention sur un compte publicitaire coûte une phase de
> réapprentissage. Corriger du bruit, c'est payer pour dégrader.

---

## Bloc 3 — Le goulot (10 minutes)

Une seule question : **qu'est-ce qui limite l'entreprise cette semaine ?**

Le goulot change de nature selon le palier, et travailler le mauvais goulot est
la façon la plus courante de perdre un an en travaillant beaucoup :

| Palier | Goulot dominant | Le symptôme qui le trahit |
|---|---|---|
| **P1** | L'offre | Le trafic vient, il n'achète pas |
| **P2** | La machine créative | Le CAC monte à budget constant, aucun concept nouveau ne perce |
| **P3** | La créa **et** le cash | Ça marche, mais on ne peut pas financer le stock du mois suivant |
| **P4** | L'organisation et les marchés | Les décisions attendent une personne ; les chiffres ne concordent pas |
| **P5** | La marge | Le CA progresse, l'EBITDA non |

Écris le goulot en **une phrase**. S'il t'en faut trois, c'est que tu n'as pas
tranché — et une équipe qui poursuit trois goulots n'en résout aucun.

---

## Bloc 4 — La décision (10 minutes)

**Une seule décision par semaine.** Pas trois. Une.

Elle s'écrit dans ce format, sans exception :

```
DÉCISION DE LA SEMAINE ____

Ce que je fais :
  ______________________________________________________________

Pourquoi (le goulot que ça traite) :
  ______________________________________________________________

L'indicateur qui dira si ça a marché :
  ______________________________________________________________

Le seuil de RÉUSSITE, écrit maintenant :
  ______________________________________________________________

Le seuil d'ARRÊT, écrit maintenant :
  ______________________________________________________________

Date de jugement :
  ______________________________________________________________
```

> **Les deux seuils s'écrivent avant, jamais après.** Un seuil écrit après le
> résultat n'est pas un seuil, c'est une justification. C'est la règle centrale du
> module racine 12 sur la publicité scientifique, et c'est ce qui sépare un test
> d'une anecdote.
>
> La **date de jugement** est aussi importante que les seuils. Sans elle, un test
> qui ne marche pas ne meurt jamais : il devient « une stratégie de long terme ».

---

## Bloc 5 — La clôture (5 minutes)

Deux questions, dans cet ordre :

1. **Qu'est-ce qu'on arrête cette semaine ?** Une campagne, un outil, une
   habitude, une réunion, un produit. Cette question rapporte plus que toutes les
   autres réunies, et c'est celle qu'on saute quand on est pressé. Une entreprise
   qui n'arrête jamais rien accumule des coûts fixes et de la complexité jusqu'à
   ce que la complexité devienne le goulot.
2. **Quelle décision de la semaine dernière arrive à sa date de jugement ?** On la
   juge maintenant, contre ses seuils écrits. Trois issues : on garde, on arrête,
   on prolonge — et « on prolonge » n'est acceptable qu'une seule fois.

---

## Ce qu'on ne fait **pas** pendant la revue

| Interdit | Pourquoi |
|---|---|
| Ouvrir le gestionnaire de publicités | Tu vas trouver une anomalie, la commenter, et perdre 20 minutes sur du bruit |
| Regarder les concurrents | Ce n'est pas une décision, c'est de l'anxiété |
| Refaire le calcul d'un chiffre | Si un chiffre est douteux, la mise en place de sa mesure devient le chantier — pas maintenant |
| Décider d'un recrutement | Un recrutement est une décision trimestrielle, jamais hebdomadaire |
| Débattre d'une refonte du site | Idem : décision trimestrielle |
| Prendre plus d'une décision | La deuxième dilue la première et aucune n'est exécutée |

---

## Le compte rendu à m'envoyer

Cinq lignes. Pas plus.

```
SEMAINE ____
Goulot identifié : ______________________________________
Décision prise : ________________________________________
Seuil de réussite / d'arrêt : ___________________________
Jugement de la décision de S−1 : ☐ gardée ☐ arrêtée ☐ prolongée
Ce que j'ai arrêté : ____________________________________
```

Si tu n'arrives pas à remplir ces cinq lignes, la revue n'a pas eu lieu — elle
s'est transformée en une séance de consultation de chiffres, ce qui est agréable
et sans effet.

---

*Le rituel trimestriel, lui, est décrit dans [jalons.md](jalons.md) § « Le rituel
de porte ».*
