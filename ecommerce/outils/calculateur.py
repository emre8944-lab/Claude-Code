#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculateur de sante economique d'une marque DTC.

Cet outil prend TES chiffres — pas ceux du cursus — et rend un diagnostic
complet : la cascade de marge, les seuils de MER, le cout d'acquisition, la
LTV, un verdict en clair, la table des leviers classee par gain, et les trois
choses a faire ensuite.

Il ne fabrique aucun chiffre. Tout ce qu'il affiche est derive de ce que tu
saisis. Quand une hypothese de modelisation est necessaire (la forme de la
courbe de reachat entre tes deux points de mesure), elle est signalee dans le
rapport.

Usage
-----
    # mode interactif — lance sans aucun argument, il te pose les questions
    python3 ecommerce/outils/calculateur.py

    # mode arguments — tout ce qui n'est pas fourni prend sa valeur par defaut
    python3 ecommerce/outils/calculateur.py --aov-premiere 64 --aov-reachat 85 \
        --cogs 14,5 --logistique 11 --pub 1494206 --commandes 60200

    # mode valeurs par defaut, sans questions
    python3 ecommerce/outils/calculateur.py --defauts

    # mode demonstration — tourne sur le palier P5 de NORA et verifie que les
    # chiffres canoniques sont retrouves
    python3 ecommerce/outils/calculateur.py --demo

Les nombres s'ecrivent indifferemment « 14,5 » ou « 14.5 », avec ou sans
espaces, avec ou sans le signe % ou €. Les pourcentages se saisissent en
points : --cogs 14,5 veut dire 14,5 % du CA HT.

Conventions de sortie : français, virgule decimale, espace avant % et €, tout
montant marque TTC ou HT. Voir ecommerce/CHARTE.md § 5.

Python 3.9+. Aucune dependance externe.
Reference des chiffres de demonstration : ecommerce/donnees/chiffres-canoniques.md
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple

LARGEUR = 78


# ---------------------------------------------------------------------------
# 0. FORMATAGE — mêmes conventions que modele_nora.py
# ---------------------------------------------------------------------------

def eur(x: float, d: int = 0) -> str:
    """Formate un montant en euros, espace comme separateur de milliers."""
    s = f"{x:,.{d}f}".replace(",", " ").replace(".", ",").replace("-", "−")
    return s + " €"


def pct(x: float, d: int = 1) -> str:
    """Formate une proportion (0,615) en pourcentage francais (61,5 %)."""
    return f"{x * 100:.{d}f}".replace(".", ",") + " %"


def dec(x: float, d: int = 2) -> str:
    """Formate un nombre decimal nu (un MER, un ratio)."""
    return f"{x:.{d}f}".replace(".", ",")


def ent(x: float) -> str:
    """Formate un entier avec separateur de milliers."""
    return f"{x:,.0f}".replace(",", " ")


def pts(x: float, d: int = 1) -> str:
    """Formate un ecart en points de pourcentage, signe compris."""
    return f"{x * 100:+.{d}f}".replace(".", ",") + " pts"


def nombre(s: str) -> float:
    """Lit un nombre ecrit a la francaise ou a l'anglaise. « 1 494 206,50 € » -> float."""
    t = str(s)
    for parasite in (" ", " ", " ", "€", "%", " "):
        t = t.replace(parasite, "")
    t = t.replace("−", "-").replace(",", ".")
    if t in ("", "-", "+"):
        raise ValueError(f"« {s} » n'est pas un nombre")
    try:
        return float(t)
    except ValueError:
        raise ValueError(f"« {s} » n'est pas un nombre")


def titre(t: str) -> List[str]:
    return ["", t.upper(), "─" * LARGEUR]


def tableau(entetes: Sequence[str], lignes: Sequence[Sequence[str]],
            aligns: Sequence[str], indent: str = "  ") -> List[str]:
    """Rend un tableau texte a colonnes alignees. 'g' = gauche, 'd' = droite."""
    cols = list(zip(*([entetes] + [list(l) for l in lignes]))) if lignes else [(e,) for e in entetes]
    larg = [max(len(c) for c in col) for col in cols]

    def rendre(cells: Sequence[str]) -> str:
        out = []
        for c, w, a in zip(cells, larg, aligns):
            out.append(c.ljust(w) if a == "g" else c.rjust(w))
        return indent + "  ".join(out).rstrip()

    res = [rendre(entetes), indent + "  ".join("─" * w for w in larg)]
    for l in lignes:
        res.append(rendre(l))
    return res


# ---------------------------------------------------------------------------
# 1. LES ENTREES
# ---------------------------------------------------------------------------

@dataclass
class Entrees:
    """Les quatorze nombres que tu dois connaitre sur ta propre marque."""

    aov_premiere_ttc: float     # panier moyen TTC d'une premiere commande
    aov_reachat_ttc: float      # panier moyen TTC d'une commande de reachat
    tva: float                  # taux de TVA moyen pondere, en proportion
    cogs: float                 # cout marchandise, en % du CA HT
    logistique: float           # transport + pick & pack + emballage, en % du CA HT
    psp: float                  # commissions d'encaissement, en % du CA HT
    retours: float              # retours et SAV, en % du CA HT
    remises: float              # codes promo, soldes, ventes privees, en % du CA HT
    pub_mois: float             # depense publicitaire mensuelle, tout canal confondu
    commandes_mois: float       # nombre total de commandes par mois
    part_reachat: float         # part des commandes passees par un client deja acquis
    fixes_mois: float           # salaires, loyers, outils, honoraires — hors pub
    passage_90j: float          # taux de passage 1re -> 2e commande a 90 jours
    reachats_12m: float         # nombre moyen de reachats par client acquis a 12 mois

    def valider(self) -> List[str]:
        """Renvoie la liste des anomalies bloquantes ou suspectes."""
        alertes: List[str] = []
        if self.commandes_mois <= 0:
            alertes.append("Le nombre de commandes mensuelles doit être strictement positif.")
        if self.aov_premiere_ttc <= 0 or self.aov_reachat_ttc <= 0:
            alertes.append("Les paniers moyens TTC doivent être strictement positifs.")
        if not 0 <= self.part_reachat < 1:
            alertes.append("La part de commandes en réachat doit être comprise entre 0 % et 100 %.")
        if self.tva < 0 or self.tva > 0.5:
            alertes.append("Le taux de TVA saisi est hors de toute plage européenne plausible.")
        if self.pub_mois < 0 or self.fixes_mois < 0:
            alertes.append("La dépense publicitaire et les frais fixes ne peuvent pas être négatifs.")
        return alertes


