# Test for Palindromic Permutations

# Prompt:
# a program to test whether the letters forming a string can be permuted to form a palindrome 

# Example: 
# Input - "edified"
# Output - true ; "deified"

import collections

def can_form_palindrome(s):
    # a string can be permuted to form a palindrome if and only if the number of chars whose frequencies is odd is at most 1.
    # at least one of the chars frequency will be odd when the string's length is odd
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1

print(can_form_palindrome("edified")) # => True