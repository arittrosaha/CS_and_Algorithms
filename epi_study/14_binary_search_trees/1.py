# Test if a binary tree satisfies the BST property

# Prompt: a program that takes a binary tree head and checks if the tree satisfies the BST property

# Time: O(n)
# Space: O(h), h is the height of the tree for the call stacks

# PDF - 200; Book - 214

def is_binary_tree_bst_v1(tree, low_range=float("-inf"), high_range=float("inf")):
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return (is_binary_tree_bst_v1(tree.left, low_range, tree.data) and
            is_binary_tree_bst_v1(tree.right, tree.data, high_range)
            )

# Time: O(n) ; this approach reduces time complexity when the property is violated at a node whose depth is small or closer to root
# Space: O(n)

import collections
def is_binary_tree_bst_v2(tree):
    queue_node = collections.namedtuple("q_node", ("node", "lower", "upper"))

    bfs_queue = collections.deque(
        [queue_node(tree, float("-inf"), float("inf"))]
    )
    # Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction
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
