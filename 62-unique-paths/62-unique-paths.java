class Solution {
    public int uniquePaths(int m, int n) {  
        int[][] dp = new int[m+1][n+1];
        dp[1][1] = 1;
        
        return dfs(dp, m, n);   
    }
    
    private int dfs(int[][] dp, int row, int col){
        if(row == 0 || col == 0){
            return 0;
        }
        if(dp[row][col] != 0){
            return dp[row][col];
        }else{
            int waysThere =  dfs(dp,row-1, col) + dfs(dp, row, col-1);
            dp[row][col] = waysThere;
            return dp[row][col];
        }
    }
}