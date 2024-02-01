import numpy as np
import unittest
from LIC_evaluation import *
from decide import *

####################################################################################################################

# System Test 1
# Given inputs
parsed_input_1 = {
    "numpoints" : 25,
    "datapoints" : [ 
        np.array([-41.79, 20.89]),
        np.array([-80.49, -26.36]),
        np.array([24.02, 61.12]),
        np.array([42.68, 98.24]),
        np.array([-32.83, 39.57]),
        np.array([71.98, 62.03]),
        np.array([91.22, 77.82]),
        np.array([-15.20, -63.71]),
        np.array([16.52, -93.39]),
        np.array([-48.80, -99.81]),
        np.array([-50.48, -73.60]),
        np.array([-78.21, 54.09]),
        np.array([-54.29, 96.93]),
        np.array([77.65, -65.06]),
        np.array([80.00, -52.88]),
        np.array([59.98, -96.91]),
        np.array([29.29, 44.62]),
        np.array([-77.94, -57.04]),
        np.array([-62.11, -37.21]),
        np.array([-83.97, -97.39]),
        np.array([81.45, 24.37]),
        np.array([-44.56, 27.45]),
        np.array([-18.32, -53.41]),
        np.array([-43.28, -11.07]),
        np.array([-36.75, -26.21])],

    "parameters" : {
        "length1"   : 500.0,
        "radius1"   : 200.0,
        "epsilon"   : 0.1,
        "area1"     : 20.0, 
        "qpts"      : 4,
        "quads"     : 3,
        "dist"      : 1.0,
        "npts"      : 10,
        "kpts"      : 10,
        "apts"      : 10,
        "bpts"      : 10, 
        "cpts"      : 10, 
        "dpts"      : 10, 
        "epts"      : 10, 
        "fpts"      : 10, 
        "gpts"      : 10, 
        "length2"   : 1.0,
        "radius2"   : 1.0,
        "area2"     : 1.0
    },
    "LCM" : [ [CONNECTORS.ANDD   ,CONNECTORS.ANDD   ,CONNECTORS.ORR    ,CONNECTORS.ANDD    ,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.ANDD   ,CONNECTORS.ANDD   ,CONNECTORS.ORR    ,CONNECTORS.ORR    ,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.ORR    ,CONNECTORS.ORR    ,CONNECTORS.ANDD   ,CONNECTORS.ANDD   ,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.ANDD   ,CONNECTORS.ORR    ,CONNECTORS.ANDD   ,CONNECTORS.ANDD   ,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED] ],

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
    "LCM" : [ [CONNECTORS.ANDD   ,CONNECTORS.ANDD   ,CONNECTORS.ORR,    CONNECTORS.ANDD    ,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.ANDD   ,CONNECTORS.ANDD   ,CONNECTORS.ORR    ,CONNECTORS.ORR    ,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.ORR    ,CONNECTORS.ORR    ,CONNECTORS.ANDD   ,CONNECTORS.ANDD   ,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.ANDD   ,CONNECTORS.ORR    ,CONNECTORS.ANDD   ,CONNECTORS.ANDD   ,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED] ],

    "PUV" : [True, False, True
            ,False,True , True
            ,False,True ,False
            ,True ,False, True
            ,False,True ,False]
}

# System Test 3
# Given inputs
parsed_input_3 = {
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
    "LCM" : [ [CONNECTORS.ANDD   ,CONNECTORS.ANDD   ,CONNECTORS.ORR    ,CONNECTORS.ANDD    ,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.ANDD   ,CONNECTORS.ANDD   ,CONNECTORS.ORR    ,CONNECTORS.ORR    ,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.ORR    ,CONNECTORS.ORR    ,CONNECTORS.ANDD   ,CONNECTORS.ANDD   ,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.ANDD   ,CONNECTORS.ORR    ,CONNECTORS.ANDD   ,CONNECTORS.ANDD   ,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED]
            , [CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED,CONNECTORS.NOTUSED] ],

    "PUV" : [True, False, True
            ,False,True , True
            ,False,True ,False
            ,True ,False, True
            ,False,True ,False]
}

####################################################################################################################
# CORRECT VALUES FOR TEST 1 THAT ACT AS COMPUTATIONAL CHECKPOINTS
CMV_correct_test_1 = [ False, True , True , True , False
               ,True, True, False, False, True
               ,True, True, False, False, False]

PUM_correct_test_1 =   [ [False,False ,True ,False,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]               
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True]
                        ,[True ,True ,True ,True ,True,True,True,True,True,True,True,True,True,True,True] ]

