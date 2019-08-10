# Find the first key greater than a given value in a BST

# Prompt:
# A program that takes a BST head and a value, and returns the first key that greater than input value (or the first key that would appear next in an inorder traversal)

# Time: O(h), h is height of the tree
# Space: O(1)

# PDF - 201; Book - 215

def find_first_greater_than_k(tree, k):
    subtree, first_so_far = tree, None 
    while subtree:
        if subtree.data > k: 
            # only when a key is greater than k, we check for the left side to make sure there are not a less greater value than k
            # only when a key is greater than k, we assign the current key as the last value for first_so_far
            first_so_far, subtree = subtree, subtree.left
        else:
            # if key is not greater than k then it is either equal to or less than k. And for both we look for the right subtree to find the next greater value
            # here we do not assign because only greater values are assigned as possible answer
            subtree = subtree.right
    # when we reach towards a node that is a leaf or node with missing children, subtree.right or subtree.left becomes None and the while loop exists
    # this algorithm only goes down one path by taking advantage of the BST property
    return first_so_far