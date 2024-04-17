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


# 2 половины конструктора класса __init__ и __new__
class First:
    def __init__(self, name):
        self.name = name
        print('First.__init__')

    # new создает пустой объект, в котором ничего нет
    # после создания new передает пустой объект в init
    # super - вызывает метод родителя
    def __new__(cls, *args, **kwargs):
        print('First.__new__')
        return super().__new__(cls)

    def custom_method(self):
        print('First.custom_method')


class Second(First):
    def __init__(self, name, last_name):
        self.last_name = last_name
        print('Second.__init__')
        super().__init__(name)

    def custom_2_method(self):
        print('Second.custom_2_method')
        super().custom_method()


s = Second('Ivan', 'Ivanov')
s.custom_2_method()
