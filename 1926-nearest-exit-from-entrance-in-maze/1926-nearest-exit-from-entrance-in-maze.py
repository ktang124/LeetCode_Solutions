class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        visited = [[False] * cols for _ in range(rows)] 
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        queue = deque()
        queue.append(entrance)
        level = 0
        visited[entrance[0]][entrance[1]] = True
        while queue:
            size = len(queue)
            level += 1
            while size:
                size -= 1
                row, col = queue.popleft()
                
                for r,c in dirs:
                    nR = r+row
                    nC = c+col
                    if (nR >= 0 and nC >= 0 and nR < rows and nC < cols) and not visited[nR][nC] and maze[nR][nC] == '.':
                        if (nR == 0 or nC == 0 or nR == rows-1 or nC == cols-1) and maze[nR][nC] == '.':
                            return level
                        queue.append([nR,nC])
                        visited[nR][nC] = True
            
        return -1
            
        """def dfs(row, col):
            if row < 0 or col < 0 or col >= cols or row >= rows or maze[row][col] == '+':
                return float('inf')
            if (row == 0 or col == 0 or row == rows-1 or col == cols-1) and maze[row][col] == '.':
                return 0
            if dp[row][col] != 0:
                return dp[row][col]
            dp[row][col] = 1+ min(dfs(row+r,col+c) for r,c in dirs)
            return dp[row][col]
        res = dfs(entrance[0],entrance[1])
        """
        
       