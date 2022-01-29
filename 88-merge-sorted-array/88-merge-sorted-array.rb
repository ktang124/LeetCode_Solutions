# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
    j = 0
   for i in m.. nums1.length-1 do
       nums1[i] = nums2[j]
       j += 1
   end
    nums1.sort!
    nums1
    
end