class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = defaultdict(int)
        desiredSize = len(arr)//2
        for num in arr:
            counter[num] += 1
        
        #remove all of the most common occurences
        vals = counter.values()
        sortVals = sorted(vals, reverse = True)
        length = len(arr)
        for i, val in enumerate(sortVals):
            length -= val
            if length <= desiredSize:
                return i+1
            
        return length
            
        