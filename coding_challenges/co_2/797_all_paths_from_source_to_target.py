# https://leetcode.com/problems/all-paths-from-source-to-target/
# https://www.techopedia.com/definition/5739/directed-acyclic-graph-dag

def all_paths_from_source_to_target(node): # Time: O(n) ; Space: O(n)
    def helper(node):
        if len(node.children) is 0:
            return [[node.value]]
        next_nodes = node.children
        all_paths = []
        for next_node in next_nodes:
            prev_paths = helper(next_node)
            for path in prev_paths: path.append(node.value)
            all_paths.extend(prev_paths)
        return all_paths
    return [path[::-1] for path in helper(node)]

class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children


three = Node(3, [])
two = Node(2, [three])
one = Node(1, [three])
zero = Node(0, [one, two])

print(all_paths_from_source_to_target(zero))
