#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modele economique canonique du cursus e-commerce.

Marque fil rouge : NORA (soin capillaire premium, DTC, Europe).
Marque FICTIVE. Les chiffres sont un modele calibre sur des ordres de grandeur
publics et sectoriels ; ils ne sont les comptes reels d'aucune entreprise.

Ce fichier est la SOURCE DE VERITE du cursus. Tout chiffre cite dans un module,
une etude de cas ou un exercice doit sortir d'ici ou etre explicitement marque
comme externe.

Usage :
    python3 ecommerce/outils/modele_nora.py            # affiche le rapport
    python3 ecommerce/outils/modele_nora.py --ecrire   # ecrit donnees/chiffres-canoniques.md

Aucune dependance externe. Python 3.9+.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from typing import List, Dict

TVA = 0.20  # taux moyen pondere Europe de l'Ouest, simplifie a 20 %


def ht(ttc: float) -> float:
    """Convertit un montant TTC en HT."""
    return ttc / (1 + TVA)


def eur(x: float, d: int = 0) -> str:
    """Formate un montant en euros, espace fine insecable comme separateur."""
    s = f"{x:,.{d}f}".replace(",", " ").replace(".", ",").replace("-", "−")
    return s + " €"


def pct(x: float, d: int = 1) -> str:
    return f"{x * 100:.{d}f}".replace(".", ",") + " %"


# ---------------------------------------------------------------------------
# 1. LA GAMME
# ---------------------------------------------------------------------------

@dataclass
class Produit:
    nom: str
    pvc_ttc: float          # prix de vente conseille TTC
    cogs: float             # cout de revient marchandise rendu entrepot
    unites: int = 1         # nombre d'unites physiques (pour le pick & pack)

    @property
    def pvc_ht(self) -> float:
        return ht(self.pvc_ttc)

    @property
    def marge_marchandise(self) -> float:
        return self.pvc_ht - self.cogs

    @property
    def taux_marge_marchandise(self) -> float:
        return self.marge_marchandise / self.pvc_ht

    @property
    def coefficient(self) -> float:
        """Coefficient multiplicateur : PVC TTC / COGS. Le reflexe metier."""
        return self.pvc_ttc / self.cogs


GAMME: List[Produit] = [
    Produit("Sérum Densité 50 ml (héros)", 39.00, 4.80, 1),
    Produit("Shampooing Fortifiant 250 ml", 24.00, 3.10, 1),
    Produit("Masque Réparateur 200 ml", 29.00, 3.60, 1),
    Produit("Rituel Complet (les 3)", 74.00, 11.50, 3),
    Produit("Cure 3 mois (3 serums)", 99.00, 14.40, 3),
]


# ---------------------------------------------------------------------------
# 2. LES PALIERS
# ---------------------------------------------------------------------------

@dataclass
class Palier:
    code: str
    nom: str
    mois: str
    commandes_mois: int
    part_commandes_repeat: float   # part des commandes passees par un client deja acquis
    aov_new_ttc: float             # panier moyen d'une premiere commande
    aov_repeat_ttc: float          # panier moyen d'une commande de reachat
    mer: float                     # CA TTC / depense publicitaire
    # structure de cout variable, en % du CA HT
    cogs_pct: float
    logistique_pct: float
    psp_pct: float
    retours_sav_pct: float
    remises_pct: float
    # structure fixe
    fixes_mois: float
    etp: float
    marches: str

    # -- volumes -----------------------------------------------------------
    @property
    def commandes_repeat(self) -> float:
        return self.commandes_mois * self.part_commandes_repeat

    @property
    def commandes_new(self) -> float:
        return self.commandes_mois - self.commandes_repeat

    @property
    def ca_new_ttc(self) -> float:
        return self.commandes_new * self.aov_new_ttc

    @property
    def ca_repeat_ttc(self) -> float:
        return self.commandes_repeat * self.aov_repeat_ttc

    @property
    def ca_ttc(self) -> float:
        return self.ca_new_ttc + self.ca_repeat_ttc

    @property
    def ca_ht(self) -> float:
        return ht(self.ca_ttc)

    @property
    def ca_semaine_ttc(self) -> float:
        return self.ca_ttc * 12 / 52

    @property
    def aov_blended_ttc(self) -> float:
        return self.ca_ttc / self.commandes_mois

    @property
    def part_ca_repeat(self) -> float:
        return self.ca_repeat_ttc / self.ca_ttc

    # -- marge -------------------------------------------------------------
    @property
    def taux_variable(self) -> float:
        return (self.cogs_pct + self.logistique_pct + self.psp_pct
                + self.retours_sav_pct + self.remises_pct)

    @property
    def taux_marge_brute(self) -> float:
        """Marge brute apres TOUS les couts variables, en % du CA HT. = CM2."""
        return 1 - self.taux_variable

    @property
    def marge_brute(self) -> float:
        return self.ca_ht * self.taux_marge_brute

    # -- publicite ---------------------------------------------------------
    @property
    def depense_pub(self) -> float:
        return self.ca_ttc / self.mer

    @property
    def pub_pct_ht(self) -> float:
        """Piege classique : le MER est calcule sur le TTC, la marge sur le HT."""
        return self.depense_pub / self.ca_ht

    @property
    def taux_cm3(self) -> float:
        return self.taux_marge_brute - self.pub_pct_ht

    @property
    def cm3(self) -> float:
        return self.marge_brute - self.depense_pub

    # -- acquisition -------------------------------------------------------
    @property
    def ncac(self) -> float:
        """CAC nouveau client : toute la depense pub / nouveaux clients."""
        return self.depense_pub / self.commandes_new

    @property
    def contribution_1ere_commande(self) -> float:
        return ht(self.aov_new_ttc) * self.taux_marge_brute

    @property
    def contribution_commande_repeat(self) -> float:
        return ht(self.aov_repeat_ttc) * self.taux_marge_brute

    @property
    def marge_1ere_commande(self) -> float:
        """Positif = paye a la premiere commande. Negatif = finance par le reachat."""
        return self.contribution_1ere_commande - self.ncac

    @property
    def mer_seuil(self) -> float:
        """MER minimum pour un CM3 nul (equilibre avant frais fixes)."""
        return (1 + TVA) / self.taux_marge_brute

    @property
    def mer_objectif(self) -> float:
        """MER necessaire pour couvrir variables + fixes (equilibre EBITDA)."""
        marge_dispo = self.taux_marge_brute - self.fixes_mois / self.ca_ht
        return (1 + TVA) / marge_dispo if marge_dispo > 0 else float("inf")

    # -- resultat ----------------------------------------------------------
    @property
    def taux_fixes(self) -> float:
        return self.fixes_mois / self.ca_ht

    @property
    def ebitda(self) -> float:
        return self.cm3 - self.fixes_mois

    @property
    def taux_ebitda(self) -> float:
        return self.ebitda / self.ca_ht

    @property
    def ca_par_etp(self) -> float:
        return self.ca_ht * 12 / self.etp