# La demonstration : palier P5 de NORA, tel que fige dans
# ecommerce/donnees/chiffres-canoniques.md § 2, § 2.1, § 2.2 et § 3.
# Le taux de passage a 90 jours est la valeur canonique de reachats cumules a
# 3 mois (0,34, § 3) : a cet horizon la troisieme commande est marginale, les
# deux grandeurs se confondent a moins de deux points pres.
def entrees_demo() -> Entrees:
    commandes = 60_200
    part_reachat = 0.38
    aov_new, aov_rep = 64.00, 85.00
    ca_ttc = (commandes * (1 - part_reachat) * aov_new
              + commandes * part_reachat * aov_rep)
    return Entrees(
        aov_premiere_ttc=aov_new,
        aov_reachat_ttc=aov_rep,
        tva=0.20,
        cogs=0.145,
        logistique=0.110,
        psp=0.0155,
        retours=0.035,
        remises=0.080,
        pub_mois=ca_ttc / 2.90,      # MER canonique de P5 = 2,90
        commandes_mois=commandes,
        part_reachat=part_reachat,
        fixes_mois=360_000,
        passage_90j=0.34,
        reachats_12m=1.24,
    )


def entrees_defaut() -> Entrees:
    """Valeurs par defaut : une marque francaise en phase de traction.

    Ce sont des ordres de grandeur de depart, PAS des chiffres canoniques.
    Remplace-les par les tiens : c'est tout l'interet de l'outil.
    """
    return Entrees(
        aov_premiere_ttc=55.00,
        aov_reachat_ttc=72.00,
        tva=0.20,
        cogs=0.180,
        logistique=0.140,
        psp=0.017,
        retours=0.025,
        remises=0.050,
        pub_mois=104_636.00,
        commandes_mois=4_000,
        part_reachat=0.15,
        fixes_mois=28_000,
        passage_90j=0.30,
        reachats_12m=1.10,
    )


# ---------------------------------------------------------------------------
# 2. LE DIAGNOSTIC
# ---------------------------------------------------------------------------

# Forme de la courbe de reachat, calibree sur la courbe canonique de NORA
# (chiffres canoniques § 3 : 0,06 / 0,34 / 0,72 / 1,24 reachats par client
# acquis a 1, 3, 6 et 12 mois). On ne reprend PAS ses niveaux — ceux-la
# viennent de tes deux mesures — seulement ses proportions.
PART_M1_DANS_M3 = 0.06 / 0.34          # ≈ 0,176
PART_M6_ENTRE_M3_ET_M12 = (0.72 - 0.34) / (1.24 - 0.34)   # ≈ 0,422


@dataclass
class Diagnostic:
    e: Entrees

    # -- volumes et chiffre d'affaires -------------------------------------
    @property
    def commandes_reachat(self) -> float:
        return self.e.commandes_mois * self.e.part_reachat

    @property
    def commandes_premieres(self) -> float:
        return self.e.commandes_mois - self.commandes_reachat

    @property
    def ca_premieres_ttc(self) -> float:
        return self.commandes_premieres * self.e.aov_premiere_ttc

    @property
    def ca_reachat_ttc(self) -> float:
        return self.commandes_reachat * self.e.aov_reachat_ttc

    @property
    def ca_ttc(self) -> float:
        return self.ca_premieres_ttc + self.ca_reachat_ttc

    @property
    def ca_ht(self) -> float:
        return self.ca_ttc / (1 + self.e.tva)

    @property
    def tva_collectee(self) -> float:
        return self.ca_ttc - self.ca_ht

    @property
    def ca_semaine_ttc(self) -> float:
        return self.ca_ttc * 12 / 52

    @property
    def aov_mixte_ttc(self) -> float:
        return self.ca_ttc / self.e.commandes_mois

    @property
    def part_ca_reachat(self) -> float:
        return self.ca_reachat_ttc / self.ca_ttc

    # -- cascade de marge --------------------------------------------------
    @property
    def cm1(self) -> float:
        """Marge marchandise : CA HT − COGS."""
        return self.ca_ht * (1 - self.e.cogs)

    @property
    def taux_cm1(self) -> float:
        return 1 - self.e.cogs

    @property
    def taux_variable_hors_cogs(self) -> float:
        return self.e.logistique + self.e.psp + self.e.retours + self.e.remises

    @property
    def taux_marge_brute(self) -> float:
        """CM2 en % du CA HT : ce qui reste apres TOUS les couts variables."""
        return 1 - self.e.cogs - self.taux_variable_hors_cogs

    @property
    def cm2(self) -> float:
        return self.ca_ht * self.taux_marge_brute

    @property
    def pub_pct_ht(self) -> float:
        """Le piege : le MER se calcule sur le TTC, la marge sur le HT."""
        return self.e.pub_mois / self.ca_ht

    @property
    def cm3(self) -> float:
        return self.cm2 - self.e.pub_mois

    @property
    def taux_cm3(self) -> float:
        return self.taux_marge_brute - self.pub_pct_ht

    @property
    def taux_fixes(self) -> float:
        return self.e.fixes_mois / self.ca_ht

    @property
    def ebitda(self) -> float:
        return self.cm3 - self.e.fixes_mois

    @property
    def taux_ebitda(self) -> float:
        return self.ebitda / self.ca_ht

    @property
    def ebitda_annuel(self) -> float:
        return self.ebitda * 12

    # -- MER ---------------------------------------------------------------
    @property
    def mer(self) -> float:
        """CA TTC / depense publicitaire. Infini si tu ne depenses rien."""
        if self.e.pub_mois <= 0:
            return float("inf")
        return self.ca_ttc / self.e.pub_mois

    @property
    def mer_seuil_cm3(self) -> float:
        """MER minimum pour un CM3 nul : (1 + TVA) / marge brute."""
        if self.taux_marge_brute <= 0:
            return float("inf")
        return (1 + self.e.tva) / self.taux_marge_brute

    @property
    def mer_seuil_ebitda(self) -> float:
        """MER minimum pour couvrir aussi les frais fixes."""
        dispo = self.taux_marge_brute - self.taux_fixes
        if dispo <= 0:
            return float("inf")
        return (1 + self.e.tva) / dispo

    @property
    def ecart_seuil_cm3(self) -> float:
        if self.mer_seuil_cm3 in (0.0, float("inf")) or self.mer == float("inf"):
            return float("inf")
        return self.mer / self.mer_seuil_cm3 - 1

    @property
    def ecart_seuil_ebitda(self) -> float:
        if self.mer_seuil_ebitda == float("inf") or self.mer == float("inf"):
            return float("-inf") if self.mer_seuil_ebitda == float("inf") else float("inf")
        return self.mer / self.mer_seuil_ebitda - 1

    # -- acquisition -------------------------------------------------------
    @property
    def ncac(self) -> float:
        """Cout d'acquisition d'un nouveau client : toute la pub / premieres commandes."""
        if self.commandes_premieres <= 0:
            return float("inf")
        return self.e.pub_mois / self.commandes_premieres

    @property
    def contribution_premiere(self) -> float:
        return (self.e.aov_premiere_ttc / (1 + self.e.tva)) * self.taux_marge_brute

    @property
    def contribution_reachat(self) -> float:
        return (self.e.aov_reachat_ttc / (1 + self.e.tva)) * self.taux_marge_brute

    @property
    def marge_premiere_commande(self) -> float:
        """Positif = le client est paye des la 1re commande. Negatif = finance par le reachat."""
        return self.contribution_premiere - self.ncac

    @property
    def reachats_pour_rembourser(self) -> float:
        """Combien de reachats par client acquis suffisent a couvrir le deficit initial."""
        if self.marge_premiere_commande >= 0:
            return 0.0
        if self.contribution_reachat <= 0:
            return float("inf")
        return -self.marge_premiere_commande / self.contribution_reachat

    # -- cohorte et LTV ----------------------------------------------------
    @property
    def courbe(self) -> Dict[int, float]:
        """Reachats cumules par client acquis, aux quatre jalons.

        Ancree sur TES deux mesures (90 jours et 12 mois). Les jalons 1 et
        6 mois sont interpoles avec la forme de la courbe canonique de NORA.
        """
        r3 = self.e.passage_90j
        r12 = self.e.reachats_12m
        r1 = r3 * PART_M1_DANS_M3
        r6 = r3 + PART_M6_ENTRE_M3_ET_M12 * (r12 - r3)
        return {1: r1, 3: r3, 6: r6, 12: r12}

    def ltv(self, mois: int) -> float:
        """LTV en marge de contribution — la seule qui serve a decider."""
        return self.contribution_premiere + self.courbe[mois] * self.contribution_reachat

    @property
    def ltv_12m(self) -> float:
        return self.ltv(12)

    @property
    def ltv_sur_cac(self) -> float:
        if self.ncac <= 0 or self.ncac == float("inf"):
            return float("inf")
        return self.ltv_12m / self.ncac

    @property
    def payback_mois(self) -> float:
        """Mois ou la contribution cumulee d'un client rattrape son cout d'acquisition."""
        cac = self.ncac
        if cac == float("inf"):
            return float("inf")
        cum = self.contribution_premiere
        if cum >= cac:
            return 0.0
        prev_m, prev_c = 0.0, cum
        for m in (1, 3, 6, 12):
            c = self.ltv(m)
            if c >= cac:
                if c == prev_c:
                    return float(m)
                return prev_m + (cac - prev_c) / (c - prev_c) * (m - prev_m)
            prev_m, prev_c = float(m), c
        return float("inf")


