# Find the k largest elements in a BST

# Prompt: 
# A Program that takes a BST head and an integer k 
# returns the k largest elementsin the BST in descending order

# The book describes this approach as reverse inorder traversal and it is not preorder traversal

# Time: O(h+k), h is the height. 
    # The highest amount of stack descent that can be is h + The highest amount of possible ascent is k
    # If k equals n, worst case is O(n)

def find_k_largest_in_bst(tree, k):
    def recursive_helper(tree):
        if tree: # safety against Nones
            # at each step we check against k before traversing further
            if len(k_largest_elements) < k:
                recursive_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
            if len(k_largest_elements) < k:
                recursive_helper(tree.left)
    
    k_largest_elements = []
    recursive_helper(tree)
    return k_largest_elements

