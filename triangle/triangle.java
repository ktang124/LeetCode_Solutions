class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int[][] dp = new int[triangle.size()][triangle.size()];
        /*initialize dp triangle, more like a square*/
        //fill everything with max
        for(int[] d : dp){
            Arrays.fill(d, Integer.MAX_VALUE-5);
        }
        
        
        dp[0][0] = triangle.get(0).get(0);
        //base case is that the min path from the top always contains the top element
        
        for(int row = 1; row < dp.length; row++){
            for(int col = 0; col <= row; col++){
                int min = Integer.MAX_VALUE;// try to get the lowest tabulated value;
                if(col != 0){
                    min = Math.min(dp[row-1][col-1],min);
                }
                min = Math.min(dp[row-1][col],min);
                dp[row][col] = triangle.get(row).get(col) + min;
            }
        }
        int res = Integer.MAX_VALUE;
        for(int i = 0; i < triangle.size();i++){
            res = Math.min(dp[triangle.size()-1][i], res);
        }
        return res;
    }
    
}