import unittest
from coe_number.funny_string import funnyString


class FunnyStringTest(unittest.TestCase):
    def test_give_acxz_should_return_funny(self):
        # Arrange
        s = "acxz"
        # Act
        result = funnyString(s)
        # Assert
        self.assertEqual(result, "Funny")

    def test_give_bcxz_should_return_not_funny(self):
        # Arrange
        s = "bcxz"
        # Act
        result = funnyString(s)
        # Assert
        self.assertEqual(result, "Not Funny")

    def test_give_abcd_should_return_funny(self):
        # Arrange
        s = "abcd"
        # Act
        result = funnyString(s)
        # Assert
        self.assertEqual(result, "Funny")

    def test_give_empty_diff_chars_should_return_funny(self):
        # เคสตัวอักษรซ้ำ ผลต่างจะเป็น 0 ทั้งหมด
        s = "aaaaa"
        result = funnyString(s)
        self.assertEqual(result, "Funny")
