from peewee import IntegerField, CharField, ForeignKeyField
from model.BaseModel import BaseModel

class Issue(BaseModel):
    id = IntegerField(unique=True)
    title = CharField()
    sprintId = IntegerField()
    leadTime = IntegerField()
    statusInSprint = CharField()
    status = CharField()
    type = CharField()