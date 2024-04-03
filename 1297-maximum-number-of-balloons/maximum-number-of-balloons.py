import math
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
#   Input: String 'text'
#   Output: Integer representing # of times can spell 'balloon' using characters in text ONLY ONCE
#   Create char_count dict
        char_count: {int: int} = {}
#   Loop through text and populate char_count if char is either 'b', 'a', 'l', 'o', or 'n'
        for char in text:
            if char in ['b', 'a', 'l', 'o', 'n']:
                if char in char_count: char_count[char] += 1
                else: char_count[char] = 1
#   If length char_count != 5 return 0
        if not (len(char_count) == 5): return 0
#   Define count = inf
        count = float('inf')
#   Loop through char_count
        for char in char_count: 
#       count is min value associated with each char, with l and o needing to be floor value after / 2
            if char in ['l', 'o']:
                count = min(count, math.floor(char_count[char]/2))
            else: 
                count = min(count, char_count[char])
#   Return count
        return count