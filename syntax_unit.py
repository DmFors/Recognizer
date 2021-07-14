"""
1.4 Синтаксический блок
"""
from ident_unit import *
from exeptions import KeywordError, IdError, StateError


def check_the_formula(chain_lexemes: list):
    """
    Получает цепочку лексем вида ("символ входного языка", "класс символа входного языка") и
    устанавливает, соответствует ли она заданным формулам Бэкуса-Наура.
    :param chain_lexemes:список, каждый элемент которого представляет кортеж
                        вида ("символ входного языка", "класс символа входного языка").
    :return: результат работы распознавателя: строку, “ACCEPT” или “REJECT”
    """
    result = "REJECT"
    state = "НАЧ"
    for lexeme in chain_lexemes:
        word, word_class = lexeme
        if state == "НАЧ":
            if word == "type":
                state = "TYPE"
            else:
                raise KeywordError(f"Expected 'type', but received '{word}' on state {state}")
        elif state == "TYPE":
            if word_class == "идент" and identify_pascal(word) is False:
                state = "ИМЯ_МАССИВА"
            else:
                raise IdError(f"Invalid array name on state {state}")
        elif state == "ИМЯ_МАССИВА":
            if word == "=":
                state = "РАВНО"
            else:
                raise KeywordError(f"Excepted '=', but received {word} on state {state}")
        elif state == "РАВНО":
            if word == "array":
                state = "ARRAY"
            else:
                raise KeywordError(f"Expected 'array', but received '{word}' on state {state}")
        elif state == "ARRAY":
            if word == '[':
                state = 'ЛВСКОБКА'
            else:
                raise KeywordError(f"Expected '[', but received '{word}' on state {state}")
        elif state == "ЛВСКОБКА":
            if word_class == 'знак':
                state = "ЗНАК_НИЖ"
            elif word_class == 'целое':
                state = "ЦЕЛОЕ_НИЖ"
            else:
                raise KeywordError(f"Expected 'знак' or 'целое', but received '{word}' on state {state}")
        elif state == "ЗНАК_НИЖ":
            if word_class == "целое":
                state = "ЦЕЛОЕ_НИЖ"
            else:
                raise KeywordError(f"Expected 'целое', but received '{word}' on state {state}")
        elif state == "ЦЕЛОЕ_НИЖ":
            if word_class == "бинзнак" or word == "div" or word == "mod":
                state = "БИНЗНАК_НИЖ"
            else:
                raise KeywordError(f"Expected 'бинзнак' or 'div' or 'mod', but received '{word}' on state {state}")
        elif state == "БИНЗНАК_НИЖ":
            if word_class == "идент" and identify_pascal(word) is False:
                state = "ИМЯ_НИЖ"
            else:
                raise IdError(f"Invalid name of the first variable ({word}) on state {state}")
        elif state == "ИМЯ_НИЖ":
            if word == "..":
                state = "ДВЕТЧК"
            else:
                raise KeywordError(f"Expected '..', but received '{word}' on state {state}")
        elif state == "ДВЕТЧК":
            if word_class == "знак":
                state = "ЗНАК_ВЕРХ"
            elif word_class == "целое":
                state = "ЦЕЛОЕ_ВЕРХ"
            else:
                raise KeywordError(f"Expected 'знак' or 'целое', but received '{word}' on state {state}")
        elif state == "ЗНАК_ВЕРХ":
            if word_class == "целое":
                state = "ЦЕЛОЕ_ВЕРХ"
            else:
                raise KeywordError(f"Expected 'целое', but received '{word}' on state {state}")
        elif state == "ЦЕЛОЕ_ВЕРХ":
            if word_class == "бинзнак" or word == "div" or word == "mod":
                state = "БИНЗНАК_ВЕРХ"
            else:
                raise KeywordError(f"Expected 'бинзнак' or 'div' or 'mod', but received '{word}' on state {state}")
        elif state == "БИНЗНАК_ВЕРХ":
            if word_class == "идент" and identify_pascal(word) is False:
                state = "ИМЯ_ВЕРХ"
            else:
                raise IdError(f"Invalid name of the second variable ({word}) on state {state}")
        elif state == "ИМЯ_ВЕРХ":
            if word == "]":
                state = "ПРСКОБКА"
            else:
                raise KeywordError(f"Expected ']', but received '{word}' on state {state}")
        elif state == "ПРСКОБКА":
            if word == "of":
                state = "OF"
            else:
                raise KeywordError(f"Expected 'of', but received '{word}' on state {state}")
        elif state == "OF":
            if word_class == "идент" and identify_stdtype(word) is True:
                state = "STDTYPE"
            else:
                raise KeywordError(f"Expected 'stdtype', but received '{word}' on state {state}")
        elif state == "STDTYPE":
            if word == ";":
                state = "ТЧКЗПТ"
            else:
                raise KeywordError(f"Expected ';', but received '{word}' on state {state}")
        else:
            raise StateError(f"Invalid state of automate ({state})")
    # The symbol in the correct last lexeme of the list chain_lexemes will ALWAYS be ';'
    if state == "ТЧКЗПТ":
        result = "ACCEPT"
    return result
