class AbstractMatryoshka:
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
medium = MediumMatryoshka('Синий')
medium.open()
small = SmallMatryoshka('Желтый')
small.open()

# big.display_info()
