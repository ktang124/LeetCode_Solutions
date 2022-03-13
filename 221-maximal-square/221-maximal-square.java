class Solution {
    public int maximalSquare(char[][] matrix) {
        int max = 0;
        int[][] dp = new int[matrix.length][matrix[0].length];
        for(int row = 0; row < matrix.length; row++){
            for(int col = 0; col < matrix[0].length; col++){
                if(matrix[row][col] == '1'){
                    max = Math.max(max, findSquare(matrix, dp, row, col));
                }
            }
        }
        return max*max;
    }
    
    private int findSquare(char[][] matrix, int[][] dp, int row, int col){
        if(row < 0 || col < 0 || row>= matrix.length || col >= matrix[0].length || matrix[row][col] == '0'){
            return 0;
        }
        if(dp[row][col] != 0){
            return dp[row][col];
        }
        int right = 1+ findSquare(matrix, dp, row, col+1);
        int bottom = 1+ findSquare(matrix, dp, row+1, col);
        int rightDiag = 1+ findSquare(matrix, dp, row+1, col+1);
        
        int m = Math.min(right,bottom);
        dp[row][col] = Math.min(m, rightDiag);
        return dp[row][col];
        
    }
}