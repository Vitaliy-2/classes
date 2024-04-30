"""
HomeWork №31-32
Погодный Аналитик с Marshmallow и Dataclasses
# pip install requests marshmallow marshmallow-dataclass marshmallow-jsonschema

"""
from dataclasses import dataclass
from pprint import pprint
from dataclasses import dataclass, field
from marshmallow import Schema, fields, pre_load, post_load, INCLUDE
import marshmallow_dataclass
from marshmallow.validate import Range


import requests


def get_weather(city_name):
    api_key = "23496c2a58b99648af590ee8a29c5348"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'lang': 'ru',
        'units': 'metric',
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()


# Пример использования
city = "Петрозаводск"
weather_data = get_weather(city)
# pprint(weather_data)


@dataclass
class CityWeather:
    name: str
    temp: float
    feels_like: float
    wind_speed: float

    def __str__(self):
        return (f"Город: {self.name}, Температура: {self.temp}, "
                f"Ощущается как: {self.feels_like}, Скорость ветра: {self.wind_speed}")


# Создание схемы на основе датакласса
WeatherSchema = marshmallow_dataclass.class_schema(CityWeather)


# Расширение своей схемой, схему созданную на основе датакласса
class ExtendWeatherSchema(WeatherSchema):
    temp = fields.Float(validate=Range(min=-80, max=80))

    @pre_load()
    def prepare_data(self, data, **kwargs):
        data['temp'] = data['main']['temp']
        data['feels_like'] = data['main']['feels_like']
        data['wind_speed'] = data['wind']['speed']
        allowed_key = ['name', 'temp', 'feels_like', 'wind_speed']

        return {key: data[key] for key in allowed_key}


city_weather_schema = ExtendWeatherSchema()
city_weather = city_weather_schema.load(weather_data)
print(city_weather)

city_weather_dict = city_weather_schema.dump(city_weather)
print(city_weather_dict)

# На основе схемы создаем JSON схему
# json_schema = JSONSchema()
# schema = json_schema.dump(city_weather_schema)
# pprint(schema)
