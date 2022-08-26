class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        twoPows = [(1<<i) for i in range(31)]
        compare = sorted(str(n))
        for twoPow in twoPows:
            sortStr = sorted(str(twoPow))
            if compare == sortStr:
                return True
            
        return False
        
        
        