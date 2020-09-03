import unittest
from WayTooLong800 import reduce


class WayTooLongTestCase(unittest.TestCase):
    """Tests for the way too long problem"""

    def test_function(self):
        result = reduce("pneumonoultramicroscopicsilicovolcanoconiosis")
        self.assertEqual(result, "p43s")


if __name__ == "__main__":
    unittest.main()
