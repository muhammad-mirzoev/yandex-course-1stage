from datetime import datetime, time, timedelta
import sys

list_of_meetings = []


class Report:
    def __init__(self, theme, time, duration):
        self.theme, self.time, self.duration = theme, time, duration
        self.time = timedelta(hours=int(self.time.split('.')[0]), minutes=int(self.time.split('.')[1]))
        self.duration = timedelta(hours=int(self.duration.split('.')[0]),
                                  minutes=int(self.duration.split('.')[1]))
        self.end_time = self.time + self.duration


class Conference:
    def __init__(self, theme, time, duration):
        self.theme, self.time, self.duration = theme, time, duration
        self.time = timedelta(hours=int(self.time.split('.')[0]), minutes=int(self.time.split('.')[1]))
        self.duration = timedelta(hours=int(self.duration.split('.')[0]),
                                  minutes=int(self.duration.split('.')[1]))
        self.end_time = self.time + self.duration


def create_meeting(properties):
    global list_of_meetings
    if not properties:
        return 'Некорректно введены данные'
    else:
        theme_res, time_res, dur_res = map(str, properties)
        if theme_res.lower() == 'доклад' or theme_res.lower() == 'конференция':
            meeting = Report(theme_res, time_res, dur_res)
            if len(list_of_meetings) == 0:
                list_of_meetings.append(meeting)
                return f'{theme_res} добавлен(a) в расписание'
            else:
                for i in list_of_meetings:
                    if i.end_time <= meeting.time:
                        list_of_meetings.append(meeting)
                        return f'{theme_res} добавлен(a) в расписание'
                return 'Данное время недоступно'
        else:
            return 'Введен неверный тип встречи'


def easier_exit(text):
    answer = input(f'{text} (да / нет)? ')
    sys.exit() if answer.lower() == 'нет' else main()


def main():
    input_data = input('Введите данные встречи через запятую (тип, время начала, длительность): ').split(',')
    input_data_copy = []
    for i in input_data:
        j = i.rstrip()
        input_data_copy.append(j.strip())
    result = create_meeting(input_data_copy)
    print(result)
    if (result == 'Некорректно введены данные' or result == 'Введен неверный тип встречи'
            or result == 'Данное время недоступно'):
        easier_exit('Попробовать еще раз')
    elif (result.lower() == 'доклад добавлен(a) в расписание'
          or result.lower() == 'конференция добавлен(a) в расписание'):
        easier_exit('Добавить еще встречу')
    else:
        print()


main()