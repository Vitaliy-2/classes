# HomeWork 5. Расшифровка послания

# Данные в виде списка, состоящего из списков
secret_letter = [['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
    ['оafбasdf%^о^FFжа$#af243ю'], ['afпFsfайFтFsfо13н'], ['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
    ['и$ՐҶsfF'], ['вSFSDам'], ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'], ['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']]

# Буквы для поиска
small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
    'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
    'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# Строка для наполнения нужных символов
result_string = ''
# Цикл поиска русских букв
# Цикл перебора списков в списке
for list_fragment in secret_letter:
    # Цикл перебора объектов списка
    for list_obj in list_fragment:
        result_string += ' '  # Добавление пробела между объектами списка
        # Цикл перебора символов объекта списка
        for letter_symbol in list_obj:
            # Проверка на совпадение символов согласно условию задачи
            if letter_symbol in small_rus:
                result_string += letter_symbol

# Выводим результат, удаляя пробел перед текстом.
print(result_string.strip().capitalize())

input('Для выхода из программы нажмите Enter')
