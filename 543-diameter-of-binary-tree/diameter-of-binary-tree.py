# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode]) -> int:
            if not root: 
                return
            
            left = helper(root.left)
            right = helper(root.right)
            
            if not left and not right: 
                return [1,0]
            
            if not left and right:
                return [
                    1 + right[0], 
                    max(right[0], right[1])
                ]
            
            if left and not right:
                return [
                    1 + left[0], 
                    max(left[0], left[1])
                ]
            return [
                max(1 + left[0], 1 + right[0]),
                max(left[0] + right[0], left[1], right[1])
            ]
        
        return helper(root)[1]