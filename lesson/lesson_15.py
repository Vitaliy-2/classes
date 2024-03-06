"""
Lesson 15
05.02.2024
Аннотации типов
- базовые типы
- пользовательские типы
- установка mypy
"""
import dataclasses
from typing import List, Dict, Union, Any

# Типы данных
# int
# float
# str
# bool
# list
# set
# tuple
# dict
# None

some_int: int = 5  # Тип данных - int
some_float: float = 5.5
some_str: str = 'Hello'
some_bool: bool = True
some_list: list = [1, 2, 3]
# some_list_int = list[int] = [1, 2, 3]
some_set: set = {1, 2, 3}
some_tuple: tuple = (1, 2, 3)
some_dict: dict = {'one': 1, 'two': 2, 'three': 3}
some_none: None = None


class SomeClass:
    pass


some_instance: SomeClass = SomeClass()

"""
Пайчарм отлично понимает базовые типы данных. 
Немного хуже у него с пониманием пользовательских типов данных
Так и с аннотациями типов Typing
"""

# TODO
"""
1. Установить mypy pip install mypy
2. Сделать правильную и неправильную аннотацию типов
3. Запустить mypy на файле
- Вам надо в терминале быть в папке с файлом (или указать путь)
- Ввести команду mypy имя_файла.py
"""

# Typing - библиотека для аннотаций типов (List, Dict, Tuple, Set, Any, Union)
# Аннотации Typing пишут с большой буквы, так же у нас есть возможность указывать
# типы данных для коллекций


"""
Для простых типов данных - базовые аннотации. Их не надо импортировать
- int
- float
- str
- bool
- None

Для коллекций - аннотации Typing. Их надо импортировать
- List
- Dict
- Tuple
- Set
- Any
- Union

"""

some_list_int: List[int] = [1, 2, 3]  # В квадратных скобках указываем тип данных
some_list_str: List[str] = ['1', '2', '3']
# Для словарей указываем тип ключа и тип значения через запятую
some_dict_int_str: Dict[int, str] = {1: 'one', 2: 'two', 3: 'three'}
some_list_dict: List[Dict[str, int]] = [{'one': 1}, {'two': 2}, {'three': 3}]

multi_list: List[Union[int, float, str]] = [1, 2.2, '3']
any_list: List[Any] = [1, 2.2, '3', True, [1, 2, 3], {'one': 1}]
any_list2: List = [1, 2.2, '3', True, [1, 2, 3], {'one': 1}]
any_list3: list = [1, 2.2, '3', True, [1, 2, 3], {'one': 1}]

# TODO Практика
person_dict: Dict[str, Union[str, int, List[str]]] = {
    'name': 'Сергей',
    'age': 35,
    'skills': ['JS', 'Python', 'C++', 'C#', 'Java']
}

person_dict_list: List[Dict[str, Union[str, int, List[str]]]] = [
    {
        'name': 'Сергей',
        'age': 35,
        'skills': ['JS', 'Python', 'C++', 'C#', 'Java']
    }
]


# Напишите аннотацию типов для переменной person_dict
# ключи строки, значениия, строка, число, список строк
# Напишите аннотацию типов для списка словарей person_dict_list
# Проверьте mypy на этом файле

def get_sum(a: int, b: int) -> int:
    return a + b


def get_sum2(*integers: int) -> int:
    """
    Функция которая принимает неопределенное количество целых чисел
    :param integers: Неопределенное количество целых чисел
    :return: Сумма всех чисел
    :exception: TypeError - если хотя бы один аргумент не целое число
    """
    if all(isinstance(i, int) for i in integers):
        return sum(integers)
    else:
        raise TypeError('Все аргументы должны быть целыми числами')


params = [1, 2, 3, 4, 'банан']
# get_sum2(1, 2, 3, 4, 'банан')
get_sum2(*params)


@dataclasses
class City:
    name: str
    population: int
    is_capital: bool


list_cities: List[City] = [
    City('Москва', 12_000_000, True),
    City('Санкт-Петербург', 5_000_000, False),
    City('Новосибирск', 1_500_000, False),
]


