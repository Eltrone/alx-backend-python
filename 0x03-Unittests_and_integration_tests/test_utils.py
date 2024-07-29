import unittest
from utils import access_nested_map, get_json, memoize

class TestUtils(unittest.TestCase):

    def test_access_nested_map_valid(self):
        """ Test access_nested_map with a valid path. """
        nested_map = {"a": {"b": {"c": 1}}}
        path = ["a", "b", "c"]
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, 1)

    def test_access_nested_map_invalid(self):
        """ Test access_nested_map with an invalid path. """
        nested_map = {"a": {"b": {"c": 1}}}
        path = ["a", "b", "d"]
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

    def test_get_json(self):
        """ Test get_json function. """
        # This test requires a live request so normally you would mock this.
        # For this example, we will assume the function can be called as is.
        url = "https://api.github.com"  # Example URL
        result = get_json(url)
        self.assertIn('current_user_url', result)

    def test_memoize(self):
        """ Test memoize decorator. """
        class MyClass:
            def __init__(self):
                self.count = 0

            @memoize
            def count_method(self):
                self.count += 1
                return self.count

        my_instance = MyClass()
        first_call = my_instance.count_method
        second_call = my_instance.count_method
        self.assertEqual(first_call, 1)
        self.assertEqual(second_call, 1)  # Should not increment count because it's memoized

if __name__ == '__main__':
    unittest.main()
