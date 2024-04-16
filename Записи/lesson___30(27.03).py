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


# Определим простой класс Car, который имеет один атрибут - brand (марка авто)
class Car:
    def __init__(self, brand) -> None:
        self.brand = brand

    # Создадим декоратор класса, который добавляет новый метод и атрибут к классу


# cls и self это всего лишь переменные, который могут называться как угодно
def add_method_and_attribute(cls) -> Any:
    cls.country = 'Japan'  # Добавляем новый атрибут класса

    def get_info(self) -> str:  # Определяем новый метод
        return f'This {self.brand} is form {self.country}'

    cls.get_info = get_info  # добавляем метод к классу
    return cls  # Возвращаем модифицированный класс


# Применяем декоратор к классу Car
@add_method_and_attribute
class Car:
    def __init__(self, brand) -> None:
        self.brand: Any = brand


# Создаем экземпляр класса Car и проверяем добавленный метод и атрибут
car = Car('Toyota')
info: Any = car.get_info()
car_country: Any = Car.country

print(info, car_country)
