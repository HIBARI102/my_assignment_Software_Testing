import unittest
from coe_number.cat_mouse import cat_mouse


class CatMouseTest(unittest.TestCase):
    def test_cat_a_closer_should_return_cat_a(self):
        # Arrange (Cat A อยู่ที่ 1, Cat B อยู่ที่ 5, หนู อยู่ที่ 2)
        x, y, z = 1, 5, 2
        # Act
        result = cat_mouse(x, y, z)
        # Assert
        self.assertEqual(result, "Cat A")

    def test_cat_b_closer_should_return_cat_b(self):
        x, y, z = 1, 5, 4
        result = cat_mouse(x, y, z)
        self.assertEqual(result, "Cat B")

    def test_both_cats_same_distance_should_return_mouse_c(self):
        x, y, z = 1, 3, 2
        result = cat_mouse(x, y, z)
        self.assertEqual(result, "Mouse C")
