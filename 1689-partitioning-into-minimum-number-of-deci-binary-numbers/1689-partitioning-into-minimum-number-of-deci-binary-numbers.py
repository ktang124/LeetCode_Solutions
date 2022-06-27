class Solution:
    def minPartitions(self, n: str) -> int:
        maximum = 0
        for c in n:
            maximum = max(int(c),maximum)
            
        return maximum