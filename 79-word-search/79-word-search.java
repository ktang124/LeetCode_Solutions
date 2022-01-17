class Solution {
   private static final int[][] DIRS = new int[][] {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    
    public boolean exist(char[][] board, String word) {
        if (board.length == 0 || board[0].length == 0 || word.length() == 0)
            return false;
        
        if (!charsExist(board, word) || !charNeighborsExist(board, word)) return false;
        
        char firstChar = word.charAt(0);
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == firstChar &&
                   wordExists(board, word, 0, i, j))
                    return true;
            }
        }
        
        return false;
    }
    
    private boolean charsExist(char[][] board, String word) {
        int[] chars = new int[255];
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                chars[board[i][j]]++;
            }
        }
        
        for (char c : word.toCharArray()) {
            if (--chars[c] < 0) return false;
        }
        
        return true;
    }
    
    private boolean charNeighborsExist(char[][] board, String word) {
        boolean[][] neighborMap = new boolean[128][128];
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (i > 0) {
                    //setNeighbor(neighborMap, board[i - 1][j], board[i][j]);
                    char c1 = board[i - 1][j], c2 = board[i][j];
                    neighborMap[c1][c2] = true;
                    neighborMap[c2][c1] = true;
                }
                if (j > 0) {
                    //setNeighbor(neighborMap, board[i][j - 1], board[i][j]);
                    char c1 = board[i][j - 1], c2 = board[i][j];
                    neighborMap[c1][c2] = true;
                    neighborMap[c2][c1] = true;
                }
            }
        }
        
        for (int i = 1; i < word.length(); i++) {
            if (!neighborMap[word.charAt(i - 1)][word.charAt(i)])
                return false;
        }
        
        return true;
    }
    
    private void setNeighbor(boolean[][] neighborMap, char c1, char c2) {
        neighborMap[c1][c2] = true;
        neighborMap[c2][c1] = true;
    }
    
    private boolean wordExists(char[][] board, String word, int index, int x, int y) {
        if (index == word.length()) return true;
        if (x < 0 || x >= board.length || y < 0 || y >= board[0].length) return false;
        if (board[x][y] != word.charAt(index)) return false;
        
        board[x][y] -= 26;
        for (int[] dir : DIRS) {
            if (wordExists(board, word, index + 1, x + dir[0], y + dir[1])) {
                return true;
            }
        }
        board[x][y] += 26;
        
        return false;
    }
}