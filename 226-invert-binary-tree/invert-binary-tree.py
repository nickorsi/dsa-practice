# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case is root == None, return
        if root == None:
            return
        # Reassign left and right values
        root.left, root.right = [root.right, root.left]
        # Recurse passing in left
        self.invertTree(root.left)
        # Recurse passing in right
        self.invertTree(root.right)
        # Return root
        return root