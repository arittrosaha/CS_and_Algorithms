# Because the file name starts with a number, normal from ... import ... is not 
# working. So the following are two ways to get around that:

# importlib (recommended)
# ref -> https://docs.python.org/3/library/importlib.html#importlib.import_module
import importlib
zero = importlib.import_module('0')
SinglyListNode = zero.SinglyListNode
print_list = zero.print_list

# __import__ (not recommended)
# ref -> https://docs.python.org/3/library/functions.html#__import__
# zero = __import__('0')
# SinglyListNode = zero.SinglyListNode
# print_list = zero.print_list

# Either of the above two ways creates that __pycache__ folder



# Merge two sorted lists

# Prompt:
# Merge two sorted linked list, with nodes carring integer values as data, in 
# ascending order

# Example:
# l1 -> 2 -> 5 -> 7
# l2 -> 3 -> 11
# rl -> 2 -> 3 -> 5 -> 7 -> 11

def merge_two_sorted_lists_epi(l1, l2):
    dummy_head = tail = SinglyListNode() # declarating two variables at the same time pointing to the same object node
    # dummy_head created to have a reference of the head to be returned later
    # tail will act as the frontier pointer
    while l1 and l2:
        # the smaller of the two will be added 
        if l1.data < l2.data: 
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next # tail gets updated in preparation of the next iteration
    tail.next = l1 or l2 # add whatever remained from either l1 or l2 at the end
    return dummy_head.next # next of the dummy head is the start of the actual list

# seven = SinglyListNode(7)
# five = SinglyListNode(5, seven)
# two = SinglyListNode(2, five)
# print_list(two)
# print("-----")

# eleven = SinglyListNode(11)
# three = SinglyListNode(3, eleven)
# print_list(three)
# print("-----")

# merged_ll = merge_two_sorted_lists_epi(two, three)

# print_list(merged_ll)


# def merge_two_sorted_lists (l1, l2):
#     head = l1
#     l1_curr_node = l1
#     l2_curr_node = l2
#     while l1_curr_node.next: # this will not work if l1 had a larger head than l2
#         l1_next_node = l1_curr_node.next
#         if l1_curr_node.data <= l2_curr_node.data <= l1_next_node.data:
#             l1_curr_node.next, l2_curr_node.next, l2_curr_node = l2_curr_node, l1_next_node, l2_curr_node.next
#         l1_curr_node = l1_next_node
#     if l1_curr_node.next != l2_curr_node:
#         l1_curr_node.next = l2_curr_node
#     return head