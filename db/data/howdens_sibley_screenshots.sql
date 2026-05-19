-- ============================================================================
-- Howdens / SIBLEY (file 001) — matter row + 20 screenshot rows
--
-- Source folder: Google Drive Screenshots_SIBLEY (id 1xWxU-8zp5LgkHOjCSxIt3n4HVmAZFOSJ)
-- Dual-frame tagging:
--   Frame A — curator's framing (curated against respondent, i.e. against Cory)
--   Frame B strands:
--     B1_lease_displacement     joint tenancy → sole-name lease in complainant's name
--     B2_dvo_as_property_tool   DVO invoked to settle a tenancy / property dispute
--     B3_third_party_recruitment  property manager, respondent's family etc. enlisted
--     B4_verbal_labelling       name-calling / labelling applied in complainant's chat
--     B5_untested_allegations   serious allegations made to third parties without
--                               independent corroboration in this set
--     B6_engaging_process       respondent engaging with lease/court/police process
--     B7_financial_asymmetry    contemporaneous statements consistent with
--                               respondent paying / complainant not contributing
--     gap                       zero-byte / unreadable file
--
-- Run on MySQL:
--   mysql -u root -p southport_matter < db/data/howdens_sibley_screenshots.sql
--
-- File is idempotent: INSERT ... ON DUPLICATE KEY UPDATE on (matter_id, file_id).
-- ============================================================================

USE southport_matter;

-- ---- Matter row ----
INSERT INTO matters (matter_ref, parties, court, evidence_root, opened_on, notes)
VALUES (
  'HOWDENS-SIBLEY-001',
  'Sibley criminal matter (Howden Saggers defence)',
  'Magistrates Court of Queensland, Southport',
  'C:\\Evidence\\Howdens\\001_SIBLEY',
  NULL,
  'Curated screenshots reviewed; dual-frame (A vs B) tagging applied. See v_screenshots_by_strand. Counter-narrative emphasises lease acquisition + financial asymmetry.'
)
ON DUPLICATE KEY UPDATE
  parties = VALUES(parties),
  court = VALUES(court),
  evidence_root = VALUES(evidence_root),
  notes = VALUES(notes);

SET @m := (SELECT id FROM matters WHERE matter_ref = 'HOWDENS-SIBLEY-001');

-- ---- Screenshots ----

-- 1. Cory FB message advising friend attendance — conciliatory
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1zxKJPs31iHm9w8sgtbsG81Jt9258mfk2',
  'Cory_FB_msg_to_Alexia_regarding_attending_appt.png', NULL, 'Cory Shepherd',
  'I''m going to sleep just advise your friend 8Am please. I''m always late so you never know. I also offered morris a place to stay, the homeless one his friends are planning a big soup so tomorrow night your friend could even join them. I won''t be there but just respect my decision and boundaries.',
  'control_by_cory', 'cory_courtesy_notice', 'B6_engaging_process',
  'Tone conciliatory; advance notice of attendance; respects boundaries.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), sender=VALUES(sender),
  verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 2. Cory email "Peace and love" asserting lease entry right
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1GRF-QlECZKUup9n70xgL70zRLt_qQs-g',
  'Cory_claiming_he_can_enter_appt.png', NULL, 'Cory Shepherd',
  'Subject: Peace and love towards each other. ... I am legally able to enter our residence being that I didn''t consent for 3 months ... I could have reported abuse from the beginning and over the past 5 years equally. I even went to the effort to export all of our chat which only allowed you to be the perpetrator even with my apparent threats.',
  'control_by_cory', 'assertion_of_lease_rights', 'B6_engaging_process',
  'Asserts joint tenancy entry right; references long-form chat export that he says shows reciprocal conduct. Cross-ref the Form 18a (file 5) showing joint lease.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), sender=VALUES(sender),
  verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 3. Cory threat to go to police — UNREADABLE (OCR failed twice)
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1ciptSwb_m-KRPxm-IVswrmcPHDgtEdLc',
  'Cory_threat_to_go_to_police.png', NULL, NULL,
  NULL, 'control_by_cory', NULL, 'A_curated_against_respondent',
  'OCR returned no text on two attempts. Filename is curator-applied — not evidence of content. Re-OCR locally or describe to me visually.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), strand=VALUES(strand), notes=VALUES(notes);

