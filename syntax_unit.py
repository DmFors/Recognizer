"""
1.4 Синтаксический блок
"""
from ident_unit import *


def check_the_formula(chain_lexemes: list):
    """
    Получает цепочку лексем вида ("символ входного языка", "класс символа входного языка") и
    устанавливает, соответствует ли она заданным формулам Бэкуса-Наура.
    :param chain_lexemes:список, каждый элемент которого представляет кортеж
                        вида ("символ входного языка", "класс символа входного языка").
    :return: результат работы распознавателя: строку, “ACCEPT” или “REJECT”
    """
    identifier = ""
    processed_identifier = identify(identifier)
    result = ""
    return result
