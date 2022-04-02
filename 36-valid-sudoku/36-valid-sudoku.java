class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rowMap = new boolean[9][9];
        boolean[][] colMap = new boolean[9][9];
        boolean[][] quadMap = new boolean[9][9];
        
        for(int row = 0; row < board.length; row++){
            for(int col = 0; col < board.length; col++){
                if(board[row][col] != '.'){
                    int cur = Character.getNumericValue(board[row][col]) - 1;
                    int quad = ((row/3)*3) + (col/3);
                    if(rowMap[row][cur] || colMap[col][cur] || quadMap[quad][cur]){
                        return false;
                    }
                    rowMap[row][cur] = true;
                    colMap[col][cur] = true;
                    quadMap[quad][cur] = true;
                }
            }
        }
        return true;
    }
    
}