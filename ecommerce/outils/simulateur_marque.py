#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulateur de marque — le coeur pedagogique du cursus e-commerce.

Tu crees une marque DTC, tu la pilotes mois par mois, et tu vois les
consequences chiffrees de chaque decision — tresorerie comprise.

L'objectif du cursus : 1 000 000 EUR de CA TTC par semaine avec un EBITDA
qui tient (>= 15 % du CA HT), soutenu 3 mois consecutifs. La partie est
perdue des que la tresorerie passe sous zero.

Le simulateur est ENTIEREMENT DETERMINISTE a graine fixee : la meme graine
et les memes decisions produisent les memes chiffres au centime. C'est ce
qui rend les exercices corrigeables.

Usage
-----
    python3 simulateur_marque.py --comparer
    python3 simulateur_marque.py --auto equilibree --categorie soin_cheveux
    python3 simulateur_marque.py --interactif
    python3 simulateur_marque.py --scenario scenarios/S01-la-discipline-creative.json
    python3 simulateur_marque.py --verifier
    python3 simulateur_marque.py --auto equilibree --rapport /tmp/partie.md

Python 3.9+. Bibliotheque standard uniquement. Aucune dependance.
Conventions de sortie : francais, virgule decimale, espace avant % et EUR,
tout montant marque TTC ou HT. Voir ecommerce/CHARTE.md § 5.
Reference chiffree : ecommerce/donnees/chiffres-canoniques.md
"""

from __future__ import annotations

import argparse
import json
import math
import os
import random
import sys
from dataclasses import dataclass, field, replace
from typing import Dict, List, Optional, Tuple

# ===========================================================================
# 0. CONSTANTES DU MODELE — tout ce qui pilote le jeu est declare ici
# ===========================================================================

TVA = 0.20                      # taux moyen pondere Europe de l'Ouest
HORIZON_DEFAUT = 60             # mois
OBJECTIF_CA_TTC_SEMAINE = 1_000_000.0
OBJECTIF_EBITDA_PCT = 0.15
MOIS_CONSECUTIFS_VICTOIRE = 3
SEMAINES_PAR_MOIS = 4.3333333333

# --- acquisition -----------------------------------------------------------
EXPOSANT_RENDEMENT_PUB = 0.72   # b : clients = A x budget^b. CAC marginal = CAC / b
A_BASE = 0.82                   # calibre sur les paliers P1/P2/P5 canoniques
CPM_REFERENCE = 14.0
EXPOSANT_CPM = 0.60
EXPOSANT_PRIX = 0.85            # elasticite du nombre de clients au prix
EXPOSANT_SATURATION = 0.80
SATURATION_MAX = 0.92
MARQUE_PLAFOND = 0.55           # halo de marque : jusqu'a +55 % de clients a budget egal
MARQUE_DEMI_VIE_CLIENTS = 60_000
MATURITE_PLANCHER = 0.72        # penalite de demarrage (signal algorithmique pauvre)
MATURITE_CLIENTS_CIBLE = 5_000

# --- machine creative ------------------------------------------------------
COUT_TEST_ANCRE = 259.0         # EUR par concept teste au budget d'ancrage
BUDGET_ANCRE_TEST = 104_636.0   # budget mensuel du palier P2 canonique
EXPOSANT_COUT_TEST = 0.47
COUT_TEST_MIN = 250.0
COUT_TEST_MAX = 900.0
TAUX_REUSSITE_PETIT = 0.12      # 12 % de gagnants a petit budget
TAUX_REUSSITE_GROS = 0.09       # 9 % a gros budget (canoniques § 6)
BUDGET_REUSSITE_BASSE = 1_500_000.0
DUREE_VIE_GAGNANT_MIN = 4.0     # mois
DUREE_VIE_GAGNANT_MAX = 6.0
EXPOSANT_FATIGUE = 1.8
GAGNANTS_REFERENCE = 8.0        # gagnants requis au budget d'ancrage
EXPOSANT_GAGNANTS_REFERENCE = 0.35
QUALITE_MIN = 0.55
QUALITE_MAX = 1.45
GAGNANTS_AU_LANCEMENT = 2
MALUS_RUPTURE_CREA = 0.15       # apprentissage casse par une rupture de stock
DECROISSANCE_MALUS_CREA = 0.82

# --- panier et offre -------------------------------------------------------
MULT_OFFRE_BASE = 1.10
MULT_OFFRE_PLAFOND = 1.45
OFFRE_DEMI_VIE = 90_000.0       # EUR cumules d'investissement offre

# --- retention -------------------------------------------------------------
TAUX_BASE_REACHAT = 0.40
REACHAT_FORME = 1.7             # forme de la bosse du calendrier de consommation
REACHAT_FIDELITE_PLANCHER = 0.30
REACHAT_FIDELITE_DECROISSANCE = 0.93
REACHAT_QUEUE_POIDS = 0.45      # segment fidele, quasi-abonne
REACHAT_QUEUE_DECROISSANCE = 0.97
RETENTION_GAIN_MAX = 0.35
RETENTION_DEMI_VIE_MIN = 50_000.0
RETENTION_DEMI_VIE_PART_CA = 0.06
BOOST_CONVERSION_REMISE = 0.90  # 30 % de remise = +27 % de clients a budget egal
PENALITE_REMISE_REACHAT = 1.4   # 30 % de remise = 42 % de reachat en moins
PENALITE_REMISE_PLANCHER = 0.35

# --- marge -----------------------------------------------------------------
PSP_PCT = 0.017                 # frais de paiement, % du CA HT — fixe
COUT_RELATIF_RETOUR = 0.75      # un retour coute 75 % de la valeur HT de la commande
PALIERS_COGS = [                # (unites cumulees, multiplicateur du COGS theorique)
    (5_000, 1.35), (25_000, 1.25), (100_000, 1.15),
    (400_000, 1.07), (1_500_000, 1.02), (float("inf"), 0.97),
]
# Logistique. Dans les chiffres canoniques, le cout d'un colis est quasi PLAT
# en euros (6,13 EUR a P1, 6,60 EUR a P5) : si la logistique passe de 16 % a
# 11 % du CA HT, ce n'est pas parce que le colis coute moins cher, c'est parce
# que le panier monte. On modelise donc un cout par COLIS, pas un pourcentage.
LOG_COEF_ANCRAGE = 1.391        # cale le colis sur 16 % du CA HT au lancement
LOG_EXPOSANT_PANIER = 0.30      # un panier plus gros = un colis un peu plus lourd
LOG_FACTEUR_PETIT = 1.15        # remise volume reelle, modeste
LOG_FACTEUR_GROS = 1.00
LOG_VOLUME_PLEIN = 45_000       # commandes/mois pour atteindre le tarif plancher
CIBLAGE_QUALIFIE_PART = 0.05    # part du marche adressable mensuel restant qualifiee
MAJORATION_RETOUR_MAX = 0.90

# --- structure -------------------------------------------------------------
ETP_BASE = 1.5
CA_HT_PAR_ETP = 95_000.0
SALAIRE_CHARGE_ETP = 3_000.0
FRAIS_OUTILS_BASE = 1_200.0
FRAIS_PAR_MARCHE = 1_800.0
FRAIS_VARIABLES_PCT_CA_HT = 0.055
COUT_RECRUTEMENT = 2_500.0

# --- tresorerie ------------------------------------------------------------
PART_ENCAISSEE_MOIS = 0.78      # reversement PSP : 78 % dans le mois, 22 % le mois suivant
ACOMPTE_FOURNISSEUR = 0.30      # acompte a la commande, au lancement
ACOMPTE_FOURNISSEUR_MIN = 0.15  # apres negociation, a l'echelle
ACOMPTE_VOLUME_PLEIN = 400_000  # unites cumulees pour obtenir les meilleures conditions
DELAI_LIVRAISON_MOIS = 2
PART_CAPITAL_STOCK_INITIAL = 0.12   # premier lot achete avant l'ouverture
AVANCE_PUB_PART = 0.15          # part du budget pub avancee (affichee dans le BFR)

# --- marches ---------------------------------------------------------------
PART_PAYS = {
    "FR": 1.00, "BE": 0.18, "DE": 1.55, "ES": 0.85,
    "IT": 0.95, "NL": 0.30, "UK": 1.35,
}
ORDRE_OUVERTURE = ["BE", "DE", "ES", "IT", "NL", "UK"]
SEUIL_CA_OUVERTURE = 200_000.0  # CA TTC mensuel minimum pour ouvrir un marche
COUT_OUVERTURE_MARCHE = 30_000.0
RAMPE_MARCHE_MOIS = 4

# --- evenements aleatoires (probabilites mensuelles) -----------------------
P_BANNISSEMENT_BASE = 0.020
BANNISSEMENT_FACTEUR_MONOCANAL = 1.8    # multiplie par la concentration au-dela de 60 %
BANNISSEMENT_FACTEUR_REMISE = 2.2
BANNISSEMENT_PERTE_BUDGET = 0.62        # 62 % du budget du mois rendu inefficace
P_RETARD_FOURNISSEUR = 0.09
RETARD_FOURNISSEUR_MOIS = 1
P_CONCURRENT = 0.055
CONCURRENT_EFFET = 0.89                 # -11 % de clients a budget egal, durable
P_VIRAL = 0.045
VIRAL_EFFET = 1.38
VIRAL_DUREE = 2
P_LITIGE = 0.025
LITIGE_SURCOUT_RETOUR = 0.020           # +2,0 points de taux de retour
LITIGE_DUREE = 3
LITIGE_COUT_FIXE = 12_000.0
SAISON_CPM = {                          # indice de CPM par mois calendaire
    1: 0.86, 2: 0.90, 3: 0.95, 4: 0.98, 5: 1.00, 6: 0.97,
    7: 0.92, 8: 0.90, 9: 1.02, 10: 1.08, 11: 1.32, 12: 1.45,
}

# ===========================================================================
# 1. FORMATAGE — memes conventions que modele_nora.py
# ===========================================================================

def eur(x: float, d: int = 0) -> str:
    s = f"{x:,.{d}f}".replace(",", " ").replace(".", ",").replace("-", "−")
    return s + " €"


def num(x: float, d: int = 0) -> str:
    return f"{x:,.{d}f}".replace(",", " ").replace(".", ",").replace("-", "−")


def pct(x: float, d: int = 1) -> str:
    return f"{x * 100:.{d}f}".replace(".", ",").replace("-", "−") + " %"


def dec(x: float, d: int = 2) -> str:
    return f"{x:.{d}f}".replace(".", ",").replace("-", "−")


def lire_nombre(s: str, defaut: Optional[float] = None) -> float:
    """Accepte « 12,5 », « 12.5 », « 12 500 € », « 30 % »."""
    s = (s or "").strip().replace("€", "").replace("%", "").replace(" ", "")
    s = s.replace(" ", "").replace(" ", "").replace(",", ".")
    if not s:
        if defaut is None:
            raise ValueError("valeur manquante")
        return defaut
    return float(s)


def borner(x: float, bas: float, haut: float) -> float:
    return max(bas, min(haut, x))


# ===========================================================================
# 2. LES CATEGORIES — le tour 0 de la partie
# ===========================================================================

@dataclass(frozen=True)
class Categorie:
    code: str
    libelle: str
    coef_max: float             # coefficient maximum atteignable (PVC TTC / COGS)
    freq_reachat_mois: float    # delai moyen entre deux commandes, en mois
    taux_retour: float          # taux de retour structurel de la categorie
    part_logistique: float      # logistique en % du CA HT au tarif plancher
    taille_marche: float        # CA annuel adressable en ligne, France, TTC
    cpm_base: float             # cout pour mille impressions de reference
    prix_reference: float       # prix TTC de reference de la categorie


CATEGORIES: Dict[str, Categorie] = {
    "soin_cheveux": Categorie(
        "soin_cheveux", "Soin capillaire premium",
        8.0, 3.0, 0.035, 0.11, 45_000_000, 14.0, 39.0),
    "complement": Categorie(
        "complement", "Complément alimentaire",
        7.5, 1.5, 0.020, 0.09, 38_000_000, 16.0, 45.0),
    "soin_visage": Categorie(
        "soin_visage", "Soin du visage",
        8.5, 2.5, 0.040, 0.10, 62_000_000, 18.0, 49.0),
    "animalerie": Categorie(
        "animalerie", "Animalerie",
        6.0, 2.0, 0.050, 0.15, 28_000_000, 12.0, 35.0),
    "maison_deco": Categorie(
        "maison_deco", "Maison et décoration",
        4.5, 14.0, 0.120, 0.22, 70_000_000, 11.0, 65.0),
    "mode_accessoire": Categorie(
        "mode_accessoire", "Mode et accessoires",
        3.5, 10.0, 0.280, 0.17, 120_000_000, 13.0, 55.0),
}


# ===========================================================================
# 3. LES DECISIONS DU JOUEUR
# ===========================================================================

@dataclass
class Decision:
    budget_pub: float = 0.0             # EUR du mois
    part_test_crea: float = 0.15        # 0 a 0,30 du budget pub
    remise: float = 0.0                 # 0 a 0,30
    invest_retention: float = 0.0       # EUR du mois (CRM, contenu, packaging)
    invest_offre: float = 0.0           # EUR ponctuel (bundles, upsell)
    commande_stock: float = 0.0         # unites commandees
    recrutement: float = 0.0            # variation d'ETP
    ouvrir_marche: Optional[str] = None # code pays ou None
    prix_ttc: Optional[float] = None    # None = on garde le prix courant
    part_canal_principal: float = 0.80  # concentration du budget sur un seul canal

    def normalisee(self) -> "Decision":
        return replace(
            self,
            budget_pub=max(0.0, self.budget_pub),
            part_test_crea=borner(self.part_test_crea, 0.0, 0.30),
            remise=borner(self.remise, 0.0, 0.30),
            invest_retention=max(0.0, self.invest_retention),
            invest_offre=max(0.0, self.invest_offre),
            commande_stock=max(0.0, self.commande_stock),
            recrutement=borner(self.recrutement, -10.0, 20.0),
            part_canal_principal=borner(self.part_canal_principal, 0.25, 1.0),
        )


@dataclass
class Cohorte:
    mois_acq: int
    taille: float
    remise_acq: float
    indice_retention_acq: float


@dataclass
class Gagnant:
    ne_le: int
    duree: float

    def poids(self, mois: int) -> float:
        age = mois - self.ne_le
        if age >= self.duree:
            return 0.0
        return max(0.0, 1.0 - (age / self.duree) ** EXPOSANT_FATIGUE)


@dataclass
class Mois:
    """Une ligne du tableau de bord : tout ce qui s'est passe pendant un mois."""
    mois: int
    mois_calendaire: int
    ca_ttc: float = 0.0             # encaisse, net de remise
    ca_ttc_facture: float = 0.0     # catalogue, avant remise
    ca_ht: float = 0.0              # base des pourcentages (= facture / 1,20)
    commandes: float = 0.0
    commandes_new: float = 0.0
    commandes_reachat: float = 0.0
    aov_ttc: float = 0.0
    part_reachat: float = 0.0
    budget_pub: float = 0.0
    budget_pub_efficace: float = 0.0
    mer: float = 0.0
    cac_moyen: float = 0.0
    cac_marginal: float = 0.0
    qualite_crea: float = 0.0
    gagnants: int = 0
    gagnants_effectifs: float = 0.0
    concepts_testes: float = 0.0
    nouveaux_gagnants: int = 0
    cout_test: float = 0.0
    pct_cogs: float = 0.0
    pct_log: float = 0.0
    pct_psp: float = 0.0
    pct_retours: float = 0.0
    pct_remises: float = 0.0
    marge_brute_pct: float = 0.0
    marge_brute: float = 0.0
    cm3: float = 0.0
    cm3_pct: float = 0.0
    fixes: float = 0.0
    ebitda: float = 0.0
    ebitda_pct: float = 0.0
    tresorerie: float = 0.0
    stock_unites: float = 0.0
    jours_stock: float = 0.0
    rupture: bool = False
    etp: float = 0.0
    marches: int = 1
    saturation: float = 0.0
    prix_ttc: float = 0.0
    remise: float = 0.0
    ca_ttc_semaine: float = 0.0
    evenements: List[str] = field(default_factory=list)
    alertes: List[str] = field(default_factory=list)


