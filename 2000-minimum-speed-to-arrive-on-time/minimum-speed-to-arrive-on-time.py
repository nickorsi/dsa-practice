class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:   
        # Can check to make sure that rounded up hours is always larger than the dist size, otherwise impossible to travel in h time
        if len(dist) > math.ceil(hour): 
            return -1

        def check(speed: int) -> float:
            travel_time: float = 0
            
            # Need to round up trip for all legs EXCEPT the last leg
            for leg in range(len(dist)):
                if leg != len(dist) - 1:
                    travel_time += math.ceil(dist[leg] / speed)
                else: 
                    travel_time += dist[leg] / speed

            return travel_time
        
        # Use binary search to determine speed, which will be from 0 to the max speed
        # Craft binary search such that it finds the left most value
        left = 1
        # right = max(*dist) # Did not read statement in entirety, max speed is stated as 10^7, so should start by checking there
        right = 10000000

        while left <= right:
        # On each speed, must check to see if the sum of all the distances / mid is...
            speed = math.floor((right + left) / 2)
            # print("left= ", left)
            # print("right= ", right)
            # print("speed= ", speed)
            # print("check(speed)= ", check(speed))
            # Less than or equal to the time, then lower speed by setting right to speed - 1
            if check(speed) <= hour:
                right = speed - 1
            # Greater than time, then increase speed by setting left to speed + 1
            else:
                left = speed + 1
        # Once outside of while loop, do a final check to make sure left will result in a time less than hour

        return left if check(left) <= hour else -1
