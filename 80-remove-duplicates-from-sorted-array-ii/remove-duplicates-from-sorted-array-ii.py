class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    # Keep track of seen nums in a counter
    # Use two pointer method and while loop?   
        # If at 2 or more, swap to the back and increment dup_count
            # How to swap? Does the swap have to occur with every num unitl at the back? Seem like brute force
        num_count: Dict[int, int] = {}

        left = 0
        right = len(nums) - 1
        dup_count = 0

        while left <= right:
            # print("dup_count= ", dup_count)
            # print("num_count= ", num_count)
            # print("left= ", left)
            # print("right= ", right)
            # print("nums= ", nums)
            # print("\n")
            curr_num = nums[left]
            # Update counter
            if curr_num in num_count:
                num_count[curr_num] += 1
            else:
                num_count[curr_num] = 1
            # Check if count for curr_num is now greater than 2, if so increment dup_count and swap to back
            if num_count[curr_num] > 2:
                # print("Here")
                dup_count += 1
                # If at the end, return dup_count
                if left == right:
                    return len(nums) - dup_count
                # Change the right pointer until it's at a num diff than curr_num
                while nums[right] == curr_num:
                    num_count[curr_num] += 1
                    if num_count[curr_num] > 2:
                        dup_count += 1
                    right -= 1
                    # If now at left, can't go further swapping and should return, think of case like [1, 1, 1, 1, 1, 1]
                    if right == left:
                        return len(nums) - dup_count
                
                # Swap to back
                temp_left = left
                next_pointer = temp_left + 1
                
                while temp_left < right:
                    nums[next_pointer], nums[temp_left] = [nums[temp_left], nums[next_pointer]]
                    temp_left += 1
                    next_pointer += 1
                
                right -= 1
            
            else:
                left += 1

        return len(nums) - dup_count