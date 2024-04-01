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

class Mana:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        if isinstance(other, int):
            self.value -= other
        else:
            raise ValueError('Можно вычитать только целые числа')
        return self.value


class Mage:
    def __init__(self):
        self.mana = Mana(100)


# mage = Mage()
# mage.mana - 30
# print(mage.mana.value)


class Health:
    def __init__(self, value):
        self.value = value
        print(f'Начальное здоровье: {self.value}')

    def __add__(self, other):
        self.value += other
        print(f'Здоровье повысилось до: {self.value}')
        return self.value

    def __sub__(self, other):
        self.value -= other
        print(f'Здоровье уменьшилось до: {self.value}')
        return self.value


class Berserk:
    def __init__(self, health: int = 120):
        self.health = Health(health)


berserk = Berserk()
# print(f'Начальное состояние здоровья: {berserk.health.value}')
berserk.health + 70
# print(f'Состояние здоровья после хилки на 70 хп: {berserk.health.value}')
berserk.health - 50
# print(f'Состояние здоровья после получения урона: {berserk.health.value}')
