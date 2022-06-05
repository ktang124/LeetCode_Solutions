class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for i in range(n)]
        self.oneRowMap = defaultdict(lambda:0)
        self.oneColMap = defaultdict(lambda:0)
        self.oneDiagMap = defaultdict(lambda:0)
        self.n  = n
        self.twoDiagMap = defaultdict(lambda:0)
        self.twoRowMap = defaultdict(lambda:0)
        self.twoColMap = defaultdict(lambda:0)
       
    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.oneRowMap[row] += 1
            self.oneColMap[col] += 1
            if self.oneRowMap[row] == self.n or self.oneColMap[col] == self.n:
                return 1
            
            if row == col:
                self.oneDiagMap[0] += 1
                
            if self.n - row-1 == col:
                self.oneDiagMap[1] += 1
                
            if self.oneDiagMap[0] == self.n or self.oneDiagMap[1] == self.n:
                return 1
           
            return 0
        else:
            self.twoRowMap[row] += 1
            self.twoColMap[col] += 1
            if self.twoRowMap[row] == self.n or self.twoColMap[col] == self.n:
                return 2
            
            if row == col:
                self.twoDiagMap[0] += 1
                
            if self.n - row-1 == col:
                self.twoDiagMap[1] += 1
                
            if self.twoDiagMap[0] == self.n or self.twoDiagMap[1] == self.n:
                return 2
            
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)