-- 4. ZERO BYTES — empty file
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1cHnSGpFb0Yb4DHwCavTA6TwZ_4lvK4f6',
  'Cory_trying_to_coerce_with_kindness_to_come_to_appt.png', NULL, NULL,
  NULL, 'control_by_cory', NULL, 'gap',
  'Zero-byte file in Drive. Re-upload required. Filename is curator-applied only.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), strand=VALUES(strand), notes=VALUES(notes);

-- 5. RTA Form 18a — joint lease evidence
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1oqMEUq5lmmvklZCEEQGBnli1cHS25JgC',
  '17f49f62-ba6a-401e-bf55-ea714ed74305.jpeg', '2024-04-11', 'Causeway Group / RTA Form 18a',
  'General tenancy agreement (Form 18a). Lessor: SCION SOUTHPORT PTY LTD. Tenant 1: Cory Shepherd (0422 438 627, coryshepherd1@hotmail.com). Tenant 2: Alexia Negro (alexianegro2@gmail.com). Premises: UNIT 104, 158 SCARBOROUGH STREET, SOUTHPORT 4215. Fixed term: 11/04/24 to 10/04/25. Agent: CAUSEWAY GROUP PTY LTD, 158 SCARBOROUGH STREET, SOUTHPORT.',
  NULL, 'joint_lease_evidence', 'B1_lease_displacement',
  'Foundation evidence: both parties were named co-tenants. Used to anchor B1 strand chronology.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), captured_on=VALUES(captured_on),
  sender=VALUES(sender), verbatim_text=VALUES(verbatim_text), frame_b_tag=VALUES(frame_b_tag),
  strand=VALUES(strand), notes=VALUES(notes);

-- 6. Italian-interface chat with "Manipulator" label and DVO threat
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1Cbg0RD1Y10lby_xiTXDZcuHq-a5hdTTO',
  'b1ce15cf-8152-440d-9909-909806c7930c.jpeg', NULL, 'Alexia Negro (phone, Italian UI)',
  '[Italian UI - "online oggi alle 19:06"] enter again but I will be living in my home. Manipulator. Everything she has is with her in Perth. I''m putting and naming an order on you because I''m scared you will disturb the peace, you are passive aggressive locking me out of my home for home a month it''s disturbing after my generosity.',
  'cory_demanding_entry', 'dvo_threat_during_property_dispute', 'B2_dvo_as_property_tool',
  '"Manipulator" labelling applied by Alexia. Explicit statement of intent to apply for an order, coupled with characterisation of the property contest. Cross-ref Frame B4 verbal labelling.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), sender=VALUES(sender),
  verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 7. 22 Feb — property manager arranging new sole-name lease in Alexia's name
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1svCp5ZNVdwB7yLuBi23UHqhGqg-VvKS7',
  '22 February after end of relationship forms served Alexia attempted to start a new lease after therapy and conciliation failed.png',
  '2025-02-22', 'Naoko / Causeway Group',
  'Hi Alexia, I think the best way is to refund the bond to Corey and you start the new lease in that case, there is no attachment on this unit. I will prepare the lease only your name and you pay for the bond. Is that ok? Naoko. [Attachment: Lease agreement(2)(1) PDF 341 KB]. Earlier in thread: Dec 9, 2024 Causeway to Alexia re: $600 instead of $590.',
  'cory_dispute_over_lease', 'sole_name_lease_arranged', 'B1_lease_displacement',
  'CRITICAL B1 evidence: agent offered to put lease in Alexia''s sole name, refunding bond to Cory. Pre-dates any final order in this set. Anchors B7 too (bond was Cory''s).')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), captured_on=VALUES(captured_on),
  sender=VALUES(sender), verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 8. ZERO BYTES — empty file (Cory claiming still on lease)
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1AwHoButpqvKds1rbpFE3WO1zxOgvwcfJ',
  'Email_from_Cory_claiming_still_on_lease.png', NULL, NULL,
  NULL, 'control_by_cory', 'assertion_of_lease_rights', 'gap',
  'Zero-byte file in Drive. Re-upload required. If readable, this likely supports B1 / B6 strands.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), strand=VALUES(strand), notes=VALUES(notes);

