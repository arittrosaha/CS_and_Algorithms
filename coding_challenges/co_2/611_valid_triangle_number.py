# https://leetcode.com/problems/valid-triangle-number/

def valid_triangle_number(sides): # Time: 2^n ; Space: n < O() < n!
    valid_combinations = 0

    def get_combinations(sides):
        if len(sides) is 0:
            return [[]]

        without_el = get_combinations(sides[1:])
        with_el = []
        for comb in without_el:
            new_comb = comb + [sides[0]]
            # new_comb = comb.append(sides[0]) # error because append returns None
            with_el.append(new_comb)

        return with_el + without_el
    
    combinations = get_combinations(sides)
    for comb in combinations:
        if len(comb) == 3:
            side1, side2, side3 = sorted(comb)
            if side3 < side1 + side2 and side2 < side1 + side3 and side1 < side2 + side3:
                valid_combinations += 1
    
    return valid_combinations


# print(valid_triangle_number([2, 2, 3, 4]))


# Better solution available with good description by the link below:
# https://leetcode.com/problems/valid-triangle-number/solution/
