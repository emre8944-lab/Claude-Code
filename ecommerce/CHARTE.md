# Charte du cursus e-commerce — règles de rédaction

> Ce fichier est destiné à quiconque écrit ou corrige un module de ce cursus.
> Il n'est pas un cours. Il existe pour qu'une quinzaine de documents écrits
> séparément forment **un seul enseignement cohérent**, et pas une pile de PDF.

---

## 1. Le contrat pédagogique

L'élève a un objectif déclaré : **1 000 000 € de chiffre d'affaires par semaine,
avec une marge nette qui tient.** Le cursus est construit pour ça, et pour rien
d'autre. Chaque module doit pouvoir répondre à la question : *« en quoi ceci
rapproche l'élève de P5+ ? »* S'il n'y a pas de réponse, le passage est coupé.

Trois interdits absolus :

1. **Ne jamais vendre du rêve.** 1 M€/semaine, c'est ~52 M€ TTC par an. En Europe,
   moins de 300 marques DTC natives y arrivent. Le cursus dit la probabilité,
   le capital nécessaire, et les modes de mort. Un élève qui abandonne en
   connaissance de cause a été mieux servi qu'un élève qui se ruine en confiance.
2. **Ne jamais donner un chiffre sans son origine.** Voir § 4.
3. **Ne jamais enseigner une tactique sans sa date de péremption.** Une astuce de
   plateforme meurt en 6 à 18 mois. Un mécanisme économique ne meurt pas. Le
   cursus enseigne les mécanismes, et signale explicitement ce qui est daté.

---

## 2. Le ton

Reprends exactement le ton du cursus existant à la racine du dépôt
(`modules/01-asymetries-information.md` est la référence) :

- **Tutoiement.** Un mentor qui parle à un élève, pas une agence à un prospect.
- **Dense.** Aucune phrase de transition vide. Pas de « nous allons maintenant
  voir », pas de « il est important de comprendre ». Tu écris la chose, point.
- **Démonstratif.** On ne dit pas *que* c'est vrai, on montre *pourquoi*. Un
  calcul déroulé vaut mieux qu'une affirmation, toujours.
- **Contradictoire quand il le faut.** Quand deux écoles s'opposent (marque vs
  performance, LTV vs payback, large vs niche), on enseigne les deux, on donne
  les conditions de validité de chacune, et on tranche explicitement.
- **Sans jargon non défini.** Tout acronyme est défini à sa première apparition
  dans le module, même s'il l'a été ailleurs.
- **Exigeant.** On dit à l'élève quand une pratique courante est de la superstition.

Interdits de style : les emojis, les listes à puces de plus de 7 éléments, les
métaphores sportives ou militaires, « game changer », « secret », « hack ultime »,
les majuscules d'emphase, les phrases d'accroche creuses en ouverture de section.

---

## 3. La structure obligatoire d'un module

```
# Module Exx — Titre

> **Prérequis :** modules …
> **Objet :** une phrase qui dit ce que l'élève saura faire à la fin.
> **Temps de travail :** ~Xh (lecture + exercices)

## 0. Pourquoi ce module existe          ← la thèse, en 15 lignes max
## 1. … à 7.                             ← le corps, numéroté, avec sous-sections x.y
## 8. Les erreurs qui coûtent cher       ← 4 à 8 erreurs, chacune chiffrée
## 9. Ce que ce module ne dit pas        ← limites, cas où le modèle est faux,
                                            module qui le contredit
## 10. Le tableau de bord du module      ← 3 à 6 indicateurs, seuil d'alerte
## 11. Exercices                          ← renvoi vers ecommerce/exercices/Exx-rendu.md
*Fin du module Exx. Suite : …*
```

Longueur cible : **20 000 à 38 000 caractères**. En dessous, c'est une fiche, pas
un module. Au-dessus, découpe.

---

## 4. Les chiffres — la règle la plus importante

Tout nombre écrit dans ce cursus appartient à **exactement une** de ces catégories,
et sa catégorie doit être lisible :

