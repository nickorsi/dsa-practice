import sys
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
#         Define max as largest negative number
        max_num = -1
#         Define numsCount as a dictionary 
        nums_count: {int: int} = {}
#         Loop through nums and populate numsCount 
        for num in nums:
#             If new num, initialize with value 1
            if num not in nums_count: nums_count[num] = 1
#             Else increment value
            else: nums_count[num] += 1
#          Loop through nums_count and determine max_num with a count of 1
        for num in nums_count:
            if nums_count[num] == 1 and num > max_num:
                max_num = num
        
        return max_num