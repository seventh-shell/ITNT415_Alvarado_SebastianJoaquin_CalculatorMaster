import unittest

from calculator import divide, multiply, subtract


class TestSubtraction(unittest.TestCase):
    def test_positive_result(self):
        self.assertEqual(subtract(7, 3), 4)

    def test_negative_result(self):
        self.assertEqual(subtract(3, 7), -4)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3)

    def test_equal_numbers(self):
        self.assertEqual(subtract(4, 4), 0)


class TestMultiplication(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_negative_number(self):
        self.assertEqual(multiply(-3, 4), -12)

    def test_zero(self):
        self.assertEqual(multiply(0, 5), 0)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(multiply(1.5, 2.2), 3.3)


class TestDivision(unittest.TestCase):
    def test_exact_result(self):
        self.assertEqual(divide(8, 2), 4)

    def test_fractional_result(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_negative_number(self):
        self.assertEqual(divide(-8, 2), -4)

    def test_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()