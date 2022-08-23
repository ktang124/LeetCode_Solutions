class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        powFour = 1
        while powFour <= n:
            if powFour == n:
                return True
            powFour *= 4
            
        return False