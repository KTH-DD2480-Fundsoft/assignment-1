import unittest
from set_CMV import *


class TestDecide(unittest.TestCase):
    def test_cmv_0(self):
        # Define test parameters (should probably be moved to JSON test file later)
        LENGTH1_1 = 2
        LENGTH1_2 = "2"
        x_1 = [0,1,2,3,4]
        y_1 = [0,1,2,3,4]
        x_2 = [0,3,0,0,0]
        y_2 = [0,4,0,0,0]
        x_3 = [-1,-3,0,1,3]
        y_3 = [0,0,0,0,0]
        x_short = [0]

        # Test computational logic in set_CMV_0 function
        self.assertFalse(set_CMV_0(LENGTH1_1, x_1, y_1), "CMV_0: Maximum distance is smaller than parameter LENGTH1")
        self.assertTrue(set_CMV_0(LENGTH1_1, x_2, y_2), "CMV_0: Maximum distance is larger than parameter LENGTH1")
        self.assertTrue(set_CMV_0(LENGTH1_1, x_3, y_3), "CMV_0: Maximum distance is larger than parameter LENGTH1")

        # Test built-in assertions in set_CMV_0 function
        with self.assertRaises(AssertionError):
            set_CMV_0(LENGTH1_2,x_1,x_2)
        with self.assertRaises(AssertionError):
            set_CMV_0(LENGTH1_1,x_short,x_2)


if __name__ == '__main__':
    unittest.main()