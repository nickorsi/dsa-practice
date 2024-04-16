# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
#         def helper(root: Optional[TreeNode], target: float, closest_value: int) -> int:
#             if not root: 
#                 return closest_value
            
#             if abs(root.val - target) < abs(closest_value - target):
#                 closest_value = root.val
#             if abs(root.val - target) == abs(closest_value - target):
#                 closest_value = closest_value if closest_value < root.val else root.val

#             if target > root.val:
#                 return helper(root.right, target, closest_value)
            
#             else:
#                 return helper(root.left, target, closest_value)
            
#         return helper(root, target, float('inf'))
        def sort_nodes(root: Optional[TreeNode]) -> List[int]:
            if not root: return []
            sorted_nodes =  [*sort_nodes(root.left), root.val, *sort_nodes(root.right)]
            return sorted_nodes
        
        sorted_values = sort_nodes(root)
    
        min_val = float('inf')
        
        for val in sorted_values:
            if abs(min_val - target) > abs(val - target):
                min_val = val
        
        return min_val
           
            
        
        