# ---------------------------------------------------------------------------
# 3. SENSIBILITE — quel levier vaut le plus ?
# ---------------------------------------------------------------------------

def sensibilite(d: Diagnostic) -> List[Tuple[str, float]]:
    """Effet sur l'EBITDA ANNUEL de chaque amelioration, toutes choses egales.

    Meme decomposition que ecommerce/outils/modele_nora.py § 7, pour que les
    deux outils ne puissent pas se contredire.
    """
    e = d.e
    base = d.ebitda_annuel
    res: List[Tuple[str, float]] = []

    # +10 % d'AOV : CA +10 % a nombre de commandes constant. La logistique est
    # un cout PAR COMMANDE : en euros elle ne bouge pas, donc son poids en % du
    # CA baisse. C'est exactement ce qui rend l'AOV superieur a la conversion.
    marge_aov = d.taux_marge_brute + e.logistique * (1 - 1 / 1.10)
    res.append(("+10 % de panier moyen (AOV, à commandes constantes)",
                (d.ca_ht * 1.10 * marge_aov - e.pub_mois - e.fixes_mois) * 12 - base))

    # +10 % de conversion : meme depense pub, +10 % de commandes et de CA.
    res.append(("+10 % de taux de conversion du site (à budget pub constant)",
                (d.ca_ht * 1.10 * d.taux_marge_brute - e.pub_mois - e.fixes_mois) * 12 - base))

    # -10 % de COGS : la marge brute gagne 10 % du poids du COGS.
    res.append(("−10 % de coût marchandise (COGS)",
                (d.ca_ht * (d.taux_marge_brute + e.cogs * 0.10)
                 - e.pub_mois - e.fixes_mois) * 12 - base))

    # +10 % de reachat : les commandes de reachat augmentent de 10 %.
    ca2_ttc = d.ca_premieres_ttc + d.commandes_reachat * 1.10 * e.aov_reachat_ttc
    res.append(("+10 % de commandes de réachat",
                (ca2_ttc / (1 + e.tva) * d.taux_marge_brute
                 - e.pub_mois - e.fixes_mois) * 12 - base))

    # -10 % de CAC a volume constant : meme CA, depense pub -10 %.
    res.append(("−10 % de CAC à volume constant",
                (d.cm2 - e.pub_mois * 0.90 - e.fixes_mois) * 12 - base))

    # -1 point de taux de retour / SAV.
    res.append(("−1 point de taux de retour / SAV",
                (d.ca_ht * (d.taux_marge_brute + 0.01)
                 - e.pub_mois - e.fixes_mois) * 12 - base))

    # -10 % de frais fixes.
    res.append(("−10 % de frais fixes",
                (d.cm3 - e.fixes_mois * 0.90) * 12 - base))

    res.sort(key=lambda t: -t[1])
    return res


# ---------------------------------------------------------------------------
# 4. LE VERDICT
# ---------------------------------------------------------------------------

# Libelles d'affichage courts. Les cles longues restent celles de
# modele_nora.py § 7, pour que le controle de la demonstration reste tracable.
LIBELLE_COURT: Dict[str, str] = {
    "+10 % de panier moyen (AOV, à commandes constantes)":
        "+10 % de panier moyen (à commandes constantes)",
    "+10 % de taux de conversion du site (à budget pub constant)":
        "+10 % de conversion (à budget pub constant)",
    "−10 % de coût marchandise (COGS)": "−10 % de coût marchandise (COGS)",
    "+10 % de commandes de réachat": "+10 % de commandes de réachat",
    "−10 % de CAC à volume constant": "−10 % de CAC (à volume constant)",
    "−1 point de taux de retour / SAV": "−1 point de retours / SAV",
    "−10 % de frais fixes": "−10 % de frais fixes",
}


VERDICTS = {
    "non_viable": "structure non viable — ne pas scaler",
    "pari_reachat": "sous le seuil de rentabilité, pari sur le réachat",
    "rentable_limite": "rentable, marge de manœuvre limitée",
    "rentable_accelerer": "rentable, tu peux accélérer",
    "sous_investi": "tu sous-investis",
}

