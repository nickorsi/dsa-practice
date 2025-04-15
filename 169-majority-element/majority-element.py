class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # N log N time
        # nums.sort()
        # return nums[math.ceil((len(nums) - 1) / 2)]
        # Linear time
        # Iterate through tracking candidate and count
        ans = 0
        count = 0 
        for num in nums: 
            if count == 0:
                ans = num
                count += 1
            elif num == ans:
                count += 1
            else: 
                count -= 1
        
        return ans