@dataclass
class Partie:
    categorie: Categorie
    prix_ttc: float
    coefficient: float
    capital: float
    graine: int
    horizon: int
    strategie: str = "manuel"
    mois_joues: int = 0
    issue: str = "en cours"
    mois_victoire: Optional[int] = None
    historique: List[Mois] = field(default_factory=list)

    @property
    def tresorerie_min(self) -> float:
        return min([m.tresorerie for m in self.historique], default=self.capital)

    @property
    def dernier(self) -> Optional[Mois]:
        return self.historique[-1] if self.historique else None

    def moyenne_fin(self, champ: str, n: int = 6) -> float:
        """Moyenne des n derniers mois — un mois isolé ne veut rien dire."""
        derniers = self.historique[-n:]
        if not derniers:
            return 0.0
        return sum(getattr(m, champ) for m in derniers) / len(derniers)

    def ebitda_pct_fin(self, n: int = 6) -> float:
        derniers = self.historique[-n:]
        ca = sum(m.ca_ht for m in derniers)
        return (sum(m.ebitda for m in derniers) / ca) if ca > 0 else 0.0

    def ca_ttc_semaine_max(self) -> float:
        return max([m.ca_ttc_semaine for m in self.historique], default=0.0)


# ===========================================================================
# 4. LE MOTEUR
# ===========================================================================

