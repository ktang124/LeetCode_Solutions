class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        res = 0
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        for row, lst in enumerate(grid):
            for col, num in enumerate(lst):
                if num == '1':
                    res += 1
                    stack.append((row,col))
                    while stack:
                         #start dfs 

                        r,c = stack.pop()
                        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c]== '1':
                            grid[r][c] = '0'
                            for d in dirs:
                                coord = (r+d[0],c+d[1])
                                stack.append(coord)
                                
        return res
                                
                   