import unittest
import time
from src.api import process_large_dataset

class TestPerformance(unittest.TestCase):

    def test_processing_speed(self):
        data = list(range(100000))

        start_time = time.time()

        process_large_dataset(data)

        end_time = time.time()

        execution_time = end_time - start_time

        print("Execution Time:", execution_time)

        self.assertLess(execution_time, 5)

if __name__ == "__main__":
    unittest.main()