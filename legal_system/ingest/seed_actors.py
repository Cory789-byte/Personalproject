"""Seed the canonical actor catalogue. These ids are the authoritative
slugs used by the rest of the pipeline.

When a new actor appears in source material, add a row here rather than
creating ad-hoc ids — that keeps cross-references stable.
"""
from __future__ import annotations

import sqlite3

ACTORS = [
    # id                          display_name              role             reg     org    notes
    ("cory-shepherd",              "Cory Lea Shepherd",      "complainant",   None,   None,  "Self-represented; QHRC Complainant EDR19098"),
    ("alexia-negro",               "Alexia Negro",           "aggrieved",     None,   None,  "Named aggrieved on QP0899 / TPO; complainant on QP2500332406"),
    ("laura-phillips",             "Laura Margaret Jean Phillips", "witness", None,  None,  "House-sitter / friend of Negro; key prosecution witness"),
    ("tom-balsey",                 "Tom Balsey",             "witness",       None,   None,  "Independent witness, AFF12 / AFF33"),
    ("leanne-shepherd",            "Leanne Shepherd",        "witness",       None,   None,  "Cory's mother; on Davies BWC at her house"),
    ("isabella-shepherd",          "Isabella Shepherd",      "third_party",   None,   None,  "Cory's younger sister (minor at time of welfare complaint)"),
    ("piergiorgio-gerace",         "Piergiorgio Gerace",     "third_party",   None,   None,  "Named victim on Negro 2018 Miami-Dade stay-away order"),
    ("denis-constable",            "Denis Constable",        "witness",       None,   "Scion building manager", "AFF11; called police 1:54am 24 Feb 2025"),
    ("naoko-arase",                "Naoko Arase",            "witness",       None,   "Leasing manager", "21 Feb 2025 Form 13 acknowledgement email"),
    # QPS officers
    ("ofc-easthope",               "Const. Tyson Easthope",  "qps_officer",   "4043895", "QPS",  "Took Negro statement 25 Feb 2025; BWC Initial Response"),
    ("ofc-bickery",                "Const. Levi Bickery",    "qps_officer",   None,   "QPS",  "Arresting officer; Davies-Bickery at Cory's mum's house"),
    ("ofc-davies",                 "Const. Mitchell Davies", "qps_officer",   "39627", "QPS",  "Arrived at U104; with Bickery at mum's house; 5-page statement undisclosed"),
    ("ofc-harmer",                 "Const. Harmer",          "qps_officer",   None,   "QPS",  "Statement: 'Constable SHEPHERD' perjury anomaly"),
    ("ofc-yaun",                   "SnrConst Ryan Peter Yaun","qps_officer",  "4017516", "QPS Robina", "Issuing officer of QP0899; admitted 'no evidence' email 21 Aug 2025"),
    ("ofc-harris",                 "A/Sgt Bradley Harris",   "qps_officer",   "21175", "QPS Robina", "Authorising officer of QP0899"),
    ("ofc-tulacz",                 "SnrSgt Luke J. Tulacz",  "qps_officer",   None,   "QPS Southport", "OIC who self-investigated SDC 8933558"),
    ("ofc-butler",                 "Const. Butler",          "qps_officer",   None,   "QPS",  "Statement listed Y/3pp on FBOE; never served"),
    ("ofc-contacos",               "Const. Contacos",        "qps_officer",   None,   "QPS",  "Romeo seizure 22 Mar 2025; 'I've got pictures of it'"),
    ("ofc-trilford",               "Const. Trilford",        "qps_officer",   None,   "QPS",  "Romeo seizure 22 Mar 2025"),
    ("ofc-jo",                     "Officer Jo",             "qps_officer",   None,   "QPS",  "Romeo seizure 22 Mar 2025; criminal-history exchange"),
    ("ofc-simpson",                "Const. Simpson",         "qps_officer",   None,   "QPS",  "Service of DV documents"),
    ("ofc-yavuzer",                "Yavuzer Harrison L",     "qps_officer",   None,   "QPS",  "Author of QP9 v1 (Iter 1) 10 Mar 2025"),
    ("ofc-beck",                   "Casey E Beck",           "qps_officer",   "4048952", "QPS", "Author of QP9 v2 (Iter 3) 29 Apr 2026"),
    # Court / legal
    ("magistrate-brunello",        "Magistrate Brunello",    "magistrate",    None,   "Southport Magistrates Court", "Vacated TPO 25 Feb 2025"),
    ("ware-nick",                  "Nick Ware",              "lawyer",        None,   "Howden Saggers Lawyers", "Defence solicitor 25/9/2025; 33-item disclosure schedule"),
    ("sibley-justin",              "Justin Sibley",          "lawyer",        None,   "Sibley Lawyers", "Current defence solicitor"),
    ("plessius-lisa",              "Lisa Plessius",          "prosecutor",    None,   "QPS Prosecutions", "Senior Prosecutor; carriage of file at Ware's letter"),
    ("brooke-winter",              "Brooke Winter",          "lawyer",        None,   "Brooke Winter Solicitors", "Represented Cory at 13 Aug 2025 hearing"),
    # Bodies
    ("qhrc",                       "Queensland Human Rights Commission", "regulator", None, "QHRC", "Conciliation 14 May 2026 — EDR19098"),
    ("ccc",                        "Crime and Corruption Commission",     "regulator", None, "CCC",  "CO-25-2722 + CO-26-1318 open"),
    ("oic",                        "Office of the Information Commissioner", "regulator", None, "OIC", "External Review 318762"),
    ("fsq",                        "Forensic Science Queensland",         "regulator", None, "FSQ",  "Specimen 22403-30264"),
    ("qps",                        "Queensland Police Service",           "agency",    None, "QPS",  "Respondent in QHRC matter"),
]


def seed(conn: sqlite3.Connection) -> int:
    cur = conn.cursor()
    n = 0
    for actor in ACTORS:
        cur.execute(
            """INSERT OR REPLACE INTO actors
               (id, display_name, role, reg_number, organisation, notes)
               VALUES (?,?,?,?,?,?)""",
            actor,
        )
        n += 1
    conn.commit()
    return n
