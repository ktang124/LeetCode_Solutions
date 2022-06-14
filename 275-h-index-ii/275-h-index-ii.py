class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)-1
        
        mid = 0
        while left <= right:
            mid = left  + (right - left) //2
            midVal = citations[mid]
            if len(citations) - mid == midVal:
                return midVal
            elif len(citations)-mid < midVal:
                right = mid-1
            else:
                left = mid+1
                
                
        return len(citations) - left
    
    #for the linear time algorithm, iterate until len(citations) - i == citations[i]