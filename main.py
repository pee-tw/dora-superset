from pipeline.ETLJira import JiraPipeline
from pipeline.ETLCalendar import CalendarPipeline
from model.jira.Sprint import Sprint

jira_pipeline = JiraPipeline()
calendar_pipeline = CalendarPipeline()

jira_data = jira_pipeline.start()
calendar_pipeline.start(jira_data)
