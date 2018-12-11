
ebay_process = [['Open Excel', 99345], \
['Open Browser', 99350], \
['Click Excel', 99351], \
['Click Browser', 99353],  \
['Search Item', 99355], \
['Click Item Page', 99358], \
['Copy Item Price', 99361], \
['Click Excel', 99363], \
['Paste Item Price', 99365], \
['Click Browser', 99367], \
['Search Item', 99369], \
['Click Item Page', 99371], \
['Copy Item Price', 99378], \
['Click Excel', 99382], \
['Paste Item Price', 99385], \
['Click Browser', 99388], \
['Search Item', 99392], \
['Click Item Page', 99393], \
['Copy Item Price', 99394], \
['Click Excel', 99398], \
['Paste Item Price', 99402], \
['Click Browser', 99408], \
['Search Item', 99412], \
['Click Item Page', 99415], \
['Copy Item Price', 99419], \
['Click Excel', 99421], \
['Paste Item Price', 99423], \
['Click Browser', 99427], \
['Search Item', 99433], \
['Click Item Page', 99435], \
['Copy Item Price', 99438], \
['Click Excel', 99540], \
['Paste Item Price', 99543], \
['Click File Dropdown', 99549], \
['Click Save Button', 99552], \
['Name File', 99558], \
['Click Save File', 99560] \
]


def create_process_dict(process_list):
	process_dict = {}
	for p in process_list:
		p_name = p[0]
		p_time = p[1]

		if p_name in process_dict:
			process_dict[p_name] = process_dict[p_name] + [p_time]
		else:
			process_dict[p_name] = [p_time]

	return(process_dict)


#process_dict = create_process_dict(ebay_process)



class Node:
    def __init__(self, subprocess, subprocess_time, print_space = ""):
        # this is the node itself
        self.process_time = subprocess_time
        # this is the edge
        self.process = subprocess
        self.child_processes = []
        self.spacing = print_space

    def add_child_process(self, child):
        self.child_processes.append(child)


    def print_children(self):
		for c in self.child_processes:
			print("{}{} has the direct child {}".format(self.spacing, self.process, c.process))
			n_children = len(c.child_processes)
			c.spacing = self.spacing.replace("\n","")+"\t"
			c.print_children()


class Tree:
	def __init__(self, full_process, print_space = ""):
		self.root = Node(full_process, -1)
		self.child_processes = []
		self.process = full_process
		self.process_time = -1
		self.spacing = print_space

	def add_child_process(self, node):
		self.child_processes.append(node)

	def print_children(self):
		for c in self.child_processes:
			print("{}{} has the direct child {}".format(self.spacing, self.process, c.process))
			n_children = len(c.child_processes)
			c.spacing = self.spacing.replace("\n","")+"\t"
			c.print_children()			#if isinstance(n, Node):
			#	n.print_children()
			#f isinstance(n, Tree):
			#	pass




# def create_suffix_tree(process_list, process_name):
# 	suffix_tree = Tree(process_name)
# 	#process_list.append(["$", -1])

# 	print("\nFULL PROCESS LIST IS {}\n".format(process_list))
# 	first_node = Node([process_list[-1][0]],\
# 		process_list[-1][1])

# 	suffix_tree.add_node(first_node)
# 	#return(suffix_tree)
# 	for p_idx in range(len(process_list)-2, 0, -1):
# 		print(p_idx)
# 		#curr_sub_process = [p[0] for p in process_list[p_idx:]]
# 		curr_sub_process = process_list[p_idx:]
# 		#process_list[p_idx:]
# 		curr_process = process_list[p_idx][0]
# 		curr_proccess_time = process_list[p_idx][1]
# 		print("Current process is {}".format(curr_process))
# 		for n_idx in range(0,len(suffix_tree.child_processes)):
# 			curr_node = suffix_tree.child_processes[n_idx]
# 			print("Looking at node {}".format(curr_node.process))
# 			if curr_process == curr_node.process[0]:
# 				print("{} already exists in our tree. Reformatting....".format(curr_process))
# 				suffix_tree.child_processes[n_idx] = create_suffix_tree(curr_sub_process, curr_node.process[0])
# 				break
# 			#else:
# 		suffix_tree.add_node(Node([p[0] for p in curr_sub_process]\
# 			, curr_proccess_time))
# 		print("{} does not yet exist in our tree. Will add".format(curr_process))
# 		#break

# 	return(suffix_tree)



def create_suffix_tree(process_list, process_name):
	suffix_tree = Tree(process_name)
	#process_list.append(["$", -1])

	print("\nFULL PROCESS LIST IS {}\n".format(process_list))
	first_node = Node([process_list[-1][0]],\
		process_list[-1][1])

	suffix_tree.add_child_process(first_node)
	#return(suffix_tree)

	for p_idx in range(len(process_list)-2, 0, -1):
		new_node = True
		print(p_idx)
		#curr_sub_process = [p[0] for p in process_list[p_idx:]]
		curr_sub_process = process_list[p_idx:]
		#process_list[p_idx:]
		curr_process = process_list[p_idx][0]
		curr_proccess_time = process_list[p_idx][1]
		print("Current process is {}".format(curr_process))
		for n_idx in range(0,len(suffix_tree.child_processes)):
			print("hereee")
			curr_node = suffix_tree.child_processes[n_idx]
			print("Looking at node {}".format(curr_node.process))
			if curr_process == curr_node.process[0]:
				print("{} already exists in our tree. Reformatting....".format(curr_process))
				print(curr_process)
				print('lsjdf')
				print(curr_node.process)
				suffix_tree.child_processes[n_idx].add_child_process(Node(curr_node.process[1:], curr_node.process_time))
				suffix_tree.child_processes[n_idx].add_child_process(Node([p[0] for p in curr_sub_process[1:]], curr_proccess_time))
				suffix_tree.child_processes[n_idx] = Node([curr_process], -1)
				new_node = False
				break
			#pass
			print("I'm on {}".format(curr_process))
		if new_node:
			suffix_tree.add_child_process(Node([p[0] for p in curr_sub_process]\
				, curr_proccess_time))
			print("{} does not yet exist in our tree. Will add".format(curr_process))
		#break

	return(suffix_tree)


#t = create_suffix_tree(ebay_process, "Ebay Process")

# Banana test 
banana = [['b', 0], ['a', 1], ['n',2], ['a', 3], ['n', 4], ['a', 5], ['$', 6]]
t = create_suffix_tree(banana, "banana")

f = Node("Open Excel", 12)
p = Node("Open Browser", 15)
l = Node("child of obrowser", 19)
q = Node("Search Item", 17)
s = Node("Find Item", 18)
r = Node("Open Broswer Again", 16)

f.add_child_process(p)
f.add_child_process(r)
p.add_child_process(q)
q.add_child_process(s)
p.add_child_process(l)

f.child_processes








        

