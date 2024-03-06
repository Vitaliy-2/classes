# Игра в города

from data.cities import cities_list

# Создаем сет со всеми городами
cities = set()
# Цикл извлечения названия города из словаря и добавление его в сет
for city_dict in cities_list:
    city = city_dict["name"].title()
    cities.add(city)
print(cities)

# Выявляем все уникальные буквы и символы
unique_letters_set = set(''.join(cities).lower())

# Сет для добавления букв, с которых не может начинаться название города
bad_letters_set = set()

# Цикл выявления неподходящих букв, сравнивая с первой буквой в названии
# Если совпадений нет, добавляем букву в сет
for letter in unique_letters_set:
    for city in cities:
        if city[0].lower() == letter:
            break  # Если буква совпадает, останавливаем внутренний цикл и идем на след итерацию
    else:
        bad_letters_set.add(letter)
print(bad_letters_set)

# Переменная для записи города компьютера
computer_city = None

# Цикл игры
while True:
    user_city = input('Ваш город: ').strip().title()
    # Остановка игры
    if user_city == 'стоп':
        print('Вы проиграли. Машина оказалась умнее.')
        break

    # Проверка, есть ли город в списке
    if user_city not in cities:
        print('Вы проиграли. Такого города нет.')
        break

    # Заглядываем в условие, если компьютер уже сделал свой ход, иначе пропускаем
    if computer_city:
        # Проверка на последнюю букву
        if user_city[0].lower() != computer_city[-1].lower():
            print('Вы проиграли. Город не на ту букву.')
            break

    # Если проверки выше пройдены, удаляем город из сета
    cities.remove(user_city)

    # Еще раз проходимся циклами для нахождения неподходящих букв (например: "Й")
    for letter in unique_letters_set:
        for city in cities:
            if city[0].lower() == letter:
                break  # Если буква совпадает, останавливаем внутренний цикл и идем на след итерацию
        else:
            bad_letters_set.add(letter)  # Обновляем сет с неподходящими буквами


    # Ход человека закончен, далее ход компьютера
    # Опираемся на последнюю букву пользовательского города
    last_user_letter = user_city[-1]

    # Компьютер перебирает города в сете
    for city in cities:
        # Если первая буква совпадает с последней буквой города человека, удаляем город из сета
        if city[0].lower() == last_user_letter:
            if city[-1].lower() in bad_letters_set:
                continue
            cities.remove(city)
            print(f'Компьютер: {city}')
            # Записываем город компьютера в переменную
            computer_city = city
            break
    # Если компьютер не нашел город, значит он проиграл
    else:
        print('Вы выиграли. Машина оказалась слабее.')
        break