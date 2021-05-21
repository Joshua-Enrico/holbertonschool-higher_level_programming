#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for Test Max Integer"""

    def test_documentation(self):
        """Modules and functions must be documented"""
        self.assertTrue(len(__import__("6-max_integer").__doc__) > 0)

        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_positives(self):
        """only positive"""
        self.assertEqual(max_integer([1, 3, 5, 7]), 7)

        self.assertEqual(max_integer([-100, 34, 55, 0]), 55)

        self.assertEqual(max_integer([-100, 34, 55, 0]), 55)

        test = [1.1, 2.2, 3.3, 4.4]
        self.assertEqual(max_integer(test), 4.4)

        test = [1.1, -2.2, 3.3, 32]
        self.assertEqual(max_integer(test), 32)

        test = [32, -2.2, 3.3, 1.1]
        self.assertEqual(max_integer(test), 32)

        test = [32, 32, 32, 100]
        self.assertEqual(max_integer(test), 100)

        test = [10 + 10, 3 - 2, 7 + 5, 23]
        self.assertEqual(max_integer(test), 23)

        test = [146, 1000, 1000 * 2, 1.1]
        self.assertEqual(max_integer(test), 2000)

        test = [32, 32, 32, 32]
        self.assertEqual(max_integer(test), 32)

        test = [32, -2.2, 55555555,  -55555555]
        self.assertEqual(max_integer(test), 55555555)

        test_list = [[1, 2, 3, 4], [4, 3, 2, 1]]
        self.assertEqual(max_integer(test_list), [4, 3, 2, 1])

        test_list = ((1, 2, 3, 4), (4, 3, 2, 1))
        self.assertEqual(max_integer(test_list), (4, 3, 2, 1))

    def test_negatives(self):
        """only negative"""
        self.assertEqual(max_integer([-1, -3, -5, -7]), -1)

        test = [-1.1, -2.2, -3.3, -4.4]
        self.assertEqual(max_integer(test), -1.1)

        test = [-1.1, -2.2, -3.3, -32]
        self.assertEqual(max_integer(test), -1.1)

        test = [-32, -2.2, -3.3, -1.1]
        self.assertEqual(max_integer(test), -1.1)

        test = [-32, -32, -32, -100]
        self.assertEqual(max_integer(test), -32)

        test = [-10 + 10, -3 - 2, -7 + 5, -23]
        self.assertEqual(max_integer(test), 0)

        test = [-146, -1000, -1000 * 2, -1.1]
        self.assertEqual(max_integer(test), -1.1)

        test = [-32, -32, -32, -32]
        self.assertEqual(max_integer(test), -32)

        test_list = [[-1, -2, -3, -4], [-4, -5, -2, -1]]
        self.assertEqual(max_integer(test_list), [-1, -2, -3, -4])

        test_list = ((-1, -2, -33, -4), (-4, -3, -2, -1))
        self.assertEqual(max_integer(test_list), (-1, -2, -33, -4))

    def test_mixed(self):
        """positive and negative"""
        self.assertEqual(max_integer([-1, 3, 5, -7]), 5)

        test = [1.1, -2.2, 3.3, -4.4]
        self.assertEqual(max_integer(test), 3.3)

        test = [1.1, -2.2, 3.3, -32]
        self.assertEqual(max_integer(test), 3.3)

        test = [-32, 2.2, -3.3, 1.1]
        self.assertEqual(max_integer(test), 2.2)

        test = [-32, 32, -32, 100]
        self.assertEqual(max_integer(test), 100)

        test = [10 + 10, -3 - 2, 7 + 5, -23]
        self.assertEqual(max_integer(test), 20)

        test = [-146, 1000, 1000 * 2, -1.1]
        self.assertEqual(max_integer(test), 2000)

        test = [32, -32, 32, -32]
        self.assertEqual(max_integer(test), 32)

    def test_not_list(self):
        """Testing incorrect types"""

        test_list = [1, 2, "bob", 46]
        self.assertRaises(TypeError)

        test_list = [1, 2, [3], 46]
        self.assertRaises(TypeError)

        test_list = [1, 2, float('inf'), 46]
        self.assertRaises(TypeError)

        test_list = []
        self.assertRaises(TypeError)

        test_list = [1, 2, True, 46]
        self.assertRaises(TypeError)

        test_list = {1, 2, 3, 4}
        self.assertRaises(TypeError)

        test_list = "aeraekz"
        self.assertEqual(max_integer(test_list), 'z')

        test_list = None
        self.assertRaises(TypeError)

if __name__ == '__main__':
    unittest.main()
