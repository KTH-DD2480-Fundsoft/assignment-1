import numpy as np
import math

def evaluate_LIC_0(num_points, datapoints, parameters):
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

def evaluate_LIC_1(numpoints, datapoints, parameters):
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

def evaluate_LIC_2(num_points, datapoints, parameters):
    epsilon = parameters["epsilon"]
    angle_cond = False
    for i in range(num_points-2):
        p1 = datapoints[i]
        p2 = datapoints[i+1]
        p3 = datapoints[i+2]
        
        # Cannot form an angle if the first or third point is equal to the vertex
        if np.array_equal(p1, p2) or np.array_equal(p3, p2):
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

def evaluate_LIC_3(num_points, data_points, parameters):
    ''' Returns true iff there exists three consecutive
        points in 'data_points' that form a triangle 
        of size greater than parameters["AREA1"]. '''

    area = parameters["area1"]
    for i in range(num_points-2):
        v1,v2,v3 = ( np.array(data_points[i])
                   , np.array(data_points[i+1])
                   , np.array(data_points[i+2]) ) 
        a = np.abs(np.cross(v2-v1,v3-v1))/2
        if a > area: return True
    return False

def evaluate_LIC_4(num_points, data_points, parameters):
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

def evaluate_LIC_5(num_points, data_points, parameters):
    for i in range(0, num_points-1):
        if (data_points[i][0] > data_points[i+1][0]):
            return True # found two consecutive points such that X[i] > X[+1]
    return False # found no satisfactory points

def evaluate_LIC_6(num_points, data_points, parameters):
    """
        Evaluates the truth value of the LIC 6 given the parameters.
        
        Parameters
        ----------
        num_points : (`int`)
            The total number of data points.
        data_points : (`List[Tuple[float, float]]`)
            The data points.
        parameters : (`Dict[str]`)
            The LIC parameters.

        Returns
        ----------
        truth_value : (`Bool`)
            `True` if the LIC (6) is true given the data, otherwise false.
    """

    N_PTS = parameters['npts']
    DIST = parameters['dist']

    assert (3 <= N_PTS and N_PTS <= num_points), "CMV_11: `N_PTS` value is not between 3 and `num_points`."
    assert (0 <= DIST), "CMV_11: `DIST` value is not greater than or equal to 0."

    # The cases `N_PTS < 3` and `N_PTS > num_points` are still being handled, for robustness.
    if num_points < 3 or N_PTS < 3 or N_PTS > num_points:
        return False

    for i in range(num_points - N_PTS + 1):
        subset = data_points[i:i + N_PTS]
        start_point, end_point = subset[0], subset[-1]
        for point in subset:
            if distance_from_line(point, start_point, end_point) > DIST:
                return True

    return False

# Should be moved to a utils module.
def distance_from_line(point, start_point, end_point):
    """
        Calculate the shortest distance between a point from a line segment defined by two points.
        
        Parameters
        ----------
        point : (`Tuple[float, float]`)
            The point of which the distance will be calculated
        start_point : (`Tuple[float, float]`)
            The start point of the line segment.
        end_point : (`Tuple[float, float]`)
            The end point of the line segment.

        Returns
        ----------
        distance : (`float`)
            The shortest distance between `point` and the line segment defined by
            `start_point` and `end_point`.
    """

    start_point_arr, end_point_arr = np.array(start_point), np.array(end_point)
    if np.array_equal(start_point_arr, end_point_arr):
        # If line degenerates to a point
        return np.linalg.norm(np.array(point) - start_point_arr)

    # Calculate vectors
    line_vec = end_point_arr - start_point_arr
    point_vec = np.array(point) - start_point_arr

    # Calculate the scalar projection of point_vec onto line_vec
    scalar_projection = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)

    if scalar_projection < 0.0 or scalar_projection > 1.0:
        # If the projection falls outside the line segment, use the nearest endpoint
        nearest_point = start_point_arr if scalar_projection < 0.0 else end_point_arr
        return np.linalg.norm(np.array(point) - nearest_point)

    # Perpendicular distance within the segment
    return np.linalg.norm(np.cross(line_vec, point_vec)) / np.linalg.norm(line_vec)

