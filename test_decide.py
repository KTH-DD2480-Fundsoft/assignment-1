import numpy as np
import unittest
from LIC_evaluation import *

class TestDecide(unittest.TestCase):
    def test_cmv_4_two_valid_sets(self):
        parameters = {
            'qpts' : 4,
            'quads' : 3
        }
        data_points = [(0.1, 0.1), (-0.1, 0.1), (0.1, -0.1), (-0.1, -0.1), (0.1, 0.1)]
        num_points = len(data_points)
        self.assertTrue(evaluate_LIC_4(num_points, data_points, parameters), "4 consecutive points occupy 4 quadrants")

    def test_cmv_4_no_valid_sets(self):
        parameters = {
            'qpts' : 4,
            'quads' : 3
        }
        data_points = [(0.1, 0.1), (0.1, -0.1), (0.1, -0.1), (-0.1, 0.1), (0.1, 0.1)]
        num_points = len(data_points)
        self.assertFalse(evaluate_LIC_4(num_points, data_points, parameters), "No 4 consecutive points occupy 4 quadrants")

    def test_cmv_4_impossible(self):
        parameters = {
            'qpts' : 2,
            'quads' : 3
        }
        data_points = [(0.1, 0.1), (-0.1, 0.1), (0.1, -0.1), (-0.1, -0.1), (0.1, 0.1)]
        num_points = len(data_points)
        self.assertFalse(evaluate_LIC_4(num_points, data_points, parameters), "Impossible since quads > qpts")

    def test_cmv_4_last_set_in_datapoints_is_valid(self):
        parameters = {
            'qpts' : 3,
            'quads' : 2
        }
        data_points = [(0.1, 0.1), (0.1, -0.1), (0.1, -0.1), (0.1, -0.1), (0.1, 0.1), (-0.1, -0.1)]
        num_points = len(data_points)
        self.assertTrue(evaluate_LIC_4(num_points, data_points, parameters), "The qpts last points occupy more than 2 quadrants")

    def test_cmv_4_qpts_equal_to_numpoints_and_condition_still_met(self):
        data_points = [(0.1, 0.1), (0.1, -0.1), (0.1, -0.1), (0.1, -0.1), (-0.1, 0.1), (-0.1, -0.1)]
        num_points = len(data_points)
        parameters = {
            'qpts' : num_points,
            'quads' : 3
        }
        self.assertTrue(evaluate_LIC_4(num_points, data_points, parameters), "qpts = num_points, all 4 quadrants are occupied")

    def test_cmv_0(self):
        # Define test parameters (should probably be moved to JSON test file later)
        parameters = {}
        parameters["length1"] = 2

        num_points = 5

        datapoints_1 = [(0,0),(1,1),(2,2),(3,3),(4,4)]
        datapoints_2 = [(0,0),(3,4),(0,0),(0,0),(0,0)]
        datapoints_3 = [(-1,0),(-3,0),(0,0),(1,0),(3,0)]

        # Test computational logic in evaluate_LIC_0 function
        self.assertFalse(evaluate_LIC_0(num_points, datapoints_1, parameters), "CMV_0: Maximum distance is smaller than parameter LENGTH1")
        self.assertTrue(evaluate_LIC_0(num_points, datapoints_2, parameters), "CMV_0: Maximum distance is larger than parameter LENGTH1")
        self.assertTrue(evaluate_LIC_0(num_points, datapoints_3, parameters), "CMV_0: Maximum distance is larger than parameter LENGTH1")

    def test_cmv_3(self): 
        ''' Tests the function evaluate_LIC_3 which calculates the 
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
            evaluate_LIC_3(
                num_points,
                data_points_true1,
                parameters_true1 
            )
        )
        self.assertTrue(
            evaluate_LIC_3(
                num_points,
                data_points_true2,
                parameters_true2 
            )
        )
        self.assertFalse(
            evaluate_LIC_3(
                num_points,
                data_points_false1,
                parameters_false1 
            )
        )
        self.assertFalse(
            evaluate_LIC_3(
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

        #def evaluate_LIC_10(num_points, datapoints, parameters):

        # Test computational logic in evaluate_LIC_10 function
        self.assertFalse(evaluate_LIC_10(num_points, datapoints_0, parameters))
        self.assertFalse(evaluate_LIC_10(num_points, datapoints_2, parameters))
        self.assertTrue(evaluate_LIC_10( num_points, datapoints_1, parameters))
        self.assertTrue(evaluate_LIC_10( num_points, datapoints_3, parameters))

        # Change AREA1 to test comparative computations
        parameters["area1"] = 100
        self.assertFalse(evaluate_LIC_10(num_points, datapoints_1, parameters))
        self.assertFalse(evaluate_LIC_10(num_points, datapoints_3, parameters))

        # Test built-in assertions in evaluate_LIC_10 function
        with self.assertRaises(AssertionError):   # Tests that NUMPOINTS-3 is larger than sum of E_PTS and F_PTS
            evaluate_LIC_10(num_points_less, datapoints_0, parameters)   

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


        # Test computational logic in evaluate_LIC_11 function
        self.assertFalse(evaluate_LIC_11(num_points, datapoints_1, parameters), "test_cmv_11: x vector is only increasing")
        self.assertTrue(evaluate_LIC_11( num_points, datapoints_2, parameters), "test_cmv_11: x vector includes correct set of datapoints")
        self.assertTrue(evaluate_LIC_11( num_points, datapoints_3, parameters), "test_cmv_11: x vector includes correct set of datapoints")
        self.assertFalse(evaluate_LIC_11(num_points_less, datapoints_2, parameters), "test_cmv_11: NUMPOINTS less than 3")

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
        
        self.assertTrue(evaluate_LIC_2(len(datapoints_1), datapoints_1, parameters_1))
        self.assertFalse(evaluate_LIC_2(len(datapoints_2), datapoints_2, parameters_2))
        self.assertFalse(evaluate_LIC_2(len(datapoints_3), datapoints_3, parameters_3))
        self.assertTrue(evaluate_LIC_2(len(datapoints_4), datapoints_4, parameters_4))

    def test_cmv_12(self):
        num_points = 11    
        parameters = { "KPTS" : 3 
                     , "LENGTH1" : 10.0 
                     , "LENGTH2" : 1.0 }
        data_points = [ (0.75,0.0), (1.0,0.0), (1.25,0.0), 
                        (1.5,0.0), (5.5,0.0), (3.0,0.0),  
                        (4.0,0.0), (5.0,0.0), (6.0,0.0), 
                        (7.0,0.0), (15.0,0.0) ]
        data_points = [np.array(e) for e in data_points]
        
        self.assertTrue(evaluate_LIC_12(num_points,data_points,parameters))
        data_points[10] = np.array((8.0,0.0))
        self.assertFalse(evaluate_LIC_12(num_points,data_points,parameters))

        num_points = 11    
        parameters = { "KPTS" : 3 
                     , "LENGTH1" : 10.0 
                     , "LENGTH2" : 1.0 }
        data_points = [ (1.0,0.0), (2.0,0.0), (3.0,0.0), 
                        (4.0,0.0), (5.0,0.0), (6.0,0.0),  
                        (7.0,0.0), (8.0,0.0), (9.0,0.0), 
                        (10.0,0.0), (18.0,0.0) ]
        data_points = [np.array(e) for e in data_points]
        self.assertFalse(evaluate_LIC_12(num_points,data_points,parameters))
        data_points[0] = np.array((4.5,0))
        self.assertTrue(evaluate_LIC_12(num_points,data_points,parameters))

    def test_cmv_5(self):
        # Define test parameters
        parameters = {}

        num_points = 5

        datapoints_1 = [(0,0),(1,1),(2,2),(3,3),(4,4)]
        datapoints_2 = [(0,0),(0,4),(0,0),(1,0),(0,0)]
        datapoints_3 = [(-1,0),(-3,0),(0,0),(1,0),(3,0)]
        datapoints_4 = [(-1,0),(-0,0),(0,0),(1,0),(3,0)]

        # Test computational logic in evaluate_LIC_5 function
        self.assertFalse(evaluate_LIC_5(num_points, datapoints_1, parameters), "CMV_5: No X[i] > X[i+1]")
        self.assertTrue(evaluate_LIC_5(num_points, datapoints_2, parameters), "CMV_5: Last two points satisifes X[i] > X[i+1]")
        self.assertTrue(evaluate_LIC_5(num_points, datapoints_3, parameters), "CMV_5: Points with negative x-values satisifes X[i] > X[i+1]")
        self.assertFalse(evaluate_LIC_5(num_points, datapoints_4, parameters), "CMV_5: Edge case -0, no satisfactory consecutive points")

    def test_cmv_8(self):
        """
        This function tests the set_cmv_8 function which is responsible for 
        LIC condition number 8. set_cmv_8 should return true iff there exist
        at least one set of three data points separated by A_PTS and B_PTS 
        who cannot be encircled by a circle of radius RADIUS1
        """
        # (3.0, 1.0), (10.0, 2.0), and (3.0, 3.0) create a circle with radius 3.57
        # set_cmv_8 should therefore be true for radius1 = 3 but not for radius1 = 4
        datapoints_1 = np.asarray([(3.0, 1.0), (1.0, 1.0), (10.0, 2.0), (2.0, 1.0), (2.0, 1.0), (3.0, 3.0)])
        datapoints_1  = [np.array(p) for p in datapoints_1]
        parameters_1 = {"apts" : 1, "bpts" : 2, "radius1" : 3}
        parameters_2 = {"apts" : 1, "bpts" : 2, "radius1" : 4}

        # (2.0, 1.0), (5.0, 2.0), and (3.0, 2.5) create a circle with radius 1.67
        # set_cmv_8 should therefore be true for radius1 = 1 but not for radius1 = 2
        datapoints_2 = np.asarray([(1.8, 0.9), (2.0, 1.0), (2.0, 1.0), (0.0, 0.0), (5.0, 2.0), (5.0, 2.0), (0.0, 0.0), (3.0, 2.5), (2.0, 2.0)])
        datapoints_2 = [np.array(p) for p in datapoints_2]
        parameters_3 = {"apts" : 2, "bpts" : 2, "radius1" : 1}
        parameters_4 = {"apts" : 2, "bpts" : 2, "radius1" : 2}

        self.assertTrue(evaluate_LIC_8(len(datapoints_1), datapoints_1, parameters_1))
        self.assertFalse(evaluate_LIC_8(len(datapoints_1), datapoints_1, parameters_2))

        self.assertTrue(evaluate_LIC_8(len(datapoints_2), datapoints_2, parameters_3))
        self.assertFalse(evaluate_LIC_8(len(datapoints_2), datapoints_2, parameters_4))
        
    def test_cmv_14(self):
        num_points = 8    
        parameters = { "EPTS" : 2
                     , "FPTS" : 2 
                     , "AREA1" : 4.0 
                     , "AREA2" : 1.1 }
        data_points = [ (0.0,0.0), (1.0,0.0), (2.0,0.0), 
                        (3.0,0.0), (3.0,1.0), (3.0,2.0),  
                        (3.0,3.0), (1.0,1.0)]
        data_points = [np.array(e) for e in data_points]
        self.assertTrue(evaluate_LIC_14(num_points,data_points,parameters))
        data_points = [ (0.0,0.0), (1.0,0.0), (2.0,0.0), 
                        (3.0,0.0), (3.0,1.0), (3.0,2.0),  
                        (3.0,3.0), (10.0,10.0)]
        data_points = [np.array(e) for e in data_points]
        self.assertFalse(evaluate_LIC_14(num_points,data_points,parameters))
        data_points = [ (0.0,0.0), (1.0,0.0), (2.0,0.0), 
                        (3.0,0.0), (3.0,0.5), (3.0,1.0),  
                        (3.0,1.5), (1.0,1.0)]
        data_points = [np.array(e) for e in data_points]
        self.assertFalse(evaluate_LIC_14(num_points,data_points,parameters))

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
        self.assertFalse(evaluate_LIC_1(num_points, datapoints, parameters))

    def test_cmv_1_collinear(self):
        """
        Given a set of three collinear points, the points should not 
        be able to be contained by a circle.
        """
        parameters = {}
        parameters["radius1"] = 0.5
        datapoints = [(1.0, 1.0), (2.0, 2.0), (3.0, 3.0)]
        num_points = len(datapoints)
        self.assertFalse(evaluate_LIC_1(num_points, datapoints, parameters))

    def test_cmv_1(self):
        """
        The points (1, 0), (-1, 0), and (0, 1) should be contained a by a circle
        with radius 1. evaluate_LIC_1 should therefore be true with RADIUS set to 0.5
        but not when RADIUS is set to 1. 
        """
        parameters = {}
        parameters["radius1"] = 0.5
        datapoints = [(0.0, 0.0), (1.0, 0.0), (-1.0, 0.0), (0.0, 1.0), (0.0, 0.0)]
        num_points = len(datapoints)

        self.assertTrue(evaluate_LIC_1(num_points, datapoints, parameters))
        parameters["radius1"] = 1
        self.assertFalse(evaluate_LIC_1(num_points, datapoints, parameters))

    def test_cmv_7(self):
        """
        This function tests the set_cmv_7 function which is responsible for 
        LIC condition number 7. set_cmv_7 should return true iff there exist
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
        self.assertTrue(evaluate_LIC_7(len(datapoints_1), datapoints_1, parameters_1))
        # Tests that (0, 0) ... (9.0) is found
        self.assertTrue(evaluate_LIC_7(len(datapoints_1), datapoints_1, parameters_2))
        # Since the hop between points in datapoints_1 is of size 1, the difference
        # will never be larger than 2
        self.assertFalse(evaluate_LIC_7(len(datapoints_1), datapoints_1, parameters_3))
        # No points in datapoints_2 have a difference of 9 with 1 point in between
        self.assertFalse(evaluate_LIC_7(len(datapoints_2), datapoints_2, parameters_4))

    def test_cmv_9_too_few_datapoints(self):
        # Define test parameters
        parameters = {
            'cpts' : 2,
            'dpts' : 3,
            'epsilon' : np.pi/4
        }

        datapoints = [(0,0),(1,0),(2,0)]
        num_points = len(datapoints)

        # Test computational logic in evaluate_LIC_9 function
        self.assertFalse(evaluate_LIC_9(num_points, datapoints, parameters), "num_points is less than 5, not satisfactory")

    def test_cmv_9_only_angles_of_PI_radians(self):
        # Define test parameters
        parameters = {
            'cpts' : 2,
            'dpts' : 3,
            'epsilon' : 0
        }

        datapoints = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0)]
        num_points = len(datapoints)

        # Test computational logic in evaluate_LIC_9 function
        self.assertFalse(evaluate_LIC_9(num_points, datapoints, parameters), "All points are along a line Y=0, angle is always pi which is in forbidden range")
    
    def test_cmv_9_no_valid_angles(self):
        # Define test parameters
        parameters = {
            'cpts' : 3,
            'dpts' : 4,
            'epsilon' : np.pi/2 + 0.00001 # needs a threshold (we have an angle (PI/2) that is right on the edge of the invalid range PI±ε)
        }

        datapoints = [(-1,0),(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(4,9),(10,0)]
        num_points = len(datapoints)

        # Test computational logic in evaluate_LIC_9 function
        self.assertFalse(evaluate_LIC_9(num_points, datapoints, parameters), "One angle close to the edge of invalid range, but still invalid. THe rest are clearly invalid")

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

        # Test computational logic in evaluate_LIC_9 function
        self.assertTrue(evaluate_LIC_9(num_points, datapoints_0, parameters), "One set have an angle slightly less than PI/2, is outside forbidden range PI±PI/2")
        self.assertFalse(evaluate_LIC_9(num_points, datapoints_1, parameters), "All angles are PI exept on that is slightly greater than PI/2, still in forbidden range PI±PI/2")

    def test_cmv_9_set_with_coinciding_points_followed_by_satisfactory_set(self):
        
        # Define test parameters
        parameters = {
            'cpts' : 2,
            'dpts' : 2,
            'epsilon' : np.pi/2
        }

        datapoints_0 = [(-1,0), (0,0),(0,0),(2,0),(3,0),(4,0),(2,0),(6,0),(7,0),(8,0),(3,9),(10,0)]
        datapoints_1 = [(-1,0), (0,0),(0,0),(-1,0),(3,0),(4,0),(2,0),(6,0),(7,0),(8,0),(3,9),(10,0)]
        num_points = len(datapoints_0)

        # Test computational logic in evaluate_LIC_9 function
        self.assertTrue(evaluate_LIC_9(num_points, datapoints_0, parameters), "The first set has coinciding points, the second last has a satisfactory set with angle≈0.4PI which is outside the invalid range PI±PI/2")
        self.assertTrue(evaluate_LIC_9(num_points, datapoints_1, parameters), "The first set has coinciding points, the second last has a satisfactory set with angle≈0.4PI which is outside the invalid range PI±PI/2")

    def test_cmv_9_two_sets_with_coinciding_points_but_no_other_satisfactory_sets(self):
        
        # Define test parameters
        parameters = {
            'cpts' : 2,
            'dpts' : 1,
            'epsilon' : np.pi/2
        }

        datapoints_0 = [(-1,0), (4,0), (2,0), (3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0)]
        datapoints_1 = [(-1,0), (1,0), (2,0), (3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(8,0)]
        num_points_0 = len(datapoints_0)
        num_points_1 = len(datapoints_1)

        # Test computational logic in evaluate_LIC_9 function
        self.assertFalse(evaluate_LIC_9(num_points_0, datapoints_0, parameters), "Second set has coinciding points, but no other sets are satisfactory")
        self.assertFalse(evaluate_LIC_9(num_points_1, datapoints_1, parameters), "Last set has coinciding points, but no other sets are satisfactory")
        
    def test_distance_from_line(self):
        # Test with points on the line
        self.assertAlmostEqual(distance_from_line((2, 2), (0, 0), (3, 3)), 0.0)
        
        # Test with points off the line
        self.assertAlmostEqual(distance_from_line((1, 2), (0, 0), (2, 2)), np.sqrt(0.5))

        # Test the degenerate case (line is a point)
        self.assertAlmostEqual(distance_from_line((2, 3), (1, 1), (1, 1)), np.sqrt(5))

    def test_cmv_6(self):
        parameters = {
            "npts" : 3,
            "dist" : 1.0
        }


        # Test case where condition is met
        self.assertTrue(evaluate_LIC_6(4, [(0, 0), (1, 1), (2, 2), (0, 10)], parameters))

        self.assertTrue(evaluate_LIC_6(4, [(0, 0), (1, 1), (2, 2), (0, 0)], parameters))

        self.assertFalse(evaluate_LIC_6(3, [(0, 0), (0.4, 0.5), (0, 0)], parameters))

        # Test edge case with fewer than 3 points
        self.assertFalse(evaluate_LIC_6(2, [(0, 0), (1, 1)], parameters))

        parameters = {
            "npts" : 3,
            "dist" : 10.0
        }

        # Test case where condition is not met
        self.assertFalse(evaluate_LIC_6(4, [(0, 0), (1, 1), (2, 2), (3, 3)], parameters))

    def test_cmv_13(self):

        num_points = 10
        parameters = {
            "APTS" : 2,
            "BPTS" : 3,
            "RADIUS1" : 1,
            "RADIUS2" : 2
        }

        datapoints_1 = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        datapoints_2 = [(0,0),(1.4,1.4),(1,1),(1,1),(1.5,0),(0,0),(0,0),(0,1),(0,-1.9),(1,1)]
        datapoints_3 = [(1.4,1.4),(0,0),(0,0),(1.4,1.4),(0,0),(0,0),(0,0),(-1.1,-1.1),(0,0),(0,0)]
        datapoints_4 = [(-1.5,0),(0,0),(0,0),(0,0),(5,5),(5,5),(0,0),(3,0),(0,0),(0,0)]


        # Test computational logic in evaluate_LIC_13 function
        self.assertFalse(evaluate_LIC_13(num_points, datapoints_1, parameters), "test_cmv_13: - ") # Tests when all points are the same
        self.assertTrue( evaluate_LIC_13(num_points, datapoints_2, parameters), "test_cmv_13: - ") # Tests when many points are the origin but one combination is outside radius1
        self.assertTrue( evaluate_LIC_13(num_points, datapoints_3, parameters), "test_cmv_13: - ") # Tests when two points are the same. Outside fo radius 1 but inside radius 2
        self.assertFalse(evaluate_LIC_13(num_points, datapoints_4, parameters), "test_cmv_13: - ") # Tests colinear points that are outside both radius 1 and radius2 
    

    def test_smallest_containting_circle(self):
        points_1 = [(0,0),(1,0),(0,1)]
        points_2 = [(-1,0),(1,0),(0,1)]
        points_3 = [(-3,0),(-4,3),(-4,-3)]
        points_4 = [(1,1),(3,3),(5,5)]
        points_5 = [(-1,0),(3,0),(5,0)]
        points_6 = [(1,1),(1,1),(1,1)]
        points_7 = [(-4,-3),(-4,-3),(-4,3)]

        # Test for points in Quadrant 1
        center_1, radius_1 = smallest_containting_circle(points_1)
        self.assertEqual(center_1,(0.5,0.5))
        self.assertEqual(radius_1, 0.7071067811865476)

        # Test for points on unit circle
        center_2, radius_2 = smallest_containting_circle(points_2)
        self.assertEqual(center_2,(0.0,0.0))
        self.assertEqual(radius_2, 1.0)

        # Test for negative points in Quadrants 2 and 3
        center_3, radius_3 = smallest_containting_circle(points_3)
        self.assertEqual(center_3,(-4.0,0.0))
        self.assertEqual(radius_3, 3.0)

        # Test for diagonal colinear points
        center_4, radius_4 = smallest_containting_circle(points_4)
        self.assertEqual(center_4,(3.0,3.0))
        self.assertEqual(radius_4, 2.8284271247461903) 

        # Test for horisontal colinear points
        center_5, radius_5 = smallest_containting_circle(points_5)
        self.assertEqual(center_5,(2.0,0.0))
        self.assertEqual(radius_5, 3.0)

        # Test when all three points are the same
        center_6, radius_6 = smallest_containting_circle(points_6)
        self.assertEqual(center_6,(1.0,1.0))
        self.assertEqual(radius_6, 0)

        # Test when all two points are the same
        center_7, radius_7 = smallest_containting_circle(points_7)
        self.assertEqual(center_7,(-4.0,0.0))
        self.assertEqual(radius_7, 3.0)



if __name__ == '__main__':
    unittest.main()
