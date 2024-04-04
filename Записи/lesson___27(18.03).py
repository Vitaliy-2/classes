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


@dataclass
class Person:
    """
    Уберем name и city из сравнения
    """
    name: str
    age: int = field(compare=False)  # Данная переменная не будет участвовать в сравнении __eq__
    city: str = field(compare=False)


p1 = Person('Вася', 20, 'Архангельск')
p2 = Person('Маша', 18, 'Санкт-Петербург')
p3 = Person('Вася', 20, 'Москва')
p4 = Person('Вася', 21, 'Москва')

p1_str = str(p1)
p1_new = eval(p1_str)

print(p1 == p4)
