def combinations(master_list): # Time: O(2^n) - two choices per element: either take it or leave it
    # if len(master_list) == 0:
    #     return [[]]
    if len(master_list) == 0: return [[]]

    el = master_list[0]
    rest = master_list[1:]

    without_el = combinations(rest)
    
    # with_el = []
    # for comb in without_el:
    #     new_comb = comb + [el]
    #     with_el.append(new_comb)

    with_el = [comb + [el] for comb in without_el]

    return with_el + without_el

# print(combinations(["a", "b", "c"]))




