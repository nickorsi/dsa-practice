/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int maxSum;
    int minLevel;
    public int maxLevelSum(TreeNode root) {
        // Travel through tree via BFS
        // Keep track of maxLevelSum, levelSum, and level
        // Return maxLavelSum
        bFS(root);
        return this.minLevel;
    }

    public void bFS(TreeNode node) {
        Queue<NodeLevel> queue = new LinkedList<>();
        queue.offer(new NodeLevel(node, 1));
        int levelSum = node.val;
        int currentLevel = 1;
        this.maxSum = node.val;
        this.minLevel = 1;

        while(queue.size() != 0) {
            NodeLevel currentNodeLevel = queue.poll();
            
            if(currentNodeLevel.depth > currentLevel) {
                if(levelSum > this.maxSum) {
                    this.maxSum = levelSum;
                    this.minLevel = currentLevel;
                }
                levelSum = currentNodeLevel.node.val;
                currentLevel = currentNodeLevel.depth;
            } else {
                levelSum += currentNodeLevel.node.val;
            }
            if(currentNodeLevel.node.left != null) {
                queue.offer(new NodeLevel(currentNodeLevel.node.left, currentLevel + 1));
            }           
            if(currentNodeLevel.node.right != null) {
                queue.offer(new NodeLevel(currentNodeLevel.node.right, currentLevel + 1));
            } 
            // Need to account for instance where this is the last node
            if(queue.size() == 0) {
                if(levelSum > this.maxSum) {
                    this.maxSum = levelSum;
                    this.minLevel = currentLevel;
                }
            }    
        }
    }
}

class NodeLevel {
    TreeNode node;
    int depth;

    NodeLevel(TreeNode node, int depth) {
        this.node = node;
        this.depth = depth;
    }
}