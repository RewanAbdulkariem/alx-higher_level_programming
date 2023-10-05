#!/usr/bin/python3
'''
Unittest for max_integer([..])
'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class SimpleTest(unittest.TestCase):
    '''
    unittest class for max_integer
    '''
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_list(self):
        self.assertEqual(max_integer([4, 2, 1, -9]), 4)
        self.assertEqual(max_integer([4, -2, 10, -5]), 10)
        self.assertEqual(max_integer([-4, -2, -10, -5]), -2)


if __name__ == '__main__':
    unittest.main()
