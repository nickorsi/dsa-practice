class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
#   Declare hash map for nums to indexk
        nums_to_ind = dict()
#   Iterate through nums2 to create hash table of values to indices
        for i in range(len(nums2)):
            nums_to_ind[nums2[i]] = i
#   Iterate through nums1
        for num in nums1:
#       Declare ans_num = -1
            ans_num = -1
#       Iterate through nums2 from the corresponding index value to the length of nums2
            for j in range(nums_to_ind[num], len(nums2)):
#           if value is larger than num1 then reassgn ans_num to num1
                if nums2[j] > num:
                    ans_num = nums2[j]
                    break
#       Push ans_num to ans
            ans.append(ans_num)
#   Return ans
        return ans