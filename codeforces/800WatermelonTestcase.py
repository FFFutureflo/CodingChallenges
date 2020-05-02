import unittest
from Watermelon800 import function


class WatermelonTestCase(unittest.TestCase):
    """Tests for the watermelon problem"""

    def test_function(self):
        result = function(10)
        self.assertEqual(result, "YES")


if __name__ == "__main__":
    unittest.main()
