import os
import re

from dotenv import load_dotenv
from github import Github

from model.jira.Issue import Issue
from model.jira.Sprint import Sprint

from .lib.JiraSprintReport import SprintReport

load_dotenv()

PAT = os.getenv("JIRA_PAT")
AUTH_USER = os.getenv("AUTH_USER")
SERVER = os.getenv("SERVER")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
BOARD_ID = 1
PROJECT_PREFIX = "GP-"


class JiraPipeline:
    def start(self):
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo("pee-tw/dora-superset")
        releases = repo.get_releases()
        
        release_with_issues = []
        for release in releases:
            issues = re.findall(f"{PROJECT_PREFIX}(\d+)", release.body)
            issues_with_prefix = []
            for issue in issues:
                issues_with_prefix.append(f"{PROJECT_PREFIX}{issue}")
            release_with_issues.append(
                {"issues": issues_with_prefix, "date": release.created_at}
            )

        sprint_report = SprintReport(SERVER, AUTH_USER, PAT)
        sprints = sprint_report.get_sprints(BOARD_ID)
        response = []
        for sprint in range(len(sprints)):
            reports = sprint_report.get_complete_noncomplete_issues(
                BOARD_ID, sprints[sprint].id
            )
            cards = [
                *reports["completedIssues"]["data"],
                *reports["issuesNotCompletedInCurrentSprint"]["data"],
            ]
            flattern = map(lambda card: card["key"], cards)
            response.append(
                {
                    "name": sprints[sprint].name,
                    "id": sprints[sprint].id,
                    "cards": list(flattern),
                }
            )

            issues = sprint_report.get_issues_by_sprint_id(sprints[sprint].id)
            for issue in issues:
                released_on = None
                # TODO: Calculate lead time
                # first_appeared = datetime().now()
                for release in release_with_issues:
                    if issue.key in release["issues"]:
                        released_on = release['date']
                lead_time = 0
                Issue.create(
                    id=issue.id,
                    title=issue.fields.summary,
                    sprintId=sprints[sprint].id,
                    leadTime=lead_time,
                    statusInSprint=issue.fields.status.name,
                    type=issue.fields.issuetype.name,
                )

            Sprint.create(
                id=sprints[sprint].id, name=sprints[sprint].name, totalIssue=len(issues)
            )
        return response


pipeline = JiraPipeline()
pipeline.start()
