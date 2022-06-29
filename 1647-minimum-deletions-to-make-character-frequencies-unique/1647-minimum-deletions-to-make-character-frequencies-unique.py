class Solution:
    def minDeletions(self, s: str) -> int:
        s = sorted(s)
        deletes = 0
        counts = set()
        curCount = 1
        for i in range(1,len(s)):
            prev = s[i-1]
            cur = s[i]
            if cur != prev:
                while curCount > 0 and curCount in counts:
                    deletes += 1
                    curCount -= 1
                    
                counts.add(curCount)
                curCount = 1
            else:
                curCount += 1
                
        while curCount > 0 and curCount in counts:
            deletes += 1
            curCount -= 1
        return deletes
            
        