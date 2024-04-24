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
from typing import Union, Dict

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
        lat = self.city["coords"]["lat"]
        try:
            float(lat)
        except ValueError:
            raise ValueError(f"Широта должна быть числом {lat}")
        lon = self.city["coords"]["lon"]
        try:
            float(lon)
        except ValueError:
            raise ValueError(f"Долгота должна быть числом {lon}")
        return self.city


class CitySerializer:
    def __init__(self):
        self.__city: Union[None | Dict | City] = None
        self.__city_validator = CityValidator()

    def __city_validate(self, city: dict):
        return self.__city_validator.validate(city)

    def serialize(self, city: City):
        self.__city = city
        return {
            "name": self.__city.name,
            "population": self.__city.population,
            "district": self.__city.district,
            "subject": self.__city.subject,
            "coords": {
                "lat": self.__city.lat,
                "lon": self.__city.lon
            }
        }

    def deserialize(self, data):
        self.__city = self.__city_validate(data)
        return City(
            name=self.__city["name"],
            population=self.__city["population"],
            district=self.__city["district"],
            subject=self.__city["subject"],
            lat=float(self.__city["coords"]["lat"]),
            lon=float(self.__city["coords"]["lon"])
        )


city_serializer = CitySerializer()

cities = [city_serializer.deserialize(city) for city in cities.cities_list]
print(cities)
