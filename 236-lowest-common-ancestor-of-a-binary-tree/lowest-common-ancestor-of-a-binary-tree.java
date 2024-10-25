/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    TreeNode ans;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // ALL NODES ARE UNIQUE!
        // Need to traverse entire tree, DFS or BFS? Use DFS
        // When traversing tree, need to know if p an q have been seen, either on the left, right, or on self
        // There will only be ONE time the targets have been seen on left and right, self and left, or self and right
        // At this point can assign the node to ans
        this.dFS(root, p, q);
        return this.ans; 
    }
    public boolean dFS(TreeNode node, TreeNode p, TreeNode q) {
        if(node == null) {
            return false;
        } 
        
        int left = this.dFS(node.left, p,  q) ? 1 : 0;

        int right = this.dFS(node.right, p,  q) ? 1 : 0;

        int self = (node == p || node == q) ? 1 : 0;

        if(left + right + self >= 2) {
            this.ans = node;
        }

        return (left + right + self > 0);
    }
}