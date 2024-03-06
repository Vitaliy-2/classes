# Задача №1.
data_list = ['1', '2', '3', '4d', 5]
new_list = []

# Цикл перебора элементов списка
for element in data_list:
    try:
        if element == int(element):
            new_list.append(element)  # Добавление числа в список
        else:
            print(f'\'{element}\' - не является числом. Это строка.')
    # Печать ошибки, когда элемент не является числом
    except ValueError:
        print(f'{element} - не является числом.')

print(f'Список, состоящий только из чисел:\n{new_list}')
