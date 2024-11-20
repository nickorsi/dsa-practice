class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Use 2 binary searches, one to find the left most value and one to find the right most value
        ans = [-1,-1]

        if len(nums) == 1:
            if nums[0] == target: return [0,0]
            else: return ans

        left = 0
        right = len(nums) - 1

        while left < right:
            # print("Here", left, right)
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else: 
                left = mid + 1

        if left < len(nums) and left >= 0 and nums[left] == target: 
            ans[0] = left

        left2 = 0 
        right2 = len(nums) - 1

        while left2 < right2: 
            print("Here2", left2, right2)
            mid = (left2 + right2) // 2

            if nums[mid] > target: 
                right2 = mid
            else:
                left2 = mid + 1
        print(left2)
        if left2 < len(nums) and left2 >=0 and nums[left2] == target:
            ans[1] = left2
        elif left2 - 1 < len(nums) and left2 - 1 >= 0 and nums[left2 - 1] == target: 
            ans[1] = left2 - 1

        return ans