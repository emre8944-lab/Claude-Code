#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Constructeur de tableau de cohortes, a partir d'un export de commandes.

Une marque qui ne lit pas ses cohortes ne sait pas si elle gagne de l'argent.
Elle sait seulement si elle en a gagne le mois dernier, ce qui n'est pas la
meme chose : le compte de resultat d'un mois melange des clients acquis a
douze dates differentes, dans douze conditions d'acquisition differentes.
La cohorte separe ce melange. C'est le seul instrument qui reponde a la
question qui decide de tout : « le client que j'achete AUJOURD'HUI vaut-il
encore ce que valait celui que j'achetais il y a un an ? »

Ce que l'outil produit
----------------------
  1. Le tableau de cohortes. Lignes = mois d'acquisition, colonnes = M0 a M12,
     valeur au choix : commandes cumulees par client acquis, CA cumule TTC par
     client acquis, ou contribution cumulee par client acquis.
  2. La courbe de reachat moyenne, toutes cohortes confondues, a 1, 3, 6 et
     12 mois — au format exact de la courbe canonique du § 3, pour comparaison
     ligne a ligne.
  3. Le taux de passage de la 1re a la 2e commande a 30, 60, 90 et 180 jours.
  4. La LTV en contribution a 3, 6 et 12 mois, le ratio LTV/CAC et le payback
     interpole, si le taux de marge brute et le nCAC sont fournis.
  5. L'ALERTE : les cohortes recentes sous-performent-elles les anciennes au
     meme age ? C'est le signal numero un de degradation d'une marque, et il
     se lit sur M1-M6 bien avant d'etre lisible sur M12 ou sur l'EBITDA.

Le fichier d'entree
-------------------
Un CSV avec au minimum trois colonnes : une date de commande, un identifiant
de client, un montant TTC. Les noms usuels sont reconnus automatiquement
(date_commande, date, created_at, order_date / identifiant_client, client,
customer_id, email / montant_ttc, montant, total, total_price...). Sinon,
--colonne-date, --colonne-client, --colonne-montant les imposent.

Le separateur (« ; », « , », tabulation, « | ») est detecte. La virgule
decimale francaise, le symbole euro, les espaces de milliers et le BOM des
exports Excel sont acceptes. Si l'export est au niveau LIGNE DE PRODUIT et
non au niveau commande, --colonne-commande regroupe les lignes.

Usage
-----
    # 1. fabriquer un jeu de donnees de demonstration
    python3 ecommerce/outils/cohortes.py --generer-exemple

    # 2. l'analyser
    python3 ecommerce/outils/cohortes.py \
        --fichier ecommerce/outils/scenarios/cohortes-exemple.csv \
        --marge-brute 61,5 --ncac 40,03

    # les deux d'un coup, sur les parametres canoniques de NORA
    python3 ecommerce/outils/cohortes.py --demo

    # sur tes chiffres, avec un export dont les colonnes s'appellent autrement
    python3 ecommerce/outils/cohortes.py --fichier export.csv \
        --colonne-date "Created at" --colonne-client "Email" \
        --colonne-montant "Total" --colonne-commande "Name" \
        --valeur contribution --marge-brute 58 --ncac 34,50

Conventions de sortie : francais, virgule decimale, espace avant % et €, tout
montant marque TTC ou HT. Voir ecommerce/CHARTE.md § 5. Un CAC est toujours
HT : c'est un cout. Un panier est toujours TTC : c'est un prix client.

Python 3.9+. Aucune dependance externe : argparse, csv, datetime, math, os,
random (graine fixe), sys, unicodedata — tout est dans la bibliotheque standard.
Chiffres de reference : ecommerce/donnees/chiffres-canoniques.md § 3.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import math
import os
import random
import sys
import unicodedata
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

LARGEUR = 78

# Espace fine insecable : separateur de milliers et espace avant % et €.
FINE = " "

TVA_DEFAUT = 0.20          # taux moyen pondere Europe de l'Ouest, comme modele_nora.py
GRAINE_DEFAUT = 1804       # graine fixe : deux executions donnent le meme fichier
JOURS_PAR_MOIS = 365.25 / 12


# ---------------------------------------------------------------------------
# 0. FORMATAGE — mêmes conventions que modele_nora.py et test_significativite.py
# ---------------------------------------------------------------------------

def eur(x: float, d: int = 0) -> str:
    """Formate un montant en euros, espace fine comme separateur de milliers."""
    if x == float("inf"):
        return "illimité"
    if x != x:
        return "—"
    s = f"{x:,.{d}f}".replace(",", FINE).replace(".", ",").replace("-", "−")
    return s + FINE + "€"


def eur_signe(x: float, d: int = 2) -> str:
    """Formate un ecart en euros, signe compris : +3,20 € / −7,45 €."""
    if x != x:
        return "—"
    s = f"{x:+,.{d}f}".replace(",", FINE).replace(".", ",").replace("-", "−")
    return s + FINE + "€"


def pct(x: float, d: int = 1) -> str:
    """Formate une proportion (0,615) en pourcentage francais (61,5 %)."""
    if x in (float("inf"), float("-inf")):
        return ("∞" if x > 0 else "−∞") + FINE + "%"
    if x != x:
        return "—"
    return f"{x * 100:.{d}f}".replace(".", ",") + FINE + "%"


def pct_signe(x: float, d: int = 1) -> str:
    """Formate un ecart relatif avec son signe : +10,0 % / −7,5 %."""
    if x in (float("inf"), float("-inf")):
        return ("+∞" if x > 0 else "−∞") + FINE + "%"
    if x != x:
        return "—"
    return f"{x * 100:+.{d}f}".replace(".", ",").replace("-", "−") + FINE + "%"


def pts(x: float, d: int = 1) -> str:
    """Formate un ecart en points de pourcentage, signe compris."""
    if x != x:
        return "—"
    return f"{x * 100:+.{d}f}".replace(".", ",").replace("-", "−") + FINE + "pts"


def dec(x: float, d: int = 2) -> str:
    """Formate un nombre decimal nu (un ratio, un nombre de commandes)."""
    if x == float("inf"):
        return "∞"
    if x != x:
        return "—"
    return f"{x:.{d}f}".replace(".", ",").replace("-", "−")


def dec_signe(x: float, d: int = 2) -> str:
    if x != x:
        return "—"
    return f"{x:+.{d}f}".replace(".", ",").replace("-", "−")


def ent(x: float) -> str:
    """Formate un entier avec separateur de milliers."""
    if x == float("inf"):
        return "∞"
    return f"{x:,.0f}".replace(",", FINE).replace("-", "−")


def nombre(s: str) -> float:
    """Lit un nombre ecrit a la francaise ou a l'anglaise. « 1 494,50 € » -> float."""
    t = str(s)
    for parasite in (" ", FINE, " ", " ", "€", "%", "EUR", "eur"):
        t = t.replace(parasite, "")
    t = t.replace("−", "-").replace(",", ".")
    if t in ("", "-", "+"):
        raise ValueError(f"« {s} » n'est pas un nombre")
    try:
        return float(t)
    except ValueError:
        raise ValueError(f"« {s} » n'est pas un nombre")


def taux(s: str) -> float:
    """Lit un taux saisi en POINTS (« 61,5 » -> 0,615). Accepte « 0,615 » aussi."""
    v = nombre(s)
    return v / 100.0 if abs(v) > 1.0 else v


def _mots(txt: str) -> List[str]:
    """Decoupe en mots SANS casser les espaces fines insecables.

    « 40,03 € » est un seul mot : c'est tout l'interet de l'espace fine, et
    str.split() la traiterait comme un separateur, ce qui renverrait le
    symbole a la ligne suivante.
    """
    plat = txt.replace("\n", " ").replace("\t", " ")
    bruts = [m for m in plat.split(" ") if m]
    # Un guillemet ouvrant seul en fin de ligne, ou un guillemet fermant seul en
    # debut de ligne, est une faute de composition. On les recolle au mot qu'ils
    # encadrent avec une espace fine insecable, qui est de toute facon la bonne
    # espace a l'interieur de guillemets francais.
    mots: List[str] = []
    for m in bruts:
        if mots and mots[-1].endswith("«"):
            mots[-1] += FINE + m
        elif m.startswith("»") and mots:
            mots[-1] += FINE + m
        else:
            mots.append(m)
    return mots


def bandeau(t: str, sous_titre: str = "") -> List[str]:
    out = ["═" * LARGEUR, t.upper().center(LARGEUR)]
    if sous_titre:
        out.append(sous_titre.center(LARGEUR))
    out.append("═" * LARGEUR)
    return out


def titre(t: str) -> List[str]:
    return ["", t.upper(), "─" * LARGEUR]


def cadre(t: str) -> List[str]:
    """Encadre une ligne : reserve aux verdicts qu'on ne doit pas rater."""
    interieur = t[:LARGEUR - 4].ljust(LARGEUR - 4)
    return ["┌" + "─" * (LARGEUR - 2) + "┐",
            "│ " + interieur + " │",
            "└" + "─" * (LARGEUR - 2) + "┘"]


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


def tableau_matrice(tete: str, entetes: Sequence[str],
                    lignes: Sequence[Tuple[str, Sequence[str]]],
                    indent: str = "  ", largeur: int = LARGEUR) -> List[str]:
    """Rend une matrice large en la decoupant en blocs de colonnes qui tiennent.

    La premiere colonne — le libelle de la cohorte — est repetee dans chaque
    bloc. Un tableau de cohortes M0..M12 en euros ne tient pas sur 78 colonnes ;
    plutot que de tronquer ou de deborder, on le coupe en deux ou trois blocs
    lisibles l'un sous l'autre.
    """
    if not lignes:
        return [indent + "(aucune cohorte)"]
    w0 = max([len(tete)] + [len(l[0]) for l in lignes])
    wcol = [max(len(entetes[j]), max(len(l[1][j]) for l in lignes))
            for j in range(len(entetes))]

    blocs: List[List[int]] = []
    courant: List[int] = []
    utilise = len(indent) + w0
    for j, w in enumerate(wcol):
        besoin = 2 + w
        if courant and utilise + besoin > largeur:
            blocs.append(courant)
            courant, utilise = [], len(indent) + w0
        courant.append(j)
        utilise += besoin
    if courant:
        blocs.append(courant)

    out: List[str] = []
    for n, bloc in enumerate(blocs):
        if n:
            out.append("")
        out.append(indent + tete.ljust(w0) + "  "
                   + "  ".join(entetes[j].rjust(wcol[j]) for j in bloc))
        out.append(indent + "─" * w0 + "  "
                   + "  ".join("─" * wcol[j] for j in bloc))
        for lab, cells in lignes:
            out.append(indent + lab.ljust(w0) + "  "
                       + "  ".join(cells[j].rjust(wcol[j]) for j in bloc))
    return out


