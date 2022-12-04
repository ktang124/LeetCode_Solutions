class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        accumSum = [0] * len(nums)
        prev= 0
        for i,n in enumerate(nums):
            accumSum[i] = prev + n
            prev = accumSum[i]
        minimum = float('inf')
        minimumIndex = -1
        for i, n in enumerate(nums):
            l, r = accumSum[i], accumSum[-1] - accumSum[i]
            avgL, avgR = l//(i+1) , r//(len(nums)-i-1) if i+1< len(nums) else 0
            if (abs(avgL-avgR)) < minimum:
                minimum = (abs(avgL-avgR))
                minimumIndex = i
        return minimumIndex