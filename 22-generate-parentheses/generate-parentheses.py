class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Have option of being opened or closed
        # Combination is successful when there are n open and closed parenthesis
        # Well formed only if there is the same number of closed as there are opened and end with a count of 0 unclosed parenthesis
        paren_combos: List[str] = []

        def backtrack(curr_combo: List[str], unclosed_paren_count: int) -> None:
            if len(curr_combo) == n * 2:
                if curr_combo[-1] == ")" and unclosed_paren_count == 0:
                    # print("*****Here, curr_combo= ", curr_combo)
                    paren_combos.append(('').join(curr_combo))
                return 
            
            paren_options: List[str] = ["(", ")"]
            # print("curr_combo= ", curr_combo)
            # print("unclosed_paren_count= ", unclosed_paren_count)
            for paren in paren_options:
                # print("paren= ", paren)
                # print("\n")
                if paren == "(":
                    curr_combo.append(paren)
                    unclosed_paren_count += 1
                    backtrack(curr_combo, unclosed_paren_count)
                    unclosed_paren_count -= 1
                    curr_combo.pop()
                else:
                    if unclosed_paren_count > 0: 
                        curr_combo.append(paren)
                        unclosed_paren_count -= 1
                        backtrack(curr_combo, unclosed_paren_count)
                        unclosed_paren_count += 1
                        curr_combo.pop()
                
            
            return 

        backtrack(["("], 1)

        return paren_combos
