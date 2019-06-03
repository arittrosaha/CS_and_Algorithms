# Compute Binary tree nodes in order of increasing depth

# Prompt:
# Given a binary tree, return an array consisting of the keys at the same level.

# Example:
# Input:
#               314
#          /            \
#         6              6
#       /   \          /   \
#     271    561      2    271
#    /   \     \       \     \
#   28    0     3       1    28
#              /       / \
#             17    401   257
#                    \
#                    641
# Output:
# [[314], [6,6], [271,561,2,271], [28,0,3,1,28], [17,401,257], [641]]

def binary_tree_depth_order(binary_tree_head):
    if not binary_tree_head:
        return []
    depth_levels = [[binary_tree_head]]
    curr_level = [binary_tree_head]
    while curr_level:
        children_level = []
        for parent in curr_level:
            if parent.left:
                children_level.append(parent.left)
            if parent.right:
                children_level.append(parent.right)
        depth_levels.append(children_level)
        curr_level = children_level
    return depth_levels


def binary_tree_depth_order_epi(tree):
    result = []
    if not tree:
        return result
    
    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child
            for curr in curr_depth_nodes for child in (curr.left, curr.right)
            if child
        ]
    return result


