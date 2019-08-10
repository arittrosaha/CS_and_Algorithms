# Test if a binary tree satisfies the BST property

# Prompt: a program that takes a binary tree head and checks if the tree satisfies the BST property

# PDF - 200; Book - 214

def is_binary_tree_bst(tree, low_range=float("-inf"), high_range=float("inf")):
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return (is_binary_tree_bst(tree.left, low_range, tree.data) and
            is_binary_tree_bst(tree.right, tree.data, high_range)
            )

            
import collections
def is_binary_tree_bst_v2(tree):
    queue_node = collections.namedtuple("q_node", ("node", "lower", "upper"))

    bfs_queue = collections.deque(
        [queue_node(tree, float("-inf"), float("inf"))]
    )
    # ref -> https://docs.python.org/3/library/collections.html#collections.deque

    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node: # this is a check against Nones getting appended from leaves
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [
                queue_node(tree.left, front.lower, front.node.data),
                queue_node(tree.right, front.node.data, front.upper)
            ]
    
    return True
