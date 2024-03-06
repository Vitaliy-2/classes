# Игра в города через функции
from typing import Set
import json

cities_json = 'cities.json'


def read_cities_from_json(file_path: str = cities_json) -> Set[str]:
    """
    Функция чтения сета городов из json файла
    :param file_path: Путь к файлу
    :return: Сет городов
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return set(data)


def get_unique_letters_set(cities_set: Set[str]) -> Set[str]:
    """
    Функция для получения сета уникальных букв, который используется
    при поиске плохих букв
    :param cities_set: Сет городов
    :return: Сет уникальных букв
    """
    return set(''.join(cities_set).lower())


def get_bad_letters_set(cities_set: Set[str], unique_letters_set: Set[str]) -> Set[str]:
    """
    Функция для получения сета плохих букв. Ищет буквы, с которых не начинается ни один
    город из сета городов
    :param cities_set: Сет городов
    :param unique_letters_set: Сет уникальных букв
    :return: Сет плохих букв
    """
    # Сет для добавления букв, с которых не может начинаться название города
    bad_letters_set = set()

    # Цикл выявления неподходящих букв, сравнивая с первой буквой в названии
    # Если совпадений нет, добавляем букву в сет
    for letter in unique_letters_set:
        for city in cities_set:
            if city[0].lower() == letter:
                break  # Если буква совпадает, останавливаем внутренний цикл и идем на след итерацию
        else:
            bad_letters_set.add(letter)
    return bad_letters_set


def is_last_letter_match(first_city: str, second_city: str) -> bool:
    """
    Функция проверяет, заканчивается ли первый город на последнюю букву второго города
    :param first_city: Первый город
    :param second_city: Второй город
    :return: True если последняя буква первого города совпадает с первой буквой второго города
    """
    return first_city[-1].lower() == second_city[0].lower()


def main() -> None:
    cities_set = read_cities_from_json()
    unique_letters_set = get_unique_letters_set(cities_set)
    bad_letters_set = get_bad_letters_set(cities_set, unique_letters_set)
    print(bad_letters_set)

    computer_city = None

    # Цикл игры
    while True:
        user_city = input('Ваш город: ').strip().title()
        # Остановка игры
        if user_city == 'стоп':
            print('Вы проиграли. Машина оказалась умнее.')
            break

        # Проверка, есть ли город в списке
        if user_city not in cities_set:
            print('Вы проиграли. Такого города нет.')
            break

        # Заглядываем в условие, если компьютер уже сделал свой ход, иначе пропускаем
        if computer_city:
            # Проверка на последнюю букву
            if not is_last_letter_match(computer_city, user_city):
                print('Вы проиграли. Город не на ту букву.')
                break

        # Если проверки выше пройдены, удаляем город из сета
        cities_set.remove(user_city)

        # Обновляем список плохих букв, учитывая использованные города
        bad_letters_set = get_bad_letters_set(cities_set, unique_letters_set)

        # Ход человека закончен, далее ход компьютера.
        # Компьютер перебирает города в сете
        for city in cities_set:
            # Если первая буква совпадает с последней буквой города человека, удаляем город из сета
            if is_last_letter_match(user_city, city):
                if city[-1].lower() in bad_letters_set:
                    continue
                cities_set.remove(city)
                print(f'Компьютер: {city}')
                # Записываем город компьютера в переменную
                computer_city = city
                break
            bad_letters_set = get_bad_letters_set(cities_set, unique_letters_set)
        # Если компьютер не нашел город, значит он проиграл
        else:
            print('Вы выиграли. Машина оказалась слабее.')
            break


if __name__ == '__main__':
    main()
