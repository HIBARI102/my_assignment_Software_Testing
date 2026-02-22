import unittest
from coe_number.alternating_characters import alternatingCharacters


class AlternatingCharactersTest(unittest.TestCase):
    def test_give_AAAA_should_return_3(self):
        # Arrange: ต้องลบ A ออก 3 ตัวเพื่อให้เหลือ A ตัวเดียว
        s = "AAAA"
        # Act
        result = alternatingCharacters(s)
        # Assert
        self.assertEqual(result, 3)

    def test_give_ABCDE_should_return_0(self):
        # Arrange: ไม่ซ้ำเลย ไม่ต้องลบ
        s = "ABCDE"
        result = alternatingCharacters(s)
        self.assertEqual(result, 0)

    def test_give_ABABAB_should_return_0(self):
        # Arrange: สลับกันอยู่แล้ว ไม่ต้องลบ
        s = "ABABAB"
        result = alternatingCharacters(s)
        self.assertEqual(result, 0)

    def test_give_AAABBB_should_return_4(self):
        # Arrange: ลบ A 2 ตัว ลบ B 2 ตัว รวมเป็น 4
        s = "AAABBB"
        result = alternatingCharacters(s)
        self.assertEqual(result, 4)
