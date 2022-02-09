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
    public void flatten(TreeNode root) {
       List<TreeNode> flat = new ArrayList<>();
        preOrder(root, flat);
        for(int i = 1; i < flat.size(); i++){
            TreeNode cur = flat.get(i);
            cur.left = null;
            cur.right = null;
            root.right = cur;
            root = root.right;
        }
    }
    private void preOrder(TreeNode root, List<TreeNode> flat){
        if(root == null){
            return;
        }
        TreeNode tempLeft = root.left;
        TreeNode tempRight = root.right;
        root.left = null;
        root.right = null;
        flat.add(root);
        preOrder(tempLeft,flat);
        preOrder(tempRight,flat);
    }
}