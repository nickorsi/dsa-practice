class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Can order the coins then use dp and start with the highest amount? 
        # What will be function and what will it return
            # Thinking it will be index for param, will return nothing
        # What is recurrent relation?
            # Hard to say
            # if 1 coin need to check how many times it divides into it, round down to the lowest whole number and subtract away from curr_amt
            # Need to memoize the coin amount and how many it could go into the amount
        # What is base case
            # Will return once i == 0? 
        # sorted_coins = sorted(coins)
        # curr_amt: int = amount
        # coin_count:int = 0
        # seen: Set[int, int] = set()

        # def dp(i: int) -> None:
        #     nonlocal curr_amt
        #     nonlocal coin_count

        #     coin:int = sorted_coins[i]

        #     if curr_amt < 0:
        #         return

        #     if i == 0:
        #         if coin not in seen:
        #             seen.add(coin)
        #             curr_coin_count = curr_amt // coin
        #             coin_count += curr_coin_count
        #             curr_amt -= curr_coin_count * coin
        #         return
            
        #     if coin not in seen:
        #         seen.add(coin)
        #         curr_coin_count = curr_amt // coin
        #         coin_count += curr_coin_count
        #         curr_amt -= curr_coin_count * coin

        #     return dp(i - 1)

        # dp(len(coins) - 1)

        # return coin_count if curr_amt == 0 else - 1

        # Above doesn't work fails test case 51 becuase there's no guarantee the largest coin will actually be used or that is should be used to the max...
        # Do dp using amount as input, return coin count
        # memo: Dict[int, int] = {}

        # def dp(amt: int) -> int:
        #     if amt == 0:
        #         return 0

        #     if amt < 0:
        #         return math.inf
            
        #     if amt in memo:
        #         return memo[amt]

        #     memo[amt] = math.inf

        #     for coin in coins:
                
        #         memo[amt] = min(memo[amt], 1 + dp(amt - coin))

        #     return memo[amt]

        # return dp(amount) if dp(amount) != math.inf else - 1

        # Bottom Up
        dp: List[int] = [math.inf] * (amount + 1)
        print(dp)
        dp[0] = 0

        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] = min(dp[amt], dp[amt - coin] + 1) 

        print(dp)
        return dp[amount] if dp[amount] != math.inf else - 1