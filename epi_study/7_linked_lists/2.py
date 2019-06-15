import importlib
zero = importlib.import_module('0')
SinglyListNode = zero.SinglyListNode
print_list = zero.print_list

# Reverse a single sublist

# Prompt:
# Input - a head for a singly linked list, two integers s and f
# Output - reverse the order of the nodes from the sth node to fth node, inclusive
# Assumption - the numbering begins with 1
# Constraint - do not allocate additional nodes

# Example:
# H -> 11 -> 3 -> 5 -> 7 -> 2
# s: 2
# f: 4
# H -> 11 -> 7 -> 5 -> 3 -> 2

def reverse_sublist_v1(head, s, f): # Time: O(n) ; Space: O(n)
    tail = head
    list_array = []
    while tail:
        list_array.append(tail)
        tail = tail.next
        
    for i in range(s-1, f//2 + 1):
        list_array[i], list_array[~i] = list_array[~i], list_array[i]
    # print([node.data for node in list_array])

    i = 1
    while i < len(list_array):
        list_array[i-1].next = list_array[i]
        i += 1

    return head


# two = SinglyListNode(2)
# seven = SinglyListNode(7, two)
# five = SinglyListNode(5, seven)
# # four = SinglyListNode(4, five)
# # three = SinglyListNode(3, four)
# three = SinglyListNode(3, five)
# eleven = SinglyListNode(11, three)
# print_list(eleven)
# print("-----")
# reversed_list = reverse_sublist_v1(eleven, 2, 4)
# print_list(reversed_list)


def reverse_sublist_v2(head, s, f): # Time: O(n) ; Space: O(1)
    remaining = None
    def reverse_recurr(head, range_i, prev=None):
        nonlocal remaining 
        if range_i == f:
            remaining = head.next
            head.next = prev
            return [head, remaining]

        result = reverse_recurr(head.next, range_i+1, head)
        # all of the following comparision won't happen until finish is reached because line 61 is before all the following
        if range_i > s:
            head.next = prev # simple reversing pointing until s is reached back again
        elif range_i == s:
            head.next = result[1] # the node at start points to the node after finish
            if prev != None:
                prev.next = result[0] # the previous node to the start points to the node at the finish
            elif prev == None:
                return result[0] # if the previous node is None indicating the start of the list, then just return the node at the finish as the new list head

        if range_i == 1: # when range_1 is 1 it indicates the first call stack
            return head # just the normal head in that scope is returned
        else:
            return result # else the array result carrying the two information from the finish edge of the list keep getting returned
            
    return reverse_recurr(head, 1)

# two = SinglyListNode(2)
# seven = SinglyListNode(7, two)
# five = SinglyListNode(5, seven)
# # four = SinglyListNode(4, five)
# # three = SinglyListNode(3, four)
# three = SinglyListNode(3, five)
# eleven = SinglyListNode(11, three)
# print_list(eleven)
# print("-----")
# reversed_list = reverse_sublist_v2(eleven, 2, 4)
# print_list(reversed_list)
