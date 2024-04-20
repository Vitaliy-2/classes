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
from data.cities import cities_list


# Бинарник для сохранения информации и дальнейшего извлечения
# Аудио, видео, картинки


# @dataclass
# class Person:
#     name: str
#     age: int
#     city: str
#
#
# # data: dict[str, str] = {'key': 'value'}
#
# data = Person('Ivan', 30, 'Moscow')
#
# serialized_data: bytes = pickle.dumps(data)  # с s потому что смотрим на строку
# print(serialized_data)
#
# with open('../data/data.pickle', 'wb') as file:
#     pickle.dump(data, file)  # без s потому сбрасываем в файл
#
# with open('../data/data.pickle', 'rb') as file:
#     data = pickle.load(file)
#     print(data)
#     print(type(data))


"""
# Практика!
1. Импортируйте переменную, содержающую список городов
2. Попробуйте создать список словарей, из Городов
3. Опишите датакласс для города
4. Создайте список экземпляров датакласса
5. Сериализуйте список экземпляров датакласса в файл cities.pickle
6. Десериализуйте файл cities.pickle обратно в список экземпляров датакласса
"""

# city = [city['name'] for city in cities_list]
# print(city)


@dataclass
class City:
    name: str
    population: int
    latitude: float
    longitude: float
    region: str


cities = []

for city_info in cities_list:
    city = City(
        name=city_info["name"],
        population=city_info["population"],
        latitude=float(city_info["coords"]["lat"]),
        longitude=float(city_info["coords"]["lon"]),
        region=city_info["subject"]
    )
    cities.append(city)

print(cities[:5])

FILE = r"../data/cities.pickle"

with open(FILE, 'wb') as file:
    pickle.dump(cities, file)  # без s потому сбрасываем в файл

with open(FILE, 'rb') as file:
    cities = pickle.load(file)
    print(cities[:5])
    print(type(cities))
    print(type(cities[0]))
