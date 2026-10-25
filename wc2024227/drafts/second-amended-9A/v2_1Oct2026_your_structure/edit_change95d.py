exec(open('edit_change95.py').read())
d=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx'); R=d.rep
R("Emergency codes, received and paged concurrently (context). The position receives emergency response notifications and distributes them to the appropriate response groups, dependent on the category of emergency, as per emergency code procedures, strictly adhering to protocols and timeframes. [¶ 8]",
  "Emergency codes, received and paged concurrently (context). The position distributes emergency notifications to the response groups by category of emergency. [¶ 8]")
R("Nor does it allege that agreement under clause 6.2 of the Award was obtained before the rostering of the Appellant's shifts on 17 and 18 March 2024 (Stressor 3(b)). [¶ 180]",
  "Nor does it allege clause 6.2 agreement before the roster of 17 and 18 March 2024. [¶ 180]")
R("that telephoning the Switchboard did not comply with the process required of him. [¶ 166]","that telephoning the Switchboard did not comply. [¶ 166]")
d.save(); print("ok")
