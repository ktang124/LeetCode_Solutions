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
class BSTIterator {
    
    List<Integer> arr;
    Iterator<Integer> iter;
    public BSTIterator(TreeNode root) {
        arr = new ArrayList<>();
        inOrder(root);
        iter = arr.iterator();
    }
    private void inOrder(TreeNode root){
        if(root == null){
            return;
        }
        inOrder(root.left);
        arr.add(root.val);
        inOrder(root.right);
        
    }
    
    public int next() {
        return iter.next();
    }
    
    public boolean hasNext() {
        return iter.hasNext();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */