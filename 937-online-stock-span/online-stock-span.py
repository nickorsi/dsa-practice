class StockSpanner:

    def __init__(self):
        self.mono_stack = []
        self.price_to_streak_history = dict()
        self.day_count = 1

    def next(self, price: int) -> int:
        while self.mono_stack and price >= self.mono_stack[-1]:
            old_price = self.mono_stack.pop()
            self.day_count += self.price_to_streak_history[old_price]
        
        self.mono_stack.append(price)
        
        self.price_to_streak_history[price] = self.day_count
        self.day_count = 1
        
        return self.price_to_streak_history[price]
        
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)