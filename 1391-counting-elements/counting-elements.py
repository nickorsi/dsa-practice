class Solution:
    def countElements(self, arr: List[int]) -> int:
#   Define count
#         count = 0
# #   Loop through arr
#         for num in arr:
# #       If arr + 1 in arr, increment count
#             if num + 1 in arr:
#                 count += 1
# #   Return count
#         return count

        countDict = {x: 0 for x in arr}
#   Loop through arr
        for num in arr:
#       If arr + 1 in countDict, increment count
            if num + 1 in countDict:
                countDict[num] += 1
#   Return sum of the values
        return sum(countDict.values())