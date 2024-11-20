class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  Naive: Iterate through each day and compare it to the next highest value in the future, keeping track of max profit
        # max_profit = -math.inf
        # for i in range(len(prices) - 1):
        #     max_profit = max(max_profit, max(prices[i+1:]) - prices[i])
        # return max_profit if max_profit > 0 else 0
        # Above Times out
        # price_day = [[prices[i], i] for i in range(len(prices))]
        # price_day.sort(key=lambda x: x[0])
        
        # max_profit = 0

        # for price, day in price_day:
        #     for i in range(len(prices) -1 , 0, -1):
        #         # print(i)
        #         future_price, future_day = price_day[i]
        #         if future_price == price and future_day:
        #             break
        #         if future_day > day:
        #             max_profit = max(max_profit, future_price - price)
        
        # return max_profit
        # Above will timeout as well
        # Need to keep track of min price and continually calculate the max_profit
        min_price = math.inf
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            # print(prices[i])
            # print(min_price)
            # print(max_profit)
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit 
