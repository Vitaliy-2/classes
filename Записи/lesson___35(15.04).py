"""
Lesson 35: Структурные паттерны
- повторение порождающих паттернов
- Abstract Factory - абстрактная фабрика
- Abstract Method - абстрактный метод
- Facade - фасад
- Adapter - адаптер
- Decorator - декоратор - повторили
- Proxy - заместитель
"""

from dataclasses import dataclass, field
from abc import ABC, abstractmethod

# Adapter - адаптер, паттерн, который позволяет объектам с несовместимыми интерфейсами работать вместе.

"""
Напишем 2 JSON файла с погодными данными, с разной структурой
Напишем датакласс Weather, который будет принимать данные из JSON файла
Напишем адаптер, который будет принимать данные из JSON файла и преобразовывать их в объект Weather
"""


@dataclass
class Weather:
    city: str
    temperature: int
    wind_speed: int
    pressure: int
    humidity: int

    def __str__(self):
        return f"{self.city}: {self.temperature}°C, {self.wind_speed} м/с, {self.pressure} мм.рт.ст., {self.humidity}%"


weather_data_1 = {
    "city": "Moscow",
    "temperature": 15,
    "wind_speed": 5,
    "pressure": 760,
    "humidity": 70
}

weather_data_2 = {
    "main_info": {
        "city": "Moscow",
        "temperature": 15
    },
    "wind_info": {
        "speed": 5
    },
    'pressure_info': {
        "pressure": 760
    },
}


# Адаптер
class AbstractAdapter(ABC):

    def __init__(self, weather_data):
        self.weather_data = weather_data

    def load_data(self, weather_data):
        self.weather_data = weather_data

    @abstractmethod
    def adapt_data(self):
        pass


class WeatherAdapter1(AbstractAdapter):
    def adapt_data(self):
        return Weather(
            city=self.weather_data["city"],
            temperature=self.weather_data["temperature"],
            wind_speed=self.weather_data["wind_speed"],
            pressure=self.weather_data["pressure"],
            humidity=self.weather_data["humidity"]
        )


class WeatherAdapter2(AbstractAdapter):
    def adapt_data(self):
        return Weather(
            city=self.weather_data["main_info"]["city"],
            temperature=self.weather_data["main_info"]["temperature"],
            wind_speed=self.weather_data["wind_info"]["speed"],
            pressure=self.weather_data["pressure_info"]["pressure"],
            humidity=0
        )


weather1 = WeatherAdapter1(weather_data_1).adapt_data()
weather2 = WeatherAdapter2(weather_data_2).adapt_data()
print(weather1)
print(weather2)
