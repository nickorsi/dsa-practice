class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        sub_string = ''
        answers = [sub_string]
        min_length = min(len(str1), len(str2))
    #   Iterate through the smallest string
        for i in range(min_length):
    #   If letter at each string doesn't match, return ''
            if str1[i] != str2[i]:
                return ''
    #   Add a letter to substring
            sub_string += str1[i]
    #   Split both str1 and str2 by this substring and see if joining the back together is equal to ''
            str1_split = str1.split(sub_string)
            str2_split = str2.split(sub_string)

            if ''.join(str1_split) == '' and ''.join(str2_split) == '':
    #   If so add this to the answers array
                answers.append(sub_string)
    #   Return the last element from the answers array
        return answers[-1]