"""
Lesson 30
27.03.2024
Class decorators
Meta classes
Вложенные классы
Итераторы
Теория сериализации и десериализации
Библиотека pickle
Практика pickle
"""


# Определим простой итератор для перебора чисел от 0 до заданного предела
class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit  # Максимальное значение для итерации
        self.value = 0  # Начальное значение счетчика

    # Метод __iter__ возвращает сам объект итератора
    def __iter__(self):
        return self

    # Метод __next__ возвращает следующее число и увеличивает счетчик
    # next()
    def __next__(self):
        if self.value < self.limit:
            current = self.value  # current - временная переменная куда попадает текущее значение
            self.value += 1
            return current
        else:
            # Когда достигнут предел, генерируется исключение StopIteration
            raise StopIteration


# Создадим итератор для чисел от 0 до 5
my_iterator = SimpleIterator(5)

# Используем итератор в цикле for для вывода чисел
for number in my_iterator:
    print(number)

# Делаем это через функцию iter() и next()

# Создадим итератор для чисел от 0 до 5
my_iterator = SimpleIterator(5)

# Получим объект итератора
iterator = iter(my_iterator)

# Получим следующее число
print(next(iterator))  # 0
print(next(iterator))  # 1
print(next(iterator))  # 2
