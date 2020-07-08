import sys
import unittest
import tests.engineTests.test_lexical_analysis
import tests.engineTests.test_semantic_analysis
import tests.engineTests.test_symbol_table
import tests.engineTests.test_syntactical_analysis
import tests.engineTests.test_translator

def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromModule(tests.engineTests.test_lexical_analysis))
    suite.addTest(loader.loadTestsFromModule(tests.engineTests.test_semantic_analysis))
    suite.addTest(loader.loadTestsFromModule(tests.engineTests.test_symbol_table))
    suite.addTest(loader.loadTestsFromModule(tests.engineTests.test_syntactical_analysis))
    suite.addTest(loader.loadTestsFromModule(tests.engineTests.test_translator))

    runner = unittest.TextTestRunner()
    return 0 if runner.run(suite).wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(main())
