# @param {Integer[][]} grid1
# @param {Integer[][]} grid2
# @return {Integer}
def count_sub_islands(grid1, grid2)
    m = grid1.size
    n = grid1[0].size
    c = 0
    (0..m-1).each do |i|
        (0..n-1).each do |j|
            if grid2[i][j] == 1 && dfs(grid1, grid2, i, j, m, n)
                c += 1
            end
        end
    end
    c
end

def dfs(grid1, grid2, i, j, m, n)
    return true if i < 0 || j < 0 || i >= m || j >= n || grid2[i][j] == 0
    
    result = true
    # set result false if grid1 is water and grid2 is land
    result = false if grid1[i][j] == 0
    
    grid2[i][j] = 0
    up = dfs(grid1, grid2, i-1, j, m, n)
    down = dfs(grid1, grid2, i+1, j, m, n)
    left = dfs(grid1, grid2, i, j-1, m, n)
    right = dfs(grid1, grid2, i, j+1, m, n)
    
    # if any one of them is false, return false 
    left && right && up && down && result
end