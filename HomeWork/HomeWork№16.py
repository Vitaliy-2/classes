# HomeWork № 16
from pprint import pprint
from typing import Dict, Union, Any

# 1 Импорт
from data.marvel import full_dict

# 2 Пользовательский ввод
user_data = input('Введите числа через пробел: ').split(' ')
user_input: list = list(map(lambda x: int(x) if x.isdigit() else None, user_data))
print(user_input)

# 3 Получение словарей, id которых совпадает с пользовательским вводом
ids = [id for id in user_input if id]

filter_dict: Dict[int, Dict[str, Any]] = dict(filter(lambda x: x[0] in ids, full_dict.items()))
print('Получений словарей, id которых совпадают с вводом:\n')
pprint(filter_dict)

# 4 Получение сета значений director
directors: set[str] = {film['director'] for film in full_dict.values() if film['director'] != 'TBA'}
print('\nПолучение сета из director:\n')
print(directors)

# 5 Заменяем тип данных у 'year' с числа, на строку
full_dict_copy: Dict[int, Dict[str, Any]] = {id: {key: value if key != 'year' else str(value) for key, value in
                                                  film.items()} for id, film in full_dict.items()}
print('\nМеняем тип данных у значения year на строку:\n')
pprint(full_dict_copy, sort_dicts=False)

# 6 Выводим только те словари, фильмы которых начинаются на "Ч"
films_ch: Dict[int, Dict[str, Any]] = {id: film for id, film in full_dict.items() if isinstance(film['title'], str)
                                       and film['title'].startswith('Ч')}
print('\nСловари, фильмы которых начинаются на "Ч":\n')
pprint(films_ch, sort_dicts=False)

# 7 Сортировка словаря full_dict по названию фильма
sorted_dict: Dict[int, Dict[str, Any]] = (
    dict(sorted(full_dict.items(), key=lambda x: x[1]['title'] if isinstance(x[1]['title'], str) else 'я')))
print('\nСортируем словари по алфавиту по названиям фильма:\n')
pprint(sorted_dict, sort_dicts=False)

# 8 Сортировка словаря full_dict по году выпуска и названию фильма.
# Пересоберем словарь, чтобы взять только те фильмы, у которых год выпуска число и название фильма строка
full_dict_final: Dict[int, Dict[str, Union[str, int]]] = \
    {id: film for id, film in full_dict.items() if isinstance(film['year'], int) and isinstance(film['title'], str)}

# Сортировка
sorted_dict_new: Dict[int, Dict[str, Union[str, int]]] = dict(
    sorted(full_dict_final.items(), key=lambda x: (x[1]['year'], x[1]['title'])))
print('\nСортировка словарей по году  выпуска и названию фильма:\n')
pprint(sorted_dict, sort_dicts=False)

# 9 используем очищенную коллекцию full_dict и фильтруем фильмы Первой фазы и сортируем по алфавиту
sorted_dict_final: Dict[int, Dict[str, Union[str, int]]] = dict(sorted(filter(lambda x: x[1]['stage'] == 'Вторая фаза',
                                                                              full_dict_final.items()),
                                                                       key=lambda x: x[1]['title']))
print('\nФильтруем словари по фазам фильмов и алфавиту:\n')
pprint(sorted_dict, sort_dicts=False)


# Проверка mypy прошла успешно. Success: no issues found in 1 source file.
