"""
HomeWork №39
Применение паттернов "Стратегия" и "Фасад" в проверке палиндромов.
"""

from abc import ABC, abstractmethod


class AbstractPalindromeStrategy(ABC):

    @abstractmethod
    def is_palindrome(self, input_string: str) -> bool:
        pass


class SingleWordPalindrome(AbstractPalindromeStrategy):
    def is_palindrome(self, input_string: str) -> bool:
        return input_string.lower() == input_string[::-1].lower()


class MultiWordPalindrome(AbstractPalindromeStrategy):
    def is_palindrome(self, input_string: str) -> bool:
        input_string = (input_string.replace(' ', '').replace(',', '')
                        .replace('.', '').lower())
        return input_string == input_string[::-1]


class PalindromeContext:
    def __init__(self, strategy: AbstractPalindromeStrategy):
        self.strategy = strategy

    def check_palindrome(self, input_string: str) -> bool:
        return self.strategy.is_palindrome(input_string)

    def set_strategy(self, strategy: AbstractPalindromeStrategy):
        self.strategy = strategy


class PalindromeFacade:
    def __init__(self):
        self.single: SingleWordPalindrome = SingleWordPalindrome()
        self.multi: MultiWordPalindrome = MultiWordPalindrome()
        self.context: PalindromeContext = PalindromeContext(self.single)

    def check_palindrome(self):
        user_input = input("Что вы хотите проверить на палиндром? (1 - Одно слово, 2 - Многословное выражение): ")
        if user_input == "1":
            input_single_word = input('Введите слово для проверки: ')
            self.context.set_strategy(self.single)
            result = self.context.check_palindrome(input_single_word)
        elif user_input == "2":
            input_multi_word = input('Введите выражение для проверки: ')
            self.context.set_strategy(self.multi)
            result = self.context.check_palindrome(input_multi_word)
        else:
            print('Неверный ввод')
            return

        if result:
            print('Это палиндром')
        else:
            print('Это не палиндром')


palindrome = PalindromeFacade()
palindrome.check_palindrome()
