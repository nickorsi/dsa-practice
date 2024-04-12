# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def findMin(root: Optional[TreeNode]) -> int:
            if not root: return 0
            
            left_depth = findMin(root.left)
            right_depth = findMin(root.right)
            
            if not left_depth and right_depth:
                return 1 + right_depth
            if left_depth and not right_depth:
                return 1 + left_depth
            if left_depth and right_depth:
                return 1 + min(right_depth, left_depth)
            return 1
    
        return findMin(root)