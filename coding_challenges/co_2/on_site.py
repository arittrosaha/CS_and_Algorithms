# 1a
# Design a function that shuffles a deck of cards(represented as "S6" for 6 of Spades) and guarantees a uniform distribution. 
# How would you do it in-place? 
# How would you change your function to account a deck with 100 million cards? 
# How would you change your function to let multiple computers shuffle the same deck?

# Python random background:
    # random() 
        # https://docs.python.org/3/library/random.html#module-random
        # this is the base random function which generates a random float uniformly in the semi-open range [0.0, 1.0). 
        # Python uses the Mersenne Twister as the core generator. 
        # The underlying implementation in C is both fast and threadsafe. 
        # The Mersenne Twister is one of the most extensively tested random number generators in existence.
            # A sequence of length 2080 is the largest that can fit within the period of the Mersenne Twister random number generator.
            # However, being completely deterministic, it is not suitable for all purposes, and is completely unsuitable for cryptographic purposes.
            # Has a long has a period of 2**19937-1
                # what is a period?
                    # https://security.stackexchange.com/questions/54530/what-does-the-period-of-a-random-number-generator-measure
                    # https://softwareengineering.stackexchange.com/questions/273105/why-is-the-period-of-a-pseudorandom-number-generator-important

    # https://docs.python.org/3/library/random.html#functions-for-integers
        # randrange(start, stop [, step]) - stop exclusive
            # Changed in version 3.2: randrange() is more sophisticated about producing equally distributed values.
            # Formerly it used a style like int(random()*n) which could produce slightly uneven distributions.
        # randint(start, stop) - stop inclusive
            # Alias for randrange(a, b+1).


import random
def shuffle(cards): # Time: O(n) ; Space: O(1)
    i = 0
    while i < len(cards):
        rand_card_idx = random.randrange(i, len(cards))
        # randrange which uses random.random base function which uses Mersenne Twister has a O(1) time complexity
            # https://stackoverflow.com/questions/25651532/what-is-the-time-complexity-of-the-mersenne-twister
        cards[i], cards[rand_card_idx] = cards[rand_card_idx], cards[i]
        i += 1

def deck_52(): # Time: O(1) because a fix of 52 cards
    cards = []
    non_numbered = ["J", "Q", "K", "A"]
    suits = ["C", "D", "H", "S"]
    for suit in suits:
        for nn in non_numbered:
            cards.append("".join([suit, nn]))
        for num in range(2, 11):
            cards.append("".join([suit, str(num)]))
    return cards

# deck = deck_52()
# print(deck)
# shuffle(deck)
# print(deck)



# 1b
# Design a stock tracker that has two functions: `stock_sold(stock, volume)` and `top_3_stocks_in_volume()`. 
# How would you return a variable number of top stocks(`top_n_stocks_in_volume(n)`)? 
# How would you change the function if the `stock_sold` function runs 1000 times every time `top_n_stocks` running once?

import collections
import heapq
class StockTracker:
    def __init__(self):
        self.stocks = collections.defaultdict(int)
    
    def stock_sold(self, ticker, volume):
        self.stocks[ticker] += volume
    
    def top_n_stocks(self, n):
        max_heap = []
        i = 0
        for ticker, volume in self.stocks.items():
            heapq.heappush(max_heap, (-volume, ticker))
            i += 1
            if i > n:
                heapq.heappop()
        return [stock[1] for stock in max_heap]
    



# 2a 
# Given a N x N bidirectional graph represented as numbers, a starting node, and a number of jumps you can perform from the starting node, how do you count the number of paths? 
    # What's the time complexity? 
# If two nodes have the same value so they're non-unique, how would you change the function? 
    # What's the time complexity? 
# Given a 3 x 3 graph and a path, how would you determine what node is in the middle? 
    # What's the time complexity?


def number_of_paths_v1(board, start_node, number_of_jumps):
    def dfs(start_node, jumps_left):
        if start_node is None:
            return
        if jumps_left is 0:
            return 1
        count = 0
        for direction in start_node.directions:
            stack_return = dfs(direction, jumps_left-1)
            if stack_return is not None:
                count += stack_return
        return count
    
    return dfs(start_node, number_of_jumps)
            



# 2b
# Given a subway system where people swipe in and swipe out, design a system that keeps track of the average time between two train stations. 
# How would you handle a huge amount of people going in and out of stations?
import datetime
import random
class Subway:
    def __init__(self):
        self.current_riders = {}
        self.average = 0
    
    def swipe_in(self, rider_id=None):
        while rider_id is None:
            get_id = self._id_generator()
            if get_id not in self.current_riders:
                rider_id = get_id
        self.current_riders[rider_id] = self._current_time()
        return rider_id
    
    def swipe_out(self, rider_id):
        time_in = self.current_riders[rider_id]
        time_out = self._current_time()
        self.average = (self.average + (time_out - time_in)) / 2
        del self.current_riders[rider_id]
    
    def _current_time(self):
        return datetime.datetime.now()

    def _id_generator(self):
        return random.randrange(len(self.current_riders)+1)


# 3a
# Design a raffle that could insert, remove, and pick a winner all in constant time.

class Raffle:
    def __init__(self):
        self.participants = {}
        self.freed_ids = []
    
    def insert(self, name):
        if len(self.freed_ids) > 0:
            get_id = self.freed_ids.pop()
        else:
            get_id = self._id_generator()
        self.participants[get_id] = name
        self.participants[name] = get_id
        return get_id
    
    def remove(self, input):
        if input in self.participants:
            if type(input) is int or input is 0:
                the_name = self.participants[input]
                the_id = self.participants[the_name]
            elif type(input) is str:
                the_id = self.participants[input]
                the_name = self.participants[the_id]
            del self.participants[the_id]
            del self.participants[the_name]

    def pick_winner(self):
        winner_id = None
        number_of_participants = len(self.participants)
        while winner_id is None:
            if number_of_participants > 0:
                winner_id = random.randrange((len(number_of_participants)//2))
            elif number_of_participants is 0:
                winner_id = 0
            if winner_id in self.participants:
                the_name = self.participants[winner_id]
                del self.participants[winner_id]
                del self.participants[the_name]
                return the_name
        
    def _id_generator(self):
        return random.randrange(len(self.participants))
    

# 3b
# It was dial pad permutations so the phone number ‘23’ represents [ad, ae, af, bd, be, bf, cd, ce, cf]

def dial_pad_permutations(str_num):
    dial_pad = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    def permutations(str_num):
        if len(str_num) is 0:
            return []
        total_perms = []
        for char in dial_pad[str_num[0]]:
            prev_perms = permutations(str_num[1:])
            if len(prev_perms) is 0:
                total_perms.append(char)
            else:
                total_perms.extend(["".join([prev_perm, char]) for prev_perm in prev_perms])
        return total_perms
    return permutations(str_num)

print(dial_pad_permutations("23"))
