class Solution {
    public boolean exist(char[][] board, String word) {
        for(int row = 0; row < board.length; row++){
            for(int col = 0; col < board[0].length; col++){
                if(board[row][col] == word.charAt(0)){
                    boolean[][] visited = new boolean[board.length][board[0].length];
                    if(search(board, row, col, word, visited, 0) || word.length() == 1) return true;
                }
            }
        }
        return false;
    }
    
    private boolean search(char[][] board, int row, int col, String word, boolean[][] visited, int index){
        if(index == word.length()) return true;
        if(visited[row][col]) return false;
        if(board[row][col] != word.charAt(index)) return false;
        
        visited[row][col] = true;
        boolean left = (col > 0 && search(board,row,col-1,word,visited,index+1));
        boolean top = (row > 0 && search(board,row-1, col, word,visited, index+1));
         boolean right = (col < board[0].length-1 && search(board,row, col+1, word,visited, index+1));
         boolean bot = (row < board.length-1 && search(board,row+1, col, word,visited, index+1));
        visited[row][col] = false;
        return left || top || right || bot;
        
    }
}