class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        maxArray = []
        minArray = []
        #brute force
        s = 0
        for i in range(len(nums)):
            minimum = nums[i]
            maximum = nums[i]
            for j in range(i, len(nums)):
                minimum = min(nums[j], minimum)
                maximum = max(nums[j],maximum)
                s += maximum - minimum
                
        return s
        