def paragraphe(txt: str, indent: str = "  ", creux: Optional[str] = None,
               largeur: int = LARGEUR) -> List[str]:
    """Coupe un paragraphe a la largeur utile, sans couper les mots."""
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
# 1. LE CALENDRIER — un mois est un index, pas une chaîne
# ---------------------------------------------------------------------------

def idx_mois(d: datetime.date) -> int:
    """Index absolu du mois. Deux dates du meme mois ont le meme index."""
    return d.year * 12 + (d.month - 1)


def libelle_mois(i: int) -> str:
    return f"{i // 12:04d}-{i % 12 + 1:02d}"


def debut_de_mois(i: int) -> datetime.date:
    return datetime.date(i // 12, i % 12 + 1, 1)


def fin_de_mois(i: int) -> datetime.date:
    suivant = debut_de_mois(i + 1)
    return suivant - datetime.timedelta(days=1)


# ---------------------------------------------------------------------------
# 2. LECTURE DU FICHIER — tolérante sur la forme, stricte sur le fond
# ---------------------------------------------------------------------------

# Noms de colonnes reconnus sans qu'on ait besoin de les declarer. La liste
# couvre les exports courants (Shopify, WooCommerce, PrestaShop, un tableur
# tenu a la main). Elle n'a pas vocation a etre exhaustive : --colonne-* est
# la pour le reste.
ALIAS: Dict[str, List[str]] = {
    "date": ["date_commande", "date_de_commande", "date", "created_at", "date_creation",
             "order_date", "processed_at", "paid_at", "day", "jour", "date_achat",
             "date_de_la_commande", "datetime"],
    "client": ["identifiant_client", "id_client", "client", "client_id", "customer_id",
               "customer", "email", "e_mail", "adresse_email", "billing_email",
               "customer_email", "acheteur", "user_id"],
    "montant": ["montant_ttc", "montant", "total_ttc", "ca_ttc", "total", "total_price",
                "prix_ttc", "chiffre_affaires_ttc", "grand_total", "order_total",
                "montant_commande", "valeur", "panier_ttc", "subtotal_ttc"],
    "commande": ["numero_commande", "id_commande", "commande", "order_id", "order_number",
                 "name", "reference", "reference_commande", "num_commande"],
}

SEPARATEURS = [";", ",", "\t", "|"]


def normaliser_entete(s: str) -> str:
    """Met un nom de colonne sous une forme comparable : sans accent, sans casse."""
    t = unicodedata.normalize("NFKD", str(s))
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.strip().lower().replace("﻿", "")
    out = []
    for c in t:
        out.append(c if c.isalnum() else "_")
    t = "".join(out)
    while "__" in t:
        t = t.replace("__", "_")
    return t.strip("_")


def detecter_separateur(entete_brute: str) -> str:
    """Detecte le separateur d'un CSV. Sniffer d'abord, comptage ensuite.

    Le comptage est le filet de securite : csv.Sniffer se trompe sur les
    fichiers a une seule colonne utile ou aux libelles contenant des virgules,
    ce qui est exactement le cas d'un export francais mal exporte.
    """
    try:
        dialecte = csv.Sniffer().sniff(entete_brute, delimiters="".join(SEPARATEURS))
        if dialecte.delimiter in SEPARATEURS:
            return dialecte.delimiter
    except csv.Error:
        pass
    comptes = {s: entete_brute.count(s) for s in SEPARATEURS}
    meilleur = max(comptes, key=lambda s: comptes[s])
    return meilleur if comptes[meilleur] > 0 else ";"


def lire_date(s: str) -> Optional[datetime.date]:
    """Lit une date. AAAA-MM-JJ d'abord, puis les formats humains courants.

    Les horodatages ISO (« 2026-01-05T14:22:31+01:00 ») sont tronques a la
    date : l'heure d'une commande n'a aucun interet pour une cohorte mensuelle,
    et elle est de toute facon exprimee dans un fuseau qu'on ne connait pas.
    """
    t = str(s).strip().strip('"')
    if not t:
        return None
    t = t.replace("T", " ").split(" ")[0].split("+")[0]
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%d.%m.%Y", "%Y%m%d"):
        try:
            return datetime.datetime.strptime(t, fmt).date()
        except ValueError:
            continue
    return None


def lire_montant(s: str) -> Optional[float]:
    """Lit un montant francais ou anglais. « 1 234,50 € » et « 1234.50 » passent.

    Le piege : « 1,234.50 » (anglais) et « 1 234,50 » (francais) veulent dire
    la meme chose et s'ecrivent avec les memes signes inverses. On tranche sur
    la position du dernier separateur.
    """
    t = str(s).strip().strip('"')
    if not t:
        return None
    for parasite in ("€", "EUR", "eur", " ", FINE, " ", " ", " "):
        t = t.replace(parasite, "")
    t = t.replace("−", "-")
    if not t or t in ("-", "+"):
        return None
    if "," in t and "." in t:
        # Le separateur decimal est le dernier des deux.
        if t.rfind(",") > t.rfind("."):
            t = t.replace(".", "").replace(",", ".")
        else:
            t = t.replace(",", "")
    elif "," in t:
        t = t.replace(",", ".")
    try:
        return float(t)
    except ValueError:
        return None


@dataclass
class Journal:
    """Ce que la lecture a produit, et surtout tout ce qu'elle a dû jeter.

    Un outil d'analyse qui ne dit pas ce qu'il a jete ment par omission :
    5 % de lignes silencieusement perdues suffisent a deplacer une courbe de
    reachat au-dela du seuil de decision.
    """
    chemin: str = ""
    separateur: str = ";"
    colonnes: Dict[str, str] = field(default_factory=dict)
    lignes_lues: int = 0
    retenues: int = 0
    sans_date: int = 0
    sans_client: int = 0
    sans_montant: int = 0
    negatives: int = 0
    lignes_par_commande: int = 1.0


@dataclass
class Commande:
    date: datetime.date
    client: str
    montant_ttc: float


def resoudre_colonne(role: str, entetes: Sequence[str], impose: Optional[str],
                     obligatoire: bool = True) -> Optional[str]:
    """Trouve la colonne qui porte un role, ou explique pourquoi elle manque."""
    normalisees = {normaliser_entete(e): e for e in entetes}
    if impose:
        cle = normaliser_entete(impose)
        if cle in normalisees:
            return normalisees[cle]
        raise ValueError(
            f"la colonne « {impose} » n'existe pas dans le fichier. "
            f"Colonnes disponibles : {', '.join(entetes)}.")
    for candidat in ALIAS[role]:
        if candidat in normalisees:
            return normalisees[candidat]
    # Deuxieme passe : une colonne qui CONTIENT un alias (« total_ttc_eur »).
    for candidat in ALIAS[role]:
        for norme, brute in normalisees.items():
            if candidat in norme:
                return brute
    if not obligatoire:
        return None
    raise ValueError(
        f"aucune colonne de {role} reconnue. Utilise --colonne-{role}. "
        f"Colonnes disponibles : {', '.join(entetes)}.")


def lire_csv(chemin: str, col_date: Optional[str] = None, col_client: Optional[str] = None,
             col_montant: Optional[str] = None, col_commande: Optional[str] = None,
             garder_negatifs: bool = False) -> Tuple[List[Commande], Journal]:
    """Lit l'export et rend une liste de commandes propres, plus son journal."""
    if not os.path.exists(chemin):
        raise ValueError(f"fichier introuvable : {chemin}")

    with open(chemin, "r", encoding="utf-8-sig", newline="") as f:
        tete = f.readline()
        if not tete.strip():
            raise ValueError("le fichier est vide ou commence par une ligne blanche.")
        separateur = detecter_separateur(tete)
        f.seek(0)
        lecteur = csv.DictReader(f, delimiter=separateur)
        entetes = [e for e in (lecteur.fieldnames or []) if e is not None]
        if len(entetes) < 2:
            raise ValueError(
                f"une seule colonne detectee avec le separateur « {separateur} ». "
                "Le fichier n'est probablement pas un CSV, ou son separateur est exotique.")

        j = Journal(chemin=chemin, separateur=separateur)
        nom_date = resoudre_colonne("date", entetes, col_date)
        nom_client = resoudre_colonne("client", entetes, col_client)
        nom_montant = resoudre_colonne("montant", entetes, col_montant)
        nom_cmd = resoudre_colonne("commande", entetes, col_commande, obligatoire=False) \
            if col_commande else None
        j.colonnes = {"date": nom_date, "client": nom_client, "montant": nom_montant}
        if nom_cmd:
            j.colonnes["commande"] = nom_cmd

        brutes: List[Tuple[Optional[str], datetime.date, str, float]] = []
        for ligne in lecteur:
            j.lignes_lues += 1
            client = (ligne.get(nom_client) or "").strip()
            if not client:
                j.sans_client += 1
                continue
            d = lire_date(ligne.get(nom_date) or "")
            if d is None:
                j.sans_date += 1
                continue
            m = lire_montant(ligne.get(nom_montant) or "")
            if m is None:
                j.sans_montant += 1
                continue
            if m < 0 and not garder_negatifs:
                j.negatives += 1
                continue
            ref = (ligne.get(nom_cmd) or "").strip() if nom_cmd else None
            brutes.append((ref, d, client, m))

    if not brutes:
        raise ValueError("aucune ligne exploitable : vérifie les colonnes et le format des dates.")

    if nom_cmd:
        # Export au niveau ligne de produit : on regroupe. La date d'une
        # commande est la plus ancienne de ses lignes, son montant leur somme.
        groupes: Dict[Tuple[str, str], List[Tuple[datetime.date, float]]] = {}
        for ref, d, client, m in brutes:
            groupes.setdefault((client, ref or f"{client}|{d}"), []).append((d, m))
        commandes = [Commande(min(x[0] for x in v), cle[0], sum(x[1] for x in v))
                     for cle, v in groupes.items()]
        j.lignes_par_commande = len(brutes) / max(1, len(commandes))
    else:
        commandes = [Commande(d, client, m) for _, d, client, m in brutes]

    commandes.sort(key=lambda c: (c.client, c.date))
    j.retenues = len(commandes)
    return commandes, j


# ---------------------------------------------------------------------------
# 3. LES COHORTES — le cœur de l'outil
# ---------------------------------------------------------------------------

MODES_VALEUR = ("commandes", "ca", "contribution")

# Jalons de la courbe canonique (§ 3), en jours. 1 mois = 30 j, 3 mois = 91 j,
# 6 mois = 183 j, 12 mois = 365 j. Les convertir en jours plutot qu'en mois
# calendaires est ce qui rend la comparaison honnete : un client acquis le
# 29 janvier et un client acquis le 2 janvier n'ont pas le meme age au
# 31 janvier, et un tableau mensuel fait semblant du contraire.
JALONS_CANONIQUES: List[Tuple[str, int]] = [
    ("1 mois", 30), ("3 mois", 91), ("6 mois", 183), ("12 mois", 365),
]

# ecommerce/donnees/chiffres-canoniques.md § 3, palier P5.
CANONIQUE_P5: Dict[int, Dict[str, float]] = {
    30:  {"cmd": 1.06, "reachats": 0.06, "ca_ttc": 69.10, "ltv": 35.38, "ratio": 0.88},
    91:  {"cmd": 1.34, "reachats": 0.34, "ca_ttc": 92.90, "ltv": 47.57, "ratio": 1.19},
    183: {"cmd": 1.72, "reachats": 0.72, "ca_ttc": 125.20, "ltv": 64.11, "ratio": 1.60},
    365: {"cmd": 2.24, "reachats": 1.24, "ca_ttc": 169.40, "ltv": 86.75, "ratio": 2.17},
}
CANONIQUE_NCAC = 40.03
CANONIQUE_MARGE = 0.615
CANONIQUE_PAYBACK = 1.8

# En dessous de ce nombre de clients pleinement observes, un horizon n'est pas
# publie : une courbe de reachat sur 12 clients est un dessin, pas une mesure.
MIN_ELIGIBLES = 30


@dataclass
class Client:
    identifiant: str
    acquisition: datetime.date
    montant_1_ttc: float
    reachats: List[Tuple[int, float]] = field(default_factory=list)  # (jours, montant TTC)

    @property
    def cohorte(self) -> int:
        return idx_mois(self.acquisition)


@dataclass
class Horizon:
    """Ce qu'on sait a un age donne, mesure en jours et non en mois calendaires."""
    jours: int
    eligibles: int
    reachats: float          # commandes de reachat cumulees par client acquis
    commandes: float         # = 1 + reachats
    ca_ttc: float            # CA cumule TTC par client acquis
    passage: float           # part des clients ayant passe une 2e commande

    @property
    def suffisant(self) -> bool:
        return self.eligibles >= MIN_ELIGIBLES


class Analyse:
    """Construit les cohortes et tout ce qui s'en deduit."""

    def __init__(self, commandes: Sequence[Commande], tva: float = TVA_DEFAUT,
                 marge_brute: Optional[float] = None, ncac: Optional[float] = None,
                 horizon: int = 12, min_cohorte: int = 20):
        self.tva = tva
        self.marge_brute = marge_brute
        self.ncac = ncac
        self.horizon = horizon
        self.min_cohorte = min_cohorte

        # -- clients ------------------------------------------------------
        par_client: Dict[str, List[Commande]] = {}
        for c in commandes:
            par_client.setdefault(c.client, []).append(c)

        self.clients: List[Client] = []
        for ident, cmds in par_client.items():
            cmds.sort(key=lambda c: c.date)
            premiere = cmds[0]
            cl = Client(ident, premiere.date, premiere.montant_ttc)
            for c in cmds[1:]:
                cl.reachats.append(((c.date - premiere.date).days, c.montant_ttc))
            self.clients.append(cl)
        self.clients.sort(key=lambda c: c.acquisition)

        self.nb_commandes = len(commandes)
        self.date_min = min(c.date for c in commandes)
        self.date_max = max(c.date for c in commandes)

        # -- le dernier mois COMPLET ---------------------------------------
        # Un mois entame n'est pas un mois. Le publier melangerait un M0 de
        # 30 jours avec un M0 de 6 jours et ferait plonger la derniere ligne
        # du tableau pour une raison purement calendaire. C'est l'erreur de
        # lecture la plus repandue sur les cohortes.
        dernier = idx_mois(self.date_max)
        self.mois_partiel = self.date_max != fin_de_mois(dernier)
        self.dernier_mois_complet = dernier - 1 if self.mois_partiel else dernier
        self.premier_mois = idx_mois(self.date_min)

        # -- matrices ------------------------------------------------------
        self.tailles: Dict[int, int] = {}
        self.cmd: Dict[int, Dict[int, float]] = {}
        self.ca: Dict[int, Dict[int, float]] = {}
        self.clients_cohorte: Dict[int, List[Client]] = {}
        for cl in self.clients:
            c = cl.cohorte
            if c > self.dernier_mois_complet:
                continue
            self.tailles[c] = self.tailles.get(c, 0) + 1
            self.clients_cohorte.setdefault(c, []).append(cl)
            self.cmd.setdefault(c, {})
            self.ca.setdefault(c, {})
            self.cmd[c][0] = self.cmd[c].get(0, 0.0) + 1
            self.ca[c][0] = self.ca[c].get(0, 0.0) + cl.montant_1_ttc
            for jours, montant in cl.reachats:
                d = cl.acquisition + datetime.timedelta(days=jours)
                m = idx_mois(d) - c
                if m < 0:
                    continue
                self.cmd[c][m] = self.cmd[c].get(m, 0.0) + 1
                self.ca[c][m] = self.ca[c].get(m, 0.0) + montant

        self.cohortes: List[int] = sorted(
            c for c, n in self.tailles.items() if n >= self.min_cohorte)
        self.cohortes_ecartees: List[int] = sorted(
            c for c, n in self.tailles.items() if n < self.min_cohorte)

        self._cache_horizons: Dict[Tuple[int, Optional[Tuple[int, ...]]], Horizon] = {}

    # -- conversions --------------------------------------------------------
    def ht(self, ttc: float) -> float:
        return ttc / (1 + self.tva)

    def contribution(self, ca_ttc: float) -> float:
        """Marge de contribution : CA HT x taux de marge brute (CM2).

        La marge se calcule sur le HT, jamais sur le TTC. La TVA n'a jamais
        appartenu a la marque : c'est de l'argent collecte pour l'Etat.
        """
        if self.marge_brute is None:
            return float("nan")
        return self.ht(ca_ttc) * self.marge_brute

    # -- le tableau ---------------------------------------------------------
    def observable(self, cohorte: int, age: int) -> bool:
        """Le mois d'age `age` de cette cohorte est-il entierement ecoule ?"""
        return cohorte + age <= self.dernier_mois_complet

    def age_max(self, cohorte: int) -> int:
        return min(self.horizon, self.dernier_mois_complet - cohorte)

    def cellule(self, cohorte: int, age: int, mode: str = "commandes") -> Optional[float]:
        """Valeur cumulee par CLIENT ACQUIS, ou None si le mois n'est pas complet."""
        if not self.observable(cohorte, age) or cohorte not in self.tailles:
            return None
        n = self.tailles[cohorte]
        if mode == "commandes":
            total = sum(v for m, v in self.cmd[cohorte].items() if m <= age)
            return total / n
        total_ca = sum(v for m, v in self.ca[cohorte].items() if m <= age)
        if mode == "ca":
            return total_ca / n
        if mode == "contribution":
            return self.contribution(total_ca / n)
        raise ValueError(f"mode de valeur inconnu : {mode}")

    def cohortes_observables(self, age: int) -> List[int]:
        return [c for c in self.cohortes if self.observable(c, age)]

    def moyenne(self, cohortes: Sequence[int], age: int, mode: str) -> Optional[float]:
        """Moyenne ponderee par la taille des cohortes = moyenne par client acquis."""
        num, den = 0.0, 0
        for c in cohortes:
            v = self.cellule(c, age, mode)
            if v is None:
                continue
            num += v * self.tailles[c]
            den += self.tailles[c]
        return num / den if den else None

    # -- la courbe en jours -------------------------------------------------
    def horizon_jours(self, jours: int,
                      cohortes: Optional[Sequence[int]] = None) -> Horizon:
        """Mesure a `jours` jours d'age, sur les seuls clients pleinement observes.

        Ne comptent que les clients acquis il y a au moins `jours` jours. Sans
        cette restriction, un client acquis la semaine derniere tirerait la
        moyenne a 12 mois vers le bas alors qu'il n'a simplement pas encore eu
        le temps de revenir. C'est le biais de troncature, et il fait sous-
        estimer la LTV de 20 a 40 % dans la plupart des tableaux faits a la main.
        """
        cle = (jours, tuple(sorted(cohortes)) if cohortes is not None else None)
        if cle in self._cache_horizons:
            return self._cache_horizons[cle]
        retenus = set(cohortes) if cohortes is not None else None
        n = 0
        reachats = 0.0
        ca = 0.0
        repeteurs = 0
        for cl in self.clients:
            if retenus is not None and cl.cohorte not in retenus:
                continue
            if (self.date_max - cl.acquisition).days < jours:
                continue
            n += 1
            ca += cl.montant_1_ttc
            k = 0
            for j, montant in cl.reachats:
                if j <= jours:
                    k += 1
                    ca += montant
            reachats += k
            if k:
                repeteurs += 1
        h = Horizon(jours=jours, eligibles=n,
                    reachats=reachats / n if n else float("nan"),
                    commandes=1 + reachats / n if n else float("nan"),
                    ca_ttc=ca / n if n else float("nan"),
                    passage=repeteurs / n if n else float("nan"))
        self._cache_horizons[cle] = h
        return h

    def passage_cohorte(self, cohorte: int, jours: int) -> Tuple[int, float]:
        """Taux de passage 1re -> 2e commande d'une cohorte, a `jours` jours."""
        n, k = 0, 0
        for cl in self.clients_cohorte.get(cohorte, []):
            if (self.date_max - cl.acquisition).days < jours:
                continue
            n += 1
            if any(j <= jours for j, _ in cl.reachats):
                k += 1
        return n, (k / n if n else float("nan"))

    # -- LTV, ratio, payback ------------------------------------------------
    def ltv(self, jours: int, cohortes: Optional[Sequence[int]] = None) -> float:
        h = self.horizon_jours(jours, cohortes)
        if not h.suffisant:
            return float("nan")
        return self.contribution(h.ca_ttc)

    def ratio_ltv_cac(self, jours: int, cohortes: Optional[Sequence[int]] = None) -> float:
        if not self.ncac:
            return float("nan")
        v = self.ltv(jours, cohortes)
        return v / self.ncac if v == v else float("nan")

    def _grille_contribution(self, jalons: Sequence[int],
                             cohortes: Optional[Sequence[int]] = None
                             ) -> List[Tuple[int, float]]:
        """Contribution cumulee par client acquis, aux jalons demandes."""
        points: List[Tuple[int, float]] = []
        for j in jalons:
            h = self.horizon_jours(j, cohortes)
            if not h.suffisant:
                break
            points.append((j, self.contribution(h.ca_ttc)))
        return points

    def payback_mois(self, jalons: Sequence[int],
                     cohortes: Optional[Sequence[int]] = None) -> float:
        """Mois ou la contribution cumulee rattrape le nCAC, par interpolation.

        Interpolation lineaire entre deux jalons, exactement comme le § 3 des
        chiffres canoniques : le resultat depend du pas de la grille, et il
        faut le savoir avant de comparer deux paybacks entre eux.
        """
        if not self.ncac or self.marge_brute is None:
            return float("nan")
        points = self._grille_contribution(jalons, cohortes)
        if not points:
            return float("nan")
        prev_j, prev_c = 0, points[0][1] if points[0][0] == 0 else 0.0
        if points[0][0] == 0 and prev_c >= self.ncac:
            return 0.0
        for j, c in points:
            if j == 0:
                continue
            if c >= self.ncac:
                if c == prev_c:
                    return j / JOURS_PAR_MOIS
                jour = prev_j + (self.ncac - prev_c) / (c - prev_c) * (j - prev_j)
                return jour / JOURS_PAR_MOIS
            prev_j, prev_c = j, c
        return float("inf")

    # -- la part réachat, isolée --------------------------------------------
    def base_premiere(self, cohorte: int, mode: str) -> float:
        """Valeur apportee par la seule 1re commande, par client acquis."""
        n = self.tailles[cohorte]
        if mode == "commandes":
            return 1.0
        ca1 = sum(cl.montant_1_ttc for cl in self.clients_cohorte[cohorte]) / n
        return ca1 if mode == "ca" else self.contribution(ca1)

    def cellule_reachat(self, cohorte: int, age: int, mode: str) -> Optional[float]:
        """La cellule, moins ce qu'a rapporte la 1re commande.

        Un tableau de commandes cumulees commence toujours a 1,00 : la 1re
        commande est un plancher constant qui DILUE l'ecart entre cohortes.
        Deux cohortes dont l'une reachete 40 % de moins que l'autre n'affichent
        que 6 % d'ecart a M1. Isoler le reachat rend l'alerte lisible des M1,
        soit cinq mois plus tot.
        """
        v = self.cellule(cohorte, age, mode)
        return None if v is None else v - self.base_premiere(cohorte, mode)

    def moyenne_reachat(self, cohortes: Sequence[int], age: int, mode: str) -> Optional[float]:
        num, den = 0.0, 0
        for c in cohortes:
            v = self.cellule_reachat(c, age, mode)
            if v is None:
                continue
            num += v * self.tailles[c]
            den += self.tailles[c]
        return num / den if den else None

    def clients_par_mois(self, cohortes: Sequence[int]) -> float:
        n = [self.tailles[c] for c in cohortes if c in self.tailles]
        return sum(n) / len(n) if n else float("nan")


# ---------------------------------------------------------------------------
# 4. L'ALERTE — les cohortes récentes tiennent-elles la comparaison ?
# ---------------------------------------------------------------------------

@dataclass
class EcartAge:
    """Comparaison des cohortes recentes et anciennes AU MEME AGE."""
    age: int
    anciennes: List[int]
    recentes: List[int]
    clients_anc: int
    clients_rec: int
    valeur_anc: float
    valeur_rec: float
    reachat_anc: float
    reachat_rec: float

    @property
    def ecart_relatif(self) -> float:
        if not self.valeur_anc:
            return float("nan")
        return (self.valeur_rec - self.valeur_anc) / self.valeur_anc

    @property
    def ecart_absolu(self) -> float:
        return self.valeur_rec - self.valeur_anc

    @property
    def ecart_reachat(self) -> float:
        if not self.reachat_anc:
            return float("nan")
        return (self.reachat_rec - self.reachat_anc) / self.reachat_anc


@dataclass
class Alerte:
    mode: str
    seuil: float
    n_recentes: int
    ecarts: List[EcartAge]
    declenchees: List[EcartAge]
    age_reference: Optional[int]
    passage_anc: float = float("nan")
    passage_rec: float = float("nan")
    passage_jours: int = 90
    manque_annuel: float = float("nan")   # en contribution, € HT
    ltv_anc: float = float("nan")
    ltv_rec: float = float("nan")

    @property
    def declenchee(self) -> bool:
        return bool(self.declenchees)

    @property
    def pire(self) -> Optional[EcartAge]:
        """L'age ou l'ecart est le plus SEVERE, l'age profond departageant les ex aequo.

        Prendre l'age le plus profond serait tentant — il est le plus complet
        economiquement — mais c'est aussi celui ou le bloc « recent » est le
        plus ancien, donc le plus dilue : a M8, les trois dernieres cohortes
        observables ont ete acquises il y a bientot un an. On titre donc sur
        l'ecart le plus fort, et on liste tous les ages franchis.
        """
        if not self.declenchees:
            return None
        return min(self.declenchees, key=lambda e: (e.ecart_relatif, -e.age))


def construire_alerte(a: Analyse, n_recentes: int = 3, seuil: float = 0.10,
                      mode: str = "commandes") -> Alerte:
    """Compare, a chaque age, les N dernieres cohortes observables aux precedentes.

    La regle de comparaison est la seule qui vaille : A AGE EGAL. Comparer la
    cohorte de janvier — quatorze mois de vie — a celle de mai — deux mois de
    vie — ne mesure rien d'autre que le temps qui passe. C'est pourtant ce que
    fait tout tableau de bord qui affiche « LTV moyenne par mois d'acquisition ».
    """
    ecarts: List[EcartAge] = []
    for age in range(0, a.horizon + 1):
        obs = a.cohortes_observables(age)
        if len(obs) < n_recentes + 2:
            continue
        recentes = obs[-n_recentes:]
        anciennes = obs[:-n_recentes]
        v_anc = a.moyenne(anciennes, age, mode)
        v_rec = a.moyenne(recentes, age, mode)
        if v_anc is None or v_rec is None:
            continue
        ecarts.append(EcartAge(
            age=age, anciennes=anciennes, recentes=recentes,
            clients_anc=sum(a.tailles[c] for c in anciennes),
            clients_rec=sum(a.tailles[c] for c in recentes),
            valeur_anc=v_anc, valeur_rec=v_rec,
            reachat_anc=a.moyenne_reachat(anciennes, age, mode) or 0.0,
            reachat_rec=a.moyenne_reachat(recentes, age, mode) or 0.0,
        ))

    declenchees = [e for e in ecarts if e.ecart_relatif == e.ecart_relatif
                   and e.ecart_relatif <= -seuil]
    al = Alerte(mode=mode, seuil=seuil, n_recentes=n_recentes,
                ecarts=ecarts, declenchees=declenchees,
                age_reference=max((e.age for e in declenchees), default=None))

    ref = al.pire or (max(ecarts, key=lambda e: e.age) if ecarts else None)
    if ref is not None:
        h_anc = a.horizon_jours(al.passage_jours, ref.anciennes)
        h_rec = a.horizon_jours(al.passage_jours, ref.recentes)
        if h_anc.suffisant:
            al.passage_anc = h_anc.passage
        if h_rec.suffisant:
            al.passage_rec = h_rec.passage
        if a.marge_brute is not None:
            c_anc = a.moyenne(ref.anciennes, ref.age, "contribution")
            c_rec = a.moyenne(ref.recentes, ref.age, "contribution")
            if c_anc is not None and c_rec is not None:
                al.ltv_anc, al.ltv_rec = c_anc, c_rec
                # Manque a gagner annualise : l'ecart de contribution par client
                # acquis, applique au rythme d'acquisition des cohortes recentes.
                al.manque_annuel = (c_rec - c_anc) * a.clients_par_mois(ref.recentes) * 12
    return al


# ---------------------------------------------------------------------------
# 5. LE JEU DE DONNÉES D'EXEMPLE — pour tester l'outil sans ses propres chiffres
# ---------------------------------------------------------------------------
#
# Ce generateur fabrique un export de commandes credible : 26 mois
# d'acquisition, une croissance mensuelle, une saisonnalite, des paniers tires
# d'une vraie gamme, des remboursements, et — volontairement — une DEGRADATION
# des cohortes recentes. Le but est que l'eleve voie l'alerte se declencher sur
# un cas ou il connait deja la reponse, avant de la lancer sur ses chiffres a
# lui, ou il ne la connait pas.
#
# La courbe de reachat des cohortes saines reproduit la courbe canonique du
# § 3 : c'est ce qui rend le resultat verifiable. La marque fil rouge NORA est
# FICTIVE, et ces donnees sont un modele, pas les comptes d'une entreprise.

FIN_EXEMPLE_DEFAUT = datetime.date(2026, 8, 14)
MOIS_ACQUISITION = 26
MOIS_DEGRADES = 10                 # les N derniers mois d'acquisition
FACTEUR_DEGRADATION = 0.58         # le reachat des cohortes recentes, en relatif
FACTEUR_AOV_DEGRADE = 0.94
PART_MONO_ACHAT = 0.42             # clients qui ne reviendront jamais
LOG_SIGMA = 0.65                   # heterogeneite des clients qui reviennent
CLIENTS_PREMIER_MOIS = 110
CROISSANCE_MENSUELLE = 0.055

# Intensite cumulee de reachat d'un client « moyen » (w = 1), en jours.
# Calquee sur ecommerce/donnees/chiffres-canoniques.md § 3.
COURBE_REACHAT: List[Tuple[int, float]] = [
    (0, 0.00), (30, 0.06), (91, 0.34), (183, 0.72),
    (365, 1.24), (548, 1.66), (730, 1.98), (1096, 2.42),
]

# La gamme NORA (chiffres canoniques § 1), en PVC TTC.
PRIX = [24.00, 29.00, 39.00, 74.00, 99.00]
POIDS_PREMIERE = [0.06, 0.06, 0.34, 0.33, 0.21]
POIDS_REACHAT = [0.04, 0.06, 0.19, 0.29, 0.42]
P_COMPLEMENT_PREMIERE = 0.16       # ajout d'un shampooing au panier
P_COMPLEMENT_REACHAT = 0.36        # ajout d'un serum au panier

SAISONNALITE = {11: 1.35, 12: 1.12, 1: 0.85, 2: 0.92, 7: 0.90, 8: 0.78}
PAYS = [("FR", 0.62), ("DE", 0.12), ("BE", 0.08), ("ES", 0.07),
        ("IT", 0.07), ("NL", 0.04)]
CANAUX_ACQUISITION = [("Meta", 0.55), ("TikTok", 0.15), ("Google", 0.19),
                      ("Influence", 0.08), ("Autre", 0.03)]
CANAUX_REACHAT = [("Email/SMS", 0.45), ("Direct", 0.35), ("Meta retargeting", 0.20)]


def _lambda_cum(t: float) -> float:
    """Nombre attendu de reachats cumules a t jours, pour un client moyen."""
    if t <= 0:
        return 0.0
    for (t0, v0), (t1, v1) in zip(COURBE_REACHAT, COURBE_REACHAT[1:]):
        if t <= t1:
            return v0 + (v1 - v0) * (t - t0) / (t1 - t0)
    return COURBE_REACHAT[-1][1]


def _lambda_inv(u: float) -> float:
    """Reciproque de _lambda_cum : tire une date de commande dans la courbe."""
    for (t0, v0), (t1, v1) in zip(COURBE_REACHAT, COURBE_REACHAT[1:]):
        if u <= v1:
            if v1 == v0:
                return t0
            return t0 + (t1 - t0) * (u - v0) / (v1 - v0)
    return float(COURBE_REACHAT[-1][0])


def _poisson(rng: random.Random, lam: float) -> int:
    """Loi de Poisson par la methode de Knuth. Suffisant pour lambda < 30."""
    if lam <= 0:
        return 0
    seuil = math.exp(-lam)
    k, p = 0, 1.0
    while True:
        p *= rng.random()
        if p <= seuil:
            return k
        k += 1
        if k > 200:
            return k


def _tirer(rng: random.Random, options: Sequence[Tuple[str, float]]) -> str:
    u = rng.random()
    cumul = 0.0
    for valeur, poids in options:
        cumul += poids
        if u <= cumul:
            return valeur
    return options[-1][0]


def _panier(rng: random.Random, premiere: bool, facteur: float) -> float:
    poids = POIDS_PREMIERE if premiere else POIDS_REACHAT
    u, cumul, prix = rng.random(), 0.0, PRIX[-1]
    for p, w in zip(PRIX, poids):
        cumul += w
        if u <= cumul:
            prix = p
            break
    p_comp = P_COMPLEMENT_PREMIERE if premiere else P_COMPLEMENT_REACHAT
    if rng.random() < p_comp:
        prix += 24.00 if premiere else 39.00
    return round(prix * facteur, 2)


def generer_exemple(chemin: str, graine: int = GRAINE_DEFAUT,
                    fin: Optional[datetime.date] = None) -> Dict[str, object]:
    """Ecrit un CSV de demonstration et rend son signalement.

    Le fichier est produit dans la forme la plus penible qu'on rencontre en
    vrai : separateur point-virgule, BOM Excel, virgule decimale, colonnes
    surnumeraires, lignes de remboursement negatives. Si l'outil le lit, il
    lira a peu pres n'importe quel export.
    """
    fin = fin or FIN_EXEMPLE_DEFAUT
    rng = random.Random(graine)
    mu = math.log(1.0 / (1.0 - PART_MONO_ACHAT)) - LOG_SIGMA ** 2 / 2

    mois_fin = idx_mois(fin)
    mois_debut = mois_fin - (MOIS_ACQUISITION - 1)
    seuil_degrade = mois_fin - (MOIS_DEGRADES - 1)

    lignes: List[Tuple[datetime.date, str, float, str, str, str]] = []
    effectif = float(CLIENTS_PREMIER_MOIS)
    total_clients = 0
    clients_degrades = 0

    for c in range(mois_debut, mois_fin + 1):
        mois_civil = c % 12 + 1
        n = max(1, int(round(effectif * SAISONNALITE.get(mois_civil, 1.0))))
        effectif *= 1 + CROISSANCE_MENSUELLE
        degrade = c >= seuil_degrade
        f_reachat = FACTEUR_DEGRADATION if degrade else 1.0
        f_aov = FACTEUR_AOV_DEGRADE if degrade else 1.0

        premier, dernier = debut_de_mois(c), min(fin, fin_de_mois(c))
        etendue = (dernier - premier).days
        if etendue < 0:
            continue
        for _ in range(n):
            total_clients += 1
            if degrade:
                clients_degrades += 1
            ident = f"CLI-{total_clients:06d}"
            pays = _tirer(rng, PAYS)
            d0 = premier + datetime.timedelta(days=rng.randint(0, etendue))
            lignes.append((d0, ident, _panier(rng, True, f_aov), "",
                           pays, _tirer(rng, CANAUX_ACQUISITION)))

            w = 0.0 if rng.random() < PART_MONO_ACHAT else rng.lognormvariate(mu, LOG_SIGMA)
            w *= f_reachat
            observe = (fin - d0).days
            n_rep = _poisson(rng, w * _lambda_cum(observe))
            plafond = _lambda_cum(observe)
            jours = sorted(_lambda_inv(rng.uniform(0.0, plafond)) for _ in range(n_rep))
            for j in jours:
                d = d0 + datetime.timedelta(days=int(round(j)))
                if d > fin:
                    continue
                lignes.append((d, ident, _panier(rng, False, f_aov), "",
                               pays, _tirer(rng, CANAUX_REACHAT)))

    lignes.sort(key=lambda x: (x[0], x[1]))

    # Black Friday : la derniere semaine de novembre est remisee. Cela ne
    # change pas le nombre de commandes, seulement le panier — et c'est
    # exactement pour ca qu'une cohorte acquise en novembre a l'air mauvaise
    # en CA et bonne en volume.
    finales: List[Tuple[str, str, str, str, str, str]] = []
    numero = 0
    remboursements = 0
    ca_total = 0.0
    for d, ident, montant, _, pays, canal in lignes:
        if d.month == 11 and 24 <= d.day <= 30:
            montant = round(montant * 0.80, 2)
        numero += 1
        ref = f"CMD-{numero:06d}"
        ca_total += montant
        finales.append((d.isoformat(), ident, f"{montant:.2f}".replace(".", ","),
                        ref, pays, canal))
        if rng.random() < 0.012:
            d_r = min(fin, d + datetime.timedelta(days=rng.randint(3, 21)))
            remboursements += 1
            finales.append((d_r.isoformat(), ident,
                            f"{-montant:.2f}".replace(".", ","),
                            "R-" + ref, pays, "Remboursement"))

    finales.sort(key=lambda x: x[0])
    dossier = os.path.dirname(os.path.abspath(chemin))
    if dossier and not os.path.isdir(dossier):
        os.makedirs(dossier, exist_ok=True)
    with open(chemin, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";", lineterminator="\n")
        w.writerow(["date_commande", "identifiant_client", "montant_ttc",
                    "numero_commande", "pays", "canal"])
        w.writerows(finales)

    return {
        "chemin": os.path.abspath(chemin),
        "lignes": len(finales),
        "commandes": numero,
        "remboursements": remboursements,
        "clients": total_clients,
        "clients_degrades": clients_degrades,
        "cohortes": MOIS_ACQUISITION,
        "debut": debut_de_mois(mois_debut),
        "fin": fin,
        "premier_mois_degrade": libelle_mois(seuil_degrade),
        "facteur": FACTEUR_DEGRADATION,
        "ca_ttc": ca_total,
    }


# ---------------------------------------------------------------------------
# 6. RENDU
# ---------------------------------------------------------------------------

UNITES = {
    "commandes": "commandes cumulées par client acquis",
    "ca": "€ TTC cumulés par client acquis",
    "contribution": "€ HT de contribution cumulée par client acquis",
}


def _fmt(v: Optional[float], mode: str) -> str:
    if v is None or v != v:
        return "·"
    return dec(v, 2) if mode == "commandes" else dec(v, 1)


def _fmt_unite(v: Optional[float], mode: str, signe: bool = False) -> str:
    """Comme _fmt(), mais avec l'unite collee : hors tableau, un montant nu est une faute."""
    if v is None or v != v:
        return "—"
    if mode == "commandes":
        return (dec_signe(v, 2) if signe else dec(v, 2)) + " commande(s)/client"
    m = eur_signe(v, 2) if signe else eur(v, 2)
    return m + (" TTC" if mode == "ca" else " HT")


def bloc_lecture(a: Analyse, j: Journal) -> List[str]:
    o = titre("1. Ce que le fichier contient")
    o += tableau(
        ["", ""],
        [["Fichier", os.path.basename(j.chemin)],
         ["Séparateur détecté", {";": "point-virgule", ",": "virgule",
                                 "\t": "tabulation", "|": "barre verticale"}.get(j.separateur, j.separateur)],
         ["Colonne date", j.colonnes.get("date", "—")],
         ["Colonne client", j.colonnes.get("client", "—")],
         ["Colonne montant", j.colonnes.get("montant", "—")],
         ["Colonne commande", j.colonnes.get("commande", "— (une ligne = une commande)")],
         ["Lignes lues", ent(j.lignes_lues)],
         ["Commandes retenues", ent(j.retenues)],
         ["Clients distincts", ent(len(a.clients))],
         ["Période couverte", f"{a.date_min.isoformat()} → {a.date_max.isoformat()}"],
         ["Dernier mois complet", libelle_mois(a.dernier_mois_complet)],
         ["Cohortes analysées", f"{ent(len(a.cohortes))} "
                               f"({libelle_mois(a.cohortes[0])} → {libelle_mois(a.cohortes[-1])})"
                               if a.cohortes else "0"]],
        ["g", "g"])

    jetees = j.sans_date + j.sans_client + j.sans_montant + j.negatives
    o.append("")
    if jetees:
        o += paragraphe(
            f"Lignes écartées : {ent(jetees)} sur {ent(j.lignes_lues)} "
            f"({pct(jetees / j.lignes_lues, 2)}) — dont {ent(j.negatives)} montants "
            f"négatifs (remboursements), {ent(j.sans_date)} dates illisibles, "
            f"{ent(j.sans_client)} sans client, {ent(j.sans_montant)} sans montant.")
    else:
        o += paragraphe("Aucune ligne écartée : toutes les lignes du fichier sont exploitables.")

    if a.mois_partiel:
        o.append("")
        o += paragraphe(
            f"Le mois {libelle_mois(idx_mois(a.date_max))} est incomplet "
            f"(données arrêtées au {a.date_max.isoformat()}). Il est EXCLU du tableau : "
            "publier un M0 de quelques jours à côté de M0 de trente jours fait plonger "
            "la dernière ligne pour une raison purement calendaire, et c'est l'erreur "
            "de lecture la plus répandue sur les cohortes.")
    if a.cohortes_ecartees:
        o.append("")
        o += paragraphe(
            f"{ent(len(a.cohortes_ecartees))} cohorte(s) écartée(s) car sous "
            f"{ent(a.min_cohorte)} clients — trop petites pour qu'une moyenne veuille "
            "dire quelque chose. Seuil réglable par --min-cohorte.")

    aov_1 = sum(cl.montant_1_ttc for cl in a.clients) / len(a.clients)
    ca_total = sum(cl.montant_1_ttc + sum(m for _, m in cl.reachats) for cl in a.clients)
    ca_reachat = sum(sum(m for _, m in cl.reachats) for cl in a.clients)
    o.append("")
    o += tableau(
        ["", ""],
        [["CA total TTC du fichier", eur(ca_total, 0)],
         ["CA total HT", eur(a.ht(ca_total), 0)],
         ["Panier moyen 1ʳᵉ commande TTC", eur(aov_1, 2)],
         ["Panier moyen de réachat TTC",
          eur(ca_reachat / max(1, a.nb_commandes - len(a.clients)), 2)],
         ["Part du CA en réachat", pct(ca_reachat / ca_total) if ca_total else "—"],
         ["Commandes par client (brut, non corrigé)",
          dec(a.nb_commandes / len(a.clients), 2)]],
        ["g", "d"])
    o.append("")
    o += paragraphe(
        "« Commandes par client (brut) » est le chiffre que sort n'importe quel "
        "tableau de bord, et il ne veut rien dire : il mélange un client acquis il y a "
        "deux ans avec un client acquis la semaine dernière. Tout ce qui suit existe "
        "pour le remplacer.")
    return o


def bloc_tableau_cohortes(a: Analyse, mode: str) -> List[str]:
    o = titre("2. Le tableau de cohortes")
    o += paragraphe(f"Lignes = mois d'acquisition. Colonnes = mois depuis l'acquisition. "
                    f"Valeur = {UNITES[mode]}. Le point « · » marque un mois "
                    f"qui n'est pas encore entièrement écoulé : il n'est pas nul, il est "
                    f"inconnu, et le confondre avec zéro est la faute classique.")
    o.append("")
    entetes = [f"M{m}" for m in range(a.horizon + 1)]
    lignes: List[Tuple[str, List[str]]] = []
    for c in a.cohortes:
        lab = f"{libelle_mois(c)} ({ent(a.tailles[c])})"
        lignes.append((lab, [_fmt(a.cellule(c, m, mode), mode) for m in range(a.horizon + 1)]))
    moyennes = [_fmt(a.moyenne(a.cohortes_observables(m), m, mode), mode)
                for m in range(a.horizon + 1)]
    lignes.append(("MOYENNE pondérée", moyennes))
    o += tableau_matrice("Cohorte (clients)", entetes, lignes)
    o.append("")
    o += paragraphe(
        "La ligne MOYENNE d'une colonne Mx ne porte que sur les cohortes ayant "
        "réellement atteint l'âge x. Elle monte donc mécaniquement de gauche à droite "
        "tout en portant sur de moins en moins de cohortes : à M12 elle ne décrit "
        "souvent que le passé lointain de la marque.")
    return o


def bloc_courbe(a: Analyse) -> List[str]:
    o = titre("3. La courbe de réachat moyenne, toutes cohortes confondues")
    o += paragraphe(
        "Mesurée en JOURS d'âge réel, pas en mois calendaires, et sur les seuls "
        "clients dont l'horizon est entièrement observé. C'est le format du § 3 des "
        "chiffres canoniques, colonne pour colonne.")
    o.append("")

    l1, l2 = [], []
    for nom, jours in JALONS_CANONIQUES:
        h = a.horizon_jours(jours)
        can = CANONIQUE_P5[jours]
        if h.suffisant:
            ecart_r = (h.reachats - can["reachats"]) / can["reachats"]
            ecart_ca = (h.ca_ttc - can["ca_ttc"]) / can["ca_ttc"]
            l1.append([nom, ent(h.eligibles), dec(h.reachats, 2),
                       dec(can["reachats"], 2), pct_signe(ecart_r)])
            l2.append([nom, dec(h.commandes, 2), dec(can["cmd"], 2),
                       eur(h.ca_ttc, 2), eur(can["ca_ttc"], 2), pct_signe(ecart_ca)])
        else:
            l1.append([nom, ent(h.eligibles), "—", dec(can["reachats"], 2),
                       "trop peu de recul"])
            l2.append([nom, "—", dec(can["cmd"], 2), "—", eur(can["ca_ttc"], 2), "—"])

    o.append("  Commandes de RÉACHAT cumulées par client acquis")
    o += tableau(["Horizon", "Clients", "Mesuré", "§ 3", "Écart"], l1,
                 ["g", "d", "d", "d", "d"])
    o.append("")
    o.append("  Commandes totales et CA cumulé TTC par client acquis")
    o += tableau(["Horizon", "Cmd/cl.", "§ 3", "CA TTC/cl.", "§ 3", "Écart"], l2,
                 ["g", "d", "d", "d", "d", "d"])
    o.append("")
    o += paragraphe(
        "Cette courbe est un AGRÉGAT : elle mélange toutes les générations de "
        "clients, et elle est pondérée par leur nombre. Une marque qui grossit a "
        "des cohortes récentes plus grosses que les anciennes — ce sont donc elles "
        "qui pèsent le plus dans les horizons courts, et le moins dans les horizons "
        "longs, où elles sont absentes. Si les cohortes récentes se dégradent, cette "
        "courbe s'affaisse à 1, 3 et 6 mois tout en restant intacte à 12 mois. "
        "C'est exactement ce que sépare le § 6.")
    o.append("")
    o += paragraphe(
        "La colonne « § 3 » est la courbe canonique de NØRA au palier P5 "
        "(ecommerce/donnees/chiffres-canoniques.md § 3), marque FICTIVE, modèle "
        "calibré sur des ordres de grandeur sectoriels. Elle sert d'étalon de "
        "lecture, pas d'objectif : une catégorie à réachat lent — un rasoir, un "
        "bagage — a une courbe légitimement plus plate.")
    return o


def bloc_passage(a: Analyse) -> List[str]:
    o = titre("4. Le taux de passage de la 1ʳᵉ à la 2ᵉ commande")
    o += paragraphe(
        "C'est la marche la plus haute de toute la rétention. Un client qui a "
        "commandé deux fois a une probabilité de troisième commande deux à trois fois "
        "plus élevée qu'un client qui n'a commandé qu'une fois. Tout l'argent de la "
        "rétention se joue sur cette marche-là.")
    o.append("")
    lignes = []
    for jours in (30, 60, 90, 180):
        h = a.horizon_jours(jours)
        if h.suffisant:
            lignes.append([f"{jours} jours", ent(h.eligibles),
                           ent(round(h.passage * h.eligibles)), pct(h.passage)])
        else:
            lignes.append([f"{jours} jours", ent(h.eligibles), "—", "trop peu de recul"])
    o += tableau(["Fenêtre", "Clients observés", "Revenus", "Taux de passage"],
                 lignes, ["g", "d", "d", "d"])
    o.append("")
    h180 = a.horizon_jours(180)
    if h180.suffisant:
        h90 = a.horizon_jours(90)
        acquis_apres_90 = h180.passage - h90.passage
        o += paragraphe(
            f"Entre 90 et 180 jours, {pts(acquis_apres_90)} de clients supplémentaires "
            f"passent leur 2ᵉ commande. Couper une relance à 90 jours parce que « le "
            f"client est perdu » revient donc à renoncer à cette part-là.")
    return o


def bloc_ltv(a: Analyse) -> List[str]:
    o = titre("5. LTV en contribution, ratio LTV/CAC et payback")
    if a.marge_brute is None:
        o += paragraphe(
            "Non calculée : il manque --marge-brute, le taux de marge brute CM2 en % du "
            "CA HT, après COGS, logistique, PSP, retours et remises. Ce n'est pas la "
            "marge marchandise : une marque à 85 % de marge marchandise tourne souvent "
            "à 60 % de marge brute une fois la logistique et les remises passées.")
        o.append("")
        o += paragraphe(
            "Sans ce nombre, un tableau de cohortes reste une courbe de trafic. Le CA "
            "cumulé ne dit rien : c'est la contribution qui rembourse le CAC.")
        return o

    o += paragraphe(
        f"Hypothèses de calcul — marge brute (CM2) : {pct(a.marge_brute)} du CA HT ; "
        f"nCAC : {eur(a.ncac, 2) + ' HT' if a.ncac else 'non fourni (--ncac)'} ; "
        f"TVA : {pct(a.tva, 0)}. "
        f"La contribution est calculée sur le CA HT : la TVA n'a jamais appartenu à la "
        f"marque.")
    o.append("")
    lignes = []
    for nom, jours in JALONS_CANONIQUES[1:]:
        h = a.horizon_jours(jours)
        can = CANONIQUE_P5[jours]
        if not h.suffisant:
            lignes.append([nom, ent(h.eligibles), "—", "—", "—", dec(can["ratio"], 2)])
            continue
        ltv = a.contribution(h.ca_ttc)
        lignes.append([nom, ent(h.eligibles), eur(h.ca_ttc, 2), eur(ltv, 2),
                       dec(ltv / a.ncac, 2) if a.ncac else "—", dec(can["ratio"], 2)])
    o += tableau(["Horizon", "Clients", "CA TTC/cl.", "LTV contrib.", "LTV/CAC", "§ 3"],
                 lignes, ["g", "d", "d", "d", "d", "d"])

    if not a.ncac:
        o.append("")
        o += paragraphe(
            "Ratio LTV/CAC et payback non calculés : il manque --ncac, le coût "
            "d'acquisition d'un NOUVEAU client, HT — toute la dépense publicitaire "
            "divisée par les nouveaux clients, pas par les commandes. Diviser par les "
            "commandes donne un « CAC » flatteur de 20 à 40 %, parce qu'il attribue à "
            "l'acquisition des commandes de réachat qui n'ont rien coûté.")
        return o

    dense = [0, 15, 30, 45, 60, 91, 122, 152, 183, 244, 305, 365, 456, 548, 640, 730]
    sparse = [0] + [j for _, j in JALONS_CANONIQUES]
    pb_dense = a.payback_mois(dense)
    pb_sparse = a.payback_mois(sparse)
    o.append("")
    lignes = [["Payback (grille fine, 16 jalons)",
               "jamais atteint" if pb_dense == float("inf") else dec(pb_dense, 1) + " mois"],
              ["Payback (méthode § 3 : jalons 1/3/6/12 mois)",
               "jamais atteint" if pb_sparse == float("inf") else dec(pb_sparse, 1) + " mois"],
              ["Payback canonique § 3 (P5, pour mémoire)", dec(CANONIQUE_PAYBACK, 1) + " mois"]]
    o += tableau(["Délai de récupération du CAC", ""], lignes, ["g", "d"])
    o.append("")
    o += paragraphe(
        "Les deux premières lignes mesurent la même chose sur la même donnée et ne "
        "donnent pas le même nombre : un payback obtenu par interpolation dépend du pas "
        "de la grille. Avant de comparer ton payback à celui d'une autre marque, demande "
        "sur quels jalons il a été interpolé.")

    r12 = a.ratio_ltv_cac(365)
    if r12 == r12:
        o.append("")
        if r12 >= 2.0 and pb_dense <= 4:
            verdict = f"LTV/CAC 12 mois = {dec(r12, 2)} et payback ≤ 4 mois : on peut accélérer."
        elif r12 < 1.5:
            verdict = f"LTV/CAC 12 mois = {dec(r12, 2)} < 1,5 : on ne scale pas, on répare."
        elif r12 > 5.0:
            verdict = f"LTV/CAC 12 mois = {dec(r12, 2)} > 5 : tu sous-investis en acquisition."
        else:
            verdict = f"LTV/CAC 12 mois = {dec(r12, 2)} : zone intermédiaire, arbitrage à faire."
        o += cadre(verdict)
        o += paragraphe("Règle de décision : chiffres canoniques § 3.")
    return o


def bloc_alerte(a: Analyse, al: Alerte, mode: str) -> List[str]:
    o = titre("6. ALERTE — les cohortes récentes tiennent-elles la comparaison ?")
    o += paragraphe(
        f"Comparaison À ÂGE ÉGAL des {ent(al.n_recentes)} dernières cohortes observables "
        f"avec toutes celles qui précèdent. Seuil de déclenchement : "
        f"{pct(al.seuil, 0)} d'écart défavorable. Valeur comparée : {UNITES[mode]}.")
    o.append("")

    if not al.ecarts:
        o += paragraphe(
            "Pas assez de cohortes pour comparer quoi que ce soit. Il en faut au moins "
            f"{ent(al.n_recentes + 2)} observables à un même âge. Reviens avec plus "
            "d'historique, ou baisse --cohortes-recentes.")
        return o

    lignes = []
    for e in al.ecarts:
        drapeau = "◄" if e in al.declenchees else " "
        lignes.append([f"M{e.age}", ent(len(e.anciennes)), ent(len(e.recentes)),
                       _fmt(e.valeur_anc, mode), _fmt(e.valeur_rec, mode),
                       pct_signe(e.ecart_relatif),
                       pct_signe(e.ecart_reachat) if e.reachat_anc else "—",
                       drapeau])
    o += tableau(["Âge", "Anc.", "Réc.", "Anciennes", "Récentes", "Écart",
                  "Réachat seul", ""],
                 lignes, ["g", "d", "d", "d", "d", "d", "d", "g"])
    o.append("")
    o += paragraphe(
        "La colonne « Réachat seul » retire la 1ʳᵉ commande, qui est un plancher "
        "constant à 1,00 et qui dilue tout écart. C'est elle qui bouge en premier : "
        "l'alerte y est lisible plusieurs mois avant de l'être sur la colonne « Écart ».")
    o.append("")

    e = al.pire
    if e is None:
        profond = max(al.ecarts, key=lambda x: x.age)
        pire = min(al.ecarts, key=lambda x: x.ecart_relatif)
        o += cadre(f"Pas de dégradation au seuil de {pct(al.seuil, 0)}.")
        o += paragraphe(
            f"À l'âge le plus profond comparable (M{profond.age}), les cohortes "
            f"récentes font {pct_signe(profond.ecart_relatif)} par rapport aux "
            f"anciennes.")
        o.append("")
        o += paragraphe(
            f"Le plus mauvais écart de tout le tableau est {pct_signe(pire.ecart_relatif)} "
            f"à M{pire.age} ({pct_signe(pire.ecart_reachat)} sur le réachat seul). "
            f"Il n'a pas franchi le seuil que TU as fixé : relis-le avant de conclure "
            f"que tout va bien, et regarde la colonne « Réachat seul », qui bouge la "
            f"première.")
        return o

    o += cadre(f"DÉGRADATION CONFIRMÉE À M{e.age} : {pct_signe(e.ecart_relatif)} "
               f"({pct_signe(e.ecart_reachat)} sur le réachat seul)")
    o += paragraphe(
        f"Les cohortes {libelle_mois(e.recentes[0])} à {libelle_mois(e.recentes[-1])} "
        f"({ent(e.clients_rec)} clients) valent {_fmt_unite(e.valeur_rec, mode)} à "
        f"M{e.age}, contre {_fmt_unite(e.valeur_anc, mode)} pour les "
        f"{ent(len(e.anciennes))} cohortes antérieures ({ent(e.clients_anc)} clients) "
        f"au même âge. Écart : {_fmt_unite(e.ecart_absolu, mode, signe=True)}, "
        f"soit {pct_signe(e.ecart_relatif)}.")

    ages = ", ".join(f"M{x.age}" for x in al.declenchees)
    o.append("")
    o += paragraphe(f"Âges où le seuil est franchi : {ages}.")

    if al.manque_annuel == al.manque_annuel:
        o.append("")
        o += tableau(
            ["Traduction en euros", ""],
            [[f"Contribution par client acquis à M{e.age}, cohortes anciennes",
              eur(al.ltv_anc, 2) + " HT"],
             [f"Contribution par client acquis à M{e.age}, cohortes récentes",
              eur(al.ltv_rec, 2) + " HT"],
             ["Écart par client acquis", eur_signe(al.ltv_rec - al.ltv_anc) + " HT"],
             ["Rythme d'acquisition des cohortes récentes",
              ent(a.clients_par_mois(e.recentes)) + " clients/mois"],
             ["Manque à gagner annualisé, en contribution",
              eur_signe(al.manque_annuel, 0) + " HT"]],
            ["g", "d"])
        o.append("")
        o += paragraphe(
            f"Ce montant est de la contribution, pas du chiffre d'affaires : il descend "
            f"à l'EBITDA presque intégralement, puisque la dépense d'acquisition qui l'a "
            f"produit, elle, a déjà été payée.")
        if a.ncac:
            r_anc = al.ltv_anc / a.ncac
            r_rec = al.ltv_rec / a.ncac
            o.append("")
            o += paragraphe(
                f"Ramené au nCAC de {eur(a.ncac, 2)} HT : le ratio LTV/CAC à M{e.age} "
                f"passe de {dec(r_anc, 2)} à {dec(r_rec, 2)}.")

    if al.passage_anc == al.passage_anc and al.passage_rec == al.passage_rec:
        o.append("")
        o += tableau(
            [f"Indicateur avancé — passage 1ʳᵉ → 2ᵉ commande à {al.passage_jours} jours", ""],
            [["Cohortes anciennes", pct(al.passage_anc)],
             ["Cohortes récentes", pct(al.passage_rec)],
             ["Écart", pts(al.passage_rec - al.passage_anc)]],
            ["g", "d"])
        o.append("")
        o += paragraphe(
            "Ce taux se lit 90 jours après l'acquisition. C'est le premier endroit où "
            "une dégradation devient visible — plusieurs mois avant que le tableau "
            "mensuel ne bouge, et environ un an avant qu'elle n'apparaisse dans le "
            "compte de résultat.")

    o.append("")
    o.append(f"  Détail par cohorte à M{e.age}")
    detail = []
    obs = a.cohortes_observables(e.age)
    for c in obs[-16:]:
        v = a.cellule(c, e.age, mode)
        ecart = (v - e.valeur_anc) / e.valeur_anc if e.valeur_anc else float("nan")
        n90, t90 = a.passage_cohorte(c, 90)
        detail.append([libelle_mois(c), ent(a.tailles[c]), _fmt(v, mode),
                       pct_signe(ecart),
                       pct(t90) if n90 >= MIN_ELIGIBLES else "—",
                       "récente" if c in e.recentes else ""])
    o += tableau(["Cohorte", "Clients", f"M{e.age}", "vs anciennes", "Passage 90 j", ""],
                 detail, ["g", "d", "d", "d", "d", "g"])
    o.append("")
    o += paragraphe(
        "Avant de conclure à une dégradation du produit ou du service, vérifie trois "
        "explications qui n'en sont pas : un changement de mix pays ou de canal "
        "d'acquisition, une promotion agressive qui a recruté des chasseurs de remise, "
        "une cohorte de Black Friday. Les trois abaissent la courbe sans qu'aucun "
        "client n'ait été déçu. Le module E08 en détaille la distinction.")
    return o


def bloc_limites(a: Analyse) -> List[str]:
    o = titre("7. Ce que cet outil ne dit pas")
    o += puces([
        "• Il ne mesure pas l'incrémentalité. Une cohorte qui réachète beaucoup peut "
        "l'avoir fait sans la moindre action de la marque. Le tableau décrit un "
        "comportement observé, pas un effet causé. Module E09.",
        "• Il ne corrige pas le mix. Deux cohortes acquises sur des pays, des canaux ou "
        "des offres différents ne sont pas comparables, même à âge égal. Refais tourner "
        "l'outil sur un export filtré par pays ou par canal avant de conclure.",
        "• Il suppose que l'identifiant client est stable. Un client qui commande une "
        "fois en invité puis une fois avec un compte apparaît comme deux clients, ce qui "
        "écrase la courbe de réachat et gonfle le nombre de nouveaux clients — donc "
        "flatte artificiellement le nCAC apparent.",
        "• Il travaille en date de commande, pas en date d'encaissement ni de livraison. "
        "Pour le cash, c'est le module E10 et un autre calendrier.",
        "• La marge brute est appliquée comme un taux unique. Si le mix produit des "
        "réachats diffère de celui des premières commandes — et il diffère presque "
        "toujours — la contribution des réachats est mal estimée de quelques points.",
        "• Les remboursements négatifs sont écartés, pas déduits : le CA cumulé est donc "
        "un CA brut. Sur une catégorie à fort taux de retour, corrige-le à la main.",
        "• La comparaison anciennes/récentes oppose un bloc récent à TOUT l'historique. "
        "Sur une marque en amélioration continue, cela sous-estime la dégradation "
        "récente ; sur une marque en déclin lent, cela l'exagère.",
    ])
    return o


def rapport(a: Analyse, j: Journal, mode: str = "commandes",
            n_recentes: int = 3, seuil: float = 0.10) -> Tuple[str, bool]:
    """Rend le rapport complet. Le booleen dit si l'alerte s'est declenchee."""
    al = construire_alerte(a, n_recentes=n_recentes, seuil=seuil, mode=mode)
    o = bandeau("Tableau de cohortes",
                f"{ent(j.retenues)} commandes · {ent(len(a.clients))} clients · "
                f"{ent(len(a.cohortes))} cohortes")
    o += bloc_lecture(a, j)
    o += bloc_tableau_cohortes(a, mode)
    o += bloc_courbe(a)
    o += bloc_passage(a)
    o += bloc_ltv(a)
    o += bloc_alerte(a, al, mode)
    o += bloc_limites(a)
    o.append("")
    o.append("═" * LARGEUR)
    o += paragraphe(
        "Étalon de lecture : ecommerce/donnees/chiffres-canoniques.md § 3 (marque NØRA, "
        "FICTIVE). Méthode et interprétation : module E08 — la rétention, les cohortes "
        "et la LTV.", indent="")
    return "\n".join(o), al.declenchee


# ---------------------------------------------------------------------------
# 7. LE MODE DÉMONSTRATION
# ---------------------------------------------------------------------------

def chemin_exemple_defaut() -> str:
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "scenarios", "cohortes-exemple.csv")


