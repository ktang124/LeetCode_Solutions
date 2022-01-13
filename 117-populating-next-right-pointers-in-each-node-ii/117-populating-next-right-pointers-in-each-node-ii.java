/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if(root == null) return null;
        Deque<Node> dq = new ArrayDeque<>();
        dq.add(root);
        
        while(!dq.isEmpty()){
            int size = dq.size();
           
            while(size > 0){
                Node polled = dq.pollFirst();
                if(!dq.isEmpty() && size != 1){
                    polled.next = dq.peek();
                }
                if(polled.left != null) dq.addLast(polled.left); 
                if(polled.right != null) dq.addLast(polled.right);
                size--;
            }
        }
        return root;
    }
}