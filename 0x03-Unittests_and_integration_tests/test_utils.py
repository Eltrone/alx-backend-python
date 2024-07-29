#!/usr/bin/env python3
"""Module for testing the utility functions."""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json, access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the correct result."""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that a KeyError is raised for given inputs."""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), repr(path[-1]))

class TestGetJson(unittest.TestCase):
    """Tests for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected result without making HTTP calls."""
        with patch('requests.get') as mocked_get:
            mocked_get.return_value = Mock(json=lambda: test_payload)
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mocked_get.assert_called_once_with(test_url)

if __name__ == '__main__':
    unittest.main()