class Simulateur:
    """Un moteur, un etat, une methode `jouer_un_mois(decision)`."""

    def __init__(self, categorie: str, prix_ttc: float, coefficient: float,
                 capital: float, graine: int = 1, horizon: int = HORIZON_DEFAUT,
                 mois_depart: int = 1, stock_initial: Optional[float] = None):
        if categorie not in CATEGORIES:
            raise ValueError(f"catégorie inconnue : {categorie}")
        self.cat = CATEGORIES[categorie]
        self.prix_ttc = float(prix_ttc)
        # le coefficient vise est plafonne par la categorie : on ne decide pas
        # d'acheter a 8x ce que le marche fournisseur vend a 4x
        self.coefficient = min(float(coefficient), self.cat.coef_max)
        self.capital = float(capital)
        self.graine = int(graine)
        self.horizon = int(horizon)
        self.mois_depart = mois_depart

        self.rng_evt = random.Random(graine * 7_919 + 11)   # flux dedie : evenements
        self.rng_crea = random.Random(graine * 104_729 + 3) # flux dedie : creation

        # --- etat -------------------------------------------------------
        self.mois = 0
        self.tresorerie = self.capital
        # le premier lot est achete et paye AVANT la premiere vente : c'est du
        # capital immobilise, pas une charge. Il est deja en entrepot au mois 1.
        cout_u = (self.prix_ttc / self.coefficient) * PALIERS_COGS[0][1]
        if stock_initial is None:
            budget_stock = self.capital * PART_CAPITAL_STOCK_INITIAL
            stock_initial = budget_stock / cout_u if cout_u > 0 else 0.0
        self.stock_unites = float(stock_initial)
        self.tresorerie -= self.stock_unites * cout_u
        self.etp = ETP_BASE
        self.marches: Dict[str, int] = {"FR": 0}   # code -> mois d'ouverture
        self.cumul_unites = 0.0
        self.cumul_clients = 0.0
        self.cumul_offre = 0.0
        self.cumul_retention = 0.0
        self.cohortes: List[Cohorte] = []
        self.gagnants: List[Gagnant] = [
            Gagnant(0, self._duree_vie(0, i)) for i in range(GAGNANTS_AU_LANCEMENT)
        ]
        self.malus_crea = 0.0
        self.facteur_concurrence = 1.0
        self.viral_restant = 0
        self.litige_restant = 0
        self.ban_restant = 0
        self.livraisons: List[Tuple[int, float, float]] = []  # (mois, unites, solde)
        self.encaissement_reporte = 0.0
        self.ca_12m: List[float] = []
        self.historique: List[Mois] = []
        self.mois_objectif_consecutifs = 0
        self.issue = "en cours"
        self.mois_victoire: Optional[int] = None
        self.budget_pub_precedent = 0.0

    # -- utilitaires deterministes --------------------------------------

    def _duree_vie(self, mois: int, indice: int) -> float:
        """Duree de vie d'un concept gagnant, tiree d'un flux indexe par le mois.

        Le flux depend de (graine, mois, indice) et non de l'historique : deux
        strategies comparees sur la meme graine subissent exactement les memes
        tirages. C'est ce qui rend --comparer honnete.
        """
        r = random.Random(self.graine * 1_000_003 + mois * 9_973 + indice)
        return DUREE_VIE_GAGNANT_MIN + (
            DUREE_VIE_GAGNANT_MAX - DUREE_VIE_GAGNANT_MIN) * r.random()

    # -- 1. qualite creative --------------------------------------------

    def cout_test_unitaire(self, budget: float) -> float:
        if budget <= 0:
            return COUT_TEST_MIN
        brut = COUT_TEST_ANCRE * (budget / BUDGET_ANCRE_TEST) ** EXPOSANT_COUT_TEST
        return borner(brut, COUT_TEST_MIN, COUT_TEST_MAX)

    def taux_reussite(self, budget: float) -> float:
        part = min(1.0, budget / BUDGET_REUSSITE_BASSE)
        return TAUX_REUSSITE_PETIT - (TAUX_REUSSITE_PETIT - TAUX_REUSSITE_GROS) * part

    def gagnants_reference(self, budget: float) -> float:
        if budget <= 0:
            return 2.0
        return max(2.0, GAGNANTS_REFERENCE
                   * (budget / BUDGET_ANCRE_TEST) ** EXPOSANT_GAGNANTS_REFERENCE)

    def _machine_creative(self, d: Decision) -> Tuple[float, float, int, float, float]:
        """Teste, tire les gagnants, fait vieillir le stock, rend la qualite."""
        cout = self.cout_test_unitaire(d.budget_pub)
        testes = (d.budget_pub * d.part_test_crea) / cout if cout > 0 else 0.0
        taux = self.taux_reussite(d.budget_pub)

        # tirage binomial : approximation normale a UN seul tirage par mois, pour
        # que le flux aleatoire reste aligne entre deux strategies comparees
        moyenne = testes * taux
        ecart = math.sqrt(max(0.0, testes * taux * (1 - taux)))
        brut = moyenne + ecart * self.rng_crea.gauss(0.0, 1.0)
        nouveaux = int(max(0, round(brut)))

        for i in range(nouveaux):
            self.gagnants.append(Gagnant(self.mois, self._duree_vie(self.mois, i)))

        # les gagnants vieillissent et meurent
        self.gagnants = [g for g in self.gagnants if g.poids(self.mois) > 0.0]
        g_eff = sum(g.poids(self.mois) for g in self.gagnants)

        n_ref = self.gagnants_reference(d.budget_pub)
        ratio = g_eff / n_ref if n_ref > 0 else 0.0
        q = 0.55 + 0.45 * math.sqrt(min(ratio, 4.0))
        q *= (1.0 - self.malus_crea)
        etp_requis = self.etp_requis()
        q *= (0.60 + 0.40 * min(1.0, self.etp / etp_requis if etp_requis > 0 else 1.0))
        q = borner(q, QUALITE_MIN, QUALITE_MAX)

        self.malus_crea *= DECROISSANCE_MALUS_CREA
        if self.malus_crea < 0.005:
            self.malus_crea = 0.0
        return q, testes, nouveaux, g_eff, cout

    # -- 2. marche et saturation ----------------------------------------

    def marche_adressable(self) -> float:
        """CA annuel TTC adressable, somme des marches ouverts avec leur rampe."""
        total = 0.0
        for code, ouvert_le in self.marches.items():
            age = self.mois - ouvert_le
            rampe = borner((age + 1) / RAMPE_MARCHE_MOIS, 0.25, 1.0)
            total += self.cat.taille_marche * PART_PAYS[code] * rampe
        return total

    def saturation(self) -> float:
        ca12 = sum(self.ca_12m[-12:])
        if len(self.ca_12m) < 12 and self.ca_12m:
            ca12 = ca12 / len(self.ca_12m[-12:]) * 12
        adressable = self.marche_adressable()
        return borner(ca12 / adressable if adressable > 0 else 0.0, 0.0, SATURATION_MAX)

    def etp_requis(self) -> float:
        ca_ht = self.historique[-1].ca_ht if self.historique else 0.0
        return ETP_BASE + ca_ht / CA_HT_PAR_ETP

    # -- 3. acquisition --------------------------------------------------

    def _acquisition(self, d: Decision, q: float, mois_cal: int,
                     budget_efficace: float) -> Tuple[float, float]:
        """Nouveaux clients du mois. Rendement decroissant : b = 0,72."""
        if budget_efficace <= 0:
            return 0.0, 0.0
        a = A_BASE
        a *= (CPM_REFERENCE / self.cat.cpm_base) ** EXPOSANT_CPM
        a *= (self.cat.prix_reference / self.prix_ttc) ** EXPOSANT_PRIX
        a *= self.facteur_concurrence
        # halo de marque et maturite du compte
        a *= 1.0 + MARQUE_PLAFOND * (
            self.cumul_clients / (self.cumul_clients + MARQUE_DEMI_VIE_CLIENTS))
        a *= MATURITE_PLANCHER + (1 - MATURITE_PLANCHER) * min(
            1.0, self.cumul_clients / MATURITE_CLIENTS_CIBLE)
        # saturation cumulee du marche adressable
        sat = self.saturation()
        a *= (1.0 - sat) ** EXPOSANT_SATURATION
        if self.viral_restant > 0:
            a *= VIRAL_EFFET
        # La remise achète de la conversion : c'est précisément ce qui la rend
        # tentante. Son coût est ailleurs — sur la marge et sur le réachat.
        a *= 1.0 + BOOST_CONVERSION_REMISE * d.remise

        saison = SAISON_CPM.get(mois_cal, 1.0)
        clients = a * (budget_efficace ** EXPOSANT_RENDEMENT_PUB) * q / saison
        return max(0.0, clients), sat

    # -- 4. panier -------------------------------------------------------

    def multiplicateur_offre(self) -> float:
        gain = (MULT_OFFRE_PLAFOND - MULT_OFFRE_BASE) * (
            1.0 - math.exp(-self.cumul_offre / OFFRE_DEMI_VIE))
        return MULT_OFFRE_BASE + gain

    # -- 5. reachat par cohortes ----------------------------------------

    def indice_retention(self) -> float:
        ca12 = sum(self.ca_12m[-12:])
        k = max(RETENTION_DEMI_VIE_MIN, RETENTION_DEMI_VIE_PART_CA * ca12)
        return 1.0 + RETENTION_GAIN_MAX * (
            self.cumul_retention / (self.cumul_retention + k))

    def _noyau_reachat(self, age: int) -> float:
        """Calendrier de consommation : une bosse a `freq_reachat_mois`, une queue fidele."""
        f = self.cat.freq_reachat_mois
        x = age / f
        bosse = (x ** REACHAT_FORME) * math.exp(-REACHAT_FORME * (x - 1.0))
        fidelite = (REACHAT_FIDELITE_PLANCHER + (1 - REACHAT_FIDELITE_PLANCHER)
                    * REACHAT_FIDELITE_DECROISSANCE ** age)
        queue = REACHAT_QUEUE_POIDS * REACHAT_QUEUE_DECROISSANCE ** age
        return (TAUX_BASE_REACHAT / f) * (bosse * fidelite + queue)

    def _reachat(self) -> float:
        indice = self.indice_retention()
        total = 0.0
        for c in self.cohortes:
            age = self.mois - c.mois_acq
            if age < 1:
                continue
            p = self._noyau_reachat(age)
            # amelioration de retention : seule la part acquise depuis
            # l'investissement en profite pleinement
            p *= 1.0 + (indice - 1.0) * 0.65 + (c.indice_retention_acq - 1.0) * 0.35
            p *= max(PENALITE_REMISE_PLANCHER,
                     1.0 - PENALITE_REMISE_REACHAT * c.remise_acq)
            total += c.taille * p
        return total

    # -- 6. marge --------------------------------------------------------

    def multiplicateur_cogs(self) -> float:
        for seuil, mult in PALIERS_COGS:
            if self.cumul_unites < seuil:
                return mult
        return PALIERS_COGS[-1][1]

    def facteur_logistique(self, commandes: float) -> float:
        part = min(1.0, commandes / LOG_VOLUME_PLEIN)
        return LOG_FACTEUR_PETIT - (LOG_FACTEUR_PETIT - LOG_FACTEUR_GROS) * math.sqrt(part)

    def taux_retour_effectif(self, budget: float) -> float:
        adressable_mois = self.marche_adressable() / 12.0
        qualifie = CIBLAGE_QUALIFIE_PART * adressable_mois
        majoration = 0.0
        if qualifie > 0 and budget > qualifie:
            majoration = min(MAJORATION_RETOUR_MAX,
                             0.5 * ((budget / qualifie) - 1.0) ** 0.7)
        # un prix au-dessus de la référence élève les attentes, donc les retours
        prime = max(0.0, self.prix_ttc / self.cat.prix_reference - 1.0)
        t = self.cat.taux_retour * (1.0 + majoration) * (1.0 + 0.25 * prime)
        if self.litige_restant > 0:
            t += LITIGE_SURCOUT_RETOUR
        return t

    # -- 8. evenements ---------------------------------------------------

    def _evenements(self, d: Decision, mois_cal: int) -> Tuple[List[str], float]:
        """Tire les evenements du mois. Rend les messages et un cout ponctuel."""
        msgs: List[str] = []
        cout = 0.0

        # bannissement du compte publicitaire
        p_ban = P_BANNISSEMENT_BASE
        exces = max(0.0, d.part_canal_principal - 0.60)
        p_ban *= 1.0 + BANNISSEMENT_FACTEUR_MONOCANAL * exces
        p_ban *= 1.0 + BANNISSEMENT_FACTEUR_REMISE * d.remise
        if self.rng_evt.random() < p_ban and self.ban_restant == 0:
            self.ban_restant = 1
            perte = d.budget_pub * BANNISSEMENT_PERTE_BUDGET
            msgs.append(
                f"BANNISSEMENT du compte publicitaire principal — "
                f"{pct(BANNISSEMENT_PERTE_BUDGET)} du budget du mois inefficace, "
                f"soit {eur(perte)} de dépense perdue. Concentration canal : "
                f"{pct(d.part_canal_principal)}, remise : {pct(d.remise)}.")

        # retard fournisseur
        if self.rng_evt.random() < P_RETARD_FOURNISSEUR and self.livraisons:
            self.livraisons = [(m + RETARD_FOURNISSEUR_MOIS, u, s)
                               for (m, u, s) in self.livraisons]
            unites = sum(u for (_, u, _) in self.livraisons)
            msgs.append(
                f"RETARD FOURNISSEUR — {num(unites)} unités décalées de "
                f"{RETARD_FOURNISSEUR_MOIS} mois. Le risque de rupture augmente.")

        # entree d'un concurrent
        if self.rng_evt.random() < P_CONCURRENT:
            self.facteur_concurrence *= CONCURRENT_EFFET
            msgs.append(
                f"ENTRÉE D'UN CONCURRENT — enchères plus chères : "
                f"{pct(1 - CONCURRENT_EFFET)} de clients en moins à budget égal, "
                f"de façon durable (cumul : ×{dec(self.facteur_concurrence)}).")

        # contenu viral
        if self.rng_evt.random() < P_VIRAL:
            self.viral_restant = VIRAL_DUREE
            msgs.append(
                f"CONTENU VIRAL — +{pct(VIRAL_EFFET - 1)} de clients à budget égal "
                f"pendant {VIRAL_DUREE} mois. Le CAC baisse d'autant.")

        # litige qualite
        if self.rng_evt.random() < P_LITIGE:
            self.litige_restant = LITIGE_DUREE
            cout += LITIGE_COUT_FIXE
            msgs.append(
                f"LITIGE QUALITÉ — taux de retour +{pct(LITIGE_SURCOUT_RETOUR)} "
                f"pendant {LITIGE_DUREE} mois et {eur(LITIGE_COUT_FIXE)} de frais "
                f"immédiats (rappel de lot, gestes commerciaux).")

        if mois_cal in (11, 12):
            msgs.append(
                f"PIC DE CPM saisonnier — indice ×{dec(SAISON_CPM[mois_cal])} : "
                f"le même budget achète {pct(1 - 1 / SAISON_CPM[mois_cal])} "
                f"de clients en moins.")
        return msgs, cout

    # -- 7. tresorerie ---------------------------------------------------

    def besoin_fonds_roulement(self, m: Mois) -> float:
        stock_valo = self.stock_unites * self.cogs_unitaire()
        dettes = sum(s for (_, _, s) in self.livraisons)
        return (stock_valo + self.encaissement_reporte
                + AVANCE_PUB_PART * m.budget_pub - dettes)

    def acompte_fournisseur(self) -> float:
        """Le délai de paiement se négocie avec le volume. C'est un levier de
        trésorerie aussi puissant qu'un point de marge — voir E10 et le modèle
        de cahier des charges fournisseur."""
        part = min(1.0, self.cumul_unites / ACOMPTE_VOLUME_PLEIN)
        return ACOMPTE_FOURNISSEUR - (
            ACOMPTE_FOURNISSEUR - ACOMPTE_FOURNISSEUR_MIN) * part

    def cogs_unitaire(self) -> float:
        """Coût de revient d'une unité vendue, au palier de volume courant."""
        return (self.prix_ttc / self.coefficient) * self.multiplicateur_cogs()

    # -- le tour ---------------------------------------------------------

    def jouer_un_mois(self, d: Decision) -> Mois:
        d = d.normalisee()
        self.mois += 1
        mois_cal = ((self.mois_depart - 1 + self.mois - 1) % 12) + 1
        if d.prix_ttc is not None and d.prix_ttc > 0:
            self.prix_ttc = float(d.prix_ttc)

        m = Mois(mois=self.mois, mois_calendaire=mois_cal)
        m.prix_ttc = self.prix_ttc
        m.remise = d.remise
        m.budget_pub = d.budget_pub

        # --- ouverture de marche ---------------------------------------
        cout_ponctuel = 0.0
        ca_prec = self.historique[-1].ca_ttc if self.historique else 0.0
        if d.ouvrir_marche:
            code = d.ouvrir_marche.upper()
            if code not in PART_PAYS:
                m.alertes.append(f"Marché inconnu : {code}. Ouverture ignorée.")
            elif code in self.marches:
                m.alertes.append(f"Marché {code} déjà ouvert. Ouverture ignorée.")
            elif ca_prec < SEUIL_CA_OUVERTURE:
                m.alertes.append(
                    f"Ouverture de {code} refusée : CA TTC du mois précédent "
                    f"{eur(ca_prec)} < seuil {eur(SEUIL_CA_OUVERTURE)}.")
            else:
                self.marches[code] = self.mois
                cout_ponctuel += COUT_OUVERTURE_MARCHE
                m.evenements.append(
                    f"OUVERTURE DU MARCHÉ {code} — {eur(COUT_OUVERTURE_MARCHE)} de "
                    f"mise en place, marché adressable porté à "
                    f"{eur(self.marche_adressable())} TTC/an, montée en charge sur "
                    f"{RAMPE_MARCHE_MOIS} mois.")

        # --- recrutement -----------------------------------------------
        if d.recrutement > 0:
            cout_ponctuel += d.recrutement * COUT_RECRUTEMENT
        self.etp = max(0.5, self.etp + d.recrutement)

        # --- evenements -------------------------------------------------
        msgs, cout_evt = self._evenements(d, mois_cal)
        m.evenements.extend(msgs)
        cout_ponctuel += cout_evt

        # --- machine creative -------------------------------------------
        q, testes, nouveaux, g_eff, cout_test = self._machine_creative(d)
        m.qualite_crea = q
        m.concepts_testes = testes
        m.nouveaux_gagnants = nouveaux
        m.gagnants = len(self.gagnants)
        m.gagnants_effectifs = g_eff
        m.cout_test = cout_test

        # --- acquisition -------------------------------------------------
        budget_efficace = d.budget_pub
        if self.ban_restant > 0:
            budget_efficace *= (1.0 - BANNISSEMENT_PERTE_BUDGET)
        m.budget_pub_efficace = budget_efficace
        clients, sat = self._acquisition(d, q, mois_cal, budget_efficace)
        m.saturation = sat

        # --- reachat ------------------------------------------------------
        reachat = self._reachat()

        # --- stock et rupture ---------------------------------------------
        mult_offre = self.multiplicateur_offre()
        unites_par_commande = mult_offre
        demande_cmd = clients + reachat
        demande_unites = demande_cmd * unites_par_commande
        # livraisons du mois
        restantes = []
        for (mois_liv, unites, solde) in self.livraisons:
            if mois_liv <= self.mois:
                self.stock_unites += unites
                cout_ponctuel += solde
            else:
                restantes.append((mois_liv, unites, solde))
        self.livraisons = restantes

        if demande_unites > self.stock_unites + 1e-9:
            ratio = (self.stock_unites / demande_unites) if demande_unites > 0 else 0.0
            m.rupture = True
            clients *= ratio
            reachat *= ratio
            demande_cmd *= ratio
            demande_unites = self.stock_unites
            self.malus_crea = min(0.45, self.malus_crea + MALUS_RUPTURE_CREA)
            m.alertes.append(
                f"RUPTURE DE STOCK — ventes plafonnées à {pct(ratio)} de la demande. "
                f"Pénalité durable de {pct(MALUS_RUPTURE_CREA)} sur la qualité "
                f"créative : l'algorithme a désappris.")
        self.stock_unites = max(0.0, self.stock_unites - demande_unites)

        # --- commande de stock --------------------------------------------
        if d.commande_stock > 0:
            valeur = d.commande_stock * self.cogs_unitaire()
            acompte = valeur * self.acompte_fournisseur()
            solde = valeur - acompte
            cout_ponctuel += acompte
            self.livraisons.append(
                (self.mois + DELAI_LIVRAISON_MOIS, d.commande_stock, solde))

        # --- chiffre d'affaires --------------------------------------------
        prix_catalogue_ttc = self.prix_ttc * mult_offre
        m.aov_ttc = prix_catalogue_ttc * (1.0 - d.remise)
        m.commandes = demande_cmd
        m.commandes_new = clients
        m.commandes_reachat = reachat
        m.part_reachat = (reachat / demande_cmd) if demande_cmd > 0 else 0.0
        m.ca_ttc_facture = demande_cmd * prix_catalogue_ttc
        m.ca_ttc = demande_cmd * m.aov_ttc
        m.ca_ht = m.ca_ttc_facture / (1 + TVA)      # base des pourcentages
        m.ca_ttc_semaine = m.ca_ttc / SEMAINES_PAR_MOIS

        # --- cascade de marge (en % du CA HT facturé, comme les canoniques) --
        cogs_eur = demande_cmd * unites_par_commande * (
            self.prix_ttc / self.coefficient) * self.multiplicateur_cogs()
        prix_catalogue_ht = prix_catalogue_ttc / (1 + TVA)
        # La logistique est un coût PHYSIQUE par colis : préparer et expédier une
        # commande coûte le même prix qu'elle contienne un produit à 39 € ou à
        # 55 €. Le coût est donc adossé au prix de RÉFÉRENCE de la catégorie et
        # au volume du panier, jamais au prix du joueur. C'est de là que vient
        # l'avantage structurel du positionnement premium.
        cout_colis = (LOG_COEF_ANCRAGE * self.cat.part_logistique
                      * (self.cat.prix_reference / (1 + TVA))
                      * (mult_offre / MULT_OFFRE_BASE) ** LOG_EXPOSANT_PANIER
                      * self.facteur_logistique(demande_cmd))
        log_eur = demande_cmd * cout_colis
        psp_eur = m.ca_ht * PSP_PCT
        taux_ret = self.taux_retour_effectif(d.budget_pub)
        retours_eur = m.ca_ht * taux_ret * COUT_RELATIF_RETOUR
        remises_eur = m.ca_ht * d.remise

        if m.ca_ht > 0:
            m.pct_cogs = cogs_eur / m.ca_ht
            m.pct_log = log_eur / m.ca_ht
            m.pct_psp = PSP_PCT
            m.pct_retours = retours_eur / m.ca_ht
            m.pct_remises = d.remise
        m.marge_brute = m.ca_ht - cogs_eur - log_eur - psp_eur - retours_eur - remises_eur
        m.marge_brute_pct = (m.marge_brute / m.ca_ht) if m.ca_ht > 0 else 0.0

        m.cm3 = m.marge_brute - d.budget_pub
        m.cm3_pct = (m.cm3 / m.ca_ht) if m.ca_ht > 0 else 0.0
        m.mer = (m.ca_ttc / d.budget_pub) if d.budget_pub > 0 else 0.0
        m.cac_moyen = (d.budget_pub / clients) if clients > 0 else 0.0
        m.cac_marginal = m.cac_moyen / EXPOSANT_RENDEMENT_PUB if clients > 0 else 0.0

        # --- frais fixes ----------------------------------------------------
        fixes = (self.etp * SALAIRE_CHARGE_ETP + FRAIS_OUTILS_BASE
                 + FRAIS_PAR_MARCHE * (len(self.marches) - 1)
                 + FRAIS_VARIABLES_PCT_CA_HT * m.ca_ht)
        m.fixes = fixes
        m.ebitda = m.cm3 - fixes
        m.ebitda_pct = (m.ebitda / m.ca_ht) if m.ca_ht > 0 else 0.0
        m.etp = self.etp
        m.marches = len(self.marches)

        # --- tresorerie ------------------------------------------------------
        # Tout est raisonne HORS TAXES : la TVA collectee est reversee, la TVA
        # sur achats est deduite. Le decalage vient du reversement du PSP et
        # des conditions fournisseur, pas de la TVA.
        # Entrees : CA HT net de remise, dont 78 % dans le mois.
        encaissable = m.ca_ht - remises_eur
        entrees = encaissable * PART_ENCAISSEE_MOIS + self.encaissement_reporte
        self.encaissement_reporte = encaissable * (1.0 - PART_ENCAISSEE_MOIS)
        # Sorties : le COGS sort par les paiements fournisseur (acompte + solde),
        # tout le reste sort dans le mois.
        sorties = (d.budget_pub + fixes + d.invest_retention + d.invest_offre
                   + cout_ponctuel + log_eur + psp_eur + retours_eur)
        self.tresorerie += entrees - sorties
        m.tresorerie = self.tresorerie
        m.stock_unites = self.stock_unites
        vendues_jour = (demande_unites / 30.0) if demande_unites > 0 else 0.0
        m.jours_stock = (self.stock_unites / vendues_jour) if vendues_jour > 0 else 999.0

        # --- mise a jour de l'etat -------------------------------------------
        self.cumul_offre += d.invest_offre
        self.cumul_retention += d.invest_retention
        self.cumul_unites += demande_unites
        self.cumul_clients += clients
        if clients > 0:
            self.cohortes.append(Cohorte(self.mois, clients, d.remise,
                                         self.indice_retention()))
        self.ca_12m.append(m.ca_ttc)
        self.budget_pub_precedent = d.budget_pub
        if self.ban_restant > 0:
            self.ban_restant -= 1
        if self.viral_restant > 0:
            self.viral_restant -= 1
        if self.litige_restant > 0:
            self.litige_restant -= 1

        self._alertes(m, d)
        self.historique.append(m)
        self._verifier_fin(m)
        return m

    # -- alertes et fin de partie ------------------------------------------

    def _alertes(self, m: Mois, d: Decision) -> None:
        if m.tresorerie < 0:
            m.alertes.append(
                f"TRÉSORERIE NÉGATIVE : {eur(m.tresorerie)}. La partie est perdue.")
        elif m.ca_ttc > 0 and m.tresorerie < (m.fixes + d.budget_pub) * 1.5:
            mois_restants = m.tresorerie / max(1.0, m.fixes + d.budget_pub)
            m.alertes.append(
                f"TRÉSORERIE TENDUE : {eur(m.tresorerie)}, soit "
                f"{dec(mois_restants, 1)} mois de dépenses courantes.")
        if d.part_test_crea < 0.05 and d.budget_pub > 0:
            m.alertes.append(
                f"BUDGET DE TEST CRÉATIF À {pct(d.part_test_crea)} — le stock de "
                f"concepts gagnants s'épuise sans être renouvelé.")
        if m.qualite_crea <= QUALITE_MIN + 0.02:
            m.alertes.append(
                f"QUALITÉ CRÉATIVE AU PLANCHER ({dec(m.qualite_crea)}) : tu paies "
                f"tes clients {pct(1 / QUALITE_MIN - 1)} plus cher qu'un compte à 1,00.")
        if 0 < m.jours_stock < 25:
            m.alertes.append(
                f"STOCK À {num(m.jours_stock, 0)} JOURS — sous le délai fournisseur "
                f"de {DELAI_LIVRAISON_MOIS} mois, la rupture est mécanique.")
        etp_req = ETP_BASE + m.ca_ht / CA_HT_PAR_ETP
        if self.etp < etp_req * 0.75:
            m.alertes.append(
                f"SOUS-EFFECTIF : {dec(self.etp, 1)} ETP pour "
                f"{dec(etp_req, 1)} requis — la qualité créative est bridée.")
        if m.mer > 0 and m.marge_brute_pct > 0:
            # le MER se lit sur le CA TTC encaisse, la marge sur le CA HT facture
            mer_seuil = 1.20 * (1.0 - d.remise) / m.marge_brute_pct
            if m.mer < mer_seuil:
                m.alertes.append(
                    f"MER {dec(m.mer)} SOUS LE SEUIL CM3 {dec(mer_seuil)} : chaque "
                    f"euro de CA supplémentaire détruit de la marge.")

    def _verifier_fin(self, m: Mois) -> None:
        if self.issue != "en cours":
            return
        if m.tresorerie < 0:
            self.issue = "faillite"
            return
        if (m.ca_ttc_semaine >= OBJECTIF_CA_TTC_SEMAINE
                and m.ebitda_pct >= OBJECTIF_EBITDA_PCT):
            self.mois_objectif_consecutifs += 1
        else:
            self.mois_objectif_consecutifs = 0
        if self.mois_objectif_consecutifs >= MOIS_CONSECUTIFS_VICTOIRE:
            self.issue = "victoire"
            self.mois_victoire = m.mois


