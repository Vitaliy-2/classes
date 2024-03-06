"""Lesson 18
14.02.2024
- Повторение областей видимости
- Замыкания
- Декораторы
- Декораторы с параметрами
- Пример декоратра замеряющего время выполнения функции
"""
import time
from typing import Callable

#
# def say_name(name: str) -> None:
#     def say_goodbye() -> None:
#         print(f"Пока, {name}!")
#
#     say_goodbye()
#
#
# say_name('Валера')
#

# Callable [[], None] - [аргументы], возвращаемое значение
# def say_name2(name: str) -> Callable[[], None]:
#     def say_goodbye() -> None:
#         print(f"Привет, {name}!")
#
#     return say_goodbye


# ppp = print
# ppp('Hello')

# sn: Callable[[], None] = say_name2('Валера')
# sn()
"""
Пока sn ссылается на функцию say_name2, то она не будет удалена из памяти.
Соответственно и Валера останется в переменной name.

Почему замыкание?

Мы держим внутренние окружения и "замыкаем" их по цепочке
Обратившись к sn

sn -> say_name2 -> say_goodbye -> name = "Валера" 
и мы получаем на принте "Привет, Валера!"
"""


def counter(start: int) -> Callable[[], int]:
    count = start

    def inner() -> int:
        nonlocal count
        count = count + 1
        return count

    return inner


c: Callable[[], int] = counter(0)
print(c())
print(c())
print(c())

# Функция с кешем
# fruit_lst: list[str] = ['apple', 'banana', 'orange', 'pineapple', 'pear']


# def sort_fruits(fruits: list[str]) -> Callable[[], list[str]]:
# Тут болтается fruit_lst
#     cache: list[str] = []
#
#     def sort() -> list[str]:
#         nonlocal cache
#         if not cache or len(fruits) != len(cache):
#             cache = sorted(fruits)
#         return cache
#
#     return sort
#

# sorter: Callable[[], list[str]] = sort_fruits(fruit_lst)
# print(sorter())
# Вызываем сортировку повторно - будет взято из кеша
# print(sorter())

# fruit_lst.append('mango')
# Вызываем сортировку повторно - будет пересортировка
# print(sorter())


# def print_decorator(func: Callable[[], None]) -> Callable[[], None]:
#     def wrapper() -> None:
#         print('Декоратор начал работу')
#         # В полноценном декораторе было бы return func()
#         func()
#         print('Декоратор закончил работу')
#
#     return wrapper
#
#
# def some_function() -> None:
#     print('Работает функция')


# Уже тут можно использовать СОБАКУ!!!
# f: Callable = print_decorator(some_function)
# f()


# def print_decorator_2(func: Callable[[], str]) -> Callable[[], str]:
#     def wrapper() -> str:
#         print('Декоратор начал работу')
#         result = func() + '!'
#         print('Декоратор закончил работу')
#         return result
#
#     return wrapper


# def some_func_2() -> str:
#     return 'Работает функция 2'
#
#
# some_func_2_mod = print_decorator_2(some_func_2)


# @ - это синтаксический сахар, сигнал для интерпретатора, что нужно применить декоратор
# @print_decorator_2
# def some_func_3() -> str:
#     return 'Работает функция 3'
#
#
# print(some_func_2_mod())
# print(some_func_3())
#

# А что, если функция, которую я хочу декорировать, принимает аргумент?

# def print_decorator_3(func: Callable[[str], str]) -> Callable[[str], str]:
#     def wrapper(name: str) -> str:
#         print('Декоратор начал работу')
#         result = func(name) + '!'
#         print('Декоратор закончил работу')
#         return result
#
#     return wrapper
#

# @print_decorator_3
# def some_func_4(name: str) -> str:
#     return f'Работает функция 4, {name}'
#
#
# @print_decorator_3
# def some_func_5(name: str) -> str:
#     return f'Работает функция 5, {name}'
#
#
# print(some_func_4('Вася'))
# print(some_func_5('Петя'))


# def print_decorator_4(func: Callable) -> Callable:
#     def wrapper(name, age):
#         print('Декоратор начал работу')
#         result = func(name, age) + '!'
#         print('Декоратор закончил работу')
#         return result
#
#     return wrapper


# @print_decorator_4
# def some_func_6(name: str, age: int) -> str:
#     return f'Работает функция 6, {name}, {age}'
#
#
# print(some_func_6('Вася', 25))


# *args, **kwargs - сделает декоратор универсальным!!!!

