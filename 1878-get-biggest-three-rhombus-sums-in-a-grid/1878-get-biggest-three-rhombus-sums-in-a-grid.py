class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        heap = []
        m = len(grid)
        n = len(grid[0])
        def modifyHeap(heap, num):
            if num not in heap:
                if len(heap) < 3:
                    heappush(heap,num)
                elif heap[0] < num:
                #if the current smallest is less than num, replace it with the bigger num
                    heapreplace(heap, num)
                
        def explore(grid, m, n, row, col, heap, dist):
            up = row - dist
            down = row + dist
            left = col - dist
            right = col+dist
            if up < 0 or down >= m or left < 0 or right >= n:
                return
            
            rhombusSum = grid[up][col]+grid[down][col] + grid[row][right]+grid[row][left]
            u, d, r, l = up + 1, down-1, col+1, col-1
            while u < row:
                rhombusSum += grid[u][r] + grid[u][l] + grid[d][r] + grid[d][l]
                u += 1
                r += 1
                l -= 1
                d -= 1
            modifyHeap(heap, rhombusSum)
            explore(grid,m,n, row, col, heap, dist+1)
        for row in range(m):
            for col in range(n):
                modifyHeap(heap, grid[row][col])
                explore(grid, m, n, row, col, heap, 1)
                
        heap = sorted(heap, reverse = True)
        return heap
    
    
        