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

def set_CMV_13(num_points, datapoints, parameters):
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
    
    apts = parameters["APTS"]
    bpts = parameters["BPTS"]
    radius1 = parameters["RADIUS1"]
    radius2 = parameters["RADIUS2"]

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
    if points[0] == points[1] == points[2]:
        return points[0],0
    # Check if two out of three points are the same
    if (points[0] == points[1]) or (points[0] == points[2]) or (points[1] == points[2]):
        if points[0] == points[1]:
            indexes = [0,2]
        if points[0] == points[2]:
            indexes = [0,1]
        if points[1] == points[2]:
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
    
def set_CMV_14():
    pass
