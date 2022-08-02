class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nList = [0] * len(nums)
        left = 0
        right = len(nums)-1
        for num in nums:
            if num & 1 == 0:
                nList[left] = num
                left += 1
            else:
                nList[right] = num
                right -= 1
                
        return nList