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
    public ListNode sortList(ListNode head) {
        if(head == null) return null;
        int min = Integer.MAX_VALUE;
        int max = 0;
        for(ListNode cur = head; cur != null; cur = cur.next){
            min = Math.min(cur.val, min);
            max = Math.max(cur.val, max);
        }
       int[] countingArray = new int[(max-min)+1];
         for(ListNode cur = head; cur != null; cur = cur.next){
            int key = cur.val - min;
            countingArray[key] += 1;
        }
        ListNode cur = new ListNode(0);
        ListNode dummy = cur;
 
      
        for(int i = 0; i < countingArray.length; i++){
            for(int j = 0; j < countingArray[i]; j++){
                cur.next = new ListNode(i+min);
                cur = cur.next;
            }
        }
        return dummy.next;
        
    }
}