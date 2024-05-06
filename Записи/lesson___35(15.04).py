"""
Lesson 35: Структурные паттерны
- повторение порождающих паттернов
- Abstract Factory - абстрактная фабрика
- Abstract Method - абстрактный метод
- Facade - фасад
- Adapter - адаптер
- Decorator - декоратор - повторили
- Proxy - заместитель
"""

import time
from dataclasses import dataclass
from abc import ABC, abstractmethod
from pprint import pprint
from typing import List

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


@dataclass
class Book:
    """
    Дата-класс для хранения информации о книге
    """
    title: str
    price: float
    rating: int
    img_url: str


# Абстрактный класс AbstractBrowser и конкретные классы ChromeBrowser и FirefoxBrowser

class AbstractBrowser(ABC):
    """
    Абстрактный класс для создания экземпляра браузера
    """
    implicit_wait = 10

    @abstractmethod
    def get_driver(self, driver_options: list = None):
        pass

    @abstractmethod
    def get_options(self, driver_options: list = None):
        pass


class ChromeBrowser(AbstractBrowser):
    """
    Конкретный класс для создания экземпляра браузера Chrome
    """

    def __init__(self):
        self.driver = None

    def get_options(self, driver_options: list = None):
        options = webdriver.ChromeOptions()
        if driver_options:
            for option in driver_options:
                options.add_argument(option)
        return options

    def get_driver(self, driver_options: list = None):
        options = self.get_options(driver_options)
        driver = webdriver.Chrome(options)
        driver.implicitly_wait(self.implicit_wait)
        self.driver = driver


class FirefoxBrowser(AbstractBrowser):
    """
    Конкретный класс для создания экземпляра браузера Firefox
    """

    def __init__(self):
        self.driver = None

    def get_options(self, driver_options: list = None):
        options = webdriver.FirefoxOptions()
        if driver_options:
            for option in driver_options:
                options.add_argument(option)
        return options

    def get_driver(self, driver_options: list = None):
        options = self.get_options(driver_options)
        driver = webdriver.Firefox(options)
        driver.implicitly_wait(self.implicit_wait)
        self.driver = driver


# Facade - управляющий класс, который спросит, какой браузер я хочу

class ParserFacede:
    def __init__(self):
        self.browser = None | AbstractBrowser

    def __call__(self):
        user_choise = input("Какой браузер использовать? Chrome или Firefox: ")
        if user_choise.lower() == "chrome":
            self.browser = ChromeBrowser()
        elif user_choise.lower() == "firefox":
            self.browser = FirefoxBrowser()
        else:
            print("Некорректный ввод")
            return

        self.browser.get_driver()
        self.browser.driver.get("http://books.toscrape.com/")
        time.sleep(10)


if __name__ == "__main__":
    facade = ParserFacede()
    facade()
