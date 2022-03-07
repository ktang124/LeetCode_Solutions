# @param {Integer[][]} grid
# @return {Integer}
def num_enclaves(grid)
    enclaves = 0 
    for row in 0..grid.length-1
        for col in 0..grid[0].length-1
            if grid[row][col] == 1 then
                num = dfs(grid,row, col)
                if (num > 0) then
                    enclaves+= num
                end
                    
            end
        end
    end
        
    enclaves
end
    
def dfs(grid,row,col)
    if row < 0 || col < 0 || row >= grid.length || col >= grid[0].length then
        return -1
    end
    if grid[row][col] == 0 then 
        return 0
    end
        
    grid[row][col] = 0
    up = dfs(grid, row-1, col)
    left = dfs(grid, row, col-1)
    bottom = dfs(grid, row+1, col)
    right = dfs(grid, row, col+1)
    
    if up == -1 || left == -1 || bottom == -1 || right == -1 then 
        return -1
    end
    res = 1+ up+ left+ bottom + right
    res
 end
        