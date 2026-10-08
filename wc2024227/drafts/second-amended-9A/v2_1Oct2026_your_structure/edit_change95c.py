exec(open('edit_change95.py').read())
d=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx'); R=d.rep
R("(Tab M6, the treating psychiatrist's clinical records, to be served on receipt)","(Tab M6 to follow)")
R("that notifying his unavailability by telephoning the Switchboard did not comply with the process required of him. [¶ 166]","that telephoning the Switchboard did not comply with the process required of him. [¶ 166]")
R("Database access removed, with no restoration alleged;","Database access removed; no restoration alleged;")
R("Operators' access to the database removed, with no restoration alleged;","Operators' access to the database removed; no restoration alleged;")
R('; the AVAC lodged that day was recorded "Part Completed" on 30 May.','; the AVAC was recorded "Part Completed" on 30 May.')
R("Seroquel 25 mg commenced, at half a tablet for three nights and then one tablet at night,","Seroquel 25 mg commenced,")
d.save(); print("ok")
