class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # Use sweetness as the binary search
        # Can iterate through the chocolates and determine if you can reach to the required number of chunks
        # If not, then reduce the sweetness by moving right down
        # If you can, then increase the sweetness by moving left up
        # Looking for the MIN sweetness, so left most value
        number_of_people = k + 1
        left = min(sweetness)
        right = sum(sweetness) // number_of_people

        while left <= right:
            mid = (left + right) // 2

            curr_sweetness = 0
            people_with_chocolate = 0

            for s in sweetness:
                curr_sweetness += s

                if curr_sweetness >= mid:
                    people_with_chocolate += 1
                    curr_sweetness = 0
            
            if people_with_chocolate >= number_of_people:
                left = mid + 1

            else: 
                right = mid - 1
            
        return left - 1