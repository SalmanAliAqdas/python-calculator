"""Automated tests. Run with:  python -m unittest -v"""

import unittest

from calculator import evaluate, format_number


class CalculatorTests(unittest.TestCase):
    def calc(self, text, last=None):
        return evaluate(text, last)[0]

    def test_basic_operations(self):
        self.assertEqual(self.calc("5 + 3"), 8)
        self.assertEqual(self.calc("9 - 4"), 5)
        self.assertEqual(self.calc("6 * 7"), 42)
        self.assertEqual(self.calc("10 / 4"), 2.5)

    def test_extra_operations(self):
        self.assertEqual(self.calc("2 ** 3"), 8)
        self.assertEqual(self.calc("10 % 3"), 1)
        self.assertEqual(self.calc("10 // 3"), 3)
        self.assertEqual(self.calc("sqrt 16"), 4)

    def test_no_spaces_and_negatives(self):
        self.assertEqual(self.calc("2+2"), 4)
        self.assertEqual(self.calc("5 - -3"), 8)
        self.assertEqual(self.calc("-2 * 4"), -8)

    def test_ans(self):
        self.assertEqual(self.calc("ans * 2", last=21), 42)
        with self.assertRaises(ValueError):
            self.calc("ans + 1")

    def test_errors(self):
        for bad in ["5 / 0", "5 % 0", "5 // 0", "sqrt -4", "0 ** -1",
                    "-8 ** 0.5", "abc", "5 +"]:
            with self.assertRaises(ValueError, msg=bad):
                self.calc(bad)

    def test_huge_power(self):
        with self.assertRaises(ValueError):
            self.calc("10.5 ** 99999")

    def test_formatting(self):
        self.assertEqual(format_number(8.0), "8")
        self.assertEqual(format_number(3.333333333), "3.3333")


if __name__ == "__main__":
    unittest.main()
