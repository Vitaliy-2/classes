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
