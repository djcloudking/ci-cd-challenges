import unittest
from app import process_data
import pandas as pd

class TestProcessData(unittest.TestCase):
    def test_process_data(self):
        data = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
        result = process_data(data)
        self.assertTrue(result is not None)

if __name__ == '__main__':
    unittest.main()
