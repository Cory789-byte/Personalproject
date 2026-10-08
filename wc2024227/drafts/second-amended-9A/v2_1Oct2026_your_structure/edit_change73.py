exec(open('edit_change68.py').read().split("CAUSAL=")[0])
l=Doc('2026-10_LETTER_to_Registry_FINAL.docx')
l.rep('The application.','and has admitted or since confirmed 29 of the 39 documents behind them.',
 'and has admitted or since confirmed 29 of the 39 documents behind them. The amendment is sought because the facts have since been largely settled by those admissions. It reorganises the pleading around the admitted record rather than changing the case, so that the issues left for hearing are narrower: whether each circumstance was management action, whether any management action was reasonable and taken in a reasonable way, and causation.')
l.save()
d=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx')
d.rep('Appellant: Cory Lea Shepherd.','employment was a significant contributing factor to it: section 32(1) of the Act.',
 'employment was a significant contributing factor to it: section 32(1) of the Act. The Appellant accepts that he bears the onus of proof (Part C, paragraph 1).')
d.save(); print('ok')