PRESCRIPTIONS: Dict[str, List[str]] = {
    "non_viable": [
        "Remonte le coefficient produit avant tout le reste. Sous ×5 (PVC TTC ÷ COGS), "
        "une marque qui achète son trafic ne survit pas à l'échelle : renégocie le COGS "
        "ou remonte le prix, l'un des deux. Module E01, puis E03.",
        "Ne touche pas au budget publicitaire tant que le CM3 est négatif : chaque euro "
        "de CA supplémentaire agrandit la perte. Coupe jusqu'au retour au MER seuil CM3. "
        "Module E06.",
        "Vérifie que la perte est structurelle et non mesurée : un CM3 négatif en "
        "attribution plateforme peut être positif en incrémental, et l'inverse arrive "
        "aussi. Module E09.",
    ],
    "pari_reachat": [
        "Le pari ne tient que si la cohorte tient. Suis le taux de passage 1ʳᵉ→2ᵉ commande "
        "à 90 jours par cohorte d'acquisition, jamais en moyenne globale — la moyenne "
        "baisse quand tu grandis, même si rien ne s'est dégradé. Module E08.",
        "Compte en mois de trésorerie, pas en ratio. C'est le payback qui borne ta vitesse "
        "de croissance, et le BFR qui te tue avant la non-rentabilité. Module E10.",
        "Fixe maintenant, par écrit, la date et le seuil de sortie du pari. Un MER sous le "
        "seuil EBITDA sans date de fin n'est plus un investissement. Module E13.",
    ],
    "rentable_limite": [
        "Attaque le premier levier de la table de sensibilité ci-dessus, pas celui sur "
        "lequel l'équipe passe ses journées. C'est presque toujours l'AOV : offre, "
        "bundles, taille de format. Module E03.",
        "Reprends la remise ligne par ligne. C'est le poste variable qui se dégrade le "
        "plus vite avec l'échelle et le seul que tu décides entièrement. Modules E03 et E09.",
        "N'augmente le budget que par tranches, en mesurant le CAC marginal de chaque "
        "tranche — le CAC moyen te dira toujours que tout va bien. Module E06.",
    ],
    "rentable_accelerer": [
        "Monte le budget par tranches jusqu'à ce que le CAC marginal atteigne ta LTV "
        "12 mois. Le ratio moyen va baisser : c'est le signe que tu fais le bon choix, "
        "pas le mauvais. Module E01 § 6.4, puis E06.",
        "Vérifie que le cash suit avant d'accélérer : à cette vitesse, le besoin en fonds "
        "de roulement absorbe plus que l'EBITDA mensuel. Module E10.",
        "Le goulot d'étranglement deviendra la production créative avant le budget. "
        "Dimensionne la machine à concepts maintenant. Module E05.",
    ],
    "sous_investi": [
        "Augmente le budget jusqu'à faire redescendre le ratio LTV/CAC vers 3. Au-dessus "
        "de 5, le ratio ne mesure pas une performance : il mesure un manque à gagner. "
        "Module E01 § 6.4.",
        "Ouvre un canal ou un marché supplémentaire plutôt que de saturer le canal "
        "actuel — c'est là que le CAC marginal remonte le moins vite. Modules E06 et E11.",
        "Avant d'accélérer, confirme par un test d'incrémentalité que ce que tu mesures "
        "existe. Un ratio superbe est souvent une récolte de demande déjà créée. Module E09.",
    ],
}


def verdict(d: Diagnostic) -> str:
    """Renvoie la cle du verdict. L'ordre des tests est l'ordre des priorites."""
    ratio = d.ltv_sur_cac
    ecart = d.ecart_seuil_ebitda
    payback = d.payback_mois

    # 1. Aucune marge brute : il n'y a rien a piloter, la structure est fausse.
    if d.taux_marge_brute <= 0:
        return "non_viable"
    # 2. Regle canonique (§ 3) : LTV/CAC 12 mois < 1,5, on ne scale pas, on repare.
    #    On ne la declenche que si le compte de resultat est deja dans le rouge —
    #    une marque rentable avec une cohorte faible est un autre probleme.
    if ratio < 1.5 and (d.taux_cm3 <= 0 or d.taux_ebitda < 0):
        return "non_viable"
    # 3. Chaque client vaut tres cher et l'acquisition est deja rentable : tu freines.
    if ratio > 5 and d.taux_cm3 > 0:
        return "sous_investi"
    # 4. En perte comptable, mais la cohorte rembourse : c'est un pari, pas une erreur.
    if d.taux_ebitda < 0:
        return "pari_reachat"
    # 5. Rentable. La regle canonique d'acceleration (§ 3) exige les trois a la fois :
    #    LTV/CAC >= 2,0, payback <= 4 mois, et un ecart au seuil EBITDA d'au moins
    #    15 % — sans quoi une degradation ordinaire te ramene sous la ligne.
    if ecart < 0.15 or payback > 4 or ratio < 2:
        return "rentable_limite"
    return "rentable_accelerer"


# ---------------------------------------------------------------------------
# 5. LE RAPPORT
# ---------------------------------------------------------------------------

def _mer_txt(x: float) -> str:
    return "—" if x == float("inf") else dec(x)


def _ecart_txt(x: float) -> str:
    if x == float("inf"):
        return "sans objet"
    if x == float("-inf"):
        return "inatteignable"
    return f"{x * 100:+.1f}".replace(".", ",") + " %"


