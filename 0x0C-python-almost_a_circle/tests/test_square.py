import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_str(self):
        s = Square(3, 1, 2, 42)
        self.assertEqual(str(s), "[Square] (42) 1/2 - 3")


if __name__ == '__main__':
    unittest.main()