def evaluate_LIC_7(num_points, datapoints, parameters):
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

def evaluate_LIC_8(num_points, datapoints, parameters):
    a_pts = parameters["apts"]
    b_pts = parameters["bpts"]
    radius_1 = parameters["radius1"]
    cmv_cond = False

    if num_points < 5:
        return False 

    # This makes it so p_3 in the last iteration has index num_points - 1 
    num_triplets = num_points - a_pts - b_pts - 2
    for i in range(num_triplets):
        p_1 = datapoints[i]
        p_2 = datapoints[i + a_pts + 1]
        p_3 = datapoints[i + a_pts + b_pts + 2]
        
        if smallest_containting_circle([p_1,p_2,p_3])[1] > radius_1:
            cmv_cond = True
            break
    return cmv_cond

def evaluate_LIC_9(num_points, datapoints, parameters):
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

          if np.array_equal(p1,p2) or np.array_equal(p3, p2):
                continue # "p1 and or p3 can not coincide with p2"
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

def evaluate_LIC_10(num_points, datapoints, parameters):
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

    

def evaluate_LIC_11(num_points, datapoints, parameters):
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

def evaluate_LIC_12(num_points, datapoints, parameters):
    """
        Set CMV_12 based on LIC 12  
        
        Parameters
        ----------
        num_points : (int)
            Total number of data points
        datapoints : List[NDArray[float]]
            List of tuples 
        parameters : (Dict)
            Contains all the LIC and CMV parameters 

        Returns Bool depending on if LIC 12 is fulfilled

    """
    if num_points < 3: return False 

    length1 = parameters["length1"]
    length2 = parameters["length2"]
    offset = parameters["kpts"] + 1
    cond1 = False 
    cond2 = False 
    i = 0
    
    ''' 
    cond1: True if there is at least one set of two points 
           seperated by KPTS with a distance between them 
           greater than LENGTH1 
    cond2: True if there is at least one set of two points 
           seperated by KPTS with a distance between them 
           less than LENGTH2 '''
    while i + offset < num_points and not (cond1 and cond2):
        dist  = np.linalg.norm(datapoints[i] - datapoints[i+offset])
        cond1 = cond1 or (dist > length1) 
        cond2 = cond2 or (dist < length2)
        i += 1
    return cond1 and cond2 





def evaluate_LIC_13(num_points, datapoints, parameters):
    """
        Set CMV_13 based on LIC 13

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
            True if LIC 13 is fulfilled, else False
    """
    
    if num_points < 5:
        return False
    
    apts = parameters["apts"]
    bpts = parameters["bpts"]
    radius1 = parameters["radius1"]
    radius2 = parameters["radius2"]

    outside_radius_1 = False
    inside_radius_2 = False

    for i in range(num_points-apts-bpts-2):
        p_1 = datapoints[i]
        p_2 = datapoints[i+apts+1]
        p_3 = datapoints[i+apts+bpts+2]

        if smallest_containting_circle([p_1,p_2,p_3])[1] > radius1:
            outside_radius_1 = True
        if smallest_containting_circle([p_1,p_2,p_3])[1] <= radius2:
            inside_radius_2 = True
   
    # If not all conditions are met return False
    return outside_radius_1 and inside_radius_2

