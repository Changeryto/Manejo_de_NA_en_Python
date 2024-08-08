#!../../env/bin/python
import unittest
import pandas_missing_extension
from pandas_missing_extension import DF_TEST_MISSIGN
class TestMissingMethods(unittest.TestCase):

    def test_na_full_count(self):
        self.assertEqual(DF_TEST_MISSIGN.missing.na_full_count(), 4)

    def test_na_full_count(self):
        self.assertEqual(DF_TEST_MISSIGN.missing.not_na_full_count(), 16)

    def test_na_proportion(self):
        self.assertEqual(DF_TEST_MISSIGN.missing.na_proportion(), 0.2)

if __name__ == "__main__":
    unittest.main()