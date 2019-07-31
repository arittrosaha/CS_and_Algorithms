# Find the nearest repeated entries in an array

# Prompt: A program which takes an array and finds the distance between a closest pair of equal entries

# Example:
# input - ["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]
# output - "no" because of the 2nd and 3rd occurrences of "no"

# Complexity analysis:
# Time: O(n), n - number of words
# Space: O(d), d - number of unique words

def find_nearest_repetition(paragraph): 
    lowest_diff_word, lowest_diff = None, float("inf")
    track_distance = {}
 
    for idx, word in enumerate(paragraph):
        if word in track_distance:
            curr_dist = idx - track_distance[word]
            if curr_dist < lowest_diff:
                lowest_diff, lowest_diff_word = curr_dist, word
        track_distance[word] = idx
    
    return lowest_diff_word


ex1 = ["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]
print(find_nearest_repetition(ex1))



def find_nearest_repetition_epi(paragraph):
    word_to_latest_index, nearest_repeated_distance = {}, float("inf")
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word_i = word_to_latest_index[word]
            nearest_repeated_distance = min(nearest_repeated_distance, i - latest_equal_word_i)
        word_to_latest_index[word] = i
    
    return nearest_repeated_distance if nearest_repeated_distance != float("inf") else -1