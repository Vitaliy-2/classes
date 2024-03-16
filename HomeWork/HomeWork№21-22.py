"""
HomeWork № 21-22
Реализация классов для работы с файлами в стиле ООП
"""
import json
import csv


class CsvFileHandler:
    """
    Класс для работы с CSV файлами
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def read_file(self, filepath, data):
        with open(self.filepath, 'r', encoding='windows-1251') as file:
            self.data = csv.reader(file, delimiter=';')
        return self.data

    def write_file(self, data, filepath):
        with open(self.filepath, 'w', encoding='windows-1251') as file:
            self.data = csv.writer(file, delimiter=';', lineterminator='\n')
            self.data.writerows(self.filepath)
            return self.data

    @staticmethod
    def append_file(filepath, data):
        with open(data, 'a', encoding='windows-1251') as file:
            data = csv.writer(file, delimiter=';', lineterminator='\n')
            data.writerow(filepath)


class JsonFileHandler:
    """
    Класс для работы с JSON файлами
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def write_file(self, data):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, insure_ascii=False, indent=4)

    def read_file(self, data):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
            return self.data

    def append_file(self, data):
        raise TypeError('Данный тип файла не поддерживает операцию дописывания')


class TxtFileHandler:
    """
    Класс для работы с TXT файлами.
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def read_file(self):
        """
        Метод для чтения данных из TXT файла. Открывает файл если он есть, иначе выводит ошибку.
        Если находит, читает данные и возвращает их.
        :return:
        :raises: FileNotFoundError: если файл не найден
        """
        try:
            with open(self.filepath, 'r') as file:
                self.data = file.read()
                return self.data
        except FileNotFoundError:
            print(f'Файл {self.filepath} не найден')

    def write_file(self, data):
        with open(self.filepath, 'w', encoding='windows-1251') as file:
            file.write(self.data)

    def append_file(self, data):
        with open(self.filepath, 'a', encoding='windows-1251') as file:
            file.write(self.data)
