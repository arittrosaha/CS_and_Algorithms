# Reverse all the words in a sentence

# Prompt: reverse the words in a string s in place

# Example:
# "Alice likes Bob" => "Bob likes Alice"

def reverse_words(s):
    s = s.split(" ")

    for i in range((len(s)//2)+1):
        s[i], s[~i] = s[~i], s[i]
    
    return " ".join(s)

# print(reverse_words("Alice likes Bob")) # => Bob likes Alice
# print(reverse_words("Alice likes Bob, Clare")) # => Clare likes Bob, Alice



# EPI way:

# Step 1: reverse the string byte array
#       : "ram is costly" => "yltsoc si mar"
# Step 2: reverse each word
#       : "yltsoc si mar" => "costly is ram"

# IMPORTANT ASSUMPTION - s is a string encoded as bytearray or else the following
#                        method won't work because string is immutable in python.
def reverse_words_epi(s):
    # reversing the whole string byte array in place
    s.reverse() 

    # method to reverse each word
    def reverse_range(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start+1, finish-1
        
    start = 0
    while True:
        finish = s.find(b" ", start)
        # find will return the index position of the first " ", starting from 
        # the start index. If not found, it will return -1.
        # ref -> https://docs.python.org/3/library/stdtypes.html#str.find

        if finish < 0: 
            break
        # in the case of last word, find will not find any " " and therefore 
        # we break. This is why reversing the last is getting handled in line 40

        reverse_range(s, start, finish-1)
        start = finish + 1
    
    # reverses the last word
    reverse_range(s, start, len(s)-1)
    return s

