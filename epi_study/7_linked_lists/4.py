import importlib
zero = importlib.import_module('0')
SinglyListNode = zero.SinglyListNode
print_list = zero.print_list

# Test for overlapping lists - lists are cycle free

# Prompt:
# a Program that takes two cycle-free singly linked lists, and determines
# if there exists a node that is common to both lists

# Example:
# l1 -> 11 -> 7 -> 9 -> 2
#             ^
#             |
# l2 ->  8 -> 5

# note: l2 is actually larger than l1


def overlapping_no_cycle_lists(l1, l2):
    def list_len(head):
        len = 0
        while head:
            head = head.next
            len += 1
        return len
    
    l1_len, l2_len = list_len(l1), list_len(l2)
    longer, shorter = None, None
    if l1_len >= l2_len:
        longer = l1
        shorter = l2
    else:
        longer = l2
        shorter = l1
    
    for _ in range(abs(l1_len - l2_len)):
        longer = longer.next
    
    while longer is not shorter:
        longer = longer.next
        shorter = shorter.next
    
    return shorter


two = SinglyListNode(2)
nine = SinglyListNode(9, two)
seven = SinglyListNode(7, nine)
list_1 = SinglyListNode(11, seven)

five = SinglyListNode(5, seven)
list_2 = SinglyListNode(8, five)

# result = overlapping_no_cycle_lists(list_1, list_2)
# print(result.data)