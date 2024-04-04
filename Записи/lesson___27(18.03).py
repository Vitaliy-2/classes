"""
Lesson 27
18.03.2024
Разбор hw_35
Dataclasses
- как определяется repr
- как определяется eq
- сериализация и десериализация
- field(default_factory=list) - для изменяемых типов
- field(compare=False) - для исключения из сравнения
- __post_init__ - для валидации
- fields(default = 0) - Значение по умолчанию

СЕРИАЛИЗАЦИЯ - упрощение, то есть превращение экземпляра в строку
ДЕСЕРИАЛИЗАЦИЯ - усложнение, превращение экземпляра из строки в объект

"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Person:
    """
    Уберем name и city из сравнения
    """
    name: str
    city: str = field(compare=False)
    hobbies: List[str] = field(default_factory=list)  # Чтобы корректно добавлять данные в список
    age: int = field(compare=False, default=0)  # Данная переменная не будет участвовать в сравнении __eq__

    def __post_init__(self):
        self.age = self.validate_age(self.age)

    @staticmethod
    def validate_age(age):
        if not isinstance(age, int):
            raise TypeError('Возраст должен быть числом')
        if age < 0:
            raise TypeError('Возраст не может быть отрицательным')
        if age > 150:
            raise TypeError('Возраст не может быть больше 150')
        return age


p1 = Person('Иван', 'Москва', ['плавание', 'путешествия'], 35)
p2 = Person('Анна', 'Санкт-Петербург', ['рафтинг', 'манга'])
p1.hobbies.append('программирование')
p2.hobbies.append('JS')
print(f'{p1=}')
print(f'{p2=}')


@dataclass
class City:
    name: str
    population: int
    lat: float = field(compare=False)
    lon: float = field(compare=False)
    region: str = field(compare=False)


city1 = City('Москва', 15_000_000, 34.234234, 45.1231231, 'Европейский')
city2 = City('Санкт-Петербург', 11_000_000, 24.234234, 35.1231231, 'Европейский')
city3 = City('Москва', 15_000_000, 10.2567234, 55.1234231, 'Европейский')
city4 = City('Петрозаводск', 9_000_000, 21.76674234, 33.12657231, 'Европейский')

print(f'{city1=}')
print(f'{city2=}')
print(f'{city3=}')
print(f'{city4=}')

print(f'Сравнение Москвы населением: {city1.population} с Москвой населением: {city1.population}: {city1 == city3}')
print(f'Сравнение Москвы населением: {city1.population} с Питером населением: {city2.population}: {city1 == city2}')
print(f'Сравнение Петрозаводска населением: {city4.population} с Москвой населением: {city1.population}: {city4 == city1}')
print(f'Сравнение Петрозаводска населением: {city4.population} с Питером населением: {city2.population}: {city4 == city2}')
