# Le parcours — de novice à expert

> Onze niveaux. Chacun se valide par une **épreuve notée**, pas par une lecture.
> Tu ne montes pas parce que tu as fini de lire : tu montes parce que tu as
> démontré une compétence sur un dossier que tu n'avais jamais vu.

---

## Les deux échelles — ne les confonds jamais

Il y a **deux** mesures dans ce cursus, et elles sont indépendantes :

| Échelle | Ce qu'elle mesure | Où elle est définie |
|---|---|---|
| **Lxx** | Ta **compétence** | Ici |
| **Nx** | L'état de ton **business** | [diagnostic](../mentorat/diagnostic.md) |

On peut être **L07 sans entreprise** — c'est le cas d'un bon salarié en agence. On
peut être **N3 avec une compétence L04** — une marque à 500 000 € par mois pilotée
par quelqu'un qui n'a jamais calculé un CAC marginal.

**Le second cas est le plus dangereux du métier**, et c'est le plus fréquent. Le
chiffre d'affaires masque l'incompétence tant que le marché est porteur. Le jour où
il ne l'est plus, la marque n'a personne pour lire ce qui se passe.

> **Objectif :** garder ton niveau L au-dessus de ton niveau N. Toujours. Si ton
> business grandit plus vite que ta compétence, tu ne pilotes plus, tu subis.

---

## Les onze niveaux

| Niveau | Nom | Ce que tu sais faire | Épreuve |
|---|---|---|---|
| **[L00](L00-novice.md)** | Novice | Le vocabulaire, les conversions TTC/HT, lire un chiffre | 25 questions, dont 10 calculs |
| **[L01](L01-initie.md)** | Initié | Construire une cascade de marges, calculer un MER seuil | Dossier chiffré + 3 erreurs à trouver |
| **[L02](L02-praticien.md)** | Praticien | Choisir une catégorie, chiffrer un COGS, valider une demande | 3 dossiers produits, tu choisis et tu prouves |
| **[L03](L03-operateur.md)** | Opérateur | Trouver un angle, écrire un script, construire une page | Corpus client brut → angle + script + page |
| **[L04](L04-acquereur.md)** | Acquéreur | Piloter un compte, distinguer CAC moyen et marginal | 8 semaines de données → allocation |
| **[L05](L05-constructeur.md)** | Constructeur | Industrialiser la créa, lire des cohortes | 12 concepts à juger + cohortes à diagnostiquer |
| **[L06](L06-gestionnaire.md)** | Gestionnaire | Piloter le cash, redresser une marge | Plan de redressement à 90 jours |
| **[L07](L07-stratege.md)** | Stratège | Mesurer l'incrémentalité, allouer au marginal | Test géographique biaisé à corriger |
| **[L08](L08-batisseur.md)** | Bâtisseur | Ouvrir un marché, structurer une organisation | Plan d'ouverture + organigramme cible |
| **[L09](L09-architecte.md)** | Architecte | Construire de la marge et de la marque | 9,4 % → 18 % d'EBITDA sans croissance |
| **[L10](L10-expert-mondial.md)** | Expert mondial | Diagnostiquer une marque inconnue en 30 minutes | Diagnostic chronométré + arbitrage + enseignement |

---

## Ce qui sépare vraiment L09 de L10

Ce n'est pas la connaissance. À L09, tu connais déjà tout ce que ce cursus contient.

C'est **la vitesse de hiérarchisation**. Devant un dossier, un L09 trouve les huit
problèmes. Un L10 trouve les huit problèmes **et sait lequel traiter en premier**,
en moins de trente minutes, et il a raison.

Et c'est **la capacité à voir ce qui ne colle pas**. Un L10 regarde un tableau et
sent qu'un chiffre est faux avant de savoir pourquoi. Cette compétence ne s'acquiert
qu'en ayant vu beaucoup de dossiers — c'est pour ça que l'épreuve L10 est un
diagnostic chronométré et pas un questionnaire.

---

