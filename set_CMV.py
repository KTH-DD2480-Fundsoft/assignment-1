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
    # set_CMV_0()
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

def set_CMV_2(num_points, datapoints, parameters):
    epsilon = parameters["epsilon"]
    angle_cond = False
    for i in range(num_points-2):
        p1 = datapoints[i]
        p2 = datapoints[i+1]
        p3 = datapoints[i+2]
        
        # Cannot form an angle if the first or third point is equal to the vertex
        if p1 == p2 or p3 == p2:
            continue

        a = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        b = np.sqrt((p3[0] - p2[0])**2 + (p3[1] - p2[1])**2)
        c = np.sqrt((p3[0] - p1[0])**2 + (p3[1] - p1[1])**2)

        # c^2 = a^2 + b^2 - 2abcos(angle p1p2p3)
        # angle p1p2p3 = arccos((a^2 + b^2 - c^2) / (2ab)), see https://en.wikipedia.org/wiki/Law_of_cosines
        angle = np.arccos((a**2 + b**2 - c**2) / (2 * a * b) )

        if angle < np.pi - epsilon or angle > np.pi + epsilon:
            angle_cond = True
            break
    return angle_cond

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

def set_CMV_4(num_points, data_points, parameters):
    ''' Returns true iff at least one set of qpts consecutive points
        occupy more than quads quadrants, and the following is true:
        (2 ≤ Q_PTS ≤ NUMPOINTS), (1 ≤ QUADS ≤ 3) '''
	
    qpts = parameters['qpts']
    quads = parameters['quads']
	
    if quads >= qpts:
		# qpts consecutive points can not be in more than quads quadrants
        return False # condition impossible

    for i in range(0, num_points+1-qpts):
        occupied_quads = [0, 0, 0, 0]
		# go through qpts consecutive elements in points counting from element i, check visited quadrants in list occupied_quads
		
        for j in range(0, qpts):
            (x, y) = data_points[i + j]
            if (x >= 0 and y >= 0):
                occupied_quads[0] = 1
            elif (x < 0 and y >= 0):
                occupied_quads[1] = 1
            elif (x < 0 and y < 0):
                occupied_quads[2] = 1
            else:
                occupied_quads[3] = 1
            if sum(occupied_quads) > quads:
				# more than quads quadrants have been vidited
                return True # condition met
			
    return False # condition not met

def set_CMV_5(num_points, data_points, parameters):
    for i in range(0, num_points-1):
        if (data_points[i][0] > data_points[i+1][0]):
            return True # found two consecutive points such that X[i] > X[+1]
    return False # found no satisfactory points

def set_CMV_6():
    pass

def set_CMV_7(num_points, datapoints, parameters):
    k_pts = parameters["kpts"]
    length1 = parameters["length1"]
    coordinates = np.array(datapoints)
    cmv_cond = False

    if num_points < 3:
        return False

    # With k_pts intervening points, the last point in the loop 
    # point will have index num_points - k_pts - 2
    num_pairs = num_points - k_pts - 1
    for i in range(num_pairs):
        point = coordinates[i + k_pts + 1]
        if np.sqrt(np.sum((coordinates[i] - point)**2)) > length1:
            cmv_cond = True
            break

    return cmv_cond

def set_CMV_8():
    pass

def set_CMV_9(num_points, datapoints, parameters):
    cpts = parameters['cpts']
    dpts = parameters['dpts']
    epsilon = parameters['epsilon']

    if num_points < 5:
          return False # "When NUMPOINTS < 5, the condition is not met"

    if not (1 <= cpts and 1 <= dpts):
          # TD: raise error here instead?
          return False # conditions not met for cpts and dpts
    if not (cpts + dpts <= num_points - 3):
          # TD: raise error here instead?
          return False # conditions not met for cpts and dpts

    # going through each possible set of three points and checking angle
    for i in range(0, num_points - cpts - dpts - 2):
          # current three points, separated by cpts and dpts points respectively
          p1 = datapoints[i]
          p2 = datapoints[i+cpts+1]
          p3 = datapoints[i+cpts+1+dpts+1]

          if (p1 == p2 or p3 == p2):
                return False # "p1 and or p3 can not coincide with p2"
          else:
                
                a = np.sqrt(
                      (p1[0]-p2[0])**2 +
                      (p1[1]-p2[1])**2
                )
                b = np.sqrt(
                      (p3[0]-p2[0])**2 +
                      (p3[1]-p2[1])**2
                )
                c = np.sqrt(
                      (p3[0]-p1[0])**2 +
                      (p3[1]-p1[1])**2
                )
                # c^2 = a^2 + b^2 - 2abcos(angle p1p2p3)
                # angle p1p2p3 = arccos((a^2 + b^2 - c^2) / (2ab)), see https://en.wikipedia.org/wiki/Law_of_cosines
                angle = np.arccos((a**2 + b**2 - c**2) / (2 * a * b) )

                if ((angle < np.pi - epsilon) or (angle > np.pi + epsilon)):
                      # angle p1p2p3 can not be in the range PI ± epsilon
                      return True
    return False

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

    pass

