from typing import Callable


# def say_name(name: str) -> None:
#     def say_goodbye() -> None:
#         print(f'Пока, {name}!')
#
#     say_goodbye()
#
#
# say_name('Валера')
#
#
# def say_name2(name: str) -> Callable[[], None]:
#     def say_goodbye() -> None:
#         print(f'Привет, {name}!')
#
#     return say_goodbye
#
#
# sn: Callable[[], None] = say_name2('Валера')
# sn()
#
#
# def counter(start):
#     count = start
#
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#
#     return inner
#
#
# c = counter(10)
# print(c())
# print(c())
# print(c())
#
#
# def print_decorator(func):
#     def wrapper():
#         print('Декоратор начал работу')
#         func()
#         print('Декоратор закончил работу')
#
#     return wrapper
#
#
# def some_function():
#     print('Работает функция')
#
#
# f = print_decorator(some_function)
# f()
#
#
# def print_decorator_2(func: Callable[[], str]) -> Callable[[], str]:
#     def wrapper() -> str:
#         print('Декоратор начал работу')
#         result = func() + '!!!!!'
#         print('Декоратор закончил работу')
#         return result
#
#     return wrapper
#
#
# @print_decorator_2
# def some_func_2() -> str:
#     return 'Работает функция 2'
#
#
# print(some_func_2())
#
#
# # @ - это синтаксический сахар, сигнал для интерпретатора, что нужно применить декоратор
# @print_decorator_2
# def some_func_3() -> str:
#     return 'Работает функция 3'
#
#
# print(some_func_3())


def print_decorator_3(func: Callable[[str], str]) -> Callable[[str], str]:
    def wrapper(name: str) -> str:
        print('Декоратор начал работу')
        result = f'{func(name) + '!'}\nДекоратор закончил работу'
        # print('Декоратор закончил работу')
        return result

    return wrapper


@print_decorator_3
def some_func_4(name: str) -> str:
    return f'Работает функция 4, {name}'


@print_decorator_3
def some_func_5(name: str) -> str:
    return f'Работает функция 5, {name}'


print(some_func_4('Вася'))
print(some_func_5('Петя'))


def print_decorator_5(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print('Декоратор начал работу')
        result = func(*args, **kwargs) + '!'
        print('Декоратор закончил работу')
        return result

    return wrapper


@print_decorator_5
def some_func_7(name: str, middle_name: str, last_name: str, age: int, address='Борвиха Лухари Виладж') -> str:
    return f'Работает функция 7, {name}, {middle_name}, {last_name}, {age}, {address}'


print(some_func_7('Вася', 'Петрович', 'Пупкин', 25))


# Декоратор с параметрами

def print_decorator_6(prefix: str, postfix: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            print(prefix)
            result = func(*args, **kwargs) + postfix
            return result

        return wrapper

    return decorator


@print_decorator_6('Декоратор начал работу', f'\nДекоратор закончил работу')
def some_func_8(name: str, middle_name: str, last_name: str, age: int, address='Борвиха Лухари Виладж') -> str:
    return f'Работает функция 8, {name}, {middle_name}, {last_name}, {age}, {address}'


print(some_func_8('Вася', 'Петрович', 'Пупкин', 25, address='Москва'))


def check_sum(sum_limit: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args):
            if sum(args) > sum_limit:
                raise ValueError('Сумма больше лимита')
            return func(*args)

        return wrapper

    return decorator


@check_sum(100)
def some_func_9(*args: int) -> int:
    return sum(args)


print(some_func_9(50, 23))
