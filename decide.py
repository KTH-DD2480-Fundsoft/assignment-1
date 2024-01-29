import math
from enum import Enum
from set_CMV import set_CMV

# CONSTANT
PI = math.pi

# TYPE DECLARATIONS
class CONNECTORS(Enum):
    NOTUSED = 777
    ORR = 778   # Assigned automatically as 1 + previous value
    ANDD = 779  # Assigned automatically as 2 + previous value

    
# TYPE DECLARATIONS

COORDINATE : [float] = [] # Typedef for double *COORDINATE

CMATRIX : [[CONNECTORS]] # Typedef for CONNECTORS **CMATRIX

BMATRIX : [[bool]] # Typedef for boolean **BMATRIX

VECTOR : [bool] # Typedef for boolean *VECTOR

class parameters_t:
    def __init__(self, LENGTH1, RADIUS1, EPSILON, AREA1, QPTS, QUADS, DIST, NPTS, KPTS, APTS, BPTS, CPTS, DPTS, EPTS, FPTS, GPTS, LENGTH2, RADIUS2, AREA2):
        self.LENGTH1 = LENGTH1
        self.RADIUS1 = RADIUS1
        self.EPSILON = EPSILON
        self.AREA1 = AREA1
        self.QPTS = QPTS
        self.QUADS = QUADS
        self.DIST = DIST
        self.NPTS = NPTS
        self.KPTS = KPTS
        self.APTS = APTS
        self.BPTS = BPTS
        self.CPTS = CPTS
        self.DPTS = DPTS
        self.EPTS = EPTS
        self.FPTS = FPTS
        self.GPTS = GPTS
        self.LENGTH2 = LENGTH2
        self.RADIUS2 = RADIUS2
        self.AREA2 = AREA2

# Global variable declarations
PARAMETERS = None

# X coordinates of data points
X : [float] = []

# Y coordinates of data points
Y : [float] = []

# Number of data points
NUMPOINTS = None
NUMPOINTS2 = None

# Logical Connector Matrix
LCM : [[CONNECTORS]]

# Preliminary Unlocking Matrix
PUM : [[bool]]

# Conditions Met Vector
CMV : [bool]

# Final Unlocking Vector
FUV : [bool]

# Decision: Launch or No Launch
LAUNCH = bool


# Function you must write
def handle_input():
    pass

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

    # TODO: Remove hardcoding of number of elements?
    cmv = [True] * 15
    
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
                else:
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