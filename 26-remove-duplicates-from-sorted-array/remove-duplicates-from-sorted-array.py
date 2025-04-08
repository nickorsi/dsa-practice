class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left: int = 0
        right: int = 1
        indexOfUniqueNums: List[int] = [left]

        while right < len(nums): 
            if nums[left] != nums[right]:
                indexOfUniqueNums.append(right)
                left = right
            right += 1

        for i in range(1, len(indexOfUniqueNums)):
            nums[indexOfUniqueNums[i]], nums[i] = [nums[i], nums[indexOfUniqueNums[i]]]

        return len(indexOfUniqueNums)
            
            
                    