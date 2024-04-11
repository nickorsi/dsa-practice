class Solution:
    def simplifyPath(self, path: str) -> str:
#       Use stack
        stack = []
#       Iterate through each portion of the path split by "/"
        print("//home/".split('/'))
        for portion in path.split("/"):
#           If it's "." or "", skip
            if portion == "." or portion == "": continue
#           If it's "..", pop off the stack
            if portion == "..": 
#               if stack is truthy pop off
                if stack: stack.pop()
                continue
#           Otherwise add to stack
            stack.append(portion)
#       Return "/" + "/".join(stack)
        return "/" + "/".join(stack)