PALIERS: List[Palier] = [
    Palier(
        code="P1", nom="Validation", mois="M1 – M3",
        commandes_mois=800, part_commandes_repeat=0.04,
        aov_new_ttc=45.50, aov_repeat_ttc=58.00, mer=1.80,
        cogs_pct=0.200, logistique_pct=0.160, psp_pct=0.018,
        retours_sav_pct=0.020, remises_pct=0.030,
        fixes_mois=6_500, etp=1.5, marches="France",
    ),
    Palier(
        code="P2", nom="Traction", mois="M4 – M9",
        commandes_mois=4_000, part_commandes_repeat=0.15,
        aov_new_ttc=55.00, aov_repeat_ttc=72.00, mer=2.20,
        cogs_pct=0.180, logistique_pct=0.140, psp_pct=0.017,
        retours_sav_pct=0.025, remises_pct=0.050,
        fixes_mois=28_000, etp=4, marches="France",
    ),
    Palier(
        code="P3", nom="Scale France", mois="M10 – M18",
        commandes_mois=18_000, part_commandes_repeat=0.27,
        aov_new_ttc=60.00, aov_repeat_ttc=80.00, mer=2.70,
        cogs_pct=0.160, logistique_pct=0.120, psp_pct=0.0165,
        retours_sav_pct=0.030, remises_pct=0.070,
        fixes_mois=105_000, etp=12, marches="France + Belgique",
    ),
    Palier(
        code="P4", nom="Multi-pays", mois="M19 – M30",
        commandes_mois=42_000, part_commandes_repeat=0.34,
        aov_new_ttc=63.00, aov_repeat_ttc=83.00, mer=2.80,
        cogs_pct=0.150, logistique_pct=0.115, psp_pct=0.016,
        retours_sav_pct=0.035, remises_pct=0.080,
        fixes_mois=230_000, etp=25, marches="FR, BE, DE, ES, IT",
    ),
    Palier(
        code="P5", nom="1 M€ / semaine", mois="M31 – M40",
        commandes_mois=60_200, part_commandes_repeat=0.38,
        aov_new_ttc=64.00, aov_repeat_ttc=85.00, mer=2.90,
        cogs_pct=0.145, logistique_pct=0.110, psp_pct=0.0155,
        retours_sav_pct=0.035, remises_pct=0.080,
        fixes_mois=360_000, etp=38, marches="FR, BE, DE, ES, IT, NL, UK",
    ),
]

# Variante : le meme CA, mais pilote sur la marge et non sur le volume.
P5_OPTIMISE = Palier(
    code="P5+", nom="1 M€ / semaine — pilote marge",
    mois="M41 +",
    commandes_mois=56_130, part_commandes_repeat=0.46,
    aov_new_ttc=68.00, aov_repeat_ttc=88.00, mer=3.40,
    cogs_pct=0.135, logistique_pct=0.105, psp_pct=0.015,
    retours_sav_pct=0.030, remises_pct=0.055,
    fixes_mois=375_000, etp=39, marches="FR, BE, DE, ES, IT, NL, UK",
)


# ---------------------------------------------------------------------------
# 3. COHORTES ET LTV
# ---------------------------------------------------------------------------

# Probabilite cumulee qu'un client acquis ait passe au moins n commandes
# supplementaires, a l'horizon donne. Calibre sur une categorie
# consommable premium (reachat naturel a 60-90 jours).
COURBE_REPEAT: Dict[int, float] = {
    #  mois depuis 1re commande : nb moyen de commandes de reachat par client acquis
    1: 0.06,
    3: 0.34,
    6: 0.72,
    12: 1.24,
    18: 1.66,
    24: 1.98,
    36: 2.42,
}


@dataclass
class Cohorte:
    palier: Palier
    courbe: Dict[int, float] = field(default_factory=lambda: dict(COURBE_REPEAT))

    def commandes_cumulees(self, mois: int) -> float:
        return 1 + self.courbe[mois]

    def ca_cumule_ttc(self, mois: int) -> float:
        return self.palier.aov_new_ttc + self.courbe[mois] * self.palier.aov_repeat_ttc

    def ltv_contribution(self, mois: int) -> float:
        """LTV en marge de contribution (la seule qui serve a decider)."""
        return (self.palier.contribution_1ere_commande
                + self.courbe[mois] * self.palier.contribution_commande_repeat)

    def ratio(self, mois: int) -> float:
        return self.ltv_contribution(mois) / self.palier.ncac

    def payback_mois(self) -> float:
        """Interpolation lineaire du mois ou la contribution cumulee = CAC."""
        cac = self.palier.ncac
        cum0 = self.palier.contribution_1ere_commande
        if cum0 >= cac:
            return 0.0
        jalons = sorted(self.courbe.keys())
        prev_m, prev_c = 0, cum0
        for m in jalons:
            c = self.ltv_contribution(m)
            if c >= cac:
                if c == prev_c:
                    return float(m)
                return prev_m + (cac - prev_c) / (c - prev_c) * (m - prev_m)
            prev_m, prev_c = m, c
        return float("inf")


# ---------------------------------------------------------------------------
# 4. BESOIN EN FONDS DE ROULEMENT
# ---------------------------------------------------------------------------

