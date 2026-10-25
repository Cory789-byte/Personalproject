exec(open('edit_change95.py').read())
d=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx'); R=d.rep
# 1 M1 spelling
R('"No psychological illness such as depression/ psychosis"','"No psycological [sic] illness such as depression/ psycosis [sic]"')
# 2 referral renewed
R("The referral letter of 16 May 2024 (Dr Zhao) referred the Appellant to a psychiatrist, Dr Amini,","The referral letter of 16 May 2024 (Dr Zhao) renewed the Appellant's referral to a psychiatrist, Dr Amini,")
R("It lists the past medical history as the history-list items","Its past medical history includes the history-list items")
R("The referral was made the day after the request to retract","The referral was renewed the day after the request to retract")
# 3 singular 15 April change
R("process changes made effective the day they were notified, with no listed record of consultation [¶¶ 51, 181, 273]","the 15 April 2024 process change made effective the day it was notified, with no listed record of consultation [¶¶ 51, 181, 273]")
R("changes to process made effective the day they were notified, with no listed record of consultation;","the 15 April 2024 process change made effective the day it was notified, with no listed record of consultation;")
# 4 add 219
R("read with the May risk-matrix discussion [¶¶ 264, 269 to 271]","read with the May risk-matrix discussion [¶¶ 219, 264, 269 to 271]")
# 5 assessment
R("no fatigue risk management at the Switchboard before 30 June 2024; and the Respondent's own review","fatigue risk management assessment at the Switchboard implemented only after 30 June 2024; and the Respondent's own review")
R("or the absence of fatigue risk management at the Switchboard before 30 June 2024.","or the implementation of fatigue risk management assessment at the Switchboard only after 30 June 2024.")
# 6 delete unsupported sentence
R(" In all that time the Respondent alleges no step other than those listed. [¶¶ 185 to 197, 203, 209, 242 to 247]"," [¶¶ 185 to 197, 203, 209, 242 to 247]")
# 7 253-255
R("It records that payroll was, as at 1 May 2024, still reviewing his entitlements; that the employer did not mention his shift on 18 March 2024; and that there was uncertainty between him and the employer regarding whether the 8-hour agreement continued to apply. [¶¶ 253 to 255]",
  'It records that payroll was, as at 1 May 2024, still reviewing his entitlements regarding public holidays not required [¶ 255]; that "The employer did not mention your shift on 18 March 2024" [¶ 253]; and that there was uncertainty between him and the employer regarding whether the 8-hour agreement continued to apply. [¶ 254]')
# 8 RBWH quote restored
R("from Switchboard Services… identifying the type of Code Blue","from Switchboard Services (except for Code Blue – external medical emergency and neonatal emergency) identifying the type of Code Blue")
# 9 include 154
R("and facts 228 to 231 were not admitted.","and facts 154 and 228 to 231 were not admitted.")
R("The Respondent's amended List of Documents of 14 August 2026 does not list the Communication Book, nor any page or entry from it; that proposition (paragraph 154 of the notice) was not admitted.",
  "The Appellant says that the Respondent's amended List of Documents of 14 August 2026 does not list the Communication Book; that proposition (paragraph 154 of the notice) was not admitted.")
# 10 tabs
R("[Tab M2; Respondent's items 7 and 8.]","[Tabs M1, M2 and M8; Respondent's items 7 and 8.]")
# 11 timing of decline
R("with the Respondent acknowledging that attachments were present when the later decline was made [¶¶ 116, 118, 134]","with the Respondent acknowledging that the attachments were present [¶¶ 116, 118, 134]")
R("the supporting attachments were in fact present when the later decline was made;","the supporting attachments were in fact present;")
# 12 1(k)
R("In that time the Respondent alleges no response to the Service,","Before the escalation the Respondent alleges no response to the Service, and in that time it alleges")
# 13 256
R('The Manager confirmed "that since your commencement','The review decision records the Manager as confirming "that since your commencement')
# 14 tab 25 only
R("Review Decision 69983 (Tab 25; Tab M8) records that WorkCover spoke","Review Decision 69983 (Tab 25) records that WorkCover spoke")
# 15 writing
R("So the day after the consecutive shifts was recorded against","The day after the consecutive shifts was recorded against")
R("The refusal relied on an agreement signed at a time the Respondent does not allege the Manager held that role, and not alleged to have been reviewed before 18 March 2024;",
  "The refusal relied on an agreement signed when the Respondent does not allege Ms Taylor was the Switchboard Manager, and not alleged to have been reviewed before 18 March 2024;")
# 16 term
R("So the guideline treated the Award under which the Appellant was employed as a supporting document.","So the guideline listed the Award under which the Appellant was employed among its related documents.")
# 19 cite style
R("(Form 24, paragraph 25)","(paragraph 25 of the Appellant's first notice to admit facts)")
d.save(); print("ok")
