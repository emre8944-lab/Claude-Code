#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plan objectif — traducteur d'objectif en plan operationnel.

Repond a une seule question : « je veux faire X € TTC par semaine — qu'est-ce
que ca exige, physiquement ? »

Un objectif de chiffre d'affaires n'est pas un plan. C'est une consequence.
Derriere « 1 M€ par semaine » il y a un nombre de commandes a l'heure, un
nombre d'impressions a acheter, un nombre de concepts publicitaires a juger,
un nombre de colis a preparer, un nombre de personnes a payer et un montant de
cash a immobiliser avant d'encaisser. Cet outil deroule cette chaine et la
confronte, ligne par ligne, a la situation actuelle de la marque.

Il ne dit pas si l'objectif est atteignable. Il dit ce qui devrait etre vrai
pour qu'il le soit, et de combien on en est loin.

Usage :
    python3 ecommerce/outils/plan_objectif.py --demo
    python3 ecommerce/outils/plan_objectif.py --verifier
    python3 ecommerce/outils/plan_objectif.py \\
        --objectif 250000 --aov 68 --marge 58 --mer 2,4 --part-reachat 30 \\
        --cpm 9,20 --ctr 1,1 --conversion 2,0 \\
        --actuel-ca 90000 --actuel-aov 61 --actuel-mer 2,1

Aucune dependance externe. Python 3.9+.
Conventions de formatage : voir ecommerce/outils/modele_nora.py (eur, pct).
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from typing import List, Optional

# ---------------------------------------------------------------------------
# 0. RACCORDEMENT AU MODELE CANONIQUE
#    modele_nora.py est la source de verite du cursus. On lui emprunte ses
#    formateurs et les hypotheses des paliers P3 et P5 qui alimentent --demo.
#    Si l'import echoue (fichier deplace), on retombe sur des copies locales
#    recopiees de donnees/chiffres-canoniques.md.
# ---------------------------------------------------------------------------

_ICI = os.path.dirname(os.path.abspath(__file__))
if _ICI not in sys.path:
    sys.path.insert(0, _ICI)

try:
    from modele_nora import PALIERS, TRESO, CREA, eur, pct, TVA  # type: ignore
    CANONIQUE_DISPONIBLE = True
except Exception:  # pragma: no cover - chemin de repli
    CANONIQUE_DISPONIBLE = False
    PALIERS = None
    TRESO = None
    CREA = None
    TVA = 0.20

    def eur(x: float, d: int = 0) -> str:
        s = f"{x:,.{d}f}".replace(",", " ").replace(".", ",").replace("-", "−")
        return s + " €"

    def pct(x: float, d: int = 1) -> str:
        return f"{x * 100:.{d}f}".replace(".", ",") + " %"


# Valeurs de repli, recopiees de donnees/chiffres-canoniques.md.
# Attention : le tableau § 2.1 affiche la marge brute P5 arrondie a 61,5 % ;
# la valeur exacte du modele est 61,45 % (1 − 38,55 % de couts variables).
REPLI = {
    "p5_ca_sem_ttc": 999_968.0, "p5_aov": 71.98, "p5_marge": 0.6145,
    "p5_mer": 2.90, "p5_part_reachat": 0.38, "p5_cogs": 0.145,
    "p5_etp": 38.0, "p5_stock_j": 105, "p5_dso": 3, "p5_dpo": 60, "p5_pub_j": 21,
    "p5_budget_concept": 900.0, "p5_reussite": 0.09, "p5_variations": 5,
    "p5_duree_vie": 4.5,
    "p3_ca_sem_ttc": 271_662.0, "p3_aov": 65.40, "p3_marge": 0.6035,
    "p3_mer": 2.70, "p3_part_reachat": 0.27, "p3_etp": 12.0,
    "p3_bfr": 481_053.0, "p3_concepts": 37.7,
}

# Cibles de verification, lues telles quelles dans chiffres-canoniques.md.
# Chaque entree : (libelle, valeur canonique, section d'origine, tolerance).
CANON = [
    ("CA TTC / mois",                 4_333_333.0, "§ 9",   0.001),
    ("CA TTC / an",                  52_000_000.0, "§ 9",   0.001),
    ("Commandes / jour",                   1_984.0, "§ 9",  0.005),
    ("Dépense pub / jour (base semaine)",  49_261.0, "§ 9", 0.002),
    ("Dépense pub / jour (base mois)",     49_151.0, "§ 5",  0.005),
    ("Dépense pub / semaine",             344_817.0, "§ 5",  0.002),
    ("Dépense pub / mois",             1_494_206.0, "§ 5",   0.002),
    ("Nouveaux clients / mois",            37_324.0, "§ 2.4", 0.002),
    ("nCAC",                                  40.03, "§ 2.4", 0.002),
    ("Budget de test créatif / semaine",   51_722.0, "§ 6",  0.002),
    ("Concepts testés / semaine",              57.0, "§ 6",  0.010),
    ("Gagnants / semaine",                      5.2, "§ 6",  0.010),
    ("Gagnants en rotation",                   23.0, "§ 6",  0.020),
    ("Assets produits / mois",              1_245.0, "§ 6",  0.005),
    ("ETP total",                              38.0, "§ 2.5", 0.005),
    ("BFR",                             2_264_655.0, "§ 4",  0.002),
    ("BFR en jours de CA TTC",                 16.0, "§ 4",  0.030),
]


# ---------------------------------------------------------------------------
# 1. FORMATAGE
# ---------------------------------------------------------------------------

def num(x: float, d: int = 0) -> str:
    """Meme formatage que eur(), sans le suffixe € (l'unite est en en-tete)."""
    return f"{x:,.{d}f}".replace(",", " ").replace(".", ",").replace("-", "−")


def num_signe(x: float, d: int = 0) -> str:
    return f"{x:+,.{d}f}".replace(",", " ").replace(".", ",").replace("-", "−")


def taux(x: float, d: int = 1) -> str:
    """Pourcentage, avec le vrai signe moins typographique."""
    return pct(x, d).replace("-", "−")


def taux_signe(x: float, d: int = 1) -> str:
    """Variation relative signee : « +40,7 % », « −12,0 % »."""
    return (f"{x * 100:+.{d}f}".replace(".", ",") + " %").replace("-", "−")


def pts(x: float, d: int = 1) -> str:
    """Ecart exprime en points de pourcentage."""
    return (f"{x * 100:+.{d}f}".replace(".", ",") + " pts").replace("-", "−")


def eur_signe(x: float, d: int = 0) -> str:
    return num_signe(x, d) + " €"


