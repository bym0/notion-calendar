from helpers.add_calendar_entry import add_calendar_entry
from helpers.get_calendar_events import get_calendar_events

def main():
    # title = "Test"
    # date = "2023-08-10"

    # add_calendar_entry(title, date)

    for event in get_calendar_events():
        add_calendar_entry(event['title'], event['date'])



if __name__ == "__main__":
    main()
