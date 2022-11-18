class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0: return False
        factors = [2,3,5]
        while sum(not n%f for f in factors):
            n = (n//2) if n % 2 == 0 else (n//3 if n % 3 == 0 else n//5)
        return n == 1