# Election item 3: witness list and outlines - explicit (served on the Respondent, 9 Sep 2026, directions 1 and 2) and bold.
exec(open('edit_change68.py').read().split("CAUSAL=")[0])
src=open('edit_change74.py').read(); exec(src[src.index('def boldify_rpr'):src.index('E=Doc(')])
E=Doc('2026-10_REQUEST_election_and_directions_FINAL.docx')
NEW=("The Appellant's list of witnesses, filed in the Industrial Registry on 9 September 2026 under direction 1, and his outlines of evidence, "
     "served on the Respondent on 9 September 2026 under direction 2, are not amended and stand as filed and served on that date.")
E.rep('3.',"The Appellant's list of witnesses filed, and outlines of evidence served, on 9 September 2026 are not amended and stand as filed and served.",NEW,contains='proposed Second Amended Statement')
bold(E,NEW)
E.save(); print('ok')
