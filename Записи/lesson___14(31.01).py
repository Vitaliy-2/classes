from pprint import pprint
from data.marvel import full_dict
print(full_dict)
# def count_avarage_mark(name='Владимир', surname='Монин', marks='marks'):
#     avarage_mark = round(sum(marks) / len(marks), 2)
#     return f'{name} {surname} имеет средний балл: {avarage_mark}.'
#
#
# func_params_dict = {
#     'name': 'Владимир',
#     'surname': 'Монин',
#     'marks': [4, 3, 3, 5, 5, 3, 5, 2]
# }
#
# print(count_avarage_mark(**func_params_dict))
user_result = {
    'name': 'Владимир',
    'surname': 'Монин',
    'marks': (5, 4, 4, 5)
}


# def count_avarage_mark(name, surname, marks):
#     marks = sum(marks) / len(marks)
#     return f'{name} {surname} имеет средний балл: {marks}'
#
#
# print(count_avarage_mark(**user_result))


def count_avarage_mark(**student):
    name = student.get('name')
    surname = student.get('surname')
    marks = student.get('marks')
    avarage_mark = sum(marks) / len(marks)

    return f'{name} {surname} имеет средний балл: {avarage_mark}'


print(count_avarage_mark(**user_result))


phase_dict = {
        1: 'Первая фаза',
        2: 'Вторая фаза',
        3: 'Третья фаза',
        4: 'Четвертая фаза',
        5: 'Пятая фаза',
        6: 'Шестая фаза',
    }

print(phase_dict.get(3))


def get_phase_name_by_number(phase_number: int) -> str | None:
    """
    Функция, которая принимает номер фазы и возвращает название фазы
    :param phase_number: Номер фазы
    :return: Название фазы
    """
    phase_dict = {
        1: 'Первая фаза',
        2: 'Вторая фаза',
        3: 'Третья фаза',
        4: 'Четвертая фаза',
        5: 'Пятая фаза',
        6: 'Шестая фаза',
    }

    return phase_dict.get(phase_number)


def get_movies_by_phase(phase_number: str, full_dict: dict) -> list:
    """
    Функция, которая принимает номер фазы и словарь marvel
    и возвращает список фильмов
    :param phase_number: Номер фазы
    :param full_dict: Словарь marvel
    :return: Список фильмов
    """
    # [movie['title'], movie['stage']
    if phase_number:
        return [f'{movie['title']}: {movie['stage']}' for movie in full_dict.values() if phase_number.lower() == movie['stage'].lower()]
    else:
        return []


def main():
    """
    Точка входа в программу
    :return: None
    """
    # 1. Чтение данных из JSON файла

    # 2. Получение номера фазы
    phase_number = int(input('Введите номер фазы: '))

    # 3. Расшифровка стадий (принимает номер стадии, возвращает название)
    phase_name = get_phase_name_by_number(phase_number)

    # 4. Поиск фильмов по стадии (принимает номер стадии, возвращает список фильмов)
    movies_list = get_movies_by_phase(phase_name, full_dict)

    # 5. Вывод результата
    print(f'Фаза: {phase_name}')
    pprint(movies_list)


if __name__ == '__main__':
    main()
