#!../../env/bin/python
import unittest
import pandas as pd
import pandas_missing_extension


# UN DATA FRAME PARA TESTEAR
DF_TEST_MISSIGN = pd.DataFrame.from_dict(
    data = {
        "a": list("asdafsdafa"),
        "b": range(0, 10)
    }
)
DF_TEST_MISSIGN.iloc[2:5, 0] = None
DF_TEST_MISSIGN.iloc[6:7, 1] = None


class TestMissingMethods(unittest.TestCase):

    def test_na_count(self):
        self.assertEqual(DF_TEST_MISSIGN.missing.na_count(), 4)
    
    def test_arged_na_count(self):
        self.assertEqual(DF_TEST_MISSIGN.missing.na_count("a"), 3)

    def test_na_proportion(self):
        self.assertEqual(DF_TEST_MISSIGN.missing.na_proportion(), 0.2)

    def test_na_percentage(self):
        self.assertEqual(DF_TEST_MISSIGN.missing.na_percentage(), 20)

    def test_not_na_proportion(self):
        self.assertEqual(DF_TEST_MISSIGN.missing.not_na_proportion(), 0.8)

    def test_not_na_percentage(self):
        self.assertEqual(DF_TEST_MISSIGN.missing.not_na_percentage(), 80)

    def test_variable_summary(self):
        wanted = pd.DataFrame.from_dict({
            "variable": ("a", "b"),
            "n_cases": (10, 10),
            "n_nas": (3, 1),
            "n_availables": (7, 9),
            "na_proportion": (0.3, 0.1),
            "na_percentage": (30.0, 10.0)
        })
        self.assertEqual(DF_TEST_MISSIGN.missing.variable_summary().to_dict(), wanted.to_dict())

if __name__ == "__main__":
    print(DF_TEST_MISSIGN)
    unittest.main()