class Solution:
    d: dict[str, str] = {
        "2": ["a","b", "c"],
        "3": ["d","e", "f"],
        "4": ["g","h", "i"],
        "5": ["j","k", "l"],
        "6": ["m","n", "o"],
        "7": ["p","q", "r", "s"],
        "8": ["t","u", "v"],
        "9": ["w","x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        return self.build_letter_combos(digits)

    def build_letter_combos(self, digits: str) -> List[str]:
        letter_combos: List[str] = []
        
        if len(digits) == 0: return letter_combos

        curr_letter_combos = self.d[digits[0]]
        # print(curr_letter_combos)
        new_digits = digits[1:]
        # print(new_digits)

        next_letter_combos = self.build_letter_combos(new_digits)
        # print(next_letter_combos)
        if len(next_letter_combos) == 0: return curr_letter_combos

        for curr_letter_combo in curr_letter_combos:
            for next_letter_combo in next_letter_combos:
                letter_combos.append(curr_letter_combo + next_letter_combo)
        
        return letter_combos
        



