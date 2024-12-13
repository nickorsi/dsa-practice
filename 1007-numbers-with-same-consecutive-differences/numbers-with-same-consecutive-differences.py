class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # n is between 2 and 9 inclusive
        # First digit of n can be 1-9, all others can be 0-9
        # Preceeding digit must always be digit + k away and can only be used if <= 9
        # Can use backtracking to make these numbers
        # Will need to convert to and from string digits to int, must be careful of this
        nums: List[int] = []

        def backtrack(curr_digits: List[str]) -> None:
            if len(curr_digits) == n:
                nums.append(int(('').join(curr_digits)))
                return

            for digit in range(0, 10):
                
                if len(curr_digits) == 0:
                    if digit == 0:
                        continue
                    else:
                        curr_digits.append(str(digit))
                        backtrack(curr_digits)
                        curr_digits.pop()
                else:
                    last_digit = int(curr_digits[-1])
                    if abs(digit - last_digit) == k:
                        curr_digits.append(str(digit))
                        backtrack(curr_digits)
                        curr_digits.pop()
            return
        
        backtrack([])
        return nums
                