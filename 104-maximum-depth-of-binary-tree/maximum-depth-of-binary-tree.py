from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Use BFS or DFS?
        self.max_level = 0

        if root == None: return self.max_level

        queue = deque([[1, root]])
        
        while queue:
            curr_level, curr_node = queue.popleft()
            
            self.max_level = max(self.max_level, curr_level)

            if curr_node.left:
                queue.append([curr_level + 1, curr_node.left])
            
            if curr_node.right:
                queue.append([curr_level + 1, curr_node.right])

        return self.max_level