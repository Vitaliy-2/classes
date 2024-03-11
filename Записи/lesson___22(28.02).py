# Инструменты классов

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# Создадим экземпляр класса
test = Test(1, 2)

# Проверим, есть ли атрибут 'a' у экземпляра класса
print(hasattr(test, 'a'))  # True
print(hasattr(test, 'c'))  # False

# Удаляем атрибут 'a' у экземпляра класса
delattr(test, 'a')
print(hasattr(test, 'a')) # False

# Установим атрибут 'a' у экземпляра класса
setattr(test, 'a', 10)
print(hasattr(test, 'a')) # True
print(test.a)

# Прямое назначение атрибута
test.z = 'z'
print(test.z)

# Отличия между прямым назначением атрибута и использованим функции setattr()
new_attr_name = 'c'
new_attr_value = 100
test.new_attr_name = new_attr_value
print(test.new_attr_name)

# getattr - добывает атрибут
print(getattr(test, 'a'))  # 10

test2 = Test(3, 4)
test2.x = 120


# __dict__ - словарь атрибутов экземпляра класса
# __dir__() - список атрибутов экземпляра класса
print(test.__dict__)  # {'b': 2, 'a': 10, 'z': 'z', 'new_attr_name': 100}
print(test2.__dict__)  # {'a': 3, 'b': 4, 'x': 120}
# print(dir(test2))  # Вся служебная информация
