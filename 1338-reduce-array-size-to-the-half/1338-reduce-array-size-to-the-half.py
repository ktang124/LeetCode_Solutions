class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        desiredSize = len(arr)//2
        
        #remove all of the most common occurences
        vals = counter.values()
        sortVals = sorted(vals, reverse = True)
        length = len(arr)
        for i, val in enumerate(sortVals):
            length -= val
            if length <= desiredSize:
                return i+1
            
        return length
            
        