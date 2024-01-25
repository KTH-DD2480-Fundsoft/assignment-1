import math

# CONSTANT
PI = math.pi

# TYPE DECLARATIONS
from enum import Enum
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
def DECIDE():
    print("hello from DECIDE")
    pass  # Implementation you must write

def main():
    DECIDE()

if __name__ == "__main__":
    main()