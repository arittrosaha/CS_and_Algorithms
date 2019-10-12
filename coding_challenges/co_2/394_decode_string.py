# https://leetcode.com/problems/decode-string/

def decode_string(str):
    result = ""
    i = 0
    while i < len(str):
        if str[i] == "[":
            min, max = detect_brackets(str, i)
            substr = decode_string(str[min+1:max-1]) # min and max exclusive or else infinite call stack because the inner string with enclosing brackets gets passed
            result = "".join([result, substr * int(str[i-1])])
            # result += (substr * int(str[i-1])) # join has an O(n+m) vs concatination O(mn)
                # https://stackoverflow.com/questions/39312099/why-is-join-faster-than-in-python
            i = max
        elif str[i].isalpha():
            result = "".join([result, str[i]])
            i += 1
        else:
            i += 1
    return result

def detect_brackets(str, i):
    stack = [1]
    j = i + 1 # shift to prevent double adding because of the already added 1 for the first "["
    while len(stack):
        if str[j] == "[":
            stack.append(1)
        elif str[j] == "]":
            stack.pop()
        j += 1
    return [i, j]


# print(decode_string("3[a]2[bc]"))      # => "aaabcbc"
# print(decode_string("3[a2[c]]"))       # => "accaccacc"
# print(decode_string("2[abc]3[cd]ef"))  # => "abcabccdcdcdef"