-- 9. Alexia → Cory's mother: characterising abuse + dog allegation
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1ABNff89ufoNapk1_46AKA3MhzjNvoClG',
  'Alexia_message_to_Cory''s_mum.png', NULL, 'Alexia Negro → Cory''s mother',
  '15:34 [Alexia]: This is my final message. I demand no further contact, harassment, or blackmail from Cory. Cory''s belongings were returned to him long ago. Any remaining items are disputed property, which is a civil matter, not a police concern. I will voluntarily given him some items just because I''m nice. I will leave the stuff he asked about in the garage and I will give a time to collect them to Dennis. However, Cory has caused significant damage to the property, including numerous holes in the walls. I need him to leave me and my family alone. His behavior is abusive, and he needs professional help. [Later, Alexia]: He break in to my Apartament and stole my dog.',
  'cory_harassing_via_family', 'third_party_outreach_plus_allegations', 'B3_third_party_recruitment',
  'Direct outreach by Alexia to respondent''s mother. Characterises behaviour as "abusive" and asserts property damage + dog theft. Cross-ref B5 — these allegations need independent corroboration (police report? bond inspection?).')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), sender=VALUES(sender),
  verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 10. Cory SMS 23/2/25 with stat dec page + reference to "tried to steal"
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1FrHnhpJwTBQt_eBWayu1K2rHMKSfziXw',
  'Cory_text_to_Alexia_appearing_to_coerce_her_into_granting_him_access.png',
  '2025-02-23', 'Cory Shepherd',
  '[Stat dec page declared at SOUTHPORT 23/02/2025]. SMS 12:05: Hi Alexia I would like to advise that I have been busy today and organising the place. I have organised a van to come to my home and collect my belongings. I don''t know where you are and my mum and I have been unable to get onto you. Thanks for being respectful and advising your friend. SMS 13:26: I have no hard feelings will leave your things there not taking anything of yours. I don''t think we are for each other. I have spent time and therapy while you have tried to steal so much while making false allegations.',
  'cory_coercing_access', 'cory_advance_notice_of_collection', 'B6_engaging_process',
  'Advance notice of collection visit. Mention of stat dec being filed same day. "Tried to steal so much" is Cory''s contemporaneous characterisation — supports B7 (financial asymmetry) but is his own assertion, not independent evidence.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), captured_on=VALUES(captured_on),
  sender=VALUES(sender), verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 11. ZERO BYTES — Documented Payments — CRITICAL FOR B7
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1JfvQQJd1oMGMib5RpaM3fAOHiQK7EycQ',
  'Documented Payments.png', NULL, NULL,
  NULL, NULL, 'financial_asymmetry_evidence', 'gap',
  'CRITICAL — zero-byte file in Drive. This is the single most important asset for B7. Re-upload immediately. Supplement with bank statements, RTA bond receipt, utility account history regardless.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), frame_b_tag=VALUES(frame_b_tag),
  strand=VALUES(strand), notes=VALUES(notes);

