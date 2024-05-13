"""
Lesson 36: Поведенческие паттерны
- Strategy - стратегия
- Observer - наблюдатель
- Visitor - посетитель
- State - состояние
"""

# State - состояние.

"""
1. Класс создающий экземплер Браузера
2. Класс контекст состояний
3. Класс сосстояния, в котором браузер идет на сайт book.toscrape.com
4. Класс сосстояния, в котором браузер идет на сайт Гугл
5. Фасад для управления состояниями и получения задачи от пользователя __call__
"""

from abc import ABC, abstractmethod
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Chrome:
    """
    Singleton класс для создания экземпляра браузера Chrome
    """
    _instance = None

    def __new__(cls, settings=None, implicity_wait=10):
        if cls._instance is None:
            cls._instance = super(Chrome, cls).__new__(cls)
            cls._instance.settings = settings
            cls._instance.implicity_wait = implicity_wait
        return cls._instance

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
        Создание и получение драйвера Chrome
        """
        options = self.get_options_object()
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(self.implicity_wait)
        return driver


class Browser:
    def __init__(self, driver):
        self.state = None
        self.driver = driver

    def change_state(self, state: 'State'):
        self.state = state

    def work(self):
        self.state.work(self.driver)


class State(ABC):
    @abstractmethod
    def work(self, driver):
        pass


class BookToscrapeState(State):
    def work(self, driver):
        driver.get("http://books.toscrape.com")
        time.sleep(5)


class GoogleState(State):
    def work(self, driver):
        driver.get("http://google.com")
        search_form = driver.find_element(By.CSS_SELECTOR, "textarea[name='q']")
        search_form.send_keys("Котики")
        search_form.submit()


class MainFacade:
    def __init__(self):
        self.driver = Chrome().get_driver()
        self.browser = Browser(self.driver)

    def __call__(self):
        while True:
            print("1. Перейти на сайт book.toscrape.com")
            print("2. Перейти на сайт Гугл")
            print("3. Выход")
            choice = input("Выберите действие: ")
            if choice == "1":
                self.browser.change_state(BookToscrapeState())
                self.browser.work()
            elif choice == "2":
                self.browser.change_state(GoogleState())
                self.browser.work()
            elif choice == "3":
                break
            else:
                print("Неверный выбор")


# Пример использования
facade = MainFacade()
facade()
