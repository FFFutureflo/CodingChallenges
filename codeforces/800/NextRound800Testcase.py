import unittest
from NextRound800 import function


class NextCaseTestCase(unittest.TestCase):
    """Tests for the next case problem"""

    def test_function(self):
        result = function(5, 5, [1, 1, 1, 1, 1])
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
