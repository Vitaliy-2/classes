"""
Lesson 31
01.04.2024

Концепция валидации данных
Ручной класс сериализатор и валидатор
Установка marshmallow
pip install marshmallow marshmallow-dataclass
Валидация с помощью marshmallow
Концепция схемы и поля
PostLoad - обработка данных после загрузки.
PostLoad - если все пройдет проверки, то данные пойдут дальше.
Настройки полей

"""

from dataclasses import dataclass, field
from typing import Union, Dict
from marshmallow import Schema, fields, post_load, ValidationError

from data import cities
# from data.cities import cities_list

# print(cities.cities_list)

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
        "email": "abaza@mail.ru"
    },]


@dataclass
class City:
    name: str
    population: int
    district: str
    subject: str
    lat: float
    lon: float
    email: str


class CitySchema(Schema):
    name = fields.Str()  # fields - говорит что поле name должно быть строкой, и сам проверит
    population = fields.Int()  # Тут может быть строка, которую в теории можно преобразовать в число
    district = fields.Str()
    subject = fields.Str()
    coords = fields.Dict()
    lat = fields.Float(required=False)  # Означает что поле необязательное
    lon = fields.Float(required=False, validate=validate.Range(min=-90, max=90))
    email = fields.Email(required=False)

    @post_load  # Позволяет обрабатывать данные только после валидации
    def make_city(self, data, **kwargs):
        coords = data.pop('coords')
        data['lat'] = coords['lat']
        data['lon'] = coords['lon']
        return City(**data)


city_schema = CitySchema()
# load - автоматом вызывает метод make_city
city = city_schema.load(cities_list[0])
print(city)

# Преобразование данных в словарь
city_dict = city_schema.dump(city)
print(city_dict)
