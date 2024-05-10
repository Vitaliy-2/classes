"""
Lesson 36: Поведенческие паттерны
- Strategy - стратегия
- Observer - наблюдатель
- Visitor - посетитель
- State - состояние
"""

# Visitor - посетитель. Паттерн позволяет добавлять новые операции к объектам без изменения их классов.
"""
Абстрактный элемент дом
Конкретный дом Совы
Конкретный дом Ослика
Конкретный дом Кролика

Абстрактный посетитель
Конкретный посетитель Винни-Пух
Конкретный посетитель Пятачок
"""

from abc import ABC, abstractmethod


class House(ABC):
    @abstractmethod
    def accept(self, visitor: 'Visitor'):
        pass


class OwlHouse(House):

    def __init__(self):
        self.sweets = ['Пирожные', 'Мед', 'Молоко', 'Медовуха']

    def accept(self, visitor: 'Visitor'):
        visitor.visit_owl_house(self)


class DonkeyHouse(House):

    def __init__(self):
        self.stories = ['Моя жизнь - это боль', 'Я никому не нужен', 'Я никогда не найду свою любовь',
                        'Я никогда не стану счастливым']

    def accept(self, visitor: 'Visitor'):
        visitor.visit_donkey_house(self)


class RabbitHouse(House):

    def __init__(self):
        self.food = ['Морковь', 'Капуста', 'Свекла', 'Картошка']

    def accept(self, visitor: 'Visitor'):
        visitor.visit_rabbit_house(self)


class Visitor(ABC):
    @abstractmethod
    def visit_owl_house(self, house: OwlHouse):
        pass

    @abstractmethod
    def visit_donkey_house(self, house: DonkeyHouse):
        pass

    @abstractmethod
    def visit_rabbit_house(self, house: RabbitHouse):
        pass


class WinnieThePooh(Visitor):
    def visit_owl_house(self, house: OwlHouse):
        print("Винни-Пух посетил дом Совы, но там нечего есть")

    def visit_donkey_house(self, house: DonkeyHouse):
        story = set(house.stories).pop()
        print(f"Винни-Пух посетил дом Ослика и послушал грустные суицидальные истории на тему: {story}")

    def visit_rabbit_house(self, house: RabbitHouse):
        food = set(house.food).pop()
        print(f"Винни-Пух посетил дом Кролика и сожрал все, до чего смог дотянуться: {food}")


class Piglet(Visitor):
    def visit_owl_house(self, house: OwlHouse):
        sweets = set(house.sweets).pop()
        print(f"Пятачок посетил дом Совы и украл все пирожные: {sweets}")

    def visit_donkey_house(self, house: DonkeyHouse):
        print("Пятачок посетил дом Ослика и поддержал его в грусти")

    def visit_rabbit_house(self, house: RabbitHouse):
        print("Пятачок посетил дом Кролика и сделал уборку после Винни-Пуха")


# Создаем дома персонажей к которым будут приходить Винни-Пух и Пятачок
owl_house = OwlHouse()
donkey_house = DonkeyHouse()
rabbit_house = RabbitHouse()

# Создаем посетителей
winnie_the_pooh = WinnieThePooh()
piglet = Piglet()

# Винни-Пух пошел объедать товарищей
owl_house.accept(winnie_the_pooh)
donkey_house.accept(winnie_the_pooh)
rabbit_house.accept(winnie_the_pooh)

# Пятачок пошел воровать у товарищей
owl_house.accept(piglet)
donkey_house.accept(piglet)
rabbit_house.accept(piglet)
