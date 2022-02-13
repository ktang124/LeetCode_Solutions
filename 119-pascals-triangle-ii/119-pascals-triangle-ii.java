class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<>();
        int[][] triangle = new int[rowIndex+1][rowIndex+1];
        triangle[0][0]= 1;
        for(int row = 1; row < triangle.length; row++){
            triangle[row][0] = 1;
            triangle[row][row] = 1;
            for(int col = 1; col < row; col++){
                triangle[row][col] = triangle[row-1][col] + triangle[row-1][col-1];
            }
        }
        for(int num : triangle[rowIndex]){
            res.add(num);
        }
        return res;
    }
}