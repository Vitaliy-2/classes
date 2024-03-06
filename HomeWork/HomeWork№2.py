# Задание №1 Перевод пользовательского ввода секунд в удобный формат: часы, минуты, секунды.
user_seconds = int(input('Введите количество секунд: '))
hours = user_seconds // 3600  # Получаем количество часов
minutes = user_seconds % 3600 // 60  # Получаем остаток после нахождения часов и делим на 60 (получая остаток)
seconds = user_seconds % 60  # Получаем остаток секунд
print(f'В указанном количестве секунд ({user_seconds}):\n'
      f'Часов: {hours}\n'
      f'Минут: {minutes}\n'
      f'Секунд: {seconds}')

# Задание №2 Преобразование градусов Цельсия в градусы: Кельвина, Фаренгейта и Реомюра.
user_temp_Celsius = float(input('Введите температуру в градусах Цельсия: '))
degrees_Kelvin = user_temp_Celsius * 274.15  # Получаем градусы Кельвина (1 к 274,15)
degrees_Fahrenheit = user_temp_Celsius * 33.8  # Получаем градусы Фаренгейта (1 к 33,8)
degrees_Reaumur = user_temp_Celsius * 0.8  # Получаем градусы Реомюра (1 к 0,8)
# С помощью метода round округляем числа до сотых
print(f'В указанном количестве градусов цельсия ({user_temp_Celsius}): \n'
      f'Градусов Кельвина: {round(degrees_Kelvin, 2)}\n'
      f'Градусов Фаренгейта: {round(degrees_Fahrenheit, 2)}\n'
      f'Градусов Реомюра: {round(degrees_Reaumur, 2)}')
