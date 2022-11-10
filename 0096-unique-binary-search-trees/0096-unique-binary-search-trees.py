class Solution:
   
    def numTrees(self, n: int) -> int:
        #what is the recurrence relationship? 
        #F(0) = 0
        #F(K) = 1 + sum(F(0)-F(K-1))
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1,n):
            _sum = 0
            for j in range(i+1):
                _sum += dp[j] * dp[i-j]
            dp[i+1] = _sum
        print(dp)
        return dp[n]