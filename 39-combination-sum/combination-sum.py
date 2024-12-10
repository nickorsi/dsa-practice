class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations: List[int] = []

        # def backtrack1(curr_combo: List[int], curr_sum:int, curr_int: int) -> None:
        #     if curr_sum >= target:
        #         if curr_sum == target:
        #             combinations.append(curr_combo[:])
        #         return
            
        #     for i in range(curr_int, len(candidates)):
        #         curr_combo.append(candidates[i])
        #         curr_sum += candidates[i]
        #         backtrack(curr_combo, curr_sum, i)
        #         curr_combo.pop()
        #         curr_sum -= candidates[i]
        
        #     return

        # backtrack1([], 0, 0)

        def backtrack2(curr_combo: List[int], curr_int: int) -> None:
            curr_sum = sum(curr_combo)

            if curr_sum >= target:
                if curr_sum == target:
                    combinations.append(curr_combo[:])
                return
            
            for i in range(curr_int, len(candidates)):
                curr_combo.append(candidates[i])
                # curr_sum += candidates[i]
                backtrack2(curr_combo, i)
                curr_combo.pop()
                # curr_sum -= candidates[i]
        
            return
        
        backtrack2([], 0)
        return combinations