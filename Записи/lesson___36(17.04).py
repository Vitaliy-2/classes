"""
Lesson 36: Поведенческие паттерны
- Strategy - стратегия
- Observer - наблюдатель
- Visitor - посетитель
- State - состояние
"""


# State - состояние. Паттерн, который позволяет объекту менять свое поведение в зависимости от своего состояния.
# Пример: бариста. В зависимости от состояния, он будет готовить кофе, чай или коктейли.

from abc import ABC, abstractmethod


class BaristaState(ABC):
    @abstractmethod
    def get_work(self):
        pass


class CoffeeState(BaristaState):
    def get_work(self):
        print("Приготовление кофе")


class TeaState(BaristaState):
    def get_work(self):
        print("Приготовление чая")


class CocktailState(BaristaState):
    def get_work(self):
        print("Приготовление коктейлей")


class CleanState(BaristaState):
    def get_work(self):
        print("Уборка")


class Barista:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def get_work(self):
        self.state.get_work()


barista = Barista()
cocktail_state = CocktailState()
tea_state = TeaState()
clean_state = CleanState()

barista.set_state(cocktail_state)
barista.get_work()
barista.set_state(tea_state)
barista.get_work()
