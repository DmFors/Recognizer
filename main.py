from io_unit import *
from lexical_unit import *
from syntax_unit import *
from transl_unit import *

if __name__ == '__main__':
    FILENAME_INP = "INPUT.TXT"
    FILENAME_OUT = "OUTPUT.TXT"
    chain = inp_data(FILENAME_INP).lower()
    chain_characters = transliteration(chain)
    chain_lexemes = to_lexemes(chain_characters)
    result = check_the_formula(chain_lexemes)
    out_data(FILENAME_OUT, result)
