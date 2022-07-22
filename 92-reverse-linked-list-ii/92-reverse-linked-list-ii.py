# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head
        dummy.next = head
        stack = []
        reverse = False
        
        if cur != None:
            for i in range(left-1):
                cur = cur.next
            for i in range((right-left)+1):
                stack.append(cur.val)
                cur = cur.next
            
        cur = head
        index = 0
        size = len(stack)
        if cur != None:
            for i in range(left-1):
                cur = cur.next
            for i in range((right-left)+1):
                cur.val = stack[size-i-1]
                cur = cur.next
                
            return dummy.next
            
        return dummy.next
            
                
                
                