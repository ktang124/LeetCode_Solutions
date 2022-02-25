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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if(root == null) return res;
        Deque<TreeNode> deque = new ArrayDeque<>();
        deque.add(root);
        
        while(!deque.isEmpty()){
            int size = deque.size();
            while(size > 0){
                TreeNode polled = deque.pollLast();
                if(polled.left != null){
                    deque.addFirst(polled.left);
                }
                if(polled.right != null){
                    deque.addFirst(polled.right);
                }
                if(size == 1) res.add(polled.val);
                size--;
            }
        }
        return res;
    }
    private boolean aux(TreeNode root, List<Integer> res){
        if(root == null){
            return false;
        }else{
            res.add(root.val);
            if(!aux(root.right, res)){
                aux(root.left, res);
            }
            return true;
        }
    }
}