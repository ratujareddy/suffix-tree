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
	return(intersection)


test1 = ['a', 'b', 'a' ,'b']
test2 = ['a', 'b', 'c', 'd', 'a' ,'b']

intersect1 = subtract_lists(test1, test2)


# Suffix tree has n direct edges, n total edges, n total leaves & n total nodes

# Edge *must* have EXACTLY ONE parent which is either
	# a root of a tree
	# a node
# Edge _can_ have n children which is either
	# a node
	# a leaf

# Leaf has ONE parent edge and ONE child edge
# Leaf also has only ONE direct parent Node

# Node has ONE parent edge
# Node can have ONE OR MANY child edges 

# Only a root of a tree and nodes can have child edges

class Tree:
	def __init__(self, tree_name):
		self.name = tree_name
		self.edges = []
		self.obj = "Tree"

	def __repr__(self):
		#return("Tree: {}".format(self.name))
		return(self.name)

	def add_edge(self, edge_obj):
		self.edges.append(edge_obj)



class Edge:
	def __init__(self, val, parent):
		self.name = val
		self.parent = parent
		self.parent_type = parent.obj
		self.obj = "Edge"
		self.child_leaves = []
		self.child_nodes = []

	def __repr__(self):
		#return("Edge: {}".format(self.name))
		return(self.name)

	def add_child_leaf(self, leaf):
		self.child_leaves.append(leaf)
		# TODO add assert, must be a leaf


	def add_child_node(self, node):
		self.child_nodes.append(node)
		# TODO add assert, must be obj node


class Node: 
	def __init__(self, parent_edge):
		self.parent_edge = parent_edge
		self.obj = "Node"
		self.child_edges = []

	def __repr__(self):
		#return("Node of Edge {}".format(self.parent_edge))
		return("Node")

	def add_child_eges(self, child_edge):
		self.child_edges.append(child_edge)




class Leaf:
	def __init__(self, val, parent_edge):
	# val will be an int representing
	# either position of string
	# or time
		self.parent_edge = parent_edge
		self.val = val
		self.obj = "Leaf"
		self.parent = parent_edge.parent
		self.parent_type = parent_edge.parent_type

	def __repr__(self):
		#return("Leaf: {}".format(self.val))
		return("{}".format(self.val))



s = "BCABBCABX"

t = Tree("Tree Test")

e1 = Edge("ABX", t)
l1 = Leaf(9, e1)
e1.add_child_leaf(l1)


e2 = Edge("X", t)
l2 = Leaf(11, e2)
e2.add_child_leaf(l2)


e3 = Edge("BX", t)
l3 = Leaf(10, e3)
e3.add_child_leaf(l3)


e4 = Edge("CABX", t)
l4 = Leaf(8, e4)
e4.add_child_leaf(l4)



t.add_edge(e1)
t.add_edge(e2)
t.add_edge(e3)
t.add_edge(e4)

for e in t.edges:
	print("{} has edge {}".format(t, e))
	for l in e.child_leaves:
		print("\tEdge {} points to leaf {}".format(e, l))




