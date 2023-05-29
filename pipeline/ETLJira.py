import os
from dotenv import load_dotenv
from .lib.JiraSprintReport import SprintReport


load_dotenv()

PAT = os.getenv('JIRA_PAT')
AUTH_USER = os.getenv('AUTH_USER')
SERVER = os.getenv('SERVER')
BOARD_ID = 1

class JiraPipeline:
    def start(self):
        sprint_report = SprintReport(SERVER, AUTH_USER, PAT)
        sprints = sprint_report.get_sprints(BOARD_ID)
        response = []
        for sprint in range(len(sprints)):
            reports = sprint_report.get_complete_noncomplete_issues(BOARD_ID, sprints[sprint].id)
            cards = [*reports['completedIssues']['data'], *reports['issuesNotCompletedInCurrentSprint']['data']]
            flattern = map(lambda card: card['key'], cards)
            response.append({
                'name': sprints[sprint].name,
                'id': sprints[sprint].id,
                'cards': list(flattern),
            })
        return response
            
pipeline = JiraPipeline()
pipeline.start()