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
    public boolean isPalindrome(ListNode head) {
        List<Integer> lst = new ArrayList<>();
        while(head != null){
            lst.add(head.val);
            head = head.next;
        }
       for(int i = 0; i < lst.size()/2; i++){
           if(lst.get(i) != lst.get(lst.size()-1-i)) return false;
       }
        return true;
    }
}