@dataclass
class Tresorerie:
    palier: Palier
    jours_stock: int          # DIO : jours de stock detenu
    delai_encaissement: int   # DSO : PSP + reserve
    delai_fournisseur: int    # DPO : credit obtenu du fabricant
    delai_pub: int            # jours entre la depense pub et l'encaissement client
    acompte_fournisseur: float = 0.30  # part payee a la commande de production

    @property
    def cogs_mensuel(self) -> float:
        return self.palier.ca_ht * self.palier.cogs_pct

    @property
    def stock_immobilise(self) -> float:
        return self.cogs_mensuel * self.jours_stock / 30

    @property
    def creances(self) -> float:
        return self.palier.ca_ttc * self.delai_encaissement / 30

    @property
    def dettes_fournisseurs(self) -> float:
        """Credit fournisseur obtenu, acompte ignore. Voir bfr_reel ci-dessous."""
        return self.cogs_mensuel * self.delai_fournisseur / 30

    @property
    def dettes_fournisseurs_reelles(self) -> float:
        """L'acompte paye comptant a la commande ne beneficie d'aucun credit."""
        return (self.cogs_mensuel * (1 - self.acompte_fournisseur)
                * self.delai_fournisseur / 30)

    @property
    def bfr_reel(self) -> float:
        """BFR acompte fournisseur inclus. C'est celui qu'il faut financer."""
        return (self.stock_immobilise + self.creances + self.avance_pub
                - self.dettes_fournisseurs_reelles)

    @property
    def avance_pub(self) -> float:
        return self.palier.depense_pub * self.delai_pub / 30

    @property
    def bfr(self) -> float:
        return (self.stock_immobilise + self.creances + self.avance_pub
                - self.dettes_fournisseurs)

    @property
    def bfr_en_jours_de_ca(self) -> float:
        return self.bfr / (self.palier.ca_ttc / 30)

    @property
    def cash_absorbe_par_croissance(self) -> float:
        """Cash immobilise pour chaque tranche de +100 k€ de CA mensuel."""
        return self.bfr / self.palier.ca_ttc * 100_000


TRESO = {
    "P1": Tresorerie(PALIERS[0], jours_stock=75, delai_encaissement=4, delai_fournisseur=0, delai_pub=2),
    "P2": Tresorerie(PALIERS[1], jours_stock=70, delai_encaissement=4, delai_fournisseur=15, delai_pub=3),
    "P3": Tresorerie(PALIERS[2], jours_stock=80, delai_encaissement=3, delai_fournisseur=30, delai_pub=7),
    "P4": Tresorerie(PALIERS[3], jours_stock=95, delai_encaissement=3, delai_fournisseur=45, delai_pub=14),
    "P5": Tresorerie(PALIERS[4], jours_stock=105, delai_encaissement=3, delai_fournisseur=60, delai_pub=21),
}


# ---------------------------------------------------------------------------
# 5. PLAN MEDIA AU PALIER 5
# ---------------------------------------------------------------------------

@dataclass
class Canal:
    nom: str
    part: float          # part de la depense totale
    ncac_canal: float    # CAC nouveau client attribue au canal (post-modelisation)
    role: str

CANAUX_P5: List[Canal] = [
    Canal("Meta (Advantage+ / ASC + prospection large)", 0.55, 38.50, "Volume, découverte, 1ᵉʳ contact"),
    Canal("TikTok (Smart+ / Spark Ads UGC)",             0.15, 44.00, "Volume jeune, nouveaux angles"),
    Canal("Google Search + Shopping (marque et générique)", 0.11, 19.00, "Récolte de la demande créée"),
    Canal("Google PMax / Demand Gen / YouTube",          0.08, 47.00, "Extension de portée"),
    Canal("Influence + affiliation (CPA et forfait)",    0.08, 41.00, "Preuve sociale, contenu source"),
    Canal("Pinterest, Snap, native, presse",             0.03, 55.00, "Incrémentalité marginale, test"),
]


# ---------------------------------------------------------------------------
# 6. LA MACHINE CREATIVE
# ---------------------------------------------------------------------------

@dataclass
class BesoinCreatif:
    palier: Palier
    budget_par_concept_test: float   # budget minimum pour juger un concept
    taux_de_reussite: float          # part des concepts qui deviennent scalables
    duree_de_vie_semaines: float     # duree de vie d'un concept gagnant
    variations_par_concept: int

    @property
    def budget_hebdo(self) -> float:
        return self.palier.depense_pub * 12 / 52

    @property
    def part_budget_test(self) -> float:
        return 0.15

    @property
    def concepts_testes_semaine(self) -> float:
        return self.budget_hebdo * self.part_budget_test / self.budget_par_concept_test

    @property
    def gagnants_semaine(self) -> float:
        return self.concepts_testes_semaine * self.taux_de_reussite

    @property
    def gagnants_en_rotation(self) -> float:
        return self.gagnants_semaine * self.duree_de_vie_semaines

    @property
    def assets_mois(self) -> float:
        return self.concepts_testes_semaine * self.variations_par_concept * 52 / 12


CREA = {
    "P2": BesoinCreatif(PALIERS[1], budget_par_concept_test=250, taux_de_reussite=0.12,
                        duree_de_vie_semaines=5, variations_par_concept=3),
    "P3": BesoinCreatif(PALIERS[2], budget_par_concept_test=400, taux_de_reussite=0.11,
                        duree_de_vie_semaines=5, variations_par_concept=4),
    "P5": BesoinCreatif(PALIERS[4], budget_par_concept_test=900, taux_de_reussite=0.09,
                        duree_de_vie_semaines=4.5, variations_par_concept=5),
}


# ---------------------------------------------------------------------------
# 7. SENSIBILITE : QUEL LEVIER VAUT LE PLUS ?
# ---------------------------------------------------------------------------

