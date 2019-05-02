# Test Palindromicity

# PROMPT:
# Defination -> A string which when all the nonalphanumeric are removed, it reads
#               the same front to back ignoring cases.

# Input -> a string s
# Output -> true if s is palindromic, false otherwise

# Examples:
# -> "A man, a plan, a canal, Panama." => True
# -> "Able was I, ere I saw Elba!" => True
# -> "Ray a ray" => False


def is_palindrome(s):
    def alphabets_range(start, end):
        return [chr(char) for char in range(ord(start), ord(end)+1)]
        # ord() -> https://docs.python.org/3/library/functions.html#ord
        # chr() -> https://docs.python.org/3/library/functions.html#chr
        # https://stackoverflow.com/questions/7001144/range-over-character-in-python
        
    left_idx, right_idx = 0, len(s)-1
    alphabets = alphabets_range("a", "z")
    while left_idx <= right_idx:
        if s[left_idx].lower() not in alphabets:
            left_idx += 1
            continue
        if s[right_idx].lower() not in alphabets:
            right_idx -= 1
            continue
        if s[left_idx].lower() != s[right_idx].lower():
            return False
        left_idx += 1
        right_idx -= 1
    
    return True


# print(is_palindrome("A man, a plan, a canal, Panama.")) # => True
# print(is_palindrome("Able was I, ere I saw Elba!")) # => True
# print(is_palindrome("Ray a ray")) # => False

# Str.isalnum() - another way to check if character is a alphabet or not
# ref -> https://docs.python.org/3/library/stdtypes.html#str.isalnum



