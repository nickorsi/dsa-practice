class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Use dp, as trying to find the max length in a string, where picking one path affects future paths
        # Need to determine function inputs and outputs
            # Inputs need to track the index position of BOTH strings, so 2-d DP problem, and output is the max length
        # Need to determine recurrence relation
            # Letters match, then do 1 PLUS the result of looking at the next letter for each string 
            # Letter don't match, then either look at next letter in str1 or str2
            # dp(i, j) = max(dp(i, j+1), dp(i+1, j))
        # Determine the base case
            # If i or j is past the respective string length, return 0
        
        memo: Dict[str, int] = {}

        def dp(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
            
            str_ij = str(i) + str(j)

            if str_ij in memo:
                return memo[str_ij]
            
            if text1[i] == text2[j]:
                memo[str_ij] = 1 + dp(i + 1, j + 1)
            
            else:
                memo[str_ij] = max(dp(i + 1, j), dp(i, j + 1))
            
            return memo[str_ij]

        return dp(0, 0)