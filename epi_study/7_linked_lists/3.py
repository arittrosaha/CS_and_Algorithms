import importlib
zero = importlib.import_module('0')
SinglyListNode = zero.SinglyListNode
print_list = zero.print_list

# Test for cyclicity

# Prompt:
# Input - head
# Output
    # -> null 
    # -> the node at the start of the cycle, if a cycle is present
# Constraints - the length of the list is unknown

def has_cycle(head): # Time: O(n) ; Space: O(n)
    dummy_head = SinglyListNode(None, head)
    visited = set()
    
    while head:
        if head in visited:
            return head
        visited.add(head)
        head = head.next
    return None


# Cycle example: 

four = SinglyListNode(4)
two = SinglyListNode(2, four)
seven = SinglyListNode(7, two)
five = SinglyListNode(5, seven)
four.next = five
three = SinglyListNode(3, four)
eleven_cycle = SinglyListNode(11, three)

# return_value_cycle = has_cycle(eleven_cycle)
# print(return_value_cycle.data)


# Non cycle example:

# two = SinglyListNode(2)
# seven = SinglyListNode(7, two)
# five = SinglyListNode(5, seven)
# four = SinglyListNode(4, five)
# three = SinglyListNode(3, four)
# eleven_non_cycle = SinglyListNode(11, three)

# return_value_non_cycle = has_cycle(eleven_non_cycle)
# print(return_value_non_cycle)

# Floyd's algorithm - check out the explanation from CTCI pg 223
def has_cycle_epi(head):
    slow, fast = head, head
    while slow and fast and slow.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if fast is slow:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
    return None

# return_value_cycle = has_cycle_epi(eleven_cycle)
# print(return_value_cycle.data)

# return_value_non_cycle = has_cycle_epi(eleven_non_cycle)
# print(return_value_non_cycle)