# Specification:

#     Create a class LeaderBoard whose interface includes the following methods:

#     Method Name: add_score

#      - Add a new score to the player's average. If a player doesn't exist in the
#       LeaderBoard, they will be automatically added.

#        Args:

#                 player_id(Integer): The player's ID.
#                 score(Integer): The score to record for the player

#         Returns:

#                 Double: The new average score for the given player

#     Method Name: top

#      - Get the top player_ids on the leaderboard ordered by their average scores
#       from highest to lowest

#        Args:

#                 num_players(Integer): The maximum number of player_ids to return

#         Returns:

#                 List < Integer >: a list of player_ids

#     Method Name: reset

#      - Removes any scoring information for a player, effectively
#       resetting them to 0

#        Args:

#                 player_id(Integer): The player's ID.

# Example Usage:

#     Create a new LeaderBoard Instance
#     leader_board = LeaderBoard()

#     Add scores for players to the LeaderBoard
#     leader_board.add_score(1, 50) # => 50.0
#     leader_board.add_score(2, 80) # => 80.0
#     leader_board.add_score(2, 70) # => 75.0
#     leader_board.add_score(2, 60) # => 70.0
#     leader_board.add_score(3, 90) # => 90.0
#     leader_board.add_score(3, 85) # => 87.5

#     Get top positions for the leaderboard
#     leader_board.top(3) # => [3, 2, 1]
#     leader_board.top(2) # => [3, 2]
#     leader_board.top(1) # => [3]

#     Reset a player 3's scores
#     leader_board.reset(3) # => void

#     Player 3 is now at the bottom of the leaderboard
#     leader_board.top(3) # => [2, 1, 3]

# Expected values
    # Player IDs will always be positive integers small enough to be
    # stored as a signed 32-bit integer Scores are integers ranging from 0-100


# We have provided stubbed out code and tests for you below. Please note that these tests are not exhaustive and do not cover all corner cases. We recommend extending the given tests to ensure your code is correct.

# Your code goes here. Feel free to make helper classes if needed

import heapq
import collections
import datetime

class LeaderBoard:
    _student = collections.namedtuple("student", ("score", "player_id"))
    _score = collections.namedtuple("score", ("value", "expiration", "rival_id"))

    def __init__(self):
        self._student_dict = {} 
    
    def add_score(self, player_id, score, expiration, rival_id): # O(1)
        if expiration <= self.todays_date() and rival_id is not player_id:
            if player_id in self._student_dict:
                self._student_dict[player_id].append(self._score(score, expiration, rival_id))
            else:
                self._student_dict[player_id] = [self._score(score, expiration, rival_id)]
            return self.avg_within_expiration(player_id)
        else:
            raise ValueError("Either the score expired or the rival_id is equal to player_id")
    
    def avg_within_expiration(self, player_id):
        self.cleanup_expired(player_id)
        sum = 0
        for score in self._student_dict[player_id]:
            sum += score.value
        return sum / len(self._student_dict[player_id])

    def cleanup_expired(self, player_id):
        print(self._student_dict)
        print(player_id)
        print(self._student_dict[player_id])
        scores = self._student_dict[player_id]
        current_date = self.todays_date()
        self._student_dict[player_id] = [score for score in scores if current_date <= score.expiration]
    
    def todays_date(self):
        return datetime.date.today()
    
    def rivals(self, player_id):
        self.cleanup_expired(player_id)
        return [score.rival_id for score in self._student_dict[player_id]]

    def reset(self, player_id):
        if player_id in self._student_dict:
            self._student_dict[player_id] = []
        else:
            raise NameError("Player does not exist!")
    
    def top(self, k):
        return self._kth_elements(k, "top")
    
    def bottom(self, k):
        return self._kth_elements(k, "bottom")
    
    def _kth_elements(self, k, order):
        student_heap = []
        i = 0
        for player_id in self._student_dict:
            # if i <= len(self._student_dict):
            if order == "top":
                heapq.heappush(student_heap, self._student(self._student_dict[player_id], player_id))
            else:
                heapq.heappush(student_heap, self._student(-self._student_dict[player_id], player_id))
            i += 1
            if i > k:
                heapq.heappop(student_heap)
        return [student.player_id for student in heapq.nlargest(k, student_heap)]

    # def top(self, k): # Time: O(nlogk) ; Space: O(k)
    #     student_heap = []
    #     i = 0
    #     for player_id in self._student_dict:
    #         if i <= len(self._student_dict):
    #             heapq.heappush(student_heap, self._student(self._student_dict[player_id], player_id))
    #             i += 1
    #         if i > k:
    #             heapq.heappop(student_heap)
    #     return [student.player_id for student in heapq.nlargest(k, student_heap)]
    
    # def bottom(self, k):
    #     student_heap = []
    #     i = 0
    #     for player_id in self._student_dict:
    #         if i <= len(self._student_dict):
    #             heapq.heappush(student_heap, self._student(-self._student_dict[player_id], player_id))
    #             i += 1
    #         if i > k:
    #             heapq.heappop(student_heap)
    #     return [student.player_id for student in heapq.nlargest(k, student_heap)]
    


    
leader_board = LeaderBoard()
print(leader_board.add_score(1, 50, datetime.date.today(), 4)) # 50.0
# print(leader_board.add_score(2, 80, datetime.date(2019, 8, 23), 5)) # 80.0
print(leader_board.add_score(2, 70, datetime.date(2020, 11, 12), 2)) # 75.0
print(leader_board.add_score(2, 60, datetime.date(2020, 12, 7), 3)) # 70.0
# print(leader_board.add_score(3, 90, datetime.date(2021, 3, 21))) # 90.0
# print(leader_board.add_score(3, 85, datetime.date(2019, 9, 4))) # 87.5
# print(leader_board.add_score(4, 50)) # 50
# print(leader_board.add_score(5, 60)) # 60
# print(leader_board.add_score(5, 70)) # 65.5

print("------------------")

print(leader_board.top(3)) # [3, 2, 1]
print(leader_board.top(1)) # [3]
print(leader_board.top(2)) # [3, 2]

print("------------------")

# print(leader_board._student_dict)
# print(leader_board.kth_elements(3, "bottom"))
# print(leader_board.kth_elements(1, "bottom"))
# print(leader_board.kth_elements(2, "bottom"))
# print(leader_board.kth_elements(6, "bottom"))



# print(leader_board.reset(3))
# print(leader_board.top(3))  # [2, 1, 3]





# def bottom will return bottom k
# write some test
