import importlib
zero = importlib.import_module('0')
SinglyListNode = zero.SinglyListNode
print_list = zero.print_list

# Remove the kth last element from a list

# Prompt: remove the kth last element from the list
    # Input:
    # - a singly linked list
    # - an integer k

    # Constraints:
    # - algorithm cannot use more than a few words of storage, regarless of 
    #   the list's length
    # - cannot assume that it is possible to record the length of the list

def remove_kth_last(list_head, k):
    dummy_head = SinglyListNode(None, list_head)
    first_pointer = dummy_head.next
    
    for _ in range(k):
        first_pointer = first_pointer.next
    
    second_pointer = dummy_head # k + 1 from last
    while first_pointer:
        second_pointer, first_pointer = second_pointer.next, first_pointer.next
    
    second_pointer.next = second_pointer.next.next
    return dummy_head.next


# dummy -> 11 -> 7 -> 9 -> 4 -> 1 -> 2
# two = SinglyListNode(2)
# one = SinglyListNode(1, two)
# four = SinglyListNode(4, one)
# nine = SinglyListNode(9, four)
# seven = SinglyListNode(7, nine)
# eleven = SinglyListNode(11, seven)

# print_list(eleven)
# result = remove_kth_last(eleven, 3)
# print_list(result)
