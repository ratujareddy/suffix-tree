def subtract_lists(l1, l2):
	''' Function to subtract two lists from eachother
	while maintaining order 
	
	Example: 
	  l1 = ['a', 'b', 'a' ,'b', 'd']
	  l2 = ['a', 'b', 'c', 'd', 'a' ,'b']

	  Returns: ['a', 'b']

	NOTE: len(l2) >= len(l1)

	Parameters:
		l1 (list): List of strings of length n
		l2 (list): List of strings of len >= n 
	
	TODO
		- Add assert regarding string length
	'''
	intersection = []
	for i in range(len(l1)):
		if l1[i] == l2[i]:
			intersection = intersection+[l1[i]]
		else:
			return(intersection)
	return(intersection)



def get_outersection(l1, l2):
	''' Function to get the outersection
	of two lists of strings while maintaining order 

	Will retrieve strings which are in l2 
	but NOT l1
	
	Example: 
	  l1 = ['a', 'b', 'a' ,'b', 'd']
	  l2 = ['a', 'b', 'c', 'd', 'a' ,'b']

	  Returns: ['c', 'd', 'a' ,'b']

	NOTE: len(l2) >= len(l1)

	Parameters:
		l1 (list): List of strings of length n
		l2 (list): List of strings of len >= n
	
	TODO
		- Add assert regarding string length
	'''

	outersection = []
	for i in range(len(l1)):
		if l1[i] == l2[i]:
			outersection = l2[i+1:]
		else:
			return(outersection)
	return(outersection)