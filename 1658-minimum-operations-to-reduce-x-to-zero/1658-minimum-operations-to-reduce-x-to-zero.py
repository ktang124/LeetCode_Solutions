class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        #every time you reduce, you either pick one or the other
        #either pick left or pick right. You can save the state of choosing left or right
        total = sum(nums)
        want = total-x
        start = 0
        
        windowSum = 0
        #want windowSum to be total-x and want the windowsize to be big
        windowSize = -1
        for end in range(0, len(nums)):
            windowSum += nums[end]
            while start < len(nums) and windowSum >want:
                windowSum -= nums[start]
                start += 1
            if windowSum == want:
                windowSize = max(windowSize, end-start+1)
                
        
        if windowSize == -1:
            return -1
                
        return len(nums) - windowSize
    
  #1,1,4 want window to equal 6

                    