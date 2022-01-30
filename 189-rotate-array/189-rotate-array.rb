# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
def rotate(nums, k)
    k = k% nums.length
    swapInRange(0,nums.length-1, nums)
    swapInRange(0,k-1, nums)
    swapInRange(k, nums.length-1, nums)
end
    
def swapInRange(left, right, nums)
    #Integer, Integer, Integer[]
    while(left < right)
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
    end
end
