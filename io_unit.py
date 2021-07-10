"""
1.1 Блок Ввода/вывода
"""


def inp_data(filename: str):
    """
    Функция считывания данных из файла.
    :param filename: имя файла, из которого считывается исходная символьная цепочка
    :return: исходная символьная цепочка
    """
    import os
    if filename in os.listdir(path="."):
        with open(filename, "r") as f:
            return f.read()
    else:
        print("There is no file with this name!")
        exit(-1)


def out_data(filename: str, result: str):
    """
    Функция выведения данных в файл.
    :param filename: имя файла, в который выводится результат работы распознавателя
    :param result: результат работы распознавателя
    :return:
    """
    pass
