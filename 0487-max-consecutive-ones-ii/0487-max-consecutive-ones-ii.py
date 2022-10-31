class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #find the max sliding window with just one zero inside
        start = 0
        countZero = 0
        maxWindow = 0
        for end, num in enumerate(nums):
            if num == 0:
                countZero +=1
            while countZero > 1:
                if nums[start] == 0:
                    countZero -= 1
                start += 1
            maxWindow = max((end-start)+1, maxWindow)
        return maxWindow