
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combos: List[List[int]] = []

        # Use recursive backtracking to build up number combos
        def backtrack(curr: Set[int], start: int) -> None:
            # Base Case: length of current combo == k
            if len(curr) == k:
                # If sum of current combo == n then append to the combo list
                if sum(curr) == n:
                    curr_list = list(curr)
                    combos.append(curr_list)
                # Return
                return
            # Loop through 1 to 9
            for num in range(start, 10):
                # Can only use each number once! Use a set in function for fast inclusion logic, then convert to a list in the base case
                # Also looking for COMBOS, so should not look at ALL of the numbers with every recurion, need to keep track of current start
                # number and use all numbers AFTER this to build the combos, otherwise will get repeated values ie [2,3,4], [4,3,2], etc
                if num not in curr:
                    # Append to current combo
                    curr.add(num)
                    # Enter backtrack
                    backtrack(curr, num + 1)
                    # Pop off the last append
                    curr.remove(num)
        
        backtrack(set(), 1)
        return combos