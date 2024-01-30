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

def set_CMV_0():
	pass

def set_CMV_1():
	pass

def set_CMV_2():
	pass

def set_CMV_3():
	pass

def set_CMV_4(num_points, data_points, parameters):
	
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