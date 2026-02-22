import unittest
from coe_number.staircase import staircase


class StaircaseTest(unittest.TestCase):
    def test_give_2_and_hash_should_return_staircase(self):
        # Arrange
        n = 2
        display = "#"
        expected_output = " #\n##"
        # Act
        result = staircase(n, display)
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_n_more_than_30_should_return_out_of_range(self):
        n = 31
        display = "#"
        result = staircase(n, display)
        self.assertEqual(result, "Out of range")
