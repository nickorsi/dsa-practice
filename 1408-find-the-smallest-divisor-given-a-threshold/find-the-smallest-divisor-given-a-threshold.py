class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    # Check if the sum of all the nums divided by the denominator is the threshold
        def check(denom: int) -> bool:
            total = 0
            for num in nums:
                total += math.ceil(num / denom)
            return total <= threshold
    # Use binary search to determine the smallest denominator by setting it up to point to left pointer
        left = 1
        right = max(nums)

        while left <= right:
            denom = math.floor((right + left) / 2)
            # print(right, left, denom)
        # If less than or equal, denom is too high and need to lower it by moving right to denom - 1
            if check(denom):
                right = denom - 1
        # Else, denom is to low and need to raise it by moving left to denom + 1
            else:
                left = denom + 1
        # Return left

        return left