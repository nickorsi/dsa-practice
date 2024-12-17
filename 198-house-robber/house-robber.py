class Solution:
    def rob(self, nums: List[int]) -> int:
        # Max amount at i = 0 is nums[0]
        # Max amount at i = 1 is either nums[0] or nums[2]
        # Max amount at i = 2 is either current num + max at 0 or max at 1
        # memo[i] = max(nums[i] + dp(i - 2), dp(i - 1))
        n: int = len(nums) - 1
        memo: Dict[int, int] = {}
        memo[0] = nums[0]
        if len(nums) > 1:
            memo[1] = max(nums[0], nums[1])

        def dp(i: int) -> int:
            # if i == 0:
            #     return nums[i]
            # if i == 1:
            #     return max(nums[i], nums[0])
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + dp(i - 2), dp(i - 1))

            return memo[i]
        
        dp(n)

        return max(memo.values())