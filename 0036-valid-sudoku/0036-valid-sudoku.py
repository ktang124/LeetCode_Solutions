class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        units = defaultdict(set)
        for row, line in enumerate(board):
            for col, num in enumerate(line):
                if num != '.':
                    unit = (row//3)*3 + col//3
                    n = int(num)-1
                    
                    if (n in rows[row] or n in cols[col] or n in units[unit]):
                        return False
                    rows[row].add(n)
                    cols[col].add(n)
                    units[unit].add(n)
                
        return True