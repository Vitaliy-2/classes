film_one = {'Человек Паук', 'Армагеддон', "Плохой Санта", "Ирония судьбы, или С легким паром!", "Карнавал"}
film_two = {'Армагеддон', "Плохой Санта", "Один дома", "Морозко", "Карнавал"}
one_two = film_one | film_two
print(f'Список фильмов которые смотрел Я: {film_one}')
print(f'Список фильмов которые смотрел Друг: {film_two}')
print(f'Все уникальные фильмы которые вы смотрели: {set(one_two)}')
print(f'Все уникальные фильмы которые вы (оба) смотрели: {set(film_one & film_two)}')
print(f'Фильмы, которые смотрел только я: {set(film_one - film_two)}')
print(f'Фильмы, которые смотрел только Друг: {set(film_two - film_one)}')

films = {
    "Плохой Санта",
    "Гарри Поттер и философский камень",
    "Один дома",
    "Один дома 2: Затерянный в Нью-Йорке",
    "Ирония судьбы, или С легким паром!",
    "Морозко",
    "Новогодние приключения Маши и Вити",
    "Чародеи",
    "Новогодний экспресс",
    "Рождественская история",
    "Любовь нарасхват",
    "Карнавал",
    "Снежная королева",
    "Снегурочка",
    "Рождественская песнь",
    "Праздничный календарь",
    "Реальная любовь",
    "Эльф",
    "Рождество с Бевинсами",
    "Зимняя вишня",
    "Рождественские каникулы",
    "Каникулы строгого режима",
    "Джингл Беллс",
    "Рождественская история",
    "Скрюдж",
    "Праздник святого Валентина",
    "Приключения Святого Николаса",
    "Новогодний переполох",
    "Гринч – похититель Рождества",
}

import tabulate

table = [
    ["Имя", "Фамилия", "Возраст", "Должность", "Зарплата"],
    ["Иван", "Иванов", 20, "Python разработчик", 200000],
    ["Петр", "Петров", 30, "Java разработчик", 300000],
    ["Алексей", "Алексеев", 40, "C# разработчик", 400000],
]

print(tabulate.tabulate(table, tablefmt="heavy_grid"))
table_str = """

"""

print(table_str)

# Supported table formats are
#
# "plain"
# "simple"
# "github"
# "grid"
# "simple_grid"
# "rounded_grid"
# "heavy_grid"
# "mixed_grid"
# "double_grid"
# "fancy_grid"
# "outline"
# "simple_outline"
# "rounded_outline"
# "heavy_outline"
# "mixed_outline"
# "double_outline"
# "fancy_outline"
# "pipe"
# "orgtbl"
# "asciidoc"
# "jira"
# "presto"
# "pretty"
# "psql"
# "rst"
# "mediawiki"
# "moinmoin"
# "youtrack"
# "html"
# "unsafehtml"
# "latex"
# "latex_raw"
# "latex_booktabs"
# "latex_longtable"
# "textile"
# "tsv"
