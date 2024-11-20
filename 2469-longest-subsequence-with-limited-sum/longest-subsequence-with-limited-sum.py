class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
#         Can sort nums and then make a prefix nums to take advantage of binary search
#         Doesn't say whether the nums in nums are distinct, so will find the right most value
#         Can then take the len - left and add this value to ans
        nums.sort(key=lambda x:x)
        prefix_nums: List[int] = []
        
        for i in range(len(nums)):
            if i == 0:
                prefix_nums.append(nums[i])
            else: 
                prefix_nums.append(nums[i] + prefix_nums[i - 1])
        
        print(prefix_nums)
        
        ans: List[int] = []
            
        for query in queries:
            left = 0
            right = len(prefix_nums) - 1

            while left < right: 
                mid = (right + left) // 2

                if prefix_nums[mid] > query:
                    right = mid
                else:
                    left = mid + 1
            if prefix_nums[left] > query:
                ans.append(left)
            else: ans.append(left + 1)
        
        return ans
            