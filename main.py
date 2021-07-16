from io_unit import *
from lexical_unit import *
from syntax_unit import *
from transl_unit import *


def main():
    filename_inp = "INPUT.TXT"
    filename_out = "OUTPUT.TXT"
    chains = list(map(str.lower, inp_data(filename_inp)))
    chains = list(map(str.strip, chains))
    out_data(filename_out, f"{'-' * 10} start of test results {'-' * 10}")
    for chain in chains:
        # try:
        chain_characters = transliteration(chain)
        right_lexemes = to_lexemes(chain_characters)
        result = check_the_formula(right_lexemes)
        out_data(filename_out, result)
        # except KeyError:
        #     out_data(filename_out, "REJECT")
        # except KeywordError:
        #     out_data(filename_out, "REJECT")
    out_data(filename_out, f"{'-' * 10} end of test results {'-' * 10}")


if __name__ == '__main__':
    main()
