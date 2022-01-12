class Solution {
    public int findCircleNum(int[][] isConnected) {
        //you are given an adjacency matrix
        int num = 0;
        for(int row = 0; row < isConnected.length; row++){
            boolean oneExists = false;
            for(int col = 0; col < isConnected[0].length; col++){
                if(isConnected[row][col] == 1){
                    oneExists = true;
                    dfs(isConnected, row);
                }
            }
            if(oneExists) num++;
        }
        
        return num;
    }
    
    private void dfs(int[][] grid, int row){
        
        for(int col = 0; col < grid[0].length; col++){
            if(grid[row][col] == 1){
                grid[row][col] = 0;
                dfs(grid, col);
            }
        }
        
    }
}