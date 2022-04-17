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
    List<Integer> lst;
    int index;
    
    public BSTIterator(TreeNode root) {
        lst = new ArrayList<>();
        build(root);
    
        index = -1;
    }
    
    private void build(TreeNode root){
        if(root == null) return;
        build(root.left);
        lst.add(root.val);
        build(root.right);
    }
    
    public boolean hasNext() {
        return index < lst.size()-1;
    }
    
    public int next() {
        index++;
       return lst.get(index);
       
    }
    
    public boolean hasPrev() {
        return index > 0;
    }
    
    public int prev() {
        index--;
      return lst.get(index);
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * boolean param_1 = obj.hasNext();
 * int param_2 = obj.next();
 * boolean param_3 = obj.hasPrev();
 * int param_4 = obj.prev();
 */