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
		self.child_edges = []
		self.obj = "Tree"
		self.depth = 0

	def __repr__(self):
		#return("Tree: {}".format(self.name))
		return(self.name)

	def add_edge(self, edge_obj):
		self.child_edges.append(edge_obj)



class Edge:
	def __init__(self, val, parent, child):
		self.name = val
		self.parent = parent
		self.parent_type = parent.obj
		self.obj = "Edge"
		self.child = child
		self.child_type = child.obj

	def __repr__(self):
		#return("Edge: {}".format(self.name))
		return(self.name)

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

	def add_child_eges(self, child_edge):
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



t.add_edge(e1)
t.add_edge(e2)
t.add_edge(e3)
t.add_edge(e4)


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
n3.add_child_eges(e3_1)


l4 = Leaf(7, 1)
e3_2 = Edge("CABX", n3, l4)
n3.add_child_eges(e3_2)


# e3.add_child_node(n3)
# n3.add_child_eges(e3_1)
# n3.add_child_eges(e3_2)

l4 = Leaf(8)
e4 = Edge("CABX", t, l4)
#e4.add_child_leaf(l4)



t.add_edge(e1)
t.add_edge(e2)
t.add_edge(e3)
t.add_edge(e4)


def print_suffix_tree(suffix_tree):
	for e in suffix_tree.child_edges:
		print("\n{}{} has edge {}".format("\t"*suffix_tree.depth,suffix_tree, e))
		print("{}Edge {} has the child {} of type {}".format("\t"*e.child.depth, e, e.child, e.child_type))

		if e.child_type == "Node":
			#print("recurisng i hope..")
			print_suffix_tree(e.child)



ltest = [('C', 0), ('A', 1), ('B', 2), ('X',3)]
def build_tree(list_of_strings, tree_name):
	t = Tree("Tree for {}".format(tree_name))



print_suffix_tree(t)

# for e in t.edges:
# 	print("{} has edge {}".format(t, e))
# 	print("\tEdge {} has the child {} of type {}".format(e, e.child, e.child_type))
# 	if e.child_type == "Node":
# 		print("\t\tNode has child edges {}".format(e.child.child_edges))
# 	# for n in e.child_nodes:
# 	# 	print("\tEdge {} points to node {}".format(e, n))
# 	# for l in e.child_leaves:
# 	# 	print("\tEdge {} points to leaf {}".format(e, l))



