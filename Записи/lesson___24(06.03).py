"""
Чтобы сделать это действительно абстрактным,
на нужно использовать ABC - Abstract Base Class и декоратор @abstractmethod.

ABC - это класс, который не может быть инсталлирован (из него нельзя создать экземпляр).

@abstractmethod - это декоратор, который указывает, что метод должен быть реализован
в дочерних классах

ABC - нужно, чтобы другие разработчики явно понимали, что точно должно наследоваться
у наследников.

- __base__ - ссылка на родительский класс
- isubclass() - проверка наследования
- isinstance() - проверка принадлежности к классу
"""
from abc import ABC, abstractmethod


class AbstractMatryoshka(ABC):
    """
    Абстрактный класс Матрешка.
    Тут может быть реализовано общее поведение для всех матрешек
    """
    count = 0

    def __init__(self):
        self.size = None
        self.color = None
        __class__.count += 1
        self.id = __class__.count

    @abstractmethod  # Означает, кто в каждом наследнике должен быть описан метод open
    def open(self):
        """
        Открывает матрешку
        :return:
        """
        print(f'{self.size} матрешка, цвет: {self.color} с ID {self.id} открывается')

    @classmethod
    def get_count(cls):
        return cls.count

    def __str__(self):
        """
        Печатает информацию о матрешке
        :return:
        """
        return f'Размер: {self.size}. Цвет: {self.color}, id: {self.id}'


class BigMatryoshka(AbstractMatryoshka):
    """
    Большая матрешка
    """

    def __init__(self, color):
        super().__init__()
        self.size = 'Большая'
        self.color = color

    def open(self):
        print(f'{self.size} матрешка, цвет: {self.color} с ID {self.id} открывается')


class MediumMatryoshka(AbstractMatryoshka):
    """
    Большая матрешка
    """

    def __init__(self, color):
        super().__init__()
        self.size = 'Средняя'
        self.color = color

    def open(self):
        super().open()


class SmallMatryoshka(AbstractMatryoshka):
    """
    Большая матрешка
    """

    def __init__(self, color):
        super().__init__()
        self.size = 'Маленькая'
        self.color = color

    def open(self):
        super().open()


big = BigMatryoshka('Красный')
big.open()
print(big)
medium = MediumMatryoshka('Синий')
medium.open()
print(medium)
small = SmallMatryoshka('Желтый')
small.open()
print(small)


# big.display_info()


class GlassMatryoshkaMixin:
    """
    Миксин для стеклянной матрешки
    """

    def __init__(self):
        self.material = 'Стекло'


class BigGlassMatryoshka(BigMatryoshka, GlassMatryoshkaMixin):
    """
    Большая стеклянная матрешка
    """

    def __init__(self, color):
        super().__init__(color)

    def open(self):
        print('Большая стеклянная матрешка открывается')


glass_matryoshka = BigGlassMatryoshka('Красный')
glass_matryoshka.open()

print(BigGlassMatryoshka.mro())
