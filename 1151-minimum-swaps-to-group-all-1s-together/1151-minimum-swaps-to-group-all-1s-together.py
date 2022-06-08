class Solution:
    def minSwaps(self, data: List[int]) -> int:
        countOnes = 0
        for num in data: 
            if num == 1:
                countOnes += 1
            
        if countOnes == 0:
            return 0
        start = 0
        countZ = 0
        minCount = 99999999
        for end, num in enumerate(data):
            if num == 0:
                countZ += 1
            if(end-start+1) == countOnes:
                minCount = min(minCount, countZ)
                if data[start] == 0:
                    countZ -= 1
                start += 1
                
        return minCount
            