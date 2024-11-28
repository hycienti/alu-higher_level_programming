#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unit tests for the max_integer function"""

    def test_ordered_list(self):
        """Test a list with ordered integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list with unordered integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element_list(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        """Test a list with both positive and negative numbers"""
        self.assertEqual(max_integer([-10, 0, 5, 3]), 5)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test a list with floating-point numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5, 3.5]), 3.5)

    def test_mixed_floats_and_integers(self):
        """Test a list with both integers and floating-point numbers"""
        self.assertEqual(max_integer([1.5, 2, 3.5, 2.5]), 3.5)

    def test_all_same_elements(self):
        """Test a list where all elements are the same"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_max_at_beginning(self):
        """Test a list where the max value is at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_at_end(self):
        """Test a list where the max value is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_string_elements(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_mixed_string_and_numbers(self):
        """Test a list with both strings and numbers"""
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])

    def test_none_argument(self):
        """Test with None as input"""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