## Les trois choses que tu fais à chaque niveau

Le parcours combine trois activités. Aucune ne suffit seule.

| Activité | Où | Ce que ça produit |
|---|---|---|
| **Tu lis** | [`modules/`](../modules/) et [`etudes-de-cas/`](../etudes-de-cas/) | Les mécanismes |
| **Tu construis** | [`atelier/`](../atelier/) | Les livrables réels d'une marque |
| **Tu joues** | [`outils/simulateur_marque.py`](../outils/simulateur_marque.py) | Les conséquences de tes décisions, en accéléré |

> **Le simulateur est ce qui rend le parcours honnête.** Un cours peut te dire que
> couper le budget de test créatif tue une marque en six mois. Le simulateur te le
> **fait vivre** : tu joues la stratégie `sans_test_crea`, tu vois ton compte
> s'éteindre mois après mois, et tu n'oublies plus. Une erreur simulée coûte dix
> minutes ; la même erreur réelle coûte deux ans.

---

## La carte complète

| Niveau | Modules | Cas | Séances d'atelier | Simulateur |
|---|---|---|---|---|
| **L00** | E00, E01 §0–2 | — | — | — |
| **L01** | E01 | C01 | S01, S02 | `--comparer` |
| **L02** | E02, E03 | C01 | S03, S04 | Deux catégories, même graine |
| **L03** | E04, E07 | — | S05, S06, S07 | — |
| **L04** | E06 | — | S08, S09 | Une partie complète en interactif |
| **L05** | E05, E08 | C03 | S10 | `sans_test_crea` contre `equilibree` |
| **L06** | E10 | C05, C08 | S11 | Scénario de crise de trésorerie |
| **L07** | E09 | C06 | — | — |
| **L08** | E11 | C04, C07 | — | Ouverture de marché |
| **L09** | E12, E13, E14 | C09, C10 | S12 | Partie complète jusqu'à P5+ |
| **L10** | Tout, relu | Tous | S12 partie 2 | Toutes stratégies, analyse comparée |

---

## Les règles du parcours

1. **Une épreuve se passe une fois par session, sans le corrigé sous les yeux.**
   Si tu échoues, tu retravailles et tu repasses une variante — pas la même.
2. **Les questions éliminatoires sont éliminatoires.** Une erreur de HT/TTC, une
   LTV en chiffre d'affaires ou un seuil écrit après le test invalide l'épreuve,
   quelle que soit la note. Ce sont les fautes qui coûtent le plus cher dans la
   vraie vie, donc elles coûtent cher ici.
3. **On ne saute pas un niveau**, même si le CA de ton entreprise est en avance.
   Voir plus haut : c'est exactement le cas dangereux.
4. **Un niveau se perd.** Sans pratique, L07 redescend à L05 en dix-huit mois. Le
   niveau L10 se ré-atteste chaque année sur un dossier neuf.

---

## Combien de temps

Je ne te donnerai pas de calendrier — une promesse de délai est une phrase de
vendeur, et le rythme dépend entièrement du temps que tu y mets et de si tu opères
une marque en parallèle.

Ce que je peux te dire honnêtement :

- **L00 à L02** se franchissent vite si tu es rigoureux : ce sont des automatismes
  de calcul et une méthode de sélection.
- **L03 à L05** demandent de la répétition, pas de la lecture. On n'apprend pas à
  juger un concept créatif en lisant comment on juge un concept créatif.
- **L06 à L08** demandent d'avoir vu des choses casser. Le simulateur en remplace
  une partie, pas la totalité.
- **L09 et L10** ne s'atteignent pas sans avoir opéré ou audité de vraies marques.
  Le cursus t'y prépare complètement ; il ne s'y substitue pas, et je préfère te le
  dire d'emblée plutôt qu'à la fin.

---

*Commence par [L00](L00-novice.md), même si tu penses le dépasser. L'épreuve L00 se
passe en 25 minutes, et elle révèle presque toujours deux automatismes manquants.*