def sensibilite(p: Palier) -> List[tuple]:
    """Effet sur l'EBITDA annuel d'une amelioration de 10 % de chaque levier."""
    base = p.ebitda * 12
    res = []

    # +10 % de taux de conversion => meme depense pub, +10 % de commandes et de CA
    mer2 = p.mer * 1.10
    e = (p.ca_ht * 1.10 * p.taux_marge_brute - (p.ca_ttc * 1.10) / mer2 - p.fixes_mois) * 12
    res.append(("+10 % de taux de conversion du site (à budget pub constant)", e - base))

    # +10 % d'AOV : CA +10 % a nombre de commandes constant. La logistique est un
    # cout PAR COMMANDE : en euros elle ne bouge pas, donc son poids en % du CA baisse.
    # C'est exactement ce qui rend l'AOV superieur a la conversion.
    marge2 = p.taux_marge_brute + p.logistique_pct * (1 - 1 / 1.10)
    e = (p.ca_ht * 1.10 * marge2 - p.depense_pub - p.fixes_mois) * 12
    res.append(("+10 % de panier moyen (AOV, à commandes constantes)", e - base))

    # -10 % de COGS
    e = (p.ca_ht * (p.taux_marge_brute + p.cogs_pct * 0.10) - p.depense_pub - p.fixes_mois) * 12
    res.append(("−10 % de coût marchandise (COGS)", e - base))

    # +10 % de reachat : les commandes repeat augmentent de 10 %
    cmd_rep = p.commandes_repeat * 1.10
    ca2 = p.ca_new_ttc + cmd_rep * p.aov_repeat_ttc
    e = (ht(ca2) * p.taux_marge_brute - p.depense_pub - p.fixes_mois) * 12
    res.append(("+10 % de commandes de réachat", e - base))

    # -10 % de CAC (a volume constant) => depense pub -10 %
    e = (p.marge_brute - p.depense_pub * 0.90 - p.fixes_mois) * 12
    res.append(("−10 % de CAC à volume constant", e - base))

    # -10 % de frais fixes
    e = (p.cm3 - p.fixes_mois * 0.90) * 12
    res.append(("−10 % de frais fixes", e - base))

    # -1 pt de taux de retour/SAV
    e = (p.ca_ht * (p.taux_marge_brute + 0.01) - p.depense_pub - p.fixes_mois) * 12
    res.append(("−1 point de taux de retour / SAV", e - base))

    res.sort(key=lambda t: -t[1])
    return res


# ---------------------------------------------------------------------------
# 8. RENDU
# ---------------------------------------------------------------------------

