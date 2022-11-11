class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = [False] * 201
        #hashset of 200 elements
        
        for n in nums:
            key = n+100
            counter[key] = True
        keyIndex = 0
        k = sum(counter)
        for i in range(len(nums)):
            while keyIndex < 200 and not counter[keyIndex]:
                keyIndex += 1
            nums[i] = keyIndex-100
            keyIndex += 1
        return k
        