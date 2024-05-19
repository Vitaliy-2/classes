"""
Lesson 38
Pytest
- Фикстуры
- Параметризация фикстур
"""
import pytest
import time

# Кейсы использования фикстур:
# 1. Подготовка данных для теста
# - Возвращение данных для одного текста
# - Возвращение данных для параметризатора
# 2. Очистка данных после теста
# 3. Подготовка сложных объектов для теста


class WeatherRequest:
    def __init__(self, city: str, api_key: str):
        self.city = city
        self.api_key = api_key
        self.response = None
        self.route = f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}'

    def get_weather(self):
        time.sleep(5)
        self.response = 'Sunny'


@pytest.fixture(scope='session')
def weather_data() -> WeatherRequest:
    weather_request = WeatherRequest('Moscow', '1234567890')
    weather_request.get_weather()
    return weather_request


def test_is_request_string(weather_data):
    assert isinstance(weather_data.response, str), 'Ответ не является строкой'


def test_is_request_sunny(weather_data):
    assert weather_data.response == 'Sunny', 'Погода не ясная'


def test_len_request(weather_data):
    assert len(weather_data.response) > 0, 'Данные не получены'
