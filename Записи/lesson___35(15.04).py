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

from dataclasses import dataclass, field
from abc import ABC, abstractmethod

# Proxy - заместитель
# Паттерн Proxy предоставляет объект-заместитель или заполнитель для другого объекта, чтобы контролировать доступ к нему.

"""
Напишем простой пример с использованием паттерна Proxy.
Асбтрактный класс Документ, который имеет метод открыть и закрыть документ.
А так же класс ProxyDocument, который является заместителем для класса Document.
"""


class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass


@dataclass
class SecretDocument(Document):
    secret: str

    def open(self):
        print("Открываем секретный документ")

    def close(self):
        print("Закрываем секретный документ")


@dataclass
class ProxyDocument(Document):
    def __post_init__(self):
        self.secret_document = SecretDocument(secret="Секретный текст")

    def open(self):
        password = input("Введите пароль: ")
        if password == "123":
            self.secret_document.open()

    def close(self):
        self.secret_document.close()
