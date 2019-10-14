# https://leetcode.com/problems/add-two-numbers-ii/

def add_two_numbers(ll_head_1, ll_head_2):
    def reverse_ll(ll):
        ll_length = 0
        prev_ll, curr_ll = None, ll
        while curr_ll is not None:
            ll_length += 1
            next_ll = curr_ll.next
            curr_ll.next = prev_ll
            prev_ll = curr_ll
            curr_ll = next_ll
        return [prev_ll, ll_length]
    
    reversed_ll_1, ll1_length = reverse_ll(ll_head_1)
    reversed_ll_2, ll2_length = reverse_ll(ll_head_2)

    empty_head1 = Node(None, reversed_ll_1)
    empty_head2 = Node(None, reversed_ll_2)

    carry = 0
    while reversed_ll_1 is not None or reversed_ll_2 is not None:
        
        operand_1 = reversed_ll_1.val if reversed_ll_1 is not None else 0
        operand_2 = reversed_ll_2.val if reversed_ll_2 is not None else 0

        if operand_1 + operand_2 + carry > 9:
            ones_digit = (operand_1 + operand_2 + carry) % 10
            if ll1_length >= ll2_length:
                reversed_ll_1.val = ones_digit
            else:
                reversed_ll_2.val = ones_digit
            carry = (operand_1 + operand_2 + carry) // 10
        else:
            ones_digit = (operand_1 + operand_2 + carry)
            carry = 0
            if ll1_length >= ll2_length:
                reversed_ll_1.val = ones_digit
            else:
                reversed_ll_2.val = ones_digit

        reversed_ll_1 = reversed_ll_1.next if reversed_ll_1 is not None else None
        reversed_ll_2 = reversed_ll_2.next if reversed_ll_2 is not None else None
    
    if ll1_length >= ll2_length:
        sum_ll = reverse_ll(empty_head1.next)[0]
    else:
        sum_ll = reverse_ll(empty_head2.next)[0]
    
    if carry > 0:
        return Node(carry, sum_ll)
    else:
        return sum_ll

def print_ll(ll_head):
    while ll_head:
        print(ll_head.val)
        ll_head = ll_head.next

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


three = Node(3)
four = Node(4, three)
two = Node(2, four)
seven = Node(7, two)

four = Node(4)
six = Node(6, four)
five = Node(5, six)


sum_head = add_two_numbers(seven, five)
print_ll(sum_head)

            
