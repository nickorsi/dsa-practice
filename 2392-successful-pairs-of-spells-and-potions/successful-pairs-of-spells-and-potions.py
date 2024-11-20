class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Can sort potions then do binary search for the value math.ceil(success / spells[i]) and find the left most value
        # When at the left most value, must determine that it actually does make a stronger potion
        # If it does add all the value from the end to the left position, otherwise add 0
        potions.sort(key=lambda x:x)
        ans: List[int] = []

        for spell in spells:
            target = math.ceil(success / spell)

            left = 0
            right = len(potions) - 1

            while left < right:
                mid = math.floor((right + left) / 2)

                if potions[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            
            if potions[left] * spell >= success:
                ans.append(len(potions) - left)
            else:
                ans.append(0)
        
        return ans