def duree(secondes: float) -> str:
    """« 10,4 s », « 3 min 12 s » — pour donner un rythme, pas un chiffre."""
    if secondes < 90:
        return num(secondes, 1) + " s"
    m = int(secondes // 60)
    s = secondes - 60 * m
    return f"{m} min {num(s, 0)} s"


def lire_taux(s: str) -> float:
    """« 61,5 », « 61.5 », « 61,5 % » -> 0,615."""
    s = s.strip().replace(" ", "").replace(" ", "").replace(" ", "")
    s = s.replace("%", "").replace("−", "-").replace(",", ".")
    return float(s) / 100.0


def lire_nombre(s: str) -> float:
    """« 2,9 » ou « 2.9 » -> 2.9. Un MER s'écrit avec une virgule en français."""
    return float(s.strip().replace("−", "-").replace(",", "."))


def lire_montant(s: str) -> float:
    """« 1 000 000 », « 1000000,50 », « 250k », « 1,2M » -> float."""
    s = s.strip().replace(" ", "").replace(" ", "").replace(" ", "")
    s = s.replace("€", "").replace("−", "-").replace(",", ".")
    mult = 1.0
    if s and s[-1] in "kK":
        mult, s = 1_000.0, s[:-1]
    elif s and s[-1] in "mM":
        mult, s = 1_000_000.0, s[:-1]
    return float(s) * mult


def tableau(entetes: List[str], lignes: List[List[str]],
            gauche: Optional[List[int]] = None) -> List[str]:
    """Tableau texte a colonnes alignees. Largeurs calculees sur le contenu."""
    gauche = gauche or []
    cols = len(entetes)
    larg = [len(entetes[i]) for i in range(cols)]
    for ln in lignes:
        for i in range(cols):
            larg[i] = max(larg[i], len(ln[i]))

    def rendre(cellules: List[str]) -> str:
        out = []
        for i, c in enumerate(cellules):
            out.append(c.ljust(larg[i]) if i in gauche else c.rjust(larg[i]))
        return "  ".join(out).rstrip()

    barre = "  ".join("─" * l for l in larg)
    return [rendre(entetes), barre] + [rendre(l) for l in lignes]


def titre(t: str, souligne: str = "-") -> List[str]:
    return ["", t, souligne * len(t)]


# ---------------------------------------------------------------------------
# 2. LES ENTREES
#    Un objectif hebdomadaire, et les quatorze parametres qui decident de ce
#    qu'il exige. Les montants d'entree sont TTC quand ils viennent du client
#    (CA, AOV) et HT quand ils viennent d'un fournisseur (pub, salaires, COGS).
# ---------------------------------------------------------------------------

SEMAINES_AN = 52
JOURS_SEMAINE = 7


@dataclass(frozen=True)
class Objectif:
    """Les hypotheses du plan. Tout le reste en est deduit."""

    # -- les quatorze entrees principales ---------------------------------
    ca_ttc_semaine: float            # objectif de CA TTC par semaine
    aov_ttc: float                   # panier moyen TTC vise, toutes commandes
    taux_marge_brute: float          # CM2 : marge apres TOUS couts variables, % du CA HT
    mer: float                       # CA TTC / depense publicitaire
    part_commandes_reachat: float    # part des commandes passees par un client deja acquis
    cpm: float                       # cout HT pour mille impressions achetees
    taux_clic: float                 # impressions -> clics
    taux_conversion: float           # sessions -> commandes
    part_budget_test: float          # part de la depense pub reservee au test creatif
    budget_par_concept: float        # budget HT minimal pour juger un concept
    taux_reussite_concepts: float    # part des concepts testes qui deviennent scalables
    tickets_sav_par_commande: float  # sollicitations service client par commande
    commandes_par_preparateur_jour: float   # productivite logistique, par personne et par jour
    ca_ht_annuel_par_etp: float      # productivite de la structure

    # -- parametres secondaires, avec des defauts explicites ---------------
    tva: float = 0.20
    taux_arrivee: float = 0.90       # clics -> sessions (10 % ne chargent jamais la page)
    jours_ouvres: int = 5            # jours travailles par semaine (entrepot et bureaux)
    heures_par_jour: float = 8.0
    unites_par_commande: float = 1.8
    variations_par_concept: int = 5  # declinaisons produites par concept teste
    duree_vie_concept_semaines: float = 4.5
    tickets_par_agent_jour: float = 50.0
    cout_etp_annuel: float = 72_000.0       # cout employeur charge, HT, par ETP et par an

    # -- besoin en fonds de roulement --------------------------------------
    cogs_pct: float = 0.145          # cout marchandise, % du CA HT
    jours_stock: int = 105           # DIO
    delai_encaissement: int = 3      # DSO : reserve PSP + versement
    delai_fournisseur: int = 60      # DPO : credit obtenu du fabricant
    delai_pub: int = 21              # jours entre la depense pub et l'encaissement
    coussin_semaines: float = 4.0    # semaines de pub a tenir sans encaisser


@dataclass(frozen=True)
class Actuel:
    """La situation de depart. Tout est optionnel : on compare ce qu'on a."""
    ca_ttc_semaine: Optional[float] = None
    aov_ttc: Optional[float] = None
    mer: Optional[float] = None
    taux_marge_brute: Optional[float] = None
    part_commandes_reachat: Optional[float] = None
    taux_conversion: Optional[float] = None
    cpm: Optional[float] = None
    concepts_semaine: Optional[float] = None
    commandes_par_preparateur_jour: Optional[float] = None
    tickets_sav_par_commande: Optional[float] = None
    etp: Optional[float] = None
    bfr: Optional[float] = None

    @property
    def vide(self) -> bool:
        return all(getattr(self, f) is None for f in self.__dataclass_fields__)

    # Ce qui se deduit du trio CA / AOV / MER, quand il est fourni.
    @property
    def commandes_semaine(self) -> Optional[float]:
        if self.ca_ttc_semaine is None or not self.aov_ttc:
            return None
        return self.ca_ttc_semaine / self.aov_ttc

    @property
    def commandes_jour(self) -> Optional[float]:
        c = self.commandes_semaine
        return None if c is None else c / JOURS_SEMAINE

    @property
    def nouveaux_clients_jour(self) -> Optional[float]:
        c = self.commandes_jour
        if c is None or self.part_commandes_reachat is None:
            return None
        return c * (1 - self.part_commandes_reachat)

    @property
    def pub_semaine(self) -> Optional[float]:
        if self.ca_ttc_semaine is None or not self.mer:
            return None
        return self.ca_ttc_semaine / self.mer

    @property
    def pub_jour(self) -> Optional[float]:
        p = self.pub_semaine
        return None if p is None else p / JOURS_SEMAINE

    @property
    def ncac(self) -> Optional[float]:
        p, n = self.pub_semaine, self.nouveaux_clients_jour
        if p is None or not n:
            return None
        return p / (n * JOURS_SEMAINE)

    def unites_jour(self, unites_par_commande: float) -> Optional[float]:
        c = self.commandes_jour
        return None if c is None else c * unites_par_commande

    @property
    def tickets_jour(self) -> Optional[float]:
        c = self.commandes_jour
        if c is None or self.tickets_sav_par_commande is None:
            return None
        return c * self.tickets_sav_par_commande


# ---------------------------------------------------------------------------
# 3. LE PLAN
#    Une seule classe, que des proprietes. Chaque nombre affiche dans le
#    rapport sort d'ici, et d'une formule lisible en une ligne.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Plan:
    o: Objectif

    # -- 1. le chiffre d'affaires -----------------------------------------
    @property
    def ca_ttc_semaine(self) -> float:
        return self.o.ca_ttc_semaine

    @property
    def ca_ht_semaine(self) -> float:
        return self.o.ca_ttc_semaine / (1 + self.o.tva)

    @property
    def ca_ttc_mois(self) -> float:
        return self.o.ca_ttc_semaine * SEMAINES_AN / 12

    @property
    def ca_ht_mois(self) -> float:
        return self.ca_ttc_mois / (1 + self.o.tva)

    @property
    def ca_ttc_an(self) -> float:
        return self.o.ca_ttc_semaine * SEMAINES_AN

    @property
    def ca_ht_an(self) -> float:
        return self.ca_ttc_an / (1 + self.o.tva)

    # -- 2. les commandes --------------------------------------------------
    @property
    def commandes_semaine(self) -> float:
        return self.ca_ttc_semaine / self.o.aov_ttc

    @property
    def commandes_jour(self) -> float:
        return self.commandes_semaine / JOURS_SEMAINE

    @property
    def commandes_mois(self) -> float:
        return self.commandes_semaine * SEMAINES_AN / 12

    @property
    def commandes_jour_ouvre(self) -> float:
        return self.commandes_semaine / self.o.jours_ouvres

    @property
    def commandes_heure_ouvree(self) -> float:
        return self.commandes_semaine / (self.o.jours_ouvres * self.o.heures_par_jour)

    @property
    def secondes_par_commande(self) -> float:
        return 3600 / self.commandes_heure_ouvree

    @property
    def effet_panier_plus_un_euro(self) -> float:
        """Commandes / jour economisees par euro de panier moyen en plus,
        a chiffre d'affaires identique. Le levier le moins cher du plan."""
        return self.commandes_jour / (self.o.aov_ttc + 1)

    # -- 3. acquisition ----------------------------------------------------
    @property
    def commandes_reachat_semaine(self) -> float:
        return self.commandes_semaine * self.o.part_commandes_reachat

    @property
    def nouvelles_commandes_semaine(self) -> float:
        return self.commandes_semaine - self.commandes_reachat_semaine

    @property
    def nouveaux_clients_jour(self) -> float:
        """Hypothese : une premiere commande = un nouveau client."""
        return self.nouvelles_commandes_semaine / JOURS_SEMAINE

    @property
    def nouveaux_clients_mois(self) -> float:
        return self.nouvelles_commandes_semaine * SEMAINES_AN / 12

    @property
    def pub_semaine(self) -> float:
        return self.ca_ttc_semaine / self.o.mer

    @property
    def pub_jour(self) -> float:
        return self.pub_semaine / JOURS_SEMAINE

    @property
    def pub_mois(self) -> float:
        return self.pub_semaine * SEMAINES_AN / 12

    @property
    def pub_pct_ht(self) -> float:
        """Le piege du MER : il se calcule sur le TTC, la marge sur le HT."""
        return self.pub_mois / self.ca_ht_mois

    @property
    def ncac(self) -> float:
        return self.pub_semaine / self.nouvelles_commandes_semaine

    @property
    def contribution_premiere_commande(self) -> float:
        return (self.o.aov_ttc / (1 + self.o.tva)) * self.o.taux_marge_brute

    @property
    def marge_premiere_commande(self) -> float:
        """Negatif = la premiere commande ne paie pas son acquisition."""
        return self.contribution_premiere_commande - self.ncac

    @property
    def mer_seuil_cm3(self) -> float:
        return (1 + self.o.tva) / self.o.taux_marge_brute

    # -- 4. le funnel media ------------------------------------------------
    #    Chaine remontante : on part des nouveaux clients qu'il faut acquerir
    #    et on remonte jusqu'aux impressions a acheter. Le cout media que cette
    #    chaine implique est ensuite confronte au budget que le MER autorise.
    @property
    def sessions_payantes_jour(self) -> float:
        return self.nouveaux_clients_jour / self.o.taux_conversion

    @property
    def sessions_site_jour(self) -> float:
        """Toutes sources : le reachat passe aussi par le site."""
        return self.commandes_jour / self.o.taux_conversion

    @property
    def clics_jour(self) -> float:
        return self.sessions_payantes_jour / self.o.taux_arrivee

    @property
    def impressions_jour(self) -> float:
        return self.clics_jour / self.o.taux_clic

    @property
    def cpc(self) -> float:
        return self.o.cpm / 1000 / self.o.taux_clic

    @property
    def cout_par_session(self) -> float:
        return self.cpc / self.o.taux_arrivee

    @property
    def cac_du_funnel(self) -> float:
        """CAC implique par CPM x CTR x taux d'arrivee x conversion."""
        return self.cout_par_session / self.o.taux_conversion

    @property
    def cout_media_jour(self) -> float:
        return self.impressions_jour / 1000 * self.o.cpm

    @property
    def ecart_media_jour(self) -> float:
        """> 0 : le funnel coute plus cher que ce que le MER autorise."""
        return self.cout_media_jour - self.pub_jour

    @property
    def cpm_maximal(self) -> float:
        return self.pub_jour / self.impressions_jour * 1000

    @property
    def conversion_requise(self) -> float:
        """Taux de conversion qui refermerait l'ecart, CPM et CTR inchanges."""
        sessions_financables = (self.pub_jour / self.o.cpm * 1000
                                * self.o.taux_clic * self.o.taux_arrivee)
        return self.nouveaux_clients_jour / sessions_financables

    # -- 5. la machine creative -------------------------------------------
    @property
    def budget_test_semaine(self) -> float:
        return self.pub_semaine * self.o.part_budget_test

    @property
    def concepts_semaine(self) -> float:
        return self.budget_test_semaine / self.o.budget_par_concept

    @property
    def gagnants_semaine(self) -> float:
        return self.concepts_semaine * self.o.taux_reussite_concepts

    @property
    def gagnants_en_rotation(self) -> float:
        return self.gagnants_semaine * self.o.duree_vie_concept_semaines

    @property
    def assets_mois(self) -> float:
        return self.concepts_semaine * self.o.variations_par_concept * SEMAINES_AN / 12

    @property
    def concepts_jour_ouvre(self) -> float:
        return self.concepts_semaine / self.o.jours_ouvres

    @property
    def budget_perdu_semaine(self) -> float:
        """Ce que coutent les concepts qui ne passeront pas. C'est le prix du test."""
        return self.budget_test_semaine * (1 - self.o.taux_reussite_concepts)

    # -- 6. les operations -------------------------------------------------
    @property
    def unites_jour(self) -> float:
        return self.commandes_jour * self.o.unites_par_commande

    @property
    def unites_jour_ouvre(self) -> float:
        return self.commandes_jour_ouvre * self.o.unites_par_commande

    @property
    def preparateurs(self) -> float:
        return self.commandes_jour_ouvre / self.o.commandes_par_preparateur_jour

    @property
    def tickets_jour(self) -> float:
        return self.commandes_jour * self.o.tickets_sav_par_commande

    @property
    def tickets_jour_ouvre(self) -> float:
        return self.commandes_jour_ouvre * self.o.tickets_sav_par_commande

    @property
    def etp_sav(self) -> float:
        return self.tickets_jour_ouvre / self.o.tickets_par_agent_jour

    # -- 7. la structure ---------------------------------------------------
    @property
    def etp_total(self) -> float:
        return self.ca_ht_an / self.o.ca_ht_annuel_par_etp

    @property
    def etp_autres(self) -> float:
        """Ce qui reste une fois le service client interne compte."""
        return self.etp_total - self.etp_sav

    @property
    def masse_salariale_an(self) -> float:
        return self.etp_total * self.o.cout_etp_annuel

    @property
    def masse_salariale_mois(self) -> float:
        return self.masse_salariale_an / 12

    @property
    def masse_pct_ca_ht(self) -> float:
        return self.masse_salariale_an / self.ca_ht_an

    # -- 8. le cash --------------------------------------------------------
    @property
    def cogs_mois(self) -> float:
        return self.ca_ht_mois * self.o.cogs_pct

    @property
    def stock_immobilise(self) -> float:
        return self.cogs_mois * self.o.jours_stock / 30

    @property
    def creances(self) -> float:
        return self.ca_ttc_mois * self.o.delai_encaissement / 30

    @property
    def avance_pub(self) -> float:
        return self.pub_mois * self.o.delai_pub / 30

    @property
    def dettes_fournisseurs(self) -> float:
        return self.cogs_mois * self.o.delai_fournisseur / 30

    @property
    def bfr(self) -> float:
        return (self.stock_immobilise + self.creances + self.avance_pub
                - self.dettes_fournisseurs)

    @property
    def bfr_jours_ca(self) -> float:
        return self.bfr / (self.ca_ttc_mois / 30)

    @property
    def cm3_mois(self) -> float:
        """Marge brute moins publicite. Avant frais fixes."""
        return self.ca_ht_mois * (self.o.taux_marge_brute - self.pub_pct_ht)

    @property
    def reste_apres_salaires(self) -> float:
        return self.cm3_mois - self.masse_salariale_mois

    @property
    def coussin(self) -> float:
        return self.o.coussin_semaines * self.pub_semaine

    def capital_de_croissance(self, bfr_actuel: Optional[float]) -> float:
        return (self.bfr - (bfr_actuel or 0.0)) + self.coussin


# ---------------------------------------------------------------------------
# 4. « CE QUI DOIT ETRE VRAI »
# ---------------------------------------------------------------------------

@dataclass
class Exigence:
    nom: str
    genre: str                    # "montant" | "nombre" | "taux" | "ratio"
    cible: float
    actuel: Optional[float]
    sens: str = "hausse"          # sens de l'effort demande : hausse | baisse
    d: int = 0                    # decimales d'affichage

    def fmt(self, x: float) -> str:
        if self.genre == "montant":
            return eur(x, self.d)
        if self.genre == "taux":
            return taux(x, 2)
        if self.genre == "ratio":
            return num(x, 2)
        return num(x, self.d)

    def fmt_ecart(self, x: float) -> str:
        if self.genre == "montant":
            return eur_signe(x, self.d)
        if self.genre == "taux":
            return pts(x, 2)
        if self.genre == "ratio":
            return num_signe(x, 2)
        return num_signe(x, self.d)

    def ligne(self) -> List[str]:
        if self.actuel is None:
            return [self.nom, self.fmt(self.cible), "—", "—", "non fourni"]
        ecart = self.cible - self.actuel
        if abs(self.actuel) < 1e-12:
            facteur = "depuis zéro"
        elif self.genre == "taux":
            facteur = taux_signe(self.cible / self.actuel - 1, 1)
        else:
            r = self.cible / self.actuel
            facteur = ("×" + num(r, 2)) if r >= 1 else taux_signe(r - 1, 1)
        if self.sens == "baisse":
            facteur += " (à baisser)" if ecart <= 0 else " (dégradation admise)"
        return [self.nom, self.fmt(self.cible), self.fmt(self.actuel),
                self.fmt_ecart(ecart), facteur]


def exigences(p: Plan, a: Actuel) -> List[Exigence]:
    """La liste de tout ce qui doit devenir vrai, dans l'ordre de la chaine."""
    o = p.o
    return [
        Exigence("CA TTC / semaine", "montant", p.ca_ttc_semaine, a.ca_ttc_semaine),
        Exigence("Panier moyen TTC", "montant", o.aov_ttc, a.aov_ttc, d=2),
        Exigence("Commandes / jour", "nombre", p.commandes_jour, a.commandes_jour, d=0),
        Exigence("Part des commandes en réachat", "taux",
                 o.part_commandes_reachat, a.part_commandes_reachat),
        Exigence("Nouveaux clients / jour", "nombre",
                 p.nouveaux_clients_jour, a.nouveaux_clients_jour, d=0),
        Exigence("Dépense pub HT / jour", "montant", p.pub_jour, a.pub_jour),
        Exigence("MER", "ratio", o.mer, a.mer),
        Exigence("nCAC", "montant", p.ncac, a.ncac, sens="baisse", d=2),
        Exigence("Marge brute (CM2, % CA HT)", "taux",
                 o.taux_marge_brute, a.taux_marge_brute),
        Exigence("Taux de conversion du site", "taux",
                 o.taux_conversion, a.taux_conversion),
        Exigence("CPM acheté", "montant", o.cpm, a.cpm, sens="baisse", d=2),
        Exigence("Concepts testés / semaine", "nombre",
                 p.concepts_semaine, a.concepts_semaine, d=1),
        Exigence("Assets créatifs / mois", "nombre", p.assets_mois, None, d=0),
        Exigence("Unités expédiées / jour", "nombre", p.unites_jour,
                 a.unites_jour(o.unites_par_commande), d=0),
        Exigence("Commandes / préparateur / jour", "nombre",
                 o.commandes_par_preparateur_jour,
                 a.commandes_par_preparateur_jour, d=0),
        Exigence("Tickets SAV / jour", "nombre", p.tickets_jour, a.tickets_jour, d=0),
        Exigence("ETP total", "nombre", p.etp_total, a.etp, d=1),
        Exigence("BFR", "montant", p.bfr, a.bfr),
    ]


# ---------------------------------------------------------------------------
# 5. RENDU
# ---------------------------------------------------------------------------

def rapport(o: Objectif, a: Optional[Actuel] = None,
            entete: Optional[List[str]] = None) -> str:
    p = Plan(o)
    a = a or Actuel()
    out: List[str] = []
    add = out.append

    add("=" * 78)
    add(f"PLAN OBJECTIF — CE QUE {eur(o.ca_ttc_semaine)} TTC PAR SEMAINE EXIGE")
    add("=" * 78)
    for l in (entete or []):
        add(l)

    # -- hypotheses --------------------------------------------------------
    out += titre("0. Hypothèses retenues")
    out += tableau(
        ["Paramètre", "Valeur", "Paramètre", "Valeur"],
        [
            ["Objectif CA TTC / semaine", eur(o.ca_ttc_semaine),
             "Budget de test créatif", taux(o.part_budget_test, 0)],
            ["Panier moyen TTC visé", eur(o.aov_ttc, 2),
             "Budget HT / concept testé", eur(o.budget_par_concept)],
            ["Marge brute (CM2, % CA HT)", taux(o.taux_marge_brute, 2),
             "Taux de réussite des concepts", taux(o.taux_reussite_concepts, 1)],
            ["MER visé (CA TTC / pub)", num(o.mer, 2),
             "Variations / concept", num(o.variations_par_concept)],
            ["Part des commandes en réachat", taux(o.part_commandes_reachat, 1),
             "Tickets SAV / commande", num(o.tickets_sav_par_commande, 2)],
            ["CPM HT acheté", eur(o.cpm, 2),
             "Cmd. / préparateur / jour", num(o.commandes_par_preparateur_jour)],
            ["Taux de clic", taux(o.taux_clic, 2),
             "Tickets / agent / jour", num(o.tickets_par_agent_jour)],
            ["Taux d'arrivée (clic → session)", taux(o.taux_arrivee, 0),
             "CA HT annuel / ETP", eur(o.ca_ht_annuel_par_etp)],
            ["Taux de conversion du site", taux(o.taux_conversion, 2),
             "Coût employeur HT / ETP / an", eur(o.cout_etp_annuel)],
            ["Unités / commande", num(o.unites_par_commande, 1),
             "COGS (% CA HT)", taux(o.cogs_pct, 1)],
            ["Jours ouvrés / semaine", f"{o.jours_ouvres} j",
             "Stock détenu (DIO)", f"{o.jours_stock} j"],
            ["Heures ouvrées / jour", num(o.heures_par_jour, 0) + " h",
             "Encaissement (DSO)", f"{o.delai_encaissement} j"],
            ["TVA", taux(o.tva, 0), "Crédit fournisseur (DPO)", f"{o.delai_fournisseur} j"],
            ["Durée de vie d'un gagnant", num(o.duree_vie_concept_semaines, 1) + " sem.",
             "Avance publicitaire", f"{o.delai_pub} j"],
        ],
        gauche=[0, 2],
    )

    # -- 1. le chiffre d'affaires -----------------------------------------
    out += titre("1. Le chiffre d'affaires, dans les trois unités de temps")
    out += tableau(
        ["Période", "CA TTC", "CA HT", "Rappel"],
        [
            ["Semaine", eur(p.ca_ttc_semaine), eur(p.ca_ht_semaine), "l'objectif"],
            ["Mois", eur(p.ca_ttc_mois), eur(p.ca_ht_mois),
             f"= semaine × {SEMAINES_AN} ÷ 12"],
            ["An", eur(p.ca_ttc_an), eur(p.ca_ht_an), f"= semaine × {SEMAINES_AN}"],
        ],
        gauche=[0, 3],
    )
    add("")
    add(f"Le seul chiffre comptable est le CA HT : {eur(p.ca_ht_an)} HT par an.")
    add(f"L'écart de {eur(p.ca_ttc_an - p.ca_ht_an)} avec le TTC est de la TVA. Elle transite")
    add("par ta trésorerie, elle ne t'appartient pas, et la confondre avec du")
    add("chiffre d'affaires est l'erreur n° 1 du métier.")

    # -- 2. les commandes --------------------------------------------------
    out += titre("2. Le volume de commandes")
    out += tableau(
        ["Rythme", "Commandes", "Base"],
        [
            ["Par semaine", num(p.commandes_semaine, 0), "CA TTC ÷ panier moyen TTC"],
            ["Par jour calendaire", num(p.commandes_jour, 0), f"÷ {JOURS_SEMAINE} jours"],
            ["Par mois", num(p.commandes_mois, 0), f"× {SEMAINES_AN} ÷ 12"],
            ["Par jour ouvré", num(p.commandes_jour_ouvre, 0),
             f"÷ {o.jours_ouvres} jours ouvrés"],
            ["Par heure ouvrée", num(p.commandes_heure_ouvree, 0),
             f"÷ {o.jours_ouvres} × {num(o.heures_par_jour, 0)} h"],
        ],
        gauche=[0, 2],
    )
    add("")
    add(f"Une commande toutes les {duree(p.secondes_par_commande)} en heure ouvrée : c'est le rythme que")
    add("doivent tenir le paiement, le stock, l'entrepôt et le SAV. Et c'est le")
    add("rythme moyen — la pointe est deux à quatre fois plus haute.")
    add("")
    add(f"Le panier retenu vaut {eur(o.aov_ttc, 2)}. À chiffre d'affaires identique, un euro")
    add(f"de panier moyen en plus retire {num(p.effet_panier_plus_un_euro, 0)} commandes à préparer, à expédier")
    add("et à servir chaque jour. C'est le levier le moins cher de tout ce plan :")
    add("il baisse le coût de servir sans rien coûter à l'acquisition.")

    # -- 3. acquisition ----------------------------------------------------
    out += titre("3. L'acquisition")
    out += tableau(
        ["Grandeur", "Valeur", "Base"],
        [
            ["Commandes de réachat / semaine", num(p.commandes_reachat_semaine, 0),
             f"{taux(o.part_commandes_reachat, 1)} des commandes"],
            ["Nouvelles commandes / semaine", num(p.nouvelles_commandes_semaine, 0),
             "le solde"],
            ["Nouveaux clients / jour", num(p.nouveaux_clients_jour, 0),
             "1 première commande = 1 client"],
            ["Nouveaux clients / mois", num(p.nouveaux_clients_mois, 0), ""],
            ["Dépense pub HT / jour", eur(p.pub_jour), "CA TTC ÷ MER ÷ 7"],
            ["Dépense pub HT / semaine", eur(p.pub_semaine), ""],
            ["Dépense pub HT / mois", eur(p.pub_mois), ""],
            ["Pub en % du CA HT", taux(p.pub_pct_ht, 1),
             f"= {num(1 + o.tva, 2)} ÷ {num(o.mer, 2)}"],
            ["nCAC impliqué", eur(p.ncac, 2), "pub ÷ nouveaux clients"],
            ["Contribution 1ʳᵉ commande", eur(p.contribution_premiere_commande, 2),
             "AOV HT × marge brute"],
            ["Marge à la 1ʳᵉ commande", eur(p.marge_premiere_commande, 2),
             "contribution − nCAC"],
            ["MER seuil (CM3 = 0)", num(p.mer_seuil_cm3, 2),
             f"= {num(1 + o.tva, 2)} ÷ marge brute"],
        ],
        gauche=[0, 2],
    )
    add("")
    if p.marge_premiere_commande < 0:
        add(f"La première commande perd {eur(-p.marge_premiere_commande, 2)} : ce plan n'est pas financé par la")
        add("première vente, il est financé par le réachat. Si la courbe de réachat ne")
        add("tient pas au volume cible, l'objectif devient un mécanisme de ruine.")
    else:
        add(f"La première commande dégage {eur(p.marge_premiere_commande, 2)} : l'acquisition s'autofinance dès")
        add("la première vente. C'est rare, et c'est un actif.")
    add("")
    if o.mer >= p.mer_seuil_cm3:
        add(f"MER visé {num(o.mer, 2)} contre un seuil CM3 à {num(p.mer_seuil_cm3, 2)}, soit "
            f"{taux(o.mer / p.mer_seuil_cm3 - 1, 1)} au-dessus de la ligne")
        add("de flottaison. Ce seuil ne couvre que les coûts variables : les frais")
        add("fixes, eux, restent à payer au-dessus.")
    else:
        add(f"MER visé {num(o.mer, 2)} contre un seuil CM3 à {num(p.mer_seuil_cm3, 2)}, soit "
            f"{taux(1 - o.mer / p.mer_seuil_cm3, 1)} SOUS la ligne de")
        add("flottaison. À ce MER, chaque euro de CA supplémentaire détruit de la marge.")

    # -- 4. le funnel media ------------------------------------------------
    out += titre("4. Le funnel média — ce qu'il faut acheter")
    out += tableau(
        ["Étage", "Par jour", "Base"],
        [
            ["Impressions à acheter", num(p.impressions_jour, 0),
             f"clics ÷ {taux(o.taux_clic, 2)} de clic"],
            ["Clics", num(p.clics_jour, 0), f"sessions ÷ {taux(o.taux_arrivee, 0)} d'arrivée"],
            ["Sessions payantes", num(p.sessions_payantes_jour, 0),
             f"nouveaux clients ÷ {taux(o.taux_conversion, 2)}"],
            ["Nouveaux clients", num(p.nouveaux_clients_jour, 0), "l'exigence de § 3"],
            ["Sessions du site, toutes sources", num(p.sessions_site_jour, 0),
             "commandes totales ÷ conversion"],
        ],
        gauche=[0, 2],
    )
    add("")
    out += tableau(
        ["Confrontation au budget", "Valeur", "Lecture"],
        [
            ["Coût média impliqué / jour", eur(p.cout_media_jour),
             f"impressions × CPM {eur(o.cpm, 2)}"],
            ["Budget autorisé par le MER / jour", eur(p.pub_jour), "CA TTC ÷ MER ÷ 7"],
            ["Écart", eur_signe(p.ecart_media_jour),
             "> 0 : le funnel coûte trop cher"],
            ["CPM maximal soutenable", eur(p.cpm_maximal, 2), "à CTR et conversion tenus"],
            ["Conversion requise au CPM visé", taux(p.conversion_requise, 2),
             "à CPM et CTR tenus"],
            ["CPC impliqué", eur(p.cpc, 2), "CPM ÷ 1 000 ÷ taux de clic"],
            ["Coût par session", eur(p.cout_par_session, 2), "CPC ÷ taux d'arrivée"],
            ["CAC du funnel", eur(p.cac_du_funnel, 2), "coût session ÷ conversion"],
        ],
        gauche=[0, 2],
    )
    add("")
    marge_rel = -p.ecart_media_jour / p.pub_jour
    if p.ecart_media_jour <= 0:
        add(f"Le funnel referme, avec {taux(marge_rel, 1)} de marge sur le budget. Les trois")
        add("hypothèses média (CPM, taux de clic, conversion) et le MER visé sont")
        add("compatibles entre eux. C'est la condition minimale d'un plan sérieux.")
    else:
        add(f"Le funnel ne referme pas : il manque {eur(p.ecart_media_jour)} par jour, soit")
        add(f"{taux(p.ecart_media_jour / p.pub_jour, 1)} du budget. Ton MER de {num(o.mer, 2)} et tes hypothèses média")
        add("se contredisent. Trois sorties, et une seule à la fois : baisser le CPM à")
        add(f"{eur(p.cpm_maximal, 2)}, monter la conversion à {taux(p.conversion_requise, 2)}, ou accepter un MER plus bas.")

    # -- 5. la machine creative -------------------------------------------
    out += titre("5. La machine créative")
    out += tableau(
        ["Grandeur", "Valeur", "Base"],
        [
            ["Budget de test HT / semaine", eur(p.budget_test_semaine),
             f"{taux(o.part_budget_test, 0)} de la dépense pub"],
            ["Concepts nouveaux testés / semaine", num(p.concepts_semaine, 1),
             f"÷ {eur(o.budget_par_concept)} par concept"],
            ["Concepts / jour ouvré", num(p.concepts_jour_ouvre, 1), "à produire ET à juger"],
            ["Gagnants attendus / semaine", num(p.gagnants_semaine, 1),
             f"× {taux(o.taux_reussite_concepts, 1)} de réussite"],
            ["Gagnants en rotation", num(p.gagnants_en_rotation, 0),
             f"× {num(o.duree_vie_concept_semaines, 1)} sem. de durée de vie"],
            ["Assets produits / mois", num(p.assets_mois, 0),
             f"× {o.variations_par_concept} variations"],
            ["Budget de test non converti / sem.", eur(p.budget_perdu_semaine),
             "le prix du test, pas une perte"],
        ],
        gauche=[0, 2],
    )
    add("")
    add(f"Voilà le vrai goulot : {num(p.concepts_semaine, 0)} concepts nouveaux par semaine, dont "
        f"{num(p.gagnants_semaine, 1)} survivront.")
    add(f"Ce n'est pas un budget, c'est une chaîne de production : {num(p.assets_mois, 0)} assets par")
    add("mois à briefer, tourner, monter, poster et juger, et un rituel de décision")
    add("capable de tuer neuf concepts sur dix sans discuter.")

    # -- 6. les operations -------------------------------------------------
    out += titre("6. Les opérations — colis et service client")
    out += tableau(
        ["Grandeur", "Par jour calendaire", "Par jour ouvré"],
        [
            ["Commandes à expédier", num(p.commandes_jour, 0), num(p.commandes_jour_ouvre, 0)],
            ["Unités à prélever", num(p.unites_jour, 0), num(p.unites_jour_ouvre, 0)],
            ["Tickets SAV", num(p.tickets_jour, 0), num(p.tickets_jour_ouvre, 0)],
        ],
        gauche=[0],
    )
    add("")
    out += tableau(
        ["Ressource", "Nombre", "Base"],
        [
            ["Personnes en préparation", num(p.preparateurs, 1),
             f"÷ {num(o.commandes_par_preparateur_jour)} commandes / personne / jour"],
            ["ETP de service client", num(p.etp_sav, 1),
             f"÷ {num(o.tickets_par_agent_jour)} tickets / agent / jour"],
        ],
        gauche=[0, 2],
    )
    add("")
    add(f"Les {num(p.preparateurs, 1)} personnes en préparation ne sont pas dans ta masse salariale si")
    add("ta logistique est externalisée : leur coût est déjà dans la ligne de coût")
    add("variable « logistique ». Les compter deux fois est une erreur classique de")
    add("modèle. Les agents de service client, eux, sont dans la structure.")

    # -- 7. la structure ---------------------------------------------------
    out += titre("7. La structure et ce qu'elle coûte")
    out += tableau(
        ["Grandeur", "Valeur", "Base"],
        [
            ["ETP total impliqué", num(p.etp_total, 1),
             f"CA HT annuel ÷ {eur(o.ca_ht_annuel_par_etp)} par ETP"],
            ["dont service client", num(p.etp_sav, 1), "calculé en § 6"],
            ["dont autres fonctions", num(p.etp_autres, 1),
             "créa, acquisition, produit, supply, data, direction"],
            ["Masse salariale HT / mois", eur(p.masse_salariale_mois),
             f"× {eur(o.cout_etp_annuel)} chargés / ETP / an"],
            ["Masse salariale HT / an", eur(p.masse_salariale_an), ""],
            ["En % du CA HT", taux(p.masse_pct_ca_ht, 1), ""],
            ["CM3 / mois (marge − pub)", eur(p.cm3_mois), "avant frais fixes"],
            ["Reste après salaires", eur(p.reste_apres_salaires),
             "avant loyers, outils, honoraires"],
        ],
        gauche=[0, 2],
    )
    add("")
    a_recruter = p.etp_total - (a.etp or 0.0)
    add(f"Il y a {num(a_recruter, 0)} ETP à recruter"
        + (f" depuis les {num(a.etp, 0)} d'aujourd'hui." if a.etp is not None else " depuis zéro.")
        + " À un rythme")
    add(f"soutenable de deux recrutements nets par mois, cela prend {num(a_recruter / 2, 0)} mois —")
    add("avant même de compter les six mois de montée en compétence de chacun.")

    # -- 8. le cash --------------------------------------------------------
    out += titre("8. Le cash — BFR et capital de croissance")
    out += tableau(
        ["Poste", "Montant", "Base"],
        [
            ["Stock immobilisé", eur(p.stock_immobilise),
             f"COGS mensuel × {o.jours_stock} j ÷ 30"],
            ["Encaissements en attente", eur(p.creances),
             f"CA TTC × {o.delai_encaissement} j ÷ 30"],
            ["Avance publicitaire", eur(p.avance_pub),
             f"pub × {o.delai_pub} j ÷ 30"],
            ["− Dettes fournisseurs", eur(-p.dettes_fournisseurs),
             f"COGS × {o.delai_fournisseur} j ÷ 30"],
            ["BFR à l'objectif", eur(p.bfr), f"soit {num(p.bfr_jours_ca, 0)} jours de CA TTC"],
        ],
        gauche=[0, 2],
    )
    add("")
    bfr_actuel = a.bfr
    delta_bfr = p.bfr - (bfr_actuel or 0.0)
    capital = p.capital_de_croissance(bfr_actuel)
    out += tableau(
        ["Capital de croissance", "Montant", "Base"],
        [
            ["BFR à l'objectif", eur(p.bfr), ""],
            ["− BFR déjà financé", eur(-(bfr_actuel or 0.0)),
             "situation actuelle" if bfr_actuel is not None else "non fourni — supposé nul"],
            ["Besoin incrémental de BFR", eur(delta_bfr), ""],
            ["Coussin de sécurité", eur(p.coussin),
             f"{num(o.coussin_semaines, 0)} semaines de dépense pub"],
            ["Capital à mobiliser", eur(capital), ""],
            ["En mois de CM3", num(capital / p.cm3_mois, 1) if p.cm3_mois > 0 else "∞",
             "durée d'autofinancement, hors frais fixes"],
        ],
        gauche=[0, 2],
    )
    add("")
    add(f"Chaque tranche de {eur(100_000)} de CA TTC mensuel supplémentaire immobilise")
    add(f"{eur(p.bfr / p.ca_ttc_mois * 100_000)} de cash avant d'en rendre le premier euro. C'est ce décalage,")
    add("et non l'absence de rentabilité, qui tue la majorité des marques en croissance.")

    # -- 9. ce qui doit etre vrai -----------------------------------------
    out += titre("9. Ce qui doit être vrai")
    lignes = [e.ligne() for e in exigences(p, a)]
    out += tableau(
        ["Exigence", "Cible", "Aujourd'hui", "Écart", "Facteur"],
        lignes, gauche=[0, 4],
    )
    add("")
    if a.vide:
        add("Aucune situation actuelle fournie : la colonne « Aujourd'hui » est vide.")
        add("Relance avec --actuel-ca, --actuel-aov, --actuel-mer et les autres options")
        add("--actuel-* pour obtenir les écarts chiffrés. Sans elles, cet outil décrit")
        add("une exigence ; avec elles, il décrit un chemin.")
    else:
        renseignes = [e for e in exigences(p, a) if e.actuel is not None]
        durs = sorted(
            [e for e in renseignes
             if e.genre in ("montant", "nombre") and e.actuel and e.sens == "hausse"],
            key=lambda e: -(e.cible / e.actuel),
        )[:3]
        add("Les trois multiplications les plus dures de ce plan :")
        for e in durs:
            add(f"  · {e.nom} : ×{num(e.cible / e.actuel, 2)}")
        add("")
        add("Un plan n'échoue jamais sur sa moyenne. Il échoue sur sa ligne la plus")
        add("tendue. Commence par celle-là, et refais tourner cet outil quand elle a bougé.")

    add("")
    add("─" * 78)
    add("Rappel : cet outil traduit un objectif, il ne le valide pas. Il suppose")
    add("que le panier, la marge, le MER et le taux de réachat visés tiennent au")
    add("volume cible — ce qui est précisément l'hypothèse la plus fragile.")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# 6. LES DEFAUTS ET LE MODE DEMO
# ---------------------------------------------------------------------------

def _p(indice: int, champ: str, cle_repli: str):
    """Lit une hypothese canonique via modele_nora, avec repli sur REPLI."""
    if CANONIQUE_DISPONIBLE:
        return getattr(PALIERS[indice], champ)
    return REPLI[cle_repli]


def objectif_demo() -> Objectif:
    """1 M€ TTC / semaine, avec les hypothèses de NØRA au palier P5.

    Les quatorze entrees principales viennent des chiffres canoniques § 2,
    § 2.1, § 2.4, § 2.5 et § 6. Les parametres secondaires sont des hypotheses
    propres a cet outil, declarees comme telles dans le rapport.
    """
    if CANONIQUE_DISPONIBLE:
        p5 = PALIERS[4]
        t5 = TRESO["P5"]
        c5 = CREA["P5"]
        aov = p5.aov_blended_ttc
        marge = p5.taux_marge_brute
        mer = p5.mer
        part_reachat = p5.part_commandes_repeat
        cogs = p5.cogs_pct
        etp = p5.etp
        ca_par_etp = p5.ca_par_etp
        budget_concept = c5.budget_par_concept_test
        reussite = c5.taux_de_reussite
        variations = c5.variations_par_concept
        duree_vie = c5.duree_de_vie_semaines
        part_test = c5.part_budget_test
        stock_j, dso, dpo, pub_j = (t5.jours_stock, t5.delai_encaissement,
                                    t5.delai_fournisseur, t5.delai_pub)
    else:  # pragma: no cover - chemin de repli
        aov, marge, mer = REPLI["p5_aov"], REPLI["p5_marge"], REPLI["p5_mer"]
        part_reachat, cogs, etp = REPLI["p5_part_reachat"], REPLI["p5_cogs"], REPLI["p5_etp"]
        ca_par_etp = REPLI["p5_ca_sem_ttc"] * 52 / 1.2 / etp
        budget_concept, reussite = REPLI["p5_budget_concept"], REPLI["p5_reussite"]
        variations, duree_vie, part_test = REPLI["p5_variations"], REPLI["p5_duree_vie"], 0.15
        stock_j, dso, dpo, pub_j = (REPLI["p5_stock_j"], REPLI["p5_dso"],
                                    REPLI["p5_dpo"], REPLI["p5_pub_j"])

    return Objectif(
        ca_ttc_semaine=1_000_000.0,
        aov_ttc=aov,
        taux_marge_brute=marge,
        mer=mer,
        part_commandes_reachat=part_reachat,
        # Hypotheses media propres a l'outil, calibrees pour que le funnel
        # referme au MER canonique de 2,90 : voir § 4 du rapport.
        cpm=9.70,
        taux_clic=0.0120,
        taux_conversion=0.0225,
        part_budget_test=part_test,
        budget_par_concept=budget_concept,
        taux_reussite_concepts=reussite,
        tickets_sav_par_commande=0.12,
        commandes_par_preparateur_jour=250.0,
        ca_ht_annuel_par_etp=ca_par_etp,
        variations_par_concept=variations,
        duree_vie_concept_semaines=duree_vie,
        cogs_pct=cogs,
        jours_stock=stock_j,
        delai_encaissement=dso,
        delai_fournisseur=dpo,
        delai_pub=pub_j,
    )


def actuel_demo() -> Actuel:
    """La situation de depart : le palier P3 des chiffres canoniques.

    On ne renseigne QUE ce qui est canonique. Le taux de conversion, le CPM,
    la productivite logistique et le ratio de tickets SAV de P3 ne figurent pas
    dans chiffres-canoniques.md : ils restent vides, et le rapport l'affiche.
    """
    if CANONIQUE_DISPONIBLE:
        p3 = PALIERS[2]
        return Actuel(
            ca_ttc_semaine=p3.ca_semaine_ttc,
            aov_ttc=p3.aov_blended_ttc,
            mer=p3.mer,
            taux_marge_brute=p3.taux_marge_brute,
            part_commandes_reachat=p3.part_commandes_repeat,
            concepts_semaine=CREA["P3"].concepts_testes_semaine,
            etp=p3.etp,
            bfr=TRESO["P3"].bfr,
        )
    return Actuel(  # pragma: no cover - chemin de repli
        ca_ttc_semaine=REPLI["p3_ca_sem_ttc"], aov_ttc=REPLI["p3_aov"],
        mer=REPLI["p3_mer"], taux_marge_brute=REPLI["p3_marge"],
        part_commandes_reachat=REPLI["p3_part_reachat"],
        concepts_semaine=REPLI["p3_concepts"], etp=REPLI["p3_etp"],
        bfr=REPLI["p3_bfr"],
    )


def demo() -> str:
    entete = [
        "Mode démonstration. Objectif : 1 000 000 € TTC par semaine, avec les",
        "hypothèses de NØRA au palier P5 (chiffres canoniques § 2, § 2.1, § 2.4,",
        "§ 2.5, § 4 et § 6). Situation actuelle comparée : le palier P3.",
        "NØRA est une marque fictive ; le modèle est calibré sur des ordres de",
        "grandeur sectoriels, ce ne sont les comptes d'aucune entreprise réelle.",
        "Note d'arrondi : le § 9 canonique affiche 1 984 commandes par jour sur un",
        "panier de 72,00 € ; au panier mixte réel de P5 (71,98 €) le calcul donne",
        "1 984,7. Lance --verifier pour le détail des écarts avec le canonique.",
    ]
    if not CANONIQUE_DISPONIBLE:  # pragma: no cover
        entete.append("modele_nora.py introuvable : hypothèses lues dans le repli local.")
    return rapport(objectif_demo(), actuel_demo(), entete)


# ---------------------------------------------------------------------------
# 7. VERIFICATION CONTRE LES CHIFFRES CANONIQUES
# ---------------------------------------------------------------------------

def valeurs_du_plan(p: Plan) -> dict:
    return {
        "CA TTC / mois": p.ca_ttc_mois,
        "CA TTC / an": p.ca_ttc_an,
        "Commandes / jour": p.commandes_jour,
        "Dépense pub / jour (base semaine)": p.pub_jour,
        "Dépense pub / jour (base mois)": p.pub_mois / 30.4,
        "Dépense pub / semaine": p.pub_semaine,
        "Dépense pub / mois": p.pub_mois,
        "Nouveaux clients / mois": p.nouveaux_clients_mois,
        "nCAC": p.ncac,
        "Budget de test créatif / semaine": p.budget_test_semaine,
        "Concepts testés / semaine": p.concepts_semaine,
        "Gagnants / semaine": p.gagnants_semaine,
        "Gagnants en rotation": p.gagnants_en_rotation,
        "Assets produits / mois": p.assets_mois,
        "ETP total": p.etp_total,
        "BFR": p.bfr,
        "BFR en jours de CA TTC": p.bfr_jours_ca,
    }


def verifier() -> str:
    """Confronte le plan de demonstration aux chiffres canoniques publies."""
    p = Plan(objectif_demo())
    obtenu = valeurs_du_plan(p)
    out: List[str] = []
    add = out.append
    add("=" * 78)
    add("VÉRIFICATION DU MODE DÉMO CONTRE LES CHIFFRES CANONIQUES")
    add("=" * 78)
    add("")
    add("Objectif testé : 1 000 000 € TTC / semaine, hypothèses NØRA au palier P5.")
    add("Le palier P5 canonique fait 999 968 € TTC / semaine : un écart de départ de")
    add("0,003 % est donc attendu sur toutes les grandeurs proportionnelles au CA.")
    add("")

    lignes = []
    pire = 0.0
    hors = 0
    for libelle, cible, section, tol in CANON:
        val = obtenu[libelle]
        rel = (val - cible) / cible if cible else 0.0
        pire = max(pire, abs(rel))
        ok = abs(rel) <= tol
        hors += 0 if ok else 1
        d = 2 if abs(cible) < 100 else 0
        lignes.append([libelle, section, num(cible, d), num(val, d),
                       taux(rel, 3), "ok" if ok else "ÉCART"])
    out += tableau(
        ["Grandeur", "Source", "Canonique", "Plan objectif", "Écart", "Verdict"],
        lignes, gauche=[0, 1, 5],
    )
    add("")
    add(f"Écart relatif maximal : {taux(pire, 3)} sur {len(CANON)} grandeurs contrôlées, "
        f"{hors} hors tolérance.")
    add("")
    add("Écarts résiduels assumés, et leur cause :")
    add("")
    add("  1. Dépense pub / jour. Les chiffres canoniques donnent deux valeurs :")
    add("     49 261 € au § 9 (semaine ÷ 7) et 49 151 € au § 5 (mois ÷ 30,4).")
    add("     Les deux diffèrent de 0,22 % parce que 52 semaines font 364 jours et")
    add("     non 365. Cet outil calcule tout à partir de la semaine — un entrepôt")
    add("     et un compte publicitaire vivent en semaines, pas en douzièmes")
    add("     d'année — et reproduit donc le § 9 à l'euro près. La ligne « base")
    add("     mois » ci-dessus montre qu'il reproduit aussi le § 5 quand on lui")
    add("     applique le même diviseur.")
    add("")
    add("  2. Commandes / jour. Le § 9 arrondit à 1 984 sur un panier de 72,00 € ;")
    add("     l'AOV mixte réel de P5 est 71,98 €, ce qui donne 1 984,7. L'écart de")
    add("     0,7 commande par jour est un arrondi d'affichage du tableau canonique.")
    add("")
    add("  3. Concepts et gagnants. Le § 6 affiche des entiers (57, 5,2, 23) là où")
    add("     le calcul donne 57,5, 5,17 et 23,3. Écart d'arrondi, pas de formule.")
    add("")
    add("Les hypothèses média (CPM 9,70 €, taux de clic 1,20 %, conversion 2,25 %)")
    add("et les hypothèses opérationnelles (0,12 ticket SAV par commande,")
    add("250 commandes par préparateur et par jour, 1,8 unité par commande,")
    add("72 000 € chargés par ETP) ne figurent PAS dans les chiffres canoniques.")
    add("Ce sont des hypothèses propres à cet outil. Elles sont calibrées pour")
    add("refermer le funnel au MER canonique de 2,90, et rien de plus.")
    add("")
    masse = p.masse_salariale_mois
    add(f"Contrôle de vraisemblance : la masse salariale estimée ({eur(masse)} / mois)")
    add(f"représente {taux(masse / 360_000, 1)} des frais fixes canoniques du palier P5")
    add("(360 000 € / mois, § 2.5). Le solde couvre loyers, outils, honoraires et")
    add("prestations — un ratio salaires/fixes de l'ordre de 60 à 70 % est cohérent.")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# 8. LIGNE DE COMMANDE
# ---------------------------------------------------------------------------

DEFAUTS = dict(
    objectif=1_000_000.0, aov=71.98, marge=0.6145, mer=2.90, part_reachat=0.38,
    cpm=9.70, ctr=0.0120, conversion=0.0225, part_test=0.15, budget_concept=900.0,
    taux_reussite=0.09, tickets_commande=0.12, commandes_preparateur=250.0,
    ca_par_etp=1_140_315.0,
)


def construire_parseur() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="plan_objectif.py",
        description="Traduit un objectif de CA TTC hebdomadaire en plan opérationnel : "
                    "commandes, impressions, concepts créatifs, colis, ETP, cash.",
        epilog="Les taux s'écrivent en pourcentage (« 61,45 » = 61,45 %). "
               "Les montants acceptent la virgule, l'espace, « k » et « M ».",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    g = p.add_argument_group("modes")
    g.add_argument("--demo", action="store_true",
                   help="1 M€/semaine avec les hypothèses NØRA au palier P5, comparé à P3")
    g.add_argument("--verifier", action="store_true",
                   help="confronte le mode démo aux chiffres canoniques et liste les écarts")

    g = p.add_argument_group("objectif et économie (les 14 entrées principales)")
    g.add_argument("--objectif", type=lire_montant, default=DEFAUTS["objectif"],
                   metavar="€", help="objectif de CA TTC par semaine")
    g.add_argument("--aov", type=lire_nombre, default=DEFAUTS["aov"],
                   metavar="€", help="panier moyen TTC visé")
    g.add_argument("--marge", type=lire_taux, default=DEFAUTS["marge"],
                   metavar="%", help="taux de marge brute (CM2, %% du CA HT)")
    g.add_argument("--mer", type=lire_nombre, default=DEFAUTS["mer"],
                   metavar="N", help="MER visé (CA TTC ÷ dépense publicitaire)")
    g.add_argument("--part-reachat", type=lire_taux, default=DEFAUTS["part_reachat"],
                   metavar="%", help="part des commandes passées par un client déjà acquis")
    g.add_argument("--cpm", type=lire_nombre, default=DEFAUTS["cpm"],
                   metavar="€", help="CPM HT moyen acheté")
    g.add_argument("--ctr", type=lire_taux, default=DEFAUTS["ctr"],
                   metavar="%", help="taux de clic moyen")
    g.add_argument("--conversion", type=lire_taux, default=DEFAUTS["conversion"],
                   metavar="%", help="taux de conversion du site")
    g.add_argument("--part-test", type=lire_taux, default=DEFAUTS["part_test"],
                   metavar="%", help="part de la dépense pub consacrée au test créatif")
    g.add_argument("--budget-concept", type=lire_montant, default=DEFAUTS["budget_concept"],
                   metavar="€", help="budget HT minimal pour juger un concept")
    g.add_argument("--taux-reussite", type=lire_taux, default=DEFAUTS["taux_reussite"],
                   metavar="%", help="part des concepts testés qui deviennent scalables")
    g.add_argument("--tickets-commande", type=lire_nombre, default=DEFAUTS["tickets_commande"],
                   metavar="N", help="tickets SAV par commande")
    g.add_argument("--commandes-preparateur", type=lire_nombre,
                   default=DEFAUTS["commandes_preparateur"],
                   metavar="N", help="commandes traitées par personne et par jour en logistique")
    g.add_argument("--ca-par-etp", type=lire_montant, default=DEFAUTS["ca_par_etp"],
                   metavar="€", help="CA HT annuel par ETP")

    g = p.add_argument_group("paramètres secondaires")
    g.add_argument("--tva", type=lire_taux, default=TVA, metavar="%")
    g.add_argument("--taux-arrivee", type=lire_taux, default=0.90, metavar="%",
                   help="part des clics qui deviennent des sessions")
    g.add_argument("--jours-ouvres", type=int, default=5, metavar="N")
    g.add_argument("--heures-jour", type=lire_nombre, default=8.0, metavar="N")
    g.add_argument("--unites-commande", type=lire_nombre, default=1.8, metavar="N")
    g.add_argument("--variations", type=int, default=5, metavar="N",
                   help="déclinaisons produites par concept testé")
    g.add_argument("--duree-vie", type=lire_nombre, default=4.5, metavar="SEM",
                   help="durée de vie d'un concept gagnant, en semaines")
    g.add_argument("--tickets-agent", type=lire_nombre, default=50.0, metavar="N")
    g.add_argument("--cout-etp", type=lire_montant, default=72_000.0, metavar="€",
                   help="coût employeur HT chargé par ETP et par an")
    g.add_argument("--cogs", type=lire_taux, default=0.145, metavar="%")
    g.add_argument("--jours-stock", type=int, default=105, metavar="J")
    g.add_argument("--dso", type=int, default=3, metavar="J")
    g.add_argument("--dpo", type=int, default=60, metavar="J")
    g.add_argument("--delai-pub", type=int, default=21, metavar="J")
    g.add_argument("--coussin", type=lire_nombre, default=4.0, metavar="SEM",
                   help="semaines de dépense pub gardées en coussin de sécurité")

    g = p.add_argument_group("situation actuelle (optionnelle, pour le § 9)")
    g.add_argument("--actuel-ca", type=lire_montant, default=None, metavar="€",
                   help="CA TTC par semaine aujourd'hui")
    g.add_argument("--actuel-aov", type=lire_nombre, default=None, metavar="€")
    g.add_argument("--actuel-mer", type=lire_nombre, default=None, metavar="N")
    g.add_argument("--actuel-marge", type=lire_taux, default=None, metavar="%")
    g.add_argument("--actuel-part-reachat", type=lire_taux, default=None, metavar="%")
    g.add_argument("--actuel-conversion", type=lire_taux, default=None, metavar="%")
    g.add_argument("--actuel-cpm", type=lire_nombre, default=None, metavar="€")
    g.add_argument("--actuel-concepts", type=lire_nombre, default=None, metavar="N",
                   help="concepts créatifs nouveaux testés par semaine aujourd'hui")
    g.add_argument("--actuel-preparateur", type=lire_nombre, default=None, metavar="N")
    g.add_argument("--actuel-tickets", type=lire_nombre, default=None, metavar="N")
    g.add_argument("--actuel-etp", type=lire_nombre, default=None, metavar="N")
    g.add_argument("--actuel-bfr", type=lire_montant, default=None, metavar="€")
    return p


def objectif_depuis_args(ns: argparse.Namespace) -> Objectif:
    return Objectif(
        ca_ttc_semaine=ns.objectif, aov_ttc=ns.aov, taux_marge_brute=ns.marge,
        mer=ns.mer, part_commandes_reachat=ns.part_reachat, cpm=ns.cpm,
        taux_clic=ns.ctr, taux_conversion=ns.conversion,
        part_budget_test=ns.part_test, budget_par_concept=ns.budget_concept,
        taux_reussite_concepts=ns.taux_reussite,
        tickets_sav_par_commande=ns.tickets_commande,
        commandes_par_preparateur_jour=ns.commandes_preparateur,
        ca_ht_annuel_par_etp=ns.ca_par_etp,
        tva=ns.tva, taux_arrivee=ns.taux_arrivee, jours_ouvres=ns.jours_ouvres,
        heures_par_jour=ns.heures_jour, unites_par_commande=ns.unites_commande,
        variations_par_concept=ns.variations,
        duree_vie_concept_semaines=ns.duree_vie,
        tickets_par_agent_jour=ns.tickets_agent, cout_etp_annuel=ns.cout_etp,
        cogs_pct=ns.cogs, jours_stock=ns.jours_stock,
        delai_encaissement=ns.dso, delai_fournisseur=ns.dpo,
        delai_pub=ns.delai_pub, coussin_semaines=ns.coussin,
    )


def actuel_depuis_args(ns: argparse.Namespace) -> Actuel:
    return Actuel(
        ca_ttc_semaine=ns.actuel_ca, aov_ttc=ns.actuel_aov, mer=ns.actuel_mer,
        taux_marge_brute=ns.actuel_marge,
        part_commandes_reachat=ns.actuel_part_reachat,
        taux_conversion=ns.actuel_conversion, cpm=ns.actuel_cpm,
        concepts_semaine=ns.actuel_concepts,
        commandes_par_preparateur_jour=ns.actuel_preparateur,
        tickets_sav_par_commande=ns.actuel_tickets,
        etp=ns.actuel_etp, bfr=ns.actuel_bfr,
    )


def main(argv: Optional[List[str]] = None) -> int:
    ns = construire_parseur().parse_args(argv)

    if ns.verifier:
        print(verifier())
        return 0
    if ns.demo:
        print(demo())
        return 0

    o = objectif_depuis_args(ns)
    if o.ca_ttc_semaine <= 0 or o.aov_ttc <= 0 or o.mer <= 0:
        print("Objectif, panier moyen et MER doivent être strictement positifs.",
              file=sys.stderr)
        return 2
    if not (0 <= o.part_commandes_reachat < 1):
        print("La part de commandes en réachat doit être dans [0 % ; 100 %[.",
              file=sys.stderr)
        return 2
    if o.taux_conversion <= 0 or o.taux_clic <= 0 or o.cpm <= 0:
        print("CPM, taux de clic et taux de conversion doivent être positifs.",
              file=sys.stderr)
        return 2
    # Tout taux se saisit en pourcentage (« 2,25 » = 2,25 %). Une valeur hors
    # de ]0 % ; 100 %] est une saisie mal exprimee, pas une hypothese audacieuse.
    for nom, valeur in (("--marge", o.taux_marge_brute), ("--ctr", o.taux_clic),
                        ("--conversion", o.taux_conversion),
                        ("--part-test", o.part_budget_test),
                        ("--taux-reussite", o.taux_reussite_concepts),
                        ("--taux-arrivee", o.taux_arrivee), ("--cogs", o.cogs_pct),
                        ("--tva", o.tva)):
        if not (0 < valeur <= 1):
            print(f"{nom} doit être un pourcentage dans ]0 % ; 100 %] "
                  f"(reçu : {taux(valeur, 2)}).", file=sys.stderr)
            return 2

    print(rapport(o, actuel_depuis_args(ns)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
