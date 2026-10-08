exec(open('edit_change68.py').read().split("CAUSAL=")[0])
d=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx')
d.rep('The Respondent does not allege that any communication was sent to Logan Switch',
 "The Appellant's evidence is that he received the complaints about the misdirected calls at the time, and saw the Registrar's emails about them, and that the feedback he received about those calls came from the registrars themselves, not from management.",
 "The Appellant's evidence is that the complaints about the misdirected calls reached him at the time in the registrars' own calls to the Switchboard, and that what he received from the Manager about them was her email to Logan Switch at 10:15 am on 9 May 2024. [¶¶ 66 to 67] The Registrar's emails of 3 and 8 May 2024 were addressed to the Manager and Dr Wong. [¶¶ 56, 59]")
d.rep('Nine occasions of calls reaching the wrong team','with the complaints and feedback reaching the Appellant from the registrars;','with the complaints reaching the Appellant in the registrars\' own calls to the Switchboard;')
d.save(); print('ok')
d=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx')
d.rep('The Respondent does not allege that any communication was sent to Logan Switch',
 "and that what he received from the Manager about them was her email to Logan Switch at 10:15 am on 9 May 2024. [¶¶ 66 to 67] The Registrar's emails of 3 and 8 May 2024 were addressed to the Manager and Dr Wong. [¶¶ 56, 59]",
 "and that what he received from the Manager about them was her email to Logan Switch at 10:15 am on 9 May 2024, which stated that it included the email trail below it for reference. [¶¶ 66 to 67] The Registrar's emails of 3 and 8 May 2024 were addressed to the Manager and Dr Wong [¶¶ 56, 59]; the Appellant's evidence is that he saw them in that trail on 9 May 2024.")
d.save(); print('ok2')
