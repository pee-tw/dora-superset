import os
import re

from dotenv import load_dotenv
from github import Github

from model.jira.Issue import Issue
from model.jira.Sprint import Sprint
from pipeline.lib.LeadTime import calculate_lead_time

from .lib.JiraSprintReport import SprintReport

load_dotenv()

PAT = os.getenv("JIRA_PAT")
AUTH_USER = os.getenv("AUTH_USER")
SERVER = os.getenv("SERVER")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
BOARD_ID = 1 # GP team
PROJECT_PREFIX = "GP-" # GP team prefix
# BOARD_ID = 2
# PROJECT_PREFIX = "BE-"


class JiraPipeline:
    def start(self):
        print('start Jira Pipeline')
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
            print(f'Run Sprint {sprints[sprint].name}')
            reports = sprint_report.get_complete_noncomplete_issues(
                BOARD_ID, sprints[sprint].id
            )
            cards = [
                *reports["completedIssues"]["data"],
                *reports["issuesNotCompletedInCurrentSprint"]["data"],
            ]

            flattern = {}
            for card in cards:
                flattern[card["key"]] = card
                
            response.append(
                {
                    "name": sprints[sprint].name,
                    "id": sprints[sprint].id,
                    "cards": list(flattern),
                }
            )
            issues = sprint_report.get_issues_by_sprint_name(sprints[sprint].name)
            
            print(" ==> Save Issues <== ")
            for issue in issues:
                lead_time = calculate_lead_time(issue)
                Issue.create(
                    id=issue.key,
                    title=issue.fields.summary,
                    sprintId=sprints[sprint].name,
                    leadTime=lead_time,
                    statusInSprint=flattern[issue.key]['statusName'],
                    status=issue.fields.status.name,
                    type=issue.fields.issuetype.name,
                )

            print(" ==> Save Sprint <== ")
            Sprint.create(
                id=sprints[sprint].name, 
                name=sprints[sprint].name, 
                totalIssues=(len(reports["completedIssues"]["data"]) + len(reports["issuesNotCompletedInCurrentSprint"]["data"])),
                completedIssues=len(reports["completedIssues"]["data"]),
                inCompletedIssues=len(reports["issuesNotCompletedInCurrentSprint"]["data"]),
            )

        return response
