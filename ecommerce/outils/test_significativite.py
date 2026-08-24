#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculateur de significativite et de taille de test.

Cet outil existe pour empecher deux fautes qui coutent tres cher, et qui sont
les deux faces de la meme piece :

  1. Couper un concept publicitaire sur du bruit. Quarante euros depenses sans
     achat ne demontrent rien du tout. Une marque qui coupe a ce stade elimine
     par tirage au sort une bonne partie des concepts qui auraient gagne.
  2. Declarer un test A/B gagnant trop tot. Un ecart de +12 % sur 300 visiteurs
     par bras est indiscernable du hasard. Le deployer, c'est graver une
     illusion dans le site.

Trois modes.

    --taille    Combien de visiteurs, de conversions et surtout d'EUROS faut-il
                pour detecter un ecart donne ? A lire AVANT de lancer un test.
    --comparer  Deux variantes observees : l'ecart est-il demontre, ou du bruit ?
    --creatif   Le cas du concept publicitaire, ou la seule variable comptee est
                le nombre d'achats : a couper, a conserver, a scaler, ou trop
                jeune pour qu'on puisse le dire ?

Usage
-----
    # combien pour detecter +10 % relatif sur un taux de conversion de 2 % ?
    python3 ecommerce/outils/test_significativite.py --taille \
        --taux 2 --ecart 10 --confiance 95 --puissance 80 --cpa-cible 40,03

    # deux variantes observees
    python3 ecommerce/outils/test_significativite.py --comparer \
        --a-visiteurs 12000 --a-conversions 240 \
        --b-visiteurs 12000 --b-conversions 276

    # un concept publicitaire en cours de test
    python3 ecommerce/outils/test_significativite.py --creatif \
        --depense 40 --achats 0 --cpa-cible 40,03

    # demonstration des trois modes, sur les chiffres canoniques de NORA
    python3 ecommerce/outils/test_significativite.py --demo

Les nombres s'ecrivent indifferemment « 2,5 » ou « 2.5 », avec ou sans espaces,
avec ou sans le signe % ou €. Les pourcentages se saisissent en points :
--taux 2 veut dire 2 % de taux de conversion.

Conventions de sortie : francais, virgule decimale, espace avant % et €, tout
montant marque TTC ou HT. Voir ecommerce/CHARTE.md § 5. Une depense
publicitaire est toujours HT : c'est un cout, pas un prix client.

Python 3.9+. Aucune dependance externe : la fonction de repartition normale,
son inverse et la loi de Poisson sont implementees ici, a partir de math.erf
et de math.lgamma.

Chiffres de demonstration : ecommerce/donnees/chiffres-canoniques.md.
"""

from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass
from typing import Callable, List, Optional, Sequence, Tuple

LARGEUR = 78

# Espace fine insecable : separateur de milliers et espace avant % et €.
FINE = " "


# ---------------------------------------------------------------------------
# 0. FORMATAGE — mêmes conventions que modele_nora.py et calculateur.py
# ---------------------------------------------------------------------------

def eur(x: float, d: int = 0) -> str:
    """Formate un montant en euros, espace fine comme separateur de milliers."""
    if x == float("inf"):
        return "illimité"
    s = f"{x:,.{d}f}".replace(",", FINE).replace(".", ",").replace("-", "−")
    return s + FINE + "€"


def _mots(txt: str) -> List[str]:
    """Decoupe en mots SANS casser les espaces fines insecables.

    « 40,03 € » et « 36,8 % » sont un seul mot : c'est tout l'interet de
    l'espace fine insecable, et str.split() la traiterait comme un separateur,
    ce qui renverrait le symbole a la ligne suivante.
    """
    plat = txt.replace("\n", " ").replace("\t", " ")
    return [m for m in plat.split(" ") if m]


def pct(x: float, d: int = 1) -> str:
    """Formate une proportion (0,615) en pourcentage francais (61,5 %)."""
    if x in (float("inf"), float("-inf")):
        return ("∞" if x > 0 else "−∞") + FINE + "%"
    if x != x:
        return "—"
    return f"{x * 100:.{d}f}".replace(".", ",") + FINE + "%"


def pct_grand(x: float, d: int = 1) -> str:
    """Comme pct(), avec separateur de milliers : un rapport peut valoir 3 931,8 %."""
    if x in (float("inf"), float("-inf")) or x != x:
        return pct(x)
    return f"{x * 100:,.{d}f}".replace(",", FINE).replace(".", ",") + FINE + "%"


def pct_signe(x: float, d: int = 1) -> str:
    """Formate un ecart relatif avec son signe : +10,0 % / −7,5 %."""
    if x in (float("inf"), float("-inf")):
        return ("+∞" if x > 0 else "−∞") + FINE + "%"
    if x != x:
        return "—"
    return f"{x * 100:+.{d}f}".replace(".", ",").replace("-", "−") + FINE + "%"


def pts(x: float, d: int = 2) -> str:
    """Formate un ecart en points de pourcentage, signe compris."""
    return f"{x * 100:+.{d}f}".replace(".", ",").replace("-", "−") + FINE + "pts"


def dec(x: float, d: int = 3) -> str:
    """Formate un nombre decimal nu (un score z, un ratio)."""
    if x == float("inf"):
        return "∞"
    if x != x:
        return "—"
    return f"{x:.{d}f}".replace(".", ",").replace("-", "−")


def ent(x: float) -> str:
    """Formate un entier avec separateur de milliers."""
    if x == float("inf"):
        return "∞"
    return f"{x:,.0f}".replace(",", FINE).replace("-", "−")


def nombre(s: str) -> float:
    """Lit un nombre ecrit a la francaise ou a l'anglaise. « 1 494 206,50 € » -> float."""
    t = str(s)
    for parasite in (" ", " ", " ", " ", "€", "%"):
        t = t.replace(parasite, "")
    t = t.replace("−", "-").replace(",", ".")
    if t in ("", "-", "+"):
        raise ValueError(f"« {s} » n'est pas un nombre")
    try:
        return float(t)
    except ValueError:
        raise ValueError(f"« {s} » n'est pas un nombre")


def bandeau(t: str, sous_titre: str = "") -> List[str]:
    out = ["═" * LARGEUR, t.upper().center(LARGEUR)]
    if sous_titre:
        out.append(sous_titre.center(LARGEUR))
    out.append("═" * LARGEUR)
    return out


def titre(t: str) -> List[str]:
    return ["", t.upper(), "─" * LARGEUR]


def _couper(txt: str, largeur: int) -> List[str]:
    """Coupe un texte en morceaux d'au plus `largeur` caracteres, sur les mots."""
    morceaux: List[str] = []
    courante = ""
    for mot in _mots(txt):
        essai = mot if not courante else courante + " " + mot
        if len(essai) > largeur and courante:
            morceaux.append(courante)
            courante = mot
        else:
            courante = essai
    if courante:
        morceaux.append(courante)
    return morceaux or [""]


def tableau(entetes: Sequence[str], lignes: Sequence[Sequence[str]],
            aligns: Sequence[str], indent: str = "  ",
            largeur: int = LARGEUR) -> List[str]:
    """Rend un tableau texte a colonnes alignees. 'g' = gauche, 'd' = droite.

    Si le tableau depasse la largeur utile, la derniere colonne — par
    convention celle qui porte du texte, pas des nombres — est retrecie et son
    contenu passe a la ligne. Aucune sortie ne peut donc deborder.
    """
    if not lignes:
        return [indent + "  ".join(entetes)]
    cols = list(zip(*([list(entetes)] + [list(l) for l in lignes])))
    larg = [max(len(c) for c in col) for col in cols]

    surplus = len(indent) + sum(larg) + 2 * (len(larg) - 1) - largeur
    if surplus > 0 and len(larg) > 1:
        larg[-1] = max(10, larg[-1] - surplus)

    def rendre(cells: Sequence[str]) -> List[str]:
        morceaux = _couper(str(cells[-1]), larg[-1])
        out = []
        for i, bout in enumerate(morceaux):
            rendu = []
            for c, w, a in zip(cells[:-1], larg[:-1], aligns[:-1]):
                texte = c if i == 0 else ""
                rendu.append(texte.ljust(w) if a == "g" else texte.rjust(w))
            rendu.append(bout.ljust(larg[-1]) if aligns[-1] == "g" else bout.rjust(larg[-1]))
            out.append((indent + "  ".join(rendu)).rstrip())
        return out

    res = rendre(entetes) + [indent + "  ".join("─" * w for w in larg)]
    for l in lignes:
        res += rendre(l)
    return res


def paragraphe(txt: str, indent: str = "  ", creux: Optional[str] = None,
               largeur: int = LARGEUR) -> List[str]:
    """Coupe un paragraphe a la largeur utile, sans couper les mots.

    `creux` est l'indentation des lignes de continuation : elle sert aux
    listes, ou la suite d'un point doit se distinguer du point suivant.
    """
    tete = indent
    suite = indent if creux is None else creux
    lignes: List[str] = []
    courante = ""
    for mot in _mots(txt):
        essai = mot if not courante else courante + " " + mot
        if len(tete) + len(essai) > largeur and courante:
            lignes.append(tete + courante)
            tete, courante = suite, mot
        else:
            courante = essai
    if courante:
        lignes.append(tete + courante)
    return lignes


def puces(items: Sequence[str]) -> List[str]:
    """Liste a points, indentation creuse, jamais plus large que LARGEUR."""
    out: List[str] = []
    for it in items:
        out += paragraphe(it, indent="  ", creux="    ")
    return out


