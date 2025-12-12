import unittest
import math

from geometric_lib import rectangle
from geometric_lib import circle
from geometric_lib import square
from geometric_lib import triangle


class TestGeometry(unittest.TestCase):

    # --- RECTANGLE TESTS ---
    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(3, 4), 12)
        self.assertAlmostEqual(rectangle.area(2.5, 4), 10.0)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(3, 4), 14)
        self.assertEqual(rectangle.perimeter(5, 5), 20)

    def test_rectangle_invalid_input(self):
        # строки
        with self.assertRaises(TypeError):
            rectangle.area("3", 4)
        with self.assertRaises(TypeError):
            rectangle.perimeter(3, "4")

        # отрицательные значения
        with self.assertRaises(ValueError):
            rectangle.area(-1, 5)
        with self.assertRaises(ValueError):
            rectangle.perimeter(3, -2)

    # --- SQUARE TESTS ---
    def test_square_area(self):
        self.assertEqual(square.area(5), 25)
        self.assertAlmostEqual(square.area(2.5), 6.25)

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)
        self.assertAlmostEqual(square.perimeter(2.5), 10.0)

    def test_square_invalid_input(self):
        with self.assertRaises(TypeError):
            square.area("5")
        with self.assertRaises(TypeError):
            square.perimeter("abc")

        with self.assertRaises(ValueError):
            square.area(-5)
        with self.assertRaises(ValueError):
            square.perimeter(-1)

    # --- TRIANGLE TESTS ---
    def test_triangle_area(self):
        self.assertEqual(triangle.area(10, 2), 10)
        self.assertAlmostEqual(triangle.area(3, 4), 6)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
        self.assertAlmostEqual(triangle.perimeter(2.5, 3.5, 4), 10.0)

    def test_triangle_invalid_input(self):
        with self.assertRaises(TypeError):
            triangle.area("3", 4)
        with self.assertRaises(TypeError):
            triangle.perimeter(3, "4", 5)

        with self.assertRaises(ValueError):
            triangle.area(-3, 4)
        with self.assertRaises(ValueError):
            triangle.perimeter(3, -4, 5)

    # --- CIRCLE TESTS ---
    def test_circle_area(self):
        self.assertAlmostEqual(circle.area(1), math.pi * 1 * 1)
        self.assertAlmostEqual(circle.area(2.5), math.pi * 2.5 * 2.5)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi * 1)
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5)

    def test_circle_invalid_input(self):
        with self.assertRaises(TypeError):
            circle.area("radius")
        with self.assertRaises(TypeError):
            circle.perimeter("5")

        with self.assertRaises(ValueError):
            circle.area(-1)
        with self.assertRaises(ValueError):
            circle.perimeter(-10)


if __name__ == "__main__":
    unittest.main()
