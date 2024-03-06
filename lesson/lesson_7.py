"""
Lesson 14
- set
- set comprehension
- while else
- методы сетов
- практика
- tuple - кортеж
- tabulate - таблицы pip install tabulate
https://pypi.org/project/tabulate/ - документация
- set comprehension
- tuple comprehension - не существует! (это генератор)
- методы кортежей))
- исключения
"""
import random

persons_list = ['Папа', 'Мама', 'Сын',
                'Дочь', 'Бабушка', 'Дедушка',
                'Кот', 'Собака', 'Попугай', 'Хомяк', 'Рыбки']

gifts_list = ['Шоколадка', 'Плейстешн 5', 'Фен Дайсон', 'Айфон', 'Киндер', 'Книжка',
              'Видеокарта', 'Ноутбук', 'Электрическая бритва', 'Корм для рыбок', 'Кошачьи вкусняшки']

max_gifts = len(persons_list) * len(gifts_list)
print(max_gifts)

# set - множество уникальных строк (Даритель дарит подарок: Подарок)
gifts_set = set()

input = int(input('Сколько подарочков вы хотите получить? '))
try_count = 0

while len(gifts_set) < input and len(gifts_set) < max_gifts:
    try_count += 1
    print(f'Попытка №{try_count}')
    # Добываем рандомного дарителя через рандом choice
    person = random.choice(persons_list)
    # Добываем рандомный подарок через рандом choice
    gift = random.choice(gifts_list)

    # Добавляем в множество
    gifts_set.add(f'{person} дарит {gift}')

print(gifts_set)
print(f'Попыток: {try_count}')
print(len(gifts_set))

# Сеты - множества
# set - неупорядоченная изменяемая коллекция уникальных элементов
# элементами множества могут быть только неизменяемые объекты
# это могут быть только строки, числа, кортежи, bool, None
# set - это хеш таблица, где хранятся только ключи

a = {1, "", (1, 2, 3), True, None}
# b = {[2], 2}
# print(b)

# Методы сетов
# add - добавляет элемент в множество
# clear - очищает множество
# remove - удаляет элемент из множества, если его нет, то выдает ошибку
# discard - удаляет элемент из множества, если его нет, то ничего не делает
# copy - возвращает копию множества
# update - добавляет в множество все элементы из другого множества
# union - возвращает объединение множеств - оператор |
# pop - возвращает и удаляет рандомный элемент множества
# difference - возвращает разницу множеств - оператор - (минус)
# intersection - возвращает пересечение множеств - оператор &
# symmetric_difference - возвращает симметричную разность множеств - оператор ^
# intersection_update - удаляет из множества все элементы, которые не входят в другое множество
# isdisjoint - возвращает True, если множества не имеют общих элементов
# issubset - возвращает True, если одно множество является подмножеством другого
# issuperset - возвращает True, если одно множество является надмножеством другого
# symmetric_difference_update - удаляет из множества все элементы, которые есть в другом множестве,
# а также добавляет все элементы из другого множества, которых нет в текущем
# difference_update - удаляет из множества все элементы, которые есть в другом множестве


# Todo Практика
"""
Вы встретились с подругой (другом) и за бутылкой коньяка решили вспомнить
все новогодние фильмы которые вы смотрели.

Создайте два множества с названиями фильмов.

Получите и выведите на экран названия следующих фильмов:
- уникальные названия ВСЕХ фильмов СУММАРНО. Метод: union
- названия фильмов которые вы (вы оба) смотрели ВМЕСТЕ (пересечение). Метод: intersection
- названия фильмов которые вы смотрели, но ваш друг (подруга) нет (разность). Метод: difference
- названия фильмов которые ваш друг (подруга) смотрел(а), но вы нет (разность). Метод: difference
- названия фильмов которые вы смотрели но ваш друг (подруга) нет и наоборот (симметричная разность). Метод: symmetric_difference
"""

