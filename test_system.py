import numpy as np
import unittest
from LIC_evaluation import *
from decide import *

####################################################################################################################

# System Test 1
# Given inputs
parsed_input_1 = {
    "numpoints" : 100,
    "datapoints" : [ 
        [-41.792822536123026, 529.1698346564233],
        [-80.49920040398172, -260.3694841809747],
        [248.0292103014608, 611.1208536393367]],

    "parameters" : {
        "LENGTH1"   : 1.0,
        "RADIUS1"   : 1.0,
        "EPSILON"   : 0.1,
        "AREA1"     : 1.0, 
        "QPTS"      : 10,
        "QUADS"     : 10,
        "DIST"      : 1.0,
        "NPTS"      : 10,
        "KPTS"      : 10,
        "APTS"      : 10,
        "BPTS"      : 10, 
        "CPTS"      : 10, 
        "DPTS"      : 10, 
        "EPTS"      : 10, 
        "FPTS"      : 10, 
        "GPTS"      : 10, 
        "LENGTH2"   : 1.0,
        "RADIUS2"   : 1.0,
        "AREA2"     : 1.0
    },
    "LCM" : [ ["ANDD"   ,"ANDD"   ,"ORR"    ,"AND"    ,"NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["ANDD"   ,"ANDD"   ,"ORR"    ,"ORR"    ,"NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["ORR"    ,"ORR"    ,"ANDD"   ,"ANDD"   ,"NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["ANDD"   ,"ORR"    ,"ANDD"   ,"ANDD"   ,"NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"] ],

    "PUV" : [True, False, True
            ,False,True , True
            ,False,True ,False
            ,True ,False, True
            ,False,True ,False]
}

# System Test 2
# Given inputs
parsed_input_2 = {
    "numpoints" : 100,
    "datapoints" : [ 
        [-41.792822536123026, 529.1698346564233],
        [-80.49920040398172, -260.3694841809747],
        [248.0292103014608, 611.1208536393367]],

    "parameters" : {
        "LENGTH1"   : 1.0,
        "RADIUS1"   : 1.0,
        "EPSILON"   : 0.1,
        "AREA1"     : 1.0, 
        "QPTS"      : 10,
        "QUADS"     : 10,
        "DIST"      : 1.0,
        "NPTS"      : 10,
        "KPTS"      : 10,
        "APTS"      : 10,
        "BPTS"      : 10, 
        "CPTS"      : 10, 
        "DPTS"      : 10, 
        "EPTS"      : 10, 
        "FPTS"      : 10, 
        "GPTS"      : 10, 
        "LENGTH2"   : 1.0,
        "RADIUS2"   : 1.0,
        "AREA2"     : 1.0
    },
    "LCM" : [ ["ANDD"   ,"ANDD"   ,"ORR"    ,"AND"    ,"NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["ANDD"   ,"ANDD"   ,"ORR"    ,"ORR"    ,"NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["ORR"    ,"ORR"    ,"ANDD"   ,"ANDD"   ,"NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["ANDD"   ,"ORR"    ,"ANDD"   ,"ANDD"   ,"NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"]
            , ["NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED","NOTUSED"] ],

    "PUV" : [True, False, True
            ,False,True , True
            ,False,True ,False
            ,True ,False, True
            ,False,True ,False]
}

# System Test 3
# Given inputs
parsed_input_3 = {
    "numpoints" : 20,
    "datapoints" : [ 
        [0.0, 0.0],
        [100.0, 100.0],
        [50.0, 50.0],
        [0.0,1.0],
        [1.0,0.0],
        [0.0,-2.0],
        [1.0,1.0],
        [11.0,1.0],
        [1.0,11.0],
        [-1.0,-1.0],
        [1.0,-1.0],
        [200.0,200.0],
        [2.0,11.0],
        [50,55],
        [6.7,42],
        [2.0,0.4],
        [0.0,0.5],
        [5.0,3.0], 
        [0.5,0.0],
        [10.0,30.0]],

    "parameters" : {
        "length1"   : 100.0,
        "radius1"   : 5.0,
        "epsilon"   : math.pi/3,
        "area1"     : 30.0, 
        "qpts"      : 3,
        "quads"     : 3,
        "dist"      : 50.0,
        "npts"      : 10,
        "kpts"      : 10,
        "apts"      : 5,
        "bpts"      : 2, 
        "cpts"      : 1, 
        "dpts"      : 3, 
        "epts"      : 6, 
        "fpts"      : 3, 
        "gpts"      : 10, 
        "length2"   : 1.0,
        "radius2"   : 1.0,
        "area2"     : 1.0
    },
    "LCM" : [ 
              [CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR],
              [CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR],
              [CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR],
              [CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR],
              [CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR],
              [CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR],
              [CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR],
              [CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR],
              [CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR],
              [CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR],
              [CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR],
              [CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ANDD,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR],
              [CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.NOTUSED,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED],
              [CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.NOTUSED,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED],
              [CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.NOTUSED,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.ORR,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED],
             ],
    "PUV" : [True, True, True
            ,True, True, True
            ,True, True, True
            ,True, True, True
            ,True, True, True]
}

####################################################################################################################
# CORRECT VALUES FOR TEST 1 THAT ACT AS COMPUTATIONAL CHECKPOINTS
CMV_correct_test_1 = [ True, True , True , True , True
               , True, True , True , True, True
               , True, True , True , True , True ]

PUM_correct_test_1 =   [ [0,   True  ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,0    ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,0    ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,0    ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,0   ,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,0   ,True,True,True,True,True,True,True,True,True]               
                        ,[True ,True ,True ,True ,True,True,0   ,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,0   ,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,0   ,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,0   ,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,0   ,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,0   ,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,0   ,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,0   ,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,0   ] ]

FUV_correct_test_1 = [True, True, True, True, True
                    ,True, True, True, True, True
                    ,True, True, True, True, True]

LAUNCH_correct_test_1 = True 

####################################################################################################################

# CORRECT VALUES FOR TEST 2 THAT ACT AS COMPUTATIONAL CHECKPOINTS
CMV_correct_test_2 = [ False, True , True , True , False
               ,False, False, False, False, False
               ,False, False, False, False, False]

PUM_correct_test_2 =   [ [0,   False ,True ,False,True,True,True,True,True,True,True,True,True,True,True]
                        ,[False,0    ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,0    ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[False,True ,True ,0    ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,0   ,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,0   ,True,True,True,True,True,True,True,True,True]               
                        ,[True ,True ,True ,True ,True,True,0   ,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,0   ,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,0   ,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,0   ,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,0   ,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,0   ,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,0   ,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,0   ,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,0   ] ]

FUV_correct_test_2 = [False, True, True, True, True
                    ,True, True, True, True, True
                    ,True, True, True, True, True]

LAUNCH_correct_test_2 = False

####################################################################################################################
# CORRECT VALUES FOR TEST 3 THAT ACT AS COMPUTATIONAL CHECKPOINTS
CMV_correct_test_3 = [True, True, True, True, False, True, True, True, True, True, True, True, False, False, False]
PUM_correct_test_3 = [ [True, True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                       ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                       ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                       ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                       ,[True ,True ,True ,True ,True   ,True,True,True,True,True,True,True,True,True,True]
                       ,[True ,True ,True ,True ,True,True   ,True,True,True,True,True,True,True,True,True]               
                       ,[True ,True ,True ,True ,True,True,True   ,True,True,True,True,True,True,True,True]
                       ,[True ,True ,True ,True ,True,True,True, True   ,True,True,True,True,True,True,True]
                       ,[True ,True ,True ,True ,True,True,True,True,True   ,True,True,True,True,True,True]
                       ,[True ,True ,True ,True ,True,True,True,True,True,True   ,True,True,True,True,True]
                       ,[True ,True ,True ,True ,True,True,True,True,True,True,True   ,True,True,True,True]
                       ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True   ,True,True,True]
                       ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True   ,True,True]
                       ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True   ,True]
                       ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True   ] ]

FUV_correct_test_3 = [True, True, True, True, True
                    ,True, True, True, True, True
                    ,True, True, True, True, True]

LAUNCH_correct_test_3 = True 

####################################################################################################################

# Test 1 inputs
num_points_test_1   = parsed_input_1["numpoints"]
data_points_test_1  = parsed_input_1["datapoints"]
parameters_test_1   = parsed_input_1["parameters"]
lcm_test_1          = parsed_input_1["LCM"]
puv_test_1          = parsed_input_1["PUV"]

# Test 2 inputs
num_points_test_2   = parsed_input_2["numpoints"]
data_points_test_2  = parsed_input_2["datapoints"]
parameters_test_2   = parsed_input_2["parameters"]
lcm_test_2          = parsed_input_2["LCM"]
puv_test_2          = parsed_input_2["PUV"]


# Test 3 inputs
num_points_test_3   = parsed_input_3["numpoints"]
data_points_test_3  = [np.array(p) for p in parsed_input_3["datapoints"]]
parameters_test_3   = parsed_input_3["parameters"]
lcm_test_3          = parsed_input_3["LCM"]
puv_test_3          = parsed_input_3["PUV"]

calculated_cmv = [ False, True , True , True , False
            ,False, False, False, False, False
            ,False, False, False, False, False]



# Test functions
# assertEqual() from unittest library can compare lists and larger data structures
class TestDecide(unittest.TestCase):
    def test_1(self):
        # calculated_cmv should be a 1x15 vector with bools as elements
        
        # Tests if the computed cmv vector is the same as the expected cmv vector for test1
        calculated_cmv = compute_cmv(parameters_test_1, num_points_test_1, data_points_test_1)
        self.assertEqual(calculated_cmv, CMV_correct_test_1), "test_1: Calculated cmv not the same as the correct test_1 version"

        # Tests if the computed PUM matrix is the same as the expected PUM matrix for test1
        calculated_PUM = compute_PUM(calculated_cmv,puv_test_1,lcm_test_1)
        self.assertEqual(calculated_PUM, PUM_correct_test_1), "test_1: Calculated PUM not the same as the correct test_1 version"

        # Tests if the computed FUV vector is the same as the expected FUV vector for test1
        calculated_FUV = compute_FUV(puv_test_1, calculated_PUM)
        self.assertEqual(calculated_FUV, FUV_correct_test_1), "test_1: Calculated FUV not the same as the correct test_1 version"

        # Test if 
        calculated_LAUNCH = compute_LAUNCH()
        self.assertEqual(calculated_LAUNCH, LAUNCH_correct_test_1), "test_1: Calculated LAUNCH not the same as the correct test_1 version"

    def test_2(self):
        # calculated_cmv should be a 1x15 vector with bools as elements
        
        # Tests if the computed cmv vector is the same as the expected cmv vector for test2
        calculated_cmv = compute_cmv(parameters_test_2, num_points_test_2, data_points_test_2)
        self.assertEqual(calculated_cmv, CMV_correct_test_2), "test_2: Calculated cmv not the same as the correct test_2 version"

        # Tests if the computed PUM matrix is the same as the expected PUM matrix for test2
        calculated_PUM = compute_PUM(lcm_test_2, calculated_cmv)
        self.assertEqual(calculated_PUM, PUM_correct_test_2), "test_2: Calculated PUM not the same as the correct test_2 version"

        # Tests if the computed FUV vector is the same as the expected FUV vector for test2
        calculated_FUV = compute_FUV(puv_test_2, calculated_PUM)
        self.assertEqual(calculated_FUV, FUV_correct_test_2), "test_2: Calculated FUV not the same as the correct test_2 version"

        # Test if 
        calculated_LAUNCH = compute_LAUNCH()
        self.assertEqual(calculated_LAUNCH, LAUNCH_correct_test_2), "test_2: Calculated LAUNCH not the same as the correct test_2 version"
        
    def test_3(self):
        # calculated_cmv should be a 1x15 vector with bools as elements
        
        # Tests if the computed cmv vector is the same as the expected cmv vector for test3
        calculated_cmv = compute_cmv(parameters_test_3, num_points_test_3, data_points_test_3)

        self.assertEqual(calculated_cmv, CMV_correct_test_3), "test_3: Calculated cmv not the same as the correct test_3 version"

        # Tests if the computed PUM matrix is the same as the expected PUM matrix for test3
        calculated_PUM = compute_PUM(calculated_cmv, puv_test_3, lcm_test_3)
        self.assertEqual(calculated_PUM, PUM_correct_test_3), "test_3: Calculated PUM not the same as the correct test_3 version"

        # Tests if the computed FUV vector is the same as the expected FUV vector for test3
        calculated_FUV = compute_FUV(calculated_PUM, puv_test_3)
        self.assertEqual(calculated_FUV, FUV_correct_test_3), "test_3: Calculated FUV not the same as the correct test_3 version"

        # Test if 
        calculated_LAUNCH = compute_LAUNCH(calculated_FUV)
        self.assertEqual(calculated_LAUNCH, LAUNCH_correct_test_3), "test_3: Calculated LAUNCH not the same as the correct test_3 version"





if __name__ == '__main__':
    unittest.main()





