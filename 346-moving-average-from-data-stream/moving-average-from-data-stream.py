from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.max_queue_size = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        
        if len(self.queue) > self.max_queue_size:
            self.queue.popleft()
        
        sum = 0
        
        for val in self.queue:
            sum += val
            
        return sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)