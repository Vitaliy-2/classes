"""
Lesson 38
Pytest
- Фикстуры
- Параметризация фикстур
"""
import json

import pytest
import time


def is_palindrome(word) -> bool:
    return word.lower().replace(' ', '') == word[::-1].lower().replace(' ', '')


@pytest.fixture
def json_data(request):
    json_str = """[
    ["дуд", true],
    ["дудка", false],
    ["банан", false],
    ["bob", true],
    ["bobik", false],
    ["бобер", false]
    ]"""
    data = json.loads(json_str)
    word, result = data[request.param]
    return word, result


@pytest.mark.parametrize('json_data', range(6), indirect=True)
def test_is_palindrome_param(json_data):
    word, result = json_data
    assert is_palindrome(word) == result, f'Слово "{word}" не является палиндромом'


"""
Подробное объяснение:

@pytest.fixture: Эта декорация определяет фикстуру. Фикстура — это функция, которая запускается перед каждым тестом, 
в котором она используется. 

Фикстура json_data загружает данные из строки JSON и возвращает пару значений (слово и ожидаемый результат) 
на основе request.param.

request.param: Это специальный параметр, который предоставляется pytest для доступа к параметрам теста в фикстуре. 
Он используется для того, чтобы выбрать нужный элемент из списка данных. Каждый раз при выполнении теста, pytest 
изменяет значение request.param в соответствии с заданным в parametrize.

@pytest.mark.parametrize: 'json_data': имя параметра теста.

range(6): создает последовательность индексов от 0 до 5, что соответствует числу элементов в данных JSON.

indirect=True: указывает pytest, что значения в range(6) должны быть переданы не напрямую в тест, а через фикстуру 
json_data, которая использует эти значения для выбора нужных данных.

Тестовая функция test_is_palindrome_param: принимает результаты из фикстуры json_data (слово и результат) и проверяет, 
является ли слово палиндромом. Сообщение об ошибке указывает, что слово должно быть палиндромом, если тест не проходит.
"""


"""
Практика!
Создайте функцию сложения двух чисел
Создайте тест для этой функции с параметризацией
"""

sum_data_set = [
    (2, 2, 4),
    (3, 3, 6),
    (4, 4, 8),
    (5, 5, 10),
    (6, 6, 12),
    (100, 100, 200),
    (0, 0, 0),
    (-1, 1, 0),
    (-1, -1, -2),
    (1, -1, 0),
    (4, -3, 1),
    (-20, 20, 0)
]


def get_sum(a, b):
    return a + b


@pytest.mark.sumt  # Дали придуманный маркер
@pytest.mark.parametrize('one, two, free', sum_data_set)
def test_sum(one, two, free):
    assert get_sum(one, two) == free, f'Сумма чисел {one} и {two} не равняется {free}'


# Фикстура которая вернет функцию сложения
@pytest.fixture(scope='module')
def sum_fixture():
    return get_sum


# Параметризация и фикстура
@pytest.mark.sumty
@pytest.mark.parametrize('one, two, free', sum_data_set)
def test_sum_fixture(sum_fixture, one, two, free):
    assert sum_fixture(one, two) == free, f'Сумма чисел {one} и {two} не равна {free}'
