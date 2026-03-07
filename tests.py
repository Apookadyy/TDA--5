import unittest
from unit import TestUnitFunctions
from integration import TestIntegration
from performance import TestPerformance

if __name__ == "__main__":
    suite = unittest.TestSuite()

    # Add unit tests
    suite.addTest(unittest.makeSuite(TestUnitFunctions))

    # Add integration tests
    suite.addTest(unittest.makeSuite(TestIntegration))

    # Add performance tests
    suite.addTest(unittest.makeSuite(TestPerformance))

    runner = unittest.TextTestRunner()
    runner.run(suite)