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


"""
Практика!

1. Напишите абстрактный класс SecretFile с абстрактными методами 
open и close.

2. Напишите конкретный класс SecretImage и SecretVideo
наследующиеся от SecretFile.

3. Напишите класс SecretFileProxy, который будет замещать любой из них, и запрашивать пароль.
Пароль будет записан в фасаде.

4. Напишите класс FBISecretFacade, который будет хранить пароль и
будет call 

При его вызове, пользователю предложат посмотреть фото или видео секретных материалов.
После выбра, будет создан экземпляр SecretImage или SecretVideo, а так же SecretFileProxy.

5. Пользователь вводит пароль, если пароль верный, то открывается файл, если нет, то выводится сообщение об ошибке.
"""


class SecretFile(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass


@dataclass
class SecretImage(SecretFile):
    """
    Совершенно секретное изображение
    """
    data: str
    password: str = "1234"

    def open(self):
        print(f"На данном снимке изображено: {self.data}")

    def close(self):
        print("Закрытие изображения")


@dataclass
class SecretVideo(SecretFile):
    """
    Совершенно секретное видео
    """
    data: str
    password: str = "1234"

    def open(self):
        print(f"На данном видео изображено: {self.data}")

    def close(self):
        print("Закрытие видео")


class SecretFileProxy(SecretFile):
    def __init__(self, secret_file: SecretFile):
        self.secret_file = secret_file
        self.password = secret_file.password

    def open(self):
        password = input("Введите пароль: ")
        if password == self.password:
            self.secret_file.open()
        else:
            print("Неверный пароль, люди в черном уже в пути!")

    def close(self):
        self.secret_file.close()


class FBISecretFacade:
    """
    Фасад для работы с секретными файлами
    """
    def __init__(self):
        self.secret_file: SecretFile | None = None
        self.secret_file_proxy: SecretFileProxy | None = None

    def __call__(self):
        file_type = input("Выберите тип файла (image/video): ")
        if file_type == "image":
            self.secret_file = SecretImage("Секретное изображение Чупакабры")
        elif file_type == "video":
            self.secret_file = SecretVideo("Секретное видео Йетти")
        else:
            raise ValueError("Неверный тип файла")

        self.secret_file_proxy = SecretFileProxy(self.secret_file)
        self.secret_file_proxy.open()
        self.secret_file_proxy.close()


# Пример использования
if __name__ == "__main__":
    fbi_facade = FBISecretFacade()
    fbi_facade()
