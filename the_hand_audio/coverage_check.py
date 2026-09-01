#!/usr/bin/env python3
"""
Coverage check: confirm the scripts still carry every entity in the source book.

Usage:  python3 coverage_check.py path/to/book.txt

Numerals are deliberately spelled out in the scripts (the speech engine reads
"39639" badly), so a miss here is only a real miss if the spoken form is absent
too — those pairs are listed in SPOKEN_FORMS and checked separately.
"""
import glob, os, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))

def norm(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()

ENTITIES = [
 "balslev","balsley","kele","mary ann brown","levendale","richmond","cutting grass",
 "oatlands","launceston","mabel","helena may","lilly","sydney balsley","william john",
 "maisie florence","bryce peter","gordon sydney thomas","turakina","rangitikei",
 "pakaraka","maxwell","maxwelltown","whanganui","portmairremener","oyster bay",
 "prosser","little swanport","eastern marshes","runnymede","leven banks","st chad",
 "friedrich buck","hamburg","sorell creek","danevirke","schleswig","holstein",
 "treaty of vienna","funen","copenhagen","rigsarkivet",
 "handley's woolshed","waitotara","nukumaru","tauranga ika","nga rauru kitahi",
 "ngati maika","ngati ruanui","titokowaru","kai-iwi","whitmore","john bryce",
 "george maxwell","agra","parihaka","ihaka takarangi",
 "tamou","kimi","pare","peter neilson","peter terapa","pita wiwo","tame kimi",
 "tio kimi","harriet","te pohe","matiu","phillips","maria tamou","agnes el hama",
 "linda rebecca","leoni mariana","mathew","rosalie","thomas sydney balsley",
 "kiel gordon balsley",
 "point 209","tebaga","mareth","long range desert group","supercharge","hikurangi",
 "ngati porou","ngarimu","victoria cross","spandau","meisser","vickers",
 "bennett","kippenberger","freyberg","montgomery","wilson","military medal",
 "panzer grenadier","pukehika","kaipo","rangiwaea","araukuku","paratupu",
 "atihau","parininihi","maori trustee","blair","pearce","stout","aotea",
 "he whiritaunoka","waitangi tribunal","native land court","royal commission",
 "court of appeal","ruruku whakatupua","ngati haua","geographic board",
 "london gazette","trove","tasmanian names index",
 "shearer","knife hand","labourer","tally","seasonal round",
 "recorded","unverified","inferred","not established","broken",
 "annexure","ratana","marae","whakapapa","hapu","iwi",
]

# Written numeral -> the spoken form the scripts must contain instead.
SPOKEN_FORMS = {
 "39639": "thirty-nine thousand, six hundred and thirty-nine",
 "W.3121": "w. three one two one",
 "1A1": "one-a-one", "1A2A": "one-a-two-a", "1A2B": "one-a-two-b",
 "1A2B3": "one-a-two-b-three",
 "MLC file 46038": "forty-six thousand and thirty-eight",
 "file 33/0A": "thirty-three stroke oh a",
 "$14.28": "fourteen dollars and twenty-eight cents",
 "$171,500": "hundred and seventy-one thousand, five hundred dollars",
 "1,249 shares": "one thousand two hundred and forty-nine shares",
 "Wai 903": "wai nine hundred and three",
 "NZDF": "new zealand defence force",
 "$3,127": "three thousand one hundred and twenty-seven dollars",
 "$1,124.26": "one thousand one hundred and twenty-four dollars and twenty-six cents",
 "$176.13": "one hundred and seventy-six dollars and thirteen cents",
 "$3,578.67": "three thousand, five hundred and seventy-eight dollars and sixty-seven cents",
 "$4,646.77": "four thousand, six hundred and forty-six dollars and seventy-seven cents",
 "$21.74": "twenty-one dollars and seventy-four cents",
 "0.1786 shares": "nought point one seven eight six",
 "Point 209": "point two-oh-nine",
}

def main():
    scripts = norm("\n".join(
        open(f, encoding="utf-8").read()
        for f in sorted(glob.glob(os.path.join(HERE, "scripts", "*.md")))))

    missing = [e for e in ENTITIES if e not in scripts]
    if len(sys.argv) > 1:                       # only flag things the book actually has
        book = norm(open(sys.argv[1], encoding="utf-8").read())
        missing = [e for e in missing if e in book]

    bad_numerals = {k: v for k, v in SPOKEN_FORMS.items() if v not in scripts}

    print(f"entities:  {len(ENTITIES) - len(missing)}/{len(ENTITIES)} present")
    print(f"numerals:  {len(SPOKEN_FORMS) - len(bad_numerals)}/{len(SPOKEN_FORMS)} spoken forms present")

    questions = sum(1 for n in range(1, 41)
                    if f"question {n}." in scripts or _word(n) in scripts)
    print(f"questions: {questions}/40 voiced")

    if missing:
        print("\nMISSING ENTITIES:")
        for e in missing:
            print("  -", e)
    if bad_numerals:
        print("\nMISSING SPOKEN NUMERALS:")
        for k, v in bad_numerals.items():
            print(f"  - {k}  (expected: \"{v}\")")
    if not missing and not bad_numerals:
        print("\nOK — the scripts carry the whole book.")
    return 1 if (missing or bad_numerals) else 0

_WORDS = ("zero one two three four five six seven eight nine ten eleven twelve "
          "thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty").split()
def _word(n):
    if n <= 20:
        return f"question {_WORDS[n]}."
    tens, unit = divmod(n, 10)
    base = {2: "twenty", 3: "thirty", 4: "forty"}[tens]
    return f"question {base}." if unit == 0 else f"question {base}-{_WORDS[unit]}."

if __name__ == "__main__":
    sys.exit(main())
