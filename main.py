from datetime import datetime, timedelta
from meetings.Meeting import Meeting
from meetings.Calendar import Calendar

calendar = Calendar()

if __name__ == '__main__':
    while True:
        option = input('What you want to do? [l] - list, [a] - add [q] - quit: ')
        if option == 'l':
            for _, meeting in calendar.meetings.items():
                print(f'{meeting.date}: {meeting.title}')

        elif option == 'a':
            title = input('The title of the meeting: ')
            date = input('Date of meeting dd.mm.rrrr h:m: ')
            meeting_date = datetime.strptime(date, '%d.%m.%Y %H:%M')

            calendar.add_meeting(Meeting(meeting_date, title))

        elif option == 'q':
            break

        else:
            print('Use [l] - list, [a] - add [q] - quit ')



