# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    hash = Hash.new()
    
    for i in 0..nums.length-1 do
        complement = target - nums[i]
        if hash[complement] then
            return Array[hash[complement], i];
        end
        hash[nums[i]] = i
    end
    
end