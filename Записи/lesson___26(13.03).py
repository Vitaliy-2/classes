"""
Lesson 26
13.03.2024
Магические методы Ч2
Магические методы для математических операций
__add__ - сложение
__sub__ - вычитание
__mul__ - умножение
__truediv__ - деление
__floordiv__ - целочисленное деление
__mod__ - остаток от деления
__pow__ - возведение в степень


Магические методы для операций inplace
__iadd__ - сложение
__isub__ - вычитание
__imul__ - умножение
__itruediv__ - деление

Практика - игровые персонажи, здоровье и мана
"""


#  Класс банковский счет с методом __add__ и __iadd__
class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self) -> str:
        return f'Банковский счет: {self.balance}'

    def __add__(self, other: float | int) -> 'BankAccount':
        if isinstance(other, (int, float)):
            self.balance += other
            return self

    def __iadd__(self, other: float | int) -> float | int:
        raise NotImplementedError

    def __sub__(self, other: float | int) -> 'BankAccount':
        if isinstance(other, (int, float)):
            # Условие чтобы не уйти в минус
            if self.balance - other < 0:
                raise ValueError('Недостаточно средств')
            self.balance -= other
            return self

    def __mul__(self, other: float | int) -> float | int:
        if isinstance(other, (int, float)):
            raise NotImplementedError

    def __truediv__(self, other: float | int) -> float | int:
        if isinstance(other, (int, float)):
            raise NotImplementedError


# Создаем объекты
my_account = BankAccount(1000)
print(my_account)

# Сложение
my_account + 500
my_account + 500
my_account + 500
my_account -= 200
print(my_account)
