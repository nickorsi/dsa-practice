class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = [[]]

        def backtrack(nums: List[int], subset: List[int]) -> None:
            if len(nums) == 0: 
                return
            
            for i in range(len(nums)):
                new_subset = [*subset, nums[i]]
                subsets.append(new_subset)
                new_nums = nums[i+1:]
                backtrack(new_nums, new_subset)

        backtrack(nums, [])
        return subsets

