def num_combinations_for_final_score(final_score, individual_play_scores, memo={}):
    key = str(final_score) + str(individual_play_scores)
    if key in memo:
        return memo[key]
    if final_score == 0:
        return 1
    if len(individual_play_scores) == 0:
        return -1
    total_combinations, i, remaining = 0, 0, final_score
    while remaining > 0:
        remaining = final_score - individual_play_scores[0] * i
        curr_combination = num_combinations_for_final_score(remaining, individual_play_scores[1:], memo)
        if curr_combination > 0:
            total_combinations += curr_combination
        i += 1
    memo[key] = total_combinations
    return memo[key]    
    
# print(num_combinations_for_final_score(12, [2,3,7]))
# print(num_combinations_for_final_score(1000, [1, 3, 7]))

def num_combinations_for_final_score_tab(final_score, individual_play_scores):
    table = [1] + [0] * final_score # => [1,0,0,0,0,0,0,0,0,0,0,0,0]
    # starting index starts of with 1 because:
        # intuitively there is only 1 way to get to a score of 0 which is making no plays
        # algorithmically the first index needs to be 1 to start of the inner loop below
    # the index represents score
    # the value at those index represents the number of ways found so far to get to those scores
    
    for play in individual_play_scores:
        # first iteration finds ways to get to the scores that are possible to get using the first play
        # second iteration adds on to the previous findings and updates possible ways to get to possible scores using the first and second play
        # n iterations adds on to the previous n-1 iterations findings using n plays
        for score in range(len(table)):
            # if there is a value at table[score], then that means I can make a play to get to table[score + play] from table[score]
            if table[score] and ((score + play) < len(table)):
                # if there are x ways to get to table[score]
                # if there were already y ways to get to table[score + play]
                # then the new number of ways to get to table[score + play] from table[score] is x + y
                table[score + play] += table[score]
    # the last value is the number of ways to get to the total score after all plays are considered
    return table[-1]

print(num_combinations_for_final_score_tab(12, [2,3,7]))
# [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# [1, 0, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 3]
# [1, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]


# print(num_combinations_for_final_score_tab(1000, [1,3,7]))
