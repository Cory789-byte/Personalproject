#!/usr/bin/env python3
"""WC/2024/227 — sweep the served set against the 303 facts and the 8 September 2026 response.

Three passes:

  1. Every fact number any served document points at, checked against the response. Anything
     the Regulator did NOT admit is flagged, so a document can never rest on a refused fact
     without the flag being seen.
  2. Every quoted phrase in the served documents, searched across all 303 facts. A phrase that
     is not in the facts is reported, because it must then be proved by a document or by oral
     evidence rather than by admission.
  3. The request letter's schedule, tab by tab: does each fact it cites actually name that tab?

⛔ The citation scanner is the part that has to be right. An earlier version used a character
class to read the numbers after "facts", which silently swallowed trailing prose and then
discarded the whole citation: "Facts 228 to 231 not admitted" parsed as nothing, so four refused
facts read as clean. This version consumes only numbers and the connectors that join them and
stops at the first other token. The self-test at the foot locks that behaviour in; run it.

Usage:  python3 drafts/check_facts_against_response.py
"""
import csv, glob, json, os, re, sys
from pypdf import PdfReader

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
os.chdir(REPO)

FACTS_JSON = "documents/regulator-response-2026-09-08/FORM24_FACTS.json"
RESPONSE_TSV = "documents/regulator-response-2026-09-08/FORM24_RESPONSE_parsed_fact_by_fact.tsv"
SERVED = sorted(glob.glob("drafts/out/FINAL_9SEP2026/1_COMMISSION/*.pdf")) + \
         sorted(glob.glob("drafts/out/FINAL_9SEP2026/2_REGULATOR/*.pdf"))

DASH = re.compile(r"[‐-―−]")
KEY = re.compile(r"(facts?|paragraphs?|paras?|¶+|items?|tabs?)\s*", re.I)
TOKEN = re.compile(r"\s*(?:(\d{1,3})|(to|and|through)\b|([,\-]))", re.I)


def norm(s):
    return DASH.sub("-", re.sub(r"\s+", " ", s)).replace("’", "'") \
              .replace("“", '"').replace("”", '"').strip()


def citations(text):
    """{number: keyword} for every number a document points at, ranges expanded."""
    t = norm(text)
    found = {}
    for k in KEY.finditer(t):
        kind = k.group(1).lower().rstrip("s").replace("¶", "paragraph")
        if kind.startswith("para"):
            kind = "paragraph"
        i, nums, pending = k.end(), [], False
        while True:
            m = TOKEN.match(t, i)
            if not m:
                break
            i = m.end()
            if m.group(1):
                n = int(m.group(1))
                if pending and nums and nums[-1] <= n <= 303:
                    nums.extend(range(nums[-1] + 1, n + 1))
                else:
                    nums.append(n)
                pending = False
            elif m.group(2):
                pending = m.group(2).lower() in ("to", "through")
            else:
                pending = m.group(3) == "-"
        for n in nums:
            if 1 <= n <= 303:
                found.setdefault(n, kind)
    return found


def selftest():
    cases = [
        ("Facts 228 to 231 not admitted. Fact 268 admits", {228, 229, 230, 231, 268}),
        ("No request is made in respect of fact 154 or Tab 24.", {154, 24}),
        ("facts 185 to 203 and 211 to 221, admitted", set(range(185, 204)) | set(range(211, 222))),
        ("Facts 14 and 15", {14, 15}),
        ("facts 2, 13, 214, 218, 263 to 265 and 269 to 271",
         {2, 13, 214, 218, 263, 264, 265, 269, 270, 271}),
        ("[¶¶ 17–25, 211–227, 285]",
         set(range(17, 26)) | set(range(211, 228)) | {285}),
    ]
    bad = [s for s, exp in cases if set(citations(s)) != exp]
    if bad:
        sys.exit("⛔ citation scanner self-test FAILED on:\n  " + "\n  ".join(bad))
    print("citation scanner self-test: passed\n")


def main():
    selftest()
    facts = json.load(open(FACTS_JSON))
    allfacts = " || ".join(norm(v) for v in facts.values())
    status = {}
    for row in csv.reader(open(RESPONSE_TSV), delimiter="\t"):
        if row and row[0].isdigit():
            status[int(row[0])] = row[1]
    refused = sorted(n for n, v in status.items() if v != "Admitted")
    print(f"response: {len(status)} facts, {sum(1 for v in status.values() if v=='Admitted')} admitted, "
          f"not admitted {refused}\n")

    print("1. FACT NUMBERS POINTED AT")
    touched = []
    for d in SERVED:
        txt = " ".join((p.extract_text() or "") for p in PdfReader(d).pages)
        c = {n: k for n, k in citations(txt).items() if k in ("fact", "paragraph")}
        if not c:
            continue
        bad = sorted(n for n in c if status.get(n) != "Admitted")
        print(f"   {os.path.basename(d)[:58]:58s} {len(c):3d} facts  "
              + ("all admitted" if not bad else f"⚠ not admitted: {bad}"))
        if bad:
            touched.append((os.path.basename(d), bad))

    print("\n2. QUOTED PHRASES")
    QUOTE = re.compile(r'"([^"]{6,200})"')
    outside = []
    for d in SERVED:
        txt = norm(" ".join((p.extract_text() or "") for p in PdfReader(d).pages))
        for m in QUOTE.finditer(txt):
            q = norm(m.group(1))
            if q not in allfacts and not (len(q) > 40 and q[:40] in allfacts):
                outside.append((os.path.basename(d), q))
    if outside:
        print("   not in any of the 303 facts — proved by document or oral evidence, not admission:")
        for f, q in outside:
            print(f"     {f[:44]:44s} \"{q[:70]}\"")
    else:
        print("   every quoted phrase appears verbatim in a fact")

    print("\n3. REQUEST LETTER: fact-to-tab")
    claims = {"31": range(228, 232), "1": range(1, 14), "5": [38], "6": [49, 163],
              "17": [14, 15], "18": [14, 15], "19": [14, 15], "20": range(263, 269),
              "21": [224], "22": range(169, 176), "23": [167, 176], "30": [71, 72],
              "30A": [85, 86, 87]}
    mismatch = []
    for tab, ns in claims.items():
        for n in ns:
            named = set(re.findall(r"Tab\s*(\d+[A-Z]?)", facts[str(n)]))
            if named and tab not in named:
                mismatch.append((tab, n, sorted(named)))
    print("   every fact names the tab the letter puts it against" if not mismatch
          else "   ⚠ " + "; ".join(f"Tab {t}: fact {n} names {x}" for t, n, x in mismatch))

    print()
    if touched:
        print("⚠ a served document points at a fact that was not admitted — check each is deliberate")
        for f, b in touched:
            print(f"   {f}: {b}")
    else:
        print("No served document rests on a fact the Regulator did not admit.")


if __name__ == "__main__":
    main()
