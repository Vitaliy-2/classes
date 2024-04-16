"""
Lesson 30
27.03.2024
Class decorators
Meta classes
Вложенные классы
Итераторы
Теория сериализации и десериализации
Библиотека pickle
Практика pickle
"""
from typing import Any


# Определим класс-декоратор, который будет добавлять серию методов к другому классу
class AddSeriesOfMethods:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        # Создаем экземпляр оригинального класса
        instance = self.cls(*args, **kwargs)

        # Добавляем методы к экземпляру
        def first_method(self):
            return "This is the first method"

        def second_method(self):
            return "This is the second method"

        def third_method(self):
            return "This is the third method"

        # __get__ - метод привязывает метод к экземпляру`
        instance.first_method = first_method.__get__(instance)
        instance.second_method = second_method.__get__(instance)
        instance.third_method = third_method.__get__(instance)

        return instance


# Определим простой класс, к которому будем применять наш класс-декоратор
@AddSeriesOfMethods
class SimpleClass:
    def __init__(self, name):
        self.name = name


# Создадим экземпляр декорированного класса и проверим добавленные методы
decorated_instance = SimpleClass("Example")
print(decorated_instance.first_method())
print(decorated_instance.second_method())
print(decorated_instance.third_method())