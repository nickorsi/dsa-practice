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
    HashSet<TreeNode> seenGoingLeft = new HashSet<>();
    HashSet<TreeNode> seenGoingRight = new HashSet<>();
    int maxPathCount = 0;
    int longestPath = 0;

    public int longestZigZag(TreeNode root) {
        // Go through all of the nodes with a queue doing BFS and traverse each node in zigzag fashion doing DFS
        // Keep track of elements seen going each direction to avoid duplicate path travels
        // Keep track of longest path when traversing in sizzag
        bFS(root);
        return longestPath;
    }
    public void bFS(TreeNode node) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(node);
        TreeNode currentNode;

        while(queue.size() > 0) {
            currentNode = queue.poll();
            // System.out.println("Start zig left");
            maxPathCount = 0;
            dFSZigZag(currentNode, true, 0);
            longestPath = Math.max(longestPath, maxPathCount);
            // System.out.println("Start zig right");
            maxPathCount = 0;
            dFSZigZag(currentNode, false, 0);
            longestPath = Math.max(longestPath, maxPathCount);
            if(currentNode.left != null) {
                queue.offer(currentNode.left);
            }
            if(currentNode.right != null) {
                queue.offer(currentNode.right);
            }
       }
    }
    public void dFSZigZag(TreeNode node, boolean goingLeft, int pathCount) {
        // System.out.println(node);
        // System.out.println("pathCount= " + pathCount);
        // System.out.println("goingLeft= " + goingLeft);
        if(node == null) {
            maxPathCount = Math.max(maxPathCount, pathCount - 1);
            return;
        } 
        if(goingLeft) {
            if(!seenGoingLeft.contains(node)) {
                seenGoingLeft.add(node);
                dFSZigZag(node.left, false, pathCount + 1);
            }
            maxPathCount = Math.max(maxPathCount, pathCount - 1);
            return;
        } else {
            if(!seenGoingRight.contains(node)) {
                seenGoingRight.add(node);
                dFSZigZag(node.right, true, pathCount + 1);
            }
            maxPathCount = Math.max(maxPathCount, pathCount - 1);
            return;
        }
    }
}