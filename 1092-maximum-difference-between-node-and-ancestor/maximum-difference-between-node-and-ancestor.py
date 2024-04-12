# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def find_max_diff (root: Optional[TreeNode]) -> List[int]:
            if not root: return [None, None, float('-Inf')]
            
            left_values = find_max_diff(root.left)
            right_values = find_max_diff(root.right)

            if left_values[0] == None and right_values[0] == None:
                return [root.val, root.val, float('-Inf')]
            
            if left_values[0] == None and right_values[0] != None:
                return [
                    max(root.val, right_values[0]),
                    min(root.val, right_values[1]),
                    max(
                        abs(root.val - right_values[0]), 
                        abs(root.val - right_values[1]), 
                        right_values[2],
                    )
                ]
            if left_values[0] != None and right_values[0] == None:
                return [
                    max(root.val, left_values[0]),
                    min(root.val, left_values[1]),
                    max(
                        abs(root.val - left_values[0]), 
                        abs(root.val - left_values[1]), 
                        left_values[2], 
                    )
                ]
            return [
                    max(root.val, left_values[0], right_values[0]),
                    min(root.val, left_values[1], right_values[1]),
                    max(
                        abs(root.val - left_values[0]),
                        abs(root.val - right_values[0]),
                        abs(root.val - left_values[1]),
                        abs(root.val - right_values[1]),
                        left_values[2],
                        right_values[2],
                    )
                ]
        
        return find_max_diff(root)[2]
            