# ===========================================================================
# 5. LES STRATEGIES AUTOMATIQUES
# ===========================================================================

STRATEGIES = ["prudente", "agressive", "equilibree", "sans_test_crea",
              "remise_permanente"]

DESCRIPTION_STRATEGIES = {
    "prudente": "MER visé 3,00, croissance plafonnée à +20 %/mois, jamais de "
                "remise, 15 % de test créatif, trésorerie protégée.",
    "agressive": "MER visé 1,40, croissance jusqu'à +85 %/mois, 92 % de la "
                 "trésorerie engagée, 10 % de test créatif, 14 % de remise, "
                 "un seul canal à 95 %, stock au plus juste.",
    "equilibree": "MER visé 2,45, croissance plafonnée à +35 %/mois et par la "
                  "trésorerie, 15 % de test créatif, 3 % de remise (+ dérive "
                  "d'échelle), 4,5 % du CA HT en rétention, bascule sur le "
                  "pilotage de la marge à 70 % de l'objectif.",
    "sans_test_crea": "Identique à « équilibrée », sauf part_test_crea = 0. "
                      "C'est la seule différence.",
    "remise_permanente": "Identique à « équilibrée », sauf remise = 18 % en permanence. "
                         "C'est la seule différence.",
}

_PARAMS = {
    #                 croiss  part_treso  test  remise  reten  canal  seuil_ouv  couv
    "prudente":       (1.20,  0.80,       0.15, 0.00,   0.035, 0.75,  260_000,  5.0),
    "agressive":      (1.70,  0.85,       0.10, 0.14,   0.010, 0.95,  140_000,  3.4),
    "equilibree":     (1.35,  1.20,       0.15, 0.03,   0.045, 0.72,  220_000,  5.0),
    "sans_test_crea": (1.35,  1.20,       0.00, 0.03,   0.045, 0.72,  220_000,  5.0),
    "remise_permanente": (1.35, 1.20,     0.15, 0.18,   0.045, 0.72,  220_000,  5.0),
}

