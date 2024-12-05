class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        # permutations: List[int] = []

        # def backtrack(nums: List[int], permutation: List[int]) -> None:
        #     if len(nums) == 0:
        #         permutations.append(permutation)
        #         return
            
        #     for i in range(len(nums)):
        #         new_permutation = [*permutation, nums[i]]
        #         new_nums = [*nums[0:i:], *nums[i+1::]]
        #         backtrack(new_nums, new_permutation)
        
        # backtrack(nums, [])
        
        # return permutations

        # Above solution does not take advantage of the fact that all nums are unique, can therefore do the below: 

        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans
    
            