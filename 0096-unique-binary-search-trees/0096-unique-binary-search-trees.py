class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1,1] + ([0] * (n-1))
        for i in range(1,n): dp[i+1] = sum(dp[j] * dp[i-j] for j in range(i+1))
        return dp[n]