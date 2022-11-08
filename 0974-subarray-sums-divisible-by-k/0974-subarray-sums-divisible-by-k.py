class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #naive solution would be to iterate through every subarray
        #n^2 solution times out
        prefix = [0] * (len(nums)+1)
        counter = defaultdict(int)
        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i] + num
        for i,c in enumerate(prefix):
            counter[c%k] += 1
        return sum((n*(n-1))//2 for n in counter.values())