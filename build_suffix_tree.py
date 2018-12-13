from Tree import *
from utils import *

# These functions are used to build the Suffix Tree
# Given a list of tuples (str, int)

def leaf_to_node(old_leaf, old_edge, new_substr, match_val, cur_time):
	''' This function creates a leaf to a Node with two child leaves
	once a substring match is found. It assigns values of
	the intersection of the substrings to the parent edge
	and the outersections to the two children edges.
	The values of the leaves are the values associated
	with the substrings of the child edges plus the parent edge.

	Parameters:
		- old_leaf (Leaf obj): Leaf which will be changed 
		to a node.
		- old_edge (Edge obj): Parent obj of the old leaf.
		- new_subtr (list of str): New list of strings which 
		 will split the leaf
		- match_val (list of str) : The overlap between the 
		 new substr and the value contained in the old edge. 
		 This value will become the new value of the old edge.
		- cur_time (int) : Value associated with the new substr.
		 This will become the value of one of the new leafs.

	Returns:
		- Node obj : This node will have two children and 
		 two child edges atatched as well as a new parent edge.
	'''

	# One child edge will have the outsersection
	# of the match and the old edge
	# The other will have the outersection
	# of the match and the new substr
	sub_edge_val1 = get_outersection(match_val, old_edge.name)
	sub_edge_val2 = get_outersection(match_val, new_substr)

	new_edge = old_edge
	new_edge.name = match_val
	new_depth = old_leaf.depth +1

	#attaching our node to our new edge
	new_node = Node(new_edge, new_depth)
	new_edge.child = new_node

	# adding leaves to our new edge
	new_leaf1 = old_leaf
	new_leaf1.depth = new_depth
	# Attach child to a new edge
	new_child_edge1 = Edge(val = sub_edge_val1, \
		parent = new_node, child = new_leaf1) 

	# Second leaf will hold the new time
	new_leaf2 = Leaf(cur_time, new_depth)
	new_child_edge2 = Edge(get_outersection(match_val, new_substr), \
		new_node, new_leaf2)

	# Attach the children to the node by their edges
	new_node.add_child_edge(new_child_edge1)
	new_node.add_child_edge(new_child_edge2)



	print("MY NEW EDGES ARE {}, {}".format(new_child_edge1, new_child_edge2))

	# returning the new edge which is also connected 
	# to the new node and new leaves
	return(new_edge)



def match_edge(substr, cur_time, tree):
	''' Function to check if any edge matches
	the new incoming substring. If match is found
	a new node with leaves is created.

	Parameters:
		- substr (list of str) : Inputted substring list
		- cur_time (int) : Time (or index) vaue 
		  associated with substr
		- tree (Tree obj) : Tree object 

	Returns:
		- match (bool) : True if match is found, else False
			if True, will create a node
			if False, will create a new leaf
		- tree (Tree obj) : Returns tree with substr attached
			either in node form or as a new leaf
	'''

	match = False
	for edge in tree.child_edges:
		print("\n")
		print("Looking at substr {}".format(substr))
		print("Looking at edge {} which has child {}".format(edge, edge.child))
		itersect_val = subtract_lists(edge.name, substr)
		print(itersect_val)
		if itersect_val:
			print("found a match!")
			if edge.child_type == "Node":
				match_edge(get_outersection(itersect_val, substr),cur_time, edge.child)
			else:
				match = True
				new_edge = leaf_to_node(edge.child, edge, substr, itersect_val, cur_time)
				edge = new_edge
				edge.child.val = tree.val +  edge.name

	return(tree, match)



def build_tree(list_of_strings, tree_name):
	''' Function to generate a Suffix Tree
	from a list of strings. 

	Parameters:
		- list_of_strings (list of tuples (str, int)) :
			List of tuples, first item has the string, 
			second item contains the int value of 
			the time of the process (or index)
		- tree_name (str) : Name you would like to 
			give your tree

	Returns:
		- tree (Tree obj) : Suffix Tree which parses
			the list of strings by string matches to find 
			patterns
	'''
	suffix_tree = Tree(tree_name)
	match = False
	for s_idx in range(len(list_of_strings)-1, -1, -1):
		cur_time = list_of_strings[s_idx][1]
		sublist = list_of_strings[s_idx:]
		substr = [i[0] for i in sublist]
		suffix_tree, match = match_edge(substr,cur_time, suffix_tree)
		if not match:
		# Once it's traversed all the edges
			new_leaf = Leaf(cur_time)
			new_edge = Edge(substr, suffix_tree, new_leaf)
			suffix_tree.add_child_edge(new_edge)

	return(suffix_tree)



def print_suffix_tree(suffix_tree):
	''' Function to recursively print entire Tree

	Will indent with every level.

	Parameters:
		- suffix_tree (Tree obj) : Tree which you
		  want to print

	TODO
		- Maybe make this a tree method?
	'''

	for e in suffix_tree.child_edges:
		print("\n{}{} has edge {}".format("\t"*suffix_tree.depth,suffix_tree, e))
		print("{}Edge {} has the child {} of type {}".format("\t"*e.child.depth, e, e.child, e.child_type))

		if e.child_type == "Node":
			print_suffix_tree(e.child)
		