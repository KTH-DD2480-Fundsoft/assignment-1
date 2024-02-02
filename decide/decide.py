import json
import sys
from enum import Enum
from numpy import array, float64
from numpy.typing import NDArray
from typing import List, Tuple, TypedDict
from decide.LIC_evaluation import *

NUMBER_OF_CONDITIONS = 15

# TYPE DECLARATIONS

# Enum used in the LCM 
class CONNECTORS(Enum):
    NOTUSED = 777
    ORR = 778   # Assigned automatically as 1 + previous value
    ANDD = 779  # Assigned automatically as 2 + previous value
    
# Type of the parameter dictionary
class Parameters(TypedDict):
    length1   : float 
    radius1   : float
    epsilon   : float
    area1     : float
    qpts      : int
    quads     : int
    dist      : float
    npts      : int
    kpts      : int
    apts      : int
    bpts      : int
    cpts      : int
    dpts      : int
    epts      : int
    fpts      : int
    gpts      : int
    length2   : float
    radius2   : float
    area2     : float

def print_help():
    print('''INTERCEPTOR MISSILE LAUNCH DECISION PROGRAM "DECIDE"
USAGE: python3 decide.py input_data.json 
JSON FORMAT:
{
    "numpoints" : <INT>,
    "datapoints" : <[[FLOAT,FLOAT]]>,
    "parameters" : {
        "LENGTH1"   : <FLOAT>,
        "RADIUS1"   : <FLOAT>,
        "EPSILON"   : <FLOAT>,
        "AREA1"     : <FLOAT>,
        "QPTS"      : <INT>,
        "QUADS"     : <INT>,
        "DIST"      : <FLOAT>,
        "NPTS"      : <INT>,
        "KPTS"      : <INT>,
        "APTS"      : <INT>,
        "BPTS"      : <INT>,
        "CPTS"      : <INT>,
        "DPTS"      : <INT>,
        "EPTS"      : <INT>,
        "FPTS"      : <INT>,
        "GPTS"      : <INT>,
        "LENGTH2"   : <FLOAT>,
        "RADIUS2"   : <FLOAT>,
        "AREA2"     : <FLOAT>,
    },
    "LCM" : <[[STRING ("ANDD" | "ORR" | "NOTUSED")]]>,
    "PUV" : <[BOOLEAN]>
}  
          ''')


def handle_input() ->  \
           Tuple[ int
                , List[NDArray[float64]]
                , Parameters
                , List[List[CONNECTORS]]
                , List[bool] ]:
    ''' 
    Reads the input from a JSON file specified as a command-line argument.
    Parses the JSON and returns a tuple containg the required input for the 
    program.

    IN: Nothing

    OUT: 
        1. Number of points 
        2. The datapoints
        3. Dictionary containing program parameters 
        4. Logical connector matrix 
        5. Preliminary unlocking vector

    ''' 
    try: 
        # Check if we got exactly one argument
        if len(sys.argv) > 2:
            raise ValueError("Too many arguments.")
        if len(sys.argv) < 2:
            raise ValueError("Too few arguments.")
    
        file_path = sys.argv[1]
        
        with open(file_path) as file_descriptor: 
            # Parse the json 
            data = json.load(file_descriptor)
       
        num_points = int(data['numpoints'])

        datapoints = [array((float(l[0]),float(l[1]))) for l in data['datapoints']]
        
        if len(datapoints) != num_points:
            raise ValueError("Given number of datapoints does not match given ")
    
        parameters = data['parameters'] 
        
        # check that all parameters are present and that they are of 
        # correct type.
        params = [("length1",float), ("radius1",float), ("epsilon",float),
                  ("area1",float), ("qpts",int), ("quads",int), ("dist",float),
                  ("npts",int), ("kpts",int), ("apts",int), ("bpts",int),
                  ("cpts",int), ("dpts",int), ("epts",int), ("fpts",int),
                  ("gpts",int), ("length2",float), ("radius2",float), ("area2",float)  ]
        if len(params) > len(parameters):
            raise ValueError("Unknown parameters in " + file_path)
        if len(params) < len(parameters):
            raise ValueError("Missing parameters in " + file_path)
        if not all([key in parameters and isinstance(parameters[key],ty) for key,ty in params]): 
            raise ValueError("Unknown or malformed parameters in " + file_path)
            
       
        # Converter from json strings to CONNECTORS Enum
        def match_enum(s : str) -> CONNECTORS:
            if s == "NOTUSED": return CONNECTORS(777)
            elif s == "ORR": return CONNECTORS(778)
            elif s == "ANDD": return CONNECTORS(779)
            else: raise ValueError('Invalid LCM value "' + s + '"')
        
        # extract LCM and PUV. And check that they are of correct size
        lcm = [[match_enum(e) for e in row] for row in data['LCM']] 
        puv = [bool(b) for b in data['PUV']]
    
        if len(lcm)    != NUMBER_OF_CONDITIONS:
            raise ValueError("LCM is of wrong size.")
        if len(lcm[0]) != NUMBER_OF_CONDITIONS:
            raise ValueError("LCM is of wrong size.")
        if len(puv)    != NUMBER_OF_CONDITIONS:
            raise ValueError("PUV is of wrong size.")
    

        return (num_points,datapoints,parameters,lcm,puv) 
    
    except ValueError as e:
        print("Invalid input: " + str(e))
        print_help()
        exit(1) 
    except OSError as e:
        print("Error reading input file: " + str(e))
        print_help()
        exit(1)
    except Exception as e: 
        print("Unexpected exception: " + str(e))
        print_help()
        exit(1)
    
