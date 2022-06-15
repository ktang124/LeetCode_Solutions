class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
            
        return single