def rapport(d: Diagnostic) -> str:
    e = d.e
    o: List[str] = []
    a = o.append
    v = verdict(d)

    a("═" * LARGEUR)
    a("CALCULATEUR DE SANTÉ ÉCONOMIQUE".center(LARGEUR).rstrip())
    a("cursus e-commerce — tes chiffres, pas les nôtres".center(LARGEUR).rstrip())
    a("═" * LARGEUR)

    # -- rappel des entrees -------------------------------------------------
    o += titre("0. Ce que tu as saisi")
    o += tableau(
        ["Entrée", "Valeur", "Entrée", "Valeur"],
        [
            ["AOV 1ʳᵉ commande TTC", eur(e.aov_premiere_ttc, 2), "COGS (% CA HT)", pct(e.cogs)],
            ["AOV réachat TTC", eur(e.aov_reachat_ttc, 2), "Logistique (% CA HT)", pct(e.logistique)],
            ["TVA", pct(e.tva, 0), "PSP (% CA HT)", pct(e.psp, 2)],
            ["Commandes / mois", ent(e.commandes_mois), "Retours / SAV (% CA HT)", pct(e.retours)],
            ["Part cmd. en réachat", pct(e.part_reachat), "Remises (% CA HT)", pct(e.remises)],
            ["Publicité / mois", eur(e.pub_mois), "Frais fixes / mois", eur(e.fixes_mois)],
            ["Passage 1ʳᵉ→2ᵉ à 90 j", pct(e.passage_90j), "Réachats / client à 12 m", dec(e.reachats_12m)],
        ],
        ["g", "d", "g", "d"],
    )
    a("")
    for l in _envelopper(
            f"CA TTC : {eur(d.ca_ttc)} / mois, soit {eur(d.ca_semaine_ttc)} / semaine "
            f"et {eur(d.ca_ttc * 12)} / an. AOV mixte : {eur(d.aov_mixte_ttc, 2)} TTC. "
            f"Part du CA en réachat : {pct(d.part_ca_reachat)}.", LARGEUR - 2):
        a("  " + l)

    # -- 1. cascade ---------------------------------------------------------
    o += titre("1. La cascade de marge — mensuel")
    lignes = [
        ["  CA TTC", eur(d.ca_ttc), pct(d.ca_ttc / d.ca_ht)],
        [f"− TVA ({pct(e.tva, 0)})", eur(d.tva_collectee), pct(d.tva_collectee / d.ca_ht)],
        ["= CA HT", eur(d.ca_ht), pct(1.0)],
        [f"− COGS ({pct(e.cogs)})", eur(d.ca_ht * e.cogs), pct(e.cogs)],
        ["= CM1 — marge marchandise", eur(d.cm1), pct(d.taux_cm1)],
        [f"− Logistique ({pct(e.logistique)})", eur(d.ca_ht * e.logistique), pct(e.logistique)],
        [f"− PSP ({pct(e.psp, 2)})", eur(d.ca_ht * e.psp), pct(e.psp, 2)],
        [f"− Retours / SAV ({pct(e.retours)})", eur(d.ca_ht * e.retours), pct(e.retours)],
        [f"− Remises ({pct(e.remises)})", eur(d.ca_ht * e.remises), pct(e.remises)],
        ["= CM2 — marge brute", eur(d.cm2), pct(d.taux_marge_brute)],
        ["− Publicité", eur(e.pub_mois), pct(d.pub_pct_ht)],
        ["= CM3 — marge de contribution", eur(d.cm3), pct(d.taux_cm3)],
        ["− Frais fixes", eur(e.fixes_mois), pct(d.taux_fixes)],
        ["= EBITDA", eur(d.ebitda), pct(d.taux_ebitda)],
    ]
    o += tableau(["Poste", "Montant", "% CA HT"], lignes, ["g", "d", "d"])
    a("")
    for l in _envelopper(f"EBITDA annualisé : {eur(d.ebitda_annuel)} — soit douze fois "
                         f"le mois ci-dessus, sans saisonnalité.", LARGEUR - 2):
        a("  " + l)

    # -- 2. MER -------------------------------------------------------------
    o += titre("2. Les seuils de MER")
    o += tableau(
        ["Indicateur", "Valeur", "Lecture"],
        [
            ["MER réel (CA TTC ÷ pub)", _mer_txt(d.mer),
             f"la pub coûte {pct(d.pub_pct_ht)} du CA HT"],
            ["MER seuil CM3 = 0", _mer_txt(d.mer_seuil_cm3),
             f"(1 + {pct(e.tva, 0)}) ÷ {pct(d.taux_marge_brute)}"],
            ["MER seuil EBITDA = 0", _mer_txt(d.mer_seuil_ebitda),
             "frais fixes inclus"],
            ["Écart au seuil CM3", _ecart_txt(d.ecart_seuil_cm3), "marge avant perte à l'unité"],
            ["Écart au seuil EBITDA", _ecart_txt(d.ecart_seuil_ebitda), "marge avant perte comptable"],
        ],
        ["g", "d", "g"],
    )
    a("")
    if d.mer != float("inf"):
        piege = (f"Le MER se calcule sur le CA TTC, la marge sur le CA HT. Un MER de "
                 f"{dec(d.mer)} ne veut pas dire que la publicité coûte "
                 f"{pct(1 / d.mer)} du chiffre d'affaires : elle coûte "
                 f"{dec(1 + e.tva)} ÷ {dec(d.mer)} = {pct(d.pub_pct_ht)} du CA HT. "
                 f"C'est l'écart que la plupart des marques ne font jamais.")
        for l in _envelopper(piege, LARGEUR - 2):
            a("  " + l)

    # -- 3. acquisition -----------------------------------------------------
    o += titre("3. L'acquisition — ce que coûte un client")
    o += tableau(
        ["Indicateur", "Valeur", "Lecture"],
        [
            ["Nouveaux clients / mois", ent(d.commandes_premieres),
             "1 première commande = 1 client"],
            ["nCAC", eur(d.ncac, 2) if d.ncac != float("inf") else "—",
             "toute la pub ÷ premières commandes"],
            ["Contribution 1ʳᵉ commande", eur(d.contribution_premiere, 2),
             f"{eur(e.aov_premiere_ttc / (1 + e.tva), 2)} HT × {pct(d.taux_marge_brute)}"],
            ["Marge à la 1ʳᵉ commande", eur(d.marge_premiere_commande, 2),
             "positif = payé dès la 1ʳᵉ commande"],
            ["Contribution d'un réachat", eur(d.contribution_reachat, 2),
             f"{eur(e.aov_reachat_ttc / (1 + e.tva), 2)} HT × {pct(d.taux_marge_brute)}"],
        ],
        ["g", "d", "g"],
    )
    a("")
    if d.marge_premiere_commande >= 0:
        for l in _envelopper("Chaque client est payé dès sa première commande. Tout le "
                             "réachat est du profit net d'acquisition.", LARGEUR - 2):
            a("  " + l)
    else:
        r = d.reachats_pour_rembourser
        sur = ent(round(1 / r)) if 0 < r <= 1 else "—"
        for l in _envelopper(
                f"Le client est financé par le réachat : il faut {dec(r, 3)} réachat "
                f"par client acquis pour rembourser les "
                f"{eur(-d.marge_premiere_commande, 2)} de déficit initial, soit "
                f"1 client sur {sur} qui repasse une seule commande.", LARGEUR - 2):
            a("  " + l)

    # -- 4. LTV -------------------------------------------------------------
    o += titre("4. La cohorte et la LTV en contribution")
    lignes = []
    for m in (1, 3, 6, 12):
        ratio_m = d.ltv(m) / d.ncac if d.ncac not in (0, float("inf")) else float("inf")
        source = "mesuré" if m in (3, 12) else "interpolé"
        lignes.append([f"{m} mois", dec(d.courbe[m], 2), eur(d.ltv(m), 2),
                       dec(ratio_m) if ratio_m != float("inf") else "—", source])
    o += tableau(["Horizon", "Réachats/client", "LTV (contribution)", "LTV/CAC", "Origine"],
                 lignes, ["g", "d", "d", "d", "g"])
    a("")
    a(f"  LTV 12 mois : {eur(d.ltv_12m, 2)} — soit {eur(d.contribution_premiere, 2)} "
      f"+ {dec(e.reachats_12m)} × {eur(d.contribution_reachat, 2)}.")
    a(f"  LTV / CAC à 12 mois : {dec(d.ltv_sur_cac) if d.ltv_sur_cac != float('inf') else '—'}"
      f"   |   Payback : "
      f"{dec(d.payback_mois, 1) + ' mois' if d.payback_mois != float('inf') else 'jamais atteint'}.")
    for l in _envelopper(
            "Hypothèse de modélisation : les jalons 1 et 6 mois sont interpolés avec "
            "la forme de la courbe canonique de NØRA (§ 3). Tes deux mesures, elles, "
            "sont respectées telles quelles.", LARGEUR - 2):
        a("  " + l)

    # -- 5. verdict ---------------------------------------------------------
    o += titre("5. Verdict")
    a("")
    a(f"      ▸ {VERDICTS[v].upper()}")
    a("")
    for l in _justification(d, v):
        a(("  " + l).rstrip())

    # -- 6. sensibilite -----------------------------------------------------
    o += titre("6. Quel levier vaut le plus ? — effet sur l'EBITDA annuel")
    base = d.ebitda_annuel
    lignes = []
    for nom, gain in sensibilite(d):
        part = pct(gain / abs(base)) if abs(base) > 1e-9 else "—"
        lignes.append([LIBELLE_COURT.get(nom, nom), eur(gain), part])
    o += tableau(["Levier", "Gain annuel", "% EBITDA"], lignes, ["g", "d", "d"])
    a("")
    a(f"  EBITDA annuel de référence : {eur(base)}.")
    for l in _envelopper(
            "Toutes choses égales par ailleurs, un levier à la fois. Le premier de "
            "cette liste n'est presque jamais celui sur lequel l'équipe passe ses "
            "journées.", LARGEUR - 2):
        a("  " + l)

    # -- 7. prescriptions ---------------------------------------------------
    o += titre("7. Les trois choses à faire maintenant")
    for i, presc in enumerate(PRESCRIPTIONS[v], 1):
        a("")
        for j, l in enumerate(_envelopper(presc, LARGEUR - 6)):
            a(f"  {i}. {l}" if j == 0 else f"     {l}")

    # -- alertes et limites -------------------------------------------------
    alertes = _alertes(d)
    if alertes:
        o += titre("8. Points de vigilance sur tes propres chiffres")
        for al in alertes:
            for j, l in enumerate(_envelopper(al, LARGEUR - 6)):
                a(f"  · {l}" if j == 0 else f"    {l}")

    o += titre("Ce que ce calculateur ne dit pas")
    for lim in LIMITES:
        for j, l in enumerate(_envelopper(lim, LARGEUR - 6)):
            a(f"  · {l}" if j == 0 else f"    {l}")
    a("")
    a("═" * LARGEUR)
    return "\n".join(o)


