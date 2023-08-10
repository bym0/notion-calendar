import os
import re

from datetime import datetime
from O365 import Account, FileSystemTokenBackend
from dotenv import load_dotenv

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.env'))
load_dotenv(dotenv_path=dotenv_path)
token_backend = FileSystemTokenBackend(token_path=os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')), token_filename='o365_token.txt')

scopes = ['Calendars.Read']
credentials = (os.getenv('CLIENT_ID'), os.getenv('SECRET_ID'))

pattern = re.compile(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})')

class Event:
    def __init__(self, subject, start, end):
        self.subject = subject
        self.start = start
        self.end = end

def get_calendar_events():
    event_data_list = []

    account = Account(credentials, tenant_id=os.getenv('TENANT_ID'), token_backend=token_backend)
    if account.authenticate(scopes=scopes):
        print('Authenticated!')
        
    schedule = account.schedule()
    calendar = schedule.get_default_calendar()
    events = calendar.get_events(include_recurring=False) 
    #events = calendar.get_events(query=q, include_recurring=True) 

    for event in events:
        start_str = event.start.strftime('%Y-%m-%d %H:%M:%S')
        end_str = event.end.strftime('%Y-%m-%d %H:%M:%S')

        match = pattern.findall(start_str)
        if match:
            date, start_time = match[0]
            end_date, end_time = pattern.findall(end_str)[0]
            title = event.subject
            event_data = {
                'title': title,
                'date': date,
                'time_range': f'{start_time} to {end_time}'
            }
            event_data_list.append(event_data)
            
    return event_data_list
