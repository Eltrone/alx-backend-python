#!/usr/bin/env python3
"""Module for testing the utility functions."""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test function with different scenarios."""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()