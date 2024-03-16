class BigMatryoshka:
    """
    Большая матрешка
    """

    def __init__(self, color):
        self.size = 'Большая'
        self.color = color

    def open(self):
        """
        Открывает матрешку
        :return:
        """
        print(f'{self.size} матрешка {self.color} цвета: открывается')

    def __str__(self):
        """
        Печатает информацию о матрешке
        :return:
        """
        print(f'Размер: {self.size}. Цвет: {self.color}')


class MediumMatryoshka(BigMatryoshka):
    def __init__(self, color):
        super().__init__(color)
        self.size = 'Средняя'


big_matryoshka = BigMatryoshka('Зеленая')
big_matryoshka.open()

medium_matryoshka = MediumMatryoshka('Красная')
medium_matryoshka.open()
