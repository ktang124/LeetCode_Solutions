/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode dummy = new ListNode(0);
        ListNode res = dummy;
        PriorityQueue<ListNode> pq = new PriorityQueue<>((o1,o2)->o1.val-o2.val);
        for(ListNode l : lists){
            if(l != null)
                pq.add(l);
        }
        while(!pq.isEmpty()){
            ListNode polled = pq.poll();
            dummy.next = polled;
            polled = polled.next;
            if(polled != null) pq.add(polled);
            dummy = dummy.next;
        }
        return res.next;
    }
}