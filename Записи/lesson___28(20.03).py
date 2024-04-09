"""
Lesson 28
20.03.2024
ООП
Selenium webdriver
# Установка selenium - pip install selenium

webdriver - прослойка между нами и браузером

# NoSuchElementException - исключение, которое возникает, когда элемент не найден


# Поиск элементв на странице с помощью объекта By
# find_element_by_id
# find_element(By.ID, "id")

# Какие варианты есть в By?
# By.ID
# By.NAME
# By.TAG_NAME
# By.CLASS_NAME
# By.LINK_TEXT
# By.PARTIAL_LINK_TEXT
# By.XPATH
# By.CSS_SELECTOR
"""
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# # Создаем экземпляр драйвера
driver = webdriver.Firefox()

# Переходим на сайт
driver.get("https://www.google.com/")
# скриншот страницы
# driver.save_screenshot("google.png")
time.sleep(2)
# Закрываем браузер
# driver.quit()


# Поиск элементов на странице
# find_element_dy_id - устарелая система

# Поиск элементов на странице с помощью объекта By
# find_element(By.ID, 'id')

# Какие варианты есть в BY?
# By.ID
# By.NAME
# By.TAG_NAME
# By.CLASS_NAME
# By.LINK_TEXT
# By.PARTIAL_LINK_TEXT
# By.XPATH
# By.CSS_SELECTOR

# Ищем по CSS textarea аттрибут title='Поиск'
search_input = driver.find_element(By.CSS_SELECTOR, 'textarea[title="Поиск"]')

# Ввожу соообщение
message = "Привет группа!"
search_input.send_keys(message)

# Нажмем enter через клавиатуру (KEYS)
search_input.submit()
# search_input.send_keys(webdriver.common.keys.Keys.ENTER)
time.sleep(5)