# Les remises montent avec l'echelle (Black Friday, codes createurs, paniers
# abandonnes) : chiffres canoniques § 2.1. On modelise +5 points entre le
# lancement et 2 M EUR de CA TTC mensuel.
REMISE_DERIVE_ECHELLE = 0.05
REMISE_CA_PLEIN = 2_000_000.0

# Premiumisation : le panier moyen est le premier levier d'EBITDA (chiffres
# canoniques § 7). Les strategies non agressives montent le prix de 1,2 % par
# mois, plafonne a +40 %, et seulement quand l'EBITDA le supporte.
# MER visé par stratégie : la cible autour de laquelle le budget média est
# asservi. C'est la décision la plus structurante d'une stratégie automatique.
MER_VISE = {"prudente": 3.00, "agressive": 1.40, "_defaut": 2.45}
MER_VISE_PILOTAGE_MARGE = 2.45

PRIX_HAUSSE_MENSUELLE = 0.012
PRIX_PRIME_MAX = 1.12

_PART_CAPITAL_M1 = {"prudente": 0.06, "agressive": 0.20, "equilibree": 0.09,
                    "sans_test_crea": 0.09, "remise_permanente": 0.09}


COUVERTURE_DEFAUT = 4.5


def commande_de_recompletement(sim: Simulateur, couverture: float,
                               budget_m1: float = 0.0) -> float:
    """Niveau de recomplètement : combien commander ce mois-ci.

    La couverture visée doit dépasser le délai fournisseur (2 mois) PLUS la
    période de révision (1 mois), sinon la rupture est arithmétique quelle que
    soit la trésorerie. La demande de référence est lissée sur trois mois :
    commander sur le dernier mois seul fait osciller toute la chaîne.
    """
    mult = sim.multiplicateur_offre()
    prec = sim.historique[-1] if sim.historique else None
    if prec is None:
        unites_prev = (budget_m1 / 28.0) * mult
    else:
        recents = [h.commandes for h in sim.historique[-3:] if h.commandes > 0]
        demande_ref = sum(recents) / len(recents) if recents else prec.commandes
        demande_ref = max(demande_ref, prec.commandes * 0.85)
        if len(sim.historique) >= 4 and sim.historique[-4].commandes > 0:
            g = borner((prec.commandes / sim.historique[-4].commandes) ** (1 / 3),
                       0.92, 1.30)
        else:
            g = 1.15
        unites_prev = demande_ref * mult * (g ** 1.5)
    en_route = sum(u for (_, u, _) in sim.livraisons)
    return max(0.0, unites_prev * couverture - sim.stock_unites - en_route)


def decider(strategie: str, sim: Simulateur) -> Decision:
    """La politique de decision d'une strategie automatique, pour le mois a venir."""
    croiss, part_treso, test, remise, reten, canal, seuil_ouv, couv = _PARAMS[strategie]
    prec = sim.historique[-1] if sim.historique else None
    mois_cal = ((sim.mois_depart - 1 + sim.mois) % 12) + 1

    # --- stock, EN PREMIER ------------------------------------------------
    # Le stock passe avant la publicité. Un euro de média dépensé sans stock
    # pour le servir est un euro perdu deux fois : la vente ne se fait pas, et
    # l'algorithme désapprend. On réserve donc l'acompte fournisseur d'abord.
    mult = sim.multiplicateur_offre()
    budget_m1 = sim.capital * _PART_CAPITAL_M1[strategie]
    commande = commande_de_recompletement(sim, couv, budget_m1)
    cout_u = sim.cogs_unitaire() * sim.acompte_fournisseur()
    if strategie != "agressive" and cout_u > 0:
        acompte_max = max(0.0, sim.tresorerie * 0.45)
        commande = min(commande, acompte_max / cout_u)
    acompte = commande * cout_u

    # --- budget publicitaire -------------------------------------------
    # Trois bornes, dans cet ordre : l'ambition de croissance, le MER visé,
    # puis la trésorerie — qui a toujours le dernier mot sauf en « agressive ».
    if prec is None:
        budget = sim.capital * _PART_CAPITAL_M1[strategie]
    else:
        mer_vise = MER_VISE.get(strategie, MER_VISE["_defaut"])
        cible_eb = {"prudente": 0.12, "agressive": -1.0}.get(strategie, 0.10)
        # Bascule P5 -> P5+ : à 70 % de l'objectif, on arrête d'acheter du volume
        # et on pilote la marge. C'est le passage décrit dans les chiffres
        # canoniques § 8 : même CA, EBITDA doublé.
        pilotage_marge = (strategie != "agressive"
                          and prec.ca_ttc_semaine >= 0.70 * OBJECTIF_CA_TTC_SEMAINE)
        if pilotage_marge:
            mer_vise = max(mer_vise, MER_VISE_PILOTAGE_MARGE)
            cible_eb = 0.17
        # Discipline de marge : on n'accélère que si l'EBITDA le permet. Les neuf
        # premiers mois sont exemptés — c'est la vallée de la mort, financée par
        # le capital et remboursée par le réachat (canoniques § 2.3).
        # Correction proportionnelle : on compare le MER réalisé au MER visé.
        # Au-dessus, on peut dépenser plus ; en dessous, on coupe. Le système
        # converge vers le MER visé au lieu de le dépasser puis de s'effondrer.
        if prec.mer > 0:
            ajust = (prec.mer / mer_vise) ** 1.30
        else:
            ajust = 0.85
        # Un compte très au-dessus de son MER visé sous-investit : il peut
        # rattraper vite, parce que repartir d'un petit budget est facile.
        plafond_vitesse = croiss * (1.8 if prec.mer > 2.0 * mer_vise else 1.0)
        vitesse = borner(ajust, 0.85, plafond_vitesse)
        # La vallée de la mort est financée par le capital : on exempte la
        # discipline de marge tant qu'il reste six mois de frais fixes au chaud.
        marge_de_manoeuvre = sim.tresorerie > prec.fixes * 6.0
        if strategie != "agressive" and not (sim.mois <= 9 and marge_de_manoeuvre):
            if prec.ebitda_pct < 0.0:
                vitesse = min(vitesse, 0.95)
            elif prec.ebitda_pct < cible_eb:
                vitesse = min(vitesse, 1.0 + (croiss - 1.0) * 0.40)
        budget = prec.budget_pub * vitesse
        plafond_treso = max(0.0, sim.tresorerie - acompte) * part_treso
        budget = min(budget, plafond_treso)
        if strategie != "agressive":
            # garde-fou : on garde toujours 2 mois de frais fixes au chaud
            budget = min(budget, max(0.0, sim.tresorerie - acompte
                                     - prec.fixes * 2.0))
            # et on ne coupe jamais de plus de 20 % d'un mois sur l'autre :
            # un compte publicitaire qui décroche perd sa phase d'apprentissage
            budget = max(budget, min(prec.budget_pub * 0.80, plafond_treso, budget * 1.0)
                         if plafond_treso > prec.budget_pub * 0.80
                         else min(prec.budget_pub * 0.80, max(budget, plafond_treso)))
        # PLAFOND STOCK — appliqué EN DERNIER, et il prime sur tout le reste.
        # On ne paie pas pour du trafic qu'on ne peut pas servir. Le garde-fou
        # anti-décrochage ci-dessus est une bonne règle en régime normal ; en
        # rupture c'est une règle qui ruine, parce qu'elle maintient la dépense
        # alors que le chiffre d'affaires est plafonné par l'entrepôt.
        # Un opérateur réel coupe. La phase d'apprentissage perdue coûte cher,
        # mais infiniment moins que trente jours de média servis à vide.
        if prec.commandes > 0 and mult > 0:
            # le stock servable le mois prochain inclut les livraisons attendues :
            # ne pas les compter briderait le compte à tort
            arrivant = sum(u for (mois_liv, u, _) in sim.livraisons
                           if mois_liv <= sim.mois + 1)
            cmd_servables = (sim.stock_unites + arrivant) / mult
            if cmd_servables < prec.commandes:
                couverture = max(0.10, cmd_servables / prec.commandes)
                budget = min(budget, prec.budget_pub * couverture)
        budget = max(1_500.0, budget)

    # --- remise : dérive d'échelle + promotion saisonnière de novembre ---
    ca_prec_ttc = prec.ca_ttc if prec else 0.0
    pilotage_marge = (prec is not None and strategie != "agressive"
                      and prec.ca_ttc_semaine >= 0.70 * OBJECTIF_CA_TTC_SEMAINE)
    if strategie == "remise_permanente":
        # Expérience à variable unique : cette stratégie est identique à
        # « équilibrée » SAUF la remise, qui reste plate à sa valeur nominale.
        # Ni dérive d'échelle, ni promotion de novembre — une marque déjà
        # remisée en permanence n'empile pas une promotion saisonnière dessus.
        # Sans cette exemption, la remise effective atteindrait 30 % et le
        # tableau comparatif ne dirait plus ce qu'il prétend dire.
        r = remise
    else:
        derive = REMISE_DERIVE_ECHELLE * (0.5 if pilotage_marge else 1.0)
        r = remise + derive * min(1.0, ca_prec_ttc / REMISE_CA_PLEIN)
        if mois_cal == 11 and not pilotage_marge:
            r = r + (0.15 if strategie == "agressive" else 0.08)
        r = min(0.30, r)

    # --- investissements -------------------------------------------------
    ca_ht_prec = prec.ca_ht if prec else 0.0
    invest_ret = reten * ca_ht_prec
    part_offre = 0.06 if sim.mois < 6 else 0.02
    invest_offre = part_offre * ca_ht_prec if prec else sim.capital * 0.03

    # --- recrutement -------------------------------------------------------
    etp_cible = ETP_BASE + ca_ht_prec / CA_HT_PAR_ETP
    ecart = etp_cible - sim.etp
    vitesse = 3.5 if strategie == "agressive" else 2.5
    recrutement = borner(ecart, -1.5, vitesse)

    # --- ouverture de marche -------------------------------------------------
    ouvrir = None
    if prec and prec.ca_ttc >= seuil_ouv and sim.tresorerie > 120_000:
        dernier = max(sim.marches.values())
        ecart_min = 2 if strategie == "agressive" else 4
        if sim.mois - dernier >= ecart_min:
            for code in ORDRE_OUVERTURE:
                if code not in sim.marches:
                    ouvrir = code
                    break

    # --- premiumisation ------------------------------------------------------
    prix = None
    if (prec is not None and strategie != "agressive" and sim.mois >= 6
            and prec.ebitda_pct >= 0.08 and not prec.rupture):
        plafond_prix = sim.cat.prix_reference * PRIX_PRIME_MAX
        prix = min(plafond_prix, sim.prix_ttc * (1 + PRIX_HAUSSE_MENSUELLE))

    return Decision(
        budget_pub=budget, part_test_crea=test, remise=r, prix_ttc=prix,
        invest_retention=invest_ret, invest_offre=invest_offre,
        commande_stock=commande, recrutement=recrutement,
        ouvrir_marche=ouvrir, part_canal_principal=canal)


