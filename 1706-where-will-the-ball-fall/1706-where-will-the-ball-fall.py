class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        
        res = [-1] * cols
        dp = [[-2]* cols for i in range(rows)]
        def drop(rowNum, colNum, dp, grid):
            if rowNum == len(dp):
                return colNum
            if dp[rowNum][colNum] != -2:
                return dp[rowNum][colNum]
            if grid[rowNum][colNum] == -1:
                if colNum-1 < 0 or grid[rowNum][colNum-1] == 1:
                    dp[rowNum][colNum] = -1
                    return -1
                left = drop(rowNum+1, colNum-1,dp,grid)
                dp[rowNum][colNum] = left
                return left
            else:
                if colNum+1 >= len(grid[0]) or grid[rowNum][colNum+1] == -1:
                    dp[rowNum][colNum] = -1
                    return -1
                right = drop(rowNum+1, colNum+1, dp,grid)
                dp[rowNum][colNum]= right
                return right
        for col in range(cols):
            res[col] = drop(0,col,dp, grid)
        return res
                