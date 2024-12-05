class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations: List[int] = []

        def backtrack(nums: List[int], permutation: List[int]) -> None:
            if len(nums) == 0:
                permutations.append(permutation)
                return
            
            for i in range(len(nums)):
                new_permutation = [*permutation, nums[i]]
                new_nums = [*nums[0:i:], *nums[i+1::]]
                backtrack(new_nums, new_permutation)
        
        backtrack(nums, [])
        
        return permutations


    
            