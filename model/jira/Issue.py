from peewee import IntegerField, CharField, FloatField
from model.BaseModel import BaseModel

class Issue(BaseModel):
    id = CharField()
    title = CharField()
    sprintId = CharField()
    leadTime = FloatField()
    statusInSprint = CharField()
    status = CharField()
    type = CharField()
    class Meta:
        primary_key = False