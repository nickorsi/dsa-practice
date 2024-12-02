class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:   
        def check(mid: int) -> float:
            travel_time: float = 0
            
            # Need to round up trip for all legs EXCEPT the last leg
            for leg in range(len(dist)):
                if leg != len(dist) - 1:
                    travel_time += math.ceil(dist[leg] / mid)
                else: 
                    travel_time += dist[leg] / mid

            return travel_time
        
        # Use binary search to determine speed, which will be from 0 to the max distance
        left = 1
        # right = max(*dist)
        right = 10000000

        while left <= right:
        # On each mid, must check to see if the sum of all the distances / mid is...
            mid = math.floor((right + left) / 2)
            # Equal to the time, then return mid
            # print("left= ", left)
            # print("right= ", right)
            # print("mid= ", mid)
            # print("check(mid)= ", check(mid))
            # if check(mid) == hour:
            #     return mid
            # Less than time, then lower speed by lowering right by 1
            if check(mid) <= hour:
                right = mid - 1
            # Greater than time, then increase speed by raising left by 1
            else:
                left = mid + 1
        # Once outside of while loop, do a final check to make sure left will result in a time less than hour

        return left if check(left) <= hour else -1
