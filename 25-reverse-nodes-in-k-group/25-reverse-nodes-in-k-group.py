class Solution:
    def reverseKGroup(self, head, k):
        cur = head
        
        if cur:
            run = cur
            count = k-1
            while count > 0 and run:
                count -= 1
                run = run.next
            if count > 0 or run == None:
                #base case, could not reverse
                return head
            else:
                #can reverse
                count = k
                prev = self.reverseKGroup(run.next, k)
                
                while count>0:
                    count-=1
                    temp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = temp
                    
                return prev
        return head
                    