def jouer_auto(strategie: str, categorie: str, prix: float, coef: float,
               capital: float, graine: int, horizon: int,
               mois_depart: int = 1) -> Partie:
    sim = Simulateur(categorie, prix, coef, capital, graine, horizon, mois_depart)
    partie = Partie(sim.cat, sim.prix_ttc, sim.coefficient, capital, graine,
                    horizon, strategie)
    for _ in range(horizon):
        sim.jouer_un_mois(decider(strategie, sim))
        if sim.issue != "en cours":
            break
    partie.historique = sim.historique
    partie.mois_joues = sim.mois
    partie.issue = sim.issue if sim.issue != "en cours" else "horizon atteint"
    partie.mois_victoire = sim.mois_victoire
    return partie


# ===========================================================================
# 6. AFFICHAGE
# ===========================================================================

ENTETE = ("Mois │   CA TTC │  Cmd │   AOV │ %Réa │      Pub │  MER │  CACm │  CACx │"
          " Qcré │ Gag │  MB % │      CM3 │   EBITDA │    Trésorerie │ JSt")
SEPAR = "─" * len(ENTETE)


def ligne_mois(m: Mois) -> str:
    return (f"{m.mois:>4} │{num(m.ca_ttc):>9} │{num(m.commandes):>5} │"
            f"{dec(m.aov_ttc, 1):>6} │{pct(m.part_reachat, 0):>5} │"
            f"{num(m.budget_pub):>9} │{dec(m.mer):>5} │{dec(m.cac_moyen, 1):>6} │"
            f"{dec(m.cac_marginal, 1):>6} │{dec(m.qualite_crea):>5} │"
            f"{m.gagnants:>4} │{pct(m.marge_brute_pct, 0):>6} │{num(m.cm3):>9} │"
            f"{num(m.ebitda):>9} │{num(m.tresorerie):>14} │"
            f"{num(min(m.jours_stock, 999), 0):>4}")


def afficher_entete_tableau() -> None:
    print(SEPAR)
    print(ENTETE)
    print(SEPAR)


def afficher_mois(m: Mois, details: bool = True) -> None:
    print(ligne_mois(m))
    if details:
        for e in m.evenements:
            print(f"       ⚑ {e}")
        for a in m.alertes:
            print(f"       ! {a}")


def legende() -> str:
    return (
        "Légende — CA TTC : encaissé, net de remise. Cmd : commandes. AOV : panier "
        "moyen TTC.\n"
        "%Réa : part des commandes en réachat. MER : CA TTC ÷ dépense pub. "
        "CACm : coût d'acquisition\nmoyen d'un NOUVEAU client. CACx : coût "
        "d'acquisition MARGINAL (= CACm ÷ 0,72). Qcré : qualité\ncréative [0,55 ; "
        "1,45]. Gag : concepts gagnants vivants. MB % : marge brute (CM2) en % du "
        "CA HT\nfacturé. CM3 : marge brute − pub. JSt : jours de stock. Tous les "
        "montants sont en euros."
    )


def afficher_creation(sim: Simulateur, capital: float) -> None:
    c = sim.cat
    print(SEPAR)
    print(f"TOUR 0 — LA CRÉATION")
    print(SEPAR)
    print(f"  Catégorie ................. {c.libelle} ({c.code})")
    print(f"  Prix de vente ............. {eur(sim.prix_ttc, 2)} TTC "
          f"(soit {eur(sim.prix_ttc / 1.2, 2)} HT)")
    print(f"  Coefficient visé .......... ×{dec(sim.coefficient)} "
          f"(plafond catégorie ×{dec(c.coef_max)})")
    print(f"  Coût de revient unitaire .. {eur(sim.prix_ttc / sim.coefficient, 2)} "
          f"HT rendu entrepôt, avant paliers de volume")
    print(f"  Capital de départ ......... {eur(capital)}")
    print(f"  Réachat de la catégorie ... un client recommande tous les "
          f"{dec(c.freq_reachat_mois, 1)} mois en moyenne")
    print(f"  Taux de retour ............ {pct(c.taux_retour)}")
    print(f"  Logistique ................ {pct(c.part_logistique)} du CA HT au tarif plancher")
    print(f"  Marché adressable France .. {eur(c.taille_marche)} TTC/an")
    print(f"  CPM de référence .......... {eur(c.cpm_base, 2)}")
    print(SEPAR)


def afficher_bilan(p: Partie) -> None:
    d = p.dernier
    print(SEPAR)
    print(f"BILAN — {p.strategie.upper()} · {p.categorie.libelle} · "
          f"graine {p.graine}")
    print(SEPAR)
    verdict = {"victoire": "VICTOIRE", "faillite": "FAILLITE — trésorerie négative",
               "horizon atteint": "HORIZON ATTEINT sans victoire"}
    print(f"  Issue ..................... {verdict.get(p.issue, p.issue)}")
    print(f"  Mois joués ................ {p.mois_joues} / {p.horizon}")
    if p.mois_victoire:
        print(f"  Objectif atteint au mois .. {p.mois_victoire}")
    if d:
        print(f"  CA TTC du dernier mois .... {eur(d.ca_ttc)} "
              f"(soit {eur(d.ca_ttc_semaine)} / semaine)")
        print(f"  Meilleure semaine ......... {eur(p.ca_ttc_semaine_max())} TTC")
        print(f"  EBITDA du dernier mois .... {eur(d.ebitda)} "
              f"({pct(d.ebitda_pct)} du CA HT)")
        print(f"  Marge brute (CM2) ......... {pct(d.marge_brute_pct)}")
        print(f"  MER ....................... {dec(d.mer)}")
        print(f"  CAC moyen / marginal ...... {eur(d.cac_moyen, 2)} / "
              f"{eur(d.cac_marginal, 2)}")
        print(f"  Qualité créative .......... {dec(d.qualite_crea)} "
              f"({d.gagnants} gagnants vivants)")
        print(f"  Part du CA en réachat ..... {pct(d.part_reachat)}")
        print(f"  Marchés ouverts ........... {d.marches}")
    print(f"  Trésorerie finale ......... {eur(p.historique[-1].tresorerie) if p.historique else eur(p.capital)}")
    print(f"  Trésorerie minimale ....... {eur(p.tresorerie_min)}")
    cumul_ebitda = sum(m.ebitda for m in p.historique)
    cumul_ca = sum(m.ca_ttc for m in p.historique)
    print(f"  CA TTC cumulé ............. {eur(cumul_ca)}")
    print(f"  EBITDA cumulé ............. {eur(cumul_ebitda)}")
    print(SEPAR)


# ===========================================================================
# 7. MODE --comparer
# ===========================================================================

def comparer(categorie: str, prix: float, coef: float, capital: float,
             graine: int, horizon: int, mois_depart: int = 1) -> List[Partie]:
    parties = [jouer_auto(s, categorie, prix, coef, capital, graine, horizon,
                          mois_depart) for s in STRATEGIES]
    return parties


def tableau_comparatif(parties: List[Partie]) -> str:
    lignes = []
    e = ("Stratégie          │ Mois │ Issue            │ CA TTC/sem (6 mois) │"
         " Meilleure sem. │ EBITDA %│  Tréso. min │ EBITDA cumulé │ Qcré")
    s = "─" * len(e)
    lignes.append(s)
    lignes.append(e)
    lignes.append(s)
    for p in parties:
        d = p.dernier
        issue = {"victoire": "victoire", "faillite": "faillite (cash)",
                 "horizon atteint": "horizon atteint"}.get(p.issue, p.issue)
        ca_sem = p.moyenne_fin("ca_ttc_semaine")
        eb = p.ebitda_pct_fin()
        q = d.qualite_crea if d else 0.0
        cum = sum(m.ebitda for m in p.historique)
        lignes.append(
            f"{p.strategie:<18} │ {p.mois_joues:>4} │ {issue:<16} │"
            f" {num(ca_sem):>19} │ {num(p.ca_ttc_semaine_max()):>14} │"
            f" {pct(eb, 1):>7} │ {num(p.tresorerie_min):>11} │"
            f" {num(cum):>13} │ {dec(q):>4}")
    lignes.append(s)
    return "\n".join(lignes)


