import unittest

from calculator import subtract


class TestSubtraction(unittest.TestCase):
    def test_positive_result(self):
        self.assertEqual(subtract(7, 3), 4)

    def test_negative_result(self):
        self.assertEqual(subtract(3, 7), -4)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3)

    def test_equal_numbers(self):
        self.assertEqual(subtract(4, 4), 0)


if __name__ == "__main__":
    unittest.main()