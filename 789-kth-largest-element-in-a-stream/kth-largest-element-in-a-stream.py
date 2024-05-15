import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = [-num for num in nums]
        self.min_heap = []
        
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val) 
        ans = None
        if len(self.min_heap) < self.k:
            for _ in range(self.k):
                ans = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -ans)
            
            return -ans
        
        else:
            ans = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -ans)
            ans = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -ans)
            ans = heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, ans)
            
            return ans
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)