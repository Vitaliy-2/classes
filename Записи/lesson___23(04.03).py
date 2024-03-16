class Animal:
    def __init__(self, name='Бобик', age=0, paws=0):
        self.name = name
        self.age = 0
        self.paws = 0

    def speak(self, type_of_animal='животное'):
        print(f'В первую очередь я {__class__.__name__}, а потом {type_of_animal} ')

    def __str__(self):
        return f'Animal: {self.name, self.age}'


class Dog(Animal):

    def speak(self):
        print(f'My name is {self.name} and I am a dog.')


class Cat(Animal):
    """
    Расширим атрибуты у кота, добавим пушистость
    """

    def __init__(self, name, fluffiness, age, paws):
        super().__init__(name, age, paws)
        self.fluffiness = fluffiness

    def speak(self):
        # Вызов метода родительского класса
        class_name = self.__class__.__name__
        super().speak(class_name)
        print(f'My name is {self.name} and I am a cat.')


class Bird(Animal):
    def speak(self):
        print(f'My name is {self.name} and I am a bird.')


# dog = Dog('Рекс')
# cat = Cat('Мурзик', 5, 3, 4)
# bird = Bird('Чижик')
# print(cat)
# dog.speak()
# cat.speak()
# bird.speak()

# animal = Animal()
# animal.speak()
#
# cat = Cat('Мурзик', 5, 3, 4)
# cat.speak()

#
# # mro - показывает как в пайтоне идет цепь наследования
# print(Dog.mro())
#
# animals = [dog, cat, bird]
#
# for animal in animals:
#     animal.speak()
#
# [animal.speak() for animal in animals]

"""
Полиморфизм - это способность объектов с одинаковым интерфейсом иметь различную реализацию
Мы можем вызвать метод speak у всех объектов, но каждый из них будет вести себя по-разному
Даже логика может быть разной, главное чтобы интерфейс был одинаковым, и ожидался одинаковый результат
"""

"""
Наследование Cat работает и без вызова инициализатора родительского класса
Мы получаем методы Animal, но не получаем атрибуты!

А в них может быть логика, которая необходима для работы дочернего класса
"""

"""
Мы можем переопределить методы родительского класса в дочернем классе
Но при этом мы можем и расширить функционал родительского метода, в дочернем, добавив новую логику
"""


class BigMatryoshka:
    def __init__(self):
        self.size = 'Большая'

    def open(self):
        print('Большая матрешка открывается')


class MediumMatryoshka(BigMatryoshka):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def open(self):
        super().open()
        print('Средняя матрешка открывается')

    def display_info(self):
        print(f'Размер: {self.size}. Цвет: {self.color}')


big_matryoshka = BigMatryoshka()
big_matryoshka.open()

medium_matryoshka = MediumMatryoshka('Красная')
medium_matryoshka.open()

medium_matryoshka.display_info()

