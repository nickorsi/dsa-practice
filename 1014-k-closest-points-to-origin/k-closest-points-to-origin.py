import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
# Want k closest points to origin (0,0) which is ((x1-x2)^2 + (y1-y2)^2)^1/2 which in this case is just (x2^2+y2^2)^1/2
# Want k smallest distances away, so need to remove largest values quickly, use max_heap
        max_heap = [(-math.sqrt(point[0] ** 2 + point[1] ** 2), point) for point in points]
        heapq.heapify(max_heap)
        
        while len(max_heap) > k:
            heapq.heappop(max_heap)
            
        return [point for distance, point in max_heap]