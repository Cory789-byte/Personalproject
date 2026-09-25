"""The 303 facts as served on 28 August 2026 and answered on 8 September 2026.

Single source of truth for anything that cites a paragraph number of the notice.
Parsed from the Respondent's completed response and stored at
documents/regulator-response-2026-09-08/SERVED_303_facts_and_verdicts.json.

⛔ Do NOT read fact text from build_form24_second.py for this purpose. That file is the
working draft of a further notice and has moved on from what was served: it now holds 308
paragraphs, five of which were added after 8 September 2026, so its numbering diverges from
the served notice after paragraph 298.
"""
import json, os

_P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'documents',
                  'regulator-response-2026-09-08', 'SERVED_303_facts_and_verdicts.json')
_D = json.load(open(_P, encoding='utf-8'))

FACT = {int(k): v for k, v in _D['facts'].items()}
VERDICT = {int(k): v for k, v in _D['verdict'].items()}
TOTAL = _D['total']
NOT_ADMITTED = set(_D['not_admitted_paragraphs'])

assert TOTAL == 303 and len(FACT) == 303, (TOTAL, len(FACT))
assert sum(v == 'Admitted' for v in VERDICT.values()) == 298
assert sum(v == 'Not admitted' for v in VERDICT.values()) == 5
assert not any(v == 'Denied' for v in VERDICT.values())
assert NOT_ADMITTED == {154, 228, 229, 230, 231}
