import importlib
zero = importlib.import_module('0')
BinaryTree = zero.BinaryTree

# Test if a binary tree is symmetric

# Background: A binary tree is symmetric if you can draw a vertical line through the root and then the left subtree is
#             mirror image of the right subtree 

# Prompt: A program that checks whether a binary tree is symmetric

# Examples:

#      314
#  /         \
# 6           6
#  \         /
#   2       2
#    \     /
#     3   3
# => True

#      314
#  /         \
# 6           6
#  \         /
#  561      2
#    \     /
#     3   1
# => False

#      314
#  /         \
# 6           6
#  \         /
#  561      561
#    \     
#     3   
# => False

import collections
def is_symmetric(tree): # Time: O(n) ; Space: O(n) because of the path array
    def traversal(head, path=[]):
        if not head:
            # for the case of right, if there is no head but a path was passed on from left, that path needs to be passed back for parent to be added later
            if path:
                return path
            else:
                return []

        left_added_path = traversal(head.left, path)
        right_added_path = traversal(head.right, left_added_path)
        return right_added_path + [head.data]
    
    left_path = traversal(tree.left, [])
    right_path = traversal(tree.right, [])
    print(left_path)
    print(right_path)
    return left_path == right_path

three_hundred_and_four_1 = BinaryTree(314)
six_1a = BinaryTree(6)
six_1b = BinaryTree(6)
two_1a = BinaryTree(2)
two_1b = BinaryTree(2)
three_1a = BinaryTree(3)
three_1b = BinaryTree(3)

three_hundred_and_four_1.left = six_1a
six_1a.right = two_1a
two_1a.right = three_1a
three_hundred_and_four_1.right = six_1b
six_1b.left = two_1b
two_1b.left = three_1b


three_hundred_and_four_2 = BinaryTree(314)
six_2a = BinaryTree(6)
six_2b = BinaryTree(6)
five_sixty_one_2 = BinaryTree(561)
two = BinaryTree(2)
three_2 = BinaryTree(3)
one = BinaryTree(1)

three_hundred_and_four_2.left = six_2a
six_2a.right = five_sixty_one_2
five_sixty_one_2.right = three_2
three_hundred_and_four_2.right = six_2b
six_2b.left = two
two.left = one


three_hundred_and_four_3 = BinaryTree(314)
six_3a = BinaryTree(6)
six_3b = BinaryTree(6)
five_sixty_one_3a = BinaryTree(561)
five_sixty_one_3b = BinaryTree(561)
three_3 = BinaryTree(3)

three_hundred_and_four_3.left = six_3a
six_3a.right = five_sixty_one_3a
five_sixty_one_3a.right = three_3
three_hundred_and_four_3.right = six_3b
six_3b.left = five_sixty_one_3b



print(is_symmetric(three_hundred_and_four_1))
print(is_symmetric(three_hundred_and_four_2))
print(is_symmetric(three_hundred_and_four_3))



def is_symmetric_epi(tree): # Time: O(n) ; Space: O(h)
    def check_symmetric(subtree_0, subtree_1): # traversing left and right subtree at the same time
        if not subtree_0 and not subtree_1: # if both left and right doesn't exist, it's True because its not violating symmetry
            return True
        elif subtree_0 and subtree_1: # if both exist
            return (subtree_0.data == subtree_1.data # if the opossing parallel nodes are equal
                    and check_symmetric(subtree_0.left, subtree_1.right) # one side's left should be matched with other side's right
                    and check_symmetric(subtree_0.right, subtree_1.left)) # one side's right should be matched with other side's left
        return False # if one of them does not exist, it's obviously not symmetric
    
    # if the tree does not exist, it returns true
    return not tree or check_symmetric(tree.left, tree.right)

