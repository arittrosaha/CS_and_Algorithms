# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

import collections

def connect(root):
    levels = []
    next_level = [root]
    while len(next_level):
        levels.append(next_level)
        new_next_level = []
        for node in next_level:
            if node.left is not None:
                new_next_level.append(node.left) 
            if node.right is not None:
                new_next_level.append(node.right)
        next_level = new_next_level

    for level in levels:
        for i in range(len(level)):
            curr_node = level[i]
            right_node = level[i+1] if i+1 < len(level) else None
            curr_node.next = right_node
    
    return levels

class Node:
    def __init__(self, val=None, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def print_levels(levels):
    for level in levels:
        for node in level:
            print(node.val)
            print(node.left.val) if node.left is not None else print(None)
            print(node.right.val) if node.right is not None else print(None)
            print(node.next.val) if node.next is not None else print(None)
            print("-----------")

seven = Node(7)
six = Node(6)
five = Node(5)
four = Node(4)
three = Node(3, six, seven)
two = Node(2, four, five)
one = Node(1, two, three)

# result = connect(one)
# print_levels(result)


    
