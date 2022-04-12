class Solution {
    public void gameOfLife(int[][] board) {
        int[][] dirs = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        for(int row = 0; row < board.length; row++){
            for(int col = 0; col < board[0].length; col++){
                int neighbors = 0;
                for(int[] dir : dirs){
                    
                    int r = dir[0] + row;
                    int c = dir[1] + col;
                    if(r >= 0 && c >= 0 && r < board.length && c < board[0].length){
                        if(board[r][c] == 1 || board[r][c] ==4 ){
                             neighbors++;
                        }
                    }
                }
                if(board[row][col] == 1){
                    if(neighbors < 2 || neighbors > 3){
                        //will die
                        board[row][col] = 4;
                    }
                }else{
                    if(neighbors == 3){
                        board[row][col] = -1;
                    }
                }
            }
        }
        
       for(int row = 0; row < board.length; row++){
           for(int col = 0; col < board[0].length; col++){
                if(board[row][col]== 4) board[row][col] = 0;
               if(board[row][col]== -1) board[row][col] = 1;
           }
       }
    }
}