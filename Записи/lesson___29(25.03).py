"""
Lesosn 29
25.03.2024
Датаклассы Ч2
@dataclass(order=True) - для сравнения
Метаинформация в полях (для сериализации и других целей)
Наследование датаклассов
Декорация классов
Метаклассы - как концепция
"""

from dataclasses import dataclass, field, fields, asdict


class MetaClass(type):  # Указываем тип метакласса (type)
    def __new__(cls, name, bases, dct):  # получаем атрибуты класса
        # cls - сам объект метакласса
        # name - имя класса
        # bases - родительские классы
        # dct - атрибуты класса
        print('Создаем класс с именем', name)
        print(type(name))
        # Добавляем атрибут к классу
        dct['new_attribute'] = 100
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MetaClass):  # Определяем класс с использованием метакласса
    pass


# Создаем экземпляр класса
my_class = MyClass()
# выводим атрибут
print(my_class.new_attribute)


class User(metaclass=MetaClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age