| Catégorie | Origine | Comment l'écrire |
|---|---|---|
| **Canonique** | `ecommerce/donnees/chiffres-canoniques.md` | Cité tel quel. Renvoie au tableau : « (chiffres canoniques § 2.2) » |
| **Dérivé** | Calculé dans le module à partir d'un canonique | Le calcul est **déroulé**, pas seulement son résultat |
| **Modélisé** | Hypothèse pédagogique propre au module ou au cas | Préfixé « *hypothèse :* » ou dans un bloc d'hypothèses en tête de section |
| **Public** | Fait publiquement vérifiable sur une entreprise réelle | Nommer la source et l'année : « (rapport annuel 2023) », « (chiffre public) » |

**Interdiction absolue :** attribuer un chiffre financier privé, inventé ou
estimé, à une entreprise réelle nommée. On ne écrit jamais « Gymshark faisait
34 % de marge en 2019 » si on ne l'a pas lu quelque part. Soit c'est public et
sourcé, soit on utilise une marque fictive.

**Les marques des études de cas sont fictives et le disent.** Chaque étude de cas
ouvre par un encadré : *« Cas composite. Marque fictive. Les chiffres sont un
modèle calibré sur des ordres de grandeur sectoriels ; ce ne sont les comptes
d'aucune entreprise réelle. »*

### Cohérence avec le fil rouge

La marque **NØRA** (soin capillaire premium, DTC, Europe) traverse tout le
cursus. Ses chiffres sont figés dans `ecommerce/donnees/chiffres-canoniques.md`,
généré par `ecommerce/outils/modele_nora.py`. **Lis ce fichier avant d'écrire.**
Si un module a besoin d'un chiffre NØRA qui n'y figure pas, deux options :
soit tu le dérives par un calcul explicite à partir de ce qui y figure, soit tu
le déclares comme hypothèse locale. Tu ne le contredis jamais.

Rappel des cinq paliers, à connaître avant d'écrire une ligne :

| Palier | Période | CA TTC/semaine | EBITDA % CA HT | Ce qui s'y joue |
|---|---|---:|---:|---|
| **P1 — Validation** | M1–M3 | 8 492 € | −30,7 % | Le produit mérite-t-il d'exister |
| **P2 — Traction** | M4–M9 | 53 123 € | −10,3 % | La vallée de la mort |
| **P3 — Scale France** | M10–M18 | 271 662 € | +5,2 % | La machine créative tient-elle |
| **P4 — Multi-pays** | M19–M30 | 676 523 € | +8,1 % | L'org et le cash tiennent-ils |
| **P5 — 1 M€/sem.** | M31–M40 | 999 968 € | +10,1 % | Le volume est atteint |
| **P5+ — pilotage marge** | M41+ | 999 978 € | **+20,3 %** | **La vraie destination** |

---

## 5. Typographie et format

- Français, **virgule décimale** partout : `2,17` et jamais `2.17`.
- Séparateur de milliers : espace. `1 494 206 €`.
- Espace avant `%`, `€`, `:`, `!`, `?`, `;` — c'est du français.
- Guillemets français « … ». Tirets cadratins — pour les incises.
- Les montants sont **TTC ou HT, toujours précisé.** Un montant sans mention est
  une faute de rédaction dans ce cursus, parce que c'est une faute de gestion
  dans la vraie vie.
