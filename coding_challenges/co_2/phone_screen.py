# 1
# Given an array with duplicates elements (any data type) and more than one uniques. 
# How do you return the very first unique?

# From Python 3.6 onwards, the standard dict type maintains insertion order by default.
# ref -> https://stackoverflow.com/questions/1867861/how-to-keep-keys-values-in-same-order-as-declared

import collections
def get_first_unique_v1(elements): # O(n + n) = O(n)
    # uniques = collections.defaultdict(int)
    # for element in elements:
    #     uniques[element] += 1
    # print(uniques) # => defaultdict(<class 'int'>, {True: 4, False: 3, None: 2, '67': 1, 45: 1})
    uniques = collections.Counter(elements) # O(n)
    # print(uniques)  # => Counter({True: 4, False: 3, None: 2, '67': 1, 45: 1})
    # Hashing value of True and 1 or False and 0 are the same
    for key, value in uniques.items(): # O(n)
        if value == 1:
            return key

# print(get_first_unique_v1([True, False, None, 0, 1, None, "67", True, 0, 1, 45]))         # => "67"
# print(get_first_unique_v1([True, False, None, 0, 1, None, "67", True, 0, 1, 45, "67"]))   # => 45

def get_first_unique_v2(elements):
    uniques = collections.defaultdict(int)
    for element in elements:
        if element in uniques:
            uniques[element] = -1
        else:
            uniques[element] = 1
    for key, value in uniques.items():
        if value == 1:
            return key
        
# print(get_first_unique_v2([True, False, None, 0, 1, None, "67", True, 0, 1, 45]))         # => "67"
# print(get_first_unique_v2([True, False, None, 0, 1, None, "67", True, 0, 1, 45, "67"]))   # => 45


def get_first_unique_v3(arr):
    hash = {}
    for idx, ele in enumerate(arr):
        hash[ele] = idx
    for idx, ele in enumerate(arr):
        if hash[ele] == idx:
            return ele
        else:
            hash[ele] = idx

# print(get_first_unique_v3([True, False, None, 0, 1, None, "67", True, 0, 1, 45]))         # => "67"
# print(get_first_unique_v3([True, False, None, 0, 1, None, "67", True, 0, 1, 45, "67"]))   # => 45




# 2
# Given a singly linkedlist. 
# A node can have a next and a down - forking to a different linkedlist. 
# It is possible for the down branch to have more branches.
# How do you flattened them by prioritizing the down before next?
# 430 leet code - a little different because it deals with doubly linked
    # ref -> https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

def flatten_linked_list_recur(linked_list): # Time: O(n)
    next_ll = linked_list.next
    down_ll = linked_list.down
    if next_ll == None and down_ll == None:
        return linked_list

    if down_ll:
        prev_flattened_tail = flatten_linked_list_recur(down_ll)
        linked_list.next = down_ll
        prev_flattened_tail.next = next_ll

    if next_ll:
        return flatten_linked_list_recur(next_ll)
    else:
        return prev_flattened_tail


class Node:
    def __init__(self, val, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down

def print_ll(ll):
    if ll.next:
        print(ll.val, end = " ")
        print_ll(ll.next)
    else:
        print(ll.val)


twelve = Node(12)
eleven = Node(11, twelve)
six = Node(6)
five = Node(5, six)
four = Node(4, five)
ten = Node(10)
nine = Node(9, ten)
eight = Node(8, nine, eleven)
seven = Node(7, eight)
three = Node(3, four, seven)
two = Node(2, three)
one = Node(1, two)

# Input:
# 1---2---3---4---5---6--NULL
#         |
#         7---8---9---10--NULL
#             |
#             11--12--NULL

# Output:
# 1-2-3-7-8-11-12-9-10-4-5-6-NULL

# flatten_linked_list_recur(one) 
# print_ll(one) # => 1 2 3 7 8 11 12 9 10 4 5 6




# 3
# For a given string, there will be different types of parentheses: {}, (), and []. 
# Return true or false if the string is balanced properly: 
    # all opening parenthesis must be closed with its respective closing parenthesis and in order.
# 20 leet code - https://leetcode.com/problems/valid-parentheses/

def is_balance(paren_str): # Time: O(n) ; Space: O(n)
    stack = []
    parity = {"}" : "{", ")" : "(", "]" : "["}
    for char in paren_str:
        if char in parity and parity[char] == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0


# print(is_balance("()"))     # => True
# print(is_balance("()[]{}")) # => True
# print(is_balance("(]"))     # => False
# print(is_balance("([)]"))   # => False
# print(is_balance("{[]}"))   # => True




# 4
# For a given array of numbers, return the pair of numbers with the least absolute difference.

def least_abs_diff_pair_v1(nums): # Time: O(n^2)
    min_pair, global_min_diff = [], float("inf")
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if j > i:
                curr_min_diff = abs(num1 - num2)
                if curr_min_diff < global_min_diff:
                    global_min_diff = curr_min_diff
                    min_pair = [num1, num2]
    return min_pair


# print(least_abs_diff_pair_v1([1, 5, 3, 19, 18, 25]))                            # => [19, 18]
# print(least_abs_diff_pair_v1([30, 5, 20, 9]))                                   # => [5, 9]
# print(least_abs_diff_pair_v1([1, 19, -4, 31, 38, 25, 100]))                     # => [1, -4]
# print(least_abs_diff_pair_v1([3, -7, 0]))                                       # => [3, 0]
# print(least_abs_diff_pair_v1([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))   # => [-53, -54]
# print(least_abs_diff_pair_v1([1, -3, 71, 68, 17]))                              # => [71, 68]


# ref - > https://stackoverflow.com/questions/12232930/finding-out-the-minimum-difference-between-elements-in-an-array
def least_abs_diff_pair_v2(nums): # Time: O(nlogn) ; Space: O(n)
    sorted_nums = sorted(nums)
    global_min_val = sorted_nums[1] - sorted_nums[0]
    global_min_pair = [sorted_nums[0], sorted_nums[1]]

    for i in range(2, len(sorted_nums)):
        prev_num = sorted_nums[i-1]
        curr_num = sorted_nums[i]
        curr_min_val = abs(curr_num - prev_num)
        if curr_min_val < global_min_val:
            global_min_val = curr_min_val
            global_min_pair = [prev_num, curr_num]
    
    return global_min_pair

# print(least_abs_diff_pair_v2([1, 5, 3, 19, 18, 25]))                            # => [18, 19]
# print(least_abs_diff_pair_v2([30, 5, 20, 9]))                                   # => [5, 9]
# print(least_abs_diff_pair_v2([1, 19, -4, 31, 38, 25, 100]))                     # => [-4, 1]
# print(least_abs_diff_pair_v2([3, -7, 0]))                                       # => [0, 3]
# print(least_abs_diff_pair_v2([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))   # => [-54, -53]
# print(least_abs_diff_pair_v2([1, -3, 71, 68, 17]))                              # => [68, 71]


