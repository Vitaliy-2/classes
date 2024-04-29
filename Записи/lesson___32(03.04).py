"""
Lesson 32
03.04.2024

- Повторяем marshmallow
- Простой пример схемы
- Схема с прелоад и постлоад
- Схема с вложенными схемами
- Схема на основе датакласса (marshmallow_dataclass)
"""

from dataclasses import dataclass, field
from marshmallow import Schema, fields, pre_load, post_load
import marshmallow_dataclass
# оно позволит сократить код, без схемы указать лишь типы данных в датаклассе


@dataclass
class City:
    name: str
    population: int
    district: str
    subject: str
    email: str
    coords: dict = field(default_factory=dict)


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


class CoordsSchema(Schema):
    lat = fields.Float()
    lon = fields.Float()


class CitySchema(Schema):
    name = fields.Str()
    population = fields.Int()
    district = fields.Str()
    subject = fields.Str()
    coords = fields.Nested(CoordsSchema)  # Одна схема встроена в другую
    email = fields.Str(load_default='info@default.com')  # Устанавливаем значение по умолчанию для email

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