# ===========================================================================
# 8. MODE --scenario
# ===========================================================================

def charger_scenario(chemin: str) -> dict:
    with open(chemin, "r", encoding="utf-8") as f:
        return json.load(f)


def decision_depuis_json(bloc: dict, base: Decision) -> Decision:
    d = replace(base)
    for cle in ("budget_pub", "part_test_crea", "remise", "invest_retention",
                "invest_offre", "commande_stock", "recrutement", "prix_ttc",
                "part_canal_principal"):
        if cle in bloc:
            setattr(d, cle, float(bloc[cle]))
    d.ouvrir_marche = bloc.get("ouvrir_marche")
    return d


def recrutement_automatique(sim: Simulateur, d: Decision) -> Decision:
    """Ajuste l'effectif au besoin, quand le scénario ne le pilote pas."""
    ca_ht = sim.historique[-1].ca_ht if sim.historique else 0.0
    cible = ETP_BASE + ca_ht / CA_HT_PAR_ETP
    d.recrutement = borner(cible - sim.etp, -1.5, 2.5)
    return d


def reappro_automatique(sim: Simulateur, d: Decision) -> Decision:
    """Complète le stock au niveau de recomplètement quand le scénario ne le fait pas."""
    d.commande_stock = commande_de_recompletement(sim, COUVERTURE_DEFAUT, d.budget_pub)
    return d


def jouer_scenario(chemin: str, graine_cli: Optional[int] = None) -> Partie:
    sc = charger_scenario(chemin)
    graine = graine_cli if graine_cli is not None else int(sc.get("graine", 1))
    horizon = int(sc.get("horizon", 24))
    sim = Simulateur(sc["categorie"], float(sc["prix_ttc"]),
                     float(sc["coefficient"]), float(sc["capital"]),
                     graine, horizon, int(sc.get("mois_depart", 1)))
    partie = Partie(sim.cat, sim.prix_ttc, sim.coefficient, float(sc["capital"]),
                    graine, horizon, sc.get("nom", os.path.basename(chemin)))
    blocs = {int(b["mois"]): b for b in sc.get("decisions", [])}
    auto = bool(sc.get("reappro_auto", False))
    courante = Decision()
    for mois in range(1, horizon + 1):
        if mois in blocs:
            courante = decision_depuis_json(blocs[mois], courante)
        else:
            # Report d'un mois sur l'autre : une ouverture de marché, un
            # changement de prix, un investissement d'offre et un recrutement
            # sont des actes PONCTUELS. Le reste se reconduit.
            courante = replace(courante, ouvrir_marche=None, prix_ttc=None,
                               invest_offre=0.0, recrutement=0.0)
        d = replace(courante)
        if auto:
            d = reappro_automatique(sim, d)
        if bool(sc.get("recrutement_auto", False)) and "recrutement" not in blocs.get(mois, {}):
            d = recrutement_automatique(sim, d)
        sim.jouer_un_mois(d)
        if sim.issue != "en cours":
            break
    partie.historique = sim.historique
    partie.mois_joues = sim.mois
    partie.issue = sim.issue if sim.issue != "en cours" else "horizon atteint"
    partie.mois_victoire = sim.mois_victoire
    return partie


# ===========================================================================
# 9. MODE --interactif
# ===========================================================================

def demander(question: str, defaut: float, unite: str = "") -> float:
    txt = f"  {question} [{dec(defaut, 2)}{unite}] > "
    try:
        rep = input(txt)
    except EOFError:
        print()
        return defaut
    try:
        return lire_nombre(rep, defaut)
    except ValueError:
        print("    Valeur illisible, on garde la valeur par défaut.")
        return defaut


def jouer_interactif(categorie: str, prix: float, coef: float, capital: float,
                     graine: int, horizon: int, mois_depart: int = 1) -> Partie:
    sim = Simulateur(categorie, prix, coef, capital, graine, horizon, mois_depart)
    partie = Partie(sim.cat, sim.prix_ttc, sim.coefficient, capital, graine,
                    horizon, "interactif")
    afficher_creation(sim, capital)
    print(legende())
    d = Decision(budget_pub=capital * 0.08, part_test_crea=0.15,
                 invest_offre=capital * 0.03)
    for mois in range(1, horizon + 1):
        print()
        print(f"══ MOIS {mois} ── trésorerie {eur(sim.tresorerie)} ── "
              f"stock {num(sim.stock_unites)} unités ── "
              f"{len(sim.gagnants)} gagnants créatifs vivants")
        d = replace(d, ouvrir_marche=None, prix_ttc=None)
        d.budget_pub = demander("Budget publicitaire du mois", d.budget_pub, " €")
        d.part_test_crea = borner(
            demander("Part du budget en test créatif (0 à 30)",
                     d.part_test_crea * 100, " %") / 100, 0.0, 0.30)
        d.remise = borner(demander("Remise moyenne accordée (0 à 30)",
                                   d.remise * 100, " %") / 100, 0.0, 0.30)
        d.invest_retention = demander("Investissement rétention (CRM, contenu)",
                                      d.invest_retention, " €")
        d.invest_offre = demander("Investissement offre (bundles, upsell)", 0.0, " €")
        d.commande_stock = demander("Unités commandées au fournisseur",
                                    d.commande_stock, " unités")
        d.recrutement = demander("Variation d'ETP (négatif = départ)", 0.0, " ETP")
        try:
            pays = input("  Ouvrir un marché (BE/DE/ES/IT/NL/UK ou vide) > ").strip()
        except EOFError:
            pays = ""
        d.ouvrir_marche = pays.upper() if pays else None
        nouveau_prix = demander("Prix de vente TTC", sim.prix_ttc, " €")
        d.prix_ttc = nouveau_prix
        m = sim.jouer_un_mois(d)
        print()
        afficher_entete_tableau()
        afficher_mois(m)
        print(SEPAR)
        if sim.issue != "en cours":
            break
    partie.historique = sim.historique
    partie.mois_joues = sim.mois
    partie.issue = sim.issue if sim.issue != "en cours" else "horizon atteint"
    partie.mois_victoire = sim.mois_victoire
    afficher_bilan(partie)
    return partie


# ===========================================================================
# 10. MODE --rapport
# ===========================================================================

def ecrire_rapport(parties: List[Partie], chemin: str, titre: str) -> None:
    L: List[str] = []
    L.append(f"# {titre}")
    L.append("")
    L.append("> Rapport produit par `ecommerce/outils/simulateur_marque.py`. "
             "Simulation d'une marque **fictive** : les chiffres sont un modèle "
             "calibré sur les [chiffres canoniques]"
             "(../donnees/chiffres-canoniques.md), pas les comptes d'une "
             "entreprise réelle.")
    L.append("")
    p0 = parties[0]
    L.append(f"**Catégorie :** {p0.categorie.libelle} · **Prix :** "
             f"{eur(p0.prix_ttc, 2)} TTC · **Coefficient :** ×{dec(p0.coefficient)} "
             f"· **Capital :** {eur(p0.capital)} · **Graine :** {p0.graine} "
             f"· **Horizon :** {p0.horizon} mois")
    L.append("")
    if len(parties) > 1:
        L.append("## Tableau comparatif final")
        L.append("")
        L.append("| Stratégie | Mois | Issue | CA TTC/sem. (moy. 6 derniers mois) "
                 "| Meilleure semaine | EBITDA % CA HT (6 derniers mois) "
                 "| Trésorerie min. | CA TTC cumulé | EBITDA cumulé | Qualité créa |")
        L.append("|---|---:|---|---:|---:|---:|---:|---:|---:|---:|")
        for p in parties:
            d = p.dernier
            cum = sum(m.ebitda for m in p.historique)
            cumca = sum(m.ca_ttc for m in p.historique)
            L.append(f"| {p.strategie} | {p.mois_joues} | {p.issue} | "
                     f"{eur(p.moyenne_fin('ca_ttc_semaine'))} | "
                     f"{eur(p.ca_ttc_semaine_max())} | "
                     f"{pct(p.ebitda_pct_fin())} | "
                     f"{eur(p.tresorerie_min)} | {eur(cumca)} | {eur(cum)} | "
                     f"{dec(d.qualite_crea) if d else '—'} |")
        L.append("")
    for p in parties:
        L.append(f"## Déroulé — stratégie « {p.strategie} »")
        L.append("")
        if p.strategie in DESCRIPTION_STRATEGIES:
            L.append(f"*{DESCRIPTION_STRATEGIES[p.strategie]}*")
            L.append("")
        L.append("| Mois | CA TTC | Cmd | AOV TTC | % réachat | Pub | MER | CAC moy. "
                 "| CAC marg. | Qualité créa | Gagnants | Marge brute | CM3 | EBITDA "
                 "| Trésorerie | Jours stock |")
        L.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:"
                 "|---:|---:|---:|")
        for m in p.historique:
            L.append(
                f"| {m.mois} | {eur(m.ca_ttc)} | {num(m.commandes)} | "
                f"{eur(m.aov_ttc, 2)} | {pct(m.part_reachat)} | {eur(m.budget_pub)} | "
                f"{dec(m.mer)} | {eur(m.cac_moyen, 2)} | {eur(m.cac_marginal, 2)} | "
                f"{dec(m.qualite_crea)} | {m.gagnants} | {pct(m.marge_brute_pct)} | "
                f"{eur(m.cm3)} | {eur(m.ebitda)} | {eur(m.tresorerie)} | "
                f"{num(min(m.jours_stock, 999), 0)} |")
        L.append("")
        evts = [(m.mois, e) for m in p.historique for e in m.evenements]
        if evts:
            L.append("### Événements")
            L.append("")
            for mois, e in evts:
                L.append(f"- **M{mois}** — {e}")
            L.append("")
        alertes = [(m.mois, a) for m in p.historique for a in m.alertes]
        if alertes:
            L.append("### Alertes")
            L.append("")
            for mois, a in alertes[:120]:
                L.append(f"- **M{mois}** — {a}")
            if len(alertes) > 120:
                L.append(f"- … et {len(alertes) - 120} alertes de plus.")
            L.append("")
    L.append("*Fin du rapport.*")
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


# ===========================================================================
# 11. MODE --verifier — les quatre comportements que le simulateur doit produire
# ===========================================================================

def phase_moyenne(p: Partie, deb: int, fin: int, champ: str) -> float:
    vals = [getattr(m, champ) for m in p.historique
            if deb <= m.mois <= fin and m.ca_ht > 0]
    return sum(vals) / len(vals) if vals else 0.0


