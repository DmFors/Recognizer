"""
1.3 Лексический блок
"""
state = "НАЧ"
chain_lexemes = []


def stop():
    print(f"Лексический блок: ошибка на состоянии {state}")
    exit(-1)


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
                stop()
        elif state == "КЛСЛОВО1":
            if char_class == "буква":
                add_char(char)
            elif char_class == "пробел":
                state = "ПРОБЕЛ1"
            else:
                stop()
        elif state == "ПРОБЕЛ1":
            if char_class == "буква":
                add_word(char)
                state = "ИМЯ1"
            elif char_class == "пробел":
                pass
            else:
                stop()
        elif state == "ИМЯ1":
            if char_class == "буква" or char_class == "цифра":
                add_char(char)
            elif char_class == "равно":
                add_equally(char)
                state = "РАВНО"
            elif char_class == "пробел":
                state = "ПРОБЕЛ2"
            else:
                stop()
        elif state == "ПРОБЕЛ2":
            if char_class == "равно":
                add_equally(char)
                state = "РАВНО"
            elif char_class == "пробел":
                pass
            else:
                stop()
        elif state == "РАВНО":
            if char_class == "буква":
                add_word(char)
                state = "КЛСЛОВО2"
            elif char_class == "пробел":
                pass
            else:
                stop()
        elif state == "КЛСЛОВО2":
            if char_class == "буква":
                add_char(char)
            elif char_class == "лвскобка":
                add_leftpar(char)
                state = "ЛВСКОБКА"
            elif char_class == "пробел":
                state = "ПРОБЕЛ4"
            else:
                stop()
        elif state == "ПРОБЕЛ4":
            if char_class == "лвскобка":
                add_leftpar(char)
                state = "ЛВСКОБКА"
            elif char_class == "пробел":
                pass
            else:
                stop()
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
                stop()
        elif state == "ЗНАК1":
            if char_class == "цифра":
                add_integer(char)
                state = "ЦЕЛОЕ1"
            elif char_class == "пробел":
                pass
            else:
                stop()
        elif state == "ЦЕЛОЕ1":
            if char_class == "цифра":
                add_char(char)
            elif char_class == "знак" or char_class == "бинзнак":
                add_binsign(char)
                state = "БИНЗНАК1"
            elif char_class == "пробел":
                state = "ПРОБЕЛ7"
            else:
                stop()
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
                stop()
        elif state == "БИНЗНАК1":
            if char_class == "буква":
                add_word(char)
                state = "ИМЯ2"
            elif char_class == "пробел":
                pass
            else:
                stop()
        elif state == "КЛСЛОВО3":
            if char_class == "буква":
                add_char(char)
            elif char_class == "пробел":
                state = "ПРОБЕЛ8-2"
            else:
                stop()
        elif state == "ПРОБЕЛ8-2":
            if char_class == "буква":
                add_word(char)
                state = "ИМЯ2"
            elif char_class == "пробел":
                pass
            else:
                stop()
        elif state == "ИМЯ2":
            if char_class == "буква" or char_class == "цифра":
                add_char(char)
            elif char_class == "тчк":
                add_word(char)
                state = "КЛСЛОВО4"
            elif char_class == "пробел":
                state = "ПРОБЕЛ9"
            else:
                stop()
        elif state == "ПРОБЕЛ9":
            if char_class == "тчк":
                add_word(char)
                state = "КЛСЛОВО4"
            elif char_class == "пробел":
                state = "ПРОБЕЛ9"
            else:
                stop()
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
                stop()
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
                stop()
        elif state == "ЗНАК2":
            if char_class == "цифра":
                add_integer(char)
                state = "ЦЕЛОЕ2"
            elif char_class == "пробел":
                pass
            else:
                stop()
        elif state == "ЦЕЛОЕ2":
            if char_class == "цифра":
                add_char(char)
            elif char_class == "знак" or char_class == "бинзнак":
                add_binsign(char)
                state = "БИНЗНАК2"
            elif char_class == "пробел":
                state = "ПРОБЕЛ12"
            else:
                stop()
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
                stop()
        elif state == "БИНЗНАК2":
            if char_class == "буква":
                add_word(char)
                state = "ИМЯ3"
            elif char_class == "пробел":
                state = "БИНЗНАК2"
            else:
                stop()
        elif state == "КЛСЛОВО5":
            if char_class == "буква":
                add_char(char)
            elif char_class == "пробел":
                state = "ПРОБЕЛ13-2"
            else:
                stop()
        elif state == "ПРОБЕЛ13-2":
            if char_class == "буква":
                add_word(char)
                state = "ИМЯ3"
            elif char_class == "пробел":
                pass
            else:
                stop()
        elif state == "ИМЯ3":
            if char_class == "буква":
                add_char(char)
            elif char_class == "прскобка":
                add_rightpar(char)
                state = "ПРСКОБКА"
            elif char_class == "пробел":
                state = "ПРОБЕЛ14"
            else:
                stop()
        elif state == "ПРОБЕЛ14":
            if char_class == "прскобка":
                add_rightpar(char)
                state = "ПРСКОБКА"
            elif char_class == "пробел":
                state = "ПРОБЕЛ14"
            else:
                stop()
        elif state == "ПРСКОБКА":
            if char_class == "буква":
                add_word(char)
                state = "КЛСЛОВО6"
            elif char_class == "пробел":
                pass
            else:
                stop()
        elif state == "КЛСЛОВО6":
            if char_class == "буква":
                add_char(char)
            elif char_class == "пробел":
                state = "ПРОБЕЛ16"
            else:
                stop()
        elif state == "ПРОБЕЛ16":
            if char_class == "буква":
                add_word(char)
                state = "КЛСЛОВО7"
            elif char_class == "пробел":
                pass
            else:
                stop()
        elif state == "КЛСЛОВО7":
            if char_class == "буква":
                add_char(char)
            elif char_class == "тчкзпт":
                add_semicolon(char)
                state = "ТЧКЗПТ"
            elif char_class == "пробел":
                state = "ПРОБЕЛ17"
            else:
                stop()
        elif state == "ПРОБЕЛ17":
            if char_class == "тчкзпт":
                add_semicolon(char)
                state = "ТЧКЗПТ"
            elif char_class == "пробел":
                pass
            else:
                stop()
        elif state == "ТЧКЗПТ":
            return chain_lexemes
