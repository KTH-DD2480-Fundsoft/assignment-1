import set_CMV
import unittest

class TestDecide(unittest.TestCase):
    def test_cmv_0(self):
        pass
    

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


if __name__ == '__main__':
    unittest.main()
