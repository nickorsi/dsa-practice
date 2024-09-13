# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # What's the best way to traverse? DFS or BFS? DFS seems to be the move to keep track of the path
        # Need to know the max value in a path at all times, but how to keep track and update as we traverse down and back up? 
        # Keep track of all values seen in an array, with value and level?
        self.good_node_count = 0
        # find_nodes function takes in node, level, and max_path_values array
        def _find_good_nodes(node: TreeNode, level: int, max_path_values: List[int]) -> None:
            print(node.val, level, max_path_values, self.good_node_count)
            # If current value is greater than or equal to last value on path_values
            if node.val >= max_path_values[-1][0]:
                # Increment count
                self.good_node_count += 1
                # If greater than push onto path_values with current value and level
                if node.val > max_path_values[-1][0]:
                    max_path_values.append([node.val, level])
            # If left is truthy
            if node.left:
                # Create new level
                new_level = level + 1
                # Recurse passing in left node, new level, and max_path_values
                _find_good_nodes(node.left, new_level, max_path_values)
            # If right is truthy
            if node.right:
                # Create new level
                new_level = level + 1
                # Recurse passing in right node, new level, and max_path_values
                _find_good_nodes(node.right, new_level, max_path_values)
            # If last max_path_values equals the current value and level, pop off
            if max_path_values[-1][0] == node.val and max_path_values[-1][1] == level:
                max_path_values.pop()
        # Return good_node_count
        _find_good_nodes(root, 0, [[root.val, 0]])
        print(self.good_node_count)
        return self.good_node_count
