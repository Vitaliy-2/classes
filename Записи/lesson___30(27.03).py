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

import pickle
from dataclasses import dataclass


# Бинарник для сохранения информации и дальнейшего извлечения
# Аудио, видео, картинки


@dataclass
class Person:
    name: str
    age: int
    city: str


# data: dict[str, str] = {'key': 'value'}

data = Person('Ivan', 30, 'Moscow')

serialized_data: bytes = pickle.dumps(data)  # с s потому что смотрим на строку
print(serialized_data)

with open('../data/data.pickle', 'wb') as file:
    pickle.dump(data, file)  # без s потому сбрасываем в файл

with open('../data/data.pickle', 'rb') as file:
    data = pickle.load(file)
    print(data)
    print(type(data))
