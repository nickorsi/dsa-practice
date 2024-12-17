class Solution:
    def rob(self, nums: List[int]) -> int:
        # Use dp (optimized recursion), need to find the max of options where one decision effects future decisions
        # Will start with top down approach
            # Need to determine state dimension of the dp problem:
                # Really only matters where we are in the house robbing, so 1-D 
            # Need to determine the recurrence relation: 
                # Max amount at i = 2 is either current num + max at 0 or max at 1
                # memo[i] = max(nums[i] + dp(i - 2), dp(i - 1))
            # Need to determine base cases:
                # Max amount at i = 0 is nums[0]
                # Max amount at i = 1 is either nums[0] or nums[2]
        n: int = len(nums) - 1
        memo: Dict[int, int] = {}
        # Option 1: With the way I implemented the solution (taking max value from memo) I had to pull out the base cases in the recursion 
        # and prepopulate memo with these:
        # memo[0] = nums[0]
        # if len(nums) > 1:
        #     memo[1] = max(nums[0], nums[1])

        # def dp(i: int) -> int:
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = max(nums[i] + dp(i - 2), dp(i - 1))

        #     return memo[i]
        
        # return max(memo.values())

        # Option 2: Recognize that the max amount robbed will be saved at the last house, regardless of how the houses are robbed 
        # def dp(i: int) -> int:
        #     if i == 0:
        #         return nums[i]
        #     if i == 1:
        #         return max(nums[0], nums[i])
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = max(nums[i] + dp(i - 2), dp(i - 1))

        #     return memo[i]
        
        # return dp(n)

        # Option 3: Use cache decorator to automatically memoize the function
        @cache
        def dp(i: int) -> int:
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[i])
            
            return max(nums[i] + dp(i - 2), dp(i - 1))
        
        return dp(n)