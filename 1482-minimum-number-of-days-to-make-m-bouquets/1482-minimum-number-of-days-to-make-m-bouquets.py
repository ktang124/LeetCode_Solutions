class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < (m*k):
            return -1
        
        left = 1
        right = max(bloomDay)
        
        while left < right:
            mid = left + (right - left) // 2
            if self.canMake(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1
                
        return left
    
    def canMake(self, bloomDay, m, k, days):
        adjs = 0
        bouquets = 0
        
        for bloom in bloomDay:
            if bloom <= days:
                adjs += 1
                if adjs == k:
                    adjs = 0
                    bouquets += 1
            else:
                adjs = 0
                
        return bouquets >= m