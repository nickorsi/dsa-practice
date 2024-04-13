# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    
        def helper(root: Optional[TreeNode], val) -> Optional[TreeNode]:
            if not root:
                return TreeNode(val)
            
            if val > root.val:
                if root.right:
                    helper(root.right, val)
                else:
                    root.right = helper(root.right, val)
            
            if root.val > val:
                if root.left:
                    helper(root.left, val)
                else:
                    root.left = helper(root.left, val)

        
        if not root:
            return TreeNode(val)
        
        helper(root, val)
        
        return root