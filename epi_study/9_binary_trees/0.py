# Binary - at most 2 children
# full - 0 or all children at every node
# perfect - all leafs at same level
# complete - all levels expect the bottom are filled with max number of childrens
#            AND bottom level should be filled left to right
# Tree - no cycles
# Balanced - difference between height of left and right subtree is <= 1 AND left subtree is balanced
#                                                                        AND right subtree is balanced

# Relationship between n, number of nodes and h, height of binary tree:
# height from nodes:
# -> maximum possible height => h : n - 1
# 4        - h : 0
#  \
#   3      - h : 1
#    \
#     2    - h : 2
#      \
#       1  - h : 3
# -> minimum possible height => h : log2n
# at every depth, we have twice the amount of n

# -> nodes from height:
# -> minimum n : h + 1
# for the first edge, there are two nodes at each end. Then after for every edge, there is a node at the end
# -> maximum n : (2^(h+1)) - 1
# ref -> https://www.quora.com/What-is-the-maximum-number-of-nodes-in-a-binary-tree-Is-it-2-h-1-or-2-h+1-1/answer/Amit-Jaiswal-452


# ref -> https://www.geeksforgeeks.org/relationship-number-nodes-height-binary-tree/


# Full binary tree - the number of nonleaf nodes in a full binary tree is one less than the number of leaves.
# Perfect binary tree - contains exactly (2^(h+1)) - 1 nodes, of which 2^h are leaves
# Complete binary tree - has a height of log2n for n nodes


# Two types of skewed binary tree:
# left-skewed binary tree - no right child
# right-skewed binary tree - no left child


# Traversel
# Inorder - left -> root -> right
# Preorder - root -> left -> right
# Postorder - left -> right -> root

# Recursive implementation : O(n) time and O(h) space for the depth of call stack
# If each node has a parent attribute : O(n) and O(1) space iteratively

def tree_traversal(root, order):
    # comment back in the specific traversel line that is in need
    if root:
        if order == "pre":
            print("Preorder: %d" % root.data)
            
        tree_traversal(root.left, order)

        if order == "in":
            print("Inorder: %d" % root.data)
            
        tree_traversal(root.right, order)
        
        if order == "post":
            print("Postorder: %d" % root.data)


class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = self.parent = None
