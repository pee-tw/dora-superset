from pipeline.ETLJira import JiraPipeline
from pipeline.ETLCalendar import CalendarPipeline

jira_pipeline = JiraPipeline()
calendar_pipeline = CalendarPipeline()

jira_data = jira_pipeline.start()
calendar_pipeline.start(jira_data)