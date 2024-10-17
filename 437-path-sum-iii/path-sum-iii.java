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
    int targetSum;
    int pathCount = 0;

    public int pathSum(TreeNode root, int targetSum) {
        // Traverse through the node via recursion while collecting an array of pathSums
        // If the node is the target value, increase the pathCount
        // As the node tree is traversed, the pathSums is iterated through and the current node is added to all values in the array
        this.targetSum = targetSum;
        if(root == null) return this.pathCount;
        traversePath(root, new ArrayList<Long>());
        // System.out.println("Final output " + this.pathCount);
        return this.pathCount;
    }
    public void traversePath(TreeNode root, ArrayList<Long> pathSums) {
        // Add the current val to the tracked path sums
        updatePathSums(pathSums, root.val, false);
        // Basecase: If this is a leaf node (no children)
        if(root.left == null && root.right == null) {
            // Remove this val from the tracked path sums and return
            // System.out.println("LEAF");
            updatePathSums(pathSums, -root.val, true);
            return;
        }
        // If there's left children, traverse through this path
        if(root.left != null) {
            traversePath(root.left, pathSums);
        }
        // If there's right children, traverse through this path
        if(root.right != null) {
            traversePath(root.right, pathSums);
        }
        // If you gone through all the paths, remove the current value from the path sums
        // System.out.println("Remove Node");
        updatePathSums(pathSums, -root.val, true);
    }

    public void updatePathSums(ArrayList<Long> pathSums, int val, boolean removal) {
        // If the current value is equal to the targetSum, increment the pathCount
        // System.out.println(pathSums);
        // System.out.println(val);
        // System.out.println(this.pathCount);
        if(!removal && val == this.targetSum) {
            // System.out.print("Val is equal to target " + val);
            this.pathCount += 1;
        }
        // Iterate through the pathSums
        for(int i = 0; i < pathSums.size(); i ++) {
            // Add the value to the current pathSum
            long newPathSum = pathSums.get(i) + val;
            // System.out.println("val = " + val);
            // System.out.println("val at i = " + pathSums.get(i));
            // System.out.println("Newpathsum = " + newPathSum);
            // If this is not a removal and the newPathSum is equal to the targetSum, increment the pathCount
            if(!removal && newPathSum == this.targetSum) {
                // System.out.print("newPath is equal to target " + newPathSum);
                this.pathCount += 1;
            }
            // Update pathSums with the new value
            pathSums.set(i, newPathSum);
        }
        // If this is a removal, remove the last value
        if(removal) {
            pathSums.remove(pathSums.size() - 1);
        // Otherwise add the current value as a new pathSum
        } else {
            pathSums.add((long) val);
        }
    }
}