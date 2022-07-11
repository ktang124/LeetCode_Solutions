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
}