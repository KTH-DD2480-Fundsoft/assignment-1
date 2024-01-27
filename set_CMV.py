import numpy as np
def set_CMV():
    """
        A list of the 15 Launch Interceptor Conditions (LIC)
        

        Parameters
        ----------
        parameter1 : (`str`)
            Description of `parameter1`.
        parameter2 : (`int`)
            Description of `parameter2`

        Returns
        ----------
        descriptive_name_of_returned_value : (`int`)
            Description on what is returned
    """
    set_CMV_0()
    pass

def set_CMV_0():
    pass

def set_CMV_1():
    pass

def set_CMV_2():
    pass

def set_CMV_3():
    pass

def set_CMV_4():
    pass

def set_CMV_5():
    pass

def set_CMV_6():
    pass

def set_CMV_7():
    pass

def set_CMV_8():
    pass

def set_CMV_9():
    pass

def set_CMV_10(num_points, datapoints, parameters):
    """
        Set CMV_10 based on LIC 10

        Parameters
        ----------
        num_points : (int)
            Total number of data points
        datapoints : List[Tuple[float, float]]
            List of tuples 
        parameters : (Dict)
            Contains all the LIC and CMV parameters 
        Returns
        ----------
        Bool
            True if LIC 10 is fulfilled, else False
    """
    if num_points < 5:
        return False
    
    epts  = parameters["epts"]
    fpts  = parameters["fpts"]
    area1 = parameters["area1"]
    
    assert (epts+fpts <= num_points-3), "Sum of E_PTS and F_PTS should at most be NUMPOINTS-3"

    for i in range(num_points-epts-fpts-2):
        # The area of the triangle between the three data points is computed using a generalized cross product of 2D vectors
        # Vectors a and b are calculated by finding the distance between the different points
        # Both vectors originate from the same origin point (point 1) permitting the cross product operation
        # Components of vector a which is the difference between point 2 and point 1. 
        a_x = datapoints[i+epts+1][0] - datapoints[i][0] 
        a_y = datapoints[i+epts+1][1] - datapoints[i][1]
        # Components of vector b which is the difference between point 3 and point 1
        b_x = datapoints[i+epts+fpts+2][0] - datapoints[i][0]
        b_y = datapoints[i+epts+fpts+2][1] - datapoints[i][1]
        # Simplified cross product for 2D vectors 
        area_of_triangle = np.abs(0.5*(a_x*b_y - a_y*b_x))

        if area_of_triangle > area1:
            return True

    return False 

    

def set_CMV_11():
    pass

def set_CMV_12():
    pass

def set_CMV_13():
    pass

def set_CMV_14():
    pass
