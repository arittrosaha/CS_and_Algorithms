# Commute the k closest stars

# Background: Consider a coordinate system for the Milky Way, in which Earth is at (0,0,0). Model stars as points, 
# and assume distances are in light years. The Milky Way consists of 10^12 stars and their coordinates are stored in file

# Prompt: Compute k stars which are closest to Earth

# Complexity analysis:
    # Time O(n): If limited RAM was not an issue, we could process all the stars in an array at once
    # Time O(nlogk) : using a max heap with k elements, thus containing k stars with the kth largest stars
    # Space O(k) : the heap will only be at most k size
    
import math
class star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    # ref -> https://docs.python.org/2/library/operator.html#operator.__lt__
    # __lt__ is responsible for < operation
    def __lt__(self, rhs):
        return self.distance < rhs.distance
    
import heapq
def find_closest_k_stars(stars, k): # Time: O(nlogk) ; Space: O(k)
    max_heap = []

    for i, star in stars:
        if i <= k: 
            # under or equal to k stars, we push the star
            heapq.heappush(max_heap, (-star.distance, star))
        else: 
            # above k stars, we pop the minimum value or the maximum distance star inserted as a negative
            # then push the new star
            heapq.heappushpop(max_heap, (-star.distance, star))

    # heapq.nlargest returns a descending sorted list
    return [star[1] for star in heapq.nlargest(k, max_heap)]

    