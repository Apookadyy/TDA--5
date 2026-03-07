import unittest
from src.api import process_data

class TestUnitFunctions(unittest.TestCase):

    def test_process_data(self):
        data = [1, 2, 3, 4]
        result = process_data(data)

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 4)

    def test_empty_input(self):
        data = []
        result = process_data(data)

        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()