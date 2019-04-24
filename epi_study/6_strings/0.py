# Strings:

# How strings are stored in C:
# ref -> https://www.geeksforgeeks.org/storage-for-strings-in-c/

# Using character pointer strings can be stored in two ways:
# 1) Read only string in a shared segment ; Python probably uses this
    # char str = "GfG"
    # In the above line “GfG” is stored in a shared read-only location, but pointer 
    # str is stored in a read-write memory. You can change str to point something 
    # else but cannot change value at present str. So this kind of string should 
    # only be used when we don’t want to modify string at a later stage in the 
    # program.
    # Note - this is why python's strings are immutable
# 2) Dynamically allocated in heap segment - Ruby probably uses this making its
    # strings mutable

# How strings memory is handled by python:
# ref -> https://rushter.com/blog/python-strings-and-memory/

# "When working with empty strings or ASCII strings of one character Python uses
# string interning. Interned strings act as singletons, that is, if you have two 
# identical strings that are interned, there is only one copy of them in the 
# memory."


# Key takeaways:
# 1) Strings in python are immutable
    # s = s[1:] or s += "123" imply creating a new array of characters assigned back to s
    # concatinating using a for loop is O(n^2) but internal Python algorithm makes them O(n)
# 2) Brute-force O(n) space can usually be reduced to O(1)
# 3) Write values from the back of a mutable string because front manipulation is slower


# Basic Operations:
    # s = "Hello World"
    # t = "!"
    # -> Indexing        : s[6]   => "W"
    # -> Length          : len(s) => 11
    # -> Concatination   : s + t  => "Hello World!"
    # -> Slicing         : s[2:4] => "ll"
    #                    : And all of array's slicing techniques
    # -> Include         : "H" in s => True
    #                    : "H" in t => False
    # -> Multiplication  : 3 * "hello"  => 'hellohellohello'
    #                    : "hello" * 3  => 'hellohellohello'

# Methods:
    # -> str.format()
        # EPI:
            # "Name {name}, Rank {rank}".format(name="Archimedes", rank=3) => 'Name Archimedes, Rank 3'
        # Positional argument:
            # "Name {}".format("Archimedes") => 'Name Archimedes'
            # "Name {}, Rank {}".format("Archimedes", 3) => 'Name Archimedes, Rank 3'
            # "Name {}, Rank {}, Born {}".format("Archimedes", 3) => ERROR because number of placeholder doesn't match with arguments
        # Marked positional argument:
            # "Name {0}, Rank {1}".format("Archimedes", 3) => 'Name Archimedes, Rank 3'
            # "Name {1}, Rank {0}".format("Archimedes", 3) => 'Name 3, Rank Archimedes'
        # Mix of marked positional and keyword argument:
            # "Name {1}, Rank {rank}".format(rank=3, "Archimedes") => ERROR positional argument follows keyword argument
            # "Name {0}, Rank {1}, Born {year}".format("Archimedes", 3, year = "288 BC") => 'Name Archimedes, Rank 3, Born 288 BC'
        # Conversion:
            # "This site is {0:f}% securely {1}!!".format(100, "encrypted") => "This site is 100.000000% securely encrypted!!"
            # "My average of this {0} was {1:.2f}%".format("semester", 78.234876) => "My average of this semester was 78.23%"
            # "My average of this {0} was {1:.0f}%".format("semester", 78.234876) => "My average of this semester was 78%"
            # "The {0} of 100 is {1:b}".format("binary", 100) => "The binary of 100 is 1100100"
            # "The {0} of 100 is {1:o}".format("octal", 100) => "The octal of 100 is 144"
        # ref -> https://www.geeksforgeeks.org/python-format-function/

    # -> str.split(seperator, maxsplit=-1)
        # return a list of the words in the string, using sep as the delimiter string. 
            # -> If maxsplit is given, at most maxsplit splits are done 
            # (thus, the list will have at most maxsplit+1 elements). 
            # -> If maxsplit is not specified or -1, then there is no limit on the number of splits 
            # (all possible splits are made).
        # Examples:
            # s = "Hello World!"
            # s.split() => ['Hello', 'World!']
            # s.split("") => error
            # s.split(" ") => ['Hello', 'World!']
            # s.split("o") => ['Hell', ' W', 'rld!']
            # s.split("o", 1) => ['Hell', ' World!']
    
    # -> joiner.join(iterable)
        # Examples:
            # a = ["Hello", "World", "!"]
            # " ".join(a) => "Hello World !"
            # ",".join(("Gauss", "Prince of Mathematicians", "1777-1855")) => 'Gauss,Prince of Mathematicians,1777-1855'
        # why is it string.join(list) instead of list.join(string)?
            # -> https://stackoverflow.com/questions/493819/python-join-why-is-it-string-joinlist-instead-of-list-joinstring

    # -> str.lower()
        # "Hello".lower() => hello
    
    # -> str.upper()
        # "World".upper() => WORLD

    # -> str.strip([char]):
        # s = "  Hello  "
        # t = "--Hello--"
        # s.strip() => "Hello"
        # s.strip("-") => "Hello"
        # ref -> https://www.tutorialspoint.com/python3/string_strip.htm

    # -> str.startswith(prefix, start, end):
        # returns True if the string starts with the specified prefix, False otherwise
            # prefix : a string value or a tuple of prefixes to look for
            # start : optional; test string beginning at that position
            # end : optional; stop comparing string at that position
        # Examples:
            # s = "Hello"
            # s.startswith("H") => True
            # s.startswith("o") => False
            # s.startswith("l") => False
            # s.startswith("ll", 2) => True
            # s.startswith("ll", 3) => False
            # s.startswith("ll", 2, 3) => False
            # s.startswith("ll", 2, 4) => True
    
    # -> str.endswith(prefix, start, end):
        # returns True if the string ends with the specified suffix, False otherwise
            # suffix : a string value or a tuple of suffixes to look for
            # start : optional; test string beginning at that position
            # end : optional; stop comparing string at that position
        # Examples:
            # s = "Hello"
            # s.endswith("o") => True
            # s.endswith("H") => False
            # s.endswith("e") => False
            # s.endswith("ll", 2) => False
            # s.endswith("ll", 2, 4) => True
            # s.endswith("ll", 2, 3) => False
    
    # -> str.isupper()
        # "Hello".isupper() => False
        # "HELLO".isupper() => True
    
    # -> str.islower()
        # "Hello".islower() => False
        # "hello".islower() => True

# Palindrome:
def is_palindromic(s):
    for i in range(len(s) // 2):
        left_char = s[i]
        right_char = s[-(i+1)]
        if left_char != right_char:
            return False
    return True

s1 = "racecar"
s2 = "kayak"
s3 = "bootcamp"
# print(is_palindromic(s1)) # => True
# print(is_palindromic(s2)) # => True
# print(is_palindromic(s3)) # => False

def is_palindromic_epi(s):
    return all(s[i] == s[~i] for i in range(len(s)//2)) 
    # 0 : ~0 = -1 ; 0 : -(0+1) = -1
    # 1 : ~1 = -2 ; 1 : -(1+1) = -2 

s1_epi = "racecar"
s2_epi = "kayak"
s3_epi = "bootcamp"
# print(is_palindromic_epi(s1_epi)) # => True
# print(is_palindromic_epi(s2_epi)) # => True
# print(is_palindromic_epi(s3_epi)) # => False