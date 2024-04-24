"""
Lesson 31
01.04.2024

Концепция валидации данных
Ручной класс сериализатор и валидатор
Установка marshmallow
pip install marshmallow marshmallow-dataclass
Валидация с помощью marshmallow
Концепция схемы и поля
PostLoad - обработка данных после загрузки
Настройки полей

"""

from dataclasses import dataclass, field
from data import cities

# print(cities.cities_list)

"""
cities_list = [
    {
        "coords": {
            "lat": "52.65",
            "lon": "90.08333"
        },
        "district": "Сибирский",
        "name": "Абаза",
        "population": 14816,
        "subject": "Хакасия",
    },
"""


@dataclass
class City:
    name: str
    population: int
    district: str
    subject: str
    lat: float
    lon: float


class CityValidator:
    def __init__(self):
        self.city: dict = {}

    def validate(self, city: dict):
        self.city = city
        if not isinstance(self.city["name"], str):
            raise ValueError("Название города должно быть строкой")
        if not isinstance(self.city["population"], int):
            raise ValueError("Население должно быть числом")
        if not isinstance(self.city["district"], str):
            raise ValueError("Район должен быть строкой")
        if not isinstance(self.city["subject"], str):
            raise ValueError("Субъект должен быть строкой")
        if not isinstance(self.city["coords"], dict):
            raise ValueError("Координаты должны быть словарем")
        if not isinstance(self.city["coords"]["lat"], (float, int)):
            raise ValueError("Широта должна быть числом")
        if not isinstance(self.city["coords"]["lon"], (float, int)):
            raise ValueError("Долгота должна быть числом")
        return self.city


class CitySerializer:
    def __init__(self):
        self.city: str = ''

    def serialize(self, city: City):
        self.city = city
        return {
            "name": self.city.name,
            "population": self.city.population,
            "district": self.city.district,
            "subject": self.city.subject,
            "coords": {
                "lat": self.city.lat,
                "lon": self.city.lon
            }
        }

    @staticmethod
    def deserialize(data):
        return City(
            name=data["name"],
            population=data["population"],
            district=data["district"],
            subject=data["subject"],
            lat=data["coords"]["lat"],
            lon=data["coords"]["lon"]
        )


city_serializer = CitySerializer()

cities = [city_serializer.deserialize(city) for city in cities.cities_list]
print(cities)
