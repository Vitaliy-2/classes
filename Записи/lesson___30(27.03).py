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


# Определение метакласса, который добавляет методы и атрибут к классу
class AddMethodsMeta(type):
    def __new__(cls, name, bases, dct):
        # Добавление нового атрибута к классу
        dct['new_attribute'] = 'New Attribute Value'

        # Добавление новых методов к классу
        def first_new_method(self):
            return "First new method"

        def second_new_method(self):
            return "Second new method"

        dct['first_new_method'] = first_new_method
        dct['second_new_method'] = second_new_method

        # Создание нового класса с помощью super()
        return super().__new__(cls, name, bases, dct)


# Использование метакласса для создания нового класса
class ExtendedClass(metaclass=AddMethodsMeta):
    def original_method(self):
        return "Original method"


# Создание экземпляра класса
instance = ExtendedClass()

# Проверка работы добавленных методов и атрибута
print(instance.new_attribute)
print(instance.original_method())
print(instance.first_new_method())
print(instance.second_new_method())

