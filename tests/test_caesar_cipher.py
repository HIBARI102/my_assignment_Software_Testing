import unittest
from coe_number.caesar_cipher import caesarCipher


class CaesarCipherTest(unittest.TestCase):
    def test_give_middle_Outz_with_k_2_should_return_okff_Qwbg(self):
        # Arrange: ทดสอบตัวพิมพ์เล็ก พิมพ์ใหญ่ และอักขระพิเศษ (-)
        s = "middle-Outz"
        k = 2
        expected_output = "okffng-Qwbg"
        # Act
        result = caesarCipher(s, k)
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_Always_Look_with_k_87_should_return_Fqbfdx_Qtpp(self):
        # Arrange: ทดสอบกรณี k > 26 (87 % 26 = 9)
        s = "Always-Look-on-the-Bright-Side-of-Life"
        k = 87
        expected_output = "Fqbfdx-Qtpp-xw-ymj-Gwnlmy-Xnij-tk-Qnkj"
        # Act
        result = caesarCipher(s, k)
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_empty_string_should_return_empty(self):
        # Arrange: เคสสตริงว่าง
        s = ""
        k = 5
        result = caesarCipher(s, k)
        self.assertEqual(result, "")