LIMITES = [
    "Il ne modélise pas la trésorerie. Une marque peut être rentable sur ce rapport et "
    "en faillite technique quatre mois plus tard, parce que le stock et l'avance "
    "publicitaire immobilisent plus que l'EBITDA. Module E10.",
    "Il suppose une première commande = un nouveau client. Si tu vends en marketplace, "
    "en gros ou en retail, ce n'est plus vrai et le nCAC est faux.",
    "Il traite la publicité comme un coût attribué, pas incrémental. Si une part de tes "
    "ventes se serait faite sans pub, le nCAC réel est plus élevé. Module E09.",
    "Il annualise un mois. Sur une catégorie saisonnière, l'EBITDA annuel affiché est un "
    "ordre de grandeur, pas une prévision.",
    "Il ignore la courbure du CAC marginal : doubler le budget ne double pas les clients. "
    "La table de sensibilité surestime donc les leviers d'acquisition. Module E01 § 6.",
]


def _justification(d: Diagnostic, v: str) -> List[str]:
    """Les trois ou quatre nombres qui portent le verdict."""
    ratio = d.ltv_sur_cac
    l = [
        f"CM3 : {pct(d.taux_cm3)} du CA HT   |   EBITDA : {pct(d.taux_ebitda)} du CA HT",
        f"MER {_mer_txt(d.mer)} contre un seuil EBITDA de {_mer_txt(d.mer_seuil_ebitda)} "
        f"({_ecart_txt(d.ecart_seuil_ebitda)})",
        f"LTV/CAC 12 mois : {dec(ratio) if ratio != float('inf') else '—'}   |   "
        f"Payback : {dec(d.payback_mois, 1) + ' mois' if d.payback_mois != float('inf') else 'jamais'}",
    ]
    cause = ("la publicité ne couvre même pas la marge qu'elle produit"
             if d.taux_cm3 <= 0 else
             "la publicité couvre sa propre marge, mais pas les frais fixes")
    commentaire = {
        "non_viable": f"Le client ne se rembourse pas sur douze mois — LTV/CAC sous 1,5 — "
                      f"et {cause}. Ajouter du budget accélère la perte : on répare "
                      f"la structure d'abord, on scale ensuite.",
        "pari_reachat": "Tu perds de l'argent volontairement pour constituer une base de "
                        "clients. C'est un pari légitime — il devient une erreur le jour "
                        "où la courbe de réachat se dégrade sans que tu l'aies vue.",
        "rentable_limite": "Tu es au-dessus de la ligne de flottaison, mais le coussin est "
                           "mince. Une dégradation de quelques points de marge ou de CAC "
                           "te ramène sous le seuil.",
        "rentable_accelerer": "Les trois conditions sont réunies : contribution positive, "
                              "marge au-dessus du seuil EBITDA, récupération du CAC rapide. "
                              "La limite est désormais le cash et la production créative.",
        "sous_investi": "Ton ratio n'est pas une performance, c'est un manque à gagner : "
                        "à ce niveau, des clients rentables ne sont pas achetés.",
    }[v]
    return l + [""] + _envelopper(commentaire, LARGEUR - 4)


def _alertes(d: Diagnostic) -> List[str]:
    """Incoherences internes detectables sur les chiffres saisis."""
    e = d.e
    out: List[str] = []
    if d.taux_marge_brute < 0.45:
        out.append(f"Marge brute à {pct(d.taux_marge_brute)} du CA HT. Sous 45 %, une marque "
                   f"qui achète son trafic n'a mathématiquement pas de place pour la "
                   f"publicité : le MER seuil CM3 monte à {_mer_txt(d.mer_seuil_cm3)}.")
    if e.remises > 0.12:
        out.append(f"Les remises pèsent {pct(e.remises)} du CA HT. Au-delà de 12 %, tu ne "
                   f"vends plus ton produit, tu vends ton prix — et tes cohortes vont le dire.")
    if e.logistique > 0.18:
        out.append(f"La logistique pèse {pct(e.logistique)} du CA HT. C'est le symptôme "
                   f"habituel d'un panier trop bas, pas d'un transporteur trop cher.")
    if e.reachats_12m > 0 and e.passage_90j > 0:
        mult = e.reachats_12m / e.passage_90j
        if mult > 5:
            out.append(f"Ta courbe de réachat implique un multiplicateur de maturation de "
                       f"{dec(mult, 1)} entre 90 jours et 12 mois (référence NØRA : 3,6). "
                       f"Soit ta catégorie a un cycle très long, soit la projection à 12 mois "
                       f"est optimiste.")
        if mult < 1:
            out.append("Tes réachats à 12 mois sont inférieurs à ton taux de passage à "
                       "90 jours : l'une des deux mesures est fausse.")
    if e.part_reachat > 0 and d.commandes_premieres > 0:
        implicite = d.commandes_reachat / d.commandes_premieres
        if e.reachats_12m > 0 and implicite > e.reachats_12m * 1.5:
            out.append(f"Tes commandes de réachat représentent {dec(implicite, 2)} réachat par "
                       f"première commande du mois, alors que ta cohorte n'en produit que "
                       f"{dec(e.reachats_12m)} en douze mois. Cohérent seulement si ton "
                       f"acquisition décroît. Module E08 § 1.")
    if d.taux_fixes > 0.20:
        out.append(f"Les frais fixes pèsent {pct(d.taux_fixes)} du CA HT. Au-delà de 20 %, "
                   f"c'est la structure qui empêche la rentabilité, pas l'acquisition.")
    return out


