class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
# Want to maximize the number of boxes that return the most units/box
# Will continue to use these until there's none left or until you can't fit anymore
# Need to sort the boxes by this property, then iterate through the sorted array picking boxes
        boxTypesSorted = sorted(boxTypes, key=lambda a : a[1])
        
        ans = 0
        
        while truckSize and boxTypesSorted:
            boxes, units = boxTypesSorted.pop()
            
            if boxes < truckSize:
                ans += boxes * units
                truckSize = truckSize - boxes
            else:
                ans += truckSize * units
                truckSize = 0
        return ans
                