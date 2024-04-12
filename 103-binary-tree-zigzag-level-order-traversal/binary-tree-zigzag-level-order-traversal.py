from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#       If empty return empty array
        if not root: return []
#       Alternate using queue and stack? 
        depth = 0
        queue = deque([root])
        ans = []
        
        while queue:
            zig_order = []
            level_length = len(queue)
            for _ in range(level_length):
                current_node = queue.popleft()
                zig_order.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                    
            if depth % 2 == 0:
                ans.append(zig_order)
            else:
                zag_order = []
                
                for _ in range(level_length):
                    zag_order.append(zig_order.pop())
                
                ans.append(zag_order)
                
            depth += 1
        
        return ans
 
                

        
        
        