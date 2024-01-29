import json
import sys
from enum import Enum
from numpy import array, float64
from numpy.typing import NDArray
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
        params = [("LENGTH1",float), ("RADIUS1",float), ("EPSILON",float),
                  ("AREA1",float), ("QPTS",int), ("QUADS",int), ("DIST",float),
                  ("NPTS",int), ("KPTS",int), ("APTS",int), ("BPTS",int),
                  ("CPTS",int), ("DPTS",int), ("EPTS",int), ("FPTS",int),
                  ("GPTS",int), ("LENGTH2",float), ("RADIUS2",float), ("AREA2",float)  ]
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
    data_points : List[NDArray[float64]]   = parsed_input[1]
    parameters  : Parameters               = parsed_input[2]
    lcm         : List[List[CONNECTORS]]   = parsed_input[3]
    puv         : List[bool]               = parsed_input[4]
    print(parsed_input)
    set_CMV()
    set_PUM()
    set_FUV()

if __name__ == "__main__":
    DECIDE()
