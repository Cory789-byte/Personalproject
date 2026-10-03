# Stressor 1: letter sentence on the outlines' silence; 9A medical link from the admitted review decision.
exec(open('edit_change68.py').read().split("CAUSAL=")[0])
exec(open('edit_change74.py').read().split("E=Doc(")[0].split("CAUSAL=")[-1] if False else '')
src=open('edit_change74.py').read(); exec(src[src.index('def boldify_rpr'):src.index('E=Doc(')])
L=Doc('2026-10_LETTER_to_Registry_FINAL.docx')
L.rep("The Respondent's notified case",'. The Appellant asks that, at the opening of the conference,',
 '. Its outlines give no account of the dated events at Stressor 1(b), 1(f), 1(h) and 1(k): the removal of database access, the 15 April 2024 process change, the misdirected calls, and the directory error reported by the Integrated Respiratory Service. The Appellant asks that, at the opening of the conference,')
bold(L,'Its outlines give no account of the dated events at Stressor 1(b), 1(f), 1(h) and 1(k)')
L.save()
N=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx')
N.rep('The medical link - Stressor 1.','Tab M1 records the 28 June 2024 presentation as "stress at work" and "upset by people not following rules".',
 'Tab M1 records the 28 June 2024 presentation as "stress at work" and "upset by people not following rules". Review Decision 69983 (Tab 25; Tab M8) records that WorkCover spoke with Dr Hawes on 2 September 2024 and that he opined that the injury was caused by, among other things, "management failing to follow rules"; it records "Non-adherence to rules by management" among the factors "identified by your doctor as medically causative".')
N.save(); print('ok')
