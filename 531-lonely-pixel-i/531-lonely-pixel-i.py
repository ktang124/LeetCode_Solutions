class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        bRows = [0] * m
        bCols = [0] * n
        for row in range(m):
            for col in range(n):
                if picture[row][col] == 'B':
                    bRows[row] += 1
                    bCols[col] += 1
                    
        total = 0
        for row in range(m):
            for col in range(n):
                if picture[row][col] == 'B' and bRows[row] == 1 and bCols[col] == 1:
                    total += 1
                    
                    
        return total
                