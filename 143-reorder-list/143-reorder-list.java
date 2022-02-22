class Solution {
    public void reorderList(ListNode head) {
        Deque<ListNode> dq = new ArrayDeque<>();
        ListNode cur = head;
        ListNode addNode = new ListNode(0);
        ListNode dummy = addNode;
        while(cur != null){
            dq.addLast(cur);
            cur = cur.next;
        }
        while(!dq.isEmpty()){
            addNode.next = dq.pollFirst();
            addNode = addNode.next;
            if(!dq.isEmpty()){
                addNode.next = dq.pollLast();
                addNode = addNode.next;
            }
        }
       addNode.next = null;
       head = dummy.next;
    }
}