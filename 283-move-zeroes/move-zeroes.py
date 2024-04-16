class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use mult pointers
        # If only length 1, return
        if len(nums) == 1: return
        # Start with pointer at first position and second position
        first = 0
        second = 1
        # Use while loop with second being less than nums length
        while second < len(nums):
        # If first and second zero, advance only second
            if nums[first] == 0 and nums[second] == 0:
                second += 1
                continue
        # If first zero and second nonzero, swap and advance both
            if nums[first] == 0 and nums[second] != 0 :
                nums[first], nums[second] = [nums[second], nums[first]]
        # If first nonzerp and second zero, advance both
        # If first and second nonzero, advance both
            first += 1
            second += 1 