def verifier(categorie: str, prix: float, coef: float, capital: float,
             graine: int, horizon: int, n_graines: int = 40) -> int:
    print(SEPAR)
    print("VÉRIFICATION DES QUATRE COMPORTEMENTS ATTENDUS")
    print(SEPAR)
    echecs = 0

    parties = {p.strategie: p for p in comparer(categorie, prix, coef, capital,
                                                graine, horizon)}
    eq, st = parties["equilibree"], parties["sans_test_crea"]
    rp, ag = parties["remise_permanente"], parties["agressive"]

    # (a) sans_test_crea nettement plus mal que equilibree
    eb_eq = sum(m.ebitda for m in eq.historique)
    eb_st = sum(m.ebitda for m in st.historique)
    ca_eq = sum(m.ca_ttc for m in eq.historique)
    ca_st = sum(m.ca_ttc for m in st.historique)
    q_eq = eq.dernier.qualite_crea if eq.dernier else 0
    q_st = st.dernier.qualite_crea if st.dernier else 0
    ok_a = (ca_st < ca_eq * 0.70) and (eb_st < eb_eq) and (q_st < q_eq)
    echecs += 0 if ok_a else 1
    print(f"(a) sans_test_crea vs equilibree ........... "
          f"{'OK' if ok_a else 'ÉCHEC'}")
    print(f"    CA TTC cumulé      : {eur(ca_st):>18} contre {eur(ca_eq)} "
          f"({pct(ca_st / ca_eq - 1)})")
    print(f"    EBITDA cumulé      : {eur(eb_st):>18} contre {eur(eb_eq)}")
    print(f"    Qualité créative   : {dec(q_st):>18} contre {dec(q_eq)}")
    print(f"    Issue              : {st.issue:>18} contre {eq.issue}")

    # (b) agressive : la rupture de tresorerie doit etre le cas LE PLUS PROBABLE,
    # sans etre certaine. Une strategie agressive qui echouerait a tous les coups
    # n'enseignerait rien : personne ne la choisirait dans la vraie vie. Ce qui la
    # rend dangereuse, c'est precisement qu'elle marche parfois. La bande visee est
    # donc [50 % ; 85 %] de faillites — plus souvent qu'un tirage a pile ou face,
    # jamais systematiquement.
    ruptures = 0
    mois_survie = []
    for g in range(graine, graine + n_graines):
        pa = jouer_auto("agressive", categorie, prix, coef, capital, g, horizon)
        if pa.issue == "faillite":
            ruptures += 1
            mois_survie.append(len(pa.historique))
    taux = ruptures / n_graines
    ok_b = 0.50 <= taux <= 0.85
    echecs += 0 if ok_b else 1
    print(f"(b) agressive : rupture de trésorerie ...... "
          f"{'OK' if ok_b else 'ÉCHEC'}")
    print(f"    {ruptures} faillites sur {n_graines} graines, soit {pct(taux)} "
          f"(bande attendue : 50 % à 85 %)")
    if mois_survie:
        med = sorted(mois_survie)[len(mois_survie) // 2]
        print(f"    Survie médiane avant faillite : {med} mois")
    print("    Lecture : l'agressivité n'échoue pas toujours — c'est exactement")
    print("    pour ça qu'elle est dangereuse. Elle marche assez souvent pour")
    print("    être imitée, et rate assez souvent pour ruiner qui l'imite.")

    # (c) remise_permanente : du CA, peu d'EBITDA
    ca_rp = sum(m.ca_ttc for m in rp.historique)
    eb_rp = sum(m.ebitda for m in rp.historique)
    mois_communs = min(len(rp.historique), len(eq.historique))
    ca_eq_c = sum(m.ca_ttc for m in eq.historique[:mois_communs])
    eb_eq_c = sum(m.ebitda for m in eq.historique[:mois_communs])
    ca_rp_c = sum(m.ca_ttc for m in rp.historique[:mois_communs])
    eb_rp_c = sum(m.ebitda for m in rp.historique[:mois_communs])
    mb_rp = phase_moyenne(rp, 1, rp.mois_joues, "marge_brute_pct")
    mb_eq = phase_moyenne(eq, 1, eq.mois_joues, "marge_brute_pct")
    ok_c = (eb_rp_c < eb_eq_c) and (mb_rp < mb_eq - 0.10)
    echecs += 0 if ok_c else 1
    rendement_rp = (eb_rp_c / ca_rp_c) if ca_rp_c > 0 else 0.0
    rendement_eq = (eb_eq_c / ca_eq_c) if ca_eq_c > 0 else 0.0
    print(f"(c) remise_permanente : CA sans EBITDA ..... "
          f"{'OK' if ok_c else 'ÉCHEC'}")
    print(f"    Sur {mois_communs} mois communs — CA TTC : {eur(ca_rp_c)} contre "
          f"{eur(ca_eq_c)}")
    print(f"    EBITDA cumulé      : {eur(eb_rp_c):>18} contre {eur(eb_eq_c)}")
    print(f"    Marge brute moyenne: {pct(mb_rp):>18} contre {pct(mb_eq)}")
    print(f"    EBITDA par € de CA : {pct(rendement_rp):>18} contre "
          f"{pct(rendement_eq)}")

    # (d) ordres de grandeur canoniques sur equilibree / soin_cheveux
    mb = [m.marge_brute_pct for m in eq.historique if m.ca_ht > 0]
    mers = [m.mer for m in eq.historique
            if m.mer > 0 and m.mois >= 4 and m.budget_pub > 5_000]
    mb_min, mb_max = (min(mb), max(mb)) if mb else (0, 0)
    mb_moy = sum(mb) / len(mb) if mb else 0
    part_dans_bande = sum(1 for x in mb if 0.55 <= x <= 0.65) / len(mb) if mb else 0
    mers_tries = sorted(mers)
    mediane_mer = mers_tries[len(mers_tries) // 2] if mers_tries else 0.0
    mature = [m.mer for m in eq.historique
              if m.mois >= 18 and m.mer > 0 and m.budget_pub > 5_000]
    mer_mature = sum(mature) / len(mature) if mature else 0.0
    # La phase mature contient le basculement P5 -> P5+ : le MER canonique y
    # passe de 2,90 à 3,40 (chiffres canoniques § 8). La borne haute de la
    # phase mature est donc 3,40 et non 3,00.
    ok_d = (0.57 <= mb_moy <= 0.62) and part_dans_bande >= 0.80 \
        and 1.8 <= mediane_mer <= 3.0 and 1.8 <= mer_mature <= 3.4
    echecs += 0 if ok_d else 1
    print(f"(d) ordres de grandeur canoniques .......... "
          f"{'OK' if ok_d else 'ÉCHEC'}")
    print(f"    Marge brute (CM2)  : moyenne {pct(mb_moy)}, "
          f"amplitude {pct(mb_min)} à {pct(mb_max)}, "
          f"{pct(part_dans_bande, 0)} des mois dans [55 % ; 65 %]")
    print(f"    MER                : médiane {dec(mediane_mer)} sur M4+ "
          f"(cible canonique 1,80 à 3,00), moyenne de la phase mature M18+ "
          f"{dec(mer_mature)}")
    print(f"                         (la phase mature contient le basculement "
          f"P5 → P5+, où le MER canonique passe de 2,90 à 3,40)")
    print(SEPAR)
    print(f"{4 - echecs} vérification(s) sur 4 réussie(s).")
    print(SEPAR)
    return echecs


# ===========================================================================
# 12. LIGNE DE COMMANDE
# ===========================================================================

def construire_parseur() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="simulateur_marque.py",
        description="Simulateur de marque e-commerce — joue la création d'une "
                    "marque DTC mois par mois et mesure les conséquences.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Catégories : " + ", ".join(CATEGORIES) +
               "\nStratégies : " + ", ".join(STRATEGIES))
    p.add_argument("--interactif", action="store_true",
                   help="joue tour par tour dans le terminal")
    p.add_argument("--scenario", metavar="X.json",
                   help="rejoue une suite de décisions écrite dans un fichier")
    p.add_argument("--auto", metavar="STRATEGIE", choices=STRATEGIES,
                   help="joue seul une stratégie automatique")
    p.add_argument("--comparer", action="store_true",
                   help="lance les cinq stratégies sur la même graine")
    p.add_argument("--verifier", action="store_true",
                   help="vérifie les quatre comportements attendus du modèle")
    p.add_argument("--rapport", metavar="FICHIER.md",
                   help="écrit le déroulé complet en markdown")
    p.add_argument("--graine", type=int, default=7, help="graine aléatoire")
    p.add_argument("--categorie", default="soin_cheveux", choices=list(CATEGORIES))
    p.add_argument("--prix", type=float, default=39.0, help="prix de vente TTC")
    p.add_argument("--coef", type=float, default=8.0, help="coefficient visé")
    p.add_argument("--capital", type=float, default=250_000.0,
                   help="capital de départ en euros (défaut : pertes cumulées "
                        "P1+P2 + BFR de P2 des chiffres canoniques)")
    p.add_argument("--mois", type=int, default=HORIZON_DEFAUT,
                   help="horizon en mois")
    p.add_argument("--mois-depart", type=int, default=1,
                   help="mois calendaire du lancement (1 = janvier)")
    p.add_argument("--graines", type=int, default=40,
                   help="nombre de graines pour --verifier (test b)")
    p.add_argument("--muet", action="store_true",
                   help="n'affiche pas le déroulé mois par mois")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    a = construire_parseur().parse_args(argv)
    commun = dict(categorie=a.categorie, prix=a.prix, coef=a.coef,
                  capital=a.capital, graine=a.graine, horizon=a.mois)

    if a.verifier:
        echecs = verifier(n_graines=a.graines, **commun)
        return 1 if echecs else 0

    if a.comparer:
        parties = comparer(mois_depart=a.mois_depart, **commun)
        sim0 = Simulateur(a.categorie, a.prix, a.coef, a.capital, a.graine, a.mois)
        afficher_creation(sim0, a.capital)
        for p in parties:
            print()
            print(f"── stratégie « {p.strategie} » — "
                  f"{DESCRIPTION_STRATEGIES[p.strategie]}")
            if not a.muet:
                afficher_entete_tableau()
                for m in p.historique:
                    afficher_mois(m, details=False)
                print(SEPAR)
            afficher_bilan(p)
        print()
        print("TABLEAU COMPARATIF — cinq stratégies, même graine, mêmes paramètres")
        print(tableau_comparatif(parties))
        print()
        print(legende())
        if a.rapport:
            ecrire_rapport(parties, a.rapport,
                           f"Comparaison des cinq stratégies — "
                           f"{parties[0].categorie.libelle}, graine {a.graine}")
            print(f"\nRapport écrit : {a.rapport}")
        return 0

    if a.auto:
        p = jouer_auto(a.auto, mois_depart=a.mois_depart, **commun)
        sim0 = Simulateur(a.categorie, a.prix, a.coef, a.capital, a.graine, a.mois)
        afficher_creation(sim0, a.capital)
        print(f"Stratégie « {a.auto} » — {DESCRIPTION_STRATEGIES[a.auto]}")
        if not a.muet:
            afficher_entete_tableau()
            for m in p.historique:
                afficher_mois(m)
            print(SEPAR)
        afficher_bilan(p)
        print()
        print(legende())
        if a.rapport:
            ecrire_rapport([p], a.rapport,
                           f"Partie « {a.auto} » — {p.categorie.libelle}, "
                           f"graine {a.graine}")
            print(f"\nRapport écrit : {a.rapport}")
        return 0

    if a.scenario:
        p = jouer_scenario(a.scenario, a.graine if "--graine" in sys.argv else None)
        print(f"Scénario : {p.strategie}")
        if not a.muet:
            afficher_entete_tableau()
            for m in p.historique:
                afficher_mois(m)
            print(SEPAR)
        afficher_bilan(p)
        print()
        print(legende())
        if a.rapport:
            ecrire_rapport([p], a.rapport, f"Scénario « {p.strategie} »")
            print(f"\nRapport écrit : {a.rapport}")
        return 0

    if a.interactif:
        jouer_interactif(mois_depart=a.mois_depart, **commun)
        return 0

    construire_parseur().print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
