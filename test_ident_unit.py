import unittest

from ident_unit import identify_pascal, identify_stdtype


class IdentPascalTests(unittest.TestCase):
    def test_pascal(self):
        keywords_pascal = ('and', 'array', 'begin', 'case', 'const', 'div', 'do', 'downto', 'else', 'end', 'file',
                           'for',
                           'function', 'goto', 'if', 'in', 'label', 'mod', 'nil', 'not', 'of', 'or', 'packed',
                           'procedure',
                           'program', 'record', 'repeat', 'set', 'then', 'to', 'type', 'until', 'var', 'while', 'with')
        for word in keywords_pascal:
            self.assertEqual(identify_pascal(word), True)

    def test_not_pascal(self):
        self.assertEqual(identify_pascal("test_word"), False)
        self.assertEqual(identify_stdtype(""), False)


class IdentStdTests(unittest.TestCase):
    def test_stdtype(self):
        stdtype_words = ('boolean', 'byte', 'char', 'integer', 'longint', 'real', 'string', 'word')
        for word in stdtype_words:
            self.assertEqual(identify_stdtype(word), True)

    def test_not_stdtype(self):
        self.assertEqual(identify_stdtype("test_word"), False)
        self.assertEqual(identify_stdtype(""), False)


if __name__ == '__main__':
    unittest.main()
