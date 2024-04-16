"""
Lesosn 29
25.03.2024
Датаклассы Ч2
@dataclass(order=True) - для сравнения
Метаинформация в полях (для сериализации и других целей)
Наследование датаклассов
Декорация классов
Метаклассы - как концепция
"""

from dataclasses import dataclass, field, fields, asdict


@dataclass(order=True)
class AbstractPerson:
    first_name: str = field(metadata={"description": "Имя"})


@dataclass(order=True)  # order дает делать сравнения
class Person(AbstractPerson):
    # метадата - добавление дополнительных условий
    age: int = field(metadata={"description": "Возраст"})
    city: str = field(compare=False, metadata={"description": "Город"})

    def __str__(self):
        """
        Оправданная сложность.
        В наследниках все работает автоматически
        """
        # в fields(self) - помещается экземпляр класса, то есть вася и маша
        meta_str = ", ".join([f'{f.metadata['description']}: {getattr(self, f.name)}' for f in fields(self)])
        return meta_str


@dataclass(order=True)
class Employee(Person):
    position: str = field(metadata={"description": "Должность"})
    salary: int = field(metadata={"description": "Зарплата"})


p1 = Employee('Вася', 25, 'Москва', 'Программист', 100_000)
p2 = Employee('Маша', 30, 'Москва', 'Программист', 100_000)
p3 = Employee('Аня', 25, 'Москва', 'Тимлид', 150_000)


# print(p1)
# print(p2)
# print(p3)
# print(p1.first_name)

# fields - функция которая возвращает список полей датакласса.
# Возвращает в виде кортежа.
# Каждое поле - объект fields


@dataclass(order=True)
class Product:
    name: str = field(compare=False, metadata={"description": "Имя"})
    category: str = field(compare=False, metadata={"description": "Категория"})
    price: float = field(metadata={"description": "Цена"})

    def __str__(self):
        meta_str = ", ".join([f'{f.metadata['description']}: {getattr(self, f.name)}' for f in fields(self)])
        return meta_str


@dataclass(order=True)
class Notebook(Product):
    screen_size: float = field(compare=False, metadata={"description": "Размер экрана"})
    cpu: str = field(compare=False, metadata={"description": "Процессор"})
    ram: float = field(compare=False, metadata={"description": "Объем памяти"})


@dataclass(order=True)
class Phone(Product):
    brand: str = field(compare=False, metadata={"description": "Бренд"})
    os: str = field(compare=False, metadata={"description": "Опер. система"})
    memory: float = field(compare=False, metadata={"description": "Объем памяти"})


notebook1 = Notebook('Ноутбук Филипс', 'Электроника', 45_000, 37, 'AMD', 16)
print(notebook1)
notebook2 = Notebook('Ноутбук Эйсер', 'Электроника', 74_000, 55, 'Intel', 32)
print(notebook2)

phone1 = Phone('Redmi', 'Электроника', 22_220, 'Xiaomi', 'OS1', 8)
print(phone1)
phone2 = Phone('Айфон', 'Электроника', 95_220, 'Apple', 'OS5', 256)
print(phone2)

print(f'Сравнение ноутбука филипса и эйсера на равенство: {notebook1 == notebook2}')
print(f'Ноутбук филипс дороже эйсера: {notebook1 > notebook2}')
print(f'Ноутбук филипс дешевле эйсера: {notebook1 < notebook2}')

print(f'Сравнение телефона Редми и Айфона на равенство: {phone1 == phone2}')
print(f'Телефон Редми дороже Айфона: {phone1 > phone2}')
print(f'Телефон Редми дешевле Айфона: {phone1 < phone2}')

print(f'Сравнение Айфона с Эйсером на равенство цены: {phone2 == notebook2}')

product_list = [notebook1.price, notebook2.price, phone1.price, phone2.price]
product_list.sort()
print(f'Сортировка продуктов по цене: {product_list}')

product_list1 = [notebook2, notebook1]
product_list1.sort()
print(f'Сортировка продуктов по цене: {product_list1}')


products = [notebook1, notebook2, phone1, phone2]
print(sorted(products, key=lambda product: product.price))

