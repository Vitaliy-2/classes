"""
`NotImplemented` – специальное значение, которое можно вернуть из
метода сравнения в случае, когда сравнение между операндами невозможно, как описано выше.

`NotImplementedError` – это исключение, которое возникает, когда
абстрактный метод должен быть имплементирован классом-наследником,
 если класс_MIXIN не поддерживает этот метод, то должно быть явно указано это
 через `NotImplementedError`, однако используется он для понятия ошибки разработки
 не тестирования доступности метода сравнения разных типов объектов.


Как это работает с наследованием?

@total_ordering - декоратор, который позволяет определить все методы сравнения
Нам надо определить метод проверки на равенство
И один из методов сравнения: меньше, меньше или равно, больше, больше или равно

__call__ - вызов объекта как функции


Как это работает с наследованием?

@total_ordering - декоратор, который позволяет определить все методы сравнения
Нам надо определить метод проверки на равенство
И один из методов сравнения: меньше, меньше или равно, больше, больше или равно
Не нужно описывать методы, а только два.

__call__ - вызов объекта как функции

"""
from functools import total_ordering


@total_ordering
class Kettlebell:
    """
    Гиря
    """

    def __init__(self, weight, length=40, width=10):
        self.weight = weight
        self.length = length
        self.width = width

    def __str__(self) -> str:
        return f'Гиря весом {self.weight} кг'

    def __bool__(self) -> bool:
        return self.weight > 0

    def __len__(self) -> int:
        return self.length

    def __eq__(self, other: 'Kettlebell') -> bool:  # other - другой экземпляр этого класса
        """
        Равенство
        :param other:
        :return:
        """
        # Проверка на принадлежность к классу
        if not isinstance(other, Kettlebell):
            return NotImplemented
        return self.weight == other.weight

    def __lt__(self, other: 'Kettlebell') -> bool:
        """
        Меньше
        :param other:
        :return:
        """
        if not isinstance(other, Kettlebell):
            return NotImplemented
        return self.weight < other.weight


class Dumbbells:
    def __eq__(self, other):
        return NotImplemented
    pass


# ket1 = Kettlebell(16, 45, 11)
# print(ket1)
# if ket1:
#     print('Гиря настоящая')
#
# print(len(ket1))
#
# ket2 = Kettlebell(16)
# ket3 = Kettlebell(24)
#
# print(ket1 == ket2)
# print(ket1 != ket2)
#
# print(ket1 < ket2)
# print(ket1 <= ket2)
#
# print(ket1 > ket2)
# print(ket1 >= ket2)
#
#
# dumb1 = Dumbbells()
#
# # print(ket1 == dumb1)
#
# ket4 = Kettlebell(36)
# ket5 = Kettlebell(42)
#
# ket_list = [ket5, ket1, ket3, ket2, ket4]
# ket_list.sort(reverse=True)
# [print(k) for k in ket_list]

# Практика

@total_ordering
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f'Город: {self.name}, Население: {self.population}'

    def __eq__(self, other: 'City') -> bool:  # other - другой экземпляр этого класса
        if not isinstance(other, City):
            return NotImplemented
        return self.population == other.population

    def __lt__(self, other: 'City') -> bool:
        if not isinstance(other, City):
            return NotImplemented
        return self.population < other.population


city1 = City('Москва', 15000000)
city2 = City('Санкт-Петербург', 11000000)
city3 = City('Екатеринбург', 8000000)
city4 = City('Самара', 4000000)
city5 = City('Петрозаводск', 350000)

print(f'Сравнение на "равенство" Москвы и Питера: {city1 == city2}')
print(f'Сравнение на "неравенство" Самары и Петрозаводска: {city4 != city5}')

print(f'Сравнение на "больше" Москвы и Питера: {city1 > city2}')
print(f'Сравнение на "меньше" Екатеринбурга и Петрозаводска: {city3 < city5}')

print(f'Сравнение на "больше и равно" Москвы и Екатеринбурга: {city1 >= city3}')
print(f'Сравнение на "меньше и равно" Питера и Самары: {city2 <= city4}')

city_list = [city2, city5, city1, city4, city3]
city_list.sort()
[print(city) for city in city_list]
