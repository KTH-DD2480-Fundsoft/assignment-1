import set_CMV
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

    def test_cmv_3(self): 
        ''' Tests the function set_CMV_3 which calculates the 
            LIC3 condition. This function passes two false instances
            (where there exists no triangle in any consecutive data points 
            of area greater than AREA1) and two true instances (where 
            there exists a triangle in consecutive datapoints where the 
            area is greater than AREA1).'''

        num_points = 9
        
        # TRUE case
        parameters_true1 = { 
            "AREA1" : 7 
        } 

        data_points_true1 = [ 
            (-1.0,-1.0),(3.0,3.0), (3.0,-1.0), 
            (0.0,-1.0), (1.0,-1.0), (2.0,-1.0), 
            (2.0,2.0), (1.0,1.0), (0.0,0.0),
        ]
        # TRUE case
        parameters_true2 = { 
            "AREA1" : 40 
        } 

        data_points_true2 = [ 
            (0.0,0.0), (10.0,10.0), (10.0,0.0), 
            (-1.0,1.0), (0.0,1.0), (1.0,1.0), 
            (-1.0,-1.0), (0.0,-1.0), (1.0,-1.0) 
        ]
        # FALSE case
        parameters_false1 = { 
            "AREA1" : 7 
        } 

        data_points_false1 = [ 
            (-1.0,1.0), (0.0,1.0), (1.0,1.0), 
            (-1.0,0.0), (0.0,0.0), (1.0,0.0), 
            (-1.0,-1.0), (0.0,-1.0), (1.0,-1.0) 
        ]
        # FALSE case
        parameters_false2 = { 
            "AREA1" : 10 
        } 

        data_points_false2 = [ 
            (-1.0,-1.0), (1.0,1.0), (0.0,0.0), 
            (0.0,-1.0), (1.0,-1.0), (2.0,-1.0), 
            (2.0,2.0), (3.0,3.0), (3.0,-1.0) 
        ]

        self.assertTrue(
            set_CMV.set_CMV_3(
                num_points,
                data_points_true1,
                parameters_true1 
            )
        )
        self.assertTrue(
            set_CMV.set_CMV_3(
                num_points,
                data_points_true2,
                parameters_true2 
            )
        )
        self.assertFalse(
            set_CMV.set_CMV_3(
                num_points,
                data_points_false1,
                parameters_false1 
            )
        )
        self.assertFalse(
            set_CMV.set_CMV_3(
                num_points,
                data_points_false2,
                parameters_false2 
            )
        )
    
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

    def test_cmv_5(self):
        # Define test parameters
        parameters = {}

        num_points = 5

        datapoints_1 = [(0,0),(1,1),(2,2),(3,3),(4,4)]
        datapoints_2 = [(0,0),(0,4),(0,0),(1,0),(0,0)]
        datapoints_3 = [(-1,0),(-3,0),(0,0),(1,0),(3,0)]
        datapoints_4 = [(-1,0),(-0,0),(0,0),(1,0),(3,0)]

        # Test computational logic in set_CMV_5 function
        self.assertFalse(set_CMV_5(num_points, datapoints_1, parameters), "CMV_5: No X[i] > X[i+1]")
        self.assertTrue(set_CMV_5(num_points, datapoints_2, parameters), "CMV_5: Last two points satisifes X[i] > X[i+1]")
        self.assertTrue(set_CMV_5(num_points, datapoints_3, parameters), "CMV_5: Points with negative x-values satisifes X[i] > X[i+1]")
        self.assertFalse(set_CMV_5(num_points, datapoints_4, parameters), "CMV_5: Edge case -0, no satisfactory consecutive points")



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

    def test_cmv_7(self):
        """
        This function tests the set_cmv_1 function which is responsible for 
        LIC condition number 7. set_cmv_1 should return true iff there exist
        at least one set of two data points separated by K_PTS whose distance
        apart is greater than LENGTH1
        """

        parameters_1 = {"kpts" : 2, "length1" : 2}
        datapoints_1 = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0)]
        datapoints_2 = [(0,0),(3,0),(5,0),(6,0),(1,0),(2,0),(8,0),(9,0),(10,0),(0,0)]
        parameters_2 = {"kpts" : 8, "length1" : 8}
        parameters_3 = {"kpts" : 1, "length1" : 2}
        parameters_4 = {"kpts" : 1, "length1": 9}

        # There exists many examples with kpts = 2 and length = 2, i.e. (0, 0) ... (3, 0)
        self.assertTrue(set_CMV_7(len(datapoints_1), datapoints_1, parameters_1))
        # Tests that (0, 0) ... (9.0) is found
        self.assertTrue(set_CMV_7(len(datapoints_1), datapoints_1, parameters_2))
        # Since the hop between points in datapoints_1 is of size 1, the difference
        # will never be larger than 2
        self.assertFalse(set_CMV_7(len(datapoints_1), datapoints_1, parameters_3))
        # No points in datapoints_2 have a difference of 9 with 1 point in between
        self.assertFalse(set_CMV_7(len(datapoints_2), datapoints_2, parameters_4))

if __name__ == '__main__':
    unittest.main()
