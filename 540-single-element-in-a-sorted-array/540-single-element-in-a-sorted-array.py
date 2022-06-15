class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        #len of nums is always odd because of 2k+1 elements
        while left <= right:
            mid = left + (right-left)//2
            curNum = nums[mid]
            isLeftSame = mid > 0 and nums[mid-1] == curNum
            isRightSame = mid < len(nums) - 1 and nums[mid+1] == curNum
            if not isLeftSame and not isRightSame:
                return nums[mid]
            elif mid % 2 == 0:
                if isLeftSame:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if isLeftSame:
                    left = mid+1
                else:
                    right = mid-1
                    
        return -1
               
                
                
        #[1,1,2,3,3,4,4,8,8] len 9, mid = 4
        #[3,3,7,7,8,8,10,11,11] len 9, mid = 4