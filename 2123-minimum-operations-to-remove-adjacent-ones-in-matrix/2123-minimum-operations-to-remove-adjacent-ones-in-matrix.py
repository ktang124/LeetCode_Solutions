class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m,n, matched = len(grid),len(grid[0]),{}
        def dfs(i,j,visited):
            for i2,j2 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=i2<m and 0<=j2<n and grid[i2][j2]==1 and (i2,j2) not in visited:
                    visited.add((i2,j2))
                    if (i2,j2) not in matched or dfs(*matched[(i2,j2)],visited):
                        matched[(i2,j2)] = (i,j)
                        return True
            return False
        return sum(i%2==j%2 and dfs(i,j,set()) for i in range(m) for j in range(n) if grid[i][j]==1)