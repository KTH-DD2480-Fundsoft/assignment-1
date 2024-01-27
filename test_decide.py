import unittest
from set_CMV import *

class TestDecide(unittest.TestCase):
    def test_cmv_0(self):
        pass

    def test_cmv_11(self):
        # Define test parameters (should probably be moved to JSON test file later)
        G_PTS = 4
        NUMPOINTS = 10
        NUMPOINTS_less = 1
        y   = [0,0,0,0,0,0,0,0,0,0]
        x_1 = [0,1,2,3,4,5,6,7,8,9]
        x_2 = [0,3,5,6,1,2,8,9,10,0]
        x_3 = [-1,-2,-3,0,1,2,0,0,0,0]
        

        x_short = [0]

        # Test computational logic in set_CMV_11 function
        self.assertFalse(set_CMV_11(G_PTS,NUMPOINTS,x_1,y), "test_cmv_11: x vector is only increasing")
        self.assertTrue(set_CMV_11(G_PTS,NUMPOINTS,x_2,y), "test_cmv_11: x vector includes correct set of datapoints")
        self.assertTrue(set_CMV_11(G_PTS,NUMPOINTS,x_3,y), "test_cmv_11: x vector includes correct set of datapoints")
        self.assertFalse(set_CMV_11(G_PTS,NUMPOINTS_less,x_2,y), "test_cmv_11: NUMPOINTS less than 3")

        # Test built-in assertions in set_CMV_0 function
        with self.assertRaises(AssertionError):   # Tests that length of x vector equal to NUMPOINTS int
            set_CMV_11(G_PTS,NUMPOINTS,x_short,y)
        G_PTS_str = "4"
        with self.assertRaises(AssertionError):   # Tests that G_PTS variable is an int
            set_CMV_11(G_PTS_str,NUMPOINTS,x_short,y)
        NUMPOINTS_str = "10"
        with self.assertRaises(TypeError):        # Tests that NUMPOINTS variable is an int
            set_CMV_11(G_PTS,NUMPOINTS_str,x_short,y)
        with self.assertRaises(AssertionError):   # Tests that G_PTS is between 1 and NUMPOINTS-2
            set_CMV_11(G_PTS,NUMPOINTS,x_short,y)


if __name__ == '__main__':
    unittest.main()