import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
# Want to continuously combine the lowest value elements to get the min 'cost'
# Use a minheap to accomplish this efficiently
# While the minheap has length greater than 1, continue to pop off the two min values, combine, add to answer, then push into min heap
# Return ans
        ans = 0
        minheap = [*sticks]
        
        heapq.heapify(minheap)
        
        while len(minheap) > 1:
            min1 = heapq.heappop(minheap)
            min2 = heapq.heappop(minheap)
            
            new_stick = min1 + min2
            
            ans += new_stick
            
            heapq.heappush(minheap, new_stick)
            
        return ans
            
            