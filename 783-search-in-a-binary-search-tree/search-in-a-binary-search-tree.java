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
    public TreeNode searchBST(TreeNode root, int val) {
        // Recursively search through BST
        return recursiveBST(root, val);
    }

    public TreeNode recursiveBST(TreeNode node, int val) {
        // Base case 1, node is null return null
        if(node == null) return null;
        // Base case 2, node val is val return node
        if(node.val == val) return node;
        // If node val is less than val, recurse to right val
        if(node.val < val) {
            return recursiveBST(node.right, val);
        }
        // If node val is greater than val, recurse to left val
        if(node.val > val) {
            return recursiveBST(node.left, val);
        }
        return null;
    }
}