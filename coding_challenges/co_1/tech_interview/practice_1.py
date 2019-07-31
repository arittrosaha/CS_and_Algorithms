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

# Your code goes here
import heapq
import collections


class LeaderBoard:
  __student = collections.namedtuple("student", ("score", "player_id"))

  def __init__(self):
    self.__student_dict = {}
    
  def add_score(self, player_id, score):
    if player_id in self.__student_dict:
      self.__student_dict[player_id] = (self.__student_dict[player_id] + score) / 2
    else:
      self.__student_dict[player_id] = score
    return self.__student_dict[player_id]
	
  def top(self, num_players):
    return self.__kth_students(num_players, "top") 

  def reset(self, player_id):
    if player_id in self.__student_dict:
      self.__student_dict[player_id] = 0
    else:
      raise NameError("Player does not exist!")
      
  def bottom(self, num_players):
    return self.__kth_students(num_players, "bottom")
    
  def __kth_students(self, num_players, order):
    multiplier = -1 if order == "bottom" else 1
    student_heap = []
    i = 0
    for player_id in self.__student_dict:
    #   if i < len(self.__student_dict):
        heapq.heappush(student_heap, self.__student(multiplier * self.__student_dict[player_id], player_id))
        i += 1
        if i > num_players:
            heapq.heappop(student_heap)
    return [student.player_id for student in heapq.nlargest(num_players, student_heap)]


# Create a new LeaderBoard Instance
leader_board = LeaderBoard()

# Add scores for players to the LeaderBoard
print(leader_board.add_score(1, 50)) # => 50.0
print(leader_board.add_score(2, 80)) # => 80.0
print(leader_board.add_score(2, 70)) # => 75.0
print(leader_board.add_score(2, 60)) # => 70.0
print(leader_board.add_score(3, 90)) # => 90.0
print(leader_board.add_score(3, 85)) # => 87.5

# Get top positions for the leaderboard
print(leader_board.top(3)) # => [3, 2, 1]
print(leader_board.top(2)) # => [3, 2]
print(leader_board.top(1)) # => [3]

# Reset a player 3's scores
print(leader_board.reset(3)) # => void

# Player 3 is now at the bottom of the leaderboard
print(leader_board.top(3)) # => [2, 1, 3]
