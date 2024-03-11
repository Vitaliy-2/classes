# Синтаксис
# class LadaCar:
#     price = 100500  # Атрибут или поле. Инфа содержит каждый экземпляр этого класса
#     color = 'black'
#
#
# # Экземпляр класса
# lada = LadaCar()
# lada2 = LadaCar()
# lada3 = LadaCar()
#
# # Доступ к атрибутам
# print(lada.price)
# print(lada2.price)
# print(lada3.price)
#
# # Изменение атрибутов класс
#
# lada.color = 'red'
# lada.price = 1
# print(lada.color)
# print(lada.price)
# print(lada2.color)
# print(lada2.price)
#
#
# # Атрибуты экземпляра класса и инициализация
# # Это типо то, что будет красить машины
# # Конструктор класса делится на new  и init
#
# # При создании тайоты будут ожидаться две переменные, аргумента прайс и колор
# # self означает кто КОНКРЕТНАЯ тайота будет стоить столько, а не все
#
#
# class ToyotaCar:  # Класс
#     # Производитель - классовый атрибут
#     manufacturer = 'Кировский завод №1'
#
#     def __init__(self, price, color):  # Метод. Инициализация
#         self.price = price
#         self.color = color
#         # self.manufacturer = 'Киров'
#         print(f'Создан новый объект класса ToyotaCar '
#               f'с ценой {self.price} и цветом {self.color} '
#               f'от производителя {self.manufacturer}'
#               f'с ID {id(self)}')
#
#
#     def __new__(cls, *args, **kwargs):
#         print(f'Вызван метод __new__ класса {cls.__name__}')
#         print(f'Аргументы: {args}, {kwargs}')
#         print(f'ID объекта: {id(cls)}')
#         return super().__new__(cls)
#
#         # Распечатаем данные о производителе
#         # print(f'Производитель: {ToyotaCar.manufacturer}')
#         # print(f'Производитель: {__class__.manufacturer}')
#         #
#         # # Распечаем имя класса
#         # print(f'Имя класса: {__class__.__name__}')
#
#
# toyota = ToyotaCar(200000, 'black')
# # print(toyota.price, toyota.color)
#
# toyota2 = ToyotaCar(250000, 'yellow')
# # print(toyota2.price, toyota2.color)

class LadaCar:
    price = 1000
    bodies = ['sedan', 'hatchback', 'universal']

    def __init__(self, model, color, year, body):
        self.model = model
        self.color = color
        self.year = year
        self.body = self.validate_body(body)
        self.some_attr = None  # Это можно определить внутри методов

    def validate_body(self, body):
        if body not in self.bodies:
            raise ValueError(f'Кузов {body} не доступен для модели {self.model}')
        return body

    def get_price(self):  # Это не функция, а метод класса
        return f'Цена автомобиля {self.price}'

    def get_color(self):
        return f'Цвет автомобиля {self.color}'

    @staticmethod  # Позволяет вклинить доп метод, исключив селф
    def get_lada_value(length, width, height):
        return length * width * height

    @classmethod  # Метод работает на весь класс, а не на конкретный экземпляр
    def set_bodies(cls, bodies):
        cls.bodies = bodies


lada_kalina = LadaCar('Kalina', 'white', 2020, body='sedan')
print(lada_kalina.bodies)

lada_kalina.set_bodies(['sedan', 'hatchback', 'universal', 'crossover'])

lada_priora = LadaCar('Priora', 'black', 2015, body='crossover')
print(lada_kalina.bodies)
print(lada_priora.bodies)

print(lada_kalina.get_color())
print(lada_priora.get_color())

print(lada_kalina.get_price())
print(lada_priora.get_price())

print(lada_kalina.get_lada_value(2, 3, 4))

print(LadaCar.get_lada_value(2, 3, 4))