def smallest_containting_circle(points):
    """
        Computes the smallest enclosing circle for the given points such that all points are either within the circle or
        on its boundray edge

        Parameters
        ----------
        points : List[(x,y).....]
            a list containing tuples of all the points to be enclosed by the circle

        Returns
        ----------
        center_point : tuple(float,float)
            center point of the smallest circle that contains all the points
        smallest_radius : (float)
            radius of the smallest circle that contains all the points
        
    """

    number_of_points = len(points)
    # If there's only one point then it is trivially contained by itself in a circle of radius 0
    if number_of_points == 1:
        return points[0],0
    # If all three points are the same then they can be trivially contained within any circle
    if np.array_equal(points[0], points[1]) and np.array_equal(points[1], points[2]):
        return points[0],0
    # Check if two out of three points are the same
    if np.array_equal(points[0],points[1]) or np.array_equal(points[0], points[2]) or np.array_equal(points[1], points[2]):
        indexes = []
        if np.array_equal(points[0], points[1]):
            indexes = [0,2]
        if np.array_equal(points[0], points[2]):
            indexes = [0,1]
        if np.array_equal(points[1], points[2]):
            indexes = [0,2]
        temp = []
        for index in indexes:
            temp.append(points[index])
        points = temp
        number_of_points = len(points)
        

    # If there are only two points then the smallest circle to contain them is simply the circle with center 
    # between the points with both points on the circles edge
    if number_of_points == 2:
        center_x = (points[0][0]+points[1][0])/2
        center_y = (points[0][1]+points[1][1])/2
        radius   = np.sqrt(np.square(points[0][0]-points[1][0])+np.square(points[0][1]-points[1][1]))/2 
        return (center_x,center_y),radius 
    
    # If len(points) > 2 we must check all pairs and also all triplets of points to find optimal smallest enclosing circle
    # Find smallest circle from pairs of points
    smallest_circle = [(0,0),np.inf]
    for i in range(number_of_points):
        for j in range(i+1,number_of_points):
            center = ((points[i][0]+points[j][0])/2, (points[i][1]+points[j][1])/2)
            radius = np.sqrt(np.square(points[i][0]-points[j][0])+np.square(points[i][1]-points[j][1]))/2 
            temp_circle = [center,radius]
            valid_circle = True
            for k in range(number_of_points):
                if (np.sqrt(np.square(points[k][0]-center[0])+np.square(points[k][1]-center[1]))) > radius: 
                    valid_circle = False

            if (radius < smallest_circle[1]) and valid_circle == True:
                smallest_circle = temp_circle
 
    # Find smallest circle from pairs of points
    # This part is from https://www.geeksforgeeks.org/minimum-enclosing-circle/
    for i in range(number_of_points):
        for j in range(i+1, number_of_points):
            for k in range(j+1,number_of_points):
                # Math formula to find center point of circle from three points
                bx = points[j][0]-points[i][0]
                by = points[j][1]-points[i][1]
                cx = points[k][0]-points[i][0]
                cy = points[k][1]-points[i][1]
                B  = bx * bx + by * by
                C  = cx * cx + cy * cy
                D  = bx * cy - by * cx
                # D == 0 then points are colinear (on the same linear line) and are covered by the previous two point calculations
                if D != 0:
                    I  = [(cy*B - by*C) // (2*D),(bx*C - cx*B) // (2*D)]
                    I[0]+=points[i][0]
                    I[1]+=points[i][1]
                    center = (I[0],I[1])

                    radius = np.sqrt(np.square(I[0]-points[i][0])+np.square(I[1]-points[i][1]))
                    temp_circle = [center,radius]
                    valid_circle = True
                    for l in range(number_of_points):
                        if (np.sqrt(np.square(points[l][0]-center[0])+np.square(points[l][1]-center[1]))/2) > radius: 
                            valid_circle = False

                    if (radius < smallest_circle[1]) and valid_circle == True:
                        smallest_circle = temp_circle
    

    center_point = smallest_circle[0]
    radius = smallest_circle[1]

    return center_point, radius
    
def evaluate_LIC_14(num_points, datapoints, parameters):
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

    e_pts = parameters["epts"]
    f_pts = parameters["fpts"]
    area1 = parameters["area1"]
    area2 = parameters["area2"]
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