def ligne(cells: List[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def rapport() -> str:
    o: List[str] = []
    a = o.append

    a("# Chiffres canoniques du cursus — marque fil rouge NØRA")
    a("")
    a("> **Fichier généré.** Ne le modifie pas à la main : il est produit par")
    a("> `ecommerce/outils/modele_nora.py`. Change les hypothèses dans le script,")
    a("> relance-le, et tout le cursus reste cohérent.")
    a(">")
    a("> **NØRA est une marque fictive.** Le modèle est calibré sur des ordres de")
    a("> grandeur sectoriels publics (marges, MER, courbes de réachat d'une")
    a("> catégorie consommable premium). Ce ne sont les comptes réels d'aucune")
    a("> entreprise, et aucun chiffre ici ne doit être présenté comme tel.")
    a("")
    a(f"Hypothèse fiscale : TVA moyenne pondérée **{pct(TVA, 0)}** sur tous les marchés.")
    a("Tout ce qui est « TTC » est un prix client ; tout ce qui est « HT » est du")
    a("chiffre d'affaires comptable. **Les confondre est l'erreur n° 1 du métier.**")
    a("")
    a("---")
    a("")

    # -- 1. gamme
    a("## 1. La gamme et ses marges marchandise")
    a("")
    a(ligne(["Produit", "PVC TTC", "PVC HT", "COGS", "Marge marchandise", "Taux", "Coef."]))
    a(ligne(["---", "---:", "---:", "---:", "---:", "---:", "---:"]))
    for p in GAMME:
        a(ligne([p.nom, eur(p.pvc_ttc, 2), eur(p.pvc_ht, 2), eur(p.cogs, 2),
                 eur(p.marge_marchandise, 2), pct(p.taux_marge_marchandise),
                 f"×{p.coefficient:.1f}".replace(".", ",")]))
    a("")
    a("> **Lecture.** Le coefficient (PVC TTC ÷ COGS) est le réflexe métier : sous")
    a("> **×5**, une marque DTC qui achète son trafic ne survit pas à l'échelle. NØRA")
    a("> est entre ×6,4 et ×8,1 : c'est le minimum vital, pas un luxe. Le module E01")
    a("> démontre pourquoi.")
    a("")
    a("---")
    a("")

    # -- 2. paliers
    a("## 2. Les cinq paliers — du premier euro à 1 M€/semaine")
    a("")
    a(ligne(["Palier", "Mois", "Marchés", "Cmd/mois", "AOV mixte", "CA TTC/mois", "CA TTC/sem."]))
    a(ligne(["---", "---", "---", "---:", "---:", "---:", "---:"]))
    for p in PALIERS:
        a(ligne([f"**{p.code} — {p.nom}**", p.mois, p.marches, f"{p.commandes_mois:,}".replace(",", " "),
                 eur(p.aov_blended_ttc, 2), eur(p.ca_ttc), eur(p.ca_semaine_ttc)]))
    a("")

    a("**Composition du panier.** Ces colonnes manquaient et plusieurs calculs du")
    a("cursus en dépendent (§ 2.4 et § 3 notamment). Elles sont désormais publiées :")
    a("")
    a(ligne(["Palier", "AOV 1ʳᵉ commande TTC", "AOV réachat TTC", "Part des commandes en réachat", "Part du CA en réachat"]))
    a(ligne(["---", "---:", "---:", "---:", "---:"]))
    for p in PALIERS:
        a(ligne([p.code, eur(p.aov_new_ttc, 2), eur(p.aov_repeat_ttc, 2),
                 pct(p.part_commandes_repeat), pct(p.part_ca_repeat)]))
    a("")
    a("### 2.1 Structure de coût variable (en % du CA HT)")
    a("")
    a(ligne(["Palier", "COGS", "Logistique", "PSP", "Retours/SAV", "Remises", "**Marge brute (CM2)**"]))
    a(ligne(["---", "---:", "---:", "---:", "---:", "---:", "---:"]))
    for p in PALIERS:
        a(ligne([p.code, pct(p.cogs_pct), pct(p.logistique_pct), pct(p.psp_pct, 2),
                 pct(p.retours_sav_pct), pct(p.remises_pct), f"**{pct(p.taux_marge_brute)}**"]))
    a("")
    a("**Valeurs exactes de la marge brute**, pour qui refait les calculs au centime :")
    a("")
    a(ligne(["Palier"] + [p.code for p in PALIERS]))
    a(ligne(["---"] + ["---:"] * len(PALIERS)))
    a(ligne(["Marge brute (CM2)"] + [f"{p.taux_marge_brute * 100:.2f}".replace(".", ",") + "\u202f%" for p in PALIERS]))
    a("")
    a("> **Trois conventions de modélisation, à connaître avant de citer ces chiffres.**")
    a(">")
    a("> 1. **La logistique est modélisée en % du CA HT**, pas en euros par commande.")
    a(">    C'est une simplification. La conséquence est enseignée en E01 § 7 : c'est")
    a(">    précisément ce qui rend le panier moyen supérieur à la conversion comme")
    a(">    levier. Le module E10 § 6 refait la dérivation en euros par commande.")
    a("> 2. **Le COGS de P1 (20,0\u202f%) correspond à un coefficient effectif de ×6,0**,")
    a(">    inférieur au plus bas coefficient catalogue du § 1 (×6,4). Ce n'est pas une")
    a(">    incohérence : en petite série le coût unitaire est plus élevé — MOQ faible,")
    a(">    aucune remise de volume, casse de lancement. L'écart se referme dès P3.")
    a("> 3. **La remise est traitée comme un coût variable**, pas comme une réduction")
    a(">    du chiffre d'affaires. Comptablement les deux se défendent ; en pilotage on")
    a(">    la met en coût, ligne visible, avec un responsable. Sinon elle disparaît")
    a(">    dans le prix moyen et personne ne la défend jamais.")
    a("")
    a("> Les remises montent avec l'échelle (Black Friday, codes créateurs, paniers")
    a("> abandonnés). Les retours aussi : plus le trafic est large, moins il est")
    a("> qualifié. **La marge brute ne s'améliore pas mécaniquement en grandissant.**")
    a("> Elle s'améliore parce qu'on négocie le COGS et la logistique plus vite que")
    a("> les remises et les retours ne se dégradent.")
    a("")

    a("### 2.2 Compte de résultat mensuel")
    a("")
    a(ligne(["Palier", "CA HT", "Marge brute", "Pub", "Pub % HT", "**CM3**", "Fixes", "**EBITDA**", "% CA HT"]))
    a(ligne(["---", "---:", "---:", "---:", "---:", "---:", "---:", "---:", "---:"]))
    for p in PALIERS:
        a(ligne([p.code, eur(p.ca_ht), eur(p.marge_brute), eur(p.depense_pub),
                 pct(p.pub_pct_ht), f"**{eur(p.cm3)}**", eur(p.fixes_mois),
                 f"**{eur(p.ebitda)}**", pct(p.taux_ebitda)]))
    a("")
    a("> **Le piège du MER.** Le MER se calcule sur le CA **TTC**, la marge sur le CA")
    a("> **HT**. Un MER de 2,90 ne veut pas dire « la pub coûte 34,5 % du CA » : elle")
    a("> coûte **1,20 ÷ 2,90 = 41,4 % du CA HT**. Beaucoup de marques se croient")
    a("> rentables de 7 points parce qu'elles n'ont jamais fait cette division.")
    a("")

    a("### 2.3 Seuils de MER")
    a("")
    a(ligne(["Palier", "MER réel", "MER seuil (CM3 = 0)", "MER seuil (EBITDA = 0)", "Écart au seuil EBITDA"]))
    a(ligne(["---", "---:", "---:", "---:", "---:"]))
    for p in PALIERS:
        mo = p.mer_objectif
        mo_s = f"{mo:.2f}".replace(".", ",") if mo != float("inf") else "impossible"
        secu = (p.mer / mo - 1) if mo != float("inf") else float("-inf")
        secu_s = pct(secu) if mo != float("inf") else "—"
        a(ligne([p.code, f"{p.mer:.2f}".replace(".", ","),
                 f"{p.mer_seuil:.2f}".replace(".", ","), mo_s, secu_s]))
    a("")
    a("> **C'est le tableau le plus important du cursus.** Le MER seuil est la ligne")
    a("> de flottaison : en dessous, chaque euro de CA supplémentaire te fait perdre")
    a("> de l'argent. Aux paliers P1 et P2, NØRA est **sous** son MER d'équilibre")
    a("> EBITDA : la marque perd de l'argent volontairement pour constituer une base")
    a("> de clients. C'est un pari sur le réachat, pas une erreur — mais c'en devient")
    a("> une si le réachat ne vient pas. Voir E08.")
    a("")

    a("### 2.4 Acquisition — ce que coûte un client et ce qu'il rapporte")
    a("")
    a(ligne(["Palier", "Nouveaux clients/mois", "nCAC", "Contribution 1ʳᵉ cmd", "Marge à la 1ʳᵉ cmd", "Verdict"]))
    a(ligne(["---", "---:", "---:", "---:", "---:", "---"]))
    for p in PALIERS:
        m = p.marge_1ere_commande
        verdict = "profitable dès la 1ʳᵉ" if m >= 0 else "financé par le réachat"
        a(ligne([p.code, f"{p.commandes_new:,.0f}".replace(",", " "), eur(p.ncac, 2),
                 eur(p.contribution_1ere_commande, 2), eur(m, 2), verdict]))
    a("")

    a("### 2.5 Productivité et structure")
    a("")
    a(ligne(["Palier", "ETP", "Frais fixes/mois", "% CA HT", "CA HT annuel par ETP"]))
    a(ligne(["---", "---:", "---:", "---:", "---:"]))
    for p in PALIERS:
        a(ligne([p.code, f"{p.etp:g}".replace(".", ","), eur(p.fixes_mois), pct(p.taux_fixes),
                 eur(p.ca_par_etp)]))
    a("")
    a("---")
    a("")

    # -- 3. cohortes
    a("## 3. Cohortes et LTV (palier P5)")
    a("")
    p5 = PALIERS[4]
    c5 = Cohorte(p5)
    a(f"Base : nCAC = **{eur(p5.ncac, 2)}**, contribution 1ʳᵉ commande = "
      f"**{eur(p5.contribution_1ere_commande, 2)}**, contribution par réachat = "
      f"**{eur(p5.contribution_commande_repeat, 2)}**.")
    a("")
    a(ligne(["Horizon", "Cmd. cumulées / client", "CA cumulé TTC", "LTV en contribution", "LTV / CAC"]))
    a(ligne(["---", "---:", "---:", "---:", "---:"]))
    for m in sorted(COURBE_REPEAT):
        a(ligne([f"{m} mois", f"{c5.commandes_cumulees(m):.2f}".replace(".", ","),
                 eur(c5.ca_cumule_ttc(m), 2), eur(c5.ltv_contribution(m), 2),
                 f"{c5.ratio(m):.2f}".replace(".", ",")]))
    a("")
    a(f"**Délai de récupération du CAC : ≈ {c5.payback_mois():.1f} mois**"
      .replace(".", ",") + " (interpolation linéaire sur la courbe ci-dessus).")
    a("")
    a("> **La règle de décision.** LTV/CAC à 12 mois ≥ 2,0 et payback ≤ 4 mois : on")
    a("> peut accélérer. LTV/CAC 12 mois < 1,5 : on ne scale pas, on répare. Un ratio")
    a("> > 5 ne signifie pas « excellent » mais « tu sous-investis » — voir E01 § 6.")
    a("")

    a("### 3.1 Comparaison des cohortes entre paliers")
    a("")
    a(ligne(["Palier", "nCAC", "LTV 12 m (contrib.)", "LTV/CAC 12 m", "LTV/CAC 24 m", "Payback (mois)"]))
    a(ligne(["---", "---:", "---:", "---:", "---:", "---:"]))
    for p in PALIERS:
        c = Cohorte(p)
        pb = c.payback_mois()
        pb_s = f"{pb:.1f}".replace(".", ",") if pb != float("inf") else "jamais"
        a(ligne([p.code, eur(p.ncac, 2), eur(c.ltv_contribution(12), 2),
                 f"{c.ratio(12):.2f}".replace(".", ","),
                 f"{c.ratio(24):.2f}".replace(".", ","), pb_s]))
    a("")
    a("---")
    a("")

    # -- 4. treso
    a("## 4. Trésorerie et besoin en fonds de roulement")
    a("")
    a(ligne(["Palier", "Stock", "Encaissements en attente", "Avance pub", "− Dettes fourn.", "**BFR**", "En jours de CA"]))
    a(ligne(["---", "---:", "---:", "---:", "---:", "---:", "---:"]))
    for code in ["P1", "P2", "P3", "P4", "P5"]:
        t = TRESO[code]
        a(ligne([code, eur(t.stock_immobilise), eur(t.creances), eur(t.avance_pub),
                 eur(t.dettes_fournisseurs), f"**{eur(t.bfr)}**",
                 f"{t.bfr_en_jours_de_ca:.0f} j"]))
    a("")
    a("### 4.1 Le BFR réel — acompte fournisseur inclus")
    a("")
    a("Le tableau ci-dessus suppose que **toute** la marchandise bénéficie du délai")
    a("fournisseur négocié. C'est faux : la part payée comptant à la commande de")
    a("production — ici **" + pct(TRESO["P5"].acompte_fournisseur, 0) + "** — n'obtient aucun crédit. Le vrai besoin de")
    a("financement est donc supérieur, et c'est celui-là qu'il faut avoir en banque.")
    a("")
    a(ligne(["Palier", "BFR hors acompte", "**BFR réel**", "Écart", "Écart en %"]))
    a(ligne(["---", "---:", "---:", "---:", "---:"]))
    for code in ["P1", "P2", "P3", "P4", "P5"]:
        t = TRESO[code]
        ec = t.bfr_reel - t.bfr
        a(ligne([code, eur(t.bfr), f"**{eur(t.bfr_reel)}**", eur(ec),
                 pct(ec / t.bfr) if t.bfr else "—"]))
    a("")
    a("> **Pourquoi les deux colonnes cohabitent.** Le reste du cursus cite la")
    a("> colonne de gauche, qui est celle du modèle simple. Elle est utile pour")
    a("> comparer des paliers entre eux. Mais **le chiffre à financer est celui de")
    a("> droite.** C'est une règle générale et pas une particularité de ce modèle :")
    a("> tout modèle de BFR sous-estime la réalité, parce qu'il oublie toujours une")
    a("> sortie de cash anticipée. Prends une marge de sécurité sur ce que ton")
    a("> tableur te dit. Le simulateur")
    a("> [`simulateur_tresorerie.py`](../outils/simulateur_tresorerie.py) modélise")
    a("> l'acompte et reproduit la colonne de gauche à l'euro près quand on le met")
    a("> à zéro — c'est ainsi que cet écart a été trouvé.")
    a("")
    a(ligne(["Palier", "Cash immobilisé par +100 k€ de CA mensuel", "EBITDA mensuel", "Croissance autofinançable / mois"]))
    a(ligne(["---", "---:", "---:", "---:"]))
    for code in ["P1", "P2", "P3", "P4", "P5"]:
        t = TRESO[code]
        p = t.palier
        besoin = t.cash_absorbe_par_croissance
        capacite = (p.ebitda / besoin * 100_000) if besoin > 0 else float("inf")
        cap_s = eur(capacite) + " de CA" if capacite != float("inf") else "—"
        if p.ebitda < 0:
            cap_s = "**négative — la croissance consomme du cash**"
        a(ligne([code, eur(besoin), eur(p.ebitda), cap_s]))
    a("")
    a("> **Ce tableau tue plus de marques que la publicité.** Une marque qui croît de")
    a("> 30 % par mois avec un BFR de 45 jours de CA est en faillite technique bien")
    a("> avant d'être non rentable. Module E10.")
    a("")
    a("---")
    a("")

    # -- 5. media
    a("## 5. Plan média au palier P5")
    a("")
    a(f"Dépense publicitaire totale : **{eur(p5.depense_pub)} / mois** "
      f"(**{eur(p5.depense_pub * 12 / 52)} / semaine**, "
      f"**{eur(p5.depense_pub / 30.4)} / jour**).")
    a("")
    a(ligne(["Canal", "Part", "Budget/mois", "nCAC canal", "Nouveaux clients/mois", "Rôle"]))
    a(ligne(["---", "---:", "---:", "---:", "---:", "---"]))
    total_clients = 0.0
    for c in CANAUX_P5:
        b = p5.depense_pub * c.part
        n = b / c.ncac_canal
        total_clients += n
        a(ligne([c.nom, pct(c.part, 0), eur(b), eur(c.ncac_canal, 2),
                 f"{n:,.0f}".replace(",", " "), c.role]))
    a(ligne(["**Total**", "100 %", f"**{eur(p5.depense_pub)}**", "—",
             f"**{total_clients:,.0f}**".replace(",", " "), "—"]))
    a("")
    tot_s = f"{total_clients:,.0f}".replace(",", "\u202f")
    reel_s = f"{p5.commandes_new:,.0f}".replace(",", "\u202f")
    surattr = (total_clients / p5.commandes_new - 1) * 100
    a(f"> **Attention.** La somme des clients attribués par canal ({tot_s}) dépasse")
    a(f"> les nouveaux clients réels ({reel_s}), soit **{surattr:.0f}\u202f% de sur-attribution**.")
    a("> C'est normal et universel : chaque plateforme s'attribue le même client.")
    a("> Le seul chiffre honnête est le nCAC global — module E09.")
    a("")
    a("> **Convention à ne pas manquer.** Le modèle affecte **100\u202f% de la dépense")
    a("> publicitaire à l'acquisition de nouveaux clients** : aucun budget n'est isolé")
    a("> pour le retargeting ou la réactivation. C'est volontaire, et ça rend le nCAC")
    a("> **prudent** — il porte tout le média. Une marque qui isole 10\u202f% de son")
    a("> budget en retargeting affichera un nCAC plus flatteur sans qu'un seul euro")
    a("> ait changé de place. C'est exactement le genre de convention qu'il faut")
    a("> écrire avant de comparer deux marques entre elles.")
    a("")
    a("---")
    a("")

    # -- 6. crea
    a("## 6. La machine créative — combien de publicités faut-il produire ?")
    a("")
    a(ligne(["Palier", "Budget pub/sem.", "Budget de test (15 %)", "Concepts testés/sem.",
             "Gagnants/sem.", "Gagnants en rotation", "Assets produits/mois"]))
    a(ligne(["---", "---:", "---:", "---:", "---:", "---:", "---:"]))
    for code in ["P2", "P3", "P5"]:
        b = CREA[code]
        a(ligne([code, eur(b.budget_hebdo), eur(b.budget_hebdo * b.part_budget_test),
                 f"{b.concepts_testes_semaine:.0f}", f"{b.gagnants_semaine:.1f}".replace(".", ","),
                 f"{b.gagnants_en_rotation:.0f}", f"{b.assets_mois:,.0f}".replace(",", "\u202f")]))
    a("")
    a("> **Voilà le vrai goulot d'étranglement d'une marque à 1 M€/semaine.** Ce n'est")
    a("> ni le produit, ni le budget, ni l'algorithme : c'est la capacité à produire")
    a("> et juger ~**{:.0f} concepts publicitaires nouveaux par semaine**, dont ~{:.0f} seulement"
      .format(CREA["P5"].concepts_testes_semaine, CREA["P5"].gagnants_semaine))
    a("> survivront. Module E05.")
    a("")
    a("---")
    a("")

    # -- 7. sensibilite
    a("## 7. Quel levier vaut le plus ? (au palier P5)")
    a("")
    a("Effet sur l'**EBITDA annuel** d'une amélioration de 10 % de chaque levier,")
    a("toutes choses égales par ailleurs.")
    a("")
    a(f"EBITDA annuel de référence : **{eur(p5.ebitda * 12)}**.")
    a("")
    a(ligne(["Levier", "Gain d'EBITDA annuel", "En % de l'EBITDA"]))
    a(ligne(["---", "---:", "---:"]))
    for nom, gain in sensibilite(p5):
        a(ligne([nom, eur(gain), pct(gain / (p5.ebitda * 12))]))
    a("")
    a("> **Lis ce tableau deux fois.** Le levier le plus rentable n'est presque jamais")
    a("> celui sur lequel l'équipe passe ses journées. Refais-le avec **tes** chiffres :")
    a("> c'est l'exercice 4 du module E01.")
    a("")
    a("---")
    a("")

    # -- 8. p5 optimise
    a("## 8. Le même chiffre d'affaires, piloté sur la marge")
    a("")
    a("P5 fait 1 M€/semaine à " + pct(p5.taux_ebitda) + " d'EBITDA. P5+ fait le même")
    a("chiffre d'affaires avec moins de commandes, un panier plus élevé, plus de")
    a("réachat et moins de remises.")
    a("")
    po = P5_OPTIMISE
    a(ligne(["", "P5 — piloté volume", "P5+ — piloté marge", "Écart"]))
    a(ligne(["---", "---:", "---:", "---:"]))
    rows = [
        ("CA TTC / semaine", eur(p5.ca_semaine_ttc), eur(po.ca_semaine_ttc), ""),
        ("Commandes / mois", f"{p5.commandes_mois:,}".replace(",", " "),
         f"{po.commandes_mois:,}".replace(",", " "),
         f"{(po.commandes_mois / p5.commandes_mois - 1) * 100:+.0f} %"),
        ("AOV mixte TTC", eur(p5.aov_blended_ttc, 2), eur(po.aov_blended_ttc, 2),
         f"{(po.aov_blended_ttc / p5.aov_blended_ttc - 1) * 100:+.0f} %"),
        ("Part du CA en réachat", pct(p5.part_ca_repeat), pct(po.part_ca_repeat),
         f"{(po.part_ca_repeat - p5.part_ca_repeat) * 100:+.1f} pts".replace(".", ",")),
        ("MER", f"{p5.mer:.2f}".replace(".", ","), f"{po.mer:.2f}".replace(".", ","), ""),
        ("Marge brute (CM2)", pct(p5.taux_marge_brute), pct(po.taux_marge_brute),
         f"{(po.taux_marge_brute - p5.taux_marge_brute) * 100:+.1f} pts".replace(".", ",")),
        ("Dépense pub / mois", eur(p5.depense_pub), eur(po.depense_pub),
         f"{(po.depense_pub / p5.depense_pub - 1) * 100:+.0f} %"),
        ("**EBITDA / mois**", f"**{eur(p5.ebitda)}**", f"**{eur(po.ebitda)}**",
         f"**{(po.ebitda / p5.ebitda - 1) * 100:+.0f} %**"),
        ("**EBITDA en % du CA HT**", f"**{pct(p5.taux_ebitda)}**", f"**{pct(po.taux_ebitda)}**",
         f"**{(po.taux_ebitda - p5.taux_ebitda) * 100:+.1f} pts**".replace(".", ",")),
        ("**EBITDA annuel**", f"**{eur(p5.ebitda * 12)}**", f"**{eur(po.ebitda * 12)}**",
         f"**{eur(po.ebitda * 12 - p5.ebitda * 12)}**"),
    ]
    for r in rows:
        a(ligne(list(r)))
    a("")
    a("### 8.1 D'où viennent les 4,5 points de marge brute")
    a("")
    a("Le tableau ci-dessus donne le total. Voici sa décomposition poste par poste,")
    a("pour que chaque point ait un chantier et un responsable :")
    a("")
    a(ligne(["Poste", "P5", "P5+", "Écart", "Le chantier", "Module"]))
    a(ligne(["---", "---:", "---:", "---:", "---", "---"]))
    postes = [
        ("COGS", p5.cogs_pct, po.cogs_pct, "Paliers de volume, double source, renégociation annuelle", "E10 § 9"),
        ("Logistique", p5.logistique_pct, po.logistique_pct, "Contrat 3PL, transporteur, remplissage du colis", "E10 § 6"),
        ("PSP", p5.psp_pct, po.psp_pct, "Renégociation au volume, mix de moyens de paiement", "E10"),
        ("Retours / SAV", p5.retours_sav_pct, po.retours_sav_pct, "Fiche produit honnête, guide de choix, ciblage plus qualifié", "E07, E10 § 7"),
        ("Remises", p5.remises_pct, po.remises_pct, "Fin de la remise permanente, contrepartie exigée", "E03 § 5"),
    ]
    total_ecart = 0.0
    for nom, a5, ap, chantier, mod in postes:
        ecart = a5 - ap
        total_ecart += ecart
        a(ligne([nom, pct(a5, 2), pct(ap, 2),
                 f"**{ecart * 100:+.2f} {'pt' if abs(ecart) < 0.02 else 'pts'}**".replace(".", ","), chantier, mod]))
    a(ligne(["**Total**", f"**{pct(p5.taux_variable, 2)}**", f"**{pct(po.taux_variable, 2)}**",
             f"**{total_ecart * 100:+.2f} pts**".replace(".", ","), "—", "—"]))
    a("")
    a("> **Regarde la colonne des écarts.** Plus de la moitié du gain vient de la")
    a("> **remise** — le seul poste qui ne demande ni négociation, ni prestataire, ni")
    a("> investissement. Il ne demande que de la discipline commerciale, et c'est")
    a("> exactement pour ça qu'il est le plus difficile à tenir.")
    a("")
    a("> **C'est là que se trouve l'argent.** Le passage de P5 à P5+ ne demande")
    a("> aucun euro de chiffre d'affaires supplémentaire. Il demande un panier moyen")
    a("> plus élevé, une base de clients qui revient, et de la discipline sur la")
    a("> remise. **Ton objectif n'est pas 1 M€/semaine. Ton objectif est P5+.**")
    a("")
    a("---")
    a("")
    a("## 9. Le tableau de conversion à connaître par cœur")
    a("")
    a(ligne(["CA TTC / semaine", "CA TTC / mois", "CA TTC / an", "Commandes/jour à 72 € d'AOV", "Dépense pub/jour à MER 2,9"]))
    a(ligne(["---:", "---:", "---:", "---:", "---:"]))
    for sem in [10_000, 25_000, 50_000, 100_000, 250_000, 500_000, 1_000_000]:
        mois = sem * 52 / 12
        an = sem * 52
        cmd = sem / 7 / 72
        pub = (sem / 2.9) / 7
        a(ligne([eur(sem), eur(mois), eur(an), f"{cmd:,.0f}".replace(",", " "), eur(pub)]))
    a("")
    a("> **Deux conventions de passage au quotidien coexistent dans ce fichier, et")
    a("> c'est assumé.** Les volumes de commandes du § 9 sont dérivés de la semaine")
    a("> (÷ 7) ; la dépense publicitaire du § 5 est dérivée du mois (÷ 30,4). L'écart")
    a("> résiduel est de l'ordre de 0,2\u202f%. Ce n'est pas une erreur : c'est la")
    a("> précision réelle de ce type de modèle. **Si tu pilotes une marque sur des")
    a("> écarts de 0,2\u202f%, tu pilotes du bruit** — voir E09 § 8.")
    a("")
    a("*Fin des chiffres canoniques. Généré par `ecommerce/outils/modele_nora.py`.*")
    return "\n".join(o)


if __name__ == "__main__":
    txt = rapport()
    if "--ecrire" in sys.argv:
        import os
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        chemin = os.path.join(base, "donnees", "chiffres-canoniques.md")
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(txt + "\n")
        print(f"Écrit : {chemin}")
    else:
        print(txt)
