"""
Lesson 34: Порождающие паттерны
10.04.2024
- Singleton - одиночка
- Prototype - прототип
- Builder - строитель
- Abstract Factory - абстрактная фабрика
"""
# Builder - строитель
# Позволяет создавать сложные объекты пошагово

# Пример 1 BurgerBuilder
from abc import ABC, abstractmethod
from typing import List


class Burger:
    def __init__(self):
        self.ingredients: List[str] = []

    def add_ingredient(self, ingredient: str) -> None:
        self.ingredients.append(ingredient)

    def get_margeting_str(self) -> str:
        """Метод определяется в конкретных строителях"""
        pass


class AbstractBurgerBuilder(ABC):
    @abstractmethod
    def prepare_bun(self) -> None:
        pass

    @abstractmethod
    def insert_patty(self) -> None:
        pass

    @abstractmethod
    def add_condiments(self) -> None:
        pass

    def create_burger(self) -> None:
        self.burger = Burger()

    def get_burger(self) -> Burger:
        return self.burger


class FishBurgerBuilder(AbstractBurgerBuilder):
    def prepare_bun(self) -> None:
        self.burger.add_ingredient('Булочка для рыбургера')

    def insert_patty(self) -> None:
        self.burger.add_ingredient('Рыбный котлет')

    def add_condiments(self) -> None:
        self.burger.add_ingredient('Соус тар-тар')

    def get_margeting_str(self) -> str:
        return f'Самый вкусный рыбургер в мире! Содержит {", ".join(self.burger.ingredients)}'

    def create_burger(self) -> None:
        super().create_burger()
        self.prepare_bun()
        self.insert_patty()
        self.add_condiments()
        self.burger.get_margeting_str = self.get_margeting_str


class BurgerBuilder(AbstractBurgerBuilder):
    def prepare_bun(self) -> None:
        self.burger.add_ingredient('Булочка для бургера')

    def insert_patty(self) -> None:
        self.burger.add_ingredient('Говяжий котлет')

    def add_condiments(self) -> None:
        self.burger.add_ingredient('Кетчуп')
    
    def add_cheese(self):
        self.burger.add_ingredient('Сыр')

    def get_margeting_str(self) -> str:
        return f'Самый фукусный бургер в мире! Содержит: {", ".join(self.burger.ingredients)}'
    
    def create_burger(self) -> None:
        super().create_burger()
        self.prepare_bun()
        self.insert_patty()
        self.add_condiments()
        self.add_cheese()
        self.burger.get_margeting_str = self.get_margeting_str


b_builder = BurgerBuilder()
f_builder = FishBurgerBuilder()
b_builder.create_burger()
f_builder.create_burger()

b_burger = b_builder.get_burger()
f_burger = f_builder.get_burger()

print(b_burger.ingredients)
print(f_burger.ingredients)

print(b_burger.get_margeting_str())
print(f_burger.get_margeting_str())
