
from model.calendar.Meeting import Meeting
from model.jira.Issue import Issue
from model.jira.Sprint import Sprint
from model.BaseModel import db

def create_tables():
    with db:
        db.create_tables([Sprint, Issue, Meeting])
        
create_tables()