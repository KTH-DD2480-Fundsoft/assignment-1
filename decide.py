import json
import os
import sys
from enum import Enum
from typing import List, Tuple, TypedDict
from set_CMV import set_CMV


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



def handle_input() ->  \
           Tuple[ int
                , List[Tuple[float,float]]
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
   
    # Check if we got exactly one argument
    assert len(sys.argv) == 2 

    # Check if the file exists
    file_path = sys.argv[1]
    
    assert os.path.isfile(file_path)

    with open(file_path) as file_descriptor: 
        # Parse the json 
        data = json.load(file_descriptor)
   
    num_points = data['numpoints']
    datapoints = [(l[0],l[1]) for l in data['datapoints']]
    
    assert len(datapoints) == num_points

    parameters = data['parameters'] 
    
    # check that all parameters are present
    params = ["LENGTH1", "RADIUS1", "EPSILON",
              "AREA1", "QPTS", "QUADS", "DIST",
              "NPTS", "KPTS", "APTS", "BPTS",
              "CPTS", "DPTS", "EPTS", "FPTS",
              "GPTS", "LENGTH2", "RADIUS2", "AREA2"  ]
    assert len(params) == len(parameters)
    assert all([key in parameters for key in params]) 
        
    
    # extract LCM and PUV. And check that they are of correct size
    lcm = [[CONNECTORS(e) for e in row] for row in data['LCM']] 
    puv = data['PUV']

    assert len(lcm)    == NUMBER_OF_CONDITIONS
    assert len(lcm[0]) == NUMBER_OF_CONDITIONS
    assert len(puv)    == NUMBER_OF_CONDITIONS

    return (num_points,datapoints,parameters,lcm,puv) 


def set_PUM():
    """
        PUM[i, j] = CMV[i] <LCM[i, j]> CMV[j]
        NOTUSED -> True
        Note that the LCM is symmetric, i.e. LCM[i,j]=LCM[j,i] for all i and j.
    """
    pass


def set_FUV():
    """
        FUV[i] = True of PUV[i] is False or all elements in PUM row i are True
    """
    pass

def set_LAUNCH():
    """
        True if all elements of FUV are True
    """
    pass


def DECIDE():
    parsed_input = handle_input()
    num_points  : int                      = parsed_input[0]
    data_points : List[Tuple[float,float]] = parsed_input[1]
    parameters  : Parameters               = parsed_input[2]
    lcm         : List[List[CONNECTORS]]   = parsed_input[3]
    puv         : List[bool]               = parsed_input[4]
    print(data_points)
    set_CMV()
    set_PUM()
    set_FUV()

if __name__ == "__main__":
    DECIDE()
