"""
Lesson 33
08.04.2024
- Повторяем dataclasses
- Знакомство с UML и PlantUML
- Устанавливаем Java
- Устанавливаем PlantUML плагин
- Работаем в .wsd файлах
"""

from dataclasses import dataclass, field


# default - значение по умолчанию
# default_factory - для списков и словарей делает копии чтобы атрибуты не ссылались на одну и ту же коллекцию
@dataclass(order=True)
class Person:
    first_name: str = field(compare=False)
    last_name: str = field(compare=False)
    age: int
    growth: float = field(default=0.0, compare=False)
    is_checked: bool = field(default=False, compare=False)

    def __post_init__(self):
        if self.age < 0:
            raise ValueError('Возраст не должен быть отрицательным')
        if self.growth < 0:
            raise ValueError('Рост не должен быть отрицательным')

    def __bool__(self):
        return self.is_checked


p1 = Person('Филипп', 'Киркоров', 50, 2.10)
p2 = Person('Лариса', 'Гузеева', 56, 1.65)

print(p1 > p2)
print(p1 < p2)
print(p1)
p1_str = str(p1)
p1_str1 = repr(p1)  # Сериализация в строку
print(p1_str)
print(p1_str1)
p1_new = eval(p1_str)  # Десериализация в экземпляр датакласса
p1_new1 = eval(p1_str1)
print(p1_new)
print(p1_new1)

