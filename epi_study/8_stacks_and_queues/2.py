# Evaluate RPN expressions

# Prompt
# Reverse Polish Notation (RPN)

# Example
# Input: "3,4,+,2,x,1,+" 
# Output: (3 + 4) x 2 + 1 # => 15

# Input: "15,7,1,1,+,−,÷,3,×,2,1,1,+,+,−"
# Output: ((15 ÷ (7 − (1 + 1))) × 3) − (2 + (1 + 1)) => 5
# ref -> https://en.wikipedia.org/wiki/Reverse_Polish_notation


def evaluate_rpn(rpn_string): # Time: O(n) ; Space: O(n)
    stack = []
    operands = {
        "+": lambda y, x: x + y,
        "-": lambda y, x: x - y,
        "/": lambda y, x: x / y,
        "*": lambda y, x: x * y,
    }
    for char in rpn_string.split(","):
        if char in operands:
            stack.append(operands[char](stack.pop(), stack.pop()))
        else:
            stack.append(int(char))
    
    return stack[-1]


rpn_str_1 = "3,4,+,2,*,1,+"
rpn_str_2 = "15,7,1,1,+,-,/,3,*,2,1,1,+,+,-"
# print(evaluate_rpn(rpn_str_1)) # => 15
# print(evaluate_rpn(rpn_str_2)) # => 5
