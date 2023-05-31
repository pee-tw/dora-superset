# Introduction
This is a PoC project that demonstrate how might we keep track of lead time on across JIRA and GitHub releases. We leverage Python to connect various sources of data (Google Calendar, JIRA, GitHub Release) to get relevent data on how a team is performing.

## Tech stack
- Python
- Python Poetry (Dependency Management)
- GCSA (Google Calendar Python wrapper)
- JIRA (JIRA Python wrapper)
- pygithub (GitHub Python wrapper)
- peewee (Python MySQL ORM)

## Pre-requisites
- To authenticate with Google Calendar, you'll need to create an OAuth credentials on GCP. Run `make auth-calendar` to save token as a file. To setup OAuth authentication screen please follow the instructions [here](https://google-calendar-simple-api.readthedocs.io/en/latest/getting_started.html#getting-started)
- Have a Personal Access Token for GitHub
- Have a Personal Access Token for Jira

## How to run the script
- Install Poetry if you don't have it installed already. More info [here](https://python-poetry.org/docs/#installation).
- Run `make install` to install all the packages
- Rename `.env.example` to `.env` and populate it with relevant configs. 
- Run `make create-table` to generate relevant MySQL tables. 
- Finally, run `python main.py`

## Caveats
We intended to leverage GitHub action's cron as a scheduler to update the database, but ran out of time and left only a template on how to call the script.

Additionally, we should make this script idempotent. Feel free to fork and improve the script to your preferences.

# Start Superset with Docker
Run `docker-compose up -d` to customize details, check `docker/.env-non-dev`

To learn more about Apache Superset please [visit](https://superset.apache.org/)