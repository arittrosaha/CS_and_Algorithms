import importlib
zero = importlib.import_module('0')
BinaryTree = zero.BinaryTree

# Test if a binary tree is height-balanced

# Background - height-balanced aka balanced binary tree. It does not have to be perfect or complete
# Prompt - A program that takes the root of a binary tree and checks whether the tree is height-balanced

def is_balanced_binary_tree(tree): # Time: O(n) ; Space: O(h)
    def height_diff(tree):
        if not tree:
            return -1 # -1 rather than 0 because if height is 0 at leaf, a stack beyond should be -1
        
        left_height = height_diff(tree.left)
        if left_height == False and left_height != 0:
            return False
        right_height = height_diff(tree.right)
        if right_height == False and right_height != 0:
            return False

        left_height += 1
        right_height += 1
        if abs(left_height - right_height) > 1:
            return False
        else:
            return max(left_height, right_height)


    if height_diff(tree) is not False:
        return True
    else:
        return False


# check page 124 for diagram
A = BinaryTree("A")
B = BinaryTree("B")
C = BinaryTree("C")
D = BinaryTree("D")
E = BinaryTree("E")
F = BinaryTree("F")
G = BinaryTree("G")
H = BinaryTree("H")
I = BinaryTree("I")
J = BinaryTree("J")
K = BinaryTree("K")
L = BinaryTree("L")
M = BinaryTree("M")
N = BinaryTree("N")
O = BinaryTree("O")

A.left = B
A.right = K
B.left = C
B.right = H
C.left = D
C.right = G
D.left = E
D.right = F
H.left = I
H.right = J
K.left = L
K.right = O # if exist, then it a balanced tree other wise false
L.left = M
L.right = N

print(is_balanced_binary_tree(A))

import collections
def is_balanced_binary_tree_EPI(tree): # logically, this solution is fundamentally like mine but done lot more properly 
    # making tuples with attributes
    BalancedStatusWithHeight = collections.namedtuple("BalancedStatusWithHeight", ("balanced", "height"))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)
        
        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)
        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)
    
    return check_balanced(tree).balanced

