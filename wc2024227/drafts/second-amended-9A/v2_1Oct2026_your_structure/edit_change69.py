exec(open('edit_change68.py').read().split("CAUSAL=")[0])
d=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx')
d.rep('The Respondent does not allege that any communication was sent to Logan Switch','[¶ 69]',
 "[¶ 69] The Appellant's evidence is that he received the complaints about the misdirected calls at the time, and saw the Registrar's emails about them, and that the feedback he received about those calls came from the registrars themselves, not from management.")
d.rep('Nine occasions of calls reaching the wrong team','including a MET-call enquiry;','including a MET-call enquiry, with the complaints and feedback reaching the Appellant from the registrars;')
d.save(); print('ok')
