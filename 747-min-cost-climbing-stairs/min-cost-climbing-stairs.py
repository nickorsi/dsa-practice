class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Determine function inputs and outputs
            # Step input, min cost output
        # Determine recurrence relation
            # 1 step, 0 cost (can immediately be at top after 1 or 2 steps)
            # 2 steps, 0 cost (can immediately be at top after 2 steps)
            # 3 steps, cost is min of cost getting to 1 step plus cost AT 1 step or cost getting to 2 step plus cost AT 2 step
        # Base Case
            # if 2 steps or less (i <= 1) then return 0
        
        # memo: Dict[int, int] = {}

        # def dp(i: int) -> int: 
        #     if i <= 1:
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
        #     return memo[i]

        # return dp(len(cost))

        # Bottom up
        # n = len(cost)
        # dp = [0] * (n + 1)

        # for step in range(2, n + 1):
        #     dp[step] = min(dp[step - 1] + cost[step - 1], dp[step - 2] + cost[step - 2])

        # print(dp)
        # return dp[-1]

        # Bottom up only. caring about last 2 steps
        n = len(cost)
        dp = [0] * 2

        for step in range(2, n + 1):
            step1, step2 = dp

            dp[1] = min(step1 + cost[step - 2], step2 + cost[step - 1])
            dp[0] = step2
        
        print(dp)
        return dp[1]