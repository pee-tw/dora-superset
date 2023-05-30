from peewee import IntegerField, CharField, ForeignKeyField
from model.BaseModel import BaseModel
from model.jira.Sprint import Sprint

class Meeting(BaseModel):
    id = IntegerField(unique=True)
    sprintId = IntegerField()
    title = CharField()
    time = IntegerField()
    issue = CharField()