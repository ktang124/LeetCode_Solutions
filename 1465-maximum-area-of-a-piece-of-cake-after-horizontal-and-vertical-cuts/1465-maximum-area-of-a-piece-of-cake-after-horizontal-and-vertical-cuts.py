class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        mod = 10 ** 9 + 7
        hCuts = sorted(horizontalCuts)
        vCuts = sorted(verticalCuts)
        #find largest interval
        largestH = 0
        largestV = 0
        for i in range(len(hCuts)-1):
            largestH = max(largestH, (hCuts[i+1]-hCuts[i]))
            
        for i in range(len(vCuts)-1):
            largestV = max(largestV, (vCuts[i+1]-vCuts[i]))
            
        return (largestH * largestV) % mod
        