-- 12. Cory FB to Alexia — taking issue with Laura staying, "police know" line
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1QsREyCs1f3_IBTJcVkDv0IN23ZeUXxzW',
  'Cory_FB_message_to_Alexia_trying_to_get_access_to_appt,_and_take_issue_with_laura_staying_at_appt.png',
  NULL, 'Cory Shepherd',
  '14:50 [unread]: I''m not sure if you are getting my messages but I have advised that I was busy today and will be our apartment that''s currently in my name shortly. Could you please inform your friend to avoid any confrontation. I have tried my best for you. I also do not know the strangers name you have allowed to stay or what they look like or how many strangers you let into our place. I''m writing this message so the police know that you have been updated.',
  'cory_taking_issue_with_friend', 'cory_documenting_for_police', 'B6_engaging_process',
  'Documenting communications "so the police know that you have been updated" — pre-emptive procedural posture. Take-issue with strangers in shared residence is normal co-tenant concern.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), sender=VALUES(sender),
  verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 13. Cory's own Form 13 — 7/12/24 without grounds, immediately
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '18abAE5eHIP2exJqDB24Oqn9Hs3jnvpfG',
  'Cory_RTA_Form_13_E-signed_by_Cory.png', '2024-12-07', 'Cory Shepherd (E-signed)',
  'Form 13 Notice of intention to leave. Address: 104 158 Scarborough St Southport. Notice issued by: Cory S. Notice issued: Without grounds (checked). Notice issued on Saturday 7/12/24, method Email. I/We intend to vacate the property by midnight on Immediately.',
  'cory_was_not_on_lease', 'cory_form13_dec_2024', 'B1_lease_displacement',
  'Cory''s own act ending tenancy interest. Context for what came next — cross-ref file 7 (22 Feb sole-name lease) and file 16 (Cory asking to be reinstated). DEFENCE POINT: examine circumstances of signing (duress / understanding / advice received).')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), captured_on=VALUES(captured_on),
  sender=VALUES(sender), verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 14. Alexia → Denis (PM): "he is off the lease" / "He need to organize with the police"
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1FZG1qTQCtbp7RA05bLQdgJ-m0LTYN_aZ',
  'Alexia_SMS_to_Denis_stating_Cory_cannot_enter.png', NULL, 'Alexia Negro → Denis Constable (PM)',
  '07:21 [Alexia]: Hi, he is off the lease. He cannot enter in my home. He need to organize with the police. [Denis]: Understand Alexia, he wont be getting any access. I emailed a reply to you. Cheers Denis. Denis Constable, Property Manager Scion Southport 0412201654.',
  'cory_excluded_for_safety', 'pm_directed_to_exclude', 'B3_third_party_recruitment',
  'Property manager directed by Alexia to refuse access. Cross-ref B2 (DVO invoked as authority) and B1 (lease displacement context).')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), sender=VALUES(sender),
  verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 15. ZERO BYTES — Cory agreeing to leave with Alexia remaining
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1VaWaLCRiH7oomNnl1OWPxjvZ-JmcrSnF',
  'Email_convo_Cory_agreeing_to_leave_appt_with_Alexia_remaining.png', NULL, NULL,
  NULL, 'cory_agreed_to_leave', NULL, 'gap',
  'Zero-byte file in Drive. Re-upload required. If readable, may anchor consent timeline.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), strand=VALUES(strand), notes=VALUES(notes);

