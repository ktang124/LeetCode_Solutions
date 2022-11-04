class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        canTravel = set()
        start = None
        end = None
        for row, lst in enumerate(grid):
            for col, num in enumerate(lst):
                if num == 1:
                    start = (row,col)
                if num == 2:
                    end = (row,col)
                if num == 0:
                    canTravel.add((row,col))
                    
        def dfs(row,col,canTravel):
            if len(canTravel) == 0:
                for rr,cc in dirs:
                    r= row+rr
                    c=col+cc
                    if (r,c) == end:
                        return 1
            total = 0
            for rr,cc in dirs:
                r= row+rr
                c=col+cc
                tup = (r,c)
                if tup in canTravel:
                    canTravel.remove(tup)
                    total += dfs(r,c,canTravel)
                    canTravel.add(tup)
            return total
        return dfs(start[0],start[1],canTravel)