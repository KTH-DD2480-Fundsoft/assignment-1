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


def decide(puv, lcm, lic_parameters, nr_of_data_points, data_points ):
    cmv = compute_cmv(puv, lic_parameters, nr_of_data_points, data_points)
    return does_pum_not_contain_false_element(lcm, cmv)

def compute_cmv(puv, lic_parameters, nr_of_data_points, points):
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
    
    # cmv[0] = evaluate_lic_0(lic_parameters[0], nr_of_data_points, points)
    
    # cmv[1] = evaluate_lic_1(lic_parameters[1], nr_of_data_points, points)
    
    # cmv[2] = evaluate_lic_2(lic_parameters[2], nr_of_data_points, points)
    
    # cmv[3] = evaluate_lic_3(lic_parameters[3], nr_of_data_points, points)
    
    # cmv[4] = evaluate_lic_4(lic_parameters[4], nr_of_data_points, points)
    
    # cmv[5] = evaluate_lic_5(lic_parameters[5], nr_of_data_points, points)
    
    # cmv[6] = evaluate_lic_6(lic_parameters[6], nr_of_data_points, points)
    
    # cmv[7] = evaluate_lic_7(lic_parameters[7], nr_of_data_points, points)
    
    # cmv[8] = evaluate_lic_8(lic_parameters[8], nr_of_data_points, points)
    
    # cmv[9] = evaluate_lic_9(lic_parameters[9], nr_of_data_points, points)
    
    # cmv[10] = evaluate_lic_10(lic_parameters[10], nr_of_data_points, points)
    
    # cmv[11] = evaluate_lic_11(lic_parameters[11], nr_of_data_points, points)
    
    # cmv[12] = evaluate_lic_12(lic_parameters[12], nr_of_data_points, points)
    
    # cmv[13] = evaluate_lic_13(lic_parameters[13], nr_of_data_points, points)
    
    # cmv[14] = evaluate_lic_14(lic_parameters[14], nr_of_data_points, points)

    pass


def does_pum_not_contain_false_element(lcm, cmv, puv):
    """
        Computes the truth values of the PUM and checks if there is a meaningful
        false element in the PUM which will result in a false element in the FUV,
        and consequently prevent a launch.


        Parameters
        ----------
        lcm : (`matrix`)
            The LCM.
        cmv : (`vector`)
            The CMV.
        puv : (`vector`)
            The PUV.

        Returns
        ----------
        truth_value : (`Bool`)
            True if PUM does not contain a false element which will prevent a launch,
            otherwise False and launch should not occur.
    """
    """ Sort of pseudo for now, just to convey the idea.
    nr_of_rows, nr_of_cols = lcm.shape
    for i in range(nr_of_rows):
        # TODO: Potential out of bounds in "puv[i]"?
        if puv[i]:
            for j in range(nr_of_cols):
                if lcm[i][j] == ANDD:
                    truth_value = cmv[i] and cmv[j]
                    if truth_value == False:
                        return False
                elif lcm[i][j] == ORR:
                    truth_value = cmv[i] or cmv[j]
                    if truth_value == False:
                        return False
    return True
    """
    pass


def main():
    parsed_input = handle_input()
    num_points  : int                      = parsed_input[0]
    data_points : List[Tuple[float,float]] = parsed_input[1]
    lic_parameters  : Parameters           = parsed_input[2]
    lcm         : List[List[CONNECTORS]]   = parsed_input[3]
    puv         : List[bool]               = parsed_input[4]
    should_launch = decide(puv, lcm, lic_parameters, nr_of_data_points, data_points)
    if should_launch:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()