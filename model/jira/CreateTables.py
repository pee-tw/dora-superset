
from model.jira.Sprint import Sprint
from model.jira.BaseModel import db

def create_tables():
    with db:
        db.create_tables([Sprint])
        
create_tables()