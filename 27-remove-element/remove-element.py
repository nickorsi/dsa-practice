class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Use while loop and two pointers to swap all elements equaling val to the back
        left = 0
        right = len(nums) - 1
        val_counter = 0

        while left <= right:
            # print(left, right, nums)
            if nums[right] == val:
                # print("Here 1")
                val_counter += 1
                right -= 1 
                continue
            if nums[left] == val:
                nums[left], nums[right] = [nums[right], nums[left]]
                # print("Here 2", nums)
                right -= 1
                val_counter += 1
            
            left += 1

        return len(nums) - val_counter