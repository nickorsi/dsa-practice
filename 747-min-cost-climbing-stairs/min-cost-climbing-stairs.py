class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n: int = len(cost)
        # Top Down DP
        # memo: dict[int, int] = {}
        # def dp(i: int) -> int:
        #     # Base case
        #     if i <= 1:
        #         return 0
            
        #     if i in memo: 
        #         return memo[i]
            
        #     memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])

        #     return memo[i]
        
        # return dp(n)

        # Bottom Up DP
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost [i - 1], dp[i - 2] + cost [i - 2])

        return dp[-1]