def compute_PUM(cmv,puv,lcm):
    """
        PUM[i, j] = CMV[i] <LCM[i, j]> CMV[j]
        NOTUSED -> True
        Note that the LCM is symmetric, i.e. LCM[i,j]=LCM[j,i] for all i and j.
    """
    pum = [[True for _ in range(15)] for _ in range(15)]
    nr_of_rows, nr_of_cols = len(lcm), len(lcm[0])
    for i in range(nr_of_rows):
        if puv[i]:
            for j in range(nr_of_cols):
                if lcm[i][j] == CONNECTORS.ANDD:
                    truth_value = cmv[i] and cmv[j]
                    if truth_value == False:
                        pum[i][j] = False
                elif lcm[i][j] == CONNECTORS.ORR:
                    truth_value = cmv[i] or cmv[j]
                    if truth_value == False:
                        pum[i][j] = False
    return pum
pass


def compute_FUV(pum, puv):
    """
        FUV[i] = True of PUV[i] is False or all elements in PUM row i are True
    """
    return [all(row) or not puv[i] for i, row in enumerate(pum)]

def compute_LAUNCH(fuv):
    """
        True if all elements of FUV are True
    """
    return all(fuv)

def decide():
    
    # Read input from json
    parsed_input = handle_input()
    nr_of_data_points  : int               = parsed_input[0]
    data_points : List[NDArray[float64]]   = parsed_input[1]
    lic_parameters  : Parameters           = parsed_input[2]
    lcm         : List[List[CONNECTORS]]   = parsed_input[3]
    puv         : List[bool]               = parsed_input[4]
    
    # Compute launch logic and print decision
    cmv = compute_cmv(lic_parameters, nr_of_data_points, data_points)
    pum = compute_PUM(cmv, puv, lcm)
    fuv = compute_FUV(pum, puv)

    if compute_LAUNCH(fuv):
        print("YES")
    else:
        print("NO")

def compute_cmv(lic_parameters, nr_of_data_points, points):
    """
        Computes the CMV by evaluating each LIC.

        Parameters
        ----------
        puv : (`vector`)
            The PUV.
        lic_parameters : (`?`)
            The LIC parameters.
        nr_of_data_points : (`int`)
            The number of data points.
        points : (`list[tuple[int?, int?]]`)
            The data points.
            
        Returns
        ----------
        cmv : (`vector`)
            The CMV.
    """

    cmv = [True] * NUMBER_OF_CONDITIONS
    
    cmv[0] = evaluate_LIC_0(nr_of_data_points, points, lic_parameters)
    cmv[1] = evaluate_LIC_1(nr_of_data_points, points, lic_parameters)
    cmv[2] = evaluate_LIC_2(nr_of_data_points, points, lic_parameters)
    cmv[3] = evaluate_LIC_3(nr_of_data_points, points, lic_parameters)
    cmv[4] = evaluate_LIC_4(nr_of_data_points, points, lic_parameters)
    cmv[5] = evaluate_LIC_5(nr_of_data_points, points, lic_parameters)
    cmv[6] = evaluate_LIC_6(nr_of_data_points, points, lic_parameters)
    cmv[7] = evaluate_LIC_7(nr_of_data_points, points, lic_parameters)
    cmv[8] = evaluate_LIC_8(nr_of_data_points, points, lic_parameters)
    cmv[9] = evaluate_LIC_9(nr_of_data_points, points, lic_parameters)
    cmv[10] = evaluate_LIC_10(nr_of_data_points, points, lic_parameters)
    cmv[11] = evaluate_LIC_11(nr_of_data_points, points, lic_parameters)
    cmv[12] = evaluate_LIC_12(nr_of_data_points, points, lic_parameters)
    cmv[13] = evaluate_LIC_13(nr_of_data_points, points, lic_parameters)
    cmv[14] = evaluate_LIC_14(nr_of_data_points, points, lic_parameters)

    return cmv



