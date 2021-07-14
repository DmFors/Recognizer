import unittest

from syntax_unit import check_the_formula


class SyntaxTests(unittest.TestCase):
    def test_chain(self):
        self.assertEqual(check_the_formula([['type', 'идент'],
                                            ['arr', 'идент'],
                                            ['=', 'равно'],
                                            ['array', 'идент'],
                                            ['[', 'лвскобка'],
                                            ['-', 'знак'],
                                            ['1', 'целое'],
                                            ['/', 'бинзнак'],
                                            ['min', 'идент'],
                                            ['..', 'идент'],
                                            ['+', 'знак'],
                                            ['1', 'целое'],
                                            ['*', 'бинзнак'],
                                            ['max', 'идент'],
                                            [']', 'прскобка'],
                                            ['of', 'идент'],
                                            ['char', 'идент'],
                                            [';', 'тчкзпт']]), "ACCEPT")


if __name__ == '__main__':
    unittest.main()
