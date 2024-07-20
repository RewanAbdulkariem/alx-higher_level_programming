import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_id_auto_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_custom_id(self):
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_from_json_string(self):
        json_string = Base.from_json_string(None)
        self.assertEqual(json_string, [])

    def test_save_to_file(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists('Rectangle.json'))

    def test_load_from_Nonexistance_file(self):
        self.assertEqual(Base.load_from_file(), [])

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(
            len(list_rectangles_input), len(list_rectangles_output))


if __name__ == '__main__':
    unittest.main()
