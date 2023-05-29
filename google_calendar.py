from dateutil.parser import isoparse
from gcsa.google_calendar import GoogleCalendar

# TODO: Replace in pipeline
calendar = GoogleCalendar(credentials_path='credentials.json', token_path='token.pickle')
for event in calendar:
    print(event)


start_date = isoparse("2023-01-01")
end_date = isoparse("2023-12-31")

bad_calendar_id = '0cd3dcef458e6fbf53d7120e2867e034dfcb49d0c3ae55262996486d77ec9da0@group.calendar.google.com'
calendar = GoogleCalendar(bad_calendar_id).get_events(start_date, end_date)
for event in calendar:
    print(event)
    print(event.description)
    print(event.attendees)
    print(event.creator)
    
good_calendar_id = 'efb383684ee7890d5c9fccad76fc526bbe8346c66fd5cd8e8897e65c7da151e5@group.calendar.google.com'
calendar = GoogleCalendar(good_calendar_id).get_events(start_date, end_date)
for event in calendar:
    print(event)
    print(event.description)
    print(event.attendees)
    print(event.creator)