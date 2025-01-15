class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len_ans: int = m
        nums1_zero_location: int = m
        nums1_remaining_values: int = m
        nums2_pointer:int = 0

        for nums1_pointer in range(len(nums1)):
            # print("nums1= ", nums1)
            # print("nums1_pointer= ", nums1_pointer)
            # print("nums1_zero_location= ", nums1_zero_location)
            # print("nums1_remaining_values= ", nums1_remaining_values)
            # print("nums2_pointer= ", nums2_pointer)
            # print("\n")
            if len_ans == len(nums1):
                return
            # If all of the nums1 values are accounted for, then just fill in the nums2 values
            if nums1_remaining_values == 0:
                # print("Here")
                nums1[nums1_pointer] = nums2[nums2_pointer]
                nums2_pointer += 1
                len_ans += 1
            # If value in nums2 is less than value in nums1, bring a 0 back to current position
            elif nums2[nums2_pointer] < nums1[nums1_pointer]:
                tmp_pointer: int = nums1_zero_location
                while tmp_pointer > nums1_pointer:
                    swap_pointer: int = tmp_pointer - 1
                    # Swap with the nearest zero
                    nums1[swap_pointer], nums1[tmp_pointer] = [nums1[tmp_pointer], nums1[swap_pointer]]
                    tmp_pointer -= 1
                # Replace the value at nums1_pointer with value in nums2
                nums1[tmp_pointer] = nums2[nums2_pointer]
                # Increment nums2 pointer and nums1_zero_location
                nums1_zero_location += 1
                nums2_pointer += 1
                len_ans += 1
            else:
                nums1_remaining_values -= 1
            
