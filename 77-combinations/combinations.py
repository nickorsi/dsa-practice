class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Use same backtrack approach with building permutations, but use k as the base case
        combos: List[List[int]] = []

        def backtrack(curr: List[int], i: int) -> None:
            if len(curr) == k:
                combos.append(curr[:])
                return
            
            for j in range(i, n + 1):
                curr.append(j)
                backtrack(curr, j + 1)
                curr.pop()

        backtrack([], 1)
        return combos
