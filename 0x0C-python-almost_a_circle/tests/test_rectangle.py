import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(3, 4, 1, 2, 42)
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 3/4")


if __name__ == '__main__':
    unittest.main()
