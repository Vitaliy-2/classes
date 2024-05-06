"""
Lesson 35: Структурные паттерны
- повторение порождающих паттернов
- Abstract Factory - абстрактная фабрика
- Abstract Method - абстрактный метод
- Facade - фасад
- Adapter - адаптер
- Decorator - декоратор - повторили
- Proxy - заместитель
"""

# Facade - фасад
# Паттерн Facade предоставляет унифицированный интерфейс к группе интерфейсов в подсистеме.

# Простой пример


# Сложная система (подсистемы)
class SubsystemOne:
    def operation(self):
        return "Подсистема 1: Поехали!"

class SubsystemTwo:
    def operation(self):
        return "Подсистема 2: Поехали!"

# Фасад
class Facade:
    def __init__(self):
        self._subsystem_one = SubsystemOne()
        self._subsystem_two = SubsystemTwo()

    def operation(self):
        user_choise = input("Какую подсистему запустить? 1 или 2: ")
        if user_choise == "1":
            print("Запускаем подсистему 1")
            return self._subsystem_one.operation()
        elif user_choise == "2":
            print("Запускаем подсистему 2")
            return self._subsystem_two.operation()


# Клиентский код
facade = Facade()
print(facade.operation())