- Tableaux markdown pour toute comparaison de plus de deux lignes.
- Blocs ``` pour les formules et les décompositions de calcul.
- `> **À retenir :**` pour les encadrés de synthèse. Un à trois par module, pas plus.
- Diagrammes : zéro à deux blocs ```mermaid``` par module, seulement si le
  diagramme montre un mécanisme qu'un tableau ne montrerait pas mieux.
- Liens internes en relatif : `[E01](E01-arithmetique-de-la-marque.md)`,
  `[chiffres canoniques](../donnees/chiffres-canoniques.md)`.

---

## 6. Les exercices

Chaque module se termine par **4 à 7 exercices**, dans cet ordre :

1. Un ou deux exercices **sur les données de NØRA** — réponse numérique unique,
   vérifiable, corrigée.
2. Deux ou trois exercices **sur l'activité de l'élève** — il remplit avec ses
   chiffres, la correction est une grille de lecture.
3. Un exercice **de décision** — on lui donne une situation chiffrée et deux
   options, il tranche et justifie. La correction donne la bonne réponse *et*
   la condition sous laquelle l'autre option serait la bonne.

Chaque exercice est reproduit dans `ecommerce/exercices/Exx-rendu.md` (le
formulaire vierge) et corrigé dans `ecommerce/exercices/Exx-corrige.md`.

---

## 7. Table des modules — à respecter pour les renvois croisés

| Code | Fichier | Titre |
|---|---|---|
| E00 | `E00-cadrage.md` | Le cadrage — ce métier, vraiment |
| E01 | `E01-arithmetique-de-la-marque.md` | L'arithmétique de la marque |
| E02 | `E02-marche-et-produit.md` | Choisir le terrain : marché, catégorie, produit |
| E03 | `E03-offre-et-prix.md` | L'offre et le prix |
| E04 | `E04-psychologie-du-client.md` | Le client dans sa tête |
| E05 | `E05-machine-creative.md` | La machine créative |
| E06 | `E06-acquisition-payante.md` | L'acquisition payante et les algorithmes |
| E07 | `E07-funnel-et-conversion.md` | Le funnel et la conversion |
| E08 | `E08-retention-et-ltv.md` | La rétention, les cohortes et la LTV |
| E09 | `E09-mesure-et-incrementalite.md` | Mesurer : attribution, incrémentalité, pilotage |
| E10 | `E10-cash-et-operations.md` | Le cash, le stock et les opérations |
| E11 | `E11-passage-a-echelle.md` | Passer à l'échelle : international, équipe, org |
| E12 | `E12-marque-et-actif.md` | La marque comme actif |
| E13 | `E13-risque-de-ruine.md` | Le risque de ruine |
| E14 | `E14-plan-1M-semaine.md` | Le plan 1 M€/semaine |

| Code | Fichier | Titre |
|---|---|---|
| C01 | `C01-coefficient-insuffisant.md` | Le produit à ×2,5 qui ne pouvait pas gagner |
| C02 | `C02-vallee-de-la-mort.md` | NØRA, mois 1 à 9 : la vallée de la mort |
| C03 | `C03-anatomie-creative-gagnante.md` | Anatomie chiffrée d'un concept publicitaire gagnant |
| C04 | `C04-scale-qui-detruit-la-marge.md` | 41 M€ de CA, 5,8 M€ de perte |
| C05 | `C05-abonnement-et-cac-negatif.md` | Quand payer 2,4× le premier panier est rationnel |
| C06 | `C06-test-incrementalite.md` | Le test qui a supprimé 22 % du budget sans perdre de CA |
| C07 | `C07-ouverture-allemagne.md` | Ouvrir l'Allemagne : 5 mois, chiffres réels du modèle |
| C08 | `C08-redressement-90-jours.md` | Redressement : de −8 % à +14 % de marge nette en 90 jours |
| C09 | `C09-piege-du-black-friday.md` | Le piège du Black Friday, modélisé |
| C10 | `C10-compte-publicitaire-banni.md` | 11 jours de compte publicitaire banni |

---

## 8. Ce qu'on ne fait pas

- Pas de résumé de livre. Le cursus racine s'en charge, avec des fiches de lecture.
- Pas de « top 10 des outils ». Les outils changent ; on nomme la fonction, on
  cite deux ou trois exemples courants, on dit ce qui compte dans le choix.
- Pas de tutoriel clic-par-clic d'interface publicitaire. Les interfaces changent
  tous les trimestres. On enseigne la logique de l'enchère et du signal, qui, elle,
  ne change pas.
- Pas de promesse de délai. « En 90 jours tu feras X » est une phrase de vendeur.
