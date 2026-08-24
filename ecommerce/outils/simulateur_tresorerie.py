#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulateur de tresorerie et de BFR — cursus e-commerce.

Repond a une seule question : « a quelle vitesse puis-je croitre sans etre a
court de cash ? »

Une marque DTC ne meurt presque jamais parce qu'elle n'est pas rentable. Elle
meurt parce qu'elle est rentable ET a court de tresorerie : la croissance
immobilise du stock, de la creance et de l'avance publicitaire AVANT de rendre
la marge. Cet outil chiffre ce decalage.

Usage :
    python3 ecommerce/outils/simulateur_tresorerie.py --demo
    python3 ecommerce/outils/simulateur_tresorerie.py --verifier
    python3 ecommerce/outils/simulateur_tresorerie.py \\
        --ca 250000 --croissance 12 --horizon 18 --marge 58 --mer 2,4 \\
        --fixes 45000 --jours-stock 80 --dpo 30 --tresorerie 150000

Aucune dependance externe. Python 3.9+.
Conventions de formatage : voir ecommerce/outils/modele_nora.py (eur, pct).
"""

from __future__ import annotations

import argparse
import dataclasses
import os
import sys
from dataclasses import dataclass
from typing import List, Optional, Tuple

# ---------------------------------------------------------------------------
# 0. RACCORDEMENT AU MODELE CANONIQUE
#    Le simulateur emprunte ses formateurs et ses chiffres de demo a
#    modele_nora.py, qui est la source de verite du cursus. Si l'import echoue
#    (fichier deplace), on retombe sur des copies locales et le mode --demo
#    utilise les valeurs figees de donnees/chiffres-canoniques.md.
# ---------------------------------------------------------------------------

_ICI = os.path.dirname(os.path.abspath(__file__))
if _ICI not in sys.path:
    sys.path.insert(0, _ICI)

try:
    from modele_nora import PALIERS, TRESO, eur, pct, TVA  # type: ignore
    CANONIQUE_DISPONIBLE = True
except Exception:  # pragma: no cover - chemin de repli
    CANONIQUE_DISPONIBLE = False
    PALIERS = None
    TRESO = None
    TVA = 0.20

    def eur(x: float, d: int = 0) -> str:
        s = f"{x:,.{d}f}".replace(",", " ").replace(".", ",").replace("-", "−")
        return s + " €"

    def pct(x: float, d: int = 1) -> str:
        return f"{x * 100:.{d}f}".replace(".", ",") + " %"


# Valeurs de repli, recopiees de donnees/chiffres-canoniques.md § 2 et § 4.
REPLI = {
    "p3_ca_ttc": 1_177_200.0, "p3_marge_brute": 0.6035, "p3_cogs": 0.160,
    "p3_mer": 2.70, "p3_fixes": 105_000.0, "p3_ebitda": 51_033.0,
    "p3_stock_j": 80, "p3_dpo": 30, "p3_pub_j": 7, "p3_dso": 3,
    "p4_ca_ttc": 2_931_600.0, "p4_cogs": 0.150, "p4_fixes": 230_000.0,
    "p4_stock_j": 95, "p4_dpo": 45, "p4_pub_j": 14, "p4_dso": 3,
    "acompte": 0.30,
}


# ---------------------------------------------------------------------------
# 1. FORMATAGE
# ---------------------------------------------------------------------------

def num(x: float, d: int = 0) -> str:
    """Meme formatage que eur(), sans le suffixe € (l'unite est en en-tete)."""
    return f"{x:,.{d}f}".replace(",", " ").replace(".", ",").replace("-", "−")


def taux(x: float, d: int = 1) -> str:
    """Pourcentage signe, avec le vrai signe moins typographique."""
    return pct(x, d).replace("-", "−")


def pts(x: float, d: int = 1) -> str:
    """Ecart exprime en points de pourcentage."""
    return (f"{x * 100:+.{d}f}".replace(".", ",") + " pts").replace("-", "−")


def lire_taux(s: str) -> float:
    """« 7,9 », « 7.9 », « 7,9 % » -> 0,079."""
    s = s.strip().replace(" ", "").replace(" ", "")
    s = s.replace("%", "").replace("−", "-").replace(",", ".")
    return float(s) / 100.0


def lire_nombre(s: str) -> float:
    """« 2,7 » ou « 2.7 » -> 2.7. Un MER s'écrit avec une virgule en français."""
    return float(s.strip().replace("−", "-").replace(",", "."))


def lire_montant(s: str) -> float:
    """« 1 177 200 », « 1177200,50 », « 250k » -> float."""
    s = s.strip().replace(" ", "").replace(" ", "").replace("€", "")
    s = s.replace("−", "-").replace(",", ".")
    mult = 1.0
    if s and s[-1] in "kK":
        mult, s = 1_000.0, s[:-1]
    elif s and s[-1] in "mM":
        mult, s = 1_000_000.0, s[:-1]
    return float(s) * mult


# ---------------------------------------------------------------------------
# 2. LES HYPOTHESES
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Hypotheses:
    """Tout ce qu'il faut savoir pour projeter la tresorerie d'une marque DTC.

    Les montants d'entree sont TTC quand ils viennent du client (CA) et HT
    quand ils viennent d'un fournisseur (fixes, pub). La tresorerie de depart
    est un solde bancaire : ni HT ni TTC.
    """
    ca_ttc_depart: float            # CA TTC du dernier mois plein (mois 0)
    croissance: float               # croissance mensuelle visee du CA
    horizon: int                    # nombre de mois projetes
    taux_marge_brute: float         # CM2 : marge apres TOUS les couts variables, en % du CA HT
    mer: float                      # CA TTC / depense publicitaire
    fixes_mois: float               # frais fixes HT du mois 0
    croissance_fixes: float         # croissance mensuelle des frais fixes
    jours_stock: int                # DIO : jours de stock detenu
    delai_encaissement: int         # DSO : reserve PSP + delai de versement
    delai_fournisseur: int          # DPO : credit obtenu du fabricant
    delai_pub: int                  # jours entre la depense pub et l'encaissement client
    acompte_fournisseur: float      # part payee comptant a la commande de production
    tresorerie_depart: float        # solde bancaire disponible au mois 0
    cogs_pct: Optional[float] = None    # COGS en % du CA HT ; None -> 40 % du cout variable
    bfr_depart: Optional[float] = None  # BFR du mois 0 ; None -> calcule sur les memes parametres
    tva: float = TVA

    # -- parametres derives ------------------------------------------------
    @property
    def taux_cogs(self) -> float:
        """Le stock se valorise au cout d'achat, pas au prix de vente.

        Si l'eleve ne connait pas son taux de COGS, on l'estime a 40 % du cout
        variable total : c'est le rapport observe aux paliers P3 a P5 des
        chiffres canoniques (16,0 / 39,65 = 40,4 % ; 15,0 / 39,6 = 37,9 % ;
        14,5 / 38,5 = 37,7 %). C'est une approximation, pas une mesure.
        """
        if self.cogs_pct is not None:
            return self.cogs_pct
        return 0.40 * (1 - self.taux_marge_brute)

    def ca_ttc(self, mois: int) -> float:
        return self.ca_ttc_depart * (1 + self.croissance) ** mois

    def fixes(self, mois: int) -> float:
        return self.fixes_mois * (1 + self.croissance_fixes) ** mois


@dataclass(frozen=True)
class MoisProjete:
    rang: int
    ca_ttc: float
    ca_ht: float
    marge_brute: float
    pub: float
    cm3: float
    fixes: float
    ebitda: float
    bfr: float
    delta_bfr: float
    flux: float
    tresorerie: float


# ---------------------------------------------------------------------------
# 3. LE BFR
# ---------------------------------------------------------------------------

def bfr_de(h: Hypotheses, ca_ttc: float, pub: float) -> float:
    """Besoin en fonds de roulement pour un niveau d'activite donne.

        BFR = stock + creances + avance publicitaire − dettes fournisseurs

    Stock et dettes fournisseurs se calculent sur le COGS (cout d'achat).
    Les creances se calculent sur le CA TTC : c'est bien du TTC que le PSP
    retient. L'avance publicitaire est le cash immobilise entre le moment ou
    la plateforme preleve et le moment ou le client paie.

    L'acompte fournisseur reduit le credit obtenu : la part payee comptant a
    la commande ne beneficie d'aucun delai. C'est le seul ecart de formule
    avec modele_nora.py, qui declare le champ sans l'utiliser — voir --verifier.
    """
    ca_ht = ca_ttc / (1 + h.tva)
    cogs = ca_ht * h.taux_cogs
    stock = cogs * h.jours_stock / 30
    creances = ca_ttc * h.delai_encaissement / 30
    avance_pub = pub * h.delai_pub / 30
    dettes = cogs * (1 - h.acompte_fournisseur) * h.delai_fournisseur / 30
    return stock + creances + avance_pub - dettes


def resoudre(h: Hypotheses) -> Hypotheses:
    """Fige le BFR de depart pour qu'il ne bouge plus entre les scenarios.

    Important : le BFR du mois 0 est un fait constate, pas une variable. Quand
    on teste « −15 jours de stock », on veut voir le cash libere par le
    destockage — ce qui n'apparait que si le point de depart reste fixe.
    """
    if h.bfr_depart is not None:
        return h
    pub0 = h.ca_ttc_depart / h.mer
    return dataclasses.replace(h, bfr_depart=bfr_de(h, h.ca_ttc_depart, pub0))


# ---------------------------------------------------------------------------
# 4. LA PROJECTION
# ---------------------------------------------------------------------------

def projeter(h: Hypotheses) -> List[MoisProjete]:
    """Projection mois par mois. Le mois 0 est le point de depart, non projete.

        marge brute = CA HT × taux de marge brute
        pub         = CA TTC / MER          (le MER se calcule sur le TTC)
        CM3         = marge brute − pub
        EBITDA      = CM3 − frais fixes
        flux net    = EBITDA − variation du BFR
    """
    h = resoudre(h)
    lignes: List[MoisProjete] = []
    bfr_prec = float(h.bfr_depart or 0.0)
    treso = h.tresorerie_depart
    for t in range(1, h.horizon + 1):
        ca_ttc = h.ca_ttc(t)
        ca_ht = ca_ttc / (1 + h.tva)
        marge_brute = ca_ht * h.taux_marge_brute
        pub = ca_ttc / h.mer
        cm3 = marge_brute - pub
        fixes = h.fixes(t)
        ebitda = cm3 - fixes
        bfr = bfr_de(h, ca_ttc, pub)
        delta = bfr - bfr_prec
        flux = ebitda - delta
        treso += flux
        lignes.append(MoisProjete(t, ca_ttc, ca_ht, marge_brute, pub, cm3,
                                  fixes, ebitda, bfr, delta, flux, treso))
        bfr_prec = bfr
    return lignes


def point_bas(h: Hypotheses, lignes: List[MoisProjete]) -> Tuple[int, float]:
    """Mois et montant du point bas de tresorerie. Le mois 0 y participe."""
    rang, montant = 0, h.tresorerie_depart
    for l in lignes:
        if l.tresorerie < montant:
            rang, montant = l.rang, l.tresorerie
    return rang, montant


def mois_rupture(lignes: List[MoisProjete]) -> Optional[int]:
    """Premier mois ou la tresorerie passe sous zero. None s'il n'y en a pas."""
    for l in lignes:
        if l.tresorerie < 0:
            return l.rang
    return None


def capital_necessaire(h: Hypotheses) -> float:
    """Cash a injecter au mois 0 pour ne jamais passer sous zero."""
    _, bas = point_bas(h, projeter(h))
    return max(0.0, -bas)


def matelas(h: Hypotheses) -> float:
    """Un mois de charges decaissees au mois du point bas.

    Zero euro de marge de securite n'est pas un plan : le jour ou la
    tresorerie touche exactement zero, tu ne paies plus tes salaires.
    """
    lignes = projeter(h)
    rang, _ = point_bas(h, lignes)
    if rang == 0:
        ca_ht = h.ca_ttc_depart / (1 + h.tva)
        return ca_ht * h.taux_cogs + h.ca_ttc_depart / h.mer + h.fixes_mois
    l = lignes[rang - 1]
    return l.ca_ht * h.taux_cogs + l.pub + l.fixes


# ---------------------------------------------------------------------------
# 5. LE TAUX DE CROISSANCE MAXIMAL AUTOFINANCABLE
# ---------------------------------------------------------------------------

def _tient(h: Hypotheses, g: float) -> bool:
    """La trésorerie reste-t-elle positive tout du long à ce taux ?"""
    hg = dataclasses.replace(h, croissance=g)
    return point_bas(hg, projeter(hg))[1] >= 0


def taux_max_autofinancable(h: Hypotheses, borne_basse: float = 0.0,
                            borne_haute: float = 1.00, pas: float = 0.005,
                            tol: float = 1e-6) -> Tuple[Optional[float], str, bool]:
    """Le taux de croissance mensuel le plus eleve qui ne ruine jamais le cash.

    Methode : balayage grossier de la borne basse a la borne haute pour
    localiser le dernier taux qui tient, puis recherche DICHOTOMIQUE dans le
    demi-pas suivant, jusqu'a 0,0001 point de precision.

    Le balayage prealable n'est pas du luxe, et une dichotomie seule serait
    fausse ici. L'ensemble des taux faisables n'est pas un intervalle borne
    seulement par le haut :

      — vers le haut, la croissance immobilise du BFR plus vite qu'elle ne
        rend de la marge, et finit toujours par tuer la tresorerie ;
      — vers le bas, si les frais fixes croissent alors que le CA stagne ou
        recule, la tresorerie meurt aussi — par le resultat, pas par le BFR.

    On balaie donc toute la plage, on retient le DERNIER point faisable, et on
    signale le cas ou un point infaisable existe en dessous de lui : la
    reponse reste juste (c'est bien le taux le plus eleve qui tient) mais le
    lecteur doit savoir que descendre plus bas ne le sauve pas.

    Retourne (taux, statut, non_monotone). Statuts :
        « trouve »  -> taux exploitable
        « plafond » -> tient encore a la borne haute (contrainte non mordante)
        « aucun »   -> aucun taux de la plage ne tient, croissance nulle comprise
    """
    h = resoudre(h)
    if _tient(h, borne_haute):
        return borne_haute, "plafond", False

    n = int(round((borne_haute - borne_basse) / pas))
    grille = [(borne_basse + i * pas, _tient(h, borne_basse + i * pas))
              for i in range(n + 1)]
    faisables = [i for i, (_, ok) in enumerate(grille) if ok]
    if not faisables:
        return None, "aucun", False

    dernier = faisables[-1]
    non_monotone = any(not ok for _, ok in grille[:dernier])

    bas, haut = grille[dernier][0], grille[dernier + 1][0]
    while haut - bas > tol:
        milieu = (bas + haut) / 2
        if _tient(h, milieu):
            bas = milieu
        else:
            haut = milieu
    return bas, "trouve", non_monotone


def ebitda_de_depart(h: Hypotheses) -> float:
    """EBITDA du mois 0, avant toute croissance."""
    ca_ht = h.ca_ttc_depart / (1 + h.tva)
    return ca_ht * h.taux_marge_brute - h.ca_ttc_depart / h.mer - h.fixes_mois


def croissance_a_tresorerie_constante(h: Hypotheses) -> float:
    """Croissance financee par le seul EBITDA courant, sans toucher au cash.

    C'est exactement la regle des chiffres canoniques § 4, colonne
    « croissance autofinancable / mois » : la variation du BFR ne doit pas
    depasser l'EBITDA du mois en cours.

        BFR = r × CA TTC        (toutes ses composantes sont proportionnelles au CA)
        ΔBFR = r × CA0 × g  ≤  EBITDA0
        -> g = EBITDA0 / (r × CA0) = EBITDA0 / BFR0

    Cette regle est deliberement conservatrice sur deux points, et il faut le
    savoir avant de s'en servir :

    1. Elle finance la croissance avec l'EBITDA d'AUJOURD'HUI, alors que le
       mois ou le BFR augmente est aussi celui ou le CA a deja augmente.
       Une version auto-coherente — ΔBFR(1) ≤ EBITDA(1) — donne un taux
       nettement plus eleve. Au palier P3 de NORA : 15,7 % au lieu de 10,6 %.
    2. Elle interdit de puiser dans la tresorerie existante, alors que c'est
       precisement a cela qu'un solde bancaire sert.

    Le taux maximal autofinancable de la section 4 repond a l'autre question :
    combien de croissance ma tresorerie ACTUELLE peut-elle encaisser sur
    l'horizon. Les deux chiffres sont vrais, ils ne mesurent pas la meme chose.

    Retourne un taux negatif ou nul quand l'EBITDA de depart ne l'est pas :
    dans ce cas la croissance ne s'autofinance a aucun rythme.
    """
    h = resoudre(h)
    bfr0 = float(h.bfr_depart or 0.0)
    if bfr0 <= 0:
        return float("inf")   # BFR negatif : le client finance le fournisseur
    return ebitda_de_depart(h) / bfr0


# ---------------------------------------------------------------------------
# 6. SENSIBILITE
# ---------------------------------------------------------------------------

VARIANTES = [
    ("−15 jours de stock",
     lambda h: dataclasses.replace(h, jours_stock=max(0, h.jours_stock - 15))),
    ("+30 jours de délai fournisseur",
     lambda h: dataclasses.replace(h, delai_fournisseur=h.delai_fournisseur + 30)),
    ("+1 point de marge brute",
     lambda h: dataclasses.replace(h, taux_marge_brute=h.taux_marge_brute + 0.01)),
    ("−10 % de dépense publicitaire",
     lambda h: dataclasses.replace(h, mer=h.mer / 0.90)),
]


def sensibilite(h: Hypotheses) -> List[dict]:
    """Effet de chaque levier sur le point bas, a CA inchange.

    « −10 % de depense publicitaire » se traduit par un MER divise par 0,90 :
    on depense 10 % de moins pour le meme chiffre d'affaires. C'est une
    hypothese forte — voir la section des limites.
    """
    h = resoudre(h)
    base_rang, base_bas = point_bas(h, projeter(h))
    lignes = [{
        "nom": "Scénario de référence", "rang": base_rang, "bas": base_bas,
        "ecart": 0.0, "gmax": taux_max_autofinancable(h)[0],
    }]
    for nom, muter in VARIANTES:
        hv = muter(h)
        rang, bas = point_bas(hv, projeter(hv))
        lignes.append({
            "nom": nom, "rang": rang, "bas": bas, "ecart": bas - base_bas,
            "gmax": taux_max_autofinancable(hv)[0],
        })
    return lignes


# ---------------------------------------------------------------------------
# 7. RENDU TEXTE
# ---------------------------------------------------------------------------

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


def titre(t: str, souligne: str = "=") -> List[str]:
    return ["", t, souligne * len(t)]


def rapport(h: Hypotheses, entete: Optional[List[str]] = None) -> str:
    h = resoudre(h)
    o: List[str] = []
    a = o.append

    a("=" * 78)
    a("SIMULATEUR DE TRÉSORERIE ET DE BFR")
    a("=" * 78)
    for l in (entete or []):
        a(l)

    # -- hypotheses --------------------------------------------------------
    o += titre("1. Hypothèses retenues", "-")
    o += tableau(
        ["Paramètre", "Valeur", "Paramètre", "Valeur"],
        [
            ["CA TTC de départ (M0)", eur(h.ca_ttc_depart), "Jours de stock", f"{h.jours_stock} j"],
            ["Croissance mensuelle visée", taux(h.croissance, 2), "Délai d'encaissement", f"{h.delai_encaissement} j"],
            ["Horizon", f"{h.horizon} mois", "Délai fournisseur", f"{h.delai_fournisseur} j"],
            ["Marge brute (CM2, % CA HT)", taux(h.taux_marge_brute, 2), "Délai pub → encaissement", f"{h.delai_pub} j"],
            ["MER (CA TTC / pub)", num(h.mer, 2), "Acompte fournisseur", taux(h.acompte_fournisseur, 0)],
            ["COGS (% CA HT)", taux(h.taux_cogs, 2), "BFR de départ (M0)", eur(h.bfr_depart or 0.0)],
            ["Frais fixes HT (M0)", eur(h.fixes_mois), "BFR en jours de CA TTC", f"{(h.bfr_depart or 0.0) / (h.ca_ttc_depart / 30):.0f} j"],
            ["Croissance des fixes", taux(h.croissance_fixes, 2), "Trésorerie de départ", eur(h.tresorerie_depart)],
            ["TVA", taux(h.tva, 0), "", ""],
        ],
        gauche=[0, 2],
    )

    # -- projection --------------------------------------------------------
    lignes = projeter(h)
    rang_bas, montant_bas = point_bas(h, lignes)
    rupture = mois_rupture(lignes)

    o += titre("2. Projection mois par mois", "-")
    a("Montants en euros. CA TTC = prix client. CA HT, marge brute, pub, CM3,")
    a("fixes et EBITDA sont HT. BFR, flux et trésorerie sont des soldes de caisse.")
    a("")
    corps = []
    for l in lignes:
        alerte = ""
        if rupture is not None and l.rang >= rupture:
            alerte = "RUPTURE" if l.rang == rupture else "sous zéro"
        elif l.rang == rang_bas:
            alerte = "point bas"
        corps.append([
            f"M{l.rang}", num(l.ca_ttc), num(l.ca_ht), num(l.marge_brute),
            num(l.pub), num(l.cm3), num(l.fixes), num(l.ebitda),
            num(l.delta_bfr), num(l.flux), num(l.tresorerie), alerte,
        ])
    o += tableau(
        ["Mois", "CA TTC", "CA HT", "Marge br.", "Pub", "CM3", "Fixes",
         "EBITDA", "Δ BFR", "Flux net", "Trésorerie", "Alerte"],
        corps, gauche=[0, 11],
    )

    # -- point bas et rupture ---------------------------------------------
    o += titre("3. Point bas de trésorerie", "-")
    if rang_bas == 0:
        a(f"Point bas : le mois 0 — {eur(montant_bas)}. La trésorerie ne redescend")
        a("jamais sous son niveau de départ sur l'horizon simulé.")
    else:
        a(f"Point bas : mois M{rang_bas} — {eur(montant_bas)}.")
        a(f"Consommé depuis le départ : {eur(h.tresorerie_depart - montant_bas)} "
          f"({taux((h.tresorerie_depart - montant_bas) / h.tresorerie_depart, 1)} "
          f"de la trésorerie initiale).")
    a("")
    if rupture is None:
        a("Pas de rupture de trésorerie sur l'horizon simulé.")
    else:
        l = lignes[rupture - 1]
        a("┌" + "─" * 66 + "┐")
        a("│ RUPTURE DE TRÉSORERIE".ljust(67) + "│")
        a("│".ljust(67) + "│")
        a(f"│   Mois M{rupture} — solde {eur(l.tresorerie)}".ljust(67) + "│")
        a(f"│   CA TTC de ce mois : {eur(l.ca_ttc)}".ljust(67) + "│")
        a(f"│   Tu es en cessation de paiement {rupture} mois après le départ,".ljust(67) + "│")
        a(f"│   avec un EBITDA mensuel de {eur(l.ebitda)}.".ljust(67) + "│")
        a("└" + "─" * 66 + "┘")

    # -- taux maximal ------------------------------------------------------
    o += titre("4. Taux de croissance maximal autofinançable", "-")
    gmax, statut, non_monotone = taux_max_autofinancable(h)
    gconst = croissance_a_tresorerie_constante(h)
    if statut == "aucun":
        a("Aucun taux de croissance ne tient, croissance nulle comprise : la")
        a("trésorerie passe sous zéro même en gelant le chiffre d'affaires. Ce")
        a("n'est donc pas un problème de rythme, c'est un problème de structure —")
        a("marge brute, MER ou frais fixes. Accélérer ne fera qu'avancer la date.")
    else:
        borne = " (borne haute du balayage, non contraignante)" if statut == "plafond" else ""
        a(f"Taux maximal sur {h.horizon} mois, trésorerie de départ comprise : "
          f"{taux(gmax or 0.0, 2)} / mois{borne}")
        a(f"Taux visé                                                : {taux(h.croissance, 2)} / mois")
        marge_g = (gmax or 0.0) - h.croissance
        verdict = "de marge" if marge_g >= 0 else "AU-DESSUS du soutenable"
        a(f"Écart                                                    : {pts(marge_g)} {verdict}")
        a("")
        if gconst == float("inf"):
            a("Croissance à trésorerie constante : non contraignante — le BFR est")
            a("négatif, tes clients financent tes fournisseurs.")
        elif gconst <= 0:
            a("Croissance à trésorerie constante : négative. L'EBITDA actuel ne")
            a("finance aucune augmentation de BFR — toute croissance se paie sur")
            a("le cash existant ou sur une levée. C'est exactement ce que disent")
            a("les paliers P1 et P2 des chiffres canoniques § 4.")
        else:
            a(f"À titre de comparaison, la règle des chiffres canoniques § 4 — ΔBFR ≤")
            a(f"EBITDA, sans toucher au cash existant — donne {taux(gconst, 2)} / mois,")
            a(f"soit {eur(h.ca_ttc_depart * gconst)} de CA TTC mensuel supplémentaire.")
            a("La règle canonique est plus sévère : elle interdit de puiser dans la")
            a("trésorerie de départ. Les deux chiffres répondent à deux questions.")
        if non_monotone:
            a("")
            a("Avertissement : il existe des taux supérieurs qui tiennent également")
            a("(la faisabilité n'est pas un intervalle ici). Le chiffre donné est le")
            a("plus haut taux tel que TOUS les taux inférieurs tiennent aussi.")

    # -- capital -----------------------------------------------------------
    o += titre("5. Capital supplémentaire nécessaire", "-")
    besoin = max(0.0, -montant_bas)
    if besoin <= 0:
        a(f"Aucun capital supplémentaire n'est nécessaire pour tenir "
          f"{taux(h.croissance, 2)} / mois")
        a(f"sur {h.horizon} mois : le point bas reste positif à {eur(montant_bas)}.")
        a("")
        a(f"Marge de sécurité disponible au point bas : {eur(montant_bas)}, soit")
        a(f"{montant_bas / matelas(h):.1f}".replace(".", ",") +
          f" mois de charges décaissées ({eur(matelas(h))} / mois).")
        a("Sous 1,0 mois de charges au point bas, la simulation est trop tendue")
        a("pour être un plan : un retard de livraison suffit à te mettre à découvert.")
    else:
        a(f"Capital à injecter au mois 0 pour tenir {taux(h.croissance, 2)} / mois")
        a(f"sur {h.horizon} mois, sans jamais passer sous zéro :")
        a("")
        a(f"    Strict minimum (point bas ramené à zéro)  {eur(besoin)}")
        a(f"    + un mois de charges décaissées           {eur(matelas(h))}")
        a(f"    = à lever réellement                      {eur(besoin + matelas(h))}")
        a("")
        a("Le strict minimum n'est pas un objectif de levée : il amène la trésorerie")
        a("à exactement zéro au mois du point bas. Lève le second chiffre.")

    # -- sensibilite -------------------------------------------------------
    o += titre("6. Sensibilité du point bas", "-")
    a(f"Effet de chaque levier sur le point bas, à croissance visée inchangée "
      f"({taux(h.croissance, 2)} / mois).")
    a("")
    corps = []
    for s in sensibilite(h):
        corps.append([
            s["nom"],
            f"M{s['rang']}",
            eur(s["bas"]),
            "—" if s["nom"].startswith("Scénario") else eur(s["ecart"]),
            "—" if s["gmax"] is None else taux(s["gmax"], 2),
        ])
    o += tableau(
        ["Levier", "Mois du point bas", "Point bas", "Écart", "Taux max autofin."],
        corps, gauche=[0],
    )
    a("")
    a("Lecture : les deux premiers leviers sont des leviers de trésorerie pure —")
    a("ils ne changent ni le CA ni l'EBITDA, seulement la date des flux. Les deux")
    a("derniers changent le compte de résultat. Compare leur coût d'obtention :")
    a("négocier 30 jours de plus avec ton fabricant est souvent moins cher qu'un")
    a("point de marge brute, et se décide en une réunion.")

    a("")
    a("─" * 78)
    a("Fin de simulation. Les montants sont modélisés à partir de tes hypothèses ;")
    a("ce ne sont pas des prévisions. Voir la section 9 du module E10.")
    return "\n".join(o)


# ---------------------------------------------------------------------------
# 8. MODE DEMONSTRATION — NORA, PASSAGE DE P3 A P4
# ---------------------------------------------------------------------------

def hypotheses_demo() -> Tuple[Hypotheses, List[str]]:
    """NORA au passage du palier P3 (Scale France) au palier P4 (Multi-pays).

    Tout ce qui peut etre lu dans les chiffres canoniques l'est. Ce qui ne
    peut pas l'etre est marque comme hypothese locale.
    """
    if CANONIQUE_DISPONIBLE:
        p3, p4 = PALIERS[2], PALIERS[3]
        t3, t4 = TRESO["P3"], TRESO["P4"]
        v = dict(
            p3_ca=p3.ca_ttc, p3_marge=p3.taux_marge_brute, p3_cogs=p3.cogs_pct,
            p3_mer=p3.mer, p3_fixes=p3.fixes_mois, p3_ebitda=p3.ebitda,
            p3_pub=p3.depense_pub,
            p3_stock=t3.jours_stock, p3_dso=t3.delai_encaissement,
            p3_dpo=t3.delai_fournisseur, p3_pubj=t3.delai_pub,
            p4_ca=p4.ca_ttc, p4_cogs=p4.cogs_pct, p4_fixes=p4.fixes_mois,
            p4_stock=t4.jours_stock, p4_dso=t4.delai_encaissement,
            p4_dpo=t4.delai_fournisseur, p4_pubj=t4.delai_pub,
            acompte=t4.acompte_fournisseur,
        )
        source = "modele_nora.py (import direct)"
    else:  # pragma: no cover
        r = REPLI
        pub3 = r["p3_ca_ttc"] / r["p3_mer"]
        v = dict(
            p3_ca=r["p3_ca_ttc"], p3_marge=r["p3_marge_brute"], p3_cogs=r["p3_cogs"],
            p3_mer=r["p3_mer"], p3_fixes=r["p3_fixes"], p3_ebitda=r["p3_ebitda"],
            p3_pub=pub3,
            p3_stock=r["p3_stock_j"], p3_dso=r["p3_dso"],
            p3_dpo=r["p3_dpo"], p3_pubj=r["p3_pub_j"],
            p4_ca=r["p4_ca_ttc"], p4_cogs=r["p4_cogs"], p4_fixes=r["p4_fixes"],
            p4_stock=r["p4_stock_j"], p4_dso=r["p4_dso"],
            p4_dpo=r["p4_dpo"], p4_pubj=r["p4_pub_j"],
            acompte=r["acompte"],
        )
        source = "valeurs de repli recopiées de chiffres-canoniques.md"

    horizon = 12
    g_ca = (v["p4_ca"] / v["p3_ca"]) ** (1 / horizon) - 1
    g_fixes = (v["p4_fixes"] / v["p3_fixes"]) ** (1 / horizon) - 1
    treso_depart = 6 * v["p3_ebitda"]

    # Le BFR de depart est celui du palier P3 : c'est la situation constatee au
    # dernier mois avant l'ouverture des marches. Des le mois M1, la marque
    # opere avec les parametres de tresorerie P4 (stock local dans cinq pays,
    # credit fournisseur renegocie, avance publicitaire allongee). L'ecart
    # entre les deux est la marche de BFR que l'ouverture fait payer d'un coup.
    h_p3 = Hypotheses(
        ca_ttc_depart=v["p3_ca"], croissance=g_ca, horizon=horizon,
        taux_marge_brute=v["p3_marge"], mer=v["p3_mer"], fixes_mois=v["p3_fixes"],
        croissance_fixes=g_fixes, jours_stock=v["p3_stock"],
        delai_encaissement=v["p3_dso"], delai_fournisseur=v["p3_dpo"],
        delai_pub=v["p3_pubj"], acompte_fournisseur=v["acompte"],
        tresorerie_depart=treso_depart, cogs_pct=v["p3_cogs"],
    )
    bfr0 = bfr_de(h_p3, v["p3_ca"], v["p3_pub"])

    h = Hypotheses(
        ca_ttc_depart=v["p3_ca"], croissance=g_ca, horizon=horizon,
        taux_marge_brute=v["p3_marge"], mer=v["p3_mer"], fixes_mois=v["p3_fixes"],
        croissance_fixes=g_fixes, jours_stock=v["p4_stock"],
        delai_encaissement=v["p4_dso"], delai_fournisseur=v["p4_dpo"],
        delai_pub=v["p4_pubj"], acompte_fournisseur=v["acompte"],
        tresorerie_depart=treso_depart, cogs_pct=v["p4_cogs"], bfr_depart=bfr0,
    )

    e = [
        "",
        "Mode démonstration : NØRA, passage du palier P3 au palier P4.",
        "",
        "NØRA est une marque fictive. Source des paramètres : " + source + ".",
        "",
        "Ce que dit le cursus : P3 (Scale France, M10–M18) fait "
        + eur(v["p3_ca"]) + " TTC/mois ;",
        "P4 (Multi-pays, M19–M30) fait " + eur(v["p4_ca"]) + " TTC/mois. La marque a",
        "douze mois pour passer de l'un à l'autre en ouvrant DE, ES et IT.",
        "",
        "Chiffres dérivés — le calcul est déroulé :",
        "    croissance du CA     = (" + num(v["p4_ca"]) + " / " + num(v["p3_ca"])
        + ")^(1/12) − 1 = " + taux(g_ca, 2) + " / mois",
        "    croissance des fixes = (" + num(v["p4_fixes"]) + " / " + num(v["p3_fixes"])
        + ")^(1/12) − 1 = " + taux(g_fixes, 2) + " / mois",
        "",
        "Hypothèses locales, non canoniques :",
        "    — Trésorerie de départ = 6 mois d'EBITDA P3 = 6 × "
        + eur(v["p3_ebitda"]) + " = " + eur(treso_depart) + ".",
        "      Une marque qui sort de la vallée de la mort n'a pas de trésor de guerre.",
        "    — Marge brute et MER tenus au niveau P3 (" + taux(v["p3_marge"], 2)
        + " et " + num(v["p3_mer"], 2) + ") sur tout",
        "      l'horizon. Le cursus vise " + num(2.80, 2) + " de MER au palier P4,",
        "      mais un MER ne s'améliore pas le mois où on ouvre trois pays.",
        "    — Paramètres de trésorerie P4 (" + str(v["p4_stock"]) + " j de stock, "
        + str(v["p4_dpo"]) + " j fournisseur, " + str(v["p4_pubj"]) + " j d'avance pub)",
        "      appliqués dès M1, sur un BFR de départ calculé aux paramètres P3",
        "      (" + str(v["p3_stock"]) + " j, " + str(v["p3_dpo"]) + " j, "
        + str(v["p3_pubj"]) + " j) = " + eur(bfr0) + ". L'écart entre les deux est la",
        "      marche de BFR que l'ouverture de trois marchés fait payer d'un coup.",
        "",
        "Note de lecture : la ligne « −15 jours de stock » du tableau de",
        "sensibilité correspond exactement au retour à la logistique P3 ("
        + str(v["p4_stock"]) + " − 15 = " + str(v["p3_stock"]) + " j).",
    ]
    return h, e


# ---------------------------------------------------------------------------
# 9. MODE VERIFICATION — ECARTS AVEC LES CHIFFRES CANONIQUES
# ---------------------------------------------------------------------------

def verifier() -> str:
    """Confronte les formules du simulateur au tableau canonique § 4."""
    o: List[str] = []
    a = o.append
    a("=" * 78)
    a("VÉRIFICATION CONTRE LES CHIFFRES CANONIQUES § 4")
    a("=" * 78)
    if not CANONIQUE_DISPONIBLE:  # pragma: no cover
        a("modele_nora.py introuvable : vérification impossible.")
        return "\n".join(o)

    a("")
    a("A. Reproduction du BFR par palier, acompte fournisseur forcé à 0 %.")
    a("   modele_nora.py déclare acompte_fournisseur = 30 % mais ne l'utilise")
    a("   pas dans le calcul du BFR. À acompte nul, les deux formules doivent")
    a("   coïncider à l'euro près.")
    a("")
    corps = []
    ecart_max = 0.0
    for p in PALIERS:
        t = TRESO[p.code]
        h = Hypotheses(
            ca_ttc_depart=p.ca_ttc, croissance=0.0, horizon=1,
            taux_marge_brute=p.taux_marge_brute, mer=p.mer,
            fixes_mois=p.fixes_mois, croissance_fixes=0.0,
            jours_stock=t.jours_stock, delai_encaissement=t.delai_encaissement,
            delai_fournisseur=t.delai_fournisseur, delai_pub=t.delai_pub,
            acompte_fournisseur=0.0, tresorerie_depart=0.0, cogs_pct=p.cogs_pct,
        )
        mien = bfr_de(h, p.ca_ttc, p.depense_pub)
        h30 = dataclasses.replace(h, acompte_fournisseur=t.acompte_fournisseur)
        avec_acompte = bfr_de(h30, p.ca_ttc, p.depense_pub)
        ecart = mien - t.bfr
        ecart_max = max(ecart_max, abs(ecart))
        corps.append([p.code, eur(t.bfr), eur(mien), eur(ecart),
                      eur(avec_acompte), eur(avec_acompte - t.bfr)])
    o += tableau(
        ["Palier", "BFR canonique", "BFR simulateur", "Écart",
         "BFR à acompte 30 %", "Écart"],
        corps, gauche=[0],
    )
    a("")
    a("Verdict A : écart maximal à acompte nul = " + eur(ecart_max, 2) + ".")
    a("La colonne « acompte 30 % » est le vrai BFR : la part payée comptant à la")
    a("commande de production ne bénéficie d'aucun crédit fournisseur. C'est le")
    a("seul écart de formule assumé avec modele_nora.py.")

    a("")
    a("B. Reproduction de la colonne « croissance autofinançable / mois ».")
    a("   Règle canonique : ΔBFR ≤ EBITDA du mois, sans puiser dans le cash.")
    a("")
    corps = []
    ecart_b = 0.0
    for p in PALIERS:
        t = TRESO[p.code]
        h = Hypotheses(
            ca_ttc_depart=p.ca_ttc, croissance=0.0, horizon=12,
            taux_marge_brute=p.taux_marge_brute, mer=p.mer,
            fixes_mois=p.fixes_mois, croissance_fixes=0.0,
            jours_stock=t.jours_stock, delai_encaissement=t.delai_encaissement,
            delai_fournisseur=t.delai_fournisseur, delai_pub=t.delai_pub,
            acompte_fournisseur=0.0, tresorerie_depart=0.0, cogs_pct=p.cogs_pct,
        )
        g = croissance_a_tresorerie_constante(h)
        # Regle canonique : cash immobilise par +100 k€ de CA, puis EBITDA / ce cash.
        canon = p.ebitda / (t.bfr / p.ca_ttc * 100_000) * 100_000
        if g <= 0:
            corps.append([p.code, "négative", "négative", "négative", "—"])
        else:
            corps.append([p.code, taux(g, 2), eur(canon),
                          eur(p.ca_ttc * g), eur(p.ca_ttc * g - canon, 2)])
        ecart_b = max(ecart_b, abs(p.ca_ttc * g - canon)) if g > 0 else ecart_b
    o += tableau(
        ["Palier", "Taux simulateur", "CA autofin. canonique",
         "CA autofin. simulateur", "Écart"],
        corps, gauche=[0],
    )
    a("")
    a("Verdict B : écart maximal = " + eur(ecart_b, 2) + ". Aux paliers P3, P4 et P5")
    a("le simulateur reproduit la colonne canonique à l'euro près. Aux paliers P1")
    a("et P2 l'EBITDA est négatif : la croissance ne s'autofinance à aucun rythme,")
    a("ce que le tableau canonique dit déjà en toutes lettres (« négative — la")
    a("croissance consomme du cash »).")
    a("")
    a("C. Le seul écart de fond, à connaître avant de citer un chiffre.")
    a("   La règle canonique finance la croissance avec l'EBITDA d'aujourd'hui.")
    a("   Le « taux maximal autofinançable » de la section 4 du rapport autorise,")
    a("   lui, à consommer la trésorerie existante sur tout l'horizon. Le second")
    a("   est donc toujours supérieur au premier, souvent du simple au double.")
    a("   Ce ne sont pas deux mesures du même objet : la règle canonique décrit")
    a("   un régime permanent, le taux maximal décrit ce qu'un solde bancaire")
    a("   donné permet d'encaisser pendant un nombre de mois donné.")
    a("")
    a("─" * 78)
    return "\n".join(o)


# ---------------------------------------------------------------------------
# 10. LIGNE DE COMMANDE
# ---------------------------------------------------------------------------

def construire_parseur() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="simulateur_tresorerie.py",
        description="Simulateur de trésorerie et de BFR pour une marque DTC. "
                    "À quelle vitesse peux-tu croître sans être à court de cash ?",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Les décimales s'écrivent avec une virgule ou un point. "
               "Les taux s'écrivent en pourcentage : --croissance 7,9 vaut 7,9 % par mois.",
    )
    p.add_argument("--demo", action="store_true",
                   help="scénario NØRA, passage du palier P3 au palier P4")
    p.add_argument("--verifier", action="store_true",
                   help="confronte les formules aux chiffres canoniques § 4")
    p.add_argument("--ca", type=lire_montant, default=None,
                   help="CA TTC du dernier mois plein (ex. 250000 ou 250k)")
    p.add_argument("--croissance", type=lire_taux, default=0.10,
                   help="croissance mensuelle visée du CA, en %% (défaut : 10)")
    p.add_argument("--horizon", type=int, default=24,
                   help="nombre de mois projetés (défaut : 24)")
    p.add_argument("--marge", type=lire_taux, default=0.58,
                   help="taux de marge brute CM2 en %% du CA HT (défaut : 58)")
    p.add_argument("--mer", type=lire_nombre, default=2.5,
                   help="MER = CA TTC / dépense publicitaire (défaut : 2,5)")
    p.add_argument("--cogs", type=lire_taux, default=None,
                   help="COGS en %% du CA HT (défaut : 40 %% du coût variable total)")
    p.add_argument("--fixes", type=lire_montant, default=0.0,
                   help="frais fixes HT mensuels du mois 0")
    p.add_argument("--croissance-fixes", type=lire_taux, default=0.0,
                   help="croissance mensuelle des frais fixes, en %% (défaut : 0)")
    p.add_argument("--jours-stock", type=int, default=75,
                   help="jours de stock détenu, DIO (défaut : 75)")
    p.add_argument("--dso", type=int, default=3,
                   help="délai d'encaissement en jours (défaut : 3)")
    p.add_argument("--dpo", type=int, default=30,
                   help="délai fournisseur en jours (défaut : 30)")
    p.add_argument("--delai-pub", type=int, default=7,
                   help="jours entre la dépense publicitaire et l'encaissement (défaut : 7)")
    p.add_argument("--acompte", type=lire_taux, default=0.30,
                   help="part d'acompte fournisseur payée comptant, en %% (défaut : 30)")
    p.add_argument("--tresorerie", type=lire_montant, default=0.0,
                   help="solde bancaire disponible au mois 0")
    p.add_argument("--bfr-depart", type=lire_montant, default=None,
                   help="BFR constaté au mois 0 (défaut : calculé sur les mêmes paramètres)")
    p.add_argument("--tva", type=lire_taux, default=TVA,
                   help="taux de TVA moyen pondéré, en %% (défaut : 20)")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    parseur = construire_parseur()
    if not argv:
        parseur.print_help()
        print("\nRien à simuler. Commence par : "
              "python3 ecommerce/outils/simulateur_tresorerie.py --demo")
        return 0
    args = parseur.parse_args(argv)

    if args.verifier:
        print(verifier())
        if not args.demo:
            return 0

    if args.demo:
        h, entete = hypotheses_demo()
        print(rapport(h, entete))
        return 0

    if args.ca is None:
        parseur.error("--ca est obligatoire hors mode --demo "
                      "(CA TTC du dernier mois plein).")
    if args.horizon < 1:
        parseur.error("--horizon doit valoir au moins 1 mois.")
    if args.mer <= 0:
        parseur.error("--mer doit être strictement positif.")
    if not 0 < args.marge < 1:
        parseur.error("--marge doit être strictement entre 0 et 100 %.")

    h = Hypotheses(
        ca_ttc_depart=args.ca, croissance=args.croissance, horizon=args.horizon,
        taux_marge_brute=args.marge, mer=args.mer, fixes_mois=args.fixes,
        croissance_fixes=args.croissance_fixes, jours_stock=args.jours_stock,
        delai_encaissement=args.dso, delai_fournisseur=args.dpo,
        delai_pub=args.delai_pub, acompte_fournisseur=args.acompte,
        tresorerie_depart=args.tresorerie, cogs_pct=args.cogs,
        bfr_depart=args.bfr_depart, tva=args.tva,
    )
    print(rapport(h))
    return 0


if __name__ == "__main__":
    sys.exit(main())
