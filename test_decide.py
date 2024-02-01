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


        # Test computational logic in set_CMV_13 function
        self.assertFalse(set_CMV_13(num_points, datapoints_1, parameters), "test_cmv_13: - ") # Tests when all points are the same
        self.assertTrue( set_CMV_13(num_points, datapoints_2, parameters), "test_cmv_13: - ") # Tests when many points are the origin but one combination is outside radius1
        self.assertTrue( set_CMV_13(num_points, datapoints_3, parameters), "test_cmv_13: - ") # Tests when two points are the same. Outside fo radius 1 but inside radius 2
        self.assertFalse(set_CMV_13(num_points, datapoints_4, parameters), "test_cmv_13: - ") # Tests colinear points that are outside both radius 1 and radius2 
    

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