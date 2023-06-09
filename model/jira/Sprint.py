from peewee import IntegerField, CharField
from model.BaseModel import BaseModel

class Sprint(BaseModel):
    id = CharField(unique=True)
    name = CharField()
    totalIssues = IntegerField()
    completedIssues = IntegerField()
    inCompletedIssues = IntegerField()
    goodTimeMeeting = IntegerField()
    otherTimeMeeting = IntegerField()
    workingTime = IntegerField()