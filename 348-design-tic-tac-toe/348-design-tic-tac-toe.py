class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for i in range(n)]
        self.oneRowMap = defaultdict(lambda:0)
        self.oneColMap = defaultdict(lambda:0)
        self.n  = n
        self.twoRowMap = defaultdict(lambda:0)
        self.twoColMap = defaultdict(lambda:0)
       
    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.oneRowMap[row] += 1
            self.oneColMap[col] += 1
            if self.oneRowMap[row] == self.n or self.oneColMap[col] == self.n:
                return 1
            
            #check diag
            countOne = 0
            countTwo = 0
            self.board[row][col] = 1
            for i in range(0, self.n):
                if self.board[i][i] == 1:
                    countOne += 1
                if self.board[self.n-i-1][i] == 1:
                    countTwo += 1
            if countOne == self.n or countTwo == self.n:
                return 1
           
            return 0
        else:
            self.twoRowMap[row] += 1
            self.twoColMap[col] += 1
            if self.twoRowMap[row] == self.n or self.twoColMap[col] == self.n:
                return 2
            
            countOne = 0
            countTwo = 0
            self.board[row][col] = 2
            for i in range(0, self.n):
                if self.board[i][i] == 2:
                    countOne += 1
                if self.board[self.n-i-1][i] == 2:
                    countTwo += 1
            if countOne == self.n or countTwo == self.n:
                return 2
            
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)