def rapport_demo(chemin: Optional[str] = None, graine: int = GRAINE_DEFAUT,
                 fin: Optional[datetime.date] = None) -> Tuple[str, bool]:
    """Fabrique le jeu d'exemple, l'analyse, et verifie que l'alerte se declenche."""
    chemin = chemin or chemin_exemple_defaut()
    info = generer_exemple(chemin, graine=graine, fin=fin)

    o = bandeau("Démonstration", "jeu de données fabriqué, dégradation connue d'avance")
    o += paragraphe(
        "Le fichier ci-dessous vient d'être écrit. Sa courbe de réachat reproduit la "
        "courbe canonique du § 3 pour les cohortes anciennes, et une dégradation y a "
        "été INJECTÉE sur les cohortes récentes. On connaît donc la réponse avant de "
        "lancer l'analyse — c'est tout l'intérêt : ce qui suit vérifie l'outil, pas la "
        "marque.")
    o.append("")
    o += paragraphe("Fichier écrit : " + str(info["chemin"]))
    o.append("")
    o += tableau(
        ["Jeu de données fabriqué", ""],
        [["Lignes écrites", ent(info["lignes"])],
         ["Commandes", ent(info["commandes"])],
         ["Lignes de remboursement (montants négatifs)", ent(info["remboursements"])],
         ["Clients", ent(info["clients"])],
         ["Mois d'acquisition", ent(info["cohortes"])],
         ["Période", f"{info['debut']} → {info['fin']}"],
         ["CA TTC total", eur(float(info["ca_ttc"]), 0)],
         ["Dégradation injectée à partir de", str(info["premier_mois_degrade"])],
         ["Facteur de réachat des cohortes dégradées",
          "×" + dec(float(info["facteur"]), 2)],
         ["Clients concernés", ent(info["clients_degrades"])],
         ["Graine aléatoire", ent(graine)]],
        ["g", "d"])
    o.append("")
    o += paragraphe(
        f"Attendu : l'alerte doit se déclencher, et l'écart mesuré sur le RÉACHAT SEUL "
        f"doit tourner autour de "
        f"{pct_signe(float(info['facteur']) - 1, 0)} — c'est le facteur injecté.")
    o.append("")

    commandes, j = lire_csv(chemin)
    a = Analyse(commandes, tva=TVA_DEFAUT, marge_brute=CANONIQUE_MARGE,
                ncac=CANONIQUE_NCAC, horizon=12, min_cohorte=20)
    texte, declenchee = rapport(a, j, mode="commandes", n_recentes=3, seuil=0.10)
    o.append(texte)

    al = construire_alerte(a, n_recentes=3, seuil=0.10, mode="commandes")
    o.append("")
    o += titre("8. Vérification de la démonstration")
    e = al.pire
    lignes = [["Alerte déclenchée", "oui" if declenchee else "NON — l'outil a échoué"],
              ["Facteur de réachat injecté", "×" + dec(float(info["facteur"]), 2)]]
    if e is not None:
        lignes += [["Âge où l'écart est le plus sévère", f"M{e.age}"],
                   ["Écart mesuré sur la valeur", pct_signe(e.ecart_relatif)],
                   ["Écart mesuré sur le réachat seul", pct_signe(e.ecart_reachat)],
                   ["Écart attendu sur le réachat seul",
                    pct_signe(float(info["facteur"]) - 1, 0)],
                   ["Nombre d'âges flagués", ent(len(al.declenchees))]]
    o += tableau(["Contrôle", "Résultat"], lignes, ["g", "d"])
    o.append("")
    if declenchee:
        o += cadre("L'outil retrouve la dégradation qui a été injectée.")
    else:
        o += cadre("ÉCHEC : la dégradation injectée n'a pas été détectée.")
    return "\n".join(o), declenchee


