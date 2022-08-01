class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    up = dp[row-1][col]
                    left = dp[row][col-1]
                    dp[row][col] = up + left
                    
        return dp[m-1][n-1]