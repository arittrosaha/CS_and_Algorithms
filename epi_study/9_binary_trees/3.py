import collections
import importlib
zero = importlib.import_module('0')
BinaryTree = zero.BinaryTree

# Compute the LCA when nodes have parent pointers

# Background:
# - The root is the common ancestor for any two nodes in a binary tree
# - The LCA (Lowest Common Ancestor) of any two nodes is the node furthest from the root that is an ancestor of both nodes.
# - A practical use case for LCA is rendering web pages specially when computing CSS for a particular DOM element

# Prompt: An algorithm for computing the LCA of two nodes in a binary tree in which nodes don't have a parent field

def lca(tree, node1, node2):
    if not tree:
        return
    # if the current tree matches with either of the new nodes, we start bubbling down True upto the possible LCA
    if node1.data == tree.data or node2.data == tree.data:
        return True
    
    left_result = lca(tree.left, node1, node2)
    right_result = lca(tree.right, node1, node2)

    # As soon as any node's both left side and right side returns true, as we are going down the stack calls, we know it is the LCA
    if left_result == True and right_result == True:
        return tree.data


    if type(left_result) is not type(None) and type(left_result) is not type(True): # other than None or boolean, anything else could be data
        return left_result # if left side passed just data, then the LCA is already found and that should keep getting sent down the stack
    elif type(right_result) is not type(None) and type(left_result) is not type(True):
        return right_result  # if right side passed just data, then the LCA is already found and that should keep getting sent down the stack
    elif type(left_result) is type(True):
        return left_result # if left side is just return true, it should keep getting sent down for the possible LCA
    elif type(right_result) is type(True):
        return right_result # if right side is just return true, it should keep getting sent down for the possible LCA
    

# Figure 9.2, page 124
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
K.right = O  # if exist, then it a balanced tree other wise false
L.left = M
L.right = N

# print(lca(A, F, G)) # => C

def lca_epi(tree, node0, node1): # logically, this solution is fundamentally like mine but done lot more properly
    # making tuples with attributes
    # num_target_nodes can be either 0 or 1 or 2. When it is 2, the LCA is found and saved in ancestor. Otherwise, ancestor is always None
    Status = collections.namedtuple("Status", ("num_target_nodes", "ancestor"))

    def lca_helper(tree, node0, node1):
        if not tree:
            Status(0, None)
        
        # if LCA is already found from the left side or the right side, we need to keep sending it down the stack
        left_result = lca_helper(tree.left, node0, node1)
        if left_result.ancestor: 
            return left_result
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.ancestor:
            return right_result

        num_target_nodes = (
            left_result.num_target_nodes + # if left side found 1 of the 2 nodes
            right_result.num_target_nodes + # if right side already found 1 of the 2 nodes
            (node0, node1).count(tree) # when ever one of the node matches, it gets counted
        )

        return Status(num_target_nodes, tree if num_target_nodes == 2 else None) 
        # at any stack, if num_target_nodes is already 2, it means that node is the LCA and thus sent down the stack as the ancestor
