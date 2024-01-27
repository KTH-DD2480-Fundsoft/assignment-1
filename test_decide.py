import unittest
from set_CMV import *

class TestDecide(unittest.TestCase):
    def test_cmv_0(self):
        pass


    def test_cmv_10(self):
        # Define test parameters (should probably be moved to JSON test file later)

        parameters = {}
        parameters["epts"] = 2
        parameters["fpts"] = 3
        parameters["area1"] = 1        
        num_points = 10
        num_points_less = 6

        datapoints_0 = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        datapoints_1 = [(0,0),(0,0),(0,0),(2,0),(0,0),(2,0),(0,0),(0,2),(0,0),(0,2)]
        datapoints_2 = [(1,2),(0,0),(0,0),(1,3),(0,0),(0,0),(0,0),(2,2),(0,0),(0,0)]
        datapoints_3 = [(0,0),(-2,-3),(0,0),(0,0),(-5,1),(0,0),(0,0),(0,0),(1,2),(0,0)]

        #def set_CMV_10(num_points, datapoints, parameters):

        # Test computational logic in set_CMV_10 function
        self.assertFalse(set_CMV_10(num_points, datapoints_0, parameters))
        self.assertFalse(set_CMV_10(num_points, datapoints_2, parameters))
        self.assertTrue(set_CMV_10( num_points, datapoints_1, parameters))
        self.assertTrue(set_CMV_10( num_points, datapoints_3, parameters))

        # Change AREA1 to test comparative computations
        parameters["area1"] = 100
        self.assertFalse(set_CMV_10(num_points, datapoints_1, parameters))
        self.assertFalse(set_CMV_10(num_points, datapoints_3, parameters))

        # Test built-in assertions in set_CMV_10 function
        with self.assertRaises(AssertionError):   # Tests that NUMPOINTS-3 is larger than sum of E_PTS and F_PTS
            set_CMV_10(num_points_less, datapoints_0, parameters)
 


if __name__ == '__main__':
    unittest.main()