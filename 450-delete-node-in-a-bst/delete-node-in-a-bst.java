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
    TreeNode root;
    TreeNode parentNode;

    public TreeNode deleteNode(TreeNode root, int key) {
        // Will recursively search BST
        // When traversing, need to keep track of the parent node and direction
        // If the value is found...
            // Need to rebuild the tree knowing the direction traveled and the parent node
            // If parent was null then root becomes either left or right, with the other branch being attached at the logical spot
            // If parent not null then the parent must be adjusted with the direction traveled being rebuilt
        // Return root
        this.root = root;
        searchBTS(root, key, null, false);
        return this.root;
    }

    public TreeNode searchBTS(TreeNode node, int key, TreeNode parent, boolean isLeft) {
        if(node == null) {
            this.parentNode = parent;
            return null;
        }
        if(node.val == key) {
            // Build new tree
            if(parent == null) {
                this.root = buildNewTree(node.left, node.right);
                return this.root;
            }
            if(isLeft) {
                parent.left = buildNewTree(node.left, node.right);
                return parent;
            }
            parent.right = buildNewTree(node.left, node.right);
            return parent;
        }
        if(node.val < key) {
            return searchBTS(node.right, key, node, false);
        }
        return searchBTS(node.left, key, node, true);
    }

    public TreeNode buildNewTree(TreeNode left, TreeNode right) {
        if(left == null) return right;
        if(right == null) return left;

        searchBTS(left, right.val, null, false);
        this.parentNode.right = right;
        return left;
    }
}