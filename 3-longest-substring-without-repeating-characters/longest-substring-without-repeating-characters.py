class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
# Sliding Window with dict
#       Declare count = 0, left = 0, s_dict = dict(), max_length = 0
        count = left = max_length = 0
        s_dict: {str: int} = dict()
#       Loop through s
        for char in s:
#           Increment count
            count += 1
#           If char not in dict, add to it with value 1
            if char not in s_dict: s_dict[char] = 1
#           Else
            else:
#               Increment value of char
                s_dict[char] += 1
#               while value at char greater than 1
                while(s_dict[char] > 1):
#                   decrement value with char at left
                    s_dict[s[left]] -= 1
#                   decrement count
                    count -= 1
#                   increment left
                    left += 1
#           max_length is max value between max and count
            max_length = max(max_length, count)
#       Return max_length
        return max_length