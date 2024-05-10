"""
Lesson 36: Поведенческие паттерны
- Strategy - стратегия
- Observer - наблюдатель
- Visitor - посетитель
- State - состояние
"""

# Observer - наблюдатель - это поведенческий паттерн проектирования, который создает механизм подписки, позволяющий одним объектам следить и реагировать на события, происходящие в других объектах.

# Напишем пример с датчиками умного дома и их наблюдателями.

from abc import ABC, abstractmethod


class Sensor(ABC):
    """
    Абстрактный класс датчика
    """

    def __init__(self, name: str):
        self.name = name
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, value):
        for observer in self.observers:
            observer.update(self.name, value)

    @abstractmethod
    def get_value(self):
        pass


class TemperatureSensor(Sensor):
    """
    Класс датчика температуры
    """

    def get_value(self):
        return 25


class HumiditySensor(Sensor):
    """
    Класс датчика влажности
    """

    def get_value(self):
        return 50


class AbstractObserver(ABC):
    """
    Абстрактный класс наблюдателя
    """

    @abstractmethod
    def update(self, sensor_name, value):
        pass


class ConsoleObserver(AbstractObserver):
    """
    Консольный наблюдатель
    """

    def update(self, sensor_name, value):
        print(f"Датчик {sensor_name} сообщает значение: {value} в {self.__class__.__name__}")


class FileObserver(AbstractObserver):
    """
    Файловый наблюдатель
    """

    def update(self, sensor_name, value):
        with open("log.txt", "a") as file:
            file.write(f"Датчик {sensor_name} сообщает значение: {value} в {self.__class__.__name__}\n")


# Тесты
t1 = TemperatureSensor("Температурный датчик №1")
t2 = TemperatureSensor("Температурный датчик №2")
h1 = HumiditySensor("Датчик влажности №1")
h2 = HumiditySensor("Датчик влажности №2")

c1 = ConsoleObserver()
f1 = FileObserver()

devises = [t1, t2, h1, h2]
observers = [c1, f1]

# Подписываем наблюдателей на датчики
for device in devises:
    for observer in observers:
        device.add_observer(observer)

# Получаем значения датчиков
for device in devises:
    device.notify_observers(device.get_value())
