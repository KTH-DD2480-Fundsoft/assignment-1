import numpy as np
import math

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

def set_CMV_0(num_points, datapoints, parameters):
    """
        Set CMV_0 based on LIC 0
        
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
            True if LIC 0 is fulfilled, else False    
    """
    length1 = parameters["length1"]

    for i in range(len(datapoints)-1):
        if (np.sqrt(np.square(datapoints[i+1][0]-datapoints[i][0])+np.square(datapoints[i+1][1]-datapoints[i][1])) > length1):
            return True    
    return False

def set_CMV_1():
    pass

def set_CMV_2(num_points, datapoints, parameters):
    epsilon = parameters["epsilon"]
    angle_cond = False
    for i in range(num_points-2):
        vertex = datapoints[i+1]
        
        # Cannot form an angle if the first or third point is equal to the vertex
        if datapoints[i] == vertex or datapoints[i+2] == vertex:
            continue
    
        first_ray = np.array(vertex) - np.array(datapoints[i])
        second_ray = np.array(vertex) - np.array(datapoints[i+2])
        
		# Taken from https://stackoverflow.com/questions/2827393/angles-between-two-n-dimensional-vectors-in-python
        angle = math.atan2(np.linalg.det([second_ray, first_ray]), np.dot(second_ray, first_ray))
        if angle < np.pi - epsilon or angle > np.pi + epsilon:
            angle_cond = True
            break
    return angle_cond

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

    

def set_CMV_11(num_points, datapoints, parameters):
    """
        Set CMV_11 based on LIC 11
        
        Parameters
        ----------
       num_points : (int)
            Total number of data points
        datapoints : List[Tuple[float, float]]
            List of tuples 
        parameters : (Dict)
            Contains all the LIC and CMV parameters 

        Returns Bool depending on if LIC 11 is fulfilled

    """
    gpts = parameters["gpts"]

    if num_points < 3:
        return False
    
    assert (1<= gpts and gpts <= num_points-2), "CMV_11: G_PTS value not between 1 and NUMPOINTS-2"

    for i in range(num_points-gpts-1):
        if datapoints[i+gpts+1][0]-datapoints[i][0] < 0:
            return True
    return False

def set_CMV_12():
    pass

def set_CMV_13():
    pass

def set_CMV_14():
    pass