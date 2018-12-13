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

	A tree has no parent edges. 

	Attributes :
		- name (str): Name assigned to the tree
		- child_edges (list of Edge obj):
		 List of immediate child edges to the root of the tree
		- obj (str): "Tree"  
		- depth (str): Depth of the tree - always 0

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

	def __repr__(self):
		#return("Tree: {}".format(self.name))
		return(self.name)

	def add_child_edge(self, edge_obj):
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
		-  parent (Tree obj or Node obj): The parent
			of the edge. Can either be a Tree or a Node

		TODO
			- Add assert that parent must be either a 
			  tree or a node
	
	


	'''
	def __init__(self, val, parent, child):
		self.name = val
		self.parent = parent
		#self.parent_type = parent.obj
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

	@property
	def parent_type(self):
		return(self.parent.obj)