FUV_correct_test_1 = [False, True, True, True, True
                    ,True, True, True, True, True
                    ,True, True, True, True, True]

LAUNCH_correct_test_1 = False

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
CMV_correct_test_3 = [ False, True , True , True , False
               ,False, False, False, False, False
               ,False, False, False, False, False]

PUM_correct_test_3 =   [ [0,   False ,True ,False,True,True,True,True,True,True,True,True,True,True,True]
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

FUV_correct_test_3 = [False, True, True, True, True
                    ,True, True, True, True, True
                    ,True, True, True, True, True]

LAUNCH_correct_test_3 = False

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
data_points_test_3  = parsed_input_3["datapoints"]
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
        
        # Tests so that all CMV elements are set correctly for test1
        self.assertFalse(evaluate_LIC_0(num_points_test_1, data_points_test_1, parameters_test_1), "CMV_0: Not correct")
        self.assertTrue(evaluate_LIC_1(num_points_test_1, data_points_test_1, parameters_test_1),  "CMV_1: Not correct")
        self.assertTrue(evaluate_LIC_2(num_points_test_1, data_points_test_1, parameters_test_1),  "CMV_2: Not correct")
        self.assertTrue(evaluate_LIC_3(num_points_test_1, data_points_test_1, parameters_test_1),  "CMV_3: Not correct")
        self.assertFalse(evaluate_LIC_4(num_points_test_1, data_points_test_1, parameters_test_1), "CMV_4: Not correct")
        self.assertTrue(evaluate_LIC_5(num_points_test_1, data_points_test_1, parameters_test_1), "CMV_5: Not correct")
        self.assertTrue(evaluate_LIC_6(num_points_test_1, data_points_test_1, parameters_test_1), "CMV_6: Not correct")
        self.assertFalse(evaluate_LIC_7(num_points_test_1, data_points_test_1, parameters_test_1), "CMV_7: Not correct")
        self.assertFalse(evaluate_LIC_8(num_points_test_1, data_points_test_1, parameters_test_1), "CMV_8: Not correct")
        self.assertTrue(evaluate_LIC_9(num_points_test_1, data_points_test_1, parameters_test_1), "CMV_9: Not correct")
        self.assertTrue(evaluate_LIC_10(num_points_test_1, data_points_test_1, parameters_test_1), "CMV_10: Not correct")
        self.assertTrue(evaluate_LIC_11(num_points_test_1, data_points_test_1, parameters_test_1), "CMV_11: Not correct")
        self.assertFalse(evaluate_LIC_12(num_points_test_1, data_points_test_1, parameters_test_1), "CMV_12: Not correct")
        self.assertFalse(evaluate_LIC_13(num_points_test_1, data_points_test_1, parameters_test_1), "CMV_13: Not correct")
        self.assertFalse(evaluate_LIC_14(num_points_test_1, data_points_test_1, parameters_test_1), "CMV_14: Not correct")

        # Tests if the computed cmv vector is the same as the expected cmv vector for test1
        calculated_cmv = compute_cmv(parameters_test_1, num_points_test_1, data_points_test_1)
        self.assertEqual(calculated_cmv, CMV_correct_test_1), "test_1: Calculated cmv not the same as the correct test_1 version"
    
        # Tests if the computed PUM matrix is the same as the expected PUM matrix for test1
        calculated_PUM = compute_PUM(calculated_cmv,puv_test_1,lcm_test_1)
        #print(calculated_PUM)
        self.assertEqual(calculated_PUM, PUM_correct_test_1), "test_1: Calculated PUM not the same as the correct test_1 version"

        # Tests if the computed FUV vector is the same as the expected FUV vector for test1
        calculated_FUV = compute_FUV(calculated_PUM, puv_test_1)
        self.assertEqual(calculated_FUV, FUV_correct_test_1), "test_1: Calculated FUV not the same as the correct test_1 version"

        # Tests if the final launch condition is correct
        calculated_LAUNCH = compute_LAUNCH(calculated_FUV)
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
        calculated_FUV = compute_FUV(puv_test_3, calculated_PUM)
        self.assertEqual(calculated_FUV, FUV_correct_test_3), "test_3: Calculated FUV not the same as the correct test_3 version"

        # Test if 
        calculated_LAUNCH = compute_LAUNCH(calculated_FUV)
        self.assertEqual(calculated_LAUNCH, LAUNCH_correct_test_3), "test_3: Calculated LAUNCH not the same as the correct test_3 version"
    




if __name__ == '__main__':
    unittest.main()





