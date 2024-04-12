from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        sum_of_level = 0
        queue = deque()
        queue.append(root)
    
        while queue:
            sum_of_level = 0
            
            level_size = len(queue)
            
            for node in range(level_size):
                current_node = queue.popleft()
                sum_of_level += current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                    
        return sum_of_level