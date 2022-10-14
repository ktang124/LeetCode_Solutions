# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        count = 0
        run = head
        while run != None:
            run = run.next
            count  += 1
        if count == 1:
            return None
        
        mid = count // 2
        for i in range(mid-1):
            slow = slow.next
            
        slow.next = slow.next.next
        
        return head