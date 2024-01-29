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

def set_CMV_3(num_points, data_points, parameters):
    ''' Returns true iff there exists three consecutive
        points in 'data_points' that form a triangle 
        of size greater than parameters["AREA1"]. '''

    area = parameters["AREA1"]
    for i in range(num_points-2):
        v1,v2,v3 = ( np.array(data_points[i])
                   , np.array(data_points[i+1])
                   , np.array(data_points[i+2]) ) 
        a = np.abs(np.cross(v2-v1,v3-v1))/2
        if a > area: return True
    return False

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
