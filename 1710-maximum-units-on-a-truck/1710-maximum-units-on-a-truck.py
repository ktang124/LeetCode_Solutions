class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = sorted(boxTypes, key = lambda x: x[1],reverse = True)
        total = 0
        i = 0
        for i in range(len(boxes)):
            if(truckSize == 0):
                return total
            clear = min(boxes[i][0], truckSize)
            total += (clear * boxes[i][1])
            truckSize -= clear
            
        return total
            
            