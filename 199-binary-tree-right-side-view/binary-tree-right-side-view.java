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
    ArrayList<Integer> seen = new ArrayList<> ();

    public List<Integer> rightSideView(TreeNode root) {
        // Use a queue in this case? 
        // With each level, pick the "last" value as the seen node
        // Can track the seen nodes as a List of integers
        // Use queue with LinkedList data structure to offer and poll values on and off
        // Need to track the depth of each as well, so will make the queue and ArrayList, first element being a TreeNode and second being an int for depth
        if(root!= null) {
            bFS(root);
        }
        return this.seen;
    }

    public void bFS(TreeNode root) {
        Queue<NodeDepth> queue = new LinkedList<>();
        queue.offer(new NodeDepth(root, 0));
        NodeDepth current;

        while(queue.size() > 0) {
            current = queue.poll();
            if(current.node.left != null) queue.offer(new NodeDepth(current.node.left, current.depth + 1));
            if(current.node.right != null) queue.offer(new NodeDepth(current.node.right, current.depth + 1));

            if(queue.size() == 0) {
                this.seen.add(current.node.val);
            } else if(current.depth < queue.peek().depth) {
                this.seen.add(current.node.val);
            }
        }
    }
}

class NodeDepth {
    TreeNode node;
    int depth;

    NodeDepth(TreeNode node, int depth) {
        this.node = node;
        this.depth = depth;
    }
}