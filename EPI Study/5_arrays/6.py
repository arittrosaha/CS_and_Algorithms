# Buy and sell a stock once

# Prompt:
# An algorithm that determines the maximum profit that could have been made by
# buying and then selling a single share over a given day range, subject to the
# constraint that the buy and the sell have to take plae at the start of the day

# Example:
# [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# => maximum profit is 30 with one buy at 260 and one sell at 290

def buy_and_sell_stock_once(prices):
    max = float("-inf")
    min = float("inf")
    profit = 0
    for i in reversed(range(len(prices))):
        curr_profit = 0 # default value for every iteration
        if prices[i] > max: # if a larger max is found
            max = prices[i] 
            min = float("inf") # refresh the min in respect to the new max, in order to avoid making a curr_profit calculation with a previous min
        elif prices[i] < min: # if a lower min is found
            min = prices[i] 
            curr_profit = max - min # a new curr_profit can be calculated once a min is found
        if curr_profit > profit:  # Only if the curr_profit is larger than current global profit, update the profit
            profit = curr_profit       
    return profit 
    
prices_1 = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# print(buy_and_sell_stock_once(prices_1)) # => 30

def buy_and_sell_stock_once_epi(prices):
    curr_min, profit = float("inf"), 0.0
    for price in prices:
        curr_profit = price - curr_min
        profit = max(curr_profit, profit)
        curr_min = min(price, curr_min)
    return profit

prices_epi = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_stock_once_epi(prices_epi)) # => 30

# The maximum profit that can be made by selling on each specific day is the 
# difference of the current price and the minimum seen so far
# prices      => [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# curr_min    => [310, 310, 275, 275, 260, 260, 260, 230, 230, 230]
# curr_profit => [  0,   5,   0,  20,   0,  10,  30,  0,   25,  20]
# profit      =>                                  ^
