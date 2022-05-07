from json import load, dump
from datetime import datetime
from meetings.Meeting import Meeting
from meetings.Calendar import Calendar

calendar = Calendar()

# TODO: add exceptions when opening the main file - when there is no json file


with open('meetings.json') as file:
    data = load(file)
    for item in data:
        meeting = Meeting(
            datetime.strptime(item['date'], '%d.%m.%Y %H:%M'),
            item['title'])
        calendar.add_meeting(meeting)

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

            with open('meetings.json', 'w') as file:
                data = []
                for meeting in calendar.meetings.values():
                    data.append({
                        'title': meeting.title,
                        'date': meeting.date.strftime( '%d.%m.%Y %H:%M')
                    })
                dump(data, file)

        elif option == 'q':
            break

        else:
            print('Use [l] - list, [a] - add [q] - quit ')



