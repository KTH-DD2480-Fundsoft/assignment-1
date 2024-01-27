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

def set_CMV_0(LENGTH1, x, y):
    """
        Set CMV_0 based on LIC 1
		
		Parameters
        ----------
        LENGTH1 : (int/float)
            Maximum length between a set of two consequative points.
        x       : (list of ints/floats)
            List of x coordinates in the trajectory plane
		y       : (list of ints/floats)
            List of y coordinates in the trajectory plane

        Returns Bool depending on if LIC 1 is fulfilled
	"""
    assert (len(x)==len(y)), "Coordinate vectors x and y should be of same length"
    assert (isinstance(LENGTH1, (float, int)) and LENGTH1 >= 0), "Parameter LENGTH1 should be and int or float with value greater or equal to 0"
	
    for i in range(len(x)-1):
        if (np.sqrt(np.square(x[i+1]-x[i])+np.square(y[i+1]-y[i])) > LENGTH1):
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