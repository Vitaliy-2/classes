list_names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
list_names2 = ['Alex', 'John', 'Bob', 'Jack', 'Bill', 'Sam', 'Петя']

shop_list = ['сыр', 'хлеб', 'сыр', 'молоко', 'колбаса','шоколадный заяц', 'коньяк']

# user_data = input('Введите 5 чисел через пробел: ').split(' ')
# print(user_data)
# list_comprehension = [int(gift) ** 2 for gift in user_data if gift.isdigit()]
# print(list_comprehension)

user_input = input('Введите 5 чисел через пробел: ').split(' ')
list_comp = [int(user) ** 2 for user in user_input]
print(list_comp)




number_of_proverbs = int(input('Введите желаемое число пословиц для генерации (не более 55): '))
result = []
try_count = 0
while len(result) < number_of_proverbs:
    try_count += 0
    random_proverb = random.choice(proverbs)
    random_variant = random.choice(variants).capitalize()
    new_proverb = random_proverb.replace('Ум', random_variant)
    result.append(new_proverb)
    proverbs.remove(random_proverb)
# else:
#     print('Вы ввели неверное количество пословиц.\nПовторите запрос в диапазоне от 1 по 55')
print(result)

for qqq in result:
    try_count += 1
    print(f'№ {try_count}. {qqq}')
