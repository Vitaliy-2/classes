"""
Lesson 34: Порождающие паттерны
10.04.2024
- Singleton - одиночка
- Prototype - прототип
- Builder - строитель
- Abstract Factory - абстрактная фабрика
"""
# Prototype - прототип
# Паттерн Прототип (Prototype) - это порождающий паттерн проектирования,
# который позволяет копировать объекты, не вдаваясь в подробности их реализации.


# Абстрактный пример
import copy
import random


class Prototype:
    def __init__(self, name):
        self.name = name

    def clone(self):
        return copy.deepcopy(self)


p1 = Prototype("Original")
p2 = p1.clone()
p3 = p2.clone()

print(p1.name)
print(p2.name)
print(p3.name)

print(p1 is p2)
print(p2 is p3)


class Tree:
    def __init__(self, species, age, height):
        self.species = species  # Вид
        self.age = age  # Возраст
        self.height = height  # Высота

    def clone(self):
        """Клонирует текущий экземпляр дерева с рандомным возрастом от оригинала/2 до оригинала."""
        # Создаём глубокую копию объекта
        clone_tree = copy.deepcopy(self)
        # Устанавливаем рандомный возраст в диапазоне от оригинал/2 до оригинала
        clone_tree.age = random.randint(self.age // 2, self.age)
        clone_tree.height = random.randint(self.height // 2, self.height)
        return clone_tree

    def __str__(self):
        return f"{self.species} дерево возрастом {self.age} лет, высотой {self.height} метров."


# Создаём экземпляр дерева
original_tree = Tree("Дуб", 100, 30)

# Клонируем дерево
cloned_tree = original_tree.clone()

print(original_tree)  # Выведет информацию об оригинальном дереве
print(cloned_tree)  # Выведет информацию о клонированном дереве с изменённым возрастом

forest = [original_tree.clone() for _ in range(5)]
for tree in forest:
    print(tree)
