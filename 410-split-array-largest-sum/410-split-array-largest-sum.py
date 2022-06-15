class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums) + 2
        while left < right:
            mid = left + (right-left)//2
            if self.canSplit(nums,mid, m):
                right = mid
            else:
                left = mid +1 
            
        return left
    
    def canSplit(self, nums, largestSum, m):
        curSum = 0
        subArrays = 1
        for num in nums:
            
            if curSum + num > largestSum:
                subArrays += 1
                curSum = 0
            curSum += num
            
                
        return subArrays <= m