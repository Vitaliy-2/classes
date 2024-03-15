# Инструменты классов

# class Test:
#
#     def get_sum(self):
#         return self.a + self.b
#
#
# # Создадим экземпляр класса
# test = Test()
# test.a = 10
# test.b = 20
# print(test.get_sum())  # 30
# print(test.__dict__)  # {'a': 10, 'b': 20}

# Класс персон, содержит инфу о человеке

# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def __str__(self):  # Пользовательское представление объекта
#         """
#         Метод для представления объекта в виде  строки.
#         Используется для вывода информации об объекте через print
#         :return:
#         """
#         return f'Информация о человеке: {self.name}, {self.age}, {self.address}'
#
#     def __repr__(self):
#         """
#         Метод для представления объекта в виде строки.
#         Используется для возможности воссоздать объект через eval().
#         Вторично: для вывода информации об объекте через print
#         :return:
#         """
#         return f"{self.__class__.__name__}('{self.name}', {self.age}, '{self.address}')"
#
#
# # Создадим экземпляр класса
# person = Person('Николай', 25, 'USA')
# person2 = Person('Абрахам', 35, 'Канада')
# persons = [person, person2]
# print(person)
# print(person2)
# [print(person) for person in persons]
#
# # Получим значение репр для person
# repr_str = repr(person)
# print(repr_str)
#
# # Восстановим объект person из строки
# new_person = eval(repr_str)
# print(new_person)

# - __str__ - пользовательское представление объекта
# - __repr__ - техническое представление объекта
# - eval() - встроенная функция для выполнения строки как код Python


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f'Продукт: {self.name}. Цена: {self.price} рублей.'
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.name}', {self.price}')"
#
#
# products = []
# while True:
#     if len(products) > 4:
#         raise ValueError('Количество продуктов не должно превышать 4')
#
#     name = input('Ведите название товара: ')
#     if not name:
#         break
#
#     price = float(input('Введите цену товара: '))
#
#     product = Product(name, price)  # Создаем экземпляр класса продукт
#     products.append(product)
#
#
# print(products)  # Это будет принт  repr
# [print(product) for product in products]  # А УЖЕ ЭТО ПРИНТ str


# __len__ - метод для определения длины объекта

# class Pipe:
#     # Допустимые марки в атрибуте класса
#     marks = ['M-1', 'M-2', 'M-3', 'M-4', 'M-5']
#     def __init__(self, mark, material, diameter, length):
#         self.mark = self.mark_validate(mark)
#         self.material = material
#         self.diameter = diameter
#         self.length = length
#
#     def mark_validate(self, mark):
#         if mark not in self.marks:
#             raise ValueError(f'Марка {mark} не доступна для трубы. Выберите из {self.marks}')
#         return mark
#
# # Чтобы пайтон понял, что длина лежит именно в переменной length, а не где-то еще
#     def __len__(self):
#         return self.length
#
#     def __str__(self):
#         return f'Труба {self.mark} из {self.material} диаметром {self.diameter} мм и длиной {self.length}'
#
#
# pipe = Pipe('M-2', 'Сталь', 100, 500)
# pipe2 = Pipe('M-5', 'Сталь', 100, 1000)
# # print(len(pipe))  # 500
# # print(len(pipe2))  # 1000
# #
# # print(len(pipe) > len(pipe2))  # False
#
# print(pipe)
# print(pipe2)
#
# pipe.mark = "Труба"
# print(pipe)

# Класс персона. Имя, фамилия, должность, зарплата, срок службы

class Person:
    def __init__(self, name, age, surname, position, salary, service):
        self.__name = name  # _ - защищает от изменения атрибута. Двойное подчеркивание - гарантия
        self.__age = age
        self._surname = surname
        self.position = position
        self.salary = salary
        self.service = service

    def __str__(self):
        return f'{self.__name} {self._surname} {self.__age}'

    def __repr__(self):
        return f'Person({self.__name}, {self._surname}, {self.position}, {self.salary}, {self.service})'

    @staticmethod
    def __validate_age(age):
        if isinstance(age, int) and 16 <= age <= 100:
            return True
        return False

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        """
        Проверяем что возраст число и оно от 16 до 100
        :param age:
        :return:
        """
        if isinstance(age, int) and 16 <= age <= 100:
            self.__age = age
        else:
            raise ValueError('Возраст должен быть числом и быть в диапазоне от 16 до 100')



# person_1 = Person('Ivan', 'Ivanov', 'developer', 1000, 5)
#
# print(person_1)
# # print(person_1.__name)
#
# new_name = 'Petr'
# person_1.__name = new_name
# # print(person_1.__name)
# print(person_1.__dict__)
#
# # Переопределим в Петра
# person_1._Person__name = new_name
# print(person_1)


p1 = Person('Ivan', 30, 'Ivanov', 'developer', 1000, 5)
print(p1)
p1.age = 40
print(p1.age)
print(p1)

p1.age = 100
