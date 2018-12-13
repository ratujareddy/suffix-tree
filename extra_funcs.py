# if we have to lists of strings
# function to find overlap
# in order

# ie l1 = ['a', 'b', 'c', 'd', 'a' ,'b']
# l2 = ['a', 'b', 'a' ,'b']

# overlap is ['a', 'b']

def subtract_lists(l1, l2):
	# note: l2 should always be longest

	intersection = []
	for i in range(len(l1)):
		if l1[i] == l2[i]:
			intersection = intersection+[l1[i]]
		else:
			return(intersection)
	return(intersection)


test1 = ['a', 'b', 'a' ,'b']
test2 = ['a', 'b', 'c', 'd', 'a' ,'b']

intersect1 = subtract_lists(test1, test2)




class Tree:
	def __init__(self, tree_name):
		self.name = tree_name
		self.child_edges = []
		self.obj = "Tree"
		self.depth = 0

	def __repr__(self):
		#return("Tree: {}".format(self.name))
		return(self.name)

	def add_child_edge(self, edge_obj):
		self.child_edges.append(edge_obj)



class Edge:
	def __init__(self, val, parent, child):
		self.name = val
		self.parent = parent
		self.parent_type = parent.obj
		self.obj = "Edge"
		self.child = child
		#self.child_type = child.obj

	def __repr__(self):
		#return("Edge: {}".format(self.name))
		#return(self.name)
		return("{}".format(self.name))

	@property
	def child_type(self):
		return(self.child.obj)

	# def add_child_leaf(self, leaf):
	# 	self.child_leaves.append(leaf)
	# 	# TODO add assert, must be a leaf


	# def add_child_node(self, node):
	# 	self.child_nodes.append(node)
	# 	# TODO add assert, must be obj node


class Node: 
	def __init__(self, parent_edge, depth = 1):
		self.parent_edge = parent_edge
		self.obj = "Node"
		self.child_edges = []
		self.depth = depth

	def __repr__(self):
		#return("Node of Edge {}".format(self.parent_edge))
		return("Node")

	def add_child_edge(self, child_edge):
		self.child_edges.append(child_edge)




class Leaf:
	def __init__(self, val, depth = 0):
	# val will be an int representing
	# either position of string
	# or time
		#self.parent_edge = parent_edge
		self.val = val
		self.obj = "Leaf"
		self.depth = depth
		#self.parent = parent_edge.parent
		#self.parent_type = parent_edge.parent_type

	def __repr__(self):
		#return("Leaf: {}".format(self.val))
		return("{}".format(self.val))



##################

t = Tree("Tree for String 'CABX'")

l1 = Leaf(9)
e1 = Edge("ABX", t, l1)



l2 = Leaf(11)
e2 = Edge("X", t, l2)

#e2.add_child_leaf(l2)



l3 = Leaf(10)
e3 = Edge("BX", t, l3)
#e3.add_child_leaf(l3)



l4 = Leaf(8)
e4 = Edge("CABX", t, l4)
#e4.add_child_leaf(l4)



t.add_child_edge(e1)
t.add_child_edge(e2)
t.add_child_edge(e3)
t.add_child_edge(e4)


##################

t = Tree("Tree for String 'BCABX'")


l1 = Leaf(9)
e1 = Edge("ABX", t, l1)
#e1.add_child_leaf(l1)



l2 = Leaf(11)
e2 = Edge("X", t, l2)
#e2.add_child_leaf(l2)


n3 = Node(e3, 1)
e3 = Edge("B", t, n3)

l3 = Leaf(10, 1)
e3_1 = Edge("X", n3, l3)
n3.add_child_edge(e3_1)


l4 = Leaf(7, 1)
e3_2 = Edge("CABX", n3, l4)
n3.add_child_edge(e3_2)


# e3.add_child_node(n3)
# n3.add_child_edge(e3_1)
# n3.add_child_edge(e3_2)

l4 = Leaf(8)
e4 = Edge("CABX", t, l4)
#e4.add_child_leaf(l4)



t.add_child_edge(e1)
t.add_child_edge(e2)
t.add_child_edge(e3)
t.add_child_edge(e4)



def print_suffix_tree(suffix_tree):
	for e in suffix_tree.child_edges:
		print("\n{}{} has edge {}".format("\t"*suffix_tree.depth,suffix_tree, e))
		print("{}Edge {} has the child {} of type {}".format("\t"*e.child.depth, e, e.child, e.child_type))

		if e.child_type == "Node":
			#print("recurisng i hope..")
			print_suffix_tree(e.child)

#print_suffix_tree(t)


ltest = [ ('B', 3), ('C', 4), ('A', 5), \
	('B', 6),('B', 7), ('C', 8), \
	('A', 9), ('B', 10), ('X', 11)]


# ltest = [ ('B', 6), ('B', 7), ('C', 8), \
# 	('A', 9), ('B', 10), ('X', 11), ('$', 12)]

