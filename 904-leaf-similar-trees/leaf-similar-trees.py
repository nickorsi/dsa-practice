# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Need to traverse the tree and populate a leaf array for each
            # find_leaves function traverses binary tree and using dfs (recursion)
        leaves1 = self.find_leaves(root1)
        leaves2 = self.find_leaves(root2)
        # If the lengths of the leaf trees are not the same, return false
        if len(leaves1) != len(leaves2): return False
        # Iterate through the array, if at any point the elements at i aren't the same, return false
        for i in range(len(leaves1)):
            if leaves1[i] != leaves2[i]: return False
        # Return true
        return True

    def find_leaves(self, root: Optional[TreeNode]) -> List[int]:
        # Takes in root
        # Define leaves as empty array
        leaves: List[int] = []
        # If no children, return leaves with current root
        if not root.left and not root.right:
            leaves.append(root.val)
            return leaves
        # If left is truthy
        if root.left:
            # Append to array the spread out result of passing in left to recursion
            leaves.extend(self.find_leaves(root.left))
        if root.right:
        # If right is truthy
            # Append to array the spread out result of passing in right to recursion
            leaves.extend(self.find_leaves(root.right))
        # return leaves
        return leaves