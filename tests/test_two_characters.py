import unittest
from coe_number.two_characters import alternate


class TwoCharactersTest(unittest.TestCase):
    def test_give_beabeefeab_should_return_5(self):
        # Arrange: จากสตริงนี้ คู่ 'a' และ 'b' จะให้ "ababa" ยาว 5
        s = "beabeefeab"
        # Act
        result = alternate(s)
        # Assert
        self.assertEqual(result, 5)

    def test_give_aaaaa_should_return_0(self):
        # Arrange: มีตัวเดียว ไม่สามารถสร้างคู่สลับได้
        s = "aaaaa"
        result = alternate(s)
        self.assertEqual(result, 0)

    def test_give_abc_should_return_2(self):
        # Arrange: เลือก 'a', 'b' หรือ 'b', 'c' จะได้ความยาว 2
        s = "abc"
        result = alternate(s)
        self.assertEqual(result, 2)

    def test_give_complex_invalid_should_return_0(self):
        # Arrange: เคสที่ไม่สามารถสร้างคู่สลับได้เลย
        s = "aabb"
        result = alternate(s)
        self.assertEqual(result, 0)
