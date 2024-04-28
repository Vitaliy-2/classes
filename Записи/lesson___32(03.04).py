"""
Lesson 32
03.04.2024

- Повторяем marshmallow
- Простой пример схемы
"""

from dataclasses import dataclass
from marshmallow import Schema, fields, pre_load, post_load


@dataclass
class City:
    name: str
    population: int
    district: str
    subject: str
    lat: float
    lon: float
    email: str


cities_list = [
    {"coords": {
        "lat": "52.65",
        "lon": "90.08333"
    },
        "district": "Сибирский",
        "name": "Абаза",
        "population": 14816,
        "subject": "Хакасия"
    },
    {"coords": {
        "lat": "53.71667",
        "lon": "91.41667"
    },
        "district": "Сибирский",
        "name": "Абакан",
        "population": 187239,
        "subject": "Хакасия"
    }]


class CitySchema(Schema):
    name = fields.Str()
    population = fields.Int()
    district = fields.Str()
    subject = fields.Str()
    lat = fields.Float()
    lon = fields.Float()
    email = fields.Str(load_default='info@default.com')  # Устанавливаем значение по умолчанию для email

    # Метод сработает перед тем как начнется валидация данных
    @pre_load()
    def unwrap_coords(self, data, **kwargs):
        # Этот метод будет вызван до десериализации каждого элемента списка.
        # Он изменяет структуру данных, извлекая координаты из вложенного словаря.
        # Делаем копию словаря, чтобы не изменять оригинальные данные
        data = data.copy()
        data.update({
            'lat': data['coords']['lat'],
            'lon': data['coords']['lon']
        })
        del data['coords']  # Удаляем исходный вложенный словарь координат
        return data

    @post_load
    def make_city(self, data, **kwargs):
        # Этот метод создает экземпляр City из десериализованных данных.
        return City(**data)


schema_many = CitySchema(many=True)
schema = CitySchema()

# Поштучно и множественно
cities = schema_many.load(cities_list)
print(cities)
city = schema.load(cities_list[0])
print(city)

# Сериализация - пробуем сделать dump
city2 = schema.dump(city)
print(city2)
