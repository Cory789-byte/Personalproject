# Pinpoints (Langerak [86], Mahaffey [57]); documentary-record sentence (from the 9 Sep 2026 letter to the Respondent).
exec(open('edit_change68.py').read().split("CAUSAL=")[0])
N=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx')
N.rep('7. The ultimate statutory question',' [2020] ICQ 2, as applied in ',' [2020] ICQ 2 at [86], as applied in ')
N.rep('7. The ultimate statutory question',' [2016] ICQ 10 is consistent with',' [2016] ICQ 10 at [57] is consistent with')
N.rep('How this Part is arranged.','Each stressor is pleaded so that it can be decided on its own facts.',
 'The conduct relied on was, for the most part, done in writing - by email, roster, myHR and payroll record - so each such document is pleaded as the step taken, on the date and in the terms recorded, rather than characterised. Each stressor is pleaded so that it can be decided on its own facts.')
N.save()
L=Doc('2026-10_LETTER_to_Registry_FINAL.docx')
L.rep('How the proposed Form 9A is arranged.','Each of the three stressors is pleaded so that it can be read and assessed on its own facts.',
 "The matter is largely documentary: the directions, rosters, pay claims, requests and replies relied on were made in writing, by email, roster, myHR and payroll record. As stated in the Appellant's letter to the Respondent of 9 September 2026, where the document is itself the step taken, the admission is relied on as establishing that the step was taken on the date and in the terms recorded. The proposed Form 9A therefore sets out each such document with its date and terms, which accounts for its length. Each of the three stressors is pleaded so that it can be read and assessed on its own facts.")
L.save(); print('ok')
