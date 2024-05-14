"""
Lesson 37
Pytest

Установка pytest - pip install pytest
assert - проверка условия
assert exception - проверка исключения
главная проблема assert - остановка выполнения теста
тестовые функции должны начинаться с test_
файлы с тестами должны начинаться с test_ или заканчиваться _test
где и как должны лежать тесты?
@pytest.mark.slow - маркировка тестов slow - придуманный маркер
Запуск тестов с маркером pytest -m "slow"
Запуск тестов без маркера pytest -m "not slow" (подробнее в конспекте)
@pytest.mark.parametrize - параметризация тестов
xfail - тест который ожидает провал
xfail в параметризации обычного текста
@pytest.fixture - фикстуры, это заготовки для тестов
scope - как часто будет пересоздаваться фикстура
test_class - тестовый класс для группировки тестов
"""


def is_palindrome(word):
    return word == word[::-1]


def test_is_palindrome_registr():
    assert is_palindrome('Дед') == True, 'Ваша функция не обрабатывает регистр'
    # ТАК НЕ НАДО. Потому что, если тест упадет, то дальше не пойдет
#     assert is_palindrome('а роза упала на лапу азора') == True, 'Ваша функция не обрабатывает многословные палиндромы'


def test_is_palindrome_multiple_words():
    assert is_palindrome('а роза упала на лапу азора') == True, 'Ваша функция не обрабатывает многословные палиндромы'

