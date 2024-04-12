"""
Парсер в ООП стиле, для парсинга интернет-магазинов книг
Содерижт классы:

1. Browser - для работы с браузером (Python Selenium WebDriver)
2. AbstractParser - абстрактный класс для парсинга интернет-магазина
3. BookToScrapeParser - класс для парсинга интернет-магазина books.toscrape.com
4. Book - дата-класс для хранения информации о книге
5. DataSaver - класс для сохранения данных в файл
6. Контроллер - класс для управления парсером
"""

import json
import time
from dataclasses import dataclass
from abc import ABC, abstractmethod
from pprint import pprint
from typing import List

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Browser:
    """
    Класс для работы с браузером (Python Selenium WebDriver)
    """

    def __init__(self, driver_options: list = None):
        self.driver_options = driver_options
        self.driver = self.get_driver(self.driver_options)

    def get_driver(self, driver_options: list = None):
        """
        Создание драйвера с настройками.
        :param driver_options: Список строковых параметров для настройки драйвера.
        """
        options = webdriver.FirefoxOptions()
        if driver_options:
            for option in driver_options:
                options.add_argument(option)
        driver = webdriver.Firefox(options)
        driver.implicitly_wait(10)  # Устанавливаем неявное ожидание 10 секунд
        return driver


@dataclass
class Book:
    """
    Дата-класс для хранения информации о книге
    """
    title: str
    price: float
    rating: int
    img_url: str


class AbstractParser(ABC):
    """
    Абстрактный класс для парсинга интернет-магазина
    """

    def __init__(self, browser: Browser):
        self.browser = browser
        self.url = None
        self.books: List[Book] = []

    @abstractmethod
    def find_books_elements_on_page(self) -> List[WebElement]:
        """
        Поиск книги
        """
        pass

    @abstractmethod
    def get_one_book(self, book_element: WebElement) -> Book:
        """
        Получение информации о книге
        """
        pass

    @abstractmethod
    def get_all_book_from_page(self):
        """
        Получение информации о всех книгах на странице
        """
        pass

    @abstractmethod
    def get_all_by_category(self) -> List[str]:
        """
        Получение списка всех категорий
        """
        pass


class BookToScrapeParser(AbstractParser):
    """
    Класс для парсинга интернет-магазина books.toscrape.com
    """

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.url = "http://books.toscrape.com/index.html"
        self.driver = self.browser.driver
        self.book_marks = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5
        }

    def find_books_elements_on_page(self) -> List[WebElement]:
        """
        Поиск книги
        """
        return self.driver.find_elements(By.CLASS_NAME, "product_pod")

    def get_one_book(self, book_element: WebElement) -> Book:
        """
        Получение информации о книге
        """
        title = book_element.find_element(By.CSS_SELECTOR, "h3 > a").get_attribute("title")
        text_mark = \
            book_element.find_element(By.CSS_SELECTOR, "p[class^='star-rating']").get_attribute("class").split()[1]
        mark = self.book_marks.get(text_mark)
        price_str = book_element.find_element(By.CLASS_NAME, "price_color").text
        price = float(price_str.lstrip('£'))
        row_img_url = book_element.find_element(By.TAG_NAME, "img").get_attribute("src")
        img_url = f'{row_img_url.lstrip("..")}'

        return Book(title, price, mark, img_url)

    def get_all_book_from_page(self):
        """
        Получение информации о всех книгах на странице
        """
        books = self.find_books_elements_on_page()
        for book in books:
            self.books.append(self.get_one_book(book))

    def get_all_by_category(self) -> List[str]:
        """
        Получает ВСЕ книги со ВСЕХ страниц ОДНОЙ категории
        """
        self.driver.get(self.url)
        result = []
        while True:
            self.get_all_book_from_page()
            try:
                next_page = self.driver.find_element(By.LINK_TEXT, "next")
                next_page.click()
                time.sleep(1)

            except NoSuchElementException:
                break

        return result


class Controller:
    """
    Класс для управления парсером
    """

    def __init__(self):
        self.parser = None

    def start(self):
        """
        Запуск парсера
        """
        self.parser.get_all_by_category()
        pprint(self.parser.books)

    def __call__(self, parser: AbstractParser):
        self.parser = parser
        self.start()


# Создаем экземпляр драйвера
browser = Browser()
# Создаем экземпляр парсера
parser = BookToScrapeParser(browser)
# Создаем экземпляр контроллера
controller = Controller()
# Запускаем парсер
controller(parser)


def run_parser(parser_class, browser_options):
    browser = Browser(driver_options=browser_options)
    parser = parser_class(browser)
    parser.get_all_by_category()
    # Здесь может быть код для сохранения результатов парсинга
    print(parser.books)


from multiprocessing import Process

if __name__ == '__main__':

    # Создаем процессы
    processes = []
    for parser_class, browser_options in [
        (BookToScrapeParser, None),
        (BookToScrapeParser, None)
    ]:
        p = Process(target=run_parser, args=(parser_class, browser_options))
        processes.append(p)

    # Запускаем процессы
    for p in processes:
        p.start()

    # Ждем завершения всех процессов
    for p in processes:
        p.join()
