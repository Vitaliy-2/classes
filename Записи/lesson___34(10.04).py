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

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options


# Singleton - одиночка
# Гарантирует, что у класса есть только один экземпляр
# и предоставляет к нему глобальную точку доступа.

# Абстрактный простой пример

class Singleton:
    _instance = None  # Статическая переменная для хранения единственного экземпляра

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Использование Singleton
instance1 = Singleton()
instance2 = Singleton()

# Проверяем, являются ли эти экземпляры одним и тем же объектом
print(instance1 is instance2)  # True, это один и тот же экземпляр
print(id(instance1))
print(id(instance2))


# Пример Browser с webdriver (selenium)

class Browser:
    """
    Представляет веб-браузер с использованием паттерна Singleton.

    Аргументы:
        options_list (list): Список опций для настройки браузера.
    Атрибуты:
        options (webdriver.ChromeOptions): Настройки браузера.
        driver (webdriver.Chrome): Экземпляр драйвера браузера.
    """
    _instance = None  # Приватный атрибут для хранения единственного экземпляра

    # instance.options и instance.driver - добавляются в new,
    # потому что это классовые атрибуты, а не отдельных экземпляров
    def __new__(cls, options_list=[]):
        if cls._instance is None:
            cls._instance = super(Browser, cls).__new__(cls)
            # После создания экземпляра можно инициализировать атрибуты
            cls._instance.options = options_list
            cls._instance.driver = cls._instance.get_driver()
        return cls._instance

    def get_options_object(self):
        return Options()

    def set_options(self):
        options = self.get_options_object()
        for option in self.options:
            options.add_argument(option)
        return options

    def get_driver(self):
        options = self.set_options()
        # Имплицитное ожидание
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        return driver


# Использование Browser
browser1 = Browser(options_list=['--incognito'])
browser2 = Browser()
print(id(browser1))
print(id(browser2))
