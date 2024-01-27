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

def set_CMV_10():
	pass

def set_CMV_11(G_PTS, NUMPOINTS, x, y):
	"""
        Set CMV_11 based on LIC 11
		
		Parameters
        ----------
        G_PTS : (int)
            Number of consecutive points between the two datapoints x[i] and x[j].
		NUMPOINTS : (int)
			Number of datapoints. Equal to the length of the data vectors x and y
        x       : (list of ints/floats)
            List of x coordinates in the trajectory plane
		y       : (list of ints/floats)
            List of y coordinates in the trajectory plane

        Returns Bool depending on if LIC 11 is fulfilled
	"""
	if NUMPOINTS < 3:
		return False
	assert (isinstance(G_PTS, int)), "G_PTS needs to be an int"
	assert (isinstance(NUMPOINTS, int)), "NUMPOINTS needs to be an int"
	assert (1<= G_PTS and G_PTS <= NUMPOINTS-2), "CMV_11: G_PTS value not between 1 and NUMPOINTS-2"
	assert (len(x) == NUMPOINTS), "length of x vector should be equal to number of data points (NUMPOINTS)"
	
	for i in range(NUMPOINTS-G_PTS-1):
		if x[i+G_PTS+1]-x[i] < 0:
			return True
	return False

def set_CMV_12():
	pass

def set_CMV_13():
	pass

def set_CMV_14():
	pass