import os
from dotenv import load_dotenv
from lib.JiraSprintReport import SprintReport

load_dotenv()

PAT = os.getenv('JIRA_PAT')
AUTH_USER = os.getenv('AUTH_USER')
SERVER = os.getenv('SERVER')

sprint_report = SprintReport(SERVER, AUTH_USER, PAT)

report = sprint_report.get_complete_noncomplete_issues(1, 1)

print(report)