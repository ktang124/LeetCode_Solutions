class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        rightList = [nums[-1]]
        for i in reversed(range(len(nums)-1)):
            index = bisect.bisect_left(rightList, nums[i])
            counts[i] = index
            rightList.insert(index, nums[i])
            
        return counts