t = Tree("My new tree")
l1 = Leaf(12)
e1 = Edge(["$"], t, l1)

l2 = Leaf(10)
e2 = Edge(["B", "X"],t,l2)


t.add_child_edge(e1)
#t.add_child_edge(e2)


s_test = ["B", "C", "A", "B", "X"]

#[subtract_lists(x, s_test) for x in t.child_edges]

def get_outersection(l1, l2):
	# l2 should be longest

	outersection = []
	for i in range(len(l1)):
		if l1[i] == l2[i]:
			outersection = l2[i+1:]
		else:
			return(outersection)
	return(outersection)

osect = get_outersection(['B'], ['B', 'A', 'X'])



def leaf_to_node(old_leaf, old_edge, new_substr, match_val, cur_time):
	# print("sldj22f")
	# print(old_edge.name)
	sub_edge_val1 = get_outersection(match_val, old_edge.name)
	sub_edge_val2 = get_outersection(match_val, new_substr)


	new_edge = old_edge
	new_edge.name = match_val
	new_depth = old_leaf.depth +1

	#attaching our node to our new edge
	new_node = Node(new_edge, new_depth)
	new_edge.child = new_node
	#new_edge.child_type = new_node.obj
	# print("this is my new node {}".format(new_node))
	# print(get_outersection(match_val, new_substr))

	# adding leaves to our new edge
	new_leaf1 = old_leaf
	new_leaf1.depth = new_depth

	# print("this is my new leaf {}".format(new_leaf1))
	# print(type(new_leaf1))
	# print("sldjf")
	# print(old_edge.name)
	new_child_edge1 = Edge(sub_edge_val1, \
		new_node,new_leaf1) 

	new_leaf2 = Leaf(cur_time, new_depth)
	new_child_edge2 = Edge(get_outersection(match_val, new_substr), \
		new_node, new_leaf2)

	new_node.add_child_edge(new_child_edge1)
	new_node.add_child_edge(new_child_edge2)

	print("MY NEW EDGES ARE {}, {}".format(new_child_edge1, new_child_edge2))

	# returning the new edge which is also connected to the new node
	# and new leaves
	return(new_edge)

	


def match_edge(substr, cur_time, tree):
	match = False
	# cur_time = sub_list_of_strings[s_idx][1]
	# sublist = sub_list_of_strings[s_idx:]
	# substr = [i[0] for i in sublist]
	for edge in tree.child_edges:
		print("\n")
		print("Looking at substr {}".format(substr))
		print("Looking at edge {} which has child {}".format(edge, edge.child))
		itersect_val = subtract_lists(edge.name, substr)
		print(itersect_val)
		if itersect_val:
			print("found a match!")
			if edge.child_type == "Node":
				print("AAAH RECURSING HERE")
				match_edge(get_outersection(itersect_val, substr),cur_time, edge.child)
			else:
				match = True
				new_edge = leaf_to_node(edge.child, edge, substr, itersect_val, cur_time)
				edge = new_edge
	return(tree, match)





def build_tree(list_of_strings, tree):
	#t = Tree("Tree for {}".format(tree_name))
	match = False
	for s_idx in range(len(list_of_strings)-1, -1, -1):
		cur_time = list_of_strings[s_idx][1]
		sublist = list_of_strings[s_idx:]
		substr = [i[0] for i in sublist]
		#print(substr, cur_time)

		tree, match = match_edge(substr,cur_time, tree)
		# for edge in tree.child_edges:
		# 	print("\n")
		# 	print("Looking at substr {}".format(substr))
		# 	print("Looking at edge {} which has child {}".format(edge, edge.child))
		# 	itersect_val = subtract_lists(edge.name, substr)
		# 	print(itersect_val)
		# 	if itersect_val:
		# 		print("found a match!")
		# 		match = True
		# 		new_edge = leaf_to_node(edge.child, edge, substr, itersect_val, cur_time)
		# 		edge = new_edge
				#break
			#break
		if not match:
		# Once it's traversed all the edges
			new_leaf = Leaf(cur_time)
			new_edge = Edge(substr, tree, new_leaf)
			t.add_child_edge(new_edge)

	return(tree)
			#print(edge, substr)

		#[i[0] for i in a]
		#print(list_of_strings[s_idx] , s_idx)

suffix_tree = build_tree(ltest, t)




# for e in t.edges:
# 	print("{} has edge {}".format(t, e))
# 	print("\tEdge {} has the child {} of type {}".format(e, e.child, e.child_type))
# 	if e.child_type == "Node":
# 		print("\t\tNode has child edges {}".format(e.child.child_edges))
# 	# for n in e.child_nodes:
# 	# 	print("\tEdge {} points to node {}".format(e, n))
# 	# for l in e.child_leaves:
# 	# 	print("\tEdge {} points to leaf {}".format(e, l))



