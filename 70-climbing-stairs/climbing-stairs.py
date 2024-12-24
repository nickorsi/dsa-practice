class Solution:
    def climbStairs(self, n: int) -> int:
        # Can use DP, asking for max number of ways to climb, current action afffects future actions
        # Figure out dp function, how many params and what it should return
            # Take in number of steps, return number of ways to reach top
        # Figure out recurrence relation
            # 1 step, 1 way (1)
            # 2 steps, 2 ways (1+1, 2)
            # 3 steps, 3 ways (1+1+1, 1+2, 2+1)
            # 4 steps, 5 ways (1+1+1+1, 2+1+1, 1+2+1, 1+1+2, 2+2)
            # Number of steps is the addition of the two previous step counts? step_options = dp(i-1) + dp(i-2)
        # Figure out base case
            # i == 1, return 1
            # i == 2, return 2
        
        # memo: Dict[int, int] = {}

        # def dp(i: int) -> int:
        #     if i == 1:
        #         return 1

        #     if i == 2:
        #         return 2
            
        #     if i in memo:
        #         return memo[i]

        #     memo[i] = dp(i - 1) + dp(i - 2)

        #     return memo[i]
        
        # return dp(n)

        # Bottom Up
        # dp = [1] * n

        # for step in range(1, n):
        #     if step == 1:
        #         dp[step] = 2
        #     else:
        #         dp[step] = dp[step - 1] + dp[step - 2]
        
        # return dp[n - 1]

        # Bottom Up, only track 2 steps

        dp = [1] * 2

        for step in range(1, n):
            if step == 1:
                dp[1] = 2
            else:
                step1, step2 = dp

                dp[0] = step2
                dp[1] = step1 + step2

        return dp[-1]

