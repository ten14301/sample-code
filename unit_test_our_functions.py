import unittest

import our_functions

class date_format(unittest.TestCase):
    def test_correct_date_format(self):
        date_str = "2023-03-15"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)


if __name__ == "__main__":
    unittest.main()