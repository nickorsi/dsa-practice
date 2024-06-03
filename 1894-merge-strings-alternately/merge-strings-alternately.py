class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        # Determine the smallest array 
        min_length = min(len(word1), len(word2))
        # Iterate through this length adding element from word1 and then word2 into ans
        for i in range(min_length):
            ans.append(word1[i])
            ans.append(word2[i])
        # If word1 length > word2 length, iterate from minlength to word1 length and add to answer
        if len(word1) > len(word2):
            for i in range(min_length, len(word1)):
                ans.append(word1[i])
        # If word2 length > word1 length, iterate from minlength to word2 length and add to answer
        if len(word2) > len(word1):
            for i in range(min_length, len(word2)):
                ans.append(word2[i])
        # Return ans
        return "".join(ans)