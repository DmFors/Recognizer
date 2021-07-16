"""
1.3 Лексический блок
"""
from exeptions import *

state = "НАЧ"
chain_lexemes = []


def add_word(char):
    chain_lexemes.append(["", "идент"])
    add_char(char)


def add_char(char):
    chain_lexemes[-1][0] += char


def add_equally(char):
    chain_lexemes.append(["", "равно"])
    add_char(char)


def add_leftpar(char):
    chain_lexemes.append(["", "лвскобка"])
    add_char(char)


def add_integer(char):
    chain_lexemes.append(["", "целое"])
    add_char(char)


def add_sign(char):
    chain_lexemes.append(["", "знак"])
    add_char(char)


def add_binsign(char):
    chain_lexemes.append(["", "бинзнак"])
    add_char(char)


def add_rightpar(char):
    chain_lexemes.append(["", "прскобка"])
    add_char(char)


def add_semicolon(char):
    chain_lexemes.append(["", "тчкзпт"])
    add_char(char)


def to_lexemes(chain_characters: list):
    """
    Преобразует цепочку лексем, полученную от транслитератора, в цепочку лексем вида
    ("символ входного языка", "класс символа входного языка").
    :param chain_characters:список, каждый элемент которого представляет кортеж вида
            ("символ цепочки", "класс символа цепочки ")
    :return:цепочка лексем: список, каждый элемент которого представляет кортеж вида
            ("символ входного языка", "класс символа входного языка")
    """
    global state, chain_lexemes
    for lexeme in chain_characters:
        char, char_class = lexeme
        if state == "НАЧ":
            if char_class == "буква":
                add_word(char)
                state = "КЛСЛОВО1"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "КЛСЛОВО1":
            if char_class == "буква":
                add_char(char)
            elif char_class == "пробел":
                state = "ПРОБЕЛ1"
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "ПРОБЕЛ1":
            if char_class == "буква":
                add_word(char)
                state = "ИМЯ1"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "ИМЯ1":
            if char_class == "буква" or char_class == "цифра":
                add_char(char)
            elif char_class == "равно":
                add_equally(char)
                state = "РАВНО"
            elif char_class == "пробел":
                state = "ПРОБЕЛ2"
            else:
                raise LexicalUnitError("'буква' or 'цифра' or 'равно' or 'пробел'", char, state)
        elif state == "ПРОБЕЛ2":
            if char_class == "равно":
                add_equally(char)
                state = "РАВНО"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'равно' or 'пробел'", char, state)
        elif state == "РАВНО":
            if char_class == "буква":
                add_word(char)
                state = "КЛСЛОВО2"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "КЛСЛОВО2":
            if char_class == "буква":
                add_char(char)
            elif char_class == "лвскобка":
                add_leftpar(char)
                state = "ЛВСКОБКА"
            elif char_class == "пробел":
                state = "ПРОБЕЛ4"
            else:
                raise LexicalUnitError("'буква' or 'лвскобка' or 'пробел'", char, state)
        elif state == "ПРОБЕЛ4":
            if char_class == "лвскобка":
                add_leftpar(char)
                state = "ЛВСКОБКА"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'лвскобка' or 'пробел'", char, state)
        elif state == "ЛВСКОБКА":
            if char_class == "цифра":
                add_integer(char)
                state = "ЦЕЛОЕ1"
            elif char_class == "знак":
                add_sign(char)
                state = "ЗНАК1"
            elif char_class == "пробел":
                state = "ЛВСКОБКА"
            else:
                raise LexicalUnitError("'цифра' or 'знак' or 'пробел'", char, state)
        elif state == "ЗНАК1":
            if char_class == "цифра":
                add_integer(char)
                state = "ЦЕЛОЕ1"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'цифра' or 'пробел'", char, state)
        elif state == "ЦЕЛОЕ1":
            if char_class == "цифра":
                add_char(char)
            elif char_class == "знак" or char_class == "бинзнак":
                add_binsign(char)
                state = "БИНЗНАК1"
            elif char_class == "пробел":
                state = "ПРОБЕЛ7"
            else:
                raise LexicalUnitError("'цифра' or 'знак' or 'пробел'", char, state)
        elif state == "ПРОБЕЛ7":
            if char_class == "буква":
                add_word(char)
                state = "КЛСЛОВО3"
            elif char_class == "знак" or char_class == "бинзнак":
                add_binsign(char)
                state = "БИНЗНАК1"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'буква' or 'знак' or 'бинзнак' or 'пробел'", char, state)
        elif state == "БИНЗНАК1":
            if char_class == "буква":
                add_word(char)
                state = "ИМЯ2"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "КЛСЛОВО3":
            if char_class == "буква":
                add_char(char)
            elif char_class == "пробел":
                state = "ПРОБЕЛ8-2"
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "ПРОБЕЛ8-2":
            if char_class == "буква":
                add_word(char)
                state = "ИМЯ2"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "ИМЯ2":
            if char_class == "буква" or char_class == "цифра":
                add_char(char)
            elif char_class == "тчк":
                add_word(char)
                state = "КЛСЛОВО4"
            elif char_class == "пробел":
                state = "ПРОБЕЛ9"
            else:
                raise LexicalUnitError("'буква' or 'цифра' or 'тчк' or 'пробел'", char, state)
        elif state == "ПРОБЕЛ9":
            if char_class == "тчк":
                add_word(char)
                state = "КЛСЛОВО4"
            elif char_class == "пробел":
                state = "ПРОБЕЛ9"
            else:
                raise LexicalUnitError("'тчк' or 'пробел'", char, state)
        elif state == "КЛСЛОВО4":
            if char_class == "цифра":
                add_integer(char)
                state = "ЦЕЛОЕ2"
            elif char_class == "знак":
                add_sign(char)
                state = "ЗНАК2"
            elif char_class == "тчк":
                add_char(char)
            elif char_class == "пробел":
                state = "ПРОБЕЛ10"
            else:
                raise LexicalUnitError("'цифра' or 'знак' or 'тчк' or 'пробел'", char, state)
        elif state == "ПРОБЕЛ10":
            if char_class == "цифра":
                add_integer(char)
                state = "ЦЕЛОЕ2"
            elif char_class == "знак":
                add_sign(char)
                state = "ЗНАК2"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'цифра' or 'знак' or 'пробел'", char, state)
        elif state == "ЗНАК2":
            if char_class == "цифра":
                add_integer(char)
                state = "ЦЕЛОЕ2"
            elif char_class == "пробел":
                pass
            else:
                raise KeywordError()
        elif state == "ЦЕЛОЕ2":
            if char_class == "цифра":
                add_char(char)
            elif char_class == "знак" or char_class == "бинзнак":
                add_binsign(char)
                state = "БИНЗНАК2"
            elif char_class == "пробел":
                state = "ПРОБЕЛ12"
            else:
                raise LexicalUnitError("'цифра' or 'знак' or 'бинзнак' or 'пробел'", char, state)
        elif state == "ПРОБЕЛ12":
            if char_class == "буква":
                add_word(char)
                state = "КЛСЛОВО5"
            elif char_class == "знак" or char_class == "бинзнак":
                add_binsign(char)
                state = "БИНЗНАК2"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'знак' or 'пробел'", char, state)
        elif state == "БИНЗНАК2":
            if char_class == "буква":
                add_word(char)
                state = "ИМЯ3"
            elif char_class == "пробел":
                state = "БИНЗНАК2"
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "КЛСЛОВО5":
            if char_class == "буква":
                add_char(char)
            elif char_class == "пробел":
                state = "ПРОБЕЛ13-2"
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "ПРОБЕЛ13-2":
            if char_class == "буква":
                add_word(char)
                state = "ИМЯ3"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "ИМЯ3":
            if char_class == "буква":
                add_char(char)
            elif char_class == "прскобка":
                add_rightpar(char)
                state = "ПРСКОБКА"
            elif char_class == "пробел":
                state = "ПРОБЕЛ14"
            else:
                raise LexicalUnitError("'буква' or 'прскобка' or 'пробел'", char, state)
        elif state == "ПРОБЕЛ14":
            if char_class == "прскобка":
                add_rightpar(char)
                state = "ПРСКОБКА"
            elif char_class == "пробел":
                state = "ПРОБЕЛ14"
            else:
                raise LexicalUnitError("'прскобка' or 'пробел'", char, state)
        elif state == "ПРСКОБКА":
            if char_class == "буква":
                add_word(char)
                state = "КЛСЛОВО6"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "КЛСЛОВО6":
            if char_class == "буква":
                add_char(char)
            elif char_class == "пробел":
                state = "ПРОБЕЛ16"
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "ПРОБЕЛ16":
            if char_class == "буква":
                add_word(char)
                state = "КЛСЛОВО7"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'буква' or 'пробел'", char, state)
        elif state == "КЛСЛОВО7":
            if char_class == "буква":
                add_char(char)
            elif char_class == "тчкзпт":
                add_semicolon(char)
                state = "ТЧКЗПТ"
            elif char_class == "пробел":
                state = "ПРОБЕЛ17"
            else:
                raise LexicalUnitError("'буква' or 'тчкзпт' or 'пробел'", char, state)
        elif state == "ПРОБЕЛ17":
            if char_class == "тчкзпт":
                add_semicolon(char)
                state = "ТЧКЗПТ"
            elif char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'тчкзпт' or 'пробел'", char, state)
        elif state == "ТЧКЗПТ":
            if char_class == "пробел":
                pass
            else:
                raise LexicalUnitError("'пробел'", char, state)
        else:
            raise StateError(f"Invalid state of automate ({state})")
    if state == "ТЧКЗПТ":
        return chain_lexemes
