class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = 0
        maximum = 0
        numSet = set()
        cur = 0
        for end, num in enumerate(nums):
            cur += num
            while start < len(nums) and num in numSet:
                cur -= nums[start]
                numSet.remove(nums[start])
                start += 1
            numSet.add(num)
            maximum = max(cur, maximum)
            
        return maximum
                