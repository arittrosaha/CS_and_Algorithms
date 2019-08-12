# Compute the LCA in a BST

# Prompt:
# A program that takes a BST head and two nodes
# returns the LCA of the two nodes

# LCA for just binary trees are done with postorder traversal which O(n) time complexity

# PDF - 218 ; Book - 217

# Time: O(h), where h is the height of the tree. This is because we descend one level with each iteration

def find_LCA(tree, s, b):
    # Input nodes are nonempty and the key at s is less than or equal to that at b
    while tree.data < s or tree.data > b: 
        # if current node is less than s than it is less than the range [s:b], so we need to go to the right
        while tree.data < s: # current node is less than both s and b
            tree = tree.right
        # if current node is greater than b than it is greater than the range [s:b], so we need to go to the left
        while tree.data > b: # current node is greater than both s and b
            tree = tree.left
    # the while loop at line 11 will end when the current node is in between [s:b] or s <= tree.data and tree.data <= b
    # In a binary search tree when every key is unique, the first node that goes between [s:b] is the LCA 
    # Because of the BST property, there is exactly one node that sits between [s:b]
    return tree

