class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        newBox = [['.'] * n for i in range(m)]
        res = [['.'] * m for i in range(n)]
        point = n-1
        for row, lst in enumerate(box):
            point = n-1
            for col in reversed(range(n)):
                char = box[row][col]
                if char == '#':
                    newBox[row][point] = '#'
                    point -= 1
                elif char == '*':
                    newBox[row][col] = '*'
                    point = col-1
                    
        #rotate the box
        #0,0 0,1 0,2 0,3 goes to 0,1 1,1 2,1 3,1
        for row in range(m):
            for col in range(n):
                res[col][m-row-1] = newBox[row][col]
                
        return res