MYPY_OPTIONS = --ignore-missing-imports --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs

.PHONY: install
install:
	poetry install

.PHONY: auth-calendar
auth-calendar:
	poetry run python authen_calendar.py

.PHONY: create-table
create-table:
	poetry run python -m model.CreateTables

.PHONY: etl-jira
etl-jira:
	poetry run python -m pipeline.ETLJira

.PHONY: etl-calendar
etl-calendar:
	poetry run python -m pipeline.ETLCalendar

.PHONY: run
run:
	poetry run python main.py