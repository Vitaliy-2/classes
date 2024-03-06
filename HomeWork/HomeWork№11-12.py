# HomeWork 12. Работа с JSON файлом. Запись, чтение.
import json
from data.cities import cities_list

# Создаем пустой set для добавления городов
# cities = set()
# # Цикл извлечения города из словаря и добавление его в сет
# for city_dict in cities_list:
#     city = city_dict["name"].title()
#     cities.add(city)
#
# # Переводим set в list
# cities_list = list(cities)

# Запись списка городов в json файл
# with open('cities.json', 'w', encoding='utf-8') as file:
#     json.dump(cities_list, file, ensure_ascii=False, indent=4)

# Чтение списка из json файла и преобразование его в set
with open('cities.json', 'r', encoding='utf-8') as file:
    cities_object = set(json.load(file))

print(cities_object)
