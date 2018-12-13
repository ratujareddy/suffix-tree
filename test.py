# Testing our suffix tree

from Tree import *
from utils import *
from build_suffix_tree import *


ltest = [('X', 2), ('B', 3), ('C', 4), ('A', 5), \
	('B', 6),('B', 7), ('C', 8), \
	('A', 9), ('B', 10), ('X', 11), ('$', 12)]

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
['Click Save File', 99560], \
['$', 99561]
]

#suffix_tree = build_tree(ltest, "this is my tree")
suffix_tree = build_tree(ebay_process, "Ebay Tree")

def find_longest_process(suffix_tree, node_dict= {}):
	#node_dict = {}
	for e in suffix_tree.child_edges:
		if e.child_type == "Node":
			print("found a node")
			node_dict[e.child] = e.child.depth
			find_longest_process(e.child, node_dict)

	lonest_substr = max(node_dict, key = node_dict.get).val
	return(lonest_substr)

longest_substr = find_longest_process(suffix_tree)



