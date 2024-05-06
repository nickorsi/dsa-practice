import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
# Need to create the min sum of piles after k iterations of dividing the LARGEST pile by 2
# Must return the ceiling of the result ie 9/2 = 4.5 which must be returned as 5
# Use a MAX heap (python defaults to MIN)
# Iterate from 0 to k-1 to pull out the largest value in the heap, divide by 2, then return the result in the heap
# Return the sum of the heap
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        
        for _ in range(k):
            max_pile = heapq.heappop(heap)
            
            halved_pile = math.ceil(max_pile / 2 * -1) * -1
            
            heapq.heappush(heap, halved_pile)
            
        return sum(heap) * -1