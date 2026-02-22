import unittest
from coe_number.fizzbuzz import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    def test_give_3_should_return_fizz(self):
        # Arrange
        x = 3
        # Act
        result = fizzbuzz(x)
        # Assert
        self.assertEqual(result, "Fizz")

    def test_give_5_should_return_buzz(self):
        x = 5
        result = fizzbuzz(x)
        self.assertEqual(result, "Buzz")

    def test_give_15_should_return_fizzbuzz(self):
        x = 15
        result = fizzbuzz(x)
        self.assertEqual(result, "FizzBuzz")

    def test_give_2_should_return_2(self):
        x = 2
        result = fizzbuzz(x)
        self.assertEqual(result, "2")