# ---------------------------------------------------------------------------
# 1. LA BOÎTE À OUTILS STATISTIQUE — tout est fait maison, stdlib seule
# ---------------------------------------------------------------------------

def phi(z: float) -> float:
    """Fonction de repartition de la loi normale centree reduite.

    Phi(z) = P(Z <= z) = 1/2 * (1 + erf(z / racine(2))).
    C'est une identite exacte : math.erf fait tout le travail.
    """
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def phi_inverse(p: float) -> float:
    """Inverse de phi : le quantile z tel que P(Z <= z) = p.

    Approximation rationnelle d'Acklam (erreur relative < 1,15e−9), suivie
    d'un raffinement de Halley qui utilise phi() ci-dessus et fait tomber
    l'erreur au niveau de la precision machine.
    """
    if not 0.0 < p < 1.0:
        raise ValueError("Le quantile normal demande une probabilité strictement entre 0 et 1.")

    a = (-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00)
    b = (-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01)
    c = (-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00)
    d = (7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00)

    bas, haut = 0.02425, 1 - 0.02425
    if p < bas:
        q = math.sqrt(-2 * math.log(p))
        x = (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / \
            ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    elif p <= haut:
        q = p - 0.5
        r = q * q
        x = (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q / \
            (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1)
    else:
        q = math.sqrt(-2 * math.log(1 - p))
        x = -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / \
            ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)

    # Raffinement de Halley : une seule passe suffit.
    e = phi(x) - p
    u = e * math.sqrt(2 * math.pi) * math.exp(x * x / 2)
    return x - u / (1 + x * u / 2)


def p_bilaterale(z: float) -> float:
    """Valeur p bilaterale associee a un score z : P(|Z| >= |z|)."""
    return 2.0 * (1.0 - phi(abs(z)))


def _log_pmf_poisson(k: int, lam: float) -> float:
    return k * math.log(lam) - lam - math.lgamma(k + 1)


def poisson_sf(k: int, lam: float) -> float:
    """P(X >= k) pour X ~ Poisson(lam). Somme directe de la queue.

    On somme la queue plutot que 1 − P(X <= k−1) : pas de soustraction de deux
    nombres proches de 1, donc pas de perte de precision la ou ca compte.
    """
    if k <= 0:
        return 1.0
    if lam <= 0:
        return 0.0
    total = 0.0
    i = k
    # On monte jusqu'a ce que les termes soient negligeables, au-dela du mode.
    limite = int(lam + 12 * math.sqrt(lam + 1) + 60) + k
    while i <= limite:
        terme = math.exp(_log_pmf_poisson(i, lam))
        total += terme
        if i > lam and terme < 1e-18 * max(total, 1e-300):
            break
        i += 1
    return min(1.0, total)


def poisson_cdf(k: int, lam: float) -> float:
    """P(X <= k) pour X ~ Poisson(lam)."""
    if k < 0:
        return 0.0
    if lam <= 0:
        return 1.0
    return min(1.0, sum(math.exp(_log_pmf_poisson(i, lam)) for i in range(0, int(k) + 1)))


def _bissection(f: Callable[[float], float], bas: float, haut: float,
                iterations: int = 200) -> float:
    """Racine de f sur [bas, haut], f changeant de signe. Bissection pure."""
    fb = f(bas)
    for _ in range(iterations):
        milieu = 0.5 * (bas + haut)
        fm = f(milieu)
        if fm == 0.0 or (haut - bas) < 1e-12 * max(1.0, abs(milieu)):
            return milieu
        if (fb < 0) != (fm < 0):
            haut = milieu
        else:
            bas, fb = milieu, fm
    return 0.5 * (bas + haut)


def _chi2_quantile_wh(p: float, nu: float) -> float:
    """Quantile du khi-deux par l'approximation de Wilson-Hilferty.

    Utilisee seulement pour les grands nombres d'achats (> 1 000), ou l'erreur
    tombe sous 0,05 % et ou la somme exacte deviendrait inutilement lente.
    """
    z = phi_inverse(p)
    return nu * (1 - 2 / (9 * nu) + z * math.sqrt(2 / (9 * nu))) ** 3


SEUIL_POISSON_EXACT = 1000


def ic_poisson(k: int, confiance: float = 0.95) -> Tuple[float, float]:
    """Intervalle de confiance exact (Garwood) sur l'intensite d'une loi de Poisson.

    Pour k achats observes, renvoie l'encadrement du nombre d'achats « vrai »
    qu'on aurait obtenu en repetant ce test une infinite de fois.

    Definition :
        borne basse  : le lam tel que P(X >= k | lam) = alpha/2   (0 si k = 0)
        borne haute  : le lam tel que P(X <= k | lam) = alpha/2
    """
    if k < 0:
        raise ValueError("Le nombre d'achats ne peut pas être négatif.")
    alpha = 1.0 - confiance

    if k > SEUIL_POISSON_EXACT:
        return (_chi2_quantile_wh(alpha / 2, 2 * k) / 2,
                _chi2_quantile_wh(1 - alpha / 2, 2 * k + 2) / 2)

    if k == 0:
        bas = 0.0
    else:
        bas = _bissection(lambda lam: poisson_sf(k, lam) - alpha / 2,
                          1e-12, float(k) + 1.0)
    plafond = k + 12 * math.sqrt(k + 1) + 40
    haut = _bissection(lambda lam: alpha / 2 - poisson_cdf(k, lam),
                       max(float(k), 1e-12), plafond)
    return bas, haut


# ---------------------------------------------------------------------------
# 2. MODE --taille : COMBIEN FAUT-IL POUR SAVOIR ?
# ---------------------------------------------------------------------------

ECARTS_TABLE = (0.05, 0.10, 0.20, 0.30, 0.50)


@dataclass
class Taille:
    """Taille d'echantillon pour comparer deux proportions, test bilateral.

    taux_ref      : taux de conversion du bras temoin, en proportion (0,02)
    ecart_relatif : ecart RELATIF a detecter (0,10 = +10 % relatif, soit
                    2,00 % -> 2,20 %, et non 2,00 % -> 12,00 %)
    confiance     : 1 − alpha, en proportion
    puissance     : 1 − beta, en proportion
    cpa_cible     : cout par acquisition vise, en € HT (0 = non fourni)
    trafic_jour   : visiteurs par jour, TOUS bras confondus (0 = non fourni)
    """

    taux_ref: float
    ecart_relatif: float
    confiance: float = 0.95
    puissance: float = 0.80
    cpa_cible: float = 0.0
    trafic_jour: float = 0.0

    def valider(self) -> List[str]:
        a: List[str] = []
        if not 0 < self.taux_ref < 1:
            a.append("Le taux de conversion de référence doit être strictement compris entre 0 % et 100 %.")
        if self.ecart_relatif == 0:
            a.append("Un écart relatif de 0 % ne se détecte jamais : il faudrait un échantillon infini.")
        if self.taux_ref * (1 + self.ecart_relatif) >= 1 or self.taux_ref * (1 + self.ecart_relatif) <= 0:
            a.append("L'écart relatif demandé pousse le taux de la variante hors de l'intervalle 0 %–100 %.")
        if not 0.5 < self.confiance < 1:
            a.append("Le niveau de confiance doit être compris entre 50 % et 100 % (exclus).")
        if not 0.5 <= self.puissance < 1:
            a.append("La puissance doit être comprise entre 50 % et 100 % (exclue).")
        if self.cpa_cible < 0 or self.trafic_jour < 0:
            a.append("Le CPA cible et le trafic quotidien ne peuvent pas être négatifs.")
        return a

    @property
    def taux_variante(self) -> float:
        return self.taux_ref * (1 + self.ecart_relatif)

    @property
    def ecart_absolu(self) -> float:
        return self.taux_variante - self.taux_ref

    @property
    def z_alpha(self) -> float:
        return phi_inverse(1 - (1 - self.confiance) / 2)

    @property
    def z_beta(self) -> float:
        return phi_inverse(self.puissance)

    @property
    def visiteurs_par_variante(self) -> float:
        """Formule classique a deux proportions, variance poolee sous H0.

            n = ( z(a/2)·√(2·p̄·(1−p̄)) + z(b)·√(p1(1−p1) + p2(1−p2)) )² / (p2 − p1)²

        C'est la version qui fait la difference entre la variance sous
        l'hypothese nulle (les deux bras identiques, d'ou le poolage) et la
        variance sous l'hypothese alternative (les deux bras differents).
        """
        p1, p2 = self.taux_ref, self.taux_variante
        # Un taux cible hors de ]0 ; 1[ n'a pas d'echantillon : on renvoie
        # l'infini plutot que de lever une erreur de domaine. Les rapports
        # savent afficher l'infini ; ils ne savent pas rattraper une exception.
        if not 0 < p1 < 1 or not 0 < p2 < 1 or p1 == p2:
            return float("inf")
        pbar = (p1 + p2) / 2
        num = (self.z_alpha * math.sqrt(2 * pbar * (1 - pbar))
               + self.z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
        # Arrondi au superieur : une taille d'echantillon ne se tronque jamais.
        return float(math.ceil(num / (p2 - p1) ** 2))

    @property
    def realisable(self) -> bool:
        return self.visiteurs_par_variante != float("inf")

    @property
    def visiteurs_total(self) -> float:
        return 2 * self.visiteurs_par_variante

    @property
    def conversions_bras_ref(self) -> float:
        return self.visiteurs_par_variante * self.taux_ref

    @property
    def conversions_bras_variante(self) -> float:
        return self.visiteurs_par_variante * self.taux_variante

    @property
    def conversions_total(self) -> float:
        return self.conversions_bras_ref + self.conversions_bras_variante

    @property
    def budget_total(self) -> float:
        """Budget publicitaire HT necessaire pour acheter ce trafic.

        Le CPA cible est un cout par conversion : le trafic des deux bras coute
        donc « conversions totales × CPA cible ». Le split etant 50/50, chaque
        bras consomme la moitie du budget, meme s'il ne rend pas le meme
        nombre de conversions.
        """
        return self.conversions_total * self.cpa_cible

    @property
    def budget_par_variante(self) -> float:
        return self.budget_total / 2

    @property
    def jours(self) -> float:
        if self.trafic_jour <= 0:
            return float("inf")
        return self.visiteurs_total / self.trafic_jour

    def avec_ecart(self, e: float) -> "Taille":
        return Taille(self.taux_ref, e, self.confiance, self.puissance,
                      self.cpa_cible, self.trafic_jour)


# ---------------------------------------------------------------------------
# 3. MODE --comparer : L'ÉCART OBSERVÉ EST-IL DÉMONTRÉ ?
# ---------------------------------------------------------------------------

VERDICT_NON = "différence non démontrée — continue ou arrête, mais ne conclus pas"
VERDICT_FAIBLE = "signal faible"
VERDICT_OUI = "différence démontrée"

# Seuil de p au-dela duquel on ne parle meme plus de signal.
SEUIL_SIGNAL_FAIBLE = 0.20


@dataclass
class Comparaison:
    """Deux bras observes. visiteurs et conversions de chacun, rien d'autre."""

    a_visiteurs: float
    a_conversions: float
    b_visiteurs: float
    b_conversions: float
    confiance: float = 0.95
    puissance: float = 0.80
    cpa_cible: float = 0.0

    def valider(self) -> List[str]:
        a: List[str] = []
        if self.a_visiteurs <= 0 or self.b_visiteurs <= 0:
            a.append("Chaque bras doit avoir au moins un visiteur.")
        if self.a_conversions < 0 or self.b_conversions < 0:
            a.append("Le nombre de conversions ne peut pas être négatif.")
        if self.a_conversions > self.a_visiteurs or self.b_conversions > self.b_visiteurs:
            a.append("Un bras ne peut pas avoir plus de conversions que de visiteurs.")
        if not 0.5 < self.confiance < 1:
            a.append("Le niveau de confiance doit être compris entre 50 % et 100 % (exclus).")
        return a

    @property
    def taux_a(self) -> float:
        return self.a_conversions / self.a_visiteurs

    @property
    def taux_b(self) -> float:
        return self.b_conversions / self.b_visiteurs

    @property
    def ecart_absolu(self) -> float:
        """Difference des taux, en proportion. Positive = B devant A."""
        return self.taux_b - self.taux_a

    @property
    def ecart_relatif(self) -> float:
        if self.taux_a == 0:
            return float("inf") if self.taux_b > 0 else 0.0
        return self.taux_b / self.taux_a - 1

    @property
    def taux_poole(self) -> float:
        return ((self.a_conversions + self.b_conversions)
                / (self.a_visiteurs + self.b_visiteurs))

    @property
    def se_poolee(self) -> float:
        """Erreur standard SOUS L'HYPOTHÈSE NULLE — celle du test.

        Sous H0 les deux bras ont le meme taux : on l'estime sur les deux bras
        reunis. C'est cette erreur standard qui sert a calculer z et p.
        """
        p = self.taux_poole
        return math.sqrt(p * (1 - p) * (1 / self.a_visiteurs + 1 / self.b_visiteurs))

    @property
    def se_non_poolee(self) -> float:
        """Erreur standard sans hypothese nulle — celle de l'intervalle.

        Pour encadrer la difference reelle, on n'a plus le droit de supposer
        que les deux bras sont identiques : chaque bras porte sa variance.
        """
        pa, pb = self.taux_a, self.taux_b
        return math.sqrt(pa * (1 - pa) / self.a_visiteurs + pb * (1 - pb) / self.b_visiteurs)

    @property
    def z(self) -> float:
        se = self.se_poolee
        if se == 0:
            return 0.0
        return self.ecart_absolu / se

    @property
    def p_valeur(self) -> float:
        return p_bilaterale(self.z)

    @property
    def z_confiance(self) -> float:
        return phi_inverse(1 - (1 - self.confiance) / 2)

    @property
    def ic_difference(self) -> Tuple[float, float]:
        """IC de la difference des taux, en points de pourcentage (proportions)."""
        m = self.z_confiance * self.se_non_poolee
        return self.ecart_absolu - m, self.ecart_absolu + m

    @property
    def ic_relatif(self) -> Tuple[float, float]:
        """Le meme intervalle, exprime en ecart RELATIF au bras A."""
        if self.taux_a == 0:
            return float("-inf"), float("inf")
        bas, haut = self.ic_difference
        return bas / self.taux_a, haut / self.taux_a

    @property
    def verdict(self) -> str:
        p = self.p_valeur
        if p < 1 - self.confiance:
            return VERDICT_OUI
        if p < SEUIL_SIGNAL_FAIBLE:
            return VERDICT_FAIBLE
        return VERDICT_NON

    @property
    def effectif_attendu_minimal(self) -> float:
        """Le plus petit effectif attendu des quatre cases du tableau de contingence.

        Sous 5, l'approximation normale du test z n'est plus fiable : la valeur p
        affichee devient indicative. C'est le critere classique de Cochran.
        """
        p = self.taux_poole
        return min(self.a_visiteurs * p, self.a_visiteurs * (1 - p),
                   self.b_visiteurs * p, self.b_visiteurs * (1 - p))

    @property
    def approximation_fiable(self) -> bool:
        return self.effectif_attendu_minimal >= 5

    @property
    def verdict_court(self) -> str:
        """Le verdict en deux mots, pour les tableaux."""
        return {VERDICT_OUI: "démontrée", VERDICT_FAIBLE: "signal faible",
                VERDICT_NON: "non démontrée"}[self.verdict]

    @property
    def ecart_detectable(self) -> float:
        """Le plus petit ecart relatif que cet echantillon pouvait detecter (MDE).

        On inverse la formule de taille : a n fixe, quel ecart relatif aurait
        ete detecte avec la puissance demandee ? Tout ce qui est plus petit que
        ca, ce test ne pouvait structurellement pas le voir.
        """
        n = min(self.a_visiteurs, self.b_visiteurs)
        p1 = self.taux_a
        if p1 <= 0 or p1 >= 1 or n <= 0:
            return float("inf")
        if self.b_visiteurs <= 0:
            return float("inf")
        z_a = self.z_confiance
        z_b = phi_inverse(self.puissance)
        # Approximation a variance constante, suffisante pour un ordre de grandeur.
        delta = (z_a + z_b) * math.sqrt(2 * p1 * (1 - p1) / n)
        return delta / p1

    @property
    def visiteurs_manquants(self) -> float:
        """Visiteurs a ajouter PAR BRAS pour trancher, si l'ecart observe est reel.

        On garde le SIGNE de l'ecart observe : dimensionner une baisse comme si
        c'etait une hausse pousserait le taux de la variante au-dela de 100 %
        quand le bras de reference est deja tres haut.
        """
        if self.ecart_relatif in (0.0, float("inf")) or self.taux_a <= 0:
            return float("inf")
        t = Taille(self.taux_a, self.ecart_relatif, self.confiance, self.puissance)
        if not t.realisable:
            return float("inf")
        return max(0.0, t.visiteurs_par_variante - min(self.a_visiteurs, self.b_visiteurs))


# ---------------------------------------------------------------------------
# 4. MODE --creatif : COUPER, CONSERVER, SCALER — OU ATTENDRE ?
# ---------------------------------------------------------------------------

VERDICT_TROP_TOT = "trop tôt pour juger"
VERDICT_COUPER = "à couper"
VERDICT_CONSERVER = "à conserver"
VERDICT_SCALER = "à scaler"

# Un concept n'est « a scaler » que s'il est demontre nettement sous la cible,
# pas s'il la frole par le haut de son intervalle.
MARGE_SCALE = 0.80
# Largeur d'intervalle, rapportee a la cible, en dessous de laquelle attendre
# davantage ne change plus la decision.
PRECISION_SUFFISANTE = 0.30
# Plafond de recherche du budget manquant, en multiples du budget deja depense.
PLAFOND_ACHATS = 20_000


@dataclass
class Creatif:
    """Un concept publicitaire en cours de test.

    depense   : budget deja depense sur CE concept, en € HT
    achats    : nombre d'achats obtenus (evenement rare : loi de Poisson)
    cpa_cible : cout par acquisition vise, en € HT
    """

    depense: float
    achats: int
    cpa_cible: float
    confiance: float = 0.95

    def valider(self) -> List[str]:
        a: List[str] = []
        if self.depense <= 0:
            a.append("La dépense sur le concept doit être strictement positive.")
        if self.achats < 0:
            a.append("Le nombre d'achats ne peut pas être négatif.")
        if self.achats != int(self.achats):
            a.append("Le nombre d'achats est un entier : on ne compte pas des demi-achats.")
        if self.cpa_cible <= 0:
            a.append("Le CPA cible doit être strictement positif.")
        if not 0.5 < self.confiance < 1:
            a.append("Le niveau de confiance doit être compris entre 50 % et 100 % (exclus).")
        return a

    @property
    def cpa_observe(self) -> float:
        if self.achats == 0:
            return float("inf")
        return self.depense / self.achats

    @property
    def achats_attendus_a_la_cible(self) -> float:
        """Combien d'achats un concept qui tient EXACTEMENT la cible rendrait."""
        return self.depense / self.cpa_cible

    @property
    def proba_zero_achat_a_la_cible(self) -> float:
        """P(0 achat) pour un concept qui tient exactement la cible.

        C'est le chiffre qui condamne la coupe prematuree : il dit quelle
        proportion des BONS concepts un seuil de depense donne elimine.
        """
        return math.exp(-self.achats_attendus_a_la_cible)

    @property
    def ic_achats(self) -> Tuple[float, float]:
        return ic_poisson(int(self.achats), self.confiance)

    @property
    def ic_cpa(self) -> Tuple[float, float]:
        """IC du CPA : on inverse l'IC du nombre d'achats.

        Le CPA est depense / achats. La depense est connue exactement, c'est le
        nombre d'achats qui est incertain. Plus d'achats = CPA plus bas, donc
        la borne HAUTE des achats donne la borne BASSE du CPA.
        """
        lam_bas, lam_haut = self.ic_achats
        cpa_bas = self.depense / lam_haut if lam_haut > 0 else float("inf")
        cpa_haut = self.depense / lam_bas if lam_bas > 0 else float("inf")
        return cpa_bas, cpa_haut

    @property
    def precision_relative(self) -> float:
        """Largeur de l'IC du CPA, rapportee a la cible. Petit = decision stable."""
        cpa_bas, cpa_haut = self.ic_cpa
        if cpa_haut == float("inf"):
            return float("inf")
        return (cpa_haut - cpa_bas) / self.cpa_cible

    @property
    def decisif(self) -> bool:
        """Vrai si ce niveau de dépense suffit à trancher, quel que soit le sens."""
        return self.verdict != VERDICT_TROP_TOT

    @property
    def verdict(self) -> str:
        cpa_bas, cpa_haut = self.ic_cpa
        if cpa_bas > self.cpa_cible:
            # Meme l'hypothese la plus favorable reste au-dessus de la cible.
            return VERDICT_COUPER
        if cpa_haut < self.cpa_cible * MARGE_SCALE:
            return VERDICT_SCALER
        if cpa_haut < self.cpa_cible:
            return VERDICT_CONSERVER
        if self.precision_relative <= PRECISION_SUFFISANTE:
            # L'intervalle enjambe la cible mais il est deja serre : depenser
            # plus ne fera plus basculer la decision. On tranche sur l'observe.
            return VERDICT_CONSERVER if self.cpa_observe <= self.cpa_cible else VERDICT_COUPER
        return VERDICT_TROP_TOT

    def _clone(self, depense: float, achats: int) -> "Creatif":
        return Creatif(depense, achats, self.cpa_cible, self.confiance)

    @property
    def depense_pour_trancher(self) -> float:
        """Dépense TOTALE (€ HT) à partir de laquelle le verdict devient net.

        Deux cas.

        Zero achat : le seul verdict atteignable est « à couper ». Il arrive
        quand la borne basse du CPA depasse la cible, c'est-a-dire quand la
        depense depasse lam_haut(0) × CPA cible — environ 3,7 fois la cible a
        95 % de confiance. C'est la regle des trois CPA.

        Au moins un achat : on prolonge le CPA observe et on cherche, par
        dichotomie sur le nombre d'achats, le premier volume qui rend le
        verdict net. La recherche est monotone : l'intervalle ne fait que se
        resserrer quand les achats s'accumulent a taux constant.
        """
        if self.decisif:
            return self.depense
        if self.achats == 0:
            _, lam_haut = ic_poisson(0, self.confiance)
            return lam_haut * self.cpa_cible

        taux = self.cpa_observe
        bas, haut = int(self.achats), int(self.achats) * 2 + 8
        while haut <= PLAFOND_ACHATS and not self._clone(haut * taux, haut).decisif:
            bas, haut = haut, haut * 2
        if haut > PLAFOND_ACHATS:
            return float("inf")
        while haut - bas > 1:
            milieu = (bas + haut) // 2
            if self._clone(milieu * taux, milieu).decisif:
                haut = milieu
            else:
                bas = milieu
        return haut * taux

    @property
    def depense_manquante(self) -> float:
        d = self.depense_pour_trancher
        return float("inf") if d == float("inf") else max(0.0, d - self.depense)

    @property
    def verdict_complet(self) -> str:
        """Le verdict, avec le budget manquant quand il y en a un."""
        v = self.verdict
        if v != VERDICT_TROP_TOT:
            return v
        manque = self.depense_manquante
        if manque == float("inf"):
            return f"{VERDICT_TROP_TOT} — et ce concept ne tranchera jamais : son CPA colle à la cible"
        return f"{VERDICT_TROP_TOT} — il faut encore {eur(manque)} HT de dépense"

    @property
    def budget_minimum_de_jugement(self) -> float:
        """La dépense sous laquelle « 0 achat » ne veut rien dire du tout.

        A 95 % de confiance : 3,69 × CPA cible. En dessous, un concept parfait
        a plus de 2,5 % de chances de ne montrer aucun achat — donc l'absence
        d'achat n'est pas une information exploitable.
        """
        _, lam_haut = ic_poisson(0, self.confiance)
        return lam_haut * self.cpa_cible

    def phrase_du_bruit(self) -> str:
        """La phrase qui explique pourquoi couper trop tot est un tirage au sort."""
        lam = self.achats_attendus_a_la_cible
        p0 = self.proba_zero_achat_a_la_cible
        return (
            f"{eur(self.depense)} HT dépensés quand ta cible est à {eur(self.cpa_cible, 2)} HT "
            f"de CPA, c'est {dec(lam, 2)} achat attendu : un concept qui tient exactement "
            f"ta cible a {pct(p0)} de chances de n'en montrer aucun, et couper là-dessus "
            f"revient à éliminer au hasard cette part des concepts qui allaient gagner."
        )


def table_montee_en_depense(cpa_cible: float, multiples: Sequence[float],
                            confiance: float = 0.95) -> List[List[str]]:
    """Ce que chaque palier de dépense permet de savoir, et ne permet pas.

    Le scenario est le meilleur possible : le concept tient EXACTEMENT la cible
    et rend le nombre d'achats attendu. Meme dans ce cas ideal, on lit combien
    de temps l'intervalle reste trop large pour decider.
    """
    lignes: List[List[str]] = []
    for m in multiples:
        d = m * cpa_cible
        lam = d / cpa_cible
        k = int(round(lam))
        c = Creatif(d, k, cpa_cible, confiance)
        cpa_bas, cpa_haut = c.ic_cpa
        ic = f"{eur(cpa_bas, 2)} – {eur(cpa_haut, 2)}" if cpa_haut != float("inf") else \
             f"{eur(cpa_bas, 2)} – illimité"
        lignes.append([
            eur(d),
            f"×{dec(m, 0)}",
            ent(k),
            pct(math.exp(-lam)),
            ic,
            pct_grand(c.precision_relative) if c.precision_relative != float("inf") else "—",
        ])
    return lignes


# ---------------------------------------------------------------------------
# 5. LES RAPPORTS
# ---------------------------------------------------------------------------

def rapport_taille(t: Taille) -> str:
    o: List[str] = []
    a = o.append
    o += bandeau("Taille de test", "combien faut-il pour savoir — et combien ça coûte")

    o += titre("0. Ce que tu as saisi")
    o += tableau(
        ["Entrée", "Valeur", "Conséquence"],
        [
            ["Taux de conversion de référence", pct(t.taux_ref, 2), "le bras témoin, ton taux actuel"],
            ["Écart relatif à détecter", pct_signe(t.ecart_relatif),
             f"taux visé : {pct(t.taux_variante, 2)}"],
            ["Écart absolu correspondant", pts(t.ecart_absolu),
             "c'est LUI que le test doit voir"],
            ["Niveau de confiance", pct(t.confiance, 0), f"z(α/2) = {dec(t.z_alpha)}"],
            ["Puissance", pct(t.puissance, 0), f"z(β) = {dec(t.z_beta)}"],
            ["CPA cible", eur(t.cpa_cible, 2) + " HT" if t.cpa_cible else "non fourni",
             "sert à chiffrer le budget"],
        ],
        ["g", "d", "g"])
    a("")
    o += paragraphe(
        "La confiance protège du faux positif : déclarer un gagnant qui n'existe pas. "
        "La puissance protège du faux négatif : rater un vrai gagnant. Une marque "
        "sous-dimensionne presque toujours la seconde — elle teste avec 80 % de "
        "confiance et 30 % de puissance sans le savoir, et jette deux bons concepts sur trois.")

    o += titre("1. La réponse")
    o += tableau(
        ["Grandeur", "Par variante", "Total (2 bras)"],
        [
            ["Visiteurs", ent(t.visiteurs_par_variante), ent(t.visiteurs_total)],
            ["Conversions attendues — bras témoin", ent(t.conversions_bras_ref), "—"],
            ["Conversions attendues — bras variante", ent(t.conversions_bras_variante), "—"],
            ["Conversions attendues — les deux", "—", ent(t.conversions_total)],
        ] + ([
            ["Budget publicitaire HT", eur(t.budget_par_variante), eur(t.budget_total)],
        ] if t.cpa_cible else []) + ([
            ["Durée à " + ent(t.trafic_jour) + " visiteurs/jour",
             "—", f"{dec(t.jours, 0)} jours"],
        ] if t.trafic_jour > 0 else []),
        ["g", "d", "d"])
    a("")
    a("  Formule employée — test bilatéral sur deux proportions :")
    a("")
    a("    n = ( z(α/2)·√(2·p̄·(1−p̄)) + z(β)·√(p₁(1−p₁) + p₂(1−p₂)) )² ÷ (p₂ − p₁)²")
    a("")
    a(f"    p₁ = {pct(t.taux_ref, 3)}   p₂ = {pct(t.taux_variante, 3)}   "
      f"p̄ = {pct((t.taux_ref + t.taux_variante) / 2, 3)}")
    a(f"    n = ({dec(t.z_alpha)}·{dec(math.sqrt(2 * ((t.taux_ref + t.taux_variante) / 2) * (1 - (t.taux_ref + t.taux_variante) / 2)), 4)}"
      f" + {dec(t.z_beta)}·{dec(math.sqrt(t.taux_ref * (1 - t.taux_ref) + t.taux_variante * (1 - t.taux_variante)), 4)})²"
      f" ÷ {dec(t.ecart_absolu ** 2, 8)} = {ent(t.visiteurs_par_variante)}")
    a("")
    if t.cpa_cible:
        o += paragraphe(
            f"Le chiffre qui décide, ce n'est pas {ent(t.visiteurs_total)} visiteurs : "
            f"c'est {eur(t.budget_total)} HT. Tant que ce budget n'est pas dans le plan média, "
            f"le test n'aura pas lieu — il sera juste arrêté trop tôt et interprété quand même.")

    o += titre("2. Le prix de la précision")
    lignes = []
    for e in ECARTS_TABLE:
        # Un test dimensionne pour une baisse se lit avec des ecarts negatifs.
        te = t.avec_ecart(math.copysign(e, t.ecart_relatif))
        ligne = [pct_signe(te.ecart_relatif, 0), pct(te.taux_variante, 2),
                 ent(te.visiteurs_par_variante), ent(te.conversions_bras_ref)]
        if t.cpa_cible:
            ligne.append(eur(te.budget_total) + " HT")
        if t.trafic_jour > 0:
            ligne.append(f"{dec(te.jours, 0)} j")
        lignes.append(ligne)
    entetes = ["Écart rel.", "Taux visé", "Visiteurs/var.", "Conv./var."]
    aligns = ["d", "d", "d", "d"]
    if t.cpa_cible:
        entetes.append("Budget total")
        aligns.append("d")
    if t.trafic_jour > 0:
        entetes.append("Durée")
        aligns.append("d")
    o += tableau(entetes, lignes, aligns)
    a("")
    o += paragraphe(
        "La taille varie comme l'inverse du CARRÉ de l'écart : diviser l'écart cherché "
        "par deux multiplie le coût du test par quatre. C'est la raison pour laquelle "
        "personne ne mesure proprement un gain de 5 % — et la raison pour laquelle "
        "presque toutes les marques croient l'avoir mesuré.")
    a("")
    o += paragraphe(
        "Lecture inverse, la plus utile : regarde ton budget de test disponible, "
        "lis la ligne correspondante, et tu sais quel est le plus petit écart que tu "
        "es en droit de trancher. Tout le reste, tu le décides sur autre chose que "
        "des chiffres — et il vaut mieux le savoir.")

    o += titre("3. Ce que ce calcul ne dit pas")
    o += puces([
        "Il suppose un test à deux bras, une seule métrique, une seule décision. "
        "Trois variantes testées ensemble triplent les occasions de faux positif : "
        "à 95 % de confiance, une chance sur sept qu'au moins un bras semble gagner "
        "alors qu'aucun ne gagne.",
        "Il suppose que tu regardes le résultat UNE FOIS, à la fin. Regarder tous les "
        "jours et arrêter au premier p < 5 % transforme un test à 5 % de faux positifs "
        "en un test à 20 ou 30 %. C'est la faute la plus répandue du métier, et la "
        "seule que la statistique ne peut pas rattraper après coup.",
        "Il ne dit rien de la validité externe : un gagnant en janvier peut perdre en "
        "novembre, et un gagnant sur trafic froid peut perdre sur trafic de marque.",
    ])
    a("")
    a("═" * LARGEUR)
    return "\n".join(o)


def rapport_comparaison(c: Comparaison) -> str:
    o: List[str] = []
    a = o.append
    o += bandeau("Comparaison de deux variantes", "l'écart observé est-il démontré ?")

    o += titre("0. Les deux bras")
    o += tableau(
        ["Bras", "Visiteurs", "Conversions", "Taux"],
        [["A — référence", ent(c.a_visiteurs), ent(c.a_conversions), pct(c.taux_a, 3)],
         ["B — variante", ent(c.b_visiteurs), ent(c.b_conversions), pct(c.taux_b, 3)],
         ["Les deux réunis", ent(c.a_visiteurs + c.b_visiteurs),
          ent(c.a_conversions + c.b_conversions), pct(c.taux_poole, 3)]],
        ["g", "d", "d", "d"])

    o += titre("1. L'écart et son incertitude")
    ic_bas, ic_haut = c.ic_difference
    icr_bas, icr_haut = c.ic_relatif
    # Un ecart relatif se divise par le taux du bras A : sans conversion en A,
    # il n'est pas infini, il est indefini. On le dit plutot que d'afficher ∞.
    ref_nulle = c.taux_a == 0
    rel_point = "indéfini" if ref_nulle else pct_signe(c.ecart_relatif)
    rel_ic = ("indéfini — référence à 0" if ref_nulle
              else f"{pct_signe(icr_bas)} … {pct_signe(icr_haut)}")
    o += tableau(
        ["Grandeur", "Valeur", "Lecture"],
        [
            ["Écart absolu (B − A)", pts(c.ecart_absolu), "en points de taux"],
            ["Écart relatif", rel_point, "ce que tu annonces en réunion"],
            ["Err. standard — test (poolée)", dec(c.se_poolee * 100, 4) + FINE + "pts",
             "sous H₀ : les 2 bras égaux"],
            ["Err. standard — IC (non poolée)", dec(c.se_non_poolee * 100, 4) + FINE + "pts",
             "chaque bras porte sa variance"],
            ["Score z", dec(c.z), "écart ÷ err. standard poolée"],
            ["Valeur p bilatérale", dec(c.p_valeur, 4),
             "P(cet écart si bras égaux)"],
            [f"IC {pct(c.confiance, 0)} de la différence",
             f"{pts(ic_bas)} … {pts(ic_haut)}", "en points de taux"],
            [f"IC {pct(c.confiance, 0)} en relatif", rel_ic, "le même, en relatif"],
        ],
        ["g", "d", "g"])

    o += titre("2. Le verdict")
    a("")
    a("  ▸ " + c.verdict.upper())
    a("")
    if not c.approximation_fiable:
        o += paragraphe(
            f"Réserve importante : le plus petit effectif attendu vaut "
            f"{dec(c.effectif_attendu_minimal, 1)}, sous le seuil de 5. Le test z repose sur "
            f"une approximation normale de la loi binomiale qui ne tient plus à ce niveau. "
            f"La valeur p ci-dessous est indicative, pas exacte — et à ces volumes, "
            f"la seule conclusion solide est qu'il faut plus de données.")
        a("")
    p = c.p_valeur
    fini = abs(c.ecart_relatif) != float("inf")
    if c.verdict == VERDICT_OUI:
        o += paragraphe(
            f"La valeur p vaut {dec(p, 4)}, sous le seuil de {pct(1 - c.confiance, 0)}. "
            f"Si les deux variantes étaient réellement identiques, un écart au moins aussi "
            f"grand n'apparaîtrait que {pct(p, 2)} du temps. L'écart est démontré — ce qui "
            f"ne veut pas dire qu'il vaut ce que tu as observé.")
        a("")
        if fini:
            o += paragraphe(
                f"Le point de vigilance est ailleurs : l'intervalle va de {pct_signe(icr_bas)} "
                f"à {pct_signe(icr_haut)}. Ton point estimé, {pct_signe(c.ecart_relatif)}, est "
                f"le centre d'un intervalle large. Construis ton plan sur la borne BASSE, pas "
                f"sur le point : c'est ce que le test garantit, et rien de plus.")
        else:
            o += paragraphe(
                f"Le bras de référence n'a aucune conversion : l'écart relatif n'a pas de "
                f"sens ici, seul l'écart absolu en a un. Il va de {pts(ic_bas)} à "
                f"{pts(ic_haut)}. Construis ton plan sur la borne BASSE, pas sur le point : "
                f"c'est ce que le test garantit, et rien de plus.")
    elif c.verdict == VERDICT_FAIBLE:
        o += paragraphe(
            f"La valeur p vaut {dec(p, 4)} : au-dessus du seuil de {pct(1 - c.confiance, 0)}, "
            f"mais assez bas pour que le hasard seul soit une explication inconfortable. "
            f"Ce n'est pas un gagnant. C'est une piste, et une piste ne se déploie pas.")
        a("")
        o += paragraphe(
            f"L'intervalle {pts(ic_bas)} … {pts(ic_haut)} enjambe le zéro : la variante "
            f"peut aussi bien être meilleure que pire. Continuer le test est la seule "
            f"action qui produit de l'information.")
    else:
        o += paragraphe(
            f"La valeur p vaut {dec(p, 4)}. Un écart de cette taille survient couramment "
            f"entre deux bras strictement identiques. L'intervalle de la différence, "
            f"{pts(ic_bas)} … {pts(ic_haut)}, enjambe le zéro largement.")
        a("")
        o += paragraphe(
            "Attention au piège de lecture : « non démontrée » n'est pas « égalité prouvée ». "
            "Tu peux parfaitement arrêter le test — pour des raisons de coût, de calendrier, "
            "de conviction produit. Ce que tu ne peux pas faire, c'est écrire dans un compte "
            "rendu que la variante B est meilleure, ou qu'elle est équivalente.")

    o += titre("3. Ce que cet échantillon pouvait voir")
    manque = c.visiteurs_manquants
    o += tableau(
        ["Grandeur", "Valeur", "Lecture"],
        [
            ["Plus petit écart détectable (MDE)", pct_signe(c.ecart_detectable),
             f"à {pct(c.confiance, 0)} / {pct(c.puissance, 0)} de puissance"],
            ["Écart observé", rel_point, "sous le MDE = invisible ici"],
            ["Visiteurs par bras à ce jour", ent(min(c.a_visiteurs, c.b_visiteurs)), ""],
            ["Visiteurs à ajouter par bras", ent(manque) if manque != float("inf") else "—",
             "si l'écart observé est réel"],
        ] + ([["Budget publicitaire HT à ajouter",
               eur(2 * manque * c.taux_poole * c.cpa_cible), "les deux bras"]]
             if c.cpa_cible and manque != float("inf") else []),
        ["g", "d", "g"])
    a("")
    if not ref_nulle and abs(c.ecart_relatif) < c.ecart_detectable:
        o += paragraphe(
            f"L'écart observé ({pct_signe(c.ecart_relatif)}) est plus petit que ce que "
            f"l'échantillon pouvait détecter ({pct_signe(c.ecart_detectable)}). Ce test "
            f"n'était pas dimensionné pour répondre à la question qu'on lui pose. "
            f"Ce n'est pas un problème de statistique : c'est un problème de plan de test.")
        a("")
    o += paragraphe(
        "Un dernier rappel, qui vaut plus que tout ce qui précède : ces chiffres supposent "
        "que tu as fixé la règle d'arrêt AVANT de lancer le test. Si tu as regardé la courbe "
        "chaque matin en attendant qu'elle passe sous 5 %, la valeur p ci-dessus est fausse, "
        "et elle est fausse dans le sens qui t'arrange.")
    a("")
    a("═" * LARGEUR)
    return "\n".join(o)


def rapport_creatif(c: Creatif) -> str:
    o: List[str] = []
    a = o.append
    o += bandeau("Test de concept publicitaire", "couper, conserver, scaler — ou attendre")

    lam_bas, lam_haut = c.ic_achats
    cpa_bas, cpa_haut = c.ic_cpa

    o += titre("0. Le concept")
    o += tableau(
        ["Entrée", "Valeur"],
        [["Dépense sur ce concept", eur(c.depense, 2) + " HT"],
         ["Achats obtenus", ent(c.achats)],
         ["CPA cible", eur(c.cpa_cible, 2) + " HT"],
         ["Niveau de confiance", pct(c.confiance, 0)]],
        ["g", "d"])

    o += titre("1. Le CPA et son incertitude")
    o += tableau(
        ["Grandeur", "Valeur", "Lecture"],
        [
            ["CPA observé", eur(c.cpa_observe, 2) + " HT" if c.achats else "indéfini",
             "dépense ÷ achats" if c.achats else "aucun achat : rien à diviser"],
            ["Achats — IC " + pct(c.confiance, 0),
             f"{dec(lam_bas, 2)} … {dec(lam_haut, 2)}", "Poisson, intervalle exact"],
            ["CPA — IC " + pct(c.confiance, 0),
             f"{eur(cpa_bas, 2)} … {eur(cpa_haut, 2) if cpa_haut != float('inf') else 'illimité'}",
             "l'IC des achats, inversé"],
            ["Largeur de l'IC / cible",
             pct_grand(c.precision_relative) if c.precision_relative != float("inf") else "—",
             "sous 30 % : décision stable"],
            ["Achats attendus à la cible", dec(c.achats_attendus_a_la_cible, 2),
             "s'il tenait pile la cible"],
            ["P(0 achat) à la cible", pct(c.proba_zero_achat_a_la_cible),
             "part des bons concepts jetés"],
        ],
        ["g", "d", "g"])
    a("")
    o += paragraphe(
        "Un achat publicitaire est un évènement rare et indépendant : sa loi est celle "
        "de Poisson, pas une gaussienne. C'est pour ça que l'intervalle est asymétrique — "
        "la borne haute du CPA est toujours bien plus loin de l'observé que la borne basse. "
        "Un concept médiocre déguisé en bon concept est un accident bien plus fréquent que "
        "l'inverse.")

    o += titre("2. Le verdict")
    a("")
    a("  ▸ " + c.verdict_complet.upper())
    a("")
    v = c.verdict
    if v == VERDICT_COUPER:
        o += paragraphe(
            f"Même dans l'hypothèse la plus favorable que les données autorisent — un CPA "
            f"réel de {eur(cpa_bas, 2)} HT — ce concept reste au-dessus de ta cible de "
            f"{eur(c.cpa_cible, 2)} HT. Ce n'est plus du bruit : c'est un concept qui ne "
            f"tient pas l'économie de ta marque. Coupe-le, et garde l'angle s'il te plaît : "
            f"c'est l'exécution qu'on jette, pas forcément l'idée.")
    elif v == VERDICT_CONSERVER:
        o += paragraphe(
            f"La borne haute du CPA, {eur(cpa_haut, 2)} HT, est sous ta cible de "
            f"{eur(c.cpa_cible, 2)} HT : ce concept tient, et c'est démontré. Il n'est pas "
            f"pour autant démontré qu'il tienne à un budget supérieur. Laisse-le tourner, "
            f"augmente par paliers, et vérifie le CPA à chaque palier — un concept qui tient "
            f"à {eur(c.depense)} HT peut se dégrader à dix fois ce budget, quand l'algorithme "
            f"est obligé d'aller chercher une audience moins qualifiée.")
    elif v == VERDICT_SCALER:
        o += paragraphe(
            f"La borne haute du CPA, {eur(cpa_haut, 2)} HT, est non seulement sous ta cible "
            f"mais sous {pct(MARGE_SCALE, 0)} de ta cible ({eur(c.cpa_cible * MARGE_SCALE, 2)} HT). "
            f"Ce concept a de la marge pour se dégrader en montant en budget et rester rentable. "
            f"C'est la condition qu'on cherche avant de scaler — pas « il a un bon CPA », mais "
            f"« il a un bon CPA avec assez de marge pour survivre à sa propre montée ».")
    else:
        manque = c.depense_manquante
        borne = (f"de {eur(cpa_bas, 2)} à {eur(cpa_haut, 2)} HT"
                 if cpa_haut != float("inf")
                 else f"de {eur(cpa_bas, 2)} HT à l'infini")
        o += paragraphe(
            f"L'intervalle du CPA va {borne} : il enjambe ta cible de "
            f"{eur(c.cpa_cible, 2)} HT. Les données sont compatibles avec « ce concept est "
            f"excellent » ET avec « ce concept est mauvais ». Toute décision prise "
            f"maintenant est un tirage au sort déguisé en analyse.")
        a("")
        if manque != float("inf"):
            o += paragraphe(
                f"Il faut encore {eur(manque)} HT de dépense sur ce concept — "
                f"{eur(c.depense_pour_trancher)} HT au total — pour que l'intervalle cesse "
                f"d'enjamber la cible. C'est le prix de l'information. Si tu n'es pas prêt "
                f"à le payer, la décision honnête n'est pas « je coupe parce que c'est "
                f"mauvais », c'est « je coupe parce que je n'ai pas le budget pour savoir ».")

    o += titre("3. Pourquoi couper trop tôt est une décision prise sur du bruit")
    a("")
    o += paragraphe(c.phrase_du_bruit())
    a("")
    o += paragraphe(
        f"Le seuil sous lequel un zéro achat ne veut strictement rien dire est "
        f"{eur(c.budget_minimum_de_jugement)} HT — soit {dec(ic_poisson(0, c.confiance)[1], 2)} "
        f"fois ton CPA cible. C'est la règle des trois CPA : en dessous de trois à quatre fois "
        f"le CPA visé, l'absence d'achat est le résultat le plus probable même pour un très bon "
        f"concept, et le test n'a produit aucune information.")
    a("")
    o += tableau(
        ["Dépense HT", "= CPA×", "Achats", "P(0 achat)", "IC 95 % du CPA", "Largeur/cible"],
        table_montee_en_depense(c.cpa_cible, [1, 3, 10, 25, 50, 100, 200], c.confiance),
        ["d", "d", "d", "d", "d", "d"])
    a("")
    o += paragraphe(
        "Le tableau suppose le meilleur des cas : un concept qui tient exactement ta cible "
        "et qui rend précisément le nombre d'achats attendu. Lis la colonne P(0 achat) "
        "de haut en bas : c'est la part des BONS concepts qu'élimine un seuil de coupe placé "
        "à ce niveau de dépense. Couper au premier CPA dépensé jette plus d'un tiers de tes "
        "gagnants — et une marque qui procède ainsi conclut ensuite que la création est "
        "difficile, alors que c'est son protocole de jugement qui l'est.")
    a("")
    o += paragraphe(
        "Lis maintenant la dernière colonne. Il faut environ 200 fois le CPA cible pour que "
        "l'intervalle devienne assez étroit pour qu'attendre davantage ne change plus la "
        "décision. C'est le vrai prix d'un verdict propre sur un concept — et c'est pourquoi "
        "on ne juge jamais un concept sur le CPA seul quand le budget de test ne le permet "
        "pas : on le juge sur des évènements plus fréquents, en amont du funnel.")

    o += titre("4. Ce que ce calcul ne dit pas")
    o += puces([
        "Il ne mesure que le CPA. Un concept peut avoir un CPA médiocre et un panier "
        "moyen supérieur, ou une meilleure rétention : c'est la contribution par client "
        "qui décide, pas le CPA seul.",
        "Il suppose que le taux d'achat est stable pendant toute la dépense. Une phase "
        "d'apprentissage algorithmique viole cette hypothèse par construction : le début "
        "de vie d'un concept est presque toujours plus cher que sa suite.",
        "Il traite le concept isolément. Tester 57 concepts par semaine et garder ceux "
        "dont le CPA sort à 95 % de confiance produit mécaniquement des faux gagnants : "
        "à ce rythme, environ trois par semaine sortent du lot par hasard seul.",
        "Il ignore l'incrémentalité : un concept peut afficher un excellent CPA en "
        "récoltant une demande qui serait venue sans lui.",
    ])
    a("")
    a("═" * LARGEUR)
    return "\n".join(o)


# ---------------------------------------------------------------------------
# 6. DÉMONSTRATION ET CONTRÔLES
# ---------------------------------------------------------------------------

# Chiffres canoniques utilises par la demonstration.
# Source : ecommerce/donnees/chiffres-canoniques.md
CANON_NCAC_P5 = 40.03          # § 2.4 — nCAC au palier P5
CANON_BUDGET_TEST_P5 = 51_722  # § 6 — budget de test hebdomadaire au palier P5
CANON_CONCEPTS_P5 = 57         # § 6 — concepts testes par semaine au palier P5
CANON_NCAC_P2 = 30.78          # § 2.4 — nCAC au palier P2
CANON_BUDGET_TEST_P2 = 3_622   # § 6 — budget de test hebdomadaire au palier P2
CANON_CONCEPTS_P2 = 14         # § 6 — concepts testes par semaine au palier P2

# Hypothese pedagogique, propre a la demonstration : les chiffres canoniques
# ne figent pas de taux de conversion du site. 2,00 % est un ordre de grandeur
# de marque DTC premium sur trafic payant, pas un canonique.
HYP_TAUX_SITE = 0.0200
HYP_TRAFIC_JOUR = 3_000


def table_montee_en_echantillon(taux_a: float, taux_b: float,
                                tailles: Sequence[int],
                                confiance: float = 0.95) -> List[List[str]]:
    """Les mêmes deux taux, à des tailles d'échantillon croissantes."""
    lignes = []
    for n in tailles:
        c = Comparaison(n, round(n * taux_a), n, round(n * taux_b), confiance)
        lignes.append([ent(n), ent(c.a_conversions), ent(c.b_conversions),
                       dec(c.z, 2), dec(c.p_valeur, 4), c.verdict_court])
    return lignes


def controles() -> List[Tuple[str, str, str, bool]]:
    """Contrôles de plausibilité. (libellé, attendu, obtenu, conforme)"""
    res: List[Tuple[str, str, str, bool]] = []

    def _nu(x: str) -> str:
        """Neutralise l'espace fine insecable : elle est invisible, pas les ecarts."""
        return x.replace(FINE, " ")

    def ajoute(lib: str, attendu: str, obtenu: str) -> None:
        res.append((lib, attendu, obtenu, _nu(attendu) == _nu(obtenu)))

    ajoute("z(97,5 %) — table normale", "1,960", dec(phi_inverse(0.975)))
    ajoute("z(80 %) — puissance standard", "0,842", dec(phi_inverse(0.80)))
    ajoute("z(90 %) — puissance renforcée", "1,282", dec(phi_inverse(0.90)))
    ajoute("p bilatérale pour z = 1,960", "5,00 %", pct(p_bilaterale(phi_inverse(0.975)), 2))
    ajoute("IC Poisson k = 0 — borne haute", "3,69", dec(ic_poisson(0)[1], 2))
    ajoute("IC Poisson k = 1 — Garwood", "0,03 … 5,57",
           f"{dec(ic_poisson(1)[0], 2)} … {dec(ic_poisson(1)[1], 2)}")
    ajoute("IC Poisson k = 10 — Garwood", "4,80 … 18,39",
           f"{dec(ic_poisson(10)[0], 2)} … {dec(ic_poisson(10)[1], 2)}")
    ajoute("IC Poisson k = 100 — Garwood", "81,36 … 121,63",
           f"{dec(ic_poisson(100)[0], 2)} … {dec(ic_poisson(100)[1], 2)}")

    # Plausibilite du dimensionnement : +10 % relatif sur un taux de 2 %.
    t = Taille(0.02, 0.10, 0.95, 0.80, CANON_NCAC_P5)
    n = t.visiteurs_par_variante
    res.append(("+10 % rel. sur 2 % — visiteurs/var.", "60 000 – 110 000",
                ent(n), 60_000 <= n <= 110_000))
    conv = t.conversions_bras_ref
    res.append(("+10 % rel. sur 2 % — conv./variante", "≥ 1 000",
                ent(conv), conv >= 1_000))
    res.append(("+10 % rel. sur 2 % — conv., 2 bras", "≥ 2 000",
                ent(t.conversions_total), t.conversions_total >= 2_000))
    # Loi en 1/écart² : diviser l'écart par 2 doit multiplier n par ~4.
    ratio = Taille(0.02, 0.10).visiteurs_par_variante / Taille(0.02, 0.20).visiteurs_par_variante
    res.append(("n en 1/écart² : n(10 %)/n(20 %)", "≈ 4", dec(ratio, 2), 3.7 <= ratio <= 4.1))
    # Budget = conversions totales x CPA cible.
    res.append(("Budget = conv. totales × CPA", eur(t.conversions_total * CANON_NCAC_P5),
                eur(t.budget_total), abs(t.budget_total - t.conversions_total * CANON_NCAC_P5) < 1))
    # Symetrie du test : intervertir les deux bras ne change pas |z|.
    c1, c2 = Comparaison(12_000, 240, 12_000, 276), Comparaison(12_000, 276, 12_000, 240)
    res.append(("Symétrie : |z(A,B)| = |z(B,A)|", dec(abs(c1.z)), dec(abs(c2.z)),
                abs(abs(c1.z) - abs(c2.z)) < 1e-12))
    # La regle des trois CPA.
    cr = Creatif(40.0, 0, CANON_NCAC_P5)
    res.append(("Budget mini de jugement (3,69×CPA)",
                eur(3.688879 * CANON_NCAC_P5, 2), eur(cr.budget_minimum_de_jugement, 2),
                abs(cr.budget_minimum_de_jugement - 3.688879 * CANON_NCAC_P5) < 0.01))
    return res


def rapport_demo() -> Tuple[str, bool]:
    o: List[str] = []
    a = o.append
    o += bandeau("Démonstration — les trois modes",
                 "sur les chiffres canoniques de NØRA (marque fictive)")
    a("")
    o += paragraphe(
        "Les chiffres canoniques ne figent pas de taux de conversion du site : "
        f"le {pct(HYP_TAUX_SITE, 2)} utilisé ci-dessous est une hypothèse de démonstration, "
        f"pas un canonique. Le CPA cible {eur(CANON_NCAC_P5, 2)} HT est le nCAC du palier P5 "
        "(chiffres canoniques § 2.4). Le budget de test hebdomadaire "
        f"{eur(CANON_BUDGET_TEST_P5)} HT et les {CANON_CONCEPTS_P5} concepts testés par semaine "
        "viennent du § 6.")
    a("")

    # -- A ------------------------------------------------------------------
    a("")
    a("┌" + "─" * (LARGEUR - 2) + "┐")
    a("│ A. --taille — DIMENSIONNER UN TEST DE CONVERSION AVANT DE LE LANCER".ljust(LARGEUR - 1) + "│")
    a("└" + "─" * (LARGEUR - 2) + "┘")
    t = Taille(HYP_TAUX_SITE, 0.10, 0.95, 0.80, CANON_NCAC_P5, HYP_TRAFIC_JOUR)
    a(rapport_taille(t))
    a("")
    o += paragraphe(
        f"Mise en perspective : {eur(t.budget_total)} HT pour trancher un écart de 10 %, "
        f"quand le budget de test hebdomadaire du palier P5 est de {eur(CANON_BUDGET_TEST_P5)} HT "
        f"(§ 6). Ce seul test consommerait "
        f"{dec(t.budget_total / CANON_BUDGET_TEST_P5, 1)} semaines de budget de test. "
        "Voilà pourquoi une marque à 1 M€/semaine teste des écarts de 20 à 30 %, "
        "pas de 5 % — et pourquoi une marque au palier P1 ne teste pas du tout son taux de "
        "conversion : elle n'a pas le trafic pour se le permettre, et elle a mieux à faire.")
    a("")

    # -- B ------------------------------------------------------------------
    a("")
    a("┌" + "─" * (LARGEUR - 2) + "┐")
    a("│ B. --comparer — DEUX VARIANTES OBSERVÉES".ljust(LARGEUR - 1) + "│")
    a("└" + "─" * (LARGEUR - 2) + "┘")
    c = Comparaison(12_000, 240, 12_000, 276, 0.95, 0.80, CANON_NCAC_P5)
    a(rapport_comparaison(c))
    a("")
    o += titre("Le même écart, à des tailles d'échantillon croissantes")
    o += tableau(
        ["Visiteurs/bras", "Conv. A", "Conv. B", "z", "p", "Verdict"],
        table_montee_en_echantillon(0.0200, 0.0230, [3_000, 6_000, 12_000, 25_000, 40_000]),
        ["d", "d", "d", "d", "d", "g"])
    a("")
    o += paragraphe(
        "Les taux ne bougent pas d'une ligne à l'autre : 2,00 % contre 2,30 %, toujours. "
        "Seule la taille change. Le même écart passe de « non démontrée » à « démontrée » "
        "sans qu'aucune information nouvelle sur les variantes n'ait été produite — "
        "seulement de la précision. Une équipe qui arrête un test au moment où il croise "
        "la ligne des 5 % ne mesure pas un gagnant : elle mesure sa propre patience.")
    a("")

    # -- C ------------------------------------------------------------------
    a("")
    a("┌" + "─" * (LARGEUR - 2) + "┐")
    a("│ C. --creatif — LE CONCEPT COUPÉ À 40 € DE DÉPENSE".ljust(LARGEUR - 1) + "│")
    a("└" + "─" * (LARGEUR - 2) + "┘")
    cr = Creatif(40.0, 0, CANON_NCAC_P5)
    a(rapport_creatif(cr))
    a("")
    o += titre("Le même concept, à mesure que la dépense s'accumule")
    budget_concept = CANON_BUDGET_TEST_P5 / CANON_CONCEPTS_P5
    lignes = []
    for depense, achats in [(40, 0), (150, 2), (400, 9), (budget_concept, 22),
                            (budget_concept, 35), (2 * budget_concept, 71)]:
        cc = Creatif(depense, achats, CANON_NCAC_P5)
        cpa_bas, cpa_haut = cc.ic_cpa
        lignes.append([
            eur(depense) + " HT", ent(achats),
            eur(cc.cpa_observe, 2) if achats else "—",
            f"{eur(cpa_bas, 2)} – {eur(cpa_haut, 2) if cpa_haut != float('inf') else 'illimité'}",
            cc.verdict,
        ])
    o += tableau(["Dépense", "Achats", "CPA observé", "IC 95 % du CPA", "Verdict"],
                 lignes, ["d", "d", "d", "d", "g"])
    a("")
    o += paragraphe(
        f"Le budget de test du palier P5 donne {eur(budget_concept)} HT par concept "
        f"({eur(CANON_BUDGET_TEST_P5)} ÷ {CANON_CONCEPTS_P5} concepts, § 6), soit "
        f"{dec(budget_concept / CANON_NCAC_P5, 1)} achats attendus si le concept tient la cible. "
        "C'est le minimum pour qu'un verdict existe — et c'est encore trop peu pour distinguer "
        "un bon concept d'un excellent.")
    a("")
    budget_concept_p2 = CANON_BUDGET_TEST_P2 / CANON_CONCEPTS_P2
    o += paragraphe(
        f"Au palier P2 le même calcul donne {eur(budget_concept_p2)} HT par concept "
        f"({eur(CANON_BUDGET_TEST_P2)} ÷ {CANON_CONCEPTS_P2}, § 6) pour un nCAC de "
        f"{eur(CANON_NCAC_P2, 2)} HT, soit {dec(budget_concept_p2 / CANON_NCAC_P2, 1)} achats "
        "attendus. À ce stade, aucun test de concept isolé n'est concluant : la marque juge "
        "ses créations sur des signaux amont — taux de clic, taux de vue à 3 secondes, "
        "ajouts au panier — parce que ce sont les seuls évènements assez fréquents pour être "
        "mesurables à ce budget. C'est une contrainte statistique, pas une préférence.")
    a("")

    # -- D ------------------------------------------------------------------
    ctrl = controles()
    ok = all(c[3] for c in ctrl)
    o += titre("D. Contrôles — les valeurs sont-elles justes et plausibles ?")
    o += tableau(
        ["Contrôle", "Attendu", "Obtenu", ""],
        [[lib, att, obt, "ok" if conf else "ÉCART"] for lib, att, obt, conf in ctrl],
        ["g", "d", "d", "g"])
    a("")
    a("  Références des valeurs attendues : table de la loi normale ; intervalles de")
    a("  Garwood publiés pour la loi de Poisson ; chiffres canoniques § 2.4 et § 6.")
    a("  " + ("Tous les contrôles passent." if ok
              else "AU MOINS UN ÉCART : ne te sers pas de ces sorties avant correction."))
    a("")
    a("═" * LARGEUR)
    return "\n".join(o), ok


# ---------------------------------------------------------------------------
# 7. LIGNE DE COMMANDE
# ---------------------------------------------------------------------------

def construire_parseur() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="test_significativite.py",
        description="Calculateur de significativité et de taille de test.\n"
                    "Empêche de couper un concept créatif sur du bruit,\n"
                    "et de déclarer un test A/B gagnant trop tôt.",
        epilog="Les pourcentages se saisissent en points : --taux 2 vaut 2 % de conversion.\n"
               "La virgule décimale est acceptée partout. Toute dépense est HT.\n"
               "Chiffres de démonstration : ecommerce/donnees/chiffres-canoniques.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    m = p.add_argument_group("modes — un seul à la fois")
    m.add_argument("--taille", action="store_true",
                   help="combien de visiteurs, de conversions et d'euros pour détecter un écart")
    m.add_argument("--comparer", action="store_true",
                   help="deux variantes observées : l'écart est-il démontré ?")
    m.add_argument("--creatif", action="store_true",
                   help="un concept publicitaire : à couper, à conserver, à scaler, ou trop tôt")
    m.add_argument("--demo", action="store_true",
                   help="démonstration des trois modes sur les chiffres canoniques de NØRA")

    g = p.add_argument_group("--taille")
    g.add_argument("--taux", type=nombre, default=2.0, metavar="%",
                   help="taux de conversion de référence, en %% (défaut : 2)")
    g.add_argument("--ecart", type=nombre, default=10.0, metavar="%",
                   help="écart RELATIF à détecter, en %% (défaut : 10, soit 2,00 %% → 2,20 %%)")
    g.add_argument("--trafic-jour", type=nombre, default=0.0, metavar="N",
                   help="visiteurs par jour, tous bras confondus — pour convertir en durée")

    g = p.add_argument_group("--comparer")
    g.add_argument("--a-visiteurs", type=nombre, metavar="N", help="visiteurs du bras A (référence)")
    g.add_argument("--a-conversions", type=nombre, metavar="N", help="conversions du bras A")
    g.add_argument("--b-visiteurs", type=nombre, metavar="N", help="visiteurs du bras B (variante)")
    g.add_argument("--b-conversions", type=nombre, metavar="N", help="conversions du bras B")

    g = p.add_argument_group("--creatif")
    g.add_argument("--depense", type=nombre, metavar="€HT",
                   help="budget déjà dépensé sur ce concept, HT")
    g.add_argument("--achats", type=nombre, metavar="N", help="achats obtenus sur ce concept")

    g = p.add_argument_group("communs")
    g.add_argument("--confiance", type=nombre, default=95.0, metavar="%",
                   help="niveau de confiance, en %% (défaut : 95)")
    g.add_argument("--puissance", type=nombre, default=80.0, metavar="%",
                   help="puissance statistique, en %% (défaut : 80)")
    g.add_argument("--cpa-cible", type=nombre, default=None, metavar="€HT",
                   help="coût par acquisition visé, HT — obligatoire pour --creatif")
    return p


def _echec(messages: Sequence[str]) -> int:
    for m in messages:
        print("Erreur de saisie : " + m, file=sys.stderr)
    return 2


def main(argv: Optional[List[str]] = None) -> int:
    parseur = construire_parseur()
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        parseur.print_help()
        print("\nAucun mode demandé. Commence par --demo pour voir les trois modes "
              "tourner sur les chiffres canoniques de NØRA.")
        return 2

    ns = parseur.parse_args(argv)
    modes = [ns.taille, ns.comparer, ns.creatif, ns.demo]
    if sum(1 for m in modes if m) != 1:
        return _echec(["choisis exactement un mode : --taille, --comparer, --creatif ou --demo."])

    confiance, puissance = ns.confiance / 100, ns.puissance / 100

    if ns.demo:
        txt, ok = rapport_demo()
        print(txt)
        return 0 if ok else 1

    if ns.taille:
        t = Taille(ns.taux / 100, ns.ecart / 100, confiance, puissance,
                   ns.cpa_cible or 0.0, ns.trafic_jour)
        alertes = t.valider()
        if alertes:
            return _echec(alertes)
        print(rapport_taille(t))
        return 0

    if ns.comparer:
        manquants = [nom for nom, v in
                     (("--a-visiteurs", ns.a_visiteurs), ("--a-conversions", ns.a_conversions),
                      ("--b-visiteurs", ns.b_visiteurs), ("--b-conversions", ns.b_conversions))
                     if v is None]
        if manquants:
            return _echec([f"--comparer a besoin de : {', '.join(manquants)}."])
        c = Comparaison(ns.a_visiteurs, ns.a_conversions, ns.b_visiteurs, ns.b_conversions,
                        confiance, puissance, ns.cpa_cible or 0.0)
        alertes = c.valider()
        if alertes:
            return _echec(alertes)
        print(rapport_comparaison(c))
        return 0

    manquants = [nom for nom, v in (("--depense", ns.depense), ("--achats", ns.achats),
                                    ("--cpa-cible", ns.cpa_cible)) if v is None]
    if manquants:
        return _echec([f"--creatif a besoin de : {', '.join(manquants)}."])
    cr = Creatif(ns.depense, int(ns.achats), ns.cpa_cible, confiance)
    alertes = cr.valider()
    if alertes:
        return _echec(alertes)
    print(rapport_creatif(cr))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
