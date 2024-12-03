class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # # Use similar approach as to the chocolate question
        # # Use binary search going from the min value to the total value
        # left = min(nums)
        # right = sum(nums)
        # min_max_val = 0

        # while left <= right:
        #     # See if you can make enough splits with the current value
        #     mid = (left + right) // 2
        #     print("left= ", left)
        #     print("right= ", right)
        #     print("mid= ", mid)
        #     curr_cuts = 1
        #     curr_val = 0
        #     max_val_seen = -math.inf

        #     for i in range(len(nums)):
        #         num = nums[i]
        #         # curr_val += num
        #         print("num= ", num)
        #         print("curr_val= ", curr_val)
        #         print("curr_cuts= ", curr_cuts)
        #         print("max_val_seen= ", max_val_seen)
        #         if i == len(nums) - 1 and curr_val + num == mid: 
        #             max_val_seen = max(max_val_seen, curr_val + num)
        #         if curr_val + num > mid:
        #             curr_cuts += 1
        #             max_val_seen = max(max_val_seen, curr_val)
        #             curr_val = num
        #         else:
        #             curr_val += num

        #     # If less than or equal to the number of cuts, must decrase mid by moving right down
            
        #     print("curr_cuts= ", curr_cuts)
        #     print("\n")
        #     if curr_cuts <= k:
        #         if curr_cuts == k:
        #             min_max_val = max_val_seen
        #         right = mid - 1
        #     # If greater than number of cuts, must increase mid by moving left up
        #     else:
        #         left = mid + 1
        #     # if left > right and curr_cuts == k:
        #     #     min_max_val = max_val_seen
        # # Return left? 
        # return min_max_val
        # Above doesn't work

        # Looking at solution, have some minor tweaks
        left = max(nums)
        right = sum(nums)
        min_max_val = 0

        while left <= right:
            # See if you can make enough splits with the current value
            mid = (left + right) // 2
            # print("left= ", left)
            # print("right= ", right)
            # print("mid= ", mid)
            curr_cuts = 0
            curr_val = 0

            for num in nums:
                # print("num= ", num)
                # print("curr_val= ", curr_val)
                # print("curr_cuts= ", curr_cuts)
                if curr_val + num <= mid:
                    curr_val += num
                else:
                    curr_val = num
                    curr_cuts += 1

            # If less than or equal to the number of cuts, must decrase mid by moving right down
            
            # print("curr_cuts= ", curr_cuts)
            # print("\n")
            if curr_cuts + 1 <= k:
                min_max_val = mid
                right = mid - 1
            # If greater than number of cuts, must increase mid by moving left up
            else:
                left = mid + 1
        # Return min_max_val 
        return min_max_val