# def print_decorator_5(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         print('Декоратор начал работу')
#         result = func(*args, **kwargs) + '!'
#         print('Декоратор закончил работу')
#         return result
#
#     return wrapper
#
#
# @print_decorator_5
# def some_func_7(name: str, middle_name: str, last_name: str, age: int, address='Борвиха Лухари Виладж') -> str:
#     return f'Работает функция 7, {name}, {middle_name}, {last_name}, {age}, {address}'
#
#
# print(some_func_7('Вася', 'Петрович', 'Пупкин', 25))


# Декоратор с параметрами

# def print_decorator_6(prefix: str, postfix: str) -> Callable:
#     def decorator(func: Callable) -> Callable:
#         def wrapper(*args, **kwargs):
#             print(prefix)
#             result = func(*args, **kwargs) + postfix
#             return result
#
#         return wrapper
#
#     return decorator
#
#
# @print_decorator_6('Декоратор начал работу', 'Декоратор закончил работу')
# def some_func_8(name: str, middle_name: str, last_name: str, age: int, address='Борвиха Лухари Виладж') -> str:
#     return f'Работает функция 8, {name}, {middle_name}, {last_name}, {age}, {address}'
#
#
# print(some_func_8('Вася', 'Петрович', 'Пупкин', 25, address='Москва'))
#

# Попробуем это сделать вручную
# modded_some_func_8 = print_decorator_6('Декоратор начал работу', 'Декоратор закончил работу')(some_func_8)
# print(modded_some_func_8('Вася', 'Петрович', 'Пупкин', 25))

# Мы можем сделать декоратор с параметром (число) и декарировать функцию, которая приннимает *args чисел -
# если сумма больше параметра - функция raise ValueError

# def check_sum(sum_limit: int) -> Callable:
#     def decorator(func: Callable) -> Callable:
#         def wrapper(*args):
#             if sum(args) > sum_limit:
#                 raise ValueError(f'Столько я не сосчитаю. Считаю только до {sum_limit}')
#             return func(*args)
#         return wrapper
#     return decorator
#
#
# @check_sum(10)
# def some_func_9(*args: int) -> int:
#     return sum(args)
#
#
# print(some_func_9(1, 2, 3, 4))

"""
time.perf_counter() — это функция из модуля time в стандартной библиотеке Python, которая предоставляет доступ к 
монотонному счётчику времени с наивысшим доступным разрешением для измерения коротких промежутков времени. 
Вот несколько ключевых моментов об time.perf_counter():

Монотонность: Этот счетчик является монотонным, что означает, что его значения никогда не уменьшаются. 
Это важно для измерения временных интервалов, так как это гарантирует, что разница между концом и началом 
интервала всегда будет положительной или нулевой, даже если системные часы изменяются.

Высокое разрешение: Функция предоставляет время с высокой точностью, что делает ее идеальной для замера 
времени выполнения операций, особенно когда требуется измерить очень короткие промежутки времени.

Независимость от системного времени: Значение, возвращаемое time.perf_counter(), не зависит от системного 
времени и не подвержено изменениям из-за корректировки часов или перехода на летнее/зимнее время.

Использование: Эта функция часто используется для бенчмаркинга и профилирования кода, поскольку 
она предоставляет более точные измерения времени, чем time.time() или time.clock().

Платформонезависимость: time.perf_counter() работает на различных платформах, 
предоставляя стабильный интерфейс для замера времени.

Возвращаемое значение: Функция возвращает время в секундах как число с 
плавающей точкой. С момента запуска Python (или от момента первого вызова time.perf_counter(), 
точное определение зависит от реализации) до момента вызова функции.


start_time = time.perf_counter()
finish_time = time.perf_counter()
"""


# def check_time_decorator(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         func(*args, **kwargs)
#         finish_time = time.perf_counter()
#         result_time = finish_time - start_time
#         print(f'Прошло {result_time:.10f} секунд')
#
#     return wrapper
#
#
# @check_time_decorator
# def some_func_10() -> None:
#     for i in range(1000000):
#         pass
#
#
# # some_func_10()
#
# from data.cities import cities_list
# """
# Что быстрее?
# Цикл for или map, или list comprehension?
# Сейчас узнаем :)
# """
#
# @check_time_decorator
# def for_test() -> None:
#     cities_lst = []
#     for city in cities_list:
#         cities_lst.append(city['name'])
#
#
# @check_time_decorator
# def map_test() -> None:
#     # Map obj будет гораздо быстрее - потому что он не создает новый список, а просто генератор (вычисления по требованию)
#     # cities_map_obj = map(lambda city: city['name'], cities_list)
#     cities_lst = list(map(lambda city: city['name'], cities_list))
#
#
# @check_time_decorator
# def list_comprehension_test() -> None:
#     cities_lst = [city['name'] for city in cities_list]
#
#
# for_test()
# map_test()
# list_comprehension_test()
