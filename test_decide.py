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

    
 


    def test_cmv_1_equal_points(self):
        """
        Given a set of three points where two are equal and where the
        euclidean distance between the differing points is 2, 
        the points can be encompassed by a circle of radius 1.
        """
        parameters = {}
        parameters["radius1"] = 1
        datapoints = [(0.0, 0.0), (0.0, 0.0), (0.0, 2.0)]
        num_points = len(datapoints)
        self.assertFalse(set_CMV_1(num_points, datapoints, parameters))

    def test_cmv_1_collinear(self):
        """
        Given a set of three collinear points, the points should not 
        be able to be contained by a circle.
        """
        parameters = {}
        parameters["radius1"] = 0.5
        datapoints = [(1.0, 1.0), (2.0, 2.0), (3.0, 3.0)]
        num_points = len(datapoints)
        self.assertFalse(set_CMV_1(num_points, datapoints, parameters))

    def test_cmv_1(self):
        """
        The points (1, 0), (-1, 0), and (0, 1) should be contained a by a circle
        with radius 1. set_CMV_1 should therefore be true with RADIUS set to 0.5
        but not when RADIUS is set to 1. 
        """
        parameters = {}
        parameters["radius1"] = 0.5
        datapoints = [(0.0, 0.0), (1.0, 0.0), (-1.0, 0.0), (0.0, 1.0), (0.0, 0.0)]
        num_points = len(datapoints)

        self.assertTrue(set_CMV_1(num_points, datapoints, parameters))
        parameters["radius1"] = 1
        self.assertFalse(set_CMV_1(num_points, datapoints, parameters))


    def test_cmv_9_too_few_datapoints(self):
        # Define test parameters
        parameters = {
            'cpts' : 2,
            'dpts' : 3,
            'epsilon' : np.pi/4
        }

        datapoints = [(0,0),(1,0),(2,0)]
        num_points = len(datapoints)

        # Test computational logic in set_CMV_9 function
        self.assertFalse(set_CMV_9(num_points, datapoints, parameters), "num_points is less than 5, not satisfactory")

    def test_cmv_9_only_angles_of_PI_radians(self):
        # Define test parameters
        parameters = {
            'cpts' : 2,
            'dpts' : 3,
            'epsilon' : 0
        }

        datapoints = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0)]
        num_points = len(datapoints)

        # Test computational logic in set_CMV_9 function
        self.assertFalse(set_CMV_9(num_points, datapoints, parameters), "All points are along a line Y=0, angle is always pi which is in forbidden range")
    
    def test_cmv_9_no_valid_angles(self):
        # Define test parameters
        parameters = {
            'cpts' : 3,
            'dpts' : 4,
            'epsilon' : np.pi/2 + 0.00001 # needs a threshold (we have an angle (PI/2) that is right on the edge of the invalid range PI±ε)
        }

        datapoints = [(-1,0),(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(4,9),(10,0)]
        num_points = len(datapoints)

        # Test computational logic in set_CMV_9 function
        self.assertFalse(set_CMV_9(num_points, datapoints, parameters), "One angle close to the edge of invalid range, but still invalid. THe rest are clearly invalid")

    def test_cmv_9_test_angles_close_to_unvalid_range(self):
        # Define test parameters
        parameters = {
            'cpts' : 3,
            'dpts' : 4,
            'epsilon' : np.pi/2
        }

        datapoints_0 = [(-1,0), (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(3,9),(10,0)]
        datapoints_1 = [(-1,0), (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(5,9),(10,0)]
        num_points = 12

        # Test computational logic in set_CMV_9 function
        self.assertTrue(set_CMV_9(num_points, datapoints_0, parameters), "One set have an angle slightly less than PI/2, is outside forbidden range PI±PI/2")
        self.assertFalse(set_CMV_9(num_points, datapoints_1, parameters), "All angles are PI exept on that is slightly greater than PI/2, still in forbidden range PI±PI/2")
        


if __name__ == '__main__':
    unittest.main()