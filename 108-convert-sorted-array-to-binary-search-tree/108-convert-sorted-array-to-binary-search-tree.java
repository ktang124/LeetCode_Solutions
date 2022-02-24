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
    public TreeNode sortedArrayToBST(int[] nums) {
        return aux(nums,0,nums.length-1);
    }
    private TreeNode aux(int[] nums, int left, int right){
        if(left > right) return null;
        int mid = (right + left)/2;
        TreeNode root = new TreeNode(nums[mid]);
        TreeNode l = aux(nums, left, mid-1);
        TreeNode r = aux(nums, mid+1, right);
        root.left = l;
        root.right = r;
        return root;
    }
}