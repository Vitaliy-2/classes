"""
Lesson 30
27.03.2024
Class decorators
Meta classes
Вложенные классы
Итераторы
Теория сериализации и десериализации
Библиотека pickle
Практика pickle
"""
from dataclasses import dataclass
from typing import Any

"""
Вложенные классы, или внутренние классы, это классы, которые определены внутри другого класса. 
Они используются по разным причинам:

Инкапсуляция: Вложенный класс может быть скрыт от внешнего мира и использоваться 
только внутри внешнего класса, что улучшает инкапсуляцию.

Логическая структура: Если класс A является частью класса B и не имеет смысла 
без класса B, его можно сделать вложенным классом.

Улучшение читаемости и поддерживаемости кода: Если класс используется только 
одним внешним классом, его удобно сделать вложенным, чтобы упростить код и улучшить его поддерживаемость.
"""


class Outer:
    def __init__(self, outer_var, db_table, inner_dict: dict):
        self.outer_var = outer_var
        self.db_table = db_table
        self.inner = self.Inner(**inner_dict)

    @dataclass
    class Inner:
        inner_var: int
        db_table: str

        def get_all_params_dict(self) -> dict[str, Any]:
            return self.__dict__


inner_dict_params = {'inner_var': 2, 'db_table': 'users'}
outer = Outer(1, 'Личные данные', inner_dict_params)
print(outer.inner.get_all_params_dict())

inner = Outer.Inner(**inner_dict_params)
print(inner.get_all_params_dict())


@dataclass
class City:
    name: str
    country: str
    population: int


list_dict_cities = [
    {"name": "Moscow", "country": "Russia", "population": 12615882},
    {"name": "Paris", "country": "France", "population": 2140526},
    {"name": "Berlin", "country": "Germany", "population": 3769495},
]

cities_2 = []
for city in list_dict_cities:
    cities_2.append(City(**city))


cities = [City(**city) for city in list_dict_cities]
