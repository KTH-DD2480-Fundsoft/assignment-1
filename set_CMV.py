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

def set_CMV_10():
    pass

def set_CMV_11():
    pass

def set_CMV_12():
    pass

def set_CMV_13():
    pass

def set_CMV_14():
    pass