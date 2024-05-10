import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        distance_from_start = len(nums) - k
        heap = [*nums]
        min_heap = True
        iterator = None
        ans = None
# If distance from start 'k' is less than distance_from_end, do min_heap, else max_heap
        if k < distance_from_start:
            heap = [-num for num in heap]
            heapq.heapify(heap)
            min_heap = False
            iterator = k
        else: 
            heapq.heapify(heap)
            iterator = distance_from_start + 1
            
        for _ in range(iterator):
            ans = heapq.heappop(heap)
            
        return ans if min_heap else -ans