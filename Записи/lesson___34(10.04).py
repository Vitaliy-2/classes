"""
Lesson 34: Порождающие паттерны
10.04.2024
- Singleton - одиночка
- Prototype - прототип
- Builder - строитель
- Abstract Factory - абстрактная фабрика
"""

# Abstract Factory - абстрактная фабрика
# Паттерн Abstract Factory предоставляет интерфейс для создания семейств взаимосвязанных или взаимозависимых объектов,
# не специфицируя их конкретных классов.

from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    """
    Абстрактный продукт A. Определяет интерфейс для продуктов семейства A.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    """
    Конкретный продукт A1. Реализует интерфейс продукта A.
    Создается фабрикой 1.
    """

    def operation(self) -> str:
        return "Результат работы ConcreteProductA1"


class ConcreteProductA2(AbstractProductA):
    """
    Конкретный продукт A2. Реализует интерфейс продукта A.
    Создается фабрикой 2.
    """

    def operation(self) -> str:
        return "Результат работы ConcreteProductA2"


class AbstractFactory(ABC):
    """Абстрактная фабрика"""

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Конкретная фабрика 1. Делает продукты сеймейства 1.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()


class ConcreteFactory2(AbstractFactory):
    """
    Конкретная фабрика 2. Делает продукты сеймейства 2.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()


# Facade
# Паттерн Facade предоставляет простой интерфейс к сложной системе классов, библиотеке или фреймворку.

class Facade:
    def __init__(self):
        self.factory: AbstractFactory | None = None

    def __call__(self):
        user_input = input("Введите 1 или 2: ")
        if user_input == "1":
            self.factory = ConcreteFactory1()
        elif user_input == "2":
            self.factory = ConcreteFactory2()
        else:
            raise ValueError("Неверный ввод")

        if self.factory:
            product = self.factory.create_product_a()
            print(product.operation())


if __name__ == "__main__":
    facade = Facade()
    facade()
