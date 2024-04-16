# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def helper(root: Optional[TreeNode], target: float, closest_value: int) -> int:
            if not root: 
                return closest_value
            
            if abs(root.val - target) < abs(closest_value - target):
                closest_value = root.val
            if abs(root.val - target) == abs(closest_value - target):
                closest_value = closest_value if closest_value < root.val else root.val

            if target > root.val:
                return helper(root.right, target, closest_value)
            
            else:
                return helper(root.left, target, closest_value)
            
        return helper(root, target, float('inf'))