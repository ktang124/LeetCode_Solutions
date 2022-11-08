class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0] * (len(nums)+1)
        counter = defaultdict(lambda: -1)
        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i] + num
        for i,c in enumerate(prefix):
            if counter[c%k] == -1:
                counter[c%k] = i
        
        for i,pre in enumerate(prefix):
            #what do i need to subtract from pre to get a number divisible by k?
            complement = pre%k
            if counter[complement] != -1 and i >= counter[complement] + 2:
                return True
       
        return False