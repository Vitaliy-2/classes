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


# Абстрактные продукты
class AbstractKhinkali(ABC):
    @abstractmethod
    def eat(self) -> str:
        pass


class AbstractPelmeni(ABC):
    @abstractmethod
    def eat(self) -> str:
        pass


# Конкретные продукты
class KhinkaliWithLamb(AbstractKhinkali):
    def eat(self) -> str:
        return "Хинкали с бараниной"


class KhinkaliWithBeef(AbstractKhinkali):
    def eat(self) -> str:
        return "Хинкали с говядиной"


class PelmeniWithShrimp(AbstractPelmeni):
    def eat(self) -> str:
        return "Пельмени с креветками"


class PelmeniWithBeef(AbstractPelmeni):
    def eat(self) -> str:
        return "Пельмени с говядиной"


# Абстрактная фабрика
class AbstractDumplingFactory(ABC):
    @abstractmethod
    def create_khinkali(self) -> AbstractKhinkali:
        pass

    @abstractmethod
    def create_pelmeni(self) -> AbstractPelmeni:
        pass


# Конкретные фабрики
class KhinkaliFactory(AbstractDumplingFactory):
    def create_khinkali(self) -> AbstractKhinkali:
        return KhinkaliWithBeef()  # или KhinkaliWithLamb, в зависимости от предпочтений

    def create_pelmeni(self) -> AbstractPelmeni:
        # Эта фабрика не производит пельмени, но для соответствия интерфейсу возвращаем пельмени с говядиной
        return PelmeniWithBeef()


class PelmeniFactory(AbstractDumplingFactory):
    def create_khinkali(self) -> AbstractKhinkali:
        # Эта фабрика не производит хинкали, но для соответствия интерфейсу возвращаем хинкали с говядиной
        return KhinkaliWithBeef()

    def create_pelmeni(self) -> AbstractPelmeni:
        return PelmeniWithShrimp()  # или PelmeniWithBeef, в зависимости от предпочтений


# Фасад
class DumplingMealFacade:
    def __init__(self):
        self.factory: AbstractDumplingFactory | None = None

    def prepare_meal(self, meal_type: str):
        if meal_type == "khinkali":
            self.factory = KhinkaliFactory()
        elif meal_type == "pelmeni":
            self.factory = PelmeniFactory()
        else:
            raise ValueError("Неверный тип еды")

        khinkali = self.factory.create_khinkali()
        pelmeni = self.factory.create_pelmeni()
        print(khinkali.eat())
        print(pelmeni.eat())


# Использование
if __name__ == "__main__":
    meal_facade = DumplingMealFacade()
    meal_type = input("Выберите блюдо (khinkali/pelmeni): ")
    meal_facade.prepare_meal(meal_type)