def _envelopper(texte: str, largeur: int) -> List[str]:
    mots = texte.split()
    lignes: List[str] = []
    courante = ""
    for m in mots:
        if not courante:
            courante = m
        elif len(courante) + 1 + len(m) <= largeur:
            courante += " " + m
        else:
            lignes.append(courante)
            courante = m
    if courante:
        lignes.append(courante)
    return lignes or [""]


# ---------------------------------------------------------------------------
# 6. MODE INTERACTIF
# ---------------------------------------------------------------------------

QUESTIONS: List[Tuple[str, str, str, float]] = [
    # (attribut, question, unite affichee, defaut brut tel que saisi)
    ("aov_premiere_ttc", "Panier moyen d'une PREMIÈRE commande", "€ TTC", 55.0),
    ("aov_reachat_ttc", "Panier moyen d'une commande de RÉACHAT", "€ TTC", 72.0),
    ("tva", "Taux de TVA moyen pondéré", "%", 20.0),
    ("cogs", "Coût marchandise (COGS)", "% du CA HT", 18.0),
    ("logistique", "Logistique : transport, pick & pack, emballage", "% du CA HT", 14.0),
    ("psp", "Commissions d'encaissement (PSP)", "% du CA HT", 1.7),
    ("retours", "Retours et SAV", "% du CA HT", 2.5),
    ("remises", "Remises : codes promo, soldes, ventes privées", "% du CA HT", 5.0),
    ("pub_mois", "Dépense publicitaire mensuelle, tous canaux", "€", 104636.0),
    ("commandes_mois", "Nombre total de commandes par mois", "commandes", 4000.0),
    ("part_reachat", "Part des commandes passées par un client déjà acquis", "%", 15.0),
    ("fixes_mois", "Frais fixes mensuels, hors publicité", "€", 28000.0),
    ("passage_90j", "Taux de passage 1ʳᵉ→2ᵉ commande à 90 jours", "%", 30.0),
    ("reachats_12m", "Nombre moyen de réachats par client acquis à 12 mois", "réachats", 1.10),
]

EN_POURCENT = {"tva", "cogs", "logistique", "psp", "retours", "remises",
               "part_reachat", "passage_90j"}


def lire_interactif() -> Entrees:
    print()
    print("═" * LARGEUR)
    print("CALCULATEUR DE SANTÉ ÉCONOMIQUE — saisie".center(LARGEUR).rstrip())
    print("═" * LARGEUR)
    print()
    print("Quatorze questions. Entrée vide = la valeur par défaut entre crochets.")
    print("Les nombres s'écrivent à la française : 14,5 — ou à l'anglaise : 14.5.")
    print("Ctrl-C pour abandonner.")
    print()

    brut: Dict[str, float] = {}
    for i, (attr, question, unite, defaut) in enumerate(QUESTIONS, 1):
        gabarit = dec(defaut, 2) if defaut % 1 else ent(defaut)
        while True:
            try:
                rep = input(f"  {i:>2}/14  {question}\n         [{gabarit} {unite}] > ").strip()
            except EOFError:
                print()
                raise SystemExit("Saisie interrompue. Relance avec --defauts ou --demo.")
            if not rep:
                brut[attr] = defaut
                break
            try:
                brut[attr] = nombre(rep)
                break
            except ValueError as exc:
                print(f"         {exc} — réessaie.")
        print()

    return _construire(brut)


def _construire(brut: Dict[str, float]) -> Entrees:
    """Convertit les saisies (pourcentages en points) en Entrees (proportions)."""
    champs = {}
    for attr, *_ in QUESTIONS:
        val = brut[attr]
        champs[attr] = val / 100.0 if attr in EN_POURCENT else val
    return Entrees(**champs)


# ---------------------------------------------------------------------------
# 7. LIGNE DE COMMANDE
# ---------------------------------------------------------------------------

def construire_parseur() -> argparse.ArgumentParser:
    d = entrees_defaut()
    p = argparse.ArgumentParser(
        prog="calculateur.py",
        description="Calculateur de santé économique d'une marque DTC. "
                    "Lancé sans aucun argument, il pose les questions une à une.",
        epilog="Les pourcentages se saisissent en points : --cogs 14,5 vaut 14,5 % du CA HT. "
               "La virgule décimale est acceptée partout.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--aov-premiere", type=nombre, default=d.aov_premiere_ttc,
                   metavar="€TTC", help="panier moyen d'une première commande, TTC")
    p.add_argument("--aov-reachat", type=nombre, default=d.aov_reachat_ttc,
                   metavar="€TTC", help="panier moyen d'une commande de réachat, TTC")
    p.add_argument("--tva", type=nombre, default=d.tva * 100, metavar="%",
                   help="taux de TVA moyen pondéré")
    p.add_argument("--cogs", type=nombre, default=d.cogs * 100, metavar="%",
                   help="coût marchandise, en %% du CA HT")
    p.add_argument("--logistique", type=nombre, default=d.logistique * 100, metavar="%",
                   help="logistique, en %% du CA HT")
    p.add_argument("--psp", type=nombre, default=d.psp * 100, metavar="%",
                   help="commissions d'encaissement, en %% du CA HT")
    p.add_argument("--retours", type=nombre, default=d.retours * 100, metavar="%",
                   help="retours et SAV, en %% du CA HT")
    p.add_argument("--remises", type=nombre, default=d.remises * 100, metavar="%",
                   help="remises et codes promo, en %% du CA HT")
    p.add_argument("--pub", type=nombre, default=d.pub_mois, metavar="€",
                   help="dépense publicitaire mensuelle, tous canaux")
    p.add_argument("--commandes", type=nombre, default=d.commandes_mois, metavar="N",
                   help="nombre total de commandes par mois")
    p.add_argument("--part-reachat", type=nombre, default=d.part_reachat * 100, metavar="%",
                   help="part des commandes passées par un client déjà acquis")
    p.add_argument("--fixes", type=nombre, default=d.fixes_mois, metavar="€",
                   help="frais fixes mensuels, hors publicité")
    p.add_argument("--passage-90j", type=nombre, default=d.passage_90j * 100, metavar="%",
                   help="taux de passage 1re→2e commande à 90 jours")
    p.add_argument("--reachats-12m", type=nombre, default=d.reachats_12m, metavar="N",
                   help="nombre moyen de réachats par client acquis à 12 mois")
    p.add_argument("--demo", action="store_true",
                   help="tourne sur le palier P5 de NØRA et vérifie les chiffres canoniques")
    p.add_argument("--defauts", action="store_true",
                   help="utilise les valeurs par défaut sans poser de question")
    return p


