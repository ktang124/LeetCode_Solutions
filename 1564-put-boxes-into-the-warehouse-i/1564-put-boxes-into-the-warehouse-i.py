class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        count = 0
        point = len(warehouse)-1
        minHeight = [warehouse[0]]
        for i in range(1,len(warehouse)):
            minHeight.append(min(minHeight[-1], warehouse[i]))
            
        while point >= 0 and count < len(boxes):
            #try to place 
            if minHeight[point] >= boxes[count]:
                count+= 1
                
            point -= 1
        return count