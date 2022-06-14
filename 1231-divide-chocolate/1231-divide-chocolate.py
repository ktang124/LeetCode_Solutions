class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        left = 1
        right = sum(sweetness) + 2
        
        maximum = 0
        while left < right:
            mid =  left + (right - left)// 2
            if self.verify(sweetness, mid, k):
                maximum = mid
                left = mid + 1
            else:
                right = mid
                
        return maximum
    
    def verify(self, sweetness, candidateMin, k):
        curChunk = 0
        totalChunks = 0
        for sweet in sweetness:
            curChunk += sweet
            if curChunk >= candidateMin:
                curChunk = 0
                totalChunks += 1
                
        return totalChunks > k