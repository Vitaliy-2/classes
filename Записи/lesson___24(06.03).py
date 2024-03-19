class BigMatryoshka:
    """
    Большая матрешка
    """
    count = 0

    def __init__(self, color):
        self.size = 'Большая'
        self.color = color
        __class__.count += 1
        self.id = BigMatryoshka.count

    def open(self):
        """
        Открывает матрешку
        :return:
        """
        print(f'{self.size} матрешка, цвет: {self.color} с ID {self.id} открывается')

    @classmethod
    def get_big_count(cls):
        return cls.count

    def __str__(self):
        """
        Печатает информацию о матрешке
        :return:
        """
        return f'Размер: {self.size}. Цвет: {self.color}, id: {self.id}'


class MediumMatryoshka(BigMatryoshka):
    """
    Средняя матрешка
    """
    def __init__(self, color):
        self.big_matryoshka = BigMatryoshka(color)
        super().__init__(color)
        self.size = 'Средняя'

    def open(self):
        """
        Открывает матрешку
        :return:
        """
        self.big_matryoshka.open()
        print(f'{self.size} матрешка, цвет: {self.color} с ID {self.id} открывается')


medium_matryoshka = MediumMatryoshka('Красный')
medium_matryoshka.open()
print(medium_matryoshka.get_big_count())
