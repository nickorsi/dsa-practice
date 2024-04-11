class Solution:
    def makeGood(self, s: str) -> str:
#       If string empty, return
        if len(s) == 0: return s
#       Use a stack
        stack = []
#       Loop through string
        for char in s:
#           If last element in stack is same as current element, just reversed captilization, pop off
            if (
                stack and 
                ((char == char.upper() and char.lower() == stack[-1]) or
                (char == char.lower() and char.upper() == stack[-1]))
            ):
                stack.pop()
                continue
#           Otherwise add to stack
            stack.append(char)
#       Return stack joined
        return "".join(stack)