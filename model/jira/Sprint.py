from peewee import IntegerField, CharField
from model.jira.BaseModel import BaseModel

class Sprint(BaseModel):
    id = IntegerField(unique=True)
    sprint_name = CharField()
    
    # def __init__(self, id, sprint_name, completedIssues, issuesNotCompletedInCurrentSprint):
    #     self.id = id
    #     self.sprint_name = sprint_name
    #     self.completedIssues = completedIssues
    #     self.issuesNotCompletedInCurrentSprint = issuesNotCompletedInCurrentSprint