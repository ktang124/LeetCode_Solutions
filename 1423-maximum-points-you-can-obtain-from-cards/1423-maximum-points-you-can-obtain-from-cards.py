class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #you want the sliding window to be of size cardPoints-k and you want the window 
        #of least value
        curVal = 0
        start = 0
        
        windowEnd = len(cardPoints) - k
        for i in range(windowEnd):
            curVal += cardPoints[i]
            
        minVal = curVal
        for end in range(windowEnd, len(cardPoints)):
            curVal += cardPoints[end]
            curVal -= cardPoints[start]
            start += 1
            minVal = min(curVal,minVal)
            
        total = sum(cardPoints)
        return total-minVal