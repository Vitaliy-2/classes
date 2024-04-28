"""
Lesson 32
03.04.2024

- Повторяем marshmallow
- Простой пример схемы
"""

from dataclasses import dataclass
from marshmallow import Schema, fields


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
    email = fields.Email(missing="info@default.com")  # Устанавливаем значение по умолчанию для email


# Создаём экземпляр схемы
schema = CitySchema()

# Пример десериализации для первого города в списке
example_city_dict = cities_list[0]
example_city_dict["lat"] = example_city_dict["coords"]["lat"]
example_city_dict["lon"] = example_city_dict["coords"]["lon"]
# Удаляем вложенный словарь 'coords', так как он больше не нужен
del example_city_dict["coords"]

# Десериализация словаря в объект City
city_object = schema.load(example_city_dict)
print(city_object)

# Сериализация объекта City в словарь
city_dict = schema.dump(city_object)
print(city_dict)
