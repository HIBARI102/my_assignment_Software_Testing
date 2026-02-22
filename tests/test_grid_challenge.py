import unittest
from coe_number.grid_challenge import gridChallenge


class GridChallengeTest(unittest.TestCase):
    def test_give_sorted_grid_should_return_yes(self):
        # Arrange: ตารางที่เมื่อเรียงแถวแล้ว คอลัมน์จะเรียงด้วย
        # abc
        # hjk
        # mpq
        grid = ["abc", "hjk", "mpq"]
        # Act
        result = gridChallenge(grid)
        # Assert
        self.assertEqual(result, "YES")

    def test_give_unsorted_column_should_return_no(self):
        # Arrange: แถวเรียงแล้ว แต่คอลัมน์แรก 'e' มากกว่า 'a' (พังที่คอลัมน์)
        # e b c
        # a d f
        grid = ["ebc", "adf"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")

    def test_give_single_row_should_return_yes(self):
        # Arrange: ตารางแถวเดียว ยังไงก็ต้อง YES
        grid = ["zyx"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_give_square_grid_no_should_return_no(self):
        # Arrange: เคสจาก HackerRank
        grid = ["mpxz", "abcd", "wlrb"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")
