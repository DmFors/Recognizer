"""
1.2 Блок транслитерации
"""
from exeptions import *


def recognize_class(char):
    """
    Распознает класс символа
    :param char: символ
    :return: класс символа
    """
    print(char)
    symbols = {"=": "равно", "[": "лвскобка", "]": "прскобка", ";": "тчкзпт", "+": "знак", "-": "знак", "*": "бинзнак",
               "/": "бинзнак", ".": "тчк", " ": "пробел"}
    code = ord(char)
    if 97 <= code <= 122:
        return "буква"
    elif 48 <= code <= 57:
        return "цифра"
    else:
        if char not in symbols.keys():
            raise TranslError("Invalid character in chain!")
        else:
            return symbols[char]


def transliteration(chain: str):
    """
    Получает исходную символьную цепочку. Преобразует исходную символьную цепочку
    в цепочку лексем вида ("символ цепочки", "класс символа цепочки ").
    Классы символов цепочки: буква, цифра, пробел, плюс, минус, умножить, тчкзпт.
    :param chain: исходная символьная цепочка
    :return: список, каждый элемент которого представляет кортеж
            вида ("символ цепочки", "класс символа цепочки ")
    """
    chain_characters = []
    for char in chain:
        char_class = recognize_class(char)
        chain_characters.append([char, char_class])
    return chain_characters
