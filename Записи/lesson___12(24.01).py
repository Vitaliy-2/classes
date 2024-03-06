import json
from pprint import pprint
some_list = [
    {
        'name': 'Вася',
        'age': 20,
        'skills': ['JS', 'Python', 'C++', 'C#', 'Java'],
        'work': None,
        'is_student': True
    },
    {
        'name': 'Маша',
        'age': 18,
        'skills': ['JS', 'Python', 'C++', 'C#', 'Java']
    },
    {
        'name': 'Петя',
        'age': 25,
        'skills': ['JS', 'Python', 'C++', 'C#', 'Java']
    }
    ]
print(some_list)

json_string = json.dumps(some_list, ensure_ascii=False)
print(f'{json_string=}')

python_object = json.loads(json_string)
print(python_object)

# with open('students.json', 'w', encoding='utf-8') as file:
#     json.dump(some_list, file, ensure_ascii=False, indent=4)

with open('students.json', 'r', encoding='utf-8') as file:
    python_object = json.load(file)
print(python_object)

from data.marvel import full_dict

with open('marvel.json', 'w', encoding='utf-8') as marvel:
    json.dump(full_dict, marvel, ensure_ascii=False, indent=4)

with open('marvel.json', 'r', encoding='utf-8') as marvel:
    marvel_object = json.load(marvel)
pprint(marvel_object)

import datetime

date_ = datetime.date(2024, 1, 24)
date_2 = datetime.date(2024, 2, 24)

today_ = datetime.date.today()

print(date_)
print(date_2)
print(today_)

time_ = datetime.time(12, 30, 59)
time_now = datetime.datetime.now()

print(time_)
print(time_now)

str_time = time_now.strftime('%H:%M:%S')
print(str_time)

time_obj = datetime.datetime.strptime(str_time, '%H:%M:%S')
print(time_obj)