# ---------------------------------------------------------------------------
# 8. LIGNE DE COMMANDE
# ---------------------------------------------------------------------------

def construire_parseur() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="cohortes.py",
        description="Constructeur de tableau de cohortes à partir d'un export de "
                    "commandes. Répond à la seule question qui décide de tout : le "
                    "client acquis aujourd'hui vaut-il encore ce que valait celui "
                    "d'il y a un an ?",
        epilog="Le CSV a besoin d'une date de commande, d'un identifiant client et "
               "d'un montant TTC. Les noms usuels sont reconnus seuls ; sinon, "
               "--colonne-date, --colonne-client et --colonne-montant les imposent. "
               "Les taux se saisissent en points : --marge-brute 61,5 vaut 61,5 %%.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    m = p.add_argument_group("modes — un seul à la fois")
    m.add_argument("--fichier", metavar="CSV", help="export de commandes à analyser")
    m.add_argument("--generer-exemple", nargs="?", const="", metavar="CSV",
                   help="écrit un CSV de démonstration réaliste, puis s'arrête "
                        "(défaut : ecommerce/outils/scenarios/cohortes-exemple.csv)")
    m.add_argument("--demo", action="store_true",
                   help="fabrique le CSV d'exemple, l'analyse, et vérifie que l'alerte "
                        "de dégradation se déclenche")

    g = p.add_argument_group("colonnes du fichier")
    g.add_argument("--colonne-date", metavar="NOM", help="colonne de date de commande")
    g.add_argument("--colonne-client", metavar="NOM", help="colonne d'identifiant client")
    g.add_argument("--colonne-montant", metavar="NOM", help="colonne de montant TTC")
    g.add_argument("--colonne-commande", metavar="NOM",
                   help="colonne d'identifiant de commande — à donner si l'export est "
                        "au niveau LIGNE DE PRODUIT : les lignes seront regroupées")
    g.add_argument("--garder-negatifs", action="store_true",
                   help="conserve les montants négatifs au lieu de les écarter "
                        "(par défaut ils sont traités comme des remboursements)")

    g = p.add_argument_group("paramètres économiques")
    g.add_argument("--valeur", choices=MODES_VALEUR, default="commandes",
                   help="ce que contient le tableau : commandes cumulées par client "
                        "acquis (défaut), CA cumulé TTC, ou contribution cumulée")
    g.add_argument("--marge-brute", type=taux, default=None, metavar="%",
                   help="taux de marge brute CM2 en %% du CA HT, après COGS, logistique, "
                        "PSP, retours et remises — ex. 61,5")
    g.add_argument("--ncac", type=nombre, default=None, metavar="€HT",
                   help="coût d'acquisition d'un NOUVEAU client, HT — ex. 40,03")
    g.add_argument("--tva", type=taux, default=TVA_DEFAUT, metavar="%",
                   help="taux de TVA moyen pondéré, en %% (défaut : 20)")

    g = p.add_argument_group("réglages de lecture")
    g.add_argument("--horizon", type=int, default=12, metavar="N",
                   help="dernier mois d'âge affiché, M0 à MN (défaut : 12)")
    g.add_argument("--min-cohorte", type=int, default=20, metavar="N",
                   help="taille minimale d'une cohorte publiée (défaut : 20 clients)")
    g.add_argument("--cohortes-recentes", type=int, default=3, metavar="N",
                   help="nombre de cohortes comparées à l'historique (défaut : 3)")
    g.add_argument("--seuil-alerte", type=taux, default=0.10, metavar="%",
                   help="écart défavorable qui déclenche l'alerte, en %% (défaut : 10)")

    g = p.add_argument_group("génération de l'exemple")
    g.add_argument("--graine", type=int, default=GRAINE_DEFAUT, metavar="N",
                   help=f"graine aléatoire, fixe par défaut ({GRAINE_DEFAUT}) : deux "
                        "exécutions donnent le même fichier")
    g.add_argument("--fin-exemple", metavar="AAAA-MM-JJ", default=None,
                   help=f"dernier jour du jeu d'exemple (défaut : "
                        f"{FIN_EXEMPLE_DEFAUT.isoformat()})")
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
        print("\nAucun mode demandé. Commence par --demo : l'outil fabrique un jeu de "
              "données, l'analyse, et te montre l'alerte se déclencher sur une "
              "dégradation qu'il a lui-même injectée.")
        return 2

    ns = parseur.parse_args(argv)
    modes = [ns.fichier is not None, ns.generer_exemple is not None, ns.demo]
    if sum(1 for m in modes if m) != 1:
        return _echec(["choisis exactement un mode : --fichier, --generer-exemple "
                       "ou --demo."])

    fin = None
    if ns.fin_exemple:
        fin = lire_date(ns.fin_exemple)
        if fin is None:
            return _echec([f"--fin-exemple : « {ns.fin_exemple} » n'est pas une date "
                           "AAAA-MM-JJ."])

    if ns.demo:
        texte, ok = rapport_demo(graine=ns.graine, fin=fin)
        print(texte)
        return 0 if ok else 1

    if ns.generer_exemple is not None:
        chemin = ns.generer_exemple or chemin_exemple_defaut()
        info = generer_exemple(chemin, graine=ns.graine, fin=fin)
        print("\n".join(
            paragraphe("Fichier écrit : " + str(info["chemin"])) + [""] +
            tableau(["Jeu de données de démonstration écrit", ""],
                    [["Lignes", ent(info["lignes"])],
                     ["Commandes", ent(info["commandes"])],
                     ["Clients", ent(info["clients"])],
                     ["Mois d'acquisition", ent(info["cohortes"])],
                     ["Période", f"{info['debut']} → {info['fin']}"],
                     ["CA TTC total", eur(float(info["ca_ttc"]), 0)],
                     ["Dégradation injectée à partir de", str(info["premier_mois_degrade"])],
                     ["Facteur de réachat des cohortes dégradées",
                      "×" + dec(float(info["facteur"]), 2)],
                     ["Graine", ent(ns.graine)]],
                    ["g", "d"])))
        print("")
        print("\n".join(paragraphe(
            "Analyse-le maintenant : python3 ecommerce/outils/cohortes.py --fichier "
            f"{info['chemin']} --marge-brute 61,5 --ncac 40,03")))
        return 0

    if ns.valeur == "contribution" and ns.marge_brute is None:
        return _echec(["--valeur contribution exige --marge-brute (ex. --marge-brute 61,5)."])
    if ns.horizon < 1 or ns.horizon > 60:
        return _echec(["--horizon doit être compris entre 1 et 60 mois."])
    if ns.cohortes_recentes < 1:
        return _echec(["--cohortes-recentes doit valoir au moins 1."])
    if not 0 < ns.tva < 1:
        return _echec(["--tva doit être un taux plausible, en points (ex. 20)."])
    if ns.marge_brute is not None and not 0 < ns.marge_brute < 1:
        return _echec(["--marge-brute doit être un taux entre 0 et 100 points."])

    try:
        commandes, j = lire_csv(ns.fichier, ns.colonne_date, ns.colonne_client,
                                ns.colonne_montant, ns.colonne_commande,
                                ns.garder_negatifs)
    except ValueError as err:
        return _echec([str(err)])

    a = Analyse(commandes, tva=ns.tva, marge_brute=ns.marge_brute, ncac=ns.ncac,
                horizon=ns.horizon, min_cohorte=ns.min_cohorte)
    if not a.cohortes:
        return _echec([
            "aucune cohorte publiable : soit le fichier couvre moins d'un mois complet, "
            f"soit toutes les cohortes font moins de {ns.min_cohorte} clients "
            "(voir --min-cohorte)."])

    texte, declenchee = rapport(a, j, mode=ns.valeur, n_recentes=ns.cohortes_recentes,
                                seuil=ns.seuil_alerte)
    print(texte)
    return 0


if __name__ == "__main__":
    sys.exit(main())
