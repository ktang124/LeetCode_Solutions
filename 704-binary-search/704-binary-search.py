class Solution:
    def search(self, nums: List[int], target: int) -> int:
        insert = bisect.bisect_left(nums, target)
        if insert >= len(nums) or nums[insert]!= target:
            return -1
        else:
            return insert