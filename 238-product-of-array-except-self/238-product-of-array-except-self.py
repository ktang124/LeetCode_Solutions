class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0 ]* len(nums)
        pre = 1
        for i in range(len(nums)):
            prefix[i] = pre * nums[i]
            pre = prefix[i]
       
        #1,2,6,24
        #24,24,12,4
        
        suffix = [0] * len(nums)
        post = 1
        for i in reversed(range(len(nums))):
            suffix[i] = post * nums[i]
            post = suffix[i]
            
        res = [0 ]* len(nums)
        res[0] = suffix[1]
        res[-1] = prefix[-2]
        #24,,6
        for i in range(1,len(nums)-1):
            res[i] = prefix[i-1] * suffix[i+1]
        return res