def entrees_depuis_args(ns: argparse.Namespace) -> Entrees:
    return _construire({
        "aov_premiere_ttc": ns.aov_premiere,
        "aov_reachat_ttc": ns.aov_reachat,
        "tva": ns.tva,
        "cogs": ns.cogs,
        "logistique": ns.logistique,
        "psp": ns.psp,
        "retours": ns.retours,
        "remises": ns.remises,
        "pub_mois": ns.pub,
        "commandes_mois": ns.commandes,
        "part_reachat": ns.part_reachat,
        "fixes_mois": ns.fixes,
        "passage_90j": ns.passage_90j,
        "reachats_12m": ns.reachats_12m,
    })


# ---------------------------------------------------------------------------
# 8. VERIFICATION DE LA DEMONSTRATION
# ---------------------------------------------------------------------------

# Valeurs attendues, lues dans ecommerce/donnees/chiffres-canoniques.md.
CANONIQUES: List[Tuple[str, str, str]] = [
    ("Marge brute (CM2)", "61,5 %", "§ 2.1"),
    ("MER seuil CM3 = 0", "1,95", "§ 2.3"),
    ("EBITDA en % du CA HT", "10,1 %", "§ 2.2"),
    ("CA TTC mensuel", "4 333 196 €", "§ 2"),
    ("CA TTC hebdomadaire", "999 968 €", "§ 2"),
    ("Dépense publicitaire", "1 494 206 €", "§ 2.2"),
    ("CM3 mensuel", "724 752 €", "§ 2.2"),
    ("EBITDA mensuel", "364 752 €", "§ 2.2"),
    ("MER seuil EBITDA = 0", "2,33", "§ 2.3"),
    ("Écart au seuil EBITDA", "+24,4 %", "§ 2.3"),
    ("nCAC", "40,03 €", "§ 2.4"),
    ("Contribution 1ʳᵉ commande", "32,77 €", "§ 2.4"),
    ("Marge à la 1ʳᵉ commande", "−7,26 €", "§ 2.4"),
    ("Contribution d'un réachat", "43,53 €", "§ 3"),
    ("LTV 12 mois (contribution)", "86,75 €", "§ 3"),
    ("LTV / CAC 12 mois", "2,17", "§ 3"),
    ("Payback", "1,8 mois", "§ 3"),
    ("EBITDA annuel", "4 377 023 €", "§ 7"),
]


def valeurs_demo(d: Diagnostic) -> Dict[str, str]:
    return {
        "Marge brute (CM2)": pct(d.taux_marge_brute),
        "MER seuil CM3 = 0": dec(d.mer_seuil_cm3),
        "EBITDA en % du CA HT": pct(d.taux_ebitda),
        "CA TTC mensuel": eur(d.ca_ttc),
        "CA TTC hebdomadaire": eur(d.ca_semaine_ttc),
        "Dépense publicitaire": eur(d.e.pub_mois),
        "CM3 mensuel": eur(d.cm3),
        "EBITDA mensuel": eur(d.ebitda),
        "MER seuil EBITDA = 0": dec(d.mer_seuil_ebitda),
        "Écart au seuil EBITDA": _ecart_txt(d.ecart_seuil_ebitda),
        "nCAC": eur(d.ncac, 2),
        "Contribution 1ʳᵉ commande": eur(d.contribution_premiere, 2),
        "Marge à la 1ʳᵉ commande": eur(d.marge_premiere_commande, 2),
        "Contribution d'un réachat": eur(d.contribution_reachat, 2),
        "LTV 12 mois (contribution)": eur(d.ltv_12m, 2),
        "LTV / CAC 12 mois": dec(d.ltv_sur_cac),
        "Payback": dec(d.payback_mois, 1) + " mois",
        "EBITDA annuel": eur(d.ebitda_annuel),
    }


SENSIBILITE_CANONIQUE: Dict[str, str] = {
    "+10 % de panier moyen (AOV, à commandes constantes)": "3 139 401 €",
    "+10 % de taux de conversion du site (à budget pub constant)": "2 662 749 €",
    "−10 % de CAC à volume constant": "1 793 047 €",
    "+10 % de commandes de réachat": "1 194 871 €",
    "−10 % de coût marchandise (COGS)": "628 313 €",
    "−1 point de taux de retour / SAV": "433 320 €",
    "−10 % de frais fixes": "432 000 €",
}


def verifier_demo(d: Diagnostic) -> bool:
    obtenues = valeurs_demo(d)
    couples: List[Tuple[str, str, str]] = []
    for nom, attendu, ref in CANONIQUES:
        couples.append((f"{nom} ({ref})", attendu, obtenues[nom]))
    for nom, gain in sensibilite(d):
        couples.append((f"{LIBELLE_COURT.get(nom, nom)} (§ 7)",
                        SENSIBILITE_CANONIQUE[nom], eur(gain)))

    ok = True
    lignes = []
    for libelle, attendu, obtenu in couples:
        conforme = obtenu == attendu
        ok = ok and conforme
        lignes.append([libelle[:42], attendu, obtenu, "ok" if conforme else "ÉCART"])

    out = []
    out += titre("Contrôle : les chiffres canoniques sont-ils retrouvés ?")
    out += tableau(["Grandeur (renvoi au canonique)", "Canonique", "Calculé", ""],
                   lignes, ["g", "d", "d", "g"])
    out.append("")
    out.append("  Source : ecommerce/donnees/chiffres-canoniques.md — modele_nora.py.")
    out.append("  " + ("Tous les contrôles passent." if ok
                       else "AU MOINS UN ÉCART : le calculateur contredit le canonique."))
    out.append("")
    out.append("═" * LARGEUR)
    print("\n".join(out))
    return ok


# ---------------------------------------------------------------------------
# 9. POINT D'ENTREE
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    parseur = construire_parseur()

    if not argv:
        if sys.stdin is not None and sys.stdin.isatty():
            try:
                e = lire_interactif()
            except KeyboardInterrupt:
                print("\nAbandon.")
                return 130
        else:
            print("Aucun argument et pas de terminal interactif : "
                  "utilisation des valeurs par défaut.\n"
                  "Pour tes propres chiffres : --demo, --defauts, ou -h "
                  "pour la liste des options.\n")
            e = entrees_defaut()
        d = Diagnostic(e)
        alertes = e.valider()
        if alertes:
            for al in alertes:
                print("Erreur de saisie : " + al, file=sys.stderr)
            return 2
        print(rapport(d))
        return 0

    ns = parseur.parse_args(argv)

    if ns.demo:
        e = entrees_demo()
        d = Diagnostic(e)
        print(rapport(d))
        return 0 if verifier_demo(d) else 1

    e = entrees_defaut() if ns.defauts else entrees_depuis_args(ns)
    alertes = e.valider()
    if alertes:
        for al in alertes:
            print("Erreur de saisie : " + al, file=sys.stderr)
        return 2
    print(rapport(Diagnostic(e)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
