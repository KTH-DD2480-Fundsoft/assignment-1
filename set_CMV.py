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

def set_CMV_14(num_points, datapoints, parameters):
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
    if num_points < 5: return False

    e_pts = parameters["EPTS"]
    f_pts = parameters["FPTS"]
    area1 = parameters["AREA1"]
    area2 = parameters["AREA2"]
    offset1 = e_pts + 1 
    offset2 = f_pts + 1 
    cond1 = False 
    cond2 = False 
    i = 0

    while i + offset1 + offset2 < num_points and not (cond1 and cond2):
        p1 = datapoints[i]
        p2 = datapoints[i+offset1]
        p3 = datapoints[i+offset1+offset2]
        v1 = p2-p1
        v2 = p3-p1
        triangle_area = np.abs(np.cross(v1,v2))/2
        cond1 = cond1 or triangle_area > area1
        cond2 = cond2 or triangle_area < area2
        i += 1
    return cond1 and cond2

