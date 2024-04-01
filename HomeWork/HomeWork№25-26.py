"""
HomeWork №25-26
Рефакторинг игры в города на ООП
"""

import json

JSON_FILE = "../data/cities.json"


class JsonFile:
    """
    Класс для работы с json файлами
    """

    def __init__(self, file_name: str, encoding: str = "utf-8", indent: int = 4, ensure_ascii: bool = False):
        self.file_name = file_name
        self.encoding = encoding
        self.indent = indent
        self.ensure_ascii = ensure_ascii
        self.data = self.read()

    def read(self):
        """
        Чтение файла
        """
        with open(self.file_name, 'r', encoding=self.encoding) as file:
            return json.load(file)


class Cities:
    """
    Класс для работы с городами
    """

    def __init__(self, city_data: JsonFile):
        self.bad_letters = None
        self.bad_letter = None
        self.data = city_data
        self.cities = {city["name"] for city in self.data.data}
        self.__letters = None

    def is_city(self, city: str) -> bool:
        """
        Проверка города
        """
        return city in self.cities

    def del_city(self, city: str):
        """
        Удаление города
        """
        self.cities.remove(city)

    def __get_letters_set(self) -> set:
        """
        Получение множества букв
        """
        self.__letters = set(''.join(self.cities).lower())
        return self.__letters

    def get_bad_letters(self) -> set:
        """
        Получение букв
        """
        self.__get_letters_set()
        self.bad_letters = set()
        for letter in self.__letters:
            for city in self.cities:
                if city.lower().startswith(letter):
                    break
            else:
                self.bad_letters.add(letter)
        return self.bad_letters


class CityGame:
    """
    Класс для управления игрой
    """

    def __init__(self, cities: Cities):
        self.cities = cities
        self.computer_city = None
        self.human_city = None
        self.game_over = False

    def start_game(self):
        """
        Начало игры
        """
        self.computer_turn()

    def check_game_rules(self, city_one: str, city_two: str) -> bool:
        """
        Проверка правил игры
        """
        game_rule = city_one[-1].lower() == city_two[0].lower()
        city_in_cities = self.cities.is_city(city_two)
        not_bad_letter = city_two[0].lower() not in self.cities.bad_letters

        return game_rule and city_in_cities and not_bad_letter

    def human_turn(self, city_input: str):
        """
        Ход человека
        """
        if self.check_game_rules(self.computer_city, city_input):
            self.human_city = city_input
            self.cities.del_city(city_input)
            return True
        else:
            print('Вы проиграли')
            self.game_over = True
            return False

    def computer_turn(self):
        """
        Ход компьютера
        """
        # Обновляем плохие буквы
        self.cities.get_bad_letters()
        # Найдем город
        for city in self.cities.cities:
            if city[0].lower() not in self.cities.bad_letters:
                if self.human_city is None:
                    self.computer_city = city
                    self.cities.del_city(city)
                    print(f'Компьютер: {self.computer_city}')
                    return True
                elif self.check_game_rules(self.human_city, city):
                    self.computer_city = city
                    self.cities.del_city(city)
                    print(f'Компьютер: {self.computer_city}')
                    return True
        else:
            print('Компьютер проиграл')
            self.game_over = True
            return False


class GameManager:
    def __init__(self, city_game: CityGame):
        self.city_game = city_game

    def __call__(self):
        self.run_game()

    def run_game(self):
        self.city_game.start_game()
        while True:
            if self.city_game.game_over:
                break
            city = input('Ваш ход: ').title()
            if not self.city_game.human_turn(city):
                break
            if self.city_game.game_over:
                break
            if not self.city_game.computer_turn():
                break


game_manager = GameManager(CityGame(Cities(JsonFile(JSON_FILE))))
game_manager()
