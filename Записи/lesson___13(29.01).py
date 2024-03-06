# def get_message(name, message, age):
#     return f'Имя: {name}.\nСообщение: {message}.\nВозраст: {age}'
#
#
# print(get_message('Колян', 'Привет', 27))
# print(get_message(name='Иван', message='Пока', age=29))

# dict_ = dict(cities_list)


# def get_cities_set(cities_list):
#     return {city['name'] for city in cities_list}
#
#
# result = get_cities_set(cities_list)
# print(result)

# palindrome = ('шалаш', 'казак', 'мельница')
#
#
# def is_palindrome(*palindrome):
#     result = dict()
#     for word in palindrome:
#         result[word] = word == word[::-1]
#     return result
#     # if palindrome == palindrome[::-1]:
#     #     qwerty.update(dict(palindrome='true'))
#     # else:
#     #     qwerty.update(dict(palindrome='false'))
#     # return qwerty
#
#
# print(is_palindrome(*palindrome))


from data.cities import cities_list
from typing import List, Dict
qwerty = cities_list


def get_cities_set(city_dict: List[Dict]):
    return {city['name'] for city in city_dict}


print(get_cities_set(cities_list))

list_sum = [1, 2, 4, 6, 7]


def sum_args(*args):
    return sum(args)


print(sum_args(*list_sum))
print(list_sum)
print(*list_sum)
qwer = [sym**2 for sym in list_sum]
print(qwer)

palindrom = ['Казак', 'привет', 'шалаш', 'кино', 'дед']


# def is_palindrome(*palindrome):
#     return {word: word == word[::-1] for word in palindrome}
#
#
# print(is_palindrome(*palindrom))


def is_palindrome(*palindrome):
    result = {}
    for word in palindrom:
        row_word = word.replace(' ', '').lower()
        result[word] = row_word == row_word[::-1]
    return result


print(is_palindrome(palindrom))

ice = {1: 'привет',
       2: 'пока'}
print(ice)
ice[3] = 'опять'
print(ice)

