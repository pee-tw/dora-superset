from dateutil.parser import isoparse, parser
from gcsa.google_calendar import GoogleCalendar
from dotenv import load_dotenv
import os
import re

load_dotenv()

BAD_CALENDAR_ID = os.getenv('BAD_CALENDAR_ID')
GOOD_CALENDAR_ID = os.getenv('GOOD_CALENDAR_ID')

# TODO: Replace in pipeline
# calendar = GoogleCalendar(credentials_path='credentials.json', token_path='token.pickle')
# for event in calendar:
#     print(event)
class Calendar:
    def __init__(self, auth_key) -> None:
        self.auth_key = auth_key
        self.calendar = GoogleCalendar(self.auth_key)
    
    def get_event(self, start, end):
        return self.calendar.get_events(start, end)



sprints = [
    {
        "id": 1,
        "name": 'GP Sprint 1',
        "start": isoparse("2023-05-22"),
        "end": isoparse("2023-06-03")
    },
    {
        "id": 3,
        "name": 'GP Sprint 2',
        "start": isoparse("2023-06-05"),
        "end": isoparse("2023-06-17")
    },
    {
        "id": 4,
        "name": 'GP Sprint 3',
        "start": isoparse("2023-06-19"),
        "end": isoparse("2023-07-01")
    }
]

# bad_calendar = Calendar(BAD_CALENDAR_ID)
# for event in bad_calendar.get_event(start_date, end_date):
#     print(event)
#     print(event.description)
#     print(event.attendees)
#     print(event.creator)

def create_dict(array):
    dictionary = {}
    for item in array:
        dictionary[item] = {}
    
    return dictionary

def check_reserve_meeting(string):
    reserve_meeting = ['Standup', 'Retrospective', 'Sprint Planning']
    for reserve in reserve_meeting:
        if(reserve in string):
            return True, reserve
    
    return False, ""

class CalendarPipeline:       
    def start(self, jira_data):
        cards = {}
        for jira_sprint in jira_data:
            cards[jira_sprint['name']] = create_dict(jira_sprint['cards'])
        good_calendar = Calendar(GOOD_CALENDAR_ID)

        sprints_timer = []
        for sprint in sprints:
            timer = {
                "good_meeting_time": 0, # unit: minute
                "other_meeting_time": 0, # unit: minute
                "working_time": 2400 # unit: minute
            }
            print(f"====> {sprint['name']} <=====")
            print(f"{sprint['start']} - {sprint['end']}")
            for event in good_calendar.get_event(sprint['start'], sprint['end']):
                total_minute = 0
                print(event.summary, event.recurrence)
                name = re.findall("GP-(?:^|\d)+", event.summary)
                is_reserve, reserve = check_reserve_meeting(event.summary)
                if((len(name) > 0 and name[0] in cards[sprint['name']]) or is_reserve):
                    if(is_reserve and reserve == "Standup"):
                        total_minute = ((event.end - event.start).total_seconds() / 60) * 10
                    else:
                        total_minute = (event.end - event.start).total_seconds() / 60
                    timer['good_meeting_time'] = timer['good_meeting_time'] + total_minute
                else:
                    total_minute = (event.end - event.start).total_seconds() / 60
                    timer['other_meeting_time'] = timer['other_meeting_time'] + total_minute
            sprints_timer.append({
                "name": sprint['name'],
                "time_overall": timer
            })
        
        print(sprints_timer)