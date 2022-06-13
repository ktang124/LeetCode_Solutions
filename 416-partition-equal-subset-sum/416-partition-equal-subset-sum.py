class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        states = set()
        states.add((0,0))
        total= sum(nums)
        if total % 2 != 0:
            return False
        half = total/ 2
        for num in nums:
            newList = set()
            for lst in states:
                if lst[0] <=half and lst[1] <= half:
                    newList.add((lst[0], lst[1]+num))
                    newList.add((lst[0]+num, lst[1]))
                
            states = newList
            
        for lst in states:
            if lst[0] == lst[1]:
                return True
            
        return False
                
            