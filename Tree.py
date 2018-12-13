# This file has all the classes 
# Which build a Suffix-Tree


# Some thoughts when creating these classes:

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
	'''A tree contains:
		- n > 0  Edges
		- m > 0 Leaves 
		- p > 0 Nodes

	Note: A tree has no parent edges. 

	Attributes:
		- name (str): Name assigned to the tree
		- child_edges (list of Edge objs):
		 List of immediate child edges to the root of the tree
		- obj (str): "Tree"  
		- depth (int): Depth of the tree - always 0

	TODO 
		- add max_depth
		- method to find object at max depth 
		- Way to traverse the tree
		  and get back strings of edges
		  while traversing
		- Maybe check type with instance rather than obj attr?
	'''

	def __init__(self, tree_name):
		''' Initialize the tree

		Parameters:
			tree_name (str): Name of the tree.
				Arbitrary name, not used for anything 
				except reference.
		'''
		self.name = tree_name
		self.child_edges = []
		self.obj = "Tree"
		self.depth = 0
		self.val = []

	def __repr__(self):
		'''Returns the name of the tree'''
		return(self.name)

	def add_child_edge(self, edge_obj):
		'''Adds a child edge object to a list of child edges'''
		self.child_edges.append(edge_obj)




class Edge:
	'''An edge contains:
		- Exactly 1 child which is either:
			- A node, a leaf
		- Exactly 1 parent which is either:
			- A tree (root), a node
		- A value (name) which in this case
			is a list of strings

	Attributes:
		- name (list of strings): This contains
			the value associated with that edge.
			In the context of using the suffix tree
			for pattern matching in strings (or a list
			of strings), this name is associated with 
			the pattern in the string. Its leaf denotes
			the index of the beginning of the pattern 
			(or the time stamp of a process)
		- parent (Tree obj or Node obj): The immediate parent
			of the edge. Can either be a Tree or a Node. 
			Note: Adding a parent also adds the Edge to the 
			Parent's children. 
		- obj (str): "Edge"
		- child (Node obj or Leaf obj): The immediate child  
			of the edge. Can either be a Leaf or a Node
		- child_type (str): The object type of the child 
		- parent_type (str): The object type of the parent

	TODO
		- Add assert that parent must be either a 
		  tree or a node
		- Add assert that child must be either a
		  leaf or a node
	
	'''
	def __init__(self, val, parent, child):
		self.name = val
		self.parent = parent
		self.obj = "Edge"
		self.child = child

	def __repr__(self):
		'''Returns a stirng representation of the list
		of strings contained in the edge'''
		return("{}".format(self.name))

	@property
	def child_type(self):
		return(self.child.obj)

	@property
	def parent_type(self):
		return(self.parent.obj)


class Node(Tree): 
	''' A node contains:
		- Exactly one parent edge
		- n > 1 child edge(s)

	Attributes:
		- parent_edge (Edge obj): The immediate 
			parent edge of the node
		- child_edges (list of Edge objs): A list
			of all the immediate child edges of the node
		- obj (str): "Node"
		- depth (int): The depth of the node. Always > 1.
			The depth of the node is equivalent to 
			the depth of its immediate children. 
	
	Note: There is no inherent "value" associated 
	with a node (yet).

	TODO
		- Maybe make the "value" a composite of 
		  the preceding edges??? This would help find 
		  the full string you are looking for. 
	'''

	def __init__(self, parent_edge, depth = 1):
		self.parent_edge = parent_edge
		self.obj = "Node"
		self.child_edges = []
		self.depth = depth
		self.val = []

	def __repr__(self):
		#return("Node of Edge {}".format(self.parent_edge))
		return("Node {}".format(self.val))
		#return("Node")


class Leaf:
	def __init__(self, val, depth = 0):


		self.val = val
		self.obj = "Leaf"
		self.depth = depth
		#self.parent = parent_edge.parent
		#self.parent_type = parent_edge.parent_type

	def __repr__(self):
		#return("Leaf: {}".format(self.val))
		return("{}".format(self.val))