"""
HomeWork 23-24. Реализация системы Умного дома
"""
from abc import ABC, abstractmethod


# Абстрактный класс - умное устройство
class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def turn_on(self):  # Метод включения
        pass

    @abstractmethod
    def turn_off(self):  # Метод выключения
        pass

    @abstractmethod
    def get_state(self):  # Метод проверки состояния
        pass


# Умная лампочка
class SmartLight(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.state = 'Выключено'
        self.brightness = 50

    def turn_on(self):
        self.state = 'Включено'

    def turn_off(self):
        self.state = 'Выключено'

    def get_state(self):
        return self.state

    def adjust_brightness(self, value):
        self.brightness = value


# Умный датчик дыма
class SmartSmokeDetector(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.state = 'Выключено'
        self.qwer = None

    def turn_on(self):
        self.state = 'Включено'

    def turn_off(self):
        self.state = 'Выключено'

    def get_state(self):
        return self.state

    def check_smoke(self, smoke_level):
        if smoke_level >= 10:
            print(f'Анализ состояния воздуха.. ({smoke_level})\nПовышенный уровень дыма. Проверьте помещения.')
        else:
            print(f'Анализ состояния воздуха.. ({smoke_level})\nУровень дыма в норме')


# Умный увлажнитель воздуха
class SmartHumidifier(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.state = 'Выключено'
        self.humidity_level = 60

    def turn_on(self):
        self.state = 'Включено'

    def turn_off(self):
        self.state = 'Выключено'

    def get_state(self):
        return self.state

    def set_humidity(self, level):
        self.humidity_level = level


# Миксин срочное уведомление
class EmergencyNotificationMixin:
    def send_emergency_notification(self, message):
        print('Экстренное уведомление:', message)


# Миксин подключение к Wi-Fi
class WiFiConnectionMixin:
    def connect_to_wifi(self, network_name, password):
        print(f'Успешное подключение к сети Wi-Fi: Логин: {network_name}, пароль: {password}')


# Миксин расписание работы
class ScheduleMixin:
    def __init__(self):
        self.schedule = {}

    def set_schedule(self, schedule):
        self.schedule = schedule


# Создание обычное лампочки
class SimpleLightBulb(SmartLight, EmergencyNotificationMixin):
    def __init__(self, name):
        super().__init__(name,)
        self.message = None

    def turn_on(self):
        super().turn_on()

    def turn_off(self):
        super().turn_off()

    def get_state(self):
        super().get_state()

    def __str__(self):
        return f'Лампочка в коридоре. Состояние {self.state}.'


# Создание умной лампочки
class XiaomiLightBulb(SmartLight, WiFiConnectionMixin):
    def __init__(self, name):
        super().__init__(name)
        self.network_name = None
        self.password = None

    def turn_on(self):
        super().turn_on()

    def turn_off(self):
        super().turn_off()

    def get_state(self):
        super().get_state()

    def __str__(self):
        return f'Умная лампочка Xiaomi на кухне. Состояние {self.state}.'


# Информация про обычную лампочку в коридоре
simple_light = SimpleLightBulb('Лампочка в коридоре')
print(simple_light)
# Выявление ошибки
simple_light.send_emergency_notification('Что-то пошло не так, лампочка не включается.\n')

xiaomi_light = XiaomiLightBulb('Умная лампочка Xiaomi на кухне')
xiaomi_light.turn_on()
print(xiaomi_light)
xiaomi_light.connect_to_wifi('vit_007', 1111)

bulb = SmartLight('\nЛампочка для гостиной')
print(bulb.name)
print('Начальное состояние:', bulb.get_state())

bulb.turn_on()  # Включаем лампочку
print('Состояние после включения:', bulb.get_state())

# Регулируем яркость
bulb.adjust_brightness(75)
print(f'Уровень яркости: {bulb.brightness}\n')

# Создание умного датчика дыма
smoke_detector = SmartSmokeDetector('Кухонный детектор дыма')
print(smoke_detector.name)
print('Начальное состояние:', smoke_detector.get_state())
smoke_detector.turn_on()
# Включаем датчик дыма
print('Состояние после включения:', smoke_detector.get_state())
# Проверяем наличие дыма
smoke_detector.check_smoke(80)

# Создание умного увлажнителя воздуха
humidifier = SmartHumidifier('\nУвлажнитель для спальни')
print(humidifier.name)
# Проверяем начальное состояние
print('Начальное состояние:', humidifier.get_state())
# включаем увлажнитель воздуха
humidifier.turn_on()
# Нынешнее состояние
print('Состояние после включения:', humidifier.get_state())
# Устанавливаем влажность воздуха
humidifier.set_humidity(60)
# Проверяем уровень влажности
print('Уровень влажности:', humidifier.humidity_level)
