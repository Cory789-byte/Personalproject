# Letter: replace 'How the admitted facts are relied on' with a positive statement of what is relied on, what is admitted,
# and what the hearing member decides on that record.
exec(open('edit_change68.py').read().split("CAUSAL=")[0])
src=open('edit_change72.py').read(); exec(src[src.index('def set_body'):src.index('# ================= ELECTION')])
L=Doc('2026-10_LETTER_to_Registry_FINAL.docx')
L.rep('How the admitted facts are relied on.','How the admitted facts are relied on. ','What is relied on, and what is admitted. ')
set_body(L,'What is relied on, and what is admitted.',
 "The proposed Form 9A relies on the facts admitted by the Respondent on 8 September 2026, each marked with its paragraph number in square brackets; the documents at Annexure A, 29 of which are admitted or since confirmed (Schedule, Part 1); the other documents in Part 2 of the schedule; the treating practitioners' records, with their oral evidence; and the Appellant's own evidence, which carries no bracket. The events on which the three stressors rest are therefore admitted, to the extent recorded in the Respondent's response. What remains is for the hearing member to decide on that record: whether each event was management action, whether any management action was reasonable and taken in a reasonable way, and whether employment was a significant contributing factor to the injury, on the evidence of the treating practitioners.")
L.save(); print('ok')
# precision: name the exceptions to "admitted"
L=Doc('2026-10_LETTER_to_Registry_FINAL.docx')
L.rep('What is relied on, and what is admitted.',"The events on which the three stressors rest are therefore admitted, to the extent recorded in the Respondent's response.",
 "The dated events pleaded as causes are therefore admitted, to the extent recorded in the Respondent's response, except where the proposed Form 9A marks otherwise: the register at Tab 31 (facts 228 to 231, not admitted), Payroll's later account at 2(e), and the Appellant's own evidence.")
L.save(); print('precision ok')
