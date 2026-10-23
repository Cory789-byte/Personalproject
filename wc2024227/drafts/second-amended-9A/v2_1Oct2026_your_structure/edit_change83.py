# Letter 'The application': witness list and outlines sentence made explicit (as in election item 3) and bold.
exec(open('edit_change68.py').read().split("CAUSAL=")[0])
src=open('edit_change74.py').read(); exec(src[src.index('def boldify_rpr'):src.index('E=Doc(')])
L=Doc('2026-10_LETTER_to_Registry_FINAL.docx')
NEW=("The Appellant's list of witnesses, filed in the Industrial Registry on 9 September 2026 under direction 1, and his outlines of evidence, "
     "served on the Respondent on 9 September 2026 under direction 2, are not amended and stand as filed and served on that date.")
L.rep('The application.',"The Appellant's list of witnesses filed, and outlines of evidence served, on 9 September 2026 are not amended and stand as filed and served.",NEW)
bold(L,NEW)
L.save(); print('ok')
