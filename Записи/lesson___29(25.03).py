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


@dataclass(order=True)  # order дает делать сравнения
class Person:
    # Исключаем лишние поля
    name: str = field(compare=False, metadata={"description": "Имя"})
    # метадата - добавление дополнительных условий
    age: int = field(metadata={"description": "Возраст"})
    city: str = field(compare=False, metadata={"description": "Город"})

    def __str__(self):
        """
        Дадим данные из меты ключ description
        Неоправданно завышенная сложность.
        Просто, чтобы показать возможности метаинформации.
        """
        # в fields(self) - помещается экземпляр класса, то есть вася и маша
        meta_str = ", ".join([f'{f.metadata['description']}: {getattr(self, f.name)}' for f in fields(self)])
        return meta_str


@dataclass(order=True)
class Employee(Person):
    position: str = field(metadata={"description": "Должность"})
    salary: int = field(metadata={"description": "Зарплата"})


p1 = Employee('Вася', 25, 'Москва', 'Программист', 100_000)
p2 = Employee('Маша', 30, 'Москва', 'Программист', 100_000)

print(p1)
print(p2)
