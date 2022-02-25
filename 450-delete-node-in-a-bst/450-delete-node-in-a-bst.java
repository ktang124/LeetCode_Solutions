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
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root == null) return null;
        if(root.val == key){
            //leaf case
            if(root.left == null && root.right == null){
                return null;
            } else{
                boolean right = true;
                TreeNode replace = min(root.right);
                if(replace == null){
                    replace = max(root.left);
                    right = false;
                }
                int toDelete = replace.val;
                root.val = replace.val;
              
                if(right){
                    root.right = deleteNode(root.right, toDelete);
                }else{
                    root.left = deleteNode(root.left, toDelete);
                }
                 return root;
            }
           
        }else if(key > root.val){
            root.right = deleteNode(root.right, key);
        }else{
             root.left = deleteNode(root.left, key);
        }
        return root;
    }
    
    private TreeNode min(TreeNode root){
        if(root == null){
            return null;
        }
        if(root.left == null){
            return root;
        }
        return min(root.left);
    }
    private TreeNode max(TreeNode root){
        if(root == null){
            return null;
        }if(root.right == null){
            return root;
        }
        return max(root.right);
    }
}