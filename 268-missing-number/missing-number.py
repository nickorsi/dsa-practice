class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         Create a set of the nums
        numsSet = set(nums)
#         Loop from 0 to length of nums
        for i in range(len(nums)):
#         If i not in set, return i
            if i not in numsSet:
                return i
#         If out of for loop, return next number
        return len(nums)
