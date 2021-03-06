class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for i in range(n+1)]
        for row in range(1, len(dp)):
            for col in range(n):
                topLeft = dp[row-1][max(col-1,0)] #max(col-1, 0) ensures that if col does not go out of bounds into index -1
                topRight = dp[row-1][min(col+1, n-1)] #min(col+1, n-1) ensures that col does not go out of bounds into index n
                dp[row][col] = min(topLeft,dp[row-1][col],topRight) + matrix[row-1][col]
                
        return min(dp[-1])