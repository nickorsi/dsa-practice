class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations: List[List[int]] = []

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

        # Above solution does not take advantage of the fact that all nums are unique, can therefore do the below: 

        # def backtrack(curr):
        #     if len(curr) == len(nums):
        #         ans.append(curr[:]) 
        #         """
        #             Note how we are appending a copy of curr and not curr itself. This is becuase using curr directly 
        #             will only be passed as a reference and not as a value. This means appending curr will always point to
        #             the value that is assigned to curr. As this recursion progresses, the value assigned to curr will always 
        #             revert back to being an empty array [] based on how this function is implemented, where values are 
        #             appended but then ecentually popped off. If you were to try and append curr instead, you'll see the answer 
        #             will have the correct number of arrays in it, but they are all empty. So we have to append a copy of of 
        #             the value assigned to curr AT THIS SPECIFIC MOMENT when it needs to be appended to ans.
        #         """ 
        #         return

        #     for num in nums:
        #         if num not in curr:
        #             curr.append(num)
        #             backtrack(curr)
        #             curr.pop()

        # ans = []
        # backtrack([])
        # return ans
    
            