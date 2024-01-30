import unittest
from set_CMV import *


class TestDecide(unittest.TestCase):
    def test_cmv_0(self):
        # Define test parameters (should probably be moved to JSON test file later)
        parameters = {}
        parameters["length1"] = 2

        num_points = 5

        datapoints_1 = [(0,0),(1,1),(2,2),(3,3),(4,4)]
        datapoints_2 = [(0,0),(3,4),(0,0),(0,0),(0,0)]
        datapoints_3 = [(-1,0),(-3,0),(0,0),(1,0),(3,0)]

        # Test computational logic in set_CMV_0 function
        self.assertFalse(set_CMV_0(num_points, datapoints_1, parameters), "CMV_0: Maximum distance is smaller than parameter LENGTH1")
        self.assertTrue(set_CMV_0(num_points, datapoints_2, parameters), "CMV_0: Maximum distance is larger than parameter LENGTH1")
        self.assertTrue(set_CMV_0(num_points, datapoints_3, parameters), "CMV_0: Maximum distance is larger than parameter LENGTH1")
    
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

    def test_cmv_11(self):
        # Define test parameters (should probably be moved to JSON test file later)
        parameters = {
            "gpts" : 4
        }

        num_points = 10
        num_points_less = 1

        datapoints_1 = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0)]
        datapoints_2 = [(0,0),(3,0),(5,0),(6,0),(1,0),(2,0),(8,0),(9,0),(10,0),(0,0)]
        datapoints_3 = [(-1,0),(-2,0),(-3,0),(0,0),(1,0),(2,0),(0,0),(0,0),(0,0),(0,0)]

        # Test computational logic in set_CMV_11 function
        self.assertFalse(set_CMV_11(num_points, datapoints_1, parameters), "test_cmv_11: x vector is only increasing")
        self.assertTrue(set_CMV_11( num_points, datapoints_2, parameters), "test_cmv_11: x vector includes correct set of datapoints")
        self.assertTrue(set_CMV_11( num_points, datapoints_3, parameters), "test_cmv_11: x vector includes correct set of datapoints")
        self.assertFalse(set_CMV_11(num_points_less, datapoints_2, parameters), "test_cmv_11: NUMPOINTS less than 3")

    def test_cmv_2(self):
        """ 
        Tests the behavior of the set_cmv_2 function which should return true iff there exists
        three consecutive points s.t. the angle that they create is < PI - EPSILON or > PI - EPSILON
        """        
        # Creates an angle of 0.5236
        # 0.5236 < pi - 2
        datapoints_1 = [(-2.0, -1.0), (1.0, np.sqrt(3)), (0.0, 0.0), (np.sqrt(3), 1.0), (-3.0, -3.0)]
        parameters_1 = {"epsilon" : 2}

        # Creates an angle of −1.5708
        # -1.5708 !< pi - 5
        datapoints_2 = [(1.0, 1.0), (0.0, 0.0), (1.0, -1.0)]
        parameters_2 = {"epsilon" : 5}

        # Creates an angle of pi
        # pi !> pi + 0
        datapoints_3 = [(-1.0, -1.0), (0.0, 0.0), (1.0, 1.0)]
        parameters_3 = {"epsilon" : 0}

        # Creates an angle of 2.3562
        # 2.3562 < pi - 0.1
        datapoints_4 = [(-1.0, -2.0), (-2.0, 0.0), (0.0, 0.0), (1.0, 1.0), (-22.3, 22.0)]
        parameters_4 = {"epsilon" : 0.1}
        
        self.assertTrue(set_CMV_2(len(datapoints_1), datapoints_1, parameters_1))
        self.assertFalse(set_CMV_2(len(datapoints_2), datapoints_2, parameters_2))
        self.assertFalse(set_CMV_2(len(datapoints_3), datapoints_3, parameters_3))
        self.assertTrue(set_CMV_2(len(datapoints_4), datapoints_4, parameters_4))

if __name__ == '__main__':
    unittest.main()