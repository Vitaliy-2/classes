from pprint import pprint
from data.marvel import full_dict, simple_set
names = 'Ваня', 'Даня', 'Саша', 'Катя', 'Маша', 'Алена'
one, two, free, *_ = names
print(names)
print(free)
print(_)
print(*_)

list_items2 = [
    ('first_name', 'Захар'),
    ('middle_name', 'Илларионович'),
    ('last_name', 'Прутков'),
    ('age', 85)
]

for zzz, xxx in list_items2:
    print(f'{zzz=}, {xxx=}')

avto = {
    'Авто': 'BMW',
    'Страна': 'Германия',
    'Год': '2018',
    'Л/С': '480',
}
for key in avto.keys():
    print(key)
for value in avto.values():
    print(value)
for key, value in avto.items():
    print(f'{key}: {value}')

# name = {
#     'Имя': 'Дмитрий',
#     'Фамилия': 'Сафонов',
#     'Отчество': 'Юрьевич',
# }
# for key in name.keys():
#     print(key)
# for value in name.values():
#     print(value)
# for key, value in name.items():
#     print(f'{key=}', f'{value=}')
#
# pprint(name)
# print(name)


pprint(full_dict)
print(simple_set)
print(len(full_dict)-1)
print(len(simple_set))
