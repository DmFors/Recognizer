import unittest

from main import *
from io_unit import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print(f"Running {self.id()} test")

    def tearDown(self) -> None:
        print(f"End of {self.id()} test")

    def test_something(self):
        out_data(filename_out, f"{'-' * 10} start of test results {'-' * 10}")
        for chain in chains:
            try:
                main()
            except KeyError:
                out_data(filename_out, "REJECT")
            except KeywordError:
                out_data(filename_out, "REJECT")
        out_data(filename_out, f"{'-' * 10} end of test results {'-' * 10}")
        answers = ("ACCEPT", "ACCEPT", "ACCEPT", "REJECT")
        with open("INPUT.TXT", "r", encoding="UTF-8") as file_inp:
            with open("OUTPUT.TXT", "w", encoding="UTF-8") as file_out:
                for _ in range(len(answers)):
                    main()
                for answer in answers:
                    self.assertEqual()


if __name__ == '__main__':
    unittest.main()
