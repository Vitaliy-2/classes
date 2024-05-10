"""
Lesson 36: Поведенческие паттерны
- Strategy - стратегия
- Observer - наблюдатель
- Visitor - посетитель
- State - состояние
"""

# Стратегия - это поведенческий паттерн проектирования, который определяет семейство алгоритмов, инкапсулирует каждый
# из них и делает их взаимозаменяемыми. Он позволяет изменять алгоритмы независимо от клиентов, которые ими пользуются.

# Пример 1 - Стратегия приветствия


from abc import ABC, abstractmethod


class AbstractHelloStrategy(ABC):

    @abstractmethod
    def hello(self):
        pass


class FriendlyHelloStrategy(AbstractHelloStrategy):
    def hello(self):
        print("Привет! Как дела?")


class BuisnessHelloStrategy(AbstractHelloStrategy):
    def hello(self):
        print("Здравствуйте! Какие новости?")


class FamilyHelloStrategy(AbstractHelloStrategy):
    def hello(self):
        print("Здорово! Как день прошел?")


class HelloContext:
    def __init__(self, strategy: AbstractHelloStrategy):
        self.strategy = strategy

    def greet(self):
        self.strategy.hello()

    def set_strategy(self, strategy: AbstractHelloStrategy):
        self.strategy = strategy


class HelloFacade:
    def __init__(self):
        self.friendly: FriendlyHelloStrategy = FriendlyHelloStrategy()
        self.buisness: BuisnessHelloStrategy = BuisnessHelloStrategy()
        self.family: FamilyHelloStrategy = FamilyHelloStrategy()
        self.context: HelloContext = HelloContext(self.friendly)

    def greet(self):
        user_input = input("Какой тип приветствия вы хотите использовать? (1 - Дружеское, 2 - Деловое, 3 - Семейное): ")
        if user_input == "1":
            self.context.set_strategy(self.friendly)
        elif user_input == "2":
            self.context.set_strategy(self.buisness)
        elif user_input == "3":
            self.context.set_strategy(self.family)
        else:
            print("Неверный ввод")

        self.context.greet()


hello = HelloFacade()
hello.greet()
