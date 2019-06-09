import importlib
zero = importlib.import_module('0')
BinaryTree = zero.BinaryTree
traversal = zero.traversal

# Reconstruct a binary tree from traversal data

# Prompt: 
# Given an inorder and preorder traversal sequence of a binary tree write a program to reconstruct the tree.
# Assume each node has a unique key

def binary_tree_from_preorder_inorder(inorder, preorder): 
	# Time: O(n^2) because for every stack for n, it does n work for filteration (worst case if the tree is skewed, left or right sub tree could be just n-1 per stack)
	# Space: O(hn) because at any point the highest call stack is h and for every stack we create an array of n (worst case if the tree is skewed, left or right sub tree could be just n-1 per stack)
	if not preorder and not inorder:
		return None

	root = preorder[0]
	root_idx_inorder = inorder.index(root)
	left_sub_inorder, right_sub_inorder = inorder[:root_idx_inorder], inorder[root_idx_inorder+1:]

	left_sub_preorder = [node for node in preorder if node in left_sub_inorder]
	right_sub_preorder = [node for node in preorder if node in right_sub_inorder]

	left_node = binary_tree_from_preorder_inorder(left_sub_inorder, left_sub_preorder)
	right_node = binary_tree_from_preorder_inorder(right_sub_inorder, right_sub_preorder)

	curr_node = BinaryTree(root)
	curr_node.left = left_node
	curr_node.right = right_node
	return curr_node

H = BinaryTree("H")
B = BinaryTree("B")
C = BinaryTree("C")
F = BinaryTree("F")
E = BinaryTree("E")
A = BinaryTree("A")
C = BinaryTree("C")
D = BinaryTree("D")
G = BinaryTree("G")
I = BinaryTree("I")

H.left = B
B.left = F
B.right = E
E.left = A
H.right = C
C.right = D
D.right = G
G.left = I

# inorder = traversal(H, "in")
# preorder = traversal(H, "pre")
# print(inorder)
# print(preorder)

# print("-----------------")

# tree = binary_tree_from_preorder_inorder(
# 	['F', 'B', 'A', 'E', 'H', 'C', 'D', 'I', 'G'], 
# 	['H', 'B', 'F', 'E', 'A', 'C', 'D', 'G', 'I']
# 	)
# print(traversal(tree, "in", []))
# print(traversal(tree, "pre", []))


# Time: O(n)
# Space: O(n + h) = O(n) ; n comes from the hash map and h comes from the stacks
def binary_tree_from_preorder_inorder_epi(preorder, inorder): 
	# data pointing to inorder index
	# first variable for an enumerate function stores the index position
	node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

	def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end, inorder_start, inorder_end):
		# as the range between start and end becomes equal, there is no valid exclusive range
		if preorder_end <= preorder_start or inorder_end <= inorder_start:
			return None
		
		root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
		left_subtree_size = root_inorder_idx - inorder_start 
		# if indexing started with 1, and the root's index was at 5, then the size is 4
		# when indexing starts at 0, and the root's index is at 4, the size is still 4

		return (
			BinaryTree( 
				preorder[preorder_start], # current node
				# all ranges bellow maintains max exclusivity
				binary_tree_from_preorder_inorder_helper( # left node
					# preorder_start moves by one because each node at first index is current stack's root
					(preorder_start + 1), (preorder_start + 1 + left_subtree_size), 
					# start always stays at zerothe new root index becomes the exclusive max for the next left subtree, while
					inorder_start, root_inorder_idx
				),
				binary_tree_from_preorder_inorder_helper( # right node
					# for right side, for both preorder and inorder end's at the length which is already one more than the last index value
					(preorder_start + 1 + left_subtree_size), preorder_end,
					(root_inorder_idx + 1), inorder_end
				)
			)
		)
	
	return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0, len(inorder))

