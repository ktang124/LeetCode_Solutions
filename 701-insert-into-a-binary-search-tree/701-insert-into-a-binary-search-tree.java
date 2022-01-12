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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root == null){
            return new TreeNode(val);
        }
        
        TreeNode left; 
        TreeNode right; 
        
        if(val > root.val){
            
            right = insertIntoBST(root.right, val);
            left = root.left;
        }else{
            left = insertIntoBST(root.left, val);
            right = root.right;
        }
        root.left = left;
        root.right = right;
        
        return root;
    }
}