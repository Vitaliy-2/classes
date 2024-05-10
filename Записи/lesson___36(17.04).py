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
import time
from dataclasses import dataclass
from abc import ABC, abstractmethod
from pprint import pprint
from typing import List

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AbstractBrowserStrategy(ABC):
    """
    Абстрактный класс стратегии браузера
    """

    def __init__(self, settings: List[str]):
        self.settings = settings
        self.implicity_wait = 10

    @abstractmethod
    def get_options_object(self):
        pass

    @abstractmethod
    def get_driver(self):
        pass


class ChromeBrowserStrategy(AbstractBrowserStrategy):
    """
    Конкретная стратегия для браузера Chrome
    """

    def get_options_object(self):
        """
        Получение объекта настроек для Chrome
        """
        options = webdriver.ChromeOptions()
        if self.settings:
            for option in self.settings:
                options.add_argument(option)
        return options

    def get_driver(self):
        """
        Получение драйвера для Chrome
        """
        options = self.get_options_object()
        driver = webdriver.Chrome(options)
        driver.implicitly_wait(self.implicity_wait)
        return driver


class FirefoxBrowserStrategy(AbstractBrowserStrategy):
    """
    Конкретная стратегия для браузера Firefox
    """

    def get_options_object(self):
        """
        Получение объекта настроек для Firefox
        """
        options = webdriver.FirefoxOptions()
        if self.settings:
            for option in self.settings:
                options.add_argument(option)
        return options

    def get_driver(self):
        """
        Получение драйвера для Firefox
        """
        options = self.get_options_object()
        driver = webdriver.Firefox(options)
        driver.implicitly_wait(self.implicity_wait)
        return driver


class Browser:
    """
    Класс - контекст для работы с одним из стратегий-браузеров
    """

    def __init__(self):
        self.strategy = FirefoxBrowserStrategy([])

    def set_strategy(self, strategy: AbstractBrowserStrategy):
        """
        Установка стратегии
        """
        self.strategy = strategy

    def get_driver(self):
        """
        Получение драйвера
        """
        return self.strategy.get_driver()


def main():
    browser = Browser()  # Экземпляр контекста
    browser.set_strategy(FirefoxBrowserStrategy(["--incognito"]))  # Установка стратегии
    driver = browser.get_driver()  # Заставил контекст выполнить действие

    # Использую результат действия
    driver.get("https://google.com")
    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    main()
