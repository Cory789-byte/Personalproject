.PHONY: all db validate site json clean

all:
	python3 -m legal_system.build.run_all

db:
	python3 -m legal_system.build.build_database

validate:
	python3 -m legal_system.build.validate

site:
	python3 -m legal_system.build.build_html

json:
	python3 -m legal_system.build.export_json

clean:
	rm -rf legal_system/db/case.db legal_system/output

# Quick searches
events-lockout:
	python3 -m legal_system.build.search events --on 2025-02-24

events-romeo:
	python3 -m legal_system.build.search events --grep romeo

ware-outstanding:
	python3 -m legal_system.build.search ware --outstanding

paragraphs-dispositive:
	python3 -m legal_system.build.search paragraphs --status dispositive
