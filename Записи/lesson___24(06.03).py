class BigMatryoshka:
    """
    Большая матрешка
    """
    big_count = 0

    def __init__(self, color):
        self.size = 'Большая'
        self.color = color
        BigMatryoshka.big_count += 1
        self.id = BigMatryoshka.big_count

    def open(self):
        """
        Открывает матрешку
        :return:
        """
        print(f'{self.size} матрешка, цвет: {self.color} с ID {self.id} открывается')

    @classmethod
    def get_big_count(cls):
        return cls.big_count

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
        super().__init__(color)
        self.big_matryoshka = BigMatryoshka(color)
        self.size = 'Средняя'

    def open(self):
        """
        Открывает матрешку
        :return:
        """
        self.big_matryoshka.open()
        print(f'{self.size} матрешка {self.color} цвета: открывается')


# medium_matryoshka = MediumMatryoshka('Красный')
# medium_matryoshka2 = MediumMatryoshka('Синий')
# medium_matryoshka3 = MediumMatryoshka('Зеленый')
# medium_matryoshka.open()
# medium_matryoshka2.open()
# medium_matryoshka3.open()

big_matryoshka = BigMatryoshka('Красный')
# print(big_matryoshka)
print(big_matryoshka.get_big_count())

big_matryoshka2 = BigMatryoshka('Синий')
big_matryoshka3 = BigMatryoshka('Зеленый')

# Счетчик, который показывает сколько сделано матрешек на данный момент
print(big_matryoshka.get_big_count())
print(big_matryoshka)
print(big_matryoshka2)
print(big_matryoshka3)
