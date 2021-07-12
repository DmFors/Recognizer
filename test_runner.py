import unittest

import test_transl_unit
import test_lexical_unit


def add_to_suite(suite, test_case_class):
    suite.addTest(unittest.makeSuite(test_case_class))


TestSuite = unittest.TestSuite()
add_to_suite(TestSuite, test_transl_unit.TransliterationTests)
add_to_suite(TestSuite, test_lexical_unit.LexicalTests)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestSuite)
