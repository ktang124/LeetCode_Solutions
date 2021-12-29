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
        Deque<Node> dq = new ArrayDeque<>();
        if(root == null) return null;
        dq.add(root);
        while(!dq.isEmpty()){
            int size = dq.size();
            while(size > 0){
                size--;
                Node cur = dq.pollFirst();
                if(cur != null && cur.left != null && cur.right != null){
                    cur.left.next = cur.right;
                    if(size > 0){
                        cur.right.next = dq.peekFirst().left;
                    }
                    dq.addLast(cur.left);
                    dq.addLast(cur.right);
                }
            }
           
        }
        return root;
    }
}