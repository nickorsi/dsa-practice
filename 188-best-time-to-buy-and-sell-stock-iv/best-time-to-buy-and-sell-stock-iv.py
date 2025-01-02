class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Have to find a max solution where current choices affect future outcomes, use DP
        # What are the inputs of the function and what will it return
            # Will return the max profit as int
            # What are the things that matter
                # What day is it, i
                # Are you holding stock, boolean
                # How many transactions are left, k
            # This is a 3D DP problem
        # What is/are the recurrence relation
            # You can buy today, so start with negative price from today, move onto the next day, and decrement the transactions
                # buy = - prices[i] + dp(i + 1, true, k - 1)
            # You can sell today, so add with positive price from today, move onto the next day, and decrement the transactions
                # sell = - prices[i] + dp(i + 1, false, k - 1)
            # You can skip today, so just return everything as is will day incremented
                # hold = dp(i + 1, h, k)
        # What are base cases
            # Outside of prices or no more transactions, return 0
        # memo: Dict[str, int] = {}

        # def dp(i: int, h: bool, k: int) -> int:
        #     if i == len(prices) or k == 0:
        #         return 0
            
        #     str_ihk: str = str(i) + str(h) + str(k)
        #     # print(str_ihk)
        #     if str_ihk in memo: 
        #         return memo[str_ihk]
            
        #     skip = dp(i + 1, h, k)
        #     # print("skip= ", skip)

        #     if h:
        #         sell = prices[i] + dp(i + 1, False, k - 1)
        #         # print("sell= ", sell)
        #         memo[str_ihk] = max(sell, skip)
        #     else:
        #         buy = -prices[i] + dp(i + 1, True, k)
        #         # print("buy= ", buy)
        #         memo[str_ihk] = max(buy, skip)


        #     return memo[str_ihk]
        
        # ans = dp(0, False, k)
        # # print(memo)

        # return ans
        
        @cache
        def dp(i, holding, remain):
            if i == len(prices) or remain == 0:
                return 0
            
            ans = dp(i + 1, holding, remain)
            if holding:
                ans = max(ans, prices[i] + dp(i + 1, False, remain - 1))
            else:
                ans = max(ans, -prices[i] + dp(i + 1, True, remain))
            
            return ans
        
        return dp(0, False, k)