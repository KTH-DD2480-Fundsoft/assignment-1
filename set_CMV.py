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

def set_CMV_1(numpoints, datapoints, parameters):
	"""
	Set CMV_1 based on LIC 1
	
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
		True if LIC 1 is fulfilled, else False    
    """
	radius_cond = False
	radius = parameters["radius1"]

	for i in range(numpoints - 2):
		p_1 = complex(datapoints[i][0], datapoints[i][1])
		p_2 = complex(datapoints[i+1][0], datapoints[i+1][1])
		p_3 = complex(datapoints[i+2][0], datapoints[i+2][1])

		# We can always encompass a single point
		if p_1 == p_2 == p_3:
			continue

		# If two points are equal, then check if the distance between
		# the differing points is greater than the diameter. 
		if p_1 == p_2:
			if abs(p_3 - p_2) > 2*radius:
				radius_cond = True
			else:
				continue
		elif p_2 == p_3:
			if abs(p_1 - p_3) > 2*radius:
				radius_cond = True
			else:
				continue
		elif p_3 == p_1:
			if abs(p_2 - p_1) > 2*radius:
				radius_cond = True
			else:
				continue
		if radius_cond:
			break

		# Code taken from https://math.stackexchange.com/questions/213658/get-the-equation-of-a-circle-when-given-3-points
		w = (p_3 - p_1)/(p_2 - p_1)

		# If the points are collinear, then they cannot create a circle
		if abs(w.imag) <= 0.0001:
			continue

		c = (p_2 - p_1)*(w - abs(w)**2)/(2j*w.imag) + p_1  
		circumradius = abs(p_1 - c)

		if circumradius > radius:
			radius_cond = True
			break
	return radius_cond

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