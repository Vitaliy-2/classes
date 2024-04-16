"""
Lesosn 29
25.03.2024
Датаклассы Ч2
@dataclass(order=True) - для сравнения
Метаинформация в полях (для сериализации и других целей)
Наследование датаклассов
Декорация классов
Метаклассы - как концепция
"""

from dataclasses import dataclass, field, fields, asdict

# Класс - декоратор, который добавит к датаклассу методы

class CityDecorator:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        obj = self.cls(*args, **kwargs)
        obj.get_info = self.get_info
        return obj

    def get_info(self):
        return f'Информация о городе: {self.name}'


@CityDecorator
@dataclass
class City:
    name: str
    population: int
    latitude: float
    longitude: float
    region: str = field(default='Europe')
