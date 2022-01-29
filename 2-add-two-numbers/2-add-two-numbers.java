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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode first = dummy;
        
        boolean carry = false;
        while(l1 != null|| l2 != null){
            
            int sum = 0;
            if(carry){
                sum+= 1;
                carry = false;
            }
                
            if(l1 != null){
                sum += l1.val;
            }
            if(l2 != null){
                sum += l2.val;
            }
            if(sum >= 10){
                sum -= 10;
                carry = true;
            }
            dummy.next = new ListNode(sum);
            dummy = dummy.next;
            if(l1 != null)
                l1 = l1.next;
            if(l2 != null)
                l2 = l2.next;
        }
        if(carry){
            dummy.next = new ListNode(1);
        }
        return first.next;
    }
}