films = {
    "Плохой Санта",
    "Плохой Санта 2",
    "Гарри Поттер и философский камень",
    "Гарри Поттер и тайная комната",
    "Один дома",
    "Один дома 2: Затерянный в Нью-Йорке",
}
films2 = {
    "Плохой Санта",
    "Гарри Поттер и философский камень",
    "Новый год, мальчики!",
    "В поисках Санты",
    "Кошмар перед Рождеством",
    "Один дома",
    "Один дома 2: Затерянный в Нью-Йорке",
    "Один дома 3",
}

print(f'Все фильмы: {films.union(films2)}')
print(f'Смотрели вместе: {films.intersection(films2)}')
print(f'Смотрел, но друг нет: {films.difference(films2)}')
print(f'Друг смотрел, но я нет: {films2.difference(films)}')
print(f'Смотрел один из нас: {films.symmetric_difference(films2)}')

# Tabulate - таблицы.
import tabulate

table = [
    ["Имя", "Фамилия", "Возраст", "Должность", "Зарплата"],
    ["Иван", "Иванов", 20, "Python middle разработчик", 180000],
    ["Петр", "Петров", 30, "Java middle разработчик", 200000],
    ["Алексей", "Алексеев", 40, "C# middle разработчик", 150000],
]

table_html_str = tabulate.tabulate(table, tablefmt="html")
table_bs5_style = table_html_str.replace('<table>', '<table class="table table-striped">')

table_str = f"""
<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  </head>
  <body>
    <h1>Отчет по сотрудникам</h1>
    {table_bs5_style}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
  </body>
</html>
"""

with open("table.html", "w", encoding="utf-8") as file:
    file.write(table_str)

# Tuple - кортеж
# tuple - неизменяемая упорядоченная коллекция объектов
# tuple - это список, который нельзя изменять

# методы кортежей
# Сложение кортежей - возвращает новый кортеж
# Умножение кортежей - возвращает новый кортеж
# in - проверяет наличие элемента в кортеже
# not in - проверяет отсутствие элемента в кортеже
# срезы - возвращает новый кортеж
# count - возвращает количество элементов в кортеже
# index - возвращает индекс элемента
# len - возвращает длину кортежа
# max - возвращает максимальный элемент
# min - возвращает минимальный элемент
# sum - возвращает сумму элементов

some_float = 1, 5, "Hello", 3.14, True, None, [1, 2, 3], (1, 2, 3)
print(type(some_float))
print(some_float)


table = [
    ["Имя", "Фамилия", "Возраст", "Должность", "Зарплата"],
    ["Иван", "Иванов", 20, "Python middle разработчик", 180000],
    ["Петр", "Петров", 30, "Java middle разработчик", 200000],
    ["Алексей", "Алексеев", 40, "C# middle разработчик", 150000],
    ["Николай", "Алексеев", 24, "C++ middle разработчик", 145000],
]

# set comprehension
# {expression for item in iterable if condition}

names = {row[1].upper() for row in table if row[1].endswith("ов")}
names_lst = [row[1].lower() for row in table if row[1].endswith("ов")]
print(names)
print(names_lst)

# Exception - исключения
# try:
#     блок кода, который может вызвать ошибку
# except Exception as e:
#     блок кода, который выполняется при ошибке
# else:
#     блок кода, который выполняется при отсутствии ошибки
# finally:
#     блок кода, который выполняется в любом случае

# raise - вызов исключения

"""
Цикл while true в котором мы запрашиваем 2 числа и потом делим их друг на друга.
"""

while True:
    a = 2
    b = 0

    if b == 0:
        raise ZeroDivisionError("На ноль делить нельзя!")
    try:
        print(a / b)
        break
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
        break
    except ValueError:
        print("Вы ввели не число!")
        break
    except Exception as e:
        print("Что-то пошло не так!")
        print(e)
    finally:
        print("Это finally блок")