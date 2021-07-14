"""
2.1 Блок идентификации ключевых слов
"""


def identify_pascal(identifier: str):
    """
    Устанавливает, какому из ключевых слов языка Pascal соответствует заданный идентификатор.
    :param identifier:идентификатор, по которому следует установить соответствие ключевому слову языка Pascal.
    :return: В случае, если идентификатор совпадает с ключевым словом Pascal,
    возвращает строку “КЛСЛОВО_<ИДЕНТИФИКАТОР>”, где на месте <ИДЕНТИФИКАТОР> находится identifier.
    В ином случае, возвращает identifier.

    """
    keywords = ('and', 'array', 'begin', 'case', 'const', 'div', 'do', 'downto', 'else', 'end', 'file', 'for',
                'function', 'goto', 'if', 'in', 'label', 'mod', 'nil', 'not', 'of', 'or', 'packed', 'procedure',
                'program', 'record', 'repeat', 'set', 'then', 'to', 'type', 'until', 'var', 'while', 'with')
    if identifier in keywords:
        return True
    else:
        return False


def identify_stdtype(word: str):
    stdtype_words = ('boolean', 'byte', 'char', 'integer', 'longint', 'real', 'string', 'word')
    if word in stdtype_words:
        return True
    else:
        return False
