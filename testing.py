def take_test_data(filename):
    test_data = inp_data(filename).split("\n")
    return list(map(lambda a: a.split("\t"), test_data))


def print_table(head, form, rows):
    print(head)
    for row in rows:
        row = form.format(*row)
        print(row)


def test_transl_unit():
    test_data = take_test_data("TEST_TRANSL_UNIT.txt")
    test_table = []
    for data in test_data:
        chain = data[0]
        correct_result = data[1]
        transl_result = transliteration(chain)[0][1]
        if transl_result != correct_result:
            print(f"Test translation error:\n\tchain: {chain}\n\toutput: {transl_result}\n\tcorrect: {correct_result}")


if __name__ == '__main__':
    from io_unit import *
    from transl_unit import *
    test_transl_unit()
