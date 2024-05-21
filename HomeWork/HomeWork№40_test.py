"""
HomeWork №40
Pytest для проверки запроса погоды
"""

import pytest
import requests

API_KEY = "23496c2a58b99648af590ee8a29c5348"
UNITS = "metric"
LANG = "ru"


class WeatherRequest:
    def __init__(self, api_key: str = API_KEY, units: str = UNITS, lang: str = LANG):
        self.city: None | str = None
        self.api_key = api_key
        self.units = units
        self.lang = lang
        self.url: None | str = None
        self.data: None | dict = None

    def __get_url(self):
        self.url = (f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units="
                    f"{self.units}&lang={self.lang}")

    def __get_data(self):
        self.data: dict = requests.get(self.url).json()

    def __call__(self, city: str) -> dict:
        self.city = city
        self.__get_url()
        self.__get_data()
        return self.data


# Делаем запрос погоды Москва
wr = WeatherRequest()
weather_moscow = wr('Москва')
print(weather_moscow)


cities = [
    ('Москва', {"lon": 37.6156, "lat": 55.7522}),
    ('Воронеж', {"lon": 39.17, "lat": 51.6664}),
    ('Санкт-Петербург', {"lon": 30.2642, "lat": 59.8944}),
    ('Краснодар', {"lon": 38.9769, "lat": 45.0328}),
    ('Сочи', {"lon": 39.7303, "lat": 43.6}),
]


@pytest.fixture(scope='module')
def weather_request():
    """
    Создает экземпляр класса WeatherRequest. Делает запрос погоды для Москвы.
    Возвращает словарь с данными о погоде
    """
    return WeatherRequest(api_key=API_KEY, units=UNITS, lang=LANG)('Москва')


@pytest.fixture(scope='module')
def weather_request_parametrize():
    """
    Создает экземпляр класса WeatherRequest и возвращает его
    Тестовая функция будет принимать параметр city_name и делать запрос погоды для нужного города
    """
    return WeatherRequest(api_key=API_KEY, units=UNITS, lang=LANG)


def test_weather_request_city_name(weather_request):
    assert weather_request['name'] == 'Москва', 'Название города не соответствует ожидаемому'


def test_weather_request_coord(weather_request):
    assert weather_request['coord'] == {"lon": 37.6156, "lat": 55.7522}, 'Координаты города не соответствуют ожидаемым'


def test_weather_request_weather_key(weather_request):
    assert set(weather_request['weather'][0].keys()) == {'id', 'main', 'description', 'icon'}, ('Отсутствуют ключи '
                                                                                                'в секции weather')


def test_weather_request_main_key(weather_request):
    assert set(weather_request['main'].keys()) == {'temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity',
                                                   'sea_level', 'grnd_level'}, 'Отсутствуют ключи в секции main'


@pytest.mark.slow
@pytest.mark.parametrize('city_name, expected_coords', cities)
def test_weather_request_city_coodrd_name_parametrize_slow(weather_request_parametrize, city_name, expected_coords):
    assert weather_request_parametrize(city_name)['coord'] == expected_coords, (f'Координаты города {city_name} не '
                                                                                f'соответствуют ожидаемым')


"""
Команды запуска:
Все тесты: pytest
Только тесты с медленным тегом: pytest -m slow
Тесты без тега slow: pytest -m "not slow"
Только тесты с параметризацией: pytest -k parametrize
"""
