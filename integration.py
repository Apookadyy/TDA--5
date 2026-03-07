import unittest
from src.api import fetch_data_from_api
from cache import cache_data

class TestIntegration(unittest.TestCase):

    def test_api_and_cache(self):
        data = fetch_data_from_api()

        cached = cache_data(data)

        self.assertIsNotNone(cached)
        self.assertEqual(data, cached)

    def test_full_pipeline(self):
        data = fetch_data_from_api()
        processed = [x*2 for x in data]

        self.assertTrue(len(processed) > 0)

if __name__ == "__main__":
    unittest.main()