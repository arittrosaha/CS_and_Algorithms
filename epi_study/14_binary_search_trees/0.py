# Binary search tree (BST) properties:
# -> key is greater than or equal to left subtree
# -> key is less than or equal to right subtree

# A BST becomes balanced when the difference between a left subtree and a right subtree in height is just one

# Time - Insert, Delete, Search takes O(logn) or the height of the tree
# Space - O(n) like a hash table, in practice uses slightly more space

# bisect module give bst time complexity for list

class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
    
def search_bst(tree, key):
    if tree.data == key:
        return tree
    elif key < tree.data:
        return search_bst(tree.left, key)
    else:
        return search_bst(tree.right, key)

