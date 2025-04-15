class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        return nums[math.ceil((len(nums) - 1) / 2)]