-- 16. Alexia to property manager: "I have a DVO against him"
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '17bl1ZcG4dqFWggvLlNvFmoyfzX8OOEcy',
  'Alexia_to_property_manager.png', '2025-02-21', 'Alexia Negro + Cory Shepherd (thread)',
  '14:31 [Alexia → Causeway]: Hi, please ignore Cory email. Cory cannot be on my lease. I have a DVO against him. 14:26 [Cory Shepherd → Naoko]: Yes, that is correct while for two to three weeks Alexia searches for accommodation which I actually paid for in rent and Alexia I believe to have coerced me to do so at the time. I have continued to pay utilities until March 11th, and Alexia has more recently refused to help or pay for utilities stating she won''t help with the costs. My property remains in my home I believe to be 104 158 Scarborough street ... If we are unable to return my name to the lease, I will need to terminate the agreement entirely today, contesting my bond through the RTA. Once this termination is completed, I can then proceed to enter and retain my property within legal agreement tomorrow.',
  'cory_disputing_dvo_compliance', 'dvo_invoked_to_settle_tenancy + cory_paying_utilities',
  'B2_dvo_as_property_tool',
  'KEY EVIDENCE for B2 (DVO used as tenancy tool) and B7 (Cory paying rent + utilities to March 11; Alexia "refused to help or pay"). Get RTA bond receipt + utility statements to corroborate.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), captured_on=VALUES(captured_on),
  sender=VALUES(sender), verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 17. Italian UI chat — "knowing she paid for nothing" + DVO threat
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '19f4AlT7uuc4fHlAJP1mL4rN3araDsCb3',
  '060b6f13-6e18-43ab-8dd7-ea0e4bcf0351.jpeg', NULL, 'Alexia Negro (phone, Italian UI)',
  '[Italian UI "online oggi alle 19:06"] 16:53 [Cory]: That or I will go home today and be living in the apartment knowing she paid for nothing get a court order to enter again but I will be living in my home. [label] Manipulator. 17:13: Everything she has is with her in Perth. 17:13: I''m putting and naming an order on you because I''m scared you will [disturb the peace] ...',
  'cory_threatening_entry', 'cory_stated_financial_asymmetry + dvo_threat', 'B7_financial_asymmetry',
  'Cory''s contemporaneous statement "knowing she paid for nothing" — direct B7 evidence (his own words). Paired with Alexia''s explicit DVO-application threat in same chat. Also tagged B4 (verbal labelling) for "Manipulator".')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), sender=VALUES(sender),
  verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 18. Cory's mum text — mediation offer; police-advised property pickup
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '13FhAaGockDQaPGvr0KlvBuBQ0bHJ_Q8k',
  'Cory_mum_text_to_Cory.png', NULL, 'Cory''s mother → Alexia',
  '[Cory''s mum]: being on the receiving end of any msg that belittles another or any type of name calling is not good. Everyone need to be mindful when sending msgs of how they can be interpreted... I had hoped to catch up with you and your mum and offered to try to mediate between you and Cory if this made it easier in the current situation. Just let me know. Yesterday 20:30: Hi Alexia, I have spoken with Police to get some advice... I have been advised to organise a time with you for Police to attend either with me or Cory to attend and pick up Cory''s property when you return from Perth. I have been advised by Police that if we cannot organise a time and date with you to pick up the property then Cory has the option to report the property as stolen.',
  'cory_mum_pressuring_alexia', 'mum_offering_mediation_and_police_route', 'B6_engaging_process',
  'Cory''s mum offered mediation and pursued police-advised property pickup process. Counter-frames the curator''s "family pressure" tag.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), sender=VALUES(sender),
  verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 19. Cory email to Alexia "Friends staying" with "police attend" reference
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1KLEtPp_1KcQ40f8JPylKRvGg4iv4GX-z',
  'Cory_email_to_Alexia.png', NULL, 'Cory Shepherd',
  'Subject: Friends staying at our residence. Hi Alexia, I am more than willing to just collect my mattress and passport from our apartment and have a peaceful conversation with your friend... I''m more than accommodating if you can show kindness before I have the police attend and tell them you won''t let me enter my home. If you want to dispute my name on the lease you need to go to court. This information was given to me by the police.',
  'cory_threatening_police_if_not_complied', 'cory_citing_legal_avenue', 'B6_engaging_process',
  'Cory cites legal avenue ("go to court") and police advice. Mention of escalation to police is normal lawful entry escalation, not in itself a threat — though curator framed it as one.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), sender=VALUES(sender),
  verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- 20. Duplicate of file 12 (Cory FB Laura) — kept as separate row for completeness
INSERT INTO screenshots (matter_id, file_id, filename, captured_on, sender,
  verbatim_text, frame_a_tag, frame_b_tag, strand, notes)
VALUES (@m, '1I4FLsKQDUSEre5bnOkR8Eby3sNdw2XCK',
  'Cory_FB_message_to_Alexia_trying_to_get_access_to_appt,_and_take_issue_with_laura_staying_at_appt - Copy.png',
  NULL, 'Cory Shepherd',
  '[Same content as file 12]',
  'control_by_cory', 'cory_documenting_for_police', 'B6_engaging_process',
  'EXACT DUPLICATE of file 12 (same byte size 366338). Flag as duplicate in any exhibit list — curator filed the same image twice.')
ON DUPLICATE KEY UPDATE filename=VALUES(filename), sender=VALUES(sender),
  verbatim_text=VALUES(verbatim_text), frame_a_tag=VALUES(frame_a_tag),
  frame_b_tag=VALUES(frame_b_tag), strand=VALUES(strand), notes=VALUES(notes);

-- ============================================================================
-- Quick check: SELECT strand, COUNT(*) FROM screenshots
--              WHERE matter_id = (SELECT id FROM matters WHERE matter_ref='HOWDENS-SIBLEY-001')
--              GROUP BY strand ORDER BY strand;
-- ============================================================================
