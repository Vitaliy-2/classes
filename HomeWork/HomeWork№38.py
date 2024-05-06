"""
HomeWork №38
Система для заказа пиццы
"""

from abc import ABC, abstractmethod


# Абстрактный класс для фабрики ингредиентов
class IngredientFactory(ABC):
    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass


# Конкретная реализация фабрики ингредиентов для Dodo пиццы
class DodoIngredientFactory(IngredientFactory):
    def create_cheese(self):
        return 'Колумбия'

    def create_sauce(self):
        return 'Томатный'


# Фабрика для управления размерами пиццы
class SizeFactory:
    def create_size(self, size: str):
        if size == 'маленькая':
            return '15 см.'
        elif size == 'средняя':
            return '20 см.'
        elif size == 'большая':
            return '30 см.'
        else:
            return 'Такого размера у нас нет.'


# Строитель для сборки пиццы
class PizzaBuilder:
    def __init__(self, ingredient_factory, size_factory):
        self.ingredient_factory = ingredient_factory
        self.size_factory = size_factory
        self.pizza_type = None
        self.size = None

    def set_size(self, size):
        self.size = size

    def set_type(self, pizza_type):
        self.pizza_type = pizza_type

    def build(self):
        cheese = self.ingredient_factory.create_cheese()
        sauce = self.ingredient_factory.create_sauce()
        size = self.size_factory.create_size(self.size)
        if size != '15 см.' and size != '20 см.' and size != '30 см.':
            return 'Пиццы такого размера в меню нет.'
        else:
            return f"Пицца: Размер {size}, Тип: {self.pizza_type}, С сыром - {cheese} и соусом - {sauce}"


# Функция для создания заказа пиццы
def create_pizza():
    ingredient_factory = DodoIngredientFactory()
    size_factory = SizeFactory()
    pizza_builder = PizzaBuilder(ingredient_factory, size_factory)
    user_input = input('Выберите размер пиццы, который Вы хотите заказать ( Маленькая / Средняя / Большая ): ').lower()
    pizza_builder.set_size(user_input)
    pizza_builder.set_type("мясная")
    pizza = pizza_builder.build()
    return pizza


# Точка входа в программу
def main():
    pizza_order = create_pizza()
    print(pizza_order)


if __name__ == "__main__":
    main()
