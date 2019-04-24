# Remove and replace

# Prompt:
# 1) Replace each "a" by two "d"s
# 2) Delete each entry containing a "b"

# Input:
# -> an array of characters 
# -> an integer that denotes the number of entries of the array that the operation
#    is to be applied to

# Note: One can assume there is enough space in the array to hold the final result

# Example:
# ["a", "c", "d", "b", "b", "c", "a"]  , 7  => ["d", "d", "c", "d", "c", "d", "d"]
# ["a", "b", "a", "c", "o"]            , 4  => ["d", "d", "d", "d", "c"]
# ["a", "c", "a", "a", "v", "z", "p"]  , 4  => ["d", "d", "c", "d", "d", "d", "d"]

def replace_and_remove(size, s):
    # below is essentially a filter in place
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != "b":
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == "a":
            a_count += 1
    
    # below handles the replace from the back
    curr_idx = write_idx - 1 
    # 1 less because of the trailing incrementation of write_idx from the 
    # previous loop
    write_idx += a_count - 1 
    # -> the write_idx for this loop will start from the back which is why the 
    # a_count is added in anticipation of the extra indices needed for replacing 
    # elements 
    # -> 1 less again because of the trailing incrementation of write_idx 
    while curr_idx >= 0:
        if s[curr_idx] == "a":
            s[write_idx-1:write_idx+1] = "dd"
            write_idx -= 2
        else:
            s[write_idx] = s[curr_idx]
            write_idx -= 1
        curr_idx -= 1
    
    final_size = write_idx + 1
    return s[-final_size:]


print(replace_and_remove(7, ["a", "c", "d", "b", "b", "c", "a"]))
print(replace_and_remove(4, ["a", "b", "a", "c", "o"]))
print(replace_and_remove(4, ["a", "c", "a", "a", "v", "z", "p"]))

# losing infomation due to clash or over lap between curr_idx and write_idx 
# is not expected because of the assumption given to us from the prompt that is
# there will be always enough space in the given array to have the final array.
# Therefore, proper inputs to make sure that happens are expected with respect 
# to that assumption.