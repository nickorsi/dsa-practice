class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # Get rotations beyond length of nums, this is the realRotations
        #     # IE if array is length of 3 and make 3 rotations, array will not change
        # n = len(nums)
        # realRotations = k % n if k > n else k
        # # print(realRotations)
        # # Then iterate through realRotations, swapping from n - realRotations + i with i
        # for i in range(realRotations):
        #     nums[n - realRotations + i], nums[i] = [nums[i], nums[n - realRotations + i]]
        # # Then need to figure out how many unaccounted shifts remain, n - realRotations * 2
        # unaccountedRotations = n - realRotations * 2
        # # print(unaccountedRotations)
        # # print(nums)
        # # Create nested loop if unaccountedRotations > 0
        # if (unaccountedRotations > 0):
        #     # Outer loop iterates through unaccountedShifts
        #     for i in range(unaccountedRotations):
        #     # Inner loop iterates through realRotations
        #         for j in range(realRotations):
        #         # Swap n - realRotation - outerI - 1 with n - realRotation - outerI
        #             nums[n - i - realRotations + j - 1], nums[n - i - realRotations + j] = [nums[n - i - realRotations + j], nums[n - i - realRotations + j - 1]]
        #             # print(nums)
        # elif (unaccountedRotations < 0):
        #     for i in range(n - realRotations + unaccountedRotations):
        #         for j in range(abs(unaccountedRotations)):
        #             nums[n - i - abs(unaccountedRotations) + j - 1], nums[n - i - abs(unaccountedRotations) + j] = [nums[n - i - abs(unaccountedRotations) + j], nums[n - i - abs(unaccountedRotations) + j - 1]]
        #             # print(nums)
        # Above continues to fail, try new approach
        # Find rotation index
        rotation_index = k % len(nums)
        print(nums[:-rotation_index])
        print(nums[-rotation_index:])
        if rotation_index > 0:
            nums[:rotation_index], nums[rotation_index:] = [nums[-rotation_index:], nums[:-rotation_index]]