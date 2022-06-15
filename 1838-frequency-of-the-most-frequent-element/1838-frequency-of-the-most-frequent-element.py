class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #pick a number in nums and try to increment the numbers behind it to a max frequency
        #this is brute force n^2
        nums.sort()
        maxFreq = 1 #length of sliding window
        start = 0
        curSum = 0
        #sliding window has property such that sum of sliding window + k >= nums[end] * length of window
        for end, num in enumerate(nums):
            curSum += num
            while start < len(nums) and curSum + k < ((end-start+1) * num):
                curSum -= nums[start]
                start += 1
                
            maxFreq = max(maxFreq, end-start+1)
            
        return maxFreq
    
  