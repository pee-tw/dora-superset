import requests
from requests.auth import HTTPBasicAuth
from jira import JIRA

class SprintReport:
    def __init__(self, server, username, password) -> None:
        self.SERVER = server
        self.USERNAME = username
        self.PASSWORD = password
        options = { 'server': self.SERVER }
        self.JIRA = JIRA(options, basic_auth=(self.USERNAME, self.PASSWORD))
    
    def get_report(self, board_id, sprint_id):
        response = requests.get(f"{self.SERVER}//rest/greenhopper/latest/rapid/charts/sprintreport?rapidViewId={board_id}&sprintId={sprint_id}", auth=HTTPBasicAuth(self.USERNAME, self.PASSWORD))
        return response

    def get_complete_noncomplete_issues(self, board_id, sprint_id):
        keys = ['completedIssues', 'issuesNotCompletedInCurrentSprint']
        requre_data_key = ['id', 'key', 'statusName', 'typeName']
        response = requests.get(f"{self.SERVER}//rest/greenhopper/latest/rapid/charts/sprintreport?rapidViewId={board_id}&sprintId={sprint_id}", auth=HTTPBasicAuth(self.USERNAME, self.PASSWORD))
        contents = response.json()['contents']
        return_object = {}
        for key in keys:
            data = []
            for item in contents[key]:
                sub_data = {}
                for data_key in requre_data_key:
                    sub_data[data_key] = item[data_key]
                data.append(sub_data)
            return_object[key] = {
                "length": len(contents[key]),
                "data": data
            }
        
        return return_object

    def get_sprints(self, board_id):
        return self.JIRA.sprints(board_id)