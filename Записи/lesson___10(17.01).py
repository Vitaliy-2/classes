from data.marvel import full_dict
from pprint import pprint
# print(full_dict)
# dict_list = [d_list for d_list in full_dict.values()]
# print(dict_list)
# # pprint(dict_list)

data_user = input('Введите фазу Марвел: ')

films_list = [
    {
        'id': id_film,
        'title': film['title'],
        'year': film['year'],
        'stage': film['stage']
    }
    for id_film, film in full_dict.items()
    if film['stage